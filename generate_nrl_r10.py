#!/usr/bin/env python3
"""Generate NRL Round 10 2026 match pages and hub from confirmed team lists."""
import json, os, re

BASE = "https://puntguide.com.au"

MATCHES = [
    {
        "slug": "nrl-dolphins-vs-bulldogs-round-10-2026",
        "home": "Dolphins", "away": "Canterbury Bulldogs",
        "home_short": "Dolphins", "away_short": "Bulldogs",
        "date": "Thursday, 7 May 2026", "time": "7:50 PM", "venue": "Suncorp Stadium",
        "h2h_home": "$1.50", "h2h_away": "$2.60", "line": "Dolphins -6.5",
        "tip": "Dolphins", "tip_margin": "7–12 points",
        "home_form": "LLLWL", "away_form": "LWLLL",
        "home_pos": "11th (8pts)", "away_pos": "12th (8pts)",
        "home_team": [
            "1. Hamiso Tabuai-Fidow", "2. Jamayne Isaako", "3. Jack Bostock",
            "4. Herbie Farnworth", "5. Selwyn Cobbo", "6. Brad Schneider",
            "7. Isaiya Katoa", "8. Thomas Flegler", "9. Max Plath",
            "10. Francis Molo", "11. Connelly Lemuelu", "12. Kulikefu Finefeuiaki",
            "13. Morgan Knowles",
            "Bench: 14. Ray Stone, 15. Tom Gilbert, 16. Felise Kaufusi, 17. Oryn Keeley"
        ],
        "away_team": [
            "1. Connor Tracey", "2. Jonathan Sua", "3. Bronson Xerri",
            "4. Stephen Crichton", "5. Enari Tuala", "6. Matt Burton",
            "7. Lachlan Galvin", "8. Samuel Hughes", "9. Bailey Hayward",
            "10. Leo Thompson", "11. Sitili Tupouniua", "12. Jacob Preston",
            "13. Jaeman Salmon",
            "Bench: 14. Alekolasimi Jones, 15. Sean O'Sullivan, 16. Harry Hayes, 17. Josh Curran"
        ],
        "key_stories": [
            ("Kodi Nikorima return", "Nikorima and Jeremy Marshall-King named to return from injury. If Marshall-King passes his fitness test he bolsters an experienced Dolphins bench considerably."),
            ("Bulldogs spine unchanged", "Ciraldo has resisted calls to shake up the spine despite a form slump — just one win from the last six. Kurt Mann (head knock) and Jake Turpin (biceps) are out."),
            ("Max Plath Origin bolter", "The Dolphins hooker is in red hot form and has been mentioned as a Queensland State of Origin bolter. His form is one of the stories of the Dolphins' season."),
        ],
        "analysis": "The Dolphins need a win here to keep pace in the top eight race. Their home record at Suncorp is competitive and the Bulldogs have genuine selection and form issues heading into this one. Ciraldo's reluctance to shake up his spine despite results is a concern — Dolphins to win and cover -6.5.",
        "best_bet": "Dolphins -6.5 @ Sportsbet",
    },
    {
        "slug": "nrl-roosters-vs-titans-round-10-2026",
        "home": "Sydney Roosters", "away": "Gold Coast Titans",
        "home_short": "Roosters", "away_short": "Titans",
        "date": "Friday, 8 May 2026", "time": "6:00 PM", "venue": "Polytec Stadium",
        "h2h_home": "$1.15", "h2h_away": "$6.00", "line": "Roosters -18.5",
        "tip": "Roosters", "tip_margin": "20+ points",
        "home_form": "WWWWL", "away_form": "LWLLL",
        "home_pos": "3rd (14pts)", "away_pos": "14th (6pts)",
        "home_team": [
            "1. James Tedesco", "2. Daniel Tupou", "3. Hugo Savala",
            "4. Robert Toia", "5. Cody Ramsey", "6. Daly Cherry-Evans",
            "7. Sam Walker", "8. Naufahu Whyte", "9. Reece Robson",
            "10. Spencer Leniu", "11. Angus Crichton", "12. Siua Wong",
            "13. Victor Radley",
            "Bench: 14. Connor Watson, 15. Egan Butcher, 16. Nat Butcher, 17. Salesi Foketi"
        ],
        "away_team": [
            "1. Keano Kini", "2. Jenson Taumoepeau", "3. Jojo Fifita",
            "4. AJ Brimson", "5. Phillip Sami", "6. Jayden Campbell",
            "7. Zane Harrison", "8. Klese Haas", "9. Oliver Pascoe",
            "10. Tino Fa'asuamaleaui", "11. Chris Randall", "12. Beau Fermor",
            "13. Cooper Bai",
            "Bench: 14. Kurtis Morrin, 15. Moeaki Fotuaika, 16. Josh Patston, 17. Arama Hau"
        ],
        "key_stories": [
            ("Cody Ramsey comeback", "Ramsey earns his first NRL start since 2022 after his remarkable comeback from Ulcerative Colitis, replacing the injured Mark Nawaqanitawase (ankle) on the wing."),
            ("Zane Harrison debut", "Hannay makes the bold call to hand Harrison his NRL debut at halfback, with Campbell shifting to five-eighth and Ilias dropped. The Harrison decision is the biggest selection gamble of the round."),
            ("Angus Crichton fitness watch", "Named despite a medial ligament injury. If he's ruled out, Radley shifts to second row with Whyte to lock and Nat Butcher starting at prop."),
        ],
        "analysis": "This is the mismatch of the round. The Roosters are firing with DCE, Walker, Tedesco and Robson building genuine combination. The Titans are handing NRL debuts to Harrison and Taumoepeau — brave but risky against this opposition. Back the Roosters to win easily; the -18.5 line is the question. Head-to-head at $1.15 has no value — look for margin markets.",
        "best_bet": "Roosters to win by 19+ @ Sportsbet",
    },
    {
        "slug": "nrl-cowboys-vs-eels-round-10-2026",
        "home": "North Queensland Cowboys", "away": "Parramatta Eels",
        "home_short": "Cowboys", "away_short": "Eels",
        "date": "Friday, 8 May 2026", "time": "8:00 PM", "venue": "Qld Country Bank Stadium",
        "h2h_home": "$1.35", "h2h_away": "$3.30", "line": "Cowboys -10.5",
        "tip": "Cowboys", "tip_margin": "12–16 points",
        "home_form": "WWWWL", "away_form": "LWLLL",
        "home_pos": "6th (12pts)", "away_pos": "15th (6pts)",
        "home_team": [
            "1. Scott Drinkwater", "2. Braidon Burns", "3. Jaxon Purdue",
            "4. Tomas Chester", "5. Zac Laybutt", "6. Jake Clifford",
            "7. Tom Dearden", "8. Coen Hess", "9. Reed Mahoney",
            "10. Jason Taumalolo", "11. Heilum Luki", "12. Sam McIntyre",
            "13. Reuben Cotter",
            "Bench: 14. Soni Luke, 15. Griffin Neame, 16. Thomas Mikaele, 17. Matthew Lodge"
        ],
        "away_team": [
            "1. Joash Papali'i", "2. Brian Kelly", "3. Jordan Samrani",
            "4. Sean Russell", "5. Josh Addo-Carr", "6. Ronald Volkman",
            "7. Mitchell Moses", "8. Luca Moretti", "9. Tallyn Da Silva",
            "10. Junior Paulo", "11. Kelma Tuilagi", "12. Jack Williams",
            "13. Jack de Belin",
            "Bench: 14. Dylan Walker, 15. Saxon Pryke, 16. Toni Mataele, 17. Charlie Guymer"
        ],
        "key_stories": [
            ("Taumalolo record game", "Jason Taumalolo becomes the Cowboys' most capped player in game 295, surpassing Johnathan Thurston. A massive milestone for one of the game's great forwards."),
            ("Nanai blow", "Origin lock Jeremiah Nanai re-aggravated his shoulder against the Bulldogs and is out — a massive blow for Queensland selectors ahead of Origin I."),
            ("Da Silva starts for Eels", "Tallyn Da Silva gets his shot at NRL hooker with Ryley Smith out (sternum). Da Silva left the Tigers to start — this is his chance to prove himself."),
        ],
        "analysis": "The Cowboys are formidable at home and the Eels are in disarray. Volkman is a below-average starting half at NRL level, Da Silva is untested as a starter and the Cowboys pack with Taumalolo, Hess and Cotter is one of the competition's most powerful. Back Cowboys and consider the -10.5 line given the Eels' structural weaknesses.",
        "best_bet": "Cowboys -10.5 @ Sportsbet",
    },
    {
        "slug": "nrl-dragons-vs-knights-round-10-2026",
        "home": "St George Illawarra Dragons", "away": "Newcastle Knights",
        "home_short": "Dragons", "away_short": "Knights",
        "date": "Saturday, 9 May 2026", "time": "3:00 PM", "venue": "WIN Stadium",
        "h2h_home": "$3.25", "h2h_away": "$1.35", "line": "Knights -9.5",
        "tip": "Knights", "tip_margin": "10–14 points",
        "home_form": "LLLL", "away_form": "WLWLL",
        "home_pos": "17th (2pts)", "away_pos": "10th (10pts)",
        "home_team": [
            "1. Clinton Gutherson", "2. Setu Tu", "3. Moses Suli",
            "4. Valentine Holmes", "5. Mathew Feagai", "6. Daniel Atkinson",
            "7. Kade Reed", "8. Emre Guler", "9. Damien Cook",
            "10. Toby Couchman", "11. Dylan Egan", "12. Ryan Couchman",
            "13. Hamish Stewart",
            "Bench: 14. Josh Kerr, 15. Loko Pasifiki Tonga, 16. Blake Lawrie, 17. Jacob Halangahu"
        ],
        "away_team": [
            "1. Kalyn Ponga", "2. Dominic Young", "3. Dane Gagai",
            "4. Bradman Best", "5. Greg Marzhew", "6. Fletcher Sharpe",
            "7. Dylan Brown", "8. Jacob Saifiti", "9. Phoenix Crossland",
            "10. Trey Mooney", "11. Dylan Lucas", "12. Jermaine McEwen",
            "13. Mathew Croker",
            "Bench: 14. Sandon Smith, 15. Tyson Frizell, 16. Pasami Saulo, 17. Francis Manuleleua"
        ],
        "key_stories": [
            ("Gutherson returns", "Captain Clint Gutherson is back from a hamstring injury at fullback, with Tyrell Sloan to the bench. A positive for the Dragons but it won't change the result against a resurgent Knights side."),
            ("Dylan Egan comeback", "Egan returns from an ACL injury suffered last year after a successful return in NSW Cup. A genuine boost for the Dragons' troubled edge defence."),
            ("Knights unchanged", "Holbrook has named the same side that beat the in-form Rabbitohs last week — a sign of growing confidence in a backline featuring Ponga, Best, Gagai and Marzhew."),
        ],
        "analysis": "The Dragons are winless and the Knights are building momentum after a significant backline boost. Ponga, Best and Brown are operating as a quality combination. Dragons at home will make it competitive but the Knights have too much class across the park.",
        "best_bet": "Newcastle Knights -9.5 @ Sportsbet",
    },
    {
        "slug": "nrl-rabbitohs-vs-sharks-round-10-2026",
        "home": "South Sydney Rabbitohs", "away": "Cronulla Sharks",
        "home_short": "Rabbitohs", "away_short": "Sharks",
        "date": "Saturday, 9 May 2026", "time": "5:30 PM", "venue": "Accor Stadium",
        "h2h_home": "$1.66", "h2h_away": "$2.23", "line": "Rabbitohs -2.5",
        "tip": "Rabbitohs", "tip_margin": "1–6 points",
        "home_form": "WWWLL", "away_form": "WWLL",
        "home_pos": "4th (12pts)", "away_pos": "8th (10pts)",
        "home_team": [
            "1. Jye Gray", "2. Alex Johnston", "3. Latrell Mitchell",
            "4. Campbell Graham", "5. Edward Kosi", "6. Cody Walker",
            "7. Ashton Ward", "8. Keaon Koloamatangi", "9. Bronson Garlick",
            "10. Sean Keppie", "11. Euan Aitken", "12. Tallis Duncan",
            "13. Cameron Murray",
            "Bench: 14. Matthew Dufty, 15. Lachlan Hubner, 16. Jamie Humphreys, 17. Tevita Tatola"
        ],
        "away_team": [
            "1. William Kennedy", "2. Mawene Hiroti", "3. Siosifa Talakai",
            "4. KL Iro", "5. Samuel Stonestreet", "6. Braydon Trindall",
            "7. Nicho Hynes", "8. Addin Fonua-Blake", "9. Blayke Brailey",
            "10. Toby Rudolf", "11. Briton Nikora", "12. Teig Wilton",
            "13. Cameron McInnes",
            "Bench: 14. Jesse Colquhoun, 15. Billy Burns, 16. Oregon Kaufusi, 17. Thomas Hazelton"
        ],
        "key_stories": [
            ("Ashton Ward debut", "Wayne Bennett has dropped Humphreys to the bench and handed Ward the halfback jersey in a major selection gamble. Ward's debut against the Sharks' defensive line will be one of the most watched storylines of the round."),
            ("Jye Gray at fullback", "Gray replaces the in-form Matt Dufty, who drops to the bench — a bold Bennett call. Gray is talented but this switch introduces uncertainty into a Souths side that has been building well."),
            ("Sharks unchanged", "No changes from the Sharks with Jesse Ramien (knee) still out. Hynes and the Sharks' attack will target the new-look Souths spine early."),
        ],
        "analysis": "This is the hardest game of the round to tip. Bennett's shake-up introduces a debut half and a fullback change in the same game — either a masterstroke or a gamble too far. The Sharks at $2.23 have genuine value if the new Souths combinations take time to gel. Back Souths at home but tread carefully on the line. This could easily be a 2–4 point game either way.",
        "best_bet": "Souths to win (head-to-head) @ $1.66 Sportsbet — avoid the line",
    },
    {
        "slug": "nrl-sea-eagles-vs-broncos-round-10-2026",
        "home": "Manly Sea Eagles", "away": "Brisbane Broncos",
        "home_short": "Sea Eagles", "away_short": "Broncos",
        "date": "Saturday, 9 May 2026", "time": "7:35 PM", "venue": "4 Pines Park",
        "h2h_home": "$1.70", "h2h_away": "$2.15", "line": "Sea Eagles -2.5",
        "tip": "Sea Eagles", "tip_margin": "4–10 points",
        "home_form": "WWWWL", "away_form": "LLWWL",
        "home_pos": "7th (10pts)", "away_pos": "9th (10pts)",
        "home_team": [
            "1. Tolutau Koula", "2. Jason Saab", "3. Clayton Faulalo",
            "4. Reuben Garrick", "5. Lehi Hopoate", "6. Luke Brooks",
            "7. Jamal Fogarty", "8. Taniela Paseka", "9. Brandon Wakeham",
            "10. Ethan Bullemor", "11. Haumole Olakau'atu", "12. Ben Trbojevic",
            "13. Jake Trbojevic",
            "Bench: 14. Jake Simpkin, 15. Nathan Brown, 16. Jackson Shereb, 17. Siosiua Taukeiaho"
        ],
        "away_team": [
            "1. Reece Walsh", "2. Josiah Karapani", "3. Jesse Arthars",
            "4. Gehamat Shibasaki", "5. Antonio Verhoeven", "6. Ezra Mam",
            "7. Thomas Duffy", "8. Ben Talty", "9. Cory Paix",
            "10. Jack Gosiewski", "11. Xavier Willison", "12. Jordan Riki",
            "13. Patrick Carrigan",
            "Bench: 14. Josh Rogers, 15. Preston Riki, 16. Va'a Semu, 17. Aublix Tawha"
        ],
        "key_stories": [
            ("Fogarty returns", "Jamal Fogarty is back from a groin injury — a key return for Manly who need their experienced halfback directing traffic against a Broncos side without Reynolds."),
            ("Reynolds out — Duffy starts", "Adam Reynolds is sidelined with a head knock. Tom Duffy steps in at halfback — a significant step down in experience for Brisbane. Deine Mariner (leg) and Kotoni Staggs (suspension) also miss out."),
            ("Ben Hunt on extended bench", "Hunt has been named on the extended bench and could make a shock return from a knee injury — if fit he gives the Broncos an experienced spine option off the bench."),
        ],
        "analysis": "Manly at home at 4 Pines Park is always tough, and the Broncos are coming in without Reynolds, Staggs and Mariner. That's too much quality to lose. Fogarty's return steadies Manly's attack. Back the Sea Eagles to win at home — the -2.5 line is tight enough to be value.",
        "best_bet": "Sea Eagles -2.5 @ Sportsbet",
    },
    {
        "slug": "nrl-storm-vs-wests-tigers-round-10-2026",
        "home": "Melbourne Storm", "away": "Wests Tigers",
        "home_short": "Storm", "away_short": "Wests Tigers",
        "date": "Sunday, 10 May 2026", "time": "2:00 PM", "venue": "AAMI Park",
        "h2h_home": "$1.62", "h2h_away": "$2.30", "line": "Storm -4.5",
        "tip": "Storm", "tip_margin": "6–12 points",
        "home_form": "LLLLL", "away_form": "WWWLL",
        "home_pos": "16th (4pts)", "away_pos": "5th (12pts)",
        "home_team": [
            "1. Sualauvi Faalogo", "2. William Warbrick", "3. Jack Howarth",
            "4. Nick Meaney", "5. Hugo Peel", "6. Cameron Munster",
            "7. Jahrome Hughes", "8. Stefano Utoikamanu", "9. Harry Grant",
            "10. Josh King", "11. Shawn Blore", "12. Ativalu Lisati",
            "13. Trent Loiero",
            "Bench: 14. Trent Toelau, 15. Joe Chan, 16. Davvy Moale, 17. Cooper Clarke"
        ],
        "away_team": [
            "1. Heath Mason", "2. Sunia Turuva", "3. Patrick Herbert",
            "4. Taylan May", "5. Luke Laulilii", "6. Jarome Luai",
            "7. Jock Madden", "8. Terrell May", "9. Tristan Hope",
            "10. Fonua Pole", "11. Sione Fainu", "12. Kai Pearce-Paul",
            "13. Alex Twal",
            "Bench: 14. Latu Fainu, 15. Bunty Afoa, 16. Alex Seyfarth, 17. Royce Hunt"
        ],
        "key_stories": [
            ("Jahrome Hughes returns", "Hughes is back from a head knock — a timely return with Tyran Wishart now facing a lengthy spell (ankle). Hughes' combinations with Munster and Grant are Storm's biggest attacking asset."),
            ("Tigers backline reshuffled", "Benji Marshall has dropped To'a and Tavana, named Mason at fullback (Bula sidelined) and Madden replaces the injured Doueihi (dislocated shoulder). Plenty of movement in the Tigers' lineup."),
            ("Kai Pearce-Paul returns", "A big boost for the Tigers — Pearce-Paul returning to the edge offsets the 12-week loss of Samuela Fainu (foot). He's one of their most important edge forwards."),
        ],
        "analysis": "Despite the Storm sitting 16th, they're at home at AAMI Park with Hughes, Munster, Grant and a full-strength pack. The ladder position is deceptive — this is still a quality side. The Tigers are reshuffling their backline and starting an untested halfback in Madden. Storm to win and the -4.5 line looks well within reach.",
        "best_bet": "Storm -4.5 @ Sportsbet",
    },
    {
        "slug": "nrl-raiders-vs-panthers-round-10-2026",
        "home": "Canberra Raiders", "away": "Penrith Panthers",
        "home_short": "Raiders", "away_short": "Panthers",
        "date": "Sunday, 10 May 2026", "time": "4:05 PM", "venue": "GIO Stadium",
        "h2h_home": "$3.55", "h2h_away": "$1.30", "line": "Panthers -9.5",
        "tip": "Panthers", "tip_margin": "10–16 points",
        "home_form": "WWLLL", "away_form": "WWWWL",
        "home_pos": "13th (8pts)", "away_pos": "1st (16pts)",
        "home_team": [
            "1. Kaeo Weekes", "2. Savelio Tamale", "3. Sebastian Kris",
            "4. Matthew Timoko", "5. Jed Stuart", "6. Ethan Strange",
            "7. Ethan Sanders", "8. Corey Horsburgh", "9. Tom Starling",
            "10. Joseph Tapine", "11. Hudson Young", "12. Simi Sasagi",
            "13. Jayden Brailey",
            "Bench: 14. Owen Pattie, 15. Daine Laurie, 16. Ata Mariota, 17. Morgan Smithies"
        ],
        "away_team": [
            "1. Dylan Edwards", "2. Thomas Jenkins", "3. Paul Alamoti",
            "4. Casey McLean", "5. Brian To'o", "6. Blaize Talagi",
            "7. Nathan Cleary", "8. Moses Leota", "9. Freddy Lussick",
            "10. Lindsay Smith", "11. Isaiah Papali'i", "12. Luke Garner",
            "13. Isaah Yeo",
            "Bench: 14. Jack Cole, 15. Scott Sorensen, 16. Liam Henry, 17. Izack Tago"
        ],
        "key_stories": [
            ("Panthers unchanged and rolling", "Ivan Cleary has named the same side that beat the Sea Eagles. Cleary, Talagi, Edwards, To'o and Yeo are operating at a level that justifies their ladder position."),
            ("Strange returns for Raiders", "Ethan Strange is back from an ankle injury, returning to the halves with Weekes shifting to fullback. A positive return but they face the competition leaders."),
            ("Raiders tough at home", "GIO Stadium is one of the NRL's tougher away venues. The Raiders won't roll over and Horsburgh, Tapine and Brailey will test the Panthers' defence."),
        ],
        "analysis": "GIO Stadium will make this more competitive than the $1.30 price suggests. However, the Panthers have been in dominant form and the Raiders have genuine selection issues at fullback and in the halves. Panthers to win, but the -9.5 line requires thought. A closer game than other Panthers victories is possible — back Panthers head-to-head if the line seems too big.",
        "best_bet": "Panthers to win — head-to-head @ $1.30 Sportsbet",
    },
]

