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

<ul class="layer-legend">
  <li style="--accent: var(--layer-core);">
    <span class="layer-name">Core &mdash; reference</span>
    Six bodies of material, written to be looked things up in: definitions, worked methods, papers with the argument stated, the norms nobody writes down. No order. You are not meant to finish it, and a page that says &ldquo;next&rdquo; is a page that has drifted out of the core.
  </li>
  <li style="--accent: var(--layer-path);">
    <span class="layer-name">Path &mdash; the tracks</span>
    Each track selects from the core, puts it in an order, and adds labs that produce something. Three of them, split by topic. A track is finishable; the core is not.
  </li>
  <li style="--accent: var(--layer-delivery);">
    <span class="layer-name">Delivery &mdash; running it</span>
    Session kits, decks and worksheets, generated from the module pages. For whoever is running a session, not for whoever is learning. Ignorable if you are working alone.
  </li>
</ul>

**Modes cut across all three** &mdash; you can walk a track alone, in a hosted session,
or (eventually) inside a research program. The mode axis is independent of the
topic axis: any track can be worked in any available mode.

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
| Placing a paper in the field's landscape | [The field, mapped]({{ '/kb/' | relative_url }}) | Reading forward from its reference list. The interactive maps show what a paper descends from and what built on it. |
| Explaining how this site relates to BRAIN CONNECTS, IC3, and APEX | [The ecosystem map]({{ '/core/connects-ecosystem/' | relative_url }}) | Guessing from program names. The map states what each center does and what this site's job is not. |

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
prerequisite for anything. The largest is **proofreading** — around 17,000 words of
reference material plus a unit, five worked scenarios, and a portfolio artifact, treated
as an allocation problem under a fixed budget rather than as a stage in a sequence.

<div class="arch-grid">
  <article class="arch-card" style="--accent: var(--layer-quest); --accent-tint: var(--layer-quest-tint);">
    <span class="arch-chip" aria-hidden="true">&#128295;</span>
    <h3 class="arch-title"><a href="{{ '/side-quests/proofreading/' | relative_url }}">Proofreading</a></h3>
    <p class="arch-meta"><span class="pill pill-layer">side quest</span><span class="pill pill-plain">20&ndash;30 hours</span></p>
    <p class="arch-body">Correcting reconstruction errors as an allocation problem under a fixed budget. Six stages over the reference material, ending in a portfolio artifact a lab can read and disagree with.</p>
    <div class="arch-actions">
      <a href="{{ '/side-quests/proofreading/' | relative_url }}" class="btn btn-primary">Open the side quest</a>
    </div>
  </article>
  <article class="arch-card" style="--accent: var(--layer-quest); --accent-tint: var(--layer-quest-tint);">
    <span class="arch-chip" aria-hidden="true">&#128300;</span>
    <h3 class="arch-title"><a href="{{ '/side-quests/neuroanatomy-for-proofreaders/' | relative_url }}">Neuroanatomy for Proofreaders</a></h3>
    <p class="arch-meta"><span class="pill pill-layer">side quest</span></p>
    <p class="arch-body">The EM identification training behind competent proofreading: compartment cues, confidence tiers, a unified axon&ndash;dendrite&ndash;glia decision sequence, and a self-run calibration drill on a real public volume.</p>
    <div class="arch-actions">
      <a href="{{ '/side-quests/neuroanatomy-for-proofreaders/' | relative_url }}" class="btn btn-primary">Open the side quest</a>
    </div>
  </article>
  <article class="arch-card" style="--accent: var(--layer-quest); --accent-tint: var(--layer-quest-tint);">
    <span class="arch-chip" aria-hidden="true">&#128218;</span>
    <h3 class="arch-title"><a href="{{ '/side-quests/' | relative_url }}">All side quests</a></h3>
    <p class="arch-meta"><span class="pill pill-layer">index</span></p>
    <p class="arch-body">What the category is, why material sits outside the tracks, and what else is named but not yet built.</p>
    <div class="arch-actions">
      <a href="{{ '/side-quests/' | relative_url }}" class="btn btn-secondary">Browse</a>
    </div>
  </article>
</div>
