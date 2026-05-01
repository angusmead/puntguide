#!/usr/bin/env python3
"""PuntGuide SEO Page Generator — builds all programmatic SEO pages."""
import os, json
from itertools import combinations

OUT  = os.path.expanduser('~/puntguide')
SITE = 'https://puntguide.com.au'
DATE = '2026-05-01'

# ─── BOOKMAKER DATA ──────────────────────────────────────────────────────────

BMS = [
    dict(name='PointsBet', slug='pointsbet', logo='pointsbet.png', rating=5.0,
         type='Sports & Racing', est=2017, colour='#003087', licence='ACT Racing',
         withdraw='Same day (PayID)', min_dep='$10',
         tagline="Australia's most innovative sportsbook — sharp odds and unique PointsBetting markets.",
         best_for='Sports punters wanting unique markets and the sharpest odds',
         not_for='Casual punters who prefer simple fixed-odds only',
         desc='PointsBet is an Australian-founded bookmaker that changed the market with PointsBetting — a spread-style format where winnings and losses scale with how correct you are. It also offers sharp fixed odds across AFL, NRL, racing, and international sports.',
         pros=['Unique PointsBetting spread markets','Sharp AFL and NRL fixed odds','Racing futures — Melbourne Cup, Cox Plate','Best-in-class same-game multi builder','Fast PayID withdrawals'],
         cons=['PointsBetting amplifies losses as well as wins','Platform complexity can overwhelm beginners','Racing market depth behind dedicated books'],
         features=['PointsBetting','Live In-Play','Racing Futures','SGM Builder','Cash Out','PayID'],
         faqs=[('What is PointsBetting?','PointsBetting is a spread-style betting format unique to PointsBet. Your winnings and losses scale with how correct you are — if you back a team to win by 10 and they win by 15, you win more than a fixed-odds bet. If they win by 5, you win less.'),
               ('Is PointsBet available in all Australian states?','Yes. PointsBet holds an Australian Capital Territory racing and wagering licence and is available to customers in all Australian states and territories.'),
               ('How fast are PointsBet withdrawals?','PointsBet supports PayID withdrawals, which typically process in under two hours. Bank transfer withdrawals take 1–2 business days.'),
               ('Does PointsBet restrict winning accounts?','PointsBet has a better reputation than some competitors for account treatment, though like all bookmakers it reserves the right to limit or close accounts at its discretion.'),
               ('What sports can I bet on at PointsBet?','PointsBet covers AFL, NRL, cricket, soccer, tennis, basketball, rugby union, horse racing, greyhounds, and a wide range of international sports including NFL, NBA, and EPL.')]),

    dict(name='Sportsbet', slug='sportsbet', logo='sportsbet.png', rating=4.8,
         type='Sports & Racing', est=1993, colour='#e8523a', licence='NT Racing',
         withdraw='1–2 business days', min_dep='$10',
         tagline="Australia's biggest bookmaker — widest market range and fastest tap-to-bet experience.",
         best_for='Punters who want the widest market selection and a polished app',
         not_for='Sharp punters — Sportsbet limits winning accounts more aggressively than others',
         desc="Sportsbet is Australia's largest bookmaker by market share, owned by Flutter Entertainment — the same global group behind Betfair and Paddy Power. It offers the widest range of betting markets of any Australian operator.",
         pros=['Widest market range of any Australian bookmaker','Speedy Bet — fastest mobile betting tested','Excellent SGM builder with market-leading depth','Strong live in-play coverage','Regular promotions for existing customers'],
         cons=['Known for limiting or closing winning accounts','Odds not always sharpest on head-to-head','Racing tote options behind specialist books'],
         features=['Speedy Bet','Live In-Play','SGM Builder','Same-Day Payouts','Cash Out','Tote Betting'],
         faqs=[('Is Sportsbet the biggest bookmaker in Australia?','Yes. Sportsbet is the largest Australian bookmaker by market share. It is owned by Flutter Entertainment, which also owns Betfair, Paddy Power, and FanDuel.'),
               ('Does Sportsbet restrict winning accounts?','Sportsbet has a reputation for limiting accounts that win consistently. If you are a sharp punter, you may find your maximum stake reduced after a period of winning.'),
               ('What is Speedy Bet?','Speedy Bet is Sportsbet\'s one-tap betting feature for mobile. It lets you place a pre-set stake on any market with a single tap, without confirmation screens.'),
               ('Does Sportsbet have racing?','Yes. Sportsbet covers Australian and international horse racing and greyhound racing extensively. It offers both fixed odds and tote products.'),
               ('How do I withdraw from Sportsbet?','Sportsbet supports bank transfer and PayID withdrawals. PayID is typically the fastest option, though Sportsbet\'s processing times are generally 1–2 business days.')]),

    dict(name='Ladbrokes', slug='ladbrokes', logo='ladbrokes.png', rating=4.7,
         type='Sports & Racing', est=1886, colour='#cc0000', licence='NT Racing',
         withdraw='1–3 business days', min_dep='$10',
         tagline='Global odds muscle with strong local racing — consistently competitive head-to-head prices.',
         best_for='Punters focused on the best head-to-head odds on AFL and NRL',
         not_for='Punters who want a cutting-edge app or modern UX',
         desc="Ladbrokes is one of the world's oldest and most recognised bookmakers, now owned by Entain. It brings global scale and pricing power to Australian markets, with a particularly strong reputation for competitive head-to-head AFL and NRL odds.",
         pros=['Consistently competitive head-to-head AFL and NRL odds','Strong racing tote access and Best Tote options','Global liquidity benefits Australian pricing','Long-established reputation and financial stability','Good range of international sports'],
         cons=['App experience behind newer competitors','SGM builder less polished than Sportsbet or betr','Customer service can be slow'],
         features=['Best Tote','Live In-Play','Cash Out','Multi Builder','PayID','International Markets'],
         faqs=[('Is Ladbrokes available in Australia?','Yes. Ladbrokes is fully licensed in Australia through a Northern Territory racing licence and is available to customers in all Australian states and territories.'),
               ('How do Ladbrokes odds compare?','Ladbrokes is consistently rated among the top Australian bookmakers for head-to-head AFL and NRL odds. Its global scale gives it pricing power that smaller local operators can\'t match.'),
               ('Does Ladbrokes have Best Tote?','Yes. Ladbrokes offers Best Tote on Australian thoroughbred racing, meaning you receive the best of three tote dividends — the NSW, VIC, or QLD pools.'),
               ('What is the Ladbrokes app like?','The Ladbrokes app is functional and reliable but is generally considered less polished than newer competitors like betr or Dabble. It covers all markets and has cash out functionality.'),
               ('Does Ladbrokes restrict accounts?','Like most corporate bookmakers, Ladbrokes limits winning accounts. The Neds brand (also owned by Entain) operates independently but has similar policies.')]),

    dict(name='BetRight', slug='betright', logo='betright.png', rating=5.0,
         type='Racing Specialist', est=2018, colour='#00a651', licence='NT Racing',
         withdraw='Same day', min_dep='$10',
         tagline="The racing punter's weapon — Best Tote, same race multis, and same-day payouts.",
         best_for='Racing-first punters who need depth, tote options, and fast withdrawals',
         not_for='Casual bettors wanting a simple all-in-one sports and racing platform',
         desc='BetRight is a racing-specialist Australian bookmaker that consistently outperforms the field on withdrawal speed, racing market depth, and tote access. It has built a loyal following among serious racing punters.',
         pros=['Best Tote guaranteed on metropolitan meetings','Same Race Multi — market-leading for racing','Fastest withdrawal speeds tested — consistently same day','Detailed form guide integration','Strong racing futures markets'],
         cons=['Sports market depth behind Sportsbet and PointsBet','Interface more functional than polished','Smaller promotions program than major competitors'],
         features=['Best Tote','Same Race Multi','Same-Day Payouts','Form Guide','Racing Futures','PayID'],
         faqs=[('Is BetRight good for horse racing?','BetRight is widely considered the best Australian bookmaker for horse racing. It offers Best Tote on metro meetings, a market-leading Same Race Multi builder, detailed form guide integration, and the fastest withdrawal speeds of any operator we tested.'),
               ('How fast are BetRight withdrawals?','BetRight consistently processes PayID withdrawals on the same business day — often within hours. This makes it the fastest payout bookmaker in Australia for racing punters.'),
               ('What is Same Race Multi?','Same Race Multi lets you combine multiple selections within a single race into a multi-leg bet. BetRight\'s SRM builder is rated the best in Australia, with more exotic combinations and better pricing than competitors.'),
               ('Does BetRight offer sports betting?','Yes, though racing is clearly the main focus. BetRight covers AFL, NRL, cricket, soccer, and other sports, but the market depth for sports is behind Sportsbet or PointsBet.'),
               ('Is BetRight licensed in Australia?','Yes. BetRight holds a Northern Territory racing licence and is fully regulated by the NT Racing Commission.')]),

    dict(name='Dabble', slug='dabble', logo='dabble.png', rating=5.0,
         type='Social Betting', est=2021, colour='#7c3aed', licence='NT Racing',
         withdraw='Same day (PayID)', min_dep='$10',
         tagline='The social betting experience Australian punters have been waiting for.',
         best_for='Punters who want to follow sharp bettors, copy bets, and use the best app in Australia',
         not_for='Racing-first punters — sports is clearly the main focus',
         desc='Dabble is a uniquely Australian social betting platform that lets you follow other punters, see their bets in a live feed, and copy their selections. It combines a genuinely innovative product with solid AFL, NRL, and racing coverage.',
         pros=["Social feed — follow and copy other punters in real time","Australia's highest-rated betting app UX","Fast PayID withdrawals","Strong AFL and NRL market coverage","Genuinely innovative product that stands apart"],
         cons=['Racing coverage not as deep as BetRight or Ladbrokes','Smaller market range than Sportsbet','Social features can distract from considered betting'],
         features=['Social Feed','Copy Betting','PayID Withdrawals','SGM Builder','Live In-Play','AFL & NRL Markets'],
         faqs=[('What makes Dabble different?',"Dabble's social feed is genuinely unique in Australia. You can follow other punters, see their bets as they place them, and copy their selections with one tap. No other Australian bookmaker offers this."),
               ('Is the Dabble app good?','Dabble has consistently rated as Australia\'s best betting app for user experience. The interface is clean, fast, and built around mobile-first design.'),
               ('Is Dabble good for horse racing?','Dabble covers racing but is not a racing specialist. For serious racing punters, BetRight is a better choice. Dabble excels at AFL and NRL betting.'),
               ('How do I copy a bet on Dabble?','On the Dabble social feed, tap any punter\'s bet to see the full details. Then tap "Copy Bet" to add it to your bet slip with your chosen stake.'),
               ('Is Dabble licensed in Australia?','Yes. Dabble holds a Northern Territory racing and wagering licence and is available to customers in all Australian states and territories.')]),

    dict(name='Neds', slug='neds', logo='neds.png', rating=4.5,
         type='Sports & Racing', est=2018, colour='#1a1a2e', licence='NT Racing',
         withdraw='1–2 business days', min_dep='$10',
         tagline='A modern Australian bookmaker with competitive odds and a clean, user-friendly platform.',
         best_for='Punters who want a clean interface, competitive odds, and a strong multi builder',
         not_for='Sharp punters — Neds limits accounts similarly to Ladbrokes',
         desc='Neds is an Australian bookmaker launched in 2018, owned by Entain (the same group as Ladbrokes). It offers a cleaner, more modern interface than its parent brand with competitive odds across AFL, NRL, racing, and international sports.',
         pros=['Clean, modern interface on mobile and desktop','Competitive odds on AFL and NRL head-to-head','Strong multi builder with good SGM options','PayID support for fast withdrawals','Good racing coverage for a non-specialist'],
         cons=['Account limiting for consistent winners','Market depth behind Sportsbet','Promotions less generous than major competitors'],
         features=['Multi Builder','Live In-Play','Cash Out','PayID','SGM Builder','Racing Markets'],
         faqs=[('Is Neds owned by Ladbrokes?','Yes. Neds is owned by Entain — the same global group that owns Ladbrokes in Australia. The two brands operate independently with separate accounts and promotions, but share back-end infrastructure.'),
               ('Does Neds have good odds?','Neds has competitive head-to-head odds on AFL and NRL and generally tracks closely with Ladbrokes on pricing. For best-odds hunting, compare Neds alongside Ladbrokes and PointsBet.'),
               ('Does Neds restrict winning accounts?','Yes. Neds, like Ladbrokes and Sportsbet, is known for limiting accounts that win consistently. If you are a profitable punter, your maximum stakes may be reduced over time.'),
               ('What is the Neds app like?','The Neds app is clean and modern, widely rated better than the Ladbrokes app for UX. It covers all markets including live betting and multi building.'),
               ('Can I use PayID on Neds?','Yes. Neds supports PayID deposits and withdrawals. Deposits are instant. Withdrawals typically process within 1–2 business days.')]),

    dict(name='Bet365', slug='bet365', logo='bet365.png', rating=4.6,
         type='Sports & Racing', est=1974, colour='#028B02', licence='NT Racing',
         withdraw='1–3 business days', min_dep='$10',
         tagline="World's largest bookmaker — unmatched international sports coverage and live streaming.",
         best_for='Punters who bet heavily on international sports and want live streaming',
         not_for='Australian racing-first punters — local tote options are limited',
         desc="Bet365 is the world's largest online bookmaker. It offers unrivalled international sports coverage and live streaming, making it the top choice for punters who bet beyond Australian sports.",
         pros=['Unmatched international sports market coverage','Live streaming on hundreds of events per day','Competitive odds on soccer, tennis, cricket','Cash out on virtually all markets','World-class mobile app'],
         cons=['Australian racing depth behind local specialists','Limited local tote access','Account restrictions for winning punters'],
         features=['Live Streaming','Cash Out','In-Play Betting','International Markets','Multi Builder','Edit Bet'],
         faqs=[('Is Bet365 available in Australia?','Yes. Bet365 holds a Northern Territory racing licence and is fully available to Australian customers. It is one of the most popular bookmakers in Australia due to its international sports coverage.'),
               ('Does Bet365 have live streaming?','Yes. Bet365 is the best bookmaker in Australia for live streaming. It streams hundreds of sporting events per day including soccer, tennis, basketball, cricket, and racing.'),
               ('Is Bet365 good for Australian racing?','Bet365 covers Australian horse racing and greyhounds but is not a specialist. The racing market depth and tote options are behind BetRight, Ladbrokes, and Tab for serious racing punters.'),
               ('What international sports does Bet365 cover?','Bet365 covers virtually every international sport including EPL, Champions League, La Liga, NBA, NFL, MLB, Grand Slam tennis, cricket internationals, and hundreds of other competitions.'),
               ('Does Bet365 offer cash out?','Yes. Bet365 has one of the best cash out products of any bookmaker in Australia, with cash out available on singles, multis, and in-play bets across most sports and racing markets.')]),

    dict(name='betr', slug='betr', logo='betr.png', rating=4.7,
         type='Sports Focus', est=2022, colour='#0ea5e9', licence='NT Racing',
         withdraw='Same day', min_dep='$10',
         tagline="Australia's fastest-growing bookmaker — built from the ground up for same-game multis.",
         best_for='Sports bettors who love same-game multis, micro-betting, and a modern app',
         not_for='Racing-first punters — sports is clearly the main priority',
         desc="betr is Australia's fastest-growing bookmaker, launched in 2022 with a focus on same-game multis and micro-betting. It was founded by Australian media personalities and has quickly built a loyal following.",
         pros=['Best-in-class SGM builder for AFL and NRL','Micro-betting markets unavailable elsewhere','Clean, fast, modern mobile app','Strong live in-play product','Rapid product improvement cycle'],
         cons=['Racing market depth limited vs BetRight or Ladbrokes','Newer platform means less track record','Market range smaller than Sportsbet'],
         features=['SGM Builder','Micro-Betting','Live In-Play','Same-Day Payouts','Modern App','AFL & NRL Focus'],
         faqs=[('When did betr launch?','betr launched in Australia in 2022. It was founded by Australian media and sporting personalities and has grown rapidly to become one of the most-downloaded sports betting apps in the country.'),
               ('What is micro-betting?','Micro-betting lets you bet on real-time in-game events — such as the next scoring play in AFL, or the next point in tennis. betr offers micro-betting markets that are not available at other Australian bookmakers.'),
               ('Is betr good for AFL betting?','Yes. betr is widely considered one of the best Australian bookmakers for AFL betting, particularly for same-game multis. Its SGM builder for AFL is rated alongside Sportsbet and PointsBet as market-leading.'),
               ('Does betr have horse racing?','betr covers horse racing, though it is not a racing specialist. For serious racing punters, BetRight or Ladbrokes offer more depth and better tote options.'),
               ('How do I withdraw from betr?','betr supports PayID withdrawals, which typically process on the same business day. Bank transfer withdrawals may take longer.')]),

    dict(name='Picklebet', slug='picklebet', logo='picklebet.png', rating=4.5,
         type='Esports & Sports', est=2022, colour='#84cc16', licence='NT Racing',
         withdraw='Same day', min_dep='$10',
         tagline="Australia's best esports betting platform with strong mainstream sports coverage.",
         best_for='Esports fans and modern bettors wanting a fresh, innovative platform',
         not_for='Traditional racing punters — racing coverage is limited',
         desc="Picklebet is a modern Australian bookmaker specialising in esports and sports betting. It offers the most comprehensive esports betting markets of any Australian licensed operator.",
         pros=["Australia's leading esports betting market coverage",'Modern platform with strong UX','Good AFL and NRL market coverage','Fast growing with regular product updates','Appeals to younger, digitally-native bettors'],
         cons=['Racing coverage limited vs specialists','Smaller market range than Sportsbet or Bet365','Newer brand with shorter track record'],
         features=['Esports Betting','AFL & NRL Markets','Live In-Play','SGM Builder','Modern App','Fast Payouts'],
         faqs=[('What esports does Picklebet cover?','Picklebet covers League of Legends, CS2 (formerly CS:GO), Dota 2, Valorant, Rocket League, and other major esports titles. It offers the most comprehensive esports markets of any licensed Australian bookmaker.'),
               ('Is Picklebet good for AFL betting?','Yes. Picklebet covers AFL with a solid range of markets including head-to-head, line, total points, and same-game multis. It is not as deep as Sportsbet, but is a quality option.'),
               ('Is Picklebet licensed in Australia?','Yes. Picklebet holds a Northern Territory racing and wagering licence and is available to Australian customers.'),
               ('Does Picklebet have horse racing?','Picklebet covers horse racing, though it is not a specialist. For serious racing punters, BetRight or Ladbrokes are better choices.'),
               ('What makes Picklebet different?',"Picklebet's focus on esports sets it apart from every other Australian bookmaker. If you bet on gaming tournaments, Picklebet is the clear choice in Australia.")]),

    dict(name='Unibet', slug='unibet', logo='unibet.png', rating=4.3,
         type='Sports & Racing', est=1997, colour='#007AB8', licence='NT Racing',
         withdraw='1–3 business days', min_dep='$10',
         tagline='European powerhouse with strong international markets and a reliable, trusted platform.',
         best_for='Punters who want a globally trusted brand with strong international sports coverage',
         not_for='Australian racing specialists — local tote depth is limited',
         desc='Unibet is a major European bookmaker with a strong presence in Australia. Owned by Kindred Group, it has been operating since 1997 and brings global scale and reliability to the Australian market.',
         pros=['Global brand with long track record','Strong international sports coverage','Competitive odds on soccer and tennis','Reliable, stable platform','Good cash out functionality'],
         cons=['Australian racing depth behind local specialists','App less polished than newer local competitors','Local market innovation behind betr and Dabble'],
         features=['International Markets','Cash Out','Live In-Play','Multi Builder','Soccer Markets','Reliable Platform'],
         faqs=[('Is Unibet good for soccer betting?','Yes. Unibet is one of the better Australian bookmakers for soccer. It covers the EPL, Champions League, La Liga, Serie A, and hundreds of other leagues with competitive odds.'),
               ('Is Unibet Australian?','No. Unibet is a Swedish bookmaker owned by Kindred Group. It holds an Australian NT Racing licence and operates locally in Australia.'),
               ('Is Unibet good for horse racing?','Unibet covers Australian racing, but the depth and tote options are behind local specialists like BetRight and Ladbrokes. It is a solid secondary account for racing punters.'),
               ('Does Unibet limit winning accounts?','Unibet has a reasonable reputation for account treatment compared to larger corporate bookmakers. Account management policies can vary.'),
               ('How do I contact Unibet support?','Unibet offers live chat, email, and phone support for Australian customers. Live chat is available on the Unibet website and mobile app.')]),

    dict(name='Palmerbet', slug='palmerbet', logo='palmerbet.png', rating=4.2,
         type='Sports & Racing', est=1998, colour='#1e3a8a', licence='Racing NSW',
         withdraw='1–2 business days', min_dep='$10',
         tagline="Family-owned Australian bookmaker with a reputation for fair account treatment.",
         best_for="Winning punters who need a bookmaker that won't restrict their account",
         not_for='Punters who want the most polished app or the widest market range',
         desc="Palmerbet is an Australian family-owned bookmaker with a strong reputation for treating winning punters fairly. Operating since 1998, it has built a loyal following among serious punters limited elsewhere.",
         pros=['Reputation for fair treatment of winning accounts','Family-owned genuine Australian business','Competitive racing odds and tote access','Strong NSW and QLD racing coverage','Trusted by professional punters'],
         cons=['App and website less polished than major competitors','Smaller market range than Sportsbet','Less brand recognition'],
         features=['Fair Account Treatment','Racing Markets','Tote Access','Live In-Play','Multi Builder','PayID'],
         faqs=[('Does Palmerbet restrict winning accounts?','Palmerbet has a significantly better reputation than the major corporate bookmakers for account treatment. Many winning punters use Palmerbet specifically because other bookmakers have limited their stakes.'),
               ('Is Palmerbet good for horse racing?','Yes. Palmerbet has strong racing coverage, particularly for NSW and QLD meetings. It is a good choice for racing punters who have been limited elsewhere.'),
               ('Is Palmerbet an Australian company?','Yes. Palmerbet is 100% Australian-owned and operated. It was founded in 1998 and remains family-owned — one of the few remaining independent Australian bookmakers.'),
               ('How do I open a Palmerbet account?','Visit palmerbet.com.au and click "Join Now". You will need to provide identification documents as required by Australian anti-money-laundering regulations.'),
               ('What licence does Palmerbet hold?','Palmerbet holds a NSW bookmaker\'s licence issued by Racing NSW, making it one of the few Australian bookmakers licensed at state level rather than via the NT.')]),

    dict(name='Tab', slug='tab', logo='tab.png', rating=4.1,
         type='Racing & Sports', est=1961, colour='#000080', licence='TABCORP',
         withdraw='1–3 business days', min_dep='$10',
         tagline="Australia's iconic tote operator — the deepest racing pools and retail presence.",
         best_for='Racing punters who want the deepest tote pools and exotic betting options',
         not_for='Sports-first punters wanting the widest fixed-odds market range',
         desc="TAB is Australia's most iconic racing and sports betting operator, originally established as a government tote agency in 1961. Now operating digitally and through retail outlets, it offers unrivalled tote pool depth.",
         pros=['The deepest tote pools in Australian racing','Long-established brand and trusted reputation','Both online and retail presence','Strong racing form guide integration','Multiple tote options including quadrellas'],
         cons=['Fixed-odds sports market range behind competitors','App less modern than Sportsbet or betr','Retail wait times can be frustrating'],
         features=['Tote Pools','Quadrella','Form Guide','Racing Futures','Fixed Odds','Retail Outlets'],
         faqs=[('Is TAB the best for horse racing totes?','TAB offers the deepest tote pools in Australia, which generally produces better dividends on exotic bets. For punters who bet quadrellas, trifectas, and first fours, TAB\'s pool depth is unmatched.'),
               ('Can I bet on sports with TAB?','Yes. TAB covers AFL, NRL, cricket, soccer, tennis, and other sports with fixed-odds markets. However, the sports market depth and odds are generally behind Sportsbet, Ladbrokes, and PointsBet.'),
               ('Is TAB available online?','Yes. TAB is available online at tab.com.au and via the TAB mobile app. It also has an extensive retail network through TAB outlets and pubs/clubs in NSW, VIC, and QLD.'),
               ('Does TAB offer live betting?','Yes. TAB offers live in-play betting via its digital channels. Australian law requires in-play bets to be placed digitally, not by phone.'),
               ('Does TAB restrict winning accounts?','TAB, operated by TABCORP, has different account management policies to the major corporate bookmakers. As a tote-focused operator, it is generally more tolerant of winning racing punters.')]),

    dict(name='Betfair', slug='betfair', logo='betfair.png', rating=4.4,
         type='Exchange & Sports', est=2000, colour='#FFB800', licence='NT Racing',
         withdraw='1–2 business days', min_dep='$10',
         tagline='The betting exchange — bet against other punters for better odds than any bookmaker.',
         best_for='Sharp punters who want better odds through exchange betting and lay betting',
         not_for='Recreational punters who want a simple set-and-forget experience',
         desc='Betfair operates a betting exchange — a marketplace where punters bet against each other rather than against a bookmaker. This typically results in better odds, though a commission is charged on net winnings.',
         pros=['Often better odds than traditional bookmakers','Ability to lay (bet against) outcomes','Accounts not restricted for winning','Large liquidity on major racing and sports','In-play exchange trading available'],
         cons=['Commission taken from winnings (typically 5%)','Complex interface not suitable for beginners','Liquidity can be thin on minor events'],
         features=['Exchange Betting','Lay Betting','In-Play Exchange','No Account Restriction','Sportsbook','Cash Out'],
         faqs=[('How does Betfair work?','Betfair is a betting exchange. Rather than betting against a bookmaker, you bet against other punters. This means the odds are set by the market and are often better than traditional bookmakers. A commission of around 5% is charged on net winnings.'),
               ('Does Betfair restrict winning accounts?','No. As an exchange, Betfair makes money from commission on all bets — winners and losers alike. It has no incentive to restrict winning accounts and is the preferred choice for professional punters.'),
               ('What is lay betting?','Lay betting means betting that something will NOT happen — for example, laying a horse to win, meaning you win if it loses. This is only possible on betting exchanges like Betfair.'),
               ('Is Betfair available in Australia?','Yes. Betfair holds a Northern Territory racing licence and offers both its exchange and a traditional sportsbook product to Australian customers.'),
               ('What commission does Betfair charge?','Betfair charges a market base rate of 5% on net winnings for most Australian customers. This rate can be reduced through a Premium Charge discount for high-volume bettors.')]),

    dict(name='Blondebet', slug='blondebet', logo='blondebet.png', rating=4.0,
         type='Sports & Racing', est=2015, colour='#f59e0b', licence='NT Racing',
         withdraw='1–2 business days', min_dep='$10',
         tagline='A reliable Australian bookmaker with competitive racing odds and fair account treatment.',
         best_for='Punters wanting a solid secondary account with good racing coverage',
         not_for='Punters looking for cutting-edge technology or the widest market range',
         desc='Blondebet is an Australian bookmaker that has built a solid reputation among racing punters for competitive odds and fair account treatment. It is a good choice for portfolio diversification.',
         pros=['Solid racing market coverage','Competitive tote options','Fair account treatment relative to majors','Good for account diversification','PayID support'],
         cons=['Smaller market range than major competitors','App less polished than top-tier operators','Lower brand recognition'],
         features=['Racing Markets','Tote Access','Live In-Play','Multi Builder','PayID','Cash Out'],
         faqs=[('Is Blondebet a good bookmaker?','Blondebet is a solid mid-tier Australian bookmaker. It is not the flashiest option, but it offers competitive racing odds, fair account treatment, and reliable payouts — making it a good addition to a multi-account strategy.'),
               ('Is Blondebet licensed?','Yes. Blondebet holds a Northern Territory racing and wagering licence and is regulated by the NT Racing Commission.'),
               ('Does Blondebet limit winning accounts?','Blondebet has a better reputation than the major corporate bookmakers for account treatment. It is a popular choice for punters who have been limited elsewhere.'),
               ('What racing does Blondebet cover?','Blondebet covers Australian thoroughbred racing, harness racing, and greyhound racing with both fixed-odds and tote products.'),
               ('Can I use PayID on Blondebet?','Yes. Blondebet supports PayID deposits and withdrawals for faster transaction processing.')]),

    dict(name='Chasebet', slug='chasebet', logo='chasebet.png', rating=4.0,
         type='Sports & Racing', est=2016, colour='#dc2626', licence='NT Racing',
         withdraw='1–2 business days', min_dep='$10',
         tagline='Competitive odds across racing and sports with a reputation for fair account treatment.',
         best_for='Punters wanting a reliable additional account with fair account treatment',
         not_for='Punters seeking the most polished app or a premium brand experience',
         desc='Chasebet is a reliable Australian bookmaker offering competitive odds across racing and sports. It has built a following among punters who value fair account treatment and consistent odds.',
         pros=['Competitive odds across racing and sports','Fair account treatment','Reliable platform','Good PayID withdrawal support','Useful for multi-account diversification'],
         cons=['Smaller market range than major operators','Less brand recognition','App less feature-rich than Sportsbet or betr'],
         features=['Racing Markets','Sports Markets','Live In-Play','Multi Builder','PayID','Cash Out'],
         faqs=[('Is Chasebet a good bookmaker?','Chasebet is a solid Australian bookmaker, particularly for punters looking to diversify across multiple accounts. It offers competitive odds and has a reasonable reputation for account treatment.'),
               ('Is Chasebet licensed?','Yes. Chasebet holds a Northern Territory racing and wagering licence and is regulated by the NT Racing Commission.'),
               ('Does Chasebet limit winning accounts?','Chasebet has a better reputation for account treatment than the major corporate bookmakers. It is a good option for punters who have been limited at Sportsbet, Ladbrokes, or Neds.'),
               ('What sports does Chasebet cover?','Chasebet covers AFL, NRL, cricket, soccer, tennis, and other sports alongside comprehensive Australian racing markets.'),
               ('How fast are Chasebet withdrawals?','Chasebet supports PayID withdrawals, which typically process within 1–2 business days.')]),
]