FORM_MAP = {'W': ('fw', 'W'), 'L': ('fl', 'L'), 'D': ('fd', 'D')}

def form_html(form_str):
    badges = ''.join(f'<span class="fb {FORM_MAP[c][0]}">{FORM_MAP[c][1]}</span>' for c in form_str)
    return f'<div class="form-badges">{badges}</div>'

CSS = """<style>
:root{--bg:hsl(205 60% 96%);--fg:hsl(215 45% 16%);--primary:hsl(48 92% 64%);--pfg:hsl(215 45% 16%);--muted:hsl(205 40% 92%);--muted-fg:hsl(215 20% 42%);--accent:hsl(200 88% 58%);--border:hsl(205 40% 86%);--gg:linear-gradient(135deg,hsl(50 96% 72%),hsl(44 92% 60%));--sg:0 10px 40px -10px hsl(48 92% 54%/.4);--sc:0 4px 24px -8px hsl(215 50% 30%/.1);--ch:36px;--nh:80px;}
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
.hero-in{max-width:1100px;margin:0 auto;}
.bc{font-size:12px;color:var(--muted-fg);margin-bottom:10px;}.bc a{color:var(--muted-fg);text-decoration:none;}
.eye{display:flex;align-items:center;gap:10px;margin-bottom:12px;}.eye-l{height:1px;width:32px;background:var(--primary);}
.eye-t{font-family:"JetBrains Mono",monospace;font-size:11px;color:var(--primary);text-transform:uppercase;letter-spacing:.2em;}
.wrap{max-width:1100px;margin:0 auto;padding:44px 32px 80px;}
.section{background:#fff;border:1px solid var(--border);border-radius:14px;padding:24px 28px;margin:24px 0;box-shadow:var(--sc);}
.section h2{font-size:20px;font-weight:700;margin-bottom:14px;padding-bottom:10px;border-bottom:1px solid var(--border);}
.match-hero{display:flex;align-items:center;justify-content:space-between;gap:20px;padding:28px;background:hsl(215 45% 16%);border-radius:14px;margin:24px 0;color:#fff;}
.team-block{flex:1;text-align:center;}.team-name{font-size:20px;font-weight:800;font-family:"Geist",sans-serif;letter-spacing:-0.02em;}
.team-rec{font-size:11px;color:rgba(255,255,255,.6);margin-top:4px;font-family:"JetBrains Mono",monospace;}
.vs-col{text-align:center;}.vs-txt{font-size:28px;font-weight:800;color:var(--primary);}.match-info{font-size:12px;color:rgba(255,255,255,.6);margin-top:6px;}
.odds-strip{display:flex;gap:10px;margin:16px 0;flex-wrap:wrap;}
.odds-box{flex:1;min-width:140px;background:var(--muted);border-radius:10px;padding:14px;text-align:center;}
.odds-label{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:6px;}
.odds-val{font-size:22px;font-weight:800;font-family:"JetBrains Mono",monospace;}
.tip-box{background:hsl(140 40% 96%);border:2px solid hsl(140 50% 40%);border-radius:12px;padding:20px 24px;margin:16px 0;}
.tip-label{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:hsl(140 50% 35%);margin-bottom:6px;}
.tip-pick{font-size:18px;font-weight:800;font-family:"Geist",sans-serif;}
.best-bet{background:hsl(48 80% 97%);border:2px solid hsl(48 60% 70%);border-radius:10px;padding:14px 18px;margin-top:12px;font-size:14px;font-weight:700;}
.teams-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:14px 0;}
.team-list{background:var(--muted);border-radius:10px;padding:16px;}
.team-list h3{font-size:13px;font-weight:700;margin-bottom:8px;padding-bottom:6px;border-bottom:1px solid var(--border);}
.team-list ul{list-style:none;font-size:12px;line-height:1.9;color:hsl(215 45% 16%/.8);}
.story-item{margin-bottom:14px;padding-bottom:14px;border-bottom:1px solid var(--border);}
.story-item:last-child{border-bottom:none;margin-bottom:0;padding-bottom:0;}
.story-title{font-weight:700;font-size:14px;margin-bottom:4px;}
.story-body{font-size:14px;line-height:1.75;color:hsl(215 45% 16%/.8);}
.form-row{display:flex;align-items:center;gap:10px;margin:8px 0;}
.form-label{font-size:12px;color:var(--muted-fg);min-width:80px;}
.form-badges{display:flex;gap:3px;}
.fb{width:20px;height:20px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:9px;font-weight:700;color:#fff;}
.fw{background:hsl(140 50% 40%);}.fl{background:hsl(16 70% 45%);}.fd{background:hsl(215 30% 60%);}
.bm-row{display:flex;align-items:center;gap:14px;padding:12px;background:var(--muted);border-radius:10px;margin-bottom:10px;}
.bm-logo{width:44px;height:44px;border-radius:10px;object-fit:contain;background:#fff;box-shadow:var(--sc);flex-shrink:0;}
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
@media(max-width:768px){.nav-links{display:none;}.wrap,.hero{padding-left:16px;padding-right:16px;}.nav{padding:0 20px;}.teams-grid{grid-template-columns:1fr;}.match-hero{flex-direction:column;gap:12px;}.odds-strip{flex-direction:column;}}
</style>"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800&family=Inter+Tight:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">'

CB = '<div class="cb"><span class="cb-t">Bet Responsibly</span><span class="cb-h">Gambling Help: <a href="tel:1800858858">1800 858 858</a> · <a href="https://www.gamblinghelponline.org.au" target="_blank">gamblinghelponline.org.au</a></span><div class="cb-b"><span>18+</span><span>AUS ONLY</span></div></div>'

NAV = '<nav class="nav"><a href="/index.html" class="nav-logo"><img src="/puntguide-logo.png" alt="PuntGuide"></a><ul class="nav-links"><li><a href="/nrl-tips.html">NRL Tips</a></li><li><a href="/nrl-round-10-tips-2026.html" style="color:var(--primary)">Round 10</a></li><li><a href="/nrl-ladder-2026.html">NRL Ladder</a></li><li><a href="/best-betting-sites-for-nrl.html">Best for NRL</a></li><li><a href="/all-betting-sites.html">All Sites</a></li></ul><a href="/best-betting-sites-australia.html" class="btn-g">Bet Now →</a></nav>'

FAQ_JS = '<script>document.querySelectorAll(".faq-q").forEach(b=>b.addEventListener("click",function(){const a=this.nextElementSibling;a.classList.toggle("open");this.querySelector(".fi").textContent=a.classList.contains("open")?"−":"+";}));</script>'

def gen_match(m):
    slug = m['slug']
    title = f"{m['home']} vs {m['away']} Tips & Prediction — NRL Round 10 2026 | PuntGuide"
    desc = f"Expert {m['home_short']} vs {m['away_short']} tip for NRL Round 10 2026. Our prediction: {m['tip']} by {m['tip_margin']}. Team lists, key ins & outs, odds and best bet."
    canonical = f"{BASE}/{slug}.html"

    schema_event = json.dumps({
        "@context": "https://schema.org", "@type": "SportsEvent",
        "name": f"{m['home']} vs {m['away']}",
        "startDate": f"2026-05-{m['date'].split()[1].zfill(2)}T{m['time'].replace(' PM','').replace(' AM','').strip()}:00+10:00",
        "location": {"@type": "Place", "name": m['venue'], "address": {"@type": "PostalAddress", "addressCountry": "AU"}},
        "sport": "Rugby League",
        "competitor": [{"@type": "SportsTeam", "name": m['home']}, {"@type": "SportsTeam", "name": m['away']}],
        "organizer": {"@type": "Organization", "name": "NRL"},
        "eventStatus": "https://schema.org/EventScheduled",
        "image": f"{BASE}/puntguide-logo.png",
        "performer": [{"@type": "SportsTeam", "name": m['home']}, {"@type": "SportsTeam", "name": m['away']}],
        "description": desc
    })

    schema_faq = json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": f"Who will win {m['home_short']} vs {m['away_short']}?",
             "acceptedAnswer": {"@type": "Answer", "text": f"Our tip is {m['tip']} to win by {m['tip_margin']}. {m['analysis'][:200]}"}},
            {"@type": "Question", "name": f"When is {m['home_short']} vs {m['away_short']} Round 10?",
             "acceptedAnswer": {"@type": "Answer", "text": f"{m['home']} vs {m['away']} kicks off at {m['time']} AEST on {m['date']} at {m['venue']}."}},
            {"@type": "Question", "name": f"What are the odds for {m['home_short']} vs {m['away_short']}?",
             "acceptedAnswer": {"@type": "Answer", "text": f"{m['home']} are priced at {m['h2h_home']} and {m['away']} at {m['h2h_away']}. Line: {m['line']}."}},
        ]
    })

    stories_html = ''.join(f'''<div class="story-item">
      <div class="story-title">{s[0]}</div>
      <div class="story-body">{s[1]}</div>
    </div>''' for s in m['key_stories'])

    home_list = ''.join(f'<li>{p}</li>' for p in m['home_team'])
    away_list = ''.join(f'<li>{p}</li>' for p in m['away_team'])

    day_num = m['date'].split()[1]
    iso_date = f"2026-05-{day_num.zfill(2)}"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{m['home_short']} vs {m['away_short']} — NRL Round 10 2026 | PuntGuide">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="article">
<meta property="og:image" content="{BASE}/puntguide-logo.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@puntguide">
<meta name="twitter:title" content="{m['home_short']} vs {m['away_short']} — NRL Round 10 2026 | PuntGuide">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{BASE}/puntguide-logo.png">
<meta name="robots" content="index, follow">
<link rel="icon" type="image/png" href="/pg-icon.png">
{FONTS}
<script type="application/ld+json">{schema_event}</script>
<script type="application/ld+json">{schema_faq}</script>
{CSS}
</head>
<body>
{CB}
{NAV}
<div class="pb">
<div class="hero"><div class="hero-in">
  <div class="bc"><a href="/index.html">Home</a> › <a href="/nrl-tips.html">NRL Tips 2026</a> › <a href="/nrl-round-10-tips-2026.html">Round 10</a> › {m['home_short']} vs {m['away_short']}</div>
  <div class="eye"><span class="eye-l"></span><span class="eye-t">NRL Round 10 · {m['date']} · {m['time']} AEST</span></div>
  <h1>{m['home']} vs {m['away']} Tips & Prediction</h1>
  <p style="font-size:16px;color:hsl(215 45% 16%/.65);max-width:700px;line-height:1.8;margin-top:10px">NRL Round 10 2026 — {m['venue']}. Expert tip, confirmed team lists, key ins & outs and best bet recommendation.</p>
</div></div>
<div class="wrap">

  <div class="match-hero">
    <div class="team-block">
      <div class="team-name">{m['home']}</div>
      <div class="team-rec">{m['home_pos']}</div>
      <div class="form-row" style="justify-content:center;margin-top:8px;">{form_html(m['home_form'])}</div>
    </div>
    <div class="vs-col">
      <div class="vs-txt">VS</div>
      <div class="match-info">{m['date']}<br>{m['time']} AEST<br>{m['venue']}</div>
    </div>
    <div class="team-block">
      <div class="team-name">{m['away']}</div>
      <div class="team-rec">{m['away_pos']}</div>
      <div class="form-row" style="justify-content:center;margin-top:8px;">{form_html(m['away_form'])}</div>
    </div>
  </div>

  <div class="section">
    <h2>Odds — {m['home_short']} vs {m['away_short']}</h2>
    <div class="odds-strip">
      <div class="odds-box">
        <div class="odds-label">{m['home_short']} Win</div>
        <div class="odds-val" style="color:var(--accent)">{m['h2h_home']}</div>
      </div>
      <div class="odds-box">
        <div class="odds-label">Line</div>
        <div class="odds-val" style="font-size:16px">{m['line']}</div>
      </div>
      <div class="odds-box">
        <div class="odds-label">{m['away_short']} Win</div>
        <div class="odds-val" style="color:var(--accent)">{m['h2h_away']}</div>
      </div>
    </div>
    <p style="font-size:11px;color:var(--muted-fg)">Odds from Sportsbet · Subject to change · Always compare across bookmakers · 18+ · Bet responsibly</p>
  </div>

  <div class="section">
    <h2>Our Tip — {m['home_short']} vs {m['away_short']}</h2>
    <div class="tip-box">
      <div class="tip-label">NRL Round 10 Prediction</div>
      <div class="tip-pick">✅ {m['tip']} to win by {m['tip_margin']}</div>
    </div>
    <p style="font-size:14px;line-height:1.8;margin-top:14px;">{m['analysis']}</p>
    <div class="best-bet">🏆 Best Bet: {m['best_bet']}</div>
    <p style="font-size:11px;color:var(--muted-fg);margin-top:8px;">Tips are editorial opinion only. Always gamble responsibly. 18+ only.</p>
  </div>

  <div class="section">
    <h2>Team Lists — Round 10</h2>
    <div class="teams-grid">
      <div class="team-list">
        <h3>{m['home']}</h3>
        <ul>{home_list}</ul>
      </div>
      <div class="team-list">
        <h3>{m['away']}</h3>
        <ul>{away_list}</ul>
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Key Storylines</h2>
    {stories_html}
  </div>

  <div class="section">
    <h2>Best Bookmakers for NRL Betting</h2>
    <div class="bm-row">
      <img src="/sportsbet.png" alt="Sportsbet" class="bm-logo">
      <div style="flex:1"><div style="font-weight:700;margin-bottom:2px">Sportsbet</div><div style="font-size:13px;color:var(--muted-fg)">Widest NRL market range · Same-game multis · Best odds on NRL props</div></div>
      <a href="/review-sportsbet.html" class="btn-g" style="font-size:12px;padding:7px 13px">Review →</a>
    </div>
    <div class="bm-row">
      <img src="/pointsbet.png" alt="PointsBet" class="bm-logo">
      <div style="flex:1"><div style="font-weight:700;margin-bottom:2px">PointsBet</div><div style="font-size:13px;color:var(--muted-fg)">Sharp NRL odds · PointsBetting on player stats · Competitive live markets</div></div>
      <a href="/review-pointsbet.html" class="btn-g" style="font-size:12px;padding:7px 13px">Review →</a>
    </div>
    <div class="bm-row">
      <img src="/betr.png" alt="betr" class="bm-logo">
      <div style="flex:1"><div style="font-weight:700;margin-bottom:2px">betr</div><div style="font-size:13px;color:var(--muted-fg)">Best same-game multi builder for NRL in Australia</div></div>
      <a href="/review-betr.html" class="btn-g" style="font-size:12px;padding:7px 13px">Review →</a>
    </div>
  </div>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:0 0 24px;">
    <a href="/best-betting-sites-australia.html" style="display:flex;align-items:center;justify-content:center;gap:8px;background:hsl(215 45% 16%);color:#fff;border-radius:10px;padding:15px;text-decoration:none;font-size:13px;font-weight:700;" onmouseover="this.style.opacity='.85'" onmouseout="this.style.opacity='1'">🏆 Best Betting Sites →</a>
    <a href="/all-betting-sites.html" style="display:flex;align-items:center;justify-content:center;gap:8px;background:var(--gg);color:hsl(215 45% 16%);border-radius:10px;padding:15px;text-decoration:none;font-size:13px;font-weight:700;box-shadow:var(--sg);" onmouseover="this.style.opacity='.85'" onmouseout="this.style.opacity='1'">📋 All 130+ Bookmakers →</a>
  </div>

  <div class="int-links"><h3>NRL Round 10 Tips</h3>
    <a href="/nrl-round-10-tips-2026.html">Round 10 Hub</a>
    <a href="/nrl-tips.html">NRL Tips 2026</a>
    <a href="/nrl-ladder-2026.html">NRL Ladder</a>
    <a href="/best-betting-sites-for-nrl.html">Best Sites for NRL</a>
    <a href="/best-betting-sites-australia.html">Best Betting Sites</a>
  </div>

  <div class="faq">
    <h2>Frequently asked questions</h2>
    <div class="faq-item"><button class="faq-q">Who will win {m['home_short']} vs {m['away_short']}? <span class="fi">+</span></button><div class="faq-a">Our tip is <strong>{m['tip']}</strong> to win by {m['tip_margin']}. {m['analysis'][:300]}</div></div>
    <div class="faq-item"><button class="faq-q">When is {m['home_short']} vs {m['away_short']} playing? <span class="fi">+</span></button><div class="faq-a">{m['home']} vs {m['away']} kicks off at {m['time']} AEST on {m['date']} at {m['venue']}.</div></div>
    <div class="faq-item"><button class="faq-q">What are the odds for this match? <span class="fi">+</span></button><div class="faq-a">{m['home']} are priced at {m['h2h_home']} and {m['away']} at {m['h2h_away']} with Sportsbet. Line: {m['line']}. Always compare odds across bookmakers before placing.</div></div>
  </div>

</div>
</div>
<footer class="site-footer"><div class="footer-in">
<img src="/puntguide-logo.png" alt="PuntGuide" class="footer-logo">
<p class="footer-desc">{m['home']} vs {m['away']} tips — NRL Round 10 2026.</p>
<div class="footer-links">
  <a href="/nrl-round-10-tips-2026.html">NRL Round 10 Tips</a>
  <a href="/nrl-tips.html">NRL Tips 2026</a>
  <a href="/nrl-ladder-2026.html">NRL Ladder</a>
  <a href="/best-betting-sites-for-nrl.html">Best for NRL</a>
  <a href="/best-betting-sites-australia.html">Best Betting Sites</a>
</div>
<div class="footer-rg">Gamble responsibly. Call <a href="tel:1800858858">Gambling Help 1800 858 858</a> or visit <a href="https://www.gamblinghelponline.org.au" target="_blank">gamblinghelponline.org.au</a>. 18+ only. Tips are editorial predictions only.</div>
</div></footer>
{FAQ_JS}
<script src="/nav-drawer.js"></script>
</body></html>"""


