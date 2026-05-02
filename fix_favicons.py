#!/usr/bin/env python3
"""Add missing favicon link to pages that don't have it."""
import os, re

FAVICON = '<link rel="icon" type="image/png" href="/pg-icon.png">'

pages = [
    'best-betting-apps-australia.html',
    'best-betting-sites-for-afl.html',
    'afl-premiership-odds-2026.html',
    'fastest-withdrawal-betting-sites-australia.html',
    'index.html',
    'new-betting-sites-australia.html',
    'best-betting-sites-australia.html',
    'fastest-payout-betting-sites-australia.html',
    'nrl-premiership-odds-2026.html',
    'which-betting-sites-worth-using-australia.html',
    'best-betting-sites-afl-nrl.html',
    'best-betting-sites-for-racing.html',
]

fixed = 0
for page in pages:
    with open(page, 'r', encoding='utf-8') as f:
        html = f.read()
    if 'rel="icon"' in html:
        print(f"  SKIP (already has it): {page}")
        continue
    # Insert after </title> or after last <meta> in head, or before </head>
    if '</title>' in html:
        html = html.replace('</title>', f'</title>\n{FAVICON}', 1)
    else:
        html = html.replace('</head>', f'{FAVICON}\n</head>', 1)
    with open(page, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  FIXED: {page}")
    fixed += 1

print(f"\nDone — {fixed} pages updated")
