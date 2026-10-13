from pathlib import Path
import re
R=Path('.')
def edit(path,old,new):
 p=R/path; s=p.read_text(); assert old in s,(path,old[:90]); p.write_text(s.replace(old,new))
def write(path,s):
 p=R/path; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(s)
edit('_data/navigation.yml','      - title: "Longer learning paths"\n        url: "/tracks/"\n','')
edit('_data/navigation.yml','      - title: "Find papers and citations"\n        url: "/technical-training/journal-club/graph/"','      - title: "Find research papers"\n        url: "/technical-training/journal-club/"')
for path in ['index.html','resources/index.md']:
 edit(path,"'/technical-training/journal-club/graph/'", "'/technical-training/journal-club/'")
p=R/'teaching/index.md'; s=p.read_text(); a=s.index('<section class="section"><h2>Materials by module</h2>'); b=s.index('</section>',a)+len('</section>'); p.write_text(s[:a]+s[b:])
edit('teaching/sessions/index.md','<div class="cards-grid">','''<div class="resource-search"><label for="session-search">Find a session by topic</label><input type="search" id="session-search" placeholder="e.g. synapse, Python, research" aria-controls="session-results"><label for="session-status">Development status</label><select id="session-status"><option value="all">All statuses</option><option value="available">Available</option><option value="in_development">In development</option><option value="unreviewed">Status not confirmed</option></select><p id="session-count" role="status" aria-live="polite"></p></div>
<div class="cards-grid" id="session-results">''')
edit('teaching/sessions/index.md','  <article class="card">','  {% include ui/module-status-value.html item=p %}\n  <article class="card session-card" data-status="{{ module_state }}">')
edit('assets/js/module-interactives.js',"var checks = Array.from(root.querySelectorAll('.nt-progress-step'));\n    if (!checks.length) return;", "var checks = Array.from(root.querySelectorAll('.nt-progress-step:not([data-assessment])'));\n    if (!checks.length) return;")
edit('assets/js/module-interactives.js',"if (text) text.textContent = pct + '% complete';", """if (text) text.textContent = pct + '% of self-reported activities checked';
    if (bar) bar.setAttribute('aria-label', 'Self-reported activity progress');
    root.querySelectorAll('[data-assessment]').forEach(function (el) {
      el.checked = root.getAttribute('data-' + el.dataset.assessment + '-passed') === 'true';
    });
    var result = root.querySelector('.nt-assessment-status');
    if (result) result.textContent = root.querySelector('.nt-quiz-submit')
      ? (root.getAttribute('data-quiz-passed') === 'true' ? 'Checkpoint: passed in this browser.' : 'Checkpoint: not yet passed.')
      : 'Checkpoint: not available for this module.';""")
