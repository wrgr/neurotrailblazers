---
layout: page
title: "Technical Training Slide Deck Drafts"
permalink: /technical-training/slides/
slug: technical-training-slides
---

## Draft decks
These are structured lecture-deck drafts for each technical-training unit.

<div class="cards-grid">
  {% for item in site.data.technical_track.modules %}
  <article class="card">
    <h3 class="card-title"><a href="{{ '/technical-training/slides/' | append: item.slug | append: '/' | relative_url }}">{{ item.title }}</a></h3>
    <p class="card-description">12-slide draft sequence with speaker-note prompts and figure integration points.</p>
    <p><a href="{{ '/technical-training/' | append: item.slug | append: '/' | relative_url }}">Open unit page</a></p>
  </article>
  {% endfor %}
</div>
