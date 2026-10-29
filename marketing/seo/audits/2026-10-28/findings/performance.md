# Performance (CWV) — pmuacademia.com

Score: **75/100** (weight 10%) · Audit date: 2026-10-28

## What works

- Lab LCP about 1.4-2.1 s and CLS 0 on the main site (mobile emulation, 4x CPU slowdown).

## Findings

### [Medium] 2.9 MB of JavaScript for a 4-page marketing site

**Evidence:** Main site loads ~2.9 MB of uncompressed JS; the agenda funnel loads ~4.1 MB JS + 0.9 MB CSS and took ~15 s to finish loading; kit has 1.35 s server response and 1.7 MB of images.

**Fix:** Pre-rendering (Technical finding 1) removes most of this; compress kit images to WebP and size them for mobile.
