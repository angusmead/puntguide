#!/usr/bin/env python3
"""Fill in Eagle Farm tips from BestBets — Saturday 2 May 2026."""

with open('horse-racing-tips-today.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_eagle = '''  <!-- ── EAGLE FARM ──────────────────────────────────────────────────────── -->
  <div class="section" id="tips-eagle-farm">
    <h2>Eagle Farm — Saturday 2 May 2026</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">Metropolitan Saturday meeting at Eagle Farm, Brisbane.</p>
    <div style="background:hsl(205 40% 97%);border:1px dashed var(--border);border-radius:12px;padding:20px;text-align:center;color:var(--muted-fg);">
      <div style="font-size:14px;font-weight:600;margin-bottom:6px;">Tips for Eagle Farm</div>
      <div style="font-size:13px;">Send us the BestBets card for Eagle Farm to add today\'s selections here.</div>
    </div>
    <p style="font-size:11px;color:var(--muted-fg);margin-top:10px">Tips are editorial predictions only. Gamble responsibly. 18+</p>
  </div>'''

new_eagle = '''  <!-- ── EAGLE FARM ──────────────────────────────────────────────────────── -->
  <div class="section" id="tips-eagle-farm">
    <h2>Eagle Farm — Saturday 2 May 2026</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">Metropolitan Saturday meeting at Eagle Farm, Brisbane. Features the Magic Millions and Ladbrokes Victory Stakes. Tips sourced from BestBets.com.au.</p>

    <div style="display:flex;align-items:center;gap:8px;margin:0 0 14px">
      <span style="background:hsl(215 45% 16%);color:var(--primary);font-size:11px;font-weight:700;padding:3px 9px;border-radius:5px;font-family:\'JetBrains Mono\',monospace;">BEST OF THE DAY</span>
    </div>

    <div style="display:flex;flex-direction:column;gap:12px;margin-bottom:18px;">

      <div style="background:hsl(48 80% 97%);border:2px solid hsl(48 60% 70%);border-radius:12px;padding:16px 20px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
        <div>
          <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:4px">Race 4 · Magic Millions · Bm90</div>
          <div style="font-size:18px;font-weight:800;font-family:\'Geist\',sans-serif;letter-spacing:-0.02em">8. Jenni Moreese</div>
          <div style="font-size:13px;color:var(--muted-fg);margin-top:3px">Magic Millions (Bm90)</div>
          <div style="font-size:12px;color:hsl(140 45% 35%);margin-top:6px;font-weight:600">✓ Scott McDonell</div>
        </div>
        <div style="display:flex;gap:10px;text-align:center;">
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:10px 16px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Win</div>
            <div style="font-size:22px;font-weight:800;font-family:\'JetBrains Mono\',monospace;">$3.30</div>
          </div>
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:10px 16px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Place</div>
            <div style="font-size:22px;font-weight:800;font-family:\'JetBrains Mono\',monospace;color:var(--accent);">$1.40</div>
          </div>
        </div>
      </div>

      <div style="background:hsl(48 80% 97%);border:2px solid hsl(48 60% 70%);border-radius:12px;padding:16px 20px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
        <div>
          <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:4px">Race 4 · Magic Millions · Bm90</div>
          <div style="font-size:18px;font-weight:800;font-family:\'Geist\',sans-serif;letter-spacing:-0.02em">11. Cavalry Man</div>
          <div style="font-size:13px;color:var(--muted-fg);margin-top:3px">Magic Millions (Bm90)</div>
          <div style="font-size:12px;color:hsl(140 45% 35%);margin-top:6px;font-weight:600">✓ Joel Marshall</div>
        </div>
        <div style="display:flex;gap:10px;text-align:center;">
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:10px 16px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Win</div>
            <div style="font-size:22px;font-weight:800;font-family:\'JetBrains Mono\',monospace;">$5.00</div>
          </div>
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:10px 16px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Place</div>
            <div style="font-size:22px;font-weight:800;font-family:\'JetBrains Mono\',monospace;color:var(--accent);">$1.75</div>
          </div>
        </div>
      </div>

      <div style="background:hsl(140 40% 96%);border:2px solid hsl(140 50% 40%);border-radius:12px;padding:16px 20px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
        <div>
          <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:hsl(140 50% 35%);margin-bottom:4px">Race 1 · RESULTED ✓ 1ST</div>
          <div style="font-size:18px;font-weight:800;font-family:\'Geist\',sans-serif;letter-spacing:-0.02em">3. Mercurial Lady</div>
          <div style="font-size:13px;color:var(--muted-fg);margin-top:3px">R1 — Won at $6.00</div>
          <div style="font-size:12px;color:hsl(140 45% 35%);margin-top:6px;font-weight:700">🏆 Winner — Adam Williams</div>
        </div>
        <div style="display:flex;gap:10px;text-align:center;">
          <div style="background:#fff;border:1px solid hsl(140 50% 60%);border-radius:8px;padding:10px 16px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Win</div>
            <div style="font-size:22px;font-weight:800;font-family:\'JetBrains Mono\',monospace;color:hsl(140 50% 35%);">$6.00</div>
          </div>
          <div style="background:#fff;border:1px solid hsl(140 50% 60%);border-radius:8px;padding:10px 16px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Place</div>
            <div style="font-size:22px;font-weight:800;font-family:\'JetBrains Mono\',monospace;color:hsl(140 50% 35%);">$2.15</div>
          </div>
        </div>
      </div>

    </div>

    <div style="display:flex;align-items:center;gap:8px;margin:18px 0 14px">
      <span style="background:hsl(200 88% 50%);color:#fff;font-size:11px;font-weight:700;padding:3px 9px;border-radius:5px;font-family:\'JetBrains Mono\',monospace;">VALUE BETS</span>
    </div>

    <div style="display:flex;flex-direction:column;gap:12px;">

      <div style="background:var(--muted);border-radius:12px;padding:14px 18px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
        <div>
          <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:3px">Race 5 · 14:23</div>
          <div style="font-size:15px;font-weight:800;font-family:\'Geist\',sans-serif;">9. He\'s Tru Blue</div>
          <div style="font-size:12px;color:var(--muted-fg);margin-top:2px">Xxxx Hcp</div>
          <div style="font-size:12px;color:hsl(200 70% 40%);margin-top:3px;font-weight:600">Joel Marshall</div>
        </div>
        <div style="display:flex;gap:8px;text-align:center;">
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:8px 12px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Win</div>
            <div style="font-size:18px;font-weight:800;font-family:\'JetBrains Mono\',monospace;">$12.00</div>
          </div>
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:8px 12px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Place</div>
            <div style="font-size:18px;font-weight:800;font-family:\'JetBrains Mono\',monospace;color:var(--accent);">$3.00</div>
          </div>
        </div>
      </div>

      <div style="background:var(--muted);border-radius:12px;padding:14px 18px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
        <div>
          <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:3px">Race 8 · 16:13 · Victory Stakes</div>
          <div style="font-size:15px;font-weight:800;font-family:\'Geist\',sans-serif;">12. Abounding</div>
          <div style="font-size:12px;color:var(--muted-fg);margin-top:2px">Ladbrokes Victory Stakes</div>
          <div style="font-size:12px;color:hsl(200 70% 40%);margin-top:3px;font-weight:600">Adam Williams</div>
        </div>
        <div style="display:flex;gap:8px;text-align:center;">
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:8px 12px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Win</div>
            <div style="font-size:18px;font-weight:800;font-family:\'JetBrains Mono\',monospace;">$20.00</div>
          </div>
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:8px 12px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Place</div>
            <div style="font-size:18px;font-weight:800;font-family:\'JetBrains Mono\',monospace;color:var(--accent);">$4.50</div>
          </div>
        </div>
      </div>

      <div style="background:var(--muted);border-radius:12px;padding:14px 18px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
        <div>
          <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:3px">Race 9 · 16:50 · Bm85</div>
          <div style="font-size:15px;font-weight:800;font-family:\'Geist\',sans-serif;">14. Cosmo Centaurus</div>
          <div style="font-size:12px;color:var(--muted-fg);margin-top:2px">Sky Racing (Bm85)</div>
          <div style="font-size:12px;color:hsl(200 70% 40%);margin-top:3px;font-weight:600">Scott McDonell</div>
        </div>
        <div style="display:flex;gap:8px;text-align:center;">
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:8px 12px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Win</div>
            <div style="font-size:18px;font-weight:800;font-family:\'JetBrains Mono\',monospace;">$3.60</div>
          </div>
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:8px 12px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Place</div>
            <div style="font-size:18px;font-weight:800;font-family:\'JetBrains Mono\',monospace;color:var(--accent);">$1.40</div>
          </div>
        </div>
      </div>

    </div>
    <p style="font-size:11px;color:var(--muted-fg);margin-top:12px">Source: BestBets.com.au · Tips are editorial predictions only. Gamble responsibly. 18+</p>
  </div>'''

html = html.replace(old_eagle, new_eagle)

with open('horse-racing-tips-today.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done — Eagle Farm tips added")
