#!/usr/bin/env python3
"""Add upward link to best-betting-sites-australia.html on the 3 pages missing it."""
import re

LINK_BLOCK = '''  <div class="int-links" style="margin:28px 0;">
    <h3 style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:hsl(215 20% 42%);margin-bottom:12px;">Related pages</h3>
    <a href="/best-betting-sites-australia.html" style="display:inline-block;background:hsl(205 40% 92%);border-radius:6px;padding:5px 11px;margin:3px;font-size:13px;font-weight:500;text-decoration:none;color:hsl(215 45% 16%);">🏆 Best Betting Sites Australia</a>
    <a href="/all-betting-sites.html" style="display:inline-block;background:hsl(205 40% 92%);border-radius:6px;padding:5px 11px;margin:3px;font-size:13px;font-weight:500;text-decoration:none;color:hsl(215 45% 16%);">All 130+ Bookmakers</a>
    <a href="/best-betting-sites-for-racing.html" style="display:inline-block;background:hsl(205 40% 92%);border-radius:6px;padding:5px 11px;margin:3px;font-size:13px;font-weight:500;text-decoration:none;color:hsl(215 45% 16%);">Best for Racing</a>
  </div>'''

LINK_BLOCK_AFL = '''  <div class="int-links" style="margin:28px 0;">
    <h3 style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:hsl(215 20% 42%);margin-bottom:12px;">Related pages</h3>
    <a href="/best-betting-sites-australia.html" style="display:inline-block;background:hsl(205 40% 92%);border-radius:6px;padding:5px 11px;margin:3px;font-size:13px;font-weight:500;text-decoration:none;color:hsl(215 45% 16%);">🏆 Best Betting Sites Australia</a>
    <a href="/all-betting-sites.html" style="display:inline-block;background:hsl(205 40% 92%);border-radius:6px;padding:5px 11px;margin:3px;font-size:13px;font-weight:500;text-decoration:none;color:hsl(215 45% 16%);">All 130+ Bookmakers</a>
    <a href="/best-betting-sites-for-afl.html" style="display:inline-block;background:hsl(205 40% 92%);border-radius:6px;padding:5px 11px;margin:3px;font-size:13px;font-weight:500;text-decoration:none;color:hsl(215 45% 16%);">Best for AFL</a>
  </div>'''

LINK_BLOCK_NRL = '''  <div class="int-links" style="margin:28px 0;">
    <h3 style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:hsl(215 20% 42%);margin-bottom:12px;">Related pages</h3>
    <a href="/best-betting-sites-australia.html" style="display:inline-block;background:hsl(205 40% 92%);border-radius:6px;padding:5px 11px;margin:3px;font-size:13px;font-weight:500;text-decoration:none;color:hsl(215 45% 16%);">🏆 Best Betting Sites Australia</a>
    <a href="/all-betting-sites.html" style="display:inline-block;background:hsl(205 40% 92%);border-radius:6px;padding:5px 11px;margin:3px;font-size:13px;font-weight:500;text-decoration:none;color:hsl(215 45% 16%);">All 130+ Bookmakers</a>
    <a href="/best-betting-sites-for-nrl.html" style="display:inline-block;background:hsl(205 40% 92%);border-radius:6px;padding:5px 11px;margin:3px;font-size:13px;font-weight:500;text-decoration:none;color:hsl(215 45% 16%);">Best for NRL</a>
  </div>'''

fixes = [
    ('afl-round-8-tips-2026.html',  LINK_BLOCK_AFL),
    ('nrl-round-10-tips-2026.html', LINK_BLOCK_NRL),
    ('racing-futures-2026.html',    LINK_BLOCK),
]

for fn, block in fixes:
    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()
    # Insert before footer (handles both footer class variants)
    for footer_tag in ['<footer class="site-footer">', '<footer class="pg">']:
        if footer_tag in html:
            html = html.replace(footer_tag, block + '\n' + footer_tag, 1)
            break
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Fixed: {fn}")

print("Done.")
