(() => {
  const input = document.getElementById('site-search');
  if (!input) return;
  const list = document.getElementById('site-search-results'), status = document.getElementById('site-search-status'), more = document.getElementById('site-search-more');
  let pages = [], limit = 20, timer;
  const fold = s => String(s || '').normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  function render() {
    list.replaceChildren();
    const query = fold(input.value).trim();
    if (!query) { status.textContent = 'Type a topic to search page titles and descriptions.'; more.hidden = true; return; }
    const tokens = query.split(/\s+/);
    const found = pages.filter(p => tokens.every(t => p.search.includes(t))).sort((a,b) => {
      const score = p => (p.titleFold.startsWith(query) ? 100 : 0) + tokens.filter(t => p.titleFold.includes(t)).length * 10;
      return score(b) - score(a) || a.title.localeCompare(b.title);
    });
    status.textContent = found.length ? 'Showing ' + Math.min(limit, found.length) + ' of ' + found.length + ' matching pages.' : 'No pages match. Try fewer words, or choose a resource below.';
    found.slice(0, limit).forEach(p => {
      const li = document.createElement('li'), a = document.createElement('a'), description = document.createElement('p');
      a.href = p.url; a.textContent = p.title;
      li.appendChild(a);
      if (p.status) {
        const badge = document.createElement('span'); badge.className = 'content-status status-' + p.status;
        badge.textContent = { in_development: 'In development', unreviewed: 'Status not confirmed', available: 'Available' }[p.status] || 'Status not confirmed';
        li.appendChild(badge);
      }
      description.textContent = p.description; li.appendChild(description); list.appendChild(li);
    });
    more.hidden = limit >= found.length;
  }
  input.addEventListener('input', () => { clearTimeout(timer); timer = setTimeout(() => { limit = 20; render(); }, 180); });
  more.addEventListener('click', () => { limit += 20; render(); });
  fetch(input.dataset.indexUrl).then(r => { if (!r.ok) throw new Error('Search index unavailable'); return r.json(); }).then(data => {
    pages = data.filter(p => p.title && p.url && p.url.startsWith('/')).map(p => ({ ...p, titleFold: fold(p.title), search: fold(p.title + ' ' + p.description + ' ' + p.keywords) }));
    input.disabled = false;
    input.value = new URLSearchParams(location.search).get('q') || '';
    render();
  }).catch(() => { status.textContent = 'Search is unavailable right now. Use the resource links below.'; });
})();
