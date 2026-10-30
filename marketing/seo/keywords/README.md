# Keyword research

Source: Google Ads Keyword Planner data pulled through DataForSEO (Composio, "keywords for keywords", US). About $0.09 per batch of up to 20 seed keywords.

`2026-10-29-keyword-planner.csv` has the artist-side keywords with volume, plus the top 60 client-side keywords per language. Columns: lang (`es` = people using Google in Spanish, so English words like "microblading" appear too), side (`artist` = business questions an artist asks, `client` = someone looking for the service), monthly US searches, CPC, competition. Small volumes are rounded buckets: 10 means roughly 0–10.

## What the 2026-10-29 pull says

- **Spanish artist-side Google searches are tiny.** "como conseguir clientes en facebook", "publicidad para salon de belleza" and "consentimiento informado micropigmentacion" are each about 10 a month. Spanish-speaking artists ask these questions in Facebook groups, YouTube and ChatGPT, not Google. So PMU Academia's articles are mainly for AI answers and YouTube, with Google as a bonus.
- **The one real Spanish artist-side topic is courses:** "curso de microblading" 90, "curso de micropigmentacion" 50, plus about 60 variants at ~10 each (labios, online, New York, New Jersey). That fits Lexxi's 1-a-1 masterclass.
- **English artist-side demand is in licensing, certification, consent forms and salon marketing:** "permanent makeup license" 170 (plus "cosmetic tattoo license" 170 and "permanent cosmetics license" 170, likely the same searches), "permanent makeup certification" 140, "permanent makeup consent form" 50 + "pmu consent form" 40, "marketing for beauty salon" 320, "beauty salon promotion ideas" 110. "pmu marketing" and "how to get pmu clients" are 10–20.
- **Client-side volume is large:** "micropigmentacion de cejas" 1,900, "microblading cerca de mí" 1,000, "micropigmentacion de labios" 1,000; English "microblading cost" variants 4,400, "eyebrow tattoo cost" 1,600. That's what clients' own sites should target (price pages, "cerca de mí"), not pmuacademia.com.

## Article priorities from this data (Spanish, for artists)

1. Licencia de micropigmentación por estado en EE. UU. (English demand, no one answering in Spanish)
2. Consentimiento informado para micropigmentación: plantilla en español (downloadable, doubles as a lead magnet)
3. Cómo elegir un curso de micropigmentación en Estados Unidos (links to Lexxi's masterclass)
4. Ideas de marketing y promociones para micropigmentadoras
5. Keep `content/01-cuanto-cuesta-clienta-cejas-anuncios.md`: almost no Google volume, but it's original data, which is what AI answers quote.

## Search Console's role

Search Console only shows searches where pmuacademia.com already appears (24 impressions since July as of 2026-10-29). Once articles are live, pull its queries monthly to see which searches each article actually shows up for, then add those words to the article or write the next one around them.
