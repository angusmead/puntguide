#!/usr/bin/env python3
"""Generate NRL Round 14 2026 hub + 8 per-match pages in the R13 layout.

Hub:       ~/puntguide/nrl-round-14-tips-2026.html
Per-match: ~/puntguide/nrl/2026/round-14/<slug>.html

Uses Betr NRL affiliate prefix (zJS8NRxe1pCYNevImT-MDGNd7ZgqdRLk) and the
/go/?to=betr-nrl tracking link, matching the R13 build.
"""
import os, json

OUT  = os.path.expanduser('~/puntguide')
PM_DIR = os.path.join(OUT, 'nrl', '2026', 'round-14')
SITE = 'https://puntguide.com.au'

# ── Fixture ─────────────────────────────────────────────────────────────────
MATCHES = [
    dict(
        home_full='Manly Sea Eagles', home_slug='sea-eagles', home_nick='Manly',
        away_full='South Sydney Rabbitohs', away_slug='rabbitohs', away_nick='Souths',
        day='Thursday', date_str='Thursday 4 June 2026', date_short='Thursday 4 June', time_str='7:50 PM',
        iso_start='2026-06-04T19:50:00+10:00',
        venue='4 Pines Park',
        h2h_home='1.57', h2h_away='2.40',
        line_home_h='-4.5', line_home_o='1.94', line_away_h='+4.5', line_away_o='1.86',
    ),
    dict(
        home_full='Melbourne Storm', home_slug='storm', home_nick='Storm',
        away_full='Newcastle Knights', away_slug='knights', away_nick='Knights',
        day='Friday', date_str='Friday 5 June 2026', date_short='Friday 5 June', time_str='6:00 PM',
        iso_start='2026-06-05T18:00:00+10:00',
        venue='AAMI Park, Melbourne',
        h2h_home='1.61', h2h_away='2.32',
        line_home_h='-4.5', line_home_o='1.93', line_away_h='+4.5', line_away_o='1.87',
    ),
    dict(
        home_full='Canberra Raiders', home_slug='raiders', home_nick='Raiders',
        away_full='Sydney Roosters', away_slug='roosters', away_nick='Roosters',
        day='Friday', date_str='Friday 5 June 2026', date_short='Friday 5 June', time_str='8:00 PM',
        iso_start='2026-06-05T20:00:00+10:00',
        venue='GIO Stadium, Canberra',
        h2h_home='2.20', h2h_away='1.67',
        line_home_h='+2.5', line_home_o='1.90', line_away_h='-2.5', line_away_o='1.90',
    ),
    dict(
        home_full='North Queensland Cowboys', home_slug='cowboys', home_nick='Cowboys',
        away_full='Dolphins', away_slug='dolphins', away_nick='Dolphins',
        day='Saturday', date_str='Saturday 6 June 2026', date_short='Saturday 6 June', time_str='5:30 PM',
        iso_start='2026-06-06T17:30:00+10:00',
        venue='Queensland Country Bank Stadium',
        h2h_home='2.39', h2h_away='1.58',
        line_home_h='+3.5', line_home_o='1.95', line_away_h='-3.5', line_away_o='1.86',
    ),
    dict(
        home_full='Brisbane Broncos', home_slug='broncos', home_nick='Broncos',
        away_full='Gold Coast Titans', away_slug='titans', away_nick='Titans',
        day='Saturday', date_str='Saturday 6 June 2026', date_short='Saturday 6 June', time_str='7:35 PM',
        iso_start='2026-06-06T19:35:00+10:00',
        venue='Suncorp Stadium',
        h2h_home='1.43', h2h_away='2.81',
        line_home_h='-8.5', line_home_o='1.97', line_away_h='+8.5', line_away_o='1.84',
        match_of_round=True,
    ),
    dict(
        home_full='Wests Tigers', home_slug='wests-tigers', home_nick='Tigers',
        away_full='Penrith Panthers', away_slug='panthers', away_nick='Panthers',
        day='Sunday', date_str='Sunday 7 June 2026', date_short='Sunday 7 June', time_str='2:00 PM',
        iso_start='2026-06-07T14:00:00+10:00',
        venue='CommBank Stadium',
        h2h_home='4.25', h2h_away='1.23',
        line_home_h='+12.5', line_home_o='1.90', line_away_h='-12.5', line_away_o='1.90',
    ),
    dict(
        home_full='Cronulla Sharks', home_slug='sharks', home_nick='Sharks',
        away_full='St George Illawarra Dragons', away_slug='dragons', away_nick='Dragons',
        day='Sunday', date_str='Sunday 7 June 2026', date_short='Sunday 7 June', time_str='4:05 PM',
        iso_start='2026-06-07T16:05:00+10:00',
        venue='Ocean Protect Stadium',
        h2h_home='1.29', h2h_away='3.64',
        line_home_h='-11.5', line_home_o='1.82', line_away_h='+11.5', line_away_o='1.99',
    ),
    dict(
        home_full='Canterbury Bulldogs', home_slug='bulldogs', home_nick='Bulldogs',
        away_full='Parramatta Eels', away_slug='eels', away_nick='Eels',
        day='Monday', date_str='Monday 8 June 2026', date_short='Monday 8 June', time_str='4:05 PM',
        iso_start='2026-06-08T16:05:00+10:00',
        venue='Accor Stadium',
        h2h_home='1.64', h2h_away='2.27',
        line_home_h='-3.5', line_home_o='1.90', line_away_h='+3.5', line_away_o='1.90',
    ),
]

BYE_TEAM = 'New Zealand Warriors'

# Match of the Round
MOTR_KEY = 'broncos-vs-titans'

