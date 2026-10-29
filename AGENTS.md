# PMU Academia: Business Brain

Read this file first, every session. Then read the README in whatever folder you're working in, and the last 7 days of `work-logs/`.

## What this business does

PMU Academia is a done-for-you growth system for Spanish-speaking permanent makeup (PMU) artists in the US. It's the brand (DBA) of Academia Growth LLC, a single-member Ohio LLC owned by Adriano Rodriguez.

We sell it as **Sistema Agenda Llena**: we run the artist's Meta ads, build her booking page and site, follow up with every lead by text, and get consults and appointments booked. It all runs inside the Agenda Llena app, which Adriano built to replace GoHighLevel/Zuops.

- Price: $297/month (a $1,000 setup fee is being considered, not live)
- 30-day money-back guarantee, any reason
- No free or $1 trials anymore
- Typical client ad spend: around $15–20/day, paid by the client to Meta
- Website: pmuacademia.com · Instagram: @pmuacademiausa

## Where everything lives

| Folder | What's in it |
|---|---|
| `marketing/` | How PMU Academia gets its own clients: ads, funnels, content, SEO |
| `sales/` | The sales call process, booking flow, offer and objections |
| `operations/` | Tools, stack, logins (no passwords), how the machine runs |
| `fulfillment/` | Delivering for clients: onboarding, the standard campaign, one file per client |
| `work-logs/` | One dated log per work session. This is the memory. |

Related code repos (all under github.com/AdrianoPMU):
- `agenda-llena`: the Agenda Llena app (CRM, booking, texting, AI assistant)
- `cocora-aesthetics`, `yoly-brow-studio`: client landing pages (Cloudflare Pages)
- `pmu-garantia`

## Tools agents can use here

- **claude-seo** (`/seo` commands) for SEO and AI-search audits, content briefs and schema. On a computer it's enabled through `.claude/settings.json` once you trust this folder; in cloud sessions run `bash scripts/install-seo.sh` first. How we use it: `marketing/seo/README.md`.

## How to log work

At the end of every session, add a file to `work-logs/` named:

```
YYYY-MM-DD-short-topic.md
```

Use the template in `work-logs/README.md`. Keep it short: what got done, what got decided, what's still open.

If something about the business changed (price, offer, a tool, a client's status), also update the README where that fact lives. The log says what happened; the READMEs say how things are now.

## Rules for agents

1. Anything a lead or client reads is in Spanish, and it should sound like a real person wrote it, not a template.
2. AI texting presents as the artist's assistant and never denies being AI if someone asks.
3. Never put passwords, API keys or card numbers in this repo.
4. Don't change a client's live ads, budgets or money without Adriano saying so.
5. When you're not sure about something, check `work-logs/` before asking Adriano.
