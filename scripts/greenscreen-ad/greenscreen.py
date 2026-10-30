"""Green-screen composite: presenter cut out of her room, small in the bottom-right corner,
over the results reel, with the headline pills on top. Keeps her voice.

  python3 -I greenscreen.py head.mp4 bg_loop.mp4 cap.png model.tflite out.mp4 [scale]

Fixes for AI-generation drift: her skin colour is locked to the first second, and small bright
specks on her clothes are cleaned frame by frame.
"""
import sys, subprocess
import numpy as np, cv2, mediapipe as mp
from mediapipe.tasks.python import vision, BaseOptions

head_p, bg_p, cap_p, model_p, out_p = sys.argv[1:6]
SC = float(sys.argv[6]) if len(sys.argv) > 6 else 0.37
W, H = 1080, 1920
pw, ph = int(W * SC), int(H * SC)
px, py = W - pw - 24, H - ph

seg = vision.ImageSegmenter.create_from_options(vision.ImageSegmenterOptions(
    base_options=BaseOptions(model_asset_path=model_p), running_mode=vision.RunningMode.VIDEO,
    output_confidence_masks=True))
head = cv2.VideoCapture(head_p)
fps = head.get(cv2.CAP_PROP_FPS) or 30
bg = cv2.VideoCapture(bg_p)
cap = cv2.imread(cap_p, cv2.IMREAD_UNCHANGED)
ca = cap[..., 3:4].astype(np.float32) / 255.0
cc = cap[..., :3].astype(np.float32)

enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', f'{fps}', '-i', '-',
                        '-i', head_p, '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20',
                        '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', out_p],
                       stdin=subprocess.PIPE)

k5 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
prev = None; refs = []; ref = None; smooth = None; i = 0
while True:
    ok, f = head.read()
    if not ok:
        break
    okb, b = bg.read()
    if not okb:
        bg.set(cv2.CAP_PROP_POS_FRAMES, 0); _, b = bg.read()
    hh, ww = f.shape[:2]
    r = seg.segment_for_video(mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(f, cv2.COLOR_BGR2RGB)), int(i * 1000 / fps))
    m = [cv2.resize(c.numpy_view(), (ww, hh)) for c in r.confidence_masks]
    # masks: 0 background, 1 hair, 2 body skin, 3 face skin, 4 clothes, 5 other

    clothes = cv2.GaussianBlur(cv2.erode((m[4] > 0.6).astype(np.float32), k5), (0, 0), 2)[..., None]
    opened = cv2.medianBlur(cv2.morphologyEx(f, cv2.MORPH_OPEN, k5), 5)
    f = (f * (1 - clothes) + np.minimum(f, opened) * clothes).astype(np.uint8)

    skin = (m[3] > 0.7) | (m[2] > 0.7)
    if skin.sum() > 500:
        lab = cv2.cvtColor(f, cv2.COLOR_BGR2LAB).astype(np.float32)
        px_ = lab[skin]
        st = np.concatenate([px_.mean(0), px_.std(0)])
        if i < int(fps):
            refs.append(st)
        elif ref is None:
            ref = np.mean(refs, 0)
        if ref is not None:
            smooth = st if smooth is None else 0.9 * smooth + 0.1 * st
            body = cv2.GaussianBlur(((m[3] > 0.3) | (m[2] > 0.3)).astype(np.float32), (0, 0), 6)[..., None]
            mu, sd = smooth[:3], np.maximum(smooth[3:], 1)
            adj = (lab - mu) * (ref[3:] / sd) + ref[:3]
            lab = lab * (1 - body) + adj * body
            f = cv2.cvtColor(np.clip(lab, 0, 255).astype(np.uint8), cv2.COLOR_LAB2BGR)

    a = np.clip(1 - m[0], 0, 1).astype(np.float32)
    prev = a if prev is None else 0.6 * a + 0.4 * prev
    a = np.clip((prev - 0.3) / 0.45, 0, 1)
    a = cv2.GaussianBlur(a, (0, 0), 1.2)

    fs = cv2.resize(f, (pw, ph), interpolation=cv2.INTER_AREA).astype(np.float32)
    as_ = cv2.resize(a, (pw, ph), interpolation=cv2.INTER_AREA)[..., None]
    out = b.astype(np.float32)
    sh = cv2.GaussianBlur(as_[..., 0], (0, 0), 14)[..., None] * 0.35
    sx, sy = px - 10, py + 6
    reg = out[sy:sy + ph, sx:sx + pw]
    out[sy:sy + ph, sx:sx + pw] = reg * (1 - sh[:reg.shape[0], :reg.shape[1]])
    reg = out[py:py + ph, px:px + pw]
    out[py:py + ph, px:px + pw] = reg * (1 - as_) + fs * as_
    out = out * (1 - ca) + cc * ca
    enc.stdin.write(np.clip(out, 0, 255).astype(np.uint8).tobytes())
    i += 1
enc.stdin.close(); enc.wait()
print('frames', i, 'fps', fps)
