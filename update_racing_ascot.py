#!/usr/bin/env python3
"""Fill in Ascot tips from BestBets for Saturday 2 May 2026."""

with open('horse-racing-tips-today.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_ascot = '''  <!-- ── ASCOT ───────────────────────────────────────────────────────────── -->
  <div class="section" id="tips-ascot">
    <h2>Ascot — Saturday 2 May 2026</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">Metropolitan Saturday meeting at Ascot Racecourse, Perth.</p>
    <div style="background:hsl(205 40% 97%);border:1px dashed var(--border);border-radius:12px;padding:20px;text-align:center;color:var(--muted-fg);">
      <div style="font-size:14px;font-weight:600;margin-bottom:6px;">Tips for Ascot</div>
      <div style="font-size:13px;">Send us the BestBets card for Ascot to add today\'s selections here.</div>
    </div>
    <p style="font-size:11px;color:var(--muted-fg);margin-top:10px">Tips are editorial predictions only. Gamble responsibly. 18+</p>
  </div>'''

new_ascot = '''  <!-- ── ASCOT ───────────────────────────────────────────────────────────── -->
  <div class="section" id="tips-ascot">
    <h2>Ascot — Saturday 2 May 2026</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">Metropolitan Saturday meeting at Ascot Racecourse, Perth. Tips sourced from BestBets.com.au.</p>

    <div style="display:flex;align-items:center;gap:8px;margin-bottom:14px">
      <span style="background:hsl(215 45% 16%);color:var(--primary);font-size:11px;font-weight:700;padding:3px 9px;border-radius:5px;font-family:\'JetBrains Mono\',monospace;">BEST OF THE DAY</span>
    </div>

    <div style="display:flex;flex-direction:column;gap:12px;margin-bottom:18px;">
      <div style="background:hsl(48 80% 97%);border:2px solid hsl(48 60% 70%);border-radius:12px;padding:16px 20px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
        <div>
          <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:4px">Race 4 · 15:29 · Bm72+</div>
          <div style="font-size:18px;font-weight:800;font-family:\'Geist\',sans-serif;letter-spacing:-0.02em">4. Rock \'N\' The Jam</div>
          <div style="font-size:13px;color:var(--muted-fg);margin-top:3px">Pearce Racing Ladies Day</div>
          <div style="font-size:12px;color:hsl(140 45% 35%);margin-top:6px;font-weight:600">✓ Tipped by Greg Hooper &amp; Joel Marshall</div>
        </div>
        <div style="display:flex;gap:10px;text-align:center;">
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:10px 16px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Win</div>
            <div style="font-size:22px;font-weight:800;font-family:\'JetBrains Mono\',monospace;">$2.10</div>
          </div>
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:10px 16px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Place</div>
            <div style="font-size:22px;font-weight:800;font-family:\'JetBrains Mono\',monospace;color:var(--accent);">$1.30</div>
          </div>
        </div>
      </div>

      <div style="background:hsl(48 80% 97%);border:2px solid hsl(48 60% 70%);border-radius:12px;padding:16px 20px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
        <div>
          <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:4px">Race 8 · 18:10 · WA Sires\' Produce Stakes</div>
          <div style="font-size:18px;font-weight:800;font-family:\'Geist\',sans-serif;letter-spacing:-0.02em">2. Beatty</div>
          <div style="font-size:13px;color:var(--muted-fg);margin-top:3px">W.A. Sires\' Produce Stakes</div>
          <div style="font-size:12px;color:hsl(140 45% 35%);margin-top:6px;font-weight:600">✓ Tipped by Paul Kelly</div>
        </div>
        <div style="display:flex;gap:10px;text-align:center;">
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:10px 16px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Win</div>
            <div style="font-size:22px;font-weight:800;font-family:\'JetBrains Mono\',monospace;">$1.65</div>
          </div>
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:10px 16px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Place</div>
            <div style="font-size:22px;font-weight:800;font-family:\'JetBrains Mono\',monospace;color:var(--accent);">$1.06</div>
          </div>
        </div>
      </div>
    </div>

    <div style="display:flex;align-items:center;gap:8px;margin-bottom:14px">
      <span style="background:hsl(200 88% 50%);color:#fff;font-size:11px;font-weight:700;padding:3px 9px;border-radius:5px;font-family:\'JetBrains Mono\',monospace;">VALUE BETS</span>
    </div>

    <div style="display:flex;flex-direction:column;gap:12px;">
      <div style="background:var(--muted);border-radius:12px;padding:14px 18px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
        <div>
          <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:3px">Race 3 · 14:54</div>
          <div style="font-size:15px;font-weight:800;font-family:\'Geist\',sans-serif;">6. Moonwalk</div>
          <div style="font-size:12px;color:var(--muted-fg);margin-top:2px">Liquor Barons (Rs0ly)</div>
          <div style="font-size:12px;color:hsl(200 70% 40%);margin-top:3px;font-weight:600">Greg Hooper</div>
        </div>
        <div style="display:flex;gap:8px;text-align:center;">
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:8px 12px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Win</div>
            <div style="font-size:18px;font-weight:800;font-family:\'JetBrains Mono\',monospace;">$2.35</div>
          </div>
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:8px 12px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Place</div>
            <div style="font-size:18px;font-weight:800;font-family:\'JetBrains Mono\',monospace;color:var(--accent);">$1.20</div>
          </div>
        </div>
      </div>

      <div style="background:var(--muted);border-radius:12px;padding:14px 18px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
        <div>
          <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:3px">Race 7 · 17:35</div>
          <div style="font-size:15px;font-weight:800;font-family:\'Geist\',sans-serif;">2. Crunchy Nut</div>
          <div style="font-size:12px;color:var(--muted-fg);margin-top:2px">Mc Polytrack (Rs1mw)</div>
          <div style="font-size:12px;color:hsl(200 70% 40%);margin-top:3px;font-weight:600">Paul Kelly</div>
        </div>
        <div style="display:flex;gap:8px;text-align:center;">
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:8px 12px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Win</div>
            <div style="font-size:18px;font-weight:800;font-family:\'JetBrains Mono\',monospace;">$6.50</div>
          </div>
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:8px 12px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Place</div>
            <div style="font-size:18px;font-weight:800;font-family:\'JetBrains Mono\',monospace;color:var(--accent);">$2.15</div>
          </div>
        </div>
      </div>

      <div style="background:var(--muted);border-radius:12px;padding:14px 18px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
        <div>
          <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:3px">Race 9 · 18:45 · Bm66+</div>
          <div style="font-size:15px;font-weight:800;font-family:\'Geist\',sans-serif;">8. Auto Cruise</div>
          <div style="font-size:12px;color:var(--muted-fg);margin-top:2px">City of Belmont</div>
          <div style="font-size:12px;color:hsl(200 70% 40%);margin-top:3px;font-weight:600">Joel Marshall</div>
        </div>
        <div style="display:flex;gap:8px;text-align:center;">
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:8px 12px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Win</div>
            <div style="font-size:18px;font-weight:800;font-family:\'JetBrains Mono\',monospace;">$3.00</div>
          </div>
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:8px 12px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Place</div>
            <div style="font-size:18px;font-weight:800;font-family:\'JetBrains Mono\',monospace;color:var(--accent);">$1.30</div>
          </div>
        </div>
      </div>
    </div>
    <p style="font-size:11px;color:var(--muted-fg);margin-top:12px">Source: BestBets.com.au · Tips are editorial predictions only. Gamble responsibly. 18+</p>
  </div>'''

html = html.replace(old_ascot, new_ascot)

with open('horse-racing-tips-today.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done — Ascot tips added")
