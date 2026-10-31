# 2026-10-30: Acuity bookings flow into the app automatically

**Where:** agenda-llena (functions/_lib/googleImport.ts, /api/google/autoimport, migration 0066); Beauty Spot by Jami

**Done**
- Jami books in Acuity, which writes to her Google Calendar. The app only imported those events once (the manual import), so newer bookings showed as grey "busy" blocks with no client or service.
- New job every 5 minutes (pg_cron `google-import-run`) reads changed events on each studio's Google calendars and turns booking-tool events (Acuity) into real appointments with the client's name, phone/email and matching service. It also moves an imported appointment when Acuity moves it and cancels it when Acuity deletes it.
- Acuity titles ("Name: Type (Calendar)") are now parsed properly; English types match her Spanish services ("Hybrid refill" -> "Pestañas híbridas retoque").
- People/bookings that come from a calendar import (`imported_from = 'google'`) never trigger flows, AI calls or "new lead" pushes: they never opted in.
- Cleaned Jami's 9 earlier imports (names like "Rebecca Shaw Hybrid refill Jami Gavilanes" -> "Rebecca Shaw", services filled). First run brought in 12 missing Acuity bookings.

**Decided**
- Only events that clearly come from a booking tool are imported automatically; personal events stay busy blocks.

**Open / next**
- Brows By Lexxi's old imports still have the time in the name ("2 00 pm Ayleen Duenas").
- Other schedulers (Square, Vagaro, GlossGenius) could be added to `fromBookingTool` when a client uses one.
