# 2026-10-31: Booking texts in the client's language

**Where:** agenda-llena, branch `booking-texts-in-her-language` (not on main yet)

**Done**
- Found that booking pages sent the page language but the server ignored it: every booking confirmation and reminder went out in Spanish, even for clients who booked on the English page.
- `/api/funnel/book` and `/api/site/book` now save her language on the lead (same "Idioma de la página" answer the follow-ups, workflows, AI texting and AI calls already read). New helper `functions/_lib/leadLang.ts`.
- English versions of: the booking confirmation (procedure, phone consult, in-person consult, Google Meet call), the artist-booked confirmation, and the day-of / 15-minute reminders. English dates and time zones ("Wednesday, October 28 at 5:30 PM (Eastern Time)"). Uses the studio site's English service name when it's up to date.
- Spanish texts unchanged. Build and all tests pass (new `leadLang.test.ts`).

**Decided**
- Language is stored in the existing form-answers field, not a new column, so no migration was needed and everything already reading it stays in sync.

**Open / next**
- Adriano to review and merge the branch to main (goes live on merge).
- Still Spanish only: pre-call video invite texts (`precall.ts`). The AI texter (Sofía) already switches to English when the client writes in English.
