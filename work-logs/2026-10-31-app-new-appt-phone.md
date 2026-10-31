# 2026-10-31: Phone number when booking a typed name

**Where:** agenda-llena (commit 8a154a7), `src/components/NewDrawers.tsx`

**Done**
- In Nueva cita, the "✏️ Escribir un nombre" option now has a "Teléfono (opcional)" field under the name.
- With a phone: the person is saved as a lead (or matched to an existing lead with the same last 10 digits, so no duplicates), the appointment books under that lead, and the "Mandarle la confirmación por texto" checkbox shows up. She gets the confirmation and the appointment reminders by text.
- Without a phone: works like before. The time is held on the calendar, no lead is created, nothing is texted.
- `repo.createLead` now returns the new lead's id (Supabase and demo repos).

**Decided**
- A typed person with a phone becomes a lead, not a client, because the text thread lives on a lead.
- The "AI call to new leads" flow does fire on that new lead, but it stops on booking, and the booking event right behind it stops it before any step runs.

**Open / next**
- Check on the live app: book a typed name with a test number and confirm the text arrives.
