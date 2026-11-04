#!/usr/bin/env python3
"""Daily privacy / cybersecurity / AI-governance digest.

Pulls RSS/Atom feeds from regulators, standards bodies and trusted
practitioner sources, filters for relevance, and writes:

  updates/YYYY-MM-DD.md   dated digest (only if there is something new)
  updates/index.md        reverse-chronological index of digests
  data/seen.json          IDs already reported (so items are reported once)

Run from the repo root:  python tools/fetch_updates.py
"""

from __future__ import annotations

import json
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import feedparser

ROOT = Path(__file__).resolve().parent.parent
UPDATES = ROOT / "updates"
DATA = ROOT / "data"
SEEN_FILE = DATA / "seen.json"

LOOKBACK_DAYS = 3        # how far back to look on each run
MAX_PER_SOURCE = 8       # cap per source per digest
SEEN_KEEP_DAYS = 60      # prune seen-IDs older than this

FEEDS = [
    # Practitioner / industry
    {"source": "IAPP", "url": "https://iapp.org/news/rss/", "category": "Privacy & AI governance"},
    {"source": "Future of Privacy Forum", "url": "https://fpf.org/feed/", "category": "Privacy & AI governance"},
    {"source": "EFF Deeplinks", "url": "https://www.eff.org/rss/updates.xml", "category": "Privacy & digital rights"},
    # EU
    {"source": "EDPB", "url": "https://www.edpb.europa.eu/feed/news_en", "category": "EU data protection"},
    {"source": "CNIL", "url": "https://www.cnil.fr/fr/rss.xml", "category": "EU data protection"},
    {"source": "ENISA", "url": "https://www.enisa.europa.eu/front-page/RSS", "category": "EU cybersecurity"},
    {"source": "EU Digital Strategy", "url": "https://digital-strategy.ec.europa.eu/en/rss.xml", "category": "EU digital policy"},
    # UK
    {"source": "ICO", "url": "https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/rss/", "category": "UK data protection"},
    {"source": "UK NCSC", "url": "https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml", "category": "UK cybersecurity"},
    # US
    {"source": "FTC", "url": "https://www.ftc.gov/feeds/press-releases.xml", "category": "US enforcement"},
    {"source": "NIST", "url": "https://www.nist.gov/news-events/news/rss.xml", "category": "Standards"},
    {"source": "CISA advisories", "url": "https://www.cisa.gov/cybersecurity-advisories/all.xml", "category": "Cybersecurity advisories"},
]

# Relevance filter for the broad feeds (FTC, NIST, EU Digital Strategy, EFF).
# Regulator-specific feeds (EDPB, ICO, CNIL, ENISA, CISA, IAPP, FPF) are kept whole.
UNFILTERED = {"IAPP", "Future of Privacy Forum", "EDPB", "CNIL", "ENISA", "ICO", "CISA advisories", "UK NCSC"}
KEYWORDS = re.compile(
    r"\b(privacy|data protection|gdpr|personal data|biometric|surveillance|"
    r"cyber|ransomware|breach|vulnerabilit|zero[- ]day|encryption|"
    r"artificial intelligence|\bai\b|algorithm|machine learning|generative|agent|"
    r"children|coppa|health data|location data|data broker|"
    r"transfer|adequacy|data privacy framework|dpia|consent)\b",
    re.IGNORECASE,
)


def load_seen() -> dict[str, str]:
    if SEEN_FILE.exists():
        try:
            return json.loads(SEEN_FILE.read_text())
        except json.JSONDecodeError:
            return {}
    return {}


def save_seen(seen: dict[str, str]) -> None:
    cutoff = (datetime.now(timezone.utc) - timedelta(days=SEEN_KEEP_DAYS)).date().isoformat()
    pruned = {k: v for k, v in seen.items() if v >= cutoff}
    DATA.mkdir(exist_ok=True)
    SEEN_FILE.write_text(json.dumps(pruned, indent=1, sort_keys=True))


def entry_date(e) -> datetime | None:
    for key in ("published_parsed", "updated_parsed"):
        t = e.get(key)
        if t:
            return datetime.fromtimestamp(time.mktime(t), tz=timezone.utc)
    return None


def clean(text: str, limit: int = 280) -> str:
    text = re.sub(r"<[^>]+>", " ", text or "")
    text = re.sub(r"\s+", " ", text).strip()
    return (text[: limit - 1] + "…") if len(text) > limit else text


