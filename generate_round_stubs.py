#!/usr/bin/env python3
"""Generate round stub pages for all AFL and NRL rounds in 2026."""
import os, json

OUT  = os.path.expanduser('~/puntguide')
SITE = 'https://puntguide.com.au'

# Current rounds (these already have full content)
AFL_CURRENT = 8
NRL_CURRENT = 9  # file is named round-10 but content is round 9

AFL_TOTAL = 23
NRL_TOTAL = 27

CSS = """:root{--bg:hsl(205 60% 96%);--fg:hsl(215 45% 16%);--primary:hsl(48 92% 64%);--pfg:hsl(215 45% 16%);--muted:hsl(205 40% 92%);--muted-fg:hsl(215 20% 42%);--accent:hsl(200 88% 58%);--border:hsl(205 40% 86%);--gg:linear-gradient(135deg,hsl(50 96% 72%),hsl(44 92% 60%));--sg:0 10px 40px -10px hsl(48 92% 54%/.4);--sc:0 4px 24px -8px hsl(215 50% 30%/.1);--ch:36px;--nh:80px;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--fg);font-family:"Inter Tight",sans-serif;line-height:1.65;font-size:15px;}
h1,h2,h3{font-family:"Geist",sans-serif;letter-spacing:-0.03em;}
a{color:inherit;}
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
.section{background:#fff;border:1px solid var(--border);border-radius:14px;padding:24px 28px;margin:24px 0;box-shadow:var(--sc);}
.section h2{font-size:20px;font-weight:700;margin-bottom:14px;}
.rounds-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:10px;margin:16px 0;}
.round-btn{display:block;text-align:center;padding:12px 8px;background:var(--muted);border-radius:8px;text-decoration:none;font-weight:600;font-size:13px;transition:background .15s;}
.round-btn:hover{background:var(--border);}
.round-btn.current{background:var(--primary);color:var(--pfg);}
.round-btn.past{opacity:0.7;}
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
@media(max-width:768px){.nav-links{display:none;}.wrap,.hero{padding-left:16px;padding-right:16px;}.nav{padding:0 20px;}}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800&family=Inter+Tight:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">'

def faq_schema(sport, rnd):
    if sport == 'AFL':
        faqs = [
            (f"Where can I find AFL Round {rnd} tips?", f"PuntGuide publishes expert AFL tips for every game in Round {rnd} 2026. Our analysis covers team form, head-to-head records, venue factors and betting market value for every match."),
            (f"Which bookmaker is best for AFL Round {rnd} betting?", "PointsBet is our top pick for AFL betting — sharp head-to-head odds and unique PointsBetting markets. Sportsbet has the widest AFL market range. Ladbrokes is most competitive on head-to-head prices."),
            (f"What AFL matches are in Round {rnd} 2026?", f"AFL Round {rnd} 2026 fixtures will be confirmed by the AFL in advance of the round. Check this page for full match details, tips and analysis as they are published."),
            ("How do I bet on AFL in Australia?", "To bet on AFL in Australia, open an account with a licensed Australian bookmaker such as PointsBet, Sportsbet or Ladbrokes. You must be 18 or over. Compare odds across multiple bookmakers for best value."),
            ("Are AFL betting tips legal in Australia?", "Yes. AFL betting tips and predictions are legal in Australia. Betting on AFL with a licensed bookmaker is legal for adults 18 and over. Tips are editorial predictions only and are not financial advice."),
        ]
    else:
        faqs = [
            (f"Where can I find NRL Round {rnd} tips?", f"PuntGuide publishes expert NRL tips for every game in Round {rnd} 2026. Our analysis covers team form, head-to-head records, venue factors and betting market value for every match."),
            (f"Which bookmaker is best for NRL Round {rnd} betting?", "PointsBet is our top pick for NRL — sharp odds and PointsBetting markets on NRL stats. betr has the best same-game multi builder. Sportsbet has the widest NRL market range."),
            (f"What NRL matches are in Round {rnd} 2026?", f"NRL Round {rnd} 2026 fixtures will be confirmed by the NRL ahead of the round. Check this page for full match details, tips and analysis as they are published."),
            ("How do I bet on NRL in Australia?", "To bet on NRL in Australia, open an account with a licensed bookmaker such as PointsBet, betr or Sportsbet. You must be 18 or over. Always compare odds across bookmakers for best value."),
            ("Are NRL betting tips legal in Australia?", "Yes. NRL betting tips are legal in Australia. Betting on NRL with a licensed bookmaker is legal for adults 18 and over. Tips are editorial predictions only and are not financial advice."),
        ]
    items = ','.join([f'{{"@type":"Question","name":{json.dumps(q)},"acceptedAnswer":{{"@type":"Answer","text":{json.dumps(a)}}}}}' for q,a in faqs])
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{items}]}}</script>', faqs

def rounds_grid(sport, total, current, current_slug):
    html = '<div class="rounds-grid">'
    for r in range(1, total + 1):
        if sport == 'AFL':
            slug = f'/afl-round-{r}-tips-2026.html'
            label = f'Round {r}'
        else:
            slug = f'/nrl-round-{r}-tips-2026.html'
            label = f'Round {r}'
        if r == current:
            cls = 'round-btn current'
        elif r < current:
            cls = 'round-btn past'
        else:
            cls = 'round-btn'
        html += f'<a href="{slug}" class="{cls}">{label}</a>'
    html += '</div>'
    return html

def build_stub(sport, rnd, total, current):
    is_past    = rnd < current
    is_current = rnd == current
    is_future  = rnd > current
    emoji      = '🏈' if sport == 'AFL' else '🏉'

    if sport == 'AFL':
        slug          = f'afl-round-{rnd}-tips-2026.html'
        hub_slug      = '/afl-tips.html'
        hub_label     = 'AFL Tips 2026'
        ladder_slug   = '/afl-ladder-2026.html'
        best_slug     = '/best-betting-sites-for-afl.html'
        best_label    = 'Best Sites for AFL'
        current_slug  = f'/afl-round-{AFL_CURRENT}-tips-2026.html'
        odds_slug     = '/afl-premiership-odds-2026.html'
        odds_label    = 'AFL Premiership Odds'
        bm1_logo, bm1_name, bm1_tag = 'pointsbet.png', 'PointsBet', 'Sharpest AFL odds + PointsBetting markets'
        bm2_logo, bm2_name, bm2_tag = 'sportsbet.png', 'Sportsbet', 'Widest AFL market range in Australia'
    else:
        slug          = f'nrl-round-{rnd}-tips-2026.html'
        hub_slug      = '/nrl-tips.html'
        hub_label     = 'NRL Tips 2026'
        ladder_slug   = '/nrl-ladder-2026.html'
        best_slug     = '/best-betting-sites-afl-nrl.html'
        best_label    = 'Best Sites for NRL'
        current_slug  = '/nrl-round-10-tips-2026.html'
        odds_slug     = '/nrl-premiership-odds-2026.html'
        odds_label    = 'NRL Premiership Odds'
        bm1_logo, bm1_name, bm1_tag = 'pointsbet.png', 'PointsBet', 'Sharpest NRL odds + PointsBetting markets'
        bm2_logo, bm2_name, bm2_tag = 'betr.png', 'betr', 'Best NRL same-game multi builder in Australia'

    # Skip if file already has full content
    full_path = os.path.join(OUT, slug)
    if os.path.exists(full_path) and os.path.getsize(full_path) > 20000:
        return None  # already has rich content

    if is_past:
        title    = f'{sport} Round {rnd} Tips 2026 — Results & Analysis | PuntGuide'
        desc     = f'{sport} Round {rnd} 2026 — results, match analysis and key moments. Plus tips for upcoming rounds and best Australian bookmakers for {sport} betting.'
        h1       = f'{emoji} {sport} Round {rnd} Tips & Results 2026'
        eyebrow  = f'{sport} 2026 · Round {rnd} · Completed'
        body_content = f'''<div class="section">
  <h2>Round {rnd} — Completed</h2>
  <p style="font-size:15px;line-height:1.8;color:hsl(215 45% 16%/.8);margin-bottom:16px">{sport} Round {rnd} 2026 has been completed. See the updated {sport} ladder for the latest standings after this round's results, and check our current round tips page for this week's matches and analysis.</p>
  <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:16px">
    <a href="{ladder_slug}" class="btn-g">{emoji} View {sport} Ladder 2026 →</a>
    <a href="{current_slug}" style="display:inline-flex;align-items:center;background:var(--muted);color:var(--fg);font-size:13px;font-weight:600;padding:9px 18px;border-radius:10px;text-decoration:none">Current Round Tips →</a>
  </div>
</div>'''
    elif is_current:
        title    = f'{sport} Round {rnd} Tips 2026 — Expert Predictions & Best Bets | PuntGuide'
        desc     = f'{sport} Round {rnd} tips 2026. Expert predictions, best bets, odds comparison and analysis for every match this round. Updated with latest team news.'
        h1       = f'{emoji} {sport} Round {rnd} Tips 2026'
        eyebrow  = f'{sport} 2026 · Round {rnd} · Tips Live'
        body_content = f'''<div class="section">
  <h2>Round {rnd} — Full Tips & Analysis</h2>
  <p style="font-size:15px;line-height:1.8;color:hsl(215 45% 16%/.8);margin-bottom:16px">Our full Round {rnd} tips and analysis page covers every match with detailed analysis, predicted margins, key player matchups, head-to-head records and betting market recommendations.</p>
  <a href="{current_slug}" class="btn-g">{emoji} View Full Round {rnd} Analysis →</a>
</div>'''
    else:
        title    = f'{sport} Round {rnd} Tips 2026 — Predictions & Best Bets | PuntGuide'
        desc     = f'{sport} Round {rnd} tips and predictions 2026. Expert analysis, best bets and top bookmakers — published ahead of every round throughout the 2026 season.'
        h1       = f'{emoji} {sport} Round {rnd} Tips 2026'
        eyebrow  = f'{sport} 2026 · Round {rnd} · Coming Soon'
        body_content = f'''<div class="section">
  <h2>Round {rnd} Tips — Coming Soon</h2>
  <p style="font-size:15px;line-height:1.8;color:hsl(215 45% 16%/.8);margin-bottom:16px">Our {sport} Round {rnd} 2026 tips and match previews will be published ahead of the round. Bookmark this page and check back closer to game time for expert analysis, predicted margins, best bets and our top bookmaker recommendations for every match.</p>
  <p style="font-size:14px;color:var(--muted-fg);margin-bottom:16px">In the meantime, check the current round tips or browse our {sport} futures markets below.</p>
  <div style="display:flex;gap:12px;flex-wrap:wrap">
    <a href="{current_slug}" class="btn-g">{emoji} Current Round Tips →</a>
    <a href="{odds_slug}" style="display:inline-flex;align-items:center;background:var(--muted);color:var(--fg);font-size:13px;font-weight:600;padding:9px 18px;border-radius:10px;text-decoration:none">{odds_label} →</a>
  </div>
</div>'''

    schema_tag, faqs = faq_schema(sport, rnd)
    faq_items = ''.join(f'<div class="faq-item"><button class="faq-q">{q} <span class="fi">+</span></button><div class="faq-a">{a}</div></div>' for q,a in faqs)
    rnd_grid = rounds_grid(sport, total, current, current_slug)

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
{schema_tag}
<style>{CSS}</style>
</head>
<body>
<div class="cb"><span class="cb-t">Bet Responsibly</span><span class="cb-h">Gambling Help: <a href="tel:1800858858">1800 858 858</a> · <a href="https://www.gamblinghelponline.org.au" target="_blank">gamblinghelponline.org.au</a></span><div class="cb-b"><span>18+</span><span>AUS ONLY</span></div></div>
<nav class="nav"><a href="/index.html" class="nav-logo"><img src="/puntguide-logo.png" alt="PuntGuide"></a><ul class="nav-links"><li><a href="{hub_slug}">{sport} Tips</a></li><li><a href="{ladder_slug}">{sport} Ladder</a></li><li><a href="{odds_slug}">{sport} Odds</a></li><li><a href="{best_slug}">{best_label}</a></li><li><a href="/all-betting-sites.html">All Sites</a></li></ul><a href="/all-betting-sites.html" class="btn-g">Bet Now →</a></nav>
<div class="pb">
<div class="hero"><div class="hero-in">
  <div class="bc"><a href="/index.html">Home</a> › <a href="{hub_slug}">{hub_label}</a> › Round {rnd}</div>
  <div class="eye"><span class="eye-l"></span><span class="eye-t">{eyebrow}</span></div>
  <h1>{h1}</h1>
  <p style="font-size:16px;color:hsl(215 45% 16%/.65);max-width:700px;line-height:1.8;margin-top:10px">{desc}</p>
</div></div>
<div class="wrap">
  {body_content}
  <div class="section">
    <h2>All {sport} Rounds 2026</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:4px">Jump to any round for tips, predictions and analysis.</p>
    {rnd_grid}
  </div>
  <div class="section">
    <h2>Best Bookmakers for {sport} Betting</h2>
    <div style="display:flex;flex-direction:column;gap:10px">
      <div style="display:flex;align-items:center;gap:14px;padding:12px;background:var(--muted);border-radius:10px;">
        <img src="/{bm1_logo}" alt="{bm1_name}" style="width:44px;height:44px;border-radius:10px;object-fit:contain;background:#fff;flex-shrink:0;">
        <div style="flex:1"><div style="font-weight:700;margin-bottom:2px">{bm1_name}</div><div style="font-size:13px;color:var(--muted-fg)">{bm1_tag}</div></div>
        <a href="#" onclick="return false;" class="btn-g" style="font-size:12px;padding:7px 13px">Bet Now →</a>
      </div>
      <div style="display:flex;align-items:center;gap:14px;padding:12px;background:var(--muted);border-radius:10px;">
        <img src="/{bm2_logo}" alt="{bm2_name}" style="width:44px;height:44px;border-radius:10px;object-fit:contain;background:#fff;flex-shrink:0;">
        <div style="flex:1"><div style="font-weight:700;margin-bottom:2px">{bm2_name}</div><div style="font-size:13px;color:var(--muted-fg)">{bm2_tag}</div></div>
        <a href="#" onclick="return false;" class="btn-g" style="font-size:12px;padding:7px 13px">Bet Now →</a>
      </div>
    </div>
  </div>
  <div class="int-links"><h3>Related pages</h3>
    <a href="{hub_slug}">{hub_label}</a>
    <a href="{ladder_slug}">{sport} Ladder 2026</a>
    <a href="{odds_slug}">{odds_label}</a>
    <a href="{best_slug}">{best_label}</a>
    <a href="/best-betting-sites-australia.html">Best Betting Sites</a>
    <a href="/compare-betting-sites.html">Compare Betting Sites</a>
    <a href="/all-betting-sites.html">All 130 Bookmakers</a>
  </div>
  <div class="faq"><h2>Frequently asked questions</h2>{faq_items}</div>
</div>
</div>
<footer class="site-footer"><div class="footer-in">
<img src="/puntguide-logo.png" alt="PuntGuide" class="footer-logo">
<p class="footer-desc">Expert {sport} tips and predictions for every round of the 2026 season.</p>
<div class="footer-links">
  <a href="{hub_slug}">{hub_label}</a>
  <a href="{ladder_slug}">{sport} Ladder</a>
  <a href="{odds_slug}">{odds_label}</a>
  <a href="{best_slug}">{best_label}</a>
  <a href="/all-betting-sites.html">All 130 Bookmakers</a>
</div>
<div class="footer-rg">Gamble responsibly. Call <a href="tel:1800858858">Gambling Help 1800 858 858</a> or visit <a href="https://www.gamblinghelponline.org.au" target="_blank">gamblinghelponline.org.au</a>. 18+ only. Tips are editorial predictions only.</div>
</div></footer>
<script>document.querySelectorAll('.faq-q').forEach(b=>b.addEventListener('click',function(){{const a=this.nextElementSibling;a.classList.toggle('open');this.querySelector('.fi').textContent=a.classList.contains('open')?'−':'+';}}));</script>
<script src="/nav-drawer.js"></script>
</body></html>"""

    with open(os.path.join(OUT, slug), 'w') as f:
        f.write(html)
    return slug

