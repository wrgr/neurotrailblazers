---
layout: default
title: "Citation Graph"
permalink: /technical-training/journal-club/graph/
track: core-concepts-methods
pathways:
  - technical foundation
  - shared vocabulary
description: "The journal club collection as a citation graph: 1,057 papers, linked by which core papers they cite. Filter by k-core, era, or organism; click a node to read it; drag to rearrange."
content_type: core
---

<div class="layout-content layout-page">

<section class="jc-hero">
  <h1>Citation Graph</h1>
  <p>The same {{ site.data.journal_papers.papers.size }}-paper collection as a graph. An edge means one core paper cites another core paper &mdash; not a raw citation count, a link inside this collection. Node size is k-core: how embedded a paper is in the densest, most cross-referenced part of the field.</p>
</section>

<section class="section section-compact">
  <div class="jcg-layout">
    <div class="jcg-controls">
      <label for="jcg-kcore">Minimum k-core: <span id="jcg-kcore-val">8</span></label>
      <input type="range" id="jcg-kcore" min="0" max="13" value="8" step="1">

      <fieldset class="jcg-era-fieldset">
        <legend>Era</legend>
        <label><input type="checkbox" class="jcg-era-check" value="history" checked> History</label>
        <label><input type="checkbox" class="jcg-era-check" value="contemporary" checked> Contemporary</label>
        <label><input type="checkbox" class="jcg-era-check" value="sota" checked> SOTA</label>
      </fieldset>

      <label for="jcg-dimension">Dimension:</label>
      <select id="jcg-dimension">
        <option value="all">All dimensions</option>
        {%- for group in site.data.paper_views.dimension.groups %}
        {%- assign mapped = site.data.content_tags.dimension_labels[group.key] %}
        {%- if mapped %}{% assign dlabel = mapped %}{% else %}{% assign dlabel = group.key | replace: '-', ' ' | capitalize %}{% endif %}
        <option value="{{ group.key }}">{{ dlabel }} ({{ group.n }})</option>
        {%- endfor %}
      </select>

      <label for="jcg-organism">Organism:</label>
      <select id="jcg-organism">
        <option value="all">All organisms</option>
        {%- for group in site.data.paper_views.organism.groups %}
        <option value="{{ group.key }}">{{ group.label | default: group.key | capitalize }} ({{ group.n }})</option>
        {%- endfor %}
      </select>

      <label for="jcg-dataset">Dataset:</label>
      <select id="jcg-dataset">
        <option value="all">All datasets</option>
        {%- for group in site.data.paper_views.dataset.groups %}
        <option value="{{ group.key }}">{{ group.label | default: group.key }} ({{ group.n }})</option>
        {%- endfor %}
      </select>

      <label for="jcg-search">Highlight (title, author, method…):</label>
      <input type="text" id="jcg-search" placeholder="e.g. FlyWire, Lichtman, CATMAID…">

      <button id="jcg-reset" type="button">Reset view</button>

      <p class="jcg-count" id="jcg-count"></p>
      <p class="jcg-hint">Drag the background to pan, scroll to zoom, drag a node to move it, click a node to read it.</p>

      <div class="jcg-legend" id="jcg-legend"></div>
    </div>

    <div class="jcg-canvas-wrap">
      <canvas id="jcg-canvas"></canvas>
      <div class="jcg-tooltip hidden" id="jcg-tooltip"></div>
      <div class="jcg-panel hidden" id="jcg-panel">
        <button class="jcg-panel-close" id="jcg-panel-close" aria-label="Close">&times;</button>
        <div class="jcg-panel-body" id="jcg-panel-body"></div>
      </div>
    </div>
  </div>
</section>

</div>

