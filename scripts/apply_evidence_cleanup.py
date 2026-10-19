#!/usr/bin/env python3
"""One-time source migration for PR 194; remove after application.

Accept only the inspected file revisions. No network calls or credential handling.
"""
from pathlib import Path
import hashlib
R = Path(__file__).resolve().parents[1]
EXPECTED = {
 '.github/workflows/paper-evidence.yml':'9e71b2fe03cfd6ab462a52c8fc03c09e79d22b9c7892842e2890f423f02cacb2',
 '.github/workflows/validate.yml':'e9665e68665a376a713de914d4ef4b9a9f616ebc1b2446dd518f45d7ef6fded9',
 '_config.yml':'4e6fe7243a3f1df2ce32046a68b459a83bcf6bcd0e7ca5562240b691f9d6dabb',
 'assets/js/paper-browser.js':'8bd801cb9aabaef85d20f0c936177bebc8187538fd6d38a63df33ca58c0aa1bd',
 'assets/js/paper-evidence.js':'a389ab277be03489b6a241fccde3de7130c992b853c9474c7c9c25726af4cebf',
 'scripts/check_paper_graph.cjs':'39fc56f1db1421dd47b15f41866a8853db56d415e4d34307602e58b9361c2eb5',
 'technical-training/journal-club/graph-data.json':'237f4119ca389311ef1b7a9dff0e1f24c0b5b3b912687aba02e2aa31cbd2f225',
 'technical-training/journal-club/graph.md':'eeb2dd6ca38f84587f052dfeef3fc97093534f4b8bbfd78f635facc54978340b',
 'technical-training/journal-club/index.md':'17deb5d01ac3fec6741f6c683484311b2684e5be475ee1e540ec8de0b3933dfb'
}
for path,digest in EXPECTED.items():
    assert hashlib.sha256((R/path).read_bytes()).hexdigest()==digest, 'Source changed: '+path

def sub(s,old,new):
    assert s.count(old)==1,(old[:100],s.count(old))
    return s.replace(old,new)
def span(s,start,end,new):
    a=s.index(start); b=s.index(end,a)
    return s[:a]+new+s[b:]

