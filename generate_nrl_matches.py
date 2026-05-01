#!/usr/bin/env python3
"""
NRL Match Page Generator
Usage: edit ROUND and MATCHES below, then run python3 generate_nrl_matches.py
"""
import os, json, re

OUT  = os.path.expanduser('~/puntguide')
SITE = 'https://puntguide.com.au'

ROUND      = 10
ROUND_YEAR = 2026
ROUND_SLUG = f'nrl-round-{ROUND}-tips-{ROUND_YEAR}'

TEAMS = {
    'Bulldogs':   dict(short='CBY', colour='#0057A8', full='Canterbury-Bankstown Bulldogs'),
    'Cowboys':    dict(short='NQC', colour='#003B6F', full='North Queensland Cowboys'),
    'Dolphins':   dict(short='DOL', colour='#CC0000', full='Redcliffe Dolphins'),
    'Storm':      dict(short='MEL', colour='#4B0082', full='Melbourne Storm'),
    'Titans':     dict(short='GCT', colour='#00263A', full='Gold Coast Titans'),
    'Raiders':    dict(short='CBR', colour='#6ABF4B', full='Canberra Raiders'),
    'Eels':       dict(short='PEE', colour='#0055A5', full='Parramatta Eels'),
    'Warriors':   dict(short='NZW', colour='#1A1A1A', full='New Zealand Warriors'),
    'Roosters':   dict(short='SYD', colour='#CC0000', full='Sydney Roosters'),
    'Broncos':    dict(short='BRI', colour='#4B0020', full='Brisbane Broncos'),
    'Knights':    dict(short='NEW', colour='#003A8C', full='Newcastle Knights'),
    'Rabbitohs':  dict(short='SSR', colour='#007A3D', full='South Sydney Rabbitohs'),
    'Sharks':     dict(short='CRO', colour='#00AEEF', full='Cronulla-Sutherland Sharks'),
    'Wests Tigers': dict(short='WST', colour='#FF6600', full='Wests Tigers'),
    'Panthers':   dict(short='PEN', colour='#1A1A1A', full='Penrith Panthers'),
    'Sea Eagles': dict(short='MAN', colour='#6B0020', full='Manly-Warringah Sea Eagles'),
}

