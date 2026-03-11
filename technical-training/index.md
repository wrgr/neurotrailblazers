---
layout: page
title: "Technical Training: Nanoscale Connectomics"
description: "Canonical open connectomics course focused on technical skills from imaging to NeuroAI."
permalink: /technical-training/
slug: technical-training
summary: "Track hub for the technical connectomics course."
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
    </div>
  </section>

  <section class="section">
    <div class="cards-grid">
      {% for item in site.data.technical_track.modules %}
      <article class="card">
        <h3 class="card-title"><a href="{{ '/technical-training/' | append: item.slug | append: '/' | relative_url }}">{{ forloop.index }}. {{ item.title }}</a></h3>
        <p class="card-description">{{ item.mapping_note }}</p>
        {% if item.mapped_modules and item.mapped_modules.size > 0 %}
        <p><strong>Current overlap:</strong>
          {% for mod in item.mapped_modules %}
            <a href="{{ '/modules/' | append: mod | append: '/' | relative_url }}">{{ mod }}</a>{% unless forloop.last %}, {% endunless %}
          {% endfor %}
        </p>
        {% endif %}
      </article>
      {% endfor %}
    </div>
  </section>
</div>