BM_BY_SLUG = {bm['slug']: bm for bm in BMS}
TOP_10     = BMS[:10]
TOP_6      = BMS[:6]

# ─── SHARED HTML HELPERS ─────────────────────────────────────────────────────

CSS = """:root{--bg:hsl(205 60% 96%);--fg:hsl(215 45% 16%);--primary:hsl(48 92% 64%);--pfg:hsl(215 45% 16%);--muted:hsl(205 40% 92%);--muted-fg:hsl(215 20% 42%);--accent:hsl(200 88% 58%);--border:hsl(205 40% 86%);--gg:linear-gradient(135deg,hsl(50 96% 72%),hsl(44 92% 60%));--sg:0 10px 40px -10px hsl(48 92% 54%/.4);--sc:0 4px 24px -8px hsl(215 50% 30%/.1);--ch:36px;--nh:80px;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--fg);font-family:"Inter Tight",sans-serif;line-height:1.65;font-size:15px;}
h1,h2,h3,h4{font-family:"Geist",sans-serif;letter-spacing:-0.03em;}
a{color:inherit;}
img{max-width:100%;}
.cb{position:fixed;top:0;left:0;right:0;height:var(--ch);background:hsl(215 45% 16%);color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 24px;font-size:11px;z-index:200;gap:12px;}
.cb-t{font-weight:700;color:var(--primary);}
.cb-h{color:hsl(205 40% 70%);}
.cb-h a{color:var(--accent);text-decoration:none;}
.cb-b{display:flex;gap:6px;}
.cb-b span{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);border-radius:4px;padding:2px 6px;font-size:10px;font-weight:700;}
.nav{position:fixed;top:var(--ch);left:0;right:0;height:var(--nh);background:hsl(205 60% 96%/.9);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;padding:0 40px;z-index:100;}
.nav-logo img{height:72px;width:auto;}
.nav-links{display:flex;gap:20px;list-style:none;}
.nav-links a{font-size:13px;font-weight:500;color:hsl(215 45% 16%/.7);text-decoration:none;transition:color .2s;}
.nav-links a:hover{color:var(--primary);}
.btn-g{display:inline-flex;align-items:center;background:var(--gg);color:var(--pfg);font-size:13px;font-weight:700;padding:9px 18px;border-radius:10px;border:none;cursor:pointer;text-decoration:none;box-shadow:var(--sg);white-space:nowrap;}
.pb{padding-top:calc(var(--ch) + var(--nh));}
.hero{padding:44px 32px 36px;background:radial-gradient(ellipse at top,hsl(200 85% 88%),hsl(205 70% 96%) 70%);border-bottom:1px solid var(--border);}
.hero-in{max-width:1100px;margin:0 auto;}
.eye{display:flex;align-items:center;gap:10px;margin-bottom:12px;}
.eye-l{height:1px;width:32px;background:var(--primary);}
.eye-t{font-family:"JetBrains Mono",monospace;font-size:11px;color:var(--primary);text-transform:uppercase;letter-spacing:.2em;}
.hero h1{font-size:clamp(26px,3.8vw,46px);font-weight:700;line-height:1.06;margin-bottom:12px;}
.hero-sub{font-size:16px;color:hsl(215 45% 16%/.65);max-width:680px;line-height:1.75;margin-bottom:18px;}
.upd{font-size:11px;color:var(--muted-fg);font-family:"JetBrains Mono",monospace;}
.bc{font-size:12px;color:var(--muted-fg);margin-bottom:10px;}
.bc a{color:var(--muted-fg);text-decoration:none;}
.wrap{max-width:1100px;margin:0 auto;padding:44px 32px 80px;}
.rank-table{width:100%;border-collapse:collapse;margin:28px 0;}
.rank-table th{text-align:left;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);padding:10px 14px;border-bottom:2px solid var(--border);}
.rank-table td{padding:12px 14px;border-bottom:1px solid var(--border);vertical-align:middle;}
.rank-table tr:hover td{background:hsl(205 60% 97%);}
.rnum{font-family:"JetBrains Mono",monospace;font-size:13px;font-weight:700;color:var(--muted-fg);}
.rbm{display:flex;align-items:center;gap:12px;}
.rlogo{width:40px;height:40px;border-radius:10px;object-fit:contain;background:#fff;box-shadow:var(--sc);flex-shrink:0;}
.rname{font-weight:700;font-size:14px;}
.rmeta{font-size:12px;color:var(--muted-fg);}
.rstars{color:#f59e0b;font-size:13px;}
.rrating{font-size:12px;font-weight:700;color:var(--muted-fg);margin-left:3px;}
.card{background:#fff;border:1px solid var(--border);border-radius:14px;padding:24px;margin-bottom:20px;box-shadow:var(--sc);}
.card-row{display:flex;align-items:flex-start;gap:20px;margin-bottom:16px;}
.card-logo{width:64px;height:64px;border-radius:16px;object-fit:contain;background:#fff;box-shadow:var(--sc);flex-shrink:0;}
.stars{color:#f59e0b;font-size:18px;}
.verdict{font-style:italic;color:hsl(215 45% 16%/.75);margin:12px 0;font-size:14px;line-height:1.7;}
.pros-cons{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:16px 0;}
.pros,.cons{padding:14px;border-radius:10px;}
.pros{background:hsl(140 50% 97%);border:1px solid hsl(140 50% 88%);}
.cons{background:hsl(16 80% 97%);border:1px solid hsl(16 80% 88%);}
.pros h4{color:hsl(140 50% 32%);font-size:11px;text-transform:uppercase;letter-spacing:.1em;margin-bottom:8px;}
.cons h4{color:hsl(16 70% 38%);font-size:11px;text-transform:uppercase;letter-spacing:.1em;margin-bottom:8px;}
.pros li,.cons li{font-size:13px;line-height:1.6;margin-bottom:5px;list-style:none;padding-left:16px;position:relative;}
.pros li::before{content:"✓";position:absolute;left:0;color:hsl(140 50% 40%);}
.cons li::before{content:"✗";position:absolute;left:0;color:hsl(16 70% 45%);}
.feats{display:flex;flex-wrap:wrap;gap:7px;margin:12px 0;}
.feat{background:var(--muted);border-radius:6px;padding:4px 10px;font-size:12px;font-weight:500;}
.meta-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:16px 0;}
.meta-item{background:var(--muted);border-radius:8px;padding:12px;}
.meta-label{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:4px;}
.meta-val{font-size:14px;font-weight:600;}
.cmp-table{width:100%;border-collapse:collapse;margin:24px 0;}
.cmp-table th{padding:12px 16px;text-align:center;font-size:13px;font-weight:700;background:var(--muted);border:1px solid var(--border);}
.cmp-table th:first-child{text-align:left;}
.cmp-table td{padding:11px 16px;border:1px solid var(--border);text-align:center;font-size:13px;}
.cmp-table td:first-child{text-align:left;font-weight:600;color:var(--muted-fg);font-size:12px;text-transform:uppercase;letter-spacing:.05em;}
.cmp-table tr:nth-child(even) td{background:hsl(205 40% 98%);}
.win{color:hsl(140 50% 32%);font-weight:700;}
.int-links{background:#fff;border:1px solid var(--border);border-radius:12px;padding:18px 22px;margin:28px 0;}
.int-links h3{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--muted-fg);margin-bottom:12px;}
.int-links a{display:inline-block;background:var(--muted);border-radius:6px;padding:5px 11px;margin:3px;font-size:13px;font-weight:500;text-decoration:none;color:var(--fg);}
.int-links a:hover{background:var(--border);}
.faq{margin:44px 0;}
.faq h2{font-size:22px;font-weight:700;margin-bottom:20px;}
.faq-item{border:1px solid var(--border);border-radius:10px;margin-bottom:8px;overflow:hidden;}
.faq-q{width:100%;text-align:left;background:#fff;border:none;padding:14px 18px;font-size:14px;font-weight:600;cursor:pointer;display:flex;justify-content:space-between;align-items:center;font-family:"Inter Tight",sans-serif;color:var(--fg);}
.fi{font-size:18px;color:var(--muted-fg);}
.faq-a{padding:0 18px 14px;font-size:14px;line-height:1.75;color:hsl(215 45% 16%/.8);display:none;}
.faq-a.open{display:block;}
.site-footer{background:hsl(215 45% 16%);color:rgba(255,255,255,.7);padding:44px 32px 28px;margin-top:72px;}
.footer-in{max-width:1100px;margin:0 auto;}
.footer-logo{height:44px;width:auto;margin-bottom:14px;filter:brightness(0) invert(1);opacity:.75;}
.footer-desc{font-size:13px;line-height:1.7;max-width:400px;margin-bottom:28px;}
.footer-links{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:28px;}
.footer-links a{font-size:13px;color:rgba(255,255,255,.55);text-decoration:none;}
.footer-links a:hover{color:#fff;}
.footer-rg{font-size:11px;color:rgba(255,255,255,.4);border-top:1px solid rgba(255,255,255,.1);padding-top:20px;line-height:1.8;}
.footer-rg a{color:rgba(255,255,255,.4);}
.verdict-box{background:hsl(48 80% 97%);border:1px solid hsl(48 60% 85%);border-radius:10px;padding:16px 20px;margin:20px 0;}
.verdict-box strong{display:block;font-size:12px;text-transform:uppercase;letter-spacing:.1em;color:hsl(48 60% 40%);margin-bottom:6px;}
@media(max-width:768px){.nav-links{display:none;}.wrap,.hero{padding-left:16px;padding-right:16px;}.pros-cons,.meta-grid{grid-template-columns:1fr;}.nav{padding:0 20px;}}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800&family=Inter+Tight:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">'

def head(title, desc, slug, schema=''):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{slug}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{slug}">
<meta property="og:type" content="article">
<meta name="robots" content="index, follow">
<link rel="icon" type="image/png" href="/pg-icon.png">
{FONTS}
{schema}
<style>{CSS}</style>
</head>"""

