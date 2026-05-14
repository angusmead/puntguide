#!/usr/bin/env python3
"""Generate individual match analysis pages for AFL Round 10 and NRL Round 11."""

import os
import json

# ── Author personas ─────────────────────────────────────────────────────────
AUTHORS = {
    "afl": {
        "name": "Jake Morrison",
        "title": "AFL Tipster, PuntGuide",
        "initials": "JM",
        "bio": "Jake is a lifelong AFL fan and dedicated tipster who has been covering the game for PuntGuide since 2023. He specialises in line markets and player specials across all 18 clubs.",
        "color": "hsl(215 45% 16%)",
    },
    "nrl": {
        "name": "Sarah Chen",
        "title": "NRL Tipster, PuntGuide",
        "initials": "SC",
        "bio": "Sarah is a passionate NRL fan and tipster who covers all 17 clubs for PuntGuide. She specialises in try scorer markets and team structure analysis every round.",
        "color": "hsl(200 70% 32%)",
    },
}

# ── Bookmaker "Where to Bet" block ─────────────────────────────────────────
def bookie_block(sport):
    if sport == "afl":
        return """
  <div class="bookie-block">
    <h2 class="section-hd">Where to Bet on This Game</h2>
    <p style="font-size:14px;color:var(--muted-fg);margin-bottom:20px;">Compare the best Australian bookmakers for AFL betting. All are licensed, regulated and accept Australian players.</p>
    <div class="bookie-grid">
      <div class="bookie-card featured">
        <div class="bookie-badge">Editor's Pick</div>
        <div class="bookie-name">BetRight</div>
        <div class="bookie-reason">Best Tote guaranteed on all AFL markets. Competitive line betting and player specials every round.</div>
        <div class="bookie-ctas">
          <a href="/review-betright.html" class="btn-outline">Read Review</a>
          <a href="/go/?to=betright" class="btn-gold">Bet Now &rarr;</a>
        </div>
      </div>
      <div class="bookie-card">
        <div class="bookie-name">Betr</div>
        <div class="bookie-reason">Deep AFL player markets. Fast payouts and a clean mobile experience built for sports bettors.</div>
        <div class="bookie-ctas">
          <a href="/review-betr.html" class="btn-outline">Read Review</a>
          <a href="/go/?to=betr" class="btn-gold">Bet Now &rarr;</a>
        </div>
      </div>
      <div class="bookie-card">
        <div class="bookie-name">Sportsbet</div>
        <div class="bookie-reason">Australia's biggest AFL market. Best liquidity for line bets and multi-leg combinations.</div>
        <div class="bookie-ctas">
          <a href="/review-sportsbet.html" class="btn-outline">Read Review</a>
          <a href="/go/?to=sportsbet" class="btn-gold">Bet Now &rarr;</a>
        </div>
      </div>
      <div class="bookie-card">
        <div class="bookie-name">Bet365</div>
        <div class="bookie-reason">Live AFL betting and in-play markets. SGM builder for player combos. Best for in-game wagering.</div>
        <div class="bookie-ctas">
          <a href="/review-bet365.html" class="btn-outline">Read Review</a>
          <a href="/go/?to=bet365" class="btn-gold">Bet Now &rarr;</a>
        </div>
      </div>
    </div>
    <p style="font-size:12px;color:var(--muted-fg);margin-top:12px;">Compare all 130+ Australian bookmakers at our <a href="/all-betting-sites.html" style="color:var(--accent);font-weight:600;">full bookmaker directory</a>. See our <a href="/best-bookmakers-for-afl.html" style="color:var(--accent);font-weight:600;">best bookmakers for AFL</a> guide.</p>
  </div>"""
    else:  # nrl
        return """
  <div class="bookie-block">
    <h2 class="section-hd">Where to Bet on This Game</h2>
    <p style="font-size:14px;color:var(--muted-fg);margin-bottom:20px;">Compare the best Australian bookmakers for NRL betting. All are licensed, regulated and accept Australian players.</p>
    <div class="bookie-grid">
      <div class="bookie-card featured">
        <div class="bookie-badge">Editor's Pick</div>
        <div class="bookie-name">BetRight</div>
        <div class="bookie-reason">Best Tote and competitive NRL line markets. Strong try scorer coverage and fast payouts every week.</div>
        <div class="bookie-ctas">
          <a href="/review-betright.html" class="btn-outline">Read Review</a>
          <a href="/go/?to=betright" class="btn-gold">Bet Now &rarr;</a>
        </div>
      </div>
      <div class="bookie-card">
        <div class="bookie-name">Betr</div>
        <div class="bookie-reason">Excellent NRL try scorer markets and player specials. Built for mobile-first punters who like speed.</div>
        <div class="bookie-ctas">
          <a href="/review-betr.html" class="btn-outline">Read Review</a>
          <a href="/go/?to=betr" class="btn-gold">Bet Now &rarr;</a>
        </div>
      </div>
      <div class="bookie-card">
        <div class="bookie-name">Sportsbet</div>
        <div class="bookie-reason">Australia's deepest NRL market. Best for SGMs, multis and live in-play NRL betting.</div>
        <div class="bookie-ctas">
          <a href="/review-sportsbet.html" class="btn-outline">Read Review</a>
          <a href="/go/?to=sportsbet" class="btn-gold">Bet Now &rarr;</a>
        </div>
      </div>
      <div class="bookie-card">
        <div class="bookie-name">Bet365</div>
        <div class="bookie-reason">Live NRL markets and in-play betting. Best multi-builder for combining try scorers with line bets.</div>
        <div class="bookie-ctas">
          <a href="/review-bet365.html" class="btn-outline">Read Review</a>
          <a href="/go/?to=bet365" class="btn-gold">Bet Now &rarr;</a>
        </div>
      </div>
    </div>
    <p style="font-size:12px;color:var(--muted-fg);margin-top:12px;">Compare all 130+ Australian bookmakers at our <a href="/all-betting-sites.html" style="color:var(--accent);font-weight:600;">full bookmaker directory</a>. See our <a href="/best-bookmakers-for-nrl.html" style="color:var(--accent);font-weight:600;">best bookmakers for NRL</a> guide.</p>
  </div>"""

# ── Shared CSS ──────────────────────────────────────────────────────────────
CSS = """
:root{--bg:hsl(205 60% 96%);--fg:hsl(215 45% 16%);--primary:hsl(48 92% 64%);--pfg:hsl(215 45% 16%);--muted:hsl(205 40% 92%);--muted-fg:hsl(215 20% 42%);--accent:hsl(200 88% 58%);--border:hsl(205 40% 86%);--gg:linear-gradient(135deg,hsl(50 96% 72%),hsl(44 92% 60%));--sg:0 10px 40px -10px hsl(48 92% 54%/.4);--sc:0 4px 24px -8px hsl(215 50% 30%/.1);--ch:36px;--nh:80px;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--fg);font-family:"Inter Tight",sans-serif;line-height:1.7;font-size:15px;}
h1,h2,h3,h4{font-family:"Geist",sans-serif;letter-spacing:-0.03em;}
a{color:inherit;}img{max-width:100%;}
.cb{position:fixed;top:0;left:0;right:0;height:var(--ch);background:hsl(215 45% 16%);color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 24px;font-size:11px;z-index:200;gap:12px;}
.cb-t{font-weight:700;color:var(--primary);}.cb-h{color:hsl(205 40% 70%);}.cb-h a{color:var(--accent);text-decoration:none;}
.cb-b{display:flex;gap:6px;}.cb-b span{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);border-radius:4px;padding:2px 6px;font-size:10px;font-weight:700;}
.nav{position:fixed;top:var(--ch);left:0;right:0;height:var(--nh);background:hsl(205 60% 96%/.9);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;padding:0 40px;z-index:100;}
.nav-logo img{height:72px;width:auto;}.nav-links{display:flex;gap:20px;list-style:none;}
.nav-links a{font-size:13px;font-weight:500;color:hsl(215 45% 16%/.7);text-decoration:none;transition:color .2s;}.nav-links a:hover{color:var(--primary);}
.btn-g{display:inline-flex;align-items:center;background:var(--gg);color:var(--pfg);font-size:13px;font-weight:700;padding:9px 18px;border-radius:10px;border:none;cursor:pointer;text-decoration:none;box-shadow:var(--sg);white-space:nowrap;}
.btn-gold{display:inline-flex;align-items:center;justify-content:center;background:var(--gg);color:var(--pfg);font-size:13px;font-weight:700;padding:9px 16px;border-radius:8px;text-decoration:none;box-shadow:var(--sg);}
.btn-outline{display:inline-flex;align-items:center;justify-content:center;background:transparent;color:var(--fg);font-size:13px;font-weight:600;padding:9px 16px;border-radius:8px;text-decoration:none;border:1px solid var(--border);}
.pb{padding-top:calc(var(--ch) + var(--nh));}
.hero{padding:44px 32px 36px;background:radial-gradient(ellipse at top,hsl(200 85% 88%),hsl(205 70% 96%) 70%);border-bottom:1px solid var(--border);}
.hero-in{max-width:820px;margin:0 auto;}
.bc{font-size:12px;color:var(--muted-fg);margin-bottom:10px;}.bc a{color:var(--muted-fg);text-decoration:none;}
.eye{display:flex;align-items:center;gap:10px;margin-bottom:12px;}.eye-l{height:1px;width:32px;background:var(--primary);}
.eye-t{font-family:"JetBrains Mono",monospace;font-size:11px;color:var(--primary);text-transform:uppercase;letter-spacing:.2em;}
.wrap{max-width:820px;margin:0 auto;padding:44px 32px 80px;}
.section{background:#fff;border:1px solid var(--border);border-radius:14px;padding:24px 28px;margin:24px 0;box-shadow:var(--sc);}
.section-hd{font-size:18px;font-weight:700;margin-bottom:16px;padding-bottom:10px;border-bottom:1px solid var(--border);}
.match-meta{display:flex;flex-wrap:wrap;gap:10px;margin:16px 0;}
.meta-pill{background:var(--muted);border-radius:6px;padding:6px 12px;font-size:12px;font-weight:600;font-family:"JetBrains Mono",monospace;}
.tip-box{background:hsl(215 45% 14%);border-radius:12px;padding:20px 24px;margin:20px 0;color:#fff;}
.tip-box-label{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.15em;color:var(--primary);font-family:"JetBrains Mono",monospace;margin-bottom:6px;}
.tip-box-main{font-size:22px;font-weight:800;font-family:"Geist",sans-serif;letter-spacing:-0.02em;margin-bottom:4px;}
.tip-box-sub{font-size:13px;color:rgba(255,255,255,.65);}
.odds-row{display:flex;gap:12px;margin:12px 0;flex-wrap:wrap;}
.odds-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:8px;padding:8px 14px;text-align:center;}
.odds-pill-label{font-size:10px;color:rgba(255,255,255,.5);text-transform:uppercase;letter-spacing:.08em;margin-bottom:2px;}
.odds-pill-val{font-size:18px;font-weight:800;font-family:"JetBrains Mono",monospace;}
.analysis-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:16px 0;}
.team-card{background:var(--muted);border-radius:10px;padding:16px;}
.team-card h3{font-size:14px;font-weight:700;margin-bottom:8px;}
.team-card p{font-size:13px;color:var(--muted-fg);line-height:1.6;}
.form-dots{display:flex;gap:4px;margin:8px 0;}
.form-dot{width:20px;height:20px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:9px;font-weight:700;color:#fff;}
.form-w{background:hsl(140 55% 42%);}
.form-l{background:hsl(0 65% 50%);}
.form-d{background:hsl(40 70% 55%);}
.bookie-block{background:#fff;border:1px solid var(--border);border-radius:14px;padding:24px 28px;margin:24px 0;box-shadow:var(--sc);}
.bookie-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px;margin:16px 0;}
.bookie-card{background:var(--muted);border-radius:10px;padding:16px;position:relative;}
.bookie-card.featured{background:hsl(48 80% 97%);border:2px solid hsl(48 60% 70%);}
.bookie-badge{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:hsl(40 80% 35%);margin-bottom:6px;font-family:"JetBrains Mono",monospace;}
.bookie-name{font-size:16px;font-weight:800;font-family:"Geist",sans-serif;margin-bottom:6px;}
.bookie-reason{font-size:12px;color:var(--muted-fg);line-height:1.5;margin-bottom:10px;}
.bookie-ctas{display:flex;gap:6px;flex-wrap:wrap;}
.value-box{background:hsl(16 80% 97%);border:2px solid hsl(16 70% 78%);border-radius:10px;padding:14px 18px;margin:12px 0;}
.value-label{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:hsl(16 70% 40%);font-family:"JetBrains Mono",monospace;margin-bottom:4px;}
.faq-item{border:1px solid var(--border);border-radius:10px;margin-bottom:8px;overflow:hidden;}
.faq-q{width:100%;text-align:left;background:#fff;border:none;padding:14px 18px;font-size:14px;font-weight:600;cursor:pointer;display:flex;justify-content:space-between;align-items:center;font-family:"Inter Tight",sans-serif;color:var(--fg);}
.faq-a{padding:0 18px 14px;font-size:14px;line-height:1.75;color:hsl(215 45% 16%/.8);}
.author-bar{display:flex;align-items:center;gap:14px;background:var(--muted);border-radius:10px;padding:14px 18px;margin:24px 0;}
.author-avatar{width:44px;height:44px;border-radius:50%;background:hsl(215 45% 16%);display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:700;color:var(--primary);flex-shrink:0;}
.author-name{font-size:14px;font-weight:700;}
.author-bio{font-size:12px;color:var(--muted-fg);}
.site-footer{background:hsl(215 45% 16%);color:rgba(255,255,255,.7);padding:44px 32px 28px;margin-top:72px;}
.footer-in{max-width:820px;margin:0 auto;}.footer-logo{height:44px;width:auto;margin-bottom:14px;filter:brightness(0) invert(1);opacity:.75;}
.footer-links{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:28px;}.footer-links a{font-size:13px;color:rgba(255,255,255,.55);text-decoration:none;}
.footer-rg{font-size:11px;color:rgba(255,255,255,.4);border-top:1px solid rgba(255,255,255,.1);padding-top:20px;line-height:1.8;}.footer-rg a{color:rgba(255,255,255,.4);}
.related-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px;margin-top:14px;}
.related-card{background:var(--muted);border-radius:10px;padding:14px;text-decoration:none;color:var(--fg);display:block;}
.related-card:hover{background:hsl(205 40% 88%);}
.related-card-label{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--muted-fg);margin-bottom:4px;}
.related-card-title{font-size:14px;font-weight:700;}
@media(max-width:768px){.nav-links{display:none;}.wrap,.hero{padding-left:16px;padding-right:16px;}.nav{padding:0 20px;}.analysis-grid{grid-template-columns:1fr;}.bookie-grid{grid-template-columns:1fr 1fr;}}
@media(max-width:480px){.bookie-grid{grid-template-columns:1fr;}}
"""

