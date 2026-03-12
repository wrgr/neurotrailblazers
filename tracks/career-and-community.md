---
layout: page
title: "Track: Career & Community"
permalink: /tracks/career-and-community/
slug: track-career-and-community
track: career-and-community
pathways:
  - mentoring
  - professional growth
---

{% assign track = site.data.track_catalog.tracks | where: 'slug', 'career-and-community' | first %}

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

  {% include ui/track-need-explorer.html
    track_slug='career-and-community'
    title='Concepts in This Track'
    intro='Filter concepts by immediate need to identify mentoring and professional-development resources.' %}
</div>
