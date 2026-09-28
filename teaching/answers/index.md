---
layout: page
title: "Module model responses"
permalink: /teaching/answers/
slug: module-answers-index
content_type: delivery
description: "Public formative model responses for the module session kits, the order in which the remaining keys will be written, and how to use them."
---

These pages give worked responses to the module session kits' learner worksheets.
Each one answers every section of its worksheet in order, lists common misconceptions
with feedback, and scores against the kit's own rubric tiers.

## Available keys

{%- comment -%}
  One row per key page under teaching/answers/, in module order, so a new key
  appears here as soon as it exists. Titles come from _data/modules.yml.
{%- endcomment -%}
{%- assign module_keys = site.pages | where_exp: 'p', "p.url contains '/teaching/answers/module'" | sort: 'url' %}

| Module | Worksheet | Key |
|---|---|---|
{%- for k in module_keys %}
{%- assign numpad = k.url | remove: '/teaching/answers/module' | remove: '/' %}
{%- assign num = numpad | plus: 0 %}
{%- assign m = site.data.modules | where: 'number', num | first %}
| {{ numpad }}: {{ m.title }} | [Worksheet]({{ '/assets/worksheets/module' | append: numpad | append: '/module' | append: numpad | append: '-activity.md' | relative_url }}) | [Model responses]({{ k.url | relative_url }}) |
{%- endfor %}

The four connectomics lectures and the Ethics and Governance session have their own
keys, linked from the [lecture series]({{ '/teaching/lectures/' | relative_url }}) and
from each session on the [short lecture series]({{ '/teaching/sequence/' | relative_url }})
page. A separate [assessment bank]({{ '/teaching/assessment/' | relative_url }}) covers the
four lecture outcomes, and the
[unit assessments]({{ '/teaching/assessment/units/' | relative_url }}) cover the nine
technical units.

## Backlog order

Eleven module keys exist: 01, 07 and 18, plus every module the
[16-week syllabus map]({{ '/teaching/syllabi/16-week/' | relative_url }}) schedules
(02, 08, 17, 19, 20, 21, 22, 25). Fourteen remain. They will be written in
module-number order: 03, 04, 05, 06, 09, 10, 11, 12, 13, 14, 15, 16, 23, 24.

Where the site publishes a synthetic kit folder under `assets/kits/` (Modules 03, 06, 09,
10, 11, 12, 13, 14, 16 and 19 in these lists), the key will work from those files, as the
Module 07 and 18 keys do. Modules 04 and 05 use a patch set the instructor builds, so
their keys will give the reasoning for each step plus a clearly labeled invented example.

## Use policy

- **Public and formative.** Every key here is published. Learners can read it after
  attempting the worksheet. Use the keys for feedback, self-assessment and revision.
- **Not secure exam material.** Anything graded for a course grade under exam
  conditions needs new items that are not on this site. The assessment bank gives
  variant templates for that purpose.
- **Examples, not the only answer.** Where a worksheet asks for a learner's own question
  or data, the key shows one invented learner's work at the kit's Strong level.
- **Invented values are labeled.** Where a kit works from an instructor-built patch set
  or a learner's own question, every number the key adds is marked as invented.
- **Local rubrics.** Each key uses the kit's own Minimum and Strong tiers. These are
  local teaching rubrics, not validated assessment or calibration instruments, and
  should not be reported as such.

[Session kits]({{ '/teaching/sessions/' | relative_url }}) · [Facilitator guide]({{ '/teaching/facilitator-guide/' | relative_url }}) · [Teaching Hub]({{ '/teaching/' | relative_url }})

Teaching material: CC BY 4.0, NeuroTrailblazers.
