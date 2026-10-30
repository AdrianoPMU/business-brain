"""Write out/captions.ass from lines.json + durations.json + per-clip word timings."""
import json, re
lines = {int(k): v for k, v in json.load(open('lines.json')).items()}
durs = {int(k): v for k, v in json.load(open('durations.json')).items()}
SHOW = [("tres minutos", "3 minutos"), ("veintinueve de septiembre", "29 de septiembre"), ("veintiocho de octubre", "28 de octubre"),
        ("cinco estudios", "5 estudios"), ("ciento noventa y nueve", "199"), ("unos diez dólares y medio", "unos $10.50"),
        ("unos quince dólares", "unos $15"), ("treinta minutos", "30 minutos"), ("quinientos dólares", "$500"),
        ("doscientos noventa y siete", "$297"), ("unos cuatrocientos dólares", "unos $400"), ("treinta días", "30 días"),
        ("las nueve de la noche", "las 9 de la noche")]
def show(t):
    for a, b in SHOW: t = t.replace(a, b)
    return t
def chunks(text, maxc=30):
    words, out, cur = text.split(), [], []
    for w in words:
        if cur and (len(' '.join(cur + [w])) > maxc or cur[-1][-1] in '.?!:'):
            out.append(cur); cur = []
        cur.append(w)
    if cur: out.append(cur)
    return [' '.join(c) for c in out]
def wrap2(c, maxl=17):
    if len(c) <= maxl: return c
    ws = c.split(); best = None
    for i in range(1, len(ws)):
        a, b = ' '.join(ws[:i]), ' '.join(ws[i:]); sc = max(len(a), len(b))
        if best is None or sc < best[0]: best = (sc, a, b)
    return best[1] + r'\N' + best[2]
def ts(t):
    h, m = int(t // 3600), int(t % 3600 // 60); s = t % 60
    return f'{h}:{m:02d}:{s:05.2f}'
head = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,DM Sans 9pt,46,&H00FFFFFF,&H00FFFFFF,&H00202330,&H80000000,-1,0,0,0,100,100,0,0,1,3.2,1.5,2,0,0,0,1
Style: Lbl,DM Sans 9pt,22,&H00FFFFFF,&H00FFFFFF,&H55283234,&H00000000,-1,0,0,0,100,100,1,0,3,9,0,7,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ev, t0 = [], 0.0
for n in range(1, 43):
    d = durs[n]['dur']; trim = durs[n]['start']
    words = json.load(open(f'clips/clip-{n}.mp4.words.json'))
    sp0 = max(0.0, (words[0][1] - trim)) if words else 0.1
    sp1 = min(d, (words[-1][2] - trim)) if words else d - 0.2
    cs = chunks(show(lines[n])); total = sum(len(c) for c in cs); acc = 0
    for c in cs:
        a = t0 + sp0 + (sp1 - sp0) * acc / total; acc += len(c)
        b = t0 + sp0 + (sp1 - sp0) * acc / total
        ev.append(f"Dialogue: 1,{ts(a)},{ts(b + 0.06)},Cap,,0,0,0,,{{\\an2\\pos(1560,972)}}{wrap2(c)}")
    t0 += d
ev.append(f"Dialogue: 0,{ts(0)},{ts(t0)},Lbl,,0,0,0,,{{\\an7\\pos(1322,92)}}✦ Presentadora creada con IA")
open('out/captions.ass', 'w').write(head + '\n'.join(ev) + '\n')
print('events', len(ev), 'total', round(t0, 2))
