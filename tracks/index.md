---
layout: page
title: "Learning paths"
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
<section class="hero hero-spaced hero-rounded"><div class="hero-content"><h1>Learning paths</h1><p>Start with the connectomics course, or choose a path for the work you want to do.</p></div></section>
<section class="section"><h2>Recommended for new learners</h2><article class="card"><h3>Nine-lesson connectomics course</h3><p>Learn why we map the brain, how images become reconstructions, and how to interpret the results. Each lesson has examples and an exercise.</p><div class="cta-buttons"><a class="btn btn-primary" href="{{ '/technical-training/01-why-map-the-brain/' | relative_url }}">Begin with Why Map the Brain</a><a class="btn btn-secondary" href="{{ '/technical-training/' | relative_url }}">See the course</a></div></article></section>
<section class="section"><h2>Paths for a longer program</h2><p>These paths combine lessons with research and professional practice. Choose one that fits your goal.</p><div class="cards-grid">
{% for track in site.data.track_catalog.tracks %}<article class="card"><h3><a href="{{ '/tracks/' | append: track.slug | append: '/' | relative_url }}">{{ track.title }}</a></h3><p>{{ track.description }}</p><p><strong>Time:</strong> {{ track.time_estimate }}</p><p><strong>Starting point:</strong> {{ track.entry_requirement }}</p><a href="{{ '/tracks/' | append: track.slug | append: '/' | relative_url }}">See the sequence →</a></article>{% endfor %}
</div></section>
<section class="section"><h2>Prefer one topic?</h2><p>Browse <a href="{{ '/modules/' | relative_url }}">topic modules</a>, practise <a href="{{ '/side-quests/proofreading/' | relative_url }}">proofreading</a>, or use <a href="{{ '/resources/' | relative_url }}">reference resources</a> for a question you have now.</p></section>
<details class="secondary-options"><summary>Study on your own or teach a group</summary><p>You can work through lessons at your own pace. To run a group session, use the <a href="{{ '/teaching/' | relative_url }}">teaching materials</a> and check each module’s status.</p>{% include ui/mode-picker.html %}<p><a href="{{ '/modes/' | relative_url }}">Details about study and workshop options</a></p></details>
</div>
