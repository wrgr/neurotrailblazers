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
      <a href="{{ '/technical-training/slides/' | relative_url }}" class="btn btn-secondary">Slide Deck Drafts</a>
      <a href="{{ '/concepts/' | relative_url }}" class="btn btn-secondary">Concept Explorer</a>
    </div>
  </section>

  <section class="section">
    <div class="cards-grid">
      {% for item in site.data.technical_track.modules %}
      <article class="card">
        <h3 class="card-title"><a href="{{ '/technical-training/' | append: item.slug | append: '/' | relative_url }}">{{ item.title }}</a></h3>
        <p class="card-description">{{ item.mapping_note }}</p>
      </article>
      {% endfor %}
    </div>
  </section>
</div>
