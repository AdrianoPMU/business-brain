# AI Search Readiness — pmuacademia.com

Score: **30/100** (weight 10%) · Audit date: 2026-10-28

## What works

- All AI search crawlers are allowed in robots.txt.
- Homepage fallback paragraph is a clean, quotable definition of what PMU Academia is.

## Findings

### [High] Brand entity is invisible and ambiguous

**Evidence:** Searches for 'PMU Academia' and site:pmuacademia.com returned Prince Mohammad Bin Fahd University (PMU) and The PMU Academy Essex; nothing from pmuacademia.com.

**Fix:** Use one consistent name everywhere ('PMU Academia USA' + 'Sistema Agenda Llena'), get indexed via Search Console/Bing, and build third-party mentions.

### [High] No off-site brand mentions

**Evidence:** No YouTube channel, Facebook page, LinkedIn, podcast, directory or press mention found. Third-party studies find brand mentions (YouTube strongest) correlate with AI citations far more than backlinks.

**Fix:** YouTube channel in Spanish, client-site footer credits, LinkedIn for Adriano, guest spots on Spanish PMU podcasts and Facebook groups.

### [Info] No llms.txt (informational)

**Evidence:** /llms.txt returns 404. Google says it does not help Search; it carries no weight in this score.

**Fix:** Optional: add a short llms.txt once the content hub exists. Do not prioritize it.
