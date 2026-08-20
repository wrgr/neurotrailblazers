---
layout: page
title: "Learning Tracks"
permalink: /tracks/
slug: learning-tracks
track: career-and-community
pathways:
  - program design
  - professional growth
summary: "Paths through the core reference material, on two axes: topic and mode of use."
content_type: navigation
use_layout_hero: false
---

<div class="main-content">
  <div class="hero hero-spaced hero-rounded">
    <div class="hero-content">
      <h1 class="hero-title-impact">Learning Tracks</h1>
      <p class="hero-subtitle">Paths through the core, on two independent axes: what you are learning, and how you are using it.</p>
    </div>
  </div>

  <section class="section">
    <h2>Core with tracks</h2>
    <p><a href="{{ '/core/' | relative_url }}"><strong>The core</strong></a> is reference material: the content library, dictionary, journal club, atlas, hidden curriculum, and datasets. It has no order, and you are not meant to finish it.</p>
    <p><strong>Tracks are paths through it.</strong> Each selects from the core, puts it in a sequence, and adds labs that end in something you have made. A track is finishable, and each track page states what "done" means as a capability rather than as a set of pages visited.</p>
    <p>Tracks are split two ways, and the two are independent:</p>
    <ul class="list-tight">
      <li><strong>Topic</strong> &mdash; three tracks, aligned to the Fadel dimensions of Knowledge, Skills, Character and Meta-learning.</li>
      <li><strong>Mode of use</strong> &mdash; whether you are working alone, running a hosted session, or inside a research programme.</li>
    </ul>
    <p>Any track can be worked in any available mode. Pick the topic below, then the mode &mdash; or the other way round, if your situation is the fixed part.</p>
  </section>

  <section class="section">
    <div class="axis-head">
      <span class="axis-eyebrow">Axis 1</span>
      <h2>Topic &mdash; what you are learning</h2>
      <p class="axis-lede">Three tracks, aligned to the Fadel dimensions. Most people should start with Core Concepts &amp; Methods and layer the others in as their practice develops.</p>
    </div>
    <div class="arch-grid">
      {% for track in site.data.track_catalog.tracks %}
      <article class="arch-card" style="--accent: var(--layer-path); --accent-tint: var(--layer-path-tint);">
        <h3 class="arch-title"><a href="{{ '/tracks/' | append: track.slug | append: '/' | relative_url }}">{{ track.title }}</a></h3>
        <p class="arch-meta">
          <span class="pill pill-layer">{{ track.fadel_alignment | join: ' + ' | downcase }}</span>
          <span class="pill pill-plain">{{ track.module_numbers | size }} modules</span>
        </p>
        <p class="arch-body">{{ track.description }}</p>
        <p class="arch-body"><small><strong>Time:</strong> {{ track.time_estimate }}</small></p>
        <p class="arch-note"><strong>Starting point:</strong> {{ track.entry_requirement }}</p>
      </article>
      {% endfor %}
    </div>
  </section>

  <section class="section">
    <div class="axis-head">
      <span class="axis-eyebrow">Axis 2</span>
      <h2>Mode of use &mdash; how you are using it</h2>
      <p class="axis-lede">The same track is a different thing depending on the situation you are in. Two modes exist today; the third is declared because the gap is real, not because it is built.</p>
    </div>
    {% include ui/mode-picker.html %}
    <p class="mt-1"><a href="{{ '/modes/' | relative_url }}">What each mode assumes, gives, and does not give &rarr;</a></p>
  </section>

  <section class="section">
    <div class="axis-head">
      <span class="axis-eyebrow">Underneath both axes</span>
      <h2>The core they draw on</h2>
      <p class="axis-lede">Every track routes through the same reference layer. If a track's sequence does not suit you, going straight to the core is a legitimate way to use this site.</p>
    </div>
    {% include ui/core-surfaces.html compact=true %}
    <p class="mt-1"><a href="{{ '/core/' | relative_url }}">How the core and the tracks fit together &rarr;</a></p>
  </section>

  <section class="section">
    <h2>If you would rather not pick a track</h2>
    <p>The tracks are a convenience, not a gate. Four routes that work as well for many people:</p>
    <div class="cta-buttons">
      <a href="{{ '/side-quests/' | relative_url }}" class="btn btn-secondary">Take a side quest</a>
      <a href="{{ '/concepts/' | relative_url }}" class="btn btn-secondary">Follow a concept instead</a>
      <a href="{{ '/technical-training/' | relative_url }}" class="btn btn-secondary">Work the technical sequence straight through</a>
      <a href="{{ '/core/' | relative_url }}" class="btn btn-secondary">Browse the core</a>
    </div>
  </section>
</div>