# ── Picks ───────────────────────────────────────────────────────────────────
PICKS = {
    'sea-eagles-vs-rabbitohs': dict(
        tip_label='Manly -4.5', tip_odds='1.94', tip_type='Line',
        tip_sub="Olakau'atu back from rest, Koula named, Trbojevic pack at home &middot; Souths get Fifita/Smith/Murray back but still no Latrell &middot; Sportsbet",
        tryscorer='Jason Saab', tryscorer_sub="Manly winger &middot; Strike threat off Fogarty's kicking game &middot; Betr",
        odds_form="Manly $1.57, Souths $2.40. Handicap: Manly &minus;4.5 $1.94, Souths +4.5 $1.86. Souths have plenty of injury returns but no Latrell &mdash; Manly's full pack at 4 Pines is the side.",
        analysis_hub="Manly welcome back Haumole Olakau'atu from rest and have Tolu Koula named pending HIA clearance from Origin 1. The Trbojevic brothers anchor a heavy pack with Brooks/Fogarty steering. Souths get David Fifita (hamstring, first game since R6), Brandon Smith (calf), Cameron Murray and Campbell Graham all back &mdash; but Latrell remains out with a back injury and the spine takes time to gel. Manly at home with their preferred 17 cover the line.",
        analysis_paragraphs=[
            "Manly host South Sydney at 4 Pines Park on Thursday night with both sides receiving major boosts from injury and Origin returns. Haumole Olakau'atu returns from a week's rest to give the home side's left edge its bite back, while Tolu Koula has been named pending HIA clearance after failing a check during Origin I. The Sea Eagles pack &mdash; Paseka, Hetherington, Ben and Jake Trbojevic &mdash; should dominate field position around the Brooks/Fogarty steering combination.",
            "South Sydney are buoyed by the long-awaited return of David Fifita (hamstring, first game since Round 6), Brandon Smith from a calf injury, Cameron Murray and Campbell Graham (calf). Tallis Duncan shifts to the back row and Keaon Koloamatangi moves to the front row to accommodate. Jye Gray reclaims the No.1 jersey from Matt Dufty. But Latrell Mitchell remains sidelined with a back complaint and any spine missing its best playmaker is going to take time to find rhythm.",
            "At $1.57 the moneyline has zero value. The play is the &minus;4.5 line at $1.94 &mdash; Manly's edge talent, home venue and a Souths side that needs a re-set after a fortnight of injury chaos should be enough to cover. Jason Saab gets the anytime tryscorer pick &mdash; Manly's strike winger off Fogarty's kicking game with a heavy forward edge feeding him."
        ],
        team_form_home="Olakau'atu returns from rest, Koula named pending HIA clearance. Full Trbojevic-led pack at 4 Pines.",
        team_form_away="Big ins: Fifita (R6 return from hamstring), Smith (calf), Murray, Graham (calf). Still no Latrell Mitchell (back).",
        injury_summary="Manly: Olakau'atu returns from rest; Koula pending HIA clearance; Bullemor OUT. Souths: Fifita, Smith, Murray, Graham, Garlick all back from injury; Latrell still out with back."
    ),
    'storm-vs-knights': dict(
        tip_label='Storm -4.5', tip_odds='1.93', tip_type='Line',
        tip_sub="Full Hughes/Munster/Grant/Faalogo spine &middot; Knights spine disrupted with Sandon Smith out &middot; Sportsbet",
        tryscorer='Will Warbrick', tryscorer_sub="Storm right winger &middot; Consistent late-game finisher &middot; Betr",
        odds_form="Storm $1.61, Knights $2.32. Handicap: Storm &minus;4.5 $1.93, Knights +4.5 $1.87. Storm full-strength at home vs a Knights spine missing Sandon Smith &mdash; line is conservative.",
        analysis_hub="Storm at AAMI with full firepower &mdash; Hughes, Munster, Grant and Faalogo all named. Newcastle are working around Sandon Smith (calf) which sees Fletcher Sharpe shift to five-eighth and Fletcher Hunt come off the bench into the centres. Dylan Brown at halfback with an inexperienced Sharpe is a tall ask. Storm forwards roll yardage and Munster pulls the strings &mdash; -4.5 is conservative.",
        analysis_paragraphs=[
            "Friday night football opens with the Storm welcoming Newcastle to AAMI Park, and Craig Bellamy names a full-strength spine: Jahrome Hughes, Cameron Munster, Harry Grant and Sualauvi Faalogo. With Nick Meaney sidelined (calf), Manaia Waitere starts in the centres after a productive bench cameo against the Roosters. Shawn Blore is listed in the reserves as he works back from concussion.",
            "Newcastle's preparation has been disrupted by Sandon Smith's calf injury. Fletcher Sharpe shifts from the back to five-eighth and Fletcher Hunt promotes off the bench into the centres. Dylan Brown is asked to steer the ship at halfback alongside an inexperienced playmaker, while Francis Manuleleua is the new face on the six-man bench. Thomas Cant looks set for game time after going unused last week.",
            "On a track Melbourne defend like a fortress, the &minus;4.5 line is fair value. The Storm forward pack &mdash; Utoikamanu, King, Loiero &mdash; should dominate yardage and Munster will pull strings from the back. Will Warbrick gets the anytime tryscorer pick: the Storm right winger has consistently finished late-game strike plays and the matchup gives him plenty of width."
        ],
        team_form_home="Full-strength spine. Meaney OUT (calf), Waitere starts centres. Blore reserves, back from concussion.",
        team_form_away="Sandon Smith OUT (calf). Sharpe to 5/8, Hunt into centres, Manuleleua debuts on bench.",
        injury_summary="Storm: Meaney OUT (calf), Waitere starts. Knights: Sandon Smith OUT (calf), Sharpe shifts to 5/8, Manuleleua first bench appearance."
    ),
    'raiders-vs-roosters': dict(
        tip_label='Roosters -2.5', tip_odds='1.90', tip_type='Line',
        tip_sub="Full Roosters spine (Tedesco/DCE/Walker/Robson) &middot; Raiders cover for Kris &middot; Sportsbet",
        tryscorer='James Tedesco', tryscorer_sub="Roosters captain at fullback &middot; Has scoring runs in him every game &middot; Betr",
        odds_form="Raiders $2.20, Roosters $1.67. Handicap: Raiders +2.5 $1.90, Roosters &minus;2.5 $1.90. Quality Roosters spine on the road cover the short line.",
        analysis_hub="Roosters favoured despite the road trip at 2.5 points. Trent Robinson's spine of Tedesco, Cherry-Evans, Walker and Robson is settled and Canberra cover for Seb Kris (concussion) with Daine Laurie shifting from lock to centre. Jayden Brailey returns from concussion to slot in at lock and Joe Roddy (hand) joins the bench. Roosters experience at halfback &mdash; DCE vs Sanders &mdash; tilts this on the road.",
        analysis_paragraphs=[
            "GIO Stadium hosts a top-eight showdown with the Roosters listed as 2.5-point favourites despite the road trip. Trent Robinson's spine of Tedesco, Cherry-Evans, Walker and Robson is settled. The pack &mdash; Whyte, Collins, Crichton, Radley &mdash; matches Canberra's physicality blow for blow. Mark Nawaqanitawase is named in the extended squad as he chases a return from a syndesmosis injury suffered in Round 9.",
            "The Raiders cover for Seb Kris (concussion) with Daine Laurie shifting from lock to centre. Jayden Brailey returns from concussion to slot in at lock and Joe Roddy joins the bench from a hand injury. Strange and Sanders have to find continuity against an experienced Cherry-Evans/Walker combination, which is the matchup that decides the contest.",
            "The Roosters' experience at halfback and a settled forward pack edges this on the road. James Tedesco gets the anytime tryscorer pick &mdash; the captain has scoring runs in him every game and the Roosters' attacking shape gives the No.1 plenty of late-game touches."
        ],
        team_form_home="Kris OUT (concussion). Laurie shifts to centre, Brailey returns from concussion at lock. Roddy back from hand.",
        team_form_away="No changes from Storm loss. Nawaqanitawase chases syndesmosis return.",
        injury_summary="Raiders: Kris OUT (concussion), Uta out, Laurie shifts to centre, Brailey returns at lock. Roosters: No changes, Nawaqanitawase listed in extended squad."
    ),
    'cowboys-vs-dolphins': dict(
        tip_label='Dolphins -3.5', tip_odds='1.86', tip_type='Line',
        tip_sub="MASSIVE Dolphins ins: Tabuai-Fidow, Farnworth, Nikorima, Plath, Cobbo all back &middot; Sportsbet",
        tryscorer='Herbie Farnworth', tryscorer_sub="Dolphins strike centre returning from hamstring &middot; Betr",
        odds_form="Cowboys $2.39, Dolphins $1.58. Handicap: Cowboys +3.5 $1.95, Dolphins &minus;3.5 $1.86. Dolphins essentially full-strength back vs Cowboys carrying a Mikaele knee concern.",
        analysis_hub="A re-energised Dolphins outfit get a full hand back: Tabuai-Fidow (FB), Farnworth (C), Nikorima (5/8), Plath (H) and Cobbo (W) all return from injury or Origin duty. Cowboys welcome back skipper Reuben Cotter from rest with Soni Luke (knee) good to go &mdash; but Tom Mikaele plays through a knee concern. The Phins are essentially full-strength; the Cowboys aren't quite. -3.5 covers on the road.",
        analysis_paragraphs=[
            "Townsville hosts a re-energised Dolphins outfit who get a full hand back at once: Hamiso Tabuai-Fidow at fullback, Herbie Farnworth at centre, Kodi Nikorima at five-eighth, Max Plath at hooker and Selwyn Cobbo on the wing all return from injury or Origin duty. Felise Kaufusi and Brad Schneider slide back to the bench to accommodate.",
            "The Cowboys welcome back skipper Reuben Cotter from rest and have Soni Luke (knee) cleared to play at hooker. Tom Mikaele has been named despite leaving the field in Canberra with a knee concern, which is the worry &mdash; if Mikaele struggles, the Cowboys' rotation gets thin against a Dolphins pack with the better depth.",
            "Effectively the Dolphins are at full strength while North Queensland are working around an injury concern at prop. Backline pace and a settled spine should be enough to cover the road handicap. Herbie Farnworth gets the anytime tryscorer pick &mdash; class strike centre returning from injury straight into a winnable matchup."
        ],
        team_form_home="Cotter back from rest, Soni Luke (knee) good to go. Mikaele plays through knee concern.",
        team_form_away="HUGE INS: Tabuai-Fidow, Farnworth, Nikorima, Plath, Cobbo all back from injury or Origin duty.",
        injury_summary="Cowboys: Cotter + Luke return from rest/knee; Mikaele plays through knee concern. Dolphins: Tabuai-Fidow, Farnworth, Nikorima, Plath, Cobbo all back &mdash; full-strength outfit."
    ),
    'broncos-vs-titans': dict(
        tip_label='Broncos H2H', tip_odds='1.43', tip_type='Head to Head',
        tip_sub="Banker of the round &middot; Walsh/Reynolds at Suncorp &middot; Titans get Tino + Fifita back &middot; Sportsbet",
        tryscorer='Reece Walsh', tryscorer_sub="Broncos fullback &middot; Backs himself in attack every week &middot; Betr",
        odds_form="Broncos $1.43, Titans $2.81. Handicap: Broncos &minus;8.5 $1.97, Titans +8.5 $1.84. Take the H2H banker &mdash; the &minus;8.5 line is steep with Tino + Fifita back for GC.",
        analysis_hub="Saturday night at Suncorp and Brisbane are heavy favourites at $1.43. The line of &minus;8.5 is steep with the Titans getting Tino Fa'asuamaleaui and Jojo Fifita back from Maroons duty. Brisbane lose Pat Carrigan (ankle) &mdash; significant &mdash; with Willison to lock and Duffy promoted to 5/8 (Mam to bench). Banker of the round on H2H. Walsh tryscorer at the Stadium where he loves backing himself.",
        analysis_paragraphs=[
            "Suncorp on a Saturday night with Brisbane heavy favourites at $1.43. Reece Walsh at fullback, Adam Reynolds steering and a forward pack led by Payne Haas: the Broncos are box-office at home. Grant Anderson comes into the centres with Gehamat Shibasaki nursing a knee injury, while the loss of Pat Carrigan (ankle) sees Xavier Willison shift to lock and Jack Gosiewski start in the second row. Thomas Duffy has been promoted to start at five-eighth with Ezra Mam relegated to the bench.",
            "The Titans get a significant boost with captain Tino Fa'asuamaleaui and Jojo Fifita back from Maroons duty. Klese Haas and Jaylan De Groot slide to the interchange to accommodate. Hooker Oliver Pascoe is right to play after going through HIA protocols from Round 12, while Lachlan Ilias and Adam Christensen drop from the squad. The Gold Coast forward pack has the firepower to make Brisbane uncomfortable.",
            "The &minus;8.5 line is steep when the Titans have their two best forwards back. Take the H2H at $1.43 as the banker of the round. Walsh gets the tryscorer pick &mdash; the Broncos fullback backs himself in attack every week and Suncorp is his second home."
        ],
        team_form_home="Carrigan OUT (ankle), Willison to lock, Duffy promoted to 5/8, Mam to bench. Anderson into centres for Shibasaki (knee).",
        team_form_away="Tino Fa'asuamaleaui + Jojo Fifita back from Maroons. Pascoe cleared from HIA.",
        injury_summary="Broncos: Carrigan (ankle) OUT, Shibasaki (knee) OUT. Willison to lock, Duffy promoted to 5/8, Mam to bench. Titans: Tino + Jojo Fifita back from Origin; Haas + De Groot slide to bench."
    ),
    'wests-tigers-vs-panthers': dict(
        tip_label='Tigers +12.5', tip_odds='1.90', tip_type='Line',
        tip_sub="Generous line on a Tigers side playing better than the price &middot; Panthers full strength back &middot; Sportsbet",
        tryscorer="Brian To’o", tryscorer_sub="Panthers left winger back from rest &middot; Set-piece try threat &middot; Betr",
        odds_form="Tigers $4.25, Panthers $1.23. Handicap: Tigers +12.5 $1.90, Panthers &minus;12.5 $1.90. Generous handicap on a Tigers spine that's been competitive lately.",
        analysis_hub="Sunday afternoon at CommBank and Penrith roll out a near-full-strength outfit with Cleary, Yeo and To'o all back from rest. The Tigers' spine of Luai, Madden, Bula and Koroisau has been competitive lately and Mavrik Geyer comes in for Sione Fainu (concussion). Charlie Murray gets his first NRL game of 2026 for Twal (knee). +12.5 is generous &mdash; Tigers stay in the game.",
        analysis_paragraphs=[
            "CommBank Stadium on Sunday afternoon and the Tigers face a near-full-strength Panthers outfit with Nathan Cleary, Isaah Yeo and Brian To'o all back from rest. Jack Cogger, Liam Henry and Izack Tago revert to the bench while Paul Alamoti shifts to centre to accommodate the return of To'o. Utility Jack Cole has been added to the six-man bench while Billy Phillips, Luron Patea and Billy Scott drop to the reserves.",
            "The Tigers' spine (Luai, Madden, Bula, Koroisau) has been competitive lately and the home venue helps. Mavrik Geyer will make his second appearance of the season as he comes in for Sione Fainu (concussion). Lock Charlie Murray gets his first NRL game of 2026 (and sixth of his career) as he replaces Alex Twal (knee). Young gun Ethan Roberts and Bunty Afoa are new faces on the bench. Heamasi Makasini plays through a shoulder concern.",
            "The +12.5 line is generous given the Tigers are playing better football than the price suggests. Penrith will look to roll the Tigers off the park but Tago coming off the bench is below the standard the Panthers usually run with. Brian To'o gets the anytime tryscorer pick &mdash; the Panthers' left wing is back fresh and is the set-piece try threat in this team."
        ],
        team_form_home="Geyer in for Fainu (concussion); Murray first NRL game of 2026 (Twal OUT knee); Makasini plays through shoulder concern.",
        team_form_away="Big guns Cleary, Yeo + To'o back from rest. Alamoti shifts to centre for To'o's return.",
        injury_summary="Wests Tigers: Fainu OUT (concussion), Twal OUT (knee). Geyer + Murray promoted. Panthers: Cleary, Yeo, To'o all back from rest. Phillips/Patea/Scott drop to reserves."
    ),
    'sharks-vs-dragons': dict(
        tip_label='Dragons +11.5', tip_odds='1.99', tip_type='Line',
        tip_sub="Sharks miss Hynes (calf) AND Brailey (arm) &middot; Berrell debut at hooker, Puru at #7 &middot; Sportsbet",
        tryscorer='Valentine Holmes', tryscorer_sub="Dragons strike centre &middot; Finishes everything inside the 10 &middot; Betr",
        odds_form="Sharks $1.29, Dragons $3.64. Handicap: Sharks &minus;11.5 $1.82, Dragons +11.5 $1.99. Without Hynes' kicking game the 11.5 line is generous.",
        analysis_hub="Sharks miss two of their most important players &mdash; Hynes (calf) and Brailey (arm). Niwhai Puru steps in at #7 with Jayden Berrell debuting at hooker in a key role. Dragons have Gutherson, Holmes, Suli, Flanagan and Cook &mdash; experienced and capable of staying in this. Jacob Liddle returns from hamstring. +11.5 is generous on the road.",
        analysis_paragraphs=[
            "Ocean Protect Stadium hosts a local derby with the Sharks missing two of their most important players &mdash; Nicho Hynes (calf) and Blayke Brailey (arm). That's a massive disruption to Cronulla's spine and structure. Niwhai Puru steps in at halfback with Jayden Berrell debuting at hooker in a key role. Briton Nikora is back from rest after Maroons duty, but the spine disruption matters far more.",
            "The Dragons have settled experience &mdash; Clinton Gutherson, Valentine Holmes, Moses Suli, Kyle Flanagan and Damien Cook &mdash; and are capable of staying in this game. Hooker Jacob Liddle returns from a hamstring complaint and damaging edge forward Jaydn Su'A is listed in the reserves as he looks to return from a calf injury. Tyrell Sloan drops back to the reserves after an eight-minute cameo last week.",
            "Without Hynes' kicking game the 11.5-point handicap is generous on the road. Valentine Holmes gets the anytime tryscorer pick as the Dragons' strike centre who finishes everything inside the 10."
        ],
        team_form_home="Hynes OUT (calf), Brailey OUT (arm). Puru at #7, Berrell debuts at hooker. Nikora back from Maroons.",
        team_form_away="Liddle back from hamstring. Su'A in reserves working back from calf. Sloan to reserves.",
        injury_summary="Sharks: Hynes OUT (calf), Brailey OUT (arm). Puru steps in at halfback, Berrell debuts at hooker. Dragons: Liddle returns from hamstring; Su'A close to return from calf."
    ),
    'bulldogs-vs-eels': dict(
        tip_label='Bulldogs -3.5', tip_odds='1.90', tip_type='Line',
        tip_sub="Bulldogs settled 17 at Accor &middot; Eels rebuilding spine &middot; Sportsbet",
        tryscorer='Stephen Crichton', tryscorer_sub="Bulldogs captain centre &middot; Backs himself in attack &middot; Betr",
        odds_form="Bulldogs $1.64, Eels $2.27. Handicap: Bulldogs &minus;3.5 $1.90, Eels +3.5 $1.90. Settled Bulldogs at home over a rebuilding Eels side covers the line.",
        analysis_hub="Monday Night Football slot at Accor and Cameron Ciraldo names a settled 17 with only minor bench tweaks &mdash; O'Sullivan and Spinks added (Hopoi and Sua out). Tracey + Montoya near returns from injury. Parramatta rebuild &mdash; Volkman and Papalii pair in the halves with Tallyn Da Silva at hooker. Bulldogs spine (Galvin, Burton, Mann) plus Crichton has too much class.",
        analysis_paragraphs=[
            "Accor Stadium for the Monday Night Football slot with Canterbury bouncing off a loss to the Tigers. Cameron Ciraldo names a settled 17 with only minor bench tweaks &mdash; Sean O'Sullivan and Logan Spinks added in place of Lipoi Hopoi and Jonathan Sua. Connor Tracey (hamstring) and Marcelo Montoya (knee) are listed among the reserves as they work their way back from injury, which is positive news for the run home.",
            "Parramatta continue to rebuild. Ronald Volkman and Joash Papalii pair up in the halves with Tallyn Da Silva named to start at hooker (Harrison Edwards on the bench, though they could swap on game day as they did against the Knights). After a sternum injury comeback in NSW Cup last weekend, Ryley Smith is listed in the reserves. Teancum Brown has been added to the six-man bench in place of Charlie Guymer.",
            "The Bulldogs' spine (Galvin, Burton, Mann) plus Crichton in the centres has too much class for an Eels side still finding its identity. Canterbury cover the line at home. Stephen Crichton gets the anytime tryscorer pick &mdash; the Bulldogs' captain centre backs himself in attack every week."
        ],
        team_form_home="Settled 17 from Tigers loss. O'Sullivan + Spinks added to bench (Hopoi + Sua out). Tracey + Montoya in reserves nearing returns.",
        team_form_away="Da Silva to start at hooker (Edwards on bench). Ryley Smith in reserves on sternum return. Brown added to bench for Guymer.",
        injury_summary="Bulldogs: Settled lineup; Tracey (hamstring) + Montoya (knee) listed in reserves. Eels: Da Silva starts at hooker; Ryley Smith back in reserves from sternum injury."
    ),
}

