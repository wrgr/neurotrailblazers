---
layout: default
title: "Research papers"
permalink: /technical-training/journal-club/
track: core-concepts-methods
pathways:
  - technical foundation
  - shared vocabulary
description: "Search connectomics papers by title, author, DOI, topic, or organism. Open an abstract and source-checked contribution notes, or switch to the citation map."
content_type: core
---

<div class="layout-content layout-page paper-browser-page">

{%- assign jc_dims = site.data.journal_papers.papers | map: 'dimension' | compact | uniq -%}
<section class="jc-hero">
  <h1>Research papers</h1>
  <p>Search {{ site.data.journal_papers.papers.size }} connectomics papers. Read abstracts and source-checked notes, or explore the citation graph.</p>
  <nav class="paper-view-links" aria-label="Paper view"><span aria-current="page">Paper list</span><a id="jc-graph-view" href="{{ '/technical-training/journal-club/graph/' | relative_url }}">Citation graph</a></nav>
  <p class="paper-view-help">Your search, topic, and organism carry between views.</p>
</section>


<section class="section section-compact">
  <div class="jc-filters paper-filter-panel" id="jc-filters" role="region" aria-labelledby="paper-filter-title">
    <div class="paper-filter-heading"><h2 id="paper-filter-title">Find and filter papers</h2><button type="button" id="jc-reset" class="btn btn-secondary">Clear filters</button></div>
    <div class="paper-filter-grid"><div class="paper-filter-field paper-search-field"><label for="jc-search">Search papers</label><input type="text" id="jc-search" placeholder="Title, author, DOI, or topic…"></div>
<div class="paper-filter-field"><label for="jc-dimension">Topic</label><select id="jc-dimension">
      <option value="all">All {{ jc_dims.size }} topics</option>
      {%- for dim in dims %}
      {%- assign mapped = site.data.content_tags.dimension_labels[dim] %}
      {%- if mapped %}{% assign label = mapped %}{% else %}{% assign label = dim | replace: '-', ' ' | capitalize %}{% endif %}
      <option value="{{ dim }}">{{ label }}</option>
      {%- endfor %}
    </select></div>
<div class="paper-filter-field"><label for="jc-organism">Organism</label><select id="jc-organism"><option value="all">All organisms</option><option value="mouse">Mouse</option><option value="drosophila">Drosophila</option><option value="human">Human</option><option value="c-elegans">C. elegans</option><option value="zebrafish">Zebrafish</option><option value="rat">Rat</option><option value="macaque">Macaque</option><option value="other">Other tagged systems</option><option value="unclassified">Not tagged / general</option></select></div>
<div class="paper-filter-field"><label for="jc-tier">Browse subset</label><select id="jc-tier">
      <option value="500">500-paper subset</option>
      <option value="1000">1,000-paper subset</option>
      <option value="2000" selected>All 2,000 papers</option>
    </select></div>
<div class="paper-filter-field"><label for="jc-era">Publication era</label><select id="jc-era">
      <option value="all">All eras</option>
      {%- for group in site.data.paper_views.era.groups %}
      <option value="{{ group.key }}">{{ group.label | capitalize }} ({{ group.n }})</option>
      {%- endfor %}
    </select></div>