edit('_includes/ui/module-interactive-lab.html','<h3 class="card-title">Progress Tracker</h3>','<h3 class="card-title">Activity progress (self-reported)</h3>')
edit('_includes/ui/module-interactive-lab.html','<input type="checkbox" class="nt-progress-step" data-step-index="{{ forloop.index0 }}">','''<input type="checkbox" class="nt-progress-step" data-step-index="{{ forloop.index0 }}"{% if forloop.index0 == 3 %} data-assessment="quiz" disabled{% elsif forloop.index0 == 4 %} data-assessment="task" disabled{% elsif forloop.index0 == 5 %} data-assessment="annotation" disabled{% endif %}>''')
edit('_includes/ui/module-interactive-lab.html','<p class="nt-progress-text">0% complete</p>','''<p class="nt-progress-text">0% of self-reported activities checked</p><p class="nt-assessment-status" role="status" aria-live="polite">{% if module_data.quiz %}Checkpoint: not yet passed.{% else %}Checkpoint: not available for this module.{% endif %}</p><p>Scored items update from your answers, not from checkboxes. Compare your work with the lesson rubric: this tracker does not certify proficiency.</p>''')
edit('technical-training/journal-club/graph.md','  <h1>Papers and citations</h1>', '''  <h1>Papers and citations</h1><nav class="paper-view-links" aria-label="Paper view"><a id="jcg-list-view" href="{{ '/technical-training/journal-club/' | relative_url }}">Paper list</a><span aria-current="page">Citation map</span></nav>''')
edit('technical-training/journal-club/graph.md','>Journal club card</a>', '>Paper details and reading notes</a>')
edit('technical-training/journal-club/graph.md',"    var fullCardUrl = JC_BASE_URL + '#paper-' + encodeURIComponent(p.id);", "    var fullCardUrl = JC_BASE_URL + '?paper=' + encodeURIComponent(p.id);")
edit('technical-training/journal-club/graph.md',"    panel.classList.remove('hidden');\n    var tierLabel", "    if (panel.classList.contains('hidden')) drawerReturnFocus = document.activeElement;\n    panel.classList.remove('hidden');\n    if (panelClose.focus) panelClose.focus({ preventScroll: true });\n    var tierLabel")
edit('technical-training/journal-club/graph.md',"  panelClose.addEventListener('click', function () {\n    panel.classList.add('hidden');\n    selectedNode = null;\n    wakeAnimation();\n  });", """  var drawerReturnFocus = null;
  panelClose.addEventListener('click', function () {
    panel.classList.add('hidden'); selectedNode = null; wakeAnimation();
    if (drawerReturnFocus && drawerReturnFocus.isConnected && drawerReturnFocus.focus) drawerReturnFocus.focus({ preventScroll: true });
  });
  window.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && !panel.classList.contains('hidden')) {
      event.preventDefault(); panelClose.click();
    }
  });""")
edit('technical-training/journal-club/graph.md', "function () { selectAndCenterPaper(p); canvas.scrollIntoView({ block: 'center', behavior: 'smooth' }); }", "function () { selectAndCenterPaper(p); }")
edit('technical-training/journal-club/graph.md',"    applyFilters();\n    fitView();\n\n    if (params.has('paper'))", """    if (params.has('q')) searchEl.value = params.get('q');
    if (params.has('organism') && organismEl.querySelector('option[value="' + CSS.escape(params.get('organism')) + '"]')) organismEl.value = params.get('organism');
    if (params.has('era')) eraChecks.forEach(function (el) { el.checked = params.get('era').split(',').indexOf(el.value) !== -1; });
    if (params.has('minDegree')) degreeEl.value = Math.max(0, parseInt(params.get('minDegree'), 10) || 0);
    applyFilters();
    fitView();

    if (params.has('paper'))""")
edit('technical-training/journal-club/graph.md',"    countEl.textContent = visibleNodes.length + ' papers (' + visibleEdges.length + ' citation links)';", """    var shared = new URLSearchParams();
    if (query) shared.set('q', query);
    if (selectedCat !== 'all') shared.set('dimension', selectedCat);
    if (selectedOrg !== 'all') shared.set('organism', selectedOrg);
    if (activeEras.length !== eraChecks.length) shared.set('era', activeEras.join(','));
    if (minDeg > 0) shared.set('minDegree', minDeg);
    shared.set('tier', String(currentTier));
    var listView = document.getElementById('jcg-list-view');
    if (listView) listView.href = JC_BASE_URL + '?' + shared.toString();
    countEl.textContent = visibleNodes.length + ' papers (' + visibleEdges.length + ' citation links)';""")
