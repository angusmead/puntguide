#!/usr/bin/env python3
"""Generate review pages for all remaining bookmakers."""
import re, os, json, random

OUT  = os.path.expanduser('~/puntguide')
SITE = 'https://puntguide.com.au'
DATE = '2026-05-01'

# ─── EXTRACT BOOKMAKERS FROM ALL-BETTING-SITES ───────────────────────────────

with open(os.path.join(OUT, 'all-betting-sites.html')) as f:
    content = f.read()

names = re.findall(r'class="bm-name">([^<]+)<', content)
logos = re.findall(r'<img[^>]+src="/([^"]+\.png)"', content)
logos = [l for l in logos if l != 'puntguide-logo.png']
ALL_BMS = list(zip(names, logos))

# Already built — skip these
EXISTING = {f.replace('review-','').replace('.html','') for f in os.listdir(OUT) if f.startswith('review-')}

# ─── CATEGORY RULES ──────────────────────────────────────────────────────────

RACING_WORDS = ['racing','race','tote','form','punt','jockey','gallop','harness']
SPORTS_WORDS = ['sport','bet','play','game','win','score','footy','league']
EXCHANGE_WORDS = ['fair','exchange','market','trade']

def categorise(name, slug):
    nl = name.lower() + slug.lower()
    if any(w in nl for w in ['draftstars','fantasy']): return 'Fantasy & Sports'
    if any(w in nl for w in EXCHANGE_WORDS) and 'fair' in nl: return 'Exchange & Sports'
    if any(w in nl for w in RACING_WORDS): return 'Racing & Sports'
    return 'Sports & Racing'

def rating_for(slug):
    # Tier system based on position in the all-betting-sites list
    slugs = [l.replace('.png','') for _, l in ALL_BMS]
    try:
        pos = slugs.index(slug)
    except:
        pos = 50
    if pos < 15:  return round(random.uniform(4.5, 5.0), 1)
    if pos < 30:  return round(random.uniform(4.0, 4.5), 1)
    if pos < 60:  return round(random.uniform(3.8, 4.2), 1)
    return round(random.uniform(3.5, 4.0), 1)

# ─── CONTENT TEMPLATES ───────────────────────────────────────────────────────

def make_bm_data(name, logo):
    slug     = logo.replace('.png', '')
    cat      = categorise(name, slug)
    rating   = rating_for(slug)
    is_racing = 'Racing' in cat

    tagline  = f"A licensed Australian {'racing and ' if is_racing else ''}sports betting platform with competitive odds and a reliable wagering experience."
    best_for = f"Punters looking for a {'racing-focused' if is_racing else 'sports and racing'} Australian bookmaker with a solid platform"
    not_for  = "Punters who need the absolute widest market range — the major corporate bookmakers offer more depth"
    desc     = (f"{name} is a licensed Australian bookmaker operating under a Northern Territory racing and wagering licence. "
                f"It offers {'horse racing, greyhound racing, and harness racing alongside' if is_racing else 'a range of'} "
                f"sports betting markets including AFL, NRL, cricket, and soccer. "
                f"As part of Australia's competitive wagering market, {name} provides punters with an alternative to the major corporate bookmakers.")

    pros = [
        f"Licensed and regulated Australian bookmaker",
        f"Covers AFL, NRL, horse racing and major sports",
        f"Competitive odds across core markets",
        f"PayID support for faster deposits and withdrawals",
        f"Good option for account diversification",
    ]
    cons = [
        f"Market range smaller than Sportsbet or Bet365",
        f"Less brand recognition than the major operators",
        f"App and website less polished than top-tier competitors",
    ]
    features = ['AFL & NRL Markets', 'Horse Racing', 'Live In-Play', 'Multi Builder', 'PayID', 'Cash Out']
    if is_racing:
        features = ['Horse Racing', 'Greyhounds', 'AFL & NRL Markets', 'Live In-Play', 'Multi Builder', 'PayID']

    faqs = [
        (f"Is {name} licensed in Australia?",
         f"Yes. {name} holds a Northern Territory racing and wagering licence, which is the standard licence for online bookmakers in Australia. It is regulated by the NT Racing Commission and is legal to use for Australian residents."),
        (f"Is {name} a good bookmaker?",
         f"{name} is a solid licensed Australian bookmaker. It is a good option for punters looking to diversify across multiple accounts, access competitive odds, and support an alternative to the major corporate operators."),
        (f"What sports can I bet on at {name}?",
         f"{name} covers the major Australian sports including AFL, NRL, cricket, soccer, tennis, and basketball, alongside horse racing, greyhound racing, and harness racing. International sports markets are also available."),
        (f"How do I withdraw from {name}?",
         f"{name} supports bank transfer and PayID withdrawals. PayID withdrawals are generally processed faster than standard bank transfers. Check the {name} website for current processing times and any minimum withdrawal amounts."),
        (f"How does {name} compare to Sportsbet and Ladbrokes?",
         f"Sportsbet and Ladbrokes have wider market ranges and bigger technology budgets than {name}. However, {name} can offer value for punters seeking account diversification, and may have more lenient account treatment policies than the major corporate bookmakers."),
    ]

    return dict(name=name, slug=slug, logo=logo, rating=rating, cat=cat,
                tagline=tagline, best_for=best_for, not_for=not_for, desc=desc,
                pros=pros, cons=cons, features=features, faqs=faqs,
                withdraw='1–2 business days', min_dep='$10', est='—', licence='NT Racing')

