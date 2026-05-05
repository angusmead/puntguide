"""
apply_affiliate_links.py
Reads data/affiliate_links.json and permanently bakes affiliate URLs into
review page HTML files for all bookmakers with status "live".

Run this once you've confirmed an affiliate URL is correct and want it
hard-coded into the HTML (rather than relying on the JS router at load time).

Usage:
    python apply_affiliate_links.py           # Updates all "live" bookmakers
    python apply_affiliate_links.py sportsbet # Updates one bookmaker only
"""

import json, re, sys
from pathlib import Path

SITE = Path(__file__).parent
DATA = SITE / 'data' / 'affiliate_links.json'

def apply(slug, bm):
    page = SITE / f'review-{slug}.html'
    if not page.exists():
        print(f'  SKIP  {slug} — review page not found')
        return

    html = page.read_text(encoding='utf-8')
    url  = bm['affiliate_url']
    name = bm['name']

    # Replace href="#" on primary CTA buttons with the affiliate URL
    # Handles: href="#" onclick="return false;" and plain href="#"
    original = html

    # Pattern: href="#" with optional onclick noise, inside an <a> tag with btn-g or bcta class
    html = re.sub(
        r'(<a\b[^>]*\bclass="[^"]*\b(?:btn-g|bcta|bet-cta)\b[^"]*"[^>]*)href="#"[^>]*>',
        lambda m: m.group(1) + f'href="{url}" target="_blank" rel="noopener sponsored">',
        html
    )

    # Also catch the reversed attribute order (href before class)
    html = re.sub(
        r'(<a\b[^>]*)href="#"([^>]*\bclass="[^"]*\b(?:btn-g|bcta|bet-cta)\b[^"]*"[^>]*)>',
        lambda m: m.group(1) + f'href="{url}" target="_blank" rel="noopener sponsored"' + m.group(2) + '>',
        html
    )

    if html == original:
        print(f'  NONE  {slug} ({name}) — no placeholder CTAs found to update')
    else:
        page.write_text(html, encoding='utf-8')
        count = original.count('href="#"') - html.count('href="#"')
        print(f'  DONE  {slug} ({name}) — {count} CTA(s) updated → {url}')

def main():
    affiliates = json.loads(DATA.read_text(encoding='utf-8'))

    target = sys.argv[1] if len(sys.argv) > 1 else None

    print('\n=== PuntGuide Affiliate Link Applicator ===\n')

    updated = 0
    for slug, bm in affiliates.items():
        if slug.startswith('_'):
            continue  # skip readme/metadata keys
        if target and slug != target:
            continue
        if bm.get('status') != 'live':
            if not target:
                continue  # silently skip non-live in bulk mode
            else:
                print(f'  SKIP  {slug} — status is "{bm.get("status")}", not "live"')
                continue
        if not bm.get('affiliate_url'):
            print(f'  SKIP  {slug} — affiliate_url is empty')
            continue

        apply(slug, bm)
        updated += 1

    print(f'\n{updated} bookmaker(s) processed.\n')
    if not target:
        print('Tip: Run  python apply_affiliate_links.py sportsbet  to test a single bookmaker first.')

if __name__ == '__main__':
    main()
