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
    <p>Two kinds of tool matter here, and they live in different places.</p>
    <p><strong>The tools on this page</strong> are NeuroTrailblazers' own: guided support for
    getting unstuck, and structured practice in judging connectome quality. Use them when you
    need a person's expertise or a scaffolded exercise.</p>
    <p><strong>The tools you will actually run</strong> &mdash; Neuroglancer, CAVE and
    <code>caveclient</code>, CloudVolume, neuPrint, CATMAID, webKnossos, <code>navis</code>,
    <code>graspologic</code>, DotMotif, BossDB &mdash; are third-party software. They are
    catalogued by workflow stage in the
    <a href="{{ '/technical-training/atlas-connectomics-reference/' | relative_url }}">connectomics atlas</a>,
    with what each one does and where it fits. For credentials, clients, and starter
    notebooks, go to the <a href="{{ '/datasets/access/' | relative_url }}">dataset access guide</a>.</p>
    <p>If you are trying to work out which tool you need rather than how to use one you have
    already chosen, the atlas table is the faster route: it is organised by the stage of the
    pipeline you are standing in.</p>
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