p=R/'technical-training/journal-club/graph.md'; s=p.read_text()
s=sub(s,'<script>',"<script src=\"{{ '/assets/js/paper-evidence.js' | relative_url }}?v={{ site.time | date: '%s' }}\"></script>\n<script>")
s=sub(s,'  var JC_BASE_URL =','  var evidenceApi = window.NTPaperEvidence;\n  var JC_BASE_URL =')
s=sub(s,"        summary: d.summary || '',","        evidence: d.evidence || null,")
s=sub(s,"        searchText: [d.title, d.authors, d.journal, d.doi, d.summary, d.abstract, JSON.stringify(d.ocar || {}), orgs.join(' ')].join(' ').toLowerCase(),","        // Bibliographic search excludes generated interpretations and tags.\n        searchText: [d.title, d.authors, d.journal, d.doi].join(' ').toLowerCase(),")
s=sub(s,"        ocar: d.ocar || null,\n        summaries: d.summaries || null,\n        discussion_prompts: d.discussion_prompts || [],\n",'')
s=span(s,'    // OCAR Section','    // Interactive Citation Lineage Chips',"    var evidenceHtml = evidenceApi ? evidenceApi.render(p.evidence, p.doi) :\n      '<p class=\"jcg-hint\">Contribution notes could not load. Open the publication for its findings.</p>';\n\n")
s=span(s,'    var paperMetaHtml =','    var abstractHtml =',"    var indexingHtml = '<details class=\"jcg-paper-metadata\"><summary>Indexing information</summary>' +\n      '<p class=\"jcg-hint\">Topic and organism tags support navigation; they are not verified methods, dataset use, affiliations, or results. Citation links record references, not agreement or demonstrated improvements.</p>' +\n      '<p>Assigned topic: ' + escapeHtml(p.dimension.replace(/-/g, ' ')) + '. Organism tags: ' + escapeHtml(organismLabel(p)) + '.</p>' +\n      '<p class=\"jcg-hint\">Imported network metrics: in ' + p.in_degree + ', out ' + p.out_degree + '. These may include links outside the displayed corpus and are not measures of scientific quality. The citation controls above count links resolved within this corpus.</p>' +\n      '<button type=\"button\" class=\"jcg-secondary-btn\" id=\"jcg-btn-ai-prompt\">Prepare a paper review prompt</button></details>';\n")
s=sub(s,"      ecosystemAndPipelineHtml +\n      '<details class=\"jcg-corpus-notes\"><summary>Corpus reading notes (unverified)</summary><p class=\"jcg-hint\">These notes have not been checked against this paper. Use the abstract and original publication for its methods and findings.</p>' +\n      ocarHtml +\n      summariesHtml +\n      promptsHtml +\n      '</details>' +",'      evidenceHtml +\n      indexingHtml +')
s=span(s,'    // Attach summary tab switcher','    // Attach lineage jump chips','')
s=span(s,'  function generateSynthesisPrompt() {','  function openAiTray() {', '''  function generateSynthesisPrompt() {
    var selection = singlePaperTarget ? [singlePaperTarget] : visibleNodes;
    var count = selection.length;
    modalTitleEl.textContent = singlePaperTarget ? 'Paper review prompt' : 'Research review prompt';
    modalDescEl.textContent = singlePaperTarget ?
      'Uses this publication\u2019s recorded abstract and any source-checked contribution note. Verify against the original.' :
      'Uses the first ' + Math.min(count, 35) + ' of ' + count + ' matches in the current order; not a representative or quality-ranked sample.';
    promptTextarea.value = evidenceApi ? evidenceApi.reviewPrompt(selection, currentPromptMode, count) :
      'The review prompt helper did not load. Reload to retry, or open the original publications directly.';
  }

''')
s=sub(s,"    var tierLabel = p.tier === 500 ? '500 Core Flagship' : (p.tier === 1000 ? '1000 Landmark' : '2000 Comprehensive');\n",'')
s=s.replace('Paper details and reading notes','Paper abstract and evidence').replace(' Foundational References',' References in Corpus')
s=s.replace('Core Hub (Foundational)','Imported hub label').replace('High-Impact Authority','Imported authority label').replace('Citation Role (Foundational / Hub / Bridge)','Imported network role (not evidence)')
s=s.replace('500 Flagship / 1000 / 2000','500 / 1000 / 2000').replace('Publication Era (History / Contemporary / SOTA)','Publication period')
s=s.replace('Copy this grounded prompt into','Copy this review prompt into')
s=s.replace('Search all 2,000 papers. Topic and organism filters narrow your results. Choose a paper below to read it.','Search publication titles, authors, journals, and DOI identifiers. Topic and organism tags narrow results but do not establish dataset use or findings.')
s=s.replace("var html = '<h3>' + p.title + '</h3>'", "var html = '<h3>' + escapeHtml(p.title) + '</h3>'")
s=s.replace("+ p.authors + ' &bull; <em>' + p.journal +", "+ escapeHtml(p.authors) + ' &bull; <em>' + escapeHtml(p.journal) +")
s=s.replace("'<strong>Full Citation:</strong> ' + p.citation", "'<strong>Full Citation:</strong> ' + escapeHtml(p.citation)")
s=s.replace("+ cp.id + '\">'", "+ escapeHtml(cp.id) + '\">'")
s=s.replace("(cp.authors.split(';')[0].split(',')[0] || 'Author')", "escapeHtml(cp.authors.split(';')[0].split(',')[0] || 'Author')")
s=s.replace("(cp.title.length > 38 ? cp.title.slice(0, 36) + '…' : cp.title)","escapeHtml(cp.title.length > 38 ? cp.title.slice(0, 36) + '…' : cp.title)")
s=s.replace("    var pdfButton = p.pdf_url ?", "    var pdfUrl = evidenceApi ? evidenceApi.safeSourceUrl(p.pdf_url) : '';\n    var pdfButton = pdfUrl ?")
s=s.replace("+ p.pdf_url +", "+ escapeHtml(pdfUrl) +").replace("+ p.doi +", "+ escapeHtml(p.doi) +")
s=s.replace('// Rich Slide-Out Drawer with Deep OCAR Integration','// Publication-first drawer: no category-generated claims.')
s=s.replace('<!-- Slide-Out Paper Detail Drawer with Deep OCAR Integration -->','<!-- Source-checked publication detail drawer -->')
s=s.replace('<!-- Dynamically populated with OCAR cards, 3-tier summaries, and citation lineage -->','<!-- Source-checked contributions, abstract, and recorded citation links -->')
s=s.replace('/* 5-Part OCAR Container */','/* Shared detail styles (also used for the citation footer). */')
s=s.replace('<!-- On-Demand AI Literature Synthesis & Discussion Tray -->','<!-- Optional review prompts; not automated scientific findings -->')
s=s.replace('.jcg-paper-abstract h4 {','.jcg-paper-evidence { margin: 1rem 0; padding: 0.75rem; border: 1px solid #cbd5e1; border-radius: 8px; }\n.jcg-paper-evidence p { font-size: 0.82rem; line-height: 1.55; }\n.jcg-paper-abstract h4 {')
assert 'p.ocar' not in s and 'p.summaries' not in s and 'Ground-Truth' not in s
p.write_text(s)

