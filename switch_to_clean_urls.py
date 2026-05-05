"""
switch_to_clean_urls.py
Changes all canonical and og:url tags from .html to clean URLs sitewide.

Before: https://puntguide.com.au/best-betting-sites-australia.html
After:  https://puntguide.com.au/best-betting-sites-australia

Special case: index.html → https://puntguide.com.au/ (not /index)
Also updates sitemap.xml to use clean URLs.
"""

import os, re

SITE = 'https://puntguide.com.au'
ROOT = os.path.dirname(os.path.abspath(__file__))

def clean_url(url):
    # index.html → homepage
    url = url.replace(f'{SITE}/index.html', f'{SITE}/')
    # everything else: strip .html
    url = re.sub(r'\.html(?=["\s]|$)', '', url)
    return url

updated_html = 0
updated_sitemap = 0

# --- HTML files ---
for fname in os.listdir(ROOT):
    if not fname.endswith('.html'):
        continue
    path = os.path.join(ROOT, fname)
    try:
        html = open(path, encoding='utf-8').read()
    except Exception:
        continue

    original = html

    # Canonical tag
    html = re.sub(
        r'(<link\s+rel="canonical"\s+href=")([^"]+\.html)(")',
        lambda m: m.group(1) + clean_url(m.group(2)) + m.group(3),
        html
    )

    # og:url
    html = re.sub(
        r'(<meta\s+property="og:url"\s+content=")([^"]+\.html)(")',
        lambda m: m.group(1) + clean_url(m.group(2)) + m.group(3),
        html
    )

    if html != original:
        open(path, 'w', encoding='utf-8').write(html)
        updated_html += 1

print(f'HTML pages updated: {updated_html}')

# --- sitemap.xml ---
sitemap_path = os.path.join(ROOT, 'sitemap.xml')
if os.path.exists(sitemap_path):
    sitemap = open(sitemap_path, encoding='utf-8').read()
    original = sitemap

    sitemap = re.sub(
        r'(https://puntguide\.com\.au/[^<]+)\.html',
        lambda m: m.group(0).replace('.html', '') if '/index.html' not in m.group(0) else m.group(0).replace('index.html', ''),
        sitemap
    )
    # Fix index.html → trailing slash
    sitemap = sitemap.replace(f'{SITE}/index', f'{SITE}/')

    if sitemap != original:
        open(sitemap_path, 'w', encoding='utf-8').write(sitemap)
        updated_sitemap = 1
        print('sitemap.xml updated')
    else:
        print('sitemap.xml — no changes needed')

print(f'\nDone. {updated_html} pages updated.')
print('Next: git add -A && git push, then resubmit sitemap.xml in Google Search Console.')
