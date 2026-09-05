---
layout: dataset
title: "Connectomics Datasets - Learning with Real Scientific Data"
description: "Explore curated connectomics datasets from landmark studies including H01, MICrONS, FlyWire, Hemibrain, and more. Learn with the same data used by leading researchers."
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
      <p><strong>Learn with real scientific data from groundbreaking research.</strong></p>
      <p>These pages collect datasets from landmark connectomics studies &mdash; H01, MICrONS, FlyWire, the hemibrain, and others &mdash; with links to the data portals, the papers behind them, and the site material that uses each one.</p>
    </div>
  </section>

  {% include ui/learning-tracks.html title="How Datasets Fit the Tracks" intro="Datasets power all three tracks: concept-building, hands-on research practice, and professional growth through authentic scientific context." %}

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
    <p>Every dataset in the catalogue, oldest first. Forty years separate the first complete
    nervous system from the first complete adult brain.</p>
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
    <h2>Dataset Categories</h2>
    <p>Connectomics datasets vary in scope, species, and methodology. Understanding these categories helps you choose the right data for your learning goals.</p>

    <div class="grid-md mt-2 mb-2">
      <div class="card-gray">
        <h3 style="color: var(--neural-blue); margin-bottom: 1rem;">By Species</h3>
        <ul style="color: #4b5563; margin: 0; line-height: 1.8;">
          <li><strong>C. elegans:</strong> Simple, complete nervous system (302 neurons)</li>
          <li><strong>Drosophila:</strong> Complex invertebrate brain (~140,000 neurons)</li>
          <li><strong>Mouse:</strong> Mammalian cortical circuits (thousands to millions of neurons)</li>
          <li><strong>Human:</strong> Cortical samples (tens of thousands of neurons)</li>
        </ul>
      </div>

      <div class="card-gray">
        <h3 style="color: var(--cerebral-purple); margin-bottom: 1rem;">By Resolution</h3>
        <ul style="color: #4b5563; margin: 0; line-height: 1.8;">
          <li><strong>Synaptic:</strong> Individual synapses and connections</li>
          <li><strong>Cellular:</strong> Complete neuronal morphologies</li>
          <li><strong>Circuit:</strong> Functional neural networks</li>
          <li><strong>Regional:</strong> Large-scale brain organization</li>
        </ul>
      </div>

      <div class="card-gray">
        <h3 style="color: var(--synapse-green); margin-bottom: 1rem;">By Data Type</h3>
        <ul style="color: #4b5563; margin: 0; line-height: 1.8;">
          <li><strong>Structural:</strong> Electron microscopy-based anatomy</li>
          <li><strong>Functional:</strong> Calcium imaging or electrophysiology</li>
          <li><strong>Multimodal:</strong> Combined structural and functional data</li>
          <li><strong>Comparative:</strong> Multiple species or conditions</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section text-center">
    <h2>Accessing These Datasets</h2>
    <p>Most datasets are freely available through dedicated platforms. Each dataset entry above includes direct links to data portals, original publications, and popular press coverage where available.</p>
    <div class="flex-center mt-2">

    <div class="dataset-card featured spotlight" style="text-align: left; margin: 2rem auto; max-width: 600px;">
      <div class="dataset-header">
        <h3><a href="{{ '/datasets/getting-started' | relative_url }}">Getting Started with Data</a></h3>
        <div class="dataset-meta">
          <span class="dataset-type">Start here</span>
          <span class="dataset-status">Onboarding</span>
        </div>
      </div>
      <p>The gap between "the data is public" and "I have a DataFrame" is where most new teams stall. This guide closes it: a four-level ladder from browser to imagery cutouts, the CAVE token walkthrough start to finish, version pinning, byte math, and a failure-signature table for when it breaks.</p>
      <div class="dataset-actions">
        <a href="{{ '/datasets/getting-started' | relative_url }}" class="btn btn-primary">Take the Ladder</a>
        <a href="{{ '/open-problems/' | relative_url }}" class="btn btn-secondary">Open Problems On-Ramps</a>
      </div>
    </div>

    <div class="dataset-card featured spotlight" style="text-align: left; margin: 2rem auto; max-width: 600px;">
      <div class="dataset-header">
        <h3><a href="{{ '/datasets/access' | relative_url }}">Accessing Public EM Datasets</a></h3>
        <div class="dataset-meta">
          <span class="dataset-type">Tutorials</span>
          <span class="dataset-status">Resources</span>
        </div>
      </div>
      <p>Curated example notebooks for downloading connectomics data from Google, the Allen Institute, Janelia, and bossDB — the notebook collection behind the getting-started ladder.</p>
      <div class="dataset-actions">
        <a href="{{ '/datasets/access' | relative_url }}" class="btn btn-primary">View Notebooks</a>
      </div>
    </div>

    <div style="margin: 2rem 0;">
      <a href="https://bossdb.org/projects" class="btn btn-primary" target="_blank" style="margin: 0.5rem;">Browse BossDB</a>
      <a href="https://h01-release.storage.googleapis.com/" class="btn btn-secondary" target="_blank" style="margin: 0.5rem;">H01 Portal</a>
      <a href="https://www.microns-explorer.org/" class="btn btn-secondary" target="_blank" style="margin: 0.5rem;">MICrONS Explorer</a>
      <a href="https://flywire.ai/" class="btn btn-secondary" target="_blank" style="margin: 0.5rem;">FlyWire Codex</a>
    </div>
</div>
  </section>
</div>
