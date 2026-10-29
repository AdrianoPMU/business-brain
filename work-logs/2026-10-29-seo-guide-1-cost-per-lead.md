# 2026-10-29: Guide 1 drafted, and a measurement that questions the top priority

**Where:** business-brain, `marketing/seo/`

**Done**
- Wrote the first `/guias/` article in full Spanish: `content/01-cuanto-cuesta-clienta-cejas-anuncios.md`. 1,265 words before the internal notes. Answer in the first two sentences, the numbers table directly under it, question-style H2s, a weekly checklist, and five FAQ questions ready to become FAQPage schema. Byline and a 90-day refresh note included.
- Every figure in it is checked against the handoff table (29 Sep – 28 Oct 2026): 199 people interested, $2,081 spend, $10.46 each. Recomputed each row so a reader dividing the displayed numbers gets the same answer (the handoff had $11.33, $13.04, $13.47, $17.50; the table now shows $11.32, $13.00, $13.46, $17.49). Yoly's $2,382 over 6 deposits is $87.50 a deposit and 4.54x on $525.
- Measured the live site instead of trusting the audit's wording: homepage raw HTML is 5.7 KB and 68 words; `/book` 32; `/resultados` 40. `sitemap.xml` is missing `/book`. `?lang=en` returns the same 68-word Spanish page but declares its own hreflang. All five crawler user agents tested (Googlebot, bingbot, GPTBot, OAI-SearchBot, PerplexityBot) get the same 68 words as a browser.

**Decided**
- The article runs on aggregates plus "Estudio A–E", with no client named, so it can publish before every client gives consent. The named version waits for the OKs.
- C1 (pre-render) is now an open question, not a settled task. Lovable's own docs say published apps pre-render for *verified* crawlers, which is almost certainly IP-checked, so a spoofed user agent can't prove anything. Settle it with Search Console's crawled HTML or Lovable's SEO scan before paying for a rebuild.

**Open / next**
- Confirm the client names before the table can name studios (Jami, Yoly, Cocora, Genluxe, Lexxi).
- Lexxi's "$900 / 2 citas" still has only one $76.95 deposit paid in the app. The article says "citas", not "depósitos cobrados", until that is confirmed.
- Refresh the Meta numbers immediately before publishing; they are a month old and move weekly.
- Still nobody has seen what Google actually receives on pmuacademia.com. That one check decides whether `/guias/` articles will be readable at all once published on the same Lovable app.
- Next article in the map, or the `/resultados` rewrite that reuses this table, both ready to start.
