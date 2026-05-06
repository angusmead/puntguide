"""
update_homepages.py
Updates data/affiliate_links.json with correct homepage URLs,
then applies them to all review page CTA buttons.
Run once. When affiliate codes arrive, apply_affiliate_links.py takes over.
"""

import json, re, os

ROOT = os.path.dirname(os.path.abspath(__file__))

# Verified homepage URLs from user — slug: full URL
URL_MAP = {
    'sportsbet':     'https://www.sportsbet.com.au',
    'pointsbet':     'https://www.pointsbet.com.au',
    'betr':          'https://www.betr.com.au',
    'nextbet':       'https://www.nextbet.com.au',
    'draftstars':    'https://www.draftstars.com.au',
    'neds':          'https://www.neds.com.au',
    'bet365':        'https://www.bet365.com.au',
    'picklebet':     'https://www.picklebet.com.au',
    'dabble':        'https://www.dabble.com.au',
    'ladbrokes':     'https://www.ladbrokes.com.au',
    'betright':      'https://www.betright.com.au',
    'betdeluxe':     'https://www.betdeluxe.com.au',
    'puntnow':       'https://www.puntnow.com.au',
    'puntzone':      'https://www.puntzone.com.au',
    'betnation':     'https://www.betnation.com.au',
    'surge':         'https://www.surge.com.au',
    'noisy':         'https://www.noisy.com.au',
    'pulsebet':      'https://www.pulsebet.com.au',
    'bigbet':        'https://www.bigbet.com.au',
    'mightybet':     'https://www.mightybet.com.au',
    'yesbet':        'https://www.yesbet.com.au',
    'betexpress':    'https://www.betexpress.com.au',
    'betjet':        'https://www.betjet.com.au',
    'betzooka':      'https://www.betzooka.com.au',
    'betreal':       'https://www.betreal.com.au',
    'tradiebet':     'https://tradie.bet',
    'upyago':        'https://www.upyago.com.au',
    'next2go':       'https://www.next2go.com.au',
    'teambet':       'https://www.teambet.com.au',
    'milennialbet':  'https://www.millenialbet.com.au',
    'betvista':      'https://www.betvista.com.au',
    'puntx':         'https://www.puntx.com.au',
    'betblitz':      'https://www.betblitz.com.au',
    'unibet':        'https://www.unibet.com.au',
    'blondebet':     'https://www.blondebet.com.au',
    'betestate':     'https://www.betestate.com.au',
    'betsupreme':    'https://www.betsupreme.com.au',
    'ausbet':        'https://www.betaus.com.au',
    'marantellibet': 'https://www.marantellibet.com.au',
    'terrybet':      'https://www.terrybet.com.au',
    'topbet':        'https://topbet.au',
    'wizbet':        'https://www.wizbet.com.au',
    'betyoucan':     'https://betyoucan.au',
    'dowbet':        'https://www.dowbet.com.au',
    'betchamps':     'https://www.betchamps.com.au',
    'mintbet':       'https://mintbet.au',
    'betdragon':     'https://betdragon.au',
    'ripperbet':     'https://ripperbet.au',
    'betbuzz':       'https://betbuzz.au',
    'betalpha':      'https://betalpha.au',
    'readybet':      'https://www.readybet.com.au',
    'betfair':       'https://www.betfair.com.au',
    'betlocal':      'https://www.betlocal.com.au',
    'baggybet':      'https://www.baggybet.com.au',
    'lightningbet':  'https://www.lightningbet.com.au',
    'punt123':       'https://punt123.bet',
    'upcoz':         'https://www.upcoz.com',
    'epicodds':      'https://www.epicodds.com.au',
    'realbookie':    'https://www.realbookie.com.au',
    'betnova':       'https://www.betnova.com.au',
    'ninjabet':      'https://www.ninjabet.com.au',
    'dashbet':       'https://www.dashbet.com.au',
    'pandabet':      'https://www.pandabet.com.au',
    'justbet':       'https://www.justbet.com.au',
    'winnersbet':    'https://www.winnersbet.com.au',
    'midasbet':      'https://www.midasbet.com.au',
    'swiftbet':      'https://www.swiftbet.com.au',
    'palmerbet':     'https://www.palmerbet.com',
    'chasebet':      'https://www.chasebet.com.au',
    'elitebet':      'https://www.elitebet.com.au',
    'vicbet':        'https://www.vicbet.com.au',
    'robwaterhouse': 'https://www.robwaterhouse.com.au',
    'picnicbet':     'https://www.picnicbet.com',
    'okebet':        'https://www.okebet.com.au',
    'tab':           'https://www.tab.com.au',
    'tabtouch':      'https://www.tabtouch.com.au',
    'betgold':       'https://www.betgold.com.au',
    'bossbet':       'https://www.bossbet.com.au',
    'wishbet':       'https://www.wishbet.com.au',
    'mybet':         'https://www.mybet.com.au',
    'playwest':      'https://www.playwestbet.com',
    'truebet':       'https://www.truebet.com.au',
    'starsports':    'https://www.starsports.com.au',
    'ponybet':       'https://www.ponybet.com.au',
    'allbets':       'https://www.allbets.com.au',
    'betdash':       'https://www.betdash.com.au',
    'betlegends':    'https://www.betlegends.com.au',
    'betit':         'https://www.betit.com.au',
    'stablebet':     'https://www.stablebet.com.au',
    'betshop':       'https://www.betshop.com.au',
    'knucklebet':    'https://www.knucklebet.com.au',
    'earlycrow':     'https://earlycrow.bet',
    'crownbet':      'https://www.crownbet.com.au',
    'xcelbet':       'https://www.xcelbet.com.au',
    'fatbet':        'https://www.fatbet.com.au',
    'ballrbet':      'https://www.ballrbet.com.au',
    'betfocus':      'https://www.betfocus.com.au',
    'xbet':          'https://xbet.net.au',
    'premiumbet':    'https://www.premiumbet.com.au',
    'goldenbet':     'https://www.goldenbet888.com.au',
    'titanbet':      'https://www.titanbet.com.au',
    'chromabet':     'https://www.chromabet.com.au',
    'bet777':        'https://www.bet777.com.au',
    'templebet':     'https://www.templebet.com.au',
    'juicybet':      'https://www.juicybet.com.au',
    'betprofessor':  'https://www.betprofessor.com.au',
    'wellbet':       'https://www.wellbet.com.au',
    'questbet':      'https://www.questbet.com.au',
    'betgalaxy':     'https://www.betgalaxy.com.au',
    'betbetbet':     'https://www.betbetbet.net.au',
    'letsbet':       'https://www.letsbet.net.au',
    'havabet':       'https://www.havabet.com.au',
    'colossalbet':   'https://www.colossalbet.com.au',
    '123bet':        'https://www.123bet.com.au',
    'betmax':        'https://www.betmax.com.au',
    'jimmybet':      'https://www.jimmybet.com.au',
    'goldbet':       'https://www.goldbet.com.au',
    'ultrabet':      'https://www.ultrabet.com.au',
    'betkings':      'https://www.betkings.com.au',
    'hotbet':        'https://www.hotbet.com.au',
    'boostbet':      'https://www.boostbet.com.au',
    'grsbet':        'https://www.grsbet.com.au',
    'favbet':        'https://www.favbet.com.au',
    'bearbet':       'https://www.bearbet.com.au',
    'cashcage':      'https://www.cashcage.com.au',
    'multis':        'https://www.multis.com.au',
    'betbox':        'https://www.betbox.com.au',
    'laserbet':      'https://www.laserbet.com.au',
    'puntsport':     'https://www.puntsport.com.au',
    # Coming soon
    'riverbet':      'https://www.riverbet.com.au',
    'dafabet':       'https://www.dafabet.com.au',
    'clubbet':       'https://clubbet.au',
    'gembet':        'https://www.gembet.com.au',
    'betbunker':     'https://www.betbunker.com.au',
}