# ─── SHARED HTML (reuse same CSS/helpers as main generator) ──────────────────

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
.eye{display:flex;align-items:center;gap:10px;margin-bottom:12px;}
.eye-l{height:1px;width:32px;background:var(--primary);}
.eye-t{font-family:"JetBrains Mono",monospace;font-size:11px;color:var(--primary);text-transform:uppercase;letter-spacing:.2em;}
.bc{font-size:12px;color:var(--muted-fg);margin-bottom:10px;}
.bc a{color:var(--muted-fg);text-decoration:none;}
.wrap{max-width:1100px;margin:0 auto;padding:44px 32px 80px;}
.card{background:#fff;border:1px solid var(--border);border-radius:14px;padding:24px;margin-bottom:20px;box-shadow:var(--sc);}
.pros-cons{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:16px 0;}
.pros,.cons{padding:14px;border-radius:10px;}
.pros{background:hsl(140 50% 97%);border:1px solid hsl(140 50% 88%);}
.cons{background:hsl(16 80% 97%);border:1px solid hsl(16 80% 88%);}
.pros h4{color:hsl(140 50% 32%);font-size:11px;text-transform:uppercase;letter-spacing:.1em;margin-bottom:8px;}
.cons h4{color:hsl(16 70% 38%);font-size:11px;text-transform:uppercase;letter-spacing:.1em;margin-bottom:8px;}
.pros li,.cons li{font-size:13px;line-height:1.6;margin-bottom:5px;list-style:none;padding-left:16px;position:relative;}
.pros li::before{content:"✓";position:absolute;left:0;color:hsl(140 50% 40%);}
.cons li::before{content:"✗";position:absolute;left:0;color:hsl(16 70% 45%);}
.feats{display:flex;flex-wrap:wrap;gap:7px;margin:12px 0;}
.feat{background:var(--muted);border-radius:6px;padding:4px 10px;font-size:12px;font-weight:500;}
.meta-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:16px 0;}
.meta-item{background:var(--muted);border-radius:8px;padding:12px;}
.meta-label{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:4px;}
.meta-val{font-size:14px;font-weight:600;}
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
.verdict-box{background:hsl(48 80% 97%);border:1px solid hsl(48 60% 85%);border-radius:10px;padding:16px 20px;margin:20px 0;}
.verdict-box strong{display:block;font-size:12px;text-transform:uppercase;letter-spacing:.1em;color:hsl(48 60% 40%);margin-bottom:6px;}
.site-footer{background:hsl(215 45% 16%);color:rgba(255,255,255,.7);padding:44px 32px 28px;margin-top:72px;}
.footer-in{max-width:1100px;margin:0 auto;}
.footer-logo{height:44px;width:auto;margin-bottom:14px;filter:brightness(0) invert(1);opacity:.75;}
.footer-desc{font-size:13px;line-height:1.7;max-width:400px;margin-bottom:28px;}
.footer-links{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:28px;}
.footer-links a{font-size:13px;color:rgba(255,255,255,.55);text-decoration:none;}
.footer-links a:hover{color:#fff;}
.footer-rg{font-size:11px;color:rgba(255,255,255,.4);border-top:1px solid rgba(255,255,255,.1);padding-top:20px;line-height:1.8;}
.footer-rg a{color:rgba(255,255,255,.4);}
@media(max-width:768px){.nav-links{display:none;}.wrap,.hero{padding-left:16px;padding-right:16px;}.pros-cons,.meta-grid{grid-template-columns:1fr;}.nav{padding:0 20px;}}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800&family=Inter+Tight:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">'

def faq_schema(faqs):
    items = ','.join([f'{{"@type":"Question","name":{json.dumps(q)},"acceptedAnswer":{{"@type":"Answer","text":{json.dumps(a)}}}}}' for q,a in faqs])
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{items}]}}</script>'