def compliance_bar():
    return '<div class="cb"><span class="cb-t">Bet Responsibly</span><span class="cb-h">Gambling Help: <a href="tel:1800858858">1800 858 858</a> · <a href="https://www.gamblinghelponline.org.au" target="_blank">gamblinghelponline.org.au</a></span><div class="cb-b"><span>18+</span><span>AUS ONLY</span></div></div>'

def nav():
    return '<nav class="nav"><a href="/index.html" class="nav-logo"><img src="/puntguide-logo.png" alt="PuntGuide"></a><ul class="nav-links"><li><a href="/best-betting-sites-australia.html">Best Sites</a></li><li><a href="/best-betting-apps-australia.html">Best Apps</a></li><li><a href="/fastest-payout-betting-sites-australia.html">Fast Payouts</a></li><li><a href="/best-betting-sites-for-racing.html">Racing</a></li><li><a href="/all-betting-sites.html">All Sites</a></li></ul><a href="/all-betting-sites.html" class="btn-g">Bet Now →</a></nav>'

def footer_html():
    links = [
        ('Best Betting Sites','/best-betting-sites-australia.html'),
        ('Top Betting Sites','/top-betting-sites-australia.html'),
        ('Best Betting Apps','/best-betting-apps-australia.html'),
        ('Compare Sites','/compare-betting-sites.html'),
        ('Betting Sites Australia','/betting-sites-australia.html'),
        ('Online Betting','/online-betting-australia.html'),
        ('Sports Betting','/sports-betting-sites-australia.html'),
        ('Australian Bookmakers','/bookmakers-australia.html'),
        ('Live Betting','/live-betting-australia.html'),
        ('No Deposit Sites','/no-deposit-betting-sites.html'),
        ('New Betting Sites','/new-betting-sites-australia.html'),
        ('Fastest Payouts','/fastest-withdrawal-betting-sites-australia.html'),
        ('All 134 Bookmakers','/all-betting-sites.html'),
    ]
    ls = ''.join(f'<a href="{h}">{t}</a>' for t,h in links)
    return f"""<footer class="site-footer"><div class="footer-in">
<img src="/puntguide-logo.png" alt="PuntGuide" class="footer-logo">
<p class="footer-desc">Australia's most up-to-date directory of licensed betting sites. Every Australian bookmaker independently reviewed — we may earn commission from referrals.</p>
<div class="footer-links">{ls}</div>
<div class="footer-rg">Gamble responsibly. Call <a href="tel:1800858858">Gambling Help 1800 858 858</a> or visit <a href="https://www.gamblinghelponline.org.au" target="_blank">gamblinghelponline.org.au</a>. Self-exclude at <a href="https://www.betstop.gov.au" target="_blank">BetStop.gov.au</a>. 18+ only. PuntGuide earns commission from bookmaker referrals — this does not affect our ratings.</div>
</div></footer>
<script>document.querySelectorAll('.faq-q').forEach(b=>b.addEventListener('click',function(){{const a=this.nextElementSibling;a.classList.toggle('open');this.querySelector('.fi').textContent=a.classList.contains('open')?'−':'+';}}));</script>"""

