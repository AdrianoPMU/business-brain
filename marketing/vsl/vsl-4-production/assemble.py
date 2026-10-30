"""Trim each clip to its speech and join them. Writes presenter.mp4 and durations.json.  python3 assemble.py [N:max_end ...]"""
import json, os, subprocess, sys, numpy as np
LAST = int(os.environ.get("LAST", 42))
caps = dict(a.split(':') for a in sys.argv[1:])
def speech_bounds(path, max_end=None):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True).stdout
    a = np.frombuffer(raw, np.float32); win = 800
    db = np.array([20 * np.log10(np.sqrt((a[i:i + win] ** 2).mean()) + 1e-9) for i in range(0, len(a) - win, win)])
    loud = np.where(db > -33)[0]
    start, end = loud[0] * 0.05, (loud[-1] + 1) * 0.05
    if max_end is not None: end = min(end, max_end)
    return max(0.0, start - 0.12), min(len(a) / 16000, end + 0.3)
parts, durs = [], {}
for n in range(1, LAST + 1):
    path = f'clips/clip-{n}.mp4'
    s, e = speech_bounds(path, float(caps[str(n)]) if str(n) in caps else None)
    d = round(round((e - s) * 24) / 24, 4)  # whole frames
    seg = f'clips/seg-{n}.mp4'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{s:.3f}', '-i', path, '-t', f'{d:.4f}', '-vf', 'fps=24,scale=720:1280,format=yuv420p',
                    '-af', f'aresample=48000,afade=t=in:d=0.03,afade=t=out:st={max(0, d - 0.05):.3f}:d=0.05',
                    '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-c:a', 'aac', '-b:a', '192k', seg], check=True)
    parts.append(seg); durs[n] = {'start': s, 'dur': d}
    print(n, f'{s:.2f}+{d:.2f}', flush=True)
open('clips/list.txt', 'w').write(''.join(f"file '{p.split('/')[-1]}'\n" for p in parts))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', 'clips/list.txt', '-c:v', 'libx264', '-preset', 'veryfast',
                '-crf', '16', '-c:a', 'aac', '-b:a', '192k', 'out/presenter.mp4'], check=True)
json.dump(durs, open('durations.json', 'w'), indent=0)
print('total', round(sum(v['dur'] for v in durs.values()), 2))
