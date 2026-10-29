# Schema / Structured Data — pmuacademia.com

Score: **55/100** (weight 10%) · Audit date: 2026-10-28

## What works

- Organization (legalName Academia Growth LLC, logo, email, phone, address locality, founder, knowsLanguage) and WebSite in raw HTML.

## Findings

### [Medium] Missing Service/Offer, FAQPage and Person

**Evidence:** The homepage shows a priced service and an FAQ, but no Service, Offer or FAQPage markup. Founder is a bare name with no Person @id or sameAs.

**Fix:** Add Service (provider = Organization, areaServed US, availableLanguage es) with Offer price 297 USD/month, FAQPage for the visible FAQ, and a Person entity for Adriano with sameAs.

### [Medium] sameAs lists only Instagram

**Evidence:** No Facebook page, YouTube, LinkedIn or TikTok profile in sameAs.

**Fix:** Create/claim those profiles and add them to sameAs so search engines can reconcile the entity.
