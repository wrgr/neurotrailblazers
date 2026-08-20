# Seed corpus reset: deep research brief

## Why we are resetting rather than repairing

`_data/expert_seed_papers/` holds 150 records that look like a verified bibliography.
Checking every one against Crossref showed it is not:

| Check | Result |
|---|---|
| Records whose DOI resolves and whose every listed author is on that paper | **56 of 125** |
| Author overlap below 50% | 22 |
| Author overlap of **zero** — no listed author is on the paper | 11 |
| DOIs resolving to a **completely unrelated paper** | 11 |
| DOIs that return 404 | 5 |
| Records with no DOI at all | 18 |

`boyden-2025-liconn` lists seven authors; LICONN (`10.1038/s41586-025-08985-1`) is by
Tavakoli, Lyudchik, Januszewski and ten others — none of the seven. `dorkenwald-2024-neurd`
resolves to a subcellular-imaging paper. `plaza-2023-manc` and `rivlin-2023-manc` — the
same paper twice — both resolve to a cardiomyocyte drug-safety study.
`10.1109/TPAMI.2018.2835451`, cited for Funke's structured-loss paper, does not exist.

**Titles are mostly correct. That is what made it dangerous** — it looks checked, and
nothing signals that only one field is trustworthy.

## The methodology was sound; it was never executed

`discovery_strategy.json` specifies a real pipeline: a four-tier author taxonomy defined
by **criteria**, and five discovery steps — forward citations, co-citation, reverse
PageRank over the citation graph, co-authorship betweenness for bridging authors, and
targeted gap-fill for thin dimensions. It names the tools (Semantic Scholar / OpenAlex,
networkx) and the phases.

None of it ran. The outputs carry the signature of generation, not retrieval.

So the reset is not a new strategy. **It is that strategy, executed, with verification as
a gate.** The brief below does that.

### One correction to an earlier draft of this brief

A previous version opened by handing the research tool a list of ~40 investigator names.
Those names were written from recall — reintroducing, at the very first step, the exact
failure being repaired. The strategy document defines tiers by criteria and treats names
as *hypotheses to investigate*, which is the better design.

**The query below therefore contains no remembered names.** It bootstraps from seven
DOIs verified against Crossref in this session and derives everyone else from the real
author records on those papers and from the citation graph.

---

## The query

