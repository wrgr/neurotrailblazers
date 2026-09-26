---
layout: tool
title: "Tools"
description: "What runs in the browser on this site, what you will run elsewhere, and where to ask a person when neither helps."
permalink: /tools/
slug: index
track: research-in-action
pathways:
  - research workflow
  - mentoring
summary: "The site's own interactives, the third-party software you will actually run, and how to get help."
use_cases:
  - Finding the right tool for a pipeline stage
  - Exploring the literature without an install
  - Quality-control practice
recommended_modules: []
related_datasets: []
last_reviewed: 2026-09-07
maintainer: NeuroTrailblazers Team
use_layout_hero: false
content_type: core
---

<div class="main-content">
  <div class="hero hero-spaced hero-rounded">
    <div class="hero-content">
      <h1 class="hero-title-impact">Tools</h1>
      <p class="hero-subtitle">What runs here, what you will run elsewhere, and who to ask when neither helps.</p>
    </div>
  </div>

  <section class="section">
    <p>Find browser interactives, specialist software, and help.</p>
    <p><strong>The interactives on this site</strong> run in the browser, here, with no account
    and no install. They are for exploring the literature and practising judgement, not for
    analysing your own data.</p>
    <p><strong>The software you will actually run</strong> &mdash; Neuroglancer, CAVE and
    <code>caveclient</code>, CloudVolume, neuPrint, CATMAID, webKnossos, <code>navis</code>,
    <code>graspologic</code>, DotMotif, BossDB &mdash; is third-party. It is cataloged by
    workflow stage in the
    <a href="{{ '/technical-training/atlas-connectomics-reference/' | relative_url }}">connectomics atlas</a>,
    with what each one does and where it fits; credentials, clients and starter notebooks are in
    the <a href="{{ '/datasets/access/' | relative_url }}">dataset access guide</a>. If you are
    working out <em>which</em> tool you need rather than how to drive one you have chosen, the
    atlas table is the faster route: it is organized by the stage of the pipeline you are
    standing in.</p>
    <p><strong>Help</strong> is the third thing, and it is at the bottom of this page.</p>
  </section>

  <section class="section">
    <h2 class="section-title left">Interactive on this site</h2>
    <ul>
      <li><a href="{{ '/technical-training/journal-club/graph/' | relative_url }}">Citation graph explorer</a> &mdash; the 2,000-paper corpus as a citation network, filterable by dimension, era and tier.</li>
      <li><a href="{{ '/technical-training/journal-club/' | relative_url }}">Journal club</a> &mdash; the same corpus as cards, each with an OCAR summary and discussion prompts.</li>
      <li><a href="{{ '/concepts/' | relative_url }}">Concept explorer</a> &mdash; concepts filtered by track and stage, each linked to where it is taught.</li>
      <li><a href="{{ '/kb/' | relative_url }}">The field, mapped</a> &mdash; visualisations of the literature and the methods landscape.</li>
      <li><a href="{{ '/technical-training/dictionary/' | relative_url }}">Connectomics dictionary</a> &mdash; 127 terms, with definitions, common confusions, and typical values where applicable.</li>
      <li><a href="{{ '/modules/' | relative_url }}">Module practice labs</a> &mdash; the retrieval-practice check at the foot of each module page.</li>
      <li><a href="{{ '/neuronauts/kids/' | relative_url }}">Junior Lab quiz</a> &mdash; for younger readers and classrooms.</li>
    </ul>
  </section>

  <section class="section">
    <h2 class="section-title left">Practice</h2>
    <p>Scaffolded exercises rather than software: you bring judgement, the page supplies the
    cases and the criteria.</p>
    <div class="cards-grid">
      {% assign sorted_pages = site.pages | sort: "title" %}
      {% for tool in sorted_pages %}
        {% if tool.path contains 'tools/' and tool.layout == 'tool' and tool.name != 'index.md' and tool.name != 'ask-an-expert.md' and tool.url and tool.url != '' %}
          {% include cards/tool-card.html tool=tool %}
        {% endif %}
      {% endfor %}
    </div>
  </section>

  <section class="section">
    <h2 class="section-title left">Getting help</h2>
    <p>Two routes, and they are not equivalent. Start with the one that fits the question.</p>
    <ul>
      <li><strong><a href="{{ '/ask-an-expert/' | relative_url }}">Ask an Expert</a></strong> &mdash;
      a curated AI chatbot built on Dr. Jeff Lichtman's public materials, for concept questions and
      exploratory guidance. It is not Dr. Lichtman, it does not reflect his current views, and it
      needs a ChatGPT account. Check anything load-bearing against the primary literature.</li>
      <li><strong>A person.</strong> For questions about using the curriculum, running a session,
      partnering, or anything the site does not answer, email
      <a href="mailto:{{ site.email }}">{{ site.email }}</a>. If a page here is wrong, say so:
      <a href="https://github.com/{{ site.github_username }}/neurotrailblazers/issues">open an issue</a>
      naming the page and the line, or email the same address. The
      <a href="{{ '/about/#contact' | relative_url }}">about page</a> has the full contact and
      corrections routes.</li>
    </ul>
  </section>

</div>
