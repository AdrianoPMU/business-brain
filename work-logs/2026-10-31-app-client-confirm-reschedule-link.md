# 2026-10-31: Clients confirm or reschedule from a link

**Where:** agenda-llena (commits c2b927d, d2a09c1, cc2662f), Supabase migration 0068 (applied to the live database)

**Done**
- Every appointment has its own private link: `/cita/<token>`. It works on app.pmuacademia.com and on studio domains.
- The booking confirmation text (booking pages, website, and appointments the artist books from Agenda) now ends with that link instead of "respóndeme aquí". English bookings get English wording and `?lang=en` on the link.
- The page shows her appointment and two buttons: **Confirmar mi cita** and **Cambiar el día o la hora**. Changing shows the real free times (same engine and studio rule as Sofía) and moves the same appointment, so deposit, forms and Google Calendar follow it.
- The studio's reschedule rule (Ajustes > Reglas de citas, default 2 days before) applies. Past the deadline, or for services that can't be moved, the page tells her to reply to the text instead.
- When she confirms or moves it: a note in the lead's chat, a push to the artist, a "Confirmó ✓" badge in Agenda. Moving also resets the reminders for the new day and texts her the new time (only with text consent, 8 AM–8 PM).
- Day-of reminder: if she hasn't confirmed, it includes the link to confirm with one tap; if she already confirmed, it just says "te esperamos".
- Agenda appointment details have a button to copy her link (to send by WhatsApp, say).
- Migration: `appointments.manage_token` (filled for all existing appointments without firing triggers) and `appointments.client_confirmed_at`.

**Decided**
- No cancel button on the page; to cancel she replies to the text.
- Google Meet call confirmations (PMU Academia sales calls) don't get the link; they keep the pre-call video confirmation.

**Open / next**
- Watch the first real confirmations and reschedules come through.