<div class="paper-filter-field"><label for="jc-sort">Sort results</label><select id="jc-sort">
      <option value="year-desc">Newest first</option>
      <option value="year-asc">Oldest first</option>
      <option value="kcore-desc">Highest k-core first</option>
      <option value="dimension">By dimension</option>
    </select></div></div>
    <div class="paper-filter-actions"><span class="jc-filter-count" id="jc-count" role="status" aria-live="polite">Loading search; the first 20 papers are available below.</span><button type="button" id="jc-prompt-btn" class="jc-prompt-trigger-btn btn btn-secondary">Prepare a review prompt (<span id="jc-prompt-count">2000</span>)</button></div>
  </div>

  <!-- AI Synthesis Prompt Modal -->
  <div class="jc-prompt-modal hidden" id="jc-prompt-modal" role="dialog" aria-modal="true" aria-labelledby="jc-prompt-modal-title" style="position: fixed; inset: 0; background: rgba(15, 23, 42, 0.75); display: flex; align-items: center; justify-content: center; z-index: 1000; padding: 1.5rem;">
    <div class="jc-prompt-modal-content" style="background: #fff; border-radius: 12px; max-width: 720px; width: 100%; max-height: 90vh; display: flex; flex-direction: column; padding: 1.5rem; box-shadow: 0 20px 40px rgba(0,0,0,0.3); border: 1px solid #cbd5e1;">
      <div class="jc-prompt-modal-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
        <h3 style="margin: 0; font-size: 1.2rem; color: #0f172a;" id="jc-prompt-modal-title">Research review prompt</h3>
        <button class="jc-prompt-modal-close" id="jc-prompt-close" style="background: none; border: none; font-size: 1.5rem; cursor: pointer; color: #64748b; line-height: 1;" aria-label="Close">&times;</button>
      </div>
      <p class="jc-prompt-modal-desc" style="font-size: 0.84rem; color: #475569; margin: 0 0 0.75rem 0; line-height: 1.45;" id="jc-prompt-modal-desc">
        Copy this review prompt into <strong>ChatGPT</strong>, <strong>Claude</strong>, or <strong>Gemini</strong> to prepare a source-based review of the <strong id="jc-modal-paper-count">0</strong> papers currently filtered in your view.
      </p>

      <!-- Mode Switcher Tabs -->
      <div class="jc-prompt-modes" id="jc-prompt-mode-tabs" style="display: flex; gap: 0.35rem; margin-bottom: 0.75rem; background: #f1f5f9; padding: 0.25rem; border-radius: 8px;">
        <button type="button" class="jc-pmode-btn active" data-mode="synthesis">📑 Synthesis Review</button>
        <button type="button" class="jc-pmode-btn" data-mode="methods">🔬 Methods Compare</button>
        <button type="button" class="jc-pmode-btn" data-mode="problems">💡 Open Problems</button>
        <button type="button" class="jc-pmode-btn" data-mode="seminar">🎓 Seminar Guide</button>
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

  <p class="jc-shown-note" id="jc-shown-note">Search matches bibliographic text across the full corpus regardless of browse subset; topic and organism tags still filter results. Tags and citation metrics are navigation aids, not verified methods, affiliations, dataset use, or scientific quality. Abstracts are recorded publication text; contribution notes are shown only with a source and checking provenance.</p>
  <noscript><p>JavaScript is off: the first 20 papers are shown. For the complete catalog, <a href="{{ '/technical-training/journal-club/index-data.json' | relative_url }}">open the compact paper index</a>.</p></noscript>

  <div class="jc-grid" id="jc-grid" data-index-url="{{ '/technical-training/journal-club/index-data.json' | relative_url }}?v={{ site.time | date: '%s' }}" data-detail-base="{{ '/technical-training/journal-club/details/' | relative_url }}" data-version="{{ site.time | date: '%s' }}">
    {% assign sorted_papers = site.data.journal_papers.papers | sort: "year" | reverse %}
    {% for paper in sorted_papers limit: 20 %}
      {% include cards/journal-paper-card.html paper=paper %}
    {% endfor %}
  </div>
  <nav class="paper-pagination" aria-label="Paper result pages"><button type="button" id="jc-prev" disabled>Previous</button><span id="jc-page-status" role="status"></span><button type="button" id="jc-next" disabled>Next</button></nav>
  <div class="jc-empty hidden" id="jc-empty">No papers match your filters. Try broadening your search.</div>
</section>

<details class="secondary-options"><summary>Corpus navigation and reuse</summary><div class="jc-paths">{% for group in site.data.paper_views.reading_paths.groups %}<div class="jc-path-card"><h3>{{ group.label }}</h3><p>{{ group.description }}</p></div>{% endfor %}</div><p>Source-checked contribution notes and review prompts are Nanoscale material under CC BY 4.0. <a href="{{ '/about/#cite-this-site' | relative_url }}">How to cite this site</a>. Publications remain the property of their publishers. Source-checked notes identify the source used and checking limits; they are not expert peer review. Historical generated notes are not published.</p></details>

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


<script src="{{ '/assets/js/paper-browser.js' | relative_url }}?v={{ site.time | date: '%s' }}" defer></script>
