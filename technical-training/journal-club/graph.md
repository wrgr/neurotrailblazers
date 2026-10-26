---
layout: default
title: "Papers and citations"
permalink: /technical-training/journal-club/graph/
track: core-concepts-methods
pathways:
  - technical foundation
  - shared vocabulary
description: "Search 2,000 connectomics papers, read abstracts, and explore the papers they cite and the works that cite them."
content_type: core
---

<div class="layout-content layout-page jcg-page">

<section class="jc-hero">
  <h1>Research papers</h1><nav class="paper-view-links" aria-label="Paper view"><a id="jcg-list-view" href="{{ '/technical-training/journal-club/' | relative_url }}">Paper list</a><span aria-current="page">Citation graph</span></nav>
  <p>Find a paper, read its abstract, then explore the works it cites and the papers that cite it.</p>
</section>

<section class="section section-compact">
  <h2 class="paper-filter-title">Find and filter papers</h2>
  <div class="jcg-basic-controls">
      <!-- Search Filter -->
      <div class="jcg-control-group">
        <label for="jcg-search">Search papers:</label>
        <input type="text" id="jcg-search" placeholder="e.g. MICrONS, Kasthuri, proofreading, U-Net...">
      </div>

      <!-- Category Filter -->
      <div class="jcg-control-group">
        <label for="jcg-dimension">Topic:</label>
        <select id="jcg-dimension">
          <option value="all">All categories</option>
          <option value="circuit-structure">Circuit Structure</option>
          <option value="pipeline">Pipeline &amp; Software</option>
          <option value="physiology">Physiology</option>
          <option value="behaviour">Behaviour</option>
          <option value="imaging">Imaging &amp; Optics</option>
          <option value="cell-types">Cell Types &amp; Census</option>
          <option value="neuroanatomy">Neuroanatomy</option>
          <option value="synthesis">Synthesis &amp; Reviews</option>
          <option value="dataset">Datasets &amp; Volumes</option>
          <option value="neuroai">NeuroAI &amp; Models</option>
          <option value="health">Health &amp; Disease</option>
          <option value="training-outreach">Training &amp; Outreach</option>
          <option value="other">Other / unclassified</option>
          <option value="mri">MRI</option>
        </select>
      </div>

      <!-- Organism Filter -->
      <div class="jcg-control-group">
        <label for="jcg-organism">Organism:</label>
        <select id="jcg-organism">
          <option value="all">All Organisms</option>
          <option value="mouse">Mouse (Mus musculus)</option>
          <option value="drosophila">Drosophila (Fruit Fly)</option>
          <option value="human">Human Cortex</option>
          <option value="c-elegans">C. elegans</option>
          <option value="zebrafish">Zebrafish</option>
          <option value="rat">Rat</option>
          <option value="macaque">Macaque</option>
          <option value="other">Other tagged systems</option>
          <option value="unclassified">Not tagged / general</option>
        </select>
      </div>

      <p class="jcg-hint">Organism filters use corpus tags. Papers without an organism tag appear under “Not tagged / general”.</p>

  </div>
  <div class="jcg-basic-actions"><button id="jcg-reset" type="button" class="jcg-secondary-btn">Clear filters</button><p class="jcg-count" id="jcg-count" role="status" aria-live="polite">Loading papers…</p></div>
  <p class="jcg-hint">Search publication titles, authors, journals, and DOI identifiers. Topic and organism tags narrow results but do not establish dataset use or findings.</p>
  <div class="paper-graph-layout">      <!-- Layout Mode -->
      <div class="jcg-control-group">
        <label for="jcg-layout-buttons">Map layout:</label>
        <div class="jcg-tier-btn-group" id="jcg-layout-buttons">
          <button type="button" class="jcg-layout-btn" data-mode="organic">Free layout</button>
          <button type="button" class="jcg-layout-btn active" data-mode="cluster">Group by topic</button>
          <button type="button" class="jcg-layout-btn" data-mode="timeline">Timeline</button>
        </div>
      </div>

</div>
    <details class="jcg-filter-panel" id="jcg-filter-panel">
      <summary>Display and additional filters</summary>
      <div class="jcg-controls">

      <!-- Tier Selector -->
      <div class="jcg-control-group">
        <label for="jcg-tier-buttons">Browse subset (ranked by citation metrics):</label>
        <div class="jcg-tier-btn-group" id="jcg-tier-buttons">
          <button type="button" class="jcg-tier-btn" data-tier="500">Top 500</button>
          <button type="button" class="jcg-tier-btn" data-tier="1000">Top 1,000</button>
          <button type="button" class="jcg-tier-btn active" data-tier="2000">All 2,000</button>
        </div>
      </div>

      <!-- Edge Controls -->
      <fieldset class="jcg-era-fieldset">
        <legend>Citation links</legend>
        <label><input type="checkbox" id="jcg-show-edges" checked> Draw Citation Edges</label>
        <label><input type="checkbox" id="jcg-all-edges"> Show all links (dense overview)</label>
        <p class="jcg-hint">Select a paper to see its citation links. Enable all links for the full network.</p>
        <label><input type="checkbox" id="jcg-show-arrows"> Show Directional Arrows (&rarr;)</label>
        <label><input type="checkbox" id="jcg-show-flow"> ⚡ Flow Pulse Animation</label>
        <div style="margin-top: 0.35rem;">
          <label for="jcg-edge-weighting" style="font-size: 0.76rem; font-weight: 600; color: #374151; display: block; margin-bottom: 0.2rem;">Edge Weighting / Thickness:</label>
          <select id="jcg-edge-weighting" style="padding: 0.35rem 0.5rem; font-size: 0.78rem;">
            <option value="sum" selected>Combined Degree (In + Out Sum)</option>
            <option value="in">Inbound Degree (Target / Cited Authority)</option>
            <option value="out">Outbound Degree (Source / Citing Reach)</option>
            <option value="both">Harmonic Mean (Both Nodes)</option>
            <option value="uniform">Uniform Solid Lines</option>
          </select>
        </div>
      </fieldset>

      <!-- Node Color Cue Selector -->
      <div class="jcg-control-group">
        <label for="jcg-color-by">Color papers by:</label>
        <select id="jcg-color-by">
          <option value="dimension">Category / Subfield</option>
          <option value="era">Publication period</option>
          <option value="tier">Corpus Tier (500 / 1000 / 2000)</option>
          <option value="organism">Model Organism (Mouse, Fly, Human, etc.)</option>
          <option value="citation_role">Imported network role (not evidence)</option>
        </select>
      </div>

      <!-- Era Filter -->
      <fieldset class="jcg-era-fieldset">
        <legend>Publication Era</legend>
        <label><input type="checkbox" class="jcg-era-check" value="history" checked> 2018 and earlier</label>
        <label><input type="checkbox" class="jcg-era-check" value="contemporary" checked> 2019–2023</label>
        <label><input type="checkbox" class="jcg-era-check" value="sota" checked> 2024 onwards</label>
      </fieldset>

      <!-- Minimum Centrality / Degree -->
      <div class="jcg-control-group">
        <label for="jcg-min-degree">Minimum citation metric: <span id="jcg-degree-val">0</span></label>
        <input type="range" id="jcg-min-degree" min="0" max="60" value="0" step="1">
      </div>

      <!-- Action Buttons -->
      <div class="jcg-control-group" style="margin-top: 0.25rem; gap: 0.4rem;">
        <button id="jcg-prompt-btn" type="button" class="jcg-secondary-btn" style="width:100%; font-weight:600;">
          Create a discussion prompt (<span id="jcg-prompt-count">500</span>)
        </button>
        <div style="display: flex; gap: 0.4rem;">
          <button id="jcg-sidebar-fit" type="button" class="jcg-secondary-btn" style="flex:1;">Fit map</button>
          <button id="jcg-sidebar-reheat" type="button" class="jcg-secondary-btn" style="flex:1;">Relax free layout</button>
        </div>
      </div>



      <p class="jcg-hint">Drag the map to move it. Scroll or pinch to zoom. Select a paper to read its abstract.</p>

      <div class="jcg-legend-title" id="jcg-legend-title" style="font-weight:700; font-size:0.78rem; color:#374151; margin-top:0.4rem;">Color Cue Legend:</div>
      <div class="jcg-legend" id="jcg-legend"></div>
    </div>

    </details>
  <div class="jcg-layout">

    <!-- Controls Sidebar -->


    <!-- Canvas Container & Interactive Drawer -->
      <section class="jcg-results" aria-labelledby="jcg-results-title">
        <h2 id="jcg-results-title">Papers</h2>
        <p id="jcg-results-status" role="status"></p>
        <ul id="jcg-results-list"></ul>
        <button type="button" id="jcg-results-more" class="jcg-secondary-btn hidden">Show more papers</button>
      </section>
    <div class="jcg-graph-column">


      <div class="jcg-canvas-wrap">
        <canvas id="jcg-canvas" role="img" aria-label="Citation network. Use the matching paper list to open paper details."></canvas>
        <p class="jcg-empty hidden" id="jcg-empty">No papers match these filters. Clear the search or reset the filters.</p>

        <!-- On-Canvas Floating HUD Controls -->
        <div class="jcg-canvas-hud">
          <button type="button" id="jcg-hud-zoom-in" title="Zoom In">+</button>
          <button type="button" id="jcg-hud-zoom-out" title="Zoom Out">&minus;</button>
          <button type="button" id="jcg-hud-fit" title="Fit to Screen">⛶</button>
          <button type="button" id="jcg-hud-reheat" title="Reheat Physics &amp; Relax Layout">⚡</button>
        </div>

        <!-- Subgraph Focus Mode Active Banner -->
        <div class="jcg-focus-banner hidden" id="jcg-focus-banner">
          <span>Citations for: <strong id="jcg-focus-paper-title">Paper</strong></span>
          <button type="button" id="jcg-focus-exit-btn" title="Exit Focus Mode">Back to results</button>
        </div>

        <div class="jcg-tooltip hidden" id="jcg-tooltip"></div>

        <!-- Source-checked publication detail drawer -->
        <div class="jcg-panel hidden" id="jcg-panel" role="region" aria-label="Selected paper details">
          <button class="jcg-panel-close" id="jcg-panel-close" aria-label="Close">&times;</button>
          <div class="jcg-panel-body" id="jcg-panel-body">
            <!-- Source-checked contributions, abstract, and recorded citation links -->
          </div>
        </div>
      </div>



      <!-- Optional review prompts; not automated scientific findings -->
      <div class="jcg-ai-tray collapsed" id="jcg-ai-tray">
        <div class="jcg-ai-tray-header" id="jcg-ai-tray-header">
          <h3 id="jcg-prompt-modal-title">Optional discussion prompts</h3>
          <div style="display: flex; align-items: center; gap: 0.5rem;">
            <span style="font-size: 0.75rem; color: #64748b;" id="jcg-tray-status-text">Click to expand</span>
            <button type="button" class="jcg-ai-tray-toggle-btn" id="jcg-ai-tray-toggle">▾ Expand Tray</button>
          </div>
        </div>

        <div class="jcg-ai-tray-body">
          <p class="jcg-prompt-modal-desc" id="jcg-prompt-modal-desc" style="margin-bottom: 0.75rem; color: #475569; font-size: 0.82rem;">
            Copy this review prompt into <strong>ChatGPT</strong>, <strong>Claude</strong>, or <strong>Gemini</strong> across the <strong id="jcg-modal-paper-count">0</strong> papers currently in your active filter.
          </p>

          <!-- Mode Switcher Tabs -->
          <div class="jcg-prompt-modes" id="jcg-prompt-mode-tabs" style="display: flex; flex-wrap: wrap; gap: 0.35rem; margin-bottom: 0.75rem; background: #f1f5f9; padding: 0.25rem; border-radius: 8px;">
            <button type="button" class="jcg-pmode-btn active" data-mode="synthesis">📑 Synthesis Review</button>
            <button type="button" class="jcg-pmode-btn" data-mode="methods">🔬 Methods Compare</button>
            <button type="button" class="jcg-pmode-btn" data-mode="problems">💡 Open Problems</button>
            <button type="button" class="jcg-pmode-btn" data-mode="seminar">🎓 Seminar Guide</button>
          </div>

          <div class="jcg-prompt-box" style="margin-bottom: 0.75rem;">
            <textarea id="jcg-prompt-textarea" readonly style="width: 100%; height: 220px; box-sizing: border-box; padding: 0.75rem; font-family: monospace; font-size: 0.78rem; border: 1px solid #cbd5e1; border-radius: 6px; background: #f8fafc; color: #1e293b; resize: vertical; line-height: 1.4;"></textarea>
          </div>
          <div class="jcg-prompt-modal-footer" style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.75rem;">
            <div style="display: flex; align-items: center; gap: 0.5rem;">
              <button type="button" class="jcg-copy-btn" id="jcg-copy-prompt-btn">
                📋 Copy Prompt
              </button>
              <span class="jcg-copy-status hidden" id="jcg-copy-status">✅ Copied to clipboard!</span>
            </div>
            <div style="display: flex; align-items: center; gap: 0.4rem;">
              <a href="https://chatgpt.com/" target="_blank" rel="noopener" style="background: #10a37f; color: #fff; padding: 0.4rem 0.7rem; border-radius: 6px; font-size: 0.78rem; font-weight: 600; text-decoration: none; display: inline-flex; align-items: center; gap: 0.25rem;">💬 ChatGPT &rarr;</a>
              <a href="https://claude.ai/new" target="_blank" rel="noopener" style="background: #d97706; color: #fff; padding: 0.4rem 0.7rem; border-radius: 6px; font-size: 0.78rem; font-weight: 600; text-decoration: none; display: inline-flex; align-items: center; gap: 0.25rem;">🟣 Claude &rarr;</a>
              <a href="https://gemini.google.com/app" target="_blank" rel="noopener" style="background: #2563eb; color: #fff; padding: 0.4rem 0.7rem; border-radius: 6px; font-size: 0.78rem; font-weight: 600; text-decoration: none; display: inline-flex; align-items: center; gap: 0.25rem;">✨ Gemini &rarr;</a>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</section>

