#!/usr/bin/env python3
"""
AFL Match Page Generator
Usage: edit ROUND and MATCHES below, then run python3 generate_afl_matches.py
"""
import os, json

OUT  = os.path.expanduser('~/puntguide')
SITE = 'https://puntguide.com.au'

# ─── ROUND CONFIG ─────────────────────────────────────────────────────────────

ROUND      = 8
ROUND_YEAR = 2026
ROUND_SLUG = f'afl-round-{ROUND}-tips-{ROUND_YEAR}'

# ─── TEAM DATA ────────────────────────────────────────────────────────────────

TEAMS = {
    'Collingwood':      dict(short='COLL', colour='#000000', ground='MCG'),
    'Hawthorn':         dict(short='HAW',  colour='#4D2004', ground='MCG'),
    'Western Bulldogs': dict(short='WB',   colour='#014896', ground='Marvel Stadium'),
    'Fremantle':        dict(short='FRE',  colour='#2A1A5E', ground='Optus Stadium'),
    'Adelaide Crows':   dict(short='ADEL', colour='#002B5C', ground='Adelaide Oval'),
    'Port Adelaide':    dict(short='PORT', colour='#008AAB', ground='Adelaide Oval'),
    'Essendon':         dict(short='ESS',  colour='#CC2529', ground='Marvel Stadium'),
    'Brisbane Lions':   dict(short='BL',   colour='#A30046', ground='Gabba'),
    'West Coast Eagles':dict(short='WCE',  colour='#003087', ground='Optus Stadium'),
    'Richmond':         dict(short='RICH', colour='#FFD200', ground='MCG'),
    'Geelong Cats':     dict(short='GEE',  colour='#1C3F6E', ground='GMHBA Stadium'),
    'North Melbourne':  dict(short='NM',   colour='#003A6B', ground='Marvel Stadium'),
    'Carlton':          dict(short='CARL', colour='#002147', ground='MCG'),
    'St Kilda':         dict(short='STK',  colour='#ED0F05', ground='Marvel Stadium'),
    'Sydney Swans':     dict(short='SYD',  colour='#CC0000', ground='SCG'),
    'Melbourne':        dict(short='MELB', colour='#CC2529', ground='MCG'),
    'Gold Coast SUNS':  dict(short='GCS',  colour='#E8281B', ground='People First Stadium'),
    'GWS GIANTS':       dict(short='GWS',  colour='#F15C22', ground='ENGIE Stadium'),
}

# ─── MATCH DATA ───────────────────────────────────────────────────────────────
# status: 'result' | 'upcoming'
# result: 'TEAM1_SCORE, TEAM2_SCORE' (if played)
# tip: which team to tip (for upcoming matches)
# tip_margin: expected margin
# analysis: 2-3 sentence match preview/analysis

