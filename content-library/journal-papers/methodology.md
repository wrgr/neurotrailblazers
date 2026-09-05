---
layout: page
title: "How the Paper Collection Is Built"
permalink: /content-library/journal-papers/methodology/
description: "How the 2,000-paper connectomics research corpus and its 3 nested tiers (500 Core Flagships, 1,000 Landmarks, and 2,000 Comprehensive Graph) were selected, structured with OCAR cards, and classified across 12 canonical domains."
use_layout_hero: false
content_type: core
---

# How the Paper Collection Is Built

This page explains how the **2,000-paper curated connectomics literature corpus** was retrieved, screened, stratified across 12 canonical research domains, structured into 3 nested tiers ($500 \subset 1,000 \subset 2,000$), and annotated with OCAR cards and 3-level pedagogical summaries.

---

## 🏛️ Corpus Architecture & Nested Tiers

The collection is structured into three strictly nested materializations:

| Tier | Corpus Size | Primary Target Audience &amp; Role | Metadata Depth |
| :--- | :---: | :--- | :--- |
| **500 Key Papers** | **500 papers** | Curriculum flagships, course reading lists, seminar deep-dives | Full abstract, complete author list, verified 5-part OCAR research cards, 3-level summaries, seminar discussion prompts |
| **1000 Key Papers** | **1,000 papers** | Comprehensive scholarly survey, methods reference, subfield tracking | Full abstract, complete OCAR cards, citation metrics (in/out degree, k-core), domain classifications, organism tags |
| **2000 Key Papers** | **2,000 papers** | Global bibliometric network, citation lineage modeling, AI synthesis | Complete directed citation graph ($5,460+$ internal links), complete OCAR cards, full abstract and author/venue metadata, facet views |

---

## 🔬 Multi-Channel Retrieval & Strict Scope Screening

The candidate pool was compiled using positive nanoscale/synaptic-resolution inclusion gates across Semantic Scholar, OpenAlex, Europe PMC, and PubMed:

1. **Direct Synaptic Connectomics**: Dense EM wiring diagrams, synaptic resolution imaging, automated segmentation pipelines (FFN, U-Net, affinity prediction, flood-filling).
2. **First-Class Scientific Axes**: Covers tissue preparation, FIB-SEM/SBEM acquisition, synapse detection, proofreading tools (CAVE, CATMAID, FlyWire), graph analysis (motifs, modularity, network topology), structure-function modeling, NeuroAI, cell census, health-translation, and training/outreach.
3. **Positive Nanoscale Boundary**: Macroscale non-synaptic methods (such as standard low-resolution fMRI or whole-brain fiber tractography without synaptic validation) are filtered out, preserving a clean nanoscale focus.

---

## 📊 Stratified 12-Domain Literature Taxonomy

Candidate papers are classified into 12 mutually exclusive primary domains using a strict decision-order hierarchy:

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

## 🃏 What Each Record Carries

* **Bibliographic Identity**: Title, complete author list as published (`authors`, names separated by `; `), publication year, full venue/journal name, clean lowercase DOI, and a plain-text citation in the form *First-author surname et al. (year). Title. Journal. DOI URL* (two authors are written *Surname & Surname*). These fields are re-derived from the corpus record with the same DOI by `scripts/derive_journal_papers.py`; the validator `scripts/validate_paper_counts.rb` fails if any record ships without authors, with a placeholder citation, or with a year that disagrees with the corpus.
* **Abstract**: The published abstract (`abstract`), present on all 2,000 records. Most are single paragraphs; structured or multi-paragraph abstracts keep their paragraph breaks.
* **Era**: `inclusion_role` is assigned from the publication year -- `history` (up to 2018), `contemporary` (2019--2023), `sota` (2024 onward) -- and drives the era filter on the journal club page.
* **OCAR Structure**:
  * **Opportunity**: Scientific/technological opening addressed.
  * **Challenge**: Key bottlenecks, scale limits, or biological ambiguities.
  * **Action**: Experimental, imaging, computational, or theoretical methodology executed.
  * **Resolution**: Findings, benchmarks, connectome maps, or models delivered.
  * **Future Work**: Open problems and next-generation research horizons.
* **Three-Level Pedagogical Summaries**: Beginner (no prerequisites), Intermediate (foundational knowledge), Advanced (active researcher).
* **Discussion Prompts**: Facilitator questions for journal clubs and research seminars.
* **Graph Topological Placement**: In-degree (inbound citations within corpus), Out-degree (references within corpus), k-core centrality.
* **Directed Citation Links**: List of DOIs cited by the publication.

---

## 🧭 Exploring the Collection

* **[Interactive Citation Graph Explorer]({{ '/technical-training/journal-club/graph/' | relative_url }})**: Live WebGL/Canvas network graph with organic force-directed physics, weighted directed citation arrows, and AI research synthesis prompt generator.
* **[Journal Club Card Browser]({{ '/technical-training/journal-club/' | relative_url }})**: Filterable cards by tier, domain, expertise level, and publication era.
* **[Literature Corpus Taxonomy Hub]({{ '/content-library/journal-papers/' | relative_url }})**: Domain breakdown with direct links to standalone JSON downloads.