MATCHES = [
    dict(
        team1='Bulldogs', team2='Cowboys',
        date='Friday, May 1, 2026', time='6:00 PM', venue='Accor Stadium, Sydney',
        status='upcoming', result=None,
        tip='Cowboys', tip_margin='1–12',
        analysis="The Cowboys travel to Accor Stadium as slight favourites over a rebuilding Bulldogs side. North Queensland have been one of the more consistent teams in 2026 and their experienced spine should control this game. The Bulldogs will be competitive at home but the Cowboys' class in the key positions should see them get the win.",
    ),
    dict(
        team1='Dolphins', team2='Storm',
        date='Friday, May 1, 2026', time='8:00 PM', venue='Suncorp Stadium, Brisbane',
        status='upcoming', result=None,
        tip='Storm', tip_margin='1–12',
        analysis="Melbourne Storm are the slight favourites for this Friday night clash at Suncorp Stadium. The Storm's formidable forward pack and elite defensive structure make them tough to beat regardless of venue. The Dolphins have shown plenty of heart in 2026 but face an enormous challenge against one of the NRL's powerhouse clubs.",
    ),
    dict(
        team1='Titans', team2='Raiders',
        date='Saturday, May 2, 2026', time='3:00 PM', venue='Cbus Super Stadium, Gold Coast',
        status='upcoming', result=None,
        tip='Raiders', tip_margin='1–12',
        analysis="Canberra Raiders travel to the Gold Coast with genuine confidence after a strong start to the 2026 season. The Titans have been inconsistent at home this year and the Raiders' powerful forward pack looms as a significant challenge. This is a tough game to call but the Raiders' depth and experience edges them in front.",
    ),
    dict(
        team1='Eels', team2='Warriors',
        date='Saturday, May 2, 2026', time='5:30 PM', venue='CommBank Stadium, Sydney',
        status='upcoming', result=None,
        tip='Eels', tip_margin='1–12',
        analysis="Parramatta Eels host the New Zealand Warriors at CommBank Stadium in what shapes as a competitive Saturday afternoon affair. The Eels enjoy strong home support and have been solid at CommBank in 2026. The Warriors have shown they can beat anyone but the cross-Tasman travel and Eels' home advantage gives Parramatta the edge.",
    ),
    dict(
        team1='Roosters', team2='Broncos',
        date='Saturday, May 2, 2026', time='7:35 PM', venue='Allianz Stadium, Sydney',
        status='upcoming', result=None,
        tip='Roosters', tip_margin='1–12',
        analysis="The Sydney Roosters host the Brisbane Broncos in one of the marquee Saturday night fixtures of Round 10. Allianz Stadium is a fortress for the Roosters and their talented roster should shine under the lights. The Broncos have genuine finals ambitions in 2026 but facing the Roosters in Sydney is always a major challenge.",
    ),
    dict(
        team1='Knights', team2='Rabbitohs',
        date='Sunday, May 3, 2026', time='2:00 PM', venue='McDonald Jones Stadium, Newcastle',
        status='upcoming', result=None,
        tip='Knights', tip_margin='1–12',
        analysis="Newcastle Knights look well-placed to claim victory over South Sydney Rabbitohs at McDonald Jones Stadium. The Knights have been strong at home in 2026 and their vocal home crowd gives them a significant advantage. The Rabbitohs have had an inconsistent season and a tough road trip to Newcastle looms as a step too far.",
    ),
    dict(
        team1='Sharks', team2='Wests Tigers',
        date='Sunday, May 3, 2026', time='4:05 PM', venue='Ocean Protect Stadium, Sydney',
        status='upcoming', result=None,
        tip='Sharks', tip_margin='13+',
        analysis="Cronulla Sharks are strong favourites to account for Wests Tigers at Ocean Protect Stadium. The Sharks have been one of the more consistent sides in the competition in 2026 while the Tigers are in a rebuilding phase. This shapes as a comfortable home win for Cronulla.",
    ),
    dict(
        team1='Panthers', team2='Sea Eagles',
        date='Sunday, May 3, 2026', time='6:15 PM', venue='CommBank Stadium, Sydney',
        status='upcoming', result=None,
        tip='Panthers', tip_margin='13+',
        analysis="Penrith Panthers are strong favourites to dispatch Manly-Warringah Sea Eagles at CommBank Stadium. The Panthers remain one of the NRL's benchmark teams in 2026 and their depth across the park is unmatched. Manly have shown improvement this season but facing the Panthers is a massive step up in class.",
    ),
    dict(
        team1='Dolphins', team2='Bulldogs',
        date='Thursday, May 7, 2026', time='7:50 PM', venue='Suncorp Stadium, Brisbane',
        status='upcoming', result=None,
        tip='Dolphins', tip_margin='1–12',
        analysis="The Dolphins host the Bulldogs at Suncorp Stadium in the Round 10 Thursday night opener. Suncorp is a difficult venue for visiting sides and the Dolphins have been strong at home in 2026. The Bulldogs have been competitive this season but the Dolphins' home-ground advantage and quality through the spine should be the difference.",
    ),
]

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
.team-badge{width:64px;height:64px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:13px;color:#fff;flex-shrink:0;}
.team-name{font-weight:700;font-size:15px;max-width:120px;text-align:center;}
.vs{font-family:"JetBrains Mono",monospace;font-size:18px;font-weight:700;color:var(--muted-fg);}
.match-meta{display:flex;justify-content:center;gap:20px;flex-wrap:wrap;font-size:13px;color:var(--muted-fg);border-top:1px solid var(--border);padding-top:14px;margin-top:4px;}
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
.int-links a:hover{background:var(--border);}
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
    dict(name='PointsBet', slug='pointsbet', logo='pointsbet.png', tagline='Sharpest NRL odds + unique PointsBetting markets'),
    dict(name='Sportsbet',  slug='sportsbet',  logo='sportsbet.png',  tagline='Widest NRL market range in Australia'),
    dict(name='betr',       slug='betr',       logo='betr.png',       tagline='Best-in-class NRL same-game multi builder'),
]

