# 2026-10-31: Booking forms ask for first and last name

**Where:** agenda-llena (commit 8d3ade9, pushed to main)

**Done**
- Every public booking form now has two boxes, Nombre and Apellido (First name / Last name), side by side, instead of one "Tu nombre" box: the funnel booking page (including the FB-form gate layout), the artist website booking sheet and its waitlist form, the phone-consult page (Llamada), and /reservar.
- Both boxes are required. The last name was optional on the gate layout before; now it's required there too.
- The two boxes are joined into one full name before sending, so the server, leads, texts and Meta events work the same as before.
- Links that prefill a name (?name=) split it: first word goes in Nombre, the rest in Apellido.
- New helper `src/data/names.ts` (splitName / joinName).

**Decided**
- Adriano asked for first and last name on bookings instead of a single name field.

**Open / next**
- If booked calls per visitor drop on the split tests, consider making the last name optional again on the gate layout.
