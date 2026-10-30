"""Turn the guide drafts in marketing/seo/content/ into the files the website uses.

Usage:
    python3 build_guides.py <site_repo_root> [slug-or-number ...]

For each draft it writes, inside the site repo:
    src/content/guias/<slug>.html   article body (no H1, no FAQ, no internal notes)
    src/content/guias/guias.json    metadata for every guide (title, description,
                                    dates, FAQ for the visible FAQ and FAQPage schema)

Rules for drafts (same format as 01-cuanto-cuesta-clienta-cejas-anuncios.md):
- YAML front matter with at least: slug, h1, meta_title, meta_description, autor,
  fecha (YYYY-MM-DD, the visible "actualizado" date), minutos (reading time).
- One "# H1" line (dropped here; the page renders h1 from the front matter).
- An "## Preguntas frecuentes" section with "**Question?**" lines each followed by
  the answer paragraph. It is lifted out of the body and rendered by the page.
- Everything from the "<!-- NO PUBLICAR" comment down is internal and never shipped.
"""
import json
import re
import sys
from pathlib import Path

import markdown
import yaml

CONTENT = Path(__file__).resolve().parent.parent / "content"


def split_front_matter(text: str):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError("missing front matter")
    return yaml.safe_load(m.group(1)), m.group(2)


def take_faq(body: str):
    m = re.search(r"^## Preguntas frecuentes\s*\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    if not m:
        return body, []
    faqs = []
    for q, a in re.findall(r"^\*\*(.+?)\*\*\s*\n(.+?)(?=\n\s*\n|\Z)", m.group(1), re.S | re.M):
        faqs.append({"q": q.strip(), "a": " ".join(a.split())})
    return body[: m.start()] + body[m.end():], faqs


def blank_size(n: int) -> str:
    return "corta" if n <= 4 else "media" if n <= 10 else "larga"


def plain(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return re.sub(r"[*_`]", "", text)


def build_one(path: Path):
    meta, body = split_front_matter(path.read_text(encoding="utf-8"))
    body = body.split("<!-- NO PUBLICAR")[0]
    body = re.sub(r"\n---\s*$", "\n", body.rstrip()) + "\n"
    body = re.sub(r"^# .*\n", "", body, count=1, flags=re.M)
    body, faqs = take_faq(body)
    # Fill-in blanks ("____") in templates become drawn lines; raw underscores would turn into bold/italics.
    body = re.sub(r"_{3,}", lambda m: f'<span class="guia-linea guia-linea-{blank_size(len(m.group(0)))}"></span>', body)
    # md_in_html lets a draft wrap Markdown in <div class="guia-plantilla" markdown="1">.
    html = markdown.markdown(body, extensions=["tables", "sane_lists", "md_in_html"], output_format="html")
    # Internal links stay on the site; outside links open in a new tab.
    html = re.sub(r'href="https://pmuacademia\.com(/[^"]*)"', r'href="\1"', html)
    html = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', html)
    html = html.replace("<table>", '<div class="guia-tabla"><table>').replace("</table>", "</table></div>")
    slug = meta["slug"].rstrip("/").split("/")[-1]
    entry = {
        "slug": slug,
        "h1": meta["h1"],
        "metaTitle": meta["meta_title"],
        "description": meta["meta_description"],
        "pillar": meta.get("pilar", ""),
        "author": meta.get("autor", "Adriano Rodriguez"),
        "dateModified": str(meta["fecha"]),
        "datePublished": str(meta.get("publicado_fecha") or meta["fecha"]),
        "minutes": int(meta.get("minutos", 6)),
        "faqs": [{"q": plain(f["q"]), "a": plain(f["a"])} for f in faqs],
    }
    return slug, html, entry


def main():
    site = Path(sys.argv[1])
    wanted = sys.argv[2:]
    out = site / "src/content/guias"
    out.mkdir(parents=True, exist_ok=True)
    entries = []
    for path in sorted(CONTENT.glob("[0-9][0-9]-*.md")):
        if wanted and not any(w in path.name for w in wanted):
            continue
        slug, html, entry = build_one(path)
        (out / f"{slug}.html").write_text(html, encoding="utf-8")
        entries.append(entry)
        print(f"{path.name} -> {slug} ({len(entry['faqs'])} FAQ, {len(html)} chars)")
    (out / "guias.json").write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
