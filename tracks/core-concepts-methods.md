---
layout: page
title: "Track: Core Concepts & Methods"
permalink: /tracks/core-concepts-methods/
slug: track-core-concepts-methods
track: core-concepts-methods
pathways:
  - technical foundation
  - methods depth
---

{% assign track = site.data.track_catalog.tracks | where: 'slug', 'core-concepts-methods' | first %}

<div class="main-content">
  <div class="hero hero-spaced hero-rounded">
    <div class="hero-content">
      <h1 class="hero-title-impact">{{ track.title }}</h1>
      <p class="hero-subtitle">{{ track.description }}</p>
    </div>
  </div>

  <section class="section">
    <p>{{ track.about }}</p>
    <p><strong>Fadel alignment:</strong> {{ track.fadel_alignment | join: ', ' }}</p>
  </section>

  <section class="section">
    <h2>Modules in This Track</h2>
    <div class="cards-grid">
      {% for num in track.module_numbers %}
        {% assign mod = site.data.modules | where: 'number', num | first %}
        {% if mod %}
          {% if num < 10 %}{% assign numpad = '0' | append: num %}{% else %}{% assign numpad = num | append: '' %}{% endif %}
          <article class="card">
            <p class="card-meta">{{ mod.stage }}</p>
            <h3 class="card-title"><a href="{{ '/modules/module' | append: numpad | append: '/' | relative_url }}">{{ numpad }}. {{ mod.title }}</a></h3>
            <p class="card-description">{{ mod.description }}</p>
          </article>
        {% endif %}
      {% endfor %}
    </div>
  </section>

  <section class="section">
    <h2>Resources</h2>
    <div class="cards-grid">
      {% for item in track.resources %}
      <article class="card">
        <h3 class="card-title"><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
        <p class="card-description">{{ item.summary }}</p>
      </article>
      {% endfor %}
    </div>
  </section>

  {% include ui/track-need-explorer.html
    track_slug='core-concepts-methods'
    title='Concepts in This Track'
    intro='Filter concepts by immediate need to find the most relevant next resources.' %}
</div>
