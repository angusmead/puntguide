#!/usr/bin/env python3
"""Generate NRL Round 14 2026 hub + 8 per-match pages.

Includes: confirmed team lists (NRL.com, 2 Jun 2026), Sportsbet H2H + line
odds, PuntGuide best bet + tryscorer per match, full analysis, side rails
(vertical Betr banner left, Top 6 bookmakers right), and a 6-tile bookmakers
section linking to /all-betting-sites.html and /go/?to=betr.
"""
import os, json

OUT  = os.path.expanduser('~/puntguide')
SITE = 'https://puntguide.com.au'

# ── Fixture (home, away, kickoff, venue, odds) ───────────────────────────────
MATCHES = [
    dict(
        home_full='Manly Sea Eagles', home_slug='sea-eagles', home_nick='Manly',
        away_full='South Sydney Rabbitohs', away_slug='rabbitohs', away_nick='Souths',
        day='Thursday', date_str='Thursday, 4 June 2026', date_short='4 Jun', time_str='7:50 PM',
        iso_start='2026-06-04T19:50:00+10:00', iso_end='2026-06-04T21:50:00+10:00',
        venue='4 Pines Park',
        h2h_home='1.57', h2h_away='2.40',
        line_home_h='-4.5', line_home_o='1.94', line_away_h='+4.5', line_away_o='1.86',
    ),
    dict(
        home_full='Melbourne Storm', home_slug='storm', home_nick='Storm',
        away_full='Newcastle Knights', away_slug='knights', away_nick='Knights',
        day='Friday', date_str='Friday, 5 June 2026', date_short='5 Jun', time_str='6:00 PM',
        iso_start='2026-06-05T18:00:00+10:00', iso_end='2026-06-05T20:00:00+10:00',
        venue='AAMI Park',
        h2h_home='1.61', h2h_away='2.32',
        line_home_h='-4.5', line_home_o='1.93', line_away_h='+4.5', line_away_o='1.87',
    ),
    dict(
        home_full='Canberra Raiders', home_slug='raiders', home_nick='Raiders',
        away_full='Sydney Roosters', away_slug='roosters', away_nick='Roosters',
        day='Friday', date_str='Friday, 5 June 2026', date_short='5 Jun', time_str='8:00 PM',
        iso_start='2026-06-05T20:00:00+10:00', iso_end='2026-06-05T22:00:00+10:00',
        venue='GIO Stadium',
        h2h_home='2.20', h2h_away='1.67',
        line_home_h='+2.5', line_home_o='1.90', line_away_h='-2.5', line_away_o='1.90',
    ),
    dict(
        home_full='North Queensland Cowboys', home_slug='cowboys', home_nick='Cowboys',
        away_full='Dolphins', away_slug='dolphins', away_nick='Dolphins',
        day='Saturday', date_str='Saturday, 6 June 2026', date_short='6 Jun', time_str='5:30 PM',
        iso_start='2026-06-06T17:30:00+10:00', iso_end='2026-06-06T19:30:00+10:00',
        venue='Queensland Country Bank Stadium',
        h2h_home='2.39', h2h_away='1.58',
        line_home_h='+3.5', line_home_o='1.95', line_away_h='-3.5', line_away_o='1.86',
    ),
    dict(
        home_full='Brisbane Broncos', home_slug='broncos', home_nick='Broncos',
        away_full='Gold Coast Titans', away_slug='titans', away_nick='Titans',
        day='Saturday', date_str='Saturday, 6 June 2026', date_short='6 Jun', time_str='7:35 PM',
        iso_start='2026-06-06T19:35:00+10:00', iso_end='2026-06-06T21:35:00+10:00',
        venue='Suncorp Stadium',
        h2h_home='1.43', h2h_away='2.81',
        line_home_h='-8.5', line_home_o='1.97', line_away_h='+8.5', line_away_o='1.84',
    ),
    dict(
        home_full='Wests Tigers', home_slug='wests-tigers', home_nick='Tigers',
        away_full='Penrith Panthers', away_slug='panthers', away_nick='Panthers',
        day='Sunday', date_str='Sunday, 7 June 2026', date_short='7 Jun', time_str='2:00 PM',
        iso_start='2026-06-07T14:00:00+10:00', iso_end='2026-06-07T16:00:00+10:00',
        venue='CommBank Stadium',
        h2h_home='4.25', h2h_away='1.23',
        line_home_h='+12.5', line_home_o='1.90', line_away_h='-12.5', line_away_o='1.90',
    ),
    dict(
        home_full='Cronulla Sharks', home_slug='sharks', home_nick='Sharks',
        away_full='St George Illawarra Dragons', away_slug='dragons', away_nick='Dragons',
        day='Sunday', date_str='Sunday, 7 June 2026', date_short='7 Jun', time_str='4:05 PM',
        iso_start='2026-06-07T16:05:00+10:00', iso_end='2026-06-07T18:05:00+10:00',
        venue='Ocean Protect Stadium',
        h2h_home='1.29', h2h_away='3.64',
        line_home_h='-11.5', line_home_o='1.82', line_away_h='+11.5', line_away_o='1.99',
    ),
    dict(
        home_full='Canterbury Bulldogs', home_slug='bulldogs', home_nick='Bulldogs',
        away_full='Parramatta Eels', away_slug='eels', away_nick='Eels',
        day='Monday', date_str='Monday, 8 June 2026', date_short='8 Jun', time_str='4:05 PM',
        iso_start='2026-06-08T16:05:00+10:00', iso_end='2026-06-08T18:05:00+10:00',
        venue='Accor Stadium',
        h2h_home='1.64', h2h_away='2.27',
        line_home_h='-3.5', line_home_o='1.90', line_away_h='+3.5', line_away_o='1.90',
    ),
]

BYE_TEAM = 'New Zealand Warriors'

