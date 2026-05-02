#!/usr/bin/env python3
"""
PuntGuide — programmatic page generator
Reads data/afl_2026.json and data/nrl_2026.json.
Generates:
  - Match prediction pages for every match
  - Round hub pages listing all matches with links
Preserves files > 22 KB (existing rich content).
Never overwrites existing individual match pages.
"""

import json, os
from datetime import datetime

# ─── Config ──────────────────────────────────────────────────────────────────
RICH_THRESHOLD = 22_000   # bytes — files larger than this are preserved
SITE = "https://puntguide.com.au"

# ─── Load data ────────────────────────────────────────────────────────────────
with open("data/afl_2026.json") as f:
    afl_data = json.load(f)
with open("data/nrl_2026.json") as f:
    nrl_data = json.load(f)

# ─── Team lookup maps ─────────────────────────────────────────────────────────
AFL_TEAMS = {t["squiggle"]: t for t in afl_data["teams"]}
NRL_TEAMS = {t["short"]: t for t in nrl_data["teams"]}

# ─── Helpers ──────────────────────────────────────────────────────────────────
def fmt_date(d):
    return datetime.strptime(d, "%Y-%m-%d").strftime("%A, %-d %B %Y")

def fmt_date_short(d):
    return datetime.strptime(d, "%Y-%m-%d").strftime("%-d %b")

def fmt_time(t):
    return datetime.strptime(t, "%H:%M").strftime("%-I:%M %p")

def afl_t(name):
    return AFL_TEAMS.get(name, {"name": name, "slug": name.lower().replace(" ", "-"),
                                "abbr": name[:4].upper(), "short": name.split()[0]})

def nrl_t(name):
    return NRL_TEAMS.get(name, {"name": name, "slug": name.lower().replace(" ", "-"),
                                "abbr": name[:3].upper(), "short": name})

def safe_write(path, content, overwrite_stubs=True):
    """Write file unless it's rich content (>RICH_THRESHOLD)."""
    if os.path.exists(path):
        size = os.path.getsize(path)
        if size > RICH_THRESHOLD:
            return "skip-rich"
        if not overwrite_stubs:
            return "skip-exists"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return "written"

