---
layout: page
title: "Connectomics course"
description: "Nine lessons with worked examples and exercises, from brain mapping to connectome analysis."
permalink: /technical-training/
slug: technical-training
summary: "Hub for the Connectomics course: the nine units, in order."
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
      <h1 class="hero-title-impact">Connectomics course</h1>
      <p class="hero-subtitle">Nine lessons in nanoscale connectomics, from why we map the brain through imaging, reconstruction, proofreading and analysis. Each includes a worked example and an exercise.</p>
    </div>
  </div>

  <section class="section">
    <p>Start with lesson 1 and continue in order. Each lesson includes a worked example and an exercise to check your understanding. Use the dictionary and reference atlas whenever you need them.</p>
    <div class="cta-buttons"><a href="{{ '/technical-training/01-why-map-the-brain/' | relative_url }}" class="btn btn-primary">Start lesson 1: Why map the brain</a><a href="{{ '/technical-training/slides/' | relative_url }}" class="btn btn-secondary">Open slides</a></div>
    <p>Learning a specific skill? <a href="{{ '/technical-training/proofreading-tutorials/' | relative_url }}">Try proofreading</a>. Teaching a group? <a href="{{ '/teaching/' | relative_url }}">Find lesson plans</a>.</p>
  </section>

  {%- comment -%}
    The course total is summed from each unit's `time_estimate` front matter
    ("N minutes|hours reading + M minute|hour <exercise>"), the same values the
    cards show, so the total cannot drift from them. validate_technical_evidence.rb
    fails if a unit's time_estimate stops matching that pattern.
  {%- endcomment -%}
  {%- assign course_minutes = 0 -%}
  {%- for item in site.data.technical_track.modules -%}
    {%- assign unit_page = site.pages | where: "slug", item.slug | first -%}
    {%- if unit_page.content_type == 'path' -%}
      {%- assign estimate_parts = unit_page.time_estimate | split: ' + ' -%}
      {%- for part in estimate_parts -%}
        {%- assign words = part | split: ' ' -%}
        {%- assign part_minutes = words[0] | plus: 0 -%}
        {%- if words[1] contains 'hour' -%}{%- assign part_minutes = part_minutes | times: 60 -%}{%- endif -%}
        {%- assign course_minutes = course_minutes | plus: part_minutes -%}
      {%- endfor -%}
    {%- endif -%}
  {%- endfor -%}
  {%- assign course_hours = course_minutes | divided_by: 60.0 | round -%}
  <section class="section">
    <h2>Choose a lesson</h2>
    <p>Allow about <strong>{{ course_hours }} hours</strong> for all nine lessons and their exercises. Each card gives its own time estimate and prerequisites. The atlas is a reference to consult as you go.</p>
    {% assign concept_items = site.data.concepts.concepts %}
    <div class="cards-grid">
      {% for item in site.data.technical_track.modules %}
      {% assign first_concept_slug = item.primary_concepts | first %}
      {% assign first_concept = concept_items | where: 'slug', first_concept_slug | first %}
      {% assign primary_need = item.user_needs | first %}
      <article class="card">
        <img class="module-thumb" src="{{ '/assets/images/units/' | append: item.slug | append: '.svg' | relative_url }}" alt="" aria-hidden="true" loading="lazy" width="1200" height="420">
        {% if item.slug == 'atlas-connectomics-reference' %}<p class="pill-reference">Reference &mdash; consult, do not complete</p>{% endif %}
        <h3 class="card-title"><a href="{{ '/technical-training/' | append: item.slug | append: '/' | relative_url }}">{{ item.title }}</a></h3>
        <p class="card-description">{{ item.summary | default: item.mapping_note }}</p>
        {%- comment -%}
          Time, level and prerequisites live in each unit page's front matter, not in
          technical_track.yml, so look the page up by its slug rather than duplicating
          the values into a second file where they would drift.
        {%- endcomment -%}
        {% assign unit_page = site.pages | where: "slug", item.slug | first %}
        {% if unit_page %}
        <p class="unit-meta">
          {% if unit_page.time_estimate %}<span>{{ unit_page.time_estimate }}</span>{% endif %}
          {% if unit_page.level %}<span>{{ unit_page.level }}</span>{% endif %}
        </p>
        {% if unit_page.prerequisites %}<p><small>Prerequisites: {{ unit_page.prerequisites }}</small></p>{% endif %}
        {% endif %}
      </article>
      {% endfor %}
    </div>
  </section>
<details class="secondary-options"><summary>Choose concepts by your current task</summary>  <section class="section">
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

</details>
</div>
