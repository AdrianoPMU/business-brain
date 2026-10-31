# App: artist gets alerted when a client books

**Date:** 2026-10-31

**What changed**
- New: when a client books herself (booking page, studio website, or Sofía), the artist gets an app notification, a text to her alert cells and an email. Same settings as the new-lead alerts (Ajustes > Estudio > Avisos), now titled "Avisos de leads y citas nuevas".
- Bookings the artist makes in the app herself don't alert anyone. Deposit bookings alert once the deposit is paid.
- Code: `functions/api/push/notify.ts` handles kind `appointment`; `functions/_lib/leadAlerts.ts` has `sendBookingAlert` / `bookingSms` / `bookingEmail` and a shared sender. Settings now also show "No hay celular guardado para el texto" when texts are on but no cell is saved.
- Migration `0067_booking_alerts.sql`: trigger on appointments pings /api/push/notify. Applied to the live database on 31 Oct; a test booking in the PMU Academia workspace fired it (push_sent row + /api/push/notify 200).

**Found while checking (31 Oct)**
- Before this, nothing told the artist about a booking: no text, no email; the only phone notification was "Lead nuevo" for brand-new leads.
- No studio has an alert cell saved, so even new-lead texts went nowhere.
- RESEND_API_KEY is missing from the Cloudflare Pages production settings (EMAIL_FROM is there), so no alert emails go out ("El correo no está configurado").
- Cocora, Glow Brows and Beauty By Alix have no device with app notifications turned on.

**Open / next**
- RESEND_API_KEY added in Cloudflare 31 Oct (currently as plain text; switch it to Secret) and redeployed. pmuacademia.com was already verified in Resend since Oct 17, so no sending subdomain was needed.
- Fixed: alert emails in the agency's own workspace now go to its own logins (they were skipped).
- Cleanup check: delete any lead named 'PRUEBA Aviso de cita' and its appointment (note 'Prueba de aviso (borrar)') in PMU Academia if still there.
- Add each artist's cell in her alert settings.
- Have each artist open the installed app and allow notifications.
