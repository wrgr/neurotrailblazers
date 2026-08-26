---
layout: page
title: "Session Kits"
description: "One ready-to-run page per module: prep checklist, timing, materials, misconceptions, rubric."
permalink: /teaching/sessions/
slug: session-kits
track: career-and-community
content_type: delivery
pathways:
  - classroom delivery
  - mentor support
---

Each kit is the single page to open ten minutes before walking in. Everything in it
already existed — capability target, run of show, worksheet, rubric, rendered deck —
but was spread across five locations. These assemble it.

Kits are generated from the module pages. To change one, edit
`modules/moduleNN.md` and re-run `scripts/generate_module_teaching_materials.rb`.

For the reasoning behind the session design — why half of contact time should be
learner judgment rather than explanation, how to differentiate across the learner
personas, and what to do when a session goes wrong — see the
[Facilitator Guide]({{ '/teaching/facilitator-guide/' | relative_url }}).

<div class="cards-grid">
{% assign kits = site.pages | where_exp: 'p', "p.path contains 'teaching/sessions/module'" | sort: 'path' %}
{% for p in kits %}
  <article class="card">
    <h3 class="card-title"><a href="{{ p.url | relative_url }}">{{ p.title | remove: 'Session Kit: ' }}</a></h3>
    <p class="card-description">{{ p.description }}</p>
  </article>
{% endfor %}
</div>
