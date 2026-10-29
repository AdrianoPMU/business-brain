# 2026-10-29: The three approved database changes, as one migration

**Where:** agenda-llena, `supabase/migrations/0061_ali_calendar_lexxi_role_agency_offer.sql`

**Done**
- One file does the three changes Adriano approved, in one transaction, safe to run twice: `fbf2673` on `main`.
  1. Unlinks every **client** calendar connected with `info@pmuacademia.com` (Ali's is the one known). The agency workspace is excluded, so the sales-call calendar is untouched.
  2. Adriano goes from `owner` to `agency` on Brows By Lexxi, so her new-lead alerts stop landing in the agency inbox. `agency` keeps every permission the app checks; `leadAlerts` and `email.ts` only mail members whose role is not `agency`.
  3. Re-applies `set_agency_offer` (0060 verbatim), so the offer and call link on Ajustes > Asistente IA can finally save.
- The file ends with a `select` that prints one row per change. If the Lexxi workspace can't be found, or the role change matches nothing, or the studio would be left with nobody receiving alerts, it says so in that report instead of failing silently.
- Syntax-checked with a PostgreSQL parser (pglast, PG 17 grammar). The PL/pgSQL bodies were reviewed by hand: the parser build available here can't compile even a trivial `BEGIN ... END` block.

**Decided**
- The calendar fix is rule-based, not workspace-based: any client studio connected with the agency login is wrong by definition, so it doesn't depend on guessing Ali's workspace id or slug.
- The role change keys off `info@pmuacademia.com` as the login on that workspace. If Adriano's account there uses another email, the migration reports it and changes nothing.

**Open / next**
- **Not applied yet.** No Supabase access from this machine, so Adriano pastes the file into the Supabase SQL editor. Until he does, nothing changed in production.
- After it runs: Ali has to reconnect her own Google account from Ajustes > Agenda, or her bookings stop creating calendar events. Her existing events keep their ids.
- Watch that Lexxi (or Paola) is a member of her own workspace with a role that isn't `agency`, otherwise her lead alerts land nowhere.
- Still open from the same list, all outside the repo: `RESEND_API_KEY` in Cloudflare, and Meta read access to the ad account.