# ─── Shared CSS & nav elements ────────────────────────────────────────────────
BASE_CSS = """<style>
:root{--bg:hsl(205 60% 96%);--fg:hsl(215 45% 16%);--primary:hsl(48 92% 64%);--pfg:hsl(215 45% 16%);--muted:hsl(205 40% 92%);--muted-fg:hsl(215 20% 42%);--accent:hsl(200 88% 58%);--border:hsl(205 40% 86%);--gg:linear-gradient(135deg,hsl(50 96% 72%),hsl(44 92% 60%));--sg:0 10px 40px -10px hsl(48 92% 54%/.4);--sc:0 4px 24px -8px hsl(215 50% 30%/.1);--ch:36px;--nh:80px;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--fg);font-family:"Inter Tight",sans-serif;line-height:1.65;font-size:15px;}
h1,h2,h3{font-family:"Geist",sans-serif;letter-spacing:-0.03em;}
a{color:inherit;}img{max-width:100%;}
.cb{position:fixed;top:0;left:0;right:0;height:var(--ch);background:hsl(215 45% 16%);color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 24px;font-size:11px;z-index:200;gap:12px;}
.cb-t{font-weight:700;color:var(--primary);}.cb-h{color:hsl(205 40% 70%);}.cb-h a{color:var(--accent);text-decoration:none;}
.cb-b{display:flex;gap:6px;}.cb-b span{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);border-radius:4px;padding:2px 6px;font-size:10px;font-weight:700;}
.nav{position:fixed;top:var(--ch);left:0;right:0;height:var(--nh);background:hsl(205 60% 96%/.9);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;padding:0 40px;z-index:100;}
.nav-logo img{height:72px;width:auto;}.nav-links{display:flex;gap:20px;list-style:none;}
.nav-links a{font-size:13px;font-weight:500;color:hsl(215 45% 16%/.7);text-decoration:none;transition:color .2s;}.nav-links a:hover{color:var(--primary);}
.btn-g{display:inline-flex;align-items:center;background:var(--gg);color:var(--pfg);font-size:13px;font-weight:700;padding:9px 18px;border-radius:10px;border:none;cursor:pointer;text-decoration:none;box-shadow:var(--sg);white-space:nowrap;}
.pb{padding-top:calc(var(--ch) + var(--nh));}
.hero{padding:44px 32px 36px;background:radial-gradient(ellipse at top,hsl(200 85% 88%),hsl(205 70% 96%) 70%);border-bottom:1px solid var(--border);}
.hero-in{max-width:1100px;margin:0 auto;}.bc{font-size:12px;color:var(--muted-fg);margin-bottom:10px;}.bc a{color:var(--muted-fg);text-decoration:none;}
.eye{display:flex;align-items:center;gap:10px;margin-bottom:12px;}.eye-l{height:1px;width:32px;background:var(--primary);}
.eye-t{font-family:"JetBrains Mono",monospace;font-size:11px;color:var(--primary);text-transform:uppercase;letter-spacing:.2em;}
.wrap{max-width:1100px;margin:0 auto;padding:44px 32px 80px;}
.upd{font-size:11px;color:var(--muted-fg);font-family:"JetBrains Mono",monospace;margin-top:8px;}
.section{background:#fff;border:1px solid var(--border);border-radius:14px;padding:24px 28px;margin:24px 0;box-shadow:var(--sc);}
.section h2{font-size:20px;font-weight:700;margin-bottom:14px;padding-bottom:10px;border-bottom:1px solid var(--border);}
.match-hero{display:flex;align-items:center;justify-content:center;gap:20px;padding:28px;background:hsl(215 45% 16%);border-radius:14px;margin:24px 0;color:#fff;text-align:center;}
.team-block{flex:1;}.team-name{font-size:22px;font-weight:800;font-family:"Geist",sans-serif;letter-spacing:-0.03em;}
.team-short{font-size:11px;color:rgba(255,255,255,.6);margin-top:4px;font-family:"JetBrains Mono",monospace;}
.vs-block{font-size:28px;font-weight:800;color:var(--primary);font-family:"Geist",sans-serif;}
.match-meta{display:flex;gap:12px;flex-wrap:wrap;margin-top:16px;justify-content:center;}
.meta-chip{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:6px;padding:4px 10px;font-size:12px;}
.odds-row{display:flex;gap:10px;flex-wrap:wrap;margin:12px 0;}
.odds-card{flex:1;min-width:120px;background:var(--muted);border-radius:10px;padding:14px;text-align:center;}
.odds-label{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:6px;}
.odds-val{font-size:22px;font-weight:800;font-family:"JetBrains Mono",monospace;color:var(--fg);}
.tip-box{background:hsl(140 40% 96%);border:2px solid hsl(140 50% 40%);border-radius:12px;padding:20px 24px;margin:16px 0;}
.tip-label{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:hsl(140 50% 35%);margin-bottom:6px;}
.tip-content{font-size:16px;font-weight:700;}
.match-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px;margin:16px 0;}
.match-card{background:var(--muted);border-radius:12px;padding:16px 18px;border:1px solid var(--border);transition:box-shadow .2s;}
.match-card:hover{box-shadow:var(--sc);}
.mc-teams{font-size:15px;font-weight:700;margin-bottom:6px;}
.mc-teams a{text-decoration:none;color:var(--fg);}
.mc-teams a:hover{color:var(--accent);}
.mc-meta{font-size:12px;color:var(--muted-fg);}
.mc-badge{display:inline-block;background:hsl(215 45% 16%);color:var(--primary);font-size:10px;font-weight:700;padding:2px 7px;border-radius:4px;font-family:"JetBrains Mono",monospace;margin-top:6px;}
.bk-row{display:flex;flex-direction:column;gap:10px;}
.bk-card{display:flex;align-items:center;gap:14px;padding:12px;background:var(--muted);border-radius:10px;}
.bk-card img{width:44px;height:44px;border-radius:10px;object-fit:contain;background:#fff;flex-shrink:0;}
.bk-info{flex:1;}.bk-name{font-weight:700;margin-bottom:2px;}.bk-desc{font-size:13px;color:var(--muted-fg);}
.int-links{background:#fff;border:1px solid var(--border);border-radius:12px;padding:18px 22px;margin:28px 0;}
.int-links h3{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--muted-fg);margin-bottom:12px;}
.int-links a{display:inline-block;background:var(--muted);border-radius:6px;padding:5px 11px;margin:3px;font-size:13px;font-weight:500;text-decoration:none;color:var(--fg);}
.faq{margin:44px 0;}.faq h2{font-size:22px;font-weight:700;margin-bottom:20px;}
.faq-item{border:1px solid var(--border);border-radius:10px;margin-bottom:8px;overflow:hidden;}
.faq-q{width:100%;text-align:left;background:#fff;border:none;padding:14px 18px;font-size:14px;font-weight:600;cursor:pointer;display:flex;justify-content:space-between;align-items:center;font-family:"Inter Tight",sans-serif;color:var(--fg);}
.fi{font-size:18px;color:var(--muted-fg);}.faq-a{padding:0 18px 14px;font-size:14px;line-height:1.75;color:hsl(215 45% 16%/.8);display:none;}.faq-a.open{display:block;}
.site-footer{background:hsl(215 45% 16%);color:rgba(255,255,255,.7);padding:44px 32px 28px;margin-top:72px;}
.footer-in{max-width:1100px;margin:0 auto;}.footer-logo{height:44px;width:auto;margin-bottom:14px;filter:brightness(0) invert(1);opacity:.75;}
.footer-desc{font-size:13px;line-height:1.7;max-width:400px;margin-bottom:28px;}
.footer-links{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:28px;}.footer-links a{font-size:13px;color:rgba(255,255,255,.55);text-decoration:none;}
.footer-rg{font-size:11px;color:rgba(255,255,255,.4);border-top:1px solid rgba(255,255,255,.1);padding-top:20px;line-height:1.8;}.footer-rg a{color:rgba(255,255,255,.4);}
@media(max-width:768px){.nav-links{display:none;}.wrap,.hero{padding-left:16px;padding-right:16px;}.nav{padding:0 20px;}.match-hero{flex-direction:column;gap:12px;}.team-name{font-size:18px;}}
</style>"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800&family=Inter+Tight:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">'

CB = '<div class="cb"><span class="cb-t">Bet Responsibly</span><span class="cb-h">Gambling Help: <a href="tel:1800858858">1800 858 858</a> · <a href="https://www.gamblinghelponline.org.au" target="_blank">gamblinghelponline.org.au</a></span><div class="cb-b"><span>18+</span><span>AUS ONLY</span></div></div>'

FAQ_JS = '<script>document.querySelectorAll(".faq-q").forEach(b=>b.addEventListener("click",function(){const a=this.nextElementSibling;a.classList.toggle("open");this.querySelector(".fi").textContent=a.classList.contains("open")?"−":"+";}));</script>'

FOOTER_LINKS_AFL = '''<a href="/afl-tips.html">AFL Tips 2026</a>
  <a href="/afl-ladder-2026.html">AFL Ladder</a>
  <a href="/afl-premiership-odds-2026.html">AFL Premiership Odds</a>
  <a href="/best-betting-sites-for-afl.html">Best Sites for AFL</a>
  <a href="/best-betting-sites-australia.html">Best Betting Sites</a>'''

FOOTER_LINKS_NRL = '''<a href="/nrl-tips.html">NRL Tips 2026</a>
  <a href="/nrl-ladder-2026.html">NRL Ladder</a>
  <a href="/best-betting-sites-for-nrl.html">Best Sites for NRL</a>
  <a href="/best-betting-sites-australia.html">Best Betting Sites</a>'''

BOOKMAKERS = [
    ("Sportsbet", "/sportsbet.png", "Australia's most popular — widest market range for AFL & NRL"),
    ("PointsBet", "/pointsbet.png", "Sharp odds + PointsBetting on player stats"),
    ("betr", "/betr.png", "Best same-game multi builder in Australia"),
]

def bk_html(sport):
    rows = ""
    for name, img, desc in BOOKMAKERS:
        rows += f'''<div class="bk-card"><img src="{img}" alt="{name}"><div class="bk-info"><div class="bk-name">{name}</div><div class="bk-desc">{desc}</div></div><a href="/best-betting-sites-australia.html" class="btn-g" style="font-size:12px;padding:7px 13px">Bet Now →</a></div>\n'''
    return rows

def nav_html(sport):
    if sport == "afl":
        links = '''<li><a href="/afl-tips.html">AFL Tips</a></li><li><a href="/afl-ladder-2026.html">AFL Ladder</a></li><li><a href="/afl-premiership-odds-2026.html">AFL Odds</a></li><li><a href="/best-betting-sites-for-afl.html">Best for AFL</a></li><li><a href="/all-betting-sites.html">All Sites</a></li>'''
    else:
        links = '''<li><a href="/nrl-tips.html">NRL Tips</a></li><li><a href="/nrl-ladder-2026.html">NRL Ladder</a></li><li><a href="/best-betting-sites-for-nrl.html">Best for NRL</a></li><li><a href="/all-betting-sites.html">All Sites</a></li>'''
    return f'<nav class="nav"><a href="/index.html" class="nav-logo"><img src="/puntguide-logo.png" alt="PuntGuide"></a><ul class="nav-links">{links}</ul><a href="/best-betting-sites-australia.html" class="btn-g">Bet Now →</a></nav>'

def footer_html(sport, desc):
    fl = FOOTER_LINKS_AFL if sport == "afl" else FOOTER_LINKS_NRL
    return f'''<footer class="site-footer"><div class="footer-in">
<img src="/puntguide-logo.png" alt="PuntGuide" class="footer-logo">
<p class="footer-desc">{desc}</p>
<div class="footer-links">{fl}</div>
<div class="footer-rg">Gamble responsibly. Call <a href="tel:1800858858">Gambling Help 1800 858 858</a> or visit <a href="https://www.gamblinghelponline.org.au" target="_blank">gamblinghelponline.org.au</a>. 18+ only.</div>
</div></footer>'''

# ─── Match prediction page ─────────────────────────────────────────────────────
def gen_match_page(sport, rnd, match, home, away):
    rn = rnd["round"]
    rl = rnd["label"]
    date_fmt = fmt_date(match["date"])
    time_fmt = fmt_time(match["time"])
    venue = match.get("venue", "TBC")
    iso_dt = f"{match['date']}T{match['time']}:00+10:00"

    if sport == "afl":
        league = "AFL"
        home_name = home["name"]
        away_name = away["name"]
        home_short = home.get("short", home["name"].split()[0])
        away_short = away.get("short", away["name"].split()[0])
        sport_label = "Australian Rules Football"
        hub_url = f"/{rnd['slug']}.html"
        hub_label = f"{league} {rl} Tips 2026"
        tips_url = "/afl-tips.html"
        sites_url = "/best-betting-sites-for-afl.html"
        sites_label = "Best AFL Betting Sites"
        footer_desc = f"{home_name} vs {away_name} prediction and tips — {league} {rl} 2026."
        nav = nav_html("afl")
    else:
        league = "NRL"
        home_name = home["name"]
        away_name = away["name"]
        home_short = home.get("short", home["name"].split()[0])
        away_short = away.get("short", away["name"].split()[0])
        sport_label = "Rugby League"
        hub_url = f"/{rnd['slug']}.html"
        hub_label = f"{league} {rl} Tips 2026"
        tips_url = "/nrl-tips.html"
        sites_url = "/best-betting-sites-for-nrl.html"
        sites_label = f"Best NRL Betting Sites"
        footer_desc = f"{home_name} vs {away_name} prediction and tips — {league} {rl} 2026."
        nav = nav_html("nrl")

    title = f"{home_name} vs {away_name} Prediction & Tips — {league} {rl} 2026 | PuntGuide"
    desc_meta = f"Expert {home_name} vs {away_name} prediction for {league} {rl} 2026. Odds comparison, best bet and analysis. {date_fmt} at {venue}."
    slug_file = match_fn(sport, home, away, rn, rl)
    canonical = f"{SITE}/{slug_file}"

    schema_event = json.dumps({
        "@context": "https://schema.org",
        "@type": "SportsEvent",
        "name": f"{home_name} vs {away_name}",
        "startDate": iso_dt,
        "location": {"@type": "Place", "name": venue, "address": {"@type": "PostalAddress", "addressCountry": "AU"}},
        "sport": sport_label,
        "competitor": [{"@type": "SportsTeam", "name": home_name}, {"@type": "SportsTeam", "name": away_name}],
        "organizer": {"@type": "Organization", "name": league},
        "description": desc_meta
    })

    schema_faq = json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": f"Who will win {home_short} vs {away_short}?",
             "acceptedAnswer": {"@type": "Answer", "text": f"Our {home_name} vs {away_name} tip and full analysis will be published in the days before {rl} 2026. Check back for our expert prediction, odds comparison and best bet recommendation."}},
            {"@type": "Question", "name": f"When is {home_short} vs {away_short} {league} {rl} 2026?",
             "acceptedAnswer": {"@type": "Answer", "text": f"{home_name} vs {away_name} kicks off at {time_fmt} on {date_fmt} at {venue}."}},
            {"@type": "Question", "name": f"Where can I bet on {home_short} vs {away_short}?",
             "acceptedAnswer": {"@type": "Answer", "text": f"You can bet on {home_name} vs {away_name} with Sportsbet, PointsBet and betr. Compare odds across all three before placing. Always bet responsibly — 18+ only."}},
            {"@type": "Question", "name": f"What are the best bookmakers for {league} betting?",
             "acceptedAnswer": {"@type": "Answer", "text": f"For {league} betting, Sportsbet has the widest market range, PointsBet offers sharp odds and PointsBetting on player stats, and betr has the best same-game multi builder in Australia."}}
        ]
    })

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc_meta}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{home_name} vs {away_name} — {league} {rl} 2026 | PuntGuide">
<meta property="og:description" content="{desc_meta}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="article">
<meta name="robots" content="index, follow">
<link rel="icon" type="image/png" href="/pg-icon.png">
{FONTS}
<script type="application/ld+json">{schema_event}</script>
<script type="application/ld+json">{schema_faq}</script>
{BASE_CSS}
</head>
<body>
{CB}
{nav}
<div class="pb">
<div class="hero"><div class="hero-in">
  <div class="bc"><a href="/index.html">Home</a> › <a href="{tips_url}">{league} 2026</a> › <a href="{hub_url}">{rl} Tips</a> › {home_short} vs {away_short}</div>
  <div class="eye"><span class="eye-l"></span><span class="eye-t">{league} {rl} · {date_fmt}</span></div>
  <h1>{home_name} vs {away_name} Prediction</h1>
  <p style="font-size:16px;color:hsl(215 45% 16%/.65);max-width:700px;line-height:1.8;margin-top:10px">{league} {rl} 2026 — {home_name} host {away_name} at {venue}. Expert prediction, odds comparison and best bet recommendation.</p>
  <p class="upd">{time_fmt} · {date_fmt} · {venue}</p>
</div></div>

<div class="wrap">

  <div class="match-hero">
    <div class="team-block">
      <div class="team-name">{home_name}</div>
      <div class="team-short">HOME</div>
    </div>
    <div class="vs-block">VS</div>
    <div class="team-block">
      <div class="team-name">{away_name}</div>
      <div class="team-short">AWAY</div>
    </div>
    <div class="match-meta" style="position:absolute;display:none">
      <span class="meta-chip">📅 {date_fmt}</span>
      <span class="meta-chip">⏰ {time_fmt}</span>
      <span class="meta-chip">📍 {venue}</span>
    </div>
  </div>

  <div style="display:flex;gap:10px;flex-wrap:wrap;margin:-10px 0 20px;font-size:13px;">
    <span style="background:var(--muted);border-radius:6px;padding:5px 11px;">📅 {date_fmt}</span>
    <span style="background:var(--muted);border-radius:6px;padding:5px 11px;">⏰ {time_fmt} AEST</span>
    <span style="background:var(--muted);border-radius:6px;padding:5px 11px;">📍 {venue}</span>
  </div>

  <div class="section">
    <h2>Match Preview</h2>
    <p style="font-size:14px;line-height:1.8;color:var(--muted-fg);margin-bottom:12px">Full tips and analysis for {home_name} vs {away_name} will be published in the days leading up to {rl} 2026. We cover team form, head-to-head records, key players, venue factors and best bet recommendations for every {league} match.</p>
    <p style="font-size:14px;line-height:1.8;">In the meantime, check our <a href="{hub_url}" style="color:var(--accent)">{league} {rl} Tips hub</a> for all matches this round, or visit our <a href="{sites_url}" style="color:var(--accent)">{sites_label}</a> page to compare the best odds for this match.</p>
  </div>

  <div class="section">
    <h2>Odds — {home_short} vs {away_short}</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:14px">Live odds from Australia's top bookmakers. Compare before you bet.</p>
    <div class="odds-row">
      <div class="odds-card">
        <div class="odds-label">{home_short} Win</div>
        <div class="odds-val" style="color:var(--accent)">—</div>
        <div style="font-size:11px;color:var(--muted-fg);margin-top:4px">Updated pre-match</div>
      </div>
      <div class="odds-card">
        <div class="odds-label">Draw</div>
        <div class="odds-val">—</div>
        <div style="font-size:11px;color:var(--muted-fg);margin-top:4px">Where applicable</div>
      </div>
      <div class="odds-card">
        <div class="odds-label">{away_short} Win</div>
        <div class="odds-val" style="color:var(--accent)">—</div>
        <div style="font-size:11px;color:var(--muted-fg);margin-top:4px">Updated pre-match</div>
      </div>
    </div>
    <p style="font-size:11px;color:var(--muted-fg);margin-top:8px">Odds update in the week of the match. Always compare across Sportsbet, PointsBet and betr for best value. 18+ · Bet Responsibly.</p>
  </div>

  <div class="section">
    <h2>Our Tip</h2>
    <div class="tip-box">
      <div class="tip-label">Best Bet — {league} {rl} 2026</div>
      <div class="tip-content">Full prediction published ahead of {rl}. Subscribe to PuntGuide for tips direct to your inbox.</div>
    </div>
    <p style="font-size:13px;color:var(--muted-fg);margin-top:12px">Our tips consider team form, head-to-head records, venue history, injury news and market value. We back value — not just favourites.</p>
  </div>

  <div class="section">
    <h2>Best Bookmakers for This Match</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:14px">Compare odds for {home_name} vs {away_name} across Australia's top licensed bookmakers.</p>
    <div class="bk-row">{bk_html(sport)}</div>
  </div>

  <div class="int-links"><h3>Related pages</h3>
    <a href="{hub_url}">{league} {rl} Tips 2026</a>
    <a href="{tips_url}">{league} Tips 2026</a>
    <a href="{sites_url}">{sites_label}</a>
    <a href="/best-betting-sites-australia.html">Best Betting Sites</a>
    <a href="/all-betting-sites.html">All 130+ Bookmakers</a>
  </div>

  <div class="faq">
    <h2>Frequently asked questions</h2>
    <div class="faq-item"><button class="faq-q">Who will win {home_short} vs {away_short}? <span class="fi">+</span></button><div class="faq-a">Our {home_name} vs {away_name} tip will be published in the days before {rl} 2026. Check back for our expert prediction based on form, head-to-head and odds value.</div></div>
    <div class="faq-item"><button class="faq-q">When and where is {home_short} vs {away_short} playing? <span class="fi">+</span></button><div class="faq-a">{home_name} vs {away_name} kicks off at {time_fmt} AEST on {date_fmt} at {venue}.</div></div>
    <div class="faq-item"><button class="faq-q">Where can I bet on {league} in Australia? <span class="fi">+</span></button><div class="faq-a">You can bet on {league} with Sportsbet, PointsBet and betr — all licensed Australian bookmakers. Compare odds before placing. 18+ only. Gamble responsibly.</div></div>
    <div class="faq-item"><button class="faq-q">What markets are available for {home_short} vs {away_short}? <span class="fi">+</span></button><div class="faq-a">Standard markets include head-to-head winner, line betting, over/under total points, first try scorer (NRL) or first goal scorer (AFL), and same-game multis. Sportsbet has the widest market range for {league}.</div></div>
  </div>

</div>
</div>
{footer_html(sport, footer_desc)}
{FAQ_JS}
<script src="/nav-drawer.js"></script>
</body></html>"""

