---
layout: page
title: "Teaching Hub"
description: "Instructor-ready lesson kits with module content, rendered slides, source decks, and worksheets."
permalink: /teaching/
slug: teaching-hub
track: career-and-community
pathways:
  - classroom delivery
  - mentor support
summary: "Central hub for teaching materials across all modules."
---

<div class="main-content">
  <div class="hero hero-spaced hero-rounded">
    <div class="hero-content">
      <h1 class="hero-title-impact">Teaching Hub</h1>
      <p class="hero-subtitle">Everything needed to teach each module: lesson flow, activities, slides, and worksheets.</p>
    </div>
  </div>

  <section class="section">
    <div class="cta-buttons">
      <a href="{{ '/modules/' | relative_url }}" class="btn btn-primary">Open Module Library</a>
      <a href="{{ '/modules/slides/' | relative_url }}" class="btn btn-secondary">Browse Slide Pages</a>
      <a href="{{ '/teaching/facilitator-guide/' | relative_url }}" class="btn btn-secondary">Facilitator Guide</a>
      <a href="{{ '/technical-training/' | relative_url }}" class="btn btn-secondary">Technical Course Hub</a>
    </div>
  </section>

  <section class="section">
    <h2>Module Teaching Kits</h2>
    <p>Each card links to the lesson page, rendered slide deck, editable source, and activity worksheet.</p>
    <div class="cards-grid">
      {% assign module_pages = site.modules | sort: "module_number" %}
      {% for module in module_pages %}
        {% include cards/teaching-module-card.html module=module %}
      {% endfor %}
    </div>
  </section>
</div>
