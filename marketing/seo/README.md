# SEO and AI search ("omnipresent")

Goal: when a Spanish-speaking PMU artist in the US searches Google, asks ChatGPT, Perplexity or Gemini, or watches YouTube about getting more clients, PMU Academia shows up.

## Where things stand (audit 2026-10-28)

Health score **55/100**. Full report: `audits/2026-10-28/` (start with `FULL-AUDIT-REPORT.md`, plan in `ACTION-PLAN.md`, PDF for humans).

- ~~The main site (Lovable) builds its text with JavaScript, so bots that don't run JS see 30–64 words per page.~~ Fixed 2026-10-29: pages are pre-rendered (see below).
- **Re-checked 2026-10-29 (measured, not assumed):** the homepage serves 68 words to a normal browser *and* to Googlebot, bingbot, GPTBot, OAI-SearchBot and PerplexityBot user agents. Raw HTML is 5.7 KB, one JSON-LD block, `?lang=en` returns the Spanish page with its own hreflang, and `sitemap.xml` lists only `/`, `/resultados`, `/privacidad`, `/terminos` (no `/book`). Lovable's docs say published apps pre-render for *verified* crawlers, and verification is almost certainly by IP, so a spoofed user agent cannot prove or disprove it. Check Search Console's crawled HTML or Lovable's SEO scan before spending money on pre-rendering.
- Only 4 indexable pages, all sales or legal. Nothing ranks except the brand name.
- "PMU Academia" searches return a Saudi university and a UK academy, not us.
- No off-site mentions yet; schema `sameAs` lists only Instagram.
- The Spanish niche (US-based PMU artists asking business questions) has no one answering it.

## Week 1 technical fixes (published 2026-10-29)

- **Pre-rendering is live.** The Lovable build (`vite.config.ts`, plugin `static-share-pages` → `prerenderPages`) renders `/`, `/book`, `/resultados`, `/privacidad`, `/terminos` and `/masterclass` with `src/entry-server.tsx` and writes the full markup into each page's static HTML. Bots that don't run JavaScript now read 635 words on the homepage (was 68), 647 on `/book` (was 32), 493 on `/resultados` (was 40). The browser hydrates that markup. New public pages must be added to `prerenderedRoutes` and to `public/sitemap.xml`; the Lovable project's `AGENTS.md` has the rules.
- **Schema:** Organization (sameAs Instagram + Facebook Page 602734749594350), WebSite, Person (Adriano), Service "Sistema Agenda Llena" with a $297/month Offer, and FAQPage on the homepage generated from the `faqs` array in `FAQSection.tsx`.
- **hreflang removed** (it pointed English at `?lang=en`, which served Spanish). Add it back only when English gets its own URL.
- **Sitemap** now lists `/`, `/book`, `/resultados`, `/privacidad`, `/terminos`; resubmitted to Search Console.
- **Bing Webmaster Tools:** Adriano imported the site from Search Console on 2026-10-29.
- **IndexNow:** key file `https://pmuacademia.com/834a5fcaf1e720f49126a45d91bc01d2.txt`. After publishing changes, POST the changed URLs to `https://api.indexnow.org/indexnow` with that key (the request is in `work-logs/2026-10-29-seo-prerender-live.md`).
- **llms.txt** at `https://pmuacademia.com/llms.txt` (summary, key facts, main pages). Keep its price in sync with the homepage.
- **Checking a deploy:** `tools/browser_check.mjs` serves a built `dist/` the way Lovable hosting does and opens every route in headless Chromium, reporting word counts, hydration errors and calendar loads. Chromium comes from the npm package `@sparticuz/chromium` (the normal Playwright download is blocked in cloud sessions).

## The plan, in order

1. **Week 1:** ~~pre-render every page, verify Google Search Console + Bing Webmaster Tools, sitemap + IndexNow, Service/FAQPage/Person schema, fix `?lang=en` hreflang~~ (done 2026-10-29). Still open: clean up subdomains (agenda., app.).
2. **Weeks 2–3:** one name everywhere ("PMU Academia USA" + "Sistema Agenda Llena"), `/nosotros`, data-style `/resultados`, Facebook/YouTube/LinkedIn profiles, footer credit on every client site.
3. **Month 2+:** ~~`/guias/` hub~~ (live 2026-10-30 with 5 guides; see "Guides" below), 2 Spanish articles a week from the content map in `ACTION-PLAN.md`, each turned into a YouTube video and Shorts.
4. **Ongoing:** monthly audit, drift checks after deploys, monthly AI spot check.

