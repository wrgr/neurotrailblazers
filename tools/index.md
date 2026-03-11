---
layout: tool
title: "Technical Connectomics Tools"
description: "Applied tools that support learning and execution in the technical connectomics track."
permalink: /tools/
slug: index
track: research-in-action
pathways:
  - research workflow
  - mentoring
summary: "Landing page for tools used in the technical connectomics track."
use_cases:
  - Guided exploration and Q&A
  - Quality control workflows
  - Technical skill practice
recommended_modules: []
related_datasets: []
last_reviewed: 2026-03-09
maintainer: TBD
---

<div class="main-content">
  <div class="hero hero-spaced hero-rounded">
    <div class="hero-content">
      <h1 class="hero-title-impact">Technical Connectomics Tools</h1>
      <p class="hero-subtitle">Practical tools that complement the broader curriculum and mentorship content.</p>
    </div>
  </div>

  <section class="section">
    <p>
      This collection supports the canonical open connectomics course as a technical track,
      while remaining interoperable with the rest of the NeuroTrailblazers experience.
    </p>
  </section>

  {% include ui/learning-tracks.html title="Tools Across Learning Tracks" intro="Tools support technical method-building, applied research execution, and mentorship/professional navigation." %}

  <section class="section">
    <div class="cards-grid">
      {% assign sorted_pages = site.pages | sort: "title" %}
      {% for tool in sorted_pages %}
        {% if tool.path contains 'tools/' and tool.layout == 'tool' and tool.name != 'index.md' and tool.url and tool.url != '' %}
          {% include cards/tool-card.html tool=tool %}
        {% endif %}
      {% endfor %}
    </div>
  </section>

</div>
