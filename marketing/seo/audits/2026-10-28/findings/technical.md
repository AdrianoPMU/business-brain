# Technical SEO — pmuacademia.com

Score: **60/100** (weight 22%) · Audit date: 2026-10-28

## What works

- HTTPS on every host, behind Cloudflare; no redirect chains.
- robots.txt allows all crawlers (including OAI-SearchBot, Claude-SearchBot, PerplexityBot and Googlebot) and declares the sitemap.
- Self-referencing canonicals on /, /resultados, /book, /ejemplo.
- Each route ships a small pre-rendered fallback with its own title, description, canonical and Organization schema.
- /ejemplo (demo site) and the booking app page are correctly noindex.

## Findings

### [High] Content is client-side rendered; raw HTML is thin

**Evidence:** Raw HTML word counts vs rendered: home 64 vs 597, /resultados 36 vs 472, /book 30 vs 615, /ejemplo 24 vs 298. Googlebot renders JavaScript, but GPTBot/OAI-SearchBot and PerplexityBot generally read raw HTML only, so the FAQ, pricing, founder story and results never reach them. The fallback H1 also differs from the rendered H1 on 3 pages.

**Fix:** Pre-render every public route to static HTML at build time (vite-plugin-prerender / react-snap style, or move the marketing pages to Cloudflare Pages like the client sites), so raw HTML equals what visitors see.

### [Medium] hreflang 'en' contradicted by canonical

**Evidence:** hreflang en points to https://pmuacademia.com/?lang=en, but that URL returns identical Spanish HTML whose canonical is https://pmuacademia.com/. English text only appears after JavaScript runs.

**Fix:** Either give English its own pre-rendered path (/en/) with its own canonical and reciprocal hreflang, or remove the hreflang tags until then.

### [Medium] Sitemap covers 4 URLs and omits /book

**Evidence:** sitemap.xml lists /, /resultados, /privacidad, /terminos. /book is indexable and canonical but missing. No sitemaps exist for kit.

**Fix:** Add /book (and every new content page) to the sitemap with real lastmod dates; submit in Search Console and Bing Webmaster Tools; turn on IndexNow via Cloudflare.

### [Medium] Subdomains return HTML 200 for robots.txt, sitemap.xml and llms.txt

**Evidence:** agenda.pmuacademia.com and app.pmuacademia.com answer every unknown path with the app shell (status 200, text/html). Crawlers read this as an invalid robots.txt and a soft-404 sitemap.

**Fix:** Serve a real robots.txt on each subdomain (agenda: Disallow all or noindex pages; app: Disallow private routes) and return 404 for unknown paths.

### [Low] Ad funnel subdomain is indexable with no canonical

**Evidence:** agenda.pmuacademia.com has no canonical and no robots meta, two H1s, and competes with the homepage for the same offer.

**Fix:** Add <meta name='robots' content='noindex'> to the agenda funnel; keep paid traffic pages out of the index.

### [Low] No HSTS or security headers

**Evidence:** No Strict-Transport-Security or Content-Security-Policy headers on any host.

**Fix:** Enable HSTS in Cloudflare (SSL/TLS > Edge Certificates).
