/* One canonical corpus; bounded rendering; publication details load on demand. */
(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const grid = $('jc-grid');
  if (!grid) return;
  const PAGE_SIZE = 20;
  const controls = {q: $('jc-search'), dimension: $('jc-dimension'), era: $('jc-era'), organism: $('jc-organism'), tier: $('jc-tier'), sort: $('jc-sort')};
  const modal = $('jc-prompt-modal');
  let papers = [], matches = [], page = 1, timer, ready = false, minDegree = 0;
  let promptTarget = null, opener = null, promptMode = 'synthesis';
  const chunks = new Map();
  const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;'}[c]));
  const defaults = {q:'', dimension:'all', era:'all', organism:'all', tier:'2000', sort:'year-desc'};
  const base = new URL('.', grid.dataset.indexUrl && new URL(grid.dataset.indexUrl, location.href)).pathname;
  function state() { const p = new URLSearchParams(); Object.entries(controls).forEach(([key, el]) => { if (el.value !== defaults[key]) p.set(key, el.value); }); if (minDegree) p.set('minDegree', minDegree); if (page > 1) p.set('page', page); return p; }
  function restore() {
    const p = new URLSearchParams(location.search);
    Object.entries(controls).forEach(([key, el]) => {
      const value = p.get(key) ?? defaults[key];
      // A multi-era map selection is represented explicitly rather than silently dropped.
      if (key === 'era' && ![...el.options].some(o => o.value === value)) el.add(new Option(value ? 'Map eras: ' + value : 'No eras selected', value));
      el.value = value;
      if (el.tagName === 'SELECT' && el.selectedIndex < 0) el.value = defaults[key];
    });
    minDegree = Math.max(0, Number(p.get('minDegree')) || 0);
    page = Math.max(1, Number.parseInt(p.get('page'), 10) || 1);
  }
  function organismMatch(tags, selected) {
    const values = {drosophila: /fly|drosophila/, 'c-elegans': /elegans|worm|nematode/, mouse: /mouse|rodent|mus/, human: /human|homo|h01/, zebrafish: /zebrafish|danio|fish/, unclassified: /^(none|general)$/};
    return selected === 'all' || tags.some(t => values[selected] ? values[selected].test(t.toLowerCase()) : t.toLowerCase().includes(selected));
  }
  function summary(p) {
    const article = document.createElement('article');
    article.className = 'jc-card'; article.id = 'paper-' + p.id; article.dataset.id = p.id;
    article.innerHTML = '<header class="jc-card-header"><p class="jc-card-meta">' + esc(p.year) + '</p><h3 class="jc-card-title">' + esc(p.title) + '</h3><p class="jc-card-authors">' + esc(p.authors) + '</p><p class="jc-card-journal">' + esc(p.journal) + '</p></header><div class="jc-card-links"><button type="button" class="jc-link" data-details="' + esc(p.id) + '">Read abstract and details</button><button type="button" class="jc-link jc-link-ai-prompt">AI review prompt</button>' + (p.doi ? '<a class="jc-link" href="https://doi.org/' + esc(p.doi) + '" target="_blank" rel="noopener">Open publication</a>' : '') + '<a class="jc-link" href="' + base + 'graph/?paper=' + encodeURIComponent(p.id) + '">Explore citations</a></div>';
    return article;
  }
  function render(writeURL = true) {
    if (!ready) return;
    const q = controls.q.value.trim().toLowerCase();
    const eras = controls.era.value === 'all' ? null : controls.era.value.split(',');
    matches = papers.filter(p => (q || p.tier <= Number(controls.tier.value)) && (controls.dimension.value === 'all' || p.dimension === controls.dimension.value) && (!eras || eras.includes(p.era)) && organismMatch(p.tags, controls.organism.value) && p.degree >= minDegree && (!q || p.search.includes(q)));
    const sort = controls.sort.value;
    matches.sort((a,b) => (sort === 'year-asc' ? a.year-b.year : sort === 'kcore-desc' ? b.kcore-a.kcore : sort === 'dimension' ? a.dimension.localeCompare(b.dimension) : b.year-a.year) || a.title.localeCompare(b.title) || a.id.localeCompare(b.id));
    const totalPages = Math.max(1, Math.ceil(matches.length / PAGE_SIZE));
    page = Math.min(page, totalPages);
    grid.replaceChildren(...matches.slice((page-1)*PAGE_SIZE, page*PAGE_SIZE).map(summary));
    $('jc-empty').classList.toggle('hidden', matches.length > 0);
    $('jc-count').textContent = matches.length + ' of ' + papers.length + ' papers match' + (minDegree ? ' (minimum citation metric: ' + minDegree + ')' : '') + '.';
    $('jc-page-status').textContent = matches.length ? 'Page ' + page + ' of ' + totalPages + ' · ' + Math.min(PAGE_SIZE, matches.length-(page-1)*PAGE_SIZE) + ' shown' : 'No matching results';
    $('jc-prev').disabled = page <= 1; $('jc-next').disabled = page >= totalPages;
    $('jc-prompt-count').textContent = matches.length;
    $('jc-prompt-btn').disabled = !matches.length;
    const params = state();
    $('jc-graph-view').href = base + 'graph/?' + params.toString();
    if (writeURL) history.replaceState(null, '', location.pathname + (params.size ? '?' + params : ''));
  }
  async function details(p, button) {
    if (!p) return;
    button.disabled = true; button.textContent = 'Loading details…';
    try {
      if (!chunks.has(p.chunk)) {
        const request = fetch(grid.dataset.detailBase + p.chunk + '.json?v=' + encodeURIComponent(grid.dataset.version)).then(r => { if (!r.ok) throw new Error('Detail request failed'); return r.json(); }).catch(error => { chunks.delete(p.chunk); throw error; });
        chunks.set(p.chunk, request);
      }
      const chunk = await chunks.get(p.chunk);
      if (typeof chunk[p.id] !== 'string') throw new Error('Paper not in this revision');
      const template = document.createElement('template'); template.innerHTML = chunk[p.id];
      const article = template.content.querySelector('article.jc-card');
      if (!article || article.dataset.id !== p.id) throw new Error('Invalid paper details');
      if (!button.isConnected) return;
      const old = button.closest('.jc-card'); old.replaceWith(article);
      const abstract = article.querySelector('.jc-card-details'); if (abstract) abstract.open = true;
      const title = article.querySelector('h3'); title.tabIndex = -1; title.focus({preventScroll:true});
    } catch (error) {
      button.disabled = false; button.textContent = 'Could not load details. Retry';
    }
  }
  async function jump(id) {
    const p = papers.find(p => p.id === id || p.doi.toLowerCase() === id.toLowerCase());
    if (!p) { $('jc-count').textContent = 'That linked paper is not in this corpus revision. Search by title or DOI.'; return; }
    Object.entries(controls).forEach(([key, el]) => el.value = defaults[key]); minDegree = 0;
    controls.q.value = p.doi || p.title; page = 1; render();
    const params = state(); params.set('paper', p.id); history.replaceState(null, '', location.pathname + '?' + params);
    const article = document.getElementById('paper-' + p.id);
    if (article) { article.scrollIntoView({block:'start'}); await details(p, article.querySelector('[data-details]')); }
  }
  function linkedId() {
    let hash = ''; try { hash = decodeURIComponent(location.hash.replace(/^#paper-/,'')); } catch (_) {}
    return new URLSearchParams(location.search).get('paper') || (location.hash.startsWith('#paper-') ? hash : '');
  }
  function promptPublication(p, i) {
    let text = (i+1) + '. ' + p.title + '\n' + p.authors + ' (' + p.year + '). ' + p.journal + '\n' + (p.doi ? 'https://doi.org/' + p.doi : 'DOI unavailable');
    const pair = p.publication_links;
    if (pair && pair.doi === String(p.doi || '').toLowerCase()) text += '\nPublication relationship: ' + pair.kind + '. Read both sources.\nOriginal paper: ' + pair.original.url + '\nCorrection: ' + pair.correction.url + '\nDo not attribute the original study’s findings to its correction notice.';
    return text;
  }
  function prompt() {
    const selection = promptTarget ? [promptTarget] : matches.slice(0,35);
    const instructions = {synthesis:'Compare the research questions, methods, findings and limitations.', methods:'Compare reported methods and identify differences in validation.', problems:'Identify evidence-supported gaps; label proposed research ideas as hypotheses.', seminar:'Develop discussion questions for a journal-club session.'};
    $('jc-prompt-textarea').value = 'Review these publications using original text where accessible. ' + instructions[promptMode] + '\nThis input contains bibliographic metadata, not full papers or verified summaries. Do not infer findings from titles or tags. State which publications you actually accessed; do not invent quotes, metrics or methods. Distinguish reported results from interpretation and cite evidence.\n\n' + (promptTarget ? 'One selected paper.' : 'First ' + selection.length + ' of ' + matches.length + ' matches in the current sort order; not a representative sample.') + '\n\n' + selection.map(promptPublication).join('\n\n');
    $('jc-prompt-modal-title').textContent = promptTarget ? 'Paper review prompt' : 'Research review prompt';
    $('jc-prompt-modal-desc').textContent = promptTarget ? 'A review prompt using this paper’s recorded metadata. Verify against the publication.' : 'Uses the first ' + selection.length + ' of ' + matches.length + ' matches in the current sort order. No full texts are sent automatically.';
  }
  function openPrompt(target, button) { promptTarget = target; opener = button; prompt(); $('jc-copy-status').classList.add('hidden'); modal.classList.remove('hidden'); $('jc-prompt-close').focus(); }
  function closePrompt() { modal.classList.add('hidden'); if (opener?.isConnected) opener.focus(); }
  $('jc-prompt-btn').addEventListener('click', e => openPrompt(null, e.currentTarget));
  $('jc-prompt-close').addEventListener('click', closePrompt);
  modal.addEventListener('click', e => { if (e.target === modal) closePrompt(); });
  document.addEventListener('keydown', e => {
    if (modal.classList.contains('hidden')) return;
    if (e.key === 'Escape') { e.preventDefault(); closePrompt(); }
    if (e.key === 'Tab') {
      const items = [...modal.querySelectorAll('button,a[href],textarea')].filter(el => !el.disabled && el.getClientRects().length);
      const first = items[0], last = items[items.length-1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });
  modal.querySelectorAll('.jc-pmode-btn').forEach(button => button.addEventListener('click', () => { promptMode=button.dataset.mode; modal.querySelectorAll('.jc-pmode-btn').forEach(b => b.classList.toggle('active', b===button)); prompt(); }));
  $('jc-copy-prompt-btn').addEventListener('click', async () => {
    try { await navigator.clipboard.writeText($('jc-prompt-textarea').value); $('jc-copy-status').textContent='Copied'; }
    catch (_) { $('jc-prompt-textarea').focus(); $('jc-prompt-textarea').select(); $('jc-copy-status').textContent='Copy the selected text manually.'; }
    $('jc-copy-status').classList.remove('hidden');
  });
  grid.addEventListener('click', e => {
    const button = e.target.closest('button[data-details], .jc-link-ai-prompt, .jc-related-link, [data-filter-field]');
    if (!button) return;
    const article = button.closest('.jc-card');
    const p = papers.find(p => p.id === article?.dataset.id);
    if (button.matches('[data-details]')) details(p, button);
    else if (button.matches('.jc-link-ai-prompt')) openPrompt(p, button);
    else if (button.matches('.jc-related-link')) { e.preventDefault(); jump(button.dataset.relatedId); }
    else { (button.dataset.filterField === 'era' ? controls.era : controls.q).value=button.dataset.filterValue; page=1; render(); }
  });
  Object.entries(controls).forEach(([key, el]) => el.addEventListener(key==='q' ? 'input':'change', () => { clearTimeout(timer); timer=setTimeout(() => { page=1; render(); },180); }));
  $('jc-reset').addEventListener('click', () => { clearTimeout(timer); Object.entries(controls).forEach(([key,el]) => el.value=defaults[key]); minDegree=0; page=1; render(); });
  ['prev','next'].forEach(dir => $('jc-'+dir).addEventListener('click', () => { page+=dir==='next'?1:-1; render(); grid.scrollIntoView({block:'start'}); const first=grid.querySelector('h3'); if(first){ first.tabIndex=-1; first.focus({preventScroll:true}); } }));
  window.addEventListener('popstate', () => { restore(); render(false); if(linkedId()) jump(linkedId()); });
  window.addEventListener('hashchange', () => { if(linkedId()) jump(linkedId()); });
  $('jc-prompt-btn').disabled=true;
  fetch(grid.dataset.indexUrl).then(r => { if(!r.ok) throw new Error('Index request failed'); return r.json(); }).then(data => {
    if(!Array.isArray(data) || !data.length) throw new Error('Invalid paper index');
    papers=data.map(p => ({...p, doi:p.doi||'', tags:p.tags||[], degree:Number(p.degree)||0, search:[p.title,p.authors,p.doi,p.journal].join(' ').toLowerCase()}));
    ready=true; const id=linkedId(); restore(); render(); if(id) jump(id);
  }).catch(() => { $('jc-count').textContent='Search could not load. The first 20 papers and publication links remain available. Reload to retry.'; });
})();
