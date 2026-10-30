# Marketing

How PMU Academia finds its own clients (PMU artists who'll pay $500 the first month, then $297/month).

## Current state (late Oct 2026)

- **Own ads are paused** while the sales process gets dialed in (follow-up, show-ups, no-shows, post-call).
- When running, the budget is around $50/day, split across retargeting, IG followers + FB Page likes, and the book-a-call funnel.
- Ads run from the PMU Academia page as partnership ads with Brows By Lexxi.

## The funnel in use

**agenda.pmuacademia.com**: short-video opt-in → watch the free video → book a call. Hosted on Cloudflare. Leads land in the Agenda Llena app (not Zuops). PostHog is installed for tracking.

Other assets:
- Lead magnet: "La Campaña Agenda Llena", a free branded PDF of the exact Ombré Powder campaign we run for clients, with book-a-call buttons
- $27 kit at kit.pmuacademia.com: 850+ Spanish PMU Instagram templates (Canva)
- An AI presenter avatar (female PMU artist) used across ads; funny 3D cartoon-style ads in testing

## What we've learned

- Instant Form leads come in under $5, but they skew broke or brand-new artists.
- The original VSL page didn't convert well.
- **Homepage VSL:** VSL 3 (Wistia `upq3zz4oav`, Feb 2026) pitched the old "Sistema Diamante" with three plans, so it was taken off the homepage on 2026-10-30. VSL 4 (AI presenter, about 3 min) is drafted in `vsl/vsl-4-agenda-llena.md` and waiting for Adriano's OK on the script.
- Meta audiences live in the older "Citas PMU" ad account (the pixel is linked there).

## SEO and AI search

Goal: be "omnipresent", found in Google and in AI answers, not just ads. First audit done 2026-10-28 (score 55/100). Plan, tool and KPIs: `seo/README.md`.

## Next up

- Week 1 SEO fixes on pmuacademia.com (pre-render pages, Search Console + Bing, schema, hreflang, subdomain cleanup). See `seo/audits/2026-10-28/ACTION-PLAN.md`.
