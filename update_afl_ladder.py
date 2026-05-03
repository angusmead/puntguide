#!/usr/bin/env python3
"""Update AFL ladder 2026 page with enriched columns from AFL.com"""

with open('afl-ladder-2026.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. Add CSS for next-opp and odds-chip ──────────────────────────
old_css_end = '.legend{display:flex;gap:16px;font-size:12px;color:var(--muted-fg);margin-bottom:12px;flex-wrap:wrap;}'
new_css = '''.legend{display:flex;gap:16px;font-size:12px;color:var(--muted-fg);margin-bottom:12px;flex-wrap:wrap;}
.next-opp{font-size:12px;color:var(--muted-fg);font-weight:600;}
.odds-chip{display:inline-block;background:hsl(215 45% 16%);color:var(--primary);font-family:"JetBrains Mono",monospace;font-size:11px;font-weight:700;padding:2px 7px;border-radius:5px;white-space:nowrap;}
.pos-marker{display:inline-block;font-size:9px;font-weight:700;padding:1px 5px;border-radius:3px;margin-left:5px;vertical-align:middle;}
.top6-marker{background:hsl(140 50% 40%);color:#fff;}
.wc-marker{background:hsl(200 88% 50%);color:#fff;}'''
html = html.replace(old_css_end, new_css)

# ── 2. Fix mobile media query to hide cols from nth-child(8) ────────
old_media = '@media(max-width:768px){.nav-links{display:none;}.wrap,.hero{padding-left:16px;padding-right:16px;}.nav{padding:0 20px;}.ladder-table th:nth-child(n+5){display:none;}.ladder-table td:nth-child(n+5){display:none;}.analysis-grid{grid-template-columns:1fr;}}'
new_media = '@media(max-width:768px){.nav-links{display:none;}.wrap,.hero{padding-left:16px;padding-right:16px;}.nav{padding:0 20px;}.ladder-table th:nth-child(n+8){display:none;}.ladder-table td:nth-child(n+8){display:none;}.analysis-grid{grid-template-columns:1fr;}}'
html = html.replace(old_media, new_media)

# ── 3. Update table header ───────────────────────────────────────────
old_thead = '<th>Pos</th><th>Team</th><th>P</th><th>W</th><th>L</th><th>D</th><th>PF</th><th>PA</th><th>%</th><th>Pts</th><th>Form</th>'
new_thead = '<th>Pos</th><th>Team</th><th>P</th><th>W</th><th>L</th><th>D</th><th>PF</th><th>PA</th><th>%</th><th>Pts</th><th>Next</th><th>Odds</th><th>Form</th>'
html = html.replace(old_thead, new_thead)

# ── 4. Team data ─────────────────────────────────────────────────────
teams = [
    # pos, zone, separator, team_name, P, W, L, D, PF, PA, pct, pts, next_opp, odds, form_dots, extra_marker
    (1,  'finals-zone', False, 'Fremantle',        8, 7, 1, 0, 758, 570, '133.0', 28, 'Hawthorn',      '$7.00',  'WWWWW', ''),
    (2,  'finals-zone', False, 'Hawthorn',         8, 6, 1, 1, 829, 684, '121.2', 26, 'Fremantle',     '$6.50',  'WWWWD', ''),
    (3,  'finals-zone', False, 'Sydney Swans',     7, 6, 1, 0, 814, 457, '178.1', 24, 'Melbourne',     '$5.00',  'WWWWW', ''),
    (4,  'finals-zone', False, 'Melbourne',        7, 5, 2, 0, 697, 678, '102.8', 20, 'Sydney',        '$81.00', 'WWLWW', ''),
    (5,  'finals-zone', False, 'Collingwood',      8, 4, 3, 1, 666, 613, '108.6', 18, 'Geelong',       '$26.00', 'WLWLD', ''),
    (6,  'finals-zone', True,  'Brisbane Lions',   7, 4, 3, 0, 719, 605, '118.8', 16, 'Essendon',      '$4.50',  'WWLWL', 'top6'),
    (7,  'finals-zone', False, 'North Melbourne',  7, 4, 3, 0, 678, 585, '115.9', 16, 'Geelong',       '$151.00','WLWLW', ''),
    (8,  'finals-zone', True,  'Gold Coast SUNS',  7, 4, 3, 0, 723, 632, '114.4', 16, 'GWS GIANTS',   '$12.00', 'WLWWL', ''),
    (9,  'danger-zone', False, 'Geelong Cats',     7, 4, 3, 0, 656, 604, '108.6', 16, 'North Melb.',   '$13.00', 'WWLWL', ''),
    (10, 'danger-zone', False, 'Adelaide Crows',   8, 4, 4, 0, 685, 709, '96.6',  16, 'Richmond',      '$26.00', 'WLLWL', 'wc'),
    (11, 'danger-zone', False, 'Western Bulldogs', 8, 4, 4, 0, 720, 787, '91.5',  16, 'Port Adelaide', '$34.00', 'WLWLL', ''),
    (12, 'danger-zone', False, 'Port Adelaide',    8, 3, 5, 0, 703, 634, '110.9', 12, 'W. Bulldogs',   '$101.00','LLWLL', ''),
    (13, 'danger-zone', False, 'St Kilda',         7, 3, 4, 0, 657, 597, '110.1', 12, 'Carlton',       '$67.00', 'WLLWL', ''),
    (14, 'danger-zone', False, 'GWS GIANTS',       7, 3, 4, 0, 605, 674, '89.8',  12, 'Gold Coast',    '$41.00', 'WLWLL', ''),
    (15, 'danger-zone', False, 'West Coast Eagles',7, 2, 5, 0, 469, 840, '55.8',   8, 'Richmond',      '$501.00','LWLLL', ''),
    (16, 'danger-zone', False, 'Carlton',          7, 1, 6, 0, 565, 704, '80.3',   4, 'St Kilda',      '$501.00','LLLLL', ''),
    (17, 'danger-zone', False, 'Essendon',         7, 1, 6, 0, 570, 782, '72.9',   4, 'Brisbane',      '$501.00','LLLLL', ''),
    (18, 'danger-zone', False, 'Richmond',         7, 0, 7, 0, 424, 783, '54.2',   0, 'West Coast',    '$501.00','LLLLL', ''),
]

def form_badges(dots):
    badges = []
    for ch in dots:
        if ch == 'W':
            badges.append('<span class="fb fw">W</span>')
        elif ch == 'L':
            badges.append('<span class="fb fl">L</span>')
        else:
            badges.append('<span class="fb fd">D</span>')
    return '<div class="form-badges">' + ''.join(badges) + '</div>'

def build_row(t):
    pos, zone, sep, name, P, W, L, D, PF, PA, pct, pts, nxt, odds, form, marker = t
    tr_class = zone
    if sep:
        tr_class += ' separator'

    # Team name cell
    if marker == 'top6':
        name_cell = f'{name}<span class="pos-marker top6-marker">TOP 6</span>'
    elif marker == 'wc':
        name_cell = f'{name}<span class="pos-marker wc-marker">WC</span>'
    else:
        name_cell = name

    return (
        f'        <tr class="{tr_class}"><td>{pos}</td>'
        f'<td>{name_cell}</td>'
        f'<td>{P}</td><td>{W}</td><td>{L}</td><td>{D}</td>'
        f'<td>{PF}</td><td>{PA}</td>'
        f'<td class="pct-col">{pct}</td>'
        f'<td class="pts-col">{pts}</td>'
        f'<td class="next-opp">{nxt}</td>'
        f'<td><span class="odds-chip">{odds}</span></td>'
        f'<td>{form_badges(form)}</td>'
        f'</tr>'
    )

rows = '\n'.join(build_row(t) for t in teams)

new_tbody = f'''      <tbody>
{rows}
      </tbody>'''

# Replace old tbody
import re
html = re.sub(r'<tbody>.*?</tbody>', new_tbody, html, flags=re.DOTALL)

# ── 5. Update source attribution ─────────────────────────────────────
html = html.replace(
    'Source: ZeroHanger · Updated after Round 8, 2 May 2026 · Green border = top 8 cut-off',
    'Source: AFL.com · Updated after Round 8, 2 May 2026 · Green border = top 8 cut-off · Odds: Sportsbet'
)

with open('afl-ladder-2026.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done — AFL ladder updated with Next Opp, Odds, Top 6 + WC markers")