<style>
.jcg-layout { display: grid; grid-template-columns: 260px 1fr; gap: 1.25rem; align-items: start; }
@media (max-width: 800px) { .jcg-layout { grid-template-columns: 1fr; } }
.jcg-controls { display: flex; flex-direction: column; gap: 0.6rem; font-size: 0.85rem; }
.jcg-controls label { font-weight: 600; }
.jcg-era-fieldset { border: 1px solid var(--brain-gray); border-radius: 8px; padding: 0.5rem 0.75rem; }
.jcg-era-fieldset legend { font-weight: 700; font-size: 0.8rem; padding: 0 0.3rem; }
.jcg-era-fieldset label { display: block; font-weight: 400; margin: 0.2rem 0; }
.jcg-controls select,
#jcg-search {
  width: 100%; box-sizing: border-box; padding: 0.4rem 0.6rem;
  border: 1px solid #d1d5db; border-radius: 6px; background: var(--white);
  font-size: 0.85rem; color: #374151;
}
.jcg-controls input[type="range"] { width: 100%; }
#jcg-reset {
  background: var(--brain-gray); border: 1px solid #d1d5db; border-radius: 6px;
  padding: 0.4rem 0.8rem; cursor: pointer; font-weight: 600; align-self: flex-start;
}
#jcg-reset:hover { background: #e5e7eb; }
.jcg-count { color: #6b7280; margin: 0; }
.jcg-hint { color: #9ca3af; font-size: 0.78rem; margin: 0; }
.jcg-legend { display: flex; flex-direction: column; gap: 0.25rem; }
.jcg-legend-item { display: flex; align-items: center; gap: 0.4rem; font-size: 0.75rem; color: #4b5563; }
.jcg-legend-swatch { width: 10px; height: 10px; border-radius: 50%; display: inline-block; flex-shrink: 0; }

.jcg-canvas-wrap { position: relative; background: var(--white); border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); overflow: hidden; }
#jcg-canvas { display: block; width: 100%; height: 640px; cursor: grab; }
#jcg-canvas.dragging { cursor: grabbing; }

.jcg-tooltip {
  position: absolute; pointer-events: none; z-index: 5;
  background: rgba(17, 24, 39, 0.92); color: #fff; border-radius: 6px;
  padding: 0.4rem 0.6rem; font-size: 0.78rem; line-height: 1.4;
  max-width: 260px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);
  transform: translate(12px, 12px);
}
.jcg-tooltip.hidden { display: none; }
.jcg-tooltip strong { display: block; font-size: 0.82rem; margin-bottom: 0.15rem; }
.jcg-tooltip span { color: #cbd5e1; }

.jcg-panel {
  position: absolute; top: 1rem; right: 1rem; width: min(340px, calc(100% - 2rem));
  background: var(--white); border-radius: 10px; box-shadow: 0 8px 24px rgba(0,0,0,0.18);
  padding: 1rem; max-height: calc(100% - 2rem); overflow-y: auto;
}
.jcg-panel.hidden { display: none; }
.jcg-panel-close {
  position: absolute; top: 0.5rem; right: 0.6rem; background: none; border: none;
  font-size: 1.3rem; line-height: 1; cursor: pointer; color: #9ca3af;
}
.jcg-panel-close:hover { color: #374151; }
.jcg-panel-body h3 { margin: 0 0.5rem 0.3rem 0; font-size: 1rem; }
.jcg-panel-body p { margin: 0.3rem 0; font-size: 0.85rem; color: #4b5563; line-height: 1.5; }
.jcg-panel-meta { display: flex; flex-wrap: wrap; gap: 0.3rem; margin: 0.4rem 0; }
.jcg-panel-meta span { background: var(--brain-gray); border-radius: 4px; padding: 0.1rem 0.4rem; font-size: 0.72rem; color: #6b7280; }
.jcg-panel-links { display: flex; gap: 0.5rem; margin-top: 0.6rem; }
.jcg-panel-links a {
  font-size: 0.8rem; font-weight: 600; text-decoration: none; color: var(--neural-blue);
  background: #dbeafe; padding: 0.3rem 0.6rem; border-radius: 6px;
}
.jcg-panel-links a:hover { opacity: 0.85; }
</style>

<script>
(function () {
  var DATA_URL = "{{ '/technical-training/journal-club/graph-data.json' | relative_url }}";
  var CARD_URL = "{{ '/technical-training/journal-club/' | relative_url }}";

  var DIMENSIONS = [
    'image-acquisition', 'connectomics', 'graph-analysis', 'segmentation',
    'infrastructure', 'proofreading', 'neuroai', 'methods-general',
    'neuroanatomy', 'cell-types', 'review'
  ];
  var PALETTE = [
    '#2563eb', '#7c3aed', '#06b6d4', '#f59e0b', '#10b981', '#ef4444',
    '#ec4899', '#6366f1', '#84cc16', '#0ea5e9', '#a855f7'
  ];
  var colorFor = {};
  DIMENSIONS.forEach(function (d, i) { colorFor[d] = PALETTE[i % PALETTE.length]; });

  var canvas  = document.getElementById('jcg-canvas');
  var ctx     = canvas.getContext('2d');
  var kcoreEl = document.getElementById('jcg-kcore');
  var kcoreVal = document.getElementById('jcg-kcore-val');
  var eraChecks = Array.from(document.querySelectorAll('.jcg-era-check'));
  var dimensionEl = document.getElementById('jcg-dimension');
  var organismEl = document.getElementById('jcg-organism');
  var datasetEl = document.getElementById('jcg-dataset');
  var searchEl = document.getElementById('jcg-search');
  var countEl  = document.getElementById('jcg-count');
  var resetBtn = document.getElementById('jcg-reset');
  var panel    = document.getElementById('jcg-panel');
  var panelBody = document.getElementById('jcg-panel-body');
  var panelClose = document.getElementById('jcg-panel-close');
  var legendEl = document.getElementById('jcg-legend');

  DIMENSIONS.forEach(function (d) {
    var row = document.createElement('div');
    row.className = 'jcg-legend-item';
    row.innerHTML = '<span class="jcg-legend-swatch" style="background:' + colorFor[d] + '"></span>' + d.replace(/-/g, ' ');
    legendEl.appendChild(row);
  });

  var allNodes = [];
  var view = { scale: 1, tx: 0, ty: 0 };
  var visibleNodes = [];
  var visibleEdges = [];
  var alpha = 1;
  var dragging = null;    // node being dragged
  var panning = false;
  var panStart = null;
  var rafId = null;
  var userAdjustedView = false;
  var frameCount = 0;

  function percentile(sorted, p) {
    var idx = Math.floor(sorted.length * p);
    return sorted[Math.min(idx, sorted.length - 1)];
  }

  function fitView() {
    if (!visibleNodes.length) return;
    // Percentile bounds (5th-95th) rather than true min/max: the force layout
    // occasionally flings one or two nodes out before the speed cap and
    // centering force reel them back in, and a naive min/max bounding box
    // would zoom the whole view out to fit that one outlier, shrinking the
    // real cluster to an unclickable speck. Fewer than 20 visible nodes skips
    // the trim (not enough points for percentiles to mean anything).
    var xs = visibleNodes.map(function (n) { return n.x; }).sort(function (a, b) { return a - b; });
    var ys = visibleNodes.map(function (n) { return n.y; }).sort(function (a, b) { return a - b; });
    var minX, maxX, minY, maxY;
    if (xs.length >= 20) {
      minX = percentile(xs, 0.05); maxX = percentile(xs, 0.95);
      minY = percentile(ys, 0.05); maxY = percentile(ys, 0.95);
    } else {
      minX = xs[0]; maxX = xs[xs.length - 1];
      minY = ys[0]; maxY = ys[ys.length - 1];
    }
    var w = Math.max(maxX - minX, 1), h = Math.max(maxY - minY, 1);
    var canvasW = canvas.width / devicePixelRatio, canvasH = canvas.height / devicePixelRatio;
    var scale = Math.min(canvasW / w, canvasH / h) * 0.85;
    view.scale = Math.min(4, Math.max(0.05, scale));
    view.tx = canvasW / 2 - (minX + maxX) / 2 * view.scale;
    view.ty = canvasH / 2 - (minY + maxY) / 2 * view.scale;
  }

  fetch(DATA_URL).then(function (r) { return r.json(); }).then(function (data) {
    allNodes = data.map(function (d, i) {
      var angle = (i / data.length) * Math.PI * 2;
      var r = 200 + Math.random() * 100;
      return {
        id: d.id, title: d.title, authors: d.authors, year: d.year, journal: d.journal,
        doi: d.doi, dimension: d.dimension, era: d.era, kcore: d.kcore || 0,
        organism: d.organism || [], dataset: d.dataset || [], method: d.method || [],
        axis: d.axis, summary: d.summary, cites: d.cites || [],
        x: Math.cos(angle) * r, y: Math.sin(angle) * r, vx: 0, vy: 0
      };
    });
    resizeCanvas();
    rebuild();
    startLoop();
  }).catch(function (err) {
    ctx.font = '14px sans-serif';
    ctx.fillText('Could not load graph data: ' + err, 20, 30);
  });

  function resizeCanvas() {
    var rect = canvas.parentElement.getBoundingClientRect();
    canvas.width = rect.width * devicePixelRatio;
    canvas.height = 640 * devicePixelRatio;
    canvas.style.width = rect.width + 'px';
    view.tx = canvas.width / (2 * devicePixelRatio);
    view.ty = canvas.height / (2 * devicePixelRatio);
  }
  window.addEventListener('resize', resizeCanvas);

  function rebuild() {
    var minK = parseInt(kcoreEl.value, 10);
    var eras = eraChecks.filter(function (c) { return c.checked; }).map(function (c) { return c.value; });
    var dim = dimensionEl.value;
    var organism = organismEl.value;
    var dataset = datasetEl.value;
    visibleNodes = allNodes.filter(function (n) {
      return n.kcore >= minK && eras.indexOf(n.era) !== -1 &&
        (dim === 'all' || n.dimension === dim) &&
        (organism === 'all' || n.organism.indexOf(organism) !== -1) &&
        (dataset === 'all' || n.dataset.indexOf(dataset) !== -1);
    });
    var idSet = {};
    visibleNodes.forEach(function (n) { idSet[n.id] = true; });
    visibleEdges = [];
    visibleNodes.forEach(function (n) {
      n.cites.forEach(function (targetId) {
        if (idSet[targetId]) visibleEdges.push({ source: n, target: findNode(targetId) });
      });
    });
    countEl.textContent = visibleNodes.length + ' papers, ' + visibleEdges.length + ' links shown' +
      (visibleNodes.length > 600 ? ' (large graph — layout may be slow)' : '');
    alpha = 1;
    fitView();
  }

  function findNode(id) {
    for (var i = 0; i < visibleNodes.length; i++) { if (visibleNodes[i].id === id) return visibleNodes[i]; }
    return null;
  }

  function tick() {
    if (alpha < 0.01) return;
    var n = visibleNodes.length;
    if (n === 0) { alpha = 0; return; }
    var repelK = 400;
    for (var i = 0; i < n; i++) {
      var a = visibleNodes[i];
      if (a === dragging) continue;
      var fx = 0, fy = 0;
      for (var j = 0; j < n; j++) {
        if (i === j) continue;
        var b = visibleNodes[j];
        var dx = a.x - b.x, dy = a.y - b.y;
        // Epsilon of 25 (not 0.01) floors the minimum effective distance at ~5
        // units, so two nodes spawning almost on top of each other don't produce
        // a near-singular force that flings one to the edge of the simulation --
        // that outlier then wrecked fitView()'s bounding box for everyone else.
        var d2 = dx * dx + dy * dy + 25;
        var f = repelK / d2;
        fx += dx * f; fy += dy * f;
      }
      // gentle centering
      fx += -a.x * 0.01; fy += -a.y * 0.01;
      a.vx = (a.vx + fx * alpha) * 0.85;
      a.vy = (a.vy + fy * alpha) * 0.85;
      // Speed cap: without this, a single high-alpha frame near a near-singular
      // pair could still impart enough velocity to send a node flying outward
      // faster than centering/damping can reel it back in before alpha decays.
      var speed = Math.sqrt(a.vx * a.vx + a.vy * a.vy);
      var maxSpeed = 30;
      if (speed > maxSpeed) { a.vx = a.vx / speed * maxSpeed; a.vy = a.vy / speed * maxSpeed; }
    }
    visibleEdges.forEach(function (e) {
      if (!e.target) return;
      var dx = e.target.x - e.source.x, dy = e.target.y - e.source.y;
      var dist = Math.sqrt(dx * dx + dy * dy) || 1;
      var rest = 70;
      var f = (dist - rest) * 0.02 * alpha;
      var ux = dx / dist, uy = dy / dist;
      if (e.source !== dragging) { e.source.vx += ux * f; e.source.vy += uy * f; }
      if (e.target !== dragging) { e.target.vx -= ux * f; e.target.vy -= uy * f; }
    });
    visibleNodes.forEach(function (a) {
      if (a === dragging) return;
      a.x += a.vx; a.y += a.vy;
    });
    alpha *= 0.985;
  }

  function radiusFor(n) { return 3 + Math.sqrt(n.kcore || 1) * 2; }

  function draw() {
    ctx.save();
    ctx.setTransform(devicePixelRatio, 0, 0, devicePixelRatio, 0, 0);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.translate(view.tx, view.ty);
    ctx.scale(view.scale, view.scale);

    var query = searchEl.value.trim().toLowerCase();

    ctx.strokeStyle = 'rgba(107,114,128,0.25)';
    ctx.lineWidth = 1 / view.scale;
    visibleEdges.forEach(function (e) {
      if (!e.target) return;
      ctx.beginPath();
      ctx.moveTo(e.source.x, e.source.y);
      ctx.lineTo(e.target.x, e.target.y);
      ctx.stroke();
    });

    visibleNodes.forEach(function (n) {
      var matches = query && (
        n.title.toLowerCase().indexOf(query) !== -1 ||
        (n.authors || '').toLowerCase().indexOf(query) !== -1 ||
        n.organism.join(' ').toLowerCase().indexOf(query) !== -1 ||
        n.method.join(' ').toLowerCase().indexOf(query) !== -1 ||
        n.dataset.join(' ').toLowerCase().indexOf(query) !== -1
      );
      var r = radiusFor(n);
      ctx.beginPath();
      ctx.arc(n.x, n.y, r, 0, Math.PI * 2);
      ctx.fillStyle = colorFor[n.dimension] || '#9ca3af';
      ctx.globalAlpha = query && !matches ? 0.15 : 1;
      ctx.fill();
      if (matches) {
        ctx.lineWidth = 2 / view.scale;
        ctx.strokeStyle = '#111827';
        ctx.stroke();
      }
      if (n === hoveredNode) {
        ctx.beginPath();
        ctx.arc(n.x, n.y, r + 3 / view.scale, 0, Math.PI * 2);
        ctx.lineWidth = 2 / view.scale;
        ctx.strokeStyle = '#111827';
        ctx.stroke();
      }
      ctx.globalAlpha = 1;
    });
    ctx.restore();
  }

  function loop() {
    tick();
    frameCount++;
    // Auto-fit the view to the spreading layout during the settle phase only
    // (never once the visitor has manually zoomed/panned/dragged), so nodes
    // pushed apart by repulsion don't drift off the visible canvas.
    if (!userAdjustedView && alpha > 0.02 && frameCount % 10 === 0) fitView();
    draw();
    rafId = requestAnimationFrame(loop);
  }
  function startLoop() { if (!rafId) rafId = requestAnimationFrame(loop); }

  // --- interaction: pan, zoom, drag, click ---
  function screenToWorld(px, py) {
    return { x: (px - view.tx) / view.scale, y: (py - view.ty) / view.scale };
  }

  function nodeAt(px, py) {
    var w = screenToWorld(px, py);
    for (var i = visibleNodes.length - 1; i >= 0; i--) {
      var n = visibleNodes[i];
      var r = radiusFor(n) + 2;
      var dx = w.x - n.x, dy = w.y - n.y;
      if (dx * dx + dy * dy <= r * r) return n;
    }
    return null;
  }

  function canvasPos(e) {
    var rect = canvas.getBoundingClientRect();
    return { x: e.clientX - rect.left, y: e.clientY - rect.top };
  }

  canvas.addEventListener('mousedown', function (e) {
    var pos = canvasPos(e);
    var n = nodeAt(pos.x, pos.y);
    userAdjustedView = true;
    if (n) {
      dragging = n;
    } else {
      panning = true;
      panStart = { x: e.clientX - view.tx, y: e.clientY - view.ty };
      canvas.classList.add('dragging');
    }
  });
  window.addEventListener('mousemove', function (e) {
    if (dragging) {
      var pos = canvasPos(e);
      var w = screenToWorld(pos.x, pos.y);
      dragging.x = w.x; dragging.y = w.y; dragging.vx = 0; dragging.vy = 0;
      if (alpha < 0.05) { alpha = 0.05; startLoop(); }
    } else if (panning) {
      view.tx = e.clientX - panStart.x;
      view.ty = e.clientY - panStart.y;
    }
  });
  var dragMoved = false;
  window.addEventListener('mousemove', function () { if (dragging || panning) dragMoved = true; });
  window.addEventListener('mouseup', function () {
    dragging = null;
    panning = false;
    canvas.classList.remove('dragging');
  });
  canvas.addEventListener('mousedown', function () { dragMoved = false; });
  canvas.addEventListener('click', function (e) {
    if (dragMoved) return;
    var pos = canvasPos(e);
    var n = nodeAt(pos.x, pos.y);
    if (n) showPanel(n);
  });
  canvas.addEventListener('wheel', function (e) {
    e.preventDefault();
    userAdjustedView = true;
    var pos = canvasPos(e);
    var before = screenToWorld(pos.x, pos.y);
    var factor = e.deltaY < 0 ? 1.1 : 0.9;
    view.scale = Math.min(4, Math.max(0.15, view.scale * factor));
    var after = screenToWorld(pos.x, pos.y);
    view.tx += (after.x - before.x) * view.scale;
    view.ty += (after.y - before.y) * view.scale;
  }, { passive: false });

  function showPanel(n) {
    panel.classList.remove('hidden');
    var organismStr = n.organism.length ? n.organism.join(', ') : '';
    panelBody.innerHTML =
      '<h3>' + escapeHtml(n.title) + '</h3>' +
      '<p>' + escapeHtml(n.authors || '') + ' &middot; ' + n.year + ' &middot; <em>' + escapeHtml(n.journal || '') + '</em></p>' +
      '<div class="jcg-panel-meta">' +
        '<span>' + n.dimension.replace(/-/g, ' ') + '</span>' +
        '<span>' + n.era + '</span>' +
        '<span>k-core ' + n.kcore + '</span>' +
        (organismStr ? '<span>' + escapeHtml(organismStr) + '</span>' : '') +
      '</div>' +
      (n.summary ? '<p>' + escapeHtml(n.summary) + '</p>' : '') +
      '<div class="jcg-panel-links">' +
        (n.doi ? '<a href="https://doi.org/' + encodeURIComponent(n.doi) + '" target="_blank" rel="noopener">DOI</a>' : '') +
        '<a href="' + CARD_URL + '#paper-' + n.id + '">Full card</a>' +
      '</div>';
  }
  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  panelClose.addEventListener('click', function () { panel.classList.add('hidden'); });

  // --- hover tooltip: a lightweight preview, separate from the click panel ---
  var tooltip = document.getElementById('jcg-tooltip');
  var hoveredNode = null;
  canvas.addEventListener('mousemove', function (e) {
    if (dragging || panning) { tooltip.classList.add('hidden'); return; }
    var pos = canvasPos(e);
    var n = nodeAt(pos.x, pos.y);
    if (n !== hoveredNode) {
      hoveredNode = n;
      canvas.style.cursor = n ? 'pointer' : '';
    }
    if (!n) { tooltip.classList.add('hidden'); return; }
    tooltip.innerHTML = '<strong>' + escapeHtml(n.title) + '</strong>' +
      '<span>' + (n.authors ? escapeHtml(n.authors.split(';')[0]) + ' et al., ' : '') + n.year +
      ' &middot; ' + n.dimension.replace(/-/g, ' ') + ' &middot; k-core ' + n.kcore + '</span>';
    tooltip.classList.remove('hidden');
    // Flip to the opposite side of the cursor when the default offset would
    // push the tooltip past the canvas edge and get clipped by overflow:hidden.
    var tw = tooltip.offsetWidth, th = tooltip.offsetHeight;
    var canvasCssW = canvas.width / devicePixelRatio, canvasCssH = canvas.height / devicePixelRatio;
    var left = (pos.x + 12 + tw > canvasCssW) ? pos.x - tw - 12 : pos.x + 12;
    var top = (pos.y + 12 + th > canvasCssH) ? pos.y - th - 12 : pos.y + 12;
    tooltip.style.left = Math.max(0, left) + 'px';
    tooltip.style.top = Math.max(0, top) + 'px';
    tooltip.style.transform = 'none';
  });
  canvas.addEventListener('mouseleave', function () {
    hoveredNode = null;
    tooltip.classList.add('hidden');
    canvas.style.cursor = '';
  });

  kcoreEl.addEventListener('input', function () { kcoreVal.textContent = this.value; rebuild(); startLoop(); });
  eraChecks.forEach(function (c) { c.addEventListener('change', function () { rebuild(); startLoop(); }); });
  dimensionEl.addEventListener('change', function () { rebuild(); startLoop(); });
  organismEl.addEventListener('change', function () { rebuild(); startLoop(); });
  datasetEl.addEventListener('change', function () { rebuild(); startLoop(); });
  searchEl.addEventListener('input', function () { /* draw() picks it up each frame while alpha > 0 */ if (alpha < 0.05) { alpha = 0.05; startLoop(); } });
  resetBtn.addEventListener('click', function () {
    userAdjustedView = false;
    resizeCanvas();
    rebuild();
    startLoop();
  });
})();
</script>
