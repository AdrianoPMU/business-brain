// Serves dist/ the way Lovable hosting does (route folder index.html, else SPA fallback)
// and checks each page in headless Chromium: hydration errors, visible content, embeds.
import http from "node:http";
import { readFile, stat } from "node:fs/promises";
import path from "node:path";
import chromium from "@sparticuz/chromium";
import puppeteer from "puppeteer-core";

const dist = process.argv[2];
const types = { ".html": "text/html; charset=utf-8", ".js": "text/javascript", ".css": "text/css", ".txt": "text/plain", ".xml": "application/xml", ".svg": "image/svg+xml", ".png": "image/png", ".ico": "image/x-icon" };

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, "http://x");
  const clean = decodeURIComponent(url.pathname).replace(/\/+$/, "") || "/";
  const candidates = clean === "/" ? ["index.html"] : [clean.slice(1), `${clean.slice(1)}/index.html`, `${clean.slice(1)}.html`];
  for (const rel of candidates) {
    const file = path.join(dist, rel);
    try {
      if ((await stat(file)).isFile()) {
        res.writeHead(200, { "content-type": types[path.extname(file)] ?? "application/octet-stream" });
        return res.end(await readFile(file));
      }
    } catch {}
  }
  res.writeHead(200, { "content-type": types[".html"] });
  res.end(await readFile(path.join(dist, "index.html")));
});
await new Promise((r) => server.listen(4173, r));

const browser = await puppeteer.launch({ executablePath: await chromium.executablePath(), args: chromium.args, headless: true });
const routes = ["/", "/?lang=en", "/book", "/resultados", "/privacidad", "/terminos", "/masterclass", "/start", "/kit", "/gracias", "/no-existe"];
let failures = 0;

for (const route of routes) {
  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844 });
  const errors = [];
  const iframeHits = [];
  page.on("console", (m) => { if (m.type() === "error") errors.push(m.text()); });
  page.on("pageerror", (e) => errors.push(`pageerror: ${e.message}`));
  await page.setRequestInterception(true);
  page.on("request", (r) => {
    const u = r.url();
    if (u.startsWith("http://localhost:4173")) return r.continue();
    if (u.includes("crm.adrianolocal.com")) iframeHits.push(u);
    r.abort();
  });
  await page.goto(`http://localhost:4173${route}`, { waitUntil: "networkidle0", timeout: 30000 }).catch((e) => errors.push(`goto: ${e.message}`));
  await new Promise((r) => setTimeout(r, 1200));
  const info = await page.evaluate(() => ({
    title: document.title,
    h1: document.querySelector("h1")?.textContent?.trim().slice(0, 60) ?? null,
    words: (document.getElementById("root")?.innerText ?? "").split(/\s+/).filter(Boolean).length,
    lang: document.documentElement.lang,
    iframes: document.querySelectorAll("iframe").length,
  }));
  const relevant = errors.filter((e) => !/net::ERR_FAILED|Failed to load resource|fbq|facebook|wistia|fonts\.g/i.test(e));
  const hydration = relevant.filter((e) => /hydrat|did not match|server rendered|Minified React error #4(18|19|21|23|25)/i.test(e));
  if (hydration.length) failures++;
  console.log(`${route.padEnd(14)} words=${String(info.words).padStart(4)} h1="${info.h1}" lang=${info.lang} iframes=${info.iframes} calendarLoads=${iframeHits.length} hydrationErrors=${hydration.length}`);
  for (const e of relevant.slice(0, 4)) console.log(`    ! ${e.slice(0, 220)}`);
  if (route === "/") await page.screenshot({ path: "/home/claude/browsercheck/home-mobile.png" });
  if (route === "/book") await page.screenshot({ path: "/home/claude/browsercheck/book-mobile.png" });
  await page.close();
}

await browser.close();
server.close();
console.log(failures ? `HYDRATION PROBLEMS on ${failures} route(s)` : "No hydration problems");
