# 2026-10-29: Pre-call video v2 with an on-time / reschedule ask

**Where:** agenda-llena (`public/media/pmu-academia/`), Agenda Llena live database (PMU Academia `llamada` and `agenda` funnels), ElevenLabs flow "PMU Academia - Video antes de tu llamada"

**Done**
- Made `confirmar-llamada-v2.mp4` (95.6 s): v1 with a new 25 s scene spliced in at 1:00, right before "Ahora sí, toca el botón". Same voice (ElevenLabs "Lizardo", eleven_v4), same look (Geist, cream/blush, white cards, rose checks, dark caption pill with the spoken word highlighted).
- New narration: "Una cosa más antes de confirmar. Tú sabes lo que se siente cuando una clienta agenda su cita, y luego llega tarde, o no llega, y ni te avisa. Ese espacio ya no se lo puedes dar a nadie más. Este tiempo lo aparto solo para ti, y hay otras artistas esperando un espacio. Así que te pido lo mismo que tú le pides a tus clientas: llega a tiempo, y si se te complica, avísame y lo cambiamos sin problema."
- Visuals: "Una cosa más" with a sample no-show appointment (Agendada → Llegó tarde → No llegó → Espacio perdido), then "Tu llamada" (30 min, apartada solo para ti, otras artistas esperando), then "Te pido lo mismo" with three checks.
- Pushed the file (commit 0ffbe29), checked it loads on app.pmuacademia.com, then pointed both funnels' `content.prevideo` at v2 with `durationSec` 95.6. Watch links now serve v2; the confirm button unlocks at 92 s.

**Decided**
- Adriano asked for the video to call out people who book and don't show or warn him. Wrote it as "you know how it feels when your own clients do this" instead of scolding, since she hasn't met him yet.
- v1 stays in `public/media` so it can be switched back by changing the funnel's `prevideo.url`.

**Open / next**
- Poster is still `confirmar-llamada-v1.jpg` (same first frame, so it's fine).
