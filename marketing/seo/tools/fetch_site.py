"""Fetch raw + rendered HTML for a small crawl of PMU Academia pages through the
workspace proxy, saving files for the claude-seo analyzers (which refuse local
proxies by design). Usage: fetch_site.py OUT_DIR URL [URL...]"""
import json, os, sys, re, time
from urllib.parse import urljoin, urlparse
import requests
from playwright.sync_api import sync_playwright

out = sys.argv[1]
seeds = sys.argv[2:]
os.makedirs(out, exist_ok=True)
CA = "/root/.ccr/ca-bundle.crt"
PROXY = os.environ.get("HTTPS_PROXY")
UA = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
BROWSER_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/130.0 Safari/537.36")
ALLOWED = {"pmuacademia.com", "www.pmuacademia.com", "agenda.pmuacademia.com",
           "kit.pmuacademia.com", "app.pmuacademia.com"}
MAX = 40

def slug(u):
    p = urlparse(u)
    s = (p.netloc + p.path).rstrip("/").replace("/", "_") or p.netloc
    return re.sub(r"[^A-Za-z0-9._-]", "-", s)

index = []
seen, queue = set(), list(seeds)
with sync_playwright() as pw:
    br = pw.chromium.launch(proxy={"server": PROXY} if PROXY else None,
                            args=["--ignore-certificate-errors-spki-list"])
    ctx = br.new_context(user_agent=BROWSER_UA, ignore_https_errors=False,
                         viewport={"width": 1280, "height": 900})
    while queue and len(seen) < MAX:
        u = queue.pop(0).split("#")[0]
        if u in seen:
            continue
        seen.add(u)
        rec = {"url": u, "slug": slug(u)}
        try:
            r = requests.get(u, headers={"User-Agent": UA}, timeout=30,
                             verify=CA, allow_redirects=True)
            rec.update(status=r.status_code, final_url=r.url,
                       redirects=[h.url for h in r.history],
                       headers=dict(r.headers), raw_len=len(r.text))
            open(f"{out}/{rec['slug']}.raw.html", "w").write(r.text)
        except Exception as e:
            rec["raw_error"] = str(e)
        try:
            pg = ctx.new_page()
            t0 = time.time()
            resp = pg.goto(u, wait_until="networkidle", timeout=45000)
            pg.wait_for_timeout(1500)
            html = pg.content()
            rec.update(render_status=resp.status if resp else None,
                       render_ms=int((time.time() - t0) * 1000),
                       rendered_len=len(html), title=pg.title())
            open(f"{out}/{rec['slug']}.rendered.html", "w").write(html)
            try:
                pg.screenshot(path=f"{out}/{rec['slug']}.png", full_page=False)
            except Exception:
                pass
            links = pg.eval_on_selector_all("a[href]", "els => els.map(e => e.href)")
            rec["links"] = sorted(set(links))
            for l in links:
                p = urlparse(l)
                if p.scheme in ("http", "https") and p.netloc in ALLOWED:
                    clean = l.split("#")[0].split("?")[0]
                    if clean not in seen and clean not in queue:
                        queue.append(clean)
            pg.close()
        except Exception as e:
            rec["render_error"] = str(e)[:300]
        index.append(rec)
        print(u, rec.get("status"), rec.get("render_status"), rec.get("title"), flush=True)
    br.close()

for path in ["/robots.txt", "/sitemap.xml", "/llms.txt", "/.well-known/ai-catalog.json"]:
    for host in ["pmuacademia.com", "agenda.pmuacademia.com", "app.pmuacademia.com"]:
        u = f"https://{host}{path}"
        try:
            r = requests.get(u, headers={"User-Agent": UA}, timeout=20, verify=CA)
            ct = r.headers.get("content-type", "")
            fn = f"{out}/{host}{path.replace('/', '_')}"
            open(fn, "w").write(r.text)
            index.append({"url": u, "status": r.status_code, "content_type": ct,
                          "len": len(r.text), "file": fn})
            print(u, r.status_code, ct, len(r.text))
        except Exception as e:
            print(u, "ERR", e)

json.dump(index, open(f"{out}/index.json", "w"), indent=1)