# ─── Round hub page ────────────────────────────────────────────────────────────
def gen_round_hub(sport, rnd, match_infos):
    rn = rnd["round"]
    rl = rnd["label"]
    matches = rnd["matches"]
    bye = rnd.get("bye", "")

    if sport == "afl":
        league = "AFL"
        tips_url = "/afl-tips.html"
        ladder_url = "/afl-ladder-2026.html"
        sites_url = "/best-betting-sites-for-afl.html"
        sites_label = "Best AFL Betting Sites"
        footer_desc = f"{league} {rl} 2026 — tips, predictions and odds for all matches."
        nav = nav_html("afl")
        fl = FOOTER_LINKS_AFL
    else:
        league = "NRL"
        tips_url = "/nrl-tips.html"
        ladder_url = "/nrl-ladder-2026.html"
        sites_url = "/best-betting-sites-for-nrl.html"
        sites_label = "Best NRL Betting Sites"
        footer_desc = f"{league} {rl} 2026 — tips, predictions and odds for all matches."
        nav = nav_html("nrl")
        fl = FOOTER_LINKS_NRL

    # first/last date of round
    dates = sorted(set(m["date"] for m in matches))
    first_date = fmt_date_short(dates[0])
    last_date = fmt_date_short(dates[-1])
    n_matches = len(matches)

    title = f"{league} {rl} Tips 2026 — Predictions for All {n_matches} Matches | PuntGuide"
    desc_meta = f"Expert {league} {rl} 2026 tips and predictions. All {n_matches} matches with odds comparison, best bets and analysis. {first_date}–{last_date}."
    slug_file = rnd["slug"] + ".html"
    canonical = f"{SITE}/{slug_file}"

    schema_faq = json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": f"What {league} matches are in {rl} 2026?",
             "acceptedAnswer": {"@type": "Answer", "text": f"{league} {rl} 2026 features {n_matches} matches played {first_date}–{last_date}. " + (f"The bye team is {bye}. " if bye else "") + "See above for the full fixture and links to match tips."}},
            {"@type": "Question", "name": f"Who are the best bookmakers for {league} {rl}?",
             "acceptedAnswer": {"@type": "Answer", "text": f"Sportsbet, PointsBet and betr are our top picks for {league} betting in Australia. Compare odds across all three for best value on {rl} 2026."}},
            {"@type": "Question", "name": f"Where can I find {league} {rl} 2026 tips?",
             "acceptedAnswer": {"@type": "Answer", "text": f"PuntGuide publishes expert {league} tips for every game in {rl} 2026. Our analysis covers team form, head-to-head records, venue factors and betting market value."}}
        ]
    })

    # build match cards
    cards = ""
    for m, (home, away) in zip(matches, match_infos):
        fn = match_fn(sport, home, away, rn, rl)
        home_short = home.get("short", home["name"].split()[0])
        away_short = away.get("short", away["name"].split()[0])
        date_s = fmt_date_short(m["date"])
        time_s = fmt_time(m["time"])
        venue_s = m.get("venue", "TBC")
        cards += f'''<div class="match-card">
  <div class="mc-teams"><a href="/{fn}">{home["name"]} vs {away["name"]}</a></div>
  <div class="mc-meta">📅 {date_s} · ⏰ {time_s} AEST<br>📍 {venue_s}</div>
  <a href="/{fn}" class="mc-badge">Tips & Prediction →</a>
</div>\n'''

    bye_note = f'<p style="font-size:13px;color:var(--muted-fg);margin-top:12px"><strong>Bye:</strong> {bye}</p>' if bye else ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc_meta}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{league} {rl} Tips 2026 | PuntGuide">
