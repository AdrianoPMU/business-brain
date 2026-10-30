"""Trim each talking clip to its speech (small breath before and after) and join them into one take.

  python3 -I stitch.py OUT.mp4 clip1.mp4[:max_end] clip2.mp4 ...
"""
import subprocess, sys, numpy as np

out, specs = sys.argv[1], sys.argv[2:]

def speech_bounds(path, max_end=None):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True).stdout
    a = np.frombuffer(raw, np.float32)
    win = 800  # 50 ms
    db = np.array([20 * np.log10(np.sqrt((a[i:i + win] ** 2).mean()) + 1e-9) for i in range(0, len(a) - win, win)])
    loud = np.where(db > -33)[0]
    start, end = loud[0] * 0.05, (loud[-1] + 1) * 0.05
    if max_end is not None:
        end = min(end, max_end)
    return max(0.0, start - 0.12), min(len(a) / 16000, end + 0.3)

parts = []
for k, spec in enumerate(specs):
    path, _, cap = spec.partition(':')
    s, e = speech_bounds(path, float(cap) if cap else None)
    seg = f'{out}._seg{k}.mp4'
    d = e - s
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{s:.3f}', '-i', path, '-t', f'{d:.3f}',
                    '-vf', 'fps=24,scale=720:1280,format=yuv420p',
                    '-af', f'aresample=48000,afade=t=in:d=0.03,afade=t=out:st={max(0, d - 0.04):.3f}:d=0.04',
                    '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-c:a', 'aac', '-b:a', '192k', seg], check=True)
    parts.append(seg)
    print(f'{path}: {s:.2f}-{e:.2f} ({d:.2f}s)')

lst = out + '.txt'
open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c:v', 'libx264', '-preset', 'veryfast',
                '-crf', '16', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', out], check=True)
print('total', subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', out],
                              capture_output=True, text=True).stdout.strip())
