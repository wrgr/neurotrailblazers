---
layout: page
title: "How the Paper Collection Is Built"
permalink: /content-library/journal-papers/methodology/
description: "How the 2,000-paper connectomics corpus and its 3 nested tiers (500, 1,000 and 2,000 papers) were retrieved, screened, classified into 12 research domains, and annotated."
use_layout_hero: false
content_type: core
---

# How the Paper Collection Is Built

This page explains how the **2,000-paper connectomics corpus** was retrieved, screened, sorted into 12 research domains and 3 nested tiers (the 500 are inside the 1,000, which are inside the 2,000), and annotated.

---

## Three nested tiers

Each tier contains the one below it:

| Tier | Size | Intended use | What each record carries |
| :--- | :---: | :--- | :--- |
| **500 Key Papers** | **500 papers** | Course reading lists and seminars | Abstract, author list, domain-level OCAR notes, 3-level summaries, discussion prompts |
| **1000 Key Papers** | **1,000 papers** | Methods reference and subfield survey | The same, plus citation metrics (in/out degree, k-core) and organism tags |
| **2000 Key Papers** | **2,000 papers** | Citation network and bibliometrics | The same, plus the directed citation graph (5,460 links between corpus papers) and facet views |

---

## Retrieval and screening

Candidates were pulled from Semantic Scholar, OpenAlex, Europe PMC and PubMed and screened for relevance to synaptic-resolution connectomics:

1. **Synaptic connectomics**: dense EM wiring diagrams, synaptic-resolution imaging, and automated segmentation (flood-filling networks, U-Nets, affinity prediction).
2. **Related methods and questions**: tissue preparation, FIB-SEM/SBEM acquisition, synapse detection, proofreading tools (CAVE, CATMAID, FlyWire), graph analysis (motifs, modularity, network topology), structure-function modeling, NeuroAI, cell census, health-translation, and training/outreach.
3. **Scope boundary**: macroscale methods without synaptic resolution (such as standard fMRI or tractography) were meant to be screened out. A few such papers remain in the corpus; the September 2026 audit lists the ones it found.

---

## Twelve research domains

Each paper is assigned one primary domain by a fixed decision order. The shares below are design targets. The Top 500 meets them exactly; the Top 2,000 does not, and the [corpus hub]({{ '/content-library/journal-papers/' | relative_url }}) shows the actual counts:

1. `circuit-structure` (15.0% target share / 75 in Top 500 / 300 in Top 2,000)
2. `pipeline` (15.0% target share / 75 in Top 500 / 300 in Top 2,000)
3. `physiology` (12.0% target share / 60 in Top 500 / 240 in Top 2,000)
4. `behaviour` (12.0% target share / 60 in Top 500 / 240 in Top 2,000)
5. `imaging` (8.0% target share / 40 in Top 500 / 160 in Top 2,000)
6. `cell-types` (8.0% target share / 40 in Top 500 / 160 in Top 2,000)
7. `neuroanatomy` (8.0% target share / 40 in Top 500 / 160 in Top 2,000)
8. `synthesis` (5.0% target share / 25 in Top 500 / 100 in Top 2,000)
9. `dataset` (5.0% target share / 25 in Top 500 / 100 in Top 2,000)
10. `neuroai` (5.0% target share / 25 in Top 500 / 100 in Top 2,000)
11. `health` (5.0% target share / 25 in Top 500 / 100 in Top 2,000)
12. `training-outreach` (2.0% target share / 10 in Top 500 / 40 in Top 2,000)

---

## What each record carries

* **Bibliographic Identity**: Title, complete author list as published (`authors`, names separated by `; `), publication year, full venue/journal name, clean lowercase DOI, and a plain-text citation in the form *First-author surname et al. (year). Title. Journal. DOI URL* (two authors are written *Surname & Surname*). These fields are re-derived from the corpus record with the same DOI by `scripts/derive_journal_papers.py`; the validator `scripts/validate_paper_counts.rb` fails if any record ships without authors, with a placeholder citation, or with a year that disagrees with the corpus.
* **Abstract**: The published abstract (`abstract`), present on all 2,000 records. Most are single paragraphs; structured or multi-paragraph abstracts keep their paragraph breaks.
* **Era**: `inclusion_role` is assigned from the publication year -- `history` (up to 2018), `contemporary` (2019--2023), `sota` (2024 onward) -- and drives the era filter on the journal club page.
* **OCAR notes** (drafted per research domain, not per paper; papers in the same domain share the Opportunity, Challenge, Resolution and Future Work text, and the Action line fills in the paper's title and authors):
  * **Opportunity**: Scientific/technological opening addressed.
  * **Challenge**: Key bottlenecks, scale limits, or biological ambiguities.
  * **Action**: Experimental, imaging, computational, or theoretical methodology executed.
  * **Resolution**: Findings, benchmarks, connectome maps, or models delivered.
  * **Future Work**: Open problems and next-generation research horizons.
* **Three-level summaries**: Beginner (no prerequisites), Intermediate (foundational knowledge), Advanced (active researcher). Like the OCAR notes, these are mostly shared across a domain; the abstract is the paper-specific text.
* **Discussion prompts**: facilitator questions for journal clubs, one set per domain.
* **Graph Topological Placement**: In-degree (inbound citations within corpus), Out-degree (references within corpus), k-core centrality.
* **Directed Citation Links**: List of DOIs cited by the publication.

---

## Exploring the collection

* **[Interactive Citation Graph Explorer]({{ '/technical-training/journal-club/graph/' | relative_url }})**: A force-directed network of citation links between corpus papers, with a prompt builder for AI assistants.
* **[Journal Club Card Browser]({{ '/technical-training/journal-club/' | relative_url }})**: Filterable cards by tier, domain, expertise level, and publication era.
* **[Literature Corpus Taxonomy Hub]({{ '/content-library/journal-papers/' | relative_url }})**: Domain breakdown with direct links to standalone JSON downloads.