<meta property="og:description" content="{desc_meta}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="article">
<meta name="robots" content="index, follow">
<link rel="icon" type="image/png" href="/pg-icon.png">
{FONTS}
<script type="application/ld+json">{schema_faq}</script>
{BASE_CSS}
</head>
<body>
{CB}
{nav}
<div class="pb">
<div class="hero"><div class="hero-in">
  <div class="bc"><a href="/index.html">Home</a> › <a href="{tips_url}">{league} 2026</a> › {rl} Tips</div>
  <div class="eye"><span class="eye-l"></span><span class="eye-t">{league} 2026 · {rl}</span></div>
  <h1>{league} {rl} Tips 2026</h1>
  <p style="font-size:16px;color:hsl(215 45% 16%/.65);max-width:700px;line-height:1.8;margin-top:10px">Expert tips and predictions for all {n_matches} matches in {league} {rl} 2026. Odds comparison, best bets and analysis for every game — {first_date} to {last_date}.</p>
  <p class="upd">{n_matches} matches · {first_date}–{last_date}{(' · Bye: ' + bye) if bye else ''}</p>
</div></div>

<div class="wrap">

  <div class="section">
    <h2>{rl} — All Matches & Tips</h2>
    <div class="match-grid">{cards}</div>
    {bye_note}
  </div>

  <div class="section">
    <h2>Best Bookmakers for {league} Betting</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:14px">Compare odds across Australia's top licensed bookmakers before placing on {rl} 2026.</p>
    <div class="bk-row">{bk_html(sport)}</div>
  </div>

  <div class="int-links"><h3>Related {league} pages</h3>
    <a href="{tips_url}">{league} Tips 2026</a>
    <a href="{ladder_url}">{league} Ladder 2026</a>
    <a href="{sites_url}">{sites_label}</a>
    <a href="/best-betting-sites-australia.html">Best Betting Sites</a>
    <a href="/all-betting-sites.html">All 130+ Bookmakers</a>
  </div>

  <div class="faq">
    <h2>Frequently asked questions</h2>
    <div class="faq-item"><button class="faq-q">What {league} matches are in {rl} 2026? <span class="fi">+</span></button><div class="faq-a">{league} {rl} 2026 features {n_matches} matches played from {first_date} to {last_date}.{(' Bye: ' + bye + '.') if bye else ''} See the full fixture listing above for all match details and tip links.</div></div>
    <div class="faq-item"><button class="faq-q">Which bookmaker has the best {league} odds? <span class="fi">+</span></button><div class="faq-a">Sportsbet has the widest {league} market range. PointsBet often has the sharpest head-to-head odds. betr is best for same-game multis. Always compare before betting. 18+ · Bet responsibly.</div></div>
    <div class="faq-item"><button class="faq-q">How do I bet on {league} in Australia? <span class="fi">+</span></button><div class="faq-a">To bet on {league} in Australia, open an account with a licensed bookmaker such as Sportsbet, PointsBet or betr. You must be 18 or over. Compare odds before placing and always bet within your means.</div></div>
  </div>

