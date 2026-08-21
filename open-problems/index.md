---
layout: page
title: "Open Problems"
permalink: /open-problems/
slug: open-problems
description: "Seven open connectomics problems an undergraduate team can genuinely work on, each as a card with a concrete on-ramp: what to read, how to get the data, a calibration step, a first measurement, and how to scope the semester."
content_type: navigation
track: research-in-action
pathways:
  - research workflow
  - data fluency
use_layout_hero: false
---

## Pick a problem, take the ramp

Each card below is an open problem that passes two tests: **an undergraduate team
can make real progress in one to two semesters**, and **progress matters to the
field's scaling effort** — the NIH BRAIN CONNECTS program and projects like
[MouseConnects]({{ '/content-library/case-studies/mouseconnects-himc/' | relative_url }}).

Every card has an **on-ramp**: five ordered steps from "never touched the data"
to "scoped semester project with a named customer." Steps 1–3 are each about an
hour; step 4 is your first real measurement and may take a week. Every ramp
crosses the data barrier the same way — through
[Getting Started with Data]({{ '/datasets/getting-started/' | relative_url }}) —
and every ramp's third step is *reproducing a known number*, because calibration
comes before novelty.

The full analysis behind every card — state of the art with numbers, why
CONNECTS needs it, scoped project menus, and a worked scoping example — is in
the [deep dive]({{ '/content-library/connectomics/open-problems-undergrad/' | relative_url }}).
Not sure which card is yours? The deep dive's
[decision protocol]({{ '/content-library/connectomics/open-problems-undergrad/#choosing' | relative_url }})
is four questions; the first — *what is your team's strongest existing skill?* —
usually settles it, and each card's "Team fit" pill is the shortcut.

<div class="arch-grid">
  {% for p in site.data.open_problems.problems %}
  <article class="arch-card" style="--accent: var(--layer-path); --accent-tint: var(--layer-path-tint);">
    <span class="arch-chip" aria-hidden="true">{{ p.icon }}</span>
    <h3 class="arch-title"><a href="#onramp-{{ p.slug }}">{{ p.number }}. {{ p.title }}</a></h3>
    <p class="arch-meta"><span class="pill pill-plain">Team fit: {{ p.team }}</span><span class="pill pill-plain">{{ p.cost }}</span></p>
    <p class="arch-body">{{ p.hook }}</p>
    <p class="arch-body"><strong>Customer:</strong> {{ p.customer }}</p>
    <div class="arch-actions">
      <a href="#onramp-{{ p.slug }}" class="btn btn-primary">On-ramp</a>
      <a href="{{ '/content-library/connectomics/open-problems-undergrad/' | relative_url }}#{{ p.anchor }}" class="btn btn-secondary">Deep dive</a>
    </div>
  </article>
  {% endfor %}
</div>

## The on-ramps

An on-ramp is not the project — it is the first two weeks, made explicit so that
no team stalls at "we couldn't get the data working." Each step has a **done
when** you can check without a mentor. If a step's *done when* fails twice,
that's not a detour; it's information — bring it to
[Ask an Expert]({{ '/ask-an-expert/' | relative_url }}) with what you tried.

{% for p in site.data.open_problems.problems %}
<section class="section">
  <h3 id="onramp-{{ p.slug }}">{{ p.icon }} On-ramp {{ p.number }}: {{ p.title }}</h3>
  <p><em>{{ p.hook }}</em> &mdash; <a href="{{ '/content-library/connectomics/open-problems-undergrad/' | relative_url }}#{{ p.anchor }}">full problem statement</a>.</p>
  <ol>
    {% for step in p.onramp %}
    <li>
      <strong>{{ step.name }}.</strong> {{ step.action | markdownify | remove: '<p>' | remove: '</p>' }}
      <br><span class="pill pill-plain">Done when</span> {{ step.done }}
    </li>
    {% endfor %}
  </ol>
</section>
{% endfor %}

## After the ramp

The last step of every ramp is the same on purpose: a half-page abstract
addressed to the problem's customer, naming the **minimum reportable result** —
the deliverable you get even if the ambitious version fails. Write it in week
two, not week ten. Then work the project menu in the
[deep dive]({{ '/content-library/connectomics/open-problems-undergrad/' | relative_url }}),
and when your team needs the skills a step assumes, the
[technical course]({{ '/technical-training/' | relative_url }}) and
[modules]({{ '/modules/' | relative_url }}) are the reference layer behind all
of it.
