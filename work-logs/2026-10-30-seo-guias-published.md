# 2026-10-30: /guias published, with two sections removed

**Where:** pmuacademia.com (Lovable project "PMU Offer Launch", commit `b0d0a19`, published), Search Console, IndexNow, business-brain

**Done**
- Removed the Lexxi / masterclass section and its notes from guide 4 (course guide).
- Removed everything about reviews from guide 5 (marketing guide):
  - the Google and Yelp reviews section
  - its table rows and two FAQs
  - the "no raffle for reviews" bullet and the line about referrals vs reviews
  - the review sources (Google review policy, Yelp, FTC 16 CFR 465, BrightLocal, Zenoti)

  Guide 5 now has 9 ideas.
- Changed the guide 5 description in `llms.txt` and `guias.json` from "reseñas" to "depósitos".
- Rebuilt, tested (14 pass) and ran a browser check. Sent the 4 changed files to Lovable; the hashes match.
- Published. Checked live as Googlebot: all 6 pages return 200 with full text, canonical and FAQ schema. Word counts: hub 294, cuánto cuesta 1,273, licencias 3,577, consentimiento 2,838, curso 2,406, ideas 2,111. There's no Lexxi section and no Yelp text on the live pages. The sitemap lists 11 URLs.
- IndexNow (api.indexnow.org, Bing, Yandex): 200 for the 6 guide URLs plus `sitemap.xml` and `llms.txt`. Resubmitted the sitemap in Search Console.

**Decided**
- Adriano: take out the Lexxi recommendation and the reviews section, and the consent template is good to go.
- The Agenda Llena review rewards feature stays as is (Adriano chose to change the guide, not the app).

**Open / next**
- Check Search Console indexing for the 6 `/guias` URLs around 2026-11-06.
- Possible next step: a printable PDF of the consent template as a lead magnet.
- Still open from 10-29: homepage copy (does the $500 cover month 1? does Sofía answer in English?), the /start checkout missing the $500, and the llms.txt price.