```
Execute a documented citation-discovery methodology to build a verified seed
bibliography of 120-180 papers for a nanoscale connectomics training curriculum
(audience: undergraduates through early-career researchers).

This is an execution task, not a recall task. The method below matters more
than the output size.

## Hard constraints — these override everything else

1. RETRIEVE, NEVER RECALL. Every paper and every person in your output must
   trace to a record you fetched in this session. If you cannot name the query
   that surfaced it, it does not go in.
2. NO NAME MAY ENTER FROM MEMORY. Do not begin from a list of researchers you
   believe are important. Every investigator must be *derived* — from the author
   record of a verified paper, or from the citation/co-authorship graph.
3. EVERY DOI MUST RESOLVE. Verify by resolving it. A DOI you did not resolve
   does not go in the output.
4. METADATA IS COPIED, NOT WRITTEN. Title, complete author list, year, journal,
   DOI transcribed from the resolved record. Never reconstruct an author list,
   and never truncate one to "et al." in the data — several of these papers have
   hundreds of authors.
5. IF YOU CANNOT VERIFY IT, LEAVE IT OUT. Put it under "unverified_candidates"
   with what you were missing. Never guess a DOI to complete a record.
6. NEVER PAD A THIN DIMENSION. Report it as thin instead.

Why this is spelled out: the corpus this replaces was assembled from memory. Its
titles were largely right and almost everything else was wrong — author lists
belonging to no such paper, DOIs resolving to unrelated work, DOIs that do not
exist. It looked verified. That is what made it unusable.

## Step 0 — known-answer check, before any other work

Resolve these seven DOIs and confirm you reproduce the metadata exactly. If any
differs, stop and report rather than proceeding.

  10.1038/s41586-025-08985-1  Tavakoli, Lyudchik, Januszewski et al. (2025) Nature
                              Light-microscopy-based connectomic reconstruction of
                              mammalian brain tissue
  10.1038/s41586-024-07558-y  Dorkenwald, Matsliah, Sterling et al. (2024) Nature
                              Neuronal wiring diagram of an adult brain
  10.1038/s41586-025-08790-w  Bae, Baptiste et al. (2025) Nature
                              Functional connectomics spanning multiple areas of
                              mouse visual cortex
  10.1126/science.adk4858     Shapson-Coe, Januszewski, Berger et al. (2024) Science
                              A petavoxel fragment of human cerebral cortex
                              reconstructed at nanoscale resolution
  10.7554/eLife.57443         Scheffer, Xu, Januszewski et al. (2020) eLife
                              A connectome and analysis of the adult Drosophila
                              central brain
  10.1016/j.cell.2015.06.054  Kasthuri, Hayworth, Berger et al. (2015) Cell
                              Saturated Reconstruction of a Volume of Neocortex
  10.1126/science.add9330     Winding, Pedigo, Barnes et al. (2023) Science
                              The connectome of an insect brain

These seven are also your ANCHOR SET for everything below. They were chosen to
span invertebrate and vertebrate, EM and light microscopy, and 2015 to 2025.

## Step 1 — derive the investigator pool from the anchors

Pull the complete author record for each anchor paper, with institutional
affiliations. Do not filter by whether you recognise a name.

Then widen from verifiable programme sources rather than from recall:
  - NIH RePORTER, for BRAIN CONNECTS and BRAIN Initiative connectomics awards —
    take the PIs listed on the awards.
  - The dataset and publication listings of the major public data platforms
    (BossDB, neuPrint, FlyWire, MICrONS/CAVE, DANDI) — take the PIs and
    contributors those pages credit.

Record, for every person, how they entered the pool. A person with no
derivation path is dropped, however plausible they seem.

## Step 2 — expand by citation graph

Use OpenAlex (free, no key; `api.openalex.org/works/doi:{doi}` resolves a work
and returns authorships, institutions, referenced works and citation counts) or
Semantic Scholar. Check the current API docs for filter syntax rather than
assuming it.

  a. FORWARD CITATIONS. For each corpus paper, retrieve the works citing it. A
     paper citing five or more corpus papers is a strong candidate.
  b. CO-CITATION. Find papers frequently cited alongside corpus papers.
  c. CENTRALITY. Build the citation graph over the corpus plus its one-hop
     neighbourhood and rank by PageRank. High-scoring papers not yet in the
     corpus are candidates — this surfaces connectors rather than merely
     well-cited work.
  d. AUTHOR BRIDGING. Build the co-authorship graph and compute betweenness.
     High-betweenness authors span subcommunities (someone co-authoring with
     both macro-scale network neuroscience and nanoscale EM groups) and their
     work is often the missing link between dimensions.

Report which of (a)-(d) surfaced each addition.

## Step 3 — tier by criteria, not by reputation

  Tier 1, field-shapers: last/corresponding author on three or more landmark
    connectomics papers; led or co-led a major project; introduced foundational
    methods or terminology.
  Tier 2, key contributors: first or co-first author on a landmark paper;
    developed a broadly adopted tool or method; sustained multi-year technical
    contribution. Often the person who actually built the thing.
  Tier 3, infrastructure builders: built or maintains critical infrastructure;
    frequently middle author but essential to the work.
  Tier 4, emerging: first author on a high-impact paper from 2022 onward;
    active in an emerging subfield.

Assign tiers from the evidence you retrieved — authorship position, project
role, citation position — and state the evidence for each tier-1 assignment.

## Step 4 — coverage and gap-fill

Report the count per dimension, then run targeted searches for any that come
back thin:

  - why map connectomes; what structure can and cannot establish
  - measurement scales and modality trade-offs (EM, X-ray, LM, expansion, MRI)
  - tissue preparation, staining, sectioning, and their artifacts
  - EM acquisition: ssTEM/ssSEM, SBEM, FIB-SEM, multibeam, ML-guided acquisition
  - alignment, segmentation, agglomeration
  - proofreading, error taxonomy, automated error detection, QC metrics
  - data infrastructure: chunked formats, versioning, annotation systems, serving
  - neuronal and glial ultrastructure; cell-type identification
  - connectome graph construction, null models, motif and network analysis
  - NeuroAI and connectome-constrained modelling
  - landmark datasets and case studies (C. elegans, Drosophila, mouse, human)
  - ethics, data sharing, open science, community and citizen-science efforts

Keep foundational pre-2010 work where it is still load-bearing, and weight
2023-2026 more heavily than citation count alone would, since a training corpus
goes stale from the top and citation counts lag by years.

## Output

One JSON object per paper:

{
  "title": "exact title from the resolved record",
  "authors": ["Family Initials", "..."],   // complete, in order, transcribed
  "year": 2024,
  "journal": "container title from the record",
  "doi": "10.xxxx/xxxxx",
  "url": "URL you actually visited",
  "abstract_summary": "2-3 sentences, your words, on what it established and
                       what it did not",
  "dimensions": ["from the coverage list"],
  "tier": 1,
  "tier_evidence": "why this tier, from what you retrieved",
  "found_via": "anchor | forward citation from {doi} | co-citation | pagerank |
                author bridging | gap-fill search '{query}'",
  "verified": { "doi_resolved": true, "source": "openalex|crossref",
                "date": "YYYY-MM-DD" }
}

Plus four sections:

  1. METHOD — APIs used, date of retrieval, how the investigator pool was
     derived, graph sizes at each step, and any step you could not complete.
  2. INVESTIGATOR POOL — everyone derived, their tier, and their derivation
     path.
  3. COVERAGE — per dimension, per tier, by year; and which dimensions are thin
     and why.
  4. UNVERIFIED CANDIDATES — papers you believe belong but could not confirm,
     with what was missing. Expected to be non-empty; an empty section suggests
     the constraints were not applied.
```

---

## Checking what comes back

Do not merge on trust — that is how the current state happened.

1. **`scripts/audit_citations.py`** resolves DOIs and compares real authors against
   claimed ones. Run it first.
2. **Spot-check the anchor seven** in the returned data.
3. **Confirm `UNVERIFIED CANDIDATES` is non-empty.** Zero over ~150 papers means the
   constraints were skipped.
4. **Check `found_via` is populated and varied.** If everything says "direct search",
   the citation-graph steps did not run and you have a search-engine result, not a
   derived corpus.
5. **Check author lists are complete.** Crossref lists 294 authors for FlyWire and 96
   for MICrONS; uniformly short lists are the signature of memory.
6. **Check the investigator pool has derivation paths.** A name with none is recall
   leaking back in.

Once the corpus is trustworthy, `scripts/check_curriculum_currency.py` (planned) keys on
its DOIs to report which expert-selected papers the curriculum never cites. That report
is only meaningful on verified DOIs, which is why the reset comes first.
