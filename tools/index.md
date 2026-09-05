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
maintainer: NeuroTrailblazers Team
use_layout_hero: false
content_type: core
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
    cataloged by workflow stage in the
    <a href="{{ '/technical-training/atlas-connectomics-reference/' | relative_url }}">connectomics atlas</a>,
    with what each one does and where it fits. For credentials, clients, and starter
    notebooks, go to the <a href="{{ '/datasets/access/' | relative_url }}">dataset access guide</a>.</p>
    <p>If you are trying to work out which tool you need rather than how to use one you have
    already chosen, the atlas table is the faster route: it is organized by the stage of the
    pipeline you are standing in.</p>
  </section>

  <section class="section">
    <h2 class="section-title left">Interactive on this site</h2>
    <p>These run in the browser, here, with no account and no install.</p>
    <ul>
      <li><a href="{{ '/technical-training/journal-club/graph/' | relative_url }}">Citation graph explorer</a> &mdash; the 2,000-paper corpus as a citation network, filterable by dimension, era and tier.</li>
      <li><a href="{{ '/technical-training/journal-club/' | relative_url }}">Journal club</a> &mdash; the same corpus as cards, each with an OCAR summary and discussion prompts.</li>
      <li><a href="{{ '/concepts/' | relative_url }}">Concept explorer</a> &mdash; concepts filtered by track and stage, each linked to where it is taught.</li>
      <li><a href="{{ '/kb/' | relative_url }}">The field, mapped</a> &mdash; visualisations of the literature and the methods landscape.</li>
      <li><a href="{{ '/technical-training/dictionary/' | relative_url }}">Connectomics dictionary</a> &mdash; 127 terms, each with a typical value and the confusion it usually causes.</li>
      <li><a href="{{ '/modules/' | relative_url }}">Module practice labs</a> &mdash; the retrieval-practice check at the foot of each module page.</li>
      <li><a href="{{ '/neuronauts/kids/' | relative_url }}">Junior Lab quiz</a> &mdash; for younger readers and classrooms.</li>
    </ul>
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