def team_slug(name):
    return name.lower().replace(' ', '-').replace('.', '')

def match_slug(m):
    t1 = team_slug(m['team1'])
    t2 = team_slug(m['team2'])
    date_slug = m['date'].lower().replace(',','').replace(' ','-')
    return f"nrl-{t1}-vs-{t2}-round-{ROUND}-{ROUND_YEAR}.html"

def faq_schema(faqs):
    items = ','.join([f'{{"@type":"Question","name":{json.dumps(q)},"acceptedAnswer":{{"@type":"Answer","text":{json.dumps(a)}}}}}' for q,a in faqs])
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{items}]}}</script>'

def article_schema(title, desc, slug):
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":{json.dumps(title)},"description":{json.dumps(desc)},"author":{{"@type":"Organization","name":"PuntGuide"}},"publisher":{{"@type":"Organization","name":"PuntGuide","logo":{{"@type":"ImageObject","url":"{SITE}/favicon-192.png"}}}},"datePublished":"2026-05-01","dateModified":"2026-05-01","mainEntityOfPage":"{SITE}/{slug}","image":{{"@type":"ImageObject","url":"{SITE}/favicon-192.png"}}}}</script>'

def build_match_page(m):
    slug  = match_slug(m)
    t1    = m['team1']
    t2    = m['team2']
    t1d   = TEAMS.get(t1, dict(short=t1[:3].upper(), colour='#333', full=t1))
    t2d   = TEAMS.get(t2, dict(short=t2[:3].upper(), colour='#333', full=t2))
    is_done = m['status'] == 'result'

    if is_done:
        title   = f"{t1} vs {t2} Result — NRL Round {ROUND} {ROUND_YEAR} | PuntGuide"
        desc    = f"{t1} vs {t2} NRL Round {ROUND} result: {m['result']}. Full match analysis and season implications."
        h1      = f"{t1} vs {t2} — NRL Round {ROUND} Result"
        eyebrow = f"NRL Round {ROUND} · {m['date']}"
    else:
        title   = f"{t1} vs {t2} Tips & Odds — NRL Round {ROUND} {ROUND_YEAR} | PuntGuide"
        desc    = f"{t1} vs {t2} NRL Round {ROUND} tips, odds and prediction. Expert analysis, best bets and top bookmakers for this match."
        h1      = f"{t1} vs {t2} Tips & Prediction"
        eyebrow = f"NRL Round {ROUND} · {m['date']} · {m.get('time','')}"

    faqs = []
    if is_done:
        faqs = [
            (f"What was the result of {t1} vs {t2}?",
             f"{t1} vs {t2} in NRL Round {ROUND} {ROUND_YEAR} finished: {m['result']}."),
            (f"Where was {t1} vs {t2} played?",
             f"The match was played at {m['venue']} on {m['date']}."),
            (f"How did {t1} perform in Round {ROUND}?", m['analysis']),
            (f"What NRL betting sites covered {t1} vs {t2}?",
             f"All major Australian bookmakers including PointsBet, Sportsbet, and betr offered markets on this match."),
            (f"Where can I bet on upcoming NRL matches?",
             f"PointsBet, Sportsbet, and betr are the top-rated Australian bookmakers for NRL betting. Compare odds across multiple accounts for the best value."),
        ]
    else:
        faqs = [
            (f"Who will win {t1} vs {t2} in NRL Round {ROUND}?",
             f"Our tip is {m['tip']} to win by {m['tip_margin']} points. {m['analysis']}"),
            (f"When and where is {t1} vs {t2} being played?",
             f"{t1} vs {t2} kicks off at {m.get('time','TBC')} on {m['date']} at {m['venue']}."),
            (f"What are the best betting markets for {t1} vs {t2}?",
             f"The most popular NRL markets include head-to-head, line betting, and same-game multis. PointsBet offers unique PointsBetting markets on NRL stats. betr and Sportsbet have the best SGM builders for NRL."),
            (f"Which bookmaker has the best NRL odds for {t1} vs {t2}?",
             f"Compare PointsBet, Sportsbet, and Ladbrokes before placing — all three are competitive on NRL head-to-head. betr is best for same-game multis on this match."),
            (f"Is {t1d['full']} playing at home in Round {ROUND}?",
             f"{'Yes' if 'Sydney' in m['venue'] or t1 in m['venue'] else 'Check the venue details above'}. {t1} {'host' if m['venue'] and t1.split()[0].lower() in m['venue'].lower() else 'play at'} {m['venue']} in NRL Round {ROUND} {ROUND_YEAR}."),
        ]

    time_str  = m.get('time') or 'Final'
    score_html = f'<div style="font-family:Geist,sans-serif;font-size:28px;font-weight:800;letter-spacing:-0.04em;margin:8px 0">{m["result"]}</div>' if is_done else f'<div style="font-size:13px;font-weight:600;color:var(--primary);margin:8px 0">{time_str} · {m["date"]}</div>'

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
    <span>🏟 {m['venue']}</span>
    <span>📅 {m['date']}</span>
    <span>🏉 NRL Round {ROUND} {ROUND_YEAR}</span>
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

    int_links_html = ''.join(f'<a href="{h}">{t}</a>' for t,h in [
        (f'NRL Round {ROUND} Tips', f'/nrl-round-{ROUND}-tips-{ROUND_YEAR}.html'),
        ('Best NRL Betting Sites', '/best-betting-sites-afl-nrl.html'),
        ('Best Betting Sites Australia', '/best-betting-sites-australia.html'),
        ('Compare Betting Sites', '/compare-betting-sites.html'),
        ('PointsBet Review', '/review-pointsbet.html'),
        ('Sportsbet Review', '/review-sportsbet.html'),
        ('betr Review', '/review-betr.html'),
    ])

    faq_items = ''.join(f'<div class="faq-item"><button class="faq-q">{q} <span class="fi">+</span></button><div class="faq-a">{a}</div></div>' for q,a in faqs)
    schema    = faq_schema(faqs) + '\n' + article_schema(title, desc, slug)

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
<nav class="nav"><a href="/index.html" class="nav-logo"><img src="/puntguide-logo.png" alt="PuntGuide"></a><ul class="nav-links"><li><a href="/best-betting-sites-australia.html">Best Sites</a></li><li><a href="/best-betting-sites-afl-nrl.html">NRL</a></li><li><a href="/nrl-round-{ROUND}-tips-{ROUND_YEAR}.html">Round {ROUND} Tips</a></li><li><a href="/best-betting-apps-australia.html">Best Apps</a></li><li><a href="/all-betting-sites.html">All Sites</a></li></ul><a href="/all-betting-sites.html" class="btn-g">Bet Now →</a></nav>
<div class="pb">
<div class="hero"><div class="hero-in">
  <div class="bc"><a href="/index.html">Home</a> › <a href="/nrl-round-{ROUND}-tips-{ROUND_YEAR}.html">NRL Round {ROUND} Tips</a> › {t1} vs {t2}</div>
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
<p class="footer-desc">Australia's most up-to-date guide to NRL betting — tips, odds, and the best bookmakers for every round.</p>
<div class="footer-links">
  <a href="/best-betting-sites-australia.html">Best Betting Sites</a>
  <a href="/best-betting-sites-afl-nrl.html">Best for NRL</a>
  <a href="/nrl-round-{ROUND}-tips-{ROUND_YEAR}.html">NRL Round {ROUND} Tips</a>
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
    print(f'\n── NRL Round {ROUND} Match Pages ──')
    for m in MATCHES:
        slug = build_match_page(m)
        generated.append(slug)
        print(f'  ✓ {slug}')
    update_sitemap(generated)
    print(f'\n✅ {len(generated)} NRL match pages generated\n')
