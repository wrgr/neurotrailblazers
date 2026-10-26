(() => {
  function revealAnchor() {
    const id = decodeURIComponent(location.hash.slice(1));
    if (!id) return;
    const target = document.getElementById(id);
    if (!target) return;
    for (let parent = target.parentElement; parent; parent = parent.parentElement) {
      if (parent.tagName === 'DETAILS') parent.open = true;
    }
    target.scrollIntoView();
  }
  window.addEventListener('hashchange', revealAnchor);
  revealAnchor();
  const main = document.querySelector('#main-content');
  if (!main || main.querySelector('.home-refresh, .start-guide, .jcg-page, #jc-grid, #dict-search')) return;
  const headings = [...main.querySelectorAll('h2')].filter(h => !h.closest('details, .card, .pathfinder-panel, .arch-card'));
  if (headings.length < 3) return;
  const outline = document.createElement('details');
  outline.className = 'page-outline';
  const summary = document.createElement('summary');
  summary.textContent = 'On this page';
  outline.appendChild(summary);
  const nav = document.createElement('nav');
  nav.setAttribute('aria-label', 'On this page');
  const list = document.createElement('ul');
  headings.forEach((h, i) => {
    if (!h.id) {
      const base = h.textContent.trim().toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || 'section';
      let id = base, n = 2;
      while (document.getElementById(id)) id = base + '-' + n++;
      h.id = id;
    }
    const item = document.createElement('li');
    const a = document.createElement('a');
    a.href = '#' + h.id;
    a.textContent = h.textContent.trim();
    a.addEventListener('click', () => { outline.open = false; });
    item.appendChild(a); list.appendChild(item);
  });
  nav.appendChild(list); outline.appendChild(nav);
  const target = headings[0].closest('section') || headings[0];
  target.before(outline);
})();
