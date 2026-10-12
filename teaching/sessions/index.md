---
layout: page
title: "Session plans"
description: "Find preparation, timing, slides, activities, and assessment guidance for each module."
permalink: /teaching/sessions/
slug: session-kits
track: career-and-community
content_type: delivery
pathways:
  - classroom delivery
  - mentor support
---

Choose a module to open its session plan. Check its development status, then review the preparation, slides, worksheet, and assessment criteria before teaching.

For help adapting a session to your group, read the [Facilitator Guide]({{ '/teaching/facilitator-guide/' | relative_url }}).

For other audiences, try the [public-engagement session]({{ '/teaching/module22-public-engagement/' | relative_url }}) or [From Projectome to Synapse]({{ '/teaching/projectome-to-synapse/' | relative_url }}), a 25–40 minute hands-on activity.

<div class="cards-grid">
{% assign kits = site.pages | where_exp: 'p', "p.path contains 'teaching/sessions/module'" | sort: 'path' %}
{% for p in kits %}
  <article class="card">
    {% include ui/module-status.html item=p %}
    <h3 class="card-title"><a href="{{ p.url | relative_url }}">{{ p.title | remove: 'Session Kit: ' }}</a></h3>
    <p class="card-description">{{ p.description }}</p>
  </article>
{% endfor %}
</div>