# ── PuntGuide picks (Best Bet + Tryscorer + analysis) ────────────────────────
PICKS = {
    'sea-eagles-vs-rabbitohs': dict(
        tip_type='Line', tip_label='Manly Sea Eagles -4.5', tip_odds='1.94',
        tip_short='Manly -4.5', tryscorer='Jason Saab',
        analysis="Manly host Souths at 4 Pines with both sides receiving major boosts. Haumole Olakau'atu's return from rest gives Manly's left edge teeth, while Tolu Koula slots back in pending HIA clearance after Origin I. The Sea Eagles forward pack &mdash; Paseka, Hetherington and the Trbojevic brothers &mdash; should dominate field position around Brooks and Fogarty. South Sydney get David Fifita (hamstring), Brandon Smith (calf), Cameron Murray and Campbell Graham (calf) all back from injury, but the spine is still patched without Latrell Mitchell. Cody Walker and Ashton Ward must combine quickly without their usual support. Manly's edge talent and home venue should cover the -4.5 comfortably, and Saab gets the tryscorer nod as the league's most prolific winger this season.",
    ),
    'storm-vs-knights': dict(
        tip_type='Line', tip_label='Melbourne Storm -4.5', tip_odds='1.93',
        tip_short='Storm -4.5', tryscorer='Will Warbrick',
        analysis="The Storm welcome the Knights to AAMI Park with a fully-loaded spine of Hughes, Munster, Grant and Faalogo. Newcastle have been ravaged by injury: Sandon Smith's calf issue means Fletcher Sharpe shifts to five-eighth and Fletcher Hunt comes off the bench into the centres. Dylan Brown at halfback alongside an inexperienced Sharpe is a tall ask against a Storm forward pack rolling out Utoikamanu, King and Loiero. Melbourne will dominate yardage and Munster will pull strings from the back. The -4.5 line is conservative for a side this dominant at home. Warbrick gets the tryscorer pick as Storm's right winger consistently finishes off late-game strike plays.",
    ),
    'raiders-vs-roosters': dict(
        tip_type='Line', tip_label='Sydney Roosters -2.5', tip_odds='1.90',
        tip_short='Roosters -2.5', tryscorer='James Tedesco',
        analysis="GIO Stadium hosts a top-eight showdown with the Roosters listed as 2.5-point favourites despite the road trip. Trent Robinson's spine of Tedesco, Cherry-Evans, Walker and Robson is settled, while Canberra cover for Seb Kris (concussion) with Daine Laurie shifting from lock to centre. Jayden Brailey returns from concussion to slot in at lock. The Roosters pack &mdash; Whyte, Collins, Crichton, Radley &mdash; matches the Raiders' physicality and the experience differential at halfback (DCE vs Sanders) tilts the play. The Roosters cover the line on the road. Tedesco gets the tryscorer pick &mdash; the captain at fullback has scoring runs in him every game and the Roosters' attacking shape gives him plenty of late-game opportunities.",
    ),
    'cowboys-vs-dolphins': dict(
        tip_type='Line', tip_label='Dolphins -3.5', tip_odds='1.86',
        tip_short='Dolphins -3.5', tryscorer='Herbie Farnworth',
        analysis="Townsville hosts a re-energised Dolphins outfit who get a full hand back: Hamiso Tabuai-Fidow at fullback, Herbie Farnworth at centre, Kodi Nikorima at five-eighth, Max Plath at hooker and Selwyn Cobbo on the wing all return from injury or Origin duty. The Cowboys welcome back skipper Reuben Cotter from rest, with Reed Mahoney solid at hooker, but Tom Mikaele plays through a knee concern. Effectively the Dolphins are at full strength while North Queensland aren't. Dolphins backline pace and a settled spine should cover the road handicap. Farnworth is the tryscorer pick &mdash; class strike centre returning from injury straight into a winnable matchup.",
    ),
    'broncos-vs-titans': dict(
        tip_type='Head to Head', tip_label='Brisbane Broncos to Win', tip_odds='1.43',
        tip_short='Broncos H2H', tryscorer='Reece Walsh',
        analysis="Suncorp on a Saturday night with Brisbane heavy favourites at $1.43. The line of -8.5 is steep with the Titans getting captain Tino Fa'asuamaleaui and Jojo Fifita back from Maroons duty. Brisbane lose Pat Carrigan (ankle) &mdash; significant &mdash; with Xavier Willison shifting to lock. Thomas Duffy promoted to start at five-eighth, Ezra Mam to the bench. The Broncos have the better roster and Adam Reynolds at home is hard to beat, but covering -8.5 against a more competitive Titans pack is the worry. Take the H2H for security &mdash; banker of the round. Walsh gets the tryscorer pick &mdash; Brisbane's fullback backs himself in attack and has the matchup to cross.",
    ),
    'wests-tigers-vs-panthers': dict(
        tip_type='Line', tip_label='Wests Tigers +12.5', tip_odds='1.90',
        tip_short='Tigers +12.5', tryscorer='Brian To’o',
        analysis="CommBank Stadium on Sunday afternoon and the Tigers face a near-full-strength Panthers outfit with Nathan Cleary, Isaah Yeo and Brian To'o all back from rest. The Tigers' spine (Luai, Madden, Bula, Koroisau) has been competitive lately and Heamasi Makasini has been named despite a shoulder concern. Ivan Cleary's side will look to roll the Tigers off the park but Penrith's bench is fairly rookie with Tago at 17. The Bula-Skelton pairing should keep the margin manageable. The +12.5 line is generous given the Tigers are playing better football than the price suggests. To'o is the tryscorer &mdash; Panthers' left wing back fresh, set-piece try threat.",
    ),
    'sharks-vs-dragons': dict(
        tip_type='Line', tip_label='St George Illawarra Dragons +11.5', tip_odds='1.99',
        tip_short='Dragons +11.5', tryscorer='Valentine Holmes',
        analysis="Ocean Protect Stadium hosts the local derby with the Sharks missing two of their most important players &mdash; Nicho Hynes (calf) and Blayke Brailey (arm). Niwhai Puru steps in at halfback with Jayden Berrell debuting at hooker in a key role. That's a massive disruption to Cronulla's spine and structure. The Dragons have Gutherson, Holmes, Suli, Flanagan and Cook &mdash; experienced, settled, and capable of staying in this game. Jacob Liddle's return from hamstring strengthens the bench. Without Hynes' kicking game the 11.5-point handicap is generous. Holmes gets the tryscorer pick as Dragons' strike centre who finishes everything inside the 10.",
    ),
    'bulldogs-vs-eels': dict(
        tip_type='Line', tip_label='Canterbury Bulldogs -3.5', tip_odds='1.90',
        tip_short='Bulldogs -3.5', tryscorer='Stephen Crichton',
        analysis="Accor Stadium for the Monday Night Football slot with Canterbury bouncing off a loss to the Tigers. Cameron Ciraldo names a settled 17 with only minor bench tweaks &mdash; Sean O'Sullivan and Logan Spinks added in place of Lipoi Hopoi and Jonathan Sua. Connor Tracey (hamstring) and Marcelo Montoya (knee) are nearing returns from injury. Parramatta continue to rebuild &mdash; Volkman and Papalii pair up in the halves with Tallyn Da Silva at hooker. The Bulldogs' spine (Galvin, Burton, Mann) plus Crichton in the centres has too much class for an Eels side still finding its identity. Canterbury cover at home. Crichton tryscorer &mdash; Bulldogs' captain centre backs himself in attack.",
    ),
}

# ── Confirmed team lists (NRL.com, 2 Jun 2026 03:59 PM) ──────────────────────
POSITIONS = ['FB', 'W', 'C', 'C', 'W', '5/8', 'HB', 'P', 'H', 'P', '2R', '2R', 'L']

