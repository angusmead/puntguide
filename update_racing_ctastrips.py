#!/usr/bin/env python3
"""Insert CTA strips between each race meeting section."""

with open('horse-racing-tips-today.html', 'r', encoding='utf-8') as f:
    html = f.read()

CTA_STRIP = '''
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:0 0 0 0;">
    <a href="/best-betting-sites-australia.html" style="display:flex;align-items:center;justify-content:center;gap:8px;background:hsl(215 45% 16%);color:#fff;border-radius:10px;padding:13px 14px;text-decoration:none;font-size:13px;font-weight:700;font-family:'Geist',sans-serif;" onmouseover="this.style.opacity='.85'" onmouseout="this.style.opacity='1'">🏆 Best Betting Sites →</a>
    <a href="/all-betting-sites.html" style="display:flex;align-items:center;justify-content:center;gap:8px;background:var(--gg);color:hsl(215 45% 16%);border-radius:10px;padding:13px 14px;text-decoration:none;font-size:13px;font-weight:700;font-family:'Geist',sans-serif;box-shadow:var(--sg);" onmouseover="this.style.opacity='.85'" onmouseout="this.style.opacity='1'">📋 All 130+ Bookmakers →</a>
  </div>
'''

# Insert CTA strip between each section by targeting the comment markers
gaps = [
    ('<!-- ── HAWKESBURY', '<!-- ── HAWKESBURY'),
    ('<!-- ── BENDIGO',    '<!-- ── BENDIGO'),
    ('<!-- ── EAGLE FARM', '<!-- ── EAGLE FARM'),
    ('<!-- ── ASCOT',      '<!-- ── ASCOT'),
]

for marker, _ in gaps:
    html = html.replace(f'  {marker}', CTA_STRIP + f'  {marker}', 1)

with open('horse-racing-tips-today.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Done — inserted {len(gaps)} CTA strips between race meeting sections")
