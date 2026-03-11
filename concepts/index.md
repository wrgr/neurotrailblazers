---
layout: page
title: "Concept Explorer"
permalink: /concepts/
slug: concept-explorer
summary: "Find content by concept and learner need rather than module number."
---

<div class="main-content">
  <div class="hero hero-spaced hero-rounded">
    <div class="hero-content">
      <h1 class="hero-title-impact">Concept Explorer</h1>
      <p class="hero-subtitle">Explore NeuroTrailblazers by concept, not module numbers.</p>
    </div>
  </div>

  <section class="section">
    <p>Use this page to navigate by what you need right now: a method, a workflow challenge, or professional-development support. Modules remain available as delivery objects, but discovery is concept-first.</p>
  </section>

  {% assign all = site.data.concepts.concepts %}
  {% assign tracks = site.data.track_catalog.tracks %}

  {% for tr in tracks %}
  <section class="section">
    <h2>{{ tr.title }}</h2>
    <div class="cards-grid">
      {% for item in all %}
        {% if item.track == tr.slug %}
          {% assign primary = item.resources | first %}
          {% include cards/concept-card.html item=item primary_url=primary.url %}
        {% endif %}
      {% endfor %}
    </div>
  </section>
  {% endfor %}
</div>
