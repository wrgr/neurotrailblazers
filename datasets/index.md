---
layout: dataset
title: "Connectomics Datasets"
description: "Eighteen public and planned connectomics datasets, from the 1986 C. elegans wiring diagram to FlyWire, H01 and MICrONS, each with what it is good for and what it does not support."
permalink: /datasets/
slug: index
track: research-in-action
pathways:
  - research workflow
  - data fluency
summary: "Landing page for curated connectomics datasets and learning pathways."
modality: "Electron microscopy and multi-modal neuroscience data"
species: "Mixed"
scale: "Multiple datasets and volumes"
access_level: "Public links and mixed access requirements"
use_cases:
  - Dataset discovery
  - Curriculum-aligned exploration
  - Comparative connectomics learning
recommended_modules:
  - module01
  - module02
  - module04
related_tools:
  - ask-an-expert
  - connectome-quality
related_frameworks:
  - research-incubator-model
  - education-models
resource_links: []
last_reviewed: 2026-03-09
maintainer: NeuroTrailblazers Team
use_layout_hero: false
content_type: core
---

<div class="main-content">
  <div class="hero hero-spaced hero-compact">
    <div class="hero-content">
      <h1 class="hero-title-impact">Connectomics Datasets</h1>
    </div>
  </div>

  <section class="section section-compact">
    <div class="card-gray text-center" style="max-width: 700px; margin: 0 auto;">
      <p><strong>Every dataset here is real, and every number on it names its source.</strong></p>
      <p>These pages collect datasets from landmark connectomics studies, among them H01, MICrONS, FlyWire and the hemibrain. Each page links the data portal and the paper, and says what the data can and cannot support.</p>
    </div>
  </section>

  <section class="section">
    <h2>Guides to working with the data</h2>
    <p>These are how-to pages, not datasets. Start here if you have chosen a volume and now
    need credentials, a client, or a pipeline.</p>
    <div class="cards-grid">
      {%- comment -%}
        Deliberately not cards/dataset-card.html: these are ordinary pages, and that include
        reads _datasets/ record fields, which page front matter does not carry.
      {%- endcomment -%}
      {% assign guides = site.pages | where_exp: "p", "p.path contains 'datasets/'" | where_exp: "p", "p.name != 'index.md'" | sort: "title" %}
      {% for guide in guides %}
      <article class="card">
        <h3 class="card-title"><a href="{{ guide.url | relative_url }}">{{ guide.title }}</a></h3>
        {% if guide.summary %}<p class="card-description">{{ guide.summary }}</p>
        {% elsif guide.description %}<p class="card-description">{{ guide.description }}</p>{% endif %}
      </article>
      {% endfor %}
    </div>
  </section>

  <section class="section">
    <h2>Featured datasets</h2>
    <p>The volumes this site teaches from. Every number below is rendered from the dataset
    record itself, so the card, the timeline and the dataset page cannot disagree.</p>
    <div class="cards-grid">
      {% assign featured = site.datasets | where: "featured", true | sort: "release_year" | reverse %}
      {% for dataset in featured %}
        {% include cards/dataset-card.html dataset=dataset %}
      {% endfor %}
    </div>
  </section>

  <section class="section">
    <h2>Connectomics timeline</h2>
    <p>Every dataset in the catalog, oldest first. Thirty-eight years separate the first complete
    nervous system (1986) from the first complete adult brain (2024).</p>
    <div class="timeline">
      {% assign chronological = site.datasets | sort: "release_year" %}
      {% for dataset in chronological %}
      <div class="timeline-item">
        <div class="timeline-year">{{ dataset.release_year }}</div>
        <div class="timeline-content">
          <h3 class="card-title"><a href="{{ dataset.url | relative_url }}">{{ dataset.title }}</a></h3>
          {% if dataset.blurb %}<p class="card-description">{{ dataset.blurb }}</p>{% endif %}
          <ul class="dataset-facts">
            {% if dataset.species %}<li><strong>Species:</strong> {{ dataset.species }}</li>{% endif %}
            {% if dataset.region %}<li><strong>Region:</strong> {{ dataset.region }}</li>{% endif %}
            {% if dataset.cells %}<li><strong>Cells:</strong> {{ dataset.cells }}</li>{% endif %}
            {% if dataset.synapses %}<li><strong>Synapses:</strong> {{ dataset.synapses }}</li>{% endif %}
            {% if dataset.modality %}<li><strong>Method:</strong> {{ dataset.modality }}</li>{% endif %}
            {% if dataset.size %}<li><strong>Size:</strong> {{ dataset.size }}</li>{% endif %}
          </ul>
          <div class="dataset-actions">
            <a href="{{ dataset.url | relative_url }}" class="btn btn-secondary">Dataset page</a>
            {% if dataset.paper_url %}<a href="{{ dataset.paper_url }}" class="btn btn-secondary" target="_blank" rel="noopener">Read paper</a>{% endif %}
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
    <p>BossDB hosts many datasets beyond these. Browse
    <a href="https://bossdb.org/projects" target="_blank" rel="noopener">bossdb.org/projects</a> for the rest.</p>
  </section>

  <section class="section">
    <h2>The datasets differ in how much of the network they contain</h2>
    <p>Before you pick a volume, decide whether your question needs a whole nervous system, a
    dense fragment, or a few traced cells. The answer rules most datasets in or out.</p>

    <div class="grid-md mt-2 mb-2">
      <div class="card-gray">
        <h3 style="color: var(--neural-blue); margin-bottom: 1rem;">Whole nervous systems or brains</h3>
        <ul style="color: #4b5563; margin: 0; line-height: 1.8;">
          <li><strong>C. elegans</strong> (White 1986; Witvliet 2021): 302 neurons, every one named</li>
          <li><strong>FlyWire</strong>: 139,255 neurons in one adult fly brain</li>
          <li><strong>BANC</strong>: a fly brain and nerve cord in one volume</li>
        </ul>
        <p style="color: #4b5563; margin-top: 0.75rem;">Nothing is cut off at the edge, so degree and motif counts are not truncation artifacts.</p>
      </div>

      <div class="card-gray">
        <h3 style="color: var(--cerebral-purple); margin-bottom: 1rem;">Dense fragments</h3>
        <ul style="color: #4b5563; margin: 0; line-height: 1.8;">
          <li><strong>H01</strong> and <strong>MICrONS</strong>: about 1 mm³ of human and mouse cortex</li>
          <li><strong>Hemibrain</strong>, <strong>MANC</strong>, <strong>FANC</strong>: large parts of a fly</li>
          <li><strong>Kasthuri 2015</strong>: about 1,500 μm³, every object traced</li>
        </ul>
        <p style="color: #4b5563; margin-top: 0.75rem;">Everything inside is reconstructed, but most mammalian neurons leave the volume.</p>
      </div>

      <div class="card-gray">
        <h3 style="color: var(--synapse-green); margin-bottom: 1rem;">Targeted or sparse reconstructions</h3>
        <ul style="color: #4b5563; margin: 0; line-height: 1.8;">
          <li><strong>Bock 2011</strong>, <strong>Lee 2016</strong>, <strong>Briggman 2011</strong>: cells chosen by their function</li>
          <li><strong>Phelps 2021</strong>: the 507 limb motor neurons</li>
          <li><strong>Larval zebrafish</strong>: myelinated axons only</li>
        </ul>
        <p style="color: #4b5563; margin-top: 0.75rem;">Built to answer one question. Reusing them for another usually means tracing more yourself.</p>
      </div>
    </div>
  </section>

  <section class="section text-center">
    <h2>Most of these datasets need no account to browse</h2>
    <p>Each dataset page links its portal and paper, and states its license where the
    provider publishes one. The two guides at the top of this page cover credentials,
    clients and notebooks. The main portals:</p>
    <div style="margin: 2rem 0;">
      <a href="https://bossdb.org/projects" class="btn btn-primary" target="_blank" rel="noopener" style="margin: 0.5rem;">Browse BossDB</a>
      <a href="https://h01-release.storage.googleapis.com/landing.html" class="btn btn-secondary" target="_blank" rel="noopener" style="margin: 0.5rem;">H01 release</a>
      <a href="https://www.microns-explorer.org/" class="btn btn-secondary" target="_blank" rel="noopener" style="margin: 0.5rem;">MICrONS Explorer</a>
      <a href="https://codex.flywire.ai/" class="btn btn-secondary" target="_blank" rel="noopener" style="margin: 0.5rem;">FlyWire Codex</a>
      <a href="https://neuprint.janelia.org/" class="btn btn-secondary" target="_blank" rel="noopener" style="margin: 0.5rem;">neuPrint</a>
    </div>
    <p>For a first analysis on real data with a pinned version, try the
    <a href="{{ '/notebooks/microns-lab/' | relative_url }}">MICrONS real-data lab</a>.</p>
  </section>
</div>
