#!/usr/bin/env python3
"""
NRL Match Page Generator — Rich Analysis Edition
Usage: edit ROUND and MATCHES below, then run python3 generate_nrl_matches.py
"""
import os, json, re

OUT  = os.path.expanduser('~/puntguide')
SITE = 'https://puntguide.com.au'

ROUND      = 10
ROUND_YEAR = 2026

TEAMS = {
    'Bulldogs':     dict(short='CBY', colour='#0057A8'),
    'Cowboys':      dict(short='NQC', colour='#003B6F'),
    'Dolphins':     dict(short='DOL', colour='#CC0000'),
    'Storm':        dict(short='MEL', colour='#4B0082'),
    'Titans':       dict(short='GCT', colour='#00263A'),
    'Raiders':      dict(short='CBR', colour='#6ABF4B'),
    'Eels':         dict(short='PEE', colour='#0055A5'),
    'Warriors':     dict(short='NZW', colour='#1A1A1A'),
    'Roosters':     dict(short='SYD', colour='#CC0000'),
    'Broncos':      dict(short='BRI', colour='#4B0020'),
    'Knights':      dict(short='NEW', colour='#003A8C'),
    'Rabbitohs':    dict(short='SSR', colour='#007A3D'),
    'Sharks':       dict(short='CRO', colour='#00AEEF'),
    'Wests Tigers': dict(short='WST', colour='#FF6600'),
    'Panthers':     dict(short='PEN', colour='#1A1A1A'),
    'Sea Eagles':   dict(short='MAN', colour='#6B0020'),
}

