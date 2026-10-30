# 2026-10-30: Homepage updated for the new offer; old VSL removed; VSL 4 script drafted

**Where:** pmuacademia.com (Lovable "PMU Offer Launch", commit `158216b`, published), business-brain `marketing/vsl/`

**Done**
- Removed VSL 3 (Wistia `upq3zz4oav`) from the homepage hero. It pitched "Sistema Diamante" with $297/$497/$997 plans, LLC formation and a free demo.
- Homepage copy, Spanish and English:
  - Hero sub mentions Sofía. Price line: "$500 el primer mes, después $297 al mes · Garantía de 30 días".
  - 6 cards: Meta ads with AI-presenter videos, Sofía (ES/EN, sees photos, books), booking page with deposit and coupon, automatic reviews (Google + Facebook), Google profile, own app.
  - How-it-works step 3 "Sofía le contesta"; step 4 mentions the review request.
  - Tú vs Nosotros adds Sofía and reviews.
  - Pricing box: "Un precio claro, todo incluido", $297/mes plus the first-month line.
  - 3 new FAQs (cost, Sofía, reviews), 7 in all. FAQPage schema follows them.
- Service schema Offer is now $500 first month, then $297/month. Updated the no-JS fallback and llms.txt to match.
- Tested: typecheck, 14 tests, build, and a browser check of / and /?lang=en (no hydration errors). Lovable copy verified by sha256. Published and checked live as Googlebot (837 words, no Wistia, offer 500). IndexNow pinged for / and llms.txt.
- Wrote the VSL 4 script: 42 lines, about 3.3 min, HOOKED VSL structure, with an AI presenter and 3 hook options. File: `marketing/vsl/vsl-4-agenda-llena.md`.

**Decided (Adriano)**
- Hide the old VSL now.
- The new VSL uses the AI presenter.
- The $500 covers the first month.
- Sofía answers in Spanish and English.

**Open / next**
- Adriano to OK the VSL 4 script and pick a hook. Then production: about 42 Gemini Omni clips (about $45–55 with retakes; needs his Gemini key, or Zuops credits after Nov 3), app screen recordings with a demo studio, a 16:9 composite with captions, a word-for-word transcription check, then Wistia and the hero.
- The /start Stripe checkout still charges $297/month with no $500 first month. Its meta description also says $297. Not changed: money needs Adriano's say-so.
