// Run the actual page script in an isolated DOM/canvas harness against built data.
// This gate exercises drawing, layout geometry and idle-frame scheduling without a browser dependency.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const evidenceApi = require('../assets/js/paper-evidence.js');
const source = fs.readFileSync('technical-training/journal-club/graph.md', 'utf8');
const data = JSON.parse(fs.readFileSync(path.join(process.env.SITE_DIR || '_site', 'technical-training/journal-club/graph-data.json'), 'utf8'));
const script = source.match(/<script>([\s\S]*?)<\/script>/)[1].replace(/\}\)\(\);\s*$/, `
  globalThis.graphTest = {
    state: function () { return { nodes: visibleNodes, edges: visibleEdges, view: view, alpha: alpha, selected: selectedNode, focus: focusedSubgraphNode }; },
    select: selectAndCenterPaper, focus: enterSubgraphFocus, exit: exitSubgraphFocus,
    filter: changeFilters, render: render, resize: resizeCanvas
  };
})();`);

async function harness(corpus = data, failure = false) {
  const frames = [], timers = new Map(), elements = new Map();
  let serial = 0, draws = 0, stack = 0;
  const errors = [];
  const size = { width: 900, height: 650 };
  const context = new Proxy({
    save() { stack++; }, restore() { stack--; },
    clearRect() { draws++; }, measureText(t) { return { width: t.length * 6 }; }
  }, { get(target, key) { return target[key] || (() => {}); } });
  function element(id) {
    if (elements.has(id)) return elements.get(id);
    const classes = new Set();
    const e = {
      id, value: '', checked: false, dataset: {}, style: {}, children: [], listeners: {}, textContent: '',
      classList: { add: c => classes.add(c), remove: c => classes.delete(c), contains: c => classes.has(c), toggle(c, yes) { if (yes) classes.add(c); else classes.delete(c); } },
      addEventListener(type, fn) { (this.listeners[type] ||= []).push(fn); },
      dispatch(type, event = {}) { for (const fn of this.listeners[type] || []) fn(event); },
      appendChild(child) { this.children.push(child); }, replaceChildren() { this.children = []; },
      querySelector() { return null; }, querySelectorAll() { return []; },
      getBoundingClientRect() { return { ...size, left: 0, top: 0 }; },
      getContext() { return context; }, scrollIntoView() {},
    };
    elements.set(id, e);
    return e;
  }
  const tiers = [500, 1000, 2000].map(n => { const e = element('tier-' + n); e.dataset.tier = String(n); return e; });
  const layouts = ['organic', 'cluster', 'timeline'].map(n => { const e = element(n); e.dataset.mode = n; return e; });
  const eras = ['history', 'contemporary', 'sota'].map(n => { const e = element(n); e.value = n; e.checked = true; return e; });
  const groups = { '.jcg-tier-btn': tiers, '.jcg-layout-btn': layouts, '.jcg-era-check': eras };
  for (const id of ['jcg-dimension', 'jcg-organism']) element(id).value = 'all';
  element('jcg-min-degree').value = '0';
  element('jcg-show-edges').checked = true;
  element('jcg-ai-tray').classList.add('collapsed');
  element('jcg-canvas').parentElement = element('canvas-wrap');
  const win = { NTPaperEvidence: evidenceApi, devicePixelRatio: 3, location: { search: '' }, addEventListener() {}, matchMedia() { return { matches: false, addEventListener() {} }; } };
  const sandbox = {
    document: { getElementById: element, querySelectorAll: s => groups[s] || [], createElement: type => element(type + '-' + serial++) },
    window: win, URLSearchParams, CSS: { escape: s => s }, console: { ...console, error(e) { errors.push(String(e)); } },
    ResizeObserver: class { observe() {} },
    fetch: async () => ({ ok: !failure, status: failure ? 503 : 200, json: async () => corpus }),
    requestAnimationFrame(fn) { frames.push(fn); return frames.length; },
    setTimeout(fn) { const id = ++serial; timers.set(id, fn); return id; }, clearTimeout(id) { timers.delete(id); },
  };
  vm.runInNewContext(script, sandbox, { filename: 'paper-graph-page.js' });
  await new Promise(resolve => setImmediate(resolve));
  function drain(max = 1000) { let n = 0; while (frames.length && n++ < max) frames.shift()(); return n; }
  function change(id, value, type = 'change') { element(id).value = value; element(id).dispatch(type); for (const [key, fn] of timers) { timers.delete(key); fn(); } drain(); }
  return { element, tiers, layouts, eras, errors, size, graph: sandbox.graphTest, frames, drain, change, draws: () => draws, stack: () => stack };
}
function separated(nodes) {
  for (let i = 0; i < nodes.length; i++) {
    assert.ok(Number.isFinite(nodes[i].x) && Number.isFinite(nodes[i].y));
    for (let j = i + 1; j < nodes.length; j++) {
      assert.ok(Math.hypot(nodes[i].x - nodes[j].x, nodes[i].y - nodes[j].y) >= nodes[i].radius + nodes[j].radius - 0.01,
        `Overlapping papers: ${[nodes[i].id,nodes[i].dimension,nodes[i].x,nodes[i].y,nodes[i].radius]}, ${[nodes[j].id,nodes[j].dimension,nodes[j].x,nodes[j].y,nodes[j].radius]}`);
    }
  }
}
(async () => {
  const h = await harness();
  h.drain();
  assert.equal(h.graph.state().nodes.length, 2000);
  assert.ok(h.draws() > 0, 'Initial canvas draws');
  assert.equal(h.stack(), 0, 'Canvas save/restore is balanced');
  assert.equal(h.frames.length, 0, 'Default graph stops drawing when idle');
  assert.equal(h.element('jcg-canvas').width, 1800, 'DPR capped at 2');
  for (let i = 0; i < h.tiers.length; i++) {
    h.tiers[i].dispatch('click'); h.drain();
    assert.equal(h.graph.state().nodes.length, [500, 1000, 2000][i]);
    separated(h.graph.state().nodes);
  }
  for (const cat of [...new Set(data.map(p => p.dimension))]) {
    h.change('jcg-dimension', cat);
    assert.equal(h.graph.state().nodes.length, data.filter(p => p.dimension === cat).length);
    assert.ok(h.graph.state().edges.every(e => e.source.dimension === cat && e.target.dimension === cat));
  }
  h.change('jcg-dimension', 'all');
  h.tiers[0].dispatch('click'); h.drain();
  const outside = data.find(p => p.tier === 2000 && p.doi);
  h.change('jcg-search', outside.doi, 'input');
  assert.ok(h.graph.state().nodes.some(p => p.id === outside.id), 'Search covers the full corpus regardless of browse tier');
  h.change('jcg-search', '', 'input');
  h.tiers[2].dispatch('click'); h.drain();
  h.size.width = 280; h.size.height = 360; h.graph.resize(); h.drain();
  separated(h.graph.state().nodes);
  for (const n of h.graph.state().nodes) {
    const v = h.graph.state().view;
    assert.ok(n.x * v.scale + v.tx >= 0 && n.x * v.scale + v.tx <= 280);
    assert.ok(n.y * v.scale + v.ty >= 0 && n.y * v.scale + v.ty <= 360);
  }
  h.size.width = 900; h.size.height = 650; h.graph.resize(); h.drain();
  const organismTokens = { mouse: 'mouse', drosophila: 'fly', human: 'human', 'c-elegans': 'elegans', zebrafish: 'zebrafish', rat: 'rat', macaque: 'macaque', other: 'other', unclassified: 'none' };
  for (const [value, token] of Object.entries(organismTokens)) {
    h.change('jcg-organism', value);
    assert.equal(h.graph.state().nodes.length, data.filter(p => (p.organism || []).includes(token)).length, value);
  }
  h.change('jcg-organism', 'all');
  h.change('jcg-min-degree', '50', 'input');
  assert.equal(h.graph.state().nodes.length, data.filter(p => p.in_degree + p.out_degree >= 50).length);
  h.change('jcg-min-degree', '0', 'input');
  h.eras[0].checked = false; h.eras[0].dispatch('change'); h.graph.filter(); h.drain();
  assert.equal(h.graph.state().nodes.length, data.filter(p => p.era !== 'history').length);
  h.eras.forEach(e => { e.checked = false; }); h.graph.filter(); h.drain();
  assert.equal(h.graph.state().nodes.length, 0);
  assert.equal(h.element('jcg-empty').classList.contains('hidden'), false);
  h.element('jcg-reset').dispatch('click'); h.drain();
  h.tiers[2].dispatch('click'); h.drain();
  h.layouts[2].dispatch('click'); h.drain();
  const state = h.graph.state();
  separated(state.nodes);
  const earliest = state.nodes.reduce((a,b) => a.year < b.year ? a : b);
  const latest = state.nodes.reduce((a,b) => a.year > b.year ? a : b);
  assert.ok(earliest.x < latest.x, 'Timeline uses full 1962–2026 range');
  const before = h.draws();
  h.element('jcg-hud-zoom-in').dispatch('click'); h.drain();
  assert.ok(h.draws() > before, 'Zoom wakes an idle graph');
  h.graph.select(state.nodes[0]); h.drain();
  h.graph.focus(state.nodes[0]); h.drain();
  assert.ok(h.graph.state().nodes.length < 2000);
  h.change('jcg-dimension', 'pipeline');
  assert.equal(h.graph.state().focus, null, 'Changing filters exits focus');
  assert.equal(h.graph.state().nodes.length, data.filter(p => p.dimension === 'pipeline').length);
  h.element('jcg-reset').dispatch('click'); h.drain();
  assert.equal(h.graph.state().selected, null);
  assert.equal(h.graph.state().nodes.length, 2000);
  assert.equal(h.element('jcg-edge-weighting').value, 'sum');
  h.change('jcg-search', 'this query cannot match any paper 9b85fa', 'input');
  assert.equal(h.graph.state().nodes.length, 0);
  assert.equal(h.element('jcg-results-list').children.length, 0);
  h.element('jcg-reset').dispatch('click'); h.drain();
  h.layouts[0].dispatch('click'); h.drain();
  assert.equal(h.frames.length, 0, 'Organic physics eventually sleeps');
  assert.ok(h.graph.state().nodes.every(p => Number.isFinite(p.x) && Number.isFinite(p.y)));
  h.element('jcg-sidebar-reheat').dispatch('click');
  assert.ok(h.frames.length > 0, 'Reheat restarts idle physics'); h.drain();
  const fixtures = [{ id:'fixture', title:'Title', authors:'Author', dimension:'pipeline', organism:['mouse'], tier:500, year:1960, summary:'summaryneedle', abstract:'abstractneedle', ocar:{future_work:'futureneedle'} }];
  const f = await harness(fixtures); f.drain();
  for (const q of ['summaryneedle','abstractneedle','futureneedle','mouse']) { f.change('jcg-search',q,'input'); assert.equal(f.graph.state().nodes.length, 0, 'Navigation metadata/legacy notes must not pollute bibliographic search: ' + q); }
  f.change('jcg-search','AUTHOR','input'); assert.equal(f.graph.state().nodes.length, 1);
  const ratPaper = data.find(p => p.doi === '10.1371/journal.pbio.0030068');
  assert.ok(ratPaper && ratPaper.organism.includes('rat') && !ratPaper.organism.includes('mouse'), 'Rat cortex does not imply mouse');
  h.element('jcg-reset').dispatch('click'); h.drain();
  h.graph.select(h.graph.state().nodes.find(p => p.id === ratPaper.id)); h.drain();
  const card = h.element('jcg-panel-body').innerHTML;
  assert.match(card, /Organism tags: Rat/);
  assert.match(card, /not verified methods, dataset use/);
  assert.ok(!card.includes('MICrONS / Kasthuri / MCP') && !card.includes('High-Pressure Freezing'), 'No guessed dataset or protocol');
  assert.match(card, /Paper abstract/);
  assert.ok(!card.includes('Corpus reading notes') && !card.includes('Opportunity</span>'), 'No legacy annotation drawer');
  assert.ok(evidenceApi.eligible(ratPaper.evidence, ratPaper.doi), 'Reviewed rat paper has DOI-matched evidence');
  assert.match(card, /What this paper demonstrated/);
  assert.ok(card.includes(ratPaper.evidence.contribution), 'Drawer includes the checked contribution');
  // Coverage grows over time: a fixed first paper is no longer an unreviewed fixture.
  const unchecked = data.find(p => !p.evidence);
  assert.ok(unchecked, 'Keep an actual unreviewed-paper case');
  h.graph.select(h.graph.state().nodes.find(p => p.id === unchecked.id)); h.drain();
  assert.match(h.element('jcg-panel-body').innerHTML, /source-checked contribution note is not available/);
  const conflicted = data.find(p => p.doi === '10.18260/1-2--42544');
  assert.ok(conflicted && !conflicted.evidence, 'Unresolved title/DOI conflict stays unpublished');
  assert.deepEqual(h.errors, []);
  const failed = await harness([], true);
  assert.match(failed.element('jcg-count').textContent, /Could not load/);
  assert.equal(failed.errors.length, 1);
  console.log('PASS paper graph: full corpus filters, non-overlapping anchored layouts, canvas rendering, idle/wake, focus/reset, bibliographic-only search and empty state');
})().catch(error => { console.error(error); process.exitCode = 1; });
