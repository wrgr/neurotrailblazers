---
layout: page
title: "Technical Training Slide Decks"
permalink: /technical-training/slides/
slug: technical-training-slides
---

## Technical Slide Decks
These are lecture-ready slide structures for each technical-training unit.

Each deck now includes:
- Session profile (audience, duration, expected output).
- Slide-by-slide timing and technical talking points.
- Figure integration hooks to extracted asset shortlists.
- Assessment artifacts and rubric dimensions.

## Slide source files
Production-oriented markdown slide sources are available under:
- `course/decks/marp/`
- Reference guide: `course/decks/marp/README.md`

Rendered outputs are available under:
- `course/decks/marp/out/`
- HTML: `*.html`
- PowerPoint: `*.pptx`

Need full module teaching kits? Visit the [Teaching Hub]({{ '/teaching/' | relative_url }}).

<div class="cards-grid">
  {% for item in site.data.technical_track.modules %}
  {% assign deck = item.slug %}
  <article class="card">
    <h3 class="card-title"><a href="{{ '/technical-training/slides/' | append: item.slug | append: '/' | relative_url }}">{{ item.title }}</a></h3>
    <p class="card-description">Lecture-ready draft with timing, technical depth, figure mapping, and evaluation prompts.</p>
    <p><a href="{{ '/technical-training/' | append: item.slug | append: '/' | relative_url }}">Open unit page</a></p>
    <p><a href="{{ '/course/decks/marp/out/' | append: deck | append: '.html' | relative_url }}">Open HTML deck</a> | <a href="{{ '/course/decks/marp/out/' | append: deck | append: '.pptx' | relative_url }}">PowerPoint</a></p>
  </article>
  {% endfor %}
</div>
