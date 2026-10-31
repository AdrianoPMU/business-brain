# 2026-10-31: Client messages section with AI writing help

**Where:** agenda-llena (commit 0698e0f), Supabase migration 0069_notification_texts (applied)

**Done**
- New Ajustes > Mensajes a clientas (Client messages). Studios can rewrite the texts a client gets: appointment confirmation, phone consult confirmation, in-person consult confirmation, appointment the artist books from the calendar, day-of reminder, 15-minutes-before reminder.
- Each message has a Spanish and an English version (English goes to clients who booked on the English page). Insert buttons for variables: {nombre} {asistente} {artista} {estudio} {servicio} {fecha} {hora} {direccion} {link}. Live preview with sample data. "Back to the original text" resets it.
- {link} is the /cita confirm-or-change page. If an appointment has no link, that sentence becomes the old "reply here" line; if there's no address, the {direccion} sentence becomes "Te mandamos la dirección exacta antes de tu cita."
- "Pedir ideas a la IA" opens a chat per message: the AI gives recommendations plus 3-4 versions in different tones (Formal, Amigable, Corto, Cálido con emojis). Quick buttons (more formal, friendlier, shorter, emojis, warmer) or type any request. "Usar este" puts a version in the box; nothing saves until she taps Guardar. Endpoint: /api/notifications/suggest (Sonnet), prompt keeps texts short and human, only allowed variables.
- Defaults are word for word what was going out before, so nothing changed for studios that don't edit. Small fix: website confirmations now use the studio's real assistant name instead of always "Sofía".

**Decided**
- Video-call (Google Meet) texts, the agency's sales-call texts, and the short day-of reminder for clients who already confirmed with their link stay built in (not editable).
- Not in the agency workspace's settings list (its calls use the built-in sales texts).

**Open / next**
- Not live-tested with a real text yet. To check: edit the day-of reminder for a test studio, book a test appointment for today, and see the reminder.
- Could add the same editor for follow-ups or review requests later.
