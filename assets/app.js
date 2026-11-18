(function () {
  var root = document.body.getAttribute('data-root') || '';
  var $ = function (s, el) { return (el || document).querySelector(s); };
  var $$ = function (s, el) { return Array.prototype.slice.call((el || document).querySelectorAll(s)); };

  // ---- scrolled state + back-to-top ----
  var totop = $('#totop');
  // Runs at most once per frame and only touches the page when a state actually changes.
  var wasScrolled = null, wasTop = null, ticking = false;
  function onScroll() {
    ticking = false;
    var y = window.scrollY, sc = y > 160, top = y < 600;
    if (sc !== wasScrolled) { document.body.classList.toggle('scrolled', sc); wasScrolled = sc; }
    if (totop && top !== wasTop) { totop.hidden = top; wasTop = top; }
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
  }, { passive: true }); onScroll();
  if (totop) totop.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });

  // ---- sections: collapsed on phones except first two ----
  var secs = $$('details.sec');
  if (window.innerWidth < 700) secs.forEach(function (d, i) { if (i > 1) d.removeAttribute('open'); });
  var tog = $('#toggleall');
  function syncTog() { if (tog) tog.textContent = secs.every(function (d) { return d.open; }) ? '⇕ Collapse all' : '⇕ Expand all'; }
  if (tog) tog.addEventListener('click', function () {
    var openAll = !secs.every(function (d) { return d.open; });
    secs.forEach(function (d) { d.open = openAll; }); syncTog();
  });
  secs.forEach(function (d) { d.addEventListener('toggle', syncTog); }); syncTog();

  // open a section when jumped to
  function openTarget(id) {
    var el = document.getElementById(id); if (!el) return;
    if (el.tagName === 'DETAILS') el.open = true;
    setTimeout(function () { el.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 30);
  }
  $$('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var id = a.getAttribute('href').slice(1); if (!id) return;
      e.preventDefault(); closeAll(); openTarget(id);
    });
  });

  // highlight current chip
  // Important: never call scrollIntoView() here. It runs during the user's swipe and on
  // phones it stops the page's momentum at every section ("sticky" scrolling).
  // We move only the chip bar sideways, and only when the active chip is off-screen.
  var chips = $$('#chips a.chip'), bar = $('#chips'), current = null;
  function showChip(c) {
    if (!bar) return;
    var left = c.offsetLeft, right = left + c.offsetWidth;
    if (left < bar.scrollLeft || right > bar.scrollLeft + bar.clientWidth) {
      bar.scrollLeft = left - (bar.clientWidth - c.offsetWidth) / 2;
    }
  }
  if (chips.length && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (ents) {
      ents.forEach(function (en) {
        if (!en.isIntersecting || en.target.id === current) return;
        current = en.target.id;
        chips.forEach(function (c) {
          var on = c.getAttribute('href') === '#' + current; c.classList.toggle('on', on);
          if (on) showChip(c);
        });
      });
    }, { rootMargin: '-120px 0px -65% 0px' });
    secs.forEach(function (s) { io.observe(s); });
  }

  // ---- tabs ----
  $$('.tabs').forEach(function (t) {
    $$('.tab', t).forEach(function (b) {
      b.addEventListener('click', function () {
        $$('.tab', t).forEach(function (x) { x.classList.remove('on'); });
        $$('.pane', t).forEach(function (x) { x.classList.remove('on'); });
        b.classList.add('on'); var p = document.getElementById(b.getAttribute('data-t')); if (p) p.classList.add('on');
      });
    });
  });

  // ---- overlays ----
  var search = $('#search'), sheet = $('#tocsheet');
  function closeAll() { if (search) search.hidden = true; if (sheet) sheet.hidden = true; document.body.style.overflow = ''; }
  $$('.sclose').forEach(function (b) { b.addEventListener('click', closeAll); });
  [search, sheet].forEach(function (o) { if (o) o.addEventListener('click', function (e) { if (e.target === o) closeAll(); }); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeAll();
    if (e.key === '/' && document.activeElement.tagName !== 'INPUT') { e.preventDefault(); openSearch(); }
  });
  var tocbtn = $('#tocbtn');
  if (tocbtn && sheet) tocbtn.addEventListener('click', function () { sheet.hidden = false; document.body.style.overflow = 'hidden'; });

  // ---- search ----
  var q = $('#q'), res = $('#sres'), IDX = window.HB_INDEX || [];
  function openSearch() { search.hidden = false; document.body.style.overflow = 'hidden'; q.value = ''; render(''); setTimeout(function () { q.focus(); }, 20); }
  ['#sbtn', '#sbtn2'].forEach(function (s) { var b = $(s); if (b) b.addEventListener('click', openSearch); });
  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function norm(s) { return (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); }
  function render(term) {
    var t = norm(term.trim()), words = t.split(/\s+/).filter(Boolean), out = [];
    if (!words.length) {
      out = IDX.filter(function (d) { return d.s !== 'Tools'; }).slice(0, 8).map(function (d) { return { d: d, snip: d.s }; });
    } else {
      IDX.forEach(function (d) {
        var title = norm(d.t), keys = norm(d.k + ' ' + d.h), body = norm(d.x), score = 0, ok = true;
        words.forEach(function (w) {
          var s = 0;
          if (title.indexOf(w) > -1) s += 10;
          if (keys.indexOf(w) > -1) s += 4;
          if (body.indexOf(w) > -1) s += 1;
          if (!s) ok = false; score += s;
        });
        if (ok) {
          var i = body.indexOf(words[0]), snip = d.s;
          if (i > -1) { snip = d.x.substr(Math.max(0, i - 50), 130); }
          out.push({ d: d, score: score, snip: snip });
        }
      });
      out.sort(function (a, b) { return b.score - a.score; });
    }
    res.innerHTML = out.slice(0, 20).map(function (r, n) {
      var sn = esc(r.snip);
      words.forEach(function (w) { if (w.length > 1) sn = sn.replace(new RegExp('(' + w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig'), '<mark>$1</mark>'); });
      return '<li><a href="' + root + r.d.u + '"' + (n === 0 ? ' class="sel"' : '') + '><span class="re">' + r.d.e + '</span><span><b>' + esc(r.d.t) + '</b><small>' + esc(r.d.s) + ' · ' + sn + '</small></span></a></li>';
    }).join('') || '<li style="padding:14px;color:var(--mute)">No match yet. Try another word. 🧐</li>';
  }
  if (q) {
    q.addEventListener('input', function () { render(q.value); });
    q.addEventListener('keydown', function (e) { if (e.key === 'Enter') { var a = $('#sres a.sel'); if (a) location.href = a.href; } });
  }
})();