p=R/'assets/css/usability.css'; s=p.read_text().replace('.home-refresh .btn-secondary { color: #d8f4f2; border-color: #7aabae; }', '.home-refresh .hero .btn-secondary { color: #fff; background: #174752; border-color: #b8dfdf; }\n.home-refresh .hero .btn-secondary:hover, .home-refresh .hero .btn-secondary:focus-visible { color: #fff; background: #11343e; }'); p.write_text(s)
write('technical-training/journal-club/index-data.json', '''---
layout: null
permalink: /technical-training/journal-club/index-data.json
sitemap: false
---
[{%- for p in site.data.journal_papers.papers -%}
{"id":{{ p.id | jsonify }},"title":{{ p.title | jsonify }},"authors":{{ p.authors | jsonify }},"year":{{ p.year | jsonify }},"journal":{{ p.journal | jsonify }},"doi":{{ p.doi | jsonify }},"dimension":{{ p.dimension | jsonify }},"era":{{ p.inclusion_role | jsonify }},"tier":{{ p.tier | default: 2000 | jsonify }},"kcore":{{ p.k_core | default: 0 | jsonify }},"degree":{{ p.in_degree | plus: p.out_degree | jsonify }},"tags":{{ p.tags | jsonify }},"chunk":{{ forloop.index0 | divided_by: 100 }}}{% unless forloop.last %},{% endunless %}
{%- endfor -%}]
''')
write('_includes/data/paper-detail-chunk.json','''{%- assign offset = page.chunk | times: 100 -%}
{%- assign papers = site.data.journal_papers.papers | slice: offset, 100 -%}
{ {% for paper in papers %}{% capture card %}{% include cards/journal-paper-card.html paper=paper %}{% endcapture %}{{ paper.id | jsonify }}:{{ card | jsonify }}{% unless forloop.last %},{% endunless %}{% endfor %} }
''')
for i in range(20):
 write(f'technical-training/journal-club/details/{i}.json',f'---\nlayout: null\nsitemap: false\nchunk: {i}\n---\n{{% include data/paper-detail-chunk.json %}}\n')
p=R/'technical-training/journal-club/index.md'; s=p.read_text(); s=s[:s.index('<script>')]; s=s.replace('title: "Journal club reading list"','title: "Research papers"').replace('<h1>Journal club reading list</h1>','<h1>Research papers</h1>'); s=s.replace('description: "Browse the full connectomics paper collection — filter by expertise level, dimension, era, or keyword, or explore it as a citation graph. Each paper presented with the OCAR framework — Opportunity, Challenge, Action, Resolution, and Future Work."','description: "Search connectomics papers by title, author, DOI, topic, or organism. Open an abstract and optional reading notes, or switch to the citation map."'); s=s.replace('Search {{ site.data.journal_papers.papers.size }} papers by title, author, or topic.', 'Search {{ site.data.journal_papers.papers.size }} papers by title, author, DOI, or topic. This is the research corpus, not a separately curated journal-club selection.'); s=s.replace('class="jc-graph-cta"','id="jc-graph-view" class="jc-graph-cta"');
pos=s.index('    <label for="jc-era">'); s=s[:pos]+'''    <label for="jc-organism">Organism:</label><select id="jc-organism"><option value="all">All organisms</option><option value="mouse">Mouse</option><option value="drosophila">Drosophila</option><option value="human">Human</option><option value="c-elegans">C. elegans</option><option value="zebrafish">Zebrafish</option><option value="rat">Rat</option><option value="macaque">Macaque</option><option value="other">Other tagged systems</option><option value="unclassified">Not tagged / general</option></select>
'''+s[pos:]
s=s.replace('    <span class="jc-filter-count" id="jc-count"></span>','    <button type="button" id="jc-reset" class="btn btn-secondary">Clear filters</button><span class="jc-filter-count" id="jc-count" role="status" aria-live="polite">Loading search; the first 20 papers are available below.</span>')
a=s.index('  <p class="jc-shown-note">'); b=s.index('\n  <div class="jc-grid"',a); s=s[:a]+'''  <p class="jc-shown-note" id="jc-shown-note">Search covers the full corpus regardless of browse subset; topic and organism filters still apply. Abstracts are publication text recorded in the corpus; reading notes are site-added and unverified.</p>
  <noscript><p>JavaScript is off: the first 20 papers are shown. For the complete catalog, <a href="{{ '/technical-training/journal-club/index-data.json' | relative_url }}">open the compact paper index</a>.</p></noscript>
'''+s[b:]
s=s.replace('<div class="jc-grid" id="jc-grid">', '<div class="jc-grid" id="jc-grid" data-index-url="{{ \'/technical-training/journal-club/index-data.json\' | relative_url }}?v={{ site.time | date: \'%s\' }}" data-detail-base="{{ \'/technical-training/journal-club/details/\' | relative_url }}" data-version="{{ site.time | date: \'%s\' }}">').replace('{% for paper in sorted_papers %}','{% for paper in sorted_papers limit: 20 %}')
s=s.replace('  <div class="jc-empty hidden"', '  <nav class="paper-pagination" aria-label="Paper result pages"><button type="button" id="jc-prev" disabled>Previous</button><span id="jc-page-status" role="status"></span><button type="button" id="jc-next" disabled>Next</button></nav>\n  <div class="jc-empty hidden"')
s += '\n<script src="{{ \'/assets/js/paper-browser.js\' | relative_url }}?v={{ site.time | date: \'%s\' }}" defer></script>\n'; p.write_text(s)
edit('content-library/journal-papers/data-storage.md','#7-ackerman-et-al-2022--bossdb-a-cloud-native-approach-for-petascale-neuroscience-data-management','#7-hider-et-al-2022--bossdb-a-cloud-native-approach-for-petascale-neuroscience-data-management')
for path in ['_layouts/page.html','_layouts/module.html']:
 edit(path,'  {% if page.image %}','  {% include ui/lesson-meta.html %}\n  {% if page.image %}')
