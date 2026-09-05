---
layout: page
title: "Track: Research in Action"
permalink: /tracks/research-in-action/
slug: track-research-in-action
track: research-in-action
pathways:
  - research workflow
  - reproducibility
use_layout_hero: false
content_type: navigation
---

{% assign track = site.data.track_catalog.tracks | where: 'slug', 'research-in-action' | first %}

<div class="main-content">
  <div class="hero hero-spaced hero-rounded">
    <div class="hero-content">
      <h1 class="hero-title-impact">{{ track.title }}</h1>
      <p class="hero-subtitle">{{ track.description }}</p>
    </div>
  </div>

  <section class="section">
    <p>{{ track.about }}</p>
    <p><strong>Fadel alignment:</strong> {{ track.fadel_alignment | join: ', ' }}</p>
    <p><strong>Who this is for.</strong> Readers like <a href="{{ '/avatars/gradstudent/' | relative_url }}">Maya</a>, who has the fundamentals and now needs a defensible result, and <a href="{{ '/avatars/researcher/' | relative_url }}">Amir</a>, an AI scientist who can build the model but not yet judge whether the data supports the claim.</p>
  </section>

  {% include ui/track-sequence.html track=track %}

  {% include ui/track-modes.html track=track %}

  <section class="section">
    <h2>Modules in This Track</h2>
    <div class="arch-grid">
      {% for num in track.module_numbers %}
        {% assign mod = site.data.modules | where: 'number', num | first %}
        {% if mod %}
          {% if num < 10 %}{% assign numpad = '0' | append: num %}{% else %}{% assign numpad = num | append: '' %}{% endif %}
          <article class="arch-card" style="--accent: var(--layer-path); --accent-tint: var(--layer-path-tint);">
            <p class="arch-meta"><span class="pill pill-layer">{{ mod.stage | downcase }}</span></p>
            <h3 class="arch-title"><a href="{{ '/modules/module' | append: numpad | append: '/' | relative_url }}">{{ numpad }}. {{ mod.title }}</a></h3>
            <p class="arch-body">{{ mod.description }}</p>
          </article>
        {% endif %}
      {% endfor %}
    </div>
  </section>

  <section class="section">
    <h2>Resources</h2>
    <div class="arch-grid">
      {% for item in track.resources %}
      <article class="arch-card" style="--accent: var(--layer-path); --accent-tint: var(--layer-path-tint);">
        <h3 class="arch-title"><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
        <p class="arch-body">{{ item.summary }}</p>
      </article>
      {% endfor %}
    </div>
  </section>

  {% include ui/track-need-explorer.html
    track_slug='research-in-action'
    title='Concepts in This Track'
    intro='Filter concepts by immediate need to surface practical research resources quickly.' %}
</div>
