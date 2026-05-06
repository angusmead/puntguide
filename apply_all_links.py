"""
apply_all_links.py
Applies real bookmaker URLs to every CTA button across the entire site.

Handles four patterns:
  1. all-betting-sites.html   — data-name="slug" on card articles
  2. Hub/list pages           — onclick="tc('slug','page','CPA')"
  3. Compare pages            — two buttons, slugs from filename
  4. Generic href="#"         — links to best-betting-sites-australia
"""

import json, re, os, sys

ROOT = '/Users/angusmead/puntguide'
BEST = '/best-betting-sites-australia'

# Load affiliate registry
data = json.loads(open(os.path.join(ROOT, 'data/affiliate_links.json'), encoding='utf-8').read())

def url_for(slug):
    slug = slug.lower().strip()
    bm = data.get(slug)
    if bm and bm.get('affiliate_url'):
        return bm['affiliate_url']
    if bm and bm.get('homepage'):
        return bm['homepage']
    return None

def make_link(url, original_tag):
    """Replace href="#" and remove onclick/return false from an <a> tag."""
    tag = re.sub(r'\s*onclick="[^"]*"', '', original_tag)
    tag = re.sub(r'href="#"', f'href="{url}"', tag)
    # Add target and rel if not present
    if 'target=' not in tag:
        tag = tag.replace('class=', 'target="_blank" rel="noopener" class=')
    return tag

updated_files = 0
updated_buttons = 0

# ─── 1. all-betting-sites.html ───────────────────────────────────────────────
fname = os.path.join(ROOT, 'all-betting-sites.html')
html = open(fname, encoding='utf-8').read()
original = html

def replace_card_button(m):
    card_html = m.group(0)
    slug_match = re.search(r'data-name="([^"]+)"', card_html)
    if not slug_match:
        return card_html
    slug = slug_match.group(1)
    url = url_for(slug)
    if not url:
        return card_html

    def fix_btn(bm):
        tag = bm.group(0)
        if 'href="#"' not in tag:
            return tag
        return make_link(url, tag)

    return re.sub(r'<a\b[^>]*class="btn-visit"[^>]*>', fix_btn, card_html)

html = re.sub(r'<article class="bm-card".*?</article>', replace_card_button, html, flags=re.DOTALL)

buttons_fixed = original.count('href="#"') - html.count('href="#"')
if html != original:
    open(fname, 'w', encoding='utf-8').write(html)
    updated_files += 1
    updated_buttons += buttons_fixed
    print(f'  all-betting-sites.html — {buttons_fixed} buttons updated')

# ─── 2. Hub/list pages — tc('slug',...) pattern ──────────────────────────────
HUB_PAGES = [
    'best-betting-sites-australia.html',
    'best-betting-apps-australia.html',
    'best-betting-sites-afl-nrl.html',
    'best-betting-sites-for-afl.html',
    'best-betting-sites-for-racing.html',
    'best-nba-betting-sites-australia.html',
    'bookmakers-australia.html',
    'top-betting-sites-australia.html',
    'fastest-payout-betting-sites-australia.html',
    'fastest-withdrawal-betting-sites-australia.html',
    'new-betting-sites-australia.html',
    'no-deposit-betting-sites.html',
    'live-betting-australia.html',
    'online-betting-australia.html',
    'sports-betting-sites-australia.html',
    'betting-sites-australia.html',
    'which-betting-sites-worth-using-australia.html',
    'best-betting-bonuses-australia.html',
    'index.html',
]

for page in HUB_PAGES:
    fpath = os.path.join(ROOT, page)
    if not os.path.exists(fpath):
        continue
    html = open(fpath, encoding='utf-8').read()
    original = html

    def fix_tc_button(m):
        tag = m.group(0)
        slug_match = re.search(r"tc\('([^']+)'", tag)
        if not slug_match:
            return tag
        url = url_for(slug_match.group(1))
        if not url:
            return tag
        return make_link(url, tag)

    html = re.sub(r"<a\b[^>]*href=\"#\"[^>]*onclick=\"tc\([^)]+\)[^>]*>", fix_tc_button, html)

    buttons_fixed = original.count('href="#"') - html.count('href="#"')
    if html != original:
        open(fpath, 'w', encoding='utf-8').write(html)
        updated_files += 1
        updated_buttons += buttons_fixed
        print(f'  {page} — {buttons_fixed} buttons updated')