TEAMS = {
    'sea-eagles-vs-rabbitohs': dict(
        home_players=['Clayton Faulalo','Jason Saab','Tolutau Koula','Reuben Garrick','Lehi Hopoate','Luke Brooks','Jamal Fogarty','Taniela Paseka','Jake Simpkin','Kobe Hetherington',"Haumole Olakau’atu",'Ben Trbojevic','Jake Trbojevic','Brandon Wakeham','Nathan Brown','Jackson Shereb','Simione Laiafi','Josh Feledy','Joey Walsh','Blake Wilson','Onitoni Large','Aaron Schoupp'],
        away_players=['Jye Gray','Alex Johnston','Latrell Siegwalt','Campbell Graham','Edward Kosi','Cody Walker','Ashton Ward','Tevita Tatola','Brandon Smith','Keaon Koloamatangi','David Fifita','Tallis Duncan','Cameron Murray','Lachlan Hubner','Jamie Humphreys','Euan Aitken','Sean Keppie','Matthew Dufty','Liam Le Blanc','Moala Graham-Taufa','Bronson Garlick','Thomas Fletcher'],
        home_ins=['Aaron Schoupp',"Haumole Olakau’atu",'Onitoni Large','Tolutau Koula'],
        home_outs=['Ethan Bullemor'],
        away_ins=['Brandon Smith','Bronson Garlick','Cameron Murray','Campbell Graham','David Fifita','Moala Graham-Taufa'],
        away_outs=['Adam Elliott','Peter Mamouzelos','Talanoa Penitani'],
        home_note="Back-rower Haumole Olakau’atu returns after being rested last week while Tolu Koula has been named pending a clearance from the NRL after he failed a HIA in Origin I. Josh Feledy and Jackson Shereb slide to the bench and Ethan Bullemor makes way.",
        away_note="Rampaging forward David Fifita has been named to make his first appearance since Round 6 after recovering from a hamstring injury. Tallis Duncan also shifts to the back row, with Keaon Koloamatangi returning to the front-row and Euan Aitken dropping back to the interchange. Hooker Brandon Smith has also been listed to return from a calf injury in another big boost for Wayne Bennett's side. Still no Latrell Mitchell as he battles a back injury but Campbell Graham has been named to return from a calf injury in the centres. Jye Gray reclaims the starting fullback role, with Matt Dufty dropping back to the bench.",
    ),
    'storm-vs-knights': dict(
        home_players=['Sualauvi Faalogo','Will Warbrick','Jack Howarth','Manaia Waitere','Moses Leo','Cameron Munster','Jahrome Hughes','Stefano Utoikamanu','Harry Grant','Josh King','Cooper Clarke','Ativalu Lisati','Trent Loiero','Trent Toelau','Alec MacDonald','Jack Hetherington','Josiah Pahulu','Joe Chan','Siulagi Tuimalatu-Brown','Shawn Blore','Keagan Russell-Smith','Angus Hinchey'],
        away_players=['Kalyn Ponga','Dominic Young','Dane Gagai','Fletcher Hunt','Greg Marzhew','Fletcher Sharpe','Dylan Brown','Jacob Saifiti','Phoenix Crossland','Trey Mooney','Dylan Lucas','Jermaine McEwen','Mat Croker','Harrison Graham','Tyson Frizell','Pasami Saulo','Thomas Cant','Cody Hopwood','Francis Manuleleua','James Schiller','Kyle McCarthy','Elijah Salesa-Leaumoana'],
        home_ins=['Angus Hinchey','Keagan Russell-Smith','Shawn Blore','Siulagi Tuimalatu-Brown'],
        home_outs=['Nick Meaney'],
        away_ins=['Elijah Salesa-Leaumoana','Francis Manuleleua','James Schiller','Kyle McCarthy'],
        away_outs=['Sandon Smith'],
        home_note="With Nick Meaney (calf) sidelined, Manaia Waitere starts in the centres after coming off the bench against the Roosters. Back-rower Shawn Blore has been listed among the reserves as he looks to return from concussion.",
        away_note="The injury to Sandon Smith (calf) sees Fletcher Sharpe move to five-eighth and Fletcher Hunt from the bench into the centres. Francis Manuleleua is the new face on the six-man interchange while Thomas Cant looks set to see game time after going unused last week.",
    ),
    'raiders-vs-roosters': dict(
        home_players=['Kaeo Weekes','Savelio Tamale','Daine Laurie','Matthew Timoko','Xavier Savage','Ethan Strange','Ethan Sanders','Corey Horsburgh','Tom Starling','Joseph Tapine','Hudson Young','Zac Hosking','Jayden Brailey','Owen Pattie','Ata Mariota','Morgan Smithies','Jed Stuart','Chevy Stewart','Joe Roddy','Coby Black','Vena Patuki-Case','Ethan Alaia'],
        away_players=['James Tedesco','Billy Smith','Hugo Savala','Robert Toia','Cody Ramsey','Daly Cherry-Evans','Sam Walker','Naufahu Whyte','Reece Robson','Lindsay Collins','Angus Crichton','Siua Wong','Victor Radley','Connor Watson','Spencer Leniu','Nat Butcher','Salesi Foketi','Reece Foley','Egan Butcher','Benaiah Ioelu','Tom Rodwell','Mark Nawaqanitawase'],
        home_ins=['Coby Black','Ethan Alaia','Jayden Brailey','Joe Roddy','Vena Patuki-Case'],
        home_outs=['Jordan Uta','Sebastian Kris'],
        away_ins=['Benaiah Ioelu','Mark Nawaqanitawase','Tom Rodwell'],
        away_outs=[],
        home_note="The versatile Daine Laurie moves from lock to centre to cover for Seb Kris (concussion). Jayden Brailey is back from concussion and slots in at lock. Back-rower Joe Roddy has recovered from a hand injury and joins the six-man bench.",
        away_note="No changes for Trent Robinson despite the disappointing loss to the Storm. Star winger Mark Nawaqanitawase is part of the extended squad as he chases a return from a syndesmosis injury suffered in Round 9 that required surgery.",
    ),
    'cowboys-vs-dolphins': dict(
        home_players=['Scott Drinkwater','Zac Laybutt','Jaxon Purdue','Tom Chester','Murray Taulagi','Liam Sutton','Jake Clifford','Thomas Mikaele','Reed Mahoney','Jason Taumalolo','Heilum Luki','Sam McIntyre','Reuben Cotter','Soni Luke','Griffin Neame','Matthew Lodge','Coen Hess','Robert Derby','Ethan King','Wiremu Greig','Viliami Vailea','Xavier Kerrisk'],
        away_players=['Hamiso Tabuai-Fidow','Jamayne Isaako','Jack Bostock','Herbie Farnworth','Selwyn Cobbo','Kodi Nikorima','Isaiya Katoa','Thomas Flegler','Max Plath','Francis Molo','Connelly Lemuelu','Kulikefu Finefeuiaki','Morgan Knowles','Jeremy Marshall-King','Kurt Donoghoe','Tom Gilbert','Ray Stone','Felise Kaufusi','Bradley Schneider','Oryn Keeley','Trai Fuller','Tevita Naufahu'],
        home_ins=['Reuben Cotter','Soni Luke','Viliami Vailea'],
        home_outs=[],
        away_ins=['Hamiso Tabuai-Fidow','Herbie Farnworth','Kodi Nikorima','Max Plath','Selwyn Cobbo','Thomas Flegler'],
        away_outs=['Brian Pouniu','John Fineanganofo','Lewis Symonds'],
        home_note="Skipper Reuben Cotter is back after being rested from the Raiders game and hooker Soni Luke (knee) is also good to go. Prop Tom Mikaele has been named despite leaving the field with a knee injury in Canberra.",
        away_note="Huge ins for the Phins as centre Herbie Farnworth and five-eighth Kodi Nikorima return from hamstring injuries while fullback Hamiso Tabuai-Fidow, hooker Max Plath and winger Selwyn Cobbo are back from Origin duty. Felise Kaufusi and Brad Schneider go back to the bench.",
    ),
    'broncos-vs-titans': dict(
        home_players=['Reece Walsh','Josiah Karapani','Kotoni Staggs','Grant Anderson','Jesse Arthars','Thomas Duffy','Adam Reynolds','Preston Riki','Cory Paix','Payne Haas','Brendan Piakura','Jack Gosiewski','Xavier Willison','Ben Hunt','Ben Talty',"Va’a Semu",'Aublix Tawha','Ezra Mam','Hayze Perham','Jaiyden Hunt','Phillip Coates','Josh Rogers'],
        away_players=['Keano Kini','Jensen Taumoepeau','Jojo Fifita','AJ Brimson','Phillip Sami','Jayden Campbell','Zane Harrison','Moeaki Fotuaika','Oliver Pascoe',"Tino Fa’asuamaleaui",'Arama Hau','Beau Fermor','Cooper Bai','Kurtis Morrin','Josh Patston','Chris Randall','Klese Haas','Jaylan De Groot','Luke Sommerton','Tony Francis','Bodhi Sharpley','Lachlan Ilias'],
        home_ins=['Aublix Tawha','Hayze Perham','Jaiyden Hunt','Josh Rogers','Phillip Coates'],
        home_outs=['Gehamat Shibasaki','Patrick Carrigan'],
        away_ins=['Bodhi Sharpley','Jojo Fifita',"Tino Fa’asuamaleaui",'Tony Francis'],
        away_outs=['Adam Christensen'],
        home_note="Grant Anderson comes into the centres with Gehamat Shibasaki nursing a knee injury while the loss of Pat Carrigan (ankle) sees Xavier Willison move to lock and Jack Gosiewski start in the second row. Thomas Duffy has been promoted to start at five-eighth with Ezra Mam relegated to the bench. Aublix Tawha and Hayze Perham have been added to the interchange.",
        away_note="The return of skipper Tino Fa'asuamaleaui and Jojo Fifita from Maroons duty sees prop Klese Haas and centre Jaylan De Groot slide to the interchange. Hooker Oliver Pascoe suffered a concussion against Manly in Round 12 and is right to play after going through the protocols. Lachlan Ilias and Adam Christensen drop out of the squad.",
    ),
    'wests-tigers-vs-panthers': dict(
        home_players=['Jahream Bula','Jeral Skelton','Sunia Turuva','Heamasi Makasini','Faaletino Tavana','Jarome Luai','Jock Madden','Terrell May','Apisai Koroisau','Fonua Pole','Mavrik Geyer','Kai Pearce-Paul','Charlie Murray','Latu Fainu','Alex Seyfarth','Royce Hunt','Ethan Roberts','Bunty Afoa',"Starford To’a",'Tristan Hope','Heath Mason','Javon Andrews'],
        away_players=['Dylan Edwards','Thomas Jenkins','Paul Alamoti','Casey McLean',"Brian To’o",'Blaize Talagi','Nathan Cleary','Moses Leota','Freddy Lussick','Lindsay Smith',"Isaiah Papali’i",'Liam Martin','Isaah Yeo','Jack Cogger','Scott Sorensen','Liam Henry','Izack Tago','Luke Garner','Jack Cole','Billy Phillips','Billy Scott','Luron Patea'],
        home_ins=['Bunty Afoa','Ethan Roberts','Heath Mason','Javon Andrews','Tristan Hope'],
        home_outs=['Alex Twal','Sione Fainu'],
        away_ins=["Brian To’o",'Isaah Yeo','Nathan Cleary'],
        away_outs=[],
        home_note="Mavrik Geyer will make his second appearance of the season as he comes in for Sione Fainu (concussion). Lock Charlie Murray gets his first NRL game of 2026 and sixth of his career as he replaces Alex Twal (knee). Young gun Ethan Roberts and Bunty Afoa are the new faces on the six-man bench. Centre Heamasi Makasini has been named to play despite failing to finish last week's game due to a shoulder injury.",
        away_note="Big guns Nathan Cleary, Isaah Yeo and Brian To'o are back on deck after being rested last week. Jack Cogger, Liam Henry and Izack Tago revert to the bench while Paul Alamoti shifts to centre to accommodate the return of To'o. Utility Jack Cole has been added to the six-man bench while Billy Phillips, Luron Patea and Billy Scott drop to the reserves.",
    ),
    'sharks-vs-dragons': dict(
        home_players=['William Kennedy','Samuel Stonestreet','Jesse Ramien','Mawene Hiroti','Ronaldo Mulitalo','Braydon Trindall','Niwhai Puru','Addin Fonua-Blake','Jayden Berrell','Toby Rudolf','Briton Nikora','Teig Wilton','Cameron McInnes','Siosifa Talakai','Billy Burns','Jesse Colquhoun','Thomas Hazelton','Hohepa Puru','Oregon Kaufusi','Riley Jones','KL Iro','Sione Katoa'],
        away_players=['Clinton Gutherson','Setu Tu','Moses Suli','Valentine Holmes','Mathew Feagai','Daniel Atkinson','Kyle Flanagan','Loko Jnr Pasifiki Tonga','Damien Cook','Toby Couchman','Dylan Egan','Hamish Stewart','Ryan Couchman','Jacob Liddle','Josh Kerr','Luciano Leilua','Blake Lawrie','Lyhkan King-Togia','Emre Guler','Tyrell Sloan',"Jaydn Su’A",'Nathan Lawson'],
        home_ins=['Briton Nikora','KL Iro','Oregon Kaufusi','Sione Katoa'],
        home_outs=['Blayke Brailey'],
        away_ins=['Jacob Liddle',"Jaydn Su’A",'Nathan Lawson'],
        away_outs=[],
        home_note="Maroons star Briton Nikora is back after being rested last week but Nicho Hynes (calf) and Blayke Brailey (arm) are missing. Billy Burns moves to the bench and Jayden Berrell gets the nod at hooker. A couple of big names listed in the reserves with KL Iro (knee laceration) and Sione Katoa (ankle) nearing their return from injury.",
        away_note="Hooker Jacob Liddle is back from a hamstring injury while damaging edge forward Jaydn Su'A is listed among the reserves as he looks to return from a calf injury. Tyrell Sloan drops back to the reserves after an eight-minute cameo off the bench last week.",
    ),
    'bulldogs-vs-eels': dict(
        home_players=['Jacob Kiraz','Jethro Rinakama','Bronson Xerri','Stephen Crichton','Enari Tuala','Matt Burton','Lachlan Galvin','Max King','Kurt Mann','Leo Thompson','Sitili Tupouniua','Jaeman Salmon','Harry Hayes','Bailey Hayward','Jed Reardon','Jack Underhill','Josh Curran',"Sean O’Sullivan",'Logan Spinks','Lipoi Hopoi','Connor Tracey','Marcelo Montoya'],
        away_players=['Isaiah Iongi','Brian Kelly','Jordan Samrani','Sean Russell','Josh Addo-Carr','Joash Papalii','Ronald Volkman','Luca Moretti','Tallyn Da Silva','Jack Williams','Kelma Tuilagi','Kitione Kautoga','Jack De Belin','Dylan Walker','Sam Tuivaiti','Toni Mataele','Harrison Edwards','Apa Twidle','Teancum Brown','Charlie Guymer','Ryley Smith','Araz Nanva'],
        home_ins=['Connor Tracey','Logan Spinks','Marcelo Montoya',"Sean O’Sullivan"],
        home_outs=['Jonathan Sua'],
        away_ins=['Araz Nanva','Ryley Smith','Teancum Brown'],
        away_outs=[],
        home_note="Coach Cameron Ciraldo sticks solid after the loss to Wests Tigers with the only changes coming on the interchange where Sean O'Sullivan and Logan Spinks have been added in place of Lipoi Hopoi and Jonathan Sua. Listed among the reserves are Connor Tracey (hamstring) and Marcelo Montoya (knee) as they work their way back from injury.",
        away_note="Tallyn Da Silva has again been named to start at hooker with Harrison Edwards on the bench but they could swap on game day as they did against the Knights. After returning from a sternum injury in NSW Cup last weekend, hooker Ryley Smith is listed among the reserves. Teancum Brown has been added to the six-man bench in place of Charlie Guymer.",
    ),
}