def fetch(feed: dict, since: datetime, seen: dict[str, str]) -> tuple[list[dict], str | None]:
    try:
        parsed = feedparser.parse(feed["url"], request_headers={"User-Agent": "global-privacy-cyber-hub digest/1.0"})
    except Exception as exc:  # noqa: BLE001
        return [], f"{feed['source']}: {exc}"
    if parsed.bozo and not parsed.entries:
        return [], f"{feed['source']}: feed unavailable ({getattr(parsed, 'bozo_exception', 'parse error')})"

    items = []
    for e in parsed.entries:
        link = e.get("link") or ""
        uid = e.get("id") or link
        if not uid or uid in seen:
            continue
        d = entry_date(e)
        if d and d < since:
            continue
        title = clean(e.get("title", ""), 200)
        if feed["source"] not in UNFILTERED and not KEYWORDS.search(title + " " + e.get("summary", "")):
            continue
        items.append(
            {
                "uid": uid,
                "source": feed["source"],
                "category": feed["category"],
                "title": title,
                "link": link,
                "date": d.date().isoformat() if d else "",
                "summary": clean(e.get("summary", "")),
            }
        )
        if len(items) >= MAX_PER_SOURCE:
            break
    return items, None


def write_digest(day: str, items: list[dict], errors: list[str]) -> Path:
    UPDATES.mkdir(exist_ok=True)
    path = UPDATES / f"{day}.md"
    by_cat: dict[str, list[dict]] = {}
    for it in items:
        by_cat.setdefault(it["category"], []).append(it)

    lines = [
        f"# Daily digest — {day}",
        "",
        f"{len(items)} new item(s) across {len({i['source'] for i in items})} source(s). "
        "Automated collection from official and trusted feeds; summaries are the publishers' own abstracts. "
        "Not legal advice.",
        "",
    ]
    for cat in sorted(by_cat):
        lines += [f"## {cat}", ""]
        for it in sorted(by_cat[cat], key=lambda x: (x["source"], x["date"]), reverse=False):
            date = f" ({it['date']})" if it["date"] else ""
            lines.append(f"- **{it['source']}**{date} — [{it['title']}]({it['link']})")
            if it["summary"]:
                lines.append(f"  {it['summary']}")
        lines.append("")
    if errors:
        lines += ["## Feed notes", ""] + [f"- {e}" for e in errors] + [""]
    path.write_text("\n".join(lines))
    return path


def write_index() -> None:
    digests = sorted((p for p in UPDATES.glob("????-??-??.md")), reverse=True)
    lines = [
        "# Daily updates",
        "",
        "Automated daily digest of privacy, cybersecurity and AI-governance developments from regulators, "
        "standards bodies and trusted practitioner sources (IAPP, FPF, EDPB, ICO, CNIL, ENISA, NCSC, FTC, NIST, CISA, EFF). "
        "Each item is reported once, on the day it is first seen. Sources and filters are defined in "
        "[`tools/fetch_updates.py`](https://github.com/felipelago17/global-privacy-cyber-hub/blob/main/tools/fetch_updates.py).",
        "",
        "| Date | Digest |",
        "|---|---|",
    ]
    for p in digests[:120]:
        day = p.stem
        first = p.read_text().splitlines()
        count = next((l for l in first if "new item" in l), "").split(" new item")[0]
        lines.append(f"| {day} | [{count} items]({day}.md) |")
    lines.append("")
    (UPDATES / "index.md").write_text("\n".join(lines))


def main() -> int:
    now = datetime.now(timezone.utc)
    day = now.date().isoformat()
    since = now - timedelta(days=LOOKBACK_DAYS)
    seen = load_seen()

    all_items: list[dict] = []
    errors: list[str] = []
    for feed in FEEDS:
        items, err = fetch(feed, since, seen)
        if err:
            errors.append(err)
            print(f"[warn] {err}", file=sys.stderr)
        else:
            print(f"[ok] {feed['source']}: {len(items)} new")
        all_items.extend(items)

    if not all_items:
        print("No new items; nothing written.")
        write_index()
        return 0

    for it in all_items:
        seen[it["uid"]] = day
    save_seen(seen)
    path = write_digest(day, all_items, errors)
    write_index()
    print(f"Wrote {path} with {len(all_items)} items")
    return 0


if __name__ == "__main__":
    sys.exit(main())
