# Action Plan — PMU Academia "omnipresent" SEO + AI search

Goal: when a Spanish-speaking PMU artist in the US searches Google, asks ChatGPT/Perplexity/Gemini, watches YouTube or scrolls Facebook/Instagram about getting more clients, PMU Academia shows up.

Baseline (2026-10-28): health score 55/100. Brand not found in search. 4 indexed-eligible URLs.

## Critical (week 1) — make the site readable to every crawler

| # | Fix | Where | Check it worked |
|---|---|---|---|
| C1 | Pre-render every public route to static HTML at build time so raw HTML = rendered page (FAQ, price, story, results included) | Lovable project for pmuacademia.com, or move marketing pages to Cloudflare Pages like client sites | `curl -s https://pmuacademia.com/ \| wc -w` ≥ 500 words; `/seo page` shows raw ≈ rendered |
| C2 | Verify pmuacademia.com in Google Search Console + Bing Webmaster Tools, submit sitemap, enable IndexNow (Cloudflare Crawler Hints) | GSC, Bing WMT, Cloudflare | URL Inspection shows "URL is on Google" for `/`, `/resultados`, `/book` |
| C3 | Fix hreflang: real `/en/` pre-rendered path with own canonical + reciprocal hreflang, or remove hreflang | Lovable | No hreflang/canonical conflict in `/seo hreflang` |
| C4 | Add `/book` to sitemap; static nav + footer linking Inicio, Resultados, Guías, Nosotros, Agenda tu llamada | Lovable | Sitemap lists `/book`; raw HTML has ≥ 6 internal links |
| C5 | JSON-LD: Service (provider = Organization, areaServed US, availableLanguage es) + Offer 297 USD/month; FAQPage for the visible FAQ; Person for Adriano (@id, jobTitle, sameAs) | Homepage, `/book` | `/seo schema` validates with 0 errors |

## High (weeks 2–3) — make the brand a real entity

| # | Fix | Check |
|---|---|---|
| H1 | `/nosotros`: Adriano + Lexxi story, photos, years selling advertising to local businesses, link to Brows By Lexxi | Page indexed; Person schema links to it |
| H2 | Rewrite `/resultados` as a dated, quotable data page: "Cuánto cuesta conseguir clientas de micropigmentación con anuncios (datos reales)". Lead with a 2–3 sentence answer, then the table, then method. Confirm each client agrees to be named | Page quoted when asking ChatGPT/Perplexity about PMU lead costs |
| H3 | Pick one name and use it everywhere: "PMU Academia USA" with "Sistema Agenda Llena" as the product. Same name, logo, description on IG, Facebook page, YouTube, LinkedIn, TikTok | Brand search returns pmuacademia.com first |
| H4 | Create Facebook page, YouTube channel, LinkedIn company page + Adriano's LinkedIn; add all to `sameAs` | `sameAs` ≥ 5 profiles |
| H5 | Footer credit on every client site: "Página y anuncios por PMU Academia" → pmuacademia.com (Yoly, Jami, Cocora, Ali, Aglahel, Genluxe, Lexxi), with each client's OK | 6+ referring domains |
| H6 | Subdomains: noindex agenda funnel; real `robots.txt` on agenda/app; 404 for unknown paths; kit `lang="es"` + canonical | `/seo technical` on each subdomain clean |

Google Business Profile: PMU Academia is online-only (calls on Google Meet), which Google's guidelines don't allow a profile for. Don't create one unless you start meeting clients in person at a real address.

## Content map (month 2 onward) — the open Spanish niche

Build `/guias/` as a hub. Each article: answer in the first 2–3 sentences, question-style H2s, a table or checklist, PMU Academia's own numbers where possible, byline Adriano, dated, linked to `/book`. Plan each with `/seo content-brief`, check with `/seo geo` before publishing.

**Pillar 1 — Conseguir clientas**
- Cómo conseguir clientas de micropigmentación en Estados Unidos (pillar)
- Anuncios de Facebook e Instagram para micropigmentación: guía paso a paso
- Cuánto cuesta conseguir una clienta de cejas con anuncios (reporte con datos reales) ← original data, top priority
- Perfil de Google para micropigmentadoras: cómo salir cuando buscan "cejas cerca de mí"
- Cómo pedir reseñas en Google a tus clientas (mensajes listos)
- Qué publicar en Instagram si eres micropigmentadora (links to the Kit PMU)

**Pillar 2 — Convertir y agendar**
- Qué contestar cuando te preguntan "¿cuánto cuesta?" por mensaje (plantillas)
- Cómo cobrar depósito y reducir las citas que no llegan
- Seguimiento por WhatsApp y texto a prospectas que no agendan
- Asistente con IA para agendar citas: qué hace y cuándo vale la pena

**Pillar 3 — Precios y negocio**
- Cuánto cobrar por cejas ombré / powder brows en Estados Unidos
- Cuánto cobrar por microblading, lip blush y delineado
- Formularios de consentimiento para micropigmentación en español
- Requisitos para trabajar micropigmentación por estado (TX, FL, CA, NY, IL…) — cite each state board; review yearly

Later: English versions under `/en/guides/`; comparison pages via `/seo competitor-pages` (e.g. "Agencia general vs PMU Academia").

Cadence: 2 articles a week. Refresh each article every 90 days (AI answers favor recent pages).

## Beyond the website (omnipresence)

- **YouTube (Spanish):** one video per article, plus 2–3 Shorts cut from it; embed the video in the article. Screen recordings of the app and results videos work without being on camera. Third-party studies find YouTube mentions are the strongest brand signal for AI answers.
- **Facebook groups and PMU communities:** answer questions with real numbers, link only when it helps. Same for Spanish PMU podcasts and supplier blogs; pitch the cost-per-lead report as a guest topic.
- **Directories for agencies:** Clutch, DesignRush, UpCity and Yelp (service-area, no address shown) for consistent brand mentions.
- **Paid (already running):** keep retargeting site visitors on Facebook/Instagram; add YouTube remarketing once the channel has videos.

## Monitoring (ongoing) — with claude-seo

- `/seo drift baseline https://pmuacademia.com` now; `/seo drift compare` after every site deploy.
- `/seo audit https://pmuacademia.com` monthly; save reports in `marketing/seo/audits/YYYY-MM/`.
- `/seo google setup` once Search Console is verified → real clicks, queries, indexation.
- Monthly AI spot check: ask ChatGPT, Perplexity, Gemini and Google AI Mode the 10 core questions above; log whether PMU Academia is cited.
- PostHog: track referrers chatgpt.com, perplexity.ai, gemini.google.com, copilot.microsoft.com.
- Optional: DataForSEO extension (pay-as-you-go) for Spanish keyword volumes and live SERP/AI-mention checks.

## KPI targets

| Metric | Now | 3 months | 6 months | 12 months |
|---|---|---|---|---|
| Health score | 55 | 75 | 85 | 90 |
| Indexed pages | ≤ 4 | 20 | 45 | 90 |
| Brand search shows pmuacademia.com #1 | No | Yes | Yes | Yes |
| Organic clicks / month (GSC) | unknown | 100 | 500 | 2,000 |
| Core questions where an AI answer cites PMU Academia (of 10) | 0 | 1 | 3 | 6 |
| Referring domains | ~0 | 8 | 20 | 40 |
| Booked calls from organic + AI / month | 0 | 2 | 6 | 15 |
