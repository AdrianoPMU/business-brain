# Operations

The tools and accounts that keep everything running. No passwords or keys in here, ever.

## Stack

| Tool | Used for |
|---|---|
| **Agenda Llena app** (repo `agenda-llena`) | CRM, leads, inbox, texting, booking, AI assistant, agency dashboard. Replaces Zuops and GoHighLevel. Login at app.pmuacademia.com |
| **Twilio** | Texting and calling. One approved A2P 10DLC campaign; client numbers are bought in the app and go on PMU Academia's campaign |
| **Resend** | Email from the app |
| **Meta Business Manager** | All client Pages and ad accounts connect through Adriano's BM |
| **Cloudflare** | Client domains and landing pages (Cloudflare Pages) |
| **GitHub** (AdrianoPMU) | App code, client sites, this brain |
| **Stripe** | PMU Academia billing; artists connect their own Stripe or Square |
| **PostHog** | Funnel analytics and booking-page split tests |
| **Lovable** | Older sites (pmuacademia.com, early client pages); being phased out |
| **GoHighLevel** | Only the pmuacademia.com domain and its DNS (bought through GHL). DNS changes for pmuacademia.com go here, not Cloudflare; the pmuacademia.com zone in our Cloudflare account is pending and not live |
| **Gemini API** (Omni 1.1 Flash) | AI presenter videos for ads, the same model behind Zuops Motion. Used when Zuops is out of credits. Adriano gives his key for the session; it never goes in a repo. How: `scripts/greenscreen-ad/README.md` |
| **Google Search Console** | pmuacademia.com search data. Adriano is Owner; Claude reads it through Composio. See `marketing/seo/README.md` |

## Status of the Zuops move

Zuops is no longer used for new work. Remaining clients are being moved into the Agenda Llena app (Yoly Brow Studio's leads and notes are moving now).

## Standing rules

- Client booking calendars only allow booking up to 3 days ahead.
- All follow-up texts and emails are conversational and try to get a reply.