# ── Key Team News for hub Late-changes panel (one line per team) ────────────
KEY_NEWS = [
    ("Sea Eagles", "Olakau'atu returns from rest; Koula named pending HIA clearance after Origin I. Bullemor OUT."),
    ("Rabbitohs", "<strong>David Fifita RETURNS</strong> (first game since R6, hamstring), Brandon Smith back (calf), Murray + Graham + Garlick return. Latrell still out."),
    ("Storm", "Full Hughes/Munster/Grant/Faalogo spine. Meaney OUT (calf), Waitere starts centres. Blore in reserves working back from concussion."),
    ("Knights", "<strong>Sandon Smith OUT</strong> (calf). Sharpe shifts to 5/8, Hunt promotes into centres. Manuleleua debuts on six-man bench."),
    ("Raiders", "Kris OUT (concussion). Laurie shifts to centre, Brailey returns from concussion at lock. Roddy back from hand to bench."),
    ("Roosters", "No changes from Storm loss. Mark Nawaqanitawase listed in extended squad chasing syndesmosis return."),
    ("Cowboys", "Cotter back from rest, Soni Luke (knee) good to go. Mikaele plays through knee concern."),
    ("Dolphins", "<strong>MASSIVE INS</strong> &mdash; Tabuai-Fidow, Farnworth, Nikorima, Plath and Cobbo all return from injury or Origin duty."),
    ("Broncos", "<strong>Carrigan OUT</strong> (ankle), Willison to lock, Duffy promoted to 5/8, Mam to bench. Anderson into centres for Shibasaki (knee)."),
    ("Titans", "<strong>Tino Fa'asuamaleaui + Jojo Fifita BACK</strong> from Maroons duty. Klese Haas + De Groot slide to bench."),
    ("Wests Tigers", "Geyer in for Fainu (concussion). Charlie Murray first NRL game of 2026 for Twal (knee). Makasini plays through shoulder concern."),
    ("Panthers", "<strong>Cleary, Yeo + To'o all back</strong> from rest. Alamoti shifts to centre for To'o's return. Tago to bench."),
    ("Sharks", "<strong>Hynes OUT (calf) AND Brailey OUT (arm)</strong>. Puru steps in at halfback, Berrell debuts at hooker. Nikora back from Maroons."),
    ("Dragons", "Liddle back from hamstring. Su'A listed in reserves working back from calf. Sloan to reserves."),
    ("Bulldogs", "Settled 17. O'Sullivan + Spinks added to bench (Hopoi + Sua out). Tracey + Montoya nearing returns."),
    ("Eels", "Tallyn Da Silva named to start at hooker (Edwards on bench). Brown added to bench in place of Guymer."),
]

# ── Confirmed team lists (NRL.com, 2 Jun 2026) ──────────────────────────────
POSITIONS = ['FB', 'W', 'C', 'C', 'W', '5/8', 'HB', 'P', 'H', 'P', '2R', '2R', 'L']

