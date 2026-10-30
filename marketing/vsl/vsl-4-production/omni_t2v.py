"""Text-to-video presenter candidates with Gemini Omni 1.1 Flash.
  GEMINI_KEY_FILE=... python3 -I omni_t2v.py OUT_DIR name1 "prompt1" name2 "prompt2" ...
Never prints the key."""
import json, os, sys, time, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
KEY = [l.strip() for l in Path(os.environ['GEMINI_KEY_FILE']).read_text().splitlines() if l.strip()][-1]
API = 'https://generativelanguage.googleapis.com/v1beta'
out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
pairs = list(zip(sys.argv[2::2], sys.argv[3::2]))
def call(method, url, body=None, timeout=900):
    req = urllib.request.Request(url, method=method, headers={'content-type': 'application/json', 'x-goog-api-key': KEY},
                                 data=json.dumps(body).encode() if body is not None else None)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r: return r.read()
    except urllib.error.HTTPError as e:
        raise RuntimeError(f'HTTP {e.code}: {e.read().decode(errors="replace")[:600]}')
def fetch(uri):
    fid = uri.split('/files/')[1].split(':')[0].split('?')[0]
    for _ in range(120):
        meta = json.loads(call('GET', f'{API}/files/{fid}'))
        if meta.get('state') == 'ACTIVE': return call('GET', f'{API}/files/{fid}:download?alt=media')
        if meta.get('state') == 'FAILED': raise RuntimeError('file FAILED')
        time.sleep(4)
    raise RuntimeError('file never became ACTIVE')
def one(pair):
    name, text = pair
    body = {'model': 'gemini-omni-1.1-flash', 'input': [{'type': 'text', 'text': text}],
            'response_format': {'type': 'video', 'aspect_ratio': '9:16', 'resolution': '720p', 'delivery': 'uri'}}
    t0 = time.time()
    try: raw = call('POST', f'{API}/interactions', body)
    except Exception as e: return f'{name}: {str(e)[:300]}'
    (out / f'resp-{name}.json').write_bytes(raw)
    r = json.loads(raw)
    uri = next((c.get('uri') for s in r.get('steps', []) for c in (s.get('content') or []) if c.get('type') == 'video'), None)
    if not uri: return f'{name}: no video ({r.get("status")})'
    (out / f'{name}.mp4').write_bytes(fetch(uri))
    return f'{name}: ok in {time.time() - t0:.0f}s'
with ThreadPoolExecutor(3) as ex:
    for msg in ex.map(one, pairs): print(msg, flush=True)
print('done')
