# App: artist gets alerted when a client books

**Date:** 2026-10-31

**What changed**
- New: when a client books herself (booking page, studio website, or Sofía), the artist gets an app notification, a text to her alert cells and an email. Same settings as the new-lead alerts (Ajustes > Estudio > Avisos), now titled "Avisos de leads y citas nuevas".
- Bookings the artist makes in the app herself don't alert anyone. Deposit bookings alert once the deposit is paid.
- Code: `functions/api/push/notify.ts` handles kind `appointment`; `functions/_lib/leadAlerts.ts` has `sendBookingAlert` / `bookingSms` / `bookingEmail` and a shared sender. Settings now also show "No hay celular guardado para el texto" when texts are on but no cell is saved.
- Migration `0067_booking_alerts.sql`: trigger on appointments pings /api/push/notify. Applying it from the session timed out on an approval prompt; check `select tgname from pg_trigger where tgname = 'appointments_booking_alert'` and apply it if missing.

**Found while checking (31 Oct)**
- Before this, nothing told the artist about a booking: no text, no email; the only phone notification was "Lead nuevo" for brand-new leads.
- No studio has an alert cell saved, so even new-lead texts went nowhere.
- RESEND_API_KEY is missing from the Cloudflare Pages production settings (EMAIL_FROM is there), so no alert emails go out ("El correo no está configurado").
- Cocora, Glow Brows and Beauty By Alix have no device with app notifications turned on.

**Open / next**
- Adriano: add RESEND_API_KEY in Cloudflare (Pages > agenda-llena > Settings > Variables, production, as a secret) and redeploy.
- Add each artist's cell in her alert settings.
- Have each artist open the installed app and allow notifications.
