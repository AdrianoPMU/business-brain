"""Background reel where the brows are always on screen and never under the presenter.

  python3 -I make_bg_brows.py OUT.mp4 face_landmarker.task SEG [SEG ...]

SEG forms (times in seconds):
  full:clip.mp4:dur[:start]    full-screen video (or a photo), reframed every frame so the brows sit at (540, 640)
  half:file:top|bottom:dur[:LABEL]
                               one half of a stacked before/after (image or video), full width in the
                               upper part of the screen over a blurred copy, brows near y=640.
                               LABEL (e.g. ANTES / DESPUÉS) adds a small pill; omit it when the source
                               already has its own label. For a video, the half plays from where the
                               previous half of the same file stopped.

The presenter sits bottom-right from y=922 (scale 0.52), so the brow box is kept above y=880.
"""
import subprocess, sys
import numpy as np, cv2, mediapipe as mp
from mediapipe.tasks.python import vision, BaseOptions
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
TX, TY = 540, 640            # where the brow centre goes
SAFE_BOTTOM = 880            # brows must stay above this (presenter starts at ~922)
BROWS = [70, 63, 105, 66, 107, 46, 53, 52, 65, 55, 336, 296, 334, 293, 300, 276, 283, 282, 295, 285]
out_p, model_p = sys.argv[1], sys.argv[2]
segs = sys.argv[3:]

def landmarker():
    return vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(
        base_options=BaseOptions(model_asset_path=model_p), running_mode=vision.RunningMode.IMAGE, num_faces=1))

def brows(lm, img):
    """Brow centre and span; if the face fills the frame (close-up), retry with a grey border around it."""
    h, w = img.shape[:2]
    for py, px in ((0, 0), (h // 2, w // 4)):
        x = img if not py else cv2.copyMakeBorder(img, py, py, px, px, cv2.BORDER_CONSTANT, value=(128, 128, 128))
        r = lm.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=np.ascontiguousarray(cv2.cvtColor(x, cv2.COLOR_BGR2RGB))))
        if r.face_landmarks:
            H2, W2 = x.shape[:2]
            p = np.array([[r.face_landmarks[0][i].x * W2 - px, r.face_landmarks[0][i].y * H2 - py] for i in BROWS])
            return p.mean(0), np.ptp(p, 0)          # centre, (span x, span y)
    return None

def frames_of(path, start, n):
    if path.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
        im = cv2.imread(path)
        return [im] * n
    cap = cv2.VideoCapture(path)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    out = []
    for k in range(n):
        cap.set(cv2.CAP_PROP_POS_MSEC, (start + k / FPS) * 1000) if k == 0 else None
        ok, f = cap.read()
        if not ok:
            f = out[-1] if out else None
        # source fps can differ from 30: resample by skipping/duplicating
        out.append(f)
        extra = fps / FPS - 1
        while extra >= 1:
            cap.read(); extra -= 1
    return [f for f in out if f is not None]

def smooth(vals, a=0.8):
    res, cur = [], None
    for v in vals:
        cur = v if cur is None else a * cur + (1 - a) * v
        res.append(cur)
    return res

BOLD = '/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf'
LF = ImageFont.truetype(BOLD, 44)
def label(img, text, y):
    pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)).convert('RGBA')
    d = ImageDraw.Draw(pil); tw = LF.getlength(text)
    d.rounded_rectangle((40, y, 40 + tw + 44, y + 70), radius=18, fill=(20, 20, 20, 215))
    d.text((62, y + 10), text, font=LF, fill=(255, 255, 255))
    return cv2.cvtColor(np.array(pil.convert('RGB')), cv2.COLOR_RGB2BGR)

enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                        '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-pix_fmt', 'yuv420p', out_p], stdin=subprocess.PIPE)
lm = landmarker()
played = {}       # file -> seconds already used (for halves of one video)
report = []
for seg in segs:
    parts = seg.split(':')
    kind = parts[0]
    if kind == 'full':
        path, dur = parts[1], float(parts[2]); n = int(dur * FPS)
        start = float(parts[3]) if len(parts) > 3 else 0.0
        fr = frames_of(path, start, n)
        det = [brows(lm, f) for f in fr]
        ok = [d for d in det if d]
        if not ok:
            raise SystemExit(f'no face found in {path}')
        c = [d[0] if d else None for d in det]
        for k in range(len(c)):            # fill gaps with the nearest detection
            if c[k] is None:
                c[k] = next(x for x in c[k:] + c[::-1] if x is not None)
        c = smooth(c)
        span = np.median([d[1][0] for d in ok])
        h, w = fr[0].shape[:2]
        s = min(max(W / w, H / h, 620 / max(span, 1)), 3.0)
        bad = 0
        for f, (cx, cy) in zip(fr, c):
            X = np.clip(TX - s * cx, W - s * w, 0); Y = np.clip(TY - s * cy, H - s * h, 0)
            M = np.float32([[s, 0, X], [0, s, Y]])
            o = cv2.warpAffine(f, M, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
            by = s * cy + Y
            bad += by > SAFE_BOTTOM - 60 or not (150 < s * cx + X < 930)
            enc.stdin.write(o.tobytes())
        report.append(f'{seg}: scale {s:.2f}, frames off-target {bad}/{len(fr)}')
    else:
        path, which, dur = parts[1], parts[2], float(parts[3]); lab = parts[4] if len(parts) > 4 else None
        n = int(dur * FPS); start = played.get(path, 0.0)
        fr = frames_of(path, start, n); played[path] = start + dur
        h, w = fr[0].shape[:2]
        half = (lambda f: f[: h // 2]) if which == 'top' else (lambda f: f[h - h // 2:])
        hf = [half(f) for f in fr]
        if lab:   # drop the top strip, where stacked before/afters usually carry their own small label
            cut = int(hf[0].shape[0] * 0.08); hf = [f[cut:] for f in hf]
        det = brows(lm, hf[0]) or brows(lm, hf[len(hf) // 2])
        hh, hw = hf[0].shape[:2]
        s = W / hw
        cy = det[0][1] if det else hh * 0.35
        Y = int(np.clip(TY - s * cy, -(s * hh - 520), 430))
        bad = 0
        for f in hf:
            bg = cv2.resize(f, (W, H), interpolation=cv2.INTER_AREA) if False else None
            cov = max(W / hw, H / hh)
            big = cv2.resize(f, (int(hw * cov) + 1, int(hh * cov) + 1))
            x0 = (big.shape[1] - W) // 2; y0 = (big.shape[0] - H) // 2
            bg = cv2.GaussianBlur(big[y0:y0 + H, x0:x0 + W], (0, 0), 30) * 0.65
            fg = cv2.resize(f, (W, int(hh * s)), interpolation=cv2.INTER_CUBIC)
            o = bg.astype(np.uint8)
            top, bot = max(Y, 0), min(Y + fg.shape[0], H)
            o[top:bot] = fg[top - Y: bot - Y]
            if lab:
                o = label(o, lab, max(Y + 20, 420))
            bad += (s * cy + Y) > SAFE_BOTTOM - 60
            enc.stdin.write(o.tobytes())
        report.append(f'{seg}: band y={Y}, brows at y={int(s * cy + Y)}, off-target {bad}/{len(hf)}')
enc.stdin.close(); enc.wait()
print('\n'.join(report))
