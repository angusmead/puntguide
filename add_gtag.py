#!/usr/bin/env python3
"""Add Google Analytics tag to all HTML pages immediately after <head>."""
import os

GTAG = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-X8HMP35PY6"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-X8HMP35PY6');
</script>"""

pages = [f for f in os.listdir('.') if f.endswith('.html')]
added = 0
skipped = 0

for fn in pages:
    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()
    if 'G-X8HMP35PY6' in html:
        skipped += 1
        continue
    html = html.replace('<head>', '<head>\n' + GTAG, 1)
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(html)
    added += 1

print(f"Added: {added} pages")
print(f"Already had tag: {skipped} pages")
print(f"Total: {added + skipped}")
