from __future__ import annotations

import json
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "data" / "sessions.json"

PART_META = {
    "Part-I": {"label": "Part I", "theme": "Survival wiring & trauma literacy"},
    "Part-II": {"label": "Part II", "theme": "Institutional systems & reentry"},
    "Part-III": {"label": "Part III", "theme": "Resilience & autonomy"},
    "Part-IV": {"label": "Part IV", "theme": "Facilitation & crisis management"},
}


def clean_markdown(raw: str) -> str:
    lines = raw.splitlines()
    cleaned = []
    for line in lines:
        if line.startswith("# Session "):
            continue
        if line.startswith("![Version]"):
            continue
        if "[**HOME**]" in line and "[**PART" in line:
            continue
        if line.strip() == "---" and not cleaned:
            continue
        cleaned.append(line)
    return "\n".join(cleaned).strip()


def session_number(path: Path) -> int:
    match = re.search(r"Session[_ -]?(\d+)", path.stem, flags=re.I)
    return int(match.group(1)) if match else 999


def title_from_markdown(raw: str, path: Path) -> str:
    for line in raw.splitlines():
        match = re.match(r"^#\s+Session\s+\d+\s*:\s*(.+)$", line.strip())
        if match:
            return match.group(1).strip()
    fallback = re.sub(r"^Session[_ -]?\d+[_ -]?", "", path.stem, flags=re.I)
    return fallback.replace("_", " ").replace("-", " ").strip().title()


def record_id(part_dir: str, path: Path, number: int) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", path.stem.lower()).strip("-")
    return f"{part_dir.lower()}-{number:02d}-{slug}"


def overview_text(raw: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", raw)
    text = re.sub(r"\[[^\]]+\]\([^)]*\)", "", text)
    text = re.sub(r"[*_`>#-]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:260] + ("…" if len(text) > 260 else "")


def build() -> None:
    records = []
    for part_dir, meta in PART_META.items():
        for path in sorted((ROOT / part_dir).glob("Session*.md"), key=session_number):
            raw = path.read_text(encoding="utf-8", errors="replace")
            body = clean_markdown(raw)
            html = markdown.markdown(
                body,
                extensions=["extra", "sane_lists", "nl2br"],
                output_format="html5",
            )
            number = session_number(path)
            records.append({
                "id": record_id(part_dir, path, number),
                "number": number,
                "part": part_dir,
                "partLabel": meta["label"],
                "theme": meta["theme"],
                "title": title_from_markdown(raw, path),
                "filename": path.name,
                "sourcePath": f"{part_dir}/{path.name}",
                "summary": overview_text(raw),
                "html": html,
                "text": re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip().lower(),
            })

    records.sort(key=lambda item: (item["number"], item["part"]))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps({
        "generated": "2026-08-19",
        "count": len(records),
        "parts": PART_META,
        "sessions": records,
    }, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(records)} session records to {OUTPUT}")


if __name__ == "__main__":
    build()