p=R/'technical-training/journal-club/graph-data.json'; s=p.read_text(); s=sub(s,'"abstract":{{ p.abstract | jsonify }},','"abstract":{{ p.abstract | jsonify }},"evidence":{{ checked_paper_evidence | jsonify }},'); p.write_text(s)
p=R/'assets/js/paper-browser.js'; s=p.read_text()
s=span(s,'  function expertise() {','  async function details(', '')
s=sub(s,'      expertise();\n','')
s=sub(s,"  $('jc-expertise').addEventListener('change', expertise);\n",'')
s=sub(s,"    else if (button.matches('.jc-tab')) article.querySelectorAll('.jc-tab, .jc-level').forEach(el => el.classList.toggle('active', el.dataset.level === button.dataset.level));\n",'')
s=s.replace(', .jc-tab, [data-filter-field]', ', [data-filter-field]')
s=s.replace("[p.title,p.authors,p.doi,p.journal,...(p.tags||[])]","[p.title,p.authors,p.doi,p.journal]")
s=s.replace("esc(p.year) + ' · ' + esc(p.dimension.replace(/-/g,' '))","esc(p.year)")
p.write_text(s)
p=R/'assets/js/paper-evidence.js'; s=p.read_text()
s=sub(s,'  function eligible(record, doi) {', '''  function safeSourceUrl(value) {
    try { const url = new URL(value); return url.protocol === 'https:' && !!url.hostname && !url.username && !url.password ? url.href : ''; }
    catch (_) { return ''; }
  }
  function eligible(record, doi) {''')