# ── CSS ─────────────────────────────────────────────────────────────────────
CSS = """:root{--bg:hsl(205 60% 96%);--fg:hsl(215 45% 16%);--primary:hsl(48 92% 64%);--pfg:hsl(215 45% 16%);--muted:hsl(205 40% 92%);--muted-fg:hsl(215 20% 42%);--accent:hsl(200 88% 58%);--border:hsl(205 40% 86%);--gg:linear-gradient(135deg,hsl(50 96% 72%),hsl(44 92% 60%));--sg:0 10px 40px -10px hsl(48 92% 54%/.4);--sc:0 4px 24px -8px hsl(215 50% 30%/.1);--ch:36px;--nh:80px;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--fg);font-family:"Inter Tight",sans-serif;line-height:1.65;font-size:15px;}
h1,h2,h3{font-family:"Geist",sans-serif;letter-spacing:-0.03em;}
a{color:inherit;}img{max-width:100%;}
.cb{position:fixed;top:0;left:0;right:0;height:var(--ch);background:hsl(215 45% 16%);color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 24px;font-size:11px;z-index:200;gap:12px;}
.cb-t{font-weight:700;color:var(--primary);}.cb-h{color:hsl(205 40% 70%);}.cb-h a{color:var(--accent);text-decoration:none;}
.cb-b{display:flex;gap:6px;}.cb-b span{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);border-radius:4px;padding:2px 6px;font-size:10px;font-weight:700;}
.nav{position:fixed;top:var(--ch);left:0;right:0;height:var(--nh);background:hsl(205 60% 96%/.9);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;padding:0 40px;z-index:100;}
.nav-logo img{height:72px;width:auto;}.nav-links{display:flex;gap:20px;list-style:none;}
.nav-links a{font-size:13px;font-weight:500;color:hsl(215 45% 16%/.7);text-decoration:none;transition:color .2s;}.nav-links a:hover{color:var(--primary);}
.btn-g{display:inline-flex;align-items:center;background:var(--gg);color:var(--pfg);font-size:13px;font-weight:700;padding:9px 18px;border-radius:10px;border:none;cursor:pointer;text-decoration:none;box-shadow:var(--sg);white-space:nowrap;}
.pb{padding-top:calc(var(--ch) + var(--nh));}
.hero{padding:44px 32px 36px;background:radial-gradient(ellipse at top,hsl(200 85% 88%),hsl(205 70% 96%) 70%);border-bottom:1px solid var(--border);}
.hero-in{max-width:1100px;margin:0 auto;}.bc{font-size:12px;color:var(--muted-fg);margin-bottom:10px;}.bc a{color:var(--muted-fg);text-decoration:none;}
.eye{display:flex;align-items:center;gap:10px;margin-bottom:12px;}.eye-l{height:1px;width:32px;background:var(--primary);}
.eye-t{font-family:"JetBrains Mono",monospace;font-size:11px;color:var(--primary);text-transform:uppercase;letter-spacing:.2em;}
.wrap{max-width:1100px;margin:0 auto;padding:44px 32px 80px;}
.upd{font-size:11px;color:var(--muted-fg);font-family:"JetBrains Mono",monospace;margin-top:8px;}
.section{background:#fff;border:1px solid var(--border);border-radius:14px;padding:24px 28px;margin:24px 0;box-shadow:var(--sc);}
.section h2{font-size:20px;font-weight:700;margin-bottom:14px;padding-bottom:10px;border-bottom:1px solid var(--border);}
.match-hero{display:flex;align-items:center;justify-content:center;gap:20px;padding:28px;background:hsl(215 45% 16%);border-radius:14px;margin:24px 0;color:#fff;text-align:center;}
.team-block{flex:1;}.team-name{font-size:22px;font-weight:800;font-family:"Geist",sans-serif;letter-spacing:-0.03em;}
.team-short{font-size:11px;color:rgba(255,255,255,.6);margin-top:4px;font-family:"JetBrains Mono",monospace;}
.vs-block{font-size:28px;font-weight:800;color:var(--primary);font-family:"Geist",sans-serif;}
.odds-row{display:flex;gap:10px;flex-wrap:wrap;margin:12px 0;}
.odds-card{flex:1;min-width:120px;background:var(--muted);border-radius:10px;padding:14px;text-align:center;}
.odds-label{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:6px;}
.odds-val{font-size:22px;font-weight:800;font-family:"JetBrains Mono",monospace;color:var(--fg);}
.odds-sub{font-size:11px;color:var(--muted-fg);margin-top:4px;font-family:"JetBrains Mono",monospace;}
.match-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:14px;margin:16px 0;}
.match-card{background:#fff;border:1px solid var(--border);border-radius:12px;padding:16px 18px;transition:box-shadow .2s;}
.match-card:hover{box-shadow:var(--sc);}
.mc-teams{font-size:15px;font-weight:800;font-family:"Geist",sans-serif;margin-bottom:6px;letter-spacing:-0.01em;}
.mc-teams a{text-decoration:none;color:var(--fg);}.mc-teams a:hover{color:var(--accent);}
.mc-meta{font-size:12px;color:var(--muted-fg);line-height:1.55;}
.mc-odds{font-size:12px;color:var(--muted-fg);margin-top:6px;font-family:"JetBrains Mono",monospace;}
.mc-tip{font-size:13px;font-weight:700;color:hsl(140 55% 22%);background:hsl(140 40% 96%);border:1px solid hsl(140 35% 80%);border-radius:8px;padding:8px 12px;margin-top:10px;line-height:1.55;}
.mc-tip-line{display:block;}.mc-tip-line + .mc-tip-line{margin-top:3px;font-weight:600;color:hsl(215 45% 16%);}
.mc-tip-star{color:hsl(48 95% 50%);}
.mc-badge{display:inline-block;background:hsl(215 45% 16%);color:var(--primary);font-size:10px;font-weight:700;padding:4px 10px;border-radius:5px;font-family:"JetBrains Mono",monospace;margin-top:10px;text-decoration:none;}
.mc-badge:hover{background:hsl(215 50% 22%);}
.int-links{background:#fff;border:1px solid var(--border);border-radius:12px;padding:18px 22px;margin:28px 0;}
.int-links h3{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--muted-fg);margin-bottom:12px;}
.int-links a{display:inline-block;background:var(--muted);border-radius:6px;padding:5px 11px;margin:3px;font-size:13px;font-weight:500;text-decoration:none;color:var(--fg);}
.faq{margin:44px 0;}.faq h2{font-size:22px;font-weight:700;margin-bottom:20px;}
.faq-item{border:1px solid var(--border);border-radius:10px;margin-bottom:8px;overflow:hidden;}
.faq-q{width:100%;text-align:left;background:#fff;border:none;padding:14px 18px;font-size:14px;font-weight:600;cursor:pointer;display:flex;justify-content:space-between;align-items:center;font-family:"Inter Tight",sans-serif;color:var(--fg);}
.fi{font-size:18px;color:var(--muted-fg);}.faq-a{padding:0 18px 14px;font-size:14px;line-height:1.75;color:hsl(215 45% 16%/.8);display:none;}.faq-a.open{display:block;}
.site-footer{background:hsl(215 45% 16%);color:rgba(255,255,255,.7);padding:44px 32px 28px;margin-top:72px;}
.footer-in{max-width:1100px;margin:0 auto;}.footer-logo{height:44px;width:auto;margin-bottom:14px;filter:brightness(0) invert(1);opacity:.75;}
.footer-desc{font-size:13px;line-height:1.7;max-width:400px;margin-bottom:28px;}
.footer-links{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:28px;}.footer-links a{font-size:13px;color:rgba(255,255,255,.55);text-decoration:none;}
.footer-rg{font-size:11px;color:rgba(255,255,255,.4);border-top:1px solid rgba(255,255,255,.1);padding-top:20px;line-height:1.8;}.footer-rg a{color:rgba(255,255,255,.4);}
.wrap-rails{max-width:1480px;margin:0 auto;display:grid;grid-template-columns:240px minmax(0,1100px) 240px;gap:28px;padding:0 16px;align-items:start;}
.wrap-rails .wrap{padding:44px 0 80px;max-width:none;margin:0;}
.rail{position:sticky;top:128px;padding-top:44px;}
.betr-vert-wrap{background:#fff;border:1px solid var(--border);border-radius:14px;padding:14px;box-shadow:var(--sc);text-align:center;overflow:hidden;}
.betr-vert-label{font-family:"JetBrains Mono",monospace;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--muted-fg);margin-bottom:10px;}
.rail-card{background:#fff;border:1px solid var(--border);border-radius:14px;padding:16px 14px;box-shadow:var(--sc);}
.rail-card-title{font-size:13px;font-weight:800;font-family:"Geist",sans-serif;margin-bottom:12px;padding-bottom:10px;border-bottom:2px solid hsl(215 45% 16%);}
.rail-bookies .bm-row{padding:9px 10px;gap:9px;margin-bottom:7px;flex-wrap:wrap;box-shadow:none;}
.rail-bookies .bm-row:last-child{margin-bottom:0;}
.rail-bookies .bm-logo{width:34px;height:34px;padding:4px;}
.rail-bookies .bm-info{flex:1;min-width:0;}
.rail-bookies .bm-title{font-size:12px;line-height:1.2;}
.rail-bookies .bm-desc{display:none;}
.rail-bookies .btn-claim{padding:7px 12px;font-size:11px;width:100%;text-align:center;justify-content:center;margin-top:4px;flex-basis:100%;border-radius:8px;box-shadow:none;}
.rail-foot{margin-top:10px;padding-top:10px;border-top:1px solid var(--border);font-size:11px;text-align:center;}
.rail-foot a{color:var(--accent);text-decoration:none;font-weight:600;}
.bm-row{display:flex;align-items:center;gap:14px;padding:14px 16px;background:#fff;border:1px solid var(--border);border-radius:12px;margin-bottom:10px;box-shadow:0 1px 3px hsl(215 50% 30% / .06);}
.bm-logo{width:54px;height:54px;border-radius:10px;object-fit:contain;background:#fff;border:1px solid var(--border);padding:6px;flex-shrink:0;}
.bm-info{flex:1;min-width:0;}
.bm-title{font-size:15px;font-weight:800;font-family:"Geist",sans-serif;margin-bottom:3px;color:var(--fg);line-height:1.25;}
.bm-desc{font-size:13px;color:var(--muted-fg);line-height:1.45;}
.btn-claim{display:inline-flex;align-items:center;justify-content:center;background:hsl(150 42% 38%);color:#fff;font-weight:700;font-size:14px;padding:11px 24px;border-radius:999px;text-decoration:none;white-space:nowrap;box-shadow:0 4px 12px -4px hsl(150 50% 30% / .35);font-family:"Geist",sans-serif;}
.btn-claim:hover{background:hsl(150 42% 32%);}
.tip-pick-block{background:linear-gradient(135deg,hsl(140 50% 36%),hsl(140 60% 26%));color:#fff;border-radius:14px;padding:24px;margin:16px 0;box-shadow:0 8px 24px -8px hsl(140 50% 25% / .35);}
.tip-pick-label{font-family:"JetBrains Mono",monospace;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.15em;color:hsl(48 95% 70%);margin-bottom:8px;}
.tip-pick-content{font-size:22px;font-weight:800;font-family:"Geist",sans-serif;letter-spacing:-0.02em;line-height:1.2;}
.tip-pick-sub{font-size:14px;color:rgba(255,255,255,.85);margin-top:10px;}
.tip-pick-ctas{display:flex;gap:10px;flex-wrap:wrap;margin-top:16px;}
.tip-pick-cta{display:inline-flex;align-items:center;background:hsl(48 95% 65%);color:hsl(140 55% 18%);font-weight:800;font-size:13px;padding:11px 20px;border-radius:8px;text-decoration:none;font-family:"Geist",sans-serif;}
.tip-pick-cta-outline{display:inline-flex;align-items:center;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.3);color:#fff;font-weight:700;font-size:13px;padding:11px 20px;border-radius:8px;text-decoration:none;}
.team-lists{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:16px 0;}
.team-list{background:var(--muted);border-radius:12px;padding:16px 18px;}
.tl-name{font-family:"Geist",sans-serif;font-size:17px;font-weight:800;letter-spacing:-0.02em;margin-bottom:10px;padding-bottom:10px;border-bottom:2px solid var(--accent);}
.tl-section-h{font-family:"JetBrains Mono",monospace;font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:var(--muted-fg);margin-top:14px;margin-bottom:6px;font-weight:700;}
.tl-players{list-style:none;padding:0;margin:0;}
.tl-players li{display:flex;gap:8px;padding:5px 0;font-size:13px;border-bottom:1px solid var(--border);align-items:baseline;}
.tl-players li:last-child{border-bottom:none;}
.tl-num{font-family:"JetBrains Mono",monospace;font-size:11px;color:var(--accent);font-weight:700;width:20px;flex-shrink:0;}
.tl-pos{font-family:"JetBrains Mono",monospace;font-size:10px;color:var(--muted-fg);text-transform:uppercase;width:34px;flex-shrink:0;}
.tl-name-cell{font-weight:500;flex:1;}
.tl-reserves{font-size:12px;color:var(--muted-fg);line-height:1.7;}
.tl-news{background:hsl(48 80% 96%);border-left:3px solid hsl(48 90% 55%);padding:14px 16px;margin-top:18px;border-radius:6px;font-size:13px;line-height:1.65;}
.tl-news-label{font-family:"JetBrains Mono",monospace;font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:hsl(40 70% 30%);font-weight:700;margin-bottom:8px;}
.tl-news p{margin-bottom:8px;}.tl-news p:last-child{margin-bottom:0;}
.tl-news strong{color:hsl(215 45% 16%);}
.tl-inout-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:14px;font-size:12px;}
.tl-inout-cell{background:#fff;border:1px solid var(--border);border-radius:8px;padding:10px 12px;}
.tl-inout-label{font-family:"JetBrains Mono",monospace;font-size:9px;text-transform:uppercase;letter-spacing:.1em;color:var(--muted-fg);font-weight:700;margin-bottom:4px;}
.tl-inout-list{line-height:1.6;color:var(--fg);}
@media(max-width:1200px){.wrap-rails{display:block;padding:0;}.wrap-rails .wrap{max-width:1100px;padding:44px 32px 80px;margin:0 auto;}.rail{display:none;}}
@media(max-width:768px){.nav-links{display:none;}.wrap,.hero{padding-left:16px;padding-right:16px;}.nav{padding:0 20px;}.match-hero{flex-direction:column;gap:12px;}.team-name{font-size:18px;}.team-lists{grid-template-columns:1fr;}.tl-inout-grid{grid-template-columns:1fr;}}"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800&family=Inter+Tight:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">'

GTAG = """<script async src="https://www.googletagmanager.com/gtag/js?id=G-X8HMP35PY6"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-X8HMP35PY6');</script>"""

