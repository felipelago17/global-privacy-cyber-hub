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

import html as _html
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

def gnews(query: str) -> str:
    """Google News RSS search feed — reliable fallback for sites that block bots or have no feed."""
    from urllib.parse import quote
    return f"https://news.google.com/rss/search?q={quote(query + ' when:3d')}&hl=en-US&gl=US&ceid=US:en"


FEEDS = [
    # Practitioner / industry
    {"source": "IAPP", "url": "https://iapp.org/news", "type": "iapp_html", "category": "Privacy & AI governance"},
    {"source": "Future of Privacy Forum", "url": "https://fpf.org/feed/", "category": "Privacy & AI governance"},
    {"source": "EFF Deeplinks", "url": "https://www.eff.org/rss/updates.xml", "category": "Privacy & digital rights"},
    # High-volume vendor/vuln news site — kept only where it touches incidents, critical infrastructure/OT, regulators or data
    {"source": "Cyber Security News", "url": "https://cybersecuritynews.com/feed/", "category": "Cyber incidents & threat intel", "filter": "incident"},
    # Curated from zer0yu/CyberSecurityRSS (tiny.opml / CyberSecurityRSS.opml, Sep 2026) - in-scope subset only
    {"source": "Krebs on Security", "url": "https://krebsonsecurity.com/feed/", "category": "Cyber incidents & threat intel", "filter": "incident", "max": 3},
    {"source": "SecurityWeek", "url": "https://www.securityweek.com/feed/", "category": "Cyber incidents & threat intel", "filter": "incident", "max": 4},
    {"source": "Dark Reading", "url": "https://www.darkreading.com/rss.xml", "category": "Cyber incidents & threat intel", "filter": "incident", "max": 4},
    {"source": "Infosecurity Magazine", "url": "http://www.infosecurity-magazine.com/rss/news/", "category": "Cyber incidents & threat intel", "filter": "incident", "max": 4},
    {"source": "Claroty Team82", "url": "https://claroty.com/team82/disclosure-dashboard/feed/atom", "category": "Critical infrastructure & OT", "max": 3},
    {"source": "Microsoft Security Blog", "url": "https://www.microsoft.com/security/blog/feed/", "category": "Vendor threat research", "max": 2},
    {"source": "Google Online Security Blog", "url": "http://feeds.feedburner.com/GoogleOnlineSecurityBlog?format=xml", "category": "Vendor threat research", "max": 2},
    {"source": "Trail of Bits", "url": "https://blog.trailofbits.com/feed/", "category": "AI & agent security", "max": 2},
    {"source": "Simon Willison", "url": "https://simonwillison.net/atom/everything/", "category": "AI & agent security", "filter": "ai_security", "max": 2},
    # EU
    {"source": "EDPB", "url": "https://www.edpb.europa.eu/feed/news_en", "category": "EU data protection", "fallback": "EDPB (via Google News)"},
    {"source": "EDPB (via Google News)", "url": gnews("site:edpb.europa.eu"), "category": "EU data protection"},
    {"source": "CNIL", "url": "https://www.cnil.fr/fr/rss.xml", "category": "EU data protection"},
    {"source": "ENISA (via Google News)", "url": gnews("site:enisa.europa.eu"), "category": "EU cybersecurity"},
    {"source": "EU Digital Strategy", "url": "https://digital-strategy.ec.europa.eu/en/rss.xml", "category": "EU digital policy"},
    # UK
    {"source": "ICO (via Google News)", "url": gnews("site:ico.org.uk"), "category": "UK data protection"},
    {"source": "UK NCSC", "url": "https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml", "category": "UK cybersecurity"},
    # US
    {"source": "FTC (via Google News)", "url": gnews("site:ftc.gov privacy OR data OR security OR AI"), "category": "US enforcement"},
    {"source": "NIST", "url": "https://www.nist.gov/news-events/news/rss.xml", "category": "Standards"},
    {"source": "CISA (via Google News)", "url": gnews("site:cisa.gov advisory OR alert OR vulnerability"), "category": "Cybersecurity advisories"},
]