MATCHES = [
    dict(
        team1='Collingwood', team2='Hawthorn',
        date='Thursday, April 30, 2026', time=None, venue='MCG',
        status='result', result='COLL 93, HAW 93',
        tip=None, tip_margin=None,
        analysis="Collingwood and Hawthorn produced one of the most memorable draws in recent AFL history, finishing level at 93 points each. Both teams showed incredible resilience with the Magpies and Hawks trading blows all game. The draw leaves both sides with 4 wins and 4 draws heading into the next round.",
    ),
    dict(
        team1='Western Bulldogs', team2='Fremantle',
        date='Friday, May 1, 2026', time='7:30 PM', venue='Marvel Stadium',
        status='upcoming', result=None,
        tip='Western Bulldogs', tip_margin='1–15',
        analysis="The Western Bulldogs enjoy a significant home-ground advantage at Marvel Stadium, where they've been in strong form in 2026. Fremantle travel cross-country for this Friday night clash, which historically hurts West Australian sides. The Bulldogs' forward line has been among the competition's most potent and should be too good here.",
    ),
    dict(
        team1='Adelaide Crows', team2='Port Adelaide',
        date='Friday, May 1, 2026', time='8:10 PM', venue='Adelaide Oval',
        status='upcoming', result=None,
        tip='Adelaide Crows', tip_margin='1–15',
        analysis="The Showdown is always one of the AFL's most fiercely contested fixtures. Adelaide Oval will be packed for this Friday night derby between the Crows and Power. Both sides have had inconsistent seasons so far in 2026, making this one of the hardest games of the round to predict. Home-side edge goes to the Crows in a rivalry game.",
    ),
    dict(
        team1='Essendon', team2='Brisbane Lions',
        date='Saturday, May 2, 2026', time='12:35 PM', venue='Marvel Stadium',
        status='upcoming', result=None,
        tip='Brisbane Lions', tip_margin='1–15',
        analysis="Brisbane travel to Marvel Stadium as slight favourites despite the away trip. The Lions have been one of the more consistent sides in 2026 and their experienced list should handle the Essendon pressure. The Bombers will make this competitive at home but the Lions' class through the midfield should get them over the line.",
    ),
    dict(
        team1='West Coast Eagles', team2='Richmond',
        date='Saturday, May 2, 2026', time='4:15 PM', venue='Optus Stadium',
        status='upcoming', result=None,
        tip='West Coast Eagles', tip_margin='15+',
        analysis="West Coast at Optus Stadium is a formidable proposition for any visiting side. Richmond are in a rebuilding phase in 2026 and the cross-country trip to Perth compounds the challenge. The Eagles have made Optus Stadium a genuine fortress and should win this one comfortably.",
    ),
    dict(
        team1='Geelong Cats', team2='North Melbourne',
        date='Saturday, May 2, 2026', time='4:35 PM', venue='GMHBA Stadium',
        status='upcoming', result=None,
        tip='Geelong Cats', tip_margin='15+',
        analysis="Geelong at GMHBA Stadium against North Melbourne shapes as a mismatch. The Cats have been in terrific form in 2026 and GMHBA Stadium is one of the competition's most intimidating home grounds. North Melbourne are still developing their young list and should struggle to stay with Geelong all day.",
    ),
    dict(
        team1='Carlton', team2='St Kilda',
        date='Saturday, May 2, 2026', time='7:35 PM', venue='Marvel Stadium',
        status='upcoming', result=None,
        tip='Carlton', tip_margin='1–15',
        analysis="Carlton host St Kilda in a Saturday night Marvel Stadium blockbuster. The Blues have genuine finals ambitions in 2026 and their strong forward line should cause St Kilda's defence significant problems. The Saints have shown fight in 2026 but Carlton's quality at the MCG and Marvel Stadium has been consistent.",
    ),
    dict(
        team1='Sydney Swans', team2='Melbourne',
        date='Sunday, May 3, 2026', time='3:15 PM', venue='SCG',
        status='upcoming', result=None,
        tip='Sydney Swans', tip_margin='1–15',
        analysis="Sydney at the SCG are always difficult to beat and Melbourne face a tough afternoon in harbour city. The Swans have been strong at home in 2026 and their contested ball work is among the best in the competition. Melbourne have had an up-and-down season and the SCG trip looms as a stern test.",
    ),
    dict(
        team1='Gold Coast SUNS', team2='GWS GIANTS',
        date='Sunday, May 3, 2026', time='7:20 PM', venue='People First Stadium',
        status='upcoming', result=None,
        tip='GWS GIANTS', tip_margin='1–15',
        analysis="GWS GIANTS head to Gold Coast for this Sunday evening clash. The Giants have been one of the stronger sides in 2026 and despite playing away from home, their experience should see them through. Gold Coast have shown improvement in 2026 but the Giants' even-season form makes them the value pick here.",
    ),
]

# ─── SHARED CSS ───────────────────────────────────────────────────────────────

