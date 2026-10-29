# 2026-10-29: Watch-to-confirm links for today's sales calls

**Where:** Agenda Llena live database (PMU Academia agency workspace), Zuops PMU Academia calendar

**Done**
- Today's 5 PMU Academia sales calls were booked in Zuops, not in Agenda Llena, so none had a pre-call video link. Added each one to Agenda Llena as a lead + appointment (confirmed, `watch_required`, own `watch_token`, Zuops Meet link, `funnel_id` = the `llamada` funnel so the page plays `confirmar-llamada-v1.mp4`): Yohaira 12:30 PM ET, Diana Cardenas 5:30 PM ET, Teresa Gonzalez 6:00 PM ET, Ana 6:30 PM ET, Milady 7:00 PM ET.
- Links are `https://app.pmuacademia.com/v/<token>`; all five checked on the live app (right name, time, her time zone, video loads).
- Gave Adriano a ready WhatsApp message per person (wa.me links) to send from his own number.
- Avoided side effects: `google_event_id` set to a `zuops-…` marker so the Google sync trigger doesn't add a second event to his calendar (Zuops already put them there); `watch_log.invite` marked done so the app doesn't send its own invite; `reminder_day_sent_at` / `reminder_soon_sent_at` stamped so the app's generic reminders don't double Zuops' reminders; `ai_enabled = false` so Sofía doesn't text them.
- `sms_consent = true` for the four who ticked "Acepto recibir mensajes de texto de PMU Academia sobre mi llamada" on the Zuops form; false for Ana (booked through crm.adrianolocal.com/c/pmu-academia with no consent box).

**Decided**
- The app's watch reminders (texts from 513-599-0354) and the 2-hours-before "call her" alert to Adriano still run for anyone who hasn't watched.

**Open / next**
- PMU Academia's booking calendar still lives in Zuops, so new bookings won't get a watch link automatically until the book-a-call funnel points at Agenda Llena's `/llamada` page.
- WhatsApp sender isn't connected in Agenda Llena (`whatsapp_from` is null), so the app can't send the WhatsApp invite itself yet.
- If Adriano doesn't send the WhatsApp to someone, set her appointment's `watch_required = false` so she doesn't get "¿pudiste ver el video?" texts.
