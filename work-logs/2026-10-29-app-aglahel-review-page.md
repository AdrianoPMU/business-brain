# 2026-10-29: Review page for Aglahel Ramos (ads + site, with feedback)

**Where:** agenda-llena (commit 4de8547), Supabase, client Aglahel Ramos

**Done**
- Rebuilt Aglahel's two green-screen voucher ads (ES 29s, EN 28s) from the Zuops presenter takes and her gallery photos, same scripts as the 10/28 session. The English one had never been finished in that session.
- Built a client review page at **app.pmuacademia.com/revision/aglahel-ramos/** (static, in `public/revision/aglahel-ramos/`): both ads, her voucher page, her website, and a "datos" card (hours, location, $50 deposit, photos). On each one she taps "Me encanta" or "Quiero cambios" and writes notes; progress saves on her phone.
- `POST /api/revision` saves each send to the new `client_review_feedback` table (migration 0062) and alerts the agency: push to the agency logins plus a text to the agency owner's cell (same cells as the pre-call alerts).
- Service worker now skips `/revision/` so people with the app installed still get the page.
- Fixed Aglahel's studio time zone: was America/Phoenix, now America/Chicago (San Antonio). She had no bookings or leads yet.
- Tested live: page, videos, error cases, and one labeled test send (row deleted afterwards).

**Decided**
- Review pages live on app.pmuacademia.com under `/revision/<studio-slug>/`, Spanish only.

**Open / next**
- Send her the link. Her answers arrive as a text + push; past answers are in `client_review_feedback`.
- Still missing for her: exact address, confirmed hours (site shows Mon–Sat 10–6 as a placeholder), original photos without text.
- To make one for another client, copy the folder and change the slug, videos and screenshots.