if __name__ == '__main__':
    generated = []

    print('\n── AFL Round Stubs ──')
    for r in range(1, AFL_TOTAL + 1):
        result = build_stub('AFL', r, AFL_TOTAL, AFL_CURRENT)
        if result:
            generated.append(result)
            print(f'  ✓ {result}')
        else:
            print(f'  — afl-round-{r}-tips-2026.html (skipped — has content)')

    print('\n── NRL Round Stubs ──')
    for r in range(1, NRL_TOTAL + 1):
        result = build_stub('NRL', r, NRL_TOTAL, NRL_CURRENT)
        if result:
            generated.append(result)
            print(f'  ✓ {result}')
        else:
            print(f'  — nrl-round-{r}-tips-2026.html (skipped — has content)')

    # Update sitemap
    with open(os.path.join(OUT, 'sitemap.xml')) as f:
        sitemap = f.read()
    import re
    existing = set(re.findall(r'<loc>([^<]+)</loc>', sitemap))
    additions = ''
    for slug in generated:
        url = f'{SITE}/{slug}'
        if url not in existing:
            additions += f'  <url><loc>{url}</loc><changefreq>weekly</changefreq><priority>0.7</priority></url>\n'
    if additions:
        sitemap = sitemap.replace('</urlset>', additions + '</urlset>')
        with open(os.path.join(OUT, 'sitemap.xml'), 'w') as f:
            f.write(sitemap)

    print(f'\n✅ {len(generated)} round stubs generated, sitemap updated\n')