# Relevance filter for the broad feeds (FTC, NIST, EU Digital Strategy, EFF).
# Regulator-specific feeds (EDPB, ICO, CNIL, ENISA, CISA, IAPP, FPF) are kept whole.
UNFILTERED = {"IAPP", "Future of Privacy Forum", "EDPB", "EDPB (via Google News)", "CNIL", "ENISA (via Google News)", "ICO (via Google News)", "CISA (via Google News)", "UK NCSC"}
# Tighter filter for high-volume threat-intel sites: incidents, OT/critical infrastructure, regulators, data exposure
AI_SECURITY_KEYWORDS = re.compile(
    r"(prompt[- ]injection|jailbreak|exfiltrat|vulnerab|sandbox escape|lethal trifecta|data leak|malicious (package|prompt|instruction)|security (flaw|hole|issue|bug))",
    re.IGNORECASE,
)
INCIDENT_KEYWORDS = re.compile(
    r"\b(hacked|breach|leak|ransomware attack|data (theft|exposure|stolen)|"
    r"hospital|health|blood|medical|water|energy|grid|pipeline|refrigerat|ics|scada|ot\b|plc|critical infrastructure|"
    r"cert-fr|anssi|enisa|cisa|ncsc|ico\b|cnil|edpb|ftc|gdpr|nis2|regulator|fine[sd]?\b|sanction|"
    r"supply[- ]chain|third[- ]party|vendor compromise|ai (model|agent)|llm|prompt injection)\b",
    re.IGNORECASE,
)
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
    text = _html.unescape(re.sub(r"<[^>]+>", " ", text or ""))
    text = re.sub(r"\s+", " ", text).strip()
    return (text[: limit - 1] + "…") if len(text) > limit else text


