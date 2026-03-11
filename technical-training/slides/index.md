---
layout: page
title: "Technical Training Slide Deck Drafts"
permalink: /technical-training/slides/
slug: technical-training-slides
---

## Draft decks
These are lecture-ready draft structures for each technical-training unit.

Each deck now includes:
- Session profile (audience, duration, expected output).
- Slide-by-slide timing and technical talking points.
- Figure integration hooks to extracted asset shortlists.
- Assessment artifacts and rubric dimensions.

<div class="cards-grid">
  {% for item in site.data.technical_track.modules %}
  <article class="card">
    <h3 class="card-title"><a href="{{ '/technical-training/slides/' | append: item.slug | append: '/' | relative_url }}">{{ item.title }}</a></h3>
    <p class="card-description">Lecture-ready draft with timing, technical depth, figure mapping, and evaluation prompts.</p>
    <p><a href="{{ '/technical-training/' | append: item.slug | append: '/' | relative_url }}">Open unit page</a></p>
  </article>
  {% endfor %}
</div>
