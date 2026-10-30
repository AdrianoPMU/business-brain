# 2026-10-30: Voucher rules fixed, voucher funnel rolled out to Jami, Yoly, Cocora, Alix

**Where:** agenda-llena (app, commit `8b41212`), Supabase data, Meta ad accounts for Jami, Yoly and Cocora

**Done**
- App: the "X of 15 left" count now drops only when a voucher holder books her procedure (not a consult, not cancelled or no-show). Claiming alone no longer uses one up. Lexxi's page went from "sold out / waitlist" back to 13 of 15 left.
- App: selling out no longer starts the 24-hour last call. Every voucher keeps its full days (content.voucher.days, default 7). Waitlist vouchers also get the full days, and the waitlist text and page say days instead of 24 hours.
- App: the separate "Your voucher 🎟️" picture text is off unless a funnel sets content.voucher.mms = true (it failed or went undelivered for some numbers and doubled the texts).
- Lexxi data, no texts sent: the 5 waitlist vouchers due to release at 1:45–2:10 PM today (Alyssa, Shanya, Alicia, Toni, Chas) now run to Thu Nov 5. The 11 vouchers the old 24-hour rule released early (Kathy, Chrisshay, Niurka, Robin, Sandy, Kiyana, Ana, Gayan, Selena, Imeisha, Jamie) are back with their codes, good through the original Nov 3 or 4. Each chat has a system note explaining it.
- Jami, Yoly, Cocora, Alix: added Lexxi's 6-text follow-up sequence (Spanish + English, uses {asistente}/{artista}/{estudio}, no dollar amounts; voucher steps skip themselves for non-voucher leads).
- Jami, Yoly, Alix: voucher funnels set to call only (no deposit) until they connect Stripe or Square. Cocora keeps the deposit option (Square connected).
- Cocora: her voucher funnel fired pixel 1168954625411970, which isn't in her ad account. Switched the ombre funnel to 2302573763899313 (her ad account's pixel). Her "sitio" funnel still has the old one.
- Checked all four voucher pages live: beautyspotbyjami.com/voucher, yolybrowstudio.com/voucher, beautybyalix.com/voucher, app.pmuacademia.com/f/cocora-aesthetics/ombre/voucher.
- Meta, all PAUSED for Adriano's review: "Voucher Ombré $397 - Página voucher - Oct 30" in Jami's ($15/day, 1 image ad), Yoly's ($20/day, image + her client reaction video) and Cocora's ($25/day, image + Tatiana's explanation video) accounts. Leads objective, optimized for the Lead event on each pixel, same area and Spanish targeting as their current ads, Advantage+ audience on. The current form campaigns are untouched.

**Decided**
- Adriano: fix the voucher mechanics before rolling out; voucher-page campaigns built paused and kept alongside the form ads until they get leads; call only for clients without payments.

**Open / next**
- Jami: her Ombré listing in the app is $400, but the page and ads say "normally $550". Needs her real regular price before going live.
- Alix: her "Powder Brows" listing is $300, so a $397 promo is more than her regular price. Offer needs fixing; also no pixel, no results photos, no address on her page, and no ad account connected to the Meta tools.
- Jami: current ads target Plainfield, NJ (15 mi); her page says Belleville, NJ. Copied as-is; confirm her studio location.
- Jami and Alix have no results photos/videos on their voucher pages.
- Lexxi's 5 waitlist and 11 restored leads weren't texted about the change; Sofía sees the new state if they reply.
- Lexxi's calendar is still blocked most days until mid-November.
