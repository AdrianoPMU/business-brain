"""Generate missing clips one at a time, waiting out 429s.  python3 run_slow.py N1 N2 ..."""
import json, os, subprocess, sys, time
lines = {int(k): v for k, v in json.load(open('lines.json')).items()}
env = dict(os.environ, GEMINI_KEY_FILE=os.environ.get('GEMINI_KEY_FILE', 'secret/gemini-key.txt'))
for n in map(int, sys.argv[1:]):
    for attempt in range(12):
        if os.path.exists(f'clips/clip-{n}.mp4'): break
        r = subprocess.run(['python3', '-I', 'omni_i2v_vsl.py', 'ref-start.jpg', 'Latin American Spanish', 'clips', str(n), lines[n]],
                           env=env, capture_output=True, text=True)
        msg = (r.stdout.strip().splitlines() or ['?'])[0]
        print(time.strftime('%H:%M:%S'), msg[:160], flush=True)
        if ': ok' in msg: time.sleep(16); break
        if 'per day' in msg:  # daily cap (20/day on Tier 1, resets at midnight Pacific): stop instead of retrying
            print('daily limit reached; stopping', flush=True); sys.exit(2)
        time.sleep(75 if '429' in msg else 20)
print('done', flush=True)
