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

Choose a module to open its session plan. Lesson pages, slides, worksheets, and teaching guidance are available. Status labels distinguish materials with interactive practice still in development from those whose overall readiness has not yet been reviewed. Review the preparation, activities, and assessment criteria before teaching.

For help adapting a session to your group, read the [Facilitator Guide]({{ '/teaching/facilitator-guide/' | relative_url }}).

For other audiences, try the [public-engagement session]({{ '/teaching/module22-public-engagement/' | relative_url }}) or [From Projectome to Synapse]({{ '/teaching/projectome-to-synapse/' | relative_url }}), a 25–40 minute hands-on activity.

<div class="resource-search"><label for="session-search">Find a session by topic</label><input type="search" id="session-search" placeholder="e.g. synapse, Python, research" aria-controls="session-results"><label for="session-status">Materials and practice status</label><select id="session-status"><option value="all">All statuses</option><option value="available">Materials available</option><option value="in_development">Practice in development</option><option value="unreviewed">Readiness unreviewed</option></select><p id="session-count" role="status" aria-live="polite"></p></div>
<div class="cards-grid" id="session-results">
{% assign kits = site.pages | where_exp: 'p', "p.path contains 'teaching/sessions/module'" | sort: 'path' %}
{% for p in kits %}
  {% include ui/module-status-value.html item=p %}
  <article class="card session-card" data-status="{{ module_state }}">
    {% include ui/module-status.html item=p %}
    <h3 class="card-title"><a href="{{ p.url | relative_url }}">{{ p.title | remove: 'Session Kit: ' }}</a></h3>
    <p class="card-description">{{ p.description }}</p>
  </article>
{% endfor %}
</div>
