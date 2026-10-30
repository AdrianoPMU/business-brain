"""Background reel + headline pills for a green-screen voucher ad (same look as Aglahel's and Lexxi's).

  python3 -I make_bg.py OUT_DIR photo1.jpg[:x0,y0,x1,y1] photo2.jpg ...

bg_loop.mp4  1080x1920, 30 fps: each result full width in the upper band on a soft blurred copy,
             slow push-in, quick crossfade every 3.2 s. The presenter sits bottom-right on top later.
cap_en.png / cap_es.png  white headline pills (RGBA, full frame).
"""
import subprocess, sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont

OUT = Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
W, H, FPS = 1080, 1920, 30
SLIDE, FADE = 3.2, 0.35
BOX = (0, 330, W, 1360)

def load(arg):
    path, _, box = arg.partition(':')
    im = Image.open(path).convert('RGB')
    return im.crop(tuple(int(v) for v in box.split(','))) if box else im

def cover(im, w, h, top=0.5):
    s = max(w / im.width, h / im.height)
    r = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = (r.width - w) // 2; y = round((r.height - h) * top)
    return r.crop((x, y, x + w, y + h))

def slide(im):
    bg = cover(im, W, H).filter(ImageFilter.GaussianBlur(40))
    bg = ImageEnhance.Brightness(bg).enhance(0.72)
    bw, bh = BOX[2] - BOX[0], BOX[3] - BOX[1]
    if im.height / im.width >= 1.15:
        fg = cover(im, bw, bh, top=0.3)
    else:
        s = min(bw / im.width, bh / im.height)
        fg = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    bg.paste(fg, (BOX[0] + (bw - fg.width) // 2, BOX[1] + (bh - fg.height) // 2))
    return np.asarray(bg.convert('RGB'))

slides = [slide(load(a)) for a in sys.argv[2:]]
per = int(SLIDE * FPS); fade = int(FADE * FPS); total = per * len(slides)

def zoomed(arr, t):
    z = 1 + 0.06 * t
    im = Image.fromarray(arr)
    cw, ch = round(W / z), round(H / z)
    x, y = (W - cw) // 2, round((H - ch) * 0.4)
    return np.asarray(im.crop((x, y, x + cw, y + ch)).resize((W, H), Image.BILINEAR))

enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                        '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', str(OUT / 'bg_loop.mp4')],
                       stdin=subprocess.PIPE)
for i in range(total):
    k, j = divmod(i, per)
    cur = zoomed(slides[k], j / per)
    if j >= per - fade:
        a = (j - (per - fade) + 1) / fade
        nxt = zoomed(slides[(k + 1) % len(slides)], 0)
        cur = (cur * (1 - a) + nxt * a).astype(np.uint8)
    enc.stdin.write(cur.tobytes())
enc.stdin.close(); enc.wait()

BOLD = '/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf'
EMOJI = '/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf'
F = ImageFont.truetype(BOLD, 56)
EF = ImageFont.truetype(EMOJI, 109)

def run_width(parts):
    return sum(F.getlength(t) if k == 't' else 64 for k, t in parts)

def draw_parts(img, d, x, y, parts):
    for kind, txt in parts:
        if kind == 't':
            d.text((x, y), txt, font=F, fill=(20, 20, 20)); x += F.getlength(txt)
        else:
            e = Image.new('RGBA', (140, 140), (0, 0, 0, 0))
            ImageDraw.Draw(e).text((0, 0), txt, font=EF, embedded_color=True)
            e = e.crop(e.getbbox()).resize((60, 60), Image.LANCZOS)
            img.alpha_composite(e, (int(x + 2), int(y + 6))); x += 64

def caption(lines, path):
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    y = 120; padx, pady, lh = 30, 16, 72
    for parts in lines:
        tw = run_width(parts); x0 = (W - tw) / 2
        d.rounded_rectangle((x0 - padx, y - pady + 2, x0 + tw + padx, y + lh + pady - 8), radius=22, fill=(255, 255, 255, 250))
        draw_parts(img, d, x0, y, parts)
        y += lh + pady * 2 - 12
    img.save(path)

caption([[('t', '15 vouchers for powder brows '), ('e', '👀')], [('t', '$397 (normally $550)')]], OUT / 'cap_en.png')
caption([[('t', 'cejas efecto polvo '), ('e', '👀')], [('t', '15 vouchers a $397 (antes $550)')]], OUT / 'cap_es.png')
print('ok', total / FPS, 's')
