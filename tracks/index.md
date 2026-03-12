---
layout: page
title: "Learning Tracks"
permalink: /tracks/
slug: learning-tracks
track: career-and-community
pathways:
  - program design
  - professional growth
summary: "Three-track learning architecture aligned to Fadel dimensions."
---

<div class="main-content">
  <div class="hero hero-spaced hero-rounded">
    <div class="hero-content">
      <h1 class="hero-title-impact">Learning Tracks</h1>
      <p class="hero-subtitle">A simpler structure: three tracks, one coherent journey.</p>
    </div>
  </div>

  <section class="section">
    <p>NeuroTrailblazers is organized around three tracks aligned to the Fadel dimensions: <strong>Knowledge</strong>, <strong>Skills</strong>, <strong>Character</strong>, and <strong>Meta-learning</strong>.</p>
    <p><strong>Featured:</strong> the canonical technical connectomics course is available at <a href="{{ '/technical-training/' | relative_url }}">Technical Training: Nanoscale Connectomics</a>.</p>
  </section>

  <section class="section">
    <div class="cards-grid">
      {% for track in site.data.track_catalog.tracks %}
      <article class="card">
        <h3 class="card-title"><a href="{{ '/tracks/' | append: track.slug | append: '/' | relative_url }}">{{ track.title }}</a></h3>
        <p class="card-description">{{ track.description }}</p>
        <p><strong>Fadel:</strong> {{ track.fadel_alignment | join: ', ' }}</p>
        <p><strong>Pathways:</strong> {{ track.pathways | join: ', ' }}</p>
      </article>
      {% endfor %}
    </div>
  </section>
</div>