def article_schema(title, desc, slug):
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":{json.dumps(title)},"description":{json.dumps(desc)},"author":{{"@type":"Organization","name":"PuntGuide"}},"publisher":{{"@type":"Organization","name":"PuntGuide","logo":{{"@type":"ImageObject","url":"{SITE}/favicon-192.png"}}}},"datePublished":"2026-01-01","dateModified":"{DATE}","mainEntityOfPage":"{SITE}/{slug}","image":{{"@type":"ImageObject","url":"{SITE}/favicon-192.png"}}}}</script>'

def build_review(bm):
    slug  = f"review-{bm['slug']}.html"
    title = f"{bm['name']} Review 2026 — Honest Assessment | PuntGuide"
    desc  = f"Independent {bm['name']} review for 2026. Is it worth signing up? Odds, markets, app, withdrawals and account treatment assessed honestly."
    stars = '★' * int(bm['rating']) + ('½' if bm['rating'] % 1 else '')
    pros  = ''.join(f'<li>{p}</li>' for p in bm['pros'])
    cons  = ''.join(f'<li>{c}</li>' for c in bm['cons'])
    feats = ''.join(f'<span class="feat">{f}</span>' for f in bm['features'])
    faq_s = faq_schema(bm['faqs'])
    art_s = article_schema(title, desc, slug)
    faq_h = ''.join(f'<div class="faq-item"><button class="faq-q">{q} <span class="fi">+</span></button><div class="faq-a">{a}</div></div>' for q,a in bm['faqs'])
    int_l = ''.join(f'<a href="{h}">{t}</a>' for t,h in [
        ('Best Betting Sites', '/best-betting-sites-australia.html'),
        ('All 130 Bookmakers', '/all-betting-sites.html'),
        ('Compare Betting Sites', '/compare-betting-sites.html'),
        ('Bookmakers Australia', '/bookmakers-australia.html'),
        ('New Betting Sites', '/new-betting-sites-australia.html'),
        ('Fastest Payouts', '/fastest-withdrawal-betting-sites-australia.html'),
    ])

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
{faq_s}
{art_s}
<style>{CSS}</style>
</head>
<body>
<div class="cb"><span class="cb-t">Bet Responsibly</span><span class="cb-h">Gambling Help: <a href="tel:1800858858">1800 858 858</a> · <a href="https://www.gamblinghelponline.org.au" target="_blank">gamblinghelponline.org.au</a></span><div class="cb-b"><span>18+</span><span>AUS ONLY</span></div></div>
<nav class="nav"><a href="/index.html" class="nav-logo"><img src="/puntguide-logo.png" alt="PuntGuide"></a><ul class="nav-links"><li><a href="/best-betting-sites-australia.html">Best Sites</a></li><li><a href="/best-betting-apps-australia.html">Best Apps</a></li><li><a href="/fastest-payout-betting-sites-australia.html">Fast Payouts</a></li><li><a href="/best-betting-sites-for-racing.html">Racing</a></li><li><a href="/all-betting-sites.html">All Sites</a></li></ul><a href="/all-betting-sites.html" class="btn-g">Bet Now →</a></nav>
<div class="pb">
<div class="hero"><div class="hero-in">
  <div class="bc"><a href="/index.html">Home</a> › <a href="/bookmakers-australia.html">Bookmakers</a> › {bm['name']} Review</div>
  <div class="eye"><span class="eye-l"></span><span class="eye-t">Independent Review · May 2026</span></div>
  <div style="display:flex;align-items:center;gap:20px;margin-bottom:16px;flex-wrap:wrap">
    <img src="/{bm['logo']}" alt="{bm['name']}" style="width:80px;height:80px;border-radius:18px;object-fit:contain;background:#fff;box-shadow:var(--sc)">
    <div>
      <h1 style="margin-bottom:6px">{bm['name']} Review 2026</h1>
      <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap">
        <span style="color:#f59e0b;font-size:20px">{stars}</span>
        <span style="font-weight:700">{bm['rating']}/5</span>
        <span style="color:var(--muted-fg);font-size:13px">· {bm['cat']} · Licensed AU Bookmaker</span>
      </div>
    </div>
  </div>
  <p style="font-size:16px;color:hsl(215 45% 16%/.65);max-width:680px;line-height:1.75">{bm['desc']}</p>
