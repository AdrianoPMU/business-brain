# SEO + AI Search Audit — pmuacademia.com

Date: 2026-10-28 · Tool: claude-seo v2.5.0 (run inline) · Health score: **55/100**

Business type: agency / B2B service, national (US), Spanish-language, online-only (sales calls on Google Meet).

Scope: pmuacademia.com (`/`, `/resultados`, `/book`, `/ejemplo`, `/privacidad`, `/terminos`), agenda.pmuacademia.com, kit.pmuacademia.com, app.pmuacademia.com/llamada/pmu-academia.

## Scores

| Category | Weight | Score |
|---|---|---|
| Technical SEO | 22% | 60 |
| Content Quality | 23% | 40 |
| On-Page SEO | 20% | 62 |
| Schema / Structured Data | 10% | 55 |
| Performance (lab) | 10% | 75 |
| AI Search Readiness | 10% | 30 |
| Images | 5% | 80 |
| **Weighted total** | | **55** |

## Top 5 issues

1. **AI bots see almost nothing.** The main site is a client-rendered Lovable app. Raw HTML has 64 words on the homepage vs 597 rendered (`/book` 30 vs 615, `/resultados` 36 vs 472). Googlebot renders JavaScript; OAI-SearchBot (ChatGPT Search) and PerplexityBot generally don't, so the FAQ, price, founder story and results never reach them.
2. **Nothing to rank for except the brand.** 4 URLs in the sitemap, all sales or legal pages. Spanish searches artists actually make ("cómo conseguir clientas de micropigmentación", "cuánto cobrar por cejas ombré en Estados Unidos", "anuncios de Facebook para micropigmentadoras") are answered by Spain-focused or English pages. Nobody serves Spanish-speaking PMU artists in the US. That gap is the opportunity.
3. **Brand name collision.** Searching "PMU Academia" and `site:pmuacademia.com` returned Prince Mohammad Bin Fahd University (PMU) and The PMU Academy Essex, nothing from pmuacademia.com.
4. **No off-site footprint.** No YouTube, Facebook page, LinkedIn, directory, podcast or press mention found; Organization `sameAs` lists only Instagram.
5. **English version is unindexable.** `hreflang="en"` points to `/?lang=en`, which serves the same Spanish HTML with a canonical back to `/`.

## Top 5 quick wins

1. Verify the site in Google Search Console and Bing Webmaster Tools; submit the sitemap; add `/book`; enable IndexNow in Cloudflare.
2. Add Service + Offer ($297/mo), FAQPage and Person (Adriano) JSON-LD.
3. kit.pmuacademia.com: `<html lang="en">` → `lang="es"`, add a canonical.
4. Noindex agenda.pmuacademia.com (paid funnel) and make subdomain `/robots.txt` and `/sitemap.xml` real files or 404s (today they return the app's HTML with status 200).
5. Footer credit "Página y anuncios por PMU Academia" → pmuacademia.com on each client site (with the client's OK).

## What already works

- HTTPS everywhere behind Cloudflare, no redirect chains.
- robots.txt allows every crawler and declares the sitemap; AI search bots are not blocked.
- Unique titles (36–64 chars) and descriptions (105–160 chars), OG/Twitter cards with 1200×630 images.
- Each route ships a small pre-rendered fallback with its own title, canonical and Organization schema (good base to build on).
- Organization schema has legal name, email, phone, founder and languages.
- Real experience signals: the founder story on the homepage and real client numbers on `/resultados`. Nobody else has that data.
- Lab LCP ~1.4–2.1 s, CLS 0 on mobile emulation.

## Detail

Per-category evidence and fixes: `findings/technical.md`, `findings/content.md`, `findings/on-page.md`, `findings/schema.md`, `findings/performance.md`, `findings/geo.md`, `findings/images.md`. Structured data for reports: `audit-data.json`. PDF: `pmuacademia-seo-audit-2026-10-28.pdf`.

## Limits of this audit

- No Search Console, GA4 or CrUX access: indexation and field Core Web Vitals not measured. Run `/seo google setup` after verifying Search Console.
- PageSpeed Insights API quota was exhausted; performance figures are local Playwright lab estimates (390 px, 4× CPU slowdown), not Lighthouse.
- No keyword-volume or backlink source connected (DataForSEO, Moz, Ahrefs). Search-gap findings come from live web searches, not volume data.
- claude-seo's fetcher refuses loopback proxies by design (SSRF guard), so in the cloud workspace pages were fetched through the workspace proxy and the saved HTML was run through its parsers. On a normal machine `/seo audit https://pmuacademia.com` works directly.