def fetch_iapp_html(feed: dict, seen: dict[str, str]) -> tuple[list[dict], str | None]:
    """IAPP publishes no RSS feed; parse article links from the news listing page."""
    import urllib.request
    req = urllib.request.Request(feed["url"], headers={"User-Agent": "Mozilla/5.0 (compatible; global-privacy-cyber-hub digest/1.0)"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            html = r.read().decode("utf-8", "ignore")
    except Exception as exc:  # noqa: BLE001
        return [], f"{feed['source']}: {exc}"
    items, found = [], set()
    for m in re.finditer(r'<a[^>]+href="(/news/a/[^"?#]+)"[^>]*>(.*?)</a>', html, re.S | re.I):
        path, inner = m.group(1).rstrip("/"), clean(m.group(2), 200)
        if path in found or len(inner) < 20:
            continue
        found.add(path)
        link = "https://iapp.org" + path
        if link in seen:
            continue
        items.append({"uid": link, "source": feed["source"], "category": feed["category"],
                      "title": inner, "link": link, "date": "", "summary": ""})
        if len(items) >= MAX_PER_SOURCE:
            break
    if not found:
        return [], f"{feed['source']}: no article links found on listing page (markup may have changed)"
    return items, None


BROWSER_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36 global-privacy-cyber-hub-digest/1.1"
_CTRL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
_BARE_AMP = re.compile(r"&(?!#\d+;|#x[0-9a-fA-F]+;|[A-Za-z][A-Za-z0-9]*;)")


BARE_ID = re.compile(r"^\s*(EUVD|CVE|GHSA)-[\w-]+\s*$", re.I)


def repair_xml(raw: bytes) -> bytes:
    """Fix the faults that most often make regulator feeds unparseable:
    control characters, bare ampersands and leading junk before the XML declaration."""
    text = raw.decode("utf-8", "replace")
    start = text.find("<?xml")
    if start == -1:
        start = min([i for i in (text.find("<rss"), text.find("<feed")) if i != -1] or [0])
    text = text[start:]
    text = _CTRL.sub("", text)
    text = _BARE_AMP.sub("&amp;", text)
    return text.encode("utf-8")


def parse_feed(feed: dict):
    """Download and parse a feed, trying the project's own User-Agent first and a
    browser-like one second; repair malformed XML before giving up."""
    import urllib.request
    agents = ["global-privacy-cyber-hub digest/1.0", BROWSER_UA]
    last_err = "parse error"
    for ua in agents:
        req = urllib.request.Request(feed["url"], headers={
            "User-Agent": ua,
            "Accept": "application/rss+xml, application/atom+xml, application/xml;q=0.9, text/xml;q=0.8, */*;q=0.5",
        })
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                raw = r.read()
                ctype = r.headers.get("Content-Type", "")
        except Exception as exc:  # noqa: BLE001
            last_err = f"unreachable ({exc})"
            continue
        parsed = feedparser.parse(raw)
        if parsed.entries or (not parsed.bozo and parsed.get("feed")):
            return parsed, None  # includes valid feeds that simply have no items today
        repaired = feedparser.parse(repair_xml(raw))
        if repaired.entries:
            print(f"[info] {feed['source']}: malformed XML repaired ({getattr(parsed, 'bozo_exception', '')})", file=sys.stderr)
            return repaired, None
        head = raw[:2000].lower()
        if b"<html" in head and b"<rss" not in head and b"<feed" not in head:
            last_err = f"returned an HTML page instead of a feed ({ctype or 'no content-type'}) - likely bot protection or a moved URL"
        else:
            last_err = f"feed unavailable ({getattr(parsed, 'bozo_exception', 'parse error')})"
    return None, f"{feed['source']}: {last_err}"


def fetch(feed: dict, since: datetime, seen: dict[str, str]) -> tuple[list[dict], str | None]:
    if feed.get("type") == "iapp_html":
        return fetch_iapp_html(feed, seen)
    parsed, err = parse_feed(feed)
    if err:
        return [], err

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
        if "news.google.com" in feed["url"]:
            title = re.sub(r"\s+-\s+[^-]{2,60}$", "", title)
        if BARE_ID.match(title):
            continue  # vulnerability-database stubs (e.g. ENISA "EUVD-2026-119359") carry no news value
        text = title + " " + e.get("summary", "")
        if feed.get("filter") == "incident":
            if not INCIDENT_KEYWORDS.search(text):
                continue
        elif feed.get("filter") == "ai_security":
            if not AI_SECURITY_KEYWORDS.search(text):
                continue
        elif feed["source"] not in UNFILTERED and not KEYWORDS.search(text):
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
        if len(items) >= feed.get("max", MAX_PER_SOURCE):
            break
    return items, None


PICKS_HEADING = "## Editor's picks"


def read_picks(path: Path) -> list[str]:
    """Return a hand-curated "Editor's picks" section from an existing digest, if any.

    Curated items are added by hand (e.g. from Claude on mobile) before or after the
    automated run; the section runs from its heading to the next '## ' heading or EOF
    and is preserved verbatim when the digest is regenerated.
    """
    if not path.exists():
        return []
    out: list[str] = []
    capturing = False
    for line in path.read_text().splitlines():
        if line.strip() == PICKS_HEADING:
            capturing = True
        elif capturing and line.startswith("## "):
            break
        if capturing:
            out.append(line)
    return out


def write_digest(day: str, items: list[dict], errors: list[str]) -> Path:
    UPDATES.mkdir(exist_ok=True)
    path = UPDATES / f"{day}.md"
    picks = read_picks(path)
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
    if picks:
        lines += picks + [""]
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
        "standards bodies and trusted practitioner sources (IAPP, FPF, EDPB, ICO, CNIL, ENISA, NCSC, FTC, NIST, CISA, EFF, Cyber Security News — some via Google News site-feeds where the regulator blocks automated access). "
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
        label = f"{count} items" if count else "curated"
        if any(l.strip() == PICKS_HEADING for l in first):
            label += " + editor's picks"
        lines.append(f"| {day} | [{label}]({day}.md) |")
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
            print(f"[warn] {err}", file=sys.stderr)
            if feed.get("fallback"):
                print(f"[info] {feed['source']}: covered by fallback source '{feed['fallback']}'; not reported in digest", file=sys.stderr)
            else:
                errors.append(err)
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
    day_store = DATA / "days" / f"{day}.json"
    day_store.parent.mkdir(parents=True, exist_ok=True)
    earlier = []
    if day_store.exists():
        try:
            earlier = json.loads(day_store.read_text())
        except json.JSONDecodeError:
            earlier = []
    known = {i["uid"] for i in earlier}
    merged = earlier + [i for i in all_items if i["uid"] not in known]
    day_store.write_text(json.dumps(merged, indent=1, ensure_ascii=False))
    all_items = merged
    path = write_digest(day, all_items, errors)
    write_index()
    print(f"Wrote {path} with {len(all_items)} items")
    return 0


if __name__ == "__main__":
    sys.exit(main())