Keyword Planner data and the article priorities it suggests: `keywords/README.md` (pulled 2026-10-29 through DataForSEO).

Article drafts live in `content/`, named by their order in the content map. Drafts are written before they are published, with the numbers behind them cited and a "NO PUBLICAR" block at the bottom holding what still needs checking.

## Guides (`/guias`)

**Status:** live since 2026-10-30 (Lovable commit `b0d0a19`, published). Sent to IndexNow and the sitemap resubmitted in Search Console the same day.

| # | Guide | URL |
|---|---|---|
| 1 | Cuánto cuesta una clienta de cejas con anuncios | `/guias/cuanto-cuesta-clienta-cejas-anuncios` |
| 2 | Licencia de micropigmentación por estado (17 states) | `/guias/licencia-micropigmentacion-por-estado` |
| 3 | Consentimiento informado + plantilla | `/guias/consentimiento-informado-micropigmentacion` |
| 4 | Cómo elegir un curso | `/guias/como-elegir-curso-micropigmentacion` |
| 5 | Ideas de marketing y promociones | `/guias/ideas-marketing-micropigmentadoras` |

Guides 2–5 were each checked against official sources by a separate agent on 2026-10-30, and the corrections are in.

**Pipeline**
1. Write or edit the Markdown in `content/NN-slug.md`. Front matter holds slug, titles, pillar, dates and reading time. `## Preguntas frecuentes` with `**Pregunta?**` lines becomes FAQPage schema. Everything from `<!-- NO PUBLICAR` down stays out of the page.
2. `python3 tools/build_guides.py <site_repo>` (no filter, so `guias.json` lists every guide) writes `src/content/guias/<slug>.html` and `guias.json`. Runs of 3+ underscores become fill-in lines; `<div markdown="1">` blocks work (the consent template uses one).
3. The site (`src/pages/guias/`) loads the bodies with `import.meta.glob("?raw")` and pre-renders `/guias` and every guide, with Article + BreadcrumbList + FAQPage JSON-LD. A new guide also needs its URL in `public/sitemap.xml` and `public/llms.txt`; `src/test/seo.test.ts` checks the rest.
4. Getting files into Lovable byte-for-byte: `get_file_upload_url` for each file, `PUT` the file with curl (send the returned headers), then `send_message` with the file ids attached (**max 10 files per message**) asking the agent to `cp` from the uploads and `cmp` them. This beats pasting file contents into the message.

**Decisions (Adriano, 2026-10-30)**
- No Lexxi or masterclass recommendation in the guides. If one is ever added, it has to say she's his wife and that PMU Academia runs her ads (FTC).
- Guide 5 has no section on reviews: Agenda Llena's $5 review rewards would contradict it. Write about reviews only after that feature is settled.
- The consent template is approved as is.

**Open**
- Meta changed its health and wellness ad policy on 2026-07-23; the change isn't confirmed yet (guide 5).
- Check indexing in Search Console around 2026-11-06.
- Possible next step: a printable PDF of the consent template as a lead magnet.

## Google Search Console (connected 2026-10-29)

- Property: `sc-domain:pmuacademia.com` (domain property, covers every subdomain). Adriano's Google account is Owner.
- Claude reaches it through **Composio** (toolkit `google_search_console`, account alias `pmu-academia`): list sites, search analytics, URL inspection, sitemaps. Use `site_url = "sc-domain:pmuacademia.com"` exactly.
- claude-seo's own `/seo google` needs a Google Cloud service account, which is **not** set up. Pull GSC data through Composio instead.
- `https://pmuacademia.com/sitemap.xml` submitted 2026-10-29.
- DNS for pmuacademia.com is managed in **GoHighLevel** (nameservers braden/love.ns.cloudflare.com belong to GHL). The pmuacademia.com zone in our own Cloudflare account is pending and not live. DNS changes for this domain go in GHL.

**Baseline (pulled 2026-10-29, last 90 days):**