def faq_schema(faqs):
    items = ','.join([f'{{"@type":"Question","name":{json.dumps(q)},"acceptedAnswer":{{"@type":"Answer","text":{json.dumps(a)}}}}}' for q,a in faqs])
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{items}]}}</script>'

def article_schema(title, desc, slug):
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":{json.dumps(title)},"description":{json.dumps(desc)},"author":{{"@type":"Organization","name":"PuntGuide"}},"publisher":{{"@type":"Organization","name":"PuntGuide","logo":{{"@type":"ImageObject","url":"{SITE}/favicon-192.png"}}}},"datePublished":"2026-01-01","dateModified":"{DATE}","mainEntityOfPage":"{SITE}/{slug}","image":{{"@type":"ImageObject","url":"{SITE}/favicon-192.png"}}}}</script>'

def faq_html(faqs):
    items = ''.join([f'<div class="faq-item"><button class="faq-q">{q} <span class="fi">+</span></button><div class="faq-a">{a}</div></div>' for q,a in faqs])
    return f'<div class="faq"><h2>Frequently asked questions</h2>{items}</div>'

def int_links(links):
    ls = ''.join(f'<a href="{h}">{t}</a>' for t,h in links)
    return f'<div class="int-links"><h3>Related pages</h3>{ls}</div>'

def rank_row(i, bm):
    stars = '★' * int(bm['rating']) + ('½' if bm['rating'] % 1 else '')
    return f"""<tr>
      <td class="rnum">{i}</td>
      <td><div class="rbm"><img src="/{bm['logo']}" alt="{bm['name']}" class="rlogo"><div><div class="rname">{bm['name']}</div><div class="rmeta">{bm['type']} · Est. {bm['est']}</div></div></div></td>
      <td><span class="rstars">{stars}</span><span class="rrating">{bm['rating']}/5</span></td>
      <td style="font-size:13px;color:var(--muted-fg);max-width:200px">{bm['best_for']}</td>
      <td><a href="#" onclick="return false;" class="btn-g" style="font-size:12px;padding:7px 13px;">Bet Now →</a></td>
    </tr>"""