# ─── 3. Compare pages ─────────────────────────────────────────────────────────
compare_files = [f for f in os.listdir(ROOT) if f.startswith('compare-') and f.endswith('.html')]

for fname in compare_files:
    # Extract slugs from filename: compare-A-vs-B.html
    m = re.match(r'compare-(.+)-vs-(.+)\.html', fname)
    if not m:
        continue
    slug_a, slug_b = m.group(1), m.group(2)
    url_a, url_b = url_for(slug_a), url_for(slug_b)

    fpath = os.path.join(ROOT, fname)
    html = open(fpath, encoding='utf-8').read()
    original = html

    # Find all href="#" buttons and replace in order (first = A, second = B)
    placeholders = list(re.finditer(r'<a\b[^>]*href="#"[^>]*onclick="return false;"[^>]*class="btn-g"[^>]*>', html))

    if len(placeholders) >= 1 and url_a:
        old = placeholders[0].group(0)
        new = make_link(url_a, old)
        html = html.replace(old, new, 1)
    if len(placeholders) >= 2 and url_b:
        old = placeholders[1].group(0)
        new = make_link(url_b, old)
        html = html.replace(old, new, 1)

    buttons_fixed = original.count('href="#"') - html.count('href="#"')
    if html != original:
        open(fpath, 'w', encoding='utf-8').write(html)
        updated_files += 1
        updated_buttons += buttons_fixed
        print(f'  {fname} — {buttons_fixed} buttons updated')

# ─── 4. Remaining pages — generic href="#" → best-betting-sites-australia ────
# Tips, odds, match pages where CTAs are not bookmaker-specific
GENERIC_PAGES = [
    'afl-tips.html', 'nrl-tips.html', 'mlb-tips.html', 'nfl-tips.html',
    'afl-premiership-odds-2026.html', 'nrl-premiership-odds-2026.html',
    'afl-coleman-medal-odds-2026.html', 'brownlow-medal-odds-2026.html',
    'afl-rising-star-odds-2026.html', 'nfl-super-bowl-odds-2026.html',
    'mlb-world-series-odds-2026.html', 'racing-futures-2026.html',
    'afl-round-8-tips-2026.html',
]

# Also catch all match stub pages (afl-*/nrl-* round pages)
for f in os.listdir(ROOT):
    if not f.endswith('.html'):
        continue
    if re.match(r'(afl|nrl)-.+round-[89]', f) and f not in GENERIC_PAGES:
        GENERIC_PAGES.append(f)

GENERIC_PAGES = list(set(GENERIC_PAGES))

for page in GENERIC_PAGES:
    fpath = os.path.join(ROOT, page)
    if not os.path.exists(fpath):
        continue
    html = open(fpath, encoding='utf-8').read()
    original = html

    # Replace plain href="#" onclick="return false;" with best-betting-sites
    html = re.sub(
        r'href="#"\s*onclick="return false;"',
        f'href="{BEST}" target="_blank" rel="noopener"',
        html
    )

    buttons_fixed = original.count('href="#"') - html.count('href="#"')
    if html != original:
        open(fpath, 'w', encoding='utf-8').write(html)
        updated_files += 1
        updated_buttons += buttons_fixed
        print(f'  {page} — {buttons_fixed} generic buttons → best-betting-sites-australia')

# ─── Summary ─────────────────────────────────────────────────────────────────
print(f'\nTotal: {updated_files} files, {updated_buttons} buttons updated.')

# Report any remaining href="#" outside review pages
remaining = []
for f in os.listdir(ROOT):
    if not f.endswith('.html') or f.startswith('review-'):
        continue
    html = open(os.path.join(ROOT, f), encoding='utf-8').read()
    count = html.count('href="#"')
    if count > 0:
        remaining.append((count, f))

if remaining:
    remaining.sort(reverse=True)
    print(f'\nStill has href="#" (may need manual check):')
    for count, f in remaining[:20]:
        print(f'  {count:3d}  {f}')