TEAMS = {
    'sea-eagles-vs-rabbitohs': dict(
        home_players=['Clayton Faulalo','Jason Saab','Tolutau Koula','Reuben Garrick','Lehi Hopoate','Luke Brooks','Jamal Fogarty','Taniela Paseka','Jake Simpkin','Kobe Hetherington',"Haumole Olakau’atu",'Ben Trbojevic','Jake Trbojevic','Brandon Wakeham','Nathan Brown','Jackson Shereb','Simione Laiafi','Josh Feledy','Joey Walsh','Blake Wilson','Onitoni Large','Aaron Schoupp'],
        away_players=['Jye Gray','Alex Johnston','Latrell Siegwalt','Campbell Graham','Edward Kosi','Cody Walker','Ashton Ward','Tevita Tatola','Brandon Smith','Keaon Koloamatangi','David Fifita','Tallis Duncan','Cameron Murray','Lachlan Hubner','Jamie Humphreys','Euan Aitken','Sean Keppie','Matthew Dufty','Liam Le Blanc','Moala Graham-Taufa','Bronson Garlick','Thomas Fletcher'],
    ),
    'storm-vs-knights': dict(
        home_players=['Sualauvi Faalogo','Will Warbrick','Jack Howarth','Manaia Waitere','Moses Leo','Cameron Munster','Jahrome Hughes','Stefano Utoikamanu','Harry Grant','Josh King','Cooper Clarke','Ativalu Lisati','Trent Loiero','Trent Toelau','Alec MacDonald','Jack Hetherington','Josiah Pahulu','Joe Chan','Siulagi Tuimalatu-Brown','Shawn Blore','Keagan Russell-Smith','Angus Hinchey'],
        away_players=['Kalyn Ponga','Dominic Young','Dane Gagai','Fletcher Hunt','Greg Marzhew','Fletcher Sharpe','Dylan Brown','Jacob Saifiti','Phoenix Crossland','Trey Mooney','Dylan Lucas','Jermaine McEwen','Mat Croker','Harrison Graham','Tyson Frizell','Pasami Saulo','Thomas Cant','Cody Hopwood','Francis Manuleleua','James Schiller','Kyle McCarthy','Elijah Salesa-Leaumoana'],
    ),
    'raiders-vs-roosters': dict(
        home_players=['Kaeo Weekes','Savelio Tamale','Daine Laurie','Matthew Timoko','Xavier Savage','Ethan Strange','Ethan Sanders','Corey Horsburgh','Tom Starling','Joseph Tapine','Hudson Young','Zac Hosking','Jayden Brailey','Owen Pattie','Ata Mariota','Morgan Smithies','Jed Stuart','Chevy Stewart','Joe Roddy','Coby Black','Vena Patuki-Case','Ethan Alaia'],
        away_players=['James Tedesco','Billy Smith','Hugo Savala','Robert Toia','Cody Ramsey','Daly Cherry-Evans','Sam Walker','Naufahu Whyte','Reece Robson','Lindsay Collins','Angus Crichton','Siua Wong','Victor Radley','Connor Watson','Spencer Leniu','Nat Butcher','Salesi Foketi','Reece Foley','Egan Butcher','Benaiah Ioelu','Tom Rodwell','Mark Nawaqanitawase'],
    ),
    'cowboys-vs-dolphins': dict(
        home_players=['Scott Drinkwater','Zac Laybutt','Jaxon Purdue','Tom Chester','Murray Taulagi','Liam Sutton','Jake Clifford','Thomas Mikaele','Reed Mahoney','Jason Taumalolo','Heilum Luki','Sam McIntyre','Reuben Cotter','Soni Luke','Griffin Neame','Matthew Lodge','Coen Hess','Robert Derby','Ethan King','Wiremu Greig','Viliami Vailea','Xavier Kerrisk'],
        away_players=['Hamiso Tabuai-Fidow','Jamayne Isaako','Jack Bostock','Herbie Farnworth','Selwyn Cobbo','Kodi Nikorima','Isaiya Katoa','Thomas Flegler','Max Plath','Francis Molo','Connelly Lemuelu','Kulikefu Finefeuiaki','Morgan Knowles','Jeremy Marshall-King','Kurt Donoghoe','Tom Gilbert','Ray Stone','Felise Kaufusi','Bradley Schneider','Oryn Keeley','Trai Fuller','Tevita Naufahu'],
    ),
    'broncos-vs-titans': dict(
        home_players=['Reece Walsh','Josiah Karapani','Kotoni Staggs','Grant Anderson','Jesse Arthars','Thomas Duffy','Adam Reynolds','Preston Riki','Cory Paix','Payne Haas','Brendan Piakura','Jack Gosiewski','Xavier Willison','Ben Hunt','Ben Talty',"Va’a Semu",'Aublix Tawha','Ezra Mam','Hayze Perham','Jaiyden Hunt','Phillip Coates','Josh Rogers'],
        away_players=['Keano Kini','Jensen Taumoepeau','Jojo Fifita','AJ Brimson','Phillip Sami','Jayden Campbell','Zane Harrison','Moeaki Fotuaika','Oliver Pascoe',"Tino Fa’asuamaleaui",'Arama Hau','Beau Fermor','Cooper Bai','Kurtis Morrin','Josh Patston','Chris Randall','Klese Haas','Jaylan De Groot','Luke Sommerton','Tony Francis','Bodhi Sharpley','Lachlan Ilias'],
    ),
    'wests-tigers-vs-panthers': dict(
        home_players=['Jahream Bula','Jeral Skelton','Sunia Turuva','Heamasi Makasini','Faaletino Tavana','Jarome Luai','Jock Madden','Terrell May','Apisai Koroisau','Fonua Pole','Mavrik Geyer','Kai Pearce-Paul','Charlie Murray','Latu Fainu','Alex Seyfarth','Royce Hunt','Ethan Roberts','Bunty Afoa',"Starford To’a",'Tristan Hope','Heath Mason','Javon Andrews'],
        away_players=['Dylan Edwards','Thomas Jenkins','Paul Alamoti','Casey McLean',"Brian To’o",'Blaize Talagi','Nathan Cleary','Moses Leota','Freddy Lussick','Lindsay Smith',"Isaiah Papali’i",'Liam Martin','Isaah Yeo','Jack Cogger','Scott Sorensen','Liam Henry','Izack Tago','Luke Garner','Jack Cole','Billy Phillips','Billy Scott','Luron Patea'],
    ),
    'sharks-vs-dragons': dict(
        home_players=['William Kennedy','Samuel Stonestreet','Jesse Ramien','Mawene Hiroti','Ronaldo Mulitalo','Braydon Trindall','Niwhai Puru','Addin Fonua-Blake','Jayden Berrell','Toby Rudolf','Briton Nikora','Teig Wilton','Cameron McInnes','Siosifa Talakai','Billy Burns','Jesse Colquhoun','Thomas Hazelton','Hohepa Puru','Oregon Kaufusi','Riley Jones','KL Iro','Sione Katoa'],
        away_players=['Clinton Gutherson','Setu Tu','Moses Suli','Valentine Holmes','Mathew Feagai','Daniel Atkinson','Kyle Flanagan','Loko Jnr Pasifiki Tonga','Damien Cook','Toby Couchman','Dylan Egan','Hamish Stewart','Ryan Couchman','Jacob Liddle','Josh Kerr','Luciano Leilua','Blake Lawrie','Lyhkan King-Togia','Emre Guler','Tyrell Sloan',"Jaydn Su’A",'Nathan Lawson'],
    ),
    'bulldogs-vs-eels': dict(
        home_players=['Jacob Kiraz','Jethro Rinakama','Bronson Xerri','Stephen Crichton','Enari Tuala','Matt Burton','Lachlan Galvin','Max King','Kurt Mann','Leo Thompson','Sitili Tupouniua','Jaeman Salmon','Harry Hayes','Bailey Hayward','Jed Reardon','Jack Underhill','Josh Curran',"Sean O’Sullivan",'Logan Spinks','Lipoi Hopoi','Connor Tracey','Marcelo Montoya'],
        away_players=['Isaiah Iongi','Brian Kelly','Jordan Samrani','Sean Russell','Josh Addo-Carr','Joash Papalii','Ronald Volkman','Luca Moretti','Tallyn Da Silva','Jack Williams','Kelma Tuilagi','Kitione Kautoga','Jack De Belin','Dylan Walker','Sam Tuivaiti','Toni Mataele','Harrison Edwards','Apa Twidle','Teancum Brown','Charlie Guymer','Ryley Smith','Araz Nanva'],
    ),
}

# ── Page chrome ─────────────────────────────────────────────────────────────
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800;900&family=Inter+Tight:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">'

GTAG = """<script async src="https://www.googletagmanager.com/gtag/js?id=G-X8HMP35PY6"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-X8HMP35PY6');</script>"""

ICONS = '<link rel="icon" type="image/png" sizes="32x32" href="/pg-icon.png"><link rel="icon" type="image/png" sizes="192x192" href="/pg-icon-192.png"><link rel="apple-touch-icon" sizes="192x192" href="/pg-icon-192.png">'

CBAR = '<div class="cbar"><span class="age-pill">18+</span> Gamble responsibly. <strong>Gambling Help:</strong> <a href="tel:1800858858">1800 858 858</a> &middot; <a href="https://www.gamblinghelponline.org.au" target="_blank" rel="noopener">gamblinghelponline.org.au</a></div>'

NAV_HUB = """<header>
  <div class="nav-inner">
    <a href="/" class="nav-logo"><img src="/puntguide-logo.png" alt="PuntGuide"></a>
    <nav><ul class="nav-links">
      <li><a href="/nrl-tips.html">NRL Tips</a></li>
      <li><a href="/nrl-round-14-tips-2026.html" class="active">Round 14</a></li>
      <li><a href="/nrl-ladder-2026.html">NRL Ladder</a></li>
      <li><a href="/nrl-premiership-odds-2026.html">NRL Futures</a></li>
      <li><a href="/best-bookmakers-for-nrl.html">Best for NRL</a></li>
    </ul></nav>
    <a href="/go/?to=betr-nrl" target="_blank" rel="noopener" class="btn-nav">Bet at Betr &rarr;</a>
  </div>
</header>"""

NAV_PM_TMPL = """<nav class="nav-pm">
  <a href="/index.html" class="nav-logo-pm"><img src="/puntguide-logo.png" alt="PuntGuide"></a>
  <ul class="nav-links-pm">
    <li><a href="/nrl-tips.html">NRL Tips</a></li>
    <li><a href="/nrl-round-14-tips-2026.html">Round 14</a></li>
    <li><a href="/nrl-ladder-2026.html">NRL Ladder</a></li>
    <li><a href="/best-bookmakers-for-nrl.html">Best for NRL</a></li>
  </ul>
  <a href="/go/?to=betr-nrl" target="_blank" rel="noopener" class="btn-nav-pm">Bet at Betr &rarr;</a>
</nav>"""

# Sticky right sidebar of 6 bookies
BOOKIE_SIDEBAR = """<aside class="bookie-sidebar">
  <div class="sidebar-hd">Best Bookmakers</div>

  <div class="bookie-card">
    <img src="/betr.png" alt="Betr" class="bookie-logo-box">
    <div class="bookie-body">
      <div class="bookie-title">Best for NRL</div>
      <div class="bookie-desc">NRL specials, multis &amp; try scorer props</div>
    </div>
    <a href="/go/?to=betr-nrl" target="_blank" rel="noopener" class="bookie-claim-btn">Claim</a>
  </div>

  <div class="bookie-card">
    <img src="/sportsbet.png" alt="Sportsbet" class="bookie-logo-box">
    <div class="bookie-body">
      <div class="bookie-title">Deepest NRL Markets</div>
      <div class="bookie-desc">Try scorers, margins &amp; SGM</div>
    </div>
    <a href="/go/?to=sportsbet" target="_blank" rel="noopener" class="bookie-claim-btn">Claim</a>
  </div>

  <div class="bookie-card">
    <img src="/bet365.png" alt="bet365" class="bookie-logo-box">
    <div class="bookie-body">
      <div class="bookie-title">Best Live Betting</div>
      <div class="bookie-desc">In-play NRL &mdash; cash out live</div>
    </div>
    <a href="/go/?to=bet365" target="_blank" rel="noopener" class="bookie-claim-btn">Claim</a>
  </div>

  <div class="bookie-card">
    <img src="/ladbrokes.png" alt="Ladbrokes" class="bookie-logo-box">
    <div class="bookie-body">
      <div class="bookie-title">Australia&rsquo;s #1 Bookie</div>
      <div class="bookie-desc">Huge NRL market range</div>
    </div>
    <a href="/go/?to=ladbrokes" target="_blank" rel="noopener" class="bookie-claim-btn">Claim</a>
  </div>

  <div class="bookie-card">
    <img src="/unibet.png" alt="Unibet" class="bookie-logo-box">
    <div class="bookie-body">
      <div class="bookie-title">Daily Odds Boosts</div>
      <div class="bookie-desc">Log in for NRL boosts &amp; specials</div>
    </div>
    <a href="/go/?to=unibet" target="_blank" rel="noopener" class="bookie-claim-btn">Claim</a>
  </div>

  <div class="bookie-card">
    <img src="/tab.png" alt="TAB" class="bookie-logo-box">
    <div class="bookie-body">
      <div class="bookie-title">Fixed Odds NRL</div>
      <div class="bookie-desc">TAB fixed odds &amp; PocketBet app</div>
    </div>
    <a href="/go/?to=tab" target="_blank" rel="noopener" class="bookie-claim-btn">Claim</a>
  </div>

  <p class="sidebar-legal">18+ only. Gamble responsibly. <a href="/all-betting-sites.html">Compare all 130+ bookmakers &rarr;</a></p>
</aside>"""

BETR_VERT_COL = """<div class="betr-col">
  <div class="banner-label">Advertisement</div>
  <script type="text/javascript" src="https://js.betraffiliates.com.au/javascript.php?prefix=zJS8NRxe1pCYNevImT-MDGNd7ZgqdRLk&amp;media=39&amp;campaign=1"></script>
</div>"""

BETR_BANNER_INLINE = """<div class="inline-ad" style="text-align:center;margin:0 0 28px;">
  <div style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--muted-fg);margin-bottom:6px;font-family:'JetBrains Mono',monospace;">Advertisement</div>
  <div style="overflow:hidden;max-width:min(728px,100%);margin:0 auto;">
    <script type="text/javascript" src="https://js.betraffiliates.com.au/javascript.php?prefix=zJS8NRxe1pCYNevImT-MDGNd7ZgqdRLk&amp;media=14&amp;campaign=1"></script>
  </div>
</div>"""