CB = '<div class="cb"><span class="cb-t">Bet Responsibly</span><span class="cb-h">Gambling Help: <a href="tel:1800858858">1800 858 858</a> &middot; <a href="https://www.gamblinghelponline.org.au" target="_blank">gamblinghelponline.org.au</a></span><div class="cb-b"><span>18+</span><span>AUS ONLY</span></div></div>'

NAV = '<nav class="nav"><a href="/index.html" class="nav-logo"><img src="/puntguide-logo.png" alt="PuntGuide"></a><ul class="nav-links"><li><a href="/nrl-tips.html">NRL Tips</a></li><li><a href="/nrl-ladder-2026.html">NRL Ladder</a></li><li><a href="/best-betting-sites-for-nrl.html">Best for NRL</a></li><li><a href="/all-betting-sites.html">All Sites</a></li></ul><a href="/go/?to=betr" target="_blank" rel="noopener" class="btn-g">Bet at Betr &rarr;</a></nav>'

ICONS = '<link rel="icon" type="image/png" sizes="32x32" href="/pg-icon.png"><link rel="icon" type="image/png" sizes="192x192" href="/pg-icon-192.png"><link rel="apple-touch-icon" sizes="192x192" href="/pg-icon-192.png"><meta name="viewport" content="width=device-width,initial-scale=1.0">'