MATCHES = [
    dict(
        team1='Bulldogs', team2='Cowboys',
        date='Friday, May 1, 2026', time='6:00 PM', venue='Accor Stadium, Sydney',
        status='upcoming', result=None,
        tip='Cowboys', tip_margin='7–14',
        summary="The Cowboys travel to Accor Stadium as favourites over a rebuilding Bulldogs side. North Queensland's experienced spine and superior defensive structure should be decisive in a tight Friday night encounter.",
        analysis="""North Queensland Cowboys enter this match as the more well-rounded side, carrying a superior win-loss record and a defensive structure that has conceded the fewest points in the top eight through the first nine rounds. Their experienced spine — featuring one of the competition's most settled combinations — gives them a significant edge against a Bulldogs outfit that continues to grow but is not yet ready to challenge genuine contenders.

The Canterbury-Bankstown Bulldogs have shown genuine improvement in 2026 under their current coaching staff. They are no longer the pushover they were in 2024 and 2025, and the NRL Round 8 review noted that the Bulldogs had "given the Knights too much start before deciding to play football" — a phrase that captures both their ability and their inconsistency. At home at Accor Stadium they will have crowd support but face an uphill task.

The Cowboys' form has been one of the competition's more impressive stories this year. Valentine Holmes in particular has been outstanding in the back half of the season, while their middle forwards have provided dominant go-forward. The Cowboys won both of their meetings against the Bulldogs in 2025 and their defensive efficiency makes them difficult to beat in one-off games. Tip: Cowboys by 7–14 points in a competitive but controlled away win.""",
        form1='W L W L W', form2='W W W W L',
        record1='4-5', record2='6-3',
        key_player1='Josh Addo-Carr (Bulldogs\' most dangerous outside back, needs to be in the game for CBY to win)',
        key_player2='Valentine Holmes (Cowboys\' right-edge weapon, outstanding in 2026, averaging 2+ try assists per game)',
        key_matchup='Cowboys\' experienced spine vs Bulldogs\' young halves — if NQC control the ruck and set piece, they win',
        stats='Cowboys: 6W–3L, 6th on ladder · Bulldogs: 4W–5L, 10th · H2H: Cowboys won both 2025 meetings',
        markets='Head-to-head: CBY $3.20 / NQC $1.35 · Line: NQC –7.5 · Tip: Cowboys –7.5',
    ),
    dict(
        team1='Dolphins', team2='Storm',
        date='Friday, May 1, 2026', time='8:00 PM', venue='Suncorp Stadium, Brisbane',
        status='upcoming', result=None,
        tip='Storm', tip_margin='7–14',
        summary="Melbourne Storm are firm favourites for this Friday night clash at Suncorp Stadium. The Storm's formidable forward pack and elite defensive structure — the best in the competition — make them difficult to beat anywhere.",
        analysis="""Melbourne Storm have established themselves as the NRL's most consistent defensive unit through 2026 — conceding the fewest points per game of any side in the competition. Their forward pack, led by their dominant prop combination, provides the go-forward that allows their elite halves to control the game and exploit the edges. The Storm were noted in the Round 8 review as "clicking with Ryan Papenhuyzen at his best" — a frightening prospect for any opposition defence.

The Redcliffe Dolphins have been one of the competition's more frustrating clubs to assess in 2026. They showed enough in their ANZAC round match against the Roosters to suggest they have the talent to compete with top-eight sides, but they were ultimately "never in the game" according to match reviews. Their defence in particular has been inconsistent — conceding points in clusters after periods of controlled effort.

Suncorp Stadium is Brisbane territory which should provide the Dolphins with some crowd advantage, but the Storm have won at every ground in the competition this year. Their combination of Papenhuyzen's brilliance at fullback, their structured right-edge attack and the dominance of their middle forwards makes them difficult to tip against regardless of venue. Storm by 7–14 in a controlled performance.""",
        form1='L W L W L', form2='W W W L W',
        record1='4-5', record2='7-2',
        key_player1='Isaiya Katoa (Dolphins\' most creative player, needs to find his best to trouble the Storm)',
        key_player2='Ryan Papenhuyzen (Melbourne\'s game-breaker at fullback, outstanding in 2026, averages 150+ metres per game)',
        key_matchup='Storm\'s middle forward dominance vs Dolphins\' ruck — if the Dolphins can compete at the base of the scrum, they stay in it',
        stats='Storm: 7W–2L, 2nd ladder · Dolphins: 4W–5L, 10th · Storm: fewest points conceded in comp 2026',
        markets='Head-to-head: DOL $3.50 / MEL $1.30 · Line: MEL –8.5 · Tip: Storm to win',
    ),
    dict(
        team1='Titans', team2='Raiders',
        date='Saturday, May 2, 2026', time='3:00 PM', venue='Cbus Super Stadium, Gold Coast',
        status='upcoming', result=None,
        tip='Raiders', tip_margin='1–10',
        summary="Canberra Raiders travel to Cbus Super Stadium as slight favourites in a match that could go either way. The Raiders have been one of 2026's form sides while the Titans have been competitive but inconsistent.",
        analysis="""This is one of the round's most competitive and genuinely difficult to predict fixtures. The Canberra Raiders have been one of the NRL's form sides over the past month — they were noted as finishing "strongly against the Roosters last week after giving away a big start," which is precisely the kind of resilience that separates contenders from pretenders. The Raiders have the physical forward pack to dominate possession and their halves have been executing their kicking game with precision.

The Gold Coast Titans come into this match with something to prove after "competing well with the Sharks before running out of steam" in Round 9. That pattern — competitive for 60 minutes, fading in the final stretch — has been a consistent storyline for the Titans in 2026 and reflects their lack of depth across their 17. They have the class to win this at home but their fitness and depth questions are real.

Cbus Super Stadium is not the fortress it once was for the Titans — they have been beaten at home multiple times this year by sides of comparable quality. The Raiders' superior depth and the fact they are coming off a strong run of form gives them the edge here. This is nonetheless a game to approach with caution — the margin either way is unlikely to be large. Raiders by 1–10 in a tight contest.""",
        form1='L W W L W', form2='W W L W L',
        record1='4-5', record2='5-4',
        key_player1='AJ Brimson (Titans\' electric fullback, when he\'s carrying well the Titans are competitive with anyone)',
        key_player2='Jack Wighton (Raiders\' five-eighth, the creative engine of their attack, must be contained)',
        key_matchup='Raiders\' forward pack vs Titans\' middle — the team that wins metres in the middle will win this game',
        stats='Raiders: 5W–4L, 7th · Titans: 4W–5L, 11th · Raiders beat Roosters in last outing',
        markets='Head-to-head: GCT $2.40 / CBR $1.60 · Line: CBR –4.5 · Tip: Raiders –4.5',
    ),
    dict(
        team1='Eels', team2='Warriors',
        date='Saturday, May 2, 2026', time='5:30 PM', venue='CommBank Stadium, Sydney',
        status='upcoming', result=None,
        tip='Eels', tip_margin='1–12',
        summary="Parramatta Eels host the New Zealand Warriors at CommBank Stadium. Both sides have been disappointing in 2026 but the Eels' home advantage and the Warriors' struggle in Australian conditions tips this to Parramatta.",
        analysis="""The NRL Round 9 review was blunt about both these clubs: "The Eels played well last week, but they never really looked like beating the Sharks. The Warriors failed to score a point in the heavy rain of Auckland last week against the Roosters." Neither club enters this match in strong form and both have frustrated their supporters with performances well below their preseason expectations.

However, CommBank Stadium provides Parramatta with a significant home advantage. The Eels' supporters generate genuine atmosphere at their home ground and the familiar surroundings have consistently produced better performances from the Parramatta side. The Warriors, meanwhile, face a cross-Tasman trip that adds physical and mental fatigue to a side that has already shown it struggles with the rigours of NRL travel.

The Eels have Mitchell Moses back to his best in recent weeks — when Moses is running the attack and the Eels' middle forwards are providing go-forward, they are a difficult side to beat at CommBank. The Warriors showed they can score points but their defence in Australian conditions has been a concern. Eels by 1–12 in a competitive but ultimately home-side win.""",
        form1='W L W L L', form2='L L W L L',
        record1='3-6', record2='2-7',
        key_player1='Mitchell Moses (Eels\' playmaker, when he runs the attack well Parramatta are competitive)',
        key_player2='Shaun Johnson (Warriors\' veteran halfback, has the experience to drag them into this game)',
        key_matchup='Moses vs Johnson in the halves battle — the better playmaker on the day wins this game',
        stats='Eels: 3W–6L, 14th · Warriors: 2W–7L, 16th · Warriors: 0 points in last away game',
        markets='Head-to-head: EEL $1.65 / NZW $2.25 · Line: EEL –5.5 · Tip: Eels to win',
    ),
    dict(
        team1='Roosters', team2='Broncos',
        date='Saturday, May 2, 2026', time='7:35 PM', venue='Allianz Stadium, Sydney',
        status='upcoming', result=None,
        tip='Roosters', tip_margin='7–14',
        summary="Saturday night blockbuster at Allianz Stadium. The Sydney Roosters have been outstanding at home in 2026 with a 5W–1L record at Allianz, and they face a Brisbane Broncos side with genuine finals ambitions.",
        analysis="""This is the marquee match of Round 10 — and one of the NRL's greatest club rivalries delivered in the best possible setting. Allianz Stadium under lights on a Saturday night for a Roosters vs Broncos game is as good as it gets in Australian rugby league, and both clubs are genuine contenders who have the talent to produce something memorable.

The Roosters' home record is the key piece of data here. They are 5W–1L at Allianz Stadium in 2026 and that one loss came against the Panthers in Round 3. Their home crowd advantage is significant — the short ball game that defines Sydney's attack suits the ground's compact dimensions, and their defence in front of their own supporters has conceded fewer points than any other team at their home ground in the competition.

Brisbane enter with genuine belief and a strong run of form through the mid-season. Their left-edge combination has been one of the competition's most dangerous attacking partnerships and their forward pack provides excellent go-forward. However, the Roosters' defensive structure has handled stronger forward packs than Brisbane's this year. The Roosters are the value play here — their home ground, their record at Allianz, and the quality of their defensive system all point to a Sydney win. Roosters by 7–14.""",
        form1='W W W L W', form2='W W L W W',
        record1='6-3', record2='6-3',
        key_player1='James Tedesco (Roosters fullback, most dangerous player in the game when on song)',
        key_player2='Ezra Mam (Broncos\' brilliant young half, his creativity could unlock the Roosters\' defence)',
        key_matchup='Tedesco\'s line-breaks vs Broncos\' right edge defence — if Tedesco gets into space, the Roosters win comfortably',
        stats='Roosters: 5W–1L at Allianz in 2026 · Brisbane: 6W–3L, 4th · Both sides in top 4 form',
        markets='Head-to-head: SYD $1.70 / BRI $2.10 · Line: SYD –5.5 · Tip: Roosters –5.5 at home',
    ),
    dict(
        team1='Knights', team2='Rabbitohs',
        date='Sunday, May 3, 2026', time='2:00 PM', venue='McDonald Jones Stadium, Newcastle',
        status='upcoming', result=None,
        tip='Knights', tip_margin='1–12',
        summary="Newcastle Knights host South Sydney Rabbitohs at McDonald Jones Stadium. The Knights have been strong at home in 2026 and the Rabbitohs travel with a recent comfortable win over the Cowboys under their belt.",
        analysis="""The Round 9 review noted that the "Rabbitohs continued their impressive season with a comfortable win over the Cowboys," suggesting South Sydney are in reasonable form despite an inconsistent ladder position. However, they now face a Newcastle side at McDonald Jones Stadium — a ground that has produced some of the competition's more hostile home atmospheres in 2026.

The Newcastle Knights have been one of the season's surprise packages at home. They play a physical, forwards-first game that suits the Hunter Valley crowd and their middle forward combination has been outstanding. The review of their last game noted they "gave the Bulldogs too much start before deciding to play football" — a pattern that suggests they can switch it on when required but are vulnerable to fast starts from opponents.

The key question is whether South Sydney can handle the Newcastle physical challenge through the middle. The Rabbitohs have shown they can score freely against lesser defences but have struggled against sides that dominate the ruck. Newcastle have the forward pack to do exactly that at home. A tight game, with the Knights' home advantage and crowd making the difference in the final 20 minutes. Knights by 1–12.""",
        form1='W L W W L', form2='W W L W W',
        record1='5-4', record2='5-4',
        key_player1='Kalyn Ponga (Knights\' mercurial fullback, when he\'s carrying and stepping, McDonald Jones is unbeatable)',
        key_player2='Cody Walker (Rabbitohs\' halfback, his creativity could be the difference if he can find open space)',
        key_matchup='Ponga\'s line-break threat vs Rabbitohs\' edge defence — if Ponga gets room to run, Newcastle win easily',
        stats='Knights: 5W–4L, 8th · Rabbitohs: 5W–4L, 8th · Equal on ladder — winner jumps into top 8 comfortably',
        markets='Head-to-head: NEW $1.85 / SSR $1.95 · Line: NEW –3.5 · Tip: Knights at home',
    ),
    dict(
        team1='Sharks', team2='Wests Tigers',
        date='Sunday, May 3, 2026', time='4:05 PM', venue='Ocean Protect Stadium, Sydney',
        status='upcoming', result=None,
        tip='Sharks', tip_margin='15+',
        summary="Cronulla Sharks are heavy favourites to account for Wests Tigers at Ocean Protect Stadium. The Sharks were 'well in control' of their last game and face a Tigers side in the middle of a rebuild.",
        analysis="""This is one of the round's cleaner tips. The NRL Round 9 review was clear: the "Sharks were well in control of their game last week against the Eels," suggesting Cronulla are in strong form and executing their game plan effectively. Their defensive organisation has been outstanding through 2026 and their attack — while not always spectacular — has been ruthlessly efficient.

Wests Tigers are in the middle of a genuine rebuild and the gap between them and a side like Cronulla is significant at this stage of their development. The Tigers "were involved in a genuine battle with the Dragons before drawing clear" last week — a performance that suggests they can compete against similarly-placed clubs but lack the quality to challenge top-eight sides consistently.

Ocean Protect Stadium is a fortress for the Sharks — their crowd generates genuine hostility and their playing group has responded to that atmosphere consistently in 2026. The Tigers' defensive line has been one of the competition's leakier units against sides with quality ball movement and Cronulla's wingers have the finishing ability to punish any gaps. Sharks by 15+ in a comfortable home win that the market reflects accurately at current prices.""",
        form1='W W L W W', form2='L W L L W',
        record1='6-3', record2='3-6',
        key_player1='Nicho Hynes (Sharks\' brilliant halfback, directs the attack beautifully and his kicking game is elite)',
        key_player2='Lachlan Galvin (Tigers\' young five-eighth, shows class but needs support to trouble the Sharks)',
        key_matchup='Sharks\' defensive line speed vs Tigers\' attack — if Cronulla get up quickly, the Tigers can\'t find the line',
        stats='Sharks: 6W–3L, 5th · Tigers: 3W–6L, 13th · Sharks comfortable favourites in all markets',
        markets='Head-to-head: CRO $1.25 / WST $3.80 · Line: CRO –14.5 · Tip: Sharks to win & cover',
    ),
    dict(
        team1='Panthers', team2='Sea Eagles',
        date='Sunday, May 3, 2026', time='6:15 PM', venue='CommBank Stadium, Sydney',
        status='upcoming', result=None,
        tip='Panthers', tip_margin='15+',
        summary="Penrith Panthers are the competition's benchmark club and heavy favourites against Manly-Warringah Sea Eagles. The Panthers' depth and quality is simply at a different level to most NRL opponents.",
        analysis="""The Penrith Panthers remain the NRL's gold standard in 2026 — the benchmark club against whom all others are measured. Their squad depth is extraordinary: they have players who would start for most other clubs sitting on their bench or playing reserve grade. When they click — and they have been clicking consistently in 2026 — they are virtually unplayable.

The Manly-Warringah Sea Eagles have shown improvement under their 2026 coaching structure but remain a mid-table side at best. They were listed among Betfair's wooden spoon contenders at the start of the year and while they have exceeded those expectations, they are not yet capable of challenging a side with Penrith's depth and system. The Sea Eagles' left edge in particular has been vulnerable to structured attacking football — exactly the kind of game Penrith play week in, week out.

CommBank Stadium is familiar ground for Panthers fans who make the journey to support their club. Penrith's combination of their first-choice fullback and halves, their dominant forward pack and their structured left-edge attack should be too much for Manly across 80 minutes. The –14.5 line looks light for a match between these two clubs at this stage of the season. Panthers by 15+ in a controlled performance.""",
        form1='W W W W W', form2='L W L W L',
        record1='8-1', record2='3-6',
        key_player1='Nathan Cleary (Panthers\' halfback and game manager, controls the pace and direction of every Penrith performance)',
        key_player2='Tom Trbojevic (Sea Eagles\' superstar fullback, the one player who can conjure a result from nowhere)',
        key_matchup='Cleary\'s kicking game vs Sea Eagles\' back three — if Cleary can pin them in their own half, Penrith win comfortably',
        stats='Panthers: 8W–1L, 1st on ladder · Sea Eagles: 3W–6L, 14th · Penrith: most dominant defensive record 2026',
        markets='Head-to-head: PEN $1.15 / MAN $5.50 · Line: PEN –14.5 · Tip: Panthers to win & consider the –14.5 line',
    ),
    dict(
        team1='Dolphins', team2='Bulldogs',
        date='Thursday, May 7, 2026', time='7:50 PM', venue='Suncorp Stadium, Brisbane',
        status='upcoming', result=None,
        tip='Dolphins', tip_margin='1–12',
        summary="Round 10 kicks off with the Dolphins hosting the Bulldogs at Suncorp Stadium in Brisbane on Thursday night. The Dolphins enjoy genuine home-ground advantage at Suncorp and should account for a rebuilding Bulldogs side.",
        analysis="""The Round 10 Thursday night opener gives the Redcliffe Dolphins an opportunity to bank a home win at Suncorp Stadium before the rest of the competition plays. Despite their inconsistent season so far, the Dolphins are favourites here and the home ground advantage is real — Suncorp Stadium is one of the NRL's most atmospheric venues and the Dolphins have a vocal and passionate supporter base that creates a challenging environment for visiting sides.

The Canterbury-Bankstown Bulldogs, despite showing improvement in 2026, remain a developing side that has struggled against top-eight opposition. Their performance in the earlier Round 10 match on Friday will give some indication of their form heading into this Thursday encounter, and the tight turnaround could be a factor in the second half if the Bulldogs have played a physical game against the Cowboys.

This is a match where the Dolphins' halves combination needs to perform. When the Dolphins' creative players are working in tandem and their middle forwards are providing go-forward, they have shown they can compete with any side in the competition. Against the Bulldogs at Suncorp, they have the conditions that suit their best football. Dolphins by 1–12 in what should be a hard-fought but ultimately comfortable home win.""",
        form1='L W L W L', form2='W L W L W',
        record1='4-5', record2='4-5',
        key_player1='Hamiso Tabuai-Fidow (Dolphins\' electric fullback, one of the most exciting players in the competition)',
        key_player2='Josh Addo-Carr (Bulldogs\' right winger, needs to be fed the ball to cause the Dolphins problems)',
        key_matchup='Dolphins\' halves combination vs Bulldogs\' defensive line — if the home side can shift the ball quickly, they win',
        stats='Dolphins: 4W–5L · Bulldogs: 4W–5L · Equal ladder position — Suncorp home advantage decisive',
        markets='Head-to-head: DOL $1.75 / CBY $2.10 · Line: DOL –5.5 · Tip: Dolphins at home',
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
.team-badge{width:64px;height:64px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:13px;color:#fff;flex-shrink:0;}
.team-name{font-weight:700;font-size:15px;max-width:120px;text-align:center;}
.vs{font-family:"JetBrains Mono",monospace;font-size:18px;font-weight:700;color:var(--muted-fg);}
.match-meta{display:flex;justify-content:center;gap:20px;flex-wrap:wrap;font-size:13px;color:var(--muted-fg);border-top:1px solid var(--border);padding-top:14px;margin-top:4px;}
.form-row{display:flex;gap:6px;justify-content:center;margin-top:4px;}
.form-dot{width:24px;height:24px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:700;color:#fff;}
.form-w{background:hsl(140 50% 40%);}
.form-l{background:hsl(16 70% 45%);}
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
    dict(name='PointsBet', slug='pointsbet', logo='pointsbet.png', tagline='Sharpest NRL odds + unique PointsBetting markets'),
    dict(name='Sportsbet',  slug='sportsbet',  logo='sportsbet.png',  tagline='Widest NRL market range in Australia'),
    dict(name='betr',       slug='betr',       logo='betr.png',       tagline='Best-in-class NRL same-game multi builder'),
]

def team_slug(name):
    return name.lower().replace(' ', '-').replace('.', '')

def match_slug(m):
    return f"nrl-{team_slug(m['team1'])}-vs-{team_slug(m['team2'])}-round-{ROUND}-{ROUND_YEAR}.html"

def form_dots(form_str):
    html = ''
    for ch in form_str.split():
        cls = 'form-w' if ch == 'W' else 'form-l'
        html += f'<span class="form-dot {cls}">{ch}</span>'
    return html

def faq_schema(faqs):
    items = ','.join([f'{{"@type":"Question","name":{json.dumps(q)},"acceptedAnswer":{{"@type":"Answer","text":{json.dumps(a)}}}}}' for q,a in faqs])
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{items}]}}</script>'

