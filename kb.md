---
layout: default
title: "Connectome KB"
permalink: /kb/
description: "Three interactive maps of the connectomics literature: topic clusters, how research lines evolved, and citation lineage."
content_type: core
---

<div class="layout-content layout-page">

<section class="section section-compact">
  <h1>The Field, Mapped</h1>
  <p>Three interactive views of the connectomics literature, built from the same corpus behind the <a href="{{ '/technical-training/journal-club/' | relative_url }}">journal club</a>. Use them to see where a paper you are reading sits: which cluster of work it belongs to, what it descends from, and what has since built on it. Drag to pan, scroll to zoom, hover a node for the paper it represents.</p>
</section>

<section class="section section-compact">
  <h2>Field Map</h2>
  <iframe title="Field map of the connectomics literature" src="{{ '/assets/analysis/field_map.html' | relative_url }}" width="100%" height="700" style="border:1px solid #2a2a4a; border-radius:6px; background:#0a0a1a;" loading="lazy"></iframe>
</section>

<section class="section section-compact">
  <h2>Research Evolution</h2>
  <iframe title="Research evolution graph" src="{{ '/assets/analysis/evolution_graph.html' | relative_url }}" width="100%" height="700" style="border:1px solid #2a2a4a; border-radius:6px; background:#0a0a1a;" loading="lazy"></iframe>
</section>

<section class="section section-compact">
  <h2>Citation Lineage</h2>
  <iframe title="Citation lineage graph" src="{{ '/assets/analysis/citation-lineage.html' | relative_url }}" width="100%" height="700" style="border:1px solid #2a2a4a; border-radius:6px; background:#0a0a1a;" loading="lazy"></iframe>
</section>

<section class="section section-compact">
  <h2>What these maps do not show</h2>
  <p>Node size and links on these maps come from citations, which measure attention, not correctness. A heavily cited paper is well connected, not necessarily right, and a recent paper has had less time to be cited than an old one. To judge a paper, read it: the <a href="{{ '/technical-training/journal-club/' | relative_url }}">journal club</a> states what each paper established and what it did not, and the <a href="{{ '/technical-training/journal-club/graph/' | relative_url }}">citation graph explorer</a> lets you search the same corpus by paper.</p>
</section>

</div>
