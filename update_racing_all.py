#!/usr/bin/env python3
"""Fill in Ascot, Hawkesbury and Bendigo tips from BestBets — Saturday 2 May 2026."""

with open('horse-racing-tips-today.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ─── helper to build a tip card ───────────────────────────────────────────────
def best_card(race_label, horse, race_name, tipsters, win, place, gold=True):
    bg = "hsl(48 80% 97%)" if gold else "var(--muted)"
    border = "border:2px solid hsl(48 60% 70%);" if gold else "border:1px solid var(--border);"
    tick = "✓ " if gold else ""
    return f'''      <div style="background:{bg};{border}border-radius:12px;padding:16px 20px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
        <div>
          <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:4px">{race_label}</div>
          <div style="font-size:{'18' if gold else '16'}px;font-weight:800;font-family:'Geist',sans-serif;letter-spacing:-0.02em">{horse}</div>
          <div style="font-size:13px;color:var(--muted-fg);margin-top:3px">{race_name}</div>
          <div style="font-size:12px;color:hsl({'140 45% 35%' if gold else '200 70% 40%'});margin-top:{'6' if gold else '4'}px;font-weight:600">{tick}{tipsters}</div>
        </div>
        <div style="display:flex;gap:10px;text-align:center;">
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:{'10' if gold else '8'}px {'16' if gold else '12'}px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Win</div>
            <div style="font-size:{'22' if gold else '20'}px;font-weight:800;font-family:'JetBrains Mono',monospace;">{win}</div>
          </div>
          <div style="background:#fff;border:1px solid var(--border);border-radius:8px;padding:{'10' if gold else '8'}px {'16' if gold else '12'}px;">
            <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted-fg);margin-bottom:2px">Place</div>
            <div style="font-size:{'22' if gold else '20'}px;font-weight:800;font-family:'JetBrains Mono',monospace;color:var(--accent);">{place}</div>
          </div>
        </div>
      </div>'''

def badge(label, color):
    margin = "18px" if "VALUE" in label else "0px"
    text_color = "var(--primary)" if "BEST" in label else "#fff"
    return f'    <div style="display:flex;align-items:center;gap:8px;margin:{margin} 0 14px">\n      <span style="background:{color};color:{text_color};font-size:11px;font-weight:700;padding:3px 9px;border-radius:5px;font-family:\'JetBrains Mono\',monospace;">{label}</span>\n    </div>'

def section(venue_id, venue_name, intro, best_cards, value_cards):
    return f'''  <!-- ── {venue_name.upper()} {'─'*(50-len(venue_name))} -->
  <div class="section" id="tips-{venue_id}">
    <h2>{venue_name} — Saturday 2 May 2026</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">{intro} Tips sourced from BestBets.com.au.</p>

{badge("BEST OF THE DAY", "hsl(215 45% 16%)")}

    <div style="display:flex;flex-direction:column;gap:12px;margin-bottom:18px;">
{chr(10).join(best_cards)}
    </div>

{badge("VALUE BETS", "hsl(200 88% 50%)")}

    <div style="display:flex;flex-direction:column;gap:12px;">
{chr(10).join(value_cards)}
    </div>
    <p style="font-size:11px;color:var(--muted-fg);margin-top:12px">Source: BestBets.com.au · Tips are editorial predictions only. Gamble responsibly. 18+</p>
  </div>'''

# ─── ASCOT ────────────────────────────────────────────────────────────────────
ascot_best = [
    best_card("Race 4 · 15:29 · Bm72+", "4. Rock 'N' The Jam", "Pearce Racing Ladies Day",
              "Greg Hooper &amp; Joel Marshall", "$2.10", "$1.30", True),
    best_card("Race 8 · 18:10 · WA Sires' Produce Stakes", "2. Beatty", "W.A. Sires' Produce Stakes",
              "Paul Kelly", "$1.65", "$1.06", True),
]
ascot_value = [
    best_card("Race 3 · 14:54", "6. Moonwalk", "Liquor Barons (Rs0ly)",
              "Greg Hooper", "$2.35", "$1.20", False),
    best_card("Race 7 · 17:35", "2. Crunchy Nut", "Mc Polytrack (Rs1mw)",
              "Paul Kelly", "$6.50", "$2.15", False),
    best_card("Race 9 · 18:45 · Bm66+", "8. Auto Cruise", "City of Belmont",
              "Joel Marshall", "$3.00", "$1.30", False),
]

# ─── HAWKESBURY ───────────────────────────────────────────────────────────────
hawk_best = [
    best_card("Race 7 · 14:50 · Hawkesbury Crown", "9. Bauhinia", "Pioneer Services Hawkesbury Crown",
              "Joel Marshall", "$9.50", "$2.60", True),
    best_card("Race 8 · 15:25 · Gold Cup", "5. Vivy Air", "Richmond Club Hawkesbury Gold Cup",
              "Kevin Casey &amp; Ken Coram", "$3.30", "$1.50", True),
]
hawk_value = [
    best_card("Race 5 · Bm78", "14. Couples Retreat", "Blakes Marine (Bm78)",
              "Joel Marshall", "$8.50", "$2.30", False),
    best_card("Race 7 · 14:50 · Hawkesbury Crown", "4. Oh Diamond Lil", "Pioneer Services Hawkesbury Crown",
              "Kevin Casey", "$4.00", "$1.62", False),
    best_card("Race 9 · 16:05", "3. Way To The Stars", "Hawkesbury Xxxx Gold Rush",
              "Ken Coram", "$5.00", "$1.95", False),
]

# ─── BENDIGO ──────────────────────────────────────────────────────────────────
bend_best = [
    best_card("Race 4 · Bm74 · Carlton Draught", "14. Oak Beach", "Carlton Draught (Bm74)",
              "Brendan Tupper", "$3.20", "$1.40", True),
    best_card("Race 5 · Bendigo Gold Bracelet", "1. Oh Too Good", "Catanach's Jewellers Bendigo Gold Bracelet",
              "Paul Richards", "$4.80", "$1.67", True),
    best_card("Race 5 · Bendigo Gold Bracelet", "6. Lady Jones", "Catanach's Jewellers Bendigo Gold Bracelet",
              "John Barker", "$4.00", "$1.50", True),
]
bend_value = [
    best_card("Race 4 · Bm74 · Carlton Draught", "14. Oak Beach", "Carlton Draught (Bm74)",
              "John Barker", "$3.20", "$1.40", False),
    best_card("Race 7 · 15:05", "9. Choir Point", "Turners Crossing Hcp",
              "Brendan Tupper", "$5.50", "$1.91", False),
    best_card("Race 9 · 16:20 · Golden Mile", "4. Holymanz", "Ladbrokes Golden Mile",
              "Paul Richards", "$10.00", "$3.20", False),
]

# ─── Build replacement sections ───────────────────────────────────────────────
new_ascot = section(
    "ascot", "Ascot",
    "Metropolitan Saturday meeting at Ascot Racecourse, Perth.",
    ascot_best, ascot_value
)

new_hawkesbury = section(
    "hawkesbury", "Hawkesbury",
    "Provincial Saturday meeting at Hawkesbury Racecourse, west of Sydney. Features the Hawkesbury Crown and Gold Cup.",
    hawk_best, hawk_value
)

new_bendigo = section(
    "bendigo", "Bendigo",
    "Provincial Saturday meeting at Bendigo Racecourse, central Victoria. Features the Bendigo Gold Bracelet and Ladbrokes Golden Mile.",
    bend_best, bend_value
)

# ─── Apply replacements ───────────────────────────────────────────────────────

# Ascot placeholder
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
if old_ascot in html:
    html = html.replace(old_ascot, new_ascot)
    print("Ascot: replaced placeholder")
else:
    print("Ascot: placeholder not found — may already have tips")

# Hawkesbury placeholder
old_hawk = '''  <!-- ── HAWKESBURY ─────────────────────────────────────────────────────── -->
  <div class="section" id="tips-hawkesbury">
    <h2>Hawkesbury — Saturday 2 May 2026</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">Provincial Saturday meeting at Hawkesbury Racecourse, west of Sydney.</p>
    <div style="background:hsl(205 40% 97%);border:1px dashed var(--border);border-radius:12px;padding:20px;text-align:center;color:var(--muted-fg);">
      <div style="font-size:14px;font-weight:600;margin-bottom:6px;">Tips for Hawkesbury</div>
      <div style="font-size:13px;">Send us the BestBets card for Hawkesbury to add today\'s selections here.</div>
    </div>
    <p style="font-size:11px;color:var(--muted-fg);margin-top:10px">Tips are editorial predictions only. Gamble responsibly. 18+</p>
  </div>'''
html = html.replace(old_hawk, new_hawkesbury)
print("Hawkesbury: replaced placeholder")

# Bendigo placeholder
old_bend = '''  <!-- ── BENDIGO ─────────────────────────────────────────────────────────── -->
  <div class="section" id="tips-bendigo">
    <h2>Bendigo — Saturday 2 May 2026</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">Provincial Saturday meeting at Bendigo Racecourse, central Victoria.</p>
    <div style="background:hsl(205 40% 97%);border:1px dashed var(--border);border-radius:12px;padding:20px;text-align:center;color:var(--muted-fg);">
      <div style="font-size:14px;font-weight:600;margin-bottom:6px;">Tips for Bendigo</div>
      <div style="font-size:13px;">Send us the BestBets card for Bendigo to add today\'s selections here.</div>
    </div>
    <p style="font-size:11px;color:var(--muted-fg);margin-top:10px">Tips are editorial predictions only. Gamble responsibly. 18+</p>
  </div>'''
html = html.replace(old_bend, new_bendigo)
print("Bendigo: replaced placeholder")

with open('horse-racing-tips-today.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done — all three meets updated")