</div>

<style>
.jcg-layout { display: grid; grid-template-columns: 280px minmax(0, 1fr); gap: 1.25rem; align-items: start; margin-top: 1rem; }
@media (max-width: 960px) { .jcg-layout { grid-template-columns: 1fr; } }
.jcg-page { max-width: 1440px; }
.jcg-page .jc-hero { padding: 1.5rem; }
.jcg-page .section { max-width: none; padding: 0; }
.jcg-page .jc-hero h1 { color: inherit; }
.jcg-graph-column { display: flex; flex-direction: column; gap: 1rem; min-width: 0; }
.jcg-page .jcg-filter-panel { margin: 0; padding: 0; border: 0; min-width: 0; background: transparent; }
.jcg-page .jcg-filter-panel > summary { display: block; padding: 0.65rem 1.8rem; border: 1px solid #cbd5e1; border-radius: 8px; }
.jcg-empty { position: absolute; top: 35%; left: 10%; right: 10%; text-align: center; color: #475569; }
.jcg-results { border: 1px solid #e2e8f0; border-radius: 10px; padding: 1rem; background: #fff; }
.jcg-results h2 { font-size: 1rem; margin: 0; }
#jcg-results-status { color: #64748b; font-size: 0.82rem; }
#jcg-results-list { list-style: none; margin: 0; padding: 0; max-height: 320px; overflow-y: auto; }
#jcg-results-list li { content-visibility: auto; contain-intrinsic-size: auto 70px; border-top: 1px solid #e2e8f0; }
.jcg-result-btn { width: 100%; border: 0; background: transparent; color: #1e293b; text-align: left; padding: 0.65rem; cursor: pointer; }
.jcg-result-btn:hover { background: #eff6ff; }
.jcg-result-btn small { display: block; color: #64748b; margin-top: 0.25rem; }
.jcg-page button, .jcg-page select, #jcg-search, .jcg-page summary, .jcg-drawer-btn { min-height: 44px; }
.jcg-page button { min-width: 44px; }
.jcg-era-fieldset > label { min-height: 44px; display: flex; align-items: center; gap: 0.3rem; }
#jcg-min-degree { min-height: 44px; }
.jcg-page button:active { filter: brightness(0.92); }
.jcg-page button:focus-visible, .jcg-page select:focus-visible, .jcg-page input:focus-visible { outline: 3px solid #2563eb; outline-offset: 2px; }
@media (max-width: 960px) {
  .jcg-page .jcg-filter-panel > summary { display: block; padding: 0.6rem 1.8rem; border: 1px solid #cbd5e1; border-radius: 8px; }
  .jcg-page { padding: 0 0.75rem 1rem; }
  .jcg-page .jc-hero { padding: 1rem; }
  .jcg-controls { max-height: 420px; overflow-y: auto; }
}
.jcg-controls { display: flex; flex-direction: column; gap: 0.75rem; font-size: 0.85rem; background: #fafafa; border: 1px solid #e5e7eb; border-radius: 10px; padding: 1.25rem; }
.jcg-control-group { display: flex; flex-direction: column; gap: 0.3rem; }
.jcg-control-group label { font-weight: 600; color: #374151; font-size: 0.82rem; }

.jcg-tier-btn-group { display: flex; border: 1px solid #d1d5db; border-radius: 6px; overflow: hidden; background: #fff; }
.jcg-tier-btn, .jcg-layout-btn { flex: 1; padding: 0.4rem 0.2rem; font-size: 0.75rem; font-weight: 600; border: none; background: transparent; cursor: pointer; color: #4b5563; transition: all 0.15s ease; text-align: center; }
.jcg-tier-btn:not(:last-child), .jcg-layout-btn:not(:last-child) { border-right: 1px solid #d1d5db; }
.jcg-tier-btn.active, .jcg-layout-btn.active { background: #1a56db; color: #fff; }
.jcg-tier-btn:hover:not(.active), .jcg-layout-btn:hover:not(.active) { background: #f3f4f6; }

/* Prompt-mode selector in the AI synthesis modal. Its selected state was written
   as inline styles from the click handler while an `active` class was toggled
   that no rule matched -- unlike the tier and layout buttons directly above,
   which have always done it in CSS. Same treatment as those now. */
.jcg-pmode-btn { flex: 1; min-width: 130px; padding: 0.35rem 0.5rem; font-size: 0.76rem; font-weight: 600; border: none; border-radius: 6px; background: transparent; color: #475569; cursor: pointer; }
.jcg-pmode-btn.active { background: #1a56db; color: #fff; font-weight: 700; }
.jcg-pmode-btn:hover:not(.active) { background: #e2e8f0; }

.jcg-era-fieldset { border: 1px solid #d1d5db; border-radius: 6px; padding: 0.5rem 0.75rem; background: #fff; }
.jcg-era-fieldset legend { font-weight: 700; font-size: 0.78rem; padding: 0 0.3rem; color: #374151; }
.jcg-era-fieldset label { display: block; font-weight: 400; font-size: 0.8rem; margin: 0.2rem 0; cursor: pointer; }

.jcg-controls select, #jcg-search {
  width: 100%; box-sizing: border-box; padding: 0.45rem 0.6rem;
  border: 1px solid #d1d5db; border-radius: 6px; background: #fff;
  font-size: 0.82rem; color: #374151;
}
.jcg-controls input[type="range"] { width: 100%; }

.jcg-prompt-trigger-btn {
  background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
  color: #fff; border: none; border-radius: 6px; padding: 0.6rem 0.8rem;
  font-size: 0.82rem; font-weight: 600; cursor: pointer; transition: all 0.15s ease;
  box-shadow: 0 2px 6px rgba(124, 58, 237, 0.25); text-align: center;
}
.jcg-prompt-trigger-btn:hover { opacity: 0.95; transform: translateY(-1px); box-shadow: 0 4px 10px rgba(124, 58, 237, 0.35); }

.jcg-secondary-btn {
  background: #fff; border: 1px solid #d1d5db; border-radius: 6px;
  padding: 0.4rem 0.6rem; cursor: pointer; font-weight: 600; font-size: 0.78rem; color: #4b5563;
  transition: all 0.15s ease;
}
.jcg-secondary-btn:hover { background: #f3f4f6; color: #1e293b; }

#jcg-reset {
  background: #fff; border: 1px solid #d1d5db; border-radius: 6px;
  padding: 0.45rem 0.8rem; cursor: pointer; font-weight: 600; font-size: 0.8rem; color: #4b5563;
}
#jcg-reset:hover { background: #f3f4f6; }
.jcg-count { font-weight: 600; color: #1a56db; margin: 0; font-size: 0.85rem; }
.jcg-hint { color: #6b7280; font-size: 0.75rem; margin: 0; line-height: 1.35; }

.jcg-legend { display: grid; grid-template-columns: 1fr 1fr; gap: 0.3rem; margin-top: 0.2rem; }
.jcg-legend-item { display: flex; align-items: center; gap: 0.35rem; font-size: 0.72rem; color: #4b5563; }
.jcg-legend-swatch { width: 9px; height: 9px; border-radius: 50%; display: inline-block; flex-shrink: 0; }

.jcg-canvas-wrap { position: relative; background: #ffffff; border: 1px solid #e5e7eb; border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.06); overflow: hidden; height: clamp(420px, 72vh, 760px); }
#jcg-canvas { display: block; width: 100%; height: 100%; cursor: grab; touch-action: none; }
#jcg-canvas.dragging { cursor: grabbing; }

/* Floating Canvas HUD */
.jcg-canvas-hud {
  position: absolute; bottom: 1.25rem; right: 1.25rem; display: flex; flex-direction: column; gap: 0.35rem;
  z-index: 15; background: rgba(255, 255, 255, 0.92); backdrop-filter: blur(8px);
  padding: 0.35rem; border-radius: 8px; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.jcg-canvas-hud button {
  width: 44px; height: 44px; border: 1px solid #cbd5e1; border-radius: 6px;
  background: #fff; color: #334155; font-size: 1rem; font-weight: 700;
  display: flex; align-items: center; justify-content: center; cursor: pointer; transition: all 0.15s ease;
}
.jcg-canvas-hud button:hover { background: #1a56db; color: #fff; border-color: #1a56db; }

/* Subgraph Focus Banner */
.jcg-focus-banner {
  position: absolute; top: 1rem; left: 1rem; z-index: 15;
  background: rgba(15, 23, 42, 0.92); backdrop-filter: blur(8px); color: #fff;
  padding: 0.5rem 0.85rem; border-radius: 8px; font-size: 0.82rem; display: flex; align-items: center; gap: 0.8rem;
  box-shadow: 0 4px 16px rgba(0,0,0,0.25); border: 1px solid #334155; max-width: calc(100% - 2rem);
}
.jcg-focus-banner.hidden { display: none; }
.jcg-focus-banner span { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.jcg-focus-banner strong { color: #38bdf8; }
.jcg-focus-banner button {
  background: #ef4444; color: #fff; border: none; border-radius: 4px; padding: 0.25rem 0.55rem;
  font-size: 0.72rem; font-weight: 700; cursor: pointer; white-space: nowrap; transition: opacity 0.15s;
}
.jcg-focus-banner button:hover { opacity: 0.85; }

.jcg-tooltip {
  position: absolute; pointer-events: none; z-index: 10;
  background: rgba(15, 23, 42, 0.96); color: #fff; border-radius: 8px;
  padding: 0.6rem 0.85rem; font-size: 0.78rem; line-height: 1.45;
  max-width: 320px; box-shadow: 0 6px 20px rgba(0,0,0,0.3);
  transform: translate(14px, 14px); border: 1px solid #334155;
}
.jcg-tooltip.hidden { display: none; }
.jcg-tooltip strong { display: block; font-size: 0.88rem; margin-bottom: 0.2rem; color: #60a5fa; line-height: 1.3; }
.jcg-tooltip .meta { color: #cbd5e1; font-size: 0.73rem; margin-bottom: 0.35rem; }
.jcg-tooltip .ocar-preview { color: #94a3b8; font-size: 0.72rem; border-top: 1px solid #334155; padding-top: 0.35rem; margin-top: 0.35rem; }

/* Rich Slide-Out Drawer */
.jcg-panel {
  position: absolute; top: 1rem; right: 1rem; width: min(480px, calc(100% - 2rem));
  box-sizing: border-box; background: #ffffff; border-radius: 12px; box-shadow: 0 12px 36px rgba(0,0,0,0.22);
  border: 1px solid #cbd5e1; padding: 1.35rem; max-height: calc(100% - 2rem); overflow-y: auto; z-index: 20;
}
.jcg-panel.hidden { display: none; }
.jcg-panel-close {
  position: absolute; top: 0.75rem; right: 0.85rem; background: none; border: none;
  font-size: 1.5rem; line-height: 1; cursor: pointer; color: #64748b; padding: 0.2rem; min-width: 44px; min-height: 44px;
}
.jcg-panel-close:hover { color: #0f172a; }

@media (max-width: 768px) {
  .jcg-canvas-wrap { height: clamp(360px, 55vh, 520px); border-radius: 8px; }
  .jcg-panel {
    top: auto; bottom: 0; left: 0; right: 0;
    width: 100%; max-width: 100%;
    max-height: 85%; border-radius: 16px 16px 0 0;
    padding: 1.1rem; box-shadow: 0 -8px 30px rgba(0,0,0,0.25);
  }
  .jcg-prompt-modal { padding: 0.75rem; }
  .jcg-prompt-modal-content { max-height: 94vh; padding: 1rem; }
}

.jcg-panel-body h3 { margin: 0 2.5rem 0.4rem 0; font-size: 1.1rem; line-height: 1.35; color: #0f172a; font-weight: 700; }
.jcg-panel-authors { font-size: 0.82rem; color: #64748b; margin-bottom: 0.6rem; }
.jcg-panel-meta-tags { display: flex; flex-wrap: wrap; gap: 0.35rem; margin-bottom: 0.85rem; }
.jcg-panel-tag { background: #f1f5f9; border-radius: 4px; padding: 0.18rem 0.45rem; font-size: 0.72rem; color: #475569; font-weight: 600; }
.jcg-panel-tag.tier-tag { background: #dbeafe; color: #1d4ed8; font-weight: 700; }
.jcg-panel-tag.dim-tag { background: #ede9fe; color: #6d28d9; }
.jcg-panel-tag.role-tag { background: #fef3c7; color: #92400e; }

/* Action Buttons in Drawer */
.jcg-drawer-actions { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 0.75rem; padding-bottom: 0.75rem; border-bottom: 1px solid #e2e8f0; }
.jcg-drawer-btn {
  font-size: 0.76rem; font-weight: 600; text-decoration: none; padding: 0.35rem 0.65rem; border-radius: 6px;
  display: inline-flex; align-items: center; gap: 0.3rem; border: none; cursor: pointer; transition: all 0.15s ease;
}
.jcg-drawer-btn-focus { background: #0f172a; color: #38bdf8; }
.jcg-drawer-btn-focus:hover { background: #1e293b; color: #7dd3fc; }
.jcg-drawer-btn-jc { background: #1a56db; color: #fff; }
.jcg-drawer-btn-jc:hover { background: #1e40af; }
.jcg-drawer-btn-pdf { background: #059669; color: #fff; }
.jcg-drawer-btn-pdf:hover { background: #047857; }
.jcg-drawer-btn-doi { background: #f1f5f9; color: #475569; border: 1px solid #cbd5e1; }
.jcg-drawer-btn-doi:hover { background: #e2e8f0; color: #0f172a; }

/* Direct Citation Neighborhood Toolbar */
.jcg-neighborhood-toolbar {
  background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 0.6rem 0.75rem;
  margin-bottom: 1rem; display: flex; flex-direction: column; gap: 0.45rem;
}
.jcg-neighborhood-title { font-size: 0.78rem; font-weight: 700; color: #1e293b; text-transform: uppercase; letter-spacing: 0.04em; }
.jcg-neighborhood-pills { display: flex; gap: 0.3rem; }
.jcg-nill-btn {
  flex: 1; padding: 0.35rem 0.4rem; font-size: 0.73rem; font-weight: 600; border-radius: 6px;
  border: 1px solid #cbd5e1; background: #fff; color: #475569; cursor: pointer; transition: all 0.15s ease; text-align: center;
}
.jcg-nill-btn:hover { background: #f1f5f9; border-color: #94a3b8; }
.jcg-nill-btn.active[data-dir="all"] { background: #0f172a; color: #fff; border-color: #0f172a; }
.jcg-nill-btn.active[data-dir="inbound"] { background: #059669; color: #fff; border-color: #059669; }
.jcg-nill-btn.active[data-dir="outbound"] { background: #4f46e5; color: #fff; border-color: #4f46e5; }

/* Shared detail styles (also used for the citation footer). */
.jcg-ocar-container { margin: 1rem 0; display: flex; flex-direction: column; gap: 0.5rem; }
.jcg-ocar-step {
  border-radius: 6px; padding: 0.6rem 0.75rem; font-size: 0.82rem; line-height: 1.45;
  background: #f8fafc; border: 1px solid #e2e8f0;
}
.jcg-ocar-step p { margin: 0.25rem 0 0 0; color: #334155; }
.jcg-ocar-label {
  display: inline-block; font-size: 0.7rem; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.05em; padding: 0.15rem 0.45rem; border-radius: 4px;
}
.jcg-ocar-opportunity { background: #dbeafe; color: #1e40af; }
.jcg-ocar-challenge   { background: #fef3c7; color: #92400e; }
.jcg-ocar-action      { background: #d1fae5; color: #065f46; }
.jcg-ocar-resolution  { background: #ede9fe; color: #5b21b6; }
.jcg-ocar-future      { background: #fce7f3; color: #9d174d; }

/* Ecosystem & Methodological Pipeline Container */
.jcg-ecosystem-box {
  background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 0.75rem; margin: 0.85rem 0;
}
.jcg-ecosystem-box h4 {
  margin: 0 0 0.5rem 0; font-size: 0.8rem; font-weight: 700; color: #0f172a; text-transform: uppercase; letter-spacing: 0.04em;
  display: flex; align-items: center; justify-content: space-between;
}
.jcg-ecosystem-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0.45rem; margin-bottom: 0.5rem; }
.jcg-eco-item { background: #fff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.35rem 0.5rem; font-size: 0.74rem; }
.jcg-eco-item strong { color: #475569; display: block; font-size: 0.68rem; text-transform: uppercase; margin-bottom: 0.1rem; }
.jcg-eco-item span { color: #0f172a; font-weight: 600; }

.jcg-eco-item small { display: block; margin-top: 0.2rem; color: #64748b; }
.jcg-paper-evidence { margin: 1rem 0; padding: 0.75rem; border: 1px solid #cbd5e1; border-radius: 8px; }
.jcg-paper-evidence p { font-size: 0.82rem; line-height: 1.55; }
.jcg-paper-abstract h4 { font-size: 0.9rem; margin: 1rem 0 0.4rem; }
.jcg-paper-abstract p { font-size: 0.82rem; color: #334155; line-height: 1.55; }
@media (max-width: 640px) { .jcg-ecosystem-grid { grid-template-columns: 1fr; } .jcg-eco-item { grid-column: 1 !important; } }

/* Pedagogical Summaries Tab Switcher */
.jcg-drawer-summaries { margin: 1rem 0; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; }
.jcg-summary-tabs { display: flex; background: #f1f5f9; border-bottom: 1px solid #e2e8f0; }
.jcg-summary-tab {
  flex: 1; padding: 0.35rem 0.5rem; font-size: 0.75rem; font-weight: 600; border: none;
  background: transparent; color: #64748b; cursor: pointer; text-align: center; transition: all 0.15s ease;
}
.jcg-summary-tab.active { background: #fff; color: #1a56db; font-weight: 700; border-bottom: 2px solid #1a56db; }
.jcg-summary-content { padding: 0.75rem; font-size: 0.82rem; color: #334155; line-height: 1.5; background: #fff; }

/* Seminar Discussion Prompts */
.jcg-prompts-section { margin: 0.85rem 0; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.6rem 0.75rem; font-size: 0.8rem; }
.jcg-prompts-section summary { font-weight: 700; color: #1e293b; cursor: pointer; }
.jcg-prompts-list { margin: 0.4rem 0 0 1.1rem; padding: 0; color: #475569; }
.jcg-prompts-list li { margin-bottom: 0.3rem; }

/* Interactive Lineage Traversal */
.jcg-lineage-section { margin: 1rem 0; }
.jcg-lineage-section h4 { margin: 0 0 0.4rem 0; font-size: 0.82rem; font-weight: 700; color: #1e293b; text-transform: uppercase; letter-spacing: 0.04em; }
.jcg-lineage-chips { display: flex; flex-wrap: wrap; gap: 0.35rem; margin-bottom: 0.75rem; }
.jcg-lineage-chip {
  background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 6px; padding: 0.25rem 0.55rem;
  font-size: 0.74rem; color: #1e293b; cursor: pointer; transition: all 0.15s ease; text-align: left;
}
.jcg-lineage-chip:hover { background: #1a56db; color: #fff; border-color: #1a56db; }
.jcg-lineage-chip.citing-chip { border-left: 3px solid #06b6d4; }
.jcg-lineage-chip.cited-chip { border-left: 3px solid #f59e0b; }

/* On-Demand AI Synthesis Tray */
.jcg-ai-tray {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.06);
  overflow: hidden;
  transition: all 0.25s ease-in-out;
}
.jcg-ai-tray.collapsed .jcg-ai-tray-body {
  display: none;
}
.jcg-ai-tray-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem 1.1rem;
  background: #f8fafc;
  border-bottom: 1px solid #e2e8f0;
  cursor: pointer;
  user-select: none;
}
.jcg-ai-tray.collapsed .jcg-ai-tray-header {
  border-bottom: none;
}
.jcg-ai-tray-header h3 {
  margin: 0;
  font-size: 0.92rem;
  font-weight: 700;
  color: #0f172a;
}
.jcg-ai-tray-toggle-btn {
  background: #fff;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  padding: 0.28rem 0.65rem;
  font-size: 0.75rem;
  font-weight: 600;
  color: #475569;
  cursor: pointer;
  transition: all 0.15s ease;
}
.jcg-ai-tray-toggle-btn:hover {
  background: #f1f5f9;
  color: #0f172a;
}
.jcg-ai-tray-body {
  padding: 1.15rem;
  background: #fff;
}
.jcg-copy-btn {
  background: #1a56db; color: #fff; border: none; border-radius: 6px;
  padding: 0.45rem 0.9rem; font-size: 0.82rem; font-weight: 600; cursor: pointer;
  display: inline-flex; align-items: center; gap: 0.4rem; transition: background 0.15s;
}
.jcg-copy-btn:hover { background: #1e40af; }
.jcg-copy-status { font-size: 0.8rem; font-weight: 600; color: #16a34a; }

/* Everyday task controls stay visible; presentation controls are optional. */
.jcg-page .jc-hero { text-align: left; background: #fff; color: #14263a; border: 1px solid #e2e8f0; padding: 1.2rem; }
.jcg-page .jc-hero p { max-width: none; margin: 0.5rem 0 0; }
.jcg-basic-controls { display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 0.9rem; margin: 1rem 0 0.7rem; }
.jcg-basic-controls .jcg-hint { grid-column: 1 / -1; }
.jcg-basic-controls label { font-weight: 600; font-size: 0.86rem; }
.jcg-basic-controls select { width: 100%; box-sizing: border-box; min-height: 44px; padding: 0.5rem; border: 1px solid #cbd5e1; border-radius: 6px; font: inherit; }
.jcg-basic-actions { display: flex; flex-wrap: wrap; align-items: center; gap: 1rem; margin: 0.5rem 0; }
.jcg-page .jcg-filter-panel { margin: 0.8rem 0; }
.jcg-page .jcg-controls { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); max-height: none; }
.jcg-layout { grid-template-columns: minmax(260px, 340px) minmax(0, 1fr); }
#jcg-results-list { max-height: clamp(400px, 65vh, 650px); }
.jcg-results { padding: 0.8rem; }
.jcg-canvas-wrap { height: clamp(400px, 65vh, 650px); }
.jcg-panel { max-height: calc(100% - 1rem); top: 0.5rem; right: 0.5rem; padding: 1rem; }
.jcg-drawer-actions { gap: 0.4rem; }
.jcg-panel-meta-tags { margin-top: 0.6rem; }
.jcg-panel-authors { max-height: 5rem; overflow-y: auto; }
.jcg-tooltip { max-width: 240px; font-size: 0.78rem; }
@media (max-width: 960px) {
 .jcg-basic-controls { grid-template-columns: 1fr 1fr; }
 .jcg-basic-controls > .jcg-control-group:first-child { grid-column: 1 / -1; }
 .jcg-layout { grid-template-columns: 1fr; }
 .jcg-page .jcg-controls { grid-template-columns: 1fr; max-height: 420px; overflow-y: auto; }
 #jcg-results-list { max-height: 300px; }
 .jcg-canvas-wrap { height: 440px; }
}
@media (max-width: 640px) {
 .jcg-basic-controls { grid-template-columns: 1fr; }
 .jcg-panel { top: auto; bottom: 0; left: 0; right: 0; max-height: 88%; padding: 0.8rem; }
 .jcg-page .jc-hero { padding: 1rem; }
}

</style>

<script src="{{ '/assets/js/paper-evidence.js' | relative_url }}?v={{ site.time | date: '%s' }}"></script>
<script>
(function () {
  var DATA_URL = "{{ '/technical-training/journal-club/graph-data.json' | relative_url }}?v={{ site.time | date: '%s' }}";
  var evidenceApi = window.NTPaperEvidence;
  var JC_BASE_URL = "{{ '/technical-training/journal-club/' | relative_url }}";

  var CATEGORIES = [
    'circuit-structure', 'pipeline', 'physiology', 'behaviour',
    'imaging', 'cell-types', 'neuroanatomy', 'synthesis',
    'dataset', 'neuroai', 'health', 'training-outreach', 'other', 'mri'
  ];

  var CATEGORY_COLORS = {
    'circuit-structure': '#2563eb',
    'pipeline': '#0891b2',
    'physiology': '#059669',
    'behaviour': '#d97706',
    'imaging': '#7c3aed',
    'cell-types': '#db2777',
    'neuroanatomy': '#4f46e5',
    'synthesis': '#4b5563',
    'dataset': '#0284c7',
    'neuroai': '#9333ea',
    'health': '#dc2626',
    'training-outreach': '#16a34a',
    'other': '#64748b',
    'mri': '#a16207'
  };

  var ERA_COLORS = {
    'history': '#2563eb',       // Blue
    'contemporary': '#06b6d4',  // Cyan
    'sota': '#f59e0b'           // Gold/Amber
  };

  var TIER_COLORS = {
    500: '#f59e0b',   // Gold
    1000: '#3b82f6',  // Sapphire
    2000: '#94a3b8'   // Slate
  };

  var ORGANISM_COLORS = {
    'mouse': '#2563eb',
    'drosophila': '#d97706',
    'human': '#dc2626',
    'c-elegans': '#059669',
    'zebrafish': '#7c3aed',
    'cross-species': '#db2777',
    'theory-model': '#4b5563',
    'rat': '#84cc16',
    'macaque': '#ec4899',
    'other': '#0f766e',
    'general': '#64748b'
  };

  var ROLE_COLORS = {
    'core_hub': '#f59e0b',
    'authority': '#8b5cf6',
    'bridge': '#06b6d4',
    'connected': '#10b981',
    'participant': '#64748b'
  };

  var ORGANISM_LABELS = { mouse: 'Mouse', rat: 'Rat', drosophila: 'Drosophila', fly: 'Drosophila', human: 'Human', 'c-elegans': 'C. elegans', elegans: 'C. elegans', zebrafish: 'Zebrafish', macaque: 'Macaque', other: 'Other system' };

  function organismLabel(p) {
    var labels = p.organism.map(function (o) { return ORGANISM_LABELS[o.toLowerCase()]; }).filter(Boolean);
    return Array.from(new Set(labels)).join(', ') || 'Not recorded';
  }

  function escapeHtml(value) {
    return String(value || '').replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; });
  }

  var CATEGORY_HUBS = {};
  var CATEGORY_LABELS = {
    'circuit-structure': 'Circuits', pipeline: 'Software', physiology: 'Physiology', behaviour: 'Behaviour',
    imaging: 'Imaging', 'cell-types': 'Cell types', neuroanatomy: 'Anatomy', synthesis: 'Reviews',
    dataset: 'Datasets', neuroai: 'NeuroAI', health: 'Health', 'training-outreach': 'Outreach', other: 'Other', mri: 'MRI'
  };

  // DOM Elements
  var canvas = document.getElementById('jcg-canvas');
  var ctx = canvas.getContext('2d');
  var tierButtons = Array.from(document.querySelectorAll('.jcg-tier-btn'));
  var layoutButtons = Array.from(document.querySelectorAll('.jcg-layout-btn'));
  var showEdgesCheck = document.getElementById('jcg-show-edges');
  var allEdgesCheck = document.getElementById('jcg-all-edges');
  var showArrowsCheck = document.getElementById('jcg-show-arrows');
  var showFlowCheck = document.getElementById('jcg-show-flow');
  var edgeWeightingEl = document.getElementById('jcg-edge-weighting');
  var colorByEl = document.getElementById('jcg-color-by');
  var eraChecks = Array.from(document.querySelectorAll('.jcg-era-check'));
  var dimensionEl = document.getElementById('jcg-dimension');
  var organismEl = document.getElementById('jcg-organism');
  var degreeEl = document.getElementById('jcg-min-degree');
  var degreeVal = document.getElementById('jcg-degree-val');
  var searchEl = document.getElementById('jcg-search');
  var countEl = document.getElementById('jcg-count');
  var resetBtn = document.getElementById('jcg-reset');
  var sidebarFitBtn = document.getElementById('jcg-sidebar-fit');
  var sidebarReheatBtn = document.getElementById('jcg-sidebar-reheat');
  var hudZoomInBtn = document.getElementById('jcg-hud-zoom-in');
  var hudZoomOutBtn = document.getElementById('jcg-hud-zoom-out');
  var hudFitBtn = document.getElementById('jcg-hud-fit');
  var hudReheatBtn = document.getElementById('jcg-hud-reheat');
  var focusBanner = document.getElementById('jcg-focus-banner');
  var focusPaperTitle = document.getElementById('jcg-focus-paper-title');
  var focusExitBtn = document.getElementById('jcg-focus-exit-btn');
  var promptTriggerBtn = document.getElementById('jcg-prompt-btn');
  var promptCountSpan = document.getElementById('jcg-prompt-count');
  var aiTray = document.getElementById('jcg-ai-tray');
  var aiTrayHeader = document.getElementById('jcg-ai-tray-header');
  var aiTrayToggleBtn = document.getElementById('jcg-ai-tray-toggle');
  var aiTrayStatusText = document.getElementById('jcg-tray-status-text');
  var promptTextarea = document.getElementById('jcg-prompt-textarea');
  var copyPromptBtn = document.getElementById('jcg-copy-prompt-btn');
  var copyStatus = document.getElementById('jcg-copy-status');
  var modalPaperCount = document.getElementById('jcg-modal-paper-count');
  var tooltip = document.getElementById('jcg-tooltip');
  var panel = document.getElementById('jcg-panel');
  var panelBody = document.getElementById('jcg-panel-body');
  var panelClose = document.getElementById('jcg-panel-close');
  var legendEl = document.getElementById('jcg-legend');
  var legendTitleEl = document.getElementById('jcg-legend-title');

  // Application State
  var allPapers = [];
  var idMap = {};
  var doiMap = {};
  var currentTier = 2000;
  var currentLayout = 'cluster';
  var currentColorCue = 'dimension';
  var currentEdgeWeighting = 'sum';
  var visibleNodes = [];
  var visibleEdges = [];
  var view = { scale: 1, tx: 0, ty: 0 };
  var draggingNode = null;
  var isPanning = false;
  var panStart = { x: 0, y: 0 };
  var dragMoved = false;
  var hoveredNode = null;
  var selectedNode = null;
  var focusedSubgraphNode = null;
  var highlightNeighborhoodMode = 'all';
  var hoveredLineageNode = null;
  var alpha = 1.0;
  var animFrame = null;
  var flowOffset = 0;
  var canvasRatio = 1;
  var filterTimer = null;
  var resultLimit = 40;
  var timelineMinYear = 1986;
  var timelineMaxYear = 2026;
  var timelineYearSpacing = 126;
  var timelineTop = 0;
  var timelineBottom = 0;
  var filterPanel = document.getElementById('jcg-filter-panel');
  var emptyEl = document.getElementById('jcg-empty');
  var resultsList = document.getElementById('jcg-results-list');
  var resultsStatus = document.getElementById('jcg-results-status');
  var resultsMore = document.getElementById('jcg-results-more');
  filterPanel.open = false;

  function updateResults() {
    resultsList.replaceChildren();
    visibleNodes.slice(0, resultLimit).forEach(function (p) {
      var li = document.createElement('li');
      var button = document.createElement('button');
      button.type = 'button';
      button.className = 'jcg-result-btn';
      button.textContent = p.title;
      var meta = document.createElement('small');
      meta.textContent = p.authors + ' · ' + p.year + ' · ' + p.dimension.replace(/-/g, ' ');
      button.appendChild(meta);
      button.addEventListener('click', function () { selectAndCenterPaper(p); });
      li.appendChild(button);
      resultsList.appendChild(li);
    });
    document.getElementById('jcg-results-title').textContent = focusedSubgraphNode ? 'Related papers' : 'Papers';
    resultsStatus.textContent = visibleNodes.length ? 'Showing ' + Math.min(resultLimit, visibleNodes.length) + ' of ' + visibleNodes.length + '. Select a paper to open its card.' : 'No matching papers.';
    resultsMore.classList.toggle('hidden', resultLimit >= visibleNodes.length);
  }
  resultsMore.addEventListener('click', function () { resultLimit += 40; updateResults(); });

  function getNodeColor(p) {
    if (currentColorCue === 'era') {
      return ERA_COLORS[p.era] || '#64748b';
    } else if (currentColorCue === 'tier') {
      return TIER_COLORS[p.tier] || '#94a3b8';
    } else if (currentColorCue === 'organism') {
      var org = (p.organism && p.organism[0]) ? p.organism[0].toLowerCase() : 'general';
      if (org.indexOf('fly') !== -1 || org.indexOf('drosophila') !== -1) return ORGANISM_COLORS['drosophila'];
      if (org.indexOf('elegans') !== -1 || org.indexOf('worm') !== -1) return ORGANISM_COLORS['c-elegans'];
      if (org.indexOf('mouse') !== -1 || org.indexOf('rodent') !== -1) return ORGANISM_COLORS['mouse'];
      if (org.indexOf('human') !== -1 || org.indexOf('h01') !== -1) return ORGANISM_COLORS['human'];
      if (org.indexOf('zebrafish') !== -1 || org.indexOf('danio') !== -1) return ORGANISM_COLORS['zebrafish'];
      return ORGANISM_COLORS[org] || '#64748b';
    } else if (currentColorCue === 'citation_role') {
      return ROLE_COLORS[p.citation_role] || '#64748b';
    }
    return CATEGORY_COLORS[p.dimension] || '#64748b';
  }

  function updateLegend() {
    legendEl.innerHTML = '';
    if (currentColorCue === 'era') {
      legendTitleEl.textContent = 'Color Cue: Publication Era';
      [
        { k: 'History (≤2018)', c: ERA_COLORS['history'] },
        { k: '2019–2023', c: ERA_COLORS['contemporary'] },
        { k: '2024 onwards', c: ERA_COLORS['sota'] }
      ].forEach(function (item) {
        var row = document.createElement('div');
        row.className = 'jcg-legend-item';
        row.innerHTML = '<span class="jcg-legend-swatch" style="background:' + item.c + '"></span>' + item.k;
        legendEl.appendChild(row);
      });
    } else if (currentColorCue === 'tier') {
      legendTitleEl.textContent = 'Color Cue: Corpus Scale Tier';
      [
        { k: 'Top 500', c: TIER_COLORS[500] },
        { k: 'Top 1,000', c: TIER_COLORS[1000] },
        { k: 'All 2,000', c: TIER_COLORS[2000] }
      ].forEach(function (item) {
        var row = document.createElement('div');
        row.className = 'jcg-legend-item';
        row.innerHTML = '<span class="jcg-legend-swatch" style="background:' + item.c + '"></span>' + item.k;
        legendEl.appendChild(row);
      });
    } else if (currentColorCue === 'organism') {
      legendTitleEl.textContent = 'Color Cue: Model Organism';
      [
        { k: 'Drosophila (Fruit Fly)', c: ORGANISM_COLORS['drosophila'] },
        { k: 'Mouse / Rodent', c: ORGANISM_COLORS['mouse'] },
        { k: 'Human Cortex', c: ORGANISM_COLORS['human'] },
        { k: 'C. elegans (Worm)', c: ORGANISM_COLORS['c-elegans'] },
        { k: 'Zebrafish', c: ORGANISM_COLORS['zebrafish'] },
        { k: 'Rat', c: ORGANISM_COLORS['rat'] },
        { k: 'Macaque', c: ORGANISM_COLORS['macaque'] },
        { k: 'Other tagged systems', c: ORGANISM_COLORS['other'] },
        { k: 'Not tagged / general', c: ORGANISM_COLORS['general'] }
      ].forEach(function (item) {
        var row = document.createElement('div');
        row.className = 'jcg-legend-item';
        row.innerHTML = '<span class="jcg-legend-swatch" style="background:' + item.c + '"></span>' + item.k;
        legendEl.appendChild(row);
      });
    } else if (currentColorCue === 'citation_role') {
      legendTitleEl.textContent = 'Color Cue: Citation Role';
      [
        { k: 'Imported hub label', c: ROLE_COLORS['core_hub'] },
        { k: 'Imported authority label', c: ROLE_COLORS['authority'] },
        { k: 'Inter-Domain Bridge', c: ROLE_COLORS['bridge'] },
        { k: 'Connected Literature', c: ROLE_COLORS['connected'] },
        { k: 'Network Participant', c: ROLE_COLORS['participant'] }
      ].forEach(function (item) {
        var row = document.createElement('div');
        row.className = 'jcg-legend-item';
        row.innerHTML = '<span class="jcg-legend-swatch" style="background:' + item.c + '"></span>' + item.k;
        legendEl.appendChild(row);
      });
    } else {
      legendTitleEl.textContent = 'Color Cue: Category / Domain';
      CATEGORIES.forEach(function (c) {
        var row = document.createElement('div');
        row.className = 'jcg-legend-item';
        var label = c.replace(/-/g, ' ');
        row.innerHTML = '<span class="jcg-legend-swatch" style="background:' + CATEGORY_COLORS[c] + '"></span>' + label.charAt(0).toUpperCase() + label.slice(1);
        legendEl.appendChild(row);
      });
    }
  }

  // Load Graph Data
  fetch(DATA_URL).then(function (r) { if (!r.ok) throw new Error('Graph data request failed: ' + r.status); return r.json(); }).then(function (data) {
    idMap = {};
    doiMap = {};

    allPapers = data.map(function (d) {
      var cat = d.dimension || 'circuit-structure';
      var orgs = Array.isArray(d.organism) ? d.organism : [d.organism || 'general'];
      var cleanDoi = (d.doi || '').toLowerCase().trim();

      var paperObj = {
        id: d.id,
        title: d.title || 'Untitled',
        authors: d.authors || '',
        year: d.year || 2020,
        journal: d.journal || '',
        doi: cleanDoi,
        dimension: cat,
        organism: orgs,
        era: d.era || 'contemporary',
        tier: d.tier || 2000,
        in_degree: d.in_degree || 0,
        out_degree: d.out_degree || 0,
        total_degree: (d.in_degree || 0) + (d.out_degree || 0),
        kcore: d.kcore || 5,
        citation_role: d.citation_role || 'participant',
        scope_role: d.scope_role || 'participant',
        evidence: d.evidence || null,
        publication_links: evidenceApi ? evidenceApi.publicationRelationship(d.publication_links, cleanDoi) : null,
        abstract: d.abstract || '',
        // Bibliographic search excludes generated interpretations and tags.
        searchText: [d.title, d.authors, d.journal, d.doi].join(' ').toLowerCase(),
        citation: d.citation || '',
        cites: d.cites || [],
        pdf_url: d.pdf_url || null,
        is_oa: d.is_oa || false,
        x: 0,
        y: 0,
        targetX: 0,
        targetY: 0,
        vx: 0,
        vy: 0,
        radius: Math.max(4.5, Math.min(16, 4.5 + Math.sqrt((d.in_degree || 0) + (d.out_degree || 0)) * 1.5)),
        citesNodes: [],
        citedByNodes: []
      };

      idMap[paperObj.id] = paperObj;
      if (cleanDoi) doiMap[cleanDoi] = paperObj;
      return paperObj;
    });

    // Build bi-directional citation graph links
    allPapers.forEach(function (source) {
      if (source.cites && source.cites.length) {
        source.cites.forEach(function (tgtDoi) {
          var cleanT = (tgtDoi || '').toLowerCase().trim();
          var target = doiMap[cleanT];
          if (target && target !== source) {
            source.citesNodes.push(target);
            target.citedByNodes.push(source);
          }
        });
      }
    });

    degreeEl.max = Math.max.apply(null, allPapers.map(function (p) { return p.total_degree; }));
    resizeCanvas();
    updateLegend();

    // Check URL parameters for deep-linking
    var params = new URLSearchParams(window.location.search);
    if (params.has('tier') && [500, 1000, 2000].indexOf(parseInt(params.get('tier'), 10)) !== -1) {
      currentTier = parseInt(params.get('tier'), 10);
      tierButtons.forEach(function (b) { b.classList.toggle('active', b.dataset.tier === String(currentTier)); });
    }
    if (params.has('dimension') && dimensionEl.querySelector('option[value="' + CSS.escape(params.get('dimension')) + '"]')) {
      dimensionEl.value = params.get('dimension');
    }

    if (params.has('q')) searchEl.value = params.get('q');
    if (params.has('organism') && organismEl.querySelector('option[value="' + CSS.escape(params.get('organism')) + '"]')) organismEl.value = params.get('organism');
    if (params.has('era')) eraChecks.forEach(function (el) { el.checked = params.get('era').split(',').indexOf(el.value) !== -1; });
    if (params.has('minDegree')) degreeEl.value = Math.max(0, parseInt(params.get('minDegree'), 10) || 0);
    applyFilters();
    fitView();

    if (params.has('paper')) {
      var targetId = params.get('paper');
      var matched = idMap[targetId] || doiMap[targetId.toLowerCase().trim()];
      if (matched) {
        if (matched.tier > currentTier) {
          currentTier = matched.tier;
          tierButtons.forEach(function (b) { b.classList.toggle('active', b.dataset.tier === String(currentTier)); });
          applyFilters();
        }
        if (visibleNodes.indexOf(matched) === -1) enterSubgraphFocus(matched);
        selectAndCenterPaper(matched);
      }
    }
  }).catch(function (error) {
    countEl.textContent = 'Could not load the paper graph. Please reload to try again.';
    emptyEl.textContent = countEl.textContent;
    emptyEl.classList.remove('hidden');
    console.error(error);
  });

  function resizeCanvas() {
    var rect = canvas.getBoundingClientRect();
    canvasRatio = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.round(rect.width * canvasRatio);
    canvas.height = Math.round(rect.height * canvasRatio);
    ctx.setTransform(canvasRatio, 0, 0, canvasRatio, 0, 0);
    if (visibleNodes.length && currentLayout !== 'organic') arrangeNodes();
    fitView();
    wakeAnimation();
  }
  new ResizeObserver(resizeCanvas).observe(canvas.parentElement);

  // Deterministic, separated positions; anchored layouts never converge onto one dot.
  function arrangeNodes() {
    var groups = {};
    visibleNodes.forEach(function (n) { (groups[n.dimension] || (groups[n.dimension] = [])).push(n); });
    var categories = CATEGORIES.filter(function (cat) { return groups[cat]; });
    var largest = Math.max.apply(null, categories.map(function (cat) { return groups[cat].length; }).concat([1]));
    var spacing = Math.sqrt(largest) * 52 + 180;
    var cols = Math.min(canvas.getBoundingClientRect().width < 600 ? 2 : 4, Math.ceil(Math.sqrt(categories.length)));
    CATEGORY_HUBS = {};
    timelineMinYear = Math.min.apply(null, visibleNodes.map(function (n) { return n.year; }).concat([2026]));
    timelineMaxYear = Math.max.apply(null, visibleNodes.map(function (n) { return n.year; }).concat([timelineMinYear + 1]));
    var yearCounts = {};
    visibleNodes.forEach(function (n) { var key = n.dimension + ':' + n.year; yearCounts[key] = (yearCounts[key] || 0) + 1; });
    var timelineColumns = Math.min(3, Math.max.apply(null, Object.values(yearCounts).concat([1])));
    timelineYearSpacing = timelineColumns * 36 + 18;
    timelineTop = -80;
    var laneY = 0;
    categories.forEach(function (cat, c) {
      var group = groups[cat].slice().sort(function (a, b) { return a.year - b.year || a.id.localeCompare(b.id); });
      var hub = { x: (c % cols) * spacing, y: Math.floor(c / cols) * spacing, radius: Math.sqrt(group.length) * 26 + 30 };
      CATEGORY_HUBS[cat] = hub;
      var years = {};
      group.forEach(function (n) { years[n.year] = (years[n.year] || 0) + 1; });
      var laneHeight = Math.ceil(Math.max.apply(null, Object.values(years)) / timelineColumns) * 36 + 70;
      var offsets = {};
      group.forEach(function (n, i) {
        if (currentLayout === 'timeline') {
          var offset = offsets[n.year] || 0;
          offsets[n.year] = offset + 1;
          n.targetX = (n.year - timelineMinYear) * timelineYearSpacing + (offset % timelineColumns) * 36;
          n.targetY = laneY + Math.floor(offset / timelineColumns) * 36;
        } else {
          var angle = i * Math.PI * (3 - Math.sqrt(5));
          var radius = Math.sqrt(i + 0.5) * 26;
          n.targetX = hub.x + Math.cos(angle) * radius;
          n.targetY = hub.y + Math.sin(angle) * radius;
        }
        n.x = n.targetX;
        n.y = n.targetY;
        n.vx = n.vy = 0;
      });
      hub.laneY = laneY;
      laneY += laneHeight;
    });
    timelineBottom = laneY;
    alpha = currentLayout === 'organic' ? 0.8 : 0;
  }

  function applyFilters() {
    var activeEras = eraChecks.filter(function (c) { return c.checked; }).map(function (c) { return c.value; });
    var selectedCat = dimensionEl.value;
    var selectedOrg = organismEl.value;
    var minDeg = parseInt(degreeEl.value, 10);
    var query = searchEl.value.toLowerCase().trim();

    visibleNodes = allPapers.filter(function (p) {
      if (focusedSubgraphNode) {
        // Ego-Network isolation mode: show focused node + 1-hop in & out neighbors
        var isSelf = (p === focusedSubgraphNode);
        var isCiting = focusedSubgraphNode.citedByNodes.indexOf(p) !== -1;
        var isCited = focusedSubgraphNode.citesNodes.indexOf(p) !== -1;
        if (!isSelf && !isCiting && !isCited) return false;
      } else {
        if (!query && p.tier > currentTier) return false;
        if (activeEras.indexOf(p.era) === -1) return false;
        if (selectedCat !== 'all' && p.dimension !== selectedCat) return false;
        if (selectedOrg !== 'all') {
          var orgMatch = p.organism.some(function (o) {
            var lo = o.toLowerCase();
            if (selectedOrg === 'drosophila' && (lo.indexOf('fly') !== -1 || lo.indexOf('drosophila') !== -1)) return true;
            if (selectedOrg === 'c-elegans' && (lo.indexOf('elegans') !== -1 || lo.indexOf('worm') !== -1 || lo.indexOf('nematode') !== -1)) return true;
            if (selectedOrg === 'mouse' && (lo.indexOf('mouse') !== -1 || lo.indexOf('rodent') !== -1 || lo.indexOf('mus') !== -1)) return true;
            if (selectedOrg === 'human' && (lo.indexOf('human') !== -1 || lo.indexOf('homo') !== -1 || lo.indexOf('h01') !== -1)) return true;
            if (selectedOrg === 'zebrafish' && (lo.indexOf('zebrafish') !== -1 || lo.indexOf('danio') !== -1 || lo.indexOf('fish') !== -1)) return true;
            if (selectedOrg === 'unclassified') return /^(none|general)$/.test(lo);
            return lo.indexOf(selectedOrg) !== -1;
          });
          if (!orgMatch) return false;
        }
        if (p.total_degree < minDeg) return false;
        if (query && p.searchText.indexOf(query) === -1) return false;
      }
      return true;
    });

    var activeDoiSet = {};
    visibleNodes.forEach(function (n) {
      if (n.doi) activeDoiSet[n.doi] = n;
    });

    // Extract Visible Directed Citation Edges
    visibleEdges = [];
    visibleNodes.forEach(function (sourceNode) {
      if (sourceNode.cites && sourceNode.cites.length) {
        sourceNode.cites.forEach(function (targetDoi) {
          var cleanTarget = (targetDoi || '').toLowerCase().trim();
          var targetNode = activeDoiSet[cleanTarget];
          if (targetNode && targetNode !== sourceNode) {
            visibleEdges.push({
              source: sourceNode,
              target: targetNode
            });
          }
        });
      }
    });

    var shared = new URLSearchParams();
    if (query) shared.set('q', query);
    if (selectedCat !== 'all') shared.set('dimension', selectedCat);
    if (selectedOrg !== 'all') shared.set('organism', selectedOrg);
    if (activeEras.length !== eraChecks.length) shared.set('era', activeEras.join(','));
    if (minDeg > 0) shared.set('minDegree', minDeg);
    shared.set('tier', String(currentTier));
    var listView = document.getElementById('jcg-list-view');
    if (listView) listView.href = JC_BASE_URL + '?' + shared.toString();
    countEl.textContent = visibleNodes.length + ' papers (' + visibleEdges.length + ' citation links)';
    promptCountSpan.textContent = visibleNodes.length;
    emptyEl.classList.toggle('hidden', visibleNodes.length > 0);
    if (selectedNode && visibleNodes.indexOf(selectedNode) === -1) {
      selectedNode = null;
      panel.classList.add('hidden');
    }
    hoveredNode = hoveredLineageNode = null;
    tooltip.classList.add('hidden');
    resultLimit = 40;
    updateResults();
    arrangeNodes();
    fitView();
    if (!aiTray.classList.contains('collapsed') && !singlePaperTarget) generateSynthesisPrompt();
    wakeAnimation();
  }

  function fitView(targetNodes) {
    var nodes = targetNodes || visibleNodes;
    if (!nodes.length) { view = { scale: 1, tx: 0, ty: 0 }; wakeAnimation(); return; }
    var minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity;
    nodes.forEach(function (n) {
      if (n.x < minX) minX = n.x;
      if (n.x > maxX) maxX = n.x;
      if (n.y < minY) minY = n.y;
      if (n.y > maxY) maxY = n.y;
    });
    var w = Math.max(maxX - minX + 160, 280);
    var h = Math.max(maxY - minY + 160, 280);
    var cw = canvas.width / canvasRatio;
    var ch = canvas.height / canvasRatio;
    view.scale = Math.min(cw / w, ch / h, 2.2) * 0.85;
    view.tx = cw / 2 - ((minX + maxX) / 2) * view.scale;
    view.ty = ch / 2 - ((minY + maxY) / 2) * view.scale;
    wakeAnimation();
  }

  function selectAndCenterPaper(p) {
    if (focusedSubgraphNode && focusedSubgraphNode !== p) enterSubgraphFocus(p);
    selectedNode = p;
    openPaperDrawer(p);
    var cw = canvas.width / canvasRatio;
    var ch = canvas.height / canvasRatio;
    view.scale = Math.max(view.scale, 1.2);
    // Shift slightly left to accommodate drawer on the right
    view.tx = (cw * 0.38) - p.x * view.scale;
    view.ty = (ch * 0.5) - p.y * view.scale;
    wakeAnimation();
  }

  function enterSubgraphFocus(node) {
    focusedSubgraphNode = node;
    panel.classList.add('hidden');
    focusPaperTitle.textContent = node.title.length > 50 ? node.title.slice(0, 48) + '…' : node.title;
    focusBanner.classList.remove('hidden');
    applyFilters();
    fitView();
    wakeAnimation();
  }

  function exitSubgraphFocus() {
    focusedSubgraphNode = null;
    selectedNode = null;
    panel.classList.add('hidden');
    focusBanner.classList.add('hidden');
    applyFilters();
    fitView();
    wakeAnimation();
  }

  focusExitBtn.addEventListener('click', exitSubgraphFocus);

  // Physics Simulation Loop with Spatial Grid Partitioning
  function tickPhysics() {
    if (alpha < 0.003 && !draggingNode) return;
    var dt = 0.04 * alpha;

    if (currentLayout === 'organic') {
      // 1. Hooke's Law Spring Force along citation edges
      for (var e = 0; e < visibleEdges.length; e++) {
        var edge = visibleEdges[e];
        var s = edge.source;
        var t = edge.target;
        var dx = t.x - s.x;
        var dy = t.y - s.y;
        var dist = Math.hypot(dx, dy) || 1;
        var desiredDist = 95;
        var force = (dist - desiredDist) * 0.04 * dt;
        var fx = (dx / dist) * force;
        var fy = (dy / dist) * force;

        if (s !== draggingNode) { s.vx += fx; s.vy += fy; }
        if (t !== draggingNode) { t.vx -= fx; t.vy -= fy; }
      }

      // 2. Fast Spatial Grid for O(N) Repulsion
      var cellSize = 130;
      var grid = {};
      for (var i = 0; i < visibleNodes.length; i++) {
        var n = visibleNodes[i];
        var gx = Math.floor(n.x / cellSize);
        var gy = Math.floor(n.y / cellSize);
        var cellKey = gx + ':' + gy;
        if (!grid[cellKey]) grid[cellKey] = [];
        grid[cellKey].push(n);

        // Center gravity
        if (n !== draggingNode) {
          n.vx -= n.x * 0.002 * dt;
          n.vy -= n.y * 0.002 * dt;
        }
      }

      for (var i = 0; i < visibleNodes.length; i++) {
        var n1 = visibleNodes[i];
        if (n1 === draggingNode) continue;
        var gx = Math.floor(n1.x / cellSize);
        var gy = Math.floor(n1.y / cellSize);

        for (var ox = -1; ox <= 1; ox++) {
          for (var oy = -1; oy <= 1; oy++) {
            var neighborKey = (gx + ox) + ':' + (gy + oy);
            var bucket = grid[neighborKey];
            if (!bucket) continue;
            for (var b = 0; b < bucket.length; b++) {
              var n2 = bucket[b];
              if (n2 === n1) continue;
              var rx = n2.x - n1.x;
              var ry = n2.y - n1.y;
              var distance = Math.hypot(rx, ry) || 0.01;
              var padding = n1.radius + n2.radius + 8;
              if (distance < padding) {
                n1.vx -= (rx / distance) * (padding - distance) * 0.3;
                n1.vy -= (ry / distance) * (padding - distance) * 0.3;
              }
              var r2 = rx * rx + ry * ry + 80;
              if (r2 < 36000) {
                var repForce = (2900 / r2) * dt;
                var r = Math.sqrt(r2);
                n1.vx -= (rx / r) * repForce;
                n1.vy -= (ry / r) * repForce;
              }
            }
          }
        }

        n1.vx *= 0.85;
        n1.vy *= 0.85;
        n1.x += n1.vx;
        n1.y += n1.vy;
      }

    } else {
      // Anchored Layouts (Group by topic or Timeline)
      for (var i = 0; i < visibleNodes.length; i++) {
        var n = visibleNodes[i];
        if (n === draggingNode) continue;
        var dx = n.targetX - n.x;
        var dy = n.targetY - n.y;
        n.vx += dx * dt * 0.8;
        n.vy += dy * dt * 0.8;
        n.vx *= 0.85;
        n.vy *= 0.85;
        n.x += n.vx;
        n.y += n.vy;
      }
    }

    if (!draggingNode) {
      alpha *= 0.988;
    }
  }

  function render() {
    var cw = canvas.width / canvasRatio;
    var ch = canvas.height / canvasRatio;
    ctx.clearRect(0, 0, cw, ch);

    ctx.save();
    ctx.translate(view.tx, view.ty);
    ctx.scale(view.scale, view.scale);

    // Draw Category Hub Background Rings in Cluster Mode
    if (currentLayout === 'cluster') {
      CATEGORIES.forEach(function (cat) {
        var hub = CATEGORY_HUBS[cat];
        ctx.beginPath();
        if (!hub) return;
        ctx.arc(hub.x, hub.y, hub.radius, 0, Math.PI * 2);
        ctx.fillStyle = CATEGORY_COLORS[cat] + '08';
        ctx.fill();
        ctx.strokeStyle = CATEGORY_COLORS[cat] + '22';
        ctx.lineWidth = 1 / view.scale;
        ctx.stroke();

        ctx.fillStyle = CATEGORY_COLORS[cat] + '90';
        ctx.font = 'bold ' + (10 / view.scale) + 'px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(CATEGORY_LABELS[cat] || cat, hub.x, hub.y - hub.radius - 15);
      });
    }

    // Year coordinates and lane labels use the visible corpus's actual range.
    if (currentLayout === 'timeline') {
      var step = timelineMaxYear - timelineMinYear > 60 ? 10 : 5;
      for (var yr = Math.ceil(timelineMinYear / step) * step; yr <= timelineMaxYear; yr += step) {
        var gx = (yr - timelineMinYear) * timelineYearSpacing;
        ctx.beginPath(); ctx.moveTo(gx, timelineTop); ctx.lineTo(gx, timelineBottom);
        ctx.strokeStyle = '#e2e8f0'; ctx.lineWidth = 1 / view.scale; ctx.stroke();
        ctx.fillStyle = '#64748b'; ctx.font = (12 / view.scale) + 'px sans-serif'; ctx.textAlign = 'center';
        ctx.fillText(String(yr), gx, timelineTop - 15);
      }
      CATEGORIES.forEach(function (cat) {
        var hub = CATEGORY_HUBS[cat];
        if (!hub) return;
        ctx.fillStyle = CATEGORY_COLORS[cat]; ctx.font = (11 / view.scale) + 'px sans-serif'; ctx.textAlign = 'left';
        ctx.fillText(cat.replace(/-/g, ' '), 0, hub.laneY - 25);
      });
    }

    var activeNode = hoveredNode || selectedNode || focusedSubgraphNode;
    var drawEdges = showEdgesCheck.checked;
    var drawArrows = showArrowsCheck.checked;
    var drawFlow = showFlowCheck.checked;
    flowOffset = (flowOffset + 0.015) % 1.0;

    // Direct Inbound / Outbound Sets for activeNode
    var inSet = new Set(activeNode && activeNode.citedByNodes ? activeNode.citedByNodes : []);
    var outSet = new Set(activeNode && activeNode.citesNodes ? activeNode.citesNodes : []);

    // Draw Citation Edges (Phase 1 Batched Multi-Tier Rendering)
    if (drawEdges && visibleEdges.length && (activeNode || allEdgesCheck.checked)) {
      var batches = {
        faint: [],
        tier1: [],
        tier2: [],
        tier3: [],
        tier4: []
      };
      var activeHighlights = [];

      for (var e = 0; e < visibleEdges.length; e++) {
        var edge = visibleEdges[e];
        var s = edge.source;
        var t = edge.target;

        var isSpotlightLineage = hoveredLineageNode && ((s === activeNode && t === hoveredLineageNode) || (t === activeNode && s === hoveredLineageNode));
        var isOutbound = (s === activeNode && outSet.has(t) && highlightNeighborhoodMode !== 'inbound');
        var isInbound = (t === activeNode && inSet.has(s) && highlightNeighborhoodMode !== 'outbound');

        if (isSpotlightLineage || isOutbound || isInbound) {
          activeHighlights.push({ s: s, t: t, isSpotlight: isSpotlightLineage, isOut: isOutbound, isIn: isInbound, index: e });
          continue;
        }

        if (activeNode) {
          if (highlightNeighborhoodMode === 'all') {
            batches.faint.push(edge);
          }
          continue;
        }

        var edgeMetric = 1;
        if (currentEdgeWeighting === 'sum') {
          edgeMetric = ((s.in_degree || 0) + (s.out_degree || 0) + (t.in_degree || 0) + (t.out_degree || 0)) / 2;
        } else if (currentEdgeWeighting === 'in') {
          edgeMetric = (t.in_degree || 0);
        } else if (currentEdgeWeighting === 'out') {
          edgeMetric = (s.out_degree || 0);
        } else if (currentEdgeWeighting === 'both') {
          var sourceDegree = s.total_degree, targetDegree = t.total_degree;
          edgeMetric = sourceDegree + targetDegree ? 2 * sourceDegree * targetDegree / (sourceDegree + targetDegree) : 0;
        }

        if (currentEdgeWeighting === 'uniform') {
          batches.tier2.push(edge);
        } else if (edgeMetric < 3) {
          batches.tier1.push(edge);
        } else if (edgeMetric < 8) {
          batches.tier2.push(edge);
        } else if (edgeMetric < 18) {
          batches.tier3.push(edge);
        } else {
          batches.tier4.push(edge);
        }
      }

      // 1. Draw Faint non-connected edges in focus mode (1 single draw call)
      if (batches.faint.length) {
        ctx.beginPath();
        for (var i = 0; i < batches.faint.length; i++) {
          var fe = batches.faint[i];
          ctx.moveTo(fe.source.x, fe.source.y);
          ctx.lineTo(fe.target.x, fe.target.y);
        }
        ctx.strokeStyle = '#94a3b820';
        ctx.lineWidth = 0.7 / view.scale;
        ctx.stroke();
      }

      // 2. Draw Batched Standard Edges (4 single draw calls for thousands of edges)
      var tierConfigs = [
        { edges: batches.tier1, color: 'rgba(71, 85, 105, 0.10)', width: 0.6 },
        { edges: batches.tier2, color: 'rgba(71, 85, 105, 0.14)', width: 0.8 },
        { edges: batches.tier3, color: 'rgba(51, 65, 85, 0.18)', width: 1.0 },
        { edges: batches.tier4, color: 'rgba(30, 41, 59, 0.22)', width: 1.2 }
      ];

      for (var tIdx = 0; tIdx < tierConfigs.length; tIdx++) {
        var tc = tierConfigs[tIdx];
        if (tc.edges.length) {
          ctx.beginPath();
          for (var i = 0; i < tc.edges.length; i++) {
            var be = tc.edges[i];
            ctx.moveTo(be.source.x, be.source.y);
            ctx.lineTo(be.target.x, be.target.y);
          }
          ctx.strokeStyle = tc.color;
          ctx.lineWidth = tc.width / view.scale;
          ctx.stroke();
        }
      }

      // 3. Batched Directional Arrows
      if (drawArrows && !activeNode && view.scale > 0.3) {
        ctx.beginPath();
        for (var e = 0; e < visibleEdges.length; e++) {
          var ae = visibleEdges[e];
          var as = ae.source;
          var at = ae.target;
          var adx = at.x - as.x;
          var ady = at.y - as.y;
          var aAngle = Math.atan2(ady, adx);
          var aHeadlen = 5.5 / view.scale;
          var ax = at.x - Math.cos(aAngle) * (at.radius + 3);
          var ay = at.y - Math.sin(aAngle) * (at.radius + 3);

          ctx.moveTo(ax, ay);
          ctx.lineTo(ax - aHeadlen * Math.cos(aAngle - Math.PI / 6), ay - aHeadlen * Math.sin(aAngle - Math.PI / 6));
          ctx.lineTo(ax - aHeadlen * Math.cos(aAngle + Math.PI / 6), ay - aHeadlen * Math.sin(aAngle + Math.PI / 6));
          ctx.closePath();
        }
        ctx.fillStyle = 'rgba(51, 65, 85, 0.65)';
        ctx.fill();
      }

      // 4. Draw Active Highlighted In/Out Edges & Directional Arrows
      for (var h = 0; h < activeHighlights.length; h++) {
        var hi = activeHighlights[h];
        var hs = hi.s;
        var ht = hi.t;

        ctx.beginPath();
        ctx.moveTo(hs.x, hs.y);
        ctx.lineTo(ht.x, ht.y);
        if (hi.isSpotlight) {
          ctx.strokeStyle = '#f59e0b';
          ctx.lineWidth = 4.8 / view.scale;
        } else if (hi.isOut) {
          ctx.strokeStyle = '#6366f1';
          ctx.lineWidth = 3.6 / view.scale;
        } else {
          ctx.strokeStyle = '#10b981';
          ctx.lineWidth = 3.6 / view.scale;
        }
        ctx.stroke();

        var hdx = ht.x - hs.x;
        var hdy = ht.y - hs.y;
        var hAngle = Math.atan2(hdy, hdx);
        var hHeadlen = (hi.isSpotlight ? 9.5 : 8.5) / view.scale;
        var hax = ht.x - Math.cos(hAngle) * (ht.radius + 3);
        var hay = ht.y - Math.sin(hAngle) * (ht.radius + 3);

        if (drawArrows) {
        ctx.beginPath();
        ctx.moveTo(hax, hay);
        ctx.lineTo(hax - hHeadlen * Math.cos(hAngle - Math.PI / 6), hay - hHeadlen * Math.sin(hAngle - Math.PI / 6));
        ctx.lineTo(hax - hHeadlen * Math.cos(hAngle + Math.PI / 6), hay - hHeadlen * Math.sin(hAngle + Math.PI / 6));
        ctx.closePath();
        ctx.fillStyle = hi.isSpotlight ? '#f59e0b' : (hi.isOut ? '#6366f1' : '#10b981');
        ctx.fill();

        }
        // Active Flow Pulse
        if (drawFlow && view.scale > 0.35) {
          var pOffset = (flowOffset + (hi.index * 0.13)) % 1.0;
          var px = hs.x + (ht.x - hs.x) * pOffset;
          var py = hs.y + (ht.y - hs.y) * pOffset;
          ctx.beginPath();
          ctx.arc(px, py, 3.2 / view.scale, 0, Math.PI * 2);
          ctx.fillStyle = hi.isSpotlight ? '#fef08a' : (hi.isOut ? '#a5b4fc' : '#6ee7b7');
          ctx.fill();
        }
      }

      // Live Citation Flow Pulse (Batched across all visible edges)
      if (drawFlow && !activeNode && view.scale > 0.4) {
        ctx.beginPath();
        for (var e = 0; e < visibleEdges.length; e++) {
          var fe = visibleEdges[e];
          var fs = fe.source;
          var ft = fe.target;
          var pOffset = (flowOffset + (e * 0.13)) % 1.0;
          var px = fs.x + (ft.x - fs.x) * pOffset;
          var py = fs.y + (ft.y - fs.y) * pOffset;
          ctx.moveTo(px + (1.6 / view.scale), py);
          ctx.arc(px, py, 1.6 / view.scale, 0, Math.PI * 2);
        }
        ctx.fillStyle = '#cbd5e1';
        ctx.fill();
      }
    }

    // Draw Nodes
    var labelBoxes = [];
    for (var i = 0; i < visibleNodes.length; i++) {
      var n = visibleNodes[i];
      var isSelf = (n === activeNode);
      var isInNeighbor = inSet.has(n) && (highlightNeighborhoodMode === 'all' || highlightNeighborhoodMode === 'inbound');
      var isOutNeighbor = outSet.has(n) && (highlightNeighborhoodMode === 'all' || highlightNeighborhoodMode === 'outbound');
      var isSpotlightNode = (n === hoveredLineageNode);

      if (activeNode && !isSelf && !isInNeighbor && !isOutNeighbor && !isSpotlightNode) {
        ctx.save();
        ctx.globalAlpha = 0.12;
        ctx.beginPath();
        ctx.arc(n.x, n.y, n.radius * 0.85, 0, Math.PI * 2);
        ctx.fillStyle = getNodeColor(n);
        ctx.fill();
        ctx.restore();
        continue;
      }

      ctx.beginPath();
      ctx.arc(n.x, n.y, n.radius * (isSelf ? 1.35 : (isInNeighbor || isOutNeighbor || isSpotlightNode ? 1.15 : 1.0)), 0, Math.PI * 2);
      ctx.fillStyle = getNodeColor(n);
      ctx.fill();

      // Outline rings
      if (isSelf) {
        ctx.strokeStyle = '#0f172a';
        ctx.lineWidth = 3.5 / view.scale;
        ctx.stroke();

        ctx.beginPath();
        ctx.arc(n.x, n.y, (n.radius * 1.35) + (4 / view.scale), 0, Math.PI * 2);
        ctx.strokeStyle = '#3b82f6';
        ctx.lineWidth = 2 / view.scale;
        ctx.stroke();
      } else if (isSpotlightNode) {
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 3 / view.scale;
        ctx.stroke();
      } else if (isInNeighbor) {
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 2.5 / view.scale;
        ctx.stroke();
      } else if (isOutNeighbor) {
        ctx.strokeStyle = '#6366f1';
        ctx.lineWidth = 2.5 / view.scale;
        ctx.stroke();
      } else if (n.tier === 500) {
        ctx.strokeStyle = '#ffffff88';
        ctx.lineWidth = 1.5 / view.scale;
        ctx.stroke();
      }

      // Title & Directional Badges
      var showLabel = isSelf || isSpotlightNode || isInNeighbor || isOutNeighbor || visibleNodes.length <= 30 || (n.total_degree > 18 && view.scale > 1.2);
      if (showLabel) {
        ctx.font = (isSelf || isSpotlightNode ? 'bold ' : '') + (11 / view.scale) + 'px sans-serif';
        ctx.textAlign = 'left';

        var prefix = '';
        var badgeColor = '#1e293b';
        if (isSelf) {
          prefix = '🎯 ';
          badgeColor = '#0f172a';
        } else if (isSpotlightNode) {
          prefix = '⚡ ';
          badgeColor = '#b45309';
        } else if (isInNeighbor) {
          prefix = '📥 Cited By: ';
          badgeColor = '#065f46';
        } else if (isOutNeighbor) {
          prefix = '📤 Cites: ';
          badgeColor = '#3730a3';
        }

        var labelText = prefix + (n.authors.split(';')[0].split(',')[0] || 'Paper') + ' (' + n.year + ')';
        var lx = n.x + n.radius + 5 / view.scale;
        var ly = n.y + 3 / view.scale;
        var box = { x: lx, y: ly - 11 / view.scale, w: ctx.measureText(labelText).width, h: 15 / view.scale };
        var overlaps = labelBoxes.some(function (b) { return box.x < b.x + b.w && box.x + box.w > b.x && box.y < b.y + b.h && box.y + box.h > b.y; });
        if (isSelf || (!overlaps && labelBoxes.length < 40)) {
          ctx.fillStyle = badgeColor;
          ctx.fillText(labelText, lx, ly);
          labelBoxes.push(box);
        }
      }
    }

    ctx.restore();
  }

  var isAnimating = false;

  function wakeAnimation() {
    if (!isAnimating) {
      isAnimating = true;
      animFrame = requestAnimationFrame(loop);
    }
  }

  function loop() {
    tickPhysics();
    render();

    var shouldContinue = (alpha >= 0.003) || (showFlowCheck.checked && showEdgesCheck.checked && visibleEdges.length > 0 && (hoveredNode || selectedNode || focusedSubgraphNode || allEdgesCheck.checked));
    if (shouldContinue) {
      animFrame = requestAnimationFrame(loop);
    } else {
      isAnimating = false;
    }
  }

  function getMousePos(e) {
    var rect = canvas.getBoundingClientRect();
    var mx = (e.clientX - rect.left);
    var my = (e.clientY - rect.top);
    var wx = (mx - view.tx) / view.scale;
    var wy = (my - view.ty) / view.scale;
    return { x: wx, y: wy, screenX: e.clientX, screenY: e.clientY };
  }

  function findNodeUnder(pos) {
    for (var i = visibleNodes.length - 1; i >= 0; i--) {
      var n = visibleNodes[i];
      var dist = Math.hypot(n.x - pos.x, n.y - pos.y);
      if (dist <= n.radius + 5 / view.scale) return n;
    }
    return null;
  }

  canvas.addEventListener('mouseleave', function () {
    hoveredNode = null; tooltip.classList.add('hidden'); wakeAnimation();
  });

  // Canvas Mouse Interactions
  canvas.addEventListener('mousemove', function (e) {
    wakeAnimation();
    var pos = getMousePos(e);

    if (draggingNode) {
      dragMoved = true;
      draggingNode.x = pos.x;
      draggingNode.y = pos.y;
      draggingNode.vx = 0;
      draggingNode.vy = 0;
      alpha = Math.max(alpha, 0.4);
      return;
    }

    if (isPanning) {
      dragMoved = true;
      view.tx += e.clientX - panStart.x;
      view.ty += e.clientY - panStart.y;
      panStart = { x: e.clientX, y: e.clientY };
      return;
    }

    var node = findNodeUnder(pos);
    hoveredNode = node;

    if (node) {
      canvas.style.cursor = 'pointer';
      var rect = canvas.getBoundingClientRect();
      tooltip.classList.remove('hidden');
      tooltip.style.maxWidth = Math.max(100, rect.width - 48) + 'px';
      tooltip.style.left = Math.max(0, Math.min(e.clientX - rect.left, rect.width - 350)) + 'px';
      tooltip.style.top = Math.max(0, Math.min(e.clientY - rect.top, rect.height - 180)) + 'px';

      var firstAuthor = node.authors.split(';')[0] || 'Author not recorded';
      tooltip.innerHTML = '<strong>' + escapeHtml(node.title) + '</strong><div class="meta">' + escapeHtml(firstAuthor) + (node.authors.indexOf(';') !== -1 ? ' et al.' : '') + ' · ' + node.year + '</div>';

    } else {
      canvas.style.cursor = 'grab';
      tooltip.classList.add('hidden');
    }
  });

  canvas.addEventListener('mousedown', function (e) {
    wakeAnimation();
    dragMoved = false;
    var pos = getMousePos(e);
    var node = findNodeUnder(pos);

    if (node) {
      draggingNode = node;
      canvas.classList.add('dragging');
      alpha = Math.max(alpha, 0.45);
    } else {
      isPanning = true;
      panStart = { x: e.clientX, y: e.clientY };
      canvas.classList.add('dragging');
    }
  });

  window.addEventListener('mouseup', function (e) {
    wakeAnimation();
    if (draggingNode && !dragMoved) {
      selectedNode = draggingNode;
      openPaperDrawer(draggingNode);
    }
    draggingNode = null;
    isPanning = false;
    canvas.classList.remove('dragging');
  });

  canvas.addEventListener('wheel', function (e) {
    wakeAnimation();
    e.preventDefault();
    var rect = canvas.getBoundingClientRect();
    var mx = e.clientX - rect.left;
    var my = e.clientY - rect.top;
    var zoomFactor = e.deltaY < 0 ? 1.15 : 0.85;
    var newScale = Math.max(0.15, Math.min(4.5, view.scale * zoomFactor));

    view.tx = mx - (mx - view.tx) * (newScale / view.scale);
    view.ty = my - (my - view.ty) * (newScale / view.scale);
    view.scale = newScale;
    wakeAnimation();
  }, { passive: false });

  // Mobile Touch Gestures & Pinch-to-Zoom
  var initialTouchDist = null;
  var touchMoved = false;

  function getTouchDistance(t1, t2) {
    return Math.hypot(t1.clientX - t2.clientX, t1.clientY - t2.clientY);
  }

  canvas.addEventListener('touchstart', function (e) {
    wakeAnimation();
    touchMoved = false;
    if (e.touches.length === 1) {
      var t = e.touches[0];
      var pos = getMousePos(t);
      var node = findNodeUnder(pos);
      if (node) {
        draggingNode = node;
        alpha = Math.max(alpha, 0.45);
      } else {
        isPanning = true;
        panStart = { x: t.clientX, y: t.clientY };
      }
    } else if (e.touches.length === 2) {
      isPanning = false;
      draggingNode = null;
      initialTouchDist = getTouchDistance(e.touches[0], e.touches[1]);
    }
  }, { passive: false });

  canvas.addEventListener('touchmove', function (e) {
    wakeAnimation();
    e.preventDefault();
    touchMoved = true;

    if (e.touches.length === 1) {
      var t = e.touches[0];
      var pos = getMousePos(t);
      if (draggingNode) {
        draggingNode.x = pos.x;
        draggingNode.y = pos.y;
        draggingNode.vx = 0;
        draggingNode.vy = 0;
        alpha = Math.max(alpha, 0.4);
      } else if (isPanning) {
        view.tx += t.clientX - panStart.x;
        view.ty += t.clientY - panStart.y;
        panStart = { x: t.clientX, y: t.clientY };
      }
    } else if (e.touches.length === 2 && initialTouchDist) {
      var currentDist = getTouchDistance(e.touches[0], e.touches[1]);
      var zoomFactor = currentDist / initialTouchDist;
      initialTouchDist = currentDist;

      var rect = canvas.getBoundingClientRect();
      var cx = (e.touches[0].clientX + e.touches[1].clientX) / 2 - rect.left;
      var cy = (e.touches[0].clientY + e.touches[1].clientY) / 2 - rect.top;

      var newScale = Math.max(0.15, Math.min(4.5, view.scale * zoomFactor));
      view.tx = cx - (cx - view.tx) * (newScale / view.scale);
      view.ty = cy - (cy - view.ty) * (newScale / view.scale);
      view.scale = newScale;
    }
  }, { passive: false });

  canvas.addEventListener('touchend', function (e) {
    wakeAnimation();
    if (draggingNode && !touchMoved) {
      selectedNode = draggingNode;
      openPaperDrawer(draggingNode);
    }
    if (e.touches.length === 1) {
      initialTouchDist = null;
      draggingNode = null;
      isPanning = true;
      panStart = { x: e.touches[0].clientX, y: e.touches[0].clientY };
    }
    if (e.touches.length === 0) {
      draggingNode = null;
      isPanning = false;
      initialTouchDist = null;
    }
  });

  canvas.addEventListener('touchcancel', function () {
    draggingNode = null; isPanning = false; initialTouchDist = null;
    wakeAnimation();
  });

  // Floating HUD Handlers
  function zoomBy(factor) {
    var cw = canvas.width / canvasRatio;
    var ch = canvas.height / canvasRatio;
    var mx = cw / 2;
    var my = ch / 2;
    var newScale = Math.max(0.15, Math.min(4.5, view.scale * factor));
    view.tx = mx - (mx - view.tx) * (newScale / view.scale);
    view.ty = my - (my - view.ty) * (newScale / view.scale);
    view.scale = newScale;
    wakeAnimation();
  }

  hudZoomInBtn.addEventListener('click', function () { zoomBy(1.25); });
  hudZoomOutBtn.addEventListener('click', function () { zoomBy(0.8); });
  hudFitBtn.addEventListener('click', function () { fitView(); });
  sidebarFitBtn.addEventListener('click', function () { fitView(); });

  function reheatPhysics() {
    if (currentLayout !== 'organic') { arrangeNodes(); fitView(); }
    alpha = currentLayout === 'organic' ? 1 : 0;
    wakeAnimation();
  }
  hudReheatBtn.addEventListener('click', reheatPhysics);
  sidebarReheatBtn.addEventListener('click', reheatPhysics);

  // Publication-first drawer: no category-generated claims.
  function openPaperDrawer(p) {
    if (panel.classList.contains('hidden')) drawerReturnFocus = document.activeElement;
    panel.classList.remove('hidden');
    if (panelClose.focus) panelClose.focus({ preventScroll: true });
    var pdfUrl = evidenceApi ? evidenceApi.safeSourceUrl(p.pdf_url) : '';
    var pdfButton = pdfUrl ? '<a href="' + escapeHtml(pdfUrl) + '" target="_blank" rel="noopener" class="jcg-drawer-btn jcg-drawer-btn-pdf">Open access copy</a>' : '';
    var fullCardUrl = JC_BASE_URL + '?paper=' + encodeURIComponent(p.id);

    var evidenceHtml = evidenceApi ? evidenceApi.render(p.evidence, p.doi) :
      '<p class="jcg-hint">Contribution notes could not load. Open the publication for its findings.</p>';
    var publicationHtml = evidenceApi ? evidenceApi.renderPublicationLinks(p.publication_links, p.doi) : '';
    var isCorrection = p.publication_links && p.publication_links.kind === 'correction';
    if (isCorrection) evidenceHtml = '';

    // Interactive Citation Lineage Chips
    var citingChipsHtml = '';
    if (p.citedByNodes && p.citedByNodes.length) {
      citingChipsHtml = '<div class="jcg-lineage-section">' +
        '<h4>Cited By (' + p.citedByNodes.length + ' Papers in Corpus) &darr;</h4>' +
        '<div class="jcg-lineage-chips">' +
          p.citedByNodes.slice(0, 10).map(function (cp) {
            return '<button type="button" class="jcg-lineage-chip citing-chip" data-paper-id="' + escapeHtml(cp.id) + '">' +
              '<strong>' + escapeHtml(cp.authors.split(';')[0].split(',')[0] || 'Author') + ' (' + cp.year + ')</strong>: ' +
              escapeHtml(cp.title.length > 38 ? cp.title.slice(0, 36) + '…' : cp.title) +
            '</button>';
          }).join('') +
          (p.citedByNodes.length > 10 ? '<span style="font-size:0.72rem; color:#64748b; align-self:center;">+' + (p.citedByNodes.length - 10) + ' more</span>' : '') +
        '</div>' +
      '</div>';
    }

    var citedChipsHtml = '';
    if (p.citesNodes && p.citesNodes.length) {
      citedChipsHtml = '<div class="jcg-lineage-section">' +
        '<h4>Cites (' + p.citesNodes.length + ' References in Corpus) &uarr;</h4>' +
        '<div class="jcg-lineage-chips">' +
          p.citesNodes.slice(0, 10).map(function (cp) {
            return '<button type="button" class="jcg-lineage-chip cited-chip" data-paper-id="' + escapeHtml(cp.id) + '">' +
              '<strong>' + escapeHtml(cp.authors.split(';')[0].split(',')[0] || 'Author') + ' (' + cp.year + ')</strong>: ' +
              escapeHtml(cp.title.length > 38 ? cp.title.slice(0, 36) + '…' : cp.title) +
            '</button>';
          }).join('') +
          (p.citesNodes.length > 10 ? '<span style="font-size:0.72rem; color:#64748b; align-self:center;">+' + (p.citesNodes.length - 10) + ' more</span>' : '') +
        '</div>' +
      '</div>';
    }

    var inCount = (p.citedByNodes && p.citedByNodes.length) || 0;
    var outCount = (p.citesNodes && p.citesNodes.length) || 0;
    var totalNeighbors = inCount + outCount;

    var neighborhoodToolbarHtml = '<div class="jcg-neighborhood-toolbar">' +
      '<span class="jcg-neighborhood-title">Citation links (' + totalNeighbors + ' Direct Links)</span>' +
      '<div class="jcg-neighborhood-pills">' +
        '<button type="button" class="jcg-nill-btn ' + (highlightNeighborhoodMode === 'all' ? 'active' : '') + '" data-dir="all">All (In+Out: ' + totalNeighbors + ')</button>' +
        '<button type="button" class="jcg-nill-btn ' + (highlightNeighborhoodMode === 'inbound' ? 'active' : '') + '" data-dir="inbound">Cited by (' + inCount + ')</button>' +
        '<button type="button" class="jcg-nill-btn ' + (highlightNeighborhoodMode === 'outbound' ? 'active' : '') + '" data-dir="outbound">Cites (' + outCount + ')</button>' +
      '</div>' +
    '</div>';

    var indexingHtml = '<details class="jcg-paper-metadata"><summary>Indexing information</summary>' +
      '<p class="jcg-hint">Topic and organism tags support navigation; they are not verified methods, dataset use, affiliations, or results. Citation links record references, not agreement or demonstrated improvements.</p>' +
      '<p>Assigned topic: ' + escapeHtml(p.dimension.replace(/-/g, ' ')) + '. Organism tags: ' + escapeHtml(organismLabel(p)) + '.</p>' +
      '<p class="jcg-hint">Imported network metrics: in ' + p.in_degree + ', out ' + p.out_degree + '. These may include links outside the displayed corpus and are not measures of scientific quality. The citation controls above count links resolved within this corpus.</p>' +
      '<button type="button" class="jcg-secondary-btn" id="jcg-btn-ai-prompt">Prepare a paper review prompt</button></details>';
    var abstractHtml = isCorrection ? '' : '<section class="jcg-paper-abstract"><h4>Paper abstract</h4><p>' +
      (p.abstract ? escapeHtml(p.abstract) : 'Abstract not available in this corpus. Open the publication to read it.') + '</p></section>';

    var html = '<h3>' + escapeHtml(p.title) + '</h3>' +
      '<div class="jcg-panel-authors">' + escapeHtml(p.authors) + ' &bull; <em>' + escapeHtml(p.journal) + '</em> (' + p.year + ')</div>' +
      '<div class="jcg-drawer-actions">' +
        '<button type="button" class="jcg-drawer-btn jcg-drawer-btn-focus" id="jcg-btn-focus-subgraph">Explore citations</button>' +
        '<a href="' + fullCardUrl + '" class="jcg-drawer-btn jcg-drawer-btn-jc">Paper abstract and evidence</a>' +
        (p.doi ? '<a href="https://doi.org/' + escapeHtml(p.doi) + '" target="_blank" rel="noopener" class="jcg-drawer-btn jcg-drawer-btn-doi">Open publication</a>' : '') +
        pdfButton +
      '</div>' +
      neighborhoodToolbarHtml +
      publicationHtml +
      abstractHtml +
      evidenceHtml +
      indexingHtml +
      citingChipsHtml +
      citedChipsHtml +
      '<div class="jcg-ocar-step" style="margin-top:1rem; font-size:0.75rem; color:#64748b;">' +
        '<strong>Full Citation:</strong> ' + escapeHtml(p.citation) +
      '</div>';

    panelBody.innerHTML = html;

    // Attach neighborhood mode toggles
    var nillButtons = Array.from(panelBody.querySelectorAll('.jcg-nill-btn'));
    nillButtons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        nillButtons.forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        highlightNeighborhoodMode = btn.dataset.dir;
        wakeAnimation();
      });
    });

    // Attach drawer button listeners
    var aiPromptBtn = document.getElementById('jcg-btn-ai-prompt');
    if (aiPromptBtn) {
      aiPromptBtn.addEventListener('click', function () {
        singlePaperTarget = p;
        document.getElementById('jcg-prompt-mode-tabs').style.display = 'none';
        openAiTray();
      });
    }

    var focusSubBtn = document.getElementById('jcg-btn-focus-subgraph');
    if (focusSubBtn) {
      focusSubBtn.addEventListener('click', function () { enterSubgraphFocus(p); });
    }

    // Attach lineage jump chips and hover spotlights
    var lineageChips = Array.from(panelBody.querySelectorAll('.jcg-lineage-chip'));
    lineageChips.forEach(function (chip) {
      chip.addEventListener('mouseenter', function () {
        var pid = chip.dataset.paperId;
        hoveredLineageNode = idMap[pid] || null;
        wakeAnimation();
      });
      chip.addEventListener('mouseleave', function () {
        hoveredLineageNode = null;
        wakeAnimation();
      });
      chip.addEventListener('click', function () {
        var pid = chip.dataset.paperId;
        var targetPaper = idMap[pid];
        if (targetPaper) {
          if (targetPaper.tier > currentTier) {
            currentTier = targetPaper.tier;
            tierButtons.forEach(function (b) { b.classList.toggle('active', b.dataset.tier === String(currentTier)); });
            applyFilters();
          }
          if (visibleNodes.indexOf(targetPaper) === -1) enterSubgraphFocus(targetPaper);
          selectAndCenterPaper(targetPaper);
        }
      });
    });
  }

  var drawerReturnFocus = null;
  panelClose.addEventListener('click', function () {
    panel.classList.add('hidden'); selectedNode = null; wakeAnimation();
    if (drawerReturnFocus && drawerReturnFocus.isConnected && drawerReturnFocus.focus) drawerReturnFocus.focus({ preventScroll: true });
  });
  window.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && !panel.classList.contains('hidden')) {
      event.preventDefault(); panelClose.click();
    }
  });

  // AI Synthesis Prompt Generation
  var currentPromptMode = 'synthesis';
  var singlePaperTarget = null;
  var modalTitleEl = document.getElementById('jcg-prompt-modal-title');
  var modalDescEl = document.getElementById('jcg-prompt-modal-desc');
  var modeButtons = Array.from(document.querySelectorAll('.jcg-pmode-btn'));

  function generateSynthesisPrompt() {
    var selection = singlePaperTarget ? [singlePaperTarget] : visibleNodes;
    var count = selection.length;
    modalTitleEl.textContent = singlePaperTarget ? 'Paper review prompt' : 'Research review prompt';
    modalDescEl.textContent = singlePaperTarget ?
      'Uses this publication’s recorded abstract and any source-checked contribution note. Verify against the original.' :
      'Uses the first ' + Math.min(count, 35) + ' of ' + count + ' matches in the current order; not a representative or quality-ranked sample.';
    promptTextarea.value = evidenceApi ? evidenceApi.reviewPrompt(selection, currentPromptMode, count) :
      'The review prompt helper did not load. Reload to retry, or open the original publications directly.';
  }

  function openAiTray() {
    aiTray.classList.remove('collapsed');
    aiTrayToggleBtn.textContent = '▴ Collapse Tray';
    aiTrayStatusText.textContent = 'Click to collapse';
    generateSynthesisPrompt();
    copyStatus.classList.add('hidden');
    aiTray.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  function toggleAiTray() {
    if (aiTray.classList.contains('collapsed')) {
      openAiTray();
    } else {
      aiTray.classList.add('collapsed');
      aiTrayToggleBtn.textContent = '▾ Expand Tray';
      aiTrayStatusText.textContent = 'Click to expand';
    }
  }

  aiTrayHeader.addEventListener('click', function (e) {
    if (e.target !== aiTrayToggleBtn) {
      toggleAiTray();
    }
  });
  aiTrayToggleBtn.addEventListener('click', toggleAiTray);

  // Open tray from sidebar trigger button
  promptTriggerBtn.addEventListener('click', function () {
    singlePaperTarget = null;
    document.getElementById('jcg-prompt-mode-tabs').style.display = 'flex';
    openAiTray();
  });

  // Prompt Mode Switching
  modeButtons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      // Selected state lives in `.jcg-pmode-btn.active` in this page's style
      // block. It used to be written here as inline styles, with the class
      // toggled alongside and nothing matching it.
      modeButtons.forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      currentPromptMode = btn.dataset.mode;
      generateSynthesisPrompt();
    });
  });

  copyPromptBtn.addEventListener('click', function () {
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

  // UI Event Listeners
  tierButtons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      tierButtons.forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      currentTier = parseInt(btn.dataset.tier, 10);
      changeFilters();
      fitView();
    });
  });

  layoutButtons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      layoutButtons.forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      currentLayout = btn.dataset.mode;
      applyFilters();
      fitView();
    });
  });

  showEdgesCheck.addEventListener('change', wakeAnimation);
  allEdgesCheck.addEventListener('change', wakeAnimation);
  showArrowsCheck.addEventListener('change', wakeAnimation);
  showFlowCheck.addEventListener('change', wakeAnimation);
  if (edgeWeightingEl) {
    edgeWeightingEl.addEventListener('change', function () {
      currentEdgeWeighting = edgeWeightingEl.value;
      wakeAnimation();
    });
  }

  colorByEl.addEventListener('change', function () {
    currentColorCue = colorByEl.value;
    updateLegend();
    wakeAnimation();
  });

  function changeFilters() {
    clearTimeout(filterTimer);
    focusedSubgraphNode = null;
    focusBanner.classList.add('hidden');
    applyFilters();
  }
  function queueFilters() {
    clearTimeout(filterTimer);
    filterTimer = setTimeout(changeFilters, 180);
  }
  eraChecks.forEach(function (c) { c.addEventListener('change', queueFilters); });
  dimensionEl.addEventListener('change', queueFilters);
  organismEl.addEventListener('change', queueFilters);
  degreeEl.addEventListener('input', function () { degreeVal.textContent = degreeEl.value; queueFilters(); });
  searchEl.addEventListener('input', queueFilters);

  resetBtn.addEventListener('click', function () {
    focusedSubgraphNode = null;
    focusBanner.classList.add('hidden');
    currentTier = 2000;
    clearTimeout(filterTimer);
    selectedNode = null;
    panel.classList.add('hidden');
    singlePaperTarget = null;
    highlightNeighborhoodMode = 'all';
    currentLayout = 'cluster';
    currentEdgeWeighting = 'sum';
    edgeWeightingEl.value = 'sum';
    currentColorCue = 'dimension';
    colorByEl.value = 'dimension';
    showEdgesCheck.checked = true;
    allEdgesCheck.checked = false;
    showArrowsCheck.checked = false;
    showFlowCheck.checked = false;
    tierButtons.forEach(function (b) { b.classList.toggle('active', b.dataset.tier === '2000'); });
    layoutButtons.forEach(function (b) { b.classList.toggle('active', b.dataset.mode === 'cluster'); });
    eraChecks.forEach(function (c) { c.checked = true; });
    dimensionEl.value = 'all';
    organismEl.value = 'all';
    degreeEl.value = '0';
    degreeVal.textContent = '0';
    searchEl.value = '';
    updateLegend();
    applyFilters();
    fitView();
  });

})();
</script>
