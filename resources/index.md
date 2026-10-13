---
layout: page
title: "Find resources"
description: "Search the site or choose papers, terms, methods, datasets, and research tools."
permalink: /resources/
content_type: navigation
---

<section class="resource-search" aria-labelledby="site-search-title">
<h2 id="site-search-title">Search the site</h2>
<label for="site-search">What are you looking for?</label>
<input type="search" id="site-search" placeholder="e.g. synapse, proofreading, Python" data-index-url="{{ '/resources/search-index.json' | relative_url }}?v={{ site.time | date: '%s' }}" aria-describedby="site-search-help" disabled>
<p id="site-search-help">Search page titles and descriptions. To search individual papers, use <a href="{{ '/technical-training/journal-club/' | relative_url }}">papers and citations</a>.</p>
<p id="site-search-status" role="status" aria-live="polite">Loading search…</p>
<ul id="site-search-results" class="site-search-results"></ul>
<button type="button" id="site-search-more" class="btn btn-secondary" hidden>Show more results</button>
</section>
<section class="section resource-routes"><h2>Choose a resource</h2><div class="cards-grid">
<article class="card"><h3>Find a paper</h3><p>Search 2,000 papers, read an abstract, and follow citations.</p><a href="{{ '/technical-training/journal-club/' | relative_url }}">Papers and citations →</a></article>
<article class="card"><h3>Look up a term</h3><p>Definitions and common points of confusion.</p><a href="{{ '/technical-training/dictionary/' | relative_url }}">Connectomics dictionary →</a></article>
<article class="card"><h3>Read a method or example</h3><p>Reference explanations for imaging, anatomy, proofreading, and analysis.</p><a href="{{ '/content-library/' | relative_url }}">Methods and examples →</a></article>
<article class="card"><h3>Find data</h3><p>Dataset descriptions and instructions for accessing public volumes.</p><a href="{{ '/datasets/' | relative_url }}">Datasets →</a></article>
<article class="card"><h3>Choose a research tool</h3><p>Software and interactive tools for connectomics work.</p><a href="{{ '/tools/' | relative_url }}">Research tools →</a></article>
<article class="card"><h3>Research and career advice</h3><p>Lab expectations, mentorship, scientific communication, and professional practice.</p><a href="{{ '/hidden-curriculum/' | relative_url }}">Research and career advice →</a></article>
</div><p>Checking a dataset size or an acronym? Use the <a href="{{ '/technical-training/atlas-connectomics-reference/' | relative_url }}">reference atlas</a>. Looking for a course? <a href="{{ '/technical-training/' | relative_url }}">Start learning</a>.</p></section>
<script src="{{ '/assets/js/site-search.js' | relative_url }}?v={{ site.time | date: '%s' }}" defer></script>