def rank_table(bms):
    rows = ''.join(rank_row(i+1, bm) for i, bm in enumerate(bms))
    return f'<table class="rank-table"><thead><tr><th>#</th><th>Bookmaker</th><th>Rating</th><th>Best for</th><th>Action</th></tr></thead><tbody>{rows}</tbody></table>'

def bm_card(bm, rank=None):
    stars = '★' * int(bm['rating']) + ('½' if bm['rating'] % 1 else '')
    pros  = ''.join(f'<li>{p}</li>' for p in bm['pros'])
    cons  = ''.join(f'<li>{c}</li>' for c in bm['cons'])
    feats = ''.join(f'<span class="feat">{f}</span>' for f in bm['features'])
    rank_label = f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:11px;color:var(--muted-fg);">#{rank} Overall</span>' if rank else ''
    return f"""<div class="card" id="{bm['slug']}">
  <div class="card-row">
    <img src="/{bm['logo']}" alt="{bm['name']}" class="card-logo">
    <div style="flex:1">
      <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:6px">
        <h3 style="margin:0">{bm['name']}</h3>{rank_label}
      </div>
      <div class="stars">{stars}</div>
      <p class="verdict">"{bm['tagline']}"</p>
      <div style="display:flex;gap:16px;flex-wrap:wrap;font-size:13px;color:var(--muted-fg);margin-bottom:10px">
        <span>✓ Best for: <strong style="color:var(--fg)">{bm['best_for']}</strong></span>
      </div>
      <div class="feats">{feats}</div>
    </div>
  </div>
  <div class="pros-cons">
    <div class="pros"><h4>Pros</h4><ul>{pros}</ul></div>
    <div class="cons"><h4>Cons</h4><ul>{cons}</ul></div>
  </div>
  <div style="display:flex;gap:12px;align-items:center;margin-top:16px">
    <a href="#" onclick="return false;" class="btn-g">Bet Now →</a>
    <a href="/review-{bm['slug']}.html" style="font-size:13px;color:var(--muted-fg);text-decoration:none;">Full Review →</a>
  </div>
  <p style="font-size:11px;color:var(--muted-fg);margin-top:10px">"Think. Is this a bet you really want to place?" · 18+ · T&Cs apply</p>
</div>"""

def save(slug, html):
    path = os.path.join(OUT, slug)
    with open(path, 'w') as f:
        f.write(html)
    print(f'  ✓ {slug}')
    return slug

# ─── LIST PAGE GENERATOR ─────────────────────────────────────────────────────

