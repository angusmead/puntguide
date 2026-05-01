(function () {
  // ─── NAV DATA ─────────────────────────────────────────────────────────────
  const NAV = [
    {
      label: '🏆 Best Betting Sites',
      links: [
        { text: 'Best Betting Sites Australia', href: '/best-betting-sites-australia.html' },
        { text: 'Top Betting Sites Australia',  href: '/top-betting-sites-australia.html' },
        { text: 'Compare Betting Sites',        href: '/compare-betting-sites.html' },
        { text: 'Best Betting Apps',            href: '/best-betting-apps-australia.html' },
        { text: 'Fastest Payouts',              href: '/fastest-payout-betting-sites-australia.html' },
        { text: 'Fastest Withdrawals',          href: '/fastest-withdrawal-betting-sites-australia.html' },
        { text: 'New Betting Sites 2026',       href: '/new-betting-sites-australia.html' },
      ]
    },
    {
      label: '🏈 AFL',
      links: [
        { text: 'AFL Tips 2026',               href: '/afl-tips.html' },
        { text: 'AFL Round 8 Tips 2026',        href: '/afl-round-8-tips-2026.html' },
        { text: 'AFL Premiership Odds 2026',    href: '/afl-premiership-odds-2026.html' },
        { text: 'Brownlow Medal Odds 2026',     href: '/brownlow-medal-odds-2026.html' },
        { text: 'Coleman Medal Odds 2026',      href: '/afl-coleman-medal-odds-2026.html' },
        { text: 'Rising Star Odds 2026',         href: '/afl-rising-star-odds-2026.html' },
        { text: 'Best Sites for AFL & NRL',     href: '/best-betting-sites-afl-nrl.html' },
        { text: 'Best Sites for AFL',           href: '/best-betting-sites-for-afl.html' },
      ]
    },
    {
      label: '🏉 NRL',
      links: [
        { text: 'NRL Tips 2026',               href: '/nrl-tips.html' },
        { text: 'NRL Round 9 Tips 2026',        href: '/nrl-round-10-tips-2026.html' },
        { text: 'NRL Premiership Odds 2026',    href: '/nrl-premiership-odds-2026.html' },
        { text: 'Best Sites for AFL & NRL',     href: '/best-betting-sites-afl-nrl.html' },
      ]
    },
    {
      label: '🏇 Racing',
      links: [
        { text: 'Racing Weekend Tips',          href: '/racing-weekend-may2-2026.html' },
        { text: 'Racing Futures 2026',          href: '/racing-futures-2026.html' },
        { text: 'Best Sites for Racing',        href: '/best-betting-sites-for-racing.html' },
      ]
    },
    {
      label: '📋 Bookmakers',
      links: [
        { text: 'All 130 Bookmakers',           href: '/all-betting-sites.html' },
        { text: 'Bookmakers Australia',         href: '/bookmakers-australia.html' },
        { text: 'Online Betting Australia',     href: '/online-betting-australia.html' },
        { text: 'Sports Betting Sites',         href: '/sports-betting-sites-australia.html' },
        { text: 'No Deposit Betting Sites',     href: '/no-deposit-betting-sites.html' },
        { text: 'Live Betting Australia',       href: '/live-betting-australia.html' },
      ]
    },
    {
      label: '⚾ International Sports',
      links: [
        { text: 'NFL Super Bowl LXI Odds',    href: '/nfl-super-bowl-odds-2026.html' },
        { text: 'MLB World Series Odds 2026', href: '/mlb-world-series-odds-2026.html' },
        { text: 'Bet365 Review (Best for MLB)', href: '/review-bet365.html' },
      ]
    },
    {
      label: '🔍 Reviews & Comparisons',
      links: [
        { text: 'PointsBet Review',             href: '/review-pointsbet.html' },
        { text: 'Sportsbet Review',             href: '/review-sportsbet.html' },
        { text: 'Ladbrokes Review',             href: '/review-ladbrokes.html' },
        { text: 'BetRight Review',              href: '/review-betright.html' },
        { text: 'Dabble Review',                href: '/review-dabble.html' },
        { text: 'PointsBet vs Sportsbet',       href: '/compare-pointsbet-vs-sportsbet.html' },
        { text: 'Sportsbet vs Ladbrokes',       href: '/compare-sportsbet-vs-ladbrokes.html' },
        { text: 'All Bookmaker Reviews →',      href: '/bookmakers-australia.html' },
      ]
    },
  ];

  // ─── CSS ──────────────────────────────────────────────────────────────────
  const style = document.createElement('style');
  style.textContent = `
    .pg-hamburger {
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 5px;
      width: 36px;
      height: 36px;
      padding: 6px;
      background: none;
      border: none;
      cursor: pointer;
      flex-shrink: 0;
      border-radius: 8px;
      transition: background 0.15s;
      order: -1;
    }
    .pg-hamburger:hover { background: hsl(205 40% 90%); }
    .pg-hamburger span {
      display: block;
      height: 2px;
      background: hsl(215 45% 16%);
      border-radius: 2px;
      transition: all 0.25s;
      transform-origin: center;
    }
    .pg-hamburger.open span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
    .pg-hamburger.open span:nth-child(2) { opacity: 0; transform: scaleX(0); }
    .pg-hamburger.open span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }

    .pg-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.45);
      z-index: 998;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s;
      backdrop-filter: blur(2px);
    }
    .pg-overlay.open { opacity: 1; pointer-events: all; }

    .pg-drawer {
      position: fixed;
      top: 0;
      left: 0;
      bottom: 0;
      width: 300px;
      max-width: 85vw;
      background: #fff;
      z-index: 999;
      transform: translateX(-100%);
      transition: transform 0.3s cubic-bezier(0.16,1,0.3,1);
      display: flex;
      flex-direction: column;
      box-shadow: 4px 0 32px rgba(0,0,0,0.12);
      overflow: hidden;
    }
    .pg-drawer.open { transform: translateX(0); }

    .pg-drawer-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 16px 20px;
      background: hsl(215 45% 16%);
      flex-shrink: 0;
    }
    .pg-drawer-logo {
      height: 40px;
      width: auto;
      filter: brightness(0) invert(1);
      opacity: 0.9;
    }
    .pg-drawer-close {
      background: rgba(255,255,255,0.12);
      border: none;
      color: #fff;
      font-size: 20px;
      width: 32px;
      height: 32px;
      border-radius: 6px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      line-height: 1;
      transition: background 0.15s;
    }
    .pg-drawer-close:hover { background: rgba(255,255,255,0.2); }

    .pg-drawer-body {
      flex: 1;
      overflow-y: auto;
      padding: 8px 0 32px;
    }
    .pg-drawer-body::-webkit-scrollbar { width: 4px; }
    .pg-drawer-body::-webkit-scrollbar-track { background: transparent; }
    .pg-drawer-body::-webkit-scrollbar-thumb { background: hsl(205 40% 86%); border-radius: 2px; }

    .pg-section { margin-bottom: 4px; }
    .pg-section-btn {
      width: 100%;
      text-align: left;
      background: none;
      border: none;
      padding: 10px 20px;
      font-family: 'Geist', 'Inter Tight', sans-serif;
      font-size: 13px;
      font-weight: 700;
      color: hsl(215 45% 16%);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: background 0.12s;
      letter-spacing: -0.01em;
    }
    .pg-section-btn:hover { background: hsl(205 60% 96%); }
    .pg-section-btn .pg-chevron {
      font-size: 11px;
      color: hsl(215 20% 55%);
      transition: transform 0.2s;
      margin-left: 8px;
    }
    .pg-section-btn.open .pg-chevron { transform: rotate(180deg); }

    .pg-links {
      display: none;
      flex-direction: column;
      padding: 2px 0 6px;
    }
    .pg-links.open { display: flex; }
    .pg-links a {
      padding: 8px 20px 8px 32px;
      font-size: 13px;
      color: hsl(215 45% 16% / 0.75);
      text-decoration: none;
      transition: color 0.12s, background 0.12s;
      display: block;
    }
    .pg-links a:hover {
      color: hsl(215 45% 16%);
      background: hsl(205 60% 96%);
    }

    .pg-drawer-footer {
      padding: 16px 20px;
      border-top: 1px solid hsl(205 40% 90%);
      background: hsl(205 60% 98%);
      flex-shrink: 0;
    }
    .pg-drawer-footer a {
      display: block;
      text-align: center;
      background: linear-gradient(135deg, hsl(50 96% 72%), hsl(44 92% 60%));
      color: hsl(215 45% 16%);
      font-weight: 700;
      font-size: 13px;
      padding: 10px;
      border-radius: 10px;
      text-decoration: none;
      box-shadow: 0 4px 12px hsl(48 92% 54% / 0.35);
    }

    @media (min-width: 769px) {
      .pg-hamburger { margin-right: 8px; }
    }
  `;
  document.head.appendChild(style);

  // ─── HTML ─────────────────────────────────────────────────────────────────
  const overlay = document.createElement('div');
  overlay.className = 'pg-overlay';
  document.body.appendChild(overlay);

  const drawer = document.createElement('div');
  drawer.className = 'pg-drawer';
  drawer.setAttribute('aria-label', 'Site navigation');

  const sectionsHtml = NAV.map((cat, i) => `
    <div class="pg-section">
      <button class="pg-section-btn" data-idx="${i}" aria-expanded="false">
        ${cat.label} <span class="pg-chevron">▾</span>
      </button>
      <div class="pg-links" id="pg-links-${i}">
        ${cat.links.map(l => `<a href="${l.href}">${l.text}</a>`).join('')}
      </div>
    </div>
  `).join('');

  drawer.innerHTML = `
    <div class="pg-drawer-head">
      <img src="/puntguide-logo.png" alt="PuntGuide" class="pg-drawer-logo">
      <button class="pg-drawer-close" aria-label="Close menu">✕</button>
    </div>
    <div class="pg-drawer-body">${sectionsHtml}</div>
    <div class="pg-drawer-footer">
      <a href="/all-betting-sites.html">Bet Now — View All 130 Bookmakers →</a>
    </div>
  `;
  document.body.appendChild(drawer);

  // ─── HAMBURGER BUTTON ─────────────────────────────────────────────────────
  const btn = document.createElement('button');
  btn.className = 'pg-hamburger';
  btn.setAttribute('aria-label', 'Open navigation menu');
  btn.setAttribute('aria-expanded', 'false');
  btn.innerHTML = '<span></span><span></span><span></span>';

  const nav = document.querySelector('.nav, header .nav-inner, header');
  if (nav) nav.prepend(btn);

  // ─── LOGIC ────────────────────────────────────────────────────────────────
  function open() {
    drawer.classList.add('open');
    overlay.classList.add('open');
    btn.classList.add('open');
    btn.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }
  function close() {
    drawer.classList.remove('open');
    overlay.classList.remove('open');
    btn.classList.remove('open');
    btn.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  btn.addEventListener('click', () => drawer.classList.contains('open') ? close() : open());
  overlay.addEventListener('click', close);
  drawer.querySelector('.pg-drawer-close').addEventListener('click', close);
  document.addEventListener('keydown', e => e.key === 'Escape' && close());

  // Section toggles
  drawer.querySelectorAll('.pg-section-btn').forEach(secBtn => {
    secBtn.addEventListener('click', function () {
      const idx = this.dataset.idx;
      const links = document.getElementById(`pg-links-${idx}`);
      const isOpen = links.classList.contains('open');
      // Close all
      drawer.querySelectorAll('.pg-links').forEach(l => l.classList.remove('open'));
      drawer.querySelectorAll('.pg-section-btn').forEach(b => { b.classList.remove('open'); b.setAttribute('aria-expanded','false'); });
      // Open clicked if it was closed
      if (!isOpen) {
        links.classList.add('open');
        this.classList.add('open');
        this.setAttribute('aria-expanded','true');
      }
    });
  });

  // Auto-open the section containing the current page
  const current = window.location.pathname.split('/').pop() || 'index.html';
  NAV.forEach((cat, i) => {
    if (cat.links.some(l => l.href.includes(current))) {
      document.getElementById(`pg-links-${i}`)?.classList.add('open');
      drawer.querySelector(`[data-idx="${i}"]`)?.classList.add('open');
    }
  });
})();
