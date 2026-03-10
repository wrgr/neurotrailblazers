---
layout: page
title: "Learner Personas"
description: "Representative learner personas for tailored support across the NeuroTrailblazers ecosystem."
permalink: /avatars/
---

<div class="main-content">
  <div class="hero hero-spaced hero-rounded">
    <div class="hero-content">
      <h1 class="hero-title-impact">Learner Personas</h1>
      <p class="hero-subtitle">People-centered pathways for the technical connectomics track.</p>
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
      {% assign personas = site.pages | where_exp: "p", "p.path contains 'avatars/' and p.name != 'index.md'" | sort: "title" %}
      {% for persona in personas %}
        {% include cards/persona-card.html persona=persona %}
      {% endfor %}
    </div>
  </section>
</div>
