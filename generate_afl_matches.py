#!/usr/bin/env python3
"""
AFL Match Page Generator — Rich Analysis Edition
Usage: edit ROUND and MATCHES below, then run python3 generate_afl_matches.py
"""
import os, json

OUT  = os.path.expanduser('~/puntguide')
SITE = 'https://puntguide.com.au'

ROUND      = 8
ROUND_YEAR = 2026

TEAMS = {
    'Collingwood':       dict(short='COLL', colour='#000000'),
    'Hawthorn':          dict(short='HAW',  colour='#4D2004'),
    'Western Bulldogs':  dict(short='WB',   colour='#014896'),
    'Fremantle':         dict(short='FRE',  colour='#2A1A5E'),
    'Adelaide Crows':    dict(short='ADEL', colour='#002B5C'),
    'Port Adelaide':     dict(short='PORT', colour='#008AAB'),
    'Essendon':          dict(short='ESS',  colour='#CC2529'),
    'Brisbane Lions':    dict(short='BL',   colour='#A30046'),
    'West Coast Eagles': dict(short='WCE',  colour='#003087'),
    'Richmond':          dict(short='RICH', colour='#FFD200'),
    'Geelong Cats':      dict(short='GEE',  colour='#1C3F6E'),
    'North Melbourne':   dict(short='NM',   colour='#003A6B'),
    'Carlton':           dict(short='CARL', colour='#002147'),
    'St Kilda':          dict(short='STK',  colour='#ED0F05'),
    'Sydney Swans':      dict(short='SYD',  colour='#CC0000'),
    'Melbourne':         dict(short='MELB', colour='#CC2529'),
    'Gold Coast SUNS':   dict(short='GCS',  colour='#E8281B'),
    'GWS GIANTS':        dict(short='GWS',  colour='#F15C22'),
}

