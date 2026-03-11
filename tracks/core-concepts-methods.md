---
layout: page
title: "Track: Core Concepts & Methods"
permalink: /tracks/core-concepts-methods/
slug: track-core-concepts-methods
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
    <p><strong>Fadel alignment:</strong> {{ track.fadel_alignment | join: ', ' }}</p>
  </section>

  <section class="section">
    <div class="cards-grid">
      {% for item in track.resources %}
      <article class="card">
        <h3 class="card-title"><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
        <p class="card-description">{{ item.summary }}</p>
      </article>
      {% endfor %}
    </div>
  </section>
</div>