def gen_hub():
    match_cards = ''
    for m in MATCHES:
        match_cards += f'''<div style="background:var(--muted);border-radius:12px;padding:16px 18px;border:1px solid var(--border);">
  <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--muted-fg);margin-bottom:6px;">{m['date']} · {m['time']} AEST · {m['venue']}</div>
  <div style="font-size:16px;font-weight:800;font-family:'Geist',sans-serif;margin-bottom:6px;"><a href="/{m['slug']}.html" style="text-decoration:none;color:var(--fg);">{m['home']} vs {m['away']}</a></div>
  <div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap;">
    <span style="font-size:12px;color:var(--muted-fg);">{m['h2h_home']} / {m['h2h_away']} · {m['line']}</span>
    <span style="background:hsl(140 50% 40%);color:#fff;font-size:11px;font-weight:700;padding:2px 8px;border-radius:4px;">Tip: {m['tip']}</span>
  </div>
  <a href="/{m['slug']}.html" style="display:inline-block;margin-top:8px;background:hsl(215 45% 16%);color:var(--primary);font-size:11px;font-weight:700;padding:3px 9px;border-radius:5px;text-decoration:none;font-family:'JetBrains Mono',monospace;">Tips & Team Lists →</a>
</div>\n'''

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>NRL Round 10 Tips 2026 — Team Lists, Predictions & Best Bets | PuntGuide</title>
<meta name="description" content="NRL Round 10 2026 tips — confirmed team lists, ins and outs, expert predictions and best bets for all 8 matches. Taumalolo record game, Ashton Ward debut, Zane Harrison debut.">
<link rel="canonical" href="{BASE}/nrl-round-10-tips-2026.html">
<meta property="og:title" content="NRL Round 10 Tips 2026 | PuntGuide">
<meta property="og:description" content="NRL Round 10 team lists, tips and best bets. Panthers vs Raiders, Roosters vs Titans, Cowboys vs Eels and more.">
<meta property="og:url" content="{BASE}/nrl-round-10-tips-2026.html">
<meta property="og:type" content="article">
<meta property="og:image" content="{BASE}/puntguide-logo.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@puntguide">
<meta name="twitter:title" content="NRL Round 10 Tips 2026 | PuntGuide">
<meta name="twitter:description" content="NRL Round 10 team lists, tips and best bets for all 8 matches.">
<meta name="twitter:image" content="{BASE}/puntguide-logo.png">
<meta name="robots" content="index, follow">
<link rel="icon" type="image/png" href="/pg-icon.png">
{FONTS}
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What NRL matches are in Round 10 2026?","acceptedAnswer":{"@type":"Answer","text":"NRL Round 10 2026 features 8 matches: Dolphins vs Bulldogs (Thu), Roosters vs Titans and Cowboys vs Eels (Fri), Dragons vs Knights, Rabbitohs vs Sharks and Sea Eagles vs Broncos (Sat), Storm vs Wests Tigers and Raiders vs Panthers (Sun). Warriors have the bye."}},{"@type":"Question","name":"What is the best NRL bet in Round 10?","acceptedAnswer":{"@type":"Answer","text":"Our best bet of the round is Cowboys -10.5 against a depleted Eels side. Taumalolo plays his record 295th game and the Cowboys pack is one of the competition's most powerful at home."}}]})}</script>
{CSS}
</head>
<body>
{CB}
{NAV}
<div class="pb">
<div class="hero"><div class="hero-in">
  <div class="bc"><a href="/index.html">Home</a> › <a href="/nrl-tips.html">NRL Tips 2026</a> › Round 10</div>
  <div class="eye"><span class="eye-l"></span><span class="eye-t">NRL 2026 · Round 10 · 7–10 May</span></div>
  <h1>NRL Round 10 Tips 2026</h1>
  <p style="font-size:16px;color:hsl(215 45% 16%/.65);max-width:700px;line-height:1.8;margin-top:10px">Confirmed team lists, key ins & outs, expert tips and best bets for all 8 NRL Round 10 matches. Taumalolo's record game, Ashton Ward's debut half and Zane Harrison's NRL debut.</p>
  <p style="font-size:12px;color:var(--muted-fg);margin-top:8px;font-family:'JetBrains Mono',monospace;">8 matches · 7–10 May 2026 · Bye: Warriors</p>