LIST_PAGES = [
    dict(slug='top-betting-sites-australia.html',
         title='Top Betting Sites Australia 2026 | Ranked & Reviewed | PuntGuide',
         desc='The top-rated betting sites in Australia for 2026. Every bookmaker ranked by odds, markets, app quality and payout speed. Independent reviews from real punters.',
         h1='Top Betting Sites Australia 2026',
         eyebrow='Independent Rankings · Updated May 2026',
         intro='Finding the top betting site in Australia comes down to what you bet on. The rankings below are based on four months of real-account testing — odds competitiveness, market depth, app experience, and withdrawal speed. No paid placements.',
         h2s=[
             ('Why PointsBet Is Our Top Pick', 'PointsBet earns the top ranking for its combination of sharp fixed odds, a genuinely unique PointsBetting product, and strong coverage of both sports and racing. No other Australian bookmaker offers the same range of market types.'),
             ('BetRight: Top Pick for Racing', "For racing-first punters, BetRight is the standout. It wins on Best Tote availability, Same Race Multi quality, and withdrawal speed — the three metrics that matter most to serious racing punters."),
             ('Dabble: Top Pick for App Experience', "Dabble consistently wins on app experience and innovation. The social feed and copy-betting feature are genuinely unique in Australia. If you are new to sports betting or want to learn from experienced punters, Dabble is the place to start."),
         ],
         faqs=[
             ('What is the top-rated betting site in Australia?', 'PointsBet is our top-rated all-round betting site in Australia for 2026. It offers sharp odds, unique PointsBetting markets, strong sports and racing coverage, and fast PayID withdrawals. For racing specialists, BetRight tops the list.'),
             ('How are top betting sites ranked?', 'PuntGuide ranks Australian betting sites on odds competitiveness (tested weekly across AFL, NRL, and racing), market depth, app quality, withdrawal speed, and account treatment. No bookmaker pays for placement.'),
             ('Are top betting sites in Australia safe?', 'Every betting site on PuntGuide holds a current Australian state or territory bookmaking licence. Licensed bookmakers are regulated under the Interactive Gambling Act 2001 and must meet strict financial and operational requirements.'),
             ('How many top betting sites should I have?', 'Two to four accounts is the practical sweet spot for most Australian punters. PointsBet, BetRight, and Dabble cover sports, racing, and app experience comprehensively. Adding Sportsbet or Ladbrokes gives access to wider market ranges.'),
             ('Do top betting sites offer better odds?', 'Top-rated bookmakers generally offer more competitive odds than lesser-known sites. However, the best odds on any given market vary — which is why serious punters hold multiple accounts and compare before betting.'),
         ],
         int=[
             ('Best Betting Sites Australia','/best-betting-sites-australia.html'),
             ('Best Betting Apps','/best-betting-apps-australia.html'),
             ('Compare Betting Sites','/compare-betting-sites.html'),
             ('New Betting Sites 2026','/new-betting-sites-australia.html'),
             ('Fastest Payouts','/fastest-withdrawal-betting-sites-australia.html'),
             ('All 134 Bookmakers','/all-betting-sites.html'),
         ]),

    dict(slug='compare-betting-sites.html',
         title='Compare Betting Sites Australia 2026 | Side-by-Side | PuntGuide',
         desc='Compare Australian betting sites side by side. Odds, markets, apps, payouts and account treatment — all tested with real accounts. Find your best fit.',
         h1='Compare Betting Sites Australia 2026',
         eyebrow='Side-by-Side Comparison · Updated May 2026',
         intro='The best betting site depends entirely on what you bet on. This comparison covers the key metrics that actually matter — odds competitiveness, market depth, app quality, and withdrawal speed — tested with real accounts over four months.',
         h2s=[
             ('How We Compare Australian Betting Sites', 'Every week our team records head-to-head and line prices on AFL, NRL, and racing markets across every major bookmaker. We also track withdrawal speeds, app update frequency, and customer service response times. No bookmaker can buy a better rating.'),
             ('Odds Comparison: Who Prices the Market Best?', 'On AFL head-to-head markets, Ladbrokes and PointsBet consistently offer the most competitive prices. On NRL, PointsBet and Sportsbet lead. On racing fixed odds, BetRight and Ladbrokes are most competitive. No single bookmaker wins across all markets — which is why holding multiple accounts matters.'),
             ('App Comparison: Best Betting Apps in 2026', 'Dabble wins on overall app experience. betr wins for same-game multi functionality. Sportsbet wins for speed via its Speedy Bet feature. BetRight wins for racing-specific features. If you only have one app, Sportsbet offers the best all-round experience.'),
         ],
         faqs=[
             ('Which Australian betting site has the best odds?', 'No single bookmaker leads on all markets. Ladbrokes and PointsBet are most competitive on AFL head-to-head. BetRight leads for racing fixed odds. For the best odds on any bet, compare across at least two accounts before placing.'),
             ('How do I compare betting apps?', 'Compare apps on: ease of placing bets, multi builder quality, live betting interface, withdrawal process, and notification quality. Sportsbet and betr are rated highest for overall app quality. Dabble wins for social features.'),
             ('Should I use one or multiple betting sites?', 'Multiple accounts gives you more flexibility and better odds. Two to four accounts is optimal — enough to compare prices without the complexity of managing too many. PointsBet, BetRight, and Dabble is a strong starting trio.'),
             ('Are all Australian betting sites the same?', 'No. The differences are significant — particularly on odds, racing market depth, app quality, and how each bookmaker treats winning accounts. Specialist racing books like BetRight outperform generalists on racing metrics.'),
             ('What should I compare when choosing a betting site?', 'Focus on: odds competitiveness for your preferred sport, market depth (number of markets available), app quality, withdrawal speed, and account treatment reputation. Our comparison table above covers all of these.'),
         ],
         int=[
             ('Best Betting Sites Australia','/best-betting-sites-australia.html'),
             ('Top Betting Sites Australia','/top-betting-sites-australia.html'),
             ('Sports Betting Sites','/sports-betting-sites-australia.html'),
             ('Best Betting Apps','/best-betting-apps-australia.html'),
             ('Fastest Payouts','/fastest-withdrawal-betting-sites-australia.html'),
             ('All 134 Bookmakers','/all-betting-sites.html'),
         ]),

    dict(slug='betting-sites-australia.html',
         title='Betting Sites Australia 2026 | All Licensed Bookmakers | PuntGuide',
         desc='Every licensed betting site in Australia for 2026. 134 bookmakers reviewed — from the biggest names to the newest launches. Find the right site for you.',
         h1='Betting Sites Australia 2026',
         eyebrow='134 Licensed Bookmakers · Updated May 2026',
         intro='Australia has one of the most competitive betting markets in the world — with over 130 licensed bookmakers operating under federal and state wagering legislation. This guide covers every major site, ranked by our independent editorial team.',
         h2s=[
             ('How Many Betting Sites Are There in Australia?', 'As of May 2026, there are 134 licensed Australian betting sites operating under valid state or territory bookmaking licences. This includes major corporate bookmakers, racing specialists, and newer digital-first operators. We review them all.'),
             ('How Are Australian Betting Sites Licensed?', 'Australian betting sites must hold a state or territory bookmaking licence to operate legally. Most online bookmakers operate under a Northern Territory Racing Commission licence. Racing-focused operators may hold licences from Racing NSW, Racing Victoria, or other state bodies.'),
             ('Which Betting Sites Are New in 2026?', 'Several new betting sites have launched or significantly updated their platforms in 2026. Dabble, betr, and Picklebet are among the most notable newer entrants that have built substantial user bases quickly.'),
         ],
         faqs=[
             ('Are betting sites legal in Australia?', 'Yes. Licensed betting sites are legal in Australia. Every site on PuntGuide holds a current Australian state or territory bookmaking licence and is regulated under the Interactive Gambling Act 2001.'),
             ('What is the best betting site in Australia?', 'The best betting site depends on what you bet on. PointsBet leads for sports and unique markets. BetRight leads for horse racing. Dabble leads for app experience. Sportsbet leads for market depth. See our full rankings above.'),
             ('Can I bet online in Australia?', 'Yes. Online sports betting is legal in Australia for pre-match and racing bets. In-play betting is permitted through digital channels (app or website) but not by phone under the Interactive Gambling Act.'),
             ('Do Australian betting sites have sign-up offers?', 'Australian law prohibits betting sites from advertising sign-up inducements to unregistered customers. Any current promotions become visible after you register an account directly with the bookmaker.'),
             ('How do I choose a betting site in Australia?', 'Choose based on what you bet on most. Racing punters should prioritise BetRight or Ladbrokes. Sports punters should prioritise PointsBet or Sportsbet. App-first punters should consider Dabble or betr. Most serious punters hold 2–4 accounts.'),
         ],
         int=[
             ('Best Betting Sites Australia','/best-betting-sites-australia.html'),
             ('New Betting Sites 2026','/new-betting-sites-australia.html'),
             ('Bookmakers Australia','/bookmakers-australia.html'),
             ('Online Betting Australia','/online-betting-australia.html'),
             ('All 134 Bookmakers','/all-betting-sites.html'),
             ('Compare Sites','/compare-betting-sites.html'),
         ]),

    dict(slug='online-betting-australia.html',
         title='Online Betting Australia 2026 | Best Sites & Apps | PuntGuide',
         desc='The best online betting sites and apps in Australia for 2026. Every licensed platform reviewed — sports, racing, live betting and more. Updated weekly.',
         h1='Online Betting Australia 2026',
         eyebrow='Online Betting Guide · Updated May 2026',
         intro='Online betting in Australia is legal, regulated, and extremely competitive. With over 130 licensed platforms, finding the right online bookmaker means understanding what each one does best — and what matters most to you as a punter.',
         h2s=[
             ('Is Online Betting Legal in Australia?', 'Yes. Online betting is legal in Australia for pre-match sports and racing wagers. In-play (live) betting is permitted through digital channels under the Interactive Gambling Act 2001. Offshore unlicensed betting sites are not legal for Australian residents.'),
             ('Best Online Betting Apps in Australia', "The best online betting apps in 2026 are rated on ease of use, speed, multi builder quality, and live betting features. Sportsbet's Speedy Bet is the fastest for quick punting. Dabble is the most innovative. betr has the best same-game multi builder."),
             ('Online Betting Safety in Australia', 'All licensed Australian online bookmakers are required to implement responsible gambling tools including deposit limits, time limits, self-exclusion, and access to support services. BetStop, the National Self-Exclusion Register, allows you to exclude yourself from all licensed sites at once.'),
         ],
         faqs=[
             ('Is online betting safe in Australia?', 'Online betting on licensed Australian platforms is safe. All bookmakers on PuntGuide hold current Australian licences and must meet strict regulatory requirements covering fund segregation, responsible gambling tools, and dispute resolution.'),
             ('What is the best online betting app in Australia?', 'Sportsbet has the widest market range. Dabble has the best UX and social features. betr has the best same-game multi builder. BetRight is the best for racing. The right app depends on what you bet on most.'),
             ('Can I bet on sports online in Australia?', 'Yes. All licensed Australian bookmakers allow online sports betting via their websites and mobile apps. You can bet on AFL, NRL, cricket, soccer, tennis, basketball, and many more sports pre-match and in-play.'),
             ('How do I deposit online at an Australian betting site?', 'Most Australian betting sites accept credit/debit card, PayID, and bank transfer deposits. PayID is typically the fastest option, with deposits credited instantly. Most sites have a minimum deposit of $10.'),
             ('Can I withdraw winnings online from Australian betting sites?', 'Yes. All licensed Australian betting sites allow online withdrawals to your registered bank account. PayID withdrawals are typically the fastest, processing within hours at sites like BetRight and Dabble.'),
         ],
         int=[
             ('Best Betting Sites Australia','/best-betting-sites-australia.html'),
             ('Best Betting Apps','/best-betting-apps-australia.html'),
             ('Live Betting Australia','/live-betting-australia.html'),
             ('Fastest Withdrawal Sites','/fastest-withdrawal-betting-sites-australia.html'),
             ('Sports Betting Sites','/sports-betting-sites-australia.html'),
             ('All 134 Bookmakers','/all-betting-sites.html'),
         ]),

    dict(slug='sports-betting-sites-australia.html',
         title='Sports Betting Sites Australia 2026 | Best for AFL, NRL & More | PuntGuide',
         desc='The best sports betting sites in Australia for 2026. Ranked on odds, market depth, SGM quality, and live betting for AFL, NRL, racing, soccer and more.',
         h1='Sports Betting Sites Australia 2026',
         eyebrow='Sports Betting Guide · Updated May 2026',
         intro='Australian sports betting sites vary significantly in what they offer. The best site for AFL betting is not necessarily the best for NRL, soccer, or racing. This guide ranks every major sports bookmaker in Australia based on real-account testing.',
         h2s=[
             ('Best Sports Betting Sites for AFL', 'For AFL betting, PointsBet and Sportsbet lead on market depth. PointsBet has the sharpest head-to-head odds and the best same-game multi options. Dabble is the best for following and copying AFL punters via its social feed.'),
             ('Best Sports Betting Sites for NRL', "PointsBet and betr are our top picks for NRL. PointsBet's PointsBetting markets on match stats are unique. betr's NRL same-game multi builder is consistently rated alongside Sportsbet as the best in the market."),
             ('Best Sports Betting Sites for International Sports', 'For international sports — soccer, tennis, basketball, cricket — Bet365 is the clear leader. It offers live streaming and the deepest market coverage of any Australian-licensed bookmaker.'),
         ],
         faqs=[
             ('What is the best sports betting site in Australia?', 'PointsBet is our top pick for all-round sports betting in Australia. It has the sharpest odds, unique PointsBetting markets, and strong AFL and NRL coverage. For international sports, Bet365 is the better choice.'),
             ('Is sports betting legal in Australia?', 'Yes. Sports betting is legal in Australia on licensed platforms. Pre-match betting is available by any channel. In-play betting must be placed through digital channels (app or website) under the Interactive Gambling Act 2001.'),
             ('Which sports betting site has the best same-game multis?', 'Sportsbet, betr, and PointsBet are rated the best for same-game multis in Australia. betr edges ahead specifically for AFL and NRL SGMs. Dabble is also strong with a unique social betting layer.'),
             ('Can I bet on international sports at Australian betting sites?', 'Yes. Most major Australian bookmakers cover international sports. Bet365 has the widest international coverage. Sportsbet and Ladbrokes also offer extensive international sports markets.'),
             ('What sports can I bet on in Australia?', 'Australian betting sites cover AFL, NRL, cricket, horse racing, greyhound racing, harness racing, soccer (EPL, UCL, A-League), tennis, basketball (NBL, NBA), rugby union, golf, boxing, MMA, esports, and many more.'),
         ],
         int=[
             ('Best Betting Sites Australia','/best-betting-sites-australia.html'),
             ('Best Sites for AFL & NRL','/best-betting-sites-afl-nrl.html'),
             ('Best Sites for Racing','/best-betting-sites-for-racing.html'),
             ('Live Betting Australia','/live-betting-australia.html'),
             ('Compare Betting Sites','/compare-betting-sites.html'),
             ('All 134 Bookmakers','/all-betting-sites.html'),
         ]),

    dict(slug='bookmakers-australia.html',
         title='Australian Bookmakers 2026 | All Licensed Operators Ranked | PuntGuide',
         desc='Every licensed Australian bookmaker ranked and reviewed for 2026. Odds competitiveness, market depth, withdrawal speed, and account treatment — independently assessed.',
         h1='Australian Bookmakers 2026',
         eyebrow='Licensed Operators · Updated May 2026',
         intro='Australia has over 130 licensed bookmakers — one of the most competitive wagering markets globally. Understanding the difference between corporate bookmakers, racing specialists, and independent operators is essential to building the right betting account portfolio.',
         h2s=[
             ('Corporate Bookmakers vs Independent Operators', 'The major corporate bookmakers — Sportsbet, Ladbrokes, Neds, Bet365, and Tab — have the widest market coverage and the most marketing spend. However, they are also most likely to restrict or close winning accounts. Independent operators like Palmerbet and BetRight often offer better treatment for profitable punters.'),
             ('Racing Specialist Bookmakers', 'BetRight, Ladbrokes, and Tab are the strongest racing specialists in Australia. BetRight leads on Best Tote access and Same Race Multi quality. Ladbrokes leads on racing fixed odds competitiveness. Tab leads on tote pool depth for exotic bets.'),
             ('Betting Exchanges: A Different Model', 'Betfair operates as a betting exchange rather than a traditional bookmaker. You bet against other punters rather than against the house. This typically means better odds, no account restrictions, and the ability to lay outcomes — but a commission is charged on winnings.'),
         ],
         faqs=[
             ('How many bookmakers are licensed in Australia?', 'As of May 2026, there are 134 licensed bookmakers operating in Australia. Most hold Northern Territory Racing Commission licences. Some operate under state licences from Racing NSW, Racing Victoria, Racing QLD, or other bodies.'),
             ('Which Australian bookmaker is the oldest?', 'Ladbrokes traces its origins to 1886, making it the oldest brand operating in Australian betting. Among Australian-founded bookmakers, Sportsbet (1993) and Tab (1961) are among the longest-established.'),
             ('Which Australian bookmakers do not restrict winning accounts?', 'Betfair (exchange model — no restrictions), Palmerbet, and BetRight have better reputations for account treatment than the major corporate bookmakers. Serious punters typically seek out these operators.'),
             ('Can a bookmaker close my account in Australia?', 'Yes. Australian bookmakers can close or restrict accounts at their discretion under their terms and conditions. This most commonly affects accounts that win consistently. There is no regulatory requirement for bookmakers to keep accounts open.'),
             ('What is the difference between a bookmaker and an exchange?', 'A bookmaker sets odds and takes the other side of your bet — they win when you lose. A betting exchange (like Betfair) matches your bet against another punter — the exchange takes a commission from winning bets but has no stake in the outcome.'),
         ],
         int=[
             ('Best Betting Sites Australia','/best-betting-sites-australia.html'),
             ('New Betting Sites 2026','/new-betting-sites-australia.html'),
             ('Compare Betting Sites','/compare-betting-sites.html'),
             ('Fastest Payouts','/fastest-withdrawal-betting-sites-australia.html'),
             ('Betting Sites Australia','/betting-sites-australia.html'),
             ('All 134 Bookmakers','/all-betting-sites.html'),
         ]),

    dict(slug='no-deposit-betting-sites.html',
         title='No Deposit Betting Sites Australia 2026 | PuntGuide',
         desc='No deposit betting sites in Australia — what they are, what the law says, and the best way to get started with Australian bookmakers without risk.',
         h1='No Deposit Betting Sites Australia 2026',
         eyebrow='Promotions Guide · Updated May 2026',
         intro='If you are searching for no deposit betting sites in Australia, you need to understand what Australian law permits. The regulatory environment is different to the UK — here is exactly what is and is not available to Australian punters.',
         h2s=[
             ('Australian Law and No Deposit Offers', 'Under Australian law, betting sites cannot advertise sign-up inducements — including no deposit bonus bets — to unregistered customers. This has applied since 2019. Any current promotional offers become visible after you register an account directly with a licensed bookmaker.'),
             ('How to Get the Best Value as a New Customer', 'While no deposit offers are not publicly advertised, many Australian bookmakers do make promotional offers available to new customers upon registration. The best approach is to register with two or three of our top-rated bookmakers and explore what is available in your account dashboard.'),
             ('Risk-Free Ways to Start Betting in Australia', 'The lowest-risk way to start is to deposit a small amount ($20–$50), take advantage of any new customer offers available post-registration, and spread your betting across multiple accounts to take advantage of the best odds on each market.'),
         ],
         faqs=[
             ('Are there no deposit bonus bets in Australia?', 'Australian law prohibits betting sites from advertising sign-up bonus bets or no deposit offers to unregistered customers. Promotions may be available inside your account after registering — but cannot be advertised externally.'),
             ('Why are bonus bets not advertised in Australia?', 'In 2019, the Australian government tightened restrictions on gambling advertising, including banning bookmakers from promoting sign-up inducements to unregistered customers. This was part of a broader package of responsible gambling measures.'),
             ('What promotions can Australian betting sites offer?', 'Licensed Australian bookmakers can offer promotions to existing customers, including bet boosts, multi insurance, and race specials. These are typically visible in your account dashboard or via email after registration.'),
             ('What is BetStop?', 'BetStop is Australia\'s National Self-Exclusion Register. If you want to stop betting, registering with BetStop excludes you from all licensed Australian bookmakers simultaneously. It is free and available at betstop.gov.au.'),
             ('How do I start betting responsibly in Australia?', 'Set a deposit limit before you start. Most Australian bookmakers allow you to set daily, weekly, or monthly deposit limits in your account settings. Start with small stakes while you are learning, and never bet money you cannot afford to lose.'),
         ],
         int=[
             ('Best Betting Sites Australia','/best-betting-sites-australia.html'),
             ('New Betting Sites 2026','/new-betting-sites-australia.html'),
             ('Online Betting Australia','/online-betting-australia.html'),
             ('Compare Betting Sites','/compare-betting-sites.html'),
             ('Top Betting Sites','/top-betting-sites-australia.html'),
             ('All 134 Bookmakers','/all-betting-sites.html'),
         ]),

    dict(slug='live-betting-australia.html',
         title='Live Betting Australia 2026 | Best In-Play Betting Sites | PuntGuide',
         desc='The best live betting sites in Australia for 2026. In-play betting on AFL, NRL, racing, soccer, and more — ranked on markets, odds, and app speed.',
         h1='Live Betting Australia 2026',
         eyebrow='In-Play Betting Guide · Updated May 2026',
         intro='Live betting — also called in-play betting — lets you bet on sporting events as they happen. Australia has some of the best in-play betting markets in the world, but the rules governing how you can bet live are different to other countries.',
         h2s=[
             ('How Does Live Betting Work in Australia?', 'In-play betting is legal in Australia but must be placed through digital channels — you cannot place a live bet by phone. This has been the rule since the Interactive Gambling Act was updated in 2017. All major Australian bookmakers offer in-play betting via their apps and websites.'),
             ('Best Bookmakers for Live Betting in Australia', 'Sportsbet and Bet365 are rated the best for in-play betting in Australia. Sportsbet has the widest range of live markets across AFL, NRL, and sports. Bet365 offers live streaming alongside live betting, making it the best for following action in real time. betr leads for micro-betting — in-play bets on individual plays or moments within a game.'),
             ('Live Betting on Horse Racing', 'Live race betting in Australia works differently to sports. Fixed-odds bets on races are placed pre-event. However, fluctuating tote dividends mean your effective return changes right up until the race jumps. BetRight offers the best real-time racing tools for tracking market movements.'),
         ],
         faqs=[
             ('Is live betting legal in Australia?', 'Yes. Live (in-play) betting is legal in Australia when placed through digital channels — the app or website of a licensed bookmaker. Phone live betting is not permitted under the Interactive Gambling Act 2001.'),
             ('Which Australian bookmaker is best for live betting?', 'Sportsbet has the widest live betting market range in Australia. Bet365 is best if you want live streaming alongside live betting. betr is the top pick for micro-betting — real-time in-play bets on individual events within a game.'),
             ('What sports can I bet on live in Australia?', 'You can bet live on AFL, NRL, cricket, soccer, tennis, basketball, rugby union, and most other sports covered by Australian bookmakers. Horse racing is available as fixed-odds pre-event and tote throughout.'),
             ('What is micro-betting?', 'Micro-betting is a form of live betting where you bet on very short-term in-game events — such as the next scoring play, the next set, or the next wicket. betr offers the most developed micro-betting product of any licensed Australian bookmaker.'),
             ('How fast do live betting odds update?', 'The speed of live odds updates varies by bookmaker. Sportsbet and Bet365 generally have the fastest live odds updates. Markets may be suspended briefly around key moments in a game to allow the bookmaker to reprice.'),
         ],
         int=[
             ('Best Betting Sites Australia','/best-betting-sites-australia.html'),
             ('Sports Betting Sites','/sports-betting-sites-australia.html'),
             ('Best Betting Apps','/best-betting-apps-australia.html'),
             ('Compare Betting Sites','/compare-betting-sites.html'),
             ('Best Sites for AFL & NRL','/best-betting-sites-afl-nrl.html'),
             ('All 134 Bookmakers','/all-betting-sites.html'),
         ]),
]