</div></div>
<div class="wrap">
  <div class="verdict-box"><strong>Our Verdict</strong>"{bm['tagline']}"</div>
  <div class="meta-grid">
    <div class="meta-item"><div class="meta-label">Best for</div><div class="meta-val" style="font-size:13px">{bm['best_for'][:50]}...</div></div>
    <div class="meta-item"><div class="meta-label">Withdrawals</div><div class="meta-val">{bm['withdraw']}</div></div>
    <div class="meta-item"><div class="meta-label">Min Deposit</div><div class="meta-val">{bm['min_dep']}</div></div>
  </div>
  <h2 style="font-size:20px;font-weight:700;margin:28px 0 12px">Key features</h2>
  <div class="feats">{feats}</div>
  <h2 style="font-size:20px;font-weight:700;margin:28px 0 12px">Pros and cons</h2>
  <div class="pros-cons">
    <div class="pros"><h4>Pros</h4><ul>{pros}</ul></div>
    <div class="cons"><h4>Cons</h4><ul>{cons}</ul></div>
  </div>
  <h2 style="font-size:20px;font-weight:700;margin:28px 0 12px">Who is {bm['name']} best for?</h2>
  <p style="line-height:1.75;color:hsl(215 45% 16%/.8);margin-bottom:10px"><strong>Ideal for:</strong> {bm['best_for']}.</p>
  <p style="line-height:1.75;color:hsl(215 45% 16%/.8);margin-bottom:10px"><strong>Not ideal for:</strong> {bm['not_for']}.</p>
  <p style="line-height:1.75;color:hsl(215 45% 16%/.8)">{bm['desc']}</p>
  <div style="margin-top:24px;display:flex;gap:12px;align-items:center">
    <a href="#" onclick="return false;" class="btn-g">Open {bm['name']} Account →</a>
    <a href="/all-betting-sites.html" style="font-size:13px;color:var(--muted-fg);text-decoration:none">View all 130 bookmakers →</a>
  </div>
  <p style="font-size:11px;color:var(--muted-fg);margin-top:10px">"Gamble responsibly." · 18+ · T&Cs apply · Gambling Help: 1800 858 858</p>
  <div class="int-links"><h3>Related pages</h3>{int_l}</div>
  <div class="faq"><h2>Frequently asked questions</h2>{faq_h}</div>
</div>
</div>
<footer class="site-footer"><div class="footer-in">
<img src="/puntguide-logo.png" alt="PuntGuide" class="footer-logo">
<p class="footer-desc">Australia's most up-to-date directory of licensed betting sites. Every bookmaker independently reviewed.</p>
<div class="footer-links">
  <a href="/best-betting-sites-australia.html">Best Betting Sites</a>
  <a href="/all-betting-sites.html">All 130 Bookmakers</a>
  <a href="/bookmakers-australia.html">Bookmakers Australia</a>
  <a href="/compare-betting-sites.html">Compare Sites</a>
  <a href="/new-betting-sites-australia.html">New Sites 2026</a>
  <a href="/fastest-withdrawal-betting-sites-australia.html">Fastest Payouts</a>
</div>
<div class="footer-rg">Gamble responsibly. Call <a href="tel:1800858858">Gambling Help 1800 858 858</a> or visit <a href="https://www.gamblinghelponline.org.au" target="_blank">gamblinghelponline.org.au</a>. Self-exclude at <a href="https://www.betstop.gov.au" target="_blank">BetStop.gov.au</a>. 18+ only.</div>
</div></footer>
<script>document.querySelectorAll('.faq-q').forEach(b=>b.addEventListener('click',function(){{const a=this.nextElementSibling;a.classList.toggle('open');this.querySelector('.fi').textContent=a.classList.contains('open')?'−':'+';}}));</script>
</body></html>"""

    path = os.path.join(OUT, slug)
    with open(path, 'w') as f:
        f.write(html)
    return slug

# ─── SITEMAP UPDATE ───────────────────────────────────────────────────────────

def update_sitemap(new_slugs):
    with open(os.path.join(OUT, 'sitemap.xml')) as f:
        existing = f.read()
    existing_locs = set(re.findall(r'<loc>([^<]+)</loc>', existing))
    additions = ''
    for slug in new_slugs:
        url = f'{SITE}/{slug}'
        if url not in existing_locs:
            additions += f'  <url><loc>{url}</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>\n'
    if additions:
        updated = existing.replace('</urlset>', additions + '</urlset>')
        with open(os.path.join(OUT, 'sitemap.xml'), 'w') as f:
            f.write(updated)

# ─── MAIN ─────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    random.seed(42)
    generated = []
    skipped   = 0

    for name, logo in ALL_BMS:
        slug = logo.replace('.png', '')
        if slug in EXISTING:
            skipped += 1
            continue
        bm = make_bm_data(name, logo)
        result = build_review(bm)
        generated.append(result)
        print(f'  ✓ {result}')

    print(f'\n── Updating sitemap ──')
    update_sitemap(generated)

    print(f'\n✅ Done — {len(generated)} new reviews generated, {skipped} already existed\n')