</div></div>
<div class="wrap">

  <div class="section">
    <h2>Round 10 — All Matches & Tips</h2>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:16px 0;">
      {match_cards}
    </div>
    <p style="font-size:11px;color:var(--muted-fg);margin-top:8px;">Odds from Sportsbet · Tips are editorial opinion only · 18+ · Gamble responsibly</p>
  </div>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:0 0 24px;">
    <a href="/best-betting-sites-australia.html" style="display:flex;align-items:center;justify-content:center;gap:8px;background:hsl(215 45% 16%);color:#fff;border-radius:10px;padding:15px;text-decoration:none;font-size:13px;font-weight:700;" onmouseover="this.style.opacity='.85'" onmouseout="this.style.opacity='1'">🏆 Best Betting Sites →</a>
    <a href="/all-betting-sites.html" style="display:flex;align-items:center;justify-content:center;gap:8px;background:var(--gg);color:hsl(215 45% 16%);border-radius:10px;padding:15px;text-decoration:none;font-size:13px;font-weight:700;box-shadow:var(--sg);" onmouseover="this.style.opacity='.85'" onmouseout="this.style.opacity='1'">📋 All 130+ Bookmakers →</a>
  </div>

  <div class="section">
    <h2>Round 10 Storylines</h2>
    <p style="font-size:14px;line-height:1.8;"><strong>Taumalolo's record (Cowboys v Eels):</strong> Jason Taumalolo becomes the Cowboys' most-capped player in game 295, passing Johnathan Thurston. A massive milestone for one of the great NRL forwards.</p>
    <p style="font-size:14px;line-height:1.8;margin-top:10px;"><strong>Ashton Ward debuts at halfback (Rabbitohs v Sharks):</strong> Wayne Bennett drops Humphreys and hands the halfback jersey to Ward — one of the boldest selections of the season. Souths also start Jye Gray over the in-form Matt Dufty at fullback.</p>
    <p style="font-size:14px;line-height:1.8;margin-top:10px;"><strong>Zane Harrison's NRL debut (Roosters v Titans):</strong> Josh Hannay makes the call to hand the highly touted Harrison his NRL debut at halfback against the competition's hottest team. Brave but risky.</p>
    <p style="font-size:14px;line-height:1.8;margin-top:10px;"><strong>Broncos without Reynolds (Sea Eagles v Broncos):</strong> Adam Reynolds is out with a head knock. Tom Duffy steps up at halfback. Combined with the losses of Staggs and Mariner, Brisbane face a tough ask at 4 Pines Park.</p>
  </div>

  <div class="section">
    <h2>Best Bookmakers for NRL Round 10</h2>
    <div class="bm-row">
      <img src="/sportsbet.png" alt="Sportsbet" class="bm-logo">
      <div style="flex:1"><div style="font-weight:700;margin-bottom:2px">Sportsbet</div><div style="font-size:13px;color:var(--muted-fg)">Widest NRL market · Best same-game multis · Full Round 10 coverage</div></div>
      <a href="/review-sportsbet.html" class="btn-g" style="font-size:12px;padding:7px 13px">Review →</a>
    </div>
    <div class="bm-row">
      <img src="/pointsbet.png" alt="PointsBet" class="bm-logo">
      <div style="flex:1"><div style="font-weight:700;margin-bottom:2px">PointsBet</div><div style="font-size:13px;color:var(--muted-fg)">Sharp NRL odds · PointsBetting on player stats</div></div>
      <a href="/review-pointsbet.html" class="btn-g" style="font-size:12px;padding:7px 13px">Review →</a>
    </div>
    <div class="bm-row">
      <img src="/betr.png" alt="betr" class="bm-logo">
      <div style="flex:1"><div style="font-weight:700;margin-bottom:2px">betr</div><div style="font-size:13px;color:var(--muted-fg)">Best same-game multi builder for NRL in Australia</div></div>
      <a href="/review-betr.html" class="btn-g" style="font-size:12px;padding:7px 13px">Review →</a>
    </div>
  </div>

  <div class="int-links"><h3>Related NRL pages</h3>
    <a href="/nrl-tips.html">NRL Tips 2026</a>
    <a href="/nrl-ladder-2026.html">NRL Ladder 2026</a>
    <a href="/best-betting-sites-for-nrl.html">Best Sites for NRL</a>
    <a href="/best-betting-sites-australia.html">Best Betting Sites</a>
    <a href="/all-betting-sites.html">All 130+ Bookmakers</a>
  </div>

