# 2026-10-29: Sofía sees the photos leads send

**Where:** agenda-llena (app), Sofía's replies to leads

**Done**
- Sofía now looks at the photos a lead texts her. The photos were already being copied into our storage and shown in the chat, but the assistant only saw the `📷 (foto)` placeholder, so she answered blind to anything visual.
- Her turn is sent as one image per photo plus the words, when there are words. The placeholder is dropped so it doesn't read as something the person typed.
- Limits: only the newest 3 photos, only links we host in `message-media`, and only formats Claude can read (jpeg, png, webp, gif). An iPhone HEIC photo stays a plain text bubble rather than breaking her reply.
- New block in her instructions, added only when photos are present: use just what's visible, don't describe her skin, don't guess, ask what she wants with the picture.
- Five new tests in `functions/_lib/ai.test.ts`. Full suite 383 passing, typecheck and build clean. Pushed to `main` (commit `22943b6`), live in a couple of minutes.

**Decided**
- Three photos max, newest only: every image is paid for again on each reply in that conversation.
- Twilio's own media links are never sent to the model. They need a login, so the fetch would fail and that failure would take down her whole reply.

**Open / next**
- Photos that arrive by WhatsApp or Instagram are still not seen by Sofía. `runAiReply` only handles leads on `sms` and `form`, so those channels never reach her at all. That's a separate gap from this fix.
- Watch the cost per reply on conversations with photos: three images add a few thousand tokens each time she answers.
- "Let Sofía see photos leads text in" can come off the open-items list.
- Not tested against a real inbound MMS. Worth doing on the next real photo from a lead: confirm she mentions the picture instead of asking what they mean.
