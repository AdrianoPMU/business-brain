# 2026-10-29: Pre-rendering, schema and AI-search files live on pmuacademia.com

**Where:** Lovable project "PMU Offer Launch" (3f904a98…, commit e3e5f07, published), Google Search Console, IndexNow, business-brain

**Done**
- Found why only the homepage was indexed and AI tools saw nothing: the site is a React app, so crawlers that don't run JavaScript got a 30–68 word placeholder per page.
- Extended the existing `static-share-pages` Vite plugin so the build also renders each public route with a new `src/entry-server.tsx` and writes the full markup into that page's static HTML. `main.tsx` hydrates it. Routes: `/`, `/book`, `/resultados`, `/privacidad`, `/terminos`, `/masterclass`. Any render failure keeps the old placeholder, so a publish can't break over it.
- Live word counts as GPTBot sees them: homepage 635 (was 68), `/book` 647 (was 32), `/resultados` 493 (was 40), `/privacidad` 1,146, `/terminos` 729, `/masterclass` 400.
- Schema: Organization (now with Facebook Page 602734749594350 in sameAs), WebSite, Person (Adriano), Service "Sistema Agenda Llena" with a $297/month Offer, plus FAQPage on the homepage built from the visible FAQ.
- Removed the hreflang tags (English pointed at `?lang=en`, which served Spanish). Added `/book` to the sitemap. Added `llms.txt` and an IndexNow key file.
- `/book` styles: React's server renderer escapes CSS inside `<style>`, so `Book.tsx` now uses `dangerouslySetInnerHTML` for it.
- Tested before publishing: local production build, the 13 existing tests, and a headless-Chromium pass over 11 routes (no hydration errors, English toggle works, booking calendar loads once). Compared against a build of the old code: same behavior. Checked Lovable's applied files match byte for byte, published, then re-ran the browser check on the live production files: clean.
- Resubmitted `sitemap.xml` in Search Console. Sent the 5 pages + `llms.txt` to IndexNow (api.indexnow.org, Bing, Yandex all returned 202).
- Adriano imported the site into Bing Webmaster Tools.
- Lovable cost: 3.1 credits for applying the change.

IndexNow request used (resend after future publishes with the changed URLs):
```
curl -X POST https://api.indexnow.org/indexnow -H "Content-Type: application/json; charset=utf-8" \
  --data '{"host":"pmuacademia.com","key":"834a5fcaf1e720f49126a45d91bc01d2","keyLocation":"https://pmuacademia.com/834a5fcaf1e720f49126a45d91bc01d2.txt","urlList":["https://pmuacademia.com/"]}'
```

**Decided**
- Stay on Lovable for pmuacademia.com; no DNS or hosting move needed for pre-rendering.
- Pricing to show on the homepage: $500 setup + $297/month (Adriano, 2026-10-29). Homepage features to add: Sofía the AI assistant, deposit + coupon booking page, automatic review requests, video ads with an AI presenter.

**Open / next**
- Homepage copy draft sent to Adriano (draft in this session; covers hero, 6 feature cards, how-it-works steps 3–4, price box, 3 new FAQs, schema Offer and llms.txt price). Waiting on: does the $500 cover month one, and does Sofía answer in English too.
- `/start` Stripe checkout still charges only $297/month; the $500 setup isn't in Stripe.
- Subdomains (agenda., app.) still answer unknown paths with the app shell; needs real robots.txt / noindex in the agenda-llena app without blocking clients' booking sites on their own domains.
- Check Search Console in about a week: `/book` and `/resultados` should move from "unknown" to indexed.
