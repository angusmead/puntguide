#!/usr/bin/env python3
"""Update horse-racing-tips-today.html with Saturday 2 May 2026 meets + Morphettville tips."""

with open('horse-racing-tips-today.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. Update hero subtitle and eyebrow ───────────────────────────────────────
html = html.replace(
    '<span class="eye-t">Horse Racing Tips · Australia</span>',
    '<span class="eye-t">Horse Racing Tips · Saturday 2 May 2026</span>'
)

# If eyebrow isn't present, the hero p-tag still needs updating
old_hero_p = 'Expert horse racing tips for today\'s Australian metropolitan and provincial meetings. Best bets, Best Tote analysis, Same Race Multi picks and the top bookmakers for racing in Australia.'
new_hero_p = 'Expert horse racing tips for Saturday 2 May 2026. Morphettville (Adelaide) is the featured Saturday metro meeting today, with the South Australian Derby headline race. Best bets sourced from BestBets.com.au.'
html = html.replace(old_hero_p, new_hero_p)

# ── 2. Replace venues grid section with today's actual meets + tips ───────────
old_venues = '''  <div class="section">
    <h2>Today\'s Major Australian Racing Venues</h2>
    <p style="font-size:14px;color:var(--muted-fg);margin-bottom:14px">Australian racing runs seven days a week. Saturday metro meetings carry the biggest fields and the most betting action.</p>
    <div class="venues-grid">
      <div class="venue-card"><div class="venue-state">NSW</div><div class="venue-name">Randwick</div><div class="venue-type">Metropolitan · Sydney</div></div>
      <div class="venue-card"><div class="venue-state">NSW</div><div class="venue-name">Rosehill</div><div class="venue-type">Metropolitan · Sydney</div></div>
      <div class="venue-card"><div class="venue-state">VIC</div><div class="venue-name">Flemington</div><div class="venue-type">Metropolitan · Melbourne</div></div>
      <div class="venue-card"><div class="venue-state">VIC</div><div class="venue-name">Caulfield</div><div class="venue-type">Metropolitan · Melbourne</div></div>
      <div class="venue-card"><div class="venue-state">VIC</div><div class="venue-name">Moonee Valley</div><div class="venue-type">Metropolitan · Melbourne</div></div>
      <div class="venue-card"><div class="venue-state">QLD</div><div class="venue-name">Eagle Farm</div><div class="venue-type">Metropolitan · Brisbane</div></div>
      <div class="venue-card"><div class="venue-state">QLD</div><div class="venue-name">Doomben</div><div class="venue-type">Metropolitan · Brisbane</div></div>
      <div class="venue-card"><div class="venue-state">SA</div><div class="venue-name">Morphettville</div><div class="venue-type">Metropolitan · Adelaide</div></div>
      <div class="venue-card"><div class="venue-state">WA</div><div class="venue-name">Ascot</div><div class="venue-type">Metropolitan · Perth</div></div>
      <div class="venue-card"><div class="venue-state">WA</div><div class="venue-name">Belmont</div><div class="venue-type">Metropolitan · Perth</div></div>
    </div>
    <p style="font-size:13px;color:var(--muted-fg)">Provincial and country meetings run throughout the week across all states. Check our <a href="/racing-weekend-may2-2026.html" style="color:var(--accent)">racing weekend tips</a> page for this weekend\'s analysis.</p>
  </div>'''

new_venues = '''  <div class="section">
    <h2>Today\'s Meetings — Saturday 2 May 2026</h2>
    <p style="font-size:14px;color:var(--muted-fg);margin-bottom:14px">Saturday metro racing across Australia. Morphettville is today's headline meeting, featuring the South Australian Derby.</p>
    <div class="venues-grid">
      <div class="venue-card" style="border:2px solid var(--primary)"><div class="venue-state">SA ⭐ Featured</div><div class="venue-name">Morphettville</div><div class="venue-type">Metropolitan · Adelaide · SA Derby Day</div></div>
      <div class="venue-card"><div class="venue-state">NSW</div><div class="venue-name">Randwick</div><div class="venue-type">Metropolitan · Sydney</div></div>
      <div class="venue-card"><div class="venue-state">VIC</div><div class="venue-name">Flemington</div><div class="venue-type">Metropolitan · Melbourne</div></div>
      <div class="venue-card"><div class="venue-state">QLD</div><div class="venue-name">Doomben</div><div class="venue-type">Metropolitan · Brisbane</div></div>
      <div class="venue-card"><div class="venue-state">WA</div><div class="venue-name">Ascot</div><div class="venue-type">Metropolitan · Perth</div></div>
    </div>
  </div>

  <div class="section">
    <h2>Today\'s Best Bets — Morphettville, Saturday 2 May 2026</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">Tips sourced from BestBets.com.au for today\'s Morphettville card.</p>

    <div style="display:flex;align-items:center;gap:8px;margin-bottom:14px">
      <span style="background:hsl(215 45% 16%);color:var(--primary);font-size:11px;font-weight:700;padding:3px 9px;border-radius:5px;font-family:\'JetBrains Mono\',monospace;">BEST OF THE DAY</span>
    </div>

    <div style="background:hsl(48 80% 97%);border:2px solid hsl(48 60% 70%);border-radius:12px;padding:18px 22px;margin-bottom:16px;">
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
        <div>
          <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:4px">Race 5 · 14:42 · Bm74</div>
          <div style="font-size:18px;font-weight:800;font-family:\'Geist\',sans-serif;letter-spacing:-0.02em">10. Tropical House</div>
          <div style="font-size:13px;color:var(--muted-fg);margin-top:3px">Winning Edge Presentations Adelaide In Autumn Series Final</div>
          <div style="font-size:12px;color:hsl(140 45% 35%);margin-top:6px;font-weight:600">✓ Tipped by Julie Rowland &amp; Joel Marshall</div>
        </div>
        <div style="display:flex;gap:10px;text-align:center;">
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:10px 16px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Win</div>
            <div style="font-size:22px;font-weight:800;font-family:\'JetBrains Mono\',monospace;color:hsl(215 45% 16%)">$1.90</div>
          </div>
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:10px 16px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Place</div>
            <div style="font-size:22px;font-weight:800;font-family:\'JetBrains Mono\',monospace;color:var(--accent)">$1.20</div>
          </div>
        </div>
      </div>
    </div>

    <div style="display:flex;align-items:center;gap:8px;margin:18px 0 14px">
      <span style="background:hsl(200 88% 50%);color:#fff;font-size:11px;font-weight:700;padding:3px 9px;border-radius:5px;font-family:\'JetBrains Mono\',monospace;">VALUE BETS</span>
    </div>

    <div style="display:flex;flex-direction:column;gap:12px;">

      <div style="background:var(--muted);border-radius:12px;padding:16px 20px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
        <div>
          <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:4px">Race 8 · 16:35 · SA Derby</div>
          <div style="font-size:16px;font-weight:800;font-family:\'Geist\',sans-serif;">3. Kaye Jay</div>
          <div style="font-size:13px;color:var(--muted-fg);margin-top:2px">Thomas Farms South Australian Derby</div>
          <div style="font-size:12px;color:hsl(200 70% 40%);margin-top:4px;font-weight:600">Tipped by Joel Marshall</div>
        </div>
        <div style="display:flex;gap:10px;text-align:center;">
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:8px 14px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Win</div>
            <div style="font-size:20px;font-weight:800;font-family:\'JetBrains Mono\',monospace;color:hsl(215 45% 16%)">$7.50</div>
          </div>
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:8px 14px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Place</div>
            <div style="font-size:20px;font-weight:800;font-family:\'JetBrains Mono\',monospace;color:var(--accent)">$2.40</div>
          </div>
        </div>
      </div>

      <div style="background:var(--muted);border-radius:12px;padding:16px 20px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
        <div>
          <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:4px">Race 9 · 17:10 · Bm76 Sprint</div>
          <div style="font-size:16px;font-weight:800;font-family:\'Geist\',sans-serif;">1. Streetcar Apollo</div>
          <div style="font-size:13px;color:var(--muted-fg);margin-top:2px">Sportsbet Fast Form Festival State Sprint Series Final</div>
          <div style="font-size:12px;color:hsl(200 70% 40%);margin-top:4px;font-weight:600">Tipped by Julie Rowland &amp; Paul Richards</div>
        </div>
        <div style="display:flex;gap:10px;text-align:center;">
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:8px 14px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Win</div>
            <div style="font-size:20px;font-weight:800;font-family:\'JetBrains Mono\',monospace;color:hsl(215 45% 16%)">$8.50</div>
          </div>
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:8px 14px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Place</div>
            <div style="font-size:20px;font-weight:800;font-family:\'JetBrains Mono\',monospace;color:var(--accent)">$2.75</div>
          </div>
        </div>
      </div>

    </div>
    <p style="font-size:11px;color:var(--muted-fg);margin-top:12px">Source: BestBets.com.au · Saturday 2 May 2026 · Tips are editorial predictions only. Always gamble responsibly. 18+</p>
  </div>'''

html = html.replace(old_venues, new_venues)

# ── 3. Update the racing weekend link label ───────────────────────────────────
html = html.replace(
    '<div class="match-link-teams">🏇 Weekend Racing Tips — May 2–3, 2026</div>\n      <div class="match-link-meta">Full weekend metro preview, best bets and value selections</div>',
    '<div class="match-link-teams">🏇 Weekend Racing Tips — May 2–3, 2026</div>\n      <div class="match-link-meta">Morphettville SA Derby Day + Sunday metro tips</div>'
)

# ── 4. Update meta description ────────────────────────────────────────────────
html = html.replace(
    'Horse racing tips today for Australian punters. Expert analysis for today\'s metro and provincial meetings, best bets, Best Tote advice and top bookmakers for racing in Australia.',
    'Horse racing tips today — Saturday 2 May 2026. Morphettville SA Derby Day best bets: Tropical House (R5, $1.90), Kaye Jay (R8 SA Derby, $7.50), Streetcar Apollo (R9, $8.50). Top bookmakers for Australian racing.'
)

with open('horse-racing-tips-today.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done — racing tips page updated for Saturday 2 May 2026")
