---
layout: default
title: "Connectome KB"
permalink: /kb/
description: "Visualization layer for bibliometric outputs generated in connectome-kb."
content_type: core
---

<div class="layout-content layout-page">

<section class="section section-compact">
  <h1>The Field, Mapped</h1>
  <p>Three interactive views of the connectomics literature, built from the same corpus behind the <a href="{{ '/technical-training/journal-club/' | relative_url }}">journal club</a>. Use them to see where a paper you are reading sits: which cluster of work it belongs to, what it descends from, and what has since built on it. Drag to pan, scroll to zoom, hover a node for the paper it represents.</p>
</section>

<section class="section section-compact">
  <h2>Field Map</h2>
  <iframe src="/assets/analysis/field_map.html" width="100%" height="700" style="border:1px solid #2a2a4a; border-radius:6px; background:#0a0a1a;" loading="lazy"></iframe>
</section>

<section class="section section-compact">
  <h2>Research Evolution</h2>
  <iframe src="/assets/analysis/evolution_graph.html" width="100%" height="700" style="border:1px solid #2a2a4a; border-radius:6px; background:#0a0a1a;" loading="lazy"></iframe>
</section>

<section class="section section-compact">
  <h2>Citation Lineage</h2>
  <iframe src="/assets/analysis/citation-lineage.html" width="100%" height="700" style="border:1px solid #2a2a4a; border-radius:6px; background:#0a0a1a;" loading="lazy"></iframe>
</section>

</div>
