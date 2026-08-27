---
layout: page
title: "How the Paper Collection Is Built"
permalink: /content-library/journal-papers/methodology/
description: "How the 1,074-paper visible core was selected, what a card carries, and why views (not separate corpora) are how it's filtered."
use_layout_hero: false
content_type: core
---

# How the Paper Collection Is Built

This page explains where the {{ site.data.journal_papers.papers | size }}-paper collection came from, what belongs in it, and what doesn't. It replaces an earlier split between a 96-paper hand-taught collection and a 191-paper bibliometric corpus &mdash; those were two collections built for different jobs. There is now **one collection**, with views (filters) on top.

## The visible core

The underlying literature map covers 1,806 candidate works, with a working set of 1,488 under active analysis. **Neither of those ships here.** This page describes the **visible core** &mdash; the subset that has cleared an inclusion bar and been fully annotated:

| Period | Years | Bar |
|---|---|---|
| Historical | ≤2018 | year-cohort citation percentile ≥ 50 **or** k-core ≥ 3 |
| Contemporary | 2019–2024 | that bar, **or** references ≥3 other core papers |
| SOTA (state of the art) | 2025–2026 | 2026: references ≥3 core papers **or** is cited by ≥1; 2025: both |

"References" and "is cited by" only count links to *other papers in this same core* &mdash; not raw global citation counts. That keeps a paper's place in the collection tied to how connected it is to the rest of the field being taught here, not just how popular it is.

This is not a second screening of the whole field and not a ranked canon of "the best" papers. It's the set dense enough, and connected enough, to be worth teaching from today.

## Every paper has one stable identity

Each record has a **uuid**: its DOI (lowercased) when one exists, otherwise a stable catalog work id. That uuid is what the journal-club filters, the content-library deep-dive pages, the citation graph, and "related work" links all key off of. A paper never gets a second id because it shows up in a different view.

## What a card carries

Every paper in the collection gets the same shape:

- Bibliographic identity &mdash; title, authors, year, venue, DOI/uuid
- **OCAR** &mdash; Opportunity, Challenge, Action, Resolution, Future Work
- Three reading levels &mdash; beginner, intermediate, advanced summaries
- Tags, and discussion prompts
- **Graph place** &mdash; how many core papers cite it, how many it cites, its k-core (how embedded it is in the densest part of the citation network), and its citation percentile within its publication year
- **Streams** &mdash; pipeline stage(s), organism, dataset, method, and charting axis
- **Related work** &mdash; other core papers it cites or is cited by
- Links to the paper's DOI/landing page and, where public, a PDF

Pedagogical prose (OCAR, summaries, discussion prompts) is written from the paper itself wherever a source PDF was available, which is true for the whole visible core in this drop. Where a source file couldn't be matched, the card falls back to the catalog abstract, and `annotation_status` says so &mdash; that flag exists so a mismatched or abstract-only card is never presented as more thoroughly read than it was.

## Views, not corpora

A view is an ordered or grouped list of uuids &mdash; it never adds or removes papers from the collection. Shipped views:

- **Highest k-core** &mdash; ranked by how embedded a paper is in the citation network
- **Era** &mdash; historical / contemporary / SOTA
- **Pipeline stage** &mdash; preparation through analysis
- **Organism**
- **Dataset** &mdash; named registry volumes (FlyWire, MICrONS, H01, …)
- **Method**
- **Charting axis** &mdash; including training/outreach and health-translation threads
- **Year**
- **Suggested reading paths** &mdash; editorial sequences (historical arc, methods deep dive, analysis & interpretation)

The eleven teaching dimensions used on the hand-annotated [journal paper deep-dives]({{ '/content-library/journal-papers/' | relative_url }}) are themselves a view over this same collection, not a second library. Browse the full collection, filtered any of these ways, on the [journal club]({{ '/technical-training/journal-club/' | relative_url }}) page.