RESP_BAR = '<div class="resp-bar"><strong>Gamble responsibly.</strong> Tips are editorial opinions only. Always confirm odds before placing. <a href="tel:1800858858">1800 858 858</a> &middot; <a href="https://www.gamblinghelponline.org.au" target="_blank" rel="noopener">gamblinghelponline.org.au</a>. 18+ only.</div>'

PG_FOOTER = """<footer class="pg">
  <a href="/nrl-tips.html">NRL Tips</a><a href="/nrl-round-13-tips-2026.html">Round 13 Tips</a><a href="/nrl-ladder-2026.html">NRL Ladder</a><a href="/nrl-premiership-odds-2026.html">NRL Futures</a><a href="/all-betting-sites.html">All Bookmakers</a>
  <p>PuntGuide provides general information only. Gambling involves risk. 18+ only. Australian residents only.</p>
</footer>"""

# ── CSS (R13 hub layout) ────────────────────────────────────────────────────
CSS_HUB = """:root{--bg:hsl(205 60% 96%);--fg:hsl(215 45% 16%);--primary:hsl(48 92% 64%);--primary-fg:hsl(215 45% 16%);--muted:hsl(205 40% 92%);--muted-fg:hsl(215 20% 42%);--border:hsl(205 40% 86%);--card:hsl(0 0% 100%);--grad-gold:linear-gradient(135deg,hsl(50 96% 72%) 0%,hsl(44 92% 60%) 100%);--shadow-card:0 4px 24px -8px hsl(215 50% 30%/.12);--shadow-gold:0 10px 40px -10px hsl(48 92% 54%/.45);--r:0.875rem}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth;overflow-x:hidden}
body{font-family:'Inter Tight',sans-serif;background:var(--bg);color:var(--fg);line-height:1.6;font-size:15px;overflow-x:hidden}
h1,h2,h3,h4{font-family:'Geist',sans-serif;letter-spacing:-0.035em;font-weight:600}
a{color:var(--fg);text-decoration:none}
.cbar{background:var(--fg);color:rgba(255,255,255,.75);padding:7px 24px;text-align:center;font-size:11.5px;position:fixed;top:0;left:0;right:0;z-index:200}
.cbar a{color:hsl(200 88% 75%);text-decoration:underline}.cbar strong{color:rgba(255,255,255,.92)}
.age-pill{display:inline-block;background:#c0392b;color:#fff;font-weight:700;font-size:10px;padding:1px 7px;border-radius:3px;margin-right:8px;vertical-align:middle}
header{position:fixed;top:36px;left:0;right:0;z-index:100;background:hsl(205 60% 96%/.85);backdrop-filter:blur(20px);border-bottom:1px solid hsl(205 40% 86%/.40)}
.nav-inner{max-width:80rem;margin:0 auto;padding:0 clamp(16px,2.5vw,40px);height:80px;display:flex;align-items:center;justify-content:space-between;gap:24px}
.nav-logo img{height:72px;width:auto}
.nav-links{display:flex;align-items:center;gap:28px;font-size:14px;font-weight:500;list-style:none}
.nav-links a{color:hsl(215 45% 16%/.70);transition:color .15s}
.nav-links a:hover,.nav-links a.active{color:var(--primary)}
.btn-nav{background:var(--grad-gold);color:var(--primary-fg);font-family:'Geist',sans-serif;font-weight:600;font-size:13px;padding:8px 18px;border-radius:8px;border:none;cursor:pointer;box-shadow:var(--shadow-gold);white-space:nowrap;text-decoration:none}
.page-wrap{max-width:90rem;margin:0 auto;display:grid;grid-template-columns:160px minmax(0,1fr) 290px;gap:0 24px;align-items:start;padding:calc(36px + 80px + clamp(32px,5vw,64px)) clamp(16px,3vw,32px) 60px}
.layout-main{max-width:52rem;width:100%}
.betr-col{position:sticky;top:calc(36px + 80px + 24px);display:flex;flex-direction:column;align-items:center;gap:8px;overflow:hidden;flex-shrink:0}
.banner-label{font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--muted-fg);font-family:'JetBrains Mono',monospace;text-align:center}
.bookie-sidebar{position:sticky;top:calc(36px + 80px + 24px)}
.sidebar-hd{font-family:'Geist',sans-serif;font-weight:700;font-size:17px;letter-spacing:-0.025em;margin-bottom:14px;padding-bottom:10px;border-bottom:2px solid var(--fg)}
.bookie-card{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:12px 14px;margin-bottom:10px;display:flex;align-items:center;gap:10px;box-shadow:var(--shadow-card);transition:box-shadow .15s}
.bookie-card:hover{box-shadow:0 8px 32px -8px hsl(215 50% 30%/.16)}
.bookie-logo-box{width:56px;height:56px;border-radius:8px;flex-shrink:0;object-fit:contain;background:#fff;border:1px solid var(--border);padding:4px}
.bookie-body{flex:1;min-width:0}
.bookie-title{font-family:'Geist',sans-serif;font-weight:700;font-size:13px;letter-spacing:-0.01em;line-height:1.3;margin-bottom:2px}
.bookie-desc{font-size:11px;color:var(--muted-fg);line-height:1.35}
.bookie-claim-btn{display:inline-flex;align-items:center;justify-content:center;background:hsl(168 55% 38%);color:#fff;font-family:'Geist',sans-serif;font-weight:700;font-size:12px;padding:8px 14px;border-radius:100px;text-decoration:none;white-space:nowrap;flex-shrink:0;transition:background .15s}
.bookie-claim-btn:hover{background:hsl(168 55% 32%)}
.sidebar-legal{font-size:10px;color:var(--muted-fg);text-align:center;margin-top:12px;line-height:1.55}
.sidebar-legal a{color:var(--primary);text-decoration:underline}
.breadcrumb{font-size:12px;color:var(--muted-fg);margin-bottom:24px;display:flex;align-items:center;gap:6px}
.breadcrumb a{color:var(--primary)}
.article-eyebrow{display:flex;align-items:center;gap:10px;margin-bottom:20px}
.eyebrow-line{height:1px;width:40px;background:var(--primary)}
.eyebrow-text{font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.2em;color:var(--primary)}
.article-title{font-family:'Geist',sans-serif;font-weight:700;font-size:clamp(28px,4vw,44px);letter-spacing:-0.035em;line-height:1.1;margin-bottom:16px}
.article-meta{font-size:13px;color:var(--muted-fg);margin-bottom:32px;padding-bottom:24px;border-bottom:1px solid var(--border)}
.late-changes{background:hsl(16 80% 97%);border:1px solid hsl(16 60% 85%);border-radius:var(--r);padding:16px 20px;margin-bottom:24px}
.late-changes-title{font-family:'JetBrains Mono',monospace;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.15em;color:hsl(16 70% 40%);margin-bottom:10px}
.lc{font-size:13px;color:var(--muted-fg);padding:6px 0;border-bottom:1px solid hsl(16 40% 88%);line-height:1.55}
.lc:last-child{border-bottom:none}.lc strong{color:var(--fg)}
.match-card{background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:24px;margin-bottom:0;box-shadow:var(--shadow-card)}
.match-card:hover{box-shadow:0 8px 32px -8px hsl(215 50% 30%/.16)}
.match-card.featured{border-color:var(--primary);border-width:2px}
.match-header{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-bottom:16px;flex-wrap:wrap}
.match-teams{font-family:'Geist',sans-serif;font-weight:700;font-size:20px;letter-spacing:-0.02em;color:var(--fg)}
.match-info{font-size:12px;color:var(--muted-fg);font-family:'JetBrains Mono',monospace}
.tip-badge{display:inline-flex;align-items:center;gap:4px;background:var(--grad-gold);color:var(--primary-fg);font-family:'JetBrains Mono',monospace;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;padding:4px 12px;border-radius:100px;box-shadow:var(--shadow-gold)}
.match-body{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px}
.match-section-title{font-family:'JetBrains Mono',monospace;font-size:9.5px;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:var(--primary);margin-bottom:6px}
.match-text{font-size:13.5px;color:var(--muted-fg);line-height:1.6}
.suggested-bets{grid-column:1/-1;background:hsl(205 55% 90%/.40);border:1px solid var(--border);border-radius:8px;padding:14px}
.bet-row{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:6px 0;border-bottom:1px solid hsl(205 40% 86%/.50);flex-wrap:wrap}
.bet-row:last-child{border-bottom:none}
.bet-left{display:flex;flex-direction:column;gap:2px}
.bet-desc{font-size:13px;color:var(--fg);font-weight:500}
.bet-sub{font-size:11px;color:var(--muted-fg)}
.bet-cta{display:inline-flex;align-items:center;gap:6px;background:var(--grad-gold);color:var(--primary-fg);font-family:'Geist',sans-serif;font-weight:600;font-size:12px;padding:6px 14px;border-radius:6px;box-shadow:var(--shadow-gold);white-space:nowrap;transition:transform .15s;text-decoration:none}
.bet-cta:hover{transform:scale(1.02)}
.cta-strip{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:12px 0 20px}
.cta-strip a{display:flex;align-items:center;justify-content:center;gap:8px;padding:14px;border-radius:10px;font-family:'Geist',sans-serif;font-weight:700;font-size:13px;text-decoration:none;text-align:center}
.cta-bet{background:hsl(215 45% 16%);color:#fff}
.cta-all{background:var(--grad-gold);color:hsl(215 45% 16%);box-shadow:var(--shadow-gold)}
.section-hd{font-family:'Geist',sans-serif;font-weight:700;font-size:22px;letter-spacing:-0.025em;margin:40px 0 16px;padding-bottom:12px;border-bottom:2px solid var(--fg)}
.pick-box{background:var(--grad-gold);border-radius:var(--r);padding:20px 24px;margin:24px 0;box-shadow:var(--shadow-gold)}
.pick-box-title{font-family:'Geist',sans-serif;font-weight:700;font-size:13px;text-transform:uppercase;letter-spacing:.08em;color:var(--primary-fg);opacity:.75;margin-bottom:4px}
.pick-box-pick{font-family:'Geist',sans-serif;font-weight:800;font-size:22px;letter-spacing:-0.02em;color:var(--primary-fg)}
.pick-box-sub{font-size:13px;color:var(--primary-fg);opacity:.80;margin-top:4px}
.bye-box{background:var(--muted);border-radius:var(--r);padding:16px 20px;margin:24px 0}
.bye-box-title{font-family:'JetBrains Mono',monospace;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.15em;color:var(--muted-fg);margin-bottom:8px}
.bye-teams{display:flex;flex-wrap:wrap;gap:8px}
.bye-team{background:#fff;border:1px solid var(--border);border-radius:6px;padding:4px 12px;font-size:12px;font-weight:600}
.resp-bar{background:hsl(205 55% 90%/.40);border-top:1px solid var(--border);border-bottom:1px solid var(--border);padding:20px clamp(16px,3vw,40px);font-size:13px;color:var(--muted-fg);text-align:center;line-height:1.7;margin-top:60px}
.resp-bar a{color:var(--primary);text-decoration:underline}.resp-bar strong{color:var(--fg)}
footer.pg{background:var(--fg);padding:32px clamp(16px,3vw,40px);text-align:center}
footer.pg a{color:var(--primary);font-size:13px;margin:0 12px}
footer.pg p{font-size:11.5px;color:rgba(255,255,255,.4);margin-top:12px;line-height:1.7}
@media(max-width:1100px){.page-wrap{grid-template-columns:minmax(0,1fr) 290px}.betr-col{display:none}}
@media(max-width:960px){.page-wrap{grid-template-columns:1fr}.bookie-sidebar{position:static}}
@media(max-width:768px){.inline-ad{display:none}}
@media(max-width:640px){.match-body{grid-template-columns:1fr}.nav-links{display:none}.match-header{flex-direction:column;align-items:flex-start}.cta-strip{grid-template-columns:1fr}.bookie-sidebar{width:100%;max-width:100%}}"""

