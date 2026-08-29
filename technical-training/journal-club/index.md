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

<section class="jc-hero">
  <h1>Journal Club &amp; Research Corpus</h1>
  <p>{{ site.data.journal_papers.papers.size }} connectomics papers &mdash; a multi-tiered literature network selected by their place in the field's citation graph &mdash; each presented with the OCAR framework (Opportunity, Challenge, Action, Resolution, Future Work), 3-level summaries, and seminar discussion prompts.</p>
  <div class="jc-hero-stats">
    <span class="jc-hero-stat">{{ site.data.journal_papers.papers.size }} Total Papers</span>
    <span class="jc-hero-stat">12 Research Domains</span>
    <span class="jc-hero-stat">3 Expertise Levels</span>
    <span class="jc-hero-stat">3 Tiers (500 / 1,000 / 2,000)</span>
  </div>
</section>

<section class="section section-compact">
  <p>Browse the canonical connectomics literature across 12 research domains and 3 nested tiers. Use this page to survey what exists, filter by domain/organism/era, or follow the citation graph between papers. For an interactive network visualization with self-organizing organic force physics and AI synthesis prompts, explore the graph below:</p>
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
      <option value="all">All 12 dimensions</option>
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

    <span class="jc-filter-count" id="jc-count"></span>
  </div>

  {%- assign shown_papers = site.data.journal_papers.papers | where_exp: "p", "p.tier <= 500" -%}
  <p class="jc-shown-note">Showing the {{ shown_papers.size }} flagship papers in the <strong>Top 500 Core</strong> (selected by citation centrality and stratified across 12 domains) with complete OCAR research cards and 3-level summaries. Use the tier selector above to expand to 1,000 or 2,000 papers, or explore the <a href="{{ '/technical-training/journal-club/graph/' | relative_url }}">interactive citation graph</a>.</p>

  <div class="jc-grid" id="jc-grid">
    {% assign sorted_papers = shown_papers | sort: "year" | reverse %}
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
    emptyEl.classList.toggle('hidden', visible > 0);
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

  tierSel.addEventListener('change', applyFilters);
  expSel.addEventListener('change', function () { setExpertise(this.value); });
  dimSel.addEventListener('change', applyFilters);
  eraSel.addEventListener('change', applyFilters);
  sortSel.addEventListener('change', function () { applySort(); applyFilters(); });
  searchInp.addEventListener('input', applyFilters);

  // Deep link from elsewhere on the site: ?dimension=connectomics&era=sota&q=flywire
  // pre-sets the filter controls so other pages can link straight into a filtered
  // view of the collection instead of just the unfiltered top-level page.
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

  // Deep link: /technical-training/journal-club/#paper-<id> jumps straight to a card
  // (used by the citation graph and by related-work links).
  if (location.hash.indexOf('#paper-') === 0) {
    jumpToPaper(location.hash.slice('#paper-'.length));
  }
})();
</script>
