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
      <p class="hero-subtitle">Three clear pathways through the NeuroTrailblazers connectomics curriculum.</p>
    </div>
  </div>

  <section class="section">
    <p>NeuroTrailblazers is organized around three tracks aligned to the <strong>Fadel dimensions</strong>: Knowledge, Skills, Character, and Meta-learning. Each track emphasizes a different dimension of researcher development and maps to a distinct set of the 25 curriculum modules.</p>
    <p>The full technical sequence is available as a standalone resource: <a href="{{ '/technical-training/' | relative_url }}">Technical Training: Nanoscale Connectomics</a>. Most learners begin with <strong>Core Concepts &amp; Methods</strong>, then layer in the other two tracks as their research practice develops.</p>
  </section>

  <section class="section">
    <div class="cards-grid">
      {% for track in site.data.track_catalog.tracks %}
      <article class="card">
        <h3 class="card-title"><a href="{{ '/tracks/' | append: track.slug | append: '/' | relative_url }}">{{ track.title }}</a></h3>
        <p class="card-description">{{ track.description }}</p>
        <p><strong>Fadel:</strong> {{ track.fadel_alignment | join: ', ' }}</p>
        <p><strong>Modules:</strong> {{ track.module_numbers | size }} modules</p>
        <p><strong>Pathways:</strong> {{ track.pathways | join: ', ' }}</p>
      </article>
      {% endfor %}
    </div>
  </section>
</div>