# --- Step 1: Update affiliate_links.json ---
data_path = os.path.join(ROOT, 'data', 'affiliate_links.json')
data = json.loads(open(data_path, encoding='utf-8').read())

json_updated = 0
for slug, url in URL_MAP.items():
    if slug in data:
        data[slug]['homepage'] = url
        json_updated += 1
    else:
        # Add new entry for coming-soon bookmakers not yet in JSON
        data[slug] = {
            'name': slug.capitalize(),
            'homepage': url,
            'affiliate_url': '',
            'network': 'Unknown',
            'cf_advertiser_id': '',
            'status': 'coming_soon' if slug in ('riverbet','dafabet','clubbet','gembet','betbunker') else 'pending',
            'priority': 5,
            'notes': 'Coming soon' if slug in ('riverbet','dafabet','clubbet','gembet','betbunker') else ''
        }
        json_updated += 1

open(data_path, 'w', encoding='utf-8').write(
    json.dumps(data, indent=2, ensure_ascii=False)
)
print(f'JSON updated: {json_updated} bookmakers')

# --- Step 2: Apply homepage URLs to review page CTAs ---
pages_updated = 0
ctas_updated = 0

for slug, url in URL_MAP.items():
    # Skip coming-soon bookmakers — no review pages for those yet
    if slug in ('riverbet', 'dafabet', 'clubbet', 'gembet', 'betbunker'):
        continue

    page = os.path.join(ROOT, f'review-{slug}.html')
    if not os.path.exists(page):
        print(f'  MISSING  review-{slug}.html')
        continue

    html = open(page, encoding='utf-8').read()
    original = html
    count_before = html.count('href="#"')

    # Replace href="#" onclick="return false;" patterns
    html = re.sub(r'href="#"\s*onclick="return false;"', f'href="{url}" target="_blank" rel="noopener"', html)
    # Replace plain href="#" on CTA buttons
    html = re.sub(r'(<a\b[^>]*\bclass="[^"]*\bbtn-g\b[^"]*"[^>]*)href="#"', f'\\1href="{url}" target="_blank" rel="noopener"', html)

    count_after = html.count('href="#"')
    replaced = count_before - count_after

    if html != original:
        open(page, 'w', encoding='utf-8').write(html)
        pages_updated += 1
        ctas_updated += replaced

print(f'Review pages updated: {pages_updated}')
print(f'CTA buttons updated:  {ctas_updated}')
print('\nDone. All review pages now link to real bookmaker homepages.')
print('When affiliate codes arrive, run apply_affiliate_links.py to swap to tracking URLs.')
