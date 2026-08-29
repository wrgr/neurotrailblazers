---
layout: default
title: "Citation Graph Explorer"
permalink: /technical-training/journal-club/graph/
track: core-concepts-methods
pathways:
  - technical foundation
  - shared vocabulary
description: "Interactive citation graph explorer across 500, 1,000, and 2,000 curated papers in connectomics: self-organizing organic force clustering, weighted directed citation edges, and AI synthesis prompts."
content_type: core
---

<div class="layout-content layout-page">

<section class="jc-hero" style="text-align: center; margin-bottom: 1.5rem;">
  <h1>Citation Graph Explorer</h1>
  <p style="font-size: 1.1rem; color: #555; max-width: 850px; margin: 0.5rem auto 0;">
    Explore the curated connectomics literature network across <strong>500 Flagships</strong>, <strong>1,000 Landmark Works</strong>, and the <strong>2,000-Paper Comprehensive Graph</strong>. Features self-organizing organic force clustering, weighted directed citation edges, and deep OCAR research cards.
  </p>
</section>

<section class="section section-compact">
  <div class="jcg-layout">
    
    <!-- Controls Sidebar -->
    <div class="jcg-controls">
      
      <!-- Tier Selector -->
      <div class="jcg-control-group">
        <label for="jcg-tier-select">Corpus Scale Tier:</label>
        <div class="jcg-tier-btn-group" id="jcg-tier-buttons">
          <button type="button" class="jcg-tier-btn active" data-tier="500">500 Key Papers</button>
          <button type="button" class="jcg-tier-btn" data-tier="1000">1000 Key Papers</button>
          <button type="button" class="jcg-tier-btn" data-tier="2000">2000 Key Papers</button>
        </div>
      </div>

      <!-- Layout Mode -->
      <div class="jcg-control-group">
        <label>Layout Clustering Mode:</label>
        <div class="jcg-tier-btn-group" id="jcg-layout-buttons">
          <button type="button" class="jcg-layout-btn active" data-mode="organic">Organic Force</button>
          <button type="button" class="jcg-layout-btn" data-mode="cluster">Category Hubs</button>
          <button type="button" class="jcg-layout-btn" data-mode="timeline">Timeline</button>
        </div>
      </div>

      <!-- Edge Controls -->
      <fieldset class="jcg-era-fieldset">
        <legend>Citation Edges &amp; Flow</legend>
        <label><input type="checkbox" id="jcg-show-edges" checked> Draw Citation Edges</label>
        <label><input type="checkbox" id="jcg-show-arrows" checked> Show Directional Arrows (&rarr;)</label>
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
          <option value="pipeline">Pipeline & Software</option>
          <option value="physiology">Physiology</option>
          <option value="behaviour">Behaviour</option>
          <option value="imaging">Imaging & Optics</option>
          <option value="cell-types">Cell Types & Census</option>
          <option value="neuroanatomy">Neuroanatomy</option>
          <option value="synthesis">Synthesis & Reviews</option>
          <option value="dataset">Datasets & Volumes</option>
          <option value="neuroai">NeuroAI & Models</option>
          <option value="health">Health & Disease</option>
          <option value="training-outreach">Training & Outreach</option>
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
          <option value="cross-species">Cross-Species & Comparative</option>
          <option value="theory-model">Theory & Computational Models</option>
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
        <label for="jcg-search">Search (Title, Author, Method):</label>
        <input type="text" id="jcg-search" placeholder="e.g. MICrONS, Kasthuri, U-Net, FlyWire...">
      </div>

      <!-- AI Synthesis Prompt Generator Button -->
      <div class="jcg-control-group" style="margin-top: 0.25rem;">
        <button id="jcg-prompt-btn" type="button" class="jcg-prompt-trigger-btn">
          ✨ Generate AI Synthesis Prompt (<span id="jcg-prompt-count">500</span>)
        </button>
      </div>

      <button id="jcg-reset" type="button">Reset View & Filters</button>

      <p class="jcg-count" id="jcg-count">Showing 500 papers</p>
      <p class="jcg-hint">Drag to pan &bull; Scroll to zoom &bull; Click any node for OCAR card</p>

      <div class="jcg-legend-title" id="jcg-legend-title" style="font-weight:700; font-size:0.78rem; color:#374151; margin-top:0.4rem;">Color Cue Legend:</div>
      <div class="jcg-legend" id="jcg-legend"></div>
    </div>

    <!-- Canvas Container & Interactive Drawer -->
    <div class="jcg-canvas-wrap">
      <canvas id="jcg-canvas"></canvas>
      <div class="jcg-tooltip hidden" id="jcg-tooltip"></div>
      
      <!-- Slide-Out Paper Detail Drawer -->
      <div class="jcg-panel hidden" id="jcg-panel">
        <button class="jcg-panel-close" id="jcg-panel-close" aria-label="Close">&times;</button>
        <div class="jcg-panel-body" id="jcg-panel-body">
          <!-- Dynamically populated -->
        </div>
      </div>

      <!-- AI Synthesis Prompt Modal -->
      <div class="jcg-prompt-modal hidden" id="jcg-prompt-modal">
        <div class="jcg-prompt-modal-content">
          <div class="jcg-prompt-modal-header">
            <h3>🤖 AI Research Synthesis Prompt</h3>
            <button class="jcg-prompt-modal-close" id="jcg-prompt-close" aria-label="Close">&times;</button>
          </div>
          <p class="jcg-prompt-modal-desc">
            Copy and paste this structured prompt into <strong>ChatGPT</strong>, <strong>Claude</strong>, or <strong>Gemini</strong> to generate a comprehensive literature synthesis across the <strong id="jcg-modal-paper-count">0</strong> papers currently filtered in your view.
          </p>
          <div class="jcg-prompt-box">
            <textarea id="jcg-prompt-textarea" readonly></textarea>
          </div>
          <div class="jcg-prompt-modal-footer">
            <button type="button" class="jcg-copy-btn" id="jcg-copy-prompt-btn">
              📋 Copy Prompt to Clipboard
            </button>
            <span class="jcg-copy-status hidden" id="jcg-copy-status">✅ Copied!</span>
          </div>
        </div>
      </div>

    </div>

  </div>
