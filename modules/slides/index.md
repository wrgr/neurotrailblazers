---
layout: page
title: "Module Slide Decks"
permalink: /modules/slides/
slug: module-slides
track: core-concepts-methods
pathways:
  - classroom delivery
---

## Module Slide Decks

<p>Need full lesson kits and facilitator guidance? Visit the <a href="{{ '/teaching/' | relative_url }}">Teaching Hub</a>.</p>

<div class="cards-grid">
{% assign module_pages = site.pages | where_exp: 'p', "p.path contains 'modules/slides/module'" | sort: 'path' %}
{% for p in module_pages %}
  <article class="card">
    <h3 class="card-title"><a href="{{ p.url | relative_url }}">{{ p.title }}</a></h3>
    <p class="card-description">Slide source and worksheet links for instructional delivery.</p>
  </article>
{% endfor %}
</div>
