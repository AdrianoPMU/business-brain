# 2026-10-30: Sofía stops disowning real voucher texts and stops talking over Lexxi

**Where:** agenda-llena (app), Sofía's replies and the follow-up sequence. Found by reading all 35 Brows By Lexxi conversations from Oct 20 to 30.

**What was going wrong**
- Sofía told leads their voucher code, expiry date, "vouchers are gone" and last-call deadline were made up and to ignore them (Sandy, Kathy, Maricsema, Shan, plus the hand-off note on Pamelah). They were real. Kathy was told "no need to rush today" and her voucher was released an hour later.
- Cause: the voucher request is saved as a system note, and Sofía's reply builder dropped every system note. She saw her own old text with a code and a date, nothing backing it, and a rule saying "don't invent promotions", so she "corrected" herself.
- Lexxi's own texts were fed to Sofía as if Sofía had sent them. She called Lexxi's Square link "the wrong link I sent" (Shan) and kept booking Maricsema on Saturday Oct 31 while Lexxi was texting her that Saturdays were full until December.
- Pamelah wrote in English and got the hand-off message in Spanish.
- Follow-ups kept sending "did you look at your voucher?" to leads whose voucher was already released. The day-5 and day-6 steps ("your code is good through {vence}") were about to go to those 11 leads with a date already past.

**Done** (commit `d2e380b`, pushed to `main`)
- Each reply now includes DATOS DE ESTA PERSONA: her form answers plus her live voucher state from the database (holds it until X, last call until X, released, booked, or on the waitlist), and the last 8 system notes about her.
- New prompt section for both studio and sales mode: everything already sent is real, never say it was invented, never tell her to ignore it, say how things stand now, hand off if something truly doesn't add up.
- Released voucher: Sofía says it passed to the next person and hands promo-price asks to the artist, unless the artist already told her in person she'd honor it.
- Lexxi's texts are tagged `[Lexxi en persona]` in what Sofía reads, with a rule not to contradict them. The tag is stripped if she ever copies it.
- Sofía stays quiet for 6 hours after the artist texts a lead herself (leaves a note "Sofía no contestó... Contéstale tú"), and drops a ready reply if the artist wrote while it was being written. A booking already made still gets its confirmation.
- Replies (and the hand-off message) follow the language of the lead's last text, or the page language if she hasn't written.
- Follow-ups skip any step about the voucher once it's released, expired, in last call, or if she never had one.
- "A Ombré Powder Brows voucher" now reads "An Ombré...".
- 19 new regression tests built from these conversations. Full suite 402 passing, build clean.

**Decided**
- 6 hours as the "artist is handling her" window. After that, or once Sofía has written again, Sofía answers as usual.

**Open / next**
- Leads already told their voucher was fake: Kathy and Sandy were cleared up by Lexxi. Maricsema, Shan and Pamelah were never told otherwise.
- Not a prompt problem: the booking tools showed Lexxi open on Saturday Oct 31 (11 AM to 4:30 PM) when she wasn't, and Shan saw "no dates" on the app booking page while Lexxi's Square page showed Nov 19. Lexxi's availability in the app needs to match her real calendar.
- Service names styled with bold Unicode letters (𝐁𝐑𝐎𝐖 𝐖𝐀𝐗...) show up that way in confirmation texts. Plain names would read better and keep texts in standard SMS encoding.
- Watch the next few real voucher conversations to confirm Sofía repeats codes and deadlines instead of retracting them.
