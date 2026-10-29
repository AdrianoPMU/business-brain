"""Lab performance on a mid-range mobile profile (4x CPU slowdown, Fast 4G-ish),
plus rendered text extraction and the ?lang=en check. Usage: perf_check.py OUT URL..."""
import json, os, sys
from playwright.sync_api import sync_playwright

out = sys.argv[1]
urls = sys.argv[2:]
PROXY = os.environ.get("HTTPS_PROXY")
MOBILE_UA = ("Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 "
             "(KHTML, like Gecko) Chrome/130.0 Mobile Safari/537.36")
OBS = """
window.__lcp=0; window.__cls=0;
new PerformanceObserver(l=>{for(const e of l.getEntries()) window.__lcp=e.startTime}).observe({type:'largest-contentful-paint',buffered:true});
new PerformanceObserver(l=>{for(const e of l.getEntries()) if(!e.hadRecentInput) window.__cls+=e.value}).observe({type:'layout-shift',buffered:true});
"""
res = []
with sync_playwright() as pw:
    br = pw.chromium.launch(proxy={"server": PROXY} if PROXY else None)
    for u in urls:
        ctx = br.new_context(user_agent=MOBILE_UA, viewport={"width": 390, "height": 844},
                             device_scale_factor=2, is_mobile=True, has_touch=True)
        ctx.add_init_script(OBS)
        pg = ctx.new_page()
        cdp = ctx.new_cdp_session(pg)
        cdp.send("Emulation.setCPUThrottlingRate", {"rate": 4})
        cdp.send("Network.enable")
        cdp.send("Network.emulateNetworkConditions", {"offline": False, "latency": 150,
                 "downloadThroughput": 1.6e6 / 8 * 1024 / 1000 * 1000 / 1, "uploadThroughput": 750e3 / 8})
        bytes_by_type = {}
        def on_resp(r):
            try:
                t = r.request.resource_type
                b = len(r.body()) if r.status < 300 else 0
                bytes_by_type[t] = bytes_by_type.get(t, 0) + b
            except Exception:
                pass
        pg.on("response", on_resp)
        pg.goto(u, wait_until="load", timeout=90000)
        pg.wait_for_timeout(4000)
        m = pg.evaluate("""() => { const n=performance.getEntriesByType('navigation')[0];
            const fcp=performance.getEntriesByName('first-contentful-paint')[0];
            return {ttfb:n.responseStart, fcp: fcp?fcp.startTime:null, dcl:n.domContentLoadedEventEnd,
                    load:n.loadEventEnd, lcp: window.__lcp, cls: window.__cls,
                    lang: document.documentElement.lang, h1: [...document.querySelectorAll('h1')].map(h=>h.innerText).join(' | '),
                    text: document.body.innerText}}""")
        slug = u.replace("https://", "").replace("/", "_").replace("?", "_")
        open(f"{out}/{slug}.text.txt", "w").write(m.pop("text"))
        pg.screenshot(path=f"{out}/{slug}.mobile.png")
        m.update(url=u, kb={k: round(v / 1024) for k, v in bytes_by_type.items()})
        res.append(m)
        print(json.dumps({k: (round(v) if isinstance(v, float) and k != 'cls' else v) for k, v in m.items()}, ensure_ascii=False))
        ctx.close()
    br.close()
json.dump(res, open(f"{out}/perf.json", "w"), indent=1, ensure_ascii=False)