CSS = """:root{--bg:hsl(205 60% 96%);--fg:hsl(215 45% 16%);--primary:hsl(48 92% 64%);--pfg:hsl(215 45% 16%);--muted:hsl(205 40% 92%);--muted-fg:hsl(215 20% 42%);--accent:hsl(200 88% 58%);--border:hsl(205 40% 86%);--gg:linear-gradient(135deg,hsl(50 96% 72%),hsl(44 92% 60%));--sg:0 10px 40px -10px hsl(48 92% 54%/.4);--sc:0 4px 24px -8px hsl(215 50% 30%/.1);--ch:36px;--nh:80px;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--fg);font-family:"Inter Tight",sans-serif;line-height:1.65;font-size:15px;}
h1,h2,h3,h4{font-family:"Geist",sans-serif;letter-spacing:-0.03em;}
a{color:inherit;}
img{max-width:100%;}
.cb{position:fixed;top:0;left:0;right:0;height:var(--ch);background:hsl(215 45% 16%);color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 24px;font-size:11px;z-index:200;gap:12px;}
.cb-t{font-weight:700;color:var(--primary);}
.cb-h{color:hsl(205 40% 70%);}
.cb-h a{color:var(--accent);text-decoration:none;}
.cb-b{display:flex;gap:6px;}
.cb-b span{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);border-radius:4px;padding:2px 6px;font-size:10px;font-weight:700;}
.nav{position:fixed;top:var(--ch);left:0;right:0;height:var(--nh);background:hsl(205 60% 96%/.9);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;padding:0 40px;z-index:100;}
.nav-logo img{height:72px;width:auto;}
.nav-links{display:flex;gap:20px;list-style:none;}
.nav-links a{font-size:13px;font-weight:500;color:hsl(215 45% 16%/.7);text-decoration:none;transition:color .2s;}
.nav-links a:hover{color:var(--primary);}
.btn-g{display:inline-flex;align-items:center;background:var(--gg);color:var(--pfg);font-size:13px;font-weight:700;padding:9px 18px;border-radius:10px;border:none;cursor:pointer;text-decoration:none;box-shadow:var(--sg);white-space:nowrap;}
.pb{padding-top:calc(var(--ch) + var(--nh));}
.hero{padding:44px 32px 36px;background:radial-gradient(ellipse at top,hsl(200 85% 88%),hsl(205 70% 96%) 70%);border-bottom:1px solid var(--border);}
.hero-in{max-width:1100px;margin:0 auto;}
.bc{font-size:12px;color:var(--muted-fg);margin-bottom:10px;}
.bc a{color:var(--muted-fg);text-decoration:none;}
.eye{display:flex;align-items:center;gap:10px;margin-bottom:12px;}
.eye-l{height:1px;width:32px;background:var(--primary);}
.eye-t{font-family:"JetBrains Mono",monospace;font-size:11px;color:var(--primary);text-transform:uppercase;letter-spacing:.2em;}
.wrap{max-width:1100px;margin:0 auto;padding:44px 32px 80px;}
.matchup{background:#fff;border:1px solid var(--border);border-radius:16px;padding:28px;margin:28px 0;box-shadow:var(--sc);text-align:center;}
.teams{display:flex;align-items:center;justify-content:center;gap:24px;margin-bottom:16px;flex-wrap:wrap;}
.team-block{display:flex;flex-direction:column;align-items:center;gap:8px;}
.team-badge{width:64px;height:64px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:14px;color:#fff;flex-shrink:0;}
.team-name{font-weight:700;font-size:15px;max-width:120px;text-align:center;}
.vs{font-family:"JetBrains Mono",monospace;font-size:18px;font-weight:700;color:var(--muted-fg);}
.match-meta{display:flex;justify-content:center;gap:20px;flex-wrap:wrap;font-size:13px;color:var(--muted-fg);border-top:1px solid var(--border);padding-top:14px;margin-top:4px;}
.match-meta span{display:flex;align-items:center;gap:5px;}
.result-score{font-family:"Geist",sans-serif;font-size:28px;font-weight:800;letter-spacing:-0.04em;color:var(--fg);margin:8px 0;}
.tip-box{background:hsl(140 50% 97%);border:1px solid hsl(140 50% 85%);border-radius:12px;padding:20px 24px;margin:20px 0;}
.tip-box h3{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:hsl(140 50% 32%);margin-bottom:8px;}
.tip-team{font-size:22px;font-weight:800;color:hsl(140 40% 28%);margin-bottom:4px;}
.tip-margin{font-size:13px;color:hsl(140 40% 40%);}
.card{background:#fff;border:1px solid var(--border);border-radius:14px;padding:20px 24px;margin-bottom:16px;box-shadow:var(--sc);}
.bm-row{display:flex;align-items:center;gap:14px;}
.bm-logo{width:44px;height:44px;border-radius:10px;object-fit:contain;background:#fff;box-shadow:var(--sc);flex-shrink:0;}
.int-links{background:#fff;border:1px solid var(--border);border-radius:12px;padding:18px 22px;margin:28px 0;}
.int-links h3{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--muted-fg);margin-bottom:12px;}
.int-links a{display:inline-block;background:var(--muted);border-radius:6px;padding:5px 11px;margin:3px;font-size:13px;font-weight:500;text-decoration:none;color:var(--fg);}
.faq{margin:44px 0;}
.faq h2{font-size:22px;font-weight:700;margin-bottom:20px;}
.faq-item{border:1px solid var(--border);border-radius:10px;margin-bottom:8px;overflow:hidden;}
.faq-q{width:100%;text-align:left;background:#fff;border:none;padding:14px 18px;font-size:14px;font-weight:600;cursor:pointer;display:flex;justify-content:space-between;align-items:center;font-family:"Inter Tight",sans-serif;color:var(--fg);}
.fi{font-size:18px;color:var(--muted-fg);}
.faq-a{padding:0 18px 14px;font-size:14px;line-height:1.75;color:hsl(215 45% 16%/.8);display:none;}
.faq-a.open{display:block;}
.site-footer{background:hsl(215 45% 16%);color:rgba(255,255,255,.7);padding:44px 32px 28px;margin-top:72px;}
.footer-in{max-width:1100px;margin:0 auto;}
.footer-logo{height:44px;width:auto;margin-bottom:14px;filter:brightness(0) invert(1);opacity:.75;}
.footer-desc{font-size:13px;line-height:1.7;max-width:400px;margin-bottom:28px;}
.footer-links{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:28px;}
.footer-links a{font-size:13px;color:rgba(255,255,255,.55);text-decoration:none;}
.footer-rg{font-size:11px;color:rgba(255,255,255,.4);border-top:1px solid rgba(255,255,255,.1);padding-top:20px;line-height:1.8;}
.footer-rg a{color:rgba(255,255,255,.4);}
@media(max-width:768px){.nav-links{display:none;}.wrap,.hero{padding-left:16px;padding-right:16px;}.nav{padding:0 20px;}.teams{gap:12px;}}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800&family=Inter+Tight:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">'

TOP_BOOKMAKERS = [
    dict(name='PointsBet', slug='pointsbet', logo='pointsbet.png', tagline='Sharpest AFL odds + PointsBetting markets'),
    dict(name='Sportsbet',  slug='sportsbet',  logo='sportsbet.png',  tagline='Widest AFL market range in Australia'),
    dict(name='Ladbrokes',  slug='ladbrokes',  logo='ladbrokes.png',  tagline='Consistently competitive head-to-head prices'),
]

def team_slug(name):
    return name.lower().replace(' ', '-').replace('.', '')

def match_slug(m):
    t1 = team_slug(m['team1'])
    t2 = team_slug(m['team2'])
    return f"afl-{t1}-vs-{t2}-round-{ROUND}-{ROUND_YEAR}.html"

def faq_schema(faqs):
    items = ','.join([f'{{"@type":"Question","name":{json.dumps(q)},"acceptedAnswer":{{"@type":"Answer","text":{json.dumps(a)}}}}}' for q,a in faqs])
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{items}]}}</script>'

def article_schema(title, desc, slug):
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":{json.dumps(title)},"description":{json.dumps(desc)},"author":{{"@type":"Organization","name":"PuntGuide"}},"publisher":{{"@type":"Organization","name":"PuntGuide","logo":{{"@type":"ImageObject","url":"{SITE}/favicon-192.png"}}}},"datePublished":"2026-04-30","dateModified":"2026-05-01","mainEntityOfPage":"{SITE}/{slug}","image":{{"@type":"ImageObject","url":"{SITE}/favicon-192.png"}}}}</script>'

def build_match_page(m):
    slug    = match_slug(m)
    t1      = m['team1']
    t2      = m['team2']
    t1d     = TEAMS.get(t1, dict(short=t1[:4].upper(), colour='#333', ground='TBC'))
    t2d     = TEAMS.get(t2, dict(short=t2[:4].upper(), colour='#333', ground='TBC'))
    is_done = m['status'] == 'result'

    if is_done:
        title = f"{t1} vs {t2} Result — AFL Round {ROUND} {ROUND_YEAR} | PuntGuide"
        desc  = f"{t1} vs {t2} AFL Round {ROUND} result: {m['result']}. Full match analysis and what it means for the season."
        h1    = f"{t1} vs {t2} — AFL Round {ROUND} Result"
        eyebrow = f"AFL Round {ROUND} · {m['date']}"
    else:
        title = f"{t1} vs {t2} Tips & Odds — AFL Round {ROUND} {ROUND_YEAR} | PuntGuide"
        desc  = f"{t1} vs {t2} AFL Round {ROUND} tips, odds, and predictions. Our analysts break down the key matchups, best bets, and top bookmakers for this game."
        h1    = f"{t1} vs {t2} Tips & Prediction"
        eyebrow = f"AFL Round {ROUND} · {m['date']} · {m.get('time','')}"

    faqs = []
    if is_done:
        faqs = [
            (f"What was the result of {t1} vs {t2}?",
             f"{t1} vs {t2} in AFL Round {ROUND} {ROUND_YEAR} finished: {m['result']}."),
            (f"Where was {t1} vs {t2} played?",
             f"{t1} vs {t2} was played at {m['venue']} on {m['date']}."),
            (f"How did {t1} perform in Round {ROUND}?",
             f"{m['analysis']}"),
            (f"What AFL betting sites covered {t1} vs {t2}?",
             f"All major Australian bookmakers including PointsBet, Sportsbet, and Ladbrokes offered markets on {t1} vs {t2} in AFL Round {ROUND}."),
            (f"Where can I bet on upcoming AFL games?",
             f"PointsBet, Sportsbet, and Ladbrokes are the top-rated Australian bookmakers for AFL betting. Compare odds across multiple accounts for the best value on every match."),
        ]
    else:
        faqs = [
            (f"Who will win {t1} vs {t2} in AFL Round {ROUND}?",
             f"Our analysis tips {m['tip']} to win {t1} vs {t2} in AFL Round {ROUND} {ROUND_YEAR} by {m['tip_margin']} points. {m['analysis']}"),
            (f"When is {t1} vs {t2} being played?",
             f"{t1} vs {t2} is scheduled for {m['date']} at {m.get('time','TBC')} at {m['venue']}."),
            (f"Where is {t1} vs {t2} being played?",
             f"{t1} vs {t2} in AFL Round {ROUND} {ROUND_YEAR} is being played at {m['venue']}."),
            (f"What are the best betting markets for {t1} vs {t2}?",
             f"The most popular markets for {t1} vs {t2} include head-to-head, line betting, and same-game multis. PointsBet offers PointsBetting markets on AFL stats like disposals and goals. Sportsbet has the widest SGM options."),
            (f"Which bookmaker has the best odds for {t1} vs {t2}?",
             f"Odds vary across bookmakers. Compare PointsBet, Sportsbet, and Ladbrokes before placing your bet on {t1} vs {t2} — all three are consistently competitive on AFL head-to-head markets."),
        ]

    # matchup box
    venue_str  = m['venue']
    time_str   = m.get('time') or 'Final'
    score_html = f'<div class="result-score">{m["result"]}</div>' if is_done else f'<div style="font-size:13px;font-weight:600;color:var(--primary);margin:8px 0">{time_str} · {m["date"]}</div>'

    matchup_html = f"""<div class="matchup">
  <div class="teams">
    <div class="team-block">
      <div class="team-badge" style="background:{t1d['colour']}">{t1d['short']}</div>
      <div class="team-name">{t1}</div>
    </div>
    <div class="vs">VS</div>
    <div class="team-block">
      <div class="team-badge" style="background:{t2d['colour']}">{t2d['short']}</div>
      <div class="team-name">{t2}</div>
    </div>
  </div>
  {score_html}
  <div class="match-meta">
    <span>🏟 {venue_str}</span>
    <span>📅 {m['date']}</span>
    <span>🏈 AFL Round {ROUND} {ROUND_YEAR}</span>
  </div>