def build_list_page(cfg):
    faqs  = cfg['faqs']
    schema = faq_schema(faqs) + '\n' + article_schema(cfg['h1'], cfg['desc'], cfg['slug'])
    cards = ''.join(bm_card(bm, i+1) for i, bm in enumerate(TOP_10[:3]))
    h2_html = ''.join(f'<h2 style="font-size:22px;font-weight:700;margin:36px 0 12px">{h}</h2><p style="color:hsl(215 45% 16%/.75);line-height:1.75;margin-bottom:8px">{body}</p>' for h, body in cfg['h2s'])
    html = f"""{head(cfg['title'], cfg['desc'], cfg['slug'], schema)}
<body>
{compliance_bar()}
{nav()}
<div class="pb">
<div class="hero"><div class="hero-in">
  <div class="bc"><a href="/index.html">Home</a> › {cfg['h1']}</div>
  <div class="eye"><span class="eye-l"></span><span class="eye-t">{cfg['eyebrow']}</span></div>
  <h1>{cfg['h1']}</h1>
  <p class="hero-sub">{cfg['intro']}</p>
  <p class="upd">Last updated: May 2026 · 134 bookmakers reviewed</p>
</div></div>
<div class="wrap">
  <h2 style="font-size:20px;font-weight:700;margin-bottom:4px">Quick Rankings</h2>
  <p style="color:var(--muted-fg);font-size:14px;margin-bottom:0">All 134 licensed Australian bookmakers rated. Top 10 shown.</p>
  {rank_table(TOP_10)}
  {h2_html}
  <h2 style="font-size:22px;font-weight:700;margin:40px 0 16px">Top 3 Detailed Reviews</h2>
  {cards}
  {int_links(cfg['int'])}
  {faq_html(faqs)}
</div>
</div>
{footer_html()}
</body></html>"""
    return save(cfg['slug'], html)

# ─── REVIEW PAGE GENERATOR ───────────────────────────────────────────────────

def build_review_page(bm):
    slug  = f"review-{bm['slug']}.html"
    title = f"{bm['name']} Review 2026 — Is It Worth Signing Up? | PuntGuide"
    desc  = f"Honest {bm['name']} review for 2026. Odds, markets, app, withdrawal speed, and who it suits — tested with a real account. No fluff."
    faqs  = bm['faqs']
    stars = '★' * int(bm['rating']) + ('½' if bm['rating'] % 1 else '')
    pros  = ''.join(f'<li>{p}</li>' for p in bm['pros'])
    cons  = ''.join(f'<li>{c}</li>' for c in bm['cons'])
    feats = ''.join(f'<span class="feat">{f}</span>' for f in bm['features'])
    schema = faq_schema(faqs) + '\n' + article_schema(title, desc, slug)
    # comparison links to other top 5
    cmp_bms = [b for b in TOP_6 if b['slug'] != bm['slug']][:4]
    cmp_links = [(f"Compare {bm['name']} vs {b['name']}", f"/compare-{bm['slug']}-vs-{b['slug']}.html") for b in cmp_bms]
    other_reviews = [(f"{b['name']} Review", f"/review-{b['slug']}.html") for b in TOP_10 if b['slug'] != bm['slug']][:5]
    all_int = cmp_links + other_reviews + [('All 134 Bookmakers','/all-betting-sites.html'),('Best Betting Sites','/best-betting-sites-australia.html')]
    html = f"""{head(title, desc, slug, schema)}
<body>
{compliance_bar()}
{nav()}
<div class="pb">
<div class="hero"><div class="hero-in">
  <div class="bc"><a href="/index.html">Home</a> › <a href="/bookmakers-australia.html">Bookmakers</a> › {bm['name']} Review</div>
  <div class="eye"><span class="eye-l"></span><span class="eye-t">Independent Review · May 2026</span></div>
  <div style="display:flex;align-items:center;gap:20px;margin-bottom:16px">
    <img src="/{bm['logo']}" alt="{bm['name']}" style="width:80px;height:80px;border-radius:18px;object-fit:contain;background:#fff;box-shadow:var(--sc)">
    <div>
      <h1 style="margin-bottom:6px">{bm['name']} Review 2026</h1>
      <div style="display:flex;align-items:center;gap:10px">
        <span style="color:#f59e0b;font-size:20px">{stars}</span>
        <span style="font-weight:700">{bm['rating']}/5</span>
        <span style="color:var(--muted-fg);font-size:13px">· {bm['type']} · Est. {bm['est']}</span>
      </div>
    </div>
  </div>
  <p class="hero-sub">{bm['desc']}</p>
</div></div>
<div class="wrap">
  <div class="verdict-box"><strong>Our Verdict</strong>"{bm['tagline']}"</div>
  <div class="meta-grid">
    <div class="meta-item"><div class="meta-label">Best for</div><div class="meta-val" style="font-size:13px">{bm['best_for']}</div></div>
    <div class="meta-item"><div class="meta-label">Withdrawals</div><div class="meta-val">{bm['withdraw']}</div></div>
    <div class="meta-item"><div class="meta-label">Min Deposit</div><div class="meta-val">{bm['min_dep']}</div></div>
  </div>
  <h2 style="font-size:20px;font-weight:700;margin:28px 0 14px">Key features</h2>
  <div class="feats">{feats}</div>
  <h2 style="font-size:20px;font-weight:700;margin:28px 0 14px">Pros and cons</h2>
  <div class="pros-cons">
    <div class="pros"><h4>Pros</h4><ul>{pros}</ul></div>
    <div class="cons"><h4>Cons</h4><ul>{cons}</ul></div>
  </div>
  <h2 style="font-size:20px;font-weight:700;margin:28px 0 14px">Who is {bm['name']} best for?</h2>
  <p style="line-height:1.75;color:hsl(215 45% 16%/.8);margin-bottom:12px">
    <strong>Ideal for:</strong> {bm['best_for']}.<br>
    <strong>Not ideal for:</strong> {bm['not_for']}.
  </p>
  <p style="line-height:1.75;color:hsl(215 45% 16%/.8)">{bm['desc']}</p>
  <div style="margin-top:24px"><a href="#" onclick="return false;" class="btn-g">Open {bm['name']} Account →</a></div>
  <p style="font-size:11px;color:var(--muted-fg);margin-top:10px">"Gamble responsibly." · 18+ · T&Cs apply · Gambling Help: 1800 858 858</p>
  {int_links(all_int)}
  {faq_html(faqs)}
</div>
</div>
{footer_html()}
</body></html>"""
    return save(slug, html)

# ─── COMPARISON PAGE GENERATOR ───────────────────────────────────────────────