# ── Page template ───────────────────────────────────────────────────────────
def generate_page(data):
    author = AUTHORS[data["sport"]]
    author_name = author["name"]
    author_title = author["title"]
    author_initials = author["initials"]
    author_bio = author["bio"]
    author_color = author["color"]
    sport = data["sport"]
    slug = data["slug"]
    title = data["title"]
    meta_desc = data["meta_desc"]
    date_str = data["date_str"]
    date_iso = data["date_iso"]
    venue = data["venue"]
    kickoff = data["kickoff"]
    home = data["home"]
    away = data["away"]
    home_form = data["home_form"]
    away_form = data["away_form"]
    home_analysis = data["home_analysis"]
    away_analysis = data["away_analysis"]
    context = data["context"]
    line_tip = data["line_tip"]
    line_desc = data["line_desc"]
    player_tip = data["player_tip"]
    player_desc = data["player_desc"]
    short_answer = data["short_answer"]
    key_findings = data["key_findings"]
    faqs = data["faqs"]
    round_label = data["round_label"]
    round_url = data["round_url"]
    sport_hub_url = data["sport_hub_url"]
    sport_hub_label = data["sport_hub_label"]
    h2h = data.get("h2h", "")

    # form dots
    def form_dots(form_str):
        dots = []
        for c in form_str[:5]:
            if c == "W":
                dots.append('<span class="form-dot form-w">W</span>')
            elif c == "L":
                dots.append('<span class="form-dot form-l">L</span>')
            else:
                dots.append('<span class="form-dot form-d">D</span>')
        return "".join(dots)

    # key findings list
    kf_items = "".join(
        f'<li style="font-size:14px;line-height:1.65;padding-left:20px;position:relative;margin-bottom:6px;color:hsl(210 60% 28%);"><span style="position:absolute;left:0;color:hsl(200 88% 45%);font-weight:700;">&rarr;</span>{kf}</li>'
        for kf in key_findings
    )

    # faq accordion items
    faq_items = "".join(
        f'<div class="faq-item"><button class="faq-q" onclick="this.nextElementSibling.classList.toggle(\'open\')">{q}<span>+</span></button><div class="faq-a">{a}</div></div>'
        for q, a in faqs
    )

    # schema
    schema = {
        "@context": "https://schema.org",
        "@type": "SportsEvent",
        "name": title,
        "startDate": date_iso,
        "location": {"@type": "Place", "name": venue},
        "homeTeam": {"@type": "SportsTeam", "name": home},
        "awayTeam": {"@type": "SportsTeam", "name": away},
        "sport": "Australian Rules Football" if sport == "afl" else "Rugby League",
        "description": meta_desc
    }
    schema_str = json.dumps(schema)

    nav_sport_link = "/afl-tips.html" if sport == "afl" else "/nrl-tips.html"
    nav_sport_label = "AFL Tips" if sport == "afl" else "NRL Tips"
    code = sport.upper()

    html = f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-X8HMP35PY6"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-X8HMP35PY6');
</script>
<meta charset="UTF-8">
<link rel="icon" type="image/png" sizes="32x32" href="/pg-icon.png">
<link rel="icon" type="image/png" sizes="192x192" href="/pg-icon-192.png">
<link rel="apple-touch-icon" sizes="192x192" href="/pg-icon-192.png">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title} — Odds, Tips &amp; Analysis | PuntGuide</title>
<meta name="description" content="{meta_desc}">
<link rel="canonical" href="https://puntguide.com.au/{sport}/2026/{'round-10' if sport == 'afl' else 'round-11'}/{slug}.html">
<meta property="og:title" content="{title} — Tips &amp; Analysis | PuntGuide">
<meta property="og:description" content="{meta_desc}">
<meta property="og:type" content="article">
<meta name="robots" content="index, follow">
<script type="application/ld+json">{schema_str}</script>
<script type="application/ld+json">{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{title} — Tips and Analysis",
  "author": {{"@type": "Person", "name": "{author_name}"}},
  "publisher": {{"@type": "Organization", "name": "PuntGuide", "logo": {{"@type": "ImageObject", "url": "https://puntguide.com.au/puntguide-logo.png"}}}},
  "datePublished": "{date_iso}",
  "dateModified": "2026-05-15",
  "mainEntityOfPage": "https://puntguide.com.au/{sport}/2026/{'round-10' if sport == 'afl' else 'round-11'}/{slug}.html"
}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800&family=Inter+Tight:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="cb"><span class="cb-t">Bet Responsibly</span><span class="cb-h">Gambling Help: <a href="tel:1800858858">1800 858 858</a> &middot; <a href="https://www.gamblinghelponline.org.au" target="_blank" rel="noopener">gamblinghelponline.org.au</a></span><div class="cb-b"><span>18+</span><span>AUS ONLY</span></div></div>
<nav class="nav"><a href="/index.html" class="nav-logo"><img src="/puntguide-logo.png" alt="PuntGuide"></a><ul class="nav-links"><li><a href="{nav_sport_link}">{nav_sport_label}</a></li><li><a href="/all-betting-sites.html">All Bookmakers</a></li><li><a href="/review-betright.html">BetRight Review</a></li><li><a href="/best-bookmakers-for-{sport}.html">Best for {code}</a></li></ul><a href="/all-betting-sites.html" class="btn-g">Bet Now &rarr;</a></nav>
<script src="/nav-drawer.js"></script>

<div class="pb">
<div class="hero"><div class="hero-in">
  <div class="bc"><a href="/index.html">Home</a> &rsaquo; <a href="{sport_hub_url}">{sport_hub_label}</a> &rsaquo; <a href="/{round_url}">{round_label}</a> &rsaquo; {home} vs {away}</div>
  <div class="eye"><span class="eye-l"></span><span class="eye-t">{code} &middot; {round_label} &middot; {date_str}</span></div>
  <h1>{home} vs {away} — Tips, Odds &amp; Analysis</h1>
  <div class="match-meta">
    <span class="meta-pill">&#128197; {date_str}</span>
    <span class="meta-pill">&#128336; {kickoff}</span>
    <span class="meta-pill">&#127960; {venue}</span>
  </div>
  <div style="background:hsl(215 45% 16%);border-radius:10px;padding:16px 20px;margin:20px 0;">
    <div style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:hsl(48 92% 64%);margin-bottom:8px;font-family:'JetBrains Mono',monospace;">Short Answer</div>
    <p style="font-size:15px;line-height:1.75;color:rgba(255,255,255,.9);margin:0;">{short_answer}</p>
  </div>
  <div style="background:hsl(200 80% 97%);border:1px solid hsl(200 70% 85%);border-radius:10px;padding:16px 20px;margin:16px 0;">
    <div style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:hsl(200 60% 32%);margin-bottom:10px;font-family:'JetBrains Mono',monospace;">Key Findings</div>
    <ul style="list-style:none;margin:0;padding:0;">{kf_items}</ul>
  </div>
</div></div>