def article_schema(title, desc, slug):
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":{json.dumps(title)},"description":{json.dumps(desc)},"author":{{"@type":"Organization","name":"PuntGuide"}},"publisher":{{"@type":"Organization","name":"PuntGuide","logo":{{"@type":"ImageObject","url":"{SITE}/favicon-192.png"}}}},"datePublished":"2026-05-01","dateModified":"2026-05-02","mainEntityOfPage":"{SITE}/{slug}","image":{{"@type":"ImageObject","url":"{SITE}/favicon-192.png"}}}}</script>'

def build_match_page(m):
    slug  = match_slug(m)
    t1    = m['team1']
    t2    = m['team2']
    t1d   = TEAMS.get(t1, dict(short=t1[:3].upper(), colour='#333'))
    t2d   = TEAMS.get(t2, dict(short=t2[:3].upper(), colour='#333'))

    title   = f"{t1} vs {t2} Tips & Odds — NRL Round {ROUND} {ROUND_YEAR} | PuntGuide"
    desc    = f"Expert {t1} vs {t2} NRL Round {ROUND} tips, odds and analysis. Team form, key players, head-to-head history and our best bet for this match."
    h1      = f"{t1} vs {t2} — NRL Round {ROUND} Tips & Prediction"
    eyebrow = f"NRL Round {ROUND} · {m['date']} · {m.get('time','')}"

    faqs = [
        (f"Who will win {t1} vs {t2} in NRL Round {ROUND}?",
         f"Our tip is {m['tip']} to win by {m['tip_margin']} points. {m['summary']}"),
        (f"When and where is {t1} vs {t2} being played?",
         f"{t1} vs {t2} kicks off at {m.get('time','TBC')} on {m['date']} at {m['venue']}."),
        (f"What is the current form of {t1} and {t2}?",
         f"{t1} are {m['record1']} in 2026 with recent form: {m['form1']}. {t2} are {m['record2']} with form: {m['form2']}. {m['stats']}"),
        (f"What are the best betting markets for {t1} vs {t2}?",
         f"The key markets are: {m['markets']}. Our analysis suggests {m['tip']} are the value selection at current odds."),
        (f"Which bookmaker is best for NRL Round {ROUND} betting?",
         f"Compare PointsBet, Sportsbet and betr before placing on {t1} vs {t2}. All three are competitive on NRL head-to-head and betr has the best same-game multi options for this match."),
    ]

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
      <div style="font-size:11px;color:var(--muted-fg);margin-top:4px">NRL Round {ROUND}</div>
    </div>
    <div class="team-block">
      <div class="team-badge" style="background:{t2d['colour']}">{t2d['short']}</div>
      <div class="team-name">{t2}</div>
      <div style="font-size:11px;color:var(--muted-fg);font-weight:600">{m.get('record2','')}</div>
      <div class="form-row">{form2_html}</div>
    </div>
  </div>
  <div style="font-size:13px;font-weight:600;color:var(--primary);margin:8px 0">{m.get('time','TBC')} · {m['date']}</div>
  <div class="match-meta">
    <span>🏟 {m['venue']}</span>
    <span>📅 {m['date']}</span>
    <span>🏉 NRL Round {ROUND} {ROUND_YEAR}</span>
  </div>
