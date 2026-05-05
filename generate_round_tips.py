#!/usr/bin/env python3
"""
PuntGuide — Round Tips Hub Generator
Produces AFL and NRL round tips pages in the editorial match-card design
(matching afl-round-8-tips-2026.html / nrl-round-10-tips-2026.html).

Usage:
  python3 generate_round_tips.py

Edit the ROUND_DATA dict below with the current round's matches, then run.
The script writes the hub page and prints the filename.

DESIGN RULE: All AFL/NRL round hub pages with real content MUST use this
template. Never use the stub output from generate_all_pages.py as a final hub.
"""

import json, os

# ─── CONFIGURE THIS EACH ROUND ───────────────────────────────────────────────

SPORT = "nrl"          # "nrl" or "afl"
ROUND_NUM = 11         # Round number
ROUND_LABEL = "Round 11"
DATES = "14–17 May 2026"
UPDATED = "12 May 2026"
BYE_TEAM = "Sea Eagles"  # or "" if no bye

MATCH_OF_ROUND = {
    "title": "Panthers v Cowboys — Qld Country Bank, Friday 8pm",
    "subtitle": "Our tip: Panthers H2H · Competition leaders vs top-six Cowboys"
}

INTRO = (
    "Eight NRL games across four days — Thursday through Sunday. "
    "Update this intro with the round's key storylines before publishing."
)

# Each match dict:
# home, away, date, time, venue, h2h_home, h2h_away, line,
# tip (short), analysis (2–3 sentences), key_news (list of strings, max 4),
# bets (list of {desc, sub}), match_slug
MATCHES = [
    # ── PASTE MATCHES HERE ──────────────────────────────────────────────
    # Example:
    # {
    #     "home": "Penrith Panthers",
    #     "away": "North Queensland Cowboys",
    #     "date": "Friday 15 May",
    #     "time": "8:00pm",
    #     "venue": "Qld Country Bank Stadium",
    #     "h2h_home": "$1.30",
    #     "h2h_away": "$3.50",
    #     "line": "Panthers -9.5",
    #     "tip": "Panthers H2H",
    #     "analysis": "Panthers unchanged and rolling...",
    #     "key_news": [
    #         "Panthers: Nathan Cleary returns (hamstring)",
    #         "Cowboys: Dearden named despite ankle scare",
    #     ],
    #     "bets": [
    #         {"desc": "Panthers head-to-head", "sub": "Better value than -9.5 away"},
    #         {"desc": "Panthers -9.5", "sub": "If confident on their defence"},
    #     ],
    #     "match_slug": "nrl-panthers-vs-cowboys-round-11-2026",
    # },
]

# ─── TEMPLATE ─────────────────────────────────────────────────────────────────

BASE = "https://puntguide.com.au"

