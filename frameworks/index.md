---
layout: framework
title: "Frameworks"
permalink: /frameworks/
slug: index
summary: "Program and learning frameworks that anchor the NeuroTrailblazers technical connectomics track."
framework_type: "Framework hub"
related_modules: []
related_tools: []
last_reviewed: 2026-03-09
maintainer: TBD
---

<div class="main-content">
  <div class="hero hero-spaced hero-rounded">
    <div class="hero-content">
      <h1 class="hero-title-impact">Frameworks</h1>
      <p class="hero-subtitle">Models that structure the canonical open connectomics course and adjacent programming.</p>
    </div>
  </div>

  <section class="section">
    <p>
      Frameworks define how the broader NeuroTrailblazers experience and the technical connectomics track
      fit together across mentoring, curriculum design, and learner progression.
    </p>
  </section>

  <section class="section">
    <div class="cards-grid">
      {% assign sorted_pages = site.pages | sort: "title" %}
      {% for framework in sorted_pages %}
        {% if framework.path == 'models.md' or framework.path == 'education/models.md' %}
          {% include cards/framework-card.html framework=framework %}
        {% endif %}
      {% endfor %}
    </div>
  </section>

  {% include ui/track-progression.html show_frameworks=true %}

  {% include ui/technical-track-roadmap.html %}
</div>