</div>
</div>
{footer_html(sport, footer_desc)}
{FAQ_JS}
<script src="/nav-drawer.js"></script>
</body></html>"""

# ─── Filename helpers ─────────────────────────────────────────────────────────
def match_fn(sport, home, away, round_n, round_label):
    hs = home["slug"]
    as_ = away["slug"]
    if round_n == 0:
        return f"{sport}-{hs}-vs-{as_}-opening-round-2026.html"
    return f"{sport}-{hs}-vs-{as_}-round-{round_n}-2026.html"

# ─── Main generation loop ─────────────────────────────────────────────────────
def run(sport, data, team_fn):
    written_match = 0
    written_hub = 0
    skipped_rich = 0
    skipped_exists = 0

    for rnd in data["rounds"]:
        rn = rnd["round"]
        rl = rnd["label"]
        matches = rnd["matches"]

        # Resolve team objects
        match_infos = []
        for m in matches:
            home = team_fn(m["home"])
            away = team_fn(m["away"])
            match_infos.append((home, away))

        # 1. Match prediction pages (never overwrite existing)
        for m, (home, away) in zip(matches, match_infos):
            fn = match_fn(sport, home, away, rn, rl)
            html = gen_match_page(sport, rnd, m, home, away)
            result = safe_write(fn, html, overwrite_stubs=False)
            if result == "written":
                written_match += 1
            elif result == "skip-rich":
                skipped_rich += 1
            elif result == "skip-exists":
                skipped_exists += 1

        # 2. Round hub page (overwrite stubs, preserve rich)
        hub_fn = rnd["slug"] + ".html"
        hub_html = gen_round_hub(sport, rnd, match_infos)
        result = safe_write(hub_fn, hub_html, overwrite_stubs=True)
        if result == "written":
            written_hub += 1
        elif result == "skip-rich":
            skipped_rich += 1

    print(f"{sport.upper()} — match pages written: {written_match}, skipped (exists): {skipped_exists}, skipped (rich): {skipped_rich}")
    print(f"{sport.upper()} — round hubs written: {written_hub}, skipped (rich): 0")
    return written_match + written_hub

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    total = 0
    total += run("afl", afl_data, afl_t)
    total += run("nrl", nrl_data, nrl_t)
    print(f"\nTotal pages written: {total}")