CSS = """<style>
:root{--bg:hsl(205 60% 96%);--fg:hsl(215 45% 16%);--primary:hsl(48 92% 64%);--primary-fg:hsl(215 45% 16%);--muted:hsl(205 40% 92%);--muted-fg:hsl(215 20% 42%);--border:hsl(205 40% 86%);--card:hsl(0 0% 100%);--grad-gold:linear-gradient(135deg,hsl(50 96% 72%) 0%,hsl(44 92% 60%) 100%);--shadow-card:0 4px 24px -8px hsl(215 50% 30% / 0.12);--shadow-gold:0 10px 40px -10px hsl(48 92% 54% / 0.45);--r:0.875rem;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{font-family:'Inter Tight',sans-serif;background:var(--bg);color:var(--fg);line-height:1.6;font-size:15px}
h1,h2,h3,h4{font-family:'Geist',sans-serif;letter-spacing:-0.035em;font-weight:600}a{color:var(--fg);text-decoration:none}
.cbar{background:var(--fg);color:rgba(255,255,255,.75);padding:7px 24px;text-align:center;font-size:11.5px;position:fixed;top:0;left:0;right:0;z-index:200}
.cbar a{color:hsl(200 88% 75%);text-decoration:underline}.cbar strong{color:rgba(255,255,255,.92)}
.age-pill{display:inline-block;background:#c0392b;color:#fff;font-weight:700;font-size:10px;padding:1px 7px;border-radius:3px;margin-right:8px;vertical-align:middle}
header{position:fixed;top:36px;left:0;right:0;z-index:100;background:hsl(205 60% 96% / 0.85);backdrop-filter:blur(20px);border-bottom:1px solid hsl(205 40% 86% / 0.40)}
.nav-inner{max-width:80rem;margin:0 auto;padding:0 clamp(16px,2.5vw,40px);height:80px;display:flex;align-items:center;justify-content:space-between;gap:24px}
.nav-logo img{height:72px;width:auto}.nav-links{display:flex;align-items:center;gap:28px;font-size:14px;font-weight:500}
.nav-links a{color:hsl(215 45% 16% / 0.70);transition:color .15s}.nav-links a:hover,.nav-links a.active{color:var(--primary)}
.btn-nav{background:var(--grad-gold);color:var(--primary-fg);font-family:'Geist',sans-serif;font-weight:600;font-size:13px;padding:8px 18px;border-radius:8px;border:none;cursor:pointer;box-shadow:var(--shadow-gold);white-space:nowrap;text-decoration:none}
.page-wrap{max-width:52rem;margin:0 auto;padding:calc(36px + 80px + clamp(32px,5vw,64px)) clamp(16px,3vw,32px) 60px}
.breadcrumb{font-size:12px;color:var(--muted-fg);margin-bottom:24px;display:flex;align-items:center;gap:6px}.breadcrumb a{color:var(--primary)}
.article-eyebrow{display:flex;align-items:center;gap:10px;margin-bottom:20px}
.eyebrow-line{height:1px;width:40px;background:var(--primary)}
.eyebrow-text{font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.2em;color:var(--primary)}
.article-title{font-family:'Geist',sans-serif;font-weight:700;font-size:clamp(28px,4vw,44px);letter-spacing:-0.035em;line-height:1.1;margin-bottom:16px}
.article-title .serif-accent{font-family:'Instrument Serif',serif;font-style:italic;font-weight:400;color:var(--primary)}
.article-meta{font-size:13px;color:var(--muted-fg);margin-bottom:32px;padding-bottom:24px;border-bottom:1px solid var(--border)}
.match-card{background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:24px;margin-bottom:20px;box-shadow:var(--shadow-card)}
.match-card:hover{box-shadow:0 8px 32px -8px hsl(215 50% 30% / 0.16)}
.match-card.featured{border-color:var(--primary);border-width:2px}
.match-header{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-bottom:16px;flex-wrap:wrap}
.match-teams{font-family:'Geist',sans-serif;font-weight:700;font-size:20px;letter-spacing:-0.02em;color:var(--fg)}
.match-info{font-size:12px;color:var(--muted-fg);font-family:'JetBrains Mono',monospace}
.tip-badge{display:inline-flex;align-items:center;gap:4px;background:var(--grad-gold);color:var(--primary-fg);font-family:'JetBrains Mono',monospace;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;padding:4px 12px;border-radius:100px;box-shadow:var(--shadow-gold)}
.match-body{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px}
.match-section-title{font-family:'JetBrains Mono',monospace;font-size:9.5px;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:var(--primary);margin-bottom:6px}
.match-text{font-size:13.5px;color:var(--muted-fg);line-height:1.6}
.suggested-bets{grid-column:1/-1;background:hsl(205 55% 90% / 0.40);border:1px solid var(--border);border-radius:8px;padding:14px}
.bet-row{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:6px 0;border-bottom:1px solid hsl(205 40% 86% / 0.50);flex-wrap:wrap}
.bet-row:last-child{border-bottom:none}.bet-left{display:flex;flex-direction:column;gap:2px}
.bet-desc{font-size:13px;color:var(--fg);font-weight:500}.bet-sub{font-size:11px;color:var(--muted-fg)}
.bet-cta{display:inline-flex;align-items:center;background:var(--grad-gold);color:var(--primary-fg);font-family:'Geist',sans-serif;font-weight:600;font-size:12px;padding:6px 14px;border-radius:6px;box-shadow:var(--shadow-gold);white-space:nowrap;transition:transform .15s;text-decoration:none}
.bet-cta:hover{transform:scale(1.02)}
.cgm-strip{font-size:10.5px;color:var(--muted-fg);font-style:italic;text-align:center;margin-top:10px}
.cgm-strip a{color:var(--primary);text-decoration:underline}
.section-hd{font-family:'Geist',sans-serif;font-weight:700;font-size:22px;letter-spacing:-0.025em;margin:40px 0 16px;padding-bottom:12px;border-bottom:2px solid var(--fg)}
.lead-text{font-size:16px;color:var(--muted-fg);line-height:1.75;margin-bottom:24px}
.pick-box{background:var(--grad-gold);border-radius:var(--r);padding:20px 24px;margin:24px 0;box-shadow:var(--shadow-gold)}
.pick-box-title{font-family:'Geist',sans-serif;font-weight:700;font-size:13px;text-transform:uppercase;letter-spacing:.08em;color:var(--primary-fg);opacity:.75;margin-bottom:4px}
.pick-box-pick{font-family:'Geist',sans-serif;font-weight:800;font-size:22px;letter-spacing:-0.02em;color:var(--primary-fg)}
.pick-box-sub{font-size:13px;color:var(--primary-fg);opacity:.80;margin-top:4px}
.bm-block{margin:40px 0 0;padding:24px;background:var(--card);border:1px solid var(--border);border-radius:var(--r);box-shadow:var(--shadow-card)}
.bm-row-s{display:flex;align-items:center;gap:12px;padding:10px;background:var(--muted);border-radius:8px;margin-bottom:8px}
.bm-row-s img{width:36px;height:36px;border-radius:8px;object-fit:contain;background:#fff;flex-shrink:0}
.cta-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:14px}
.cta-dark{display:flex;align-items:center;justify-content:center;background:hsl(215 45% 16%);color:#fff;border-radius:8px;padding:12px;font-size:13px;font-weight:700;text-decoration:none}
.cta-gold{display:flex;align-items:center;justify-content:center;background:var(--grad-gold);color:hsl(215 45% 16%);border-radius:8px;padding:12px;font-size:13px;font-weight:700;text-decoration:none;box-shadow:var(--shadow-gold)}
.resp-bar{background:hsl(205 55% 90% / 0.40);border-top:1px solid var(--border);padding:20px clamp(16px,3vw,40px);font-size:13px;color:var(--muted-fg);text-align:center;line-height:1.7;margin-top:60px}
.resp-bar a{color:var(--primary);text-decoration:underline}.resp-bar strong{color:var(--fg)}
footer.pg{background:var(--fg);padding:32px clamp(16px,3vw,40px);text-align:center}
footer.pg a{color:var(--primary);font-size:13px;margin:0 12px}
footer.pg p{font-size:11.5px;color:rgba(255,255,255,.4);margin-top:12px;line-height:1.7}
@media(max-width:640px){.match-body{grid-template-columns:1fr}.nav-links{display:none}.match-header{flex-direction:column;align-items:flex-start}.cta-grid{grid-template-columns:1fr}}
</style>"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800;900&family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">'

CGM_MESSAGES = [
    "Think. Is this a bet you really want to place?",
    "Chances are you're about to lose.",
    "Think. Is this a bet you really want to place?",
    "Chances are you're about to lose.",
]


def build_match_card(m, index, is_featured=False):
    key_news_html = '<br>'.join(m.get('key_news', []))
    bets = m.get('bets', [])
    bet_rows = ''
    for b in bets:
        bet_rows += f'''<div class="bet-row"><div class="bet-left"><span class="bet-desc">{b["desc"]}</span><span class="bet-sub">{b.get("sub","")}</span></div><a href="/best-betting-sites-australia.html" class="bet-cta">Bet Now →</a></div>\n'''

    odds_title = f'{m["home"]} {m["h2h_home"]} · {m["away"]} {m["h2h_away"]} · Line: {m["line"]}'
    cgm = CGM_MESSAGES[index % len(CGM_MESSAGES)]
    slug = m.get('match_slug', '')
    match_link = f'<a href="/{slug}.html" style="display:inline-block;margin-top:14px;font-size:13px;font-weight:600;color:var(--primary);border:1px solid var(--primary);border-radius:6px;padding:6px 14px;">Full Analysis & Team Lists →</a>' if slug else ''
    featured_class = ' featured' if is_featured else ''

    return f'''<div class="match-card{featured_class}">
  <div class="match-header">
    <div>
      <div class="match-teams">{m["home"]} v {m["away"]}</div>
      <div class="match-info">{m["date"]} · {m["time"]} AEST · {m["venue"]}</div>
    </div>
    <span class="tip-badge">⭐ Our Tip: {m["tip"]}</span>
  </div>
  <div class="match-body">
    <div>
      <div class="match-section-title">Analysis</div>
      <div class="match-text">{m["analysis"]}</div>
    </div>
    <div>
      <div class="match-section-title">Key News</div>
      <div class="match-text">{key_news_html}</div>
    </div>
    <div class="suggested-bets">
      <div class="match-section-title">Suggested Bets · {odds_title}</div>
      {bet_rows}
      <div class="cgm-strip">{cgm} · <a href="https://www.gamblinghelponline.org.au" target="_blank" rel="noopener">Free support: 1800 858 858</a></div>
      {match_link}
    </div>
  </div>
</div>'''


def build_page():
    sport_upper = SPORT.upper()
    sport_emoji = "🏉" if SPORT == "nrl" else "🦘"
    tips_url = f"/{SPORT}-tips.html"
    ladder_url = f"/{SPORT}-ladder-2026.html"
    hub_filename = f"{SPORT}-round-{ROUND_NUM}-tips-2026.html"
    slug = f"{SPORT}-round-{ROUND_NUM}-tips-2026"
    canonical = f"{BASE}/{hub_filename}"
    bye_note = f" · Bye: {BYE_TEAM}" if BYE_TEAM else ""
    n = len(MATCHES)

    # Featured match = last match in MATCH_OF_ROUND["title"] first word match, or just first match
    motd_teams = MATCH_OF_ROUND["title"].split("—")[0].strip() if "—" in MATCH_OF_ROUND["title"] else ""

    title = f"{sport_upper} {ROUND_LABEL} Tips 2026 — All {n} Games | PuntGuide"
    desc = f"{sport_upper} {ROUND_LABEL} 2026 tips and best bets for all {n} games. Confirmed team lists, analysis and predictions for {DATES}."

    match_cards = ''
    for i, m in enumerate(MATCHES):
        is_featured = motd_teams and (m['home'] in motd_teams or m['away'] in motd_teams)
        match_cards += build_match_card(m, i, is_featured) + '\n'

    nav_active_link = f'<a href="/{hub_filename}" class="active">{sport_emoji} {sport_upper} {ROUND_LABEL}</a>'
    other_sport = "afl" if SPORT == "nrl" else "nrl"
    other_emoji = "🦘" if SPORT == "nrl" else "🏉"

    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/png" sizes="32x32" href="/pg-icon.png">
{FONTS}
{CSS}
<meta property="og:title" content="{sport_upper} {ROUND_LABEL} Tips 2026 | PuntGuide">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="article">
<meta property="og:image" content="{BASE}/puntguide-logo.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{sport_upper} {ROUND_LABEL} Tips 2026 | PuntGuide">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{BASE}/puntguide-logo.png">
<meta name="robots" content="index, follow">
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"Article","headline":f"{sport_upper} {ROUND_LABEL} Tips 2026","description":desc,"author":{"@type":"Organization","name":"PuntGuide"},"publisher":{"@type":"Organization","name":"PuntGuide","logo":{"@type":"ImageObject","url":f"{BASE}/puntguide-logo.png"}},"datePublished":"2026-01-01","dateModified":UPDATED.replace(" ","T").split("T")[0],"mainEntityOfPage":canonical})}</script>
</head>
<body>

<div class="cbar">
  <span class="age-pill">18+</span>
  Gambling involves risk. <strong>For free and confidential support call <a href="tel:1800858858">1800 858 858</a> or visit <a href="https://www.gamblinghelponline.org.au" target="_blank" rel="noopener">gamblinghelponline.org.au</a></strong>
  &nbsp;·&nbsp; <a href="https://www.betstop.gov.au" target="_blank" rel="noopener">Self-exclude via BetStop</a>
</div>

<header>
  <div class="nav-inner">
    <a href="/index.html" class="nav-logo"><img src="/puntguide-logo.png" alt="PuntGuide"></a>
    <nav class="nav-links">
      <a href="/index.html">Home</a>
      {nav_active_link}
      <a href="/{other_sport}-tips.html">{other_emoji} {other_sport.upper()} Tips</a>
      <a href="/horse-racing-tips-today.html">🏇 Racing</a>
      <a href="/{SPORT}-premiership-odds-2026.html">{sport_upper} Futures</a>
    </nav>
    <a href="/all-betting-sites.html" class="btn-nav">Bet Now →</a>
  </div>
</header>

<div class="page-wrap">
  <div class="breadcrumb">
    <a href="/index.html">Home</a> › <a href="{tips_url}">{sport_upper} Tips 2026</a> › <span>{sport_upper} {ROUND_LABEL} Tips — All {n} Games</span>
  </div>

<div class="article-eyebrow"><span class="eyebrow-line"></span><span class="eyebrow-text">{sport_upper} · {ROUND_LABEL} · {DATES}</span></div>
<h1 class="article-title">{sport_upper} {ROUND_LABEL} Tips, Predictions <span class="serif-accent">&amp; Best Bets</span></h1>
<div class="article-meta">By PuntGuide Editorial · Updated {UPDATED} · Confirmed team lists · All tips are independent</div>

<p class="lead-text">{INTRO}</p>

<div class="pick-box">
  <div class="pick-box-title">Match of the Round</div>
  <div class="pick-box-pick">{MATCH_OF_ROUND["title"]}</div>
  <div class="pick-box-sub">{MATCH_OF_ROUND["subtitle"]}</div>
</div>

<h2 class="section-hd">All {ROUND_LABEL} Matches</h2>

{match_cards}

<div class="bm-block">
  <div class="match-section-title" style="margin-bottom:12px;">Best Bookmakers for {sport_upper} {ROUND_LABEL}</div>
  <div class="bm-row-s"><img src="/sportsbet.png" alt="Sportsbet"><div style="flex:1;font-size:13px;"><strong>Sportsbet</strong> — widest {sport_upper} market, best same-game multis</div><a href="/review-sportsbet.html" class="bet-cta" style="font-size:11px;padding:5px 12px;">Review →</a></div>
  <div class="bm-row-s"><img src="/pointsbet.png" alt="PointsBet"><div style="flex:1;font-size:13px;"><strong>PointsBet</strong> — sharp {sport_upper} odds, PointsBetting on player stats</div><a href="/review-pointsbet.html" class="bet-cta" style="font-size:11px;padding:5px 12px;">Review →</a></div>
  <div class="bm-row-s"><img src="/betr.png" alt="betr"><div style="flex:1;font-size:13px;"><strong>betr</strong> — best same-game multi builder for {sport_upper} in Australia</div><a href="/review-betr.html" class="bet-cta" style="font-size:11px;padding:5px 12px;">Review →</a></div>
  <div class="cta-grid">
    <a href="/best-betting-sites-australia.html" class="cta-dark">🏆 Best Betting Sites →</a>
    <a href="/all-betting-sites.html" class="cta-gold">📋 All 130+ Bookmakers →</a>
  </div>
</div>

</div>

<div class="resp-bar">
  <strong>Responsible Gambling:</strong> Set deposit limits before you start. Only bet what you can afford to lose.
  Free 24/7 support: <a href="tel:1800858858">1800 858 858</a> · <a href="https://www.gamblinghelponline.org.au" target="_blank" rel="noopener">gamblinghelponline.org.au</a> · Self-exclude: <a href="https://www.betstop.gov.au" target="_blank" rel="noopener">BetStop.gov.au</a>
  <br>Tips are editorial opinions only. PuntGuide earns commissions from affiliate links.
</div>

<footer class="pg">
  <a href="{tips_url}">{sport_upper} Tips 2026</a>
  <a href="{ladder_url}">{sport_upper} Ladder 2026</a>
  <a href="/best-betting-sites-for-{SPORT}.html">Best for {sport_upper}</a>
  <a href="/best-betting-sites-australia.html">Best Betting Sites</a>
  <a href="/about.html">About</a>
  <p>© 2026 PuntGuide · Independent Australian betting guide · 18+ only · <a href="/editorial-policy.html">Editorial Policy</a></p>
</footer>

<script src="/nav-drawer.js"></script>
</body></html>"""


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    hub_filename = f"{SPORT}-round-{ROUND_NUM}-tips-2026.html"
    page = build_page()
    with open(hub_filename, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"Written: {hub_filename}")
    print(f"Matches: {len(MATCHES)}")
    print(f"Next: add match pages for each fixture, then git add + push")