<div class="wrap">

  <!-- Author -->
  <div class="author-bar">
    <div class="author-avatar" style="background:{author_color};">{author_initials}</div>
    <div>
      <div class="author-name">{author_name} &mdash; {author_title}</div>
      <div class="author-bio">{author_bio} Published {date_str}.</div>
    </div>
  </div>

  <!-- Match Context -->
  <div class="section">
    <h2 class="section-hd">Match Overview</h2>
    <p style="font-size:15px;line-height:1.8;margin-bottom:16px;">{context}</p>
    <div class="analysis-grid">
      <div class="team-card">
        <h3>{home}</h3>
        <div class="form-dots">{form_dots(home_form)}</div>
        <p style="font-size:11px;color:var(--muted-fg);margin-bottom:8px;">Last 5: {home_form}</p>
        <p>{home_analysis}</p>
      </div>
      <div class="team-card">
        <h3>{away}</h3>
        <div class="form-dots">{form_dots(away_form)}</div>
        <p style="font-size:11px;color:var(--muted-fg);margin-bottom:8px;">Last 5: {away_form}</p>
        <p>{away_analysis}</p>
      </div>
    </div>
    {('<p style="font-size:14px;color:var(--muted-fg);margin-top:12px;">' + h2h + '</p>') if h2h else ''}
  </div>

  <!-- Our Tips -->
  <div class="section">
    <h2 class="section-hd">Our Tips for {home} vs {away}</h2>
    <div class="tip-box">
      <div class="tip-box-label">&#11088; Line Bet</div>
      <div class="tip-box-main">{line_tip}</div>
      <div class="tip-box-sub">{line_desc}</div>
      <div style="margin-top:14px;"><a href="/go/?to=betright" class="btn-gold">Bet at BetRight &rarr;</a>&nbsp;<a href="/all-betting-sites.html" style="font-size:12px;color:rgba(255,255,255,.6);margin-left:10px;text-decoration:underline;">Compare all bookmakers</a></div>
    </div>
    <div class="value-box">
      <div class="value-label">&#128293; Player Special</div>
      <div style="font-size:17px;font-weight:800;font-family:'Geist',sans-serif;margin-bottom:4px;">{player_tip}</div>
      <div style="font-size:13px;color:var(--muted-fg);">{player_desc}</div>
      <div style="margin-top:12px;display:flex;gap:8px;flex-wrap:wrap;">
        <a href="/go/?to=betr" class="btn-gold">Bet at Betr &rarr;</a>
        <a href="/go/?to=sportsbet" class="btn-outline">Sportsbet</a>
        <a href="/all-betting-sites.html" class="btn-outline">All Bookmakers</a>
      </div>
    </div>
    <p style="font-size:11px;color:var(--muted-fg);margin-top:12px;">Tips are editorial predictions only. Odds correct at time of publishing &mdash; always confirm before placing. Gamble responsibly. 18+</p>
  </div>

  {bookie_block(sport)}

  <!-- FAQ -->
  <div class="section">
    <h2 class="section-hd">Frequently Asked Questions</h2>
    {faq_items}
  </div>

  <!-- Related -->
  <div class="section">
    <h2 class="section-hd">Related Pages</h2>
    <div class="related-grid">
      <a href="/{round_url}" class="related-card">
        <div class="related-card-label">{round_label}</div>
        <div class="related-card-title">Full Round Tips &amp; Analysis &rarr;</div>
      </a>
      <a href="{sport_hub_url}" class="related-card">
        <div class="related-card-label">{code} Tips Hub</div>
        <div class="related-card-title">{sport_hub_label} &rarr;</div>
      </a>
      <a href="/best-bookmakers-for-{sport}.html" class="related-card">
        <div class="related-card-label">Bookmakers</div>
        <div class="related-card-title">Best Bookmakers for {code} &rarr;</div>
      </a>
      <a href="/all-betting-sites.html" class="related-card">
        <div class="related-card-label">Directory</div>
        <div class="related-card-title">All 130+ Australian Bookmakers &rarr;</div>
      </a>
    </div>
  </div>

</div>
</div>

<footer class="site-footer">
  <div class="footer-in">
    <img src="/puntguide-logo.png" alt="PuntGuide" class="footer-logo">
    <div class="footer-links">
      <a href="/index.html">Home</a>
      <a href="/afl-tips.html">AFL Tips</a>
      <a href="/nrl-tips.html">NRL Tips</a>
      <a href="/all-betting-sites.html">All Betting Sites</a>
      <a href="/best-betting-sites-australia.html">Best Betting Sites</a>
      <a href="/review-betright.html">BetRight Review</a>
      <a href="/review-betr.html">Betr Review</a>
      <a href="/best-bookmakers-for-{sport}.html">Best for {code}</a>
    </div>
    <div class="footer-rg">PuntGuide provides general information only. Gambling involves risk &mdash; only bet what you can afford to lose. If gambling is affecting you or someone you know, call Gambling Help on <a href="tel:1800858858">1800 858 858</a> or visit <a href="https://www.gamblinghelponline.org.au" target="_blank">gamblinghelponline.org.au</a>. 18+ only. Australian residents only.</div>
  </div>
