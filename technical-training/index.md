---
layout: page
title: "Technical Training: Nanoscale Connectomics"
description: "Canonical open connectomics course focused on technical skills from imaging to NeuroAI."
permalink: /technical-training/
slug: technical-training
summary: "Track hub for the technical connectomics course."
track: core-concepts-methods
pathways:
  - technical foundation
  - methods depth
last_reviewed: 2026-03-10
maintainer: TBD
---

<div class="main-content">
  {% assign concepts_base = '/concepts/' | relative_url %}
  <div class="hero hero-spaced hero-rounded">
    <div class="hero-content">
      <h1 class="hero-title-impact">Technical Training: Nanoscale Connectomics</h1>
      <p class="hero-subtitle">The canonical technical connectomics track, designed to complement the broader NeuroTrailblazers site.</p>
    </div>
  </div>

  <section class="section">
    <p>This track follows an end-to-end technical arc from motivation and imaging foundations through reconstruction, proofreading, and connectome analysis.</p>
    <div class="cta-buttons">
      <a href="{{ '/technical-training/journal-club/' | relative_url }}" class="btn btn-primary">Journal Club Reading List</a>
      <a href="{{ '/technical-training/dictionary/' | relative_url }}" class="btn btn-secondary">Connectomics Dictionary</a>
      <a href="{{ '/technical-training/slides/' | relative_url }}" class="btn btn-secondary">Technical Slide Decks</a>
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
        <h3 class="card-title"><a href="{{ '/technical-training/' | append: item.slug | append: '/' | relative_url }}">{{ item.title }}</a></h3>
        <p class="card-description">{{ item.mapping_note }}</p>
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