RAIL_LEFT = """<aside class="rail rail-left">
  <div class="betr-vert-wrap">
    <div class="betr-vert-label">Advertisement</div>
    <script type="text/javascript" src="https://js.betraffiliates.com.au/javascript.php?prefix=zJS8NRxe1pAWqcfzuvZcQGNd7ZgqdRLk&amp;media=7&amp;campaign=1"></script>
  </div>
</aside>"""

RAIL_RIGHT = """<aside class="rail rail-right">
  <div class="rail-card">
    <div class="rail-card-title">Best Bookmakers</div>
    <div class="rail-bookies">
      <div class="bm-row"><img src="/betr.png" alt="betr" class="bm-logo"><div class="bm-info"><div class="bm-title">Best NRL Pricing</div></div><a href="/go/?to=betr" class="btn-claim" target="_blank" rel="noopener">Claim</a></div>
      <div class="bm-row"><img src="/sportsbet.png" alt="Sportsbet" class="bm-logo"><div class="bm-info"><div class="bm-title">Widest NRL Markets</div></div><a href="/go/?to=sportsbet" class="btn-claim" target="_blank" rel="noopener">Claim</a></div>
      <div class="bm-row"><img src="/pointsbet.png" alt="PointsBet" class="bm-logo"><div class="bm-info"><div class="bm-title">PointsBetting</div></div><a href="/go/?to=pointsbet" class="btn-claim" target="_blank" rel="noopener">Claim</a></div>
      <div class="bm-row"><img src="/ladbrokes.png" alt="Ladbrokes" class="bm-logo"><div class="bm-info"><div class="bm-title">Sharp NRL Lines</div></div><a href="/go/?to=ladbrokes" class="btn-claim" target="_blank" rel="noopener">Claim</a></div>
      <div class="bm-row"><img src="/neds.png" alt="Neds" class="bm-logo"><div class="bm-info"><div class="bm-title">Best Promos</div></div><a href="/go/?to=neds" class="btn-claim" target="_blank" rel="noopener">Claim</a></div>
      <div class="bm-row"><img src="/picklebet.png" alt="Picklebet" class="bm-logo"><div class="bm-info"><div class="bm-title">SGM Builder</div></div><a href="/go/?to=picklebet" class="btn-claim" target="_blank" rel="noopener">Claim</a></div>
    </div>
    <p class="rail-foot"><a href="/all-betting-sites.html">All 130+ bookmakers &rarr;</a></p>
  </div>
</aside>"""

BOOKIES_BLOCK = """<div class="bm-row">
  <img src="/betr.png" alt="betr" class="bm-logo">
  <div class="bm-info">
    <div class="bm-title">Best NRL Pricing</div>
    <div class="bm-desc">Sharpest H2H + line markets and the deepest tryscorer and SGM book</div>
  </div>
  <a href="/go/?to=betr" target="_blank" rel="noopener" class="btn-claim">Claim</a>
</div>
<div class="bm-row">
  <img src="/sportsbet.png" alt="Sportsbet" class="bm-logo">
  <div class="bm-info">
    <div class="bm-title">Widest NRL Markets</div>
    <div class="bm-desc">Most markets per game in Australia &mdash; build a Round 14 multi in one tap</div>
  </div>
  <a href="/go/?to=sportsbet" target="_blank" rel="noopener" class="btn-claim">Claim</a>
</div>
<div class="bm-row">
  <img src="/pointsbet.png" alt="PointsBet" class="bm-logo">
  <div class="bm-info">
    <div class="bm-title">PointsBetting on Player Stats</div>
    <div class="bm-desc">Unique PointsBetting markets on run metres, tackles and tries scored</div>
  </div>
  <a href="/go/?to=pointsbet" target="_blank" rel="noopener" class="btn-claim">Claim</a>
</div>
<div class="bm-row">
  <img src="/ladbrokes.png" alt="Ladbrokes" class="bm-logo">
  <div class="bm-info">
    <div class="bm-title">Sharp NRL Lines</div>
    <div class="bm-desc">Consistently competitive on H2H and line markets every weekend</div>
  </div>
  <a href="/go/?to=ladbrokes" target="_blank" rel="noopener" class="btn-claim">Claim</a>
</div>
<div class="bm-row">
  <img src="/neds.png" alt="Neds" class="bm-logo">
  <div class="bm-info">
    <div class="bm-title">Best Promos &amp; Boosts</div>
    <div class="bm-desc">Frequent NRL multi boosts and same-game multi specials throughout the round</div>
  </div>
  <a href="/go/?to=neds" target="_blank" rel="noopener" class="btn-claim">Claim</a>
</div>
<div class="bm-row">
  <img src="/picklebet.png" alt="Picklebet" class="bm-logo">
  <div class="bm-info">
    <div class="bm-title">SGM &amp; Multi Builder</div>
    <div class="bm-desc">Best same-game multi builder &mdash; mix Best Bet + tryscorer in one bet</div>
  </div>
  <a href="/go/?to=picklebet" target="_blank" rel="noopener" class="btn-claim">Claim</a>
</div>"""

FOOTER = """<footer class="site-footer"><div class="footer-in">
<img src="/puntguide-logo.png" alt="PuntGuide" class="footer-logo">
<p class="footer-desc">{desc}</p>
<div class="footer-links"><a href="/nrl-tips.html">NRL Tips 2026</a>
  <a href="/nrl-ladder-2026.html">NRL Ladder</a>
  <a href="/best-betting-sites-for-nrl.html">Best Sites for NRL</a>
  <a href="/all-betting-sites.html">All 130+ Bookmakers</a></div>
<div class="footer-rg">Gamble responsibly. Call <a href="tel:1800858858">Gambling Help 1800 858 858</a> or visit <a href="https://www.gamblinghelponline.org.au" target="_blank">gamblinghelponline.org.au</a>. 18+ only.</div>
</div></footer>"""

SCRIPTS_TAIL = '<script>document.querySelectorAll(".faq-q").forEach(b=>b.addEventListener("click",function(){const a=this.nextElementSibling;a.classList.toggle("open");this.querySelector(".fi").textContent=a.classList.contains("open")?"−":"+";}));</script><script src="/nav-drawer.js"></script><script src="/js/tracking.js"></script>'


# ── Helpers ──────────────────────────────────────────────────────────────────

def team_list_html(team_name, players):
    starting = ''.join(
        f'<li><span class="tl-num">{i+1}</span><span class="tl-pos">{POSITIONS[i]}</span><span class="tl-name-cell">{players[i]}</span></li>'
        for i in range(13)
    )
    bench = ''.join(
        f'<li><span class="tl-num">{i+1}</span><span class="tl-pos">INT</span><span class="tl-name-cell">{players[i]}</span></li>'
        for i in range(13, min(19, len(players)))
    )
    reserves = ' &middot; '.join(f'{i+1}. {players[i]}' for i in range(19, min(22, len(players))))
    return f'''<div class="team-list">
  <h3 class="tl-name">{team_name}</h3>
  <div class="tl-section-h">Starting XIII</div>
  <ul class="tl-players">{starting}</ul>
  <div class="tl-section-h">Interchange (14&ndash;19)</div>
  <ul class="tl-players">{bench}</ul>
  <div class="tl-section-h">Reserves</div>
  <p class="tl-reserves">{reserves}</p>
</div>'''


