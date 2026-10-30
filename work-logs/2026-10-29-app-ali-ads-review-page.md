# 2026-10-29: Ali Beauty Lounge voucher ads + review page

**Where:** agenda-llena (commit 4e4ff8b on main), business-brain `scripts/greenscreen-ad/`, client Ali Beauty Lounge

**Done**
- Made Ali's Spanish (33s) and English (31s) green-screen voucher ads, the same style as Aglahel's and Lexxi's: AI presenter bottom-right, 6 of Ali's real Ombré photos rotating behind her, "cejas efecto polvo 👀 / 15 vouchers a $397 (antes $550)" pills. Both were transcribed word for word to check them.
- Review page is live at **app.pmuacademia.com/revision/ali-beauty-lounge/** in Champagne & Oro colors: both ads, her voucher page, her website, and her studio details. Her answers come to Adriano as a push + text, the same as Aglahel's.
- On the page she's asked to confirm her hours (closed Thu/Sun, 8–5 other weekdays, Sat 9–3) and how long Ombré lasts. Her website says 1–2 years and her voucher page says 1–3.
- Saved the ad-making scripts and what we learned in `scripts/greenscreen-ad/`.

**Decided**
- Zuops had 3 credits (resets Nov 3), so Adriano chose to call Zuops Motion's model, Gemini Omni 1.1 Flash, directly with his own Gemini key. The key was deleted from the workspace after use and never went into a repo or log.
- One 10s clip per line, each starting from the same presenter frame. Chained extensions repeated words at every seam and stop at 30s.
- English script: Google's filter blocked "You don't pay anything today…" twice, so that line became "And the best part? Just tap the button and grab your voucher, and we'll send it straight to your phone." The Spanish ad still says "Hoy no pagas nada."
- Ali has no personal voucher code, so the ads say "te llega por texto" and never promise a code.

**Open / next**
- Adriano sends Ali the link.
- Gemini cost for this was about $14 (test clip, a failed chain and re-dos included). A clean run is about $10 for both languages.
- Adriano can delete `gemini-key.txt` from his Desktop, or delete the key itself in AI Studio.
- Her ad account has no Meta pixel yet (from the Oct 28 log). Needed before running ads to the voucher page.