# ── CSS (per-match single-column) ───────────────────────────────────────────
CSS_PM = """:root{--bg:hsl(205 60% 96%);--fg:hsl(215 45% 16%);--primary:hsl(48 92% 64%);--pfg:hsl(215 45% 16%);--muted:hsl(205 40% 92%);--muted-fg:hsl(215 20% 42%);--accent:hsl(200 88% 58%);--border:hsl(205 40% 86%);--gg:linear-gradient(135deg,hsl(50 96% 72%),hsl(44 92% 60%));--sg:0 10px 40px -10px hsl(48 92% 54%/.4);--sc:0 4px 24px -8px hsl(215 50% 30%/.1);--ch:36px;--nh:80px;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--fg);font-family:"Inter Tight",sans-serif;line-height:1.7;font-size:15px;}
h1,h2,h3{font-family:"Geist",sans-serif;letter-spacing:-0.03em;}
a{color:inherit;}img{max-width:100%;}
.cb{position:fixed;top:0;left:0;right:0;height:var(--ch);background:hsl(215 45% 16%);color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 24px;font-size:11px;z-index:200;gap:12px;}
.cb-t{font-weight:700;color:var(--primary);}.cb-h{color:hsl(205 40% 70%);font-size:11px;}.cb-h a{color:var(--accent);text-decoration:none;}
.cb-b{display:flex;gap:6px;}.cb-b span{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);border-radius:4px;padding:2px 6px;font-size:10px;font-weight:700;}
.nav-pm{position:fixed;top:var(--ch);left:0;right:0;height:var(--nh);background:hsl(205 60% 96%/.9);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;padding:0 40px;z-index:100;}
.nav-logo-pm img{height:72px;width:auto;}.nav-links-pm{display:flex;gap:20px;list-style:none;}
.nav-links-pm a{font-size:13px;font-weight:500;color:hsl(215 45% 16%/.7);text-decoration:none;}
.btn-nav-pm{display:inline-flex;align-items:center;background:var(--gg);color:var(--pfg);font-size:13px;font-weight:700;padding:9px 18px;border-radius:10px;text-decoration:none;box-shadow:var(--sg);white-space:nowrap;}
.btn-gold{display:inline-flex;align-items:center;background:var(--gg);color:var(--pfg);font-size:13px;font-weight:700;padding:10px 16px;border-radius:8px;text-decoration:none;box-shadow:var(--sg);}
.pb{padding-top:calc(var(--ch) + var(--nh));}
.hero{padding:44px 32px 36px;background:radial-gradient(ellipse at top,hsl(200 85% 88%),hsl(205 70% 96%) 70%);border-bottom:1px solid var(--border);}
.hero-in{max-width:820px;margin:0 auto;}
.bc{font-size:12px;color:var(--muted-fg);margin-bottom:10px;}.bc a{color:var(--muted-fg);text-decoration:none;}
.eye{display:flex;align-items:center;gap:10px;margin-bottom:12px;}.eye-l{height:1px;width:32px;background:var(--primary);}
.eye-t{font-family:"JetBrains Mono",monospace;font-size:11px;color:var(--primary);text-transform:uppercase;letter-spacing:.2em;}
.wrap{max-width:820px;margin:0 auto;padding:44px 32px 80px;}
.section{margin-bottom:32px;}
.section h2{font-size:20px;font-weight:800;margin-bottom:14px;padding-bottom:10px;border-bottom:1px solid var(--border);}
.section p{font-size:15px;line-height:1.8;margin-bottom:12px;}
.tip-box{background:hsl(215 45% 14%);border-radius:12px;padding:20px 24px;margin:20px 0;}
.tip-label{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.15em;color:var(--primary);font-family:"JetBrains Mono",monospace;margin-bottom:8px;}
.tip-pick{font-size:22px;font-weight:800;font-family:"Geist",sans-serif;color:#fff;margin-bottom:6px;}
.tip-sub{font-size:13px;color:rgba(255,255,255,.65);line-height:1.6;}
.odds-strip{display:flex;gap:8px;flex-wrap:wrap;margin:16px 0;}
.odds-pill{background:hsl(215 45% 16%);border-radius:7px;padding:8px 12px;text-align:center;min-width:80px;}
.odds-pill.our-pick{background:hsl(140 50% 35%);}
.odds-pill-label{font-size:9px;font-weight:700;text-transform:uppercase;color:rgba(255,255,255,.5);letter-spacing:.06em;margin-bottom:2px;}
.odds-pill-val{font-size:17px;font-weight:800;font-family:"JetBrains Mono",monospace;color:#fff;line-height:1;}
.odds-pill-tag{font-size:8px;color:hsl(48 92% 64%);font-weight:700;text-transform:uppercase;margin-top:2px;}
.lineup-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:16px 0;}
.lineup-col{background:#fff;border:1px solid var(--border);border-radius:12px;padding:16px;box-shadow:var(--sc);}
.lineup-col h3{font-size:14px;font-weight:800;margin-bottom:10px;padding-bottom:8px;border-bottom:1px solid var(--border);}
.lineup-players{font-size:12px;color:var(--muted-fg);line-height:1.8;font-family:"JetBrains Mono",monospace;}
.injury-box{background:hsl(16 80% 97%);border:1px solid hsl(16 60% 85%);border-radius:10px;padding:14px 18px;margin:14px 0;font-size:13px;}
.injury-title{font-family:"JetBrains Mono",monospace;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:hsl(16 70% 38%);margin-bottom:6px;}
.bookie-row{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px;margin:14px 0;}
.bookie-tile{background:var(--muted);border-radius:10px;padding:14px;}
.bookie-tile.top{background:hsl(48 80% 97%);border:2px solid hsl(48 60% 70%);}
.bookie-tile-badge{font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:hsl(40 70% 35%);font-family:"JetBrains Mono",monospace;margin-bottom:3px;}
.bookie-tile-name{font-size:16px;font-weight:800;font-family:"Geist",sans-serif;margin-bottom:4px;}
.bookie-tile-reason{font-size:12px;color:var(--muted-fg);line-height:1.5;margin-bottom:10px;}
.bookie-tile-ctas{display:flex;gap:6px;}
.site-footer{background:hsl(215 45% 16%);color:rgba(255,255,255,.7);padding:44px 32px 28px;margin-top:72px;}
.footer-in{max-width:820px;margin:0 auto;}
.footer-logo{height:44px;width:auto;margin-bottom:14px;filter:brightness(0) invert(1);opacity:.75;}
.footer-links{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:28px;}
.footer-links a{font-size:13px;color:rgba(255,255,255,.55);text-decoration:none;}
.footer-rg{font-size:11px;color:rgba(255,255,255,.4);border-top:1px solid rgba(255,255,255,.1);padding-top:20px;line-height:1.8;}.footer-rg a{color:rgba(255,255,255,.4);}
@media(max-width:600px){.lineup-grid{grid-template-columns:1fr;}.nav-links-pm{display:none;}.wrap,.hero{padding-left:16px;padding-right:16px;}.nav-pm{padding:0 20px;}}"""


# ── Helpers ─────────────────────────────────────────────────────────────────

def short_lineup(players):
    """Render compact one-line team list: 1. Name 2. Name ... · Int: ..."""
    starters = ' '.join(f'{i+1}. {players[i]}' for i in range(13))
    bench = ', '.join(players[13:17]) if len(players) >= 17 else ''
    return f"{starters} &middot; Int: {bench}"


def match_card_html(m):
    """Build a match card for the hub."""
    key = f"{m['home_slug']}-vs-{m['away_slug']}"
    p = PICKS[key]
    slug_pm = f"/nrl/2026/round-14/{key}.html"
    featured = m.get('match_of_round', False)
    badge = ('&#11088; Match of Round  -  ' if featured else '&#11088; ') + f"{p['tip_label']} ${p['tip_odds']}"
    card_class = 'match-card featured' if featured else 'match-card'

    return f'''<div class="{card_class}">
  <div class="match-header">
    <div><div class="match-teams">{m['home_full']} v {m['away_full']}</div><div class="match-info">{m['date_short']} &middot; {m['time_str']} &middot; {m['venue']}</div></div>
    <span class="tip-badge">{badge}</span>
  </div>
  <div class="match-body">
    <div><div class="match-section-title">Analysis</div><div class="match-text">{p['analysis_hub']}</div></div>
    <div><div class="match-section-title">Odds &amp; Form</div><div class="match-text">{p['odds_form']}</div></div>
    <div class="suggested-bets"><div class="match-section-title">Suggested Bets</div>
      <div class="bet-row"><div class="bet-left"><span class="bet-desc">Bet 1  -  {p['tip_label']} ${p['tip_odds']}</span><span class="bet-sub">{p['tip_sub']}</span></div><a href="/go/?to=betr-nrl" target="_blank" rel="noopener" class="bet-cta">Bet at Betr &rarr;</a></div>
      <div class="bet-row"><div class="bet-left"><span class="bet-desc">Bet 2  -  {p['tryscorer']} anytime tryscorer</span><span class="bet-sub">{p['tryscorer_sub']}</span></div><a href="/go/?to=betr-nrl" target="_blank" rel="noopener" class="bet-cta">Props &rarr;</a></div>
    </div>
    <div style="margin-top:10px;text-align:right;"><a href="{slug_pm}" style="font-size:12px;font-weight:600;color:hsl(200 88% 58%);text-decoration:none;">Full match analysis &rarr;</a></div>
  </div>
</div>'''


CTA_STRIP = """<div class="cta-strip">
  <a href="/go/?to=betr-nrl" target="_blank" rel="noopener" class="cta-bet">&#127944; Bet at Betr &rarr;</a>
  <a href="/all-betting-sites.html" class="cta-all">&#128203; All 130+ Bookmakers &rarr;</a>
</div>"""