def team_section(m, t):
    home_list = team_list_html(m['home_full'], t['home_players'])
    away_list = team_list_html(m['away_full'], t['away_players'])
    fmt_list  = lambda xs: ', '.join(xs) if xs else '&mdash;'
    return f'''<div class="section">
  <h2>Team Lists  -  Round 14</h2>
  <p style="font-size:13px;color:var(--muted-fg);margin-bottom:14px">Confirmed by NRL.com on Tuesday 2 June 2026. Two players will be omitted 24 hours out and the final 19 confirmed 90 minutes before kickoff.</p>
  <div class="team-lists">{home_list}{away_list}</div>
  <div class="tl-inout-grid">
    <div class="tl-inout-cell"><div class="tl-inout-label">{m['home_nick']} Ins</div><div class="tl-inout-list">{fmt_list(t['home_ins'])}</div></div>
    <div class="tl-inout-cell"><div class="tl-inout-label">{m['home_nick']} Outs</div><div class="tl-inout-list">{fmt_list(t['home_outs'])}</div></div>
    <div class="tl-inout-cell"><div class="tl-inout-label">{m['away_nick']} Ins</div><div class="tl-inout-list">{fmt_list(t['away_ins'])}</div></div>
    <div class="tl-inout-cell"><div class="tl-inout-label">{m['away_nick']} Outs</div><div class="tl-inout-list">{fmt_list(t['away_outs'])}</div></div>
  </div>
  <div class="tl-news">
    <div class="tl-news-label">Team News</div>
    <p><strong>{m['home_nick']}:</strong> {t['home_note']}</p>
    <p><strong>{m['away_nick']}:</strong> {t['away_note']}</p>
  </div>
</div>'''


def analysis_section(m, p):
    return f'''<div class="section">
  <h2>Match Analysis &amp; Best Bet</h2>
  <p style="font-size:14px;line-height:1.85;margin-bottom:14px">{p['analysis']}</p>
  <div class="tip-pick-block">
    <div class="tip-pick-label">&#11088; PuntGuide Best Bet  -  {p['tip_type']}</div>
    <div class="tip-pick-content">{p['tip_label']} (${p['tip_odds']})</div>
    <div class="tip-pick-sub">Anytime Tryscorer: <strong>{p['tryscorer']}</strong></div>
    <div class="tip-pick-ctas">
      <a href="/go/?to=betr" target="_blank" rel="noopener" class="tip-pick-cta">Bet at Betr &rarr;</a>
      <a href="/all-betting-sites.html" class="tip-pick-cta-outline">Compare 130+ Bookmakers</a>
    </div>
  </div>
</div>'''


# ── Per-match page ──────────────────────────────────────────────────────────

def build_match_page(m):
    slug      = f"nrl-{m['home_slug']}-vs-{m['away_slug']}-round-14-2026"
    key       = f"{m['home_slug']}-vs-{m['away_slug']}"
    canonical = f"{SITE}/{slug}"
    title     = f"{m['home_full']} vs {m['away_full']} Tips &amp; Best Bet  -  NRL Round 14 2026 | PuntGuide"
    desc      = f"PuntGuide Best Bet for {m['home_full']} vs {m['away_full']} (NRL Round 14 2026). Team lists, analysis, Sportsbet odds and tryscorer pick. {m['date_str']} at {m['venue']}."
    p         = PICKS[key]
    t         = TEAMS[key]

    sports_event = {
        "@context": "https://schema.org",
        "@type": "SportsEvent",
        "name": f"{m['home_full']} vs {m['away_full']}",
        "startDate": m['iso_start'],
        "endDate": m['iso_end'],
        "eventStatus": "https://schema.org/EventScheduled",
        "location": {"@type": "Place", "name": m['venue'], "address": {"@type": "PostalAddress", "addressCountry": "AU"}},
        "sport": "Rugby League",
        "competitor": [
            {"@type": "SportsTeam", "name": m['home_full']},
            {"@type": "SportsTeam", "name": m['away_full']},
        ],
        "organizer": {"@type": "Organization", "name": "NRL"},
        "description": desc,
        "image": f"{SITE}/puntguide-logo.png",
    }

    faqs = [
        (f"Who will win {m['home_nick']} vs {m['away_nick']}?",
         f"PuntGuide's Best Bet for {m['home_full']} vs {m['away_full']} is {p['tip_label']} at ${p['tip_odds']}, with {p['tryscorer']} as the anytime tryscorer pick. Full analysis above."),
        (f"When and where is {m['home_nick']} vs {m['away_nick']} Round 14 2026?",
         f"{m['home_full']} vs {m['away_full']} kicks off at {m['time_str']} AEST on {m['date_str']} at {m['venue']}."),
        ("Where can I bet on this match?",
         f"PuntGuide recommends Betr for {m['home_full']} vs {m['away_full']} &mdash; sharpest line markets and the deepest tryscorer book. Sportsbet, PointsBet, Ladbrokes, Neds and Picklebet are also live. See the full comparison of 130+ Australian bookmakers."),
        ("What is the recommended pick?",
         f"PuntGuide's Round 14 Best Bet for this match is {p['tip_label']} at ${p['tip_odds']}, paired with {p['tryscorer']} to score a try at anytime. Always shop the market for best price before placing &mdash; 18+ only."),
    ]
    faq_schema_obj = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
    faq_items = ''.join(f'<div class="faq-item"><button class="faq-q">{q} <span class="fi">+</span></button><div class="faq-a">{a}</div></div>' for q, a in faqs)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
{GTAG}
<meta charset="UTF-8">
{ICONS}
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{m['home_full']} vs {m['away_full']}  -  NRL Round 14 2026 | PuntGuide">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="article">
<meta name="robots" content="index, follow">
{FONTS}
<script type="application/ld+json">{json.dumps(sports_event, separators=(',', ':'))}</script>
<script type="application/ld+json">{json.dumps(faq_schema_obj, separators=(',', ':'))}</script>
<style>{CSS}</style>
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@puntguide">
<meta name="twitter:title" content="{m['home_full']} vs {m['away_full']}  -  NRL Round 14 2026 | PuntGuide">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/puntguide-logo.png">
</head>
<body>
{CB}
{NAV}
<div class="pb">
<div class="hero"><div class="hero-in">
  <div class="bc"><a href="/index.html">Home</a> &rsaquo; <a href="/nrl-tips.html">NRL 2026</a> &rsaquo; <a href="/nrl-round-14-tips-2026.html">Round 14 Tips</a> &rsaquo; {m['home_nick']} vs {m['away_nick']}</div>
  <div class="eye"><span class="eye-l"></span><span class="eye-t">NRL Round 14 &middot; {m['date_str']}</span></div>
  <h1>{m['home_full']} vs {m['away_full']} Tips</h1>
  <div style="background:hsl(215 45% 16%);border-radius:10px;padding:16px 20px;margin:20px 0;">
    <div style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:hsl(48 92% 64%);margin-bottom:8px;font-family:'JetBrains Mono',monospace;">Short Answer</div>
    <p style="font-size:15px;line-height:1.75;color:rgba(255,255,255,.9);margin:0;">PuntGuide&rsquo;s Best Bet: <strong style="color:#fff;">{p['tip_label']} (${p['tip_odds']})</strong>. Anytime Tryscorer: <strong style="color:#fff;">{p['tryscorer']}</strong>. {m['home_full']} host {m['away_full']} at {m['venue']} on {m['date_str']} &mdash; full analysis, team lists and odds comparison below.</p>
  </div>
  <p style="font-size:16px;color:hsl(215 45% 16%/.65);max-width:700px;line-height:1.8;margin-top:10px">NRL Round 14 2026  -  {m['home_full']} host {m['away_full']} at {m['venue']}. PuntGuide Best Bet, tryscorer pick, full match analysis and Sportsbet odds comparison.</p>
  <p class="upd">{m['time_str']} &middot; {m['date_str']} &middot; {m['venue']}</p>
</div></div>

<div class="wrap-rails">
{RAIL_LEFT}

<div class="wrap">
  <div class="match-hero">
    <div class="team-block">
      <div class="team-name">{m['home_full']}</div>
      <div class="team-short">HOME</div>
    </div>
    <div class="vs-block">VS</div>
    <div class="team-block">
      <div class="team-name">{m['away_full']}</div>
      <div class="team-short">AWAY</div>
    </div>
  </div>

  <div style="display:flex;gap:10px;flex-wrap:wrap;margin:-10px 0 20px;font-size:13px;">
    <span style="background:var(--muted);border-radius:6px;padding:5px 11px;">&#128197; {m['date_str']}</span>
    <span style="background:var(--muted);border-radius:6px;padding:5px 11px;">&#9200; {m['time_str']} AEST</span>
    <span style="background:var(--muted);border-radius:6px;padding:5px 11px;">&#128205; {m['venue']}</span>
  </div>

  <div class="section">
    <h2>Sportsbet Odds  -  {m['home_nick']} vs {m['away_nick']}</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:14px">Opening market from Sportsbet. Compare with Betr, PointsBet, Ladbrokes, Neds and Picklebet for best value before placing.</p>
    <div class="odds-row">
      <div class="odds-card"><div class="odds-label">{m['home_nick']} Win (H2H)</div><div class="odds-val" style="color:var(--accent)">${m['h2h_home']}</div><div class="odds-sub">Head to Head</div></div>
      <div class="odds-card"><div class="odds-label">{m['away_nick']} Win (H2H)</div><div class="odds-val" style="color:var(--accent)">${m['h2h_away']}</div><div class="odds-sub">Head to Head</div></div>
    </div>
    <div class="odds-row">
      <div class="odds-card"><div class="odds-label">{m['home_nick']} {m['line_home_h']}</div><div class="odds-val">${m['line_home_o']}</div><div class="odds-sub">Line</div></div>
      <div class="odds-card"><div class="odds-label">{m['away_nick']} {m['line_away_h']}</div><div class="odds-val">${m['line_away_o']}</div><div class="odds-sub">Line</div></div>
    </div>
    <p style="font-size:11px;color:var(--muted-fg);margin-top:8px">Odds from Sportsbet at time of publication and subject to change. 18+ &middot; Bet Responsibly.</p>
  </div>

  {analysis_section(m, p)}

  {team_section(m, t)}

  <div class="section">
    <h2>Best Bookmakers for {m['home_nick']} vs {m['away_nick']}</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:14px">Compare Australia&rsquo;s top NRL bookmakers before placing. Direct links open at each bookmaker via PuntGuide&rsquo;s tracked affiliate.</p>
    {BOOKIES_BLOCK}
    <p style="font-size:12px;color:var(--muted-fg);text-align:center;margin-top:14px">18+ only. Gamble responsibly. <a href="/all-betting-sites.html" style="color:var(--accent);font-weight:600">Compare all 130+ bookmakers &rarr;</a></p>
  </div>

  <div class="int-links"><h3>Related pages</h3>
    <a href="/nrl-round-14-tips-2026.html">NRL Round 14 Tips Hub</a>
    <a href="/nrl-tips.html">NRL Tips 2026</a>
    <a href="/nrl-ladder-2026.html">NRL Ladder 2026</a>
    <a href="/best-betting-sites-for-nrl.html">Best NRL Betting Sites</a>
    <a href="/all-betting-sites.html">All 130+ Bookmakers</a>
  </div>

  <div class="faq">
    <h2>Frequently asked questions</h2>
    {faq_items}
  </div>

