# 2026-10-30: Videos in the app (our own Zuops Motion)

**Where:** agenda-llena (commit 26a8a0c, pushed to main), business-brain

**Done**
- New Videos screen in the app (`/videos`): pick a type (person talking, product, story, anything), a presenter photo (saved for reuse), a brief or exact words, 4–60 seconds, Spanish/English, vertical/horizontal, 720p/1080p, optional product/place photos.
- Server engine (`functions/_lib/video.ts`, runner `/api/videos/run` every minute): Claude splits the words into ~8 s lines and writes a locked look/voice description → one Gemini Omni 1.1 Flash clip per line, every clip starting from the same presenter photo (same method as `scripts/greenscreen-ad`) → Whisper checks each clip's words and finds where they end (one automatic redo if the line came out skipped/stuttered) → clips cut where the words end and joined into one MP4.
- Joining runs in plain JS (mediabunny remux, no re-encode), since Cloudflare has no ffmpeg. Tested on sample clips: output decodes clean.
- Push notification when a video is ready or fails. Cost shown per video (~$1 per clip at 720p).
- Migration `0063_video_ads.sql` written (not applied yet): `video_avatars`, `video_jobs`, `video-ads` bucket, `workspaces.video_enabled` (on for the agency workspace only), pg_cron `videos-run`.

**Decided**
- Videos start on for PMU Academia's own workspace only; turning them on for a client is an agency decision (each clip is real Gemini money). Max 10 videos per studio per day.
- Talking videos need a presenter photo (no auto-generated presenter yet).

- 15:45 ET: Adriano added `GEMINI_API_KEY` (secret) to Cloudflare Pages, app redeployed, migration 0063 applied with his OK. Videos are on for the agency workspace; the `videos-run` cron answers 200 every minute.

**Open / next**
- Keep the video key in its own Google Cloud project, not the VSL 4 one: Tier 1 is 20 Omni requests a day per project, and a 60 s video is 7+ requests.
- First real test video once both are in; check the `background: true` polling path and Whisper reading the clip audio against the live APIs (both untested live).
- Not built yet: ElevenLabs voice pass for one consistent voice, auto-made presenter photo, captions, making videos from the in-app assistant.
