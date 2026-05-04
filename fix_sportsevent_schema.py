#!/usr/bin/env python3
"""
Fix SportsEvent schema on all match prediction pages.
Adds missing fields flagged by Google Search Console:
  eventStatus, performer, offers, endDate, image
"""
import os, re, json
from datetime import datetime, timedelta, timezone

BASE = "https://puntguide.com.au"
LOGO = f"{BASE}/puntguide-logo.png"
AEST = timezone(timedelta(hours=10))

pages = [f for f in os.listdir('.')
         if f.endswith('.html') and
         re.match(r'(afl|nrl)-.+-vs-.+-(round|opening)', f)]

fixed = 0
skipped = 0

for fn in pages:
    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the SportsEvent schema block
    pattern = r'(<script type="application/ld\+json">)(.*?)(</script>)'
    matches = list(re.finditer(pattern, html, re.DOTALL))

    changed = False
    for m in matches:
        try:
            data = json.loads(m.group(2))
        except json.JSONDecodeError:
            continue

        if data.get('@type') != 'SportsEvent':
            continue

        # Only fix if missing fields
        if all(k in data for k in ('eventStatus', 'performer', 'offers', 'endDate', 'image')):
            skipped += 1
            break

        # 1. eventStatus
        data['eventStatus'] = 'https://schema.org/EventScheduled'

        # 2. image
        data['image'] = LOGO

        # 3. performer — reuse competitor array
        if 'competitor' in data:
            data['performer'] = data['competitor']

        # 4. endDate — startDate + 2h30m AFL / 2h NRL
        if 'startDate' in data and 'endDate' not in data:
            try:
                start_str = data['startDate']
                # Parse ISO datetime
                dt = datetime.fromisoformat(start_str)
                duration = timedelta(hours=2, minutes=30) if 'AFL' in data.get('sport','') else timedelta(hours=2)
                end_dt = dt + duration
                data['endDate'] = end_dt.isoformat()
            except Exception:
                pass

        # 5. offers — generic betting offer pointing to the page
        slug = fn
        data['offers'] = {
            "@type": "Offer",
            "name": f"Betting odds — {data.get('name', '')}",
            "url": f"{BASE}/{slug}",
            "priceCurrency": "AUD",
            "availability": "https://schema.org/InStock",
            "seller": {"@type": "Organization", "name": "PuntGuide"}
        }

        new_json = json.dumps(data, ensure_ascii=False)
        new_block = m.group(1) + new_json + m.group(3)
        html = html[:m.start()] + new_block + html[m.end():]
        changed = True
        break

    if changed:
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(html)
        fixed += 1

print(f"Fixed: {fixed} pages")
print(f"Skipped (already complete): {skipped} pages")
print(f"Total match pages: {len(pages)}")