s=sub(s,"    try { const url = new URL(record.source_url); return url.protocol === 'https:' && !!url.hostname && !url.username && !url.password; }\n    catch (_) { return false; }", "    return !!safeSourceUrl(record.source_url);")
s=sub(s,'Object.freeze({eligible, render, reviewPrompt})','Object.freeze({eligible, render, reviewPrompt, safeSourceUrl})'); p.write_text(s)
p=R/'technical-training/journal-club/index.md'; s=p.read_text()
s=span(s,'</select><label for="jc-expertise">','</select></div></details>', '')
s=s.replace('More filters and reading-note options','More filters').replace('optional reading notes','source-checked contribution notes').replace('optional discussion notes','source-checked contribution notes')
s=s.replace('Suggested reading paths and reuse','Corpus navigation and reuse')
s=s.replace('Corpus notes and discussion prompts are NeuroTrailblazers material under CC BY 4.0.','Source-checked contribution notes and review prompts are NeuroTrailblazers material under CC BY 4.0.')
s=s.replace('Reading notes are unverified; check them against the publication.','Source-checked notes identify the source used and checking limits; they are not expert peer review. Historical generated notes are not published.')
s=s.replace('500 Key Papers','500-paper subset').replace('1000 Key Papers','1,000-paper subset').replace('All 2000 Papers','All 2,000 papers')
s=s.replace('✨ Generate AI Synthesis Prompt','Prepare a review prompt').replace('🤖 AI Research Synthesis Prompt','Research review prompt')
s=s.replace('Copy this grounded prompt into','Copy this review prompt into').replace('to generate a rigorous analysis across','to prepare a source-based review of')
s=s.replace('Search covers the full corpus regardless of browse subset; topic and organism filters still apply. Abstracts are publication text recorded in the corpus; reading notes are site-added and unverified.','Search matches bibliographic text across the full corpus regardless of browse subset; topic and organism tags still filter results. Tags and citation metrics are navigation aids, not verified methods, affiliations, dataset use, or scientific quality. Abstracts are recorded publication text; contribution notes are shown only with a source and checking provenance.')
p.write_text(s)
p=R/'_config.yml'; s=p.read_text(); s=sub(s,'  - data/ocar_regen','  - data/ocar_regen\n  # Historical generated annotations are internal inputs, not public downloads.\n  - data/corpus_500.json\n  - data/corpus_1000.json\n  - data/corpus_2000.json'); p.write_text(s)
p=R/'scripts/check_paper_graph.cjs'; s=p.read_text()
s=sub(s,"const vm = require('node:vm');", "const vm = require('node:vm');\nconst evidenceApi = require('../assets/js/paper-evidence.js');")
s=sub(s,"  const win = { devicePixelRatio", "  const win = { NTPaperEvidence: evidenceApi, devicePixelRatio")
s=sub(s,"  for (const q of ['summaryneedle','abstractneedle','futureneedle','AUTHOR','mouse']) { f.change('jcg-search',q,'input'); assert.equal(f.graph.state().nodes.length, 1, q); }", "  for (const q of ['summaryneedle','abstractneedle','futureneedle','mouse']) { f.change('jcg-search',q,'input'); assert.equal(f.graph.state().nodes.length, 0, 'Navigation metadata/legacy notes must not pollute bibliographic search: ' + q); }\n  f.change('jcg-search','AUTHOR','input'); assert.equal(f.graph.state().nodes.length, 1);")
s=sub(s,"  assert.match(card, /<strong>Model organism<\\/strong><span>Rat<\\/span>/);\n  assert.match(card, /<strong>Dataset \\/ volume<\\/strong><span>Not recorded<\\/span>/);", "  assert.match(card, /Organism tags: Rat/);\n  assert.match(card, /not verified methods, dataset use/);")
s=sub(s,"  assert.match(card, /Corpus reading notes \\(unverified\\)/);", "  assert.ok(!card.includes('Corpus reading notes') && !card.includes('Opportunity</span>'), 'No legacy annotation drawer');\n  assert.match(card, /source-checked contribution note is not available/);")
s=s.replace('searchable abstracts and empty state','bibliographic-only search and empty state'); p.write_text(s)
p=R/'.github/workflows/validate.yml'; s=p.read_text(); s=sub(s,'      - name: Paper graph filtering, layout and redraw regression\n','      - name: Actual Liquid evidence gate and public exports\n        run: bundle exec ruby scripts/check_paper_evidence_render.rb\n\n      - name: Paper graph filtering, layout and redraw regression\n'); p.write_text(s)
p=R/'.github/workflows/paper-evidence.yml'; s=p.read_text(); s+='      - uses: actions/setup-node@v4\n        with:\n          node-version: \'22\'\n      - name: Evidence rendering and negative association tests\n        run: node scripts/check_paper_evidence_unit.cjs\n'; p.write_text(s)
print('Applied guarded cleanup to inspected sources.')
