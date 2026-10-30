# VSL 4 production kit

How VSL 4 ("Sistema Agenda Llena", script in `../vsl-4-agenda-llena.md`) is built: an AI presenter on the right, animated app graphics on the left, Spanish captions. 1920x1080, 24 fps.

No clips, key or output live here. The clips are about 56 MB and this repo is public.

## What's in here

| File | What it does |
|---|---|
| `lines.json` | The 42 spoken lines, numbered like the script table |
| `ref-start.jpg` | Neutral frame of presenter B. Every clip starts from it, so the look stays the same |
| `omni_i2v_vsl.py` | Makes one 10-second 9:16 clip per line with Gemini Omni 1.1 Flash (image-to-video from `ref-start.jpg`) |
| `omni_t2v.py` | Text-to-video, used once to pick the presenter |
| `run_slow.py N...` | Makes missing clips one at a time, waits out 429s, stops at the daily cap. Key file path in `GEMINI_KEY_FILE` |
| `transcribe.py MODEL clips...` | faster-whisper word timings → `clip-N.mp4.words.json` (audio decoded with ffmpeg, PyAV breaks) |
| `check.py [N...]` | Compares each clip's words with `lines.json` |
| `repair.py IN OUT FROM TO` | Cuts a repeated word out of a clip |
| `assemble.py [N:max_end]` | Trims each clip to its speech, joins them into `out/presenter.mp4`, writes `durations.json`. `LAST=21` stops early |
| `stage.html` + `render.mjs` | The 42 graphics scenes, rendered frame by frame with puppeteer-core + @sparticuz/chromium |
| `captions.py` | Writes `out/captions.ass` (DM Sans, numbers shown as digits, "✦ Presentadora creada con IA" label) |
| `composite.sh` | Graphics + rounded presenter at 1290,60 + captions + loudnorm → `out/vsl-4.mp4` |

## Run order

1. `GEMINI_KEY_FILE=... python3 run_slow.py 1 2 ... 42` (20 a day on Tier 1)
2. `python3 transcribe.py medium clips/clip-*.mp4`, then `python3 check.py`. Move any bad clip to `bad-N.mp4` and rerun step 1 for it, or fix it with `repair.py`.
3. `python3 assemble.py` (add `N:max_end` for a clip with noise after the line, e.g. `5:4.0`)
4. `node render.mjs out/gfx.mp4 24 "1:d1,2:d2,..."` with the durations from `durations.json` (about 6 minutes for the full video)
5. `python3 captions.py && ./composite.sh`
6. Transcribe `out/vsl-4.mp4` and read it against the script before anyone sees it.

Needs: ffmpeg, Python with numpy + faster-whisper, Node with `puppeteer-core`, `@sparticuz/chromium`, `@fontsource/dm-sans`, `@fontsource/cormorant-garamond`.
