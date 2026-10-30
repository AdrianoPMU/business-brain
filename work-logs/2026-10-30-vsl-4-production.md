# 2026-10-30: VSL 4 production, first half

**Where:** VSL 4 workspace (cloud session), Gemini API (Adriano's key), business-brain

**Done**
- Made presenter clips for lines 1–21 with Gemini Omni 1.1 Flash, image-to-video from one frame of presenter B. Same face, framing and studio in every clip, no equipment in shot.
- Checked every clip's words against the script. Lines 4 and 9 had stutters ("semanas y semanas", "a otra a otras"); fixed by cutting the repeated words out instead of paying for retakes.
- Built and sent Adriano a first-half draft (lines 1–21, 1:48) with the animated app graphics and captions. Transcribed the draft and read it against the script.
- Saved the production scripts to `marketing/vsl/vsl-4-production/` (no clips, no key) with a README.
- `scripts/greenscreen-ad/omni_i2v.py` now reads only the last line of the key file. Added the Tier 1 limits to that folder's README.

**Decided**
- App screens are animated graphics with demo data, not screen recordings (Adriano).
- The finished VSL will be a self-hosted mp4 on the site, not Wistia.

**Open / next**
- Gemini Tier 1 allows 20 Omni requests a day (resets midnight Pacific). Lines 22–42 get made Oct 31 and Nov 1; a scheduled check-in in this session restarts the run at 07:05 UTC Oct 31.
- Adriano to review the draft: presenter, voice, graphics, captions, and whether the patched lines 4 and 9 sound natural. Line 10's voice reads higher than the rest (about 232 Hz against 180–213), so it needs a listen.
- Then: full cut → Adriano's OK → homepage hero → publish → IndexNow.
- Delete `gemini-key.txt` from Adriano's Desktop once all clips are done, and recreate the key in AI Studio (it was printed into a tool log once).
- About $21 of Gemini spend so far on VSL 4 clips, plus a few dollars on presenter candidates.
- business-brain is a public GitHub repo, client files and work logs included. Adriano may want it private.
