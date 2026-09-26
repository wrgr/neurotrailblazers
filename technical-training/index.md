---
layout: page
title: "Technical Course"
description: "Nine ordered units in nanoscale connectomics, from tissue preparation and EM imaging to proofreading and connectome analysis."
permalink: /technical-training/
slug: technical-training
summary: "Hub for the Technical Course: the nine units, in order."
track: core-concepts-methods
pathways:
  - technical foundation
  - methods depth
last_reviewed: 2026-09-26
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
    <p>The nine units are ordered and cumulative. Each one ends in an exercise you hand in. Together they form the spine of the <a href="{{ '/tracks/core-concepts-methods/' | relative_url }}">Core Concepts &amp; Methods</a> track.</p>
    <p>The <a href="{{ '/technical-training/atlas-connectomics-reference/' | relative_url }}">atlas</a> sits beside the units as reference. You consult it; you do not complete it. The rest of the reference material the units draw on (dictionary, content library, journal club, hidden curriculum) is in <a href="{{ '/core/' | relative_url }}">the core</a>, and can be read in any order.</p>
    <p>Working through the units alone is <a href="{{ '/modes/#self-study' | relative_url }}">self-study mode</a>. If you are teaching a group, the <a href="{{ '/modules/' | relative_url }}">modules</a> cover the same material as tutorials, and each has a <a href="{{ '/teaching/sessions/' | relative_url }}">session kit</a> for <a href="{{ '/modes/#hosted-workshop' | relative_url }}">hosted-workshop mode</a>.</p>
    <div class="cta-buttons">
      <a href="{{ '/technical-training/01-why-map-the-brain/' | relative_url }}" class="btn btn-primary">Start Unit 1: Why Map the Brain</a>
      <a href="{{ '/technical-training/journal-club/' | relative_url }}" class="btn btn-secondary">Journal Club Reading List</a>
      <a href="{{ '/technical-training/dictionary/' | relative_url }}" class="btn btn-secondary">Connectomics Dictionary</a>
      <a href="{{ '/technical-training/slides/' | relative_url }}" class="btn btn-secondary">Presentation Decks</a>
      <a href="{{ '/technical-training/proofreading-tutorials/' | relative_url }}" class="btn btn-secondary">Proofreading Tutorials</a>
      <a href="{{ '/teaching/' | relative_url }}" class="btn btn-secondary">Teaching Hub</a>
      <a href="{{ '/concepts/' | relative_url }}" class="btn btn-secondary">Concept Explorer</a>
    </div>
  </section>

  <section class="section">
    <h2>If you need one skill now, start from the need</h2>
    <p>Each button opens the Concept Explorer filtered to the concepts that serve that need. You skip the sequence this way, so a concept may assume a unit you have not read. Each card's title links to the page that teaches it.</p>
    <div class="cta-buttons">
      <a href="{{ concepts_base }}?track=core-concepts-methods&need=starting%20a%20research%20question" class="btn btn-secondary">Start a Research Question</a>
      <a href="{{ concepts_base }}?track=core-concepts-methods&need=improving%20data%20quality" class="btn btn-secondary">Improve Data Quality</a>
      <a href="{{ concepts_base }}?track=core-concepts-methods&need=reducing%20identity%20confusion" class="btn btn-secondary">Classify Axons vs Dendrites</a>
      <a href="{{ concepts_base }}?track=research-in-action&need=prioritizing%20corrections" class="btn btn-secondary">Prioritize Proofreading</a>
      <a href="{{ concepts_base }}?track=research-in-action&need=designing%20graph%20analyses" class="btn btn-secondary">Design Graph Analyses</a>
    </div>
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
    <h2>All nine units take about {{ course_hours }} hours on your own</h2>
    <p>That total covers reading and the graded exercises, summed from the times on the cards
    below. Each unit page also gives the length of a taught session and of its slide deck.
    The atlas is last in the grid and is not in the total, because it is reference.</p>
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
