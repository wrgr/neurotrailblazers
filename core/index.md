---
layout: page
title: "The Core"
description: "The reference layer: everything the tracks draw on. Consult it, rather than working through it."
permalink: /core/
slug: core-reference
content_type: navigation
track: core-concepts-methods
pathways:
  - technical foundation
  - methods depth
---

## Core with tracks

This site has two layers, and confusing them is the fastest way to get lost in it.

**The core is reference.** Six bodies of material, written to be looked things up
in: definitions, worked methods, papers with the argument stated, the norms nobody
writes down. It has no order. You are not meant to finish it, and a page that says
"next" is a page that has drifted out of the core.

**Tracks are paths through the core.** Each one selects from this material, puts it
in an order, and adds labs that produce something. Three of them exist, split by
topic. A track is finishable; the core is not.

**Modes are how you walk a track** &mdash; alone, in a hosted session, or (eventually)
inside a research programme. The mode axis is independent of the topic axis: any
track can be worked in any available mode.

So: *what* you are learning is the track, *how* you are using it is the mode, and
*what it is built out of* is this page.

<div class="cta-buttons">
  <a href="{{ '/tracks/' | relative_url }}" class="btn btn-primary">Pick a track</a>
  <a href="{{ '/start-here/' | relative_url }}" class="btn btn-secondary">Pick a mode</a>
</div>

## What is in the core

{% include ui/core-surfaces.html %}

## When to reach for which

The failure mode this layer exists to prevent is reading a reference document
front to back because it appeared in a list. Here is what each surface is
actually for.

| You are... | Go to | Not to |
|---|---|---|
| Stopped by a word | [Dictionary]({{ '/technical-training/dictionary/' | relative_url }}) | A unit. A large share of apparent difficulty in this field is vocabulary, and it is fixable in about a week. |
| Trying to do a specific technical thing | [Content library]({{ '/content-library/' | relative_url }}) | The module that mentions it. The library entry is the depth; the module is the session. |
| Checking a number, a scale, or an acronym | [Atlas and reference]({{ '/technical-training/atlas-connectomics-reference/' | relative_url }}) | Searching the units. The atlas exists so you do not have to. |
| Assessing whether a claim in a paper holds | [Journal club]({{ '/technical-training/journal-club/' | relative_url }}) | The abstract. The entries state what each paper actually established and what it did not. |
| Unsure what is expected of you, socially or professionally | [Hidden curriculum]({{ '/hidden-curriculum/' | relative_url }}) | Guessing, or asking someone in a way that costs you. |
| Choosing or citing data | [Datasets]({{ '/datasets/' | relative_url }}) | A paper's methods section alone. You need the version, not just the citation. |

## What is *not* core

Two things on this site look like core material and are not.

**Modules and technical units are path content.** They have an order, they build on
each other, and each ends in an artifact. They belong to tracks. Where a module and
a unit cover the same ground, the module is the session and the unit is the depth
behind it.

**Session kits, slide decks and worksheets are delivery material.** They are
generated from the module pages, and they exist for whoever is running the session
rather than for whoever is learning. If you are studying alone, you can ignore
them entirely. See [teaching]({{ '/teaching/' | relative_url }}).

## Side quests

Some material is deliberately off the main paths: coherent, worth doing, and not a
prerequisite for anything.

<div class="cards-grid cards-grid-wide">
  <article class="card">
    <h3 class="card-title"><a href="{{ '/content-library/proofreading/proofreading-strategies/' | relative_url }}">Proofreading</a></h3>
    <p class="card-description">Five reference entries on error taxonomy, strategy, tooling, metrics and worked examples, plus <a href="{{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}">Unit 08</a>. Treat proofreading as an allocation problem under a fixed budget and it becomes a distinct skill with its own literature &mdash; one that a lab will value on its own, independently of the rest of the curriculum.</p>
    <p><small><strong>Distinct path, not a stage.</strong> You do not need to have finished a track to start here, and finishing here does not put you further along one.</small></p>
  </article>
  <article class="card">
    <h3 class="card-title"><a href="{{ '/content-library/journal-papers/' | relative_url }}">Reading the literature seriously</a></h3>
    <p class="card-description">Two hundred papers organised by topic, each with what it established, what it did not, and what to argue with. Workable as its own long-running habit rather than as reading assigned by a unit.</p>
  </article>
  <article class="card">
    <h3 class="card-title"><a href="{{ '/hidden-curriculum/' | relative_url }}">The hidden curriculum</a></h3>
    <p class="card-description">Also core, and also worth reading as its own thing. Relevant from week one rather than at the end, and the only part of the site that is about what happens around the science rather than in it.</p>
  </article>
</div>
