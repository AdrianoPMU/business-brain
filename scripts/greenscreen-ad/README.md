# Green-screen voucher ads (without Zuops credits)

How the Ali Beauty Lounge ads were made on Oct 29, 2026. Same look as Lexxi's and Aglahel's: a small AI presenter in the bottom-right corner, the artist's real results rotating behind her, and white headline pills on top.

Zuops Motion runs on Google's **Gemini Omni 1.1 Flash**. When Zuops is out of credits, we call that model directly with Adriano's Gemini API key (AI Studio, billing on). The key goes in a private file passed as `GEMINI_KEY_FILE`. It never goes in this repo, the app or a log.

## Steps

1. `make_bg.py OUT_DIR photo1.jpg photo2.jpg[:x0,y0,x1,y1] ...` creates the results reel (`bg_loop.mp4`) and the ES/EN headline pills. Edit the two `caption(...)` lines for a different offer.
2. Make clip 1 with a text prompt (presenter, outfit, studio, first line). Then make one clip per remaining line with `omni_i2v.py ref.jpg LANG OUT_DIR 2 "line" 3 "line" ...`, using clip 1's last frame as `ref.jpg`. Every clip starts from the same frame, so the cuts look like a normal phone video.
3. `stitch.py head.mp4 clip1.mp4 clip2.mp4[:max_end] ...` trims each clip to its speech and joins them.
4. `greenscreen.py head.mp4 bg_loop.mp4 cap.png selfie_multiclass.tflite out.mp4` cuts her out and places her over the reel. The model is MediaPipe's `selfie_multiclass_256x256.tflite`.
5. Transcribe the finished ad (faster-whisper, medium) and check it word for word.

## What we learned

- Each Omni clip is 10 seconds and costs about $1. One line of about 15 words fits in a clip.
- Don't chain clips with `previous_interaction_id` (extensions). She repeats words at every seam ("listen up, listen up"), and it stops at 30 seconds.
- Google's filter blocked the English line "You don't pay anything today…" twice. "And the best part? Just tap the button and grab your voucher…" went through.
- Running 3 clips at once can hit a spending-rate limit (HTTP 429). Wait a minute and retry one at a time.
- Tier 1 limits for Omni (seen Oct 30, 2026): 4 requests a minute, a spend-based rate limit, and **20 requests a day**. The day resets at midnight Pacific. A 42-line VSL takes 3 days, so plan long videos around it. `marketing/vsl/vsl-4-production/run_slow.py` runs clips one at a time and stops at the daily cap.
- The key file must hold only the key. The scripts read the last non-empty line, so a note above it is ignored, but an error can still print the whole file.
- A stuttered word can sometimes be cut out instead of paying for a retake: `vsl-4-production/repair.py` cuts between the two starts of the repeated word with a short crossfade. Re-transcribe after.
- Clips sometimes stutter ("Beauty Beauty Lounge"). Always transcribe every clip before stitching.