write('_includes/ui/lesson-meta.html','''{% if page.content_type == 'path' %}
{% if page.time_estimate or page.duration %}
{% assign capability = site.data.technical_capabilities.units | where: 'slug', page.slug | first %}
<aside class="lesson-meta" aria-label="Lesson at a glance">
<p><strong>Time:</strong> {{ page.time_estimate | default: page.duration | escape }}<br><strong>Prerequisites:</strong> {{ page.prerequisites | default: 'See lesson guidance below' | escape }}</p>
{% if capability.success_artifacts %}<p><strong>Your output:</strong> {{ capability.success_artifacts | first | escape }}</p>{% endif %}
<nav class="lesson-actions" aria-label="Lesson actions"><a href="{{ '/technical-training/' | relative_url }}">Course overview</a>{% if page.module_number %}<a href="{{ '/modules/' | relative_url }}">Topic module catalog</a>{% endif %}</nav>
</aside>
{% endif %}{% endif %}
''')
edit('_layouts/default.html','    <script src="{{ \'/assets/js/navigation.js\' | relative_url }}" defer></script>','    <script src="{{ \'/assets/js/navigation.js\' | relative_url }}" defer></script>\n    <script src="{{ \'/assets/js/usability-followup.js\' | relative_url }}?v={{ site.time | date: \'%s\' }}" defer></script>')
write('assets/js/usability-followup.js','''(() => {
  const area = document.querySelector('.site-breadcrumbs a:nth-of-type(2)');
  if (area) document.querySelectorAll('summary[data-nav-label]').forEach(el => el.classList.toggle('active', el.dataset.navLabel === area.textContent.trim()));
  const input = document.getElementById('session-search');
  if (input) {
    const status = document.getElementById('session-status'), count = document.getElementById('session-count');
    const cards = [...document.querySelectorAll('.session-card')].map(el => ({el, text:el.textContent.toLowerCase()}));
    let timer;
    const filter = () => { let shown=0; const q=input.value.trim().toLowerCase(); cards.forEach(({el,text}) => { el.hidden=!(text.includes(q) && (status.value==='all' || el.dataset.status===status.value)); if(!el.hidden) shown++; }); count.textContent=shown+' of '+cards.length+' session plans'+(shown ? '.' : '. Clear the search or change status.'); };
    input.addEventListener('input', () => { clearTimeout(timer); timer=setTimeout(filter,180); }); status.addEventListener('change',filter); filter();
  }
  const actions=document.querySelector('.lesson-actions');
  if(actions) {
    const headings=[...document.querySelectorAll('main h2[id]')].filter(el => !el.closest('details'));
    for(const [label, pattern] of [['Learn', /what you|why this|resolution argument/i], ['Practice', /^lab:|studio activity/i], ['Check your work', /rubric|self.check/i]]) {
      const h=headings.find(el => pattern.test(el.textContent));
      if(h){const a=document.createElement('a'); a.href='#'+h.id; a.textContent=label; actions.appendChild(a);}
    }
  }
  const draft=document.getElementById('first-observation');
  if(draft){
    const message=document.getElementById('first-save-status'), key='nt-first-observation-v1';
    try {draft.value=localStorage.getItem(key)||'';} catch(_){message.textContent='Local saving is unavailable. Copy your answer before leaving.';}
    draft.addEventListener('input',()=>{try{localStorage.setItem(key,draft.value); message.textContent='Draft saved in this browser only.';}catch(_){message.textContent='Not saved. Copy your answer before leaving.';}});
    document.getElementById('first-clear').addEventListener('click',()=>{draft.value='';try{localStorage.removeItem(key);}catch(_){} message.textContent='Draft cleared.';});
  }
})();
''')
write('start-here/first-activity.md','''---
layout: page
title: "Your first connectomics observation"
description: "A ten-minute guided exercise in separating a wiring observation from a claim about what a brain does."
permalink: /start-here/first-activity/
content_type: path
time_estimate: "10 minutes"
prerequisites: "None. Read the small table and write two sentences."
---

## 1. Read a tiny wiring map

**Synthetic teaching example, not a measurement from a real brain.** Imagine that a team has identified three neurons (brain cells), named A, B, and C. They recorded these synaptic connections. A synapse is a site where one neuron can communicate with another.

| Connection | Recorded synapses |
|---|---:|
| A to B | 4 |
| A to C | 1 |
| B to C | 0 |

**Your question:** Does this table establish that A has a larger effect on B's activity than on C's activity?

## 2. Make one defensible observation

A worked example: “The table records four synapses from A to B and one from A to C.” That sentence reports what was counted. “A controls B more strongly” goes beyond the information in the table: it does not tell us how the cells were behaving or how effective the synapses were.

Complete these two sentences in your own words. No account or external service is needed. Do not include private information.

<label for="first-observation"><strong>Your observation and its limit</strong></label>
<textarea id="first-observation" rows="5" placeholder="The map records…&#10;This alone does not establish…"></textarea>
<p id="first-save-status" role="status" aria-live="polite">Your draft stays in this browser; it is not submitted for assessment.</p>
<button type="button" id="first-clear" class="btn btn-secondary">Clear draft</button>

## 3. Check the reasoning

<details><summary>Compare your answer with the worked response</summary><p>The map records more A-to-B synapses than A-to-C synapses. Counts alone do not establish the relative effect on activity. Also, zero recorded B-to-C synapses is a result in this small example, not proof that such a connection could never exist in a different sample.</p><p>A useful answer distinguishes the recorded observation from the unsupported functional claim. Completing this exercise is practice, not evidence of general proficiency.</p></details>

## Continue

[Start Why Map the Brain]({{ '/technical-training/01-why-map-the-brain/' | relative_url }}) to develop the full reasoning, or [choose another starting point]({{ '/start-here/' | relative_url }}).
''')
edit('start-here.md','<h2 id="your-first-hour">Your first hour</h2>', '<h2 id="your-first-hour">Try it before choosing a course</h2><p><a class="btn btn-primary" href="{{ \'/start-here/first-activity/\' | relative_url }}">Try a guided 10-minute activity</a></p><p>Use a small, explicitly synthetic wiring example to write one observation and one limit. No setup or neuroscience vocabulary is assumed.</p><h3>Then try real data: your first hour</h3>')
p=R/'assets/css/usability.css'; p.write_text(p.read_text()+'''
/* Bounded paper lists and task-first reading. */
.paper-view-links, .paper-pagination, .lesson-actions { display:flex; flex-wrap:wrap; align-items:center; gap:0.75rem; margin:1rem 0; }
.paper-view-links a, .paper-view-links span, .paper-pagination button, .lesson-actions a { display:inline-flex; align-items:center; min-height:44px; padding:0.4rem 0.75rem; border:1px solid #a9b9c8; border-radius:6px; }
.paper-view-links [aria-current] { background:#e8eff7; color:#17344a; font-weight:700; }
.paper-pagination button { background:#fff; color:#174bb6; font:inherit; cursor:pointer; }
.paper-pagination button:disabled { color:#596879; cursor:default; }
#jc-grid .jc-card { content-visibility:auto; contain-intrinsic-size:auto 230px; overflow-wrap:anywhere; min-width:0; }
#jc-grid .jc-link, #jc-filters select, #jc-filters input, #jc-filters button { min-height:44px; }
#jc-filters { align-items:center; }
#jc-filters input { min-width:0; max-width:100%; }
#jc-filters select { max-width:100%; }
.lesson-meta { padding:0.75rem 1rem; margin:0.5rem 0; border-left:4px solid #006d6b; background:#f2f6f8; }
.lesson-meta p { margin:0.3rem 0; }
.layout-page:has(.lesson-meta) > .module-art img { height:140px; object-fit:contain; }
.session-card[hidden] { display:none; }
#session-search, #session-status, #first-observation { display:block; width:100%; box-sizing:border-box; min-height:44px; font:inherit; padding:0.65rem; border:1px solid #9caec0; border-radius:6px; margin:0.5rem 0; }
.jcg-page .jcg-hint { color:#475569; }
@media(max-width:640px){ #jc-filters { display:flex; flex-direction:column; align-items:stretch; } .jc-prompt-modes { flex-wrap:wrap; } .lesson-meta { margin:0.5rem 0; } }
''')
p=R/'scripts/smoke_site.cjs'; s=p.read_text().replace("'33% complete'","'33% of self-reported activities checked'").replace("'0% complete'","'0% of self-reported activities checked'"); a=s.index("    assert.equal(await page.$$eval('#jc-grid > .jc-card'"); b=s.index("    await openGroup('Resources');",a)
s=s[:a]+'''    await page.waitForFunction(() => document.getElementById('jc-count').textContent.includes('2000 of 2000'));
    assert.equal(await page.$$eval('#jc-grid > .jc-card', elements => elements.length), 20);
    assert.equal(await page.$eval('#jc-prompt-modal', element => getComputedStyle(element).display), 'none');
    const firstTitle=await page.$eval('#jc-grid h3', e=>e.textContent);
    await page.click('#jc-next');
    assert.notEqual(await page.$eval('#jc-grid h3', e=>e.textContent), firstTitle);
    assert.equal(await visibleCount('.jc-card'),20);
    await page.select('#jc-tier', '500');
    await page.waitForFunction(() => document.getElementById('jc-count').textContent.startsWith('500 of'));
    await page.type('#jc-search', '10.1109/tmi.2024.3400276');
    await page.waitForFunction(() => document.getElementById('jc-count').textContent.startsWith('1 of'));
    assert((await page.$eval('#jc-grid', e=>e.textContent)).includes('WASPSYN'));
    await page.click('[data-details]');
    await page.waitForFunction(() => !document.querySelector('[data-details]'));
    assert(await page.$('#jc-grid .jc-card-details[open]'));
    await page.click('#jc-search', {clickCount:3});
    await page.type('#jc-search', 'zzzz-no-such-paper');
    await page.waitForSelector('#jc-empty', {visible:true});
    assert.equal(await visibleCount('.jc-card'),0);
    await page.click('#jc-reset');
    await page.waitForFunction(() => document.getElementById('jc-count').textContent.startsWith('2000 of'));
    await page.click('#jc-prompt-btn');
    await page.waitForSelector('#jc-prompt-modal', {visible:true});
    assert((await page.$eval('#jc-prompt-textarea', element => element.value)).includes('First 35 of 2000'));
    await page.keyboard.press('Escape');
    await page.waitForSelector('#jc-prompt-modal', {hidden:true});
'''+s[b:]; p.write_text(s)
p=R/'scripts/check_research_modal.cjs'; s=p.read_text().replace("      assert.equal(await display(), 'none', `${width}px: overlay visible on arrival`);","      await page.waitForSelector('#jc-prompt-btn:not([disabled])');\n      assert.equal(await display(), 'none', `${width}px: overlay visible on arrival`);"); p.write_text(s)
p=R/'scripts/check_site_layout.cjs'; s=p.read_text().replace("  '/', '/resources/',", "  '/', '/resources/', '/technical-training/journal-club/', '/start-here/first-activity/',"); p.write_text(s)
p=R/'technical-training/journal-club/index.md'; s=p.read_text(); a=s.index('  <div class="jc-filters"'); b=s.index('  <!-- AI Synthesis Prompt Modal -->',a)
controls=s[a:b]; blocks={}
for key in ['tier','expertise','dimension','organism','era','sort']:
 m=re.search(r'<label for="jc-'+key+r'">.*?</select>',controls,re.S); assert m,key; blocks[key]=m.group()
