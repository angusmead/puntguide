#!/usr/bin/env python3
"""
Phase 1 SEO fixes:
1. Regenerate sitemap.xml (all 657 pages)
2. Add Twitter card meta tags sitewide
3. Fix missing OG tags (9 pages)
4. Fix missing schema (10 pages)
"""
import os, re
from datetime import date

TODAY = date.today().isoformat()
BASE = "https://puntguide.com.au"

# ─── Priority map ─────────────────────────────────────────────────────────────
def priority(fn):
    if fn == "index.html": return "1.0", "weekly"
    if fn in ("best-betting-sites-australia.html", "all-betting-sites.html",
              "new-betting-sites-australia.html", "best-betting-apps-australia.html"): return "0.9", "weekly"
    if fn.startswith("review-") or fn.startswith("compare-"): return "0.8", "monthly"
    if fn in ("afl-tips.html","nrl-tips.html","horse-racing-tips-today.html",
              "afl-ladder-2026.html","nrl-ladder-2026.html",
              "brownlow-medal-odds-2026.html","nrl-premiership-odds-2026.html",
              "afl-premiership-odds-2026.html"): return "0.8", "weekly"
    if fn.startswith("best-betting") or fn.startswith("fastest"): return "0.7", "monthly"
    if re.match(r'(afl|nrl)-round-\d+-tips', fn): return "0.6", "weekly"
    if re.match(r'(afl|nrl)-.+-vs-.+-round', fn): return "0.5", "monthly"
    return "0.5", "monthly"

# ─── 1. SITEMAP ───────────────────────────────────────────────────────────────
def build_sitemap():
    skip = {"racing-weekend-may2-2026.html"}  # redirect page
    urls = []
    for fn in sorted(os.listdir(".")):
        if not fn.endswith(".html") or fn in skip:
            continue
        pri, freq = priority(fn)
        slug = fn if fn != "index.html" else ""
        url = f"{BASE}/{slug}"
        urls.append(f"""  <url>
    <loc>{url}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{pri}</priority>
  </url>""")
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>"""
    with open("sitemap.xml", "w") as f:
        f.write(xml)
    print(f"  Sitemap: {len(urls)} URLs written")

# ─── 2. TWITTER CARDS sitewide ────────────────────────────────────────────────
def add_twitter_cards():
    added = 0
    for fn in os.listdir("."):
        if not fn.endswith(".html"):
            continue
        with open(fn, "r", encoding="utf-8") as f:
            html = f.read()
        if 'twitter:card' in html:
            continue
        # Extract OG or fallback to title/meta desc
        og_title = re.search(r'property="og:title"\s+content="([^"]+)"', html)
        og_desc  = re.search(r'property="og:description"\s+content="([^"]+)"', html)
        title    = re.search(r'<title>([^<]+)</title>', html)
        desc     = re.search(r'meta name="description"\s+content="([^"]+)"', html)
        t = (og_title.group(1) if og_title else (title.group(1) if title else "PuntGuide"))
        d = (og_desc.group(1)  if og_desc  else (desc.group(1)  if desc  else "Australia's betting guide."))
        cards = f"""<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@puntguide">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{BASE}/puntguide-logo.png">"""
        # Insert before </head>
        html = html.replace("</head>", cards + "\n</head>", 1)
        with open(fn, "w", encoding="utf-8") as f:
            f.write(html)
        added += 1
    print(f"  Twitter cards: added to {added} pages")

# ─── 3. FIX MISSING OG TAGS ───────────────────────────────────────────────────
OG_DATA = {
    "afl-round-8-tips-2026.html": (
        "AFL Round 8 Tips 2026 | PuntGuide",
        "Expert AFL Round 8 2026 tips and predictions for all 9 matches. Best bets, odds comparison and analysis.",
        "/afl-round-8-tips-2026.html"),
    "all-betting-sites.html": (
        "All Betting Sites Australia — 130+ Bookmakers | PuntGuide",
        "Complete list of all licensed Australian betting sites. Compare 130+ bookmakers by odds, bonuses, payout speed and app quality.",
        "/all-betting-sites.html"),
    "best-betting-apps-australia.html": (
        "Best Betting Apps Australia 2026 | PuntGuide",
        "The best betting apps in Australia ranked by odds, features, speed and ease of use. iOS and Android reviews.",
        "/best-betting-apps-australia.html"),
    "best-betting-sites-for-afl.html": (
        "Best Betting Sites for AFL 2026 | PuntGuide",
        "The best Australian bookmakers for AFL betting — widest markets, best odds, live betting and Same Game Multi options.",
        "/best-betting-sites-for-afl.html"),
    "best-betting-sites-for-racing.html": (
        "Best Horse Racing Betting Sites Australia 2026 | PuntGuide",
        "Top Australian bookmakers for horse racing — Best Tote, Same Race Multi, exotic betting and fastest payouts.",
        "/best-betting-sites-for-racing.html"),
    "fastest-payout-betting-sites-australia.html": (
        "Fastest Payout Betting Sites Australia 2026 | PuntGuide",
        "Australian bookmakers ranked by withdrawal speed. Same-day and instant payout options reviewed and compared.",
        "/fastest-payout-betting-sites-australia.html"),
    "nrl-round-10-tips-2026.html": (
        "NRL Round 9 Tips 2026 | PuntGuide",
        "Expert NRL Round 9 2026 tips and predictions for all matches. Best bets, odds comparison and analysis.",
        "/nrl-round-10-tips-2026.html"),
    "racing-futures-2026.html": (
        "Racing Futures 2026 — Melbourne Cup, Cox Plate & Caulfield Cup Odds | PuntGuide",
        "Current odds and analysis for Australia's biggest 2026 racing events — Melbourne Cup, Cox Plate and Caulfield Cup.",
        "/racing-futures-2026.html"),
}

def fix_og_tags():
    fixed = 0
    for fn, (title, desc, path) in OG_DATA.items():
        if not os.path.exists(fn):
            continue
        with open(fn, "r", encoding="utf-8") as f:
            html = f.read()
        if 'og:title' in html:
            continue
        og = f"""<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{BASE}{path}">
