# 2026-10-30: Aglahel's site text, real hours, and ads with Lexxi's photos

**Where:** agenda-llena (commits d6ccfb0, 9152cde), Supabase, client Aglahel Ramos

**Done**
- New About text on her website (`sitio`) and voucher funnel (`ombre`), ES + EN, written from the bio she sent over WhatsApp. Title is now "Hola, soy Aglahel Ramos" / "Hi, I'm Aglahel Ramos".
- Her real hours saved to `workspaces.schedule` (it was empty, so the site showed the Mon–Sat 10–6 placeholder): Tue 10–5, Wed 10–7, Thu 10–7, Fri 10–2, closed Sat, Sun and Mon. Procedure start times stay 10 AM and 2 PM, so Friday only offers 10 AM.
- About text on client sites and funnel pages now keeps line breaks (`white-space: pre-line`), so multi-paragraph bios show as paragraphs. Applies to every client.
- Rebuilt both green-screen voucher ads (ES 29s, EN 28s) with Lexxi's best Ombré Powder photos in the results reel instead of Aglahel's. Same presenter takes from Zuops (jobs c9fbc0d4 ES, 03782960 EN), same pills and audio. Lexxi's watermark labels cropped off.
- Swapped the new ads into app.pmuacademia.com/revision/aglahel-ramos/ and changed its chip from "Con tus fotos reales" to "Fotos de muestra por ahora".

**Decided**
- Adriano chose to run Lexxi's photos in Aglahel's ads for now with no on-screen tag, until Aglahel has stronger results of her own.

**Open / next**
- Swap her own best healed results back in once she has them.
- Still missing: exact address, original photos without text.
- Tip for the scripts: a `pgrep -f greenscreen.py` wait loop matches its own shell command and never ends; wait on the output files or the process ID instead.
