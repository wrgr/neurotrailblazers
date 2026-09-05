---
layout: page
title: "Technical Course"
description: "Canonical open connectomics course focused on technical skills from imaging to NeuroAI."
permalink: /technical-training/
slug: technical-training
summary: "Track hub for the technical connectomics course."
track: core-concepts-methods
pathways:
  - technical foundation
  - methods depth
last_reviewed: 2026-03-10
maintainer: NeuroTrailblazers Team
use_layout_hero: false
content_type: navigation
---

<div class="main-content">
  {% assign concepts_base = '/concepts/' | relative_url %}
  <div class="hero hero-spaced hero-rounded">
    <div class="hero-content">
      <h1 class="hero-title-impact">Technical Course</h1>
      <p class="hero-subtitle">Nine units in nanoscale connectomics, from why we map the brain through imaging, reconstruction, proofreading and analysis. Each ends in a graded artifact.</p>
    </div>
  </div>

  <section class="section">
    <p>This track follows an end-to-end technical arc from motivation and imaging foundations through reconstruction, proofreading, and connectome analysis.</p>
    <p>The nine units are <strong>path content</strong>: ordered, cumulative, and each ending in an artifact. They are the spine of the <a href="{{ '/tracks/core-concepts-methods/' | relative_url }}">Core Concepts &amp; Methods</a> track, and the <a href="{{ '/technical-training/atlas-connectomics-reference/' | relative_url }}">atlas</a> rides alongside them as a reference companion, consulted rather than completed. The reference material the units draw on &mdash; dictionary, content library, journal club, atlas, hidden curriculum &mdash; sits in <a href="{{ '/core/' | relative_url }}">the core</a> and can be consulted in any order. Working through this alone is <a href="{{ '/modes/#self-study' | relative_url }}">self-study mode</a>; if you are running related sessions for a group, the <a href="{{ '/modules/' | relative_url }}">modules</a> carry the same material in tutorial form, each with a <a href="{{ '/teaching/sessions/' | relative_url }}">session kit</a> for <a href="{{ '/modes/#hosted-workshop' | relative_url }}">hosted-workshop mode</a>.</p>
    <div class="cta-buttons">
      <a href="{{ '/technical-training/journal-club/' | relative_url }}" class="btn btn-primary">Journal Club Reading List</a>
      <a href="{{ '/technical-training/dictionary/' | relative_url }}" class="btn btn-secondary">Connectomics Dictionary</a>
      <a href="{{ '/technical-training/slides/' | relative_url }}" class="btn btn-secondary">Technical Lecture Plans</a>
      <a href="{{ '/teaching/' | relative_url }}" class="btn btn-secondary">Teaching Hub</a>
      <a href="{{ '/concepts/' | relative_url }}" class="btn btn-secondary">Concept Explorer</a>
    </div>
  </section>

  <section class="section">
    <h2>Start by learner need</h2>
    <p>If sequence is less important than immediate relevance, jump directly to a need-based concept view.</p>
    <div class="cta-buttons">
      <a href="{{ concepts_base }}?track=core-concepts-methods&need=starting%20a%20research%20question" class="btn btn-secondary">Start a Research Question</a>
      <a href="{{ concepts_base }}?track=core-concepts-methods&need=improving%20data%20quality" class="btn btn-secondary">Improve Data Quality</a>
      <a href="{{ concepts_base }}?track=core-concepts-methods&need=reducing%20identity%20confusion" class="btn btn-secondary">Classify Axons vs Dendrites</a>
      <a href="{{ concepts_base }}?track=research-in-action&need=prioritizing%20corrections" class="btn btn-secondary">Prioritize Proofreading</a>
      <a href="{{ concepts_base }}?track=research-in-action&need=designing%20graph%20analyses" class="btn btn-secondary">Design Graph Analyses</a>
    </div>
  </section>

  <section class="section">
    <h2>Technical units</h2>
    {% assign concept_items = site.data.concepts.concepts %}
    <div class="cards-grid">
      {% for item in site.data.technical_track.modules %}
      {% assign first_concept_slug = item.primary_concepts | first %}
      {% assign first_concept = concept_items | where: 'slug', first_concept_slug | first %}
      {% assign primary_need = item.user_needs | first %}
      <article class="card">
        <img class="module-thumb" src="{{ '/assets/images/units/' | append: item.slug | append: '.svg' | relative_url }}" alt="" aria-hidden="true" loading="lazy" width="1200" height="420">
        <h3 class="card-title"><a href="{{ '/technical-training/' | append: item.slug | append: '/' | relative_url }}">{{ item.title }}</a></h3>
        <p class="card-description">{{ item.summary | default: item.mapping_note }}</p>
        {% if item.user_needs %}
        <p>
          {% for need in item.user_needs %}
          {% if first_concept %}
          <a class="tech-tag" href="{{ concepts_base }}?track={{ first_concept.track }}&need={{ need | url_encode }}">{{ need }}</a>
          {% else %}
          <span class="tech-tag">{{ need }}</span>
          {% endif %}
          {% endfor %}
        </p>
        {% endif %}
        {% if first_concept and primary_need %}
        <p><a href="{{ concepts_base }}?track={{ first_concept.track }}&need={{ primary_need | url_encode }}">Explore this need in Concept Explorer</a></p>
        {% endif %}
        {% if item.mapped_modules and item.mapped_modules.size > 0 %}
        <p><small>Legacy overlap: {{ item.mapped_modules | join: ', ' }}</small></p>
        {% endif %}
      </article>
      {% endfor %}
    </div>
  </section>
</div>
