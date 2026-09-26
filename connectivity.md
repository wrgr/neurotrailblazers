---
layout: page
title: "Connectivity"
permalink: /connectivity/
description: >
  The neuroscience training that exists elsewhere, what each one covers that
  this site does not, and the funding routes that pay for getting there.
last_reviewed: 2026-09-15
maintainer: NeuroTrailblazers Team
content_type: core
---

{%- assign nt_total = 0 -%}
{%- for c in site.data.connectivity.categories -%}
{%- assign nt_total = nt_total | plus: c.entries.size -%}
{%- endfor -%}
Nobody should learn connectomics only from one site. This page is the map of
what else is out there: {{ nt_total }} programs, platforms and funding routes,
each with a plain statement of what it covers that NeuroTrailblazers does not.

**Where this page stops.** Three neighboring pages already cover ground that is
easy to confuse with this one, and none of them is duplicated here:

- [How we fit BRAIN CONNECTS]({{ '/core/connects-ecosystem/' | relative_url }}) — the program structure this site is funded inside, and the division of labor with IC3 and APEX.
- [Major Initiatives]({{ '/initiatives/' | relative_url }}) — the research consortia that built the field, not training.
- [Global Outreach & Citizen Science]({{ '/initiatives/outreach/' | relative_url }}) — EyeWire, crowdsourced mapping, and public participation.

This page is only about **training you can go and do**, and what funds it.

## How to choose between these

Which one is right depends on what you have already finished here.

| If you have… | Go to |
|---|---|
| Finished the fly material and want more of it | FlyWire Academy — same data, more practice |
| Finished the [technical units]({{ '/technical-training/' | relative_url }}) and want modeling depth | Neuromatch Academy |
| Finished the units and want bench or circuit-physiology skill | CAJAL, MBL or CSHL |
| To teach this material to undergraduates | The Allen Institute educators' workshop, then compare with the [session kits]({{ '/teaching/sessions/' | relative_url }}) |
| No budget and no application window | INCF TrainingSpace and SfN Neuronline |
| A plan but no money | The funding section below |

{% for category in site.data.connectivity.categories %}
## {{ category.title }} {#{{ category.id }}}

{{ category.intro }}

<div class="arch-grid">
{%- for e in category.entries %}
  <article class="arch-card">
    <h3 class="arch-title"><a href="{{ e.url }}" target="_blank" rel="noopener">{{ e.name }}</a></h3>
    <p class="arch-meta"><span class="pill pill-layer">{{ e.org }}</span><span class="pill pill-plain">{{ e.cadence }}</span></p>
    <p class="arch-body">{{ e.note }}</p>
    <p class="arch-body">
      <strong>Who it is for:</strong> {{ e.audience }}<br>
      <strong>Format:</strong> {{ e.format }}<br>
      <strong>Cost:</strong> {{ e.cost }}
    </p>
    <p class="arch-note"><strong>Next to this site:</strong> {{ e.boundary }}</p>
    <p class="arch-meta"><span class="pill pill-plain">Checked {{ e.verified | date: "%-d %B %Y" }}</span></p>
  </article>
{%- endfor %}
</div>
{% endfor %}

## What this page does not cover

- **Conferences and meetings.** SfN, COSYNE and OHBM matter for dissemination, but a list of annual meetings goes stale faster than it is useful and every society publishes its own calendar.
- **Dates and deadlines.** Deliberately absent from `_data/connectivity.yml`. Each entry says when to look; the link says the rest.
- **Programs we have not checked.** Every entry above was verified against the provider's own site on the date shown on its card. Anything we could not confirm is not listed.
- **Any judgment of quality.** These are the programs a connectomics learner is most likely to need. Being listed is not a recommendation over something absent.

## Suggest an addition

If you run relevant training, or know of something that belongs here, open an
issue on [the repository](https://github.com/{{ site.github_username }}/neurotrailblazers/issues)
or email [{{ site.email }}](mailto:{{ site.email }}). Include a link to the
provider's own page describing it; that is what gets checked before anything is
added.
