# SEO and AI search ("omnipresent")

Goal: when a Spanish-speaking PMU artist in the US searches Google, asks ChatGPT, Perplexity or Gemini, or watches YouTube about getting more clients, PMU Academia shows up.

## Where things stand (audit 2026-10-28)

Health score **55/100**. Full report: `audits/2026-10-28/` (start with `FULL-AUDIT-REPORT.md`, plan in `ACTION-PLAN.md`, PDF for humans).

- The main site (Lovable) builds its text with JavaScript, so bots that don't run JS see 30–64 words per page.
- **Re-checked 2026-10-29 (measured, not assumed):** the homepage serves 68 words to a normal browser *and* to Googlebot, bingbot, GPTBot, OAI-SearchBot and PerplexityBot user agents. Raw HTML is 5.7 KB, one JSON-LD block, `?lang=en` returns the Spanish page with its own hreflang, and `sitemap.xml` lists only `/`, `/resultados`, `/privacidad`, `/terminos` (no `/book`). Lovable's docs say published apps pre-render for *verified* crawlers, and verification is almost certainly by IP, so a spoofed user agent cannot prove or disprove it. Check Search Console's crawled HTML or Lovable's SEO scan before spending money on pre-rendering.
- Only 4 indexable pages, all sales or legal. Nothing ranks except the brand name.
- "PMU Academia" searches return a Saudi university and a UK academy, not us.
- No off-site mentions yet; schema `sameAs` lists only Instagram.
- The Spanish niche (US-based PMU artists asking business questions) has no one answering it.

## The plan, in order

1. **Week 1:** pre-render every page, verify Google Search Console + Bing Webmaster Tools, sitemap + IndexNow, Service/FAQPage/Person schema, fix `?lang=en` hreflang, clean up subdomains.
2. **Weeks 2–3:** one name everywhere ("PMU Academia USA" + "Sistema Agenda Llena"), `/nosotros`, data-style `/resultados`, Facebook/YouTube/LinkedIn profiles, footer credit on every client site.
3. **Month 2+:** `/guias/` hub, 2 Spanish articles a week from the content map in `ACTION-PLAN.md`, each turned into a YouTube video and Shorts.
4. **Ongoing:** monthly audit, drift checks after deploys, monthly AI spot check.

Article drafts live in `content/`, named by their order in the content map. Drafts are written before they are published, with the numbers behind them cited and a "NO PUBLICAR" block at the bottom holding what still needs checking.

No Google Business Profile: PMU Academia only meets clients online, which Google doesn't allow a profile for.

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
