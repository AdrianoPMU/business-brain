# 2026-10-30: AI phone calls (the assistant calls leads and books them)

**Where:** agenda-llena (commit `fddba88`, migration 0065 applied), ElevenLabs (new agent + 5 tools), Supabase data

**Done**
- One ElevenLabs agent for every studio: "Agenda Llena – Llamadas con IA (todas las clientas)" (agent_8301m66zfbq0e11sfmyx72e4hfha). Claude Haiku 5.5 (Gemini/GPT backups), Flash v2.5 voice, mu-law 8k for phone, Spanish with switch to English, voicemail message, end call, 7-min cap.
- Each call: the studio's own Twilio number dials the lead (recorded, dual channel). When she answers, the app registers the call with ElevenLabs and sends that studio's prompt, greeting, voicemail line and voice. The prompt also gets the fixed rules, services and prices, real free times, policies, the assistant's studio info and her form answers.
- Agent tools (webhooks to app.pmuacademia.com/api/ai-call/tool/...): ver_horarios, reservar_cita, reagendar_cita (same engine as Sofía's texts), pasar_a_artista (transfers the live call to a cell if one is set, else alerts the artist), guardar_resultado (outcome + summary; "no_llamar" turns off AI calls for that person).
- Booked with no deposit: she gets the normal confirmation text. With a deposit: the link goes by text during the call, slot held 45 min.
- After the call: note in her chat with the outcome, "te acabo de llamar" text if she missed it (once a day, texting hours, not right after another text), exact transcript copied from ElevenLabs (Whisper of the recording as fallback), Sonnet review of how the AI did with suggested prompt lines.
- Ajustes > Llamadas con IA (every studio): on/off, voice picker with previews (6 recommended Latina voices + anything in the ElevenLabs account), speed, stability, greeting, voicemail message, full editable call instructions, calling hours (inside 8 am–9 pm her time), missed-call text on/off, transfer cell, test call to any number (nothing gets booked), agency-only ElevenLabs key field.
- Contact panel: "Llamar con IA" button. Llamadas page: AI calls with outcome, recording, transcript, review; shows for studios with AI calls on.
- Automation step "Llamada con IA" + template "Llamada con IA a leads nuevos": call now, retry at 2 h and next day 11 am (retries skip if they already talked), stops if she books or texts back. Installed OFF in all 8 studios.
- The greeting always includes "asistente virtual" and "la llamada se graba" even if a studio edits it out.
- 9 new tests; full suite 444 passing, build clean.

**Decided**
- One shared agent with per-call overrides instead of one agent per studio, so prompt/voice edits in the app apply immediately.
- AI calls off by default everywhere; Adriano turns them on per client after a test call.

**Open / next**
- Adriano: paste the ElevenLabs API key in Ajustes > Llamadas con IA (agency login). Nothing can call until then.
- Do a test call and confirm the recording's speaker channels (agent_channel = 2 is a guess; only matters for the Whisper fallback).
- Add consent wording to each client's Meta Instant Form (automated/AI calls and texts from the studio) before turning the automation on.
- Inbound calls to studio numbers still don't go to the AI (only PMU Academia's number rings the app).
- The tool secret lives in app_settings (ai_call_tool_secret) and in the 5 ElevenLabs tool headers; if it's ever rotated, update both.
