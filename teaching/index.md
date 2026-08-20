---
layout: page
title: "Teaching Hub"
description: "Instructor-ready lesson kits with module content, rendered slides, source decks, and worksheets."
permalink: /teaching/
slug: teaching-hub
track: career-and-community
pathways:
  - classroom delivery
  - mentor support
summary: "Central hub for teaching materials across all modules."
use_layout_hero: false
content_type: delivery
---

<div class="main-content">
  <div class="hero hero-spaced hero-rounded">
    <div class="hero-content">
      <h1 class="hero-title-impact">Teaching Hub</h1>
      <p class="hero-subtitle">Everything needed to teach each module: lesson flow, activities, slides, and worksheets.</p>
    </div>
  </div>

  <section class="section">
    <div class="cta-buttons">
      <a href="{{ '/teaching/sessions/' | relative_url }}" class="btn btn-primary">Session Kits — run a session</a>
      <a href="{{ '/modules/' | relative_url }}" class="btn btn-secondary">Open Module Library</a>
      <a href="{{ '/modules/slides/' | relative_url }}" class="btn btn-secondary">Browse Slide Pages</a>
      <a href="{{ '/teaching/facilitator-guide/' | relative_url }}" class="btn btn-secondary">Facilitator Guide</a>
      <a href="{{ '/technical-training/' | relative_url }}" class="btn btn-secondary">Technical Course Hub</a>
    </div>
  </section>

  <section class="section">
    <h2>Where this sits</h2>
    <p>This is <strong>delivery material</strong>: written for whoever is running a session, not for whoever is learning. It is the <a href="{{ '/modes/#hosted-workshop' | relative_url }}">hosted-workshop mode</a> of the same curriculum that <a href="{{ '/modes/#self-study' | relative_url }}">self-study</a> learners read directly.</p>
    <p>Nothing here is a separate body of content. Session kits are generated from the module pages, and the depth behind every activity lives in <a href="{{ '/core/' | relative_url }}">the core</a> &mdash; the content library, dictionary, journal club, atlas and hidden curriculum. If a learner asks a question a kit does not answer, the core is where you look.</p>
  </section>

  <section class="section">
    <h2>Two ways in</h2>
    <p><strong>Running a session?</strong> Go to the
      <a href="{{ '/teaching/sessions/' | relative_url }}">session kits</a>. Each is one
      page holding the prep checklist, run of show, materials, misconceptions to target,
      and rubric for a single module — assembled from pieces that used to live in five
      different places.</p>
    <p><strong>Designing a course, or wondering why the sessions are shaped this way?</strong>
      Start with the <a href="{{ '/teaching/facilitator-guide/' | relative_url }}">Facilitator Guide</a>.
      It covers why at least half of contact time has to be learner judgement rather than
      explanation, how to differentiate across the four learner personas, and how to
      assess calibration rather than raw accuracy.</p>
  </section>

  <section class="section">
    <h2>Module Teaching Kits</h2>
    <p>Each card links to the lesson page, rendered slide deck, editable source, and activity worksheet.</p>
    <div class="cards-grid">
      {% assign module_pages = site.modules | sort: "module_number" %}
      {% for module in module_pages %}
        {% include cards/teaching-module-card.html module=module %}
      {% endfor %}
    </div>
  </section>
</div>
