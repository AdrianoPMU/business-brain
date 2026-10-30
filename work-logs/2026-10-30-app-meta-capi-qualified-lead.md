# 2026-10-30: Meta CAPI upgrade + QualifiedLead event

**Where:** agenda-llena (commit 712056a), Supabase funnel `pmu-academia/agenda`, PMU Academia pixel 2051595718895144

**Done**
- New `functions/_lib/capi.ts`: every server event to Meta now sends hashed email, phone, first AND last name, lead id, IP, browser, fbp, and fbc (built from the ad click id when the cookie is missing). Funnel events and pipeline-stage events both use it. Meta errors are now logged instead of ignored.
- New `QualifiedLead` server event. A funnel can set `content.qualify` rules (question + accepted answers). When a lead's answers match, Meta gets one QualifiedLead per lead (event id `ql-<leadId>`), on opt-in or booking.
- Set the rule on PMU Academia's `agenda` funnel: "¿Ya tienes clientas que te pagan por micropigmentación?" must start with "Sí".
- Website bookings: the confirmation page now sends Schedule with the same event id as the server, so each booking counts once (it was counted twice). Paid-deposit Schedule on funnel thank-you pages got a stable id.
- Optional env var `META_TEST_EVENT_CODE` shows server events in Events Manager > Test events.

**Found (pixel audit, 28 days)**
- The live agenda.pmuacademia.com opt-in still submits to the **Zuops Smart Form** (crm.adrianolocal.com), not the app. Only 1 lead in 14 days reached the app's `agenda` funnel (a test from a preview build). So the app's CAPI and QualifiedLead don't run for PMU Academia's own ads until the page is switched.
- A ready version of the page that posts to app.pmuacademia.com/api/funnel/lead (with eventId, fbp, fbc and the "¿Ya tienes clientas?" question) exists as a preview deploy: f6e8b4d7.agenda-llena-video.pages.dev. Its source isn't on GitHub.
- The browser Lead on the live page has no eventID, so it can't dedupe with Zuops' server Lead (likely why Lead counts come in pairs).
- A steady ~10–15/hour server-side PageView stream hits the pixel around the clock. It doesn't come from the app (the app sends no server PageViews); likely Zuops/GHL hosting.
- Pixel also fires on crm.adrianolocal.com, zuops.com and preview domains.
- Retargeting ad set "PA | Retargeting | $5" includes the Adriano Local pixel's website visitors and engagement audiences from two non-PMU-Academia Pages.

**Decided**
- QualifiedLead = already has paying PMU clients (first rule; more questions can be added to `content.qualify`).

**Open / next**
- Promote the preview opt-in page to production on agenda.pmuacademia.com so leads go to the app (needs the page source or a redeploy of the preview build).
- Once QualifiedLead reaches ~50/week, optimize the $100/day campaign for it.
- Events Manager: domain allowlist (pmuacademia.com, agenda., kit.), find and stop the server PageView stream.
- Clean the retargeting ad set's audiences (awaiting Adriano's OK).
