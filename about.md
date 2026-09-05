---
layout: page
title: "About"
permalink: /about/
description: "What this site is, who it is for, how it fits the NIH BRAIN CONNECTS program, and how to reach us."
slug: about
---

**{{ site.tagline | default: "Mapping connections. Making connections." }}**

NeuroTrailblazers is an open curriculum and mentorship program for nanoscale
connectomics — the effort to map brains at the resolution of individual synaptic
connections. The site is the curriculum: the pages, data, decks and worksheets are
public, and anyone may teach from them.

The double meaning in the line is the point. The field maps connections between
neurons; the program makes connections between people — students, mentors and the
research programs that need them.

## What is here

- **[The technical course]({{ '/technical-training/' | relative_url }})** — the
  canonical units, from why anyone maps a brain through EM preparation, volume
  reconstruction, ultrastructure, proofreading and analysis. Each unit has worked
  examples, self-checks with answers, and a graded lab.
- **[25 curriculum modules]({{ '/modules/' | relative_url }})** — the same material
  shaped for tutorial delivery: a capability target, a concept set with misconception
  guardrails, a studio activity and a rubric.
- **[The content library]({{ '/content-library/' | relative_url }})** — the long-form
  reference layer behind the units: neuroanatomy, imaging, cell types, proofreading,
  infrastructure and case studies.
- **[Tracks]({{ '/tracks/' | relative_url }})** and **[modes of use]({{ '/modes/' | relative_url }})**
  — what you are learning, and whether you are working alone, running a hosted session,
  or training inside a lab.
- **[Journal club]({{ '/technical-training/journal-club/' | relative_url }})** — a
  2,000-paper corpus with discussion prompts, tiered so a reading group can start at 500.
- **[Teaching material]({{ '/teaching/' | relative_url }})** — facilitator guide,
  session kits, decks and worksheets for whoever is running the room.

If you have not used the site before, [Start Here]({{ '/start-here/' | relative_url }})
is the shortest route in.

## Where this sits in BRAIN CONNECTS

NeuroTrailblazers is developed as part of the
[NIH BRAIN Initiative](https://braininitiative.nih.gov/)'s **BRAIN CONNECTS** program.
It is **not** a third data coordinating center:

> **IC3 and APEX organize and expose the science. NeuroTrailblazers organizes the
> learning.**

The two BRAIN CONNECTS coordination centers this program routes learners toward are:

| Center | Award | What it coordinates |
|---|---|---|
| **IC3** — Integrative Connectomics Coordination Center | `U24NS139927` | Common pipelines, the CONNECTS Knowledge Base, cross-modal integration, common coordinate frameworks |
| **APEX** — Axonal Projectome EXchange | `U24NS140384` | Primate projectome data, multimodal axonal imaging, standards and benchmarking |

Where those centers, the Allen Institute or a CONNECTS project already publish an
authoritative resource, this site links to it and scaffolds the reasoning around it
rather than recreating it. The full map of who does what is on
[How NeuroTrailblazers fits BRAIN CONNECTS]({{ '/core/connects-ecosystem/' | relative_url }}).

Nothing on this site is an official statement of the NIH, the BRAIN Initiative, IC3 or
APEX.

## Who runs it

The site is maintained by the {{ site.author }}.

William Gray Roncal teaches the connectomics block (modules 7–9) of **EN.585.781
Frontiers in Neuroengineering**, whose lecture decks are published here.

<!--
  ============================================================================
  HUMAN INPUT REQUIRED — the only unfinished part of this page.

  This section is deliberately a stub. The repository documents exactly one
  named person in one named role (the EN.585.781 connectomics block, see
  course/decks/marp/en585781/README.md); everything else about the team is
  undocumented, and inventing names, titles, affiliations or bios would be a
  fabrication on the page a stranger reads to find out who is behind the site.

  Replace this comment with the real roster. For each person:

    - Name (as they want it published)
    - Role on NeuroTrailblazers (e.g. curriculum lead, technical units author,
      facilitator, maintainer)
    - Institutional affiliation
    - One sentence, optional: what they work on

  Also fill in, if applicable:
    - The institution(s) hosting the program
    - The BRAIN CONNECTS project NeuroTrailblazers is attached to, and its own
      award number if it has one distinct from the IC3/APEX awards above
    - Acknowledgements: contributors, reviewers, partner programs

  When names land here, add them to CITATION.cff as author entries above the
  "NeuroTrailblazers Team" entity entry.
  ============================================================================
-->

## Contact

Email <a href="mailto:{{ site.email }}">{{ site.email }}</a> for questions about using
the curriculum, running a session, partnering, or anything the site does not answer.

## Found an error?

Please tell us — the material is full of numbers, and numbers drift.

- **Something is wrong on a page:**
  [open an issue](https://github.com/{{ site.github_username }}/neurotrailblazers/issues)
  and name the page and the line. Corrections are welcome from anyone; you do not need
  to be a connectomics researcher to report that a figure caption contradicts the text.
- **You would rather not use GitHub:** email
  <a href="mailto:{{ site.email }}">{{ site.email }}</a> instead.
- **You want to fix it yourself:** see
  [CONTRIBUTING.md](https://github.com/{{ site.github_username }}/neurotrailblazers/blob/main/CONTRIBUTING.md)
  for the content standard and the validators to run first.

## Reuse

Site content is licensed **CC BY 4.0**; the code is **MIT**. Third-party figures and
electron micrographs carry their own terms. See the
[licence page]({{ '/license/' | relative_url }}) for what that means in practice.

## Cite this site

A machine-readable citation lives in
[`CITATION.cff`](https://github.com/{{ site.github_username }}/neurotrailblazers/blob/main/CITATION.cff)
at the repository root; GitHub will render a formatted citation from it. In text:

> NeuroTrailblazers Team. *NeuroTrailblazers: an open curriculum for nanoscale
> connectomics.* <{{ site.url }}/>

If you are citing one page rather than the site, add the page title and the date you
read it — pages here are revised.