</div>

{RAIL_RIGHT}
</div>
</div>
{FOOTER.format(desc=f'{m["home_full"]} vs {m["away_full"]} tips and Best Bet  -  NRL Round 14 2026.')}
{SCRIPTS_TAIL}
</body></html>"""

    out_path = os.path.join(OUT, slug + '.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    return slug + '.html'


# ── Hub page ────────────────────────────────────────────────────────────────

def build_hub():
    cards = []
    for m in MATCHES:
        slug = f"nrl-{m['home_slug']}-vs-{m['away_slug']}-round-14-2026.html"
        p    = PICKS[f"{m['home_slug']}-vs-{m['away_slug']}"]
        cards.append(f'''<div class="match-card">
  <div class="mc-teams"><a href="/{slug}">{m['home_full']} vs {m['away_full']}</a></div>
  <div class="mc-meta">&#128197; {m['date_short']} &middot; &#9200; {m['time_str']} AEST<br>&#128205; {m['venue']}</div>
  <div class="mc-odds">H2H: {m['home_nick']} ${m['h2h_home']} &middot; {m['away_nick']} ${m['h2h_away']}</div>
  <div class="mc-tip">
    <span class="mc-tip-line"><span class="mc-tip-star">&#11088;</span> Best Bet: {p['tip_label']} (${p['tip_odds']})</span>
    <span class="mc-tip-line">Anytime Tryscorer: {p['tryscorer']}</span>
  </div>
  <a href="/{slug}" class="mc-badge">Full Analysis &rarr;</a>
</div>''')
    grid = '\n'.join(cards)

    faqs = [
        ("What NRL matches are in Round 14 2026?",
         f"NRL Round 14 2026 features 8 matches played from Thursday 4 June to Monday 8 June. The bye team is the {BYE_TEAM}. Full fixture, tips and odds above."),
        ("What are the PuntGuide Round 14 tips?",
         "PuntGuide publishes a Best Bet (winner or handicap) and an anytime tryscorer pick for every Round 14 match. All picks are listed on the match cards above and full analysis is available on each match page."),
        ("Where can I bet on NRL Round 14 2026?",
         "Betr is PuntGuide's editorial pick for NRL betting in 2026 &mdash; sharpest line markets and deepest tryscorer book. Sportsbet, PointsBet, Ladbrokes, Neds and Picklebet are also strong. Compare all 130+ Australian bookmakers before placing."),
    ]
    faq_schema_obj = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a.replace('&mdash;', '—')}} for q, a in faqs]}
    faq_items = ''.join(f'<div class="faq-item"><button class="faq-q">{q} <span class="fi">+</span></button><div class="faq-a">{a}</div></div>' for q, a in faqs)

    title = "NRL Round 14 Tips 2026  -  Best Bets &amp; Tryscorers for All 8 Matches | PuntGuide"
    desc  = "PuntGuide NRL Round 14 2026 tips. Best Bet + tryscorer pick for every match, with Sportsbet odds, team lists and full analysis. 4 Jun–8 Jun."

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
{GTAG}
<meta charset="UTF-8">
{ICONS}
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/nrl-round-14-tips-2026">
<meta property="og:title" content="NRL Round 14 Tips 2026 | PuntGuide">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/nrl-round-14-tips-2026">
<meta property="og:type" content="article">
<meta name="robots" content="index, follow">
{FONTS}
<script type="application/ld+json">{json.dumps(faq_schema_obj, separators=(',', ':'))}</script>
<style>{CSS}</style>
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@puntguide">
<meta name="twitter:title" content="NRL Round 14 Tips 2026 | PuntGuide">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/puntguide-logo.png">
</head>
<body>
{CB}
{NAV}
<div class="pb">
<div class="hero"><div class="hero-in">
  <div class="bc"><a href="/index.html">Home</a> &rsaquo; <a href="/nrl-tips.html">NRL 2026</a> &rsaquo; Round 14 Tips</div>
  <div class="eye"><span class="eye-l"></span><span class="eye-t">NRL 2026 &middot; Round 14</span></div>
  <h1>NRL Round 14 Tips 2026</h1>
  <div style="background:hsl(215 45% 16%);border-radius:10px;padding:16px 20px;margin:20px 0;"><div style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:hsl(48 92% 64%);margin-bottom:8px;font-family:'JetBrains Mono',monospace;">Short Answer</div><p style="font-size:15px;line-height:1.75;color:rgba(255,255,255,.9);margin:0;">PuntGuide picks a Best Bet (winner or handicap) and anytime tryscorer for every Round 14 match. Eight games across Thursday 4 June to Monday 8 June. Bye: {BYE_TEAM}. Sportsbet odds and team lists confirmed Tuesday 2 June.</p></div>
  <p style="font-size:16px;color:hsl(215 45% 16%/.65);max-width:700px;line-height:1.8;margin-top:10px">PuntGuide NRL Round 14 2026 tips. Best Bet + tryscorer pick for every match, with Sportsbet odds, team lists and full per-match analysis  -  4 Jun to 8 Jun.</p>
  <p class="upd">8 matches &middot; 4 Jun&ndash;8 Jun &middot; Bye: {BYE_TEAM}</p>
</div></div>

<div class="wrap-rails">
{RAIL_LEFT}

<div class="wrap">

  <div class="section">
    <h2>Round 14  -  Tips &amp; Tryscorers</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:16px">PuntGuide Best Bet and anytime tryscorer for every Round 14 match. Tap any card for full analysis, team lists and odds comparison.</p>
    <div class="match-grid">{grid}</div>
    <p style="font-size:13px;color:var(--muted-fg);margin-top:12px"><strong>Bye:</strong> {BYE_TEAM}</p>
  </div>

  <div class="section">
    <h2>Best Bookmakers for NRL Round 14</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:14px">Six top picks for NRL betting in Australia. Direct links open at each bookmaker via PuntGuide&rsquo;s tracked affiliate.</p>
    {BOOKIES_BLOCK}
    <p style="font-size:12px;color:var(--muted-fg);text-align:center;margin-top:14px">18+ only. Gamble responsibly. <a href="/all-betting-sites.html" style="color:var(--accent);font-weight:600">Compare all 130+ bookmakers &rarr;</a></p>
  </div>

  <div class="int-links"><h3>Related NRL pages</h3>
    <a href="/nrl-tips.html">NRL Tips 2026</a>
    <a href="/nrl-ladder-2026.html">NRL Ladder 2026</a>
    <a href="/best-betting-sites-for-nrl.html">Best NRL Betting Sites</a>
    <a href="/all-betting-sites.html">All 130+ Bookmakers</a>
  </div>

  <div class="faq">
    <h2>Frequently asked questions</h2>
    {faq_items}
  </div>

</div>

{RAIL_RIGHT}
</div>
</div>
{FOOTER.format(desc='PuntGuide NRL Round 14 2026  -  Best Bets, tryscorers and full analysis for all 8 matches.')}
{SCRIPTS_TAIL}
</body></html>"""

    out_path = os.path.join(OUT, 'nrl-round-14-tips-2026.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    return 'nrl-round-14-tips-2026.html'


def main():
    written = [build_hub()]
    for m in MATCHES:
        written.append(build_match_page(m))
    print(f'Wrote {len(written)} files:')
    for f in written:
        print(f'  {f}')


if __name__ == '__main__':
    main()
