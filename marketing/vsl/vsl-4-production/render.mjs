// node render.mjs OUT.mp4 FPS "n:dur,n:dur,..."   (renders the graphics track, 1920x1080, no audio)
// node render.mjs --stills DIR "n:t,n:t"          (PNG stills for checking)
import chromium from "@sparticuz/chromium"; import puppeteer from "puppeteer-core";
import { spawn } from "node:child_process"; import path from "node:path"; import { pathToFileURL } from "node:url";
const browser = await puppeteer.launch({ executablePath: await chromium.executablePath(), args: [...chromium.args, "--allow-file-access-from-files"], headless: true });
const page = await browser.newPage();
await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
await page.goto(pathToFileURL(path.resolve("stage.html")).href, { waitUntil: "load" });
await page.evaluate(() => document.fonts.ready);
const args = process.argv.slice(2);
if (args[0] === "--stills") {
  for (const spec of args[2].split(",")) {
    const [n, t] = spec.split(":").map(Number);
    await page.evaluate((n) => window.setScene(n), n);
    await page.evaluate((t) => window.seek(t), t);
    await page.screenshot({ path: `${args[1]}/s${n}-${t}.png` });
  }
} else {
  const [out, fps, list] = args;
  const ff = spawn("ffmpeg", ["-v", "error", "-y", "-f", "image2pipe", "-framerate", fps, "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", out], { stdio: ["pipe", "inherit", "inherit"] });
  let frames = 0;
  for (const spec of list.split(",")) {
    const [n, dur] = spec.split(":").map(Number);
    await page.evaluate((n) => window.setScene(n), n);
    const count = Math.round(dur * Number(fps));
    for (let i = 0; i < count; i++) {
      await page.evaluate((t) => window.seek(t), i / Number(fps));
      const buf = await page.screenshot({ type: "jpeg", quality: 92 });
      if (!ff.stdin.write(buf)) await new Promise((r) => ff.stdin.once("drain", r));
      frames++;
    }
    process.stdout.write(`${n} `);
  }
  ff.stdin.end(); await new Promise((r) => ff.on("close", r));
  console.log(`\nframes ${frames}`);
}
await browser.close();