search=re.search(r'<label for="jc-search">.*?<input[^>]+>',controls,re.S).group()
actions=controls[controls.index('    <button type="button" id="jc-prompt-btn"'):controls.rindex('  </div>')]
new='  <div class="jc-filters" id="jc-filters">'+search+blocks['dimension']+blocks['organism']+'<details class="paper-more-filters"><summary>More filters and reading-note options</summary><div class="jc-filters">'+''.join(blocks[k] for k in ['tier','era','sort','expertise'])+'</div></details>'+actions+'  </div>\n\n'
p.write_text(s[:a]+new+s[b:])
p=R/'technical-training/journal-club/graph.md'; s=p.read_text().replace('id="jcg-panel"','id="jcg-panel" role="region" aria-label="Selected paper details"'); p.write_text(s)
write('scripts/check_usability_followup.cjs', '''const assert=require('node:assert/strict'), fs=require('node:fs'), path=require('node:path'), http=require('node:http');
const puppeteer=require('puppeteer');
const site=path.resolve('_site');
const html=fs.readFileSync(path.join(site,'technical-training/journal-club/index.html'),'utf8');
assert(Buffer.byteLength(html)<500000,'Paper entry HTML must stay below 500 KB');
assert.equal((html.match(/class="jc-card"/g)||[]).length,20,'Server renders 20 cards, not 2000');
const index=JSON.parse(fs.readFileSync(path.join(site,'technical-training/journal-club/index-data.json')));
assert.equal(index.length,2000); assert.equal(new Set(index.map(p=>p.id)).size,2000);
const detailIds=new Set();
for(let n=0;n<20;n++){const chunk=JSON.parse(fs.readFileSync(path.join(site,'technical-training/journal-club/details/'+n+'.json'))); assert.equal(Object.keys(chunk).length,100); Object.keys(chunk).forEach(id=>detailIds.add(id));}
assert(index.every(p=>detailIds.has(p.id))); assert(index.every(p=>!('abstract' in p) && !('ocar' in p)));
const server=http.createServer((req,res)=>{let name=new URL(req.url,'http://localhost').pathname;if(name.endsWith('/'))name+='index.html';const file=path.resolve(site,'.'+name);if(!file.startsWith(site+path.sep)||!fs.existsSync(file)){res.writeHead(404).end();return;}const ext=path.extname(file);res.setHeader('Content-Type',({'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json','.svg':'image/svg+xml'})[ext]||'application/octet-stream');fs.createReadStream(file).pipe(res);});
(async()=>{await new Promise(r=>server.listen(0,'127.0.0.1',r));let browser;try{
 browser=await puppeteer.launch({headless:true,args:['--no-sandbox']}); const base='http://127.0.0.1:'+server.address().port;
 for(const width of [390,1440]){
 const page=await browser.newPage();await page.setViewport({width,height:900});const errors=[];page.on('pageerror',e=>errors.push(e.message));let detailRequests=0;page.on('request',req=>{if(req.url().includes('/journal-club/details/'))detailRequests++;});
 await page.goto(base+'/technical-training/journal-club/');await page.waitForFunction(()=>document.getElementById('jc-count').textContent.startsWith('2000 of'));
 assert.equal(detailRequests,0,'Details should not be fetched on arrival');assert.equal(await page.$$eval('#jc-grid .jc-card',e=>e.length),20);
 await page.type('#jc-search','10.1109/tmi.2024.3400276');await page.waitForFunction(()=>document.getElementById('jc-count').textContent.startsWith('1 of'));
 await page.click('#jc-graph-view');await page.waitForSelector('.jcg-result-btn');assert.equal(await page.$eval('#jcg-search',e=>e.value),'10.1109/tmi.2024.3400276');
 await page.focus('.jcg-result-btn');await page.keyboard.press('Enter');assert.equal(await page.evaluate(()=>document.activeElement.id),'jcg-panel-close');await page.keyboard.press('Escape');assert(await page.$eval('#jcg-panel',e=>e.classList.contains('hidden')));assert(await page.evaluate(()=>document.activeElement.classList.contains('jcg-result-btn')));
 await page.click('#jcg-list-view');await page.waitForFunction(()=>document.getElementById('jc-count').textContent.startsWith('1 of'));
 await page.click('[data-details]');await page.waitForSelector('#jc-grid .jc-card-details');assert.equal(detailRequests,1);assert(await page.$eval('#jc-grid .jc-card-details',e=>e.open));
 await page.goto(base+'/technical-training/journal-club/#paper-author-1990--pnas-0409009101');await page.waitForFunction(()=>document.querySelector('#paper-author-1990--pnas-0409009101 .jc-card-details'));
 await page.goto(base+'/teaching/');assert.equal(await page.$$eval('main a[href^="/modules/module"]',e=>e.length),0,'Teaching hub routes rather than duplicating the catalog');
 await page.goto(base+'/teaching/sessions/');await page.type('#session-search','Python');await page.waitForFunction(()=>document.getElementById('session-count').textContent.startsWith('1 of'));
 await page.goto(base+'/modules/module01/');await page.$$eval('.nt-progress-step:not([disabled])',checks=>checks.forEach(el=>el.click()));assert((await page.$eval('.nt-progress-text',e=>e.textContent)).includes('self-reported'));assert((await page.$eval('.nt-assessment-status',e=>e.textContent)).includes('not yet passed'));assert(await page.$eval('[data-assessment="quiz"]',e=>e.disabled&&!e.checked));
 await page.goto(base+'/start-here/first-activity/');await page.type('#first-observation','The table records four A-to-B synapses.');await page.reload();assert((await page.$eval('#first-observation',e=>e.value)).includes('four'));await page.click('#first-clear');assert.equal(await page.$eval('#first-observation',e=>e.value),'');
 assert.deepEqual(errors,[],width+'px runtime errors');await page.close();console.log('PASS '+width+'px: lazy details, list/map state, drawer keyboard, session search, progress semantics, draft persistence');
 }
 console.log('Paper HTML bytes: '+Buffer.byteLength(html)+'; index bytes: '+fs.statSync(path.join(site,'technical-training/journal-club/index-data.json')).size);
}finally{if(browser)await browser.close();server.close();}})().catch(e=>{console.error(e);process.exitCode=1;});
''')
edit('scripts/check_research_modal.cjs', "const root = path.resolve('_site');", "require('node:child_process').execFileSync(process.execPath, [path.join(__dirname, 'check_usability_followup.cjs')], { stdio: 'inherit' });\n\nconst root = path.resolve('_site');")
