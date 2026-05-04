#!/usr/bin/env python3
"""Update NBA Championship page with real Sportsbet odds."""
import re

with open('nba-championship-odds-2026.html', 'r', encoding='utf-8') as f:
    html = f.read()

NEW_ODDS_SECTION = '''  <div class="section">
    <h2>NBA Championship 2026 — Current Odds</h2>
    <p style="font-size:13px;color:var(--muted-fg);margin-bottom:6px">NBA Finals 2026 — Game 1 tips off <strong>Thursday 11 June 2026</strong>. Oklahoma City Thunder are the dominant market favourite at $1.67. Odds sourced from Sportsbet.</p>
    <div style="background:hsl(48 80% 97%);border:1px solid hsl(48 60% 80%);border-radius:8px;padding:10px 14px;margin-bottom:14px;font-size:12px;color:hsl(215 20% 42%);">&#9888;&#65039; Sportsbet treats NBA Finals Winner as a single event &#8212; Same Game Multi Term 5.2 applies. Odds are not multiplied independently across legs.</div>
    <table class="odds-table">
      <thead>
        <tr><th>Team</th><th>Conference</th><th style="text-align:center;">Sportsbet</th></tr>
      </thead>
      <tbody>
        <tr style="background:hsl(48 80% 97%);">
          <td><div class="team-name">Oklahoma City Thunder <span class="favourite-chip">HEAVY FAVOURITE</span></div></td>
          <td><div class="team-conf">Western Conference</div></td>
          <td style="text-align:center;"><span class="odds-chip" style="background:hsl(140 50% 35%);">$1.67</span></td>
        </tr>
        <tr>
          <td><div class="team-name">San Antonio Spurs</div></td>
          <td><div class="team-conf">Western Conference</div></td>
          <td style="text-align:center;"><span class="odds-chip">$5.00</span></td>
        </tr>
        <tr>
          <td><div class="team-name">New York Knicks</div></td>
          <td><div class="team-conf">Eastern Conference</div></td>
          <td style="text-align:center;"><span class="odds-chip">$9.50</span></td>
        </tr>
        <tr>
          <td><div class="team-name">Cleveland Cavaliers</div></td>
          <td><div class="team-conf">Eastern Conference</div></td>
          <td style="text-align:center;"><span class="odds-chip">$17.00</span></td>
        </tr>
        <tr>
          <td><div class="team-name">Detroit Pistons</div></td>
          <td><div class="team-conf">Eastern Conference</div></td>
          <td style="text-align:center;"><span class="odds-chip">$17.00</span></td>
        </tr>
        <tr>
          <td><div class="team-name">Los Angeles Lakers</div></td>
          <td><div class="team-conf">Western Conference</div></td>
          <td style="text-align:center;"><span class="odds-chip">$41.00</span></td>
        </tr>
        <tr>
          <td><div class="team-name">Philadelphia 76ers</div></td>
          <td><div class="team-conf">Eastern Conference</div></td>
          <td style="text-align:center;"><span class="odds-chip">$46.00</span></td>
        </tr>
        <tr>
          <td><div class="team-name">Minnesota Timberwolves</div></td>
          <td><div class="team-conf">Western Conference</div></td>
          <td style="text-align:center;"><span class="odds-chip">$126.00</span></td>
        </tr>
      </tbody>
    </table>
    <p style="font-size:11px;color:var(--muted-fg);">Source: Sportsbet &#183; Updated 4 May 2026 &#183; NBA Finals Game 1: 11 June 2026 &#183; Always verify current odds at your bookmaker &#183; 18+ &#183; Bet responsibly.</p>
  </div>

  <div class="section">
    <h2>NBA Championship 2026 &#8212; Analysis</h2>
    <p>Oklahoma City Thunder are a historically short $1.67 favourite &#8212; a price that reflects their position as a confirmed finalist and one of the most dominant teams in the 2025-26 NBA season. At this price, the betting case is straightforward: either you back Thunder to confirm what the market already expects, or you look for value in the opposition.</p>
    <p>San Antonio Spurs at $5.00 is the genuine surprise of the 2026 playoffs. The Spurs have made an improbable Finals run and represent the best value alternative in the market. At $5.00, a Spurs win pays more than three times a Thunder win &#8212; a meaningful difference if you believe this team can compete over a seven-game series.</p>
    <p>New York Knicks ($9.50) are the best-priced Eastern Conference option still in the market. Cleveland Cavaliers and Detroit Pistons share the $17.00 price &#8212; long shots, but the Pistons in particular have been one of the stories of this playoff season.</p>
    <p><strong>Bet365</strong> is the recommended bookmaker for in-play NBA Finals betting &#8212; they offer the deepest live market including quarter-by-quarter and real-time player props once the series begins.</p>
    <p style="font-size:12px;color:var(--muted-fg);font-style:italic;">Analysis is editorial opinion only. Always gamble responsibly. 18+.</p>
  </div>'''

# Replace the odds + analysis sections
html = re.sub(
    r'<div class="section">\s*<h2>NBA Championship 2026 — Current Odds</h2>.*?</div>\s*<div class="section">\s*<h2>NBA Championship 2026 — Analysis</h2>.*?</div>',
    NEW_ODDS_SECTION,
    html, flags=re.DOTALL, count=1
)

# Update meta description with real info
html = html.replace(
    'Current betting markets for the 2026 NBA Finals — top contenders, best odds comparison and where to bet on the NBA in Australia.',
    'NBA Finals 2026 odds — Oklahoma City Thunder $1.67 favourite, San Antonio Spurs $5.00. Game 1: 11 June 2026. Best Australian bookmakers for NBA Finals betting.'
)

# Update hero description
html = html.replace(
    'Current betting markets for the 2026 NBA Championship. Odds comparison, best bets and where to bet on the NBA Finals from Australia.',
    'NBA Finals 2026 — Oklahoma City Thunder ($1.67) vs the field. Game 1 tips off 11 June 2026. Odds comparison and best Australian bookmakers for NBA Finals betting.'
)

# Update date stamp in hero
html = html.replace(
    'Updated May 2026 · NBA Finals June 2026',
    'Updated 4 May 2026 · NBA Finals Game 1: 11 June 2026'
)

with open('nba-championship-odds-2026.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done — NBA odds updated with real Sportsbet data")
