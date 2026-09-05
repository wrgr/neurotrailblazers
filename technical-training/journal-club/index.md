---
layout: default
title: "Journal Club"
permalink: /technical-training/journal-club/
track: core-concepts-methods
pathways:
  - technical foundation
  - shared vocabulary
description: "Browse the full connectomics paper collection — filter by expertise level, dimension, era, or keyword, or explore it as a citation graph. Each paper presented with the OCAR framework — Opportunity, Challenge, Action, Resolution, and Future Work."
content_type: core
---

<div class="layout-content layout-page">

{%- assign jc_dims = site.data.journal_papers.papers | map: 'dimension' | compact | uniq -%}
<section class="jc-hero">
  <h1>Journal Club &amp; Research Corpus</h1>
  <p>{{ site.data.journal_papers.papers.size }} connectomics papers &mdash; a multi-tiered literature network selected by their place in the field's citation graph &mdash; each presented with the OCAR framework (Opportunity, Challenge, Action, Resolution, Future Work), 3-level summaries, and seminar discussion prompts.</p>
  <div class="jc-hero-stats">
    <span class="jc-hero-stat">{{ site.data.journal_papers.papers.size }} Total Papers</span>
    <span class="jc-hero-stat">{{ jc_dims.size }} Research Domains</span>
    <span class="jc-hero-stat">3 Expertise Levels</span>
    <span class="jc-hero-stat">3 Tiers (500 / 1,000 / 2,000)</span>
  </div>
</section>

<section class="section section-compact">
  <p><strong>Using this corpus?</strong> The curation, the OCAR cards and the discussion prompts are
  NeuroTrailblazers material under CC BY 4.0 &mdash; see <a href="{{ '/about/#cite-this-site' | relative_url }}">how to cite this site</a>.
  The papers themselves are the property of their publishers; each card links out to the source.</p>
</section>

<section class="section section-compact">
  <p>Browse the canonical connectomics literature across {{ jc_dims.size }} research domains and 3 nested tiers. Use this page to survey what exists, filter by domain/organism/era, or follow the citation graph between papers. For an interactive network visualization with self-organizing organic force physics and AI synthesis prompts, explore the graph below:</p>
  <p><a href="{{ '/technical-training/journal-club/graph/' | relative_url }}" class="jc-graph-cta" style="background:#1a56db; color:#fff; padding:0.6rem 1.2rem; border-radius:6px; text-decoration:none; font-weight:700; display:inline-block; margin-top:0.4rem;">Explore the Interactive Citation Graph &rarr;</a></p>
</section>

<section class="section section-compact">
  <h2 style="margin-top:0">Suggested Reading Paths</h2>
  <div class="jc-paths">
    {%- for group in site.data.paper_views.reading_paths.groups %}
    <div class="jc-path-card">
      <h3>{{ group.label }}</h3>
      <p>{{ group.description }}</p>
    </div>
    {%- endfor %}
  </div>
</section>