def build_hub():
    motr = next(m for m in MATCHES if m.get('match_of_round'))
    motr_p = PICKS[f"{motr['home_slug']}-vs-{motr['away_slug']}"]

    # Render late-changes (Key Team News) panel
    lc_items = ''.join(f'<div class="lc"><strong>{team}</strong>  -  {note}</div>' for team, note in KEY_NEWS)

    # Render match cards interleaved with CTA strips, plus a banner after 3rd
    cards_html = []
    for i, m in enumerate(MATCHES, 1):
        cards_html.append(match_card_html(m))
        cards_html.append(CTA_STRIP)
        if i == 3:
            cards_html.append(BETR_BANNER_INLINE)
    cards_block = '\n\n'.join(cards_html)

    title = "NRL Round 14 Tips 2026  -  Best Bets, Tryscorers &amp; Match Analysis | PuntGuide"
    desc  = ("NRL Round 14 tips with confirmed team lists. Picks: Manly &minus;4.5, Storm &minus;4.5, Roosters &minus;2.5, "
             "Dolphins &minus;3.5, Broncos H2H banker, Tigers +12.5, Dragons +11.5, Bulldogs &minus;3.5. "
             "Match of the Round: Broncos v Titans. PuntGuide.")

    article_schema = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": "NRL Round 14 Tips 2026",
        "author": {"@type": "Organization", "name": "PuntGuide"},
        "publisher": {"@type": "Organization", "name": "PuntGuide", "logo": {"@type": "ImageObject", "url": "https://puntguide.com.au/puntguide-logo.png"}},
        "datePublished": "2026-06-02", "dateModified": "2026-06-02",
        "mainEntityOfPage": f"{SITE}/nrl-round-14-tips-2026.html",
    }

    html = f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
{GTAG}
<meta charset="UTF-8">
{ICONS}
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/nrl-round-14-tips-2026">
{FONTS}
<meta property="og:title" content="NRL Round 14 Tips 2026 | PuntGuide">
<meta property="og:description" content="NRL Round 14 tips with confirmed team lists and Sportsbet odds. Match of the Round: Broncos v Titans.">
<meta property="og:url" content="{SITE}/nrl-round-14-tips-2026">
<meta property="og:type" content="article">
<meta name="robots" content="index, follow">
<script type="application/ld+json">{json.dumps(article_schema, separators=(',', ':'))}</script>
<style>{CSS_HUB}</style>
</head>
<body>
{CBAR}
{NAV_HUB}
<script src="/nav-drawer.js"></script>
<div class="page-wrap">

{BETR_VERT_COL}

<div class="layout-main">
  <div class="breadcrumb"><a href="/nrl-tips.html">NRL Tips 2026</a><span>&rsaquo;</span><span>Round 14</span></div>
  <div class="article-eyebrow"><span class="eyebrow-line"></span><span class="eyebrow-text">NRL Tips &middot; Round 14 &middot; 4&ndash;8 June 2026</span></div>
  <h1 class="article-title">NRL Round 14 Tips, Predictions &amp; Best Bets</h1>

  <div style="background:hsl(215 45% 16%);border-radius:10px;padding:16px 20px;margin:20px 0;"><div style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:hsl(48 92% 64%);margin-bottom:8px;font-family:'JetBrains Mono',monospace;">Short Answer</div><p style="font-size:15px;line-height:1.75;color:rgba(255,255,255,.9);margin:0;">Eight games from Thursday to Monday, every match shaped by Origin and injury returns. <strong>Broncos H2H $1.43</strong> is the banker of the round at Suncorp and the <strong>Match of the Round</strong>. Big value plays: <strong>Tigers +12.5</strong> at CommBank against a Panthers full-strength back from rest, and <strong>Dragons +11.5</strong> with Sharks missing Hynes AND Brailey. Bye: {BYE_TEAM}.</p></div>

  <div class="article-meta">PuntGuide Editorial &middot; Round 14 &middot; Thu 4 &ndash; Mon 8 June 2026 &middot; Odds: Sportsbet &middot; Team lists confirmed Tuesday 2 June</div>

  <div class="late-changes">
    <div class="late-changes-title">&#9889; Key Team News  -  Round 14</div>
    {lc_items}
  </div>

  <div class="pick-box">
    <div class="pick-box-title">Match of the Round</div>
    <div class="pick-box-pick">{motr['home_full']} v {motr['away_full']}  -  {motr['venue']}, {motr['day']} {motr['time_str']}</div>
    <div class="pick-box-sub">Our tip: {motr_p['tip_label']} ${motr_p['tip_odds']} &middot; Banker of the round &middot; Anytime tryscorer: {motr_p['tryscorer']}</div>
  </div>

  <div style="display:flex;align-items:center;justify-content:space-between;background:#fff;border:1px solid var(--border);border-radius:10px;padding:12px 18px;margin:0 0 24px;box-shadow:0 4px 24px -8px hsl(215 50% 30%/.1);">
    <a href="/nrl-round-13-tips-2026.html" style="font-size:13px;font-weight:600;color:hsl(200 88% 58%);text-decoration:none;">&larr; Round 13 Tips</a>
    <span style="font-size:12px;font-weight:700;font-family:'JetBrains Mono',monospace;color:hsl(215 20% 42%);">ROUND 14 &middot; 4&ndash;8 JUNE 2026</span>
    <span style="font-size:13px;font-weight:600;color:hsl(215 20% 42%);">Round 15 coming &rarr;</span>
  </div>

  {BETR_BANNER_INLINE}

  <h2 class="section-hd">All Round 14 Matches</h2>

  {cards_block}

  <div class="bye-box">
    <div class="bye-box-title">Round 14 Bye</div>
    <div class="bye-teams">
      <span class="bye-team">{BYE_TEAM}</span>
    </div>
  </div>

  <div style="background:hsl(215 45% 16%);border-radius:var(--r);padding:20px 24px;margin:28px 0;">
    <div style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:hsl(48 92% 64%);margin-bottom:8px;font-family:'JetBrains Mono',monospace;">Coming Up  -  17 June</div>
    <div style="font-size:17px;font-weight:700;color:#fff;margin-bottom:6px;">State of Origin Game 2  -  QLD vs NSW, Suncorp Stadium, Brisbane</div>
    <p style="font-size:13px;color:rgba(255,255,255,.7);margin-bottom:12px;">NSW lead 1&ndash;0 after Tedesco&rsquo;s dramatic Game 1 match-winner. Ponga facing suspension. Strange vs Moses the big debate. Our tips: NSW ML + NSW 1&ndash;12 $3.00.</p>
    <a href="/nrl-state-of-origin-2026-game-2.html" style="display:inline-flex;align-items:center;background:var(--grad-gold);color:hsl(215 45% 16%);font-size:13px;font-weight:700;padding:8px 16px;border-radius:8px;text-decoration:none;">Game 2 Preview &rarr;</a>
  </div>

</div><!-- /layout-main -->

{BOOKIE_SIDEBAR}

