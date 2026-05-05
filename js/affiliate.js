/**
 * PuntGuide Affiliate Link Router
 *
 * How it works:
 *   1. Reads /data/affiliate_links.json
 *   2. Detects the current bookmaker from the page URL (e.g. review-sportsbet.html → "sportsbet")
 *   3. If that bookmaker has a live affiliate_url, rewrites all primary CTA buttons to use it
 *
 * To activate a bookmaker's affiliate link:
 *   - Open data/affiliate_links.json
 *   - Set "affiliate_url" to the tracking URL from Commission Factory or the direct program
 *   - Change "status" to "live"
 *   - That's it — no HTML changes needed
 */

(function () {
  // Detect bookmaker slug from current page URL
  function getSlug() {
    var path = window.location.pathname;
    var match = path.match(/review-([^/.]+)/);
    return match ? match[1] : null;
  }

  var slug = getSlug();
  if (!slug) return; // Not a review page — nothing to do

  // Fetch the affiliate registry
  fetch('/data/affiliate_links.json')
    .then(function (r) { return r.json(); })
    .then(function (data) {
      var bm = data[slug];
      if (!bm || bm.status !== 'live' || !bm.affiliate_url) return;

      var url = bm.affiliate_url;

      // Wire up all primary CTA buttons on this page
      document.querySelectorAll('a.btn-g, a.bet-cta, a.bcta').forEach(function (el) {
        // Only update placeholder links (href="#" or href pointing to internal pages)
        var href = el.getAttribute('href') || '';
        if (href === '#' || href.startsWith('/') || href === '') {
          el.href = url;
          el.target = '_blank';
          el.rel = 'noopener sponsored';
        }
      });
    })
    .catch(function () {
      // Silently fail — affiliate links just stay as-is if JSON can't be fetched
    });
})();