</div>
</div>
<footer class="site-footer"><div class="footer-in">
<img src="/puntguide-logo.png" alt="PuntGuide" class="footer-logo">
<p class="footer-desc">NRL Round 10 2026 tips — team lists, predictions and best bets for all 8 matches.</p>
<div class="footer-links">
  <a href="/nrl-round-10-tips-2026.html">NRL Round 10</a>
  <a href="/nrl-tips.html">NRL Tips 2026</a>
  <a href="/nrl-ladder-2026.html">NRL Ladder</a>
  <a href="/best-betting-sites-for-nrl.html">Best for NRL</a>
  <a href="/best-betting-sites-australia.html">Best Betting Sites</a>
</div>
<div class="footer-rg">Gamble responsibly. Call <a href="tel:1800858858">Gambling Help 1800 858 858</a> or visit <a href="https://www.gamblinghelponline.org.au" target="_blank">gamblinghelponline.org.au</a>. 18+ only.</div>
</div></footer>
{FAQ_JS}
<script src="/nav-drawer.js"></script>
</body></html>"""


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Write match pages
    for m in MATCHES:
        fn = f"{m['slug']}.html"
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(gen_match(m))
        print(f"  Written: {fn}")

    # Write hub (overwrite old mislabeled Round 9 hub)
    with open('nrl-round-10-tips-2026.html', 'w', encoding='utf-8') as f:
        f.write(gen_hub())
    print("  Written: nrl-round-10-tips-2026.html")

    print(f"\nDone — {len(MATCHES)} match pages + 1 hub")
