#!/usr/bin/env python3
"""
Phase 2A trust signals:
1. Add Last Updated + affiliate disclosure to all 130 review pages
2. Add Last Updated to 3 key list pages missing it
"""
import os, re

UPDATED = "May 2026"

AFFILIATE_BLOCK = '''<div style="background:hsl(48 80% 97%);border:1px solid hsl(48 60% 80%);border-radius:10px;padding:12px 16px;margin:0 0 24px;font-size:13px;line-height:1.6;color:hsl(215 45% 16%/.8);">
<strong>Affiliate disclosure:</strong> PuntGuide may earn a commission if you sign up through links on this page. This does not influence our editorial rating or recommendations. <a href="/editorial-policy.html" style="color:hsl(200 88% 45%);">Learn how we review bookmakers →</a>
</div>'''

UPDATED_BADGE = f'<p style="font-size:12px;color:hsl(215 20% 42%);font-family:\'JetBrains Mono\',monospace;margin-top:6px;">Last updated: {UPDATED}</p>'

# ── 1. Review pages ────────────────────────────────────────────────────────────
review_pages = [f for f in os.listdir('.') if f.startswith('review-') and f.endswith('.html')]
fixed_reviews = 0

for fn in review_pages:
    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()

    changed = False

    # Add Last Updated after the <h1> tag if not present
    if 'Last updated:' not in html and 'last-updated' not in html:
        html = re.sub(
            r'(<h1[^>]*>[^<]*</h1>)',
            r'\1\n' + UPDATED_BADGE,
            html, count=1
        )
        changed = True

    # Add affiliate disclosure before the first <div class="section"> or <div class="wrap">
    if 'Affiliate disclosure' not in html and 'affiliate disclosure' not in html.lower():
        # Insert after the opening of the main content area
        for marker in ['<div class="wrap">', '<div class="page-wrap">', '<div id="content">']:
            if marker in html:
                html = html.replace(marker, marker + '\n' + AFFILIATE_BLOCK, 1)
                changed = True
                break

    if changed:
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(html)
        fixed_reviews += 1

print(f"Review pages updated: {fixed_reviews}/{len(review_pages)}")

# ── 2. Key list pages missing Last Updated ─────────────────────────────────────
list_pages = {
    'best-betting-sites-australia.html': 'Last updated: May 2026 · Reviewed monthly',
    'fastest-payout-betting-sites-australia.html': 'Last updated: May 2026',
    'best-betting-apps-australia.html': 'Last updated: May 2026',
}

fixed_lists = 0
for fn, label in list_pages.items():
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()
    if 'Last updated' in html or 'last updated' in html.lower():
        print(f"  SKIP (already has it): {fn}")
        continue
    # Insert after the <h1> tag
    badge = f'<p style="font-size:12px;color:hsl(215 20% 42%);font-family:\'JetBrains Mono\',monospace;margin-top:6px;">{label}</p>'
    html = re.sub(r'(<h1[^>]*>.*?</h1>)', r'\1\n' + badge, html, count=1, flags=re.DOTALL)
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Fixed: {fn}")
    fixed_lists += 1

print(f"List pages updated: {fixed_lists}")
print("Done.")