</section>

</div>

<style>
.jcg-layout { display: grid; grid-template-columns: 290px 1fr; gap: 1.25rem; align-items: start; margin-top: 1rem; }
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

#jcg-reset {
  background: #fff; border: 1px solid #d1d5db; border-radius: 6px;
  padding: 0.45rem 0.8rem; cursor: pointer; font-weight: 600; font-size: 0.8rem; color: #4b5563;
}
#jcg-reset:hover { background: #f3f4f6; }
.jcg-count { font-weight: 600; color: #1a56db; margin: 0; font-size: 0.85rem; }
.jcg-hint { color: #6b7280; font-size: 0.75rem; margin: 0; line-height: 1.3; }

.jcg-legend { display: grid; grid-template-columns: 1fr 1fr; gap: 0.3rem; margin-top: 0.2rem; }
.jcg-legend-item { display: flex; align-items: center; gap: 0.35rem; font-size: 0.72rem; color: #4b5563; }
.jcg-legend-swatch { width: 9px; height: 9px; border-radius: 50%; display: inline-block; flex-shrink: 0; }

.jcg-canvas-wrap { position: relative; background: #ffffff; border: 1px solid #e5e7eb; border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.06); overflow: hidden; height: 740px; }
#jcg-canvas { display: block; width: 100%; height: 100%; cursor: grab; }
#jcg-canvas.dragging { cursor: grabbing; }

.jcg-tooltip {
  position: absolute; pointer-events: none; z-index: 10;
  background: rgba(15, 23, 42, 0.95); color: #fff; border-radius: 6px;
  padding: 0.5rem 0.75rem; font-size: 0.78rem; line-height: 1.4;
  max-width: 280px; box-shadow: 0 6px 18px rgba(0,0,0,0.25);
  transform: translate(14px, 14px);
}
.jcg-tooltip.hidden { display: none; }
.jcg-tooltip strong { display: block; font-size: 0.85rem; margin-bottom: 0.2rem; color: #60a5fa; }
.jcg-tooltip .meta { color: #94a3b8; font-size: 0.72rem; margin-bottom: 0.3rem; }

.jcg-panel {
  position: absolute; top: 1rem; right: 1rem; width: min(420px, calc(100% - 2rem));
  background: #ffffff; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  border: 1px solid #e2e8f0; padding: 1.25rem; max-height: calc(100% - 2rem); overflow-y: auto; z-index: 20;
}
.jcg-panel.hidden { display: none; }
.jcg-panel-close {
  position: absolute; top: 0.75rem; right: 0.85rem; background: none; border: none;
  font-size: 1.4rem; line-height: 1; cursor: pointer; color: #94a3b8;
}
.jcg-panel-close:hover { color: #1e293b; }
.jcg-panel-body h3 { margin: 0 1.5rem 0.4rem 0; font-size: 1.05rem; line-height: 1.35; color: #0f172a; }
.jcg-panel-authors { font-size: 0.8rem; color: #64748b; margin-bottom: 0.5rem; }
.jcg-panel-meta-tags { display: flex; flex-wrap: wrap; gap: 0.35rem; margin-bottom: 0.75rem; }
.jcg-panel-tag { background: #f1f5f9; border-radius: 4px; padding: 0.15rem 0.45rem; font-size: 0.72rem; color: #475569; font-weight: 600; }
.jcg-panel-tag.tier-tag { background: #dbeafe; color: #1d4ed8; }

.jcg-ocar-box { background: #f8fafc; border-left: 3px solid #3b82f6; border-radius: 4px; padding: 0.6rem 0.8rem; margin: 0.6rem 0; font-size: 0.82rem; }
.jcg-ocar-box strong { color: #1e3a8a; display: block; margin-bottom: 0.15rem; }
.jcg-ocar-box p { margin: 0 0 0.4rem 0; color: #334155; line-height: 1.4; }
.jcg-ocar-box p:last-child { margin-bottom: 0; }

.jcg-panel-links { display: flex; gap: 0.5rem; margin-top: 1rem; }
.jcg-panel-links a {
  font-size: 0.8rem; font-weight: 600; text-decoration: none; color: #fff;
  background: #1a56db; padding: 0.4rem 0.8rem; border-radius: 6px; display: inline-flex; align-items: center; gap: 0.3rem;
}
.jcg-panel-links a:hover { background: #1e40af; }

/* Prompt Modal */
.jcg-prompt-modal {
  position: absolute; inset: 0; background: rgba(15, 23, 42, 0.75);
  display: flex; align-items: center; justify-content: center; z-index: 30; padding: 1.5rem;
}
.jcg-prompt-modal.hidden { display: none; }
.jcg-prompt-modal-content {
  background: #fff; border-radius: 12px; max-width: 650px; width: 100%;
  max-height: 90%; display: flex; flex-direction: column; padding: 1.5rem;
  box-shadow: 0 20px 40px rgba(0,0,0,0.3); border: 1px solid #cbd5e1;
}
.jcg-prompt-modal-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem; }
.jcg-prompt-modal-header h3 { margin: 0; font-size: 1.15rem; color: #0f172a; }
.jcg-prompt-modal-close { background: none; border: none; font-size: 1.5rem; cursor: pointer; color: #64748b; line-height: 1; }
.jcg-prompt-modal-close:hover { color: #0f172a; }
.jcg-prompt-modal-desc { font-size: 0.82rem; color: #475569; margin: 0 0 0.75rem 0; line-height: 1.4; }
.jcg-prompt-box { flex: 1; display: flex; margin-bottom: 1rem; }
#jcg-prompt-textarea {
  width: 100%; height: 280px; box-sizing: border-box; padding: 0.75rem;
  font-family: monospace; font-size: 0.78rem; border: 1px solid #cbd5e1;
  border-radius: 6px; background: #f8fafc; color: #1e293b; resize: none;
}
.jcg-prompt-modal-footer { display: flex; align-items: center; gap: 0.75rem; }
.jcg-copy-btn {
  background: #1a56db; color: #fff; border: none; border-radius: 6px;
  padding: 0.5rem 1rem; font-size: 0.85rem; font-weight: 600; cursor: pointer;
  display: inline-flex; align-items: center; gap: 0.4rem;
}
.jcg-copy-btn:hover { background: #1e40af; }
.jcg-copy-status { font-size: 0.85rem; font-weight: 600; color: #16a34a; }
</style>

<script>
(function () {
  var DATA_URL = "{{ '/technical-training/journal-club/graph-data.json' | relative_url }}";

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
    'foundational': '#f59e0b',
    'hub': '#2563eb',
    'bridge': '#10b981',
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

  var canvas = document.getElementById('jcg-canvas');
  var ctx = canvas.getContext('2d');
  var tierButtons = Array.from(document.querySelectorAll('.jcg-tier-btn'));
  var layoutButtons = Array.from(document.querySelectorAll('.jcg-layout-btn'));
  var showEdgesCheck = document.getElementById('jcg-show-edges');
  var showArrowsCheck = document.getElementById('jcg-show-arrows');
  var colorByEl = document.getElementById('jcg-color-by');
  var eraChecks = Array.from(document.querySelectorAll('.jcg-era-check'));
  var dimensionEl = document.getElementById('jcg-dimension');
  var organismEl = document.getElementById('jcg-organism');
  var degreeEl = document.getElementById('jcg-min-degree');
  var degreeVal = document.getElementById('jcg-degree-val');
  var searchEl = document.getElementById('jcg-search');
  var countEl = document.getElementById('jcg-count');
  var resetBtn = document.getElementById('jcg-reset');
  var promptTriggerBtn = document.getElementById('jcg-prompt-btn');
  var promptCountSpan = document.getElementById('jcg-prompt-count');
  var promptModal = document.getElementById('jcg-prompt-modal');
  var promptModalClose = document.getElementById('jcg-prompt-close');
  var promptTextarea = document.getElementById('jcg-prompt-textarea');
  var modalPaperCount = document.getElementById('jcg-modal-paper-count');
  var copyPromptBtn = document.getElementById('jcg-copy-prompt-btn');
  var copyStatus = document.getElementById('jcg-copy-status');
  var tooltip = document.getElementById('jcg-tooltip');
  var panel = document.getElementById('jcg-panel');
  var panelBody = document.getElementById('jcg-panel-body');
  var panelClose = document.getElementById('jcg-panel-close');
  var legendEl = document.getElementById('jcg-legend');
  var legendTitleEl = document.getElementById('jcg-legend-title');

  var allPapers = [];
  var currentTier = 500;
  var currentLayout = 'organic';
  var currentColorCue = 'dimension';
  var visibleNodes = [];
  var visibleEdges = [];
  var nodeMap = {};
  var view = { scale: 1, tx: 0, ty: 0 };
  var draggingNode = null;
  var isPanning = false;
  var panStart = { x: 0, y: 0 };
  var hoveredNode = null;
  var selectedNode = null;
  var alpha = 1.0;
  var animFrame = null;

  function getNodeColor(p) {
    if (currentColorCue === 'era') {
      return ERA_COLORS[p.era] || '#64748b';
    } else if (currentColorCue === 'tier') {
      return TIER_COLORS[p.tier] || '#94a3b8';
    } else if (currentColorCue === 'organism') {
      var org = (p.organism && p.organism[0]) ? p.organism[0].toLowerCase() : 'general';
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
        { k: 'Top 500 Core Flagship', c: TIER_COLORS[500] },
        { k: 'Top 1,000 Landmark', c: TIER_COLORS[1000] },
        { k: 'Top 2,000 Network', c: TIER_COLORS[2000] }
      ].forEach(function (item) {
        var row = document.createElement('div');
        row.className = 'jcg-legend-item';
        row.innerHTML = '<span class="jcg-legend-swatch" style="background:' + item.c + '"></span>' + item.k;
        legendEl.appendChild(row);
      });
    } else if (currentColorCue === 'organism') {
      legendTitleEl.textContent = 'Color Cue: Model Organism';
      Object.keys(ORGANISM_COLORS).forEach(function (k) {
        var row = document.createElement('div');
        row.className = 'jcg-legend-item';
        row.innerHTML = '<span class="jcg-legend-swatch" style="background:' + ORGANISM_COLORS[k] + '"></span>' + k.replace(/-/g, ' ').toUpperCase();
        legendEl.appendChild(row);
      });
    } else if (currentColorCue === 'citation_role') {
      legendTitleEl.textContent = 'Color Cue: Citation Role';
      Object.keys(ROLE_COLORS).forEach(function (k) {
        var row = document.createElement('div');
        row.className = 'jcg-legend-item';
        row.innerHTML = '<span class="jcg-legend-swatch" style="background:' + ROLE_COLORS[k] + '"></span>' + k.toUpperCase();
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
    allPapers = data.map(function (d, i) {
      var cat = d.dimension || 'circuit-structure';
      var hub = CATEGORY_HUBS[cat] || { x: 0, y: 0 };
      var jitter = (Math.random() - 0.5) * 120;
      var orgs = Array.isArray(d.organism) ? d.organism : [d.organism || 'general'];
      return {
        id: d.id,
        title: d.title || 'Untitled',
        authors: d.authors || '',
        year: d.year || 2020,
        journal: d.journal || '',
        doi: (d.doi || '').toLowerCase(),
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
        x: hub.x + jitter,
        y: hub.y + jitter,
        targetX: hub.x,
        targetY: hub.y,
        vx: 0,
        vy: 0,
        radius: Math.max(4.5, Math.min(16, 4.5 + Math.sqrt((d.in_degree || 0) + (d.out_degree || 0)) * 1.5))
      };
    });

    resizeCanvas();
    updateLegend();
    applyFilters();
    fitView();
    startPhysics();
  }).catch(function (err) {
    console.error(err);
    countEl.textContent = 'Error loading graph data.';
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
      if (p.tier > currentTier) return false;
      if (activeEras.indexOf(p.era) === -1) return false;
      if (selectedCat !== 'all' && p.dimension !== selectedCat) return false;
      if (selectedOrg !== 'all') {
        var orgMatch = p.organism.some(function (o) { return o.toLowerCase().indexOf(selectedOrg) !== -1; });
        if (!orgMatch) return false;
      }
      if (p.total_degree < minDeg) return false;
      if (query) {
        var matchT = p.title.toLowerCase().indexOf(query) !== -1;
        var matchA = p.authors.toLowerCase().indexOf(query) !== -1;
        var matchJ = p.journal.toLowerCase().indexOf(query) !== -1;
        if (!matchT && !matchA && !matchJ) return false;
      }
      return true;
    });

    nodeMap = {};
    var doiMap = {};
    visibleNodes.forEach(function (n) { 
      nodeMap[n.id] = n; 
      if (n.doi) doiMap[n.doi] = n;
    });

    // Rematerialize directed citation edges between visible nodes
    visibleEdges = [];
    visibleNodes.forEach(function (src) {
      if (src.cites && src.cites.length) {
        src.cites.forEach(function (targetDoi) {
          var tgt = doiMap[targetDoi.toLowerCase()];
          if (tgt && tgt !== src) {
            visibleEdges.push({
              source: src,
              target: tgt,
              weight: 1.0
            });
          }
        });
      }
    });

    countEl.textContent = 'Showing ' + visibleNodes.length + ' papers & ' + visibleEdges.length + ' citation edges';
    promptCountSpan.textContent = visibleNodes.length;
    alpha = 1.0;

    // Recalculate target coordinates based on layout mode
    if (currentLayout === 'timeline') {
      var minYear = 1986, maxYear = 2026;
      var spanW = 800;
      visibleNodes.forEach(function (n) {
        var normX = (n.year - minYear) / (maxYear - minYear);
        n.targetX = (normX - 0.5) * spanW;
        var catIdx = CATEGORIES.indexOf(n.dimension);
        n.targetY = ((catIdx - CATEGORIES.length / 2) / CATEGORIES.length) * 500;
      });
    } else if (currentLayout === 'cluster') {
      visibleNodes.forEach(function (n) {
        var hub = CATEGORY_HUBS[n.dimension] || { x: 0, y: 0 };
        n.targetX = hub.x;
        n.targetY = hub.y;
      });
    }
  }

  function fitView() {
    if (!visibleNodes.length) return;
    var minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity;
    visibleNodes.forEach(function (n) {
      if (n.x < minX) minX = n.x;
      if (n.x > maxX) maxX = n.x;
      if (n.y < minY) minY = n.y;
      if (n.y > maxY) maxY = n.y;
    });
    var w = Math.max(maxX - minX + 140, 260);
    var h = Math.max(maxY - minY + 140, 260);
    var cw = canvas.width / (window.devicePixelRatio || 1);
    var ch = canvas.height / (window.devicePixelRatio || 1);
    view.scale = Math.min(cw / w, ch / h, 1.8) * 0.85;
    view.tx = cw / 2 - ((minX + maxX) / 2) * view.scale;
    view.ty = ch / 2 - ((minY + maxY) / 2) * view.scale;
  }

  // High-Performance Physics Simulation Loop with Organic Force Option
  function tickPhysics() {
    if (alpha < 0.003) return;
    var dt = 0.04 * alpha;

    if (currentLayout === 'organic') {
      // 1. Organic Spring Force along Citation Edges (Hooke's Law attraction)
      for (var e = 0; e < visibleEdges.length; e++) {
        var edge = visibleEdges[e];
        var s = edge.source;
        var t = edge.target;
        var dx = t.x - s.x;
        var dy = t.y - s.y;
        var dist = Math.hypot(dx, dy) || 1;
        var desiredDist = 90;
        var force = (dist - desiredDist) * 0.04 * dt;
        var fx = (dx / dist) * force;
        var fy = (dy / dist) * force;

        s.vx += fx;
        s.vy += fy;
        t.vx -= fx;
        t.vy -= fy;
      }

      // 2. Node Repulsion (Coulomb Repulsion)
      for (var i = 0; i < visibleNodes.length; i++) {
        var n1 = visibleNodes[i];
        if (n1 === draggingNode) continue;

        // Centering gravity
        n1.vx -= n1.x * 0.002 * dt;
        n1.vy -= n1.y * 0.002 * dt;

        for (var j = i + 1; j < visibleNodes.length; j++) {
          var n2 = visibleNodes[j];
          var rx = n2.x - n1.x;
          var ry = n2.y - n1.y;
          var r2 = rx * rx + ry * ry + 100;
          if (r2 < 40000) {
            var repForce = (3000 / r2) * dt;
            var r = Math.sqrt(r2);
            var rfx = (rx / r) * repForce;
            var rfy = (ry / r) * repForce;
            n1.vx -= rfx;
            n1.vy -= rfy;
            n2.vx += rfx;
            n2.vy += rfy;
          }
        }

        n1.vx *= 0.85;
        n1.vy *= 0.85;
        n1.x += n1.vx;
        n1.y += n1.vy;
      }

    } else {
      // Anchored modes (Cluster hubs or Timeline)
      for (var i = 0; i < visibleNodes.length; i++) {
        var n = visibleNodes[i];
        if (n === draggingNode) continue;

        var dx = n.targetX - n.x;
        var dy = n.targetY - n.y;
        n.vx += dx * dt * 0.8;
        n.vy += dy * dt * 0.8;

        n.vx *= 0.88;
        n.vy *= 0.88;
        n.x += n.vx;
        n.y += n.vy;
      }
    }

    alpha *= 0.988;
  }

  function render() {
    var cw = canvas.width / (window.devicePixelRatio || 1);
    var ch = canvas.height / (window.devicePixelRatio || 1);
    ctx.clearRect(0, 0, cw, ch);

    ctx.save();
    ctx.translate(view.tx, view.ty);
    ctx.scale(view.scale, view.scale);

    // Draw Category Cluster Hub Background Rings (in Cluster mode)
    if (currentLayout === 'cluster' && view.scale > 0.4) {
      CATEGORIES.forEach(function (cat) {
        var hub = CATEGORY_HUBS[cat];
        ctx.beginPath();
        ctx.arc(hub.x, hub.y, 85, 0, Math.PI * 2);
        ctx.fillStyle = CATEGORY_COLORS[cat] + '08';
        ctx.fill();
        ctx.strokeStyle = CATEGORY_COLORS[cat] + '20';
        ctx.lineWidth = 1 / view.scale;
        ctx.stroke();

        ctx.fillStyle = CATEGORY_COLORS[cat] + '80';
        ctx.font = 'bold 11px Inter, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(cat.replace(/-/g, ' ').toUpperCase(), hub.x, hub.y - 95);
      });
    }

    // Draw Timeline Year Guides (in Timeline mode)
    if (currentLayout === 'timeline') {
      [1990, 2000, 2010, 2020, 2025].forEach(function (yr) {
        var normX = (yr - 1986) / (2026 - 1986);
        var gx = (normX - 0.5) * 800;
        ctx.beginPath();
        ctx.moveTo(gx, -300);
        ctx.lineTo(gx, 300);
        ctx.strokeStyle = '#e2e8f0';
        ctx.lineWidth = 1 / view.scale;
        ctx.stroke();

        ctx.fillStyle = '#94a3b8';
        ctx.font = 'bold 12px Inter, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(yr.toString(), gx, -310);
      });
    }

    // Draw Citation Edges with Weights and Directional Arrows
    var drawEdges = showEdgesCheck.checked;
    var drawArrows = showArrowsCheck.checked;

    if (drawEdges && visibleEdges.length) {
      for (var e = 0; e < visibleEdges.length; e++) {
        var edge = visibleEdges[e];
        var s = edge.source;
        var t = edge.target;

        var isHighlighted = (hoveredNode && (s === hoveredNode || t === hoveredNode)) ||
                            (selectedNode && (s === selectedNode || t === selectedNode));

        // When a node is hovered/selected, dim unrelated edges
        if ((hoveredNode || selectedNode) && !isHighlighted) {
          continue; // Skip drawing background edges for maximum clarity
        }

        ctx.beginPath();
        ctx.moveTo(s.x, s.y);
        ctx.lineTo(t.x, t.y);

        if (isHighlighted) {
          ctx.strokeStyle = (s === hoveredNode || s === selectedNode) ? '#f59e0b' : '#06b6d4';
          ctx.lineWidth = 2.0 / view.scale;
        } else {
          ctx.strokeStyle = '#94a3b833';
          ctx.lineWidth = 0.8 / view.scale;
        }
        ctx.stroke();

        // Draw Directional Arrowhead pointing from citing source -> cited target
        if (drawArrows || isHighlighted) {
          var dx = t.x - s.x;
          var dy = t.y - s.y;
          var angle = Math.atan2(dy, dx);
          var headlen = (isHighlighted ? 7 : 4.5) / view.scale;
          // Position arrow near target boundary
          var ax = t.x - Math.cos(angle) * (t.radius + 3);
          var ay = t.y - Math.sin(angle) * (t.radius + 3);

          ctx.beginPath();
          ctx.moveTo(ax, ay);
          ctx.lineTo(ax - headlen * Math.cos(angle - Math.PI / 6), ay - headlen * Math.sin(angle - Math.PI / 6));
          ctx.lineTo(ax - headlen * Math.cos(angle + Math.PI / 6), ay - headlen * Math.sin(angle + Math.PI / 6));
          ctx.closePath();
          ctx.fillStyle = isHighlighted ? ((s === hoveredNode || s === selectedNode) ? '#f59e0b' : '#06b6d4') : '#94a3b866';
          ctx.fill();
        }
      }
    }

    // Draw Nodes with Visual Cues
    for (var i = 0; i < visibleNodes.length; i++) {
      var n = visibleNodes[i];
      var isHovered = (n === hoveredNode);
      var isSelected = (n === selectedNode);

      ctx.beginPath();
      ctx.arc(n.x, n.y, n.radius * (isHovered ? 1.3 : 1.0), 0, Math.PI * 2);
      ctx.fillStyle = getNodeColor(n);
      ctx.fill();

      if (isHovered || isSelected || n.tier === 500) {
        ctx.strokeStyle = isSelected ? '#0f172a' : (isHovered ? '#ffffff' : '#ffffff88');
        ctx.lineWidth = (isSelected ? 3 : 1.5) / view.scale;
        ctx.stroke();
      }

      // Draw Flagship Titles when zoomed in or hovered
      if ((view.scale > 0.8 && n.total_degree > 30) || isHovered || isSelected) {
        ctx.fillStyle = '#1e293b';
        ctx.font = (isHovered ? 'bold 11px' : '9px') + ' Inter, sans-serif';
        ctx.textAlign = 'left';
        ctx.fillText(n.title.length > 25 ? n.title.slice(0, 24) + '…' : n.title, n.x + n.radius + 3, n.y + 3);
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

  // Interaction Handlers
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
      if (dist <= n.radius + 4 / view.scale) return n;
    }
    return null;
  }

  canvas.addEventListener('mousemove', function (e) {
    var pos = getMousePos(e);
    if (isPanning) {
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
      tooltip.innerHTML = '<strong>' + node.title + '</strong>' +
        '<div class="meta">' + node.authors + ' (' + node.year + ') &bull; ' + node.journal + '</div>' +
        '<div><strong>Tier ' + node.tier + '</strong> &bull; ' + node.dimension + ' &bull; In:' + node.in_degree + ' Out:' + node.out_degree + '</div>';
    } else {
      canvas.style.cursor = 'grab';
      tooltip.classList.add('hidden');
    }
  });

  canvas.addEventListener('mousedown', function (e) {
    var pos = getMousePos(e);
    var node = findNodeUnder(pos);
    if (node) {
      selectedNode = node;
      openPaperDrawer(node);
    } else {
      isPanning = true;
      panStart = { x: e.clientX, y: e.clientY };
      canvas.classList.add('dragging');
    }
  });

  window.addEventListener('mouseup', function () {
    isPanning = false;
    canvas.classList.remove('dragging');
  });

  canvas.addEventListener('wheel', function (e) {
    e.preventDefault();
    var rect = canvas.getBoundingClientRect();
    var mx = e.clientX - rect.left;
    var my = e.clientY - rect.top;
    var zoomFactor = e.deltaY < 0 ? 1.15 : 0.85;
    var newScale = Math.max(0.15, Math.min(4.0, view.scale * zoomFactor));

    view.tx = mx - (mx - view.tx) * (newScale / view.scale);
    view.ty = my - (my - view.ty) * (newScale / view.scale);
    view.scale = newScale;
  }, { passive: false });

  // Open Detailed Paper Drawer
  function openPaperDrawer(p) {
    panel.classList.remove('hidden');
    var html = '<h3>' + p.title + '</h3>' +
      '<div class="jcg-panel-authors">' + p.authors + ' &bull; <em>' + p.journal + '</em> (' + p.year + ')</div>' +
      '<div class="jcg-panel-meta-tags">' +
        '<span class="jcg-panel-tag tier-tag">Tier ' + p.tier + ' (' + (p.tier === 500 ? 'Core Flagship' : (p.tier === 1000 ? 'Landmark' : 'Comprehensive')) + ')</span>' +
        '<span class="jcg-panel-tag">' + p.dimension + '</span>' +
        '<span class="jcg-panel-tag">' + p.era + '</span>' +
        '<span class="jcg-panel-tag">In: ' + p.in_degree + ' | Out: ' + p.out_degree + '</span>' +
        '<span class="jcg-panel-tag">K-Core: ' + p.kcore + '</span>' +
      '</div>' +
      '<div class="jcg-summary-content"><strong>Summary:</strong> ' + p.summary + '</div>' +
      '<div class="jcg-ocar-box">' +
        '<strong>Citation:</strong>' +
        '<p style="font-size:0.75rem; color:#475569;">' + p.citation + '</p>' +
      '</div>' +
      '<div class="jcg-panel-links">' +
        '<a href="https://doi.org/' + p.doi + '" target="_blank" rel="noopener">Read on Publisher &rarr;</a>' +
      '</div>';
    panelBody.innerHTML = html;
  }

  panelClose.addEventListener('click', function () {
    panel.classList.add('hidden');
    selectedNode = null;
  });

  // AI Synthesis Prompt Generation
  function generateSynthesisPrompt() {
    var cat = dimensionEl.value === 'all' ? 'All Connectomics Subfields' : dimensionEl.options[dimensionEl.selectedIndex].text;
    var org = organismEl.value === 'all' ? 'All Model Organisms' : organismEl.options[organismEl.selectedIndex].text;
    var count = visibleNodes.length;

    var paperList = visibleNodes.slice(0, 40).map(function (p, idx) {
      return (idx + 1) + '. "' + p.title + '" (' + p.authors + ', ' + p.year + ', ' + p.journal + ')\n   Summary: ' + (p.summary || 'Milestone connectomics contribution') + '\n   DOI: https://doi.org/' + p.doi;
    }).join('\n\n');

    var truncationNote = count > 40 ? '\n\n... and ' + (count - 40) + ' additional selected papers from the curated corpus.' : '';

    var prompt = 'You are an expert computational neuroscientist and connectomics researcher. ' +
      'Analyze and synthesize the current state of research based on the following ' + count + ' curated milestone publications ' +
      'focusing on: Domain = [' + cat + '] and Organism = [' + org + '].\n\n' +
      '### Curated Literature Subset (N = ' + count + '):\n' +
      paperList + truncationNote + '\n\n' +
      '### Synthesis Tasks Required:\n' +
      '1. **Current State of the Subfield**: Provide an executive summary of where research in this domain currently stands based on these landmark studies.\n' +
      '2. **Major Accomplishments & Breakthroughs**: Detail the core technical or biological breakthroughs accomplished by these papers (e.g. imaging pipelines, proofreading paradigms, synaptic wiring discoveries, scaling benchmarks).\n' +
      '3. **Key Technical & Biological Challenges**: Identify the persistent bottlenecks, failure modes, and methodological debates highlighted across these works.\n' +
      '4. **Open Research Questions & Future Outlook**: What are the top 3-5 high-priority research questions that the community must address over the next 3-5 years?\n\n' +
      'Structure your response with clear markdown headings, concise bullet points, and explicit citations to the relevant papers listed above.';

    promptTextarea.value = prompt;
    modalPaperCount.textContent = count;
    copyStatus.classList.add('hidden');
    promptModal.classList.remove('hidden');
  }

  promptTriggerBtn.addEventListener('click', generateSynthesisPrompt);
  promptModalClose.addEventListener('click', function () { promptModal.classList.add('hidden'); });

  copyPromptBtn.addEventListener('click', function () {
    promptTextarea.select();
    navigator.clipboard.writeText(promptTextarea.value).then(function () {
      copyStatus.classList.remove('hidden');
      setTimeout(function () { copyStatus.classList.add('hidden'); }, 3000);
    }).catch(function (err) {
      alert('Prompt selected! Press Ctrl+C / Cmd+C to copy.');
    });
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
    currentTier = 500;
    currentLayout = 'organic';
    currentColorCue = 'dimension';
    colorByEl.value = 'dimension';
    showEdgesCheck.checked = true;
    showArrowsCheck.checked = true;
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