| Page | Google status |
|---|---|
| `https://pmuacademia.com/` | Submitted and indexed, last crawled 2026-10-27 |
| `/resultados`, `/book` | URL is unknown to Google |
| `kit.pmuacademia.com`, `agenda.pmuacademia.com` | URL is unknown to Google |

Search: 5 impressions, 0 clicks, average position 15. The only visible query was "academia pmu" (1 impression, position 13); the rest are hidden by Google for privacy.

**Open check:** in Search Console, URL Inspection → `https://pmuacademia.com/` → View crawled page → HTML. If Googlebot got the full page (FAQ, price, story), Lovable is pre-rendering for Google and the week 1 pre-render job only matters for AI bots. If it got ~68 words, pre-rendering is needed for Google too.

## The tool: claude-seo

[AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) (MIT, v2.5.0). 26 skills and 19 agents behind `/seo` commands.

**Install**
- Claude Code on your computer: open this repo and trust the folder. `.claude/settings.json` registers the plugin. If no prompt appears, run `claude plugin install claude-seo@agricidaniel-claude-seo --scope project`, then `/seo setup`.
- Cloud sessions (claude.ai, scheduled tasks): they don't load plugins from repo settings. Run `bash scripts/install-seo.sh` once per session.

**Commands we use**

| When | Command |
|---|---|
| Monthly | `/seo audit https://pmuacademia.com` → save to `audits/YYYY-MM-DD/` |
| Right now, then after every site deploy | `/seo drift baseline https://pmuacademia.com`, then `/seo drift compare https://pmuacademia.com` |
| Before writing an article | `/seo content-brief "<Spanish topic>"` |
| Before publishing an article | `/seo page <url>` and `/seo geo <url>` |
| Planning a topic cluster | `/seo cluster "<seed keyword>"` |
| Schema changes | `/seo schema https://pmuacademia.com` |
| Clicks, queries, indexation | Composio Search Console tools (see section above); `/seo google` only after a service account is set up |

**Cloud-session quirk:** claude-seo's fetcher refuses the workspace's local proxy on purpose (it's an SSRF guard). Don't patch that. Instead fetch pages with `tools/fetch_site.py` (raw + rendered HTML, robots, sitemap) and `tools/perf_check.py` (mobile lab timings), then run the tool's parsers on the saved files, e.g. `"$HOME/.claude/skills/seo/scripts/claude-seo" run parse_html.py page.rendered.html --url <url> --json`. Run both scripts with the tool's own Python: `PLAYWRIGHT_BROWSERS_PATH=$HOME/.claude/skills/seo/ms-playwright $HOME/.claude/skills/seo/.venv/bin/python -I tools/fetch_site.py <out_dir> <url>...`

## Monthly AI spot check

Ask each question in ChatGPT, Perplexity, Gemini and Google AI Mode. Log in the month's audit folder whether PMU Academia is named or linked.

1. ¿Cómo consigo más clientas de micropigmentación en Estados Unidos?
2. ¿Qué agencia de marketing ayuda a micropigmentadoras latinas en Estados Unidos?
3. ¿Cuánto cuesta conseguir una clienta de cejas con anuncios de Facebook?
4. ¿Cómo hago anuncios de Facebook para mi negocio de micropigmentación?
5. ¿Cuánto debo cobrar por cejas ombré en Estados Unidos?
6. ¿Cómo cobro depósito para citas de micropigmentación?
7. ¿Qué contesto cuando una clienta pregunta el precio por mensaje?
8. ¿Hay una app para agendar citas de micropigmentación en español?
9. Marketing agency for Spanish-speaking permanent makeup artists
10. ¿Qué es PMU Academia?

## KPIs

| Metric | Baseline (Oct 2026) | 3 months | 6 months | 12 months |
|---|---|---|---|---|
| Health score | 55 | 75 | 85 | 90 |
| Indexed pages (GSC) | 1 | 20 | 45 | 90 |
| Brand search shows pmuacademia.com first | No | Yes | Yes | Yes |
| Organic clicks / month (GSC) | 0 (5 impressions in 90 days) | 100 | 500 | 2,000 |
| Spot-check questions citing us (of 10) | 0 | 1 | 3 | 6 |
| Booked calls from organic + AI / month | 0 | 2 | 6 | 15 |