</div><!-- /page-wrap -->
{RESP_BAR}
{PG_FOOTER}
</body>
</html>"""

    out = os.path.join(OUT, 'nrl-round-14-tips-2026.html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    return 'nrl-round-14-tips-2026.html'


# ── Per-match page (single-column) ──────────────────────────────────────────

def build_match_page(m):
    key = f"{m['home_slug']}-vs-{m['away_slug']}"
    p = PICKS[key]
    t = TEAMS[key]
    out_slug = key  # filename inside /nrl/2026/round-14/
    canonical = f"{SITE}/nrl/2026/round-14/{out_slug}.html"
    title = f"{m['home_full']} v {m['away_full']} Tips  -  NRL Round 14 2026 | PuntGuide"
    desc  = (f"{m['home_nick']} v {m['away_nick']} NRL Round 14 tips and analysis. Our pick: {p['tip_label']} ${p['tip_odds']} "
             f"&middot; {p['tryscorer']} anytime tryscorer. {m['date_str']}, {m['venue']}.")

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "SportsEvent",
             "name": f"{m['home_full']} v {m['away_full']}  -  NRL Round 14 2026",
             "startDate": m['iso_start'],
             "location": {"@type": "Place", "name": m['venue']},
             "sport": "Rugby League",
             "url": canonical},
            {"@type": "Article",
             "headline": f"{m['home_nick']} v {m['away_nick']} Tips  -  NRL Round 14 2026",
             "author": {"@type": "Organization", "name": "PuntGuide"},
             "publisher": {"@type": "Organization", "name": "PuntGuide", "logo": {"@type": "ImageObject", "url": f"{SITE}/puntguide-logo.png"}},
             "datePublished": "2026-06-02", "dateModified": "2026-06-02",
             "mainEntityOfPage": canonical}
        ]
    }

    # Determine which odds pill is "our pick"
    is_home_pick = m['home_nick'] in p['tip_label'] or m['home_full'].split()[-1] in p['tip_label']
    pick_label_h = ' our-pick' if (is_home_pick and 'H2H' in p['tip_type']) else ''
    pick_label_a = ' our-pick' if (not is_home_pick and 'H2H' in p['tip_type']) else ''
    pick_label_line_h = ' our-pick' if (is_home_pick and p['tip_type'] == 'Line') else ''
    pick_label_line_a = ' our-pick' if (not is_home_pick and p['tip_type'] == 'Line') else ''

    analysis_paras = ''.join(f'<p>{para}</p>' for para in p['analysis_paragraphs'])

    home_lineup = short_lineup(t['home_players'])
    away_lineup = short_lineup(t['away_players'])

    # Next match link (sibling within round)
    idx = MATCHES.index(m)
    next_m = MATCHES[(idx + 1) % len(MATCHES)]
    next_key = f"{next_m['home_slug']}-vs-{next_m['away_slug']}"
    next_link = f"/nrl/2026/round-14/{next_key}.html"
    next_name = f"{next_m['home_nick']} v {next_m['away_nick']}"
    motr = next(mm for mm in MATCHES if mm.get('match_of_round'))
    motr_key = f"{motr['home_slug']}-vs-{motr['away_slug']}"
    motr_link = f"/nrl/2026/round-14/{motr_key}.html"
    motr_name = f"{motr['home_nick']} v {motr['away_nick']}"

    html = f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
{GTAG}
<meta charset="UTF-8">
{ICONS}
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{m['home_full']} v {m['away_full']}  -  NRL Round 14 2026 | PuntGuide">
<meta property="og:description" content="Our pick: {p['tip_label']} ${p['tip_odds']}. {m['date_str']}, {m['venue']}.">
<meta property="og:type" content="article">
<meta name="robots" content="index, follow">
<script type="application/ld+json">{json.dumps(schema, separators=(',', ':'))}</script>
{FONTS}
<style>{CSS_PM}</style>
</head>
<body>
<div class="cb"><span class="cb-t">Bet Responsibly</span><span class="cb-h">Gambling Help: <a href="tel:1800858858">1800 858 858</a> &middot; <a href="https://www.gamblinghelponline.org.au" target="_blank" rel="noopener">gamblinghelponline.org.au</a></span><div class="cb-b"><span>18+</span><span>AUS ONLY</span></div></div>
{NAV_PM_TMPL}
<script src="/nav-drawer.js"></script>
<div class="pb">
<div class="hero"><div class="hero-in">
  <div class="bc"><a href="/nrl-tips.html">NRL Tips 2026</a> &rsaquo; <a href="/nrl-round-14-tips-2026.html">Round 14</a> &rsaquo; {m['home_full']} v {m['away_full']}</div>
  <div class="eye"><span class="eye-l"></span><span class="eye-t">&#127944; NRL &middot; Round 14 &middot; {m['date_str']}</span></div>
  <h1>{m['home_full']} v {m['away_full']} Tips &amp; Preview</h1>
  <p style="font-size:16px;color:var(--muted-fg);margin:10px 0 0;">{m['date_str']} &middot; {m['time_str']} AEST &middot; {m['venue']}</p>
  <div style="background:hsl(215 45% 16%);border-radius:10px;padding:16px 20px;margin:20px 0;">
    <div style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:hsl(48 92% 64%);margin-bottom:8px;font-family:'JetBrains Mono',monospace;">Our Picks</div>
    <p style="font-size:16px;font-weight:700;color:#fff;margin:0;">{p['tip_label']} ${p['tip_odds']} &middot; {p['tryscorer']} anytime tryscorer</p>
  </div>
  <p style="font-size:12px;color:var(--muted-fg);font-family:'JetBrains Mono',monospace;margin-top:8px;">Published 2 June 2026 &middot; Odds: Sportsbet &middot; 18+</p>
</div></div>
<div class="wrap">

  <div class="section">
    <h2>Odds</h2>
    <div class="odds-strip">
      <div class="odds-pill{pick_label_h}"><div class="odds-pill-label">{m['home_nick']} H2H</div><div class="odds-pill-val">${m['h2h_home']}</div><div class="odds-pill-tag">{('&#11088; Our Pick' if pick_label_h else '&nbsp;')}</div></div>
      <div class="odds-pill{pick_label_a}"><div class="odds-pill-label">{m['away_nick']} H2H</div><div class="odds-pill-val">${m['h2h_away']}</div><div class="odds-pill-tag">{('&#11088; Our Pick' if pick_label_a else '&nbsp;')}</div></div>
      <div class="odds-pill{pick_label_line_h}"><div class="odds-pill-label">{m['home_nick']} {m['line_home_h']}</div><div class="odds-pill-val">${m['line_home_o']}</div><div class="odds-pill-tag">{('&#11088; Our Pick' if pick_label_line_h else '&nbsp;')}</div></div>
      <div class="odds-pill{pick_label_line_a}"><div class="odds-pill-label">{m['away_nick']} {m['line_away_h']}</div><div class="odds-pill-val">${m['line_away_o']}</div><div class="odds-pill-tag">{('&#11088; Our Pick' if pick_label_line_a else '&nbsp;')}</div></div>
    </div>
    <p style="font-size:12px;color:var(--muted-fg);">Odds from Sportsbet. Always confirm current prices before placing.</p>
  </div>

  <!-- Betr NRL Banner -->
  <div style="margin:0 0 24px;text-align:center;">
    <div style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--muted-fg);margin-bottom:6px;font-family:'JetBrains Mono',monospace;">Advertisement</div>
    <div style="overflow:hidden;max-width:728px;margin:0 auto;">
      <script type="text/javascript" src="https://js.betraffiliates.com.au/javascript.php?prefix=zJS8NRxe1pCYNevImT-MDGNd7ZgqdRLk&amp;media=14&amp;campaign=1"></script>
    </div>
  </div>

  <div class="tip-box">
    <div class="tip-label">&#11088; Our Pick  -  {p['tip_type']}</div>
    <div class="tip-pick">{p['tip_label']} ${p['tip_odds']}</div>
    <div class="tip-sub">{p['tip_sub']}</div>
    <div style="margin-top:14px;display:flex;gap:10px;flex-wrap:wrap;">
      <a href="/go/?to=betr-nrl" target="_blank" rel="noopener" class="btn-gold">Bet at Betr &rarr;</a>
      <a href="/all-betting-sites.html" style="display:inline-flex;align-items:center;background:rgba(255,255,255,.12);color:#fff;font-size:13px;font-weight:600;padding:10px 16px;border-radius:8px;text-decoration:none;">All 130+ Bookmakers &rarr;</a>
    </div>
  </div>

  <div class="tip-box" style="background:hsl(28 70% 18%);">
    <div class="tip-label" style="color:hsl(48 92% 64%);">&#128293; Try Scorer Bet</div>
    <div class="tip-pick">{p['tryscorer']} anytime tryscorer</div>
    <div class="tip-sub">{p['tryscorer_sub']}</div>
    <div style="margin-top:14px;"><a href="/go/?to=betr-nrl" target="_blank" rel="noopener" class="btn-gold">Find Props at Betr &rarr;</a></div>
  </div>

  <div class="section">
    <h2>Match Analysis</h2>
    {analysis_paras}
  </div>

  <div class="section">
    <h2>Form &amp; Team News</h2>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
      <div style="background:#fff;border:1px solid var(--border);border-radius:10px;padding:14px;box-shadow:var(--sc);"><div style="font-size:12px;font-weight:800;margin-bottom:6px;">{m['home_full']}</div><div style="font-size:13px;color:var(--muted-fg);line-height:1.7;">{p['team_form_home']}</div></div>
      <div style="background:#fff;border:1px solid var(--border);border-radius:10px;padding:14px;box-shadow:var(--sc);"><div style="font-size:12px;font-weight:800;margin-bottom:6px;">{m['away_full']}</div><div style="font-size:13px;color:var(--muted-fg);line-height:1.7;">{p['team_form_away']}</div></div>
    </div>
  </div>

  <div class="injury-box">
    <div class="injury-title">&#9889; Injury &amp; Selection News</div>
    <p style="font-size:13px;color:var(--muted-fg);line-height:1.65;">{p['injury_summary']}</p>
  </div>

  <div class="section">
    <h2>Team Lists</h2>
    <div class="lineup-grid">
      <div class="lineup-col"><h3>{m['home_full']}</h3><div class="lineup-players">{home_lineup}</div></div>
      <div class="lineup-col"><h3>{m['away_full']}</h3><div class="lineup-players">{away_lineup}</div></div>
    </div>
    <p style="font-size:11px;color:var(--muted-fg);margin-top:8px;">Confirmed by NRL.com on Tuesday 2 June 2026. Two players omitted 24 hours out, final 19 confirmed 90 minutes before kickoff.</p>
  </div>

  <div style="background:#fff;border:1px solid var(--border);border-radius:14px;padding:24px 28px;margin:24px 0;box-shadow:var(--sc);">
    <h2 style="font-size:18px;font-weight:700;margin-bottom:16px;padding-bottom:10px;border-bottom:1px solid var(--border);">Where to Bet</h2>
    <div class="bookie-row">
      <div class="bookie-tile top"><div class="bookie-tile-badge">&#11088; Try Scorers</div><div class="bookie-tile-name">Betr</div><div class="bookie-tile-reason">Deep NRL player props and same-game multis. Best for {p['tryscorer']} and SGM combos.</div><div class="bookie-tile-ctas"><a href="/go/?to=betr-nrl" target="_blank" rel="noopener" class="btn-gold" style="font-size:12px;padding:7px 12px;">Bet at Betr &rarr;</a><a href="/review-betr.html" style="display:inline-flex;align-items:center;background:transparent;color:var(--fg);font-size:12px;font-weight:600;padding:8px 14px;border-radius:7px;text-decoration:none;border:1px solid var(--border);">Review</a></div></div>
      <div class="bookie-tile"><div class="bookie-tile-name">Sportsbet</div><div class="bookie-tile-reason">Widest NRL line markets. Strong moneyline pricing across all Round 14 games.</div><div class="bookie-tile-ctas"><a href="/go/?to=sportsbet" target="_blank" rel="noopener" class="btn-gold" style="font-size:12px;padding:7px 12px;">Bet Now &rarr;</a><a href="/review-sportsbet.html" style="display:inline-flex;align-items:center;background:transparent;color:var(--fg);font-size:12px;font-weight:600;padding:8px 14px;border-radius:7px;text-decoration:none;border:1px solid var(--border);">Review</a></div></div>
      <div class="bookie-tile"><div class="bookie-tile-name">BetRight</div><div class="bookie-tile-reason">Competitive line markets and best tote on racing. Solid NRL handicap pricing.</div><div class="bookie-tile-ctas"><a href="/go/?to=betright" target="_blank" rel="noopener" class="btn-gold" style="font-size:12px;padding:7px 12px;">Bet Now &rarr;</a><a href="/review-betright.html" style="display:inline-flex;align-items:center;background:transparent;color:var(--fg);font-size:12px;font-weight:600;padding:8px 14px;border-radius:7px;text-decoration:none;border:1px solid var(--border);">Review</a></div></div>
    </div>
    <p style="font-size:12px;color:var(--muted-fg);margin-top:10px;">See <a href="/all-betting-sites.html" style="color:var(--accent);font-weight:600;">all 130+ Australian bookmakers</a> &middot; <a href="/best-bookmakers-for-nrl.html" style="color:var(--accent);font-weight:600;">Best for NRL</a></p>
  </div>

  <div style="background:#fff;border:1px solid var(--border);border-radius:14px;padding:24px 28px;margin:24px 0;box-shadow:var(--sc);">
    <h2 style="font-size:18px;font-weight:700;margin-bottom:14px;padding-bottom:10px;border-bottom:1px solid var(--border);">More Round 14</h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:12px;">
      <a href="/nrl-round-14-tips-2026.html" style="background:var(--muted);border-radius:10px;padding:14px;text-decoration:none;color:var(--fg);display:block;"><div style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--muted-fg);margin-bottom:4px;">Round Hub</div><div style="font-size:14px;font-weight:700;">All Round 14 Tips &rarr;</div></a>
      <a href="{next_link}" style="background:var(--muted);border-radius:10px;padding:14px;text-decoration:none;color:var(--fg);display:block;"><div style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--muted-fg);margin-bottom:4px;">Next Up</div><div style="font-size:14px;font-weight:700;">{next_name} &rarr;</div></a>
      <a href="{motr_link}" style="background:var(--muted);border-radius:10px;padding:14px;text-decoration:none;color:var(--fg);display:block;"><div style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--muted-fg);margin-bottom:4px;">Match of Round</div><div style="font-size:14px;font-weight:700;">{motr_name} &rarr;</div></a>
      <a href="/best-bookmakers-for-nrl.html" style="background:var(--muted);border-radius:10px;padding:14px;text-decoration:none;color:var(--fg);display:block;"><div style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--muted-fg);margin-bottom:4px;">Bookmakers</div><div style="font-size:14px;font-weight:700;">Best for NRL &rarr;</div></a>
    </div>
  </div>

  <p style="font-size:11px;color:var(--muted-fg);text-align:center;margin-top:8px;">Tips are editorial opinions only. Odds correct at time of publishing  -  always confirm before placing. 18+ only. Gamble responsibly.</p>
</div>
</div>
<footer class="site-footer"><div class="footer-in">
  <img src="/puntguide-logo.png" alt="PuntGuide" class="footer-logo">
  <div class="footer-links"><a href="/nrl-tips.html">NRL Tips</a><a href="/nrl-round-14-tips-2026.html">Round 14 Tips</a><a href="/nrl-ladder-2026.html">NRL Ladder</a><a href="/nrl-premiership-odds-2026.html">NRL Futures</a><a href="/all-betting-sites.html">All Bookmakers</a></div>
  <div class="footer-rg">PuntGuide provides general information only. Gambling involves risk. 18+ only. Australian residents only.</div>
</div></footer>
</body>
</html>"""

    os.makedirs(PM_DIR, exist_ok=True)
    out_path = os.path.join(PM_DIR, out_slug + '.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    return f"nrl/2026/round-14/{out_slug}.html"


def main():
    written = [build_hub()]
    for m in MATCHES:
        written.append(build_match_page(m))
    print(f'Wrote {len(written)} files:')
    for f in written:
        print(f'  {f}')


if __name__ == '__main__':
    main()
