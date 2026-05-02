#!/usr/bin/env python3
"""Fix venue cards and add tip sections for all Saturday 2 May 2026 meets."""

with open('horse-racing-tips-today.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. Replace the venues grid + Morphettville tips section with corrected full block ──

old_section = '''  <div class="section">
    <h2>Today\'s Meetings — Saturday 2 May 2026</h2>
    <p style="font-size:14px;color:var(--muted-fg);margin-bottom:14px">Saturday metro racing across Australia. Morphettville is today\'s headline meeting, featuring the South Australian Derby.</p>
    <div class="venues-grid">
      <div class="venue-card" style="border:2px solid var(--primary)"><div class="venue-state">SA ⭐ Featured</div><div class="venue-name">Morphettville</div><div class="venue-type">Metropolitan · Adelaide · SA Derby Day</div></div>
      <div class="venue-card"><div class="venue-state">NSW</div><div class="venue-name">Randwick</div><div class="venue-type">Metropolitan · Sydney</div></div>
      <div class="venue-card"><div class="venue-state">VIC</div><div class="venue-name">Flemington</div><div class="venue-type">Metropolitan · Melbourne</div></div>
      <div class="venue-card"><div class="venue-state">QLD</div><div class="venue-name">Doomben</div><div class="venue-type">Metropolitan · Brisbane</div></div>
      <div class="venue-card"><div class="venue-state">WA</div><div class="venue-name">Ascot</div><div class="venue-type">Metropolitan · Perth</div></div>
    </div>
  </div>'''

new_venues_and_tips = '''  <div class="section">
    <h2>Today\'s Meetings — Saturday 2 May 2026</h2>
    <p style="font-size:14px;color:var(--muted-fg);margin-bottom:14px">Five Saturday meetings across Australia today. Click any venue to jump to its best bets.</p>
    <div class="venues-grid">
      <div class="venue-card" style="border:2px solid var(--primary);cursor:pointer;" onclick="document.getElementById(\'tips-morphettville\').scrollIntoView({behavior:\'smooth\'})">
        <div class="venue-state">SA ⭐</div><div class="venue-name">Morphettville</div>
        <div class="venue-type">Metropolitan · SA Derby Day</div>
        <div style="font-size:11px;color:var(--accent);margin-top:6px;font-weight:600">Tips available ↓</div>
      </div>
      <div class="venue-card" style="cursor:pointer;" onclick="document.getElementById(\'tips-hawkesbury\').scrollIntoView({behavior:\'smooth\'})">
        <div class="venue-state">NSW</div><div class="venue-name">Hawkesbury</div>
        <div class="venue-type">Provincial · Sydney region</div>
        <div style="font-size:11px;color:var(--accent);margin-top:6px;font-weight:600">Tips available ↓</div>
      </div>
      <div class="venue-card" style="cursor:pointer;" onclick="document.getElementById(\'tips-bendigo\').scrollIntoView({behavior:\'smooth\'})">
        <div class="venue-state">VIC</div><div class="venue-name">Bendigo</div>
        <div class="venue-type">Provincial · Central Victoria</div>
        <div style="font-size:11px;color:var(--accent);margin-top:6px;font-weight:600">Tips available ↓</div>
      </div>
      <div class="venue-card" style="cursor:pointer;" onclick="document.getElementById(\'tips-eagle-farm\').scrollIntoView({behavior:\'smooth\'})">
        <div class="venue-state">QLD</div><div class="venue-name">Eagle Farm</div>
        <div class="venue-type">Metropolitan · Brisbane</div>
        <div style="font-size:11px;color:var(--accent);margin-top:6px;font-weight:600">Tips available ↓</div>
      </div>
      <div class="venue-card" style="cursor:pointer;" onclick="document.getElementById(\'tips-ascot\').scrollIntoView({behavior:\'smooth\'})">
        <div class="venue-state">WA</div><div class="venue-name">Ascot</div>
        <div class="venue-type">Metropolitan · Perth</div>
        <div style="font-size:11px;color:var(--accent);margin-top:6px;font-weight:600">Tips available ↓</div>
      </div>
    </div>
  </div>

  <!-- ── MORPHETTVILLE ───────────────────────────────────────────────────── -->
  <div class="section" id="tips-morphettville">
    <h2>Morphettville — Saturday 2 May 2026</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">SA Derby Day at Morphettville. Tips sourced from BestBets.com.au.</p>

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
            <div style="font-size:22px;font-weight:800;font-family:\'JetBrains Mono\',monospace;">$1.90</div>
          </div>
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:10px 16px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Place</div>
            <div style="font-size:22px;font-weight:800;font-family:\'JetBrains Mono\',monospace;color:var(--accent);">$1.20</div>
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
          <div style="font-size:12px;color:hsl(200 70% 40%);margin-top:4px;font-weight:600">Joel Marshall</div>
        </div>
        <div style="display:flex;gap:10px;text-align:center;">
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:8px 14px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Win</div>
            <div style="font-size:20px;font-weight:800;font-family:\'JetBrains Mono\',monospace;">$7.50</div>
          </div>
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:8px 14px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Place</div>
            <div style="font-size:20px;font-weight:800;font-family:\'JetBrains Mono\',monospace;color:var(--accent);">$2.40</div>
          </div>
        </div>
      </div>
      <div style="background:var(--muted);border-radius:12px;padding:16px 20px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
        <div>
          <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:4px">Race 9 · 17:10 · Bm76 Sprint</div>
          <div style="font-size:16px;font-weight:800;font-family:\'Geist\',sans-serif;">1. Streetcar Apollo</div>
          <div style="font-size:13px;color:var(--muted-fg);margin-top:2px">Sportsbet Fast Form Festival State Sprint Series Final</div>
          <div style="font-size:12px;color:hsl(200 70% 40%);margin-top:4px;font-weight:600">Julie Rowland &amp; Paul Richards</div>
        </div>
        <div style="display:flex;gap:10px;text-align:center;">
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:8px 14px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Win</div>
            <div style="font-size:20px;font-weight:800;font-family:\'JetBrains Mono\',monospace;">$8.50</div>
          </div>
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:8px 14px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Place</div>
            <div style="font-size:20px;font-weight:800;font-family:\'JetBrains Mono\',monospace;color:var(--accent);">$2.75</div>
          </div>
        </div>
      </div>
    </div>
    <p style="font-size:11px;color:var(--muted-fg);margin-top:12px">Source: BestBets.com.au · Tips are editorial predictions only. Gamble responsibly. 18+</p>
  </div>

  <!-- ── HAWKESBURY ─────────────────────────────────────────────────────── -->
  <div class="section" id="tips-hawkesbury">
    <h2>Hawkesbury — Saturday 2 May 2026</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">Provincial Saturday meeting at Hawkesbury Racecourse, west of Sydney.</p>
    <div style="background:hsl(205 40% 97%);border:1px dashed var(--border);border-radius:12px;padding:20px;text-align:center;color:var(--muted-fg);">
      <div style="font-size:14px;font-weight:600;margin-bottom:6px;">Tips for Hawkesbury</div>
      <div style="font-size:13px;">Send us the BestBets card for Hawkesbury to add today\'s selections here.</div>
    </div>
    <p style="font-size:11px;color:var(--muted-fg);margin-top:10px">Tips are editorial predictions only. Gamble responsibly. 18+</p>
  </div>

  <!-- ── BENDIGO ─────────────────────────────────────────────────────────── -->
  <div class="section" id="tips-bendigo">
    <h2>Bendigo — Saturday 2 May 2026</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">Provincial Saturday meeting at Bendigo Racecourse, central Victoria.</p>
    <div style="background:hsl(205 40% 97%);border:1px dashed var(--border);border-radius:12px;padding:20px;text-align:center;color:var(--muted-fg);">
      <div style="font-size:14px;font-weight:600;margin-bottom:6px;">Tips for Bendigo</div>
      <div style="font-size:13px;">Send us the BestBets card for Bendigo to add today\'s selections here.</div>
    </div>
    <p style="font-size:11px;color:var(--muted-fg);margin-top:10px">Tips are editorial predictions only. Gamble responsibly. 18+</p>
  </div>

  <!-- ── EAGLE FARM ──────────────────────────────────────────────────────── -->
  <div class="section" id="tips-eagle-farm">
    <h2>Eagle Farm — Saturday 2 May 2026</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">Metropolitan Saturday meeting at Eagle Farm, Brisbane.</p>
    <div style="background:hsl(205 40% 97%);border:1px dashed var(--border);border-radius:12px;padding:20px;text-align:center;color:var(--muted-fg);">
      <div style="font-size:14px;font-weight:600;margin-bottom:6px;">Tips for Eagle Farm</div>
      <div style="font-size:13px;">Send us the BestBets card for Eagle Farm to add today\'s selections here.</div>
    </div>
    <p style="font-size:11px;color:var(--muted-fg);margin-top:10px">Tips are editorial predictions only. Gamble responsibly. 18+</p>
  </div>

  <!-- ── ASCOT ───────────────────────────────────────────────────────────── -->
  <div class="section" id="tips-ascot">
    <h2>Ascot — Saturday 2 May 2026</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">Metropolitan Saturday meeting at Ascot Racecourse, Perth.</p>
    <div style="background:hsl(205 40% 97%);border:1px dashed var(--border);border-radius:12px;padding:20px;text-align:center;color:var(--muted-fg);">
      <div style="font-size:14px;font-weight:600;margin-bottom:6px;">Tips for Ascot</div>
      <div style="font-size:13px;">Send us the BestBets card for Ascot to add today\'s selections here.</div>
    </div>
    <p style="font-size:11px;color:var(--muted-fg);margin-top:10px">Tips are editorial predictions only. Gamble responsibly. 18+</p>
  </div>'''

html = html.replace(old_section, new_venues_and_tips)

with open('horse-racing-tips-today.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done")