</div>"""

    tip_html = ''
    if not is_done:
        tip_html = f"""<div class="tip-box">
  <h3>Our Tip</h3>
  <div class="tip-team">{m['tip']}</div>
  <div class="tip-margin">Expected margin: {m['tip_margin']} points</div>
  <p style="margin-top:10px;font-size:14px;line-height:1.7;color:hsl(215 45% 16%/.8)">{m['analysis']}</p>
  <p style="font-size:11px;color:hsl(140 40% 40%);margin-top:10px">Tips are editorial predictions only. Gamble responsibly. 18+.</p>
</div>"""

    bm_cards = ''
    for bm in TOP_BOOKMAKERS:
        bm_cards += f"""<div class="card">
  <div class="bm-row">
    <img src="/{bm['logo']}" alt="{bm['name']}" class="bm-logo">
    <div style="flex:1">
      <div style="font-weight:700;font-size:15px;margin-bottom:2px">{bm['name']}</div>
      <div style="font-size:13px;color:var(--muted-fg);margin-bottom:10px">{bm['tagline']}</div>
      <div style="display:flex;gap:10px">
        <a href="#" onclick="return false;" class="btn-g" style="font-size:12px;padding:7px 13px">Bet Now →</a>
        <a href="/review-{bm['slug']}.html" style="font-size:13px;color:var(--muted-fg);text-decoration:none;align-self:center">Full Review →</a>
      </div>
    </div>
  </div>
  <p style="font-size:11px;color:var(--muted-fg);margin-top:10px">"Think. Is this a bet you really want to place?" · 18+ · T&Cs apply</p>
