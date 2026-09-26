---
layout: page
title: "Learner Personas"
description: "Four invented learners the curriculum is written for, and where each one should start."
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
      Each persona is invented. Each one stands for a kind of reader the site is written for: what they bring, what
      they are missing, and which pages they should open first. The
      <a href="{{ '/teaching/facilitator-guide/' | relative_url }}">Facilitator Guide</a> uses the same four people to
      show how to adapt one session to different learners.
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