MATCHES = [
    dict(
        team1='Collingwood', team2='Hawthorn',
        date='Thursday, April 30, 2026', time=None, venue='MCG',
        status='result', result='COLL 93, HAW 93',
        tip=None, tip_margin=None,
        summary="One of the most memorable draws in recent AFL history. Both sides traded blows across four quarters in a MCG blockbuster that ended all square.",
        analysis="""Collingwood and Hawthorn produced a remarkable draw at the MCG on Thursday night, finishing locked at 93 points apiece in what was one of the competition's best games of 2026. The Magpies entered the match off the back of their dominant Anzac Day victory over Essendon while Hawthorn came in riding a league-high six-game winning streak.

Hawthorn were heavy favourites heading in, with analysts giving them a 75% chance of winning based on their blistering recent form. The Hawks had crushed Gold Coast by 49 points the week before and appeared to have superior firepower across the ground. Collingwood, however, refused to capitulate — with Darcy Moore's return from injury giving their backline added composure.

The game was decided on the finest of margins. Both sides had opportunities to win in the dying stages but neither could convert, leaving the MCG crowd on their feet for a finish that will be talked about for years. The result leaves Hawthorn's winning streak at six games (with one draw) and Collingwood in a similar position — competitive but yet to truly cement their place as a contender.""",
        form1='W W W W L', form2='W W W W W',
        record1='4-2-1', record2='6-0-1',
        key_player1='Darcy Moore (returns from injury, key to defensive structure)',
        key_player2='Will Day (midfield engine, driving Hawks\' winning streak)',
        key_matchup='Collingwood midfield vs Hawthorn\'s contested ball — the winner of this battle won it last week',
        stats='Hawthorn: 75% win probability pre-game · Collingwood: Won Anzac Day clash by 72 pts · H2H: Hawthorn won 4 of last 6',
        markets='Head-to-head: COLL $3.25 / HAW $1.33 pre-game · Line: HAW –20.5',
    ),
    dict(
        team1='Western Bulldogs', team2='Fremantle',
        date='Friday, May 1, 2026', time='7:30 PM', venue='Marvel Stadium',
        status='upcoming', result=None,
        tip='Fremantle', tip_margin='11–25',
        summary="Fremantle travel to Marvel Stadium as strong favourites over an injury-depleted Bulldogs side. The Dockers have been one of 2026's standout teams and should have too much class here.",
        analysis="""Fremantle arrive at Marvel Stadium as firm favourites in what shapes as a significant test for the Western Bulldogs' season. The Dockers sit 6-1 through seven games and have established themselves as one of the genuine contenders for the 2026 premiership. Their depth across every line of the ground is arguably unmatched in the competition at this stage of the season.

The Western Bulldogs, by contrast, have been undermanned for several weeks. Multiple long-term injuries to key players have left coach Luke Beveridge with difficult selection calls week to week. The Bulldogs were competitive against Sydney last time out but conceded the game in the third quarter — a similar pattern to recent weeks where their depth is exposed as matches wear on.

Fremantle won both of their meetings against the Western Bulldogs in 2025 and that familiarity should count for something. The Dockers' height advantage across multiple positions — particularly in their forward line — should be telling at Marvel Stadium where the compact ground suits taller, marking forwards. Expect Fremantle to control this game through their midfield and deliver a comfortable win, potentially running away in the final quarter as the Bulldogs run short of legs.""",
        form1='W L L W L', form2='W W W W W',
        record1='3-4', record2='6-1',
        key_player1='Marcus Bontempelli (needs a massive game to keep Dogs competitive)',
        key_player2='Andrew Brayshaw (Fremantle\'s midfield general, averaging 32+ disposals)',
        key_matchup='Fremantle\'s forward line height vs Bulldogs\' depleted backline — the Dockers\' marking game should dominate',
        stats='Fremantle: 66–68% win probability · Bulldogs: Conceded 40+ pts in Q3 of last 3 games · Freo won both 2025 meetings',
        markets='Head-to-head: WB $3.10 / FRE $1.38 · Line: FRE –21.5 · Tip: Fremantle to win outright',
    ),
    dict(
        team1='Adelaide Crows', team2='Port Adelaide',
        date='Friday, May 1, 2026', time='8:10 PM', venue='Adelaide Oval',
        status='upcoming', result=None,
        tip='Adelaide Crows', tip_margin='1–18',
        summary="The 36th Showdown at Adelaide Oval. Both sides enter at 3-4 and desperate for a confidence-boosting win in one of football's most intense rivalries.",
        analysis="""There is no match in Australian football that carries quite the same tribal intensity as the Showdown, and Round 8 delivers another one — albeit between two teams who have both had seasons that have fallen short of expectations. Adelaide and Port Adelaide come in at 3-4, locked together on the ladder and each desperate to use this rivalry fixture as a launching pad for the rest of 2026.

Adelaide have shown strong recovery ability from setbacks throughout the season. The Crows suffered a heavy defeat the previous week but historically respond well when their pride is on the line in Showdown fixtures. Home-crowd advantage nominally belongs to neither side at Adelaide Oval, though the Crows have traditionally performed better in the fixture across recent seasons.

Port Adelaide's form has been more impressive when it has clicked — notably their upset win over Geelong was one of the month's biggest results. However, the Power have been inconsistent from week to week and cannot be fully trusted on that basis. Our tip is Adelaide, who at $1.50 to win offer value given the uncertain nature of Showdown football. The line at –12.5 is tight and could be value on Adelaide, who have covered this spread in 3 of their last 4 Showdown appearances. Both clubs enter at 3-4 and neither can afford to lose ground on the top eight at this point in the season.""",
        form1='L W L W L', form2='W L W L W',
        record1='3-4', record2='3-4',
        key_player1='Taylor Walker (Crows veteran crucial in Showdown pressure moments)',
        key_player2='Connor Rozee (Port\'s most dangerous forward, must be tagged)',
        key_matchup='Adelaide midfield clearance vs Port\'s half-back structure — the team that wins contested ball wins the Showdown',
        stats='Adelaide: 62% win probability · H2H: Crows won 3 of last 5 Showdowns · Port: Upset Geelong Round 7',
        markets='Head-to-head: ADEL $1.50 / PORT $2.55 · Line: ADEL –12.5 · Tip: Adelaide –12.5 line',
    ),
    dict(
        team1='Essendon', team2='Brisbane Lions',
        date='Saturday, May 2, 2026', time='12:35 PM', venue='Marvel Stadium',
        status='upcoming', result=None,
        tip='Brisbane Lions', tip_margin='30+',
        summary="Brisbane Lions are enormous favourites for this Saturday lunchtime clash. A significant class gap exists between these two sides right now and the Lions are expected to win by 40+ points.",
        analysis="""There is a significant gap between Brisbane Lions and Essendon at this point in 2026 — and the betting markets reflect it accurately. The Lions enter as massive favourites and rightly so. Brisbane have been one of the competition's most powerful sides this year, combining a penetrating kick-to-hand game, relentless forward pressure, and a backline structure that has conceded the fewest points of any team in the top eight.

Essendon, meanwhile, have been inconsistent and injury-depleted in 2026. The Bombers showed they can compete on their best days — their Anzac Day victory earlier in the season demonstrated their ceiling — but they have also been blown off the park by elite opposition. Against a Brisbane outfit clicking on all cylinders, the risk of a 10-goal blowout is real.

Brisbane's forward line is a particular concern for Essendon's defence. The Lions' ability to win contested ball through the midfield and deliver quickly to their forwards has been the key driver of their success. Unless Essendon channel the intensity of their best 2026 performances, this is a match that could get very ugly very quickly. The +40.5 line is the market to watch — Brisbane have covered this margin against comparable opposition multiple times this season.""",
        form1='L W L L W', form2='W W W W W',
        record1='3-4', record2='6-1',
        key_player1='Zach Merrett (Essendon\'s only realistic chance of keeping it close through the midfield)',
        key_player2='Lachie Neale (Brisbane captain and engine, averaging 32+ disposals, dominant all year)',
        key_matchup='Brisbane\'s forward line firepower vs Essendon\'s depleted defence — the Lions\' pressure should win this quickly',
        stats='Brisbane: 89% win probability · Predicted margin: 32–77 points · Brisbane averaging +22 margin in 2026',
        markets='Head-to-head: ESS $6.50 / BL $1.12 · Line: BRL –40.5 · Tip: Brisbane to win, consider the line',
    ),
    dict(
        team1='West Coast Eagles', team2='Richmond',
        date='Saturday, May 2, 2026', time='4:15 PM', venue='Optus Stadium',
        status='upcoming', result=None,
        tip='West Coast Eagles', tip_margin='15–30',
        summary="West Coast Eagles host Richmond at Optus Stadium in a battle between two bottom-half sides. The Eagles' home advantage and greater commitment should be decisive.",
        analysis="""This is a fascinating match between two clubs at the bottom end of the ladder who have both been disappointing in 2026 for different reasons. West Coast Eagles at Optus Stadium, however, are a genuinely difficult proposition even in their current state — the roar of the Perth crowd adds five to ten points to their performance and the Tigers simply cannot replicate that on the road.

Both West Coast and Richmond rank among the worst teams in the competition for scoring and among the highest for turnovers. However, West Coast have shown greater defensive commitment — particularly at home where Optus Stadium's large surface suits their run-and-spread game. Richmond, by contrast, have appeared resigned to their position in 2026, lacking the intensity that defined their premiership era.

The line at –16.5 favours West Coast and the market has moved toward –20.5 as the week progresses — indicating significant smart money on the Eagles. West Coast beat Richmond comprehensively at Optus Stadium in 2025 and the trend suggests another comfortable home win. The Eagles have more to play for — particularly with a home crowd watching — while Richmond appear to be playing for draft picks at this stage of their rebuild.""",
        form1='L W W L W', form2='L L L L W',
        record1='3-4', record2='1-6',
        key_player1='Jack Darling (key forward at home, knows this ground better than anyone)',
        key_player2='Dustin Martin (if he fires, Tigers stay in it — if he\'s quiet, they lose by 30+)',
        key_matchup='West Coast\'s forward structure at Optus vs Richmond\'s leaky defence — Eagles should dominate in the air',
        stats='West Coast: 64% win probability · Richmond: 1W–6L, bottom of ladder · Market movement: WCE line –16.5 to –20.5',
        markets='Head-to-head: WCE $1.57 / RICH $2.30 · Line: WCE –16.5 · Tip: West Coast –16.5',
    ),
    dict(
        team1='Geelong Cats', team2='North Melbourne',
        date='Saturday, May 2, 2026', time='4:35 PM', venue='GMHBA Stadium',
        status='upcoming', result=None,
        tip='Geelong Cats', tip_margin='15–30',
        summary="Geelong seek their 15th consecutive win over North Melbourne at GMHBA Stadium. The Cats are heavy favourites but the spread looks inflated after their shock Port Adelaide loss.",
        analysis="""Geelong Cats versus North Melbourne at GMHBA Stadium is on paper one of the easier games to tip this round. The Cats have beaten the Roos in their last 14 consecutive meetings and that sequence has no end in sight. Jeremy Cameron in particular has been extraordinary against North Melbourne — he has dominated the Roos defenders so comprehensively that coaches have been forced to throw multiple bodies at him, which then opens up teammates.

However, the 28.5-point spread is worth interrogating. Geelong had a rough time in Round 7, losing to Port Adelaide in a result that exposed some defensive vulnerabilities they haven't shown all season. The Cats were clearly below their best and that needs to be factored in. North Melbourne, meanwhile, pushed GWS Giants to within single figures in their last game — a performance that suggests they are competitive even if they are unlikely to win.

The prudent betting angle here might be North Melbourne +28.5 rather than a Geelong win outright. The Cats should win — their home ground, class, and depth are all significant advantages — but whether they do so by 29+ points is much less certain given their recent form inconsistency. The Cats are 81% favourites to win the match; the line is a separate question entirely.""",
        form1='W L W W L', form2='L W L L W',
        record1='5-2', record2='2-5',
        key_player1='Jeremy Cameron (has dominated the Roos in recent years, likely to kick 3+ goals)',
        key_player2='Luke Davies-Uniacke (NM\'s midfield leader, the player most likely to keep it close)',
        key_matchup='Geelong\'s half-back run vs North Melbourne\'s forward pressure — the Cats\' transition game is their biggest weapon',
        stats='Geelong: 81% win probability · 14 consecutive wins over North Melbourne · GEE lost to Port Adelaide Round 7',
        markets='Head-to-head: GEE $1.22 / NM $4.40 · Line: GEE –28.5 · Value tip: NM +28.5',
    ),
    dict(
        team1='Carlton', team2='St Kilda',
        date='Saturday, May 2, 2026', time='7:35 PM', venue='Marvel Stadium',
        status='upcoming', result=None,
        tip='St Kilda', tip_margin='10–21',
        summary="St Kilda are the surprise favourites here, with Carlton sitting 16th on the ladder. The Saints arrive at Marvel with superior form and structural defensive advantages.",
        analysis="""This is one of the more intriguing matches of the round on paper, and the result of the week's biggest upset potential. Carlton currently sit 16th on the AFL ladder — a position that defies their preseason billing as a genuine finals contender — while St Kilda have been quietly building something in 2026 that has flying under the radar.

The Saints' defensive structure has been notably more organised than Carlton's this season. St Kilda have conceded the fewest points of any team in the bottom half of the competition and their defensive unit has beaten Carlton's forward line in two of the last three meetings. Tom De Koning and Jack Silvagni — both former Blues who left under a cloud — will be highly motivated against their old club on Saturday night.

Carlton have shown moments of competitiveness but their inability to win the close games has left them marooned at the bottom of the ladder. The Blues are 37% to win here according to the predictive models, which may actually be generous given how poor their recent form has been. St Kilda at –13.5 line is the market that stands out. The Saints have covered this margin in their last two victories and look set for another structured defensive win at Marvel Stadium.""",
        form1='L L W L L', form2='W W L W W',
        record1='1-6', record2='4-3',
        key_player1='Patrick Cripps (Blues captain needs to drag them into the contest — has been below his best in 2026)',
        key_player2='Jack Sinclair (St Kilda\'s half-back flanker, drives their transition and run)',
        key_matchup='St Kilda\'s defensive structure vs Carlton\'s forward line — the Saints have smothered rival forward lines all season',
        stats='St Kilda: 63% win probability · Carlton: 16th on ladder, 1W–6L · De Koning & Silvagni (ex-Carlton) face Blues',
        markets='Head-to-head: CARL $2.68 / STK $1.50 · Line: STK –13.5 · Tip: St Kilda –13.5',
    ),
    dict(
        team1='Sydney Swans', team2='Melbourne',
        date='Sunday, May 3, 2026', time='3:15 PM', venue='SCG',
        status='upcoming', result=None,
        tip='Sydney Swans', tip_margin='20–40',
        summary="Sydney are massive favourites at the SCG against a Melbourne side that has struggled badly away from the MCG in 2026. The Swans have been one of the year's standout teams.",
        analysis="""Sydney Swans have been one of the stories of 2026 — their percentage and form on the road and at the SCG has been outstanding. The Swans enter this game as enormous 85% favourites and the analytics back that up. Their midfield depth, defensive structure and forward-line efficiency have all ranked inside the top three all year, and at the SCG — where the shorter boundaries suit their handball-and-run game — they have been virtually unbeatable.

Melbourne, conversely, have been one of the season's biggest disappointments. The Demons have an impressive record when playing at the MCG but have struggled markedly in away games — a trend that has cost them dearly in 2026. Travelling to the SCG to face a Sydney side in this form is about as difficult as it gets. The Demons' forward line has found it hard to generate consistent scoring opportunities away from the MCG's open expanses.

The predicted margin from multiple analysts ranges from 19 to 40 points in Sydney's favour. The Swans' 'percentage indicator' — their points for versus against ratio — reveals they are outperforming Melbourne by a significant margin despite having a similar win-loss record on paper. Sydney at –32.5 line is strong and reflects a performance level the Swans have demonstrated consistently. A 30+ point Sydney win is the most likely outcome here.""",
        form1='W W W W W', form2='L L W L W',
        record1='6-1', record2='3-4',
        key_player1='Lance Franklin (if fit and selected, his experience and SCG knowledge is invaluable)',
        key_player2='Christian Petracca (Demons\' most dangerous player — must be shut down for Melbourne to stay competitive)',
        key_matchup='Sydney\'s midfield depth vs Melbourne\'s contested clearances — the Swans have won this battle all year',
        stats='Sydney: 85% win probability · Melbourne: 0W–3L away from MCG in 2026 · Predicted margin: 19–40 pts',
        markets='Head-to-head: SYD $1.18 / MELB $4.85 · Line: SYD –32.5 · Tip: Sydney to win & cover the line',
    ),
    dict(
        team1='Gold Coast SUNS', team2='GWS GIANTS',
        date='Sunday, May 3, 2026', time='7:20 PM', venue='People First Stadium',
        status='upcoming', result=None,
        tip='GWS GIANTS', tip_margin='1–13',
        summary="GWS GIANTS head north as slight favourites with an impressive recent head-to-head record. This is one of the round's tightest matches on paper with minimal separating the two sides.",
        analysis="""This Sunday night clash between Gold Coast SUNS and GWS GIANTS is one of the round's most evenly matched contests and the hardest to predict with confidence. The GIANTS hold a 16 wins from 21 meetings head-to-head record against the Suns across their AFL history, which gives them a psychological edge regardless of current form.

GWS enter with genuine momentum — they defeated North Melbourne in their last outing and have been one of the more consistent sides in the middle of the competition in 2026. Their midfield features one of the most feared combinations in the AFL with Josh Kelly, Tom Green and the returning Jacob Hopper all capable of dominating on their day. The interstate travel from Sydney to the Gold Coast is also significantly less taxing than most away trips in the competition.

Gold Coast have been competitive at People First Stadium this year and their young list has shown genuine improvement across the 2026 season. The Suns were given a 70% chance of winning in some modelling but the market disagrees — reflecting GWS's superior head-to-head record and midfield depth. The former Melbourne teammates Christian Petracca (Demons) and Bailey Smith (Suns) face off in an interesting subplot. This is genuinely 50-50 and punters should approach with caution — it is not a match to take a strong line on.""",
        form1='L W L W W', form2='W W L W W',
        record1='3-4', record2='4-3',
        key_player1='Touk Miller (Gold Coast\'s midfield captain, sets the tone for the Suns — must be best on ground for GCS to win)',
        key_player2='Josh Kelly (GWS midfield elite — when he dominates, the Giants win comfortably)',
        key_matchup='GWS midfield trio vs Gold Coast\'s wing play — whichever team controls transition will control this game',
        stats='GWS: H2H 16W from 21 meetings · Gold Coast: 70% modelling win probability vs market disagreement · Tight match',
        markets='Head-to-head: GCS $2.10 / GWS $1.75 · Line: GWS –6.5 · Tip: GWS –6.5 line (value)',
    ),
]

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
.bc{font-size:12px;color:var(--muted-fg);margin-bottom:10px;}
.bc a{color:var(--muted-fg);text-decoration:none;}
.eye{display:flex;align-items:center;gap:10px;margin-bottom:12px;}
.eye-l{height:1px;width:32px;background:var(--primary);}
.eye-t{font-family:"JetBrains Mono",monospace;font-size:11px;color:var(--primary);text-transform:uppercase;letter-spacing:.2em;}
.wrap{max-width:1100px;margin:0 auto;padding:44px 32px 80px;}
.matchup{background:#fff;border:1px solid var(--border);border-radius:16px;padding:28px;margin:28px 0;box-shadow:var(--sc);text-align:center;}
.teams{display:flex;align-items:center;justify-content:center;gap:24px;margin-bottom:16px;flex-wrap:wrap;}
.team-block{display:flex;flex-direction:column;align-items:center;gap:8px;}
.team-badge{width:64px;height:64px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:14px;color:#fff;flex-shrink:0;}
.team-name{font-weight:700;font-size:15px;max-width:130px;text-align:center;line-height:1.3;}
.vs{font-family:"JetBrains Mono",monospace;font-size:18px;font-weight:700;color:var(--muted-fg);}
.match-meta{display:flex;justify-content:center;gap:20px;flex-wrap:wrap;font-size:13px;color:var(--muted-fg);border-top:1px solid var(--border);padding-top:14px;margin-top:4px;}
.form-row{display:flex;gap:6px;justify-content:center;margin-top:4px;}
.form-dot{width:24px;height:24px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:700;color:#fff;}
.form-w{background:hsl(140 50% 40%);}
.form-l{background:hsl(16 70% 45%);}
.form-d{background:hsl(215 30% 60%);}
.tip-box{background:hsl(140 50% 97%);border:1px solid hsl(140 50% 85%);border-radius:12px;padding:20px 24px;margin:20px 0;}
.tip-box h3{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:hsl(140 50% 32%);margin-bottom:8px;}
.tip-team{font-size:22px;font-weight:800;color:hsl(140 40% 28%);margin-bottom:4px;}
.analysis-section{background:#fff;border:1px solid var(--border);border-radius:14px;padding:24px 28px;margin:20px 0;box-shadow:var(--sc);}
.analysis-section h2{font-size:18px;font-weight:700;margin-bottom:14px;padding-bottom:10px;border-bottom:1px solid var(--border);}
.stat-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin:14px 0;}
.stat-item{background:var(--muted);border-radius:8px;padding:12px 14px;}
.stat-label{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:4px;}
.stat-val{font-size:13px;font-weight:600;line-height:1.4;}
.kp-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:14px 0;}
.kp-item{background:var(--muted);border-radius:8px;padding:12px 14px;}
.kp-team{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:4px;}
.kp-name{font-size:13px;font-weight:700;margin-bottom:3px;}
.kp-desc{font-size:12px;color:var(--muted-fg);line-height:1.4;}
.markets-box{background:hsl(48 80% 97%);border:1px solid hsl(48 60% 85%);border-radius:10px;padding:16px 20px;margin:14px 0;}
.markets-box h4{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:hsl(48 60% 38%);margin-bottom:8px;}
.card{background:#fff;border:1px solid var(--border);border-radius:14px;padding:20px 24px;margin-bottom:16px;box-shadow:var(--sc);}
.bm-row{display:flex;align-items:center;gap:14px;}
.bm-logo{width:44px;height:44px;border-radius:10px;object-fit:contain;background:#fff;box-shadow:var(--sc);flex-shrink:0;}
.int-links{background:#fff;border:1px solid var(--border);border-radius:12px;padding:18px 22px;margin:28px 0;}
.int-links h3{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--muted-fg);margin-bottom:12px;}
.int-links a{display:inline-block;background:var(--muted);border-radius:6px;padding:5px 11px;margin:3px;font-size:13px;font-weight:500;text-decoration:none;color:var(--fg);}
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
.footer-rg{font-size:11px;color:rgba(255,255,255,.4);border-top:1px solid rgba(255,255,255,.1);padding-top:20px;line-height:1.8;}
.footer-rg a{color:rgba(255,255,255,.4);}
@media(max-width:768px){.nav-links{display:none;}.wrap,.hero{padding-left:16px;padding-right:16px;}.nav{padding:0 20px;}.teams{gap:12px;}.stat-grid,.kp-grid{grid-template-columns:1fr;}}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800&family=Inter+Tight:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">'

TOP_BOOKMAKERS = [
    dict(name='PointsBet', slug='pointsbet', logo='pointsbet.png', tagline='Sharpest AFL odds + PointsBetting markets'),
    dict(name='Sportsbet',  slug='sportsbet',  logo='sportsbet.png',  tagline='Widest AFL market range in Australia'),
    dict(name='Ladbrokes',  slug='ladbrokes',  logo='ladbrokes.png',  tagline='Consistently competitive AFL head-to-head prices'),
]

def team_slug(name):
    return name.lower().replace(' ', '-').replace('.', '')

def match_slug(m):
    return f"afl-{team_slug(m['team1'])}-vs-{team_slug(m['team2'])}-round-{ROUND}-{ROUND_YEAR}.html"

def form_dots(form_str):
    html = ''
    for ch in form_str.split():
        cls = 'form-w' if ch == 'W' else ('form-l' if ch == 'L' else 'form-d')
        html += f'<span class="form-dot {cls}">{ch}</span>'
    return html

def faq_schema(faqs):
    items = ','.join([f'{{"@type":"Question","name":{json.dumps(q)},"acceptedAnswer":{{"@type":"Answer","text":{json.dumps(a)}}}}}' for q,a in faqs])
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{items}]}}</script>'

def article_schema(title, desc, slug):
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":{json.dumps(title)},"description":{json.dumps(desc)},"author":{{"@type":"Organization","name":"PuntGuide"}},"publisher":{{"@type":"Organization","name":"PuntGuide","logo":{{"@type":"ImageObject","url":"{SITE}/favicon-192.png"}}}},"datePublished":"2026-04-30","dateModified":"2026-05-01","mainEntityOfPage":"{SITE}/{slug}","image":{{"@type":"ImageObject","url":"{SITE}/favicon-192.png"}}}}</script>'

def build_match_page(m):
    slug    = match_slug(m)
    t1      = m['team1']
    t2      = m['team2']
    t1d     = TEAMS.get(t1, dict(short=t1[:4].upper(), colour='#333'))
    t2d     = TEAMS.get(t2, dict(short=t2[:4].upper(), colour='#333'))
    is_done = m['status'] == 'result'

    if is_done:
        title   = f"{t1} vs {t2} Result — AFL Round {ROUND} {ROUND_YEAR} | PuntGuide"
        desc    = f"{t1} vs {t2} AFL Round {ROUND} result: {m['result']}. Full match analysis, key moments and what the result means for the season."
        h1      = f"{t1} vs {t2} — AFL Round {ROUND} Result"
        eyebrow = f"AFL Round {ROUND} · {m['date']} · Final Result"
    else:
        title   = f"{t1} vs {t2} Tips, Odds & Prediction — AFL Round {ROUND} {ROUND_YEAR} | PuntGuide"
        desc    = f"Expert {t1} vs {t2} AFL Round {ROUND} tips, odds and analysis. Team form, key players, head-to-head stats and our best bet for this match."
        h1      = f"{t1} vs {t2} — AFL Round {ROUND} Tips & Prediction"
        eyebrow = f"AFL Round {ROUND} · {m['date']} · {m.get('time','')}"

    # Build FAQs
    if is_done:
        faqs = [
            (f"What was the result of {t1} vs {t2} in AFL Round {ROUND}?",
             f"{t1} vs {t2} finished: {m['result']} in AFL Round {ROUND} {ROUND_YEAR}. {m['summary']}"),
            (f"Where was AFL Round {ROUND} {t1} vs {t2} played?",
             f"The match was played at {m['venue']} on {m['date']}."),
            (f"What was the key storyline in {t1} vs {t2}?", m['analysis'].split('\n\n')[0]),
            (f"Which bookmakers offered the best AFL Round {ROUND} odds?",
             f"PointsBet, Sportsbet and Ladbrokes are consistently the best Australian bookmakers for AFL odds. For future matches, compare all three before placing any bet to get the best value."),
            (f"Where can I bet on upcoming AFL matches?",
             f"PointsBet, Sportsbet, and Ladbrokes are our top three rated Australian bookmakers for AFL betting. Each offers competitive head-to-head odds, line markets, and same-game multis."),
        ]
    else:
        faqs = [
            (f"Who will win {t1} vs {t2} in AFL Round {ROUND}?",
             f"Our tip is {m['tip']} to win by {m['tip_margin']} points. {m['summary']} {m['analysis'].split(chr(10)+chr(10))[0]}"),
            (f"When and where is {t1} vs {t2} being played?",
             f"{t1} vs {t2} is scheduled for {m['date']} at {m.get('time','TBC')} at {m['venue']}."),
            (f"What is the current form of {t1} and {t2}?",
             f"{t1} are {m['record1']} in 2026 with recent form: {m['form1']}. {t2} are {m['record2']} with recent form: {m['form2']}. {m['stats']}"),
            (f"What are the best betting markets for {t1} vs {t2}?",
             f"The key markets are: {m['markets']}. Our analysis suggests {m['tip']} are the value pick at current prices."),
            (f"Which bookmaker has the best odds for AFL Round {ROUND}?",
             f"Compare PointsBet, Sportsbet, and Ladbrokes before placing on {t1} vs {t2}. All three are competitive on AFL head-to-head — odds can vary by 5–10% between bookmakers on the same market."),
        ]

    score_html = f'<div style="font-family:Geist,sans-serif;font-size:32px;font-weight:800;letter-spacing:-0.04em;margin:10px 0">{m["result"]}</div>' if is_done else f'<div style="font-size:13px;font-weight:600;color:var(--primary);margin:8px 0">{m.get("time","TBC")} · {m["date"]}</div>'

    # Form rows
    form1_html = form_dots(m.get('form1','L L L L L'))
    form2_html = form_dots(m.get('form2','L L L L L'))

    matchup_html = f"""<div class="matchup">
  <div class="teams">
    <div class="team-block">
      <div class="team-badge" style="background:{t1d['colour']}">{t1d['short']}</div>
      <div class="team-name">{t1}</div>
      <div style="font-size:11px;color:var(--muted-fg);font-weight:600">{m.get('record1','')}</div>
      <div class="form-row">{form1_html}</div>
    </div>
    <div style="text-align:center">
      <div class="vs">VS</div>
      <div style="font-size:11px;color:var(--muted-fg);margin-top:4px">AFL Round {ROUND}</div>
    </div>
    <div class="team-block">
      <div class="team-badge" style="background:{t2d['colour']}">{t2d['short']}</div>
      <div class="team-name">{t2}</div>
      <div style="font-size:11px;color:var(--muted-fg);font-weight:600">{m.get('record2','')}</div>
      <div class="form-row">{form2_html}</div>
    </div>
  </div>
  {score_html}
  <div class="match-meta">
    <span>🏟 {m['venue']}</span>
    <span>📅 {m['date']}</span>
    {'<span>⏰ ' + m["time"] + '</span>' if m.get('time') else ''}
  </div>
</div>"""

    tip_html = ''
    if not is_done:
        tip_html = f"""<div class="tip-box">
  <h3>Our Tip — Round {ROUND}</h3>
  <div class="tip-team">{m['tip']}</div>
  <div style="font-size:13px;color:hsl(140 40% 40%);margin-bottom:12px">Expected margin: {m['tip_margin']} points</div>
  <p style="font-size:14px;line-height:1.75;color:hsl(215 45% 16%/.85)">{m['summary']}</p>
  <p style="font-size:11px;color:hsl(140 40% 40%);margin-top:12px">Tips are editorial predictions only. Please gamble responsibly. 18+.</p>
</div>"""

    # Analysis paragraphs
    analysis_paras = ''.join(f'<p style="font-size:15px;line-height:1.8;color:hsl(215 45% 16%/.85);margin-bottom:14px">{p.strip()}</p>' for p in m['analysis'].split('\n\n') if p.strip())

    analysis_html = f"""<div class="analysis-section">
  <h2>{'Match Analysis' if is_done else 'Match Preview & Analysis'}</h2>
  {analysis_paras}
</div>"""

    # Key players
    kp_html = f"""<div class="analysis-section">
  <h2>Key Players to Watch</h2>
  <div class="kp-grid">
    <div class="kp-item">
      <div class="kp-team">{t1}</div>
      <div class="kp-name">{m.get('key_player1','').split(' (')[0]}</div>
      <div class="kp-desc">{'('.join(m.get('key_player1','').split(' (')[1:]).rstrip(')')}</div>
    </div>
    <div class="kp-item">
      <div class="kp-team">{t2}</div>
      <div class="kp-name">{m.get('key_player2','').split(' (')[0]}</div>
      <div class="kp-desc">{'('.join(m.get('key_player2','').split(' (')[1:]).rstrip(')')}</div>
    </div>
  </div>
  <div style="background:var(--muted);border-radius:8px;padding:12px 14px;margin-top:8px">
    <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:4px">Key Matchup</div>
    <div style="font-size:13px;font-weight:600">{m.get('key_matchup','')}</div>
  </div>
</div>"""

    # Stats and markets
    stats_html = f"""<div class="analysis-section">
  <h2>Stats & Betting Markets</h2>
  <div class="stat-grid">
    <div class="stat-item">
      <div class="stat-label">Form & Stats</div>
      <div class="stat-val">{m.get('stats','')}</div>
    </div>
    <div class="stat-item">
      <div class="stat-label">Markets</div>
      <div class="stat-val">{m.get('markets','')}</div>
    </div>
  </div>
  <div class="markets-box">
    <h4>💰 Best Bets for This Match</h4>
    <p style="font-size:13px;line-height:1.7">{'Result: ' + m['result'] if is_done else 'Our selection: <strong>' + m['tip'] + '</strong> — ' + m['markets']}</p>
    <p style="font-size:11px;color:hsl(48 50% 45%);margin-top:8px">Always compare odds across PointsBet, Sportsbet and Ladbrokes before placing. Odds correct at time of writing and subject to change.</p>
  </div>
</div>"""

    bm_cards = ''
    for bm in TOP_BOOKMAKERS:
        bm_cards += f"""<div class="card">
  <div class="bm-row">
    <img src="/{bm['logo']}" alt="{bm['name']}" class="bm-logo">
    <div style="flex:1">
      <div style="font-weight:700;font-size:15px;margin-bottom:2px">{bm['name']}</div>
      <div style="font-size:13px;color:var(--muted-fg);margin-bottom:10px">{bm['tagline']}</div>
      <div style="display:flex;gap:10px">
        <a href="#" onclick="return false;" class="btn-g" style="font-size:12px;padding:7px 13px">Bet Now →</a>
        <a href="/review-{bm['slug']}.html" style="font-size:13px;color:var(--muted-fg);text-decoration:none;align-self:center">Full Review →</a>
      </div>
    </div>
  </div>
  <p style="font-size:11px;color:var(--muted-fg);margin-top:10px">"Think. Is this a bet you really want to place?" · 18+ · T&Cs apply</p>
</div>"""

    int_links_html = ''.join(f'<a href="{h}">{t}</a>' for t, h in [
        (f'AFL Round {ROUND} Tips', f'/afl-round-{ROUND}-tips-{ROUND_YEAR}.html'),
        ('Best AFL Betting Sites', '/best-betting-sites-for-afl.html'),
        ('Best Betting Sites Australia', '/best-betting-sites-australia.html'),
        ('Compare Betting Sites', '/compare-betting-sites.html'),
        ('PointsBet Review', '/review-pointsbet.html'),
        ('Sportsbet Review', '/review-sportsbet.html'),
        ('Ladbrokes Review', '/review-ladbrokes.html'),
        ('AFL Premiership Odds 2026', '/afl-premiership-odds-2026.html'),
    ])

    faq_items = ''.join(f'<div class="faq-item"><button class="faq-q">{q} <span class="fi">+</span></button><div class="faq-a">{a}</div></div>' for q, a in faqs)
    schema = faq_schema(faqs) + '\n' + article_schema(title, desc, slug)

    html = f"""<!DOCTYPE html>
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
</head>
<body>
<div class="cb"><span class="cb-t">Bet Responsibly</span><span class="cb-h">Gambling Help: <a href="tel:1800858858">1800 858 858</a> · <a href="https://www.gamblinghelponline.org.au" target="_blank">gamblinghelponline.org.au</a></span><div class="cb-b"><span>18+</span><span>AUS ONLY</span></div></div>
<nav class="nav"><a href="/index.html" class="nav-logo"><img src="/puntguide-logo.png" alt="PuntGuide"></a><ul class="nav-links"><li><a href="/best-betting-sites-australia.html">Best Sites</a></li><li><a href="/best-betting-sites-for-afl.html">AFL</a></li><li><a href="/afl-round-{ROUND}-tips-{ROUND_YEAR}.html">Round {ROUND} Tips</a></li><li><a href="/best-betting-apps-australia.html">Best Apps</a></li><li><a href="/all-betting-sites.html">All Sites</a></li></ul><a href="/all-betting-sites.html" class="btn-g">Bet Now →</a></nav>
<div class="pb">
<div class="hero"><div class="hero-in">
  <div class="bc"><a href="/index.html">Home</a> › <a href="/afl-round-{ROUND}-tips-{ROUND_YEAR}.html">AFL Round {ROUND} Tips</a> › {t1} vs {t2}</div>
  <div class="eye"><span class="eye-l"></span><span class="eye-t">{eyebrow}</span></div>
  <h1>{h1}</h1>
  <p style="font-size:16px;color:hsl(215 45% 16%/.65);max-width:700px;line-height:1.8;margin-top:10px">{m['summary']}</p>
</div></div>
<div class="wrap">
  {matchup_html}
  {tip_html}
  {analysis_html}
  {kp_html}
  {stats_html}
  <h2 style="font-size:20px;font-weight:700;margin:32px 0 14px">Best bookmakers for AFL Round {ROUND}</h2>
  {bm_cards}
  <div class="int-links"><h3>Related pages</h3>{int_links_html}</div>
  <div class="faq"><h2>Frequently asked questions</h2>{faq_items}</div>
</div>
</div>
<footer class="site-footer"><div class="footer-in">
<img src="/puntguide-logo.png" alt="PuntGuide" class="footer-logo">
<p class="footer-desc">Australia's most up-to-date AFL betting guide — tips, odds, and the best bookmakers for every round.</p>
<div class="footer-links">
  <a href="/best-betting-sites-australia.html">Best Betting Sites</a>
  <a href="/best-betting-sites-for-afl.html">Best for AFL</a>
  <a href="/afl-round-{ROUND}-tips-{ROUND_YEAR}.html">AFL Round {ROUND} Tips</a>
  <a href="/afl-premiership-odds-2026.html">AFL Premiership Odds</a>
  <a href="/compare-betting-sites.html">Compare Sites</a>
  <a href="/all-betting-sites.html">All 130 Bookmakers</a>
</div>
<div class="footer-rg">Gamble responsibly. Call <a href="tel:1800858858">Gambling Help 1800 858 858</a> or visit <a href="https://www.gamblinghelponline.org.au" target="_blank">gamblinghelponline.org.au</a>. Self-exclude at <a href="https://www.betstop.gov.au" target="_blank">BetStop.gov.au</a>. 18+ only. Tips are editorial predictions only and not financial advice.</div>
</div></footer>
<script>document.querySelectorAll('.faq-q').forEach(b=>b.addEventListener('click',function(){{const a=this.nextElementSibling;a.classList.toggle('open');this.querySelector('.fi').textContent=a.classList.contains('open')?'−':'+';}}));</script>
</body></html>"""

    path = os.path.join(OUT, slug)
    with open(path, 'w') as f:
        f.write(html)
    return slug

def update_sitemap(new_slugs):
    import re
    with open(os.path.join(OUT, 'sitemap.xml')) as f:
        existing = f.read()
    existing_locs = set(re.findall(r'<loc>([^<]+)</loc>', existing))
    additions = ''
    for slug in new_slugs:
        url = f'{SITE}/{slug}'
        if url not in existing_locs:
            additions += f'  <url><loc>{url}</loc><changefreq>daily</changefreq><priority>0.8</priority></url>\n'
    if additions:
        updated = existing.replace('</urlset>', additions + '</urlset>')
        with open(os.path.join(OUT, 'sitemap.xml'), 'w') as f:
            f.write(updated)

if __name__ == '__main__':
    generated = []
    print(f'\n── AFL Round {ROUND} Match Pages (Rich Analysis) ──')
    for m in MATCHES:
        slug = build_match_page(m)
        generated.append(slug)
        print(f'  ✓ {slug}')
    update_sitemap(generated)
    print(f'\n✅ {len(generated)} AFL match pages generated\n')