</div>"""

    int_links_html = ''.join(f'<a href="{h}">{t}</a>' for t, h in [
        (f'AFL Round {ROUND} Tips', f'/afl-round-{ROUND}-tips-{ROUND_YEAR}.html'),
        ('Best AFL Betting Sites', '/best-betting-sites-for-afl.html'),
        ('Best Betting Sites Australia', '/best-betting-sites-australia.html'),
        ('Compare Betting Sites', '/compare-betting-sites.html'),
        ('PointsBet Review', '/review-pointsbet.html'),
        ('Sportsbet Review', '/review-sportsbet.html'),
        ('Ladbrokes Review', '/review-ladbrokes.html'),
    ])

    faq_items = ''.join(f'<div class="faq-item"><button class="faq-q">{q} <span class="fi">+</span></button><div class="faq-a">{a}</div></div>' for q,a in faqs)
    schema = faq_schema(faqs) + '\n' + article_schema(title, desc, slug)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{slug}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{slug}">
<meta property="og:type" content="article">
<meta name="robots" content="index, follow">
<link rel="icon" type="image/png" href="/pg-icon.png">
{FONTS}
{schema}
<style>{CSS}</style>
</head>
<body>
<div class="cb"><span class="cb-t">Bet Responsibly</span><span class="cb-h">Gambling Help: <a href="tel:1800858858">1800 858 858</a> · <a href="https://www.gamblinghelponline.org.au" target="_blank">gamblinghelponline.org.au</a></span><div class="cb-b"><span>18+</span><span>AUS ONLY</span></div></div>
<nav class="nav"><a href="/index.html" class="nav-logo"><img src="/puntguide-logo.png" alt="PuntGuide"></a><ul class="nav-links"><li><a href="/best-betting-sites-australia.html">Best Sites</a></li><li><a href="/best-betting-sites-for-afl.html">AFL</a></li><li><a href="/afl-round-{ROUND}-tips-{ROUND_YEAR}.html">Round {ROUND} Tips</a></li><li><a href="/best-betting-apps-australia.html">Best Apps</a></li><li><a href="/all-betting-sites.html">All Sites</a></li></ul><a href="/all-betting-sites.html" class="btn-g">Bet Now →</a></nav>
<div class="pb">
<div class="hero"><div class="hero-in">
  <div class="bc"><a href="/index.html">Home</a> › <a href="/afl-round-{ROUND}-tips-{ROUND_YEAR}.html">AFL Round {ROUND} Tips</a> › {t1} vs {t2}</div>
  <div class="eye"><span class="eye-l"></span><span class="eye-t">{eyebrow}</span></div>
  <h1>{h1}</h1>
  <p style="font-size:16px;color:hsl(215 45% 16%/.65);max-width:680px;line-height:1.75;margin-top:10px">{m['analysis']}</p>
</div></div>
<div class="wrap">
  {matchup_html}
  {tip_html}
  <h2 style="font-size:20px;font-weight:700;margin:32px 0 14px">Best bookmakers for this match</h2>
  {bm_cards}
  <div class="int-links"><h3>Related pages</h3>{int_links_html}</div>
  <div class="faq"><h2>Frequently asked questions</h2>{faq_items}</div>
</div>
</div>
<footer class="site-footer"><div class="footer-in">
<img src="/puntguide-logo.png" alt="PuntGuide" class="footer-logo">
<p class="footer-desc">Australia's most up-to-date guide to AFL betting — tips, odds, and the best bookmakers for every round.</p>
<div class="footer-links">
  <a href="/best-betting-sites-australia.html">Best Betting Sites</a>
  <a href="/best-betting-sites-for-afl.html">Best for AFL</a>
  <a href="/afl-round-{ROUND}-tips-{ROUND_YEAR}.html">AFL Round {ROUND} Tips</a>
  <a href="/compare-betting-sites.html">Compare Sites</a>
  <a href="/all-betting-sites.html">All 130 Bookmakers</a>
</div>
<div class="footer-rg">Gamble responsibly. Call <a href="tel:1800858858">Gambling Help 1800 858 858</a> or visit <a href="https://www.gamblinghelponline.org.au" target="_blank">gamblinghelponline.org.au</a>. Self-exclude at <a href="https://www.betstop.gov.au" target="_blank">BetStop.gov.au</a>. 18+ only. Tips are editorial predictions only.</div>
</div></footer>
<script>document.querySelectorAll('.faq-q').forEach(b=>b.addEventListener('click',function(){{const a=this.nextElementSibling;a.classList.toggle('open');this.querySelector('.fi').textContent=a.classList.contains('open')?'−':'+';}}));</script>
</body></html>"""

    path = os.path.join(OUT, slug)
    with open(path, 'w') as f:
        f.write(html)
    return slug

def update_sitemap(new_slugs):
    with open(os.path.join(OUT, 'sitemap.xml')) as f:
        existing = f.read()
    import re
    existing_locs = set(re.findall(r'<loc>([^<]+)</loc>', existing))
    additions = ''
    for slug in new_slugs:
        url = f'{SITE}/{slug}'
        if url not in existing_locs:
            additions += f'  <url><loc>{url}</loc><changefreq>daily</changefreq><priority>0.8</priority></url>\n'
    if additions:
        updated = existing.replace('</urlset>', additions + '</urlset>')
        with open(os.path.join(OUT, 'sitemap.xml'), 'w') as f:
            f.write(updated)

if __name__ == '__main__':
    generated = []
    print(f'\n── AFL Round {ROUND} Match Pages ──')
    for m in MATCHES:
        slug = build_match_page(m)
        generated.append(slug)
        print(f'  ✓ {slug}')
    update_sitemap(generated)
    print(f'\n✅ {len(generated)} match pages generated\n')
