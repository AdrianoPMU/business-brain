# 2026-10-30: /guias section with 5 guides, loaded into the Lovable preview

**Where:** business-brain `marketing/seo/`, Lovable project "PMU Offer Launch" (pmuacademia.com)

**Done**
- Wrote 4 new Spanish guides in `marketing/seo/content/`:
  - 02 licencia por estado (17 states, with a table and a section per state)
  - 03 consentimiento informado, with a full fill-in template
  - 04 cómo elegir un curso, with 2026 prices and a link to Lexxi's masterclass with a disclosure
  - 05 ideas de marketing, with the Google/Yelp/Meta/FTC/FCC rules
- Removed the duplicate "hazlo por ti" section from guide 1.
- Two separate agents fact-checked guides 2–5 against official sources, and every correction is in. Examples: Georgia's brow exception, Virginia minors, Minnesota age, California's exact FDA wording, Yelp alerts, Meta branded content, the STOP timing, Florida's 8 p.m. limit, wider course price ranges.
- `build_guides.py`: added fill-in lines for underscores and the `md_in_html` extension.
- Site code:
  - Pages: `/guias` hub and `/guias/:slug`.
  - Pre-rendered with Article + BreadcrumbList + FAQPage schema.
  - Footer links, plus sitemap and llms.txt entries.
  - The SEO test now checks the guides (14 tests pass).
  - Browser check: all 6 pages pre-render (1,100–3,300 words each) with no hydration errors.
- Loaded into Lovable (commits `c6661d6` and `e48682f`) using file uploads plus the agent's `cp`/`cmp`. The method is written up in `marketing/seo/README.md`. Lovable's agent confirmed the files match, the build and tests pass, and the preview loads. **Not published.**

**Decided**
- Adriano reviews the preview before anything is published.
- No Texas studio fee in guide 2: the two official sources disagree ($927 vs $450).

**Open / next**
- Adriano to review the preview: https://id-preview--3f904a98-8333-4bb9-b5bf-b8e1ac0c3cbe.lovable.app/guias
- Agenda Llena's review rewards conflict with guide 5's advice. This needs his decision, because it affects the app's own feature.
- He needs to OK the Lexxi disclosure ("es mi esposa"), and Lexxi needs to OK it too. Otherwise the whole section comes out.
- A lawyer should review the consent template. After that, a printable PDF download is a possible next step.
- After publishing: IndexNow ping, resubmit the sitemap in GSC, check indexing in about a week.
- Still open from 10-29: homepage copy (does the $500 cover month 1? does Sofía answer in English?), the /start checkout missing the $500, and the llms.txt price.
