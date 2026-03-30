---
layout: default
title: "Journal Club"
permalink: /technical-training/journal-club/
description: "Interactive journal club with 100+ curated connectomics papers. Filter by expertise level, dimension, or keyword. Each paper presented with the OCAR framework — Opportunity, Challenge, Action, Resolution, and Future Work."
---

<div class="layout-content layout-page">

<section class="jc-hero">
  <h1>Journal Club</h1>
  <p>{{ site.data.journal_papers.papers.size }} curated connectomics papers across 11 dimensions, each presented with the OCAR framework &mdash; Opportunity, Challenge, Action, Resolution, and Future Work.</p>
  <div class="jc-hero-stats">
    <span class="jc-hero-stat">{{ site.data.journal_papers.papers.size }} papers</span>
    <span class="jc-hero-stat">11 dimensions</span>
    <span class="jc-hero-stat">3 expertise levels</span>
    <span class="jc-hero-stat">1986 &ndash; 2025</span>
  </div>
</section>

<section class="section section-compact">
  <h2 style="margin-top:0">Suggested Reading Paths</h2>
  <div class="jc-paths">
    <div class="jc-path-card">
      <h3>Historical Arc</h3>
      <p>White 1986 &rarr; Denk &amp; Horstmann 2004 &rarr; Briggman &amp; Bock 2012 &rarr; Kasthuri 2015 &rarr; Zheng 2018 &rarr; Dorkenwald 2024</p>
    </div>
    <div class="jc-path-card">
      <h3>Methods Deep Dive</h3>
      <p><strong>Imaging:</strong> Xu 2017 &rarr; Yin 2020<br>
         <strong>Segmentation:</strong> Turaga 2010 &rarr; Januszewski 2018 &rarr; Sheridan 2023<br>
         <strong>Proofreading:</strong> Plaza 2014 &rarr; Dorkenwald 2022</p>
    </div>
    <div class="jc-path-card">
      <h3>Analysis &amp; Interpretation</h3>
      <p>Bullmore &amp; Sporns 2009 &rarr; Rubinov &amp; Sporns 2010 &rarr; Winding 2023 &rarr; Lappalainen 2024</p>
    </div>
    <div class="jc-path-card">
      <h3>Cross-Scale (EM + MRI)</h3>
      <p>Sporns 2005 &rarr; Maier-Hein 2017 &rarr; Glasser 2016 &rarr; Bae 2021 &rarr; Bassett &amp; Sporns 2017</p>
    </div>
  </div>
</section>

<section class="section section-compact">
  <div class="jc-filters" id="jc-filters">
    <label for="jc-expertise">Expertise:</label>
    <select id="jc-expertise">
      <option value="beginner">Beginner</option>
      <option value="intermediate" selected>Intermediate</option>
      <option value="advanced">Advanced</option>
    </select>

    <label for="jc-dimension">Dimension:</label>
    <select id="jc-dimension">
      <option value="all">All dimensions</option>
      <option value="neuroanatomy">Neuroanatomy</option>
      <option value="imaging">Imaging &amp; Sample Prep</option>
      <option value="computer-vision-ml">Computer Vision &amp; ML</option>
      <option value="data-storage">Data Storage &amp; Pipelines</option>
      <option value="proofreading">Proofreading &amp; QC</option>
      <option value="cell-types">Cell Types</option>
      <option value="connectomics">Graph Construction</option>
      <option value="network-analysis">Network Analysis</option>
      <option value="mri-connectomics">MRI Connectomics</option>
      <option value="neuroai">NeuroAI &amp; Modeling</option>
      <option value="case-studies">Case Studies</option>
    </select>

    <label for="jc-sort">Sort:</label>
    <select id="jc-sort">
      <option value="year-desc">Newest first</option>
      <option value="year-asc">Oldest first</option>
      <option value="dimension">By dimension</option>
    </select>

    <label for="jc-search">Search:</label>
    <input type="text" id="jc-search" placeholder="keyword, author, tag…">

    <span class="jc-filter-count" id="jc-count"></span>
  </div>

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
  var expSel    = document.getElementById('jc-expertise');
  var dimSel    = document.getElementById('jc-dimension');
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

  // Tag click to search
  grid.addEventListener('click', function (e) {
    var tag = e.target.closest('.jc-tag');
    if (!tag) return;
    searchInp.value = tag.dataset.tag;
    applyFilters();
  });

  function applyFilters() {
    var dim    = dimSel.value;
    var query  = searchInp.value.toLowerCase().trim();
    var visible = 0;

    cards.forEach(function (card) {
      var matchDim   = dim === 'all' || card.dataset.dimension === dim;
      var matchQuery = !query ||
        card.textContent.toLowerCase().indexOf(query) !== -1 ||
        (card.dataset.tags && card.dataset.tags.toLowerCase().indexOf(query) !== -1);
      var show = matchDim && matchQuery;
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
    } else if (val === 'dimension') {
      sorted.sort(function (a, b) { return a.dataset.dimension.localeCompare(b.dataset.dimension); });
    }
    sorted.forEach(function (card) { grid.appendChild(card); });
  }

  expSel.addEventListener('change', function () { setExpertise(this.value); });
  dimSel.addEventListener('change', function () { applyFilters(); });
  sortSel.addEventListener('change', function () { applySort(); applyFilters(); });
  searchInp.addEventListener('input', function () { applyFilters(); });

  // Init
  setExpertise(expSel.value);
  applyFilters();
})();
</script>
