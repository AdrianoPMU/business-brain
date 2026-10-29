# 2026-10-29: Google Search Console connected

**Done**
- Connected Google Search Console to Claude through Composio (toolkit `google_search_console`, alias `pmu-academia`).
- Added the domain property `sc-domain:pmuacademia.com`; Adriano verified it and is Owner.
- Submitted `https://pmuacademia.com/sitemap.xml`.
- Pulled the baseline: only the homepage is indexed (last crawl 2026-10-27); `/resultados`, `/book`, kit. and agenda. are unknown to Google. 5 impressions, 0 clicks, average position 15 over the last 90 days.
- Found that pmuacademia.com's DNS is run by GoHighLevel, not our Cloudflare (that zone is pending). Noted in `operations/README.md`.

**Decided**
- GSC data comes through Composio. No Google Cloud service account for claude-seo's `/seo google` for now.

**Open / next**
- Check Search Console's crawled HTML for the homepage to see whether Googlebot gets the full pre-rendered page. That decides whether the week 1 pre-render job is needed for Google or only for AI bots.
- Bing Webmaster Tools: import the site from Search Console.
- Add `/book` to the sitemap, then resubmit.
