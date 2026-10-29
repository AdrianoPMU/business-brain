# 2026-10-29: Ali Beauty Lounge voucher ads + review page (in progress)

**Where:** agenda-llena branch `ali-review-page` (commit 27df960, not on main yet), client Ali Beauty Lounge

**Done**
- Adriano asked for Ali the same as Aglahel: Spanish and English green-screen voucher ads, then a review link he can send her.
- Built her review page at `public/revision/ali-beauty-lounge/` (copy of Aglahel's, Champagne & Oro colors): both ads, voucher page (alibeautylounge.com/voucher), website, studio details. It also asks her to confirm her hours (closed Thu/Sun, 8–5 other weekdays, Sat 9–3) and how long Ombré lasts (site says 1–2 years, voucher page says 1–3).
- Results reel (6 of her photos) and headline pills rendered the same way as Aglahel's ad. Scripts are Aglahel's changed to Los Angeles / Ali Beauty Lounge, with "te llega por texto" instead of a personal code, since Ali's voucher has no personal code.

**Decided**
- Zuops has 3 credits (resets Nov 3), not enough for the ~48-credit presenter takes. Adriano chose to call the model under Zuops Motion directly: Google's Gemini Omni 1.1 Flash through the Gemini API with his own key (about $0.10 per second at 720p, about $6 for both ads).
- The review page stays off main until the ads exist, so Ali never opens a page with empty videos.

**Open / next**
- Waiting on Adriano's Gemini API key (billing on). Then: generate both presenter takes (first clip + extensions so it's one continuous take), composite the green-screen ads, add `anuncio-es/en.mp4` + posters and durations to the page, merge to main, send Adriano the link: app.pmuacademia.com/revision/ali-beauty-lounge/
- The key must never go into a repo, log or the app.
