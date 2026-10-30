"""Compare each clip's transcript with its script line. python3 check.py N1 N2 ... (default all 1-42)"""
import json, re, sys, unicodedata
lines = {int(k): v for k, v in json.load(open('lines.json')).items()}
NUM = {'3': 'tres', '29': 'veintinueve', '28': 'veintiocho', '5': 'cinco', '199': 'ciento noventa y nueve', '10': 'diez', '15': 'quince',
       '30': 'treinta', '500': 'quinientos', '297': 'doscientos noventa y siete', '400': 'cuatrocientos', '11': 'once', '9': 'nueve', '2': 'dos'}
def norm(t):
    t = t.lower().replace('$', ' ').replace('%', ' por ciento ')
    t = re.sub(r'\d+', lambda m: ' ' + NUM.get(m.group(0), m.group(0)) + ' ', t)
    t = unicodedata.normalize('NFD', t); t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z ]+', ' ', t).split()
ns = [int(x) for x in sys.argv[1:]] or range(1, 43)
bad = []
for n in ns:
    try: words = json.load(open(f'clips/clip-{n}.mp4.words.json'))
    except FileNotFoundError: print(n, 'MISSING'); bad.append(n); continue
    got = norm(' '.join(w for w, _, _ in words)); want = norm(lines[n])
    ok = got == want
    if not ok: bad.append(n)
    print(f"{n:>2} {'OK ' if ok else 'BAD'} {'' if ok else '| want: ' + ' '.join(want) + ' | got: ' + ' '.join(got)}")
print('BAD:', ' '.join(map(str, bad)))