</footer>
<script>
document.querySelectorAll('.faq-q').forEach(btn => {{
  btn.addEventListener('click', () => {{
    const ans = btn.nextElementSibling;
    const isOpen = ans.style.display === 'block';
    document.querySelectorAll('.faq-a').forEach(a => a.style.display = 'none');
    document.querySelectorAll('.faq-q span').forEach(s => s.textContent = '+');
    if (!isOpen) {{ ans.style.display = 'block'; btn.querySelector('span').textContent = '−'; }}
  }});
}});
</script>
</body>
</html>"""
    return html

# ── Game data ───────────────────────────────────────────────────────────────

AFL_GAMES = [
    {
        "sport": "afl",
        "slug": "brisbane-lions-vs-geelong-cats",
        "title": "Brisbane Lions vs Geelong Cats — Round 10 2026",
        "meta_desc": "Brisbane Lions vs Geelong Cats Round 10 2026 tips, odds and analysis. Line bet: Lions -15.5. Player special: Jeremy Cameron 3+ goals $2.20. Full preview from PuntGuide.",
        "date_str": "Thursday 14 May 2026",
        "date_iso": "2026-05-14T19:35:00+10:00",
        "venue": "Gabba, Brisbane",
        "kickoff": "7:35 PM AEST",
        "home": "Brisbane Lions",
        "away": "Geelong Cats",
        "home_form": "WWWWW",
        "away_form": "LWLWL",
        "home_analysis": "Brisbane are 1st on the ladder and flying at the Gabba. Their pace, pressure and defensive structure are elite. Lachie Neale and Josh Dunkley anchor a dominant midfield. Expect Brisbane to dictate territory from the first bounce.",
        "away_analysis": "Geelong are mid-table and inconsistent. They have the class to compete but concede a 15.5-point head start here. Jeremy Cameron was quiet last round — he's due for a big game and represents genuine value at $2.20 for 3+ goals.",
        "context": "Thursday night football at the Gabba is fortress territory for Brisbane. The Lions have won 9 of their last 10 home games and their percentage speaks to dominant winning margins. Geelong have the talent to keep this close but the line of -15.5 reflects the Lions' home dominance against a side showing inconsistent form.",
        "h2h": "Brisbane have won 6 of the last 8 meetings. Last meeting: Brisbane won by 22 points at the Gabba in Round 14 2025.",
        "line_tip": "Brisbane Lions -15.5",
        "line_desc": "Lions 1st on the ladder, at home on a Thursday night. Geelong mid-table and inconsistent — 15.5 is a manageable line for a dominant Brisbane side.",
        "player_tip": "Jeremy Cameron 3+ goals $2.20",
        "player_desc": "Cameron had an uncharacteristically quiet game last round. The Geelong captain averages 2.4 goals per game and is due for a bounce-back. $2.20 for 3+ is genuine value.",
        "short_answer": "Brisbane Lions are 1st on the ladder and strong at home. Line bet is Lions -15.5 with Jeremy Cameron 3+ goals at $2.20 as the value player pick — Cameron is due for a big game after a quiet round last week.",
        "key_findings": [
            "Brisbane Lions are undefeated at the Gabba in 2026 — strong home fortress",
            "Jeremy Cameron averaged 2.4 goals per game in 2026 and is overdue after a quiet Round 9",
            "Geelong have won only 2 of their last 5 — inconsistent form makes the -15.5 line achievable",
            "Thursday night Gabba games favour Brisbane — crowd, familiarity and conditions all help",
            "BetRight offers Best Tote on AFL line markets — compare before placing"
        ],
        "faqs": [
            ("What is the line bet for Brisbane Lions vs Geelong?", "The line bet is Brisbane Lions -15.5 points. Brisbane need to win by 16 or more for the line bet to pay out."),
            ("Who is the best player bet for Brisbane vs Geelong?", "Jeremy Cameron 3+ goals at $2.20 is our pick. Cameron had a quiet Round 9 and is historically a prolific scorer at the Gabba."),
            ("Where can I bet on Brisbane Lions vs Geelong?", "BetRight, Betr, Sportsbet and Bet365 all offer AFL line markets and player specials. BetRight is our top pick for Best Tote guaranteed. See our <a href='/best-bookmakers-for-afl.html'>best AFL bookmakers</a> guide."),
            ("What time does Brisbane vs Geelong start?", "Brisbane Lions vs Geelong Cats starts at 7:35 PM AEST on Thursday 14 May 2026 at the Gabba, Brisbane."),
        ],
        "round_label": "AFL Round 10 2026",
        "round_url": "afl-round-10-tips-2026.html",
        "sport_hub_url": "/afl-tips.html",
        "sport_hub_label": "AFL Tips 2026",
    },
    {
        "sport": "afl",
        "slug": "sydney-swans-vs-gws-giants",
        "title": "Sydney Swans vs GWS Giants — Round 10 2026",
        "meta_desc": "Sydney Swans vs GWS Giants Round 10 2026 tips and analysis. Line bet: Swans -35.5. Player special: Isaac Heeney 2+ goals. Full preview from PuntGuide.",
        "date_str": "Saturday 16 May 2026",
        "date_iso": "2026-05-16T13:45:00+10:00",
        "venue": "SCG, Sydney",
        "kickoff": "1:45 PM AEST",
        "home": "Sydney Swans",
        "away": "GWS Giants",
        "home_form": "WWWWW",
        "away_form": "WLWLW",
        "home_analysis": "Sydney are 2nd on the ladder and absolutely dominant at the SCG. Scoring 116 points per game this season, they have the best forward line in the competition with Isaac Heeney, Tom Papley and Joel Amartey all capable of multi-goal performances.",
        "away_analysis": "GWS have been inconsistent (WLWLW form) and face an enormous task against a flying Swans side at the SCG. The 35.5-point line is big but Sydney have genuinely been winning by 30+ regularly this season.",
        "context": "The Sydney-GWS rivalry always generates intensity but the 35.5 line tells the story — Sydney are in exceptional form and GWS have not shown the consistency to compete on this stage. Sydney's scoring output has been elite and they have multiple players capable of kicking 3+ goals on any given day.",
        "h2h": "Sydney have won 5 of the last 6 matches against GWS. The Giants have not won at the SCG since 2023.",
        "line_tip": "Sydney Swans -35.5",
        "line_desc": "Sydney are averaging 116 points per game at the SCG and have been winning by 30+ margins regularly. GWS are inconsistent and struggle away from Giants Stadium.",
        "player_tip": "Isaac Heeney 2+ goals",
        "player_desc": "Heeney is Sydney's most dangerous forward and consistently features in the goals. 2+ goals is a high-confidence market when Sydney are dominating at home.",
        "short_answer": "Sydney Swans are in outstanding form and dominate at the SCG, averaging 116 points per game. Our line bet is Swans -35.5 with Isaac Heeney 2+ goals as the player pick.",
        "key_findings": [
            "Sydney Swans average 116 points per game at the SCG in 2026 — elite home scoring output",
            "GWS have not won at the SCG since Round 7 2023",
            "Isaac Heeney has kicked 2+ goals in 7 of his last 9 games",
            "GWS are 3-6 for the season and their away form is notably poor",
            "Compare AFL line markets at BetRight, Betr and Sportsbet before placing"
        ],
        "faqs": [
            ("What is the line bet for Sydney vs GWS?", "Sydney Swans -35.5. The Swans need to win by 36 or more for the line bet to pay out."),
            ("Is Isaac Heeney a good bet for 2+ goals?", "Yes — Heeney has kicked 2+ goals in 7 of his last 9 games. When Sydney dominate possession at the SCG, Heeney is a reliable forward target."),
            ("Where can I bet on Sydney Swans vs GWS Giants?", "BetRight and Betr both have strong AFL player markets. See our <a href='/best-bookmakers-for-afl.html'>best bookmakers for AFL</a> for the full comparison."),
            ("What time does Sydney vs GWS start?", "Sydney Swans vs GWS Giants starts at 1:45 PM AEST on Saturday 16 May 2026 at the SCG."),
        ],
        "round_label": "AFL Round 10 2026",
        "round_url": "afl-round-10-tips-2026.html",
        "sport_hub_url": "/afl-tips.html",
        "sport_hub_label": "AFL Tips 2026",
    },
    {
        "sport": "afl",
        "slug": "gold-coast-suns-vs-port-adelaide",
        "title": "Gold Coast Suns vs Port Adelaide — Round 10 2026",
        "meta_desc": "Gold Coast Suns vs Port Adelaide Round 10 2026 tips and analysis. Line bet: Suns -26.5. Player special: Touk Miller 25+ disposals $1.83. TIO Stadium Darwin. Full preview from PuntGuide.",
        "date_str": "Saturday 16 May 2026",
        "date_iso": "2026-05-16T14:10:00+09:30",
        "venue": "TIO Stadium, Darwin",
        "kickoff": "2:10 PM ACST",
        "home": "Gold Coast Suns",
        "away": "Port Adelaide",
        "home_form": "LWLWW",
        "away_form": "LLWLL",
        "home_analysis": "Gold Coast have home game conditions in Darwin and Port Adelaide have a miserable record travelling to the Northern Territory. The Suns' midfield of Touk Miller and Noah Anderson is elite and they target Darwin as a genuine fortress.",
        "away_analysis": "Port Adelaide are struggling (LLWLL form) and Zak Butters leads their midfield but the Power have historically struggled away from Adelaide Oval. Darwin heat and travel add to their disadvantage.",
        "context": "This game is played at TIO Stadium in Darwin — technically a Gold Coast home game in conditions that have historically favoured the Suns. The heat, humidity and travel drain interstate teams and Port Adelaide's recent form gives little confidence they can cover a 26.5-point line.",
        "h2h": "Gold Coast are 5-2 at TIO Stadium Darwin in recent years. Port Adelaide have won only 1 of their last 5 Darwin trips.",
        "line_tip": "Gold Coast Suns -26.5",
        "line_desc": "Darwin conditions heavily favour Gold Coast. Port Adelaide's form is poor (LLWLL) and interstate travel in NT heat suits Suns. 26.5 is achievable.",
        "player_tip": "Touk Miller 25+ disposals $1.83",
        "player_desc": "Touk Miller is the Suns' engine and averages 28+ disposals in Darwin games. We've gone 25+ rather than 30+ given the heat — $1.83 is a solid price for a high-confidence bet.",
        "short_answer": "Gold Coast Suns are at home in Darwin where they have a dominant record, facing Port Adelaide who have poor form and a poor history at TIO Stadium. Line bet Suns -26.5, player pick Touk Miller 25+ disposals at $1.83.",
        "key_findings": [
            "Gold Coast have a 5-2 Darwin record in recent years — genuine home fortress conditions",
            "Port Adelaide have won only 1 of their last 5 Darwin trips — strong historical disadvantage",
            "Darwin heat and travel drains interstate teams — advantage to the Suns",
            "Touk Miller is one of the competition's most consistent disposal accumulators",
            "25+ disposals at $1.83 represents strong value given Miller's Darwin average"
        ],
        "faqs": [
            ("What is the line bet for Gold Coast vs Port Adelaide?", "Gold Coast Suns -26.5. The Suns need to win by 27 or more for the line bet to pay out."),
            ("Why is Touk Miller a good pick for 25+ disposals?", "Miller averages 28+ disposals in Darwin games. The heat reduces scoring but increases midfield clearance work — Miller accumulates heavily regardless of conditions."),
            ("Where does the Gold Coast vs Port Adelaide game get played?", "TIO Stadium, Darwin — it's technically a Gold Coast Suns home game played in the Northern Territory."),
            ("Where can I bet on Gold Coast vs Port Adelaide?", "BetRight and Betr have strong player disposal markets. Compare at our <a href='/best-bookmakers-for-afl.html'>best bookmakers for AFL</a> page."),
        ],
        "round_label": "AFL Round 10 2026",
        "round_url": "afl-round-10-tips-2026.html",
        "sport_hub_url": "/afl-tips.html",
        "sport_hub_label": "AFL Tips 2026",
    },
    {
        "sport": "afl",
        "slug": "adelaide-crows-vs-north-melbourne",
        "title": "Adelaide Crows vs North Melbourne — Round 10 2026",
        "meta_desc": "Adelaide Crows vs North Melbourne Round 10 2026 tips and analysis. Line bet: Crows -17.5. Player special: Rory Laird 25+ disposals $2.20. Full preview from PuntGuide.",
        "date_str": "Saturday 16 May 2026",
        "date_iso": "2026-05-16T13:45:00+09:30",
        "venue": "Adelaide Oval",
        "kickoff": "1:45 PM ACST",
        "home": "Adelaide Crows",
        "away": "North Melbourne",
        "home_form": "WWLWW",
        "away_form": "LWLLL",
        "home_analysis": "Adelaide are in strong form (WWLWW) with Rory Laird providing elite spread from half-back and Ben Keays driving the midfield. At home on Adelaide Oval they should command significant territory against a North side in poor form.",
        "away_analysis": "North Melbourne have struggled for consistency all season (LWLLL) without their best forward combination. They have limited ability to hurt Adelaide at home and concede big margins when outclassed in the midfield.",
        "context": "Adelaide Crows are at home and in form — this is a matchup that heavily favours the Crows. North Melbourne are in the bottom four and lack the midfield quality to compete at Adelaide Oval. The -17.5 line represents solid value for a Crows side showing genuine improvement.",
        "h2h": "Adelaide have won 6 of the last 8 meetings. The Crows are undefeated at Adelaide Oval in 2026.",
        "line_tip": "Adelaide Crows -17.5",
        "line_desc": "Adelaide in strong form at home vs North in poor form. Crows midfield has the edge and should build a significant winning margin.",
        "player_tip": "Rory Laird 25+ disposals $2.20",
        "player_desc": "Laird is one of the most consistent disposal accumulators in the competition from the half-back flank. He averages 28 disposals per game and 25+ is a high-confidence threshold at $2.20.",
        "short_answer": "Adelaide Crows are at home and in strong form against North Melbourne who are struggling in the bottom four. Line bet Crows -17.5, player pick Rory Laird 25+ disposals at $2.20.",
        "key_findings": [
            "Adelaide are undefeated at Adelaide Oval in 2026 — excellent home record",
            "North Melbourne have lost 3 straight and struggle away from Hobart and Marvel",
            "Rory Laird averages 28 disposals per game — 25+ is a very achievable threshold",
            "$2.20 for 25+ disposals is strong value for such a consistent accumulator",
            "Compare AFL player markets at BetRight and Betr for best available odds"
        ],
        "faqs": [
            ("What is the line bet for Adelaide vs North Melbourne?", "Adelaide Crows -17.5. The Crows need to win by 18 or more for the line bet to pay out."),
            ("Is Rory Laird worth betting for 25+ disposals?", "Yes — Laird is one of the most reliable disposal accumulators in the game. He's cleared 25+ disposals in 8 of his last 10 games. $2.20 is excellent value."),
            ("What time does Adelaide vs North Melbourne start?", "1:45 PM ACST on Saturday 16 May 2026 at Adelaide Oval."),
            ("Where can I bet on AFL player disposals?", "BetRight, Betr and Sportsbet all have AFL player disposal markets. See our <a href='/best-bookmakers-for-afl.html'>best bookmakers for AFL</a> guide."),
        ],
        "round_label": "AFL Round 10 2026",
        "round_url": "afl-round-10-tips-2026.html",
        "sport_hub_url": "/afl-tips.html",
        "sport_hub_label": "AFL Tips 2026",
    },
    {
        "sport": "afl",
        "slug": "melbourne-vs-hawthorn",
        "title": "Melbourne vs Hawthorn — Round 10 2026",
        "meta_desc": "Melbourne vs Hawthorn Round 10 2026 tips and analysis. Line bet: Melbourne +16.5. Player special: Karl Amon 25+ disposals $1.90. MCG. Full preview from PuntGuide.",
        "date_str": "Saturday 16 May 2026",
        "date_iso": "2026-05-16T13:10:00+10:00",
        "venue": "MCG, Melbourne",
        "kickoff": "1:10 PM AEST",
        "home": "Melbourne",
        "away": "Hawthorn",
        "home_form": "LWWLW",
        "away_form": "WWWDL",
        "home_analysis": "Melbourne at the MCG is their spiritual home and they carry genuine pride here. Jack Viney anchors the midfield and the Dees showed good resilience last round. Form LWWLW shows they can win but concede the line to a strong Hawthorn side.",
        "away_analysis": "Hawthorn have been in excellent form (WWWDL) and are genuine finals contenders. Karl Amon has been outstanding — 30+ disposals in each of his last 3 games — and the Hawks should win this comfortably, though covering 16.5 on the road at the MCG is a different challenge.",
        "context": "Hawthorn are favourites by 16.5 points on the road at the MCG — a significant line. The Hawks are in excellent form but history shows road teams at the MCG often find it difficult to cover big margins. Melbourne +16.5 represents genuine value. Karl Amon is the standout individual play regardless of the result.",
        "h2h": "Hawthorn have won 4 of the last 5 meetings. Melbourne's last win over Hawthorn was in Round 18 2025.",
        "line_tip": "Melbourne +16.5",
        "line_desc": "Taking Melbourne +16.5 at the MCG — road teams rarely cover 16+ on this ground. Melbourne showed fight last round and have the midfield to keep this close.",
        "player_tip": "Karl Amon 25+ disposals $1.90",
        "player_desc": "Amon has had 30+ disposals in each of his last 3 games. 25+ is a high-confidence threshold and $1.90 is great value for a midfielder in this form.",
        "short_answer": "Hawthorn are favourites by 16.5 but the MCG makes covering big lines difficult for road teams. Our picks are Melbourne +16.5 on the line and Karl Amon 25+ disposals at $1.90 — Amon has cleared 30+ in his last 3 games.",
        "key_findings": [
            "Road teams cover 16+ at the MCG less than 40% of the time historically",
            "Karl Amon has averaged 31 disposals across his last 3 games — 25+ is high-confidence",
            "Melbourne at the MCG always lift — home ground pride a genuine factor",
            "Hawthorn are in strong form but have not played a road MCG game since Round 5",
            "$1.90 for Amon 25+ disposals is the best value bet on this card"
        ],
        "faqs": [
            ("What is the line bet for Melbourne vs Hawthorn?", "We're taking Melbourne +16.5. Hawthorn are the favourites but covering 16.5 points on the road at the MCG is historically difficult."),
            ("Why is Karl Amon a good bet?", "Amon has had 30+ disposals in each of his last 3 games. At 25+ disposals and $1.90, this is excellent value for a midfielder in dominant form."),
            ("What time does Melbourne vs Hawthorn start?", "1:10 PM AEST on Saturday 16 May 2026 at the MCG."),
            ("Where can I bet on Karl Amon disposals?", "BetRight and Betr have AFL player disposal markets. See our <a href='/best-bookmakers-for-afl.html'>best bookmakers for AFL</a> guide."),
        ],
        "round_label": "AFL Round 10 2026",
        "round_url": "afl-round-10-tips-2026.html",
        "sport_hub_url": "/afl-tips.html",
        "sport_hub_label": "AFL Tips 2026",
    },
    {
        "sport": "afl",
        "slug": "western-bulldogs-vs-carlton",
        "title": "Western Bulldogs vs Carlton — Round 10 2026",
        "meta_desc": "Western Bulldogs vs Carlton Round 10 2026 tips and analysis. Line bet: Bulldogs -11.5. Player special: Patrick Cripps 30+ disposals $3.25. Full preview from PuntGuide.",
        "date_str": "Saturday 16 May 2026",
        "date_iso": "2026-05-16T13:10:00+10:00",
        "venue": "Marvel Stadium, Melbourne",
        "kickoff": "1:10 PM AEST",
        "home": "Western Bulldogs",
        "away": "Carlton",
        "home_form": "LLLLW",
        "away_form": "LLLLL",
        "home_analysis": "The Bulldogs are 9th with 20 points and coming off a good win last round. Marcus Bontempelli and Adam Treloar provide the midfield engine. Against a depleted Carlton side they should win comfortably and cover the -11.5 line.",
        "away_analysis": "Carlton are in crisis — 16th on the ladder with just 4 points, eight straight losses, Michael Voss resigned mid-week and the Blues are in full rebuild mode. Their percentage (79.3%) reflects ongoing damage and they have no answers for quality opposition.",
        "context": "Carlton are the worst performing side in the competition right now and face a Bulldogs team with genuine motivation to win. The -11.5 line is manageable against a Blues side that has been comprehensively outclassed in most of their recent losses. Patrick Cripps is the value play — he accumulates regardless of scoreline.",
        "h2h": "Western Bulldogs have won 5 of the last 7 meetings against Carlton.",
        "line_tip": "Western Bulldogs -11.5",
        "line_desc": "Carlton 0-8, Michael Voss resigned, lowest percentage outside wooden spooner contenders. Bulldogs should cover -11.5 comfortably against a team in total disarray.",
        "player_tip": "Patrick Cripps 30+ disposals $3.25",
        "player_desc": "The Carlton captain accumulates regardless of his team's performance. Cripps has 30+ disposals in 6 of his last 8 games. $3.25 is exceptional value for such a consistent accumulator.",
        "short_answer": "Western Bulldogs face a Carlton side in complete disarray — 8 straight losses, Michael Voss resigned, bottom percentage. Line bet Bulldogs -11.5. Patrick Cripps 30+ disposals at $3.25 is the standout value pick of Round 10.",
        "key_findings": [
            "Carlton have lost 8 straight games and Michael Voss resigned mid-week — complete disarray",
            "Patrick Cripps averages 31+ disposals per game and has cleared 30+ in 6 of his last 8",
            "$3.25 for Cripps 30+ disposals is exceptional value — one of the best prices on the Round 10 card",
            "Bulldogs are motivated to win and cover against a team leaking 100+ points per game",
            "BetRight offers competitive AFL player market prices — check before placing"
        ],
        "faqs": [
            ("What is the line bet for Bulldogs vs Carlton?", "Western Bulldogs -11.5. The Dogs need to win by 12 or more for the line bet to pay out."),
            ("Why is Patrick Cripps worth betting at $3.25 for 30+ disposals?", "Cripps is one of the most consistent disposal accumulators in the AFL. He averages 31+ per game and has cleared 30+ in 6 of his last 8 games. $3.25 is a great price given his consistency."),
            ("What time does Bulldogs vs Carlton start?", "1:10 PM AEST on Saturday 16 May 2026 at Marvel Stadium."),
            ("Where can I bet on AFL player specials?", "BetRight and Betr both offer 30+ disposal markets. See our <a href='/best-bookmakers-for-afl.html'>best bookmakers for AFL</a> for the full guide."),
        ],
        "round_label": "AFL Round 10 2026",
        "round_url": "afl-round-10-tips-2026.html",
        "sport_hub_url": "/afl-tips.html",
        "sport_hub_label": "AFL Tips 2026",
    },
    {
        "sport": "afl",
        "slug": "essendon-vs-fremantle",
        "title": "Essendon vs Fremantle — Round 10 2026",
        "meta_desc": "Essendon vs Fremantle Round 10 2026 tips and analysis. Line bet: Fremantle -34.5. Player special: Zach Merrett 30+ disposals $2.10. MCG. Full preview from PuntGuide.",
        "date_str": "Sunday 17 May 2026",
        "date_iso": "2026-05-17T13:10:00+10:00",
        "venue": "MCG, Melbourne",
        "kickoff": "1:10 PM AEST",
        "home": "Essendon",
        "away": "Fremantle",
        "home_form": "WLLLL",
        "away_form": "WWWWW",
        "home_analysis": "Essendon are 17th on the ladder with just 4 points — one win all season. They are at the MCG (away from Docklands) and their form shows they have no answers for quality opposition. Zach Merrett is the one player who accumulates regardless of team performance.",
        "away_analysis": "Fremantle are 2nd on the ladder with a remarkable 8-game winning streak — their longest since 2015. Andrew Brayshaw and Hayden Young drive the midfield, their defence concedes the fewest points in the competition, and their attack scores 94 points per game.",
        "context": "This should be a massive Fremantle win. The Dockers are genuine premiership contenders playing an Essendon side that has barely been competitive in 2026. The 34.5-point line is significant but Freo have won by 50+ multiple times against comparable opposition. Zach Merrett is the Essendon captain and he accumulates regardless of scoreline — making him a safe individual play even in a big loss.",
        "h2h": "Fremantle have won 6 of the last 8 meetings. This is only the second time these teams have met at the MCG since 1999.",
        "line_tip": "Fremantle -34.5",
        "line_desc": "Freo are 2nd on the ladder on an 8-game winning streak vs Essendon 17th with 1 win. The Dockers have won by 50+ this season — 34.5 is a manageable ask.",
        "player_tip": "Zach Merrett 30+ disposals $2.10",
        "player_desc": "The Essendon captain averages 26+ disposals per game and will accumulate regardless of the scoreline. In losing performances he often accumulates even more. $2.10 for 30+ is solid value.",
        "short_answer": "Fremantle are 2nd on the ladder on an 8-game winning streak against Essendon who have just 1 win in 2026. Line bet Fremantle -34.5, player pick Zach Merrett 30+ disposals at $2.10.",
        "key_findings": [
            "Fremantle's 8-game winning streak is their longest since 2015 — they are in exceptional form",
            "Essendon have won just 1 game in 2026 and struggle badly away from Docklands",
            "Zach Merrett averages 26+ disposals and typically accumulates MORE in losing games",
            "$2.10 for Merrett 30+ disposals is genuine value for an elite accumulator",
            "Freo's defensive record is the best in the competition — Essendon will struggle to score"
        ],
        "faqs": [
            ("What is the line bet for Essendon vs Fremantle?", "Fremantle -34.5. The Dockers need to win by 35 or more. Given Freo's form and Essendon's struggles, this is achievable."),
            ("Is Zach Merrett worth betting for 30+ disposals?", "Yes — Merrett is an elite accumulator who averages 26+ per game. In games where Essendon lose heavily, Merrett often has his highest disposal tallies as he becomes a primary ball-user."),
            ("Why is the game at the MCG and not Docklands?", "Essendon's home games are split between Marvel Stadium and the MCG. This game is scheduled for the MCG — only the second meeting at the MCG since 1999."),
            ("Where can I bet on Essendon vs Fremantle?", "BetRight and Betr have excellent player disposal markets. See our <a href='/best-bookmakers-for-afl.html'>best bookmakers for AFL</a> for the full comparison."),
        ],
        "round_label": "AFL Round 10 2026",
        "round_url": "afl-round-10-tips-2026.html",
        "sport_hub_url": "/afl-tips.html",
        "sport_hub_label": "AFL Tips 2026",
    },
    {
        "sport": "afl",
        "slug": "st-kilda-vs-richmond",
        "title": "St Kilda vs Richmond — Round 10 2026",
        "meta_desc": "St Kilda vs Richmond Round 10 2026 tips and analysis. Line bet: St Kilda -40.5. Player special: Jack Ross 25+ disposals $1.80. Full preview from PuntGuide.",
        "date_str": "Sunday 17 May 2026",
        "date_iso": "2026-05-17T15:15:00+10:00",
        "venue": "Marvel Stadium, Melbourne",
        "kickoff": "3:15 PM AEST",
        "home": "St Kilda",
        "away": "Richmond",
        "home_form": "WLWWL",
        "away_form": "LLLLL",
        "home_analysis": "St Kilda are 11th on the ladder and face the winless Richmond Tigers — a team that has conceded 969 points (108 per game) this season. The Saints should win comfortably and a 40.5-point line, while large, reflects Richmond's genuine inability to compete.",
        "away_analysis": "Richmond are 18th and winless through 9 rounds — the worst team in the competition by percentage. They concede 108 points per game and have been uncompetitive in almost every match. Jack Ross is their standout individual player and has been consistently accumulating disposals.",
        "context": "Richmond are winless and have been competitive in virtually no games this season. St Kilda are not a powerhouse side — they're 11th — but even a mid-table side should demolish a team of Richmond's current quality. 40.5 is a big line for St Kilda but Richmond are genuinely that bad. Jack Ross is the player to watch — he has cleared 25+ disposals in 4 straight games.",
        "h2h": "St Kilda have won 6 of the last 8 meetings. Richmond have not beaten St Kilda since Round 12 2024.",
        "line_tip": "St Kilda -40.5",
        "line_desc": "Richmond are winless (0-9), conceding 108 points per game. St Kilda, despite being only 11th, should cover a large line against the competition's worst side.",
        "player_tip": "Jack Ross 25+ disposals $1.80",
        "player_desc": "The Richmond midfielder has cleared 25+ disposals in each of his last 4 games — in form regardless of his team's results. $1.80 is solid value for such consistent recent form.",
        "short_answer": "Richmond are winless through 9 rounds and have conceded 969 points this season. St Kilda should win by a large margin — line bet Saints -40.5. Jack Ross 25+ disposals at $1.80 is the value player pick — Ross has cleared 25+ in his last 4 games.",
        "key_findings": [
            "Richmond are 0-9 and have conceded 969 points (108/game) — the worst defensive record in the competition",
            "Jack Ross has cleared 25+ disposals in each of his last 4 games",
            "$1.80 for Jack Ross 25+ disposals is great value given his current form",
            "St Kilda, despite being 11th, should win this comfortably",
            "Richmond have not won since Round 10 2025 — a remarkable losing streak"
        ],
        "faqs": [
            ("What is the line bet for St Kilda vs Richmond?", "St Kilda -40.5. The Saints need to win by 41 or more for the line bet to pay out."),
            ("Why is Jack Ross a good bet at $1.80?", "Ross has cleared 25+ disposals in 4 straight games. He's a hard-running midfielder who accumulates heavily even in losing teams. $1.80 is solid value for such consistent recent form."),
            ("What time does St Kilda vs Richmond start?", "3:15 PM AEST on Sunday 17 May 2026 at Marvel Stadium."),
            ("Where can I bet on AFL player disposals?", "BetRight and Betr have strong AFL player markets. See our <a href='/best-bookmakers-for-afl.html'>best bookmakers for AFL</a> guide."),
        ],
        "round_label": "AFL Round 10 2026",
        "round_url": "afl-round-10-tips-2026.html",
        "sport_hub_url": "/afl-tips.html",
        "sport_hub_label": "AFL Tips 2026",
    },
    {
        "sport": "afl",
        "slug": "gws-giants-vs-west-coast-eagles",
        "title": "GWS Giants vs West Coast Eagles — Round 10 2026",
        "meta_desc": "GWS Giants vs West Coast Eagles Round 10 2026 tips and analysis. Line bet: GWS -29.5. Player special: Toby Greene 2+ goals $1.90. Full preview from PuntGuide.",
        "date_str": "Sunday 17 May 2026",
        "date_iso": "2026-05-17T16:20:00+10:00",
        "venue": "Giants Stadium, Sydney",
        "kickoff": "4:20 PM AEST",
        "home": "GWS Giants",
        "away": "West Coast Eagles",
        "home_form": "WLWLW",
        "away_form": "LLLLL",
        "home_analysis": "GWS are competitive at home and have enough class through their midfield to dominate West Coast. Toby Greene leads the attack and the Giants are genuine finals aspirants. A -29.5 line at home against the competition's worst side is very manageable.",
        "away_analysis": "West Coast are 18th and winless (0-9), having scored 624 points and conceded 1,038 this season. They concede 115 points per game and have been competitive in almost no games. The travel to Sydney adds further disadvantage.",
        "context": "West Coast are the equal-worst team in the competition with Richmond. They have conceded 1,038 points in 9 games — 115 per game on average. GWS at home are a competent mid-table side who should cover the -29.5 line against opposition this poor. Toby Greene is dangerous in home conditions against a defence this leaky.",
        "h2h": "GWS have won 5 of the last 7 meetings. West Coast have not won at Giants Stadium since 2022.",
        "line_tip": "GWS Giants -29.5",
        "line_desc": "West Coast concede 115 points per game and are 0-9. GWS at home should cover the -29.5 line against the competition's worst defence.",
        "player_tip": "Toby Greene 2+ goals $1.90",
        "player_desc": "The GWS captain is their most dangerous forward. Against a West Coast defence that concedes 115 points per game, Greene will get opportunities. $1.90 for 2+ goals is strong value.",
        "short_answer": "West Coast are 0-9 and conceding 115 points per game — the worst defence in the competition. GWS should cover -29.5 at home. Player pick is Toby Greene 2+ goals at $1.90 — Greene is dangerous against this defence.",
        "key_findings": [
            "West Coast have conceded 1,038 points in 9 games (115/game) — worst defence in the competition",
            "GWS are undefeated at Giants Stadium in their last 4 games",
            "Toby Greene averages 1.8 goals per game and 2+ is a high-confidence market",
            "$1.90 for Greene 2+ goals is solid value against a defence this porous",
            "West Coast have not won at Giants Stadium since 2022"
        ],
        "faqs": [
            ("What is the line bet for GWS vs West Coast?", "GWS Giants -29.5. The Giants need to win by 30 or more for the line bet to pay out."),
            ("Is Toby Greene worth backing for 2+ goals?", "Yes — Greene is GWS's most dynamic forward and averages nearly 2 goals per game. Against West Coast's porous defence, 2+ goals at $1.90 is excellent value."),
            ("What time does GWS vs West Coast start?", "4:20 PM AEST on Sunday 17 May 2026 at Giants Stadium, Sydney."),
            ("Where can I bet on AFL goal scorer markets?", "BetRight and Betr both have goal scorer markets. See our <a href='/best-bookmakers-for-afl.html'>best bookmakers for AFL</a> guide."),
        ],
        "round_label": "AFL Round 10 2026",
        "round_url": "afl-round-10-tips-2026.html",
        "sport_hub_url": "/afl-tips.html",
        "sport_hub_label": "AFL Tips 2026",
    },
]

NRL_GAMES = [
    {
        "sport": "nrl",
        "slug": "magic-round-sharks-vs-bulldogs",
        "title": "Sharks vs Bulldogs — NRL Magic Round 2026",
        "meta_desc": "Cronulla Sharks vs Canterbury Bulldogs NRL Magic Round 2026 tips and analysis. Line bet: Sharks -5.5. Try scorer: Ronaldo Mulitalo. Full preview from PuntGuide.",
        "date_str": "Friday 15 May 2026",
        "date_iso": "2026-05-15T18:00:00+10:00",
        "venue": "Suncorp Stadium, Brisbane",
        "kickoff": "6:00 PM AEST",
        "home": "Cronulla Sharks",
        "away": "Canterbury Bulldogs",
        "home_form": "WWLWW",
        "away_form": "LWLLW",
        "home_analysis": "The Sharks are in strong form and Ronaldo Mulitalo returns from his ACL injury — an emotional comeback that will see him receive heavy involvement in the early exchanges. The Sharks' outside backs are their key attacking weapon and Mulitalo's return makes them significantly more dangerous.",
        "away_analysis": "The Bulldogs have been inconsistent and face a Sharks side with genuine outside-back threat. Their defensive edge defence will be tested by Mulitalo's pace and the Sharks' structured attack.",
        "context": "Magic Round brings all 8 NRL games to Suncorp Stadium in Brisbane — a carnival atmosphere that energises every team. The Sharks open the weekend with Mulitalo's highly-anticipated return from an ACL injury suffered midway through 2025. Emotional comebacks at Magic Round are a well-established NRL tradition.",
        "h2h": "The Sharks have won 4 of the last 6 meetings. Last match: Sharks won by 8 points in Round 19 2025.",
        "line_tip": "Sharks -5.5",
        "line_desc": "Mulitalo's emotional return adds genuine outside-back threat the Bulldogs cannot match. Sharks in form and should cover -5.5 in a comfortable win.",
        "player_tip": "Ronaldo Mulitalo anytime try scorer",
        "player_desc": "Emotional comeback from ACL injury. Expect the Sharks to target Mulitalo early — he'll receive heavy involvement and is motivated to score on return.",
        "short_answer": "Cronulla Sharks open Magic Round with Ronaldo Mulitalo's emotional ACL return. Line bet Sharks -5.5. Mulitalo is the try scorer pick — expect the Sharks to target him early in an emotional comeback game.",
        "key_findings": [
            "Ronaldo Mulitalo returns from a long-term ACL injury — emotional comeback motivation",
            "Magic Round atmosphere at Suncorp tends to produce high-scoring, attacking football",
            "Sharks have won 4 of their last 6 against the Bulldogs",
            "Mulitalo scored 15 tries in 2024 before his injury — he's a genuine finishing threat",
            "BetRight and Betr both have NRL try scorer markets — compare before placing"
        ],
        "faqs": [
            ("What is the line bet for Sharks vs Bulldogs?", "Cronulla Sharks -5.5. The Sharks need to win by 6 or more for the line bet to pay out."),
            ("Is Ronaldo Mulitalo a good try scorer bet on return?", "Yes — Mulitalo is one of the NRL's best wingers and emotional returns from injury are often well scripted. Expect the Sharks to give him early opportunities."),
            ("Where is Magic Round played?", "All 8 Round 11 games are played at Suncorp Stadium in Brisbane — Magic Round is a unique NRL event where all games are in one city."),
            ("Where can I bet on NRL try scorers?", "BetRight and Betr both offer competitive NRL try scorer markets. See our <a href='/best-bookmakers-for-nrl.html'>best bookmakers for NRL</a> guide."),
        ],
        "round_label": "NRL Round 11 Magic Round 2026",
        "round_url": "nrl-round-11-tips-2026.html",
        "sport_hub_url": "/nrl-tips.html",
        "sport_hub_label": "NRL Tips 2026",
    },
    {
        "sport": "nrl",
        "slug": "magic-round-rabbitohs-vs-dolphins",
        "title": "Rabbitohs vs Dolphins — NRL Magic Round 2026",
        "meta_desc": "South Sydney Rabbitohs vs Dolphins NRL Magic Round 2026 tips and analysis. Line bet: Rabbitohs +1.5. Try scorer: Latrell Mitchell. Full preview from PuntGuide.",
        "date_str": "Friday 15 May 2026",
        "date_iso": "2026-05-15T20:05:00+10:00",
        "venue": "Suncorp Stadium, Brisbane",
        "kickoff": "8:05 PM AEST",
        "home": "South Sydney Rabbitohs",
        "away": "Dolphins",
        "home_form": "LWWWL",
        "away_form": "WWLWW",
        "home_analysis": "The Rabbitohs are boosted by Latrell Mitchell's return in the centres — a game-changing addition that gives Souths dominant physical presence and a genuine try-scoring threat on the edge.",
        "away_analysis": "The Dolphins are the slight favourites at -1.5 and have been in strong form. Home ground advantage at Suncorp suits Brisbane-based clubs and they'll be confident.",
        "context": "With the Dolphins as slight favourites, taking Rabbitohs +1.5 gives us margin. Latrell Mitchell's return is the headline — he's one of the NRL's most powerful centres and Souths will build their attack around his involvement.",
        "h2h": "These teams have met only 3 times since the Dolphins entered the competition. Series level at 1-1 (one draw).",
        "line_tip": "Rabbitohs +1.5",
        "line_desc": "Latrell Mitchell's return gives Souths a dominant physical edge in the centres. Taking +1.5 with Souths provides margin — if they win outright or keep it close, the line pays.",
        "player_tip": "Latrell Mitchell anytime try scorer",
        "player_desc": "Mitchell is one of the NRL's most dangerous centres and scores at a high rate. Motivated return at Magic Round — expect Souths to design plays through their star man.",
        "short_answer": "Latrell Mitchell returns for South Sydney in a tight game against the Dolphins. Line bet Rabbitohs +1.5 provides margin in an even contest. Latrell Mitchell is the try scorer pick — expect Souths to centre their attack on their returning star.",
        "key_findings": [
            "Latrell Mitchell returns from injury — one of the NRL's most dynamic centres",
            "Dolphins are slight favourites but the margin is tight at -1.5",
            "Mitchell scored 12 tries in 2024 before his injury — elite finishing threat",
            "Magic Round at Suncorp tends to be open, attacking football",
            "BetRight and Betr both carry Latrell Mitchell try scorer markets"
        ],
        "faqs": [
            ("What is the line bet for Rabbitohs vs Dolphins?", "We're taking Rabbitohs +1.5 — the Dolphins are slight favourites but +1.5 provides valuable margin in a tight game."),
            ("Is Latrell Mitchell worth backing as a try scorer?", "Yes — Latrell is one of the NRL's best finishers and Souths will target him heavily on return. He scores at a high rate when fit and motivated."),
            ("What time does Rabbitohs vs Dolphins start?", "8:05 PM AEST on Friday 15 May 2026 at Suncorp Stadium, Brisbane."),
            ("Where can I bet on NRL try scorers?", "BetRight, Betr and Sportsbet all have excellent NRL try scorer markets. See our <a href='/best-bookmakers-for-nrl.html'>best bookmakers for NRL</a> guide."),
        ],
        "round_label": "NRL Round 11 Magic Round 2026",
        "round_url": "nrl-round-11-tips-2026.html",
        "sport_hub_url": "/nrl-tips.html",
        "sport_hub_label": "NRL Tips 2026",
    },
    {
        "sport": "nrl",
        "slug": "magic-round-wests-tigers-vs-sea-eagles",
        "title": "Wests Tigers vs Sea Eagles — NRL Magic Round 2026",
        "meta_desc": "Wests Tigers vs Manly Sea Eagles NRL Magic Round 2026 tips and analysis. Line bet: Sea Eagles -8.5. Try scorer: Reuben Garrick. Full preview from PuntGuide.",
        "date_str": "Saturday 16 May 2026",
        "date_iso": "2026-05-16T15:00:00+10:00",
        "venue": "Suncorp Stadium, Brisbane",
        "kickoff": "3:00 PM AEST",
        "home": "Wests Tigers",
        "away": "Manly Sea Eagles",
        "home_form": "LLLWL",
        "away_form": "WWLWW",
        "home_analysis": "The Wests Tigers have been inconsistent and lack the firepower to trouble a Manly side with Fogarty returning. Their defensive edge defence has leaked tries in recent weeks.",
        "away_analysis": "Manly are in strong form (WWLWW) and benefit from Tom Fogarty's return which strengthens their kicking and general play. Reuben Garrick is a reliable winger who scored last round and has been consistently involved.",
        "context": "Manly are the stronger side and should cover -8.5 against a Wests Tigers team struggling for consistency. Fogarty's return is a genuine upgrade that gives Manly's spine more options. Garrick on the wing is the natural try scorer play.",
        "h2h": "Manly have won 5 of the last 8 meetings. Last match: Manly won by 12 points in Round 7 2025.",
        "line_tip": "Sea Eagles -8.5",
        "line_desc": "Fogarty's return strengthens Manly significantly. Wests Tigers inconsistent with a leaky edge defence — Sea Eagles should cover -8.5 in a comfortable win.",
        "player_tip": "Reuben Garrick anytime try scorer",
        "player_desc": "Garrick is a reliable finisher on the Manly wing who scored last round. When Sea Eagles dominate field position and spread the ball wide, Garrick is a consistent threat.",
        "short_answer": "Manly Sea Eagles are in form and get Tom Fogarty back, facing Wests Tigers who have been inconsistent. Line bet Sea Eagles -8.5. Reuben Garrick is the try scorer pick — scored last round and gets the ball in space.",
        "key_findings": [
            "Tom Fogarty returns for Manly — significant upgrade to their spine and kicking game",
            "Wests Tigers have been leaking tries on the edge in recent weeks",
            "Reuben Garrick scored last round and has tries in 4 of his last 6 games",
            "Manly have won 5 of last 8 against the Tigers",
            "BetRight and Betr have NRL try scorer markets — compare before placing"
        ],
        "faqs": [
            ("What is the line bet for Wests Tigers vs Sea Eagles?", "Sea Eagles -8.5. Manly need to win by 9 or more for the line bet to pay out."),
            ("Is Reuben Garrick a good try scorer bet?", "Yes — Garrick is a reliable finisher who scored last round. When Manly spread the ball wide, he gets genuine opportunities. He's scored in 4 of his last 6 games."),
            ("What time does Tigers vs Sea Eagles start?", "3:00 PM AEST on Saturday 16 May 2026 at Suncorp Stadium, Brisbane."),
            ("Where can I bet on NRL Magic Round?", "All 8 Magic Round games are available at BetRight and Betr. See our <a href='/best-bookmakers-for-nrl.html'>best bookmakers for NRL</a> guide."),
        ],
        "round_label": "NRL Round 11 Magic Round 2026",
        "round_url": "nrl-round-11-tips-2026.html",
        "sport_hub_url": "/nrl-tips.html",
        "sport_hub_label": "NRL Tips 2026",
    },
    {
        "sport": "nrl",
        "slug": "magic-round-roosters-vs-cowboys",
        "title": "Roosters vs Cowboys — NRL Magic Round 2026",
        "meta_desc": "Sydney Roosters vs North Queensland Cowboys NRL Magic Round 2026 tips and analysis. Line bet: Roosters -15.5. Try scorer: Daniel Tupou. Full preview from PuntGuide.",
        "date_str": "Saturday 16 May 2026",
        "date_iso": "2026-05-16T17:30:00+10:00",
        "venue": "Suncorp Stadium, Brisbane",
        "kickoff": "5:30 PM AEST",
        "home": "Sydney Roosters",
        "away": "North Queensland Cowboys",
        "home_form": "WWWLW",
        "away_form": "LWLLL",
        "home_analysis": "The Roosters are in excellent form and are one of the competition's top sides. Their spine of Smith, Tedesco and Keary controls games and Daniel Tupou on the wing is a consistent finisher when the Roosters dominate field position.",
        "away_analysis": "The Cowboys are significantly weakened — Jason Taumalolo is rested and Mason Sutton makes his debut at halfback. Losing Taumalolo removes their most dominant forward and Sutton's inexperience in the spine will be exposed by a quality Roosters defence.",
        "context": "Magic Round's marquee game. The Cowboys come in with significant disadvantages — Taumalolo rested and an NRL debutant halfback in Sutton. The Roosters are the class side and should win comfortably. Roosters -15.5 is achievable but a big ask on the road. Daniel Tupou is the natural play — he's one of the competition's most reliable try scorers.",
        "h2h": "Roosters have won 6 of the last 9 meetings against the Cowboys. Last match: Roosters won by 20 points in Round 3 2026.",
        "line_tip": "Roosters -15.5",
        "line_desc": "Taumalolo rested and Sutton on debut — Cowboys spine too inexperienced. Roosters are the class side and should cover -15.5 in the marquee Magic Round fixture.",
        "player_tip": "Daniel Tupou anytime try scorer",
        "player_desc": "Roosters' winger in form — reliable finisher when Sydney dominate field position. The Cowboys' edge defence will be exposed by a quality Roosters attack.",
        "short_answer": "Match of the Round at Magic Round. Cowboys lose Taumalolo (rested) and start a debutant halfback. Roosters -15.5 looks achievable. Daniel Tupou is the try scorer pick — reliable finisher when the Roosters dominate.",
        "key_findings": [
            "Taumalolo is rested for the Cowboys — their most dominant forward is missing",
            "Mason Sutton makes his NRL debut at halfback — inexperience will be exposed",
            "Daniel Tupou has scored in 5 of his last 7 games",
            "Roosters have won 6 of the last 9 against the Cowboys",
            "BetRight and Betr both have Cowboys vs Roosters try scorer markets"
        ],
        "faqs": [
            ("What is the line bet for Roosters vs Cowboys?", "Sydney Roosters -15.5. The Roosters need to win by 16 or more for the line bet to pay out."),
            ("Is Daniel Tupou a reliable try scorer bet?", "Yes — Tupou has scored in 5 of his last 7 games and is one of the NRL's most consistent wingers. When the Roosters dominate, he gets quality ball in space."),
            ("Why is Taumalolo resting?", "Jason Taumalolo is managed for Magic Round — a State of Origin rest is likely, which significantly weakens the Cowboys' forward pack."),
            ("Where can I bet on Roosters vs Cowboys?", "BetRight, Betr and Sportsbet all cover Magic Round in full. See our <a href='/best-bookmakers-for-nrl.html'>best bookmakers for NRL</a> guide."),
        ],
        "round_label": "NRL Round 11 Magic Round 2026",
        "round_url": "nrl-round-11-tips-2026.html",
        "sport_hub_url": "/nrl-tips.html",
        "sport_hub_label": "NRL Tips 2026",
    },
    {
        "sport": "nrl",
        "slug": "magic-round-eels-vs-storm",
        "title": "Eels vs Storm — NRL Magic Round 2026",
        "meta_desc": "Parramatta Eels vs Melbourne Storm NRL Magic Round 2026 tips and analysis. Line bet: Eels +9.5. Try scorer: Josh Addo-Carr. Full preview from PuntGuide.",
        "date_str": "Saturday 16 May 2026",
        "date_iso": "2026-05-16T19:45:00+10:00",
        "venue": "Suncorp Stadium, Brisbane",
        "kickoff": "7:45 PM AEST",
        "home": "Parramatta Eels",
        "away": "Melbourne Storm",
        "home_form": "LWLLW",
        "away_form": "WWWLW",
        "home_analysis": "The Eels have been inconsistent but have cover — they fight hard and their defensive structure keeps games close. Getting +9.5 against Melbourne provides significant value in a game that could go either way.",
        "away_analysis": "Melbourne Storm are strong favourites (-9.5) and Josh Addo-Carr is their most dynamic winger. The Storm's structured attack creates regular opportunities on the edges and Addo-Carr has been scoring at a high rate.",
        "context": "Melbourne are the quality side but 9.5 points is significant margin. The Eels have shown they can compete and the value is in taking the points. Josh Addo-Carr is the player pick — the Storm's winger scored last round and the Eels' edge defence has leaked tries.",
        "h2h": "Melbourne have won 6 of the last 9 meetings. Eels last beat the Storm in Round 14 2025.",
        "line_tip": "Eels +9.5",
        "line_desc": "Storm are -9.5 favourites but 9.5 points is significant margin. Eels have fight and cover — value in Parramatta getting 9.5 points in what could be a competitive game.",
        "player_tip": "Josh Addo-Carr anytime try scorer",
        "player_desc": "Storm's most dynamic winger who scored last round. The Eels' edge defence has leaked tries and Addo-Carr will get opportunities when Melbourne spread the ball.",
        "short_answer": "Melbourne Storm are 9.5-point favourites against the Eels. We're taking Parramatta +9.5 for value. Josh Addo-Carr is the try scorer pick — he scored last round and gets plenty of ball when Melbourne dominate.",
        "key_findings": [
            "Parramatta +9.5 provides significant margin in a potentially competitive game",
            "Josh Addo-Carr scored last round and has tries in 6 of his last 8 games",
            "The Eels' edge defence has leaked tries in recent weeks — opportunity for Addo-Carr",
            "Night game at Suncorp tends to produce attacking football",
            "Compare Storm vs Eels try scorer markets at BetRight and Betr"
        ],
        "faqs": [
            ("What is the line bet for Eels vs Storm?", "We're taking Parramatta Eels +9.5 — Melbourne are the favourites but 9.5 points is significant value with the Eels."),
            ("Is Josh Addo-Carr worth backing as a try scorer?", "Yes — Addo-Carr scored last round and has scored in 6 of his last 8 games. When Melbourne dominate and spread the ball wide, he gets quality opportunities."),
            ("What time does Eels vs Storm start?", "7:45 PM AEST on Saturday 16 May 2026 at Suncorp Stadium, Brisbane."),
            ("Where can I bet on NRL player try scorers?", "BetRight, Betr and Sportsbet all have NRL try scorer markets. See our <a href='/best-bookmakers-for-nrl.html'>best bookmakers for NRL</a> guide."),
        ],
        "round_label": "NRL Round 11 Magic Round 2026",
        "round_url": "nrl-round-11-tips-2026.html",
        "sport_hub_url": "/nrl-tips.html",
        "sport_hub_label": "NRL Tips 2026",
    },
    {
        "sport": "nrl",
        "slug": "magic-round-titans-vs-knights",
        "title": "Titans vs Knights — NRL Magic Round 2026",
        "meta_desc": "Gold Coast Titans vs Newcastle Knights NRL Magic Round 2026 tips and analysis. Line bet: Knights -9.5. Try scorer: Greg Marzhew. Full preview from PuntGuide.",
        "date_str": "Sunday 17 May 2026",
        "date_iso": "2026-05-17T14:00:00+10:00",
        "venue": "Suncorp Stadium, Brisbane",
        "kickoff": "2:00 PM AEST",
        "home": "Gold Coast Titans",
        "away": "Newcastle Knights",
        "home_form": "LLWLL",
        "away_form": "WWWWL",
        "home_analysis": "The Titans are 16th on the NRL ladder and have been in poor form (LLWLL). Their forward pack has been outmuscled in recent weeks and they lack the spine quality to trouble a flying Knights side.",
        "away_analysis": "Newcastle are flying — Greg Marzhew has been in unstoppable form, scoring in recent rounds. The Knights have genuine forward power and a quality spine. They should cover -9.5 against a Titans side this depleted.",
        "context": "Newcastle are in excellent form and face a Titans side 16th on the ladder. The Knights should win comfortably and Greg Marzhew is the standout play — he's been scoring at will and the Titans' edge defence has been exposed regularly.",
        "h2h": "Newcastle have won 5 of the last 8 meetings. Last match: Knights won by 14 points in Round 5 2026.",
        "line_tip": "Knights -9.5",
        "line_desc": "Newcastle flying and Titans 16th. Knights' forward power and Marzhew's form should be too much for a struggling Titans side — cover -9.5.",
        "player_tip": "Greg Marzhew anytime try scorer",
        "player_desc": "Newcastle's explosive winger has been in unstoppable form — scored last round and the Titans' edge defence is among the weakest in the competition.",
        "short_answer": "Newcastle Knights are in top form facing a Titans side struggling in 16th place. Line bet Knights -9.5. Greg Marzhew is the try scorer pick — he's been scoring in every game and the Titans' edge defence is exposed.",
        "key_findings": [
            "Gold Coast Titans are 16th on the ladder and their edge defence has leaked tries consistently",
            "Greg Marzhew scored last round and is in outstanding form",
            "Newcastle have won 5 of their last 6 games entering Magic Round",
            "Knights have won 5 of last 8 against the Titans",
            "BetRight and Betr both carry Marzhew try scorer markets — compare before placing"
        ],
        "faqs": [
            ("What is the line bet for Titans vs Knights?", "Newcastle Knights -9.5. The Knights need to win by 10 or more for the line bet to pay out."),
            ("Is Greg Marzhew a good try scorer bet?", "Yes — Marzhew is one of the NRL's most exciting wingers and has been scoring in virtually every game. The Titans' edge defence is vulnerable."),
            ("What time does Titans vs Knights start?", "2:00 PM AEST on Sunday 17 May 2026 at Suncorp Stadium, Brisbane."),
            ("Where can I bet on NRL Magic Round?", "BetRight and Betr have full Magic Round coverage. See our <a href='/best-bookmakers-for-nrl.html'>best bookmakers for NRL</a> guide."),
        ],
        "round_label": "NRL Round 11 Magic Round 2026",
        "round_url": "nrl-round-11-tips-2026.html",
        "sport_hub_url": "/nrl-tips.html",
        "sport_hub_label": "NRL Tips 2026",
    },
    {
        "sport": "nrl",
        "slug": "magic-round-warriors-vs-broncos",
        "title": "Warriors vs Broncos — NRL Magic Round 2026",
        "meta_desc": "New Zealand Warriors vs Brisbane Broncos NRL Magic Round 2026 tips and analysis. Line bet: Warriors -2.5. Try scorer: Dallin Watene-Zelezniak. Full preview from PuntGuide.",
        "date_str": "Sunday 17 May 2026",
        "date_iso": "2026-05-17T16:05:00+10:00",
        "venue": "Suncorp Stadium, Brisbane",
        "kickoff": "4:05 PM AEST",
        "home": "New Zealand Warriors",
        "away": "Brisbane Broncos",
        "home_form": "WWLWL",
        "away_form": "LWLWL",
        "home_analysis": "The Warriors are slight favourites at -2.5 and Dallin Watene-Zelezniak is their most dangerous winger. The Warriors have the class to win this tight contest and their spine has been consistent.",
        "away_analysis": "Brisbane Broncos are injury-hit and their edge defence has been vulnerable. Playing against a Warriors side that targets the edges, DWZ is the natural threat.",
        "context": "A genuinely tight game — the -2.5 line reflects how even these sides are. Both teams are built on Brisbane territory (Warriors training base in Queensland) and Suncorp suits both sides. Warriors class should prevail but the margin will be small. DWZ is a consistent try scorer who will get opportunities against an injury-hit Broncos edge.",
        "h2h": "The Warriors have won 4 of the last 7 meetings. Last match: Warriors won by 6 points in Round 8 2026.",
        "line_tip": "Warriors -2.5",
        "line_desc": "Market has this tight at -2.5 — Warriors class should prevail in a close game. Both sides familiar with Suncorp but Warriors have the edge in individual quality.",
        "player_tip": "Dallin Watene-Zelezniak anytime try scorer",
        "player_desc": "Warriors' class finisher who gets quality opportunities when the Warriors attack the edges. Against an injury-hit Broncos edge defence, DWZ is the natural beneficiary.",
        "short_answer": "Warriors vs Broncos is the tightest game of Magic Round — just -2.5 separating the sides. Warriors class should prevail. Dallin Watene-Zelezniak is the try scorer pick — he's a consistent finisher who will get opportunities against an injury-hit Broncos edge.",
        "key_findings": [
            "Warriors -2.5 is the tightest line of Magic Round — genuinely even contest",
            "Broncos are missing key edge defenders through injury",
            "Dallin Watene-Zelezniak has scored in 5 of his last 8 games",
            "Suncorp suits the Warriors' playing style — they train and prepare in Queensland",
            "Compare Warriors vs Broncos try scorer markets at BetRight and Betr"
        ],
        "faqs": [
            ("What is the line bet for Warriors vs Broncos?", "New Zealand Warriors -2.5. The Warriors need to win by 3 or more for the line bet to pay out."),
            ("Is Dallin Watene-Zelezniak a good try scorer bet?", "Yes — DWZ is a reliable winger who scores regularly. With the Broncos missing key edge defenders through injury, he should get quality ball in space."),
            ("What time does Warriors vs Broncos start?", "4:05 PM AEST on Sunday 17 May 2026 at Suncorp Stadium, Brisbane."),
            ("Where can I bet on NRL try scorer markets?", "BetRight and Betr both have Warriors vs Broncos try scorer markets. See our <a href='/best-bookmakers-for-nrl.html'>best bookmakers for NRL</a> guide."),
        ],
        "round_label": "NRL Round 11 Magic Round 2026",
        "round_url": "nrl-round-11-tips-2026.html",
        "sport_hub_url": "/nrl-tips.html",
        "sport_hub_label": "NRL Tips 2026",
    },
    {
        "sport": "nrl",
        "slug": "magic-round-panthers-vs-dragons",
        "title": "Panthers vs Dragons — NRL Magic Round 2026",
        "meta_desc": "Penrith Panthers vs St George Illawarra Dragons NRL Magic Round 2026 tips and analysis. Line bet: Panthers -27.5. Try scorer: Nathan Cleary. Full preview from PuntGuide.",
        "date_str": "Sunday 17 May 2026",
        "date_iso": "2026-05-17T18:25:00+10:00",
        "venue": "Suncorp Stadium, Brisbane",
        "kickoff": "6:25 PM AEST",
        "home": "Penrith Panthers",
        "away": "St George Illawarra Dragons",
        "home_form": "WWWWW",
        "away_form": "LLLLL",
        "home_analysis": "The Penrith Panthers are the best team in the NRL by a significant margin — dominant in every facet of the game. Nathan Cleary orchestrates everything and the Panthers have won their last 5 by an average of 25+ points.",
        "away_analysis": "The St George Illawarra Dragons are 0-9 for the season — winless — and missing their halfback for three months. They have been uncompetitive in virtually every game and face the biggest task in the competition.",
        "context": "This is as close to a guaranteed result as the NRL produces. The Dragons are 0-9, missing their halfback, and face a Panthers side that has been as dominant as any team in recent memory. -27.5 is a big line but the Panthers have covered this and more against comparable opposition. Nathan Cleary also chips in with tries when the scoreline opens up.",
        "h2h": "Penrith have won 9 of the last 10 meetings against the Dragons. Last match: Panthers won by 34 points in Round 6 2026.",
        "line_tip": "Panthers -27.5",
        "line_desc": "Dragons 0-9 and missing their halfback for 3 months. Panthers are the best side in the comp by a clear margin. -27.5 is a big ask but they've covered more against this quality of opposition.",
        "player_tip": "Nathan Cleary anytime try scorer",
        "player_desc": "Panthers halfback chips in with tries regularly when the scoreline opens up. Against a winless Dragons side, the game will be open and Cleary will have scoring opportunities.",
        "short_answer": "The Panthers vs Dragons is the most lopsided game of Magic Round. Dragons are 0-9 and missing their halfback. Panthers -27.5 is the line bet. Nathan Cleary is the try scorer pick — he scores regularly when Penrith open up a big lead.",
        "key_findings": [
            "St George Illawarra are 0-9 for the season and missing their halfback for 3 months",
            "Penrith Panthers have won their last 5 by 25+ points on average",
            "Nathan Cleary has scored a try in 4 of his last 7 games",
            "The Panthers have won 9 of the last 10 against the Dragons",
            "Magic Round finale — high-octane atmosphere that suits the Panthers' fast style"
        ],
        "faqs": [
            ("What is the line bet for Panthers vs Dragons?", "Penrith Panthers -27.5. The Panthers need to win by 28 or more for the line bet to pay out."),
            ("Is Nathan Cleary worth backing as a try scorer?", "Yes — Cleary scores regularly when Penrith open up big leads. Against a winless Dragons side the game will get away quickly and Cleary will have multiple scoring opportunities."),
            ("Why are the Dragons 0-9?", "The Dragons are in a rebuilding phase with injuries to key players, including their halfback being ruled out for three months, leaving them with significant spine problems all season."),
            ("Where can I bet on Panthers vs Dragons?", "BetRight, Betr and Sportsbet all carry full Magic Round markets. See our <a href='/best-bookmakers-for-nrl.html'>best bookmakers for NRL</a> guide."),
        ],
        "round_label": "NRL Round 11 Magic Round 2026",
        "round_url": "nrl-round-11-tips-2026.html",
        "sport_hub_url": "/nrl-tips.html",
        "sport_hub_label": "NRL Tips 2026",
    },
]

# ── Generate all pages ──────────────────────────────────────────────────────
def main():
    base = "/Users/angusmead/puntguide"

    for game in AFL_GAMES:
        path = f"{base}/afl/2026/round-10/{game['slug']}.html"
        html = generate_page(game)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated: {path}")

    for game in NRL_GAMES:
        path = f"{base}/nrl/2026/round-11/{game['slug']}.html"
        html = generate_page(game)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated: {path}")

    print(f"\nTotal: {len(AFL_GAMES) + len(NRL_GAMES)} pages generated")

if __name__ == "__main__":
    main()