<section class="section section-compact">
  <div class="jc-filters" id="jc-filters">
    <label for="jc-tier">Corpus Tier:</label>
    <select id="jc-tier">
      <option value="500" selected>500 Key Papers</option>
      <option value="1000">1000 Key Papers</option>
      <option value="2000">2000 Key Papers</option>
    </select>

    <label for="jc-expertise">Expertise:</label>
    <select id="jc-expertise">
      <option value="beginner">Beginner</option>
      <option value="intermediate" selected>Intermediate</option>
      <option value="advanced">Advanced</option>
    </select>

    <label for="jc-dimension">Dimension:</label>
    {%- assign dims = site.data.journal_papers.papers | map: 'dimension' | compact | uniq | sort -%}
    <select id="jc-dimension">
      <option value="all">All {{ jc_dims.size }} dimensions</option>
      {%- for dim in dims %}
      {%- assign mapped = site.data.content_tags.dimension_labels[dim] %}
      {%- if mapped %}{% assign label = mapped %}{% else %}{% assign label = dim | replace: '-', ' ' | capitalize %}{% endif %}
      <option value="{{ dim }}">{{ label }}</option>
      {%- endfor %}
    </select>

    <label for="jc-era">Era:</label>
    <select id="jc-era">
      <option value="all">All eras</option>
      {%- for group in site.data.paper_views.era.groups %}
      <option value="{{ group.key }}">{{ group.label | capitalize }} ({{ group.n }})</option>
      {%- endfor %}
    </select>

    <label for="jc-sort">Sort:</label>
    <select id="jc-sort">
      <option value="year-desc">Newest first</option>
      <option value="year-asc">Oldest first</option>
      <option value="kcore-desc">Highest k-core first</option>
      <option value="dimension">By dimension</option>
    </select>

    <label for="jc-search">Search:</label>
    <input type="text" id="jc-search" placeholder="keyword, author, tag, organism, dataset…">

    <button type="button" id="jc-prompt-btn" class="jc-prompt-trigger-btn" style="background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); color: #fff; border: none; border-radius: 6px; padding: 0.45rem 0.8rem; font-size: 0.82rem; font-weight: 600; cursor: pointer; display: inline-flex; align-items: center; gap: 0.35rem; box-shadow: 0 2px 6px rgba(124, 58, 237, 0.25);">
      ✨ Generate AI Synthesis Prompt (<span id="jc-prompt-count">500</span>)
    </button>

    <span class="jc-filter-count" id="jc-count"></span>
  </div>

  <!-- AI Synthesis Prompt Modal -->
  <div class="jc-prompt-modal hidden" id="jc-prompt-modal" style="position: fixed; inset: 0; background: rgba(15, 23, 42, 0.75); display: flex; align-items: center; justify-content: center; z-index: 1000; padding: 1.5rem;">
    <div class="jc-prompt-modal-content" style="background: #fff; border-radius: 12px; max-width: 720px; width: 100%; max-height: 90vh; display: flex; flex-direction: column; padding: 1.5rem; box-shadow: 0 20px 40px rgba(0,0,0,0.3); border: 1px solid #cbd5e1;">
      <div class="jc-prompt-modal-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
        <h3 style="margin: 0; font-size: 1.2rem; color: #0f172a;" id="jc-prompt-modal-title">🤖 AI Research Synthesis Prompt</h3>
        <button class="jc-prompt-modal-close" id="jc-prompt-close" style="background: none; border: none; font-size: 1.5rem; cursor: pointer; color: #64748b; line-height: 1;" aria-label="Close">&times;</button>
      </div>
      <p class="jc-prompt-modal-desc" style="font-size: 0.84rem; color: #475569; margin: 0 0 0.75rem 0; line-height: 1.45;" id="jc-prompt-modal-desc">
        Copy this grounded prompt into <strong>ChatGPT</strong>, <strong>Claude</strong>, or <strong>Gemini</strong> to generate a rigorous analysis across the <strong id="jc-modal-paper-count">0</strong> papers currently filtered in your view.
      </p>

      <!-- Mode Switcher Tabs -->
      <div class="jc-prompt-modes" id="jc-prompt-mode-tabs" style="display: flex; gap: 0.35rem; margin-bottom: 0.75rem; background: #f1f5f9; padding: 0.25rem; border-radius: 8px;">
        <button type="button" class="jc-pmode-btn active" data-mode="synthesis" style="flex: 1; padding: 0.35rem 0.5rem; font-size: 0.76rem; font-weight: 700; border: none; border-radius: 6px; background: #1a56db; color: #fff; cursor: pointer;">📑 Synthesis Review</button>
        <button type="button" class="jc-pmode-btn" data-mode="methods" style="flex: 1; padding: 0.35rem 0.5rem; font-size: 0.76rem; font-weight: 600; border: none; border-radius: 6px; background: transparent; color: #475569; cursor: pointer;">🔬 Methods Compare</button>
        <button type="button" class="jc-pmode-btn" data-mode="problems" style="flex: 1; padding: 0.35rem 0.5rem; font-size: 0.76rem; font-weight: 600; border: none; border-radius: 6px; background: transparent; color: #475569; cursor: pointer;">💡 Open Problems</button>
        <button type="button" class="jc-pmode-btn" data-mode="seminar" style="flex: 1; padding: 0.35rem 0.5rem; font-size: 0.76rem; font-weight: 600; border: none; border-radius: 6px; background: transparent; color: #475569; cursor: pointer;">🎓 Seminar Guide</button>
      </div>

      <div class="jc-prompt-box" style="flex: 1; display: flex; margin-bottom: 1rem;">
        <textarea id="jc-prompt-textarea" readonly style="width: 100%; height: 280px; box-sizing: border-box; padding: 0.75rem; font-family: monospace; font-size: 0.78rem; border: 1px solid #cbd5e1; border-radius: 6px; background: #f8fafc; color: #1e293b; resize: none; line-height: 1.4;"></textarea>
      </div>

      <div class="jc-prompt-modal-footer" style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.75rem;">
        <div style="display: flex; align-items: center; gap: 0.5rem;">
          <button type="button" class="jc-copy-btn" id="jc-copy-prompt-btn" style="background: #1a56db; color: #fff; border: none; border-radius: 6px; padding: 0.5rem 1rem; font-size: 0.85rem; font-weight: 600; cursor: pointer; display: inline-flex; align-items: center; gap: 0.4rem;">
            📋 Copy Prompt
          </button>
          <span class="jc-copy-status hidden" id="jc-copy-status" style="font-size: 0.85rem; font-weight: 600; color: #16a34a;">✅ Copied!</span>
        </div>
        <div style="display: flex; align-items: center; gap: 0.4rem;">
          <a href="https://chatgpt.com/" target="_blank" rel="noopener" class="jc-ai-link" style="background: #10a37f; color: #fff; padding: 0.4rem 0.7rem; border-radius: 6px; font-size: 0.78rem; font-weight: 600; text-decoration: none; display: inline-flex; align-items: center; gap: 0.25rem;">💬 ChatGPT &rarr;</a>
          <a href="https://claude.ai/new" target="_blank" rel="noopener" class="jc-ai-link" style="background: #d97706; color: #fff; padding: 0.4rem 0.7rem; border-radius: 6px; font-size: 0.78rem; font-weight: 600; text-decoration: none; display: inline-flex; align-items: center; gap: 0.25rem;">🟣 Claude &rarr;</a>
          <a href="https://gemini.google.com/app" target="_blank" rel="noopener" class="jc-ai-link" style="background: #2563eb; color: #fff; padding: 0.4rem 0.7rem; border-radius: 6px; font-size: 0.78rem; font-weight: 600; text-decoration: none; display: inline-flex; align-items: center; gap: 0.25rem;">✨ Gemini &rarr;</a>
        </div>
      </div>
    </div>
  </div>

  <p class="jc-shown-note">Showing <strong id="jc-shown-tier-label">500 Key Papers</strong> in Connectomics (stratified across {{ jc_dims.size }} domains) with complete 5-part OCAR research cards and 3-level pedagogical summaries. Use the tier selector above to expand to 1,000 or 2,000 papers, or explore the <a href="{{ '/technical-training/journal-club/graph/' | relative_url }}">interactive citation graph</a>.</p>

  <div class="jc-grid" id="jc-grid">
    {% assign sorted_papers = site.data.journal_papers.papers | sort: "year" | reverse %}
    {% for paper in sorted_papers %}
      {% include cards/journal-paper-card.html paper=paper %}
    {% endfor %}
  </div>
  <div class="jc-empty hidden" id="jc-empty">No papers match your filters. Try broadening your search.</div>