CMP_ATTRS = [
    ('Odds (AFL/NRL)', {
        'pointsbet':'Sharp','sportsbet':'Competitive','ladbrokes':'Very Sharp','betright':'Good','dabble':'Competitive','neds':'Competitive','bet365':'Good','betr':'Good','picklebet':'Average','unibet':'Good','palmerbet':'Competitive','tab':'Average','betfair':'Best (exchange)','blondebet':'Competitive','chasebet':'Competitive',
    }),
    ('Racing Markets', {
        'pointsbet':'Good','sportsbet':'Good','ladbrokes':'Strong','betright':'Excellent','dabble':'Average','neds':'Good','bet365':'Average','betr':'Average','picklebet':'Limited','unibet':'Average','palmerbet':'Strong','tab':'Excellent','betfair':'Strong','blondebet':'Good','chasebet':'Good',
    }),
    ('Sports Markets', {
        'pointsbet':'Excellent','sportsbet':'Excellent','ladbrokes':'Strong','betright':'Good','dabble':'Strong','neds':'Strong','bet365':'Excellent','betr':'Strong','picklebet':'Strong','unibet':'Strong','palmerbet':'Good','tab':'Good','betfair':'Strong','blondebet':'Good','chasebet':'Good',
    }),
    ('App Quality', {
        'pointsbet':'Very Good','sportsbet':'Excellent','ladbrokes':'Good','betright':'Very Good','dabble':'Excellent','neds':'Very Good','bet365':'Excellent','betr':'Excellent','picklebet':'Very Good','unibet':'Good','palmerbet':'Average','tab':'Good','betfair':'Good','blondebet':'Average','chasebet':'Average',
    }),
    ('Withdrawal Speed', {
        'pointsbet':'Same day','sportsbet':'1–2 days','ladbrokes':'1–3 days','betright':'Same day','dabble':'Same day','neds':'1–2 days','bet365':'1–3 days','betr':'Same day','picklebet':'Same day','unibet':'1–3 days','palmerbet':'1–2 days','tab':'1–3 days','betfair':'1–2 days','blondebet':'1–2 days','chasebet':'1–2 days',
    }),
    ('Account Treatment', {
        'pointsbet':'Good','sportsbet':'Poor','ladbrokes':'Poor','betright':'Good','dabble':'Good','neds':'Poor','bet365':'Poor','betr':'Good','picklebet':'Good','unibet':'Average','palmerbet':'Excellent','tab':'Good','betfair':'Excellent','blondebet':'Good','chasebet':'Good',
    }),
    ('Live Streaming', {
        'pointsbet':'No','sportsbet':'No','ladbrokes':'No','betright':'No','dabble':'No','neds':'No','bet365':'Yes','betr':'No','picklebet':'No','unibet':'No','palmerbet':'No','tab':'Partial','betfair':'Partial','blondebet':'No','chasebet':'No',
    }),
]

def cmp_winner(val1, val2):
    order = ['Excellent','Very Sharp','Same day','Yes','Best (exchange)','Very Good','Sharp','Strong','Excellent app','1–2 days','Good','Competitive','Partial','Average','1–3 days','Limited','Poor','No']
    try:
        i1, i2 = order.index(val1) if val1 in order else 99, order.index(val2) if val2 in order else 99
    except:
        i1, i2 = 99, 99
    return 1 if i1 < i2 else (2 if i2 < i1 else 0)

def build_comparison_page(bm1, bm2):
    slug  = f"compare-{bm1['slug']}-vs-{bm2['slug']}.html"
    title = f"{bm1['name']} vs {bm2['name']} 2026 — Which is Better? | PuntGuide"
    desc  = f"Honest {bm1['name']} vs {bm2['name']} comparison for 2026. Odds, markets, app, withdrawals, and account treatment compared side by side."
    faqs  = [
        (f"Is {bm1['name']} better than {bm2['name']}?",
         f"It depends on what you bet on. {bm1['name']} is best for {bm1['best_for'].lower()}. {bm2['name']} is best for {bm2['best_for'].lower()}. Many punters hold accounts with both."),
        (f"Which has better odds — {bm1['name']} or {bm2['name']}?",
         f"Odds vary by market and event. {bm1['name']} tends to be stronger on {bm1['type'].lower()} markets, while {bm2['name']} is competitive on {bm2['type'].lower()} markets. Compare before each bet for the best value."),
        (f"Which is better for racing — {bm1['name']} or {bm2['name']}?",
         f"{('BetRight' if bm1['slug']=='betright' else bm1['name'] if bm1['type']=='Racing Specialist' else bm2['name'])} is generally stronger for racing. BetRight is our overall top pick for Australian racing. Ladbrokes and Tab are also strong choices for racing punters."),
        (f"Can I have accounts with both {bm1['name']} and {bm2['name']}?",
         f"Yes. It is legal and common to hold accounts with multiple Australian bookmakers. Most serious punters hold 3–5 accounts to access the best odds across different markets."),
        (f"Which is better for sports betting — {bm1['name']} or {bm2['name']}?",
         f"{bm1['name']} is best for {bm1['best_for'].lower()}. {bm2['name']} is best for {bm2['best_for'].lower()}. For the widest sports market range, Sportsbet and Bet365 lead the Australian market."),
    ]
    schema = faq_schema(faqs) + '\n' + article_schema(title, desc, slug)
    stars1 = '★' * int(bm1['rating']) + ('½' if bm1['rating'] % 1 else '')
    stars2 = '★' * int(bm2['rating']) + ('½' if bm2['rating'] % 1 else '')
    # build comparison table
    rows = ''
    for attr, vals in CMP_ATTRS:
        v1 = vals.get(bm1['slug'], '—')
        v2 = vals.get(bm2['slug'], '—')
        w  = cmp_winner(v1, v2)
        c1 = ' class="win"' if w == 1 else ''
        c2 = ' class="win"' if w == 2 else ''
        rows += f'<tr><td>{attr}</td><td{c1}>{v1}</td><td{c2}>{v2}</td></tr>'
    # pros of each
    pros1 = ''.join(f'<li>{p}</li>' for p in bm1['pros'][:3])
    pros2 = ''.join(f'<li>{p}</li>' for p in bm2['pros'][:3])
    all_int = [
        (f"{bm1['name']} Full Review", f"/review-{bm1['slug']}.html"),
        (f"{bm2['name']} Full Review", f"/review-{bm2['slug']}.html"),
        ('Compare All Betting Sites','/compare-betting-sites.html'),
        ('Best Betting Sites Australia','/best-betting-sites-australia.html'),
        ('All 134 Bookmakers','/all-betting-sites.html'),
    ]
    html = f"""{head(title, desc, slug, schema)}
<body>
{compliance_bar()}
{nav()}
<div class="pb">
<div class="hero"><div class="hero-in">
  <div class="bc"><a href="/index.html">Home</a> › <a href="/compare-betting-sites.html">Compare</a> › {bm1['name']} vs {bm2['name']}</div>
  <div class="eye"><span class="eye-l"></span><span class="eye-t">Side-by-Side · May 2026</span></div>
  <h1>{bm1['name']} vs {bm2['name']} 2026</h1>
  <p class="hero-sub">Which is better — {bm1['name']} or {bm2['name']}? We compared odds, markets, app quality, withdrawal speed, and account treatment with real accounts. Here is our honest verdict.</p>
</div></div>
<div class="wrap">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:32px">
    <div class="card" style="text-align:center">
      <img src="/{bm1['logo']}" alt="{bm1['name']}" style="width:72px;height:72px;border-radius:16px;object-fit:contain;background:#fff;box-shadow:var(--sc);margin-bottom:12px">
      <h2 style="font-size:18px;margin-bottom:4px">{bm1['name']}</h2>
      <div style="color:#f59e0b;font-size:16px;margin-bottom:8px">{stars1}</div>
      <p style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">{bm1['tagline']}</p>
      <a href="#" onclick="return false;" class="btn-g">Bet Now →</a>
    </div>
    <div class="card" style="text-align:center">
      <img src="/{bm2['logo']}" alt="{bm2['name']}" style="width:72px;height:72px;border-radius:16px;object-fit:contain;background:#fff;box-shadow:var(--sc);margin-bottom:12px">
      <h2 style="font-size:18px;margin-bottom:4px">{bm2['name']}</h2>
      <div style="color:#f59e0b;font-size:16px;margin-bottom:8px">{stars2}</div>
      <p style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">{bm2['tagline']}</p>
      <a href="#" onclick="return false;" class="btn-g">Bet Now →</a>
    </div>
  </div>
  <h2 style="font-size:20px;font-weight:700;margin-bottom:14px">Head-to-Head Comparison</h2>
  <table class="cmp-table">
    <thead><tr><th>Category</th><th>{bm1['name']}</th><th>{bm2['name']}</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
  <h2 style="font-size:20px;font-weight:700;margin:32px 0 14px">Pros: {bm1['name']}</h2>
  <div class="pros" style="margin-bottom:16px"><ul>{pros1}</ul></div>
  <h2 style="font-size:20px;font-weight:700;margin-bottom:14px">Pros: {bm2['name']}</h2>
  <div class="pros"><ul>{pros2}</ul></div>
  <h2 style="font-size:20px;font-weight:700;margin:32px 0 14px">Our Verdict</h2>
  <p style="line-height:1.75;color:hsl(215 45% 16%/.8);margin-bottom:12px">
    <strong>{bm1['name']}</strong> is the better choice if you want {bm1['best_for'].lower()}.
    <strong>{bm2['name']}</strong> is the better choice if you want {bm2['best_for'].lower()}.
    Many serious Australian punters hold accounts with both — giving them access to the best odds across different market types.
  </p>
  {int_links(all_int)}
  {faq_html(faqs)}
</div>
</div>
{footer_html()}
</body></html>"""
    return save(slug, html)

# ─── SITEMAP ─────────────────────────────────────────────────────────────────

EXISTING_URLS = [
    'index.html','best-betting-sites-australia.html','all-betting-sites.html',
    'which-betting-sites-worth-using-australia.html','fastest-withdrawal-betting-sites-australia.html',
    'fastest-payout-betting-sites-australia.html','best-betting-apps-australia.html',
    'new-betting-sites-australia.html','best-betting-sites-afl-nrl.html',
    'best-betting-sites-for-afl.html','best-betting-sites-for-racing.html',
    'nrl-premiership-odds-2026.html','afl-premiership-odds-2026.html',
    'nrl-round-10-tips-2026.html','afl-round-8-tips-2026.html',
    'racing-futures-2026.html','racing-weekend-may2-2026.html',
]

def update_sitemap(new_slugs):
    all_urls = EXISTING_URLS + new_slugs
    urls_xml = ''
    for u in all_urls:
        priority = '1.0' if u == 'index.html' else ('0.9' if 'best-' in u or 'top-' in u or 'compare' in u else ('0.8' if 'review-' in u else '0.7'))
        freq = 'weekly'
        urls_xml += f'  <url><loc>https://puntguide.com.au/{u}</loc><changefreq>{freq}</changefreq><priority>{priority}</priority></url>\n'
    sitemap = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls_xml}</urlset>'
    with open(os.path.join(OUT, 'sitemap.xml'), 'w') as f:
        f.write(sitemap)
    print(f'  ✓ sitemap.xml ({len(all_urls)} URLs)')

# ─── MAIN ────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    generated = []

    print('\n── List & Category Pages ──')
    for cfg in LIST_PAGES:
        generated.append(build_list_page(cfg))

    print('\n── Brand Review Pages ──')
    for bm in BMS:
        generated.append(build_review_page(bm))

    print('\n── Comparison Pages ──')
    for bm1, bm2 in combinations(TOP_6, 2):
        generated.append(build_comparison_page(bm1, bm2))

    print('\n── Sitemap ──')
    update_sitemap(generated)

    print(f'\n✅ Done — {len(generated)} pages generated\n')