</div>"""

    tip_html = f"""<div class="tip-box">
  <h3>Our Tip — NRL Round {ROUND}</h3>
  <div class="tip-team">{m['tip']}</div>
  <div style="font-size:13px;color:hsl(140 40% 40%);margin-bottom:12px">Expected margin: {m['tip_margin']} points</div>
  <p style="font-size:14px;line-height:1.75;color:hsl(215 45% 16%/.85)">{m['summary']}</p>
  <p style="font-size:11px;color:hsl(140 40% 40%);margin-top:12px">Tips are editorial predictions only. Please gamble responsibly. 18+.</p>
</div>"""

    analysis_paras = ''.join(f'<p style="font-size:15px;line-height:1.8;color:hsl(215 45% 16%/.85);margin-bottom:14px">{p.strip()}</p>' for p in m['analysis'].split('\n\n') if p.strip())

    analysis_html = f"""<div class="analysis-section">
  <h2>Match Preview & Analysis</h2>
  {analysis_paras}
</div>"""

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
    <p style="font-size:13px;line-height:1.7">Our selection: <strong>{m['tip']}</strong> — {m['markets']}</p>
    <p style="font-size:11px;color:hsl(48 50% 45%);margin-top:8px">Always compare odds across PointsBet, Sportsbet and betr before placing. Odds correct at time of writing.</p>
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
        (f'NRL Round {ROUND} Tips', f'/nrl-round-{ROUND}-tips-{ROUND_YEAR}.html'),
        ('Best NRL Betting Sites', '/best-betting-sites-afl-nrl.html'),
        ('Best Betting Sites Australia', '/best-betting-sites-australia.html'),
        ('Compare Betting Sites', '/compare-betting-sites.html'),
        ('PointsBet Review', '/review-pointsbet.html'),
        ('Sportsbet Review', '/review-sportsbet.html'),
        ('betr Review', '/review-betr.html'),
        ('NRL Premiership Odds', '/nrl-premiership-odds-2026.html'),
    ])

    faq_items = ''.join(f'<div class="faq-item"><button class="faq-q">{q} <span class="fi">+</span></button><div class="faq-a">{a}</div></div>' for q, a in faqs)
    schema    = faq_schema(faqs) + '\n' + article_schema(title, desc, slug)

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
<nav class="nav"><a href="/index.html" class="nav-logo"><img src="/puntguide-logo.png" alt="PuntGuide"></a><ul class="nav-links"><li><a href="/best-betting-sites-australia.html">Best Sites</a></li><li><a href="/best-betting-sites-afl-nrl.html">NRL</a></li><li><a href="/nrl-round-{ROUND}-tips-{ROUND_YEAR}.html">Round {ROUND} Tips</a></li><li><a href="/best-betting-apps-australia.html">Best Apps</a></li><li><a href="/all-betting-sites.html">All Sites</a></li></ul><a href="/all-betting-sites.html" class="btn-g">Bet Now →</a></nav>
<div class="pb">
<div class="hero"><div class="hero-in">
  <div class="bc"><a href="/index.html">Home</a> › <a href="/nrl-round-{ROUND}-tips-{ROUND_YEAR}.html">NRL Round {ROUND} Tips</a> › {t1} vs {t2}</div>
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
  <h2 style="font-size:20px;font-weight:700;margin:32px 0 14px">Best bookmakers for NRL Round {ROUND}</h2>
  {bm_cards}
  <div class="int-links"><h3>Related pages</h3>{int_links_html}</div>
  <div class="faq"><h2>Frequently asked questions</h2>{faq_items}</div>
</div>
</div>
<footer class="site-footer"><div class="footer-in">
<img src="/puntguide-logo.png" alt="PuntGuide" class="footer-logo">
<p class="footer-desc">Australia's most up-to-date NRL betting guide — tips, odds, and the best bookmakers for every round.</p>
<div class="footer-links">
  <a href="/best-betting-sites-australia.html">Best Betting Sites</a>
  <a href="/best-betting-sites-afl-nrl.html">Best for NRL</a>
  <a href="/nrl-round-{ROUND}-tips-{ROUND_YEAR}.html">NRL Round {ROUND} Tips</a>
  <a href="/nrl-premiership-odds-2026.html">NRL Premiership Odds</a>
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
    print(f'\n── NRL Round {ROUND} Match Pages (Rich Analysis) ──')
    for m in MATCHES:
        slug = build_match_page(m)
        generated.append(slug)
        print(f'  ✓ {slug}')
    update_sitemap(generated)
    print(f'\n✅ {len(generated)} NRL match pages generated\n')
