# 2026-10-30: Agencia > Pendientes (to-do list per client)

**Where:** agenda-llena (app, commit `773ebaf`), Supabase (new table `agency_tasks`)

**Done**
- New tab in Agencia: **Pendientes** (`/agencia#pendientes`). Adriano writes what needs doing for each client: task, client, due date, urgent flag. It shows open/overdue/next-7-days counts, a "Lo próximo" list across every client (urgent first, then earliest due), a card per client with open tasks (check off, delete with a second tap, quick add, show done), and a line listing clients who are all caught up.
- Clients who aren't in the app yet can still get tasks: pick "Otra (no está en la app)" and type the business name. They get their own card marked "Fuera de la app".
- Database: migration `0064_agency_tasks.sql` (applied live; Supabase history lists it as `0063_agency_tasks` because 0063 was taken by video ads while this was being built). Agency admins only, through RLS with `is_agency_admin()`. Checked that a signed-in non-admin sees 0 rows.
- Seeded 7 open tasks from what Adriano had already said: Yoly (domain off Lovable, finish moving Zuops leads/notes), Jami (domain off Lovable, confirm her regular Ombré price: app $400 vs page $550), Alix (onboarding access/photos/address, fix the $300 vs $397 offer), Genluxe Beauty Studio (outside the app: relaunch powder brows, due Nov 3, a guess at "early November").

**Decided**
- Adriano wanted the client to-do board inside the app rather than a separate page.

**Open / next**
- Natisoft Brows and RAM Builders (Adriano Local) aren't in the app; add them as "Otra" clients when they have a task.
- Not checked on the live app after deploy (needs Adriano's login).
- An earlier stand-alone Client Board artifact made in the same chat is now redundant.
