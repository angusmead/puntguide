#!/usr/bin/env python3
"""
Phase 2B quick wins:
1. Add Related Reviews block to all 130 review pages
2. Add internal links to editorial policy + best betting sites on all review pages
"""
import os, re

# Top bookmakers to show as "related" — rotate through so each page gets 4 different ones
TOP_BOOKS = [
    ("Sportsbet",  "review-sportsbet.html"),
    ("BetRight",   "review-betright.html"),
    ("Ladbrokes",  "review-ladbrokes.html"),
    ("TAB",        "review-tab.html"),
    ("Neds",       "review-neds.html"),
    ("PointsBet",  "review-pointsbet.html"),
    ("Palmerbet",  "review-palmerbet.html"),
    ("betr",       "review-betr.html"),
    ("Bet365",     "review-bet365.html"),
    ("Dabble",     "review-dabble.html"),
]

RELATED_BLOCK = """  <div class="int-links" style="margin:28px 0;">
    <h3 style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:hsl(215 20% 42%);margin-bottom:12px;">Related bookmaker reviews</h3>
    {links}
    <a href="/best-betting-sites-australia.html" style="display:inline-block;background:hsl(205 40% 92%);border-radius:6px;padding:5px 11px;margin:3px;font-size:13px;font-weight:500;text-decoration:none;color:hsl(215 45% 16%);">🏆 Best Betting Sites Australia</a>
    <a href="/compare-betting-sites.html" style="display:inline-block;background:hsl(205 40% 92%);border-radius:6px;padding:5px 11px;margin:3px;font-size:13px;font-weight:500;text-decoration:none;color:hsl(215 45% 16%);">Compare Betting Sites</a>
    <a href="/editorial-policy.html" style="display:inline-block;background:hsl(205 40% 92%);border-radius:6px;padding:5px 11px;margin:3px;font-size:13px;font-weight:500;text-decoration:none;color:hsl(215 45% 16%);">How We Review</a>
  </div>"""

pages = sorted([f for f in os.listdir('.') if f.startswith('review-') and f.endswith('.html')])
updated = 0

for i, fn in enumerate(pages):
    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()

    if 'Related bookmaker reviews' in html:
        continue

    # Pick 4 related books — skip self
    related = [b for b in TOP_BOOKS if b[1] != fn][:4]
    link_html = ''.join(
        f'<a href="/{slug}" style="display:inline-block;background:hsl(205 40% 92%);border-radius:6px;padding:5px 11px;margin:3px;font-size:13px;font-weight:500;text-decoration:none;color:hsl(215 45% 16%);">{name} Review</a>'
        for name, slug in related
    )

    block = RELATED_BLOCK.format(links=link_html)

    # Insert before the FAQ section or before </div></div> near footer
    if '<div class="faq">' in html:
        html = html.replace('<div class="faq">', block + '\n  <div class="faq">', 1)
    elif 'class="faq"' in html:
        html = re.sub(r'(<div[^>]+class="faq")', block + r'\n  \1', html, count=1)
    else:
        # Fallback: before site-footer
        html = html.replace('<footer class="site-footer">', block + '\n<footer class="site-footer">', 1)

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(html)
    updated += 1

print(f"Related reviews block added to {updated}/{len(pages)} review pages")