</section>

<section class="section section-compact">
  <h2>Journal Club Prep Checklist</h2>
  <ul>
    <li>Assign one person to lead methods critique and one to lead limitations critique.</li>
    <li>Require each participant to bring one claim, one supporting metric, and one unresolved uncertainty.</li>
    <li>Track discussion outcomes: method takeaway, reproducibility concern, follow-up action.</li>
    <li>Label all benchmark and performance numbers with publication year and context.</li>
  </ul>

  <h2>Suggested Cadence</h2>
  <ul>
    <li><strong>Week A:</strong> Required paper + one media demo aligned to current unit.</li>
    <li><strong>Week B:</strong> Optional paper focused on failure modes or interpretation limits.</li>
    <li><strong>Week C:</strong> Synthesis session using the atlas reference and dictionary terms.</li>
  </ul>
</section>

</div>

<script>
(function () {
  var grid      = document.getElementById('jc-grid');
  var cards     = Array.from(grid.querySelectorAll('.jc-card'));
  var countEl   = document.getElementById('jc-count');
  var emptyEl   = document.getElementById('jc-empty');
  var tierSel   = document.getElementById('jc-tier');
  var expSel    = document.getElementById('jc-expertise');
  var dimSel    = document.getElementById('jc-dimension');
  var eraSel    = document.getElementById('jc-era');
  var sortSel   = document.getElementById('jc-sort');
  var searchInp = document.getElementById('jc-search');

  // Expertise level switching (tabs inside cards)
  function setExpertise(level) {
    cards.forEach(function (card) {
      var tabs = card.querySelectorAll('.jc-tab');
      var levels = card.querySelectorAll('.jc-level');
      tabs.forEach(function (t) { t.classList.toggle('active', t.dataset.level === level); });
      levels.forEach(function (l) { l.classList.toggle('active', l.dataset.level === level); });
    });
  }

  // Tab click inside individual cards
  grid.addEventListener('click', function (e) {
    var tab = e.target.closest('.jc-tab');
    if (!tab) return;
    var card = tab.closest('.jc-card');
    card.querySelectorAll('.jc-tab').forEach(function (t) { t.classList.remove('active'); });
    card.querySelectorAll('.jc-level').forEach(function (l) { l.classList.remove('active'); });
    tab.classList.add('active');
    card.querySelector('.jc-level[data-level="' + tab.dataset.level + '"]').classList.add('active');
  });

  // Click-to-filter
  grid.addEventListener('click', function (e) {
    var chip = e.target.closest('[data-filter-field]');
    if (chip) {
      var field = chip.dataset.filterField;
      var value = chip.dataset.filterValue;
      if (field === 'era') {
        eraSel.value = value;
      } else {
        searchInp.value = value;
      }
      applyFilters();
      document.getElementById('jc-filters').scrollIntoView({ behavior: 'smooth', block: 'start' });
      return;
    }

    var relLink = e.target.closest('.jc-related-link');
    if (relLink) {
      e.preventDefault();
      jumpToPaper(relLink.dataset.relatedId);
    }
  });

  function jumpToPaper(id) {
    var target = cards.filter(function (c) { return c.dataset.id === id; })[0];
    if (!target) {
      var prev = countEl.textContent;
      countEl.textContent = "That paper is not loaded in this view — see the interactive citation graph.";
      setTimeout(function () { countEl.textContent = prev; }, 4000);
      return;
    }
    dimSel.value = 'all'; eraSel.value = 'all'; tierSel.value = '2000'; searchInp.value = '';
    applyFilters();
    target.scrollIntoView({ behavior: 'smooth', block: 'center' });
    target.classList.add('jc-card-flash');
    setTimeout(function () { target.classList.remove('jc-card-flash'); }, 1600);
  }

  function applyFilters() {
    var maxTier = parseInt(tierSel.value, 10) || 2000;
    var dim     = dimSel.value;
    var era     = eraSel.value;
    var query   = searchInp.value.toLowerCase().trim();
    var visible = 0;

    cards.forEach(function (card) {
      var cardTier   = parseInt(card.dataset.tier, 10) || 2000;
      var matchTier  = cardTier <= maxTier;
      var matchDim   = dim === 'all' || card.dataset.dimension === dim;
      var matchEra   = era === 'all' || card.dataset.era === era;
      var matchQuery = !query ||
        card.textContent.toLowerCase().indexOf(query) !== -1 ||
        (card.dataset.tags && card.dataset.tags.toLowerCase().indexOf(query) !== -1);
      var show = matchTier && matchDim && matchEra && matchQuery;
      card.classList.toggle('hidden', !show);
      if (show) visible++;
    });

    countEl.textContent = visible + ' of ' + cards.length + ' papers';
    var promptCountSpan = document.getElementById('jc-prompt-count');
    if (promptCountSpan) promptCountSpan.textContent = visible;
    emptyEl.classList.toggle('hidden', visible > 0);
    var labelEl = document.getElementById('jc-shown-tier-label');
    if (labelEl) {
      labelEl.textContent = maxTier === 500 ? '500 Key Papers' : (maxTier === 1000 ? '1000 Key Papers' : '2000 Key Papers');
    }
  }

  function applySort() {
    var val = sortSel.value;
    var sorted = cards.slice();
    if (val === 'year-desc') {
      sorted.sort(function (a, b) { return parseInt(b.dataset.year) - parseInt(a.dataset.year); });
    } else if (val === 'year-asc') {
      sorted.sort(function (a, b) { return parseInt(a.dataset.year) - parseInt(b.dataset.year); });
    } else if (val === 'kcore-desc') {
      sorted.sort(function (a, b) { return (parseInt(b.dataset.kcore) || 0) - (parseInt(a.dataset.kcore) || 0); });
    } else if (val === 'dimension') {
      sorted.sort(function (a, b) { return a.dataset.dimension.localeCompare(b.dataset.dimension); });
    }
    sorted.forEach(function (card) { grid.appendChild(card); });
  }

  // AI Prompt Modal Logic for Journal Club
  var promptModal     = document.getElementById('jc-prompt-modal');
  var promptBtn       = document.getElementById('jc-prompt-btn');
  var promptCloseBtn  = document.getElementById('jc-prompt-close');
  var promptTextarea  = document.getElementById('jc-prompt-textarea');
  var copyBtn         = document.getElementById('jc-copy-prompt-btn');
  var copyStatus      = document.getElementById('jc-copy-status');
  var modalCountEl    = document.getElementById('jc-modal-paper-count');
  var modalTitleEl    = document.getElementById('jc-prompt-modal-title');
  var modalDescEl     = document.getElementById('jc-prompt-modal-desc');
  var modeButtons     = Array.from(document.querySelectorAll('.jc-pmode-btn'));

  var currentPromptMode = 'synthesis';
  var singlePaperTarget = null;

  function getVisibleCards() {
    return cards.filter(function (c) { return !c.classList.contains('hidden'); });
  }

  function extractPaperCardData(card) {
    var titleEl = card.querySelector('.jc-card-title');
    var authEl = card.querySelector('.jc-card-authors');
    var journEl = card.querySelector('.jc-card-journal');
    var oppEl = card.querySelector('.jc-ocar-opportunity + p');
    var chalEl = card.querySelector('.jc-ocar-challenge + p');
    var actEl = card.querySelector('.jc-ocar-action + p');
    var resEl = card.querySelector('.jc-ocar-resolution + p');
    var futEl = card.querySelector('.jc-ocar-future + p');
    var sumEl = card.querySelector('.jc-level.active') || card.querySelector('.jc-level');

    return {
      id: card.dataset.id,
      title: titleEl ? titleEl.textContent.trim() : 'Untitled',
      authors: authEl ? authEl.textContent.trim() : '',
      journal: journEl ? journEl.textContent.trim() : '',
      year: card.dataset.year || '2024',
      dimension: card.dataset.dimension || 'connectomics',
      opportunity: oppEl ? oppEl.textContent.trim() : '',
      challenge: chalEl ? chalEl.textContent.trim() : '',
      action: actEl ? actEl.textContent.trim() : '',
      resolution: resEl ? resEl.textContent.trim() : '',
      future_work: futEl ? futEl.textContent.trim() : '',
      summary: sumEl ? sumEl.textContent.trim() : ''
    };
  }

  function generatePromptContent() {
    if (singlePaperTarget) {
      modalTitleEl.textContent = '🤖 AI Paper Study Guide & Seminar Critique';
      modalDescEl.innerHTML = 'Prompt tailored for: <strong>' + singlePaperTarget.title + '</strong> (' + singlePaperTarget.year + ')';
      
      var p = singlePaperTarget;
      var prompt = 'You are a principal investigator and expert seminar leader in connectomics.\n' +
        'Please provide an in-depth, rigorous scientific evaluation and discussion guide for the following landmark paper:\n\n' +
        '### Paper Metadata:\n' +
        '- **Title**: "' + p.title + '"\n' +
        '- **Authors**: ' + p.authors + '\n' +
        '- **Journal/Year**: ' + p.journal + ' (' + p.year + ')\n' +
        '- **Research Subfield**: ' + p.dimension + '\n\n' +
        '### 5-Part OCAR Narrative Framework:\n' +
        '- **Opportunity (Premise)**: ' + (p.opportunity || p.summary) + '\n' +
        '- **Challenge (Bottleneck)**: ' + p.challenge + '\n' +
        '- **Action (Methodology)**: ' + p.action + '\n' +
        '- **Resolution (Empirical Discovery)**: ' + p.resolution + '\n' +
        '- **Future Work (Open Horizons)**: ' + p.future_work + '\n\n' +
        '### Analysis Tasks Required:\n' +
        '1. **Executive Critique**: Synthesize the core biological or methodological leap of this study in 3 concise bullet points.\n' +
        '2. **Methods & Uncertainty Audit**: What are the underlying assumptions, failure modes (e.g. false merges, missing synapses, sample distortion), and validation controls in this approach?\n' +
        '3. **Claim vs. Evidence Check**: Identify the strongest verified claim and the most speculative interpretation made in this paper.\n' +
        '4. **Seminar Discussion Prompts**: Formulate 3 provocative discussion questions suitable for a graduate journal club debate.\n\n' +
        'Structure your response with clear markdown headings, concise paragraphs, and bullet points.';

      promptTextarea.value = prompt;
      return;
    }

    // Filtered set synthesis
    var vis = getVisibleCards();
    var totalCount = vis.length;
    var maxIncluded = Math.min(totalCount, 35);
    modalTitleEl.textContent = '🤖 AI Research Synthesis Prompt';
    modalDescEl.innerHTML = 'Copy this grounded prompt into <strong>ChatGPT</strong>, <strong>Claude</strong>, or <strong>Gemini</strong> across the <strong>' + totalCount + '</strong> currently filtered papers.';
    modalCountEl.textContent = totalCount;

    var cat = dimSel.value === 'all' ? 'All Connectomics Subfields' : dimSel.options[dimSel.selectedIndex].text;
    var era = eraSel.value === 'all' ? 'All Eras' : eraSel.options[eraSel.selectedIndex].text;

    var paperList = vis.slice(0, maxIncluded).map(function (card, idx) {
      var p = extractPaperCardData(card);
      var actStr = p.action ? '\n   Action: ' + p.action : '';
      var resStr = p.resolution ? '\n   Resolution: ' + p.resolution : '';
      return (idx + 1) + '. "' + p.title + '" (' + p.authors + ', ' + p.year + ', ' + p.journal + ')\n   Summary: ' + (p.summary || p.opportunity || 'Milestone contribution') + actStr + resStr;
    }).join('\n\n');

    var scopeDesc = totalCount <= 35
      ? 'based on the following ' + totalCount + ' curated milestone publications'
      : 'based on the top ' + maxIncluded + ' representative milestone publications (from ' + totalCount + ' matching papers in the active filter)';

    var prompt = '';
    if (currentPromptMode === 'methods') {
      prompt = 'You are a technical specialist in connectomics imaging, computer vision, and neural data pipelines.\n' +
        'Perform a comparative methodological audit ' + scopeDesc + ' in Domain = [' + cat + '] and Era = [' + era + '].\n\n' +
        '### Ground-Truth Papers (N = ' + maxIncluded + '):\n' + paperList + '\n\n' +
        '### Required Analysis Tasks:\n' +
        '1. **Technological Pipeline Evolution**: Map how imaging modalities, automated segmentation algorithms, and proofreading workflows have transformed across these works.\n' +
        '2. **Bottlenecks & Limitations**: What are the common failure modes, compute bottlenecks, and manual annotation burdens reported?\n' +
        '3. **Benchmarking & Validation**: How do these studies quantify accuracy (e.g. Rand error, synapse precision/recall, volumetric completeness)?\n' +
        '4. **Next-Generation Tools**: What pipeline innovations are urgently needed to scale to whole-brain mammalian connectomes?\n\n' +
        'Ground your findings strictly in the publications listed above with citations.';
    } else if (currentPromptMode === 'problems') {
      prompt = 'You are a senior neuroscience researcher and grant reviewer.\n' +
        'Identify open research problems and high-impact project proposals ' + scopeDesc + ' in Domain = [' + cat + '].\n\n' +
        '### Ground-Truth Papers (N = ' + maxIncluded + '):\n' + paperList + '\n\n' +
        '### Required Analysis Tasks:\n' +
        '1. **Persistent Scientific Blindspots**: What fundamental questions about circuit organization remain unanswered despite the progress in these papers?\n' +
        '2. **Top 3 High-Impact Research Proposals**: Outline 3 innovative 3-year research proposals addressing these gaps (specifying hypothesis, required connectomic data, and experimental validation).\n' +
        '3. **Cross-Disciplinary Synergies**: How can integration with transcriptomics, physiology (2P calcium imaging), or NeuroAI unlock deeper insights from these datasets?\n\n' +
        'Ground your synthesis in the cited publications.';
    } else if (currentPromptMode === 'seminar') {
      prompt = 'You are a university professor preparing a graduate seminar on connectomics.\n' +
        'Design a comprehensive journal club syllabus and active-learning discussion guide ' + scopeDesc + ' in [' + cat + '].\n\n' +
        '### Core Literature (N = ' + maxIncluded + '):\n' + paperList + '\n\n' +
        '### Required Seminar Components:\n' +
        '1. **Seminar Overview & Learning Objectives**: 3 clear learning outcomes for students.\n' +
        '2. **Core Debate Topics**: 3 provocative debate motions comparing competing interpretations or methods across these works.\n' +
        '3. **Critical Thinking Exercises**: Methodological critique prompts asking students to identify unaddressed confounding variables.\n' +
        '4. **Key Takeaway Cheat-Sheet**: A 5-point summary of foundational principles established by this literature.\n\n' +
        'Cite the relevant papers explicitly throughout.';
    } else {
      // Default: Comprehensive Literature Synthesis
      prompt = 'You are an expert computational neuroscientist and connectomics researcher.\n' +
        'Analyze and synthesize the state of research ' + scopeDesc + ' focusing on: Domain = [' + cat + '] and Era = [' + era + '].\n\n' +
        '### Ground-Truth Milestone Publications (N = ' + maxIncluded + (totalCount > 35 ? ' of ' + totalCount : '') + '):\n' + paperList + '\n\n' +
        '### Synthesis Tasks Required (grounded in the OCAR research framework):\n' +
        '1. **Current State of the Subfield (Opportunities)**: Executive summary of the biological and computational openings addressed by these studies.\n' +
        '2. **Core Technical Challenges**: Bottlenecks in acquisition, automated reconstruction, and proofreading documented in these works.\n' +
        '3. **Methodological Actions & Breakthroughs**: Core innovations in data volume, optical/EM resolution, and network graph analysis.\n' +
        '4. **Key Empirical Resolutions**: Definitive wiring motifs, recurrent loops, and cell-type discoveries established.\n' +
        '5. **Open Horizons & Future Outlook**: Top 3-5 high-priority research questions for the next 3-5 years.\n\n' +
        'Ground your analysis strictly in the ' + maxIncluded + ' publications listed above. Structure with clear markdown headings and explicit citations.';
    }

    promptTextarea.value = prompt;
  }

  // Open modal from filter bar button
  if (promptBtn) {
    promptBtn.addEventListener('click', function () {
      singlePaperTarget = null;
      document.getElementById('jc-prompt-mode-tabs').style.display = 'flex';
      generatePromptContent();
      copyStatus.classList.add('hidden');
      promptModal.classList.remove('hidden');
    });
  }

  // Single card AI Prompt click handler
  grid.addEventListener('click', function (e) {
    var aiBtn = e.target.closest('.jc-link-ai-prompt');
    if (aiBtn) {
      e.preventDefault();
      var card = aiBtn.closest('.jc-card');
      if (card) {
        singlePaperTarget = extractPaperCardData(card);
        document.getElementById('jc-prompt-mode-tabs').style.display = 'none';
        generatePromptContent();
        copyStatus.classList.add('hidden');
        promptModal.classList.remove('hidden');
      }
    }
  });

  // Prompt Mode Switching
  modeButtons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      modeButtons.forEach(function (b) {
        b.classList.remove('active');
        b.style.background = 'transparent';
        b.style.color = '#475569';
        b.style.fontWeight = '600';
      });
      btn.classList.add('active');
      btn.style.background = '#1a56db';
      btn.style.color = '#fff';
      btn.style.fontWeight = '700';
      currentPromptMode = btn.dataset.mode;
      generatePromptContent();
    });
  });

  if (promptCloseBtn) {
    promptCloseBtn.addEventListener('click', function () {
      promptModal.classList.add('hidden');
    });
  }

  // Reliable Copy-to-Clipboard
  if (copyBtn) {
    copyBtn.addEventListener('click', function () {
      promptTextarea.select();
      var text = promptTextarea.value;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () {
          copyStatus.classList.remove('hidden');
          setTimeout(function () { copyStatus.classList.add('hidden'); }, 3000);
        }).catch(function () {
          document.execCommand('copy');
          copyStatus.classList.remove('hidden');
          setTimeout(function () { copyStatus.classList.add('hidden'); }, 3000);
        });
      } else {
        document.execCommand('copy');
        copyStatus.classList.remove('hidden');
        setTimeout(function () { copyStatus.classList.add('hidden'); }, 3000);
      }
    });
  }

  tierSel.addEventListener('change', applyFilters);
  expSel.addEventListener('change', function () { setExpertise(this.value); });
  dimSel.addEventListener('change', applyFilters);
  eraSel.addEventListener('change', applyFilters);
  sortSel.addEventListener('change', function () { applySort(); applyFilters(); });
  searchInp.addEventListener('input', applyFilters);

  // Deep link from elsewhere on the site
  var params = new URLSearchParams(location.search);
  if (params.has('dimension') && dimSel.querySelector('option[value="' + CSS.escape(params.get('dimension')) + '"]')) {
    dimSel.value = params.get('dimension');
  }
  if (params.has('era') && eraSel.querySelector('option[value="' + CSS.escape(params.get('era')) + '"]')) {
    eraSel.value = params.get('era');
  }
  if (params.has('q')) searchInp.value = params.get('q');

  // Init
  setExpertise(expSel.value);
  applyFilters();

  if (location.hash.indexOf('#paper-') === 0) {
    jumpToPaper(location.hash.slice('#paper-'.length));
  }
})();
</script>
