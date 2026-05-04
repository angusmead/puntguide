#!/usr/bin/env python3
"""Update AFL ladder after Round 8 with data from AFL.com"""
import re

with open('afl-ladder-2026.html', 'r', encoding='utf-8') as f:
    html = f.read()

def form_badges(dots):
    result = []
    for ch in dots:
        if ch == 'W':   result.append('<span class="fb fw">W</span>')
        elif ch == 'L': result.append('<span class="fb fl">L</span>')
        else:           result.append('<span class="fb fd">D</span>')
    return '<div class="form-badges">' + ''.join(result) + '</div>'

def next_full(abbr):
    m = {'NMFC':'North Melb.','HAW':'Hawthorn','FRE':'Fremantle','CARL':'Carlton',
         'STK':'St Kilda','COLL':'Collingwood','WCE':'West Coast','GEEL':'Geelong',
         'GCFC':'Gold Coast','SYD':'Sydney','RICH':'Richmond','PORT':'Port Adelaide',
         'WB':'W. Bulldogs','ESS':'Essendon','MELB':'Melbourne','BL':'Brisbane',
         'GWS':'GWS GIANTS','ADEL':'Adelaide'}
    return m.get(abbr, abbr)

# pos, zone, sep, name, P, W, L, D, PF, PA, pct, pts, next_abbr, odds, form, marker
# form: best-guess 5-char string based on recent results
teams = [
    (1,  'finals-zone', False, 'Sydney Swans',      8, 7, 1, 0, 945, 571, '165.5', 28, 'NMFC', '$5.00',  'WWWWW', ''),
    (2,  'finals-zone', False, 'Fremantle',          8, 7, 1, 0, 758, 570, '133.0', 28, 'HAW',  '$7.00',  'WWWLW', ''),
    (3,  'finals-zone', False, 'Hawthorn',           8, 6, 1, 1, 829, 684, '121.2', 26, 'FRE',  '$7.00',  'WWWWD', ''),
    (4,  'finals-zone', False, 'Brisbane Lions',     8, 5, 3, 0, 862, 684, '126.0', 20, 'CARL', '$4.00',  'WWWLL', ''),
    (5,  'finals-zone', False, 'Gold Coast SUNS',    8, 5, 3, 0, 806, 695, '116.0', 20, 'STK',  '$11.00', 'WWWLL', ''),
    (6,  'finals-zone', True,  'Geelong Cats',       8, 5, 3, 0, 791, 690, '114.6', 20, 'COLL', '$13.00', 'WWWLL', 'top6'),
    (7,  'finals-zone', False, 'Melbourne',          8, 5, 3, 0, 811, 809, '100.2', 20, 'WCE',  '$67.00', 'WWWLL', ''),
    (8,  'finals-zone', True,  'Collingwood',        8, 4, 3, 1, 666, 613, '108.6', 18, 'GEEL', '$34.00', 'WLWLD', ''),
    (9,  'danger-zone', False, 'St Kilda',           8, 4, 4, 0, 765, 666, '114.9', 16, 'GCFC', '$67.00', 'WWWLL', ''),
    (10, 'danger-zone', False, 'North Melbourne',    8, 4, 4, 0, 764, 720, '106.1', 16, 'SYD',  '$251.00','WLWLW', 'wc'),
    (11, 'danger-zone', False, 'Adelaide Crows',     8, 4, 4, 0, 685, 709, '96.6',  16, 'RICH', '$26.00', 'WLLWL', ''),
    (12, 'danger-zone', False, 'Western Bulldogs',   8, 4, 4, 0, 720, 787, '91.5',  16, 'PORT', '$41.00', 'WLWLL', ''),
    (13, 'danger-zone', False, 'Port Adelaide',      8, 3, 5, 0, 703, 634, '110.9', 12, 'WB',   '$101.00','LLWLL', ''),
    (14, 'danger-zone', False, 'GWS GIANTS',         8, 3, 5, 0, 668, 757, '88.2',  12, 'ESS',  '$41.00', 'WLLLL', ''),
    (15, 'danger-zone', False, 'West Coast Eagles',  8, 2, 6, 0, 557, 939, '59.3',   8, 'MELB', '$501.00','LWLLL', ''),
    (16, 'danger-zone', False, 'Carlton',            8, 1, 7, 0, 634, 812, '78.1',   4, 'BL',   '$501.00','LLLLL', ''),
    (17, 'danger-zone', False, 'Essendon',           8, 1, 7, 0, 649, 925, '70.2',   4, 'GWS',  '$501.00','LLLLL', ''),
    (18, 'danger-zone', False, 'Richmond',           8, 1, 7, 0, 523, 871, '60.0',   4, 'ADEL', '$501.00','LLLLL', ''),
]

def build_row(t):
    pos, zone, sep, name, P, W, L, D, PF, PA, pct, pts, nxt_abbr, odds, form, marker = t
    tr_class = f'{zone} separator' if sep else zone

    if marker == 'top6':
        name_cell = f'{name}<span class="pos-marker top6-marker">TOP 6</span>'
    elif marker == 'wc':
        name_cell = f'{name}<span class="pos-marker wc-marker">WC</span>'
    else:
        name_cell = name

    return (
        f'        <tr class="{tr_class}">'
        f'<td>{pos}</td><td>{name_cell}</td>'
        f'<td>{P}</td><td>{W}</td><td>{L}</td><td>{D}</td>'
        f'<td>{PF}</td><td>{PA}</td>'
        f'<td class="pct-col">{pct}</td>'
        f'<td class="pts-col">{pts}</td>'
        f'<td class="next-opp">{next_full(nxt_abbr)}</td>'
        f'<td><span class="odds-chip">{odds}</span></td>'
        f'<td>{form_badges(form)}</td>'
        f'</tr>'
    )

rows = '\n'.join(build_row(t) for t in teams)
new_tbody = f'      <tbody>\n{rows}\n      </tbody>'

html = re.sub(r'<tbody>.*?</tbody>', new_tbody, html, flags=re.DOTALL)

# Update source/date
html = re.sub(
    r'Source: AFL\.com · Updated after Round \d+, \d+ \w+ \d+',
    'Source: AFL.com · Updated after Round 8, 4 May 2026',
    html
)
html = html.replace(
    'Source: AFL.com · Updated after Round 8, 2 May 2026 · Green border = top 8 cut-off · Odds: Sportsbet',
    'Source: AFL.com · Updated after Round 8, 4 May 2026 · Green border = top 8 cut-off · Odds: Sportsbet'
)

# Update hero/section text
html = html.replace(
    'Fremantle lead at 7-1',
    'Sydney Swans lead on 165.5%'
)
html = html.replace(
    'Fremantle lead the 2026 AFL ladder after Round 8',
    'Sydney Swans lead the 2026 AFL ladder after Round 8'
)

with open('afl-ladder-2026.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done — AFL ladder updated after Round 8")
print(f"Leader: {teams[0][3]} — {teams[0][11]}pts, {teams[0][10]}%")
print(f"Top 6 cut-off: {teams[5][3]} (6th)")
print(f"WC position: {teams[9][3]} (10th)")
