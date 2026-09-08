---
layout: page
title: "Learner Personas"
description: "Representative learner personas for tailored support across the NeuroTrailblazers ecosystem."
permalink: /avatars/
slug: avatars-index
track: career-and-community
pathways:
  - mentoring
  - professional growth
use_layout_hero: false
content_type: core
---

<div class="main-content">
  <div class="hero hero-spaced hero-rounded">
    <div class="hero-content">
      <h1 class="hero-title-impact">Learner Personas</h1>
      <p class="hero-subtitle">The four readers this curriculum is written for, and where each one should start.</p>
    </div>
  </div>

  <section class="section">
    <p>
      These personas complement the broader NeuroTrailblazers site by grounding the canonical open connectomics course
      in realistic learner goals, strengths, and support needs.
    </p>
  </section>

  <section class="section">
    <div class="cards-grid">
      {% assign sorted_pages = site.pages | sort: "title" %}
      {% for persona in sorted_pages %}
        {% if persona.path contains 'avatars/' and persona.name != 'index.md' %}
          {% include cards/persona-card.html persona=persona %}
        {% endif %}
      {% endfor %}
    </div>
  </section>
</div>
