---
layout: default
title: "Citation Graph Explorer"
permalink: /technical-training/journal-club/graph/
track: core-concepts-methods
pathways:
  - technical foundation
  - shared vocabulary
description: "Interactive citation graph explorer across 500, 1,000, and 2,000 curated papers in connectomics: self-organizing organic force clustering, weighted directed citation edges, deep OCAR research cards, and AI synthesis prompts."
content_type: core
---

<div class="layout-content layout-page">

<section class="jc-hero" style="text-align: center; margin-bottom: 1.5rem;">
  <h1>Citation Graph Explorer</h1>
  <p style="font-size: 1.1rem; color: #555; max-width: 850px; margin: 0.5rem auto 0;">
    Explore the curated connectomics literature network across <strong>500 Flagships</strong>, <strong>1,000 Landmark Works</strong>, and the <strong>2,000-Paper Comprehensive Graph</strong>. Features self-organizing organic force clustering, weighted directed citation edges, interactive lineage traversal, and deep OCAR research cards.
  </p>
</section>

<section class="section section-compact">
  <div class="jcg-layout">
    
    <!-- Controls Sidebar -->
    <div class="jcg-controls">
      
      <!-- Tier Selector -->
      <div class="jcg-control-group">
        <label for="jcg-tier-buttons">Corpus Scale Tier:</label>
        <div class="jcg-tier-btn-group" id="jcg-tier-buttons">
          <button type="button" class="jcg-tier-btn active" data-tier="500">500 Key Papers</button>
          <button type="button" class="jcg-tier-btn" data-tier="1000">1000 Key Papers</button>
          <button type="button" class="jcg-tier-btn" data-tier="2000">2000 Key Papers</button>
        </div>
      </div>

      <!-- Layout Mode -->
      <div class="jcg-control-group">
        <label for="jcg-layout-buttons">Layout Clustering Mode:</label>
        <div class="jcg-tier-btn-group" id="jcg-layout-buttons">
          <button type="button" class="jcg-layout-btn active" data-mode="organic">Organic Force</button>
          <button type="button" class="jcg-layout-btn" data-mode="cluster">Category Hubs</button>
          <button type="button" class="jcg-layout-btn" data-mode="timeline">Timeline</button>
        </div>
      </div>

      <!-- Edge Controls -->
      <fieldset class="jcg-era-fieldset">
        <legend>Citation Edges &amp; Dynamics</legend>
        <label><input type="checkbox" id="jcg-show-edges" checked> Draw Citation Edges</label>
        <label><input type="checkbox" id="jcg-show-arrows" checked> Show Directional Arrows (&rarr;)</label>
        <label><input type="checkbox" id="jcg-show-flow" checked> ⚡ Flow Pulse Animation</label>
      </fieldset>

      <!-- Node Color Cue Selector -->
      <div class="jcg-control-group">
        <label for="jcg-color-by">Color Cue (Node Color):</label>
        <select id="jcg-color-by">
          <option value="dimension">Category / Subfield (12 Domains)</option>
          <option value="era">Publication Era (History / Contemporary / SOTA)</option>
          <option value="tier">Corpus Tier (500 Flagship / 1000 / 2000)</option>
          <option value="organism">Model Organism (Mouse, Fly, Human, etc.)</option>
          <option value="citation_role">Citation Role (Foundational / Hub / Bridge)</option>
        </select>
      </div>

      <!-- Category Filter -->
      <div class="jcg-control-group">
        <label for="jcg-dimension">Category / Domain:</label>
        <select id="jcg-dimension">
          <option value="all">All 12 Categories</option>
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
        </select>
      </div>

      <!-- Organism Filter -->
      <div class="jcg-control-group">
        <label for="jcg-organism">Organism / Model System:</label>
        <select id="jcg-organism">
          <option value="all">All Organisms</option>
          <option value="mouse">Mouse (Mus musculus)</option>
          <option value="drosophila">Drosophila (Fruit Fly)</option>
          <option value="human">Human Cortex</option>
          <option value="c-elegans">C. elegans</option>
          <option value="zebrafish">Zebrafish</option>
          <option value="cross-species">Cross-Species &amp; Comparative</option>
          <option value="theory-model">Theory &amp; Computational Models</option>
        </select>
      </div>

      <!-- Era Filter -->
      <fieldset class="jcg-era-fieldset">
        <legend>Publication Era</legend>
        <label><input type="checkbox" class="jcg-era-check" value="history" checked> History (&le;2018)</label>
        <label><input type="checkbox" class="jcg-era-check" value="contemporary" checked> Contemporary (2019–2023)</label>
        <label><input type="checkbox" class="jcg-era-check" value="sota" checked> SOTA (2024–2026+)</label>
      </fieldset>

      <!-- Minimum Centrality / Degree -->
      <div class="jcg-control-group">
        <label for="jcg-min-degree">Minimum Degree: <span id="jcg-degree-val">0</span></label>
        <input type="range" id="jcg-min-degree" min="0" max="60" value="0" step="1">
      </div>

      <!-- Search Filter -->
      <div class="jcg-control-group">
        <label for="jcg-search">Search (Title, Author, OCAR, Method):</label>
        <input type="text" id="jcg-search" placeholder="e.g. MICrONS, Kasthuri, proofreading, U-Net...">
      </div>

      <!-- Action Buttons -->
      <div class="jcg-control-group" style="margin-top: 0.25rem; gap: 0.4rem;">
        <button id="jcg-prompt-btn" type="button" class="jcg-secondary-btn" style="width:100%; font-weight:600;">
          🤖 Open AI Synthesis Tray (<span id="jcg-prompt-count">500</span>)
        </button>
        <div style="display: flex; gap: 0.4rem;">
          <button id="jcg-sidebar-fit" type="button" class="jcg-secondary-btn" style="flex:1;">⛶ Fit View</button>
          <button id="jcg-sidebar-reheat" type="button" class="jcg-secondary-btn" style="flex:1;">⚡ Reheat</button>
        </div>
      </div>

      <button id="jcg-reset" type="button">Reset View &amp; Filters</button>

      <p class="jcg-count" id="jcg-count">Showing 500 papers</p>
      <p class="jcg-hint">💡 Drag nodes to pull physics &bull; Drag background to pan &bull; Scroll to zoom &bull; Click node for full OCAR card</p>

      <div class="jcg-legend-title" id="jcg-legend-title" style="font-weight:700; font-size:0.78rem; color:#374151; margin-top:0.4rem;">Color Cue Legend:</div>
      <div class="jcg-legend" id="jcg-legend"></div>
    </div>

    <!-- Canvas Container & Interactive Drawer -->
    <div style="display: flex; flex-direction: column; gap: 1rem;">
      <div class="jcg-canvas-wrap">
        <canvas id="jcg-canvas"></canvas>
        
        <!-- On-Canvas Floating HUD Controls -->
        <div class="jcg-canvas-hud">
          <button type="button" id="jcg-hud-zoom-in" title="Zoom In">+</button>
          <button type="button" id="jcg-hud-zoom-out" title="Zoom Out">&minus;</button>
          <button type="button" id="jcg-hud-fit" title="Fit to Screen">⛶</button>
          <button type="button" id="jcg-hud-reheat" title="Reheat Physics &amp; Relax Layout">⚡</button>
        </div>

        <!-- Subgraph Focus Mode Active Banner -->
        <div class="jcg-focus-banner hidden" id="jcg-focus-banner">
          <span>🎯 Focusing on Subgraph of: <strong id="jcg-focus-paper-title">Paper</strong></span>
          <button type="button" id="jcg-focus-exit-btn" title="Exit Focus Mode">✕ Exit Subgraph Focus</button>
        </div>

        <div class="jcg-tooltip hidden" id="jcg-tooltip"></div>
        
        <!-- Slide-Out Paper Detail Drawer with Deep OCAR Integration -->
        <div class="jcg-panel hidden" id="jcg-panel">
          <button class="jcg-panel-close" id="jcg-panel-close" aria-label="Close">&times;</button>
          <div class="jcg-panel-body" id="jcg-panel-body">
            <!-- Dynamically populated with OCAR cards, 3-tier summaries, and citation lineage -->
          </div>
        </div>
      </div>

      <!-- On-Demand AI Literature Synthesis & Discussion Tray -->
      <div class="jcg-ai-tray collapsed" id="jcg-ai-tray">
        <div class="jcg-ai-tray-header" id="jcg-ai-tray-header">
          <h3 id="jcg-prompt-modal-title">🤖 AI Research Synthesis &amp; Discussion Tray</h3>
          <div style="display: flex; align-items: center; gap: 0.5rem;">
            <span style="font-size: 0.75rem; color: #64748b;" id="jcg-tray-status-text">Click to expand</span>
            <button type="button" class="jcg-ai-tray-toggle-btn" id="jcg-ai-tray-toggle">▾ Expand Tray</button>
          </div>
        </div>
        
        <div class="jcg-ai-tray-body">
          <p class="jcg-prompt-modal-desc" id="jcg-prompt-modal-desc" style="margin-bottom: 0.75rem; color: #475569; font-size: 0.82rem;">
            Copy this grounded prompt into <strong>ChatGPT</strong>, <strong>Claude</strong>, or <strong>Gemini</strong> across the <strong id="jcg-modal-paper-count">0</strong> papers currently in your active filter.
          </p>

          <!-- Mode Switcher Tabs -->
          <div class="jcg-prompt-modes" id="jcg-prompt-mode-tabs" style="display: flex; flex-wrap: wrap; gap: 0.35rem; margin-bottom: 0.75rem; background: #f1f5f9; padding: 0.25rem; border-radius: 8px;">
            <button type="button" class="jcg-pmode-btn active" data-mode="synthesis" style="flex: 1; min-width: 130px; padding: 0.35rem 0.5rem; font-size: 0.76rem; font-weight: 700; border: none; border-radius: 6px; background: #1a56db; color: #fff; cursor: pointer;">📑 Synthesis Review</button>
            <button type="button" class="jcg-pmode-btn" data-mode="methods" style="flex: 1; min-width: 130px; padding: 0.35rem 0.5rem; font-size: 0.76rem; font-weight: 600; border: none; border-radius: 6px; background: transparent; color: #475569; cursor: pointer;">🔬 Methods Compare</button>
            <button type="button" class="jcg-pmode-btn" data-mode="problems" style="flex: 1; min-width: 130px; padding: 0.35rem 0.5rem; font-size: 0.76rem; font-weight: 600; border: none; border-radius: 6px; background: transparent; color: #475569; cursor: pointer;">💡 Open Problems</button>
            <button type="button" class="jcg-pmode-btn" data-mode="seminar" style="flex: 1; min-width: 130px; padding: 0.35rem 0.5rem; font-size: 0.76rem; font-weight: 600; border: none; border-radius: 6px; background: transparent; color: #475569; cursor: pointer;">🎓 Seminar Guide</button>
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
.jcg-layout { display: grid; grid-template-columns: 300px 1fr; gap: 1.25rem; align-items: start; margin-top: 1rem; }
@media (max-width: 960px) { .jcg-layout { grid-template-columns: 1fr; } }
.jcg-controls { display: flex; flex-direction: column; gap: 0.75rem; font-size: 0.85rem; background: #fafafa; border: 1px solid #e5e7eb; border-radius: 10px; padding: 1.25rem; }
.jcg-control-group { display: flex; flex-direction: column; gap: 0.3rem; }
.jcg-control-group label { font-weight: 600; color: #374151; font-size: 0.82rem; }

.jcg-tier-btn-group { display: flex; border: 1px solid #d1d5db; border-radius: 6px; overflow: hidden; background: #fff; }
.jcg-tier-btn, .jcg-layout-btn { flex: 1; padding: 0.4rem 0.2rem; font-size: 0.75rem; font-weight: 600; border: none; background: transparent; cursor: pointer; color: #4b5563; transition: all 0.15s ease; text-align: center; }
.jcg-tier-btn:not(:last-child), .jcg-layout-btn:not(:last-child) { border-right: 1px solid #d1d5db; }
.jcg-tier-btn.active, .jcg-layout-btn.active { background: #1a56db; color: #fff; }
.jcg-tier-btn:hover:not(.active), .jcg-layout-btn:hover:not(.active) { background: #f3f4f6; }

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

.jcg-canvas-wrap { position: relative; background: #ffffff; border: 1px solid #e5e7eb; border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.06); overflow: hidden; height: 760px; }
#jcg-canvas { display: block; width: 100%; height: 100%; cursor: grab; }
#jcg-canvas.dragging { cursor: grabbing; }

/* Floating Canvas HUD */
.jcg-canvas-hud {
  position: absolute; bottom: 1.25rem; right: 1.25rem; display: flex; flex-direction: column; gap: 0.35rem;
  z-index: 15; background: rgba(255, 255, 255, 0.92); backdrop-filter: blur(8px);
  padding: 0.35rem; border-radius: 8px; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.jcg-canvas-hud button {
  width: 32px; height: 32px; border: 1px solid #cbd5e1; border-radius: 6px;
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
  background: #ffffff; border-radius: 12px; box-shadow: 0 12px 36px rgba(0,0,0,0.22);
  border: 1px solid #cbd5e1; padding: 1.35rem; max-height: calc(100% - 2rem); overflow-y: auto; z-index: 20;
}
.jcg-panel.hidden { display: none; }
.jcg-panel-close {
  position: absolute; top: 0.75rem; right: 0.85rem; background: none; border: none;
  font-size: 1.5rem; line-height: 1; cursor: pointer; color: #94a3b8; padding: 0.2rem;
}
.jcg-panel-close:hover { color: #0f172a; }

@media (max-width: 768px) {
  .jcg-canvas-wrap { height: 520px; border-radius: 8px; }
  .jcg-panel {
    top: auto; bottom: 0; left: 0; right: 0;
    width: 100%; max-width: 100%;
    max-height: 80vh; border-radius: 16px 16px 0 0;
    padding: 1.1rem; box-shadow: 0 -8px 30px rgba(0,0,0,0.25);
  }
  .jcg-prompt-modal { padding: 0.75rem; }
  .jcg-prompt-modal-content { max-height: 94vh; padding: 1rem; }
}

.jcg-panel-body h3 { margin: 0 1.75rem 0.4rem 0; font-size: 1.1rem; line-height: 1.35; color: #0f172a; font-weight: 700; }
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

/* 5-Part OCAR Container */
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

.jcg-analysis-pipeline { margin-top: 0.5rem; border-top: 1px dashed #cbd5e1; padding-top: 0.5rem; }
.jcg-pipe-stage {
  display: flex; gap: 0.5rem; margin-bottom: 0.4rem; font-size: 0.76rem; line-height: 1.35;
  background: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.4rem 0.55rem;
}
.jcg-pipe-badge {
  font-weight: 700; font-size: 0.68rem; padding: 0.15rem 0.4rem; border-radius: 4px; height: fit-content;
  white-space: nowrap; flex-shrink: 0;
}
.jcg-badge-prep { background: #fef3c7; color: #92400e; }
.jcg-badge-recon { background: #dbeafe; color: #1e40af; }
.jcg-badge-ai { background: #ede9fe; color: #5b21b6; }
.jcg-badge-qc { background: #d1fae5; color: #065f46; }
.jcg-badge-stats { background: #fce7f3; color: #9d174d; }
.jcg-pipe-desc strong { color: #1e293b; display: block; font-size: 0.74rem; }
.jcg-pipe-desc p { margin: 0.1rem 0 0 0; color: #475569; font-size: 0.72rem; }

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
</style>

<script>
(function () {
  var DATA_URL = "{{ '/technical-training/journal-club/graph-data.json' | relative_url }}";
  var JC_BASE_URL = "{{ '/technical-training/journal-club/' | relative_url }}";

  var CATEGORIES = [
    'circuit-structure', 'pipeline', 'physiology', 'behaviour',
    'imaging', 'cell-types', 'neuroanatomy', 'synthesis',
    'dataset', 'neuroai', 'health', 'training-outreach'
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
    'training-outreach': '#16a34a'
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
    'general': '#64748b'
  };

  var ROLE_COLORS = {
    'core_hub': '#f59e0b',
    'authority': '#8b5cf6',
    'bridge': '#06b6d4',
    'connected': '#10b981',
    'participant': '#64748b'
  };

  // Pre-computed Category Hub Radial Anchors
  var CATEGORY_HUBS = {};
  CATEGORIES.forEach(function (cat, i) {
    var angle = (i / CATEGORIES.length) * Math.PI * 2 - Math.PI / 2;
    var radius = 320;
    CATEGORY_HUBS[cat] = {
      x: Math.cos(angle) * radius,
      y: Math.sin(angle) * radius
    };
  });

  // DOM Elements
  var canvas = document.getElementById('jcg-canvas');
  var ctx = canvas.getContext('2d');
  var tierButtons = Array.from(document.querySelectorAll('.jcg-tier-btn'));
  var layoutButtons = Array.from(document.querySelectorAll('.jcg-layout-btn'));
  var showEdgesCheck = document.getElementById('jcg-show-edges');
  var showArrowsCheck = document.getElementById('jcg-show-arrows');
  var showFlowCheck = document.getElementById('jcg-show-flow');
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
  var currentTier = 500;
  var currentLayout = 'organic';
  var currentColorCue = 'dimension';
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
        { k: 'Contemporary (2019–2023)', c: ERA_COLORS['contemporary'] },
        { k: 'SOTA (2024–2026+)', c: ERA_COLORS['sota'] }
      ].forEach(function (item) {
        var row = document.createElement('div');
        row.className = 'jcg-legend-item';
        row.innerHTML = '<span class="jcg-legend-swatch" style="background:' + item.c + '"></span>' + item.k;
        legendEl.appendChild(row);
      });
    } else if (currentColorCue === 'tier') {
      legendTitleEl.textContent = 'Color Cue: Corpus Scale Tier';
      [
        { k: '500 Key Papers', c: TIER_COLORS[500] },
        { k: '1000 Key Papers', c: TIER_COLORS[1000] },
        { k: '2000 Key Papers', c: TIER_COLORS[2000] }
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
        { k: 'Cross-Species / General', c: ORGANISM_COLORS['general'] }
      ].forEach(function (item) {
        var row = document.createElement('div');
        row.className = 'jcg-legend-item';
        row.innerHTML = '<span class="jcg-legend-swatch" style="background:' + item.c + '"></span>' + item.k;
        legendEl.appendChild(row);
      });
    } else if (currentColorCue === 'citation_role') {
      legendTitleEl.textContent = 'Color Cue: Citation Role';
      [
        { k: 'Core Hub (Foundational)', c: ROLE_COLORS['core_hub'] },
        { k: 'High-Impact Authority', c: ROLE_COLORS['authority'] },
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
  fetch(DATA_URL).then(function (r) { return r.json(); }).then(function (data) {
    idMap = {};
    doiMap = {};

    allPapers = data.map(function (d) {
      var cat = d.dimension || 'circuit-structure';
      var hub = CATEGORY_HUBS[cat] || { x: 0, y: 0 };
      var jitter = (Math.random() - 0.5) * 140;
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
        summary: d.summary || '',
        citation: d.citation || '',
        cites: d.cites || [],
        pdf_url: d.pdf_url || null,
        is_oa: d.is_oa || false,
        ocar: d.ocar || null,
        summaries: d.summaries || null,
        discussion_prompts: d.discussion_prompts || [],
        x: hub.x + jitter,
        y: hub.y + jitter,
        targetX: hub.x,
        targetY: hub.y,
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

    applyFilters();
    fitView();
    startPhysics();

    if (params.has('paper')) {
      var targetId = params.get('paper');
      var matched = idMap[targetId] || doiMap[targetId.toLowerCase().trim()];
      if (matched) {
        if (matched.tier > currentTier) {
          currentTier = matched.tier;
          tierButtons.forEach(function (b) { b.classList.toggle('active', b.dataset.tier === String(currentTier)); });
          applyFilters();
        }
        selectAndCenterPaper(matched);
      }
    }
  });

  function resizeCanvas() {
    var rect = canvas.getBoundingClientRect();
    canvas.width = rect.width * (window.devicePixelRatio || 1);
    canvas.height = rect.height * (window.devicePixelRatio || 1);
    ctx.scale(window.devicePixelRatio || 1, window.devicePixelRatio || 1);
  }
  window.addEventListener('resize', resizeCanvas);

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
        if (p.tier > currentTier) return false;
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
            return lo.indexOf(selectedOrg) !== -1;
          });
          if (!orgMatch) return false;
        }
        if (p.total_degree < minDeg) return false;
        if (query) {
          var matchT = p.title.toLowerCase().indexOf(query) !== -1;
          var matchA = p.authors.toLowerCase().indexOf(query) !== -1;
          var matchJ = p.journal.toLowerCase().indexOf(query) !== -1;
          var matchO = p.ocar && (
            (p.ocar.opportunity && p.ocar.opportunity.toLowerCase().indexOf(query) !== -1) ||
            (p.ocar.challenge && p.ocar.challenge.toLowerCase().indexOf(query) !== -1) ||
            (p.ocar.action && p.ocar.action.toLowerCase().indexOf(query) !== -1) ||
            (p.ocar.resolution && p.ocar.resolution.toLowerCase().indexOf(query) !== -1)
          );
          if (!matchT && !matchA && !matchJ && !matchO) return false;
        }
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

    countEl.textContent = visibleNodes.length + ' papers (' + visibleEdges.length + ' citation links)';
    promptCountSpan.textContent = visibleNodes.length;
    alpha = Math.max(alpha, 0.4);

    // Recalculate target coordinates based on layout mode
    if (currentLayout === 'timeline') {
      var minYear = 1986, maxYear = 2026;
      var spanW = 900;
      visibleNodes.forEach(function (n) {
        var normX = (n.year - minYear) / (maxYear - minYear);
        n.targetX = (normX - 0.5) * spanW;
        var catIdx = CATEGORIES.indexOf(n.dimension);
        n.targetY = ((catIdx - CATEGORIES.length / 2) / CATEGORIES.length) * 520;
      });
    } else if (currentLayout === 'cluster') {
      visibleNodes.forEach(function (n) {
        var hub = CATEGORY_HUBS[n.dimension] || { x: 0, y: 0 };
        n.targetX = hub.x;
        n.targetY = hub.y;
      });
    }
  }

  function fitView(targetNodes) {
    var nodes = targetNodes || visibleNodes;
    if (!nodes.length) return;
    var minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity;
    nodes.forEach(function (n) {
      if (n.x < minX) minX = n.x;
      if (n.x > maxX) maxX = n.x;
      if (n.y < minY) minY = n.y;
      if (n.y > maxY) maxY = n.y;
    });
    var w = Math.max(maxX - minX + 160, 280);
    var h = Math.max(maxY - minY + 160, 280);
    var cw = canvas.width / (window.devicePixelRatio || 1);
    var ch = canvas.height / (window.devicePixelRatio || 1);
    view.scale = Math.min(cw / w, ch / h, 2.2) * 0.85;
    view.tx = cw / 2 - ((minX + maxX) / 2) * view.scale;
    view.ty = ch / 2 - ((minY + maxY) / 2) * view.scale;
  }

  function selectAndCenterPaper(p) {
    selectedNode = p;
    openPaperDrawer(p);
    var cw = canvas.width / (window.devicePixelRatio || 1);
    var ch = canvas.height / (window.devicePixelRatio || 1);
    view.scale = Math.max(view.scale, 1.2);
    // Shift slightly left to accommodate drawer on the right
    view.tx = (cw * 0.38) - p.x * view.scale;
    view.ty = (ch * 0.5) - p.y * view.scale;
    alpha = Math.max(alpha, 0.3);
  }

  function enterSubgraphFocus(node) {
    focusedSubgraphNode = node;
    focusPaperTitle.textContent = node.title.length > 50 ? node.title.slice(0, 48) + '…' : node.title;
    focusBanner.classList.remove('hidden');
    applyFilters();
    fitView();
    alpha = 0.8;
  }

  function exitSubgraphFocus() {
    focusedSubgraphNode = null;
    focusBanner.classList.add('hidden');
    applyFilters();
    fitView();
    alpha = 0.8;
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
      // Anchored Layouts (Category Hubs or Timeline)
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
    var cw = canvas.width / (window.devicePixelRatio || 1);
    var ch = canvas.height / (window.devicePixelRatio || 1);
    ctx.clearRect(0, 0, cw, ch);

    ctx.save();
    ctx.translate(view.tx, view.ty);
    ctx.scale(view.scale, view.scale);

    // Draw Category Hub Background Rings in Cluster Mode
    if (currentLayout === 'cluster' && view.scale > 0.35) {
      CATEGORIES.forEach(function (cat) {
        var hub = CATEGORY_HUBS[cat];
        ctx.beginPath();
        ctx.arc(hub.x, hub.y, 85, 0, Math.PI * 2);
        ctx.fillStyle = CATEGORY_COLORS[cat] + '08';
        ctx.fill();
        ctx.strokeStyle = CATEGORY_COLORS[cat] + '22';
        ctx.lineWidth = 1 / view.scale;
        ctx.stroke();

        ctx.fillStyle = CATEGORY_COLORS[cat] + '90';
        ctx.font = 'bold 11px Inter, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(cat.replace(/-/g, ' ').toUpperCase(), hub.x, hub.y - 95);
      });
    }

    // Draw Timeline Year Guides in Timeline Mode
    if (currentLayout === 'timeline') {
      [1990, 2000, 2010, 2020, 2025].forEach(function (yr) {
        var normX = (yr - 1986) / (2026 - 1986);
        var gx = (normX - 0.5) * 900;
        ctx.beginPath();
        ctx.moveTo(gx, -320);
        ctx.lineTo(gx, 320);
        ctx.strokeStyle = '#e2e8f0';
        ctx.lineWidth = 1 / view.scale;
        ctx.stroke();

        ctx.fillStyle = '#94a3b8';
        ctx.font = 'bold 12px Inter, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(yr.toString(), gx, -330);
      });
    }

    var activeNode = hoveredNode || selectedNode;
    var drawEdges = showEdgesCheck.checked;
    var drawArrows = showArrowsCheck.checked;
    var drawFlow = showFlowCheck.checked;
    flowOffset = (flowOffset + 0.015) % 1.0;

    // Direct Inbound / Outbound Sets for activeNode
    var inSet = new Set(activeNode && activeNode.citedByNodes ? activeNode.citedByNodes : []);
    var outSet = new Set(activeNode && activeNode.citesNodes ? activeNode.citesNodes : []);

    // Draw Citation Edges
    if (drawEdges && visibleEdges.length) {
      for (var e = 0; e < visibleEdges.length; e++) {
        var edge = visibleEdges[e];
        var s = edge.source;
        var t = edge.target;

        var isSpotlightLineage = hoveredLineageNode && ((s === activeNode && t === hoveredLineageNode) || (t === activeNode && s === hoveredLineageNode));
        var isOutbound = (s === activeNode && outSet.has(t));
        var isInbound = (t === activeNode && inSet.has(s));
        var isConnected = isOutbound || isInbound;

        if (activeNode) {
          if (highlightNeighborhoodMode === 'inbound' && !isInbound) continue;
          if (highlightNeighborhoodMode === 'outbound' && !isOutbound) continue;
          if (highlightNeighborhoodMode === 'all' && !isConnected) {
            ctx.beginPath();
            ctx.moveTo(s.x, s.y);
            ctx.lineTo(t.x, t.y);
            ctx.strokeStyle = '#94a3b80e';
            ctx.lineWidth = 0.5 / view.scale;
            ctx.stroke();
            continue;
          }
        }

        ctx.beginPath();
        ctx.moveTo(s.x, s.y);
        ctx.lineTo(t.x, t.y);

        if (isSpotlightLineage) {
          ctx.strokeStyle = '#f59e0b';
          ctx.lineWidth = 4.0 / view.scale;
        } else if (isOutbound) {
          ctx.strokeStyle = '#6366f1';
          ctx.lineWidth = 2.8 / view.scale;
        } else if (isInbound) {
          ctx.strokeStyle = '#10b981';
          ctx.lineWidth = 2.8 / view.scale;
        } else {
          ctx.strokeStyle = '#94a3b833';
          ctx.lineWidth = 0.85 / view.scale;
        }
        ctx.stroke();

        // Directional Arrowheads pointing from citing source -> cited target
        if (drawArrows || isConnected || isSpotlightLineage) {
          var dx = t.x - s.x;
          var dy = t.y - s.y;
          var angle = Math.atan2(dy, dx);
          var headlen = (isConnected || isSpotlightLineage ? 7.5 : 4.5) / view.scale;
          var ax = t.x - Math.cos(angle) * (t.radius + 3);
          var ay = t.y - Math.sin(angle) * (t.radius + 3);

          ctx.beginPath();
          ctx.moveTo(ax, ay);
          ctx.lineTo(ax - headlen * Math.cos(angle - Math.PI / 6), ay - headlen * Math.sin(angle - Math.PI / 6));
          ctx.lineTo(ax - headlen * Math.cos(angle + Math.PI / 6), ay - headlen * Math.sin(angle + Math.PI / 6));
          ctx.closePath();
          ctx.fillStyle = isSpotlightLineage ? '#f59e0b' : (isOutbound ? '#6366f1' : (isInbound ? '#10b981' : '#94a3b866'));
          ctx.fill();
        }

        // Live Citation Flow Particle Pulse
        if ((drawFlow || isConnected || isSpotlightLineage) && view.scale > 0.35) {
          var pOffset = (flowOffset + (e * 0.13)) % 1.0;
          var px = s.x + (t.x - s.x) * pOffset;
          var py = s.y + (t.y - s.y) * pOffset;
          ctx.beginPath();
          ctx.arc(px, py, (isConnected || isSpotlightLineage ? 3.0 : 1.5) / view.scale, 0, Math.PI * 2);
          ctx.fillStyle = isSpotlightLineage ? '#fef08a' : (isOutbound ? '#a5b4fc' : (isInbound ? '#6ee7b7' : '#cbd5e1'));
          ctx.fill();
        }
      }
    }

    // Draw Nodes
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
        ctx.arc(n.x, n.y, n.radius * 1.35 + 3.5 / view.scale, 0, Math.PI * 2);
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 2.0 / view.scale;
        ctx.stroke();
      } else if (isSpotlightNode) {
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 3.5 / view.scale;
        ctx.stroke();
      } else if (isInNeighbor) {
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 2.8 / view.scale;
        ctx.stroke();
      } else if (isOutNeighbor) {
        ctx.strokeStyle = '#6366f1';
        ctx.lineWidth = 2.8 / view.scale;
        ctx.stroke();
      } else if (n.tier === 500) {
        ctx.strokeStyle = '#ffffff88';
        ctx.lineWidth = 1.5 / view.scale;
        ctx.stroke();
      }

      // Title & Directional Badges
      if (isSelf || isSpotlightNode || isInNeighbor || isOutNeighbor || (view.scale > 0.8 && n.total_degree > 30)) {
        ctx.font = (isSelf || isSpotlightNode ? 'bold 11px' : '10px') + ' Inter, sans-serif';
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
        ctx.fillStyle = badgeColor;
        ctx.fillText(labelText, n.x + n.radius + 5, n.y + 3);
      }
    }

    ctx.restore();
  }

  function startPhysics() {
    function loop() {
      tickPhysics();
      render();
      animFrame = requestAnimationFrame(loop);
    }
    loop();
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

  // Canvas Mouse Interactions
  canvas.addEventListener('mousemove', function (e) {
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
      tooltip.style.left = (e.clientX - rect.left) + 'px';
      tooltip.style.top = (e.clientY - rect.top) + 'px';
      
      var ocarSnippet = node.ocar && node.ocar.opportunity ? '<div class="ocar-preview"><strong>Opportunity:</strong> ' + node.ocar.opportunity.slice(0, 110) + '…</div>' : '';

      tooltip.innerHTML = '<strong>' + node.title + '</strong>' +
        '<div class="meta">' + node.authors + ' (' + node.year + ') &bull; <em>' + node.journal + '</em></div>' +
        '<div><strong>Tier ' + node.tier + '</strong> &bull; ' + node.dimension + ' &bull; In:' + node.in_degree + ' Out:' + node.out_degree + '</div>' +
        ocarSnippet;
    } else {
      canvas.style.cursor = 'grab';
      tooltip.classList.add('hidden');
    }
  });

  canvas.addEventListener('mousedown', function (e) {
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
    if (draggingNode && !dragMoved) {
      selectedNode = draggingNode;
      openPaperDrawer(draggingNode);
    }
    draggingNode = null;
    isPanning = false;
    canvas.classList.remove('dragging');
  });

  canvas.addEventListener('wheel', function (e) {
    e.preventDefault();
    var rect = canvas.getBoundingClientRect();
    var mx = e.clientX - rect.left;
    var my = e.clientY - rect.top;
    var zoomFactor = e.deltaY < 0 ? 1.15 : 0.85;
    var newScale = Math.max(0.15, Math.min(4.5, view.scale * zoomFactor));

    view.tx = mx - (mx - view.tx) * (newScale / view.scale);
    view.ty = my - (my - view.ty) * (newScale / view.scale);
    view.scale = newScale;
  }, { passive: false });

  // Mobile Touch Gestures & Pinch-to-Zoom
  var initialTouchDist = null;
  var touchMoved = false;

  function getTouchDistance(t1, t2) {
    return Math.hypot(t1.clientX - t2.clientX, t1.clientY - t2.clientY);
  }

  canvas.addEventListener('touchstart', function (e) {
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
    if (draggingNode && !touchMoved) {
      selectedNode = draggingNode;
      openPaperDrawer(draggingNode);
    }
    if (e.touches.length === 0) {
      draggingNode = null;
      isPanning = false;
      initialTouchDist = null;
    }
  });

  // Floating HUD Handlers
  function zoomBy(factor) {
    var cw = canvas.width / (window.devicePixelRatio || 1);
    var ch = canvas.height / (window.devicePixelRatio || 1);
    var mx = cw / 2;
    var my = ch / 2;
    var newScale = Math.max(0.15, Math.min(4.5, view.scale * factor));
    view.tx = mx - (mx - view.tx) * (newScale / view.scale);
    view.ty = my - (my - view.ty) * (newScale / view.scale);
    view.scale = newScale;
  }

  hudZoomInBtn.addEventListener('click', function () { zoomBy(1.25); });
  hudZoomOutBtn.addEventListener('click', function () { zoomBy(0.8); });
  hudFitBtn.addEventListener('click', function () { fitView(); });
  sidebarFitBtn.addEventListener('click', function () { fitView(); });
  
  function reheatPhysics() {
    alpha = 1.0;
  }
  hudReheatBtn.addEventListener('click', reheatPhysics);
  sidebarReheatBtn.addEventListener('click', reheatPhysics);

  // Rich Slide-Out Drawer with Deep OCAR Integration
  function openPaperDrawer(p) {
    panel.classList.remove('hidden');
    var tierLabel = p.tier === 500 ? '500 Core Flagship' : (p.tier === 1000 ? '1000 Landmark' : '2000 Comprehensive');
    var pdfButton = p.pdf_url ? '<a href="' + p.pdf_url + '" target="_blank" rel="noopener" class="jcg-drawer-btn jcg-drawer-btn-pdf">📄 Open Access PDF &rarr;</a>' : '';
    var fullCardUrl = JC_BASE_URL + '#paper-' + encodeURIComponent(p.id);

    // OCAR Section
    var ocarHtml = '';
    if (p.ocar) {
      ocarHtml = '<div class="jcg-ocar-container">' +
        '<div class="jcg-ocar-step"><span class="jcg-ocar-label jcg-ocar-opportunity">Opportunity</span><p>' + (p.ocar.opportunity || '') + '</p></div>' +
        '<div class="jcg-ocar-step"><span class="jcg-ocar-label jcg-ocar-challenge">Challenge</span><p>' + (p.ocar.challenge || '') + '</p></div>' +
        '<div class="jcg-ocar-step"><span class="jcg-ocar-label jcg-ocar-action">Action</span><p>' + (p.ocar.action || '') + '</p></div>' +
        '<div class="jcg-ocar-step"><span class="jcg-ocar-label jcg-ocar-resolution">Resolution</span><p>' + (p.ocar.resolution || '') + '</p></div>' +
        '<div class="jcg-ocar-step"><span class="jcg-ocar-label jcg-ocar-future">Future Work</span><p>' + (p.ocar.future_work || '') + '</p></div>' +
      '</div>';
    }

    // 3-Tier Summaries
    var summariesHtml = '';
    if (p.summaries) {
      summariesHtml = '<div class="jcg-drawer-summaries">' +
        '<div class="jcg-summary-tabs">' +
          '<button type="button" class="jcg-summary-tab active" data-level="intermediate">Intermediate</button>' +
          '<button type="button" class="jcg-summary-tab" data-level="beginner">Beginner</button>' +
          '<button type="button" class="jcg-summary-tab" data-level="advanced">Advanced</button>' +
        '</div>' +
        '<div class="jcg-summary-content" id="jcg-active-summary">' + (p.summaries.intermediate || p.summary || '') + '</div>' +
      '</div>';
    } else if (p.summary) {
      summariesHtml = '<div class="jcg-ocar-step" style="margin: 0.75rem 0;"><strong>Summary:</strong> ' + p.summary + '</div>';
    }

    // Discussion Prompts
    var promptsHtml = '';
    if (p.discussion_prompts && p.discussion_prompts.length) {
      promptsHtml = '<details class="jcg-prompts-section">' +
        '<summary>💡 Seminar Discussion Prompts (' + p.discussion_prompts.length + ')</summary>' +
        '<ul class="jcg-prompts-list">' +
          p.discussion_prompts.map(function (pr) { return '<li>' + pr + '</li>'; }).join('') +
        '</ul>' +
      '</details>';
    }

    // Interactive Citation Lineage Chips
    var citingChipsHtml = '';
    if (p.citedByNodes && p.citedByNodes.length) {
      citingChipsHtml = '<div class="jcg-lineage-section">' +
        '<h4>Cited By (' + p.citedByNodes.length + ' Papers in Corpus) &darr;</h4>' +
        '<div class="jcg-lineage-chips">' +
          p.citedByNodes.slice(0, 10).map(function (cp) {
            return '<button type="button" class="jcg-lineage-chip citing-chip" data-paper-id="' + cp.id + '">' +
              '<strong>' + (cp.authors.split(';')[0].split(',')[0] || 'Author') + ' (' + cp.year + ')</strong>: ' +
              (cp.title.length > 38 ? cp.title.slice(0, 36) + '…' : cp.title) +
            '</button>';
          }).join('') +
          (p.citedByNodes.length > 10 ? '<span style="font-size:0.72rem; color:#64748b; align-self:center;">+' + (p.citedByNodes.length - 10) + ' more</span>' : '') +
        '</div>' +
      '</div>';
    }

    var citedChipsHtml = '';
    if (p.citesNodes && p.citesNodes.length) {
      citedChipsHtml = '<div class="jcg-lineage-section">' +
        '<h4>Cites (' + p.citesNodes.length + ' Foundational References) &uarr;</h4>' +
        '<div class="jcg-lineage-chips">' +
          p.citesNodes.slice(0, 10).map(function (cp) {
            return '<button type="button" class="jcg-lineage-chip cited-chip" data-paper-id="' + cp.id + '">' +
              '<strong>' + (cp.authors.split(';')[0].split(',')[0] || 'Author') + ' (' + cp.year + ')</strong>: ' +
              (cp.title.length > 38 ? cp.title.slice(0, 36) + '…' : cp.title) +
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
      '<span class="jcg-neighborhood-title">🌐 Citation Neighborhood (' + totalNeighbors + ' Direct Links)</span>' +
      '<div class="jcg-neighborhood-pills">' +
        '<button type="button" class="jcg-nill-btn ' + (highlightNeighborhoodMode === 'all' ? 'active' : '') + '" data-dir="all">All (In+Out: ' + totalNeighbors + ')</button>' +
        '<button type="button" class="jcg-nill-btn ' + (highlightNeighborhoodMode === 'inbound' ? 'active' : '') + '" data-dir="inbound">📥 Cited By (' + inCount + ')</button>' +
        '<button type="button" class="jcg-nill-btn ' + (highlightNeighborhoodMode === 'outbound' ? 'active' : '') + '" data-dir="outbound">📤 Cites (' + outCount + ')</button>' +
      '</div>' +
    '</div>';

    // Ecosystem & Methodological Pipeline Breakdown
    var orgStr = (p.organism && p.organism.length) ? p.organism.join(', ') : 'Neural System';
    var datasetGuess = 'Open Connectome Volume';
    var oLower = orgStr.toLowerCase();
    if (oLower.indexOf('fly') !== -1 || oLower.indexOf('drosophila') !== -1) {
      datasetGuess = 'FlyWire / FAFB / hemibrain';
    } else if (oLower.indexOf('mouse') !== -1 || oLower.indexOf('rodent') !== -1) {
      datasetGuess = 'MICrONS / Kasthuri / MCP';
    } else if (oLower.indexOf('elegans') !== -1 || oLower.indexOf('worm') !== -1) {
      datasetGuess = 'C. elegans N2U / Cook et al.';
    } else if (oLower.indexOf('human') !== -1) {
      datasetGuess = 'H01 Human Cortex / Shapson-Coe';
    }

    var toolsGuess = 'Neuroglancer, CAVE / PyChunkedGraph, CloudVolume, natverse, Python';
    if (p.dimension === 'methods-imaging') {
      toolsGuess = 'Serial-section EM, FIB-SEM, Ilastik, VAST, AlignTK';
    } else if (p.dimension === 'segmentation-ai') {
      toolsGuess = 'Flood-Filling Networks (FFN), 3D U-Net, PyTorch, CAVE';
    }

    var actionSnippet = (p.ocar && p.ocar.action) ? p.ocar.action : 'Dense volume EM imaging and circuit reconstruction.';
    var resSnippet = (p.ocar && p.ocar.resolution) ? p.ocar.resolution : 'Identification of synaptic connectivity motifs and cell-type wiring.';

    var ecosystemAndPipelineHtml = '<div class="jcg-ecosystem-box">' +
      '<h4>🌐 Research Ecosystem Preview</h4>' +
      '<div class="jcg-ecosystem-grid">' +
        '<div class="jcg-eco-item"><strong>Model Organism</strong><span>' + orgStr + '</span></div>' +
        '<div class="jcg-eco-item"><strong>Dataset / Volume</strong><span>' + datasetGuess + '</span></div>' +
        '<div class="jcg-eco-item" style="grid-column: span 2;"><strong>Software & Tool Stack</strong><span>' + toolsGuess + '</span></div>' +
      '</div>' +
      '<details class="jcg-analysis-pipeline" open>' +
        '<summary style="font-weight:700; font-size:0.78rem; color:#1e293b; cursor:pointer; margin-bottom:0.4rem;">🔬 Analysis Protocol Breakdown (How Conducted)</summary>' +
        '<div class="jcg-pipe-stage">' +
          '<span class="jcg-pipe-badge jcg-badge-prep">1. Prep & Imaging</span>' +
          '<div class="jcg-pipe-desc"><strong>High-Pressure Freezing & Staining</strong><p>Heavy metal infiltration (OsO₄, uranyl acetate, lead aspartate) for nanometer ultrastructure contrast.</p></div>' +
        '</div>' +
        '<div class="jcg-pipe-stage">' +
          '<span class="jcg-pipe-badge jcg-badge-recon">2. Alignment</span>' +
          '<div class="jcg-pipe-desc"><strong>Non-Rigid 3D Registration</strong><p>Elastic cross-section stitching, distortion compensation, and chunked cloud pyramid storage.</p></div>' +
        '</div>' +
        '<div class="jcg-pipe-stage">' +
          '<span class="jcg-pipe-badge jcg-badge-ai">3. AI Segmentation</span>' +
          '<div class="jcg-pipe-desc"><strong>Deep Learning Affinity & Synapse Prediction</strong><p>' + actionSnippet + '</p></div>' +
        '</div>' +
        '<div class="jcg-pipe-stage">' +
          '<span class="jcg-pipe-badge jcg-badge-qc">4. Proofreading</span>' +
          '<div class="jcg-pipe-desc"><strong>Collaborative Verification & Error Correction</strong><p>Split/merge validation, false positive synapse pruning, and dendritic skeleton completeness audit.</p></div>' +
        '</div>' +
        '<div class="jcg-pipe-stage">' +
          '<span class="jcg-pipe-badge jcg-badge-stats">5. Circuit Analysis</span>' +
          '<div class="jcg-pipe-desc"><strong>Graph Topology & Biological Resolution</strong><p>' + resSnippet + '</p></div>' +
        '</div>' +
      '</details>' +
    '</div>';

    var html = '<h3>' + p.title + '</h3>' +
      '<div class="jcg-panel-authors">' + p.authors + ' &bull; <em>' + p.journal + '</em> (' + p.year + ')</div>' +
      '<div class="jcg-panel-meta-tags">' +
        '<span class="jcg-panel-tag tier-tag">' + tierLabel + '</span>' +
        '<span class="jcg-panel-tag dim-tag">' + p.dimension.replace(/-/g, ' ') + '</span>' +
        '<span class="jcg-panel-tag">' + p.era + '</span>' +
        '<span class="jcg-panel-tag role-tag">' + p.citation_role.replace(/_/g, ' ') + '</span>' +
        '<span class="jcg-panel-tag">In: ' + p.in_degree + ' | Out: ' + p.out_degree + '</span>' +
      '</div>' +
      '<div class="jcg-drawer-actions">' +
        '<button type="button" class="jcg-drawer-btn" id="jcg-btn-ai-prompt" style="background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); color: #fff;">🤖 AI Paper Prompt</button>' +
        '<button type="button" class="jcg-drawer-btn jcg-drawer-btn-focus" id="jcg-btn-focus-subgraph">🎯 Focus Citation Subgraph</button>' +
        '<a href="' + fullCardUrl + '" class="jcg-drawer-btn jcg-drawer-btn-jc">📑 Full Card in Journal Club &rarr;</a>' +
        (p.doi ? '<a href="https://doi.org/' + p.doi + '" target="_blank" rel="noopener" class="jcg-drawer-btn jcg-drawer-btn-doi">🌐 Publisher DOI &rarr;</a>' : '') +
        pdfButton +
      '</div>' +
      neighborhoodToolbarHtml +
      ecosystemAndPipelineHtml +
      ocarHtml +
      summariesHtml +
      promptsHtml +
      citingChipsHtml +
      citedChipsHtml +
      '<div class="jcg-ocar-step" style="margin-top:1rem; font-size:0.75rem; color:#64748b;">' +
        '<strong>Full Citation:</strong> ' + p.citation +
      '</div>';

    panelBody.innerHTML = html;

    // Attach neighborhood mode toggles
    var nillButtons = Array.from(panelBody.querySelectorAll('.jcg-nill-btn'));
    nillButtons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        nillButtons.forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        highlightNeighborhoodMode = btn.dataset.dir;
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

    // Attach summary tab switcher
    var summaryTabs = Array.from(panelBody.querySelectorAll('.jcg-summary-tab'));
    var summaryBox = document.getElementById('jcg-active-summary');
    summaryTabs.forEach(function (tab) {
      tab.addEventListener('click', function () {
        summaryTabs.forEach(function (t) { t.classList.remove('active'); });
        tab.classList.add('active');
        var lvl = tab.dataset.level;
        if (p.summaries && p.summaries[lvl]) {
          summaryBox.textContent = p.summaries[lvl];
        }
      });
    });

    // Attach lineage jump chips and hover spotlights
    var lineageChips = Array.from(panelBody.querySelectorAll('.jcg-lineage-chip'));
    lineageChips.forEach(function (chip) {
      chip.addEventListener('mouseenter', function () {
        var pid = chip.dataset.paperId;
        hoveredLineageNode = idMap[pid] || null;
      });
      chip.addEventListener('mouseleave', function () {
        hoveredLineageNode = null;
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
          selectAndCenterPaper(targetPaper);
        }
      });
    });
  }

  panelClose.addEventListener('click', function () {
    panel.classList.add('hidden');
    selectedNode = null;
  });

  // AI Synthesis Prompt Generation
  var currentPromptMode = 'synthesis';
  var singlePaperTarget = null;
  var modalTitleEl = document.getElementById('jcg-prompt-modal-title');
  var modalDescEl = document.getElementById('jcg-prompt-modal-desc');
  var modeButtons = Array.from(document.querySelectorAll('.jcg-pmode-btn'));

  function generateSynthesisPrompt() {
    if (singlePaperTarget) {
      modalTitleEl.textContent = '🤖 AI Analysis Deep-Dive & Methodological Protocol';
      modalDescEl.innerHTML = 'Analysis protocol & critique for: <strong>' + singlePaperTarget.title + '</strong> (' + singlePaperTarget.year + ')';
      var p = singlePaperTarget;
      var prompt = 'You are a principal investigator and expert computational neuroscientist in nanoscale connectomics.\n' +
        'Perform a comprehensive methodological analysis and technical audit for the following milestone study:\n\n' +
        '### Paper Metadata & Research Ecosystem:\n' +
        '- **Title**: "' + p.title + '"\n' +
        '- **Authors**: ' + p.authors + '\n' +
        '- **Journal/Year**: ' + p.journal + ' (' + p.year + ')\n' +
        '- **Research Subfield**: ' + p.dimension + '\n' +
        '- **Target Organism**: ' + ((p.organism && p.organism.join(', ')) || 'Neural tissue') + '\n' +
        '- **Corpus Tier**: ' + (p.tier === 500 ? 'Core Flagship' : (p.tier === 1000 ? 'Landmark' : 'Comprehensive')) + '\n\n' +
        '### 5-Part OCAR Narrative Framework:\n' +
        '- **Opportunity (Biological Premise)**: ' + ((p.ocar && p.ocar.opportunity) || p.summary) + '\n' +
        '- **Challenge (Technical Bottleneck)**: ' + ((p.ocar && p.ocar.challenge) || 'Dense volumetric reconstruction and synaptic proofreading complexity.') + '\n' +
        '- **Action (Methodology & Pipeline)**: ' + ((p.ocar && p.ocar.action) || 'Volume electron microscopy, automated segmentation, and circuit analysis.') + '\n' +
        '- **Resolution (Empirical Discovery)**: ' + ((p.ocar && p.ocar.resolution) || 'Reconstruction and cell-type connectivity mapping.') + '\n' +
        '- **Future Work (Open Horizons)**: ' + ((p.ocar && p.ocar.future_work) || 'Comparative cross-species wiring and functional validation.') + '\n\n' +
        '### In-Depth Methodological & Ecosystem Analysis Required:\n' +
        '1. **Experimental & Imaging Protocol**: Explain how tissue was preserved, stained, sectioned, and imaged (specifying electron microscopy modality, voxel resolution in nm xyz, and acquisition throughput).\n' +
        '2. **Volume Reconstruction & AI Segmentation**: Detail the algorithmic pipeline used for 3D alignment, deep learning affinity predictions (e.g. FFN / 3D U-Net), automated synapse detection, and cleft polarity assignment.\n' +
        '3. **Proofreading Protocol & Error Budget**: What proofreading platform (e.g. CAVE, PyChunkedGraph, Neuroglancer, VAST) was used? How were false splits, false merges, and volume completeness quantified?\n' +
        '4. **Circuit Graph Analysis & Statistical Models**: Detail the network metrics (e.g. graph adjacency matrices, motif censuses, path lengths, recurrent vs feedforward loops) used to establish biological claims.\n' +
        '5. **Reproducible Python Analysis Recipe**: Provide clean Python pseudo-code using standard connectomics libraries (`navis`, `caveclient`, `networkx`, `scipy`) to reproduce the primary circuit connectivity analysis.\n\n' +
        'Structure your response with clear markdown headings, concise bullet points, and explicit citations to this publication.';

      promptTextarea.value = prompt;
      return;
    }

    var totalCount = visibleNodes.length;
    var maxIncluded = Math.min(totalCount, 40);
    modalTitleEl.textContent = '🤖 AI Research Synthesis Prompt';
    modalDescEl.innerHTML = 'Copy this grounded prompt into <strong>ChatGPT</strong>, <strong>Claude</strong>, or <strong>Gemini</strong> across the <strong>' + totalCount + '</strong> currently filtered papers.';
    modalPaperCount.textContent = totalCount;

    var cat = dimensionEl.value === 'all' ? 'All Connectomics Subfields' : dimensionEl.options[dimensionEl.selectedIndex].text;
    var org = organismEl.value === 'all' ? 'All Model Organisms' : organismEl.options[organismEl.selectedIndex].text;

    var paperList = visibleNodes.slice(0, maxIncluded).map(function (p, idx) {
      var ocarAction = (p.ocar && p.ocar.action) ? '\n   Methodological Action: ' + p.ocar.action : '';
      var ocarRes = (p.ocar && p.ocar.resolution) ? '\n   Empirical Resolution: ' + p.ocar.resolution : '';
      return (idx + 1) + '. "' + p.title + '" (' + p.authors + ', ' + p.year + ', ' + p.journal + ')\n   Summary: ' + (p.summary || 'Milestone connectomics contribution') + ocarAction + ocarRes + '\n   DOI: https://doi.org/' + p.doi;
    }).join('\n\n');

    var scopeDesc = totalCount <= 40
      ? 'based on the following ' + totalCount + ' curated milestone publications' 
      : 'based on the top ' + maxIncluded + ' representative milestone publications (selected from ' + totalCount + ' matching publications in the active filter)';

    var prompt = '';
    if (currentPromptMode === 'methods') {
      prompt = 'You are a technical specialist in connectomics imaging, computer vision, and neural data pipelines.\n' +
        'Perform a comparative methodological audit ' + scopeDesc + ' in Domain = [' + cat + '] and Organism = [' + org + '].\n\n' +
        '### Ground-Truth Papers (N = ' + maxIncluded + (totalCount > 40 ? ' of ' + totalCount : '') + '):\n' + paperList + '\n\n' +
        '### Required Analysis Tasks:\n' +
        '1. **Technological Pipeline Evolution**: Map how imaging modalities, automated segmentation algorithms, and proofreading workflows have transformed across these works.\n' +
        '2. **Bottlenecks & Limitations**: What are the common failure modes, compute bottlenecks, and manual annotation burdens reported?\n' +
        '3. **Benchmarking & Validation**: How do these studies quantify accuracy (e.g. Rand error, synapse precision/recall, volumetric completeness)?\n' +
        '4. **Next-Generation Tools**: What pipeline innovations are urgently needed to scale to whole-brain mammalian connectomes?\n\n' +
        'Ground your findings strictly in the publications listed above with citations.';
    } else if (currentPromptMode === 'problems') {
      prompt = 'You are a senior neuroscience researcher and grant reviewer.\n' +
        'Identify open research problems and high-impact project proposals ' + scopeDesc + ' in Domain = [' + cat + '] and Organism = [' + org + '].\n\n' +
        '### Ground-Truth Papers (N = ' + maxIncluded + (totalCount > 40 ? ' of ' + totalCount : '') + '):\n' + paperList + '\n\n' +
        '### Required Analysis Tasks:\n' +
        '1. **Persistent Scientific Blindspots**: What fundamental questions about circuit organization remain unanswered despite the progress in these papers?\n' +
        '2. **Top 3 High-Impact Research Proposals**: Outline 3 innovative 3-year research proposals addressing these gaps (specifying hypothesis, required connectomic data, and experimental validation).\n' +
        '3. **Cross-Disciplinary Synergies**: How can integration with transcriptomics, physiology (2P calcium imaging), or NeuroAI unlock deeper insights from these datasets?\n\n' +
        'Ground your synthesis in the cited publications.';
    } else if (currentPromptMode === 'seminar') {
      prompt = 'You are a university professor preparing a graduate seminar on connectomics.\n' +
        'Design a comprehensive journal club syllabus and active-learning discussion guide ' + scopeDesc + ' in [' + cat + '].\n\n' +
        '### Core Literature (N = ' + maxIncluded + (totalCount > 40 ? ' of ' + totalCount : '') + '):\n' + paperList + '\n\n' +
        '### Required Seminar Components:\n' +
        '1. **Seminar Overview & Learning Objectives**: 3 clear learning outcomes for students.\n' +
        '2. **Core Debate Topics**: 3 provocative debate motions comparing competing interpretations or methods across these works.\n' +
        '3. **Critical Thinking Exercises**: Methodological critique prompts asking students to identify unaddressed confounding variables.\n' +
        '4. **Key Takeaway Cheat-Sheet**: A 5-point summary of foundational principles established by this literature.\n\n' +
        'Cite the relevant papers explicitly throughout.';
    } else {
      // Default: Comprehensive Literature Synthesis
      prompt = 'You are an expert computational neuroscientist and connectomics researcher.\n' +
        'Analyze and synthesize the state of research ' + scopeDesc + ' ' +
        'focusing on: Domain = [' + cat + '] and Organism = [' + org + '].\n\n' +
        '### Ground-Truth Milestone Publications (N = ' + maxIncluded + (totalCount > 40 ? ' of ' + totalCount : '') + '):\n' +
        paperList + '\n\n' +
        '### Synthesis Tasks Required (grounded in the OCAR research framework):\n' +
        '1. **Current State of the Subfield (Opportunities)**: Provide an executive summary of the biological and computational openings addressed by these landmark studies.\n' +
        '2. **Core Technical Challenges & Bottlenecks**: Detail the major imaging, alignment, automated segmentation, proofreading, and synaptic validation bottlenecks documented across these papers.\n' +
        '3. **Methodological Actions & Breakthroughs**: Detail the core technical breakthroughs accomplished (e.g. multi-beam SEM, deep learning affinities, automated cell-type clustering, connectome graph metrics).\n' +
        '4. **Key Empirical Resolutions & Wiring Discoveries**: What definitive circuit wiring motifs, feedforward/recurrent loops, or cell-type taxonomies did these studies discover?\n' +
        '5. **Open Research Horizons & Future Directions**: Outline the top 3-5 high-priority research questions that the community must address over the next 3-5 years.\n\n' +
        'Ground your analysis strictly in the ' + maxIncluded + ' publications listed above. Structure your response with clear markdown headings, concise bullet points, and explicit citations to these papers.';
    }

    promptTextarea.value = prompt;
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
      applyFilters();
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

  showEdgesCheck.addEventListener('change', render);
  showArrowsCheck.addEventListener('change', render);
  showFlowCheck.addEventListener('change', render);

  colorByEl.addEventListener('change', function () {
    currentColorCue = colorByEl.value;
    updateLegend();
    render();
  });

  eraChecks.forEach(function (c) { c.addEventListener('change', function () { applyFilters(); fitView(); }); });
  dimensionEl.addEventListener('change', function () { applyFilters(); fitView(); });
  organismEl.addEventListener('change', function () { applyFilters(); fitView(); });
  degreeEl.addEventListener('input', function () {
    degreeVal.textContent = degreeEl.value;
    applyFilters();
    fitView();
  });
  searchEl.addEventListener('input', function () { applyFilters(); fitView(); });

  resetBtn.addEventListener('click', function () {
    focusedSubgraphNode = null;
    focusBanner.classList.add('hidden');
    currentTier = 500;
    currentLayout = 'organic';
    currentColorCue = 'dimension';
    colorByEl.value = 'dimension';
    showEdgesCheck.checked = true;
    showArrowsCheck.checked = true;
    showFlowCheck.checked = true;
    tierButtons.forEach(function (b) { b.classList.toggle('active', b.dataset.tier === '500'); });
    layoutButtons.forEach(function (b) { b.classList.toggle('active', b.dataset.mode === 'organic'); });
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
