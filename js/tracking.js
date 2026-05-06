/**
 * PuntGuide — Bookmaker Click Tracking
 * Fires a GA4 'bookmaker_click' event on every outbound bookmaker link click.
 *
 * Data captured per click:
 *   bookmaker    — readable name (e.g. "Sportsbet")
 *   source_page  — which page the click came from (e.g. /review-sportsbet)
 *   button_type  — "review_cta", "hub_card", "tips_bet", "compare", "directory"
 *   button_text  — visible text on the button clicked
 */

(function () {
  // Domain → bookmaker name map (generated from affiliate_links.json)
  var BOOKMAKERS = {
    'sportsbet.com.au':       'Sportsbet',
    'pointsbet.com.au':       'PointsBet',
    'betr.com.au':            'betr',
    'nextbet.com.au':         'Nextbet',
    'draftstars.com.au':      'Draftstars',
    'neds.com.au':            'Neds',
    'bet365.com.au':          'Bet365',
    'picklebet.com.au':       'Picklebet',
    'dabble.com.au':          'Dabble',
    'ladbrokes.com.au':       'Ladbrokes',
    'betright.com.au':        'BetRight',
    'betdeluxe.com.au':       'BetDeluxe',
    'puntnow.com.au':         'PuntNow',
    'puntzone.com.au':        'PuntZone',
    'betnation.com.au':       'BetNation',
    'surge.com.au':           'Surge',
    'noisy.com.au':           'Noisy',
    'pulsebet.com.au':        'PulseBet',
    'bigbet.com.au':          'BigBet',
    'mightybet.com.au':       'MightyBet',
    'yesbet.com.au':          'YesBet',
    'betexpress.com.au':      'BetExpress',
    'betjet.com.au':          'BetJet',
    'betzooka.com.au':        'BetZooka',
    'betreal.com.au':         'BetReal',
    'tradie.bet':             'TradieBet',
    'upyago.com.au':          'UpYaGo',
    'next2go.com.au':         'Next2Go',
    'teambet.com.au':         'TeamBet',
    'millenialbet.com.au':    'MillennialBet',
    'betvista.com.au':        'BetVista',
    'puntx.com.au':           'PuntX',
    'betblitz.com.au':        'BetBlitz',
    'unibet.com.au':          'Unibet',
    'blondebet.com.au':       'BlondeBet',
    'betestate.com.au':       'BetEstate',
    'betsupreme.com.au':      'BetSupreme',
    'betaus.com.au':          'BetAus',
    'marantellibet.com.au':   'MarantelliBet',
    'terrybet.com.au':        'TerryBet',
    'topbet.au':              'TopBet',
    'wizbet.com.au':          'WizBet',
    'betyoucan.au':           'BetYouCan',
    'dowbet.com.au':          'DowBet',
    'betchamps.com.au':       'BetChamps',
    'mintbet.au':             'MintBet',
    'betdragon.au':           'BetDragon',
    'ripperbet.au':           'RipperBet',
    'betbuzz.au':             'BetBuzz',
    'betalpha.au':            'BetAlpha',
    'readybet.com.au':        'ReadyBet',
    'betfair.com.au':         'Betfair',
    'betlocal.com.au':        'BetLocal',
    'baggybet.com.au':        'BaggyBet',
    'lightningbet.com.au':    'LightningBet',
    'punt123.bet':            'Punt123',
    'upcoz.com':              'UpCoz',
    'epicodds.com.au':        'EpicOdds',
    'realbookie.com.au':      'RealBookie',
    'betnow.com.au':          'BetNow',
    'betnova.com.au':         'BetNova',
    'ninjabet.com.au':        'NinjaBet',
    'dashbet.com.au':         'DashBet',
    'pandabet.com.au':        'PandaBet',
    'justbet.com.au':         'JustBet',
    'winnersbet.com.au':      'WinnersBet',
    'midasbet.com.au':        'MidasBet',
    'swiftbet.com.au':        'SwiftBet',
    'palmerbet.com':          'Palmerbet',
    'chasebet.com.au':        'ChaseBet',
    'elitebet.com.au':        'EliteBet',
    'vicbet.com.au':          'VicBet',
    'robwaterhouse.com.au':   'Rob Waterhouse',
    'picnicbet.com':          'PicnicBet',
    'okebet.com.au':          'OkeBet',
    'tab.com.au':             'TAB',
    'tabtouch.com.au':        'TABtouch',
    'betgold.com.au':         'BetGold',
    'bossbet.com.au':         'BossBet',
    'wishbet.com.au':         'WishBet',
    'mybet.com.au':           'MyBet',
    'playwestbet.com':        'PlayWest',
    'truebet.com.au':         'TrueBet',
    'starsports.com.au':      'Star Sports',
    'ponybet.com.au':         'PonyBet',
    'allbets.com.au':         'AllBets',
    'betdash.com.au':         'BetDash',
    'betlegends.com.au':      'BetLegends',
    'betit.com.au':           'BetIt',
    'stablebet.com.au':       'StableBet',
    'betshop.com.au':         'BetShop',
    'knucklebet.com.au':      'KnuckleBet',
    'earlycrow.bet':          'EarlyCrow',
    'crownbet.com.au':        'CrownBet',
    'xcelbet.com.au':         'XcelBet',
    'fatbet.com.au':          'FatBet',
    'ballrbet.com.au':        'BallrBet',
    'betfocus.com.au':        'BetFocus',
    'xbet.net.au':            'XBet',
    'premiumbet.com.au':      'PremiumBet',
    'goldenbet888.com.au':    'GoldenBet888',
    'titanbet.com.au':        'TitanBet',
    'chromabet.com.au':       'ChromaBet',
    'bet777.com.au':          'Bet777',
    'templebet.com.au':       'TempleBet',
    'juicybet.com.au':        'JuicyBet',
    'betprofessor.com.au':    'BetProfessor',
    'wellbet.com.au':         'WellBet',
    'questbet.com.au':        'Questbet',
    'betgalaxy.com.au':       'BetGalaxy',
    'betbetbet.net.au':       'BetBetBet',
    'letsbet.net.au':         'LetsBet',
    'havabet.com.au':         'HavaBet',
    'colossalbet.com.au':     'ColossalBet',
    '123bet.com.au':          '123Bet',
    'betmax.com.au':          'BetMax',
    'jimmybet.com.au':        'JimmyBet',
    'goldbet.com.au':         'GoldBet',
    'ultrabet.com.au':        'UltraBet',
    'betkings.com.au':        'BetKings',
    'hotbet.com.au':          'HotBet',
    'boostbet.com.au':        'BoostBet',
    'grsbet.com.au':          'GRSBet',
    'favbet.com.au':          'FavBet',
    'bearbet.com.au':         'BearBet',
    'cashcage.com.au':        'CashCage',
    'multis.com.au':          'Multis',
    'betbox.com.au':          'BetBox',
    'laserbet.com.au':        'LaserBet',
    'puntsport.com.au':       'PuntSport',
  };

  function getDomain(url) {
    try {
      return new URL(url).hostname.replace(/^www\./, '');
    } catch (e) { return null; }
  }

  function getButtonType(el, page) {
    var cls = el.className || '';
    if (page.includes('review-'))   return 'review_cta';
    if (page.includes('compare-'))  return 'compare';
    if (cls.includes('btn-visit'))  return 'directory';
    if (cls.includes('bet-cta'))    return 'tips_bet';
    if (cls.includes('bcta') || cls.includes('card-cta')) return 'hub_card';
    return 'other';
  }

  document.addEventListener('click', function (e) {
    var link = e.target.closest('a[href]');
    if (!link) return;

    var href = link.href;
    if (!href || href.startsWith(window.location.origin)) return;

    var domain = getDomain(href);
    if (!domain) return;

    var bookmaker = BOOKMAKERS[domain];
    if (!bookmaker) return; // not a known bookmaker — ignore

    var page = window.location.pathname;

    if (typeof gtag === 'function') {
      gtag('event', 'bookmaker_click', {
        bookmaker:   bookmaker,
        source_page: page,
        button_type: getButtonType(link, page),
        button_text: link.textContent.trim().substring(0, 50),
      });
    }
  }, { passive: true });
})();