<meta property="og:type" content="article">
<meta property="og:image" content="{BASE}/puntguide-logo.png">"""
        html = html.replace("</head>", og + "\n</head>", 1)
        with open(fn, "w", encoding="utf-8") as f:
            f.write(html)
        fixed += 1
    print(f"  OG tags: fixed on {fixed} pages")

# ─── 4. FIX MISSING SCHEMA ────────────────────────────────────────────────────
SCHEMA_DATA = {
    "afl-premiership-odds-2026.html": {
        "type": "Article",
        "headline": "AFL Premiership Odds 2026",
        "description": "Current AFL premiership odds and futures market analysis for 2026."
    },
    "nrl-premiership-odds-2026.html": {
        "type": "Article",
        "headline": "NRL Premiership Odds 2026",
        "description": "Current NRL premiership odds and futures market analysis for 2026."
    },
    "best-betting-sites-for-afl.html": {
        "type": "Article",
        "headline": "Best Betting Sites for AFL 2026",
        "description": "The best Australian bookmakers for AFL betting ranked by odds, markets and features."
    },
    "best-betting-sites-for-racing.html": {
        "type": "Article",
        "headline": "Best Horse Racing Betting Sites Australia 2026",
        "description": "Top Australian bookmakers for horse racing — Best Tote, Same Race Multi and fastest payouts."
    },
    "best-betting-apps-australia.html": {
        "type": "Article",
        "headline": "Best Betting Apps Australia 2026",
        "description": "The best betting apps in Australia ranked by odds, features and ease of use."
    },
    "fastest-payout-betting-sites-australia.html": {
        "type": "Article",
        "headline": "Fastest Payout Betting Sites Australia 2026",
        "description": "Australian bookmakers ranked by withdrawal speed — same-day and instant payout options reviewed."
    },
    "racing-futures-2026.html": {
        "type": "Article",
        "headline": "Racing Futures 2026 — Melbourne Cup, Cox Plate & Caulfield Cup",
        "description": "Current odds and analysis for Australia's biggest 2026 racing events."
    },
    "afl-round-8-tips-2026.html": {
        "type": "Article",
        "headline": "AFL Round 8 Tips 2026",
        "description": "Expert AFL Round 8 2026 tips and predictions for all 9 matches."
    },
    "nrl-round-10-tips-2026.html": {
        "type": "Article",
        "headline": "NRL Round 9 Tips 2026",
        "description": "Expert NRL Round 9 2026 tips and predictions for all matches."
    },
}

import json

def fix_schema():
    fixed = 0
    for fn, data in SCHEMA_DATA.items():
        if not os.path.exists(fn):
            continue
        with open(fn, "r", encoding="utf-8") as f:
            html = f.read()
        if 'application/ld+json' in html:
            continue
        schema = {
            "@context": "https://schema.org",
            "@type": data["type"],
            "headline": data["headline"],
            "description": data["description"],
            "author": {"@type": "Organization", "name": "PuntGuide"},
            "publisher": {
                "@type": "Organization",
                "name": "PuntGuide",
                "logo": {"@type": "ImageObject", "url": f"{BASE}/puntguide-logo.png"}
            },
            "datePublished": "2026-01-01",
            "dateModified": TODAY,
            "mainEntityOfPage": f"{BASE}/{fn}"
        }
        tag = f'<script type="application/ld+json">{json.dumps(schema)}</script>'
        html = html.replace("</head>", tag + "\n</head>", 1)
        with open(fn, "w", encoding="utf-8") as f:
            f.write(html)
        fixed += 1
    print(f"  Schema: fixed on {fixed} pages")

# ─── RUN ALL ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Phase 1 SEO fixes running...")
    build_sitemap()
    fix_og_tags()
    fix_schema()
    add_twitter_cards()
    print("Done.")
