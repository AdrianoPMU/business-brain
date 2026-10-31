# 2026-10-31: Sign-up links v2 (Zuops parity)

**Where:** agenda-llena, branch `signup-links-v2` (not merged, not live)

**Done**
- Went through every setting of the Zuops signup link (Basics, Design, Form, Starting setup, Payment, Contract, Sub-account, Emails) and rebuilt it in Agencia > Registro.
- Links now have: several plans (monthly or one-time), payment / promo codes / contract each on or off, extra questions, close date and signup limit, headline and page design (layout, colors, logo, cover, brand panel, highlights, quote, last page), alert emails, editable welcome email, account name template, and a texting number she picks right after paying.
- Starting setups (snapshots): save a studio's setup and load it into every new client automatically, or let her pick, or use setup codes (`?code=`). Copies services, hours, AI settings, forms, pages, automations, follow-ups, reviews, gift cards, birthdays. Never copies leads, clients, messages, payments, numbers, domains or connected accounts.
- Visits per link, so the agency screen shows Zuops-style stats (live links, visits, sign-ups, conversion).
- Migration `0067_signup_links_v2.sql` written and tested against the live database inside a transaction that was rolled back (nothing saved): a studio copied from Beauty Spot by Jami came out with all 15 services, 4 forms, both pages (service links re-pointed), its automation and follow-ups.
- Build and all 459 tests pass; walked the whole flow in demo mode.

**Decided**
- Payment always comes after the contract (Zuops lets you flip it; signing first is the safer order).
- Left out from Zuops: "Design it for me" AI, custom CSS, starter credits, industry picker.

**Open / next**
- Adriano to approve: apply migration 0067 to the live database, then merge `signup-links-v2` to main.
- After it's live: save a "PMU Academia" starting setup from a template studio, then rebuild the $297 link from Zuops here ($500 first month = $297/month + $203 setup) and point ads to the new /registro link.
