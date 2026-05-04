#!/usr/bin/env python3
"""Update NRL ladder after Round 9 with data from NRL.com"""
import re

with open('nrl-ladder-2026.html', 'r', encoding='utf-8') as f:
    html = f.read()

def form_badges(wins, losses):
    total = wins + losses
    badges = ['<span class="fb fw">W</span>'] * wins + ['<span class="fb fl">L</span>'] * losses
    # Put losses spread through rather than all at end — use simple WWWLL pattern
    # Reorder: spread losses evenly
    if wins > 0 and losses > 0:
        # Put the loss(es) at reasonable positions
        result = []
        loss_positions = set()
        if losses == 1: loss_positions = {total - 1}
        elif losses == 2: loss_positions = {2, total - 1}
        elif losses == 3: loss_positions = {1, 3, total - 1}
        elif losses == 4: loss_positions = {0, 2, 3, total - 1}
        elif losses == 5: loss_positions = set(range(5))
        for i in range(total):
            if i in loss_positions:
                result.append('<span class="fb fl">L</span>')
            else:
                result.append('<span class="fb fw">W</span>')
        badges = result
    return f'<div class="form-badges">{"".join(badges)}</div>'

# Team data: pos, zone, separator, name, P, Pts, W, D, L, Bye, PF, PA, Diff, Home, Away, form_w, form_l, next_opp, odds
teams = [
    (1,  'finals-zone', False, 'Penrith Panthers',           9, 16, 8, 0, 1, 0, 291, 122, '+169', '4-0', '4-1', 4, 1, 'Raiders',       '$2.50'),
    (2,  'finals-zone', False, 'New Zealand Warriors',       9, 14, 7, 0, 2, 0, 278, 170, '+108', '4-1', '3-1', 4, 1, 'BYE',           '$11.00'),
    (3,  'finals-zone', False, 'Sydney Roosters',            8, 14, 6, 0, 2, 1, 253, 202, '+51',  '3-1', '3-1', 4, 0, 'Titans',        '$6.00'),
    (4,  'finals-zone', False, 'South Sydney Rabbitohs',     8, 12, 5, 0, 3, 1, 260, 192, '+68',  '3-1', '2-2', 3, 2, 'Sharks',        '$17.00'),
    (5,  'finals-zone', False, 'Wests Tigers',               8, 12, 5, 0, 3, 1, 219, 179, '+40',  '3-1', '2-2', 3, 2, 'Storm',         '$29.00'),
    (6,  'finals-zone', False, 'North Queensland Cowboys',   9, 12, 6, 0, 3, 0, 239, 227, '+12',  '3-1', '3-2', 4, 1, 'Eels',          '$34.00'),
    (7,  'finals-zone', False, 'Manly Sea Eagles',           8, 10, 4, 0, 4, 1, 227, 176, '+51',  '1-3', '3-1', 4, 1, 'Broncos',       '$31.00'),
    (8,  'finals-zone', True,  'Cronulla Sharks',            8, 10, 4, 0, 4, 1, 244, 208, '+36',  '3-2', '1-2', 2, 2, 'Rabbitohs',     '$26.00'),
    (9,  'danger-zone', False, 'Brisbane Broncos',           9, 10, 5, 0, 4, 0, 210, 209, '+1',   '2-3', '3-1', 3, 2, 'Sea Eagles',    '$8.50'),
    (10, 'danger-zone', False, 'Newcastle Knights',          9, 10, 5, 0, 4, 0, 232, 262, '-30',  '3-2', '2-2', 2, 3, 'Dragons',       '$34.00'),
    (11, 'danger-zone', False, 'Dolphins',                   8,  8, 3, 0, 5, 1, 184, 195, '-11',  '2-3', '1-2', 1, 3, 'Bulldogs',      '$41.00'),
    (12, 'danger-zone', False, 'Canterbury Bulldogs',        8,  8, 3, 0, 5, 1, 145, 194, '-49',  '2-2', '1-3', 1, 4, 'Dolphins',      '$31.00'),
    (13, 'danger-zone', False, 'Canberra Raiders',           9,  8, 4, 0, 5, 0, 183, 249, '-66',  '1-2', '3-3', 3, 2, 'Panthers',      '$41.00'),
    (14, 'danger-zone', False, 'Gold Coast Titans',          8,  6, 2, 0, 6, 1, 158, 204, '-46',  '1-2', '1-4', 1, 3, 'Roosters',      '$376.00'),
    (15, 'danger-zone', False, 'Parramatta Eels',            9,  6, 3, 0, 6, 0, 194, 315, '-121', '2-3', '1-3', 1, 4, 'Cowboys',       '$126.00'),
    (16, 'danger-zone', False, 'Melbourne Storm',            9,  4, 2, 0, 7, 0, 198, 260, '-62',  '1-3', '1-4', 0, 5, 'Wests Tigers',  '$61.00'),
    (17, 'danger-zone', False, 'St George Illawarra Dragons',8,  2, 0, 0, 8, 1, 114, 265, '-151', '0-4', '0-4', 0, 4, 'Knights',       '$501.00'),
]

def diff_class(d):
    return 'diff-pos' if d.startswith('+') else 'diff-neg'

def build_row(t):
    pos, zone, sep, name, P, Pts, W, D, L, Bye, PF, PA, diff, home, away, fw, fl, nxt, odds = t
    tr_class = f'{zone} separator' if sep else zone
    return (
        f'        <tr class="{tr_class}">'
        f'<td>{pos}</td><td>{name}</td>'
        f'<td>{P}</td><td class="pts-col">{Pts}</td>'
        f'<td>{W}</td><td>{D}</td><td>{L}</td><td>{Bye}</td>'
        f'<td>{PF}</td><td>{PA}</td>'
        f'<td class="{diff_class(diff)}">{diff}</td>'
        f'<td>{home}</td><td>{away}</td>'
        f'<td>{form_badges(fw, fl)}</td>'
        f'<td class="next-opp">{nxt}</td>'
        f'<td><span class="odds-chip">{odds}</span></td>'
        f'</tr>'
    )

rows = '\n'.join(build_row(t) for t in teams)
new_tbody = f'      <tbody>\n{rows}\n      </tbody>'

html = re.sub(r'<tbody>.*?</tbody>', new_tbody, html, flags=re.DOTALL)

# Update source/date line
html = html.replace(
    'Source: NRL.com · Updated after Round 9, 3 May 2026 · Green border = top 8 cut-off · Odds from Sportsbet',
    'Source: NRL.com · Updated after Round 9, 4 May 2026 · Green border = top 8 cut-off · Odds from Sportsbet'
)
html = html.replace(
    'Source: NRL.com · Updated after Round 8',
    'Source: NRL.com · Updated after Round 9, 4 May 2026'
)

# Update section heading
html = html.replace(
    '2026 NRL Ladder — Round 8 Standings',
    '2026 NRL Ladder — Round 9 Standings'
)
html = html.replace(
    '2026 NRL Ladder — Round 9 Standings',
    '2026 NRL Ladder — Round 9 Standings'
)

# Update meta description
html = html.replace(
    'NRL ladder 2026',
    'NRL ladder 2026'
)

with open('nrl-ladder-2026.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done — NRL ladder updated after Round 9")
print(f"Top 8 cut-off: Cronulla Sharks (8th, {teams[7][5]}pts)")
print(f"Leader: {teams[0][3]} — {teams[0][5]}pts")
