"""One talking clip per script line with Gemini Omni 1.1 Flash, each starting from the same presenter frame
(image-to-video), so the cuts between lines look like a normal phone video with jump cuts.

  GEMINI_KEY_FILE=... python3 -I omni_i2v.py ref.jpg LANG OUT_DIR N1 "line one" N2 "line two" ...

Writes OUT_DIR/clip-N.mp4 and resp-N.json. Runs up to 3 at a time. Never prints the key.
"""
import base64, json, os, sys, time, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

KEY = Path(os.environ['GEMINI_KEY_FILE']).read_text().strip()
API = 'https://generativelanguage.googleapis.com/v1beta'
ref, lang, out = sys.argv[1], sys.argv[2], Path(sys.argv[3])
out.mkdir(parents=True, exist_ok=True)
pairs = list(zip(sys.argv[4::2], sys.argv[5::2]))
img = base64.b64encode(Path(ref).read_bytes()).decode()

def call(method, url, body=None, timeout=900):
    req = urllib.request.Request(url, method=method, headers={'content-type': 'application/json', 'x-goog-api-key': KEY},
                                 data=json.dumps(body).encode() if body is not None else None)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        raise RuntimeError(f'HTTP {e.code}: {e.read().decode(errors="replace")[:600]}')

def fetch(uri):
    fid = uri.split('/files/')[1].split(':')[0].split('?')[0]
    for _ in range(120):
        meta = json.loads(call('GET', f'{API}/files/{fid}'))
        if meta.get('state') == 'ACTIVE':
            return call('GET', f'{API}/files/{fid}:download?alt=media')
        if meta.get('state') == 'FAILED':
            raise RuntimeError('file FAILED')
        time.sleep(4)
    raise RuntimeError('file never became ACTIVE')

def one(pair):
    n, line = pair
    text = ("The woman in this photo, in the same room, same outfit and same light, keeps filming herself selfie-style on her phone, "
            "like a real organic Instagram video. One continuous take, no cuts, no music, no captions or on-screen text. "
            f"She talks straight to the camera in natural {lang}, warm and relaxed, and says exactly this line once, word for word, "
            f"and nothing else: \"{line}\" Then she smiles and stops talking.")
    body = {'model': 'gemini-omni-1.1-flash',
            'input': [{'type': 'image', 'data': img, 'mime_type': 'image/jpeg'}, {'type': 'text', 'text': text}],
            'response_format': {'type': 'video', 'aspect_ratio': '9:16', 'resolution': '720p', 'delivery': 'uri'}}
    t0 = time.time()
    for attempt in (1, 2):
        try:
            raw = call('POST', f'{API}/interactions', body)
            break
        except (ConnectionError, TimeoutError, urllib.error.URLError) as e:
            if attempt == 2:
                return f'clip {n}: failed twice ({type(e).__name__})'
            time.sleep(5)
        except RuntimeError as e:
            return f'clip {n}: {e}'
    (out / f'resp-{n}.json').write_bytes(raw)
    r = json.loads(raw)
    uri = next((c.get('uri') for s in r.get('steps', []) for c in (s.get('content') or []) if c.get('type') == 'video'), None)
    if not uri:
        return f'clip {n}: no video ({r.get("status")})'
    (out / f'clip-{n}.mp4').write_bytes(fetch(uri))
    return f'clip {n}: ok in {time.time() - t0:.0f}s'

with ThreadPoolExecutor(3) as ex:
    for msg in ex.map(one, pairs):
        print(msg, flush=True)
print('done')
