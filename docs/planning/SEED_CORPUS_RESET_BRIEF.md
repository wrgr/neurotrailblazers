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
resolves to a subcellular-imaging paper. Two files for the same MANC paper both resolve to
a cardiomyocyte drug-safety study. `10.1109/TPAMI.2018.2835451`, cited for Funke's
structured-loss paper, does not exist.

**Titles are mostly correct. That is what made it dangerous** — it looks checked, and
nothing signals that only one field is trustworthy.

## The methodology was sound; it was never executed

`discovery_strategy.json` specifies a real pipeline: four author tiers defined by
**criteria**, and five discovery steps — forward citations, co-citation, PageRank over
the citation graph, co-authorship betweenness for bridging authors, and targeted gap-fill.
It names the tools and phases. None of it ran; the outputs carry the signature of
generation rather than retrieval.

## Two corrections to earlier drafts of this brief

**A recalled name list.** An earlier draft opened by handing the tool ~40 investigator
names written from memory — reintroducing the failure at step one. Verification rules
downstream cannot save a corpus whose starting set came from recall.

**Seeding from anchors carried lineage.** The next draft bootstrapped from seven
Crossref-verified DOIs. The metadata was sound, but *which seven* was shaped by the
corrupted corpus and by my own recall — selection bias rather than metadata error.

The query below fixes both. **It runs with no access to this repository**, seeds only from
external institutional sources, and holds the seven verified papers back as a **test set**:
if the pipeline rediscovers them independently, the method works; if it misses them, the
method is broken. That is a stronger check than using them as seeds.

**No size cap.** An earlier draft asked for 120–180 papers. That contradicts this project's
own stated design philosophy — *"Overcomplete > undercomplete. We can filter to find cores…
Better to have the full network and prune than to miss important people."* Inclusion
criteria decide membership; the count is an output, not a target.

---

## The query

Self-contained. Needs no repository access and references nothing from the old corpus.

```
Execute a citation-discovery methodology to build a verified bibliography of
nanoscale connectomics research, for use as the reading corpus behind a
training curriculum (audience: undergraduates through early-career researchers).

This is an execution task, not a recall task. The method matters more than the
result, and a smaller honest corpus beats a larger confident one.

## Hard constraints — these override everything below

1. RETRIEVE, NEVER RECALL. Every paper and every person in your output must
   trace to a record you fetched in this session. If you cannot name the query
   or the graph step that surfaced it, it does not go in.
2. NO NAME MAY ENTER FROM MEMORY. Do not begin from researchers you believe are
   important. Every investigator must be derived — from the author record of a
   retrieved paper, from a funding award, or from the citation graph.
3. EVERY DOI MUST RESOLVE. Verify by resolving it. A DOI you did not resolve
   does not go in.
4. METADATA IS COPIED, NOT WRITTEN. Title, complete author list, year, journal,
   DOI transcribed from the resolved record. Never reconstruct an author list,
   and never truncate one to "et al." in the data — some of these papers have
   several hundred authors.
5. IF YOU CANNOT VERIFY IT, LEAVE IT OUT. Put it under "unverified_candidates"
   with what was missing. Never guess a DOI to complete a record.
6. NEVER PAD A THIN AREA. Report it as thin instead.

Why this is spelled out: a previous attempt at this corpus was assembled from
model memory. Its titles were largely right and almost everything else was
wrong — author lists belonging to no such paper, DOIs resolving to unrelated
work, DOIs that did not exist at all. It looked verified. That is precisely what
made it unusable, and it is the failure mode to design against.

## On size

There is no target count and no cap. Include every paper meeting the inclusion
criteria below; stop when the citation graph stops yielding new qualifying work,
not at a round number. Overcomplete is preferred to undercomplete — it is easy
to prune a verified corpus and impossible to recover what was never found.
Report the count you arrive at and why it settled there.

Inclusion criterion: the paper is one a working connectomics researcher would
expect a trainee to have encountered — because it established a result,
introduced a method or tool now in use, released a dataset, or defines the
current state of an active argument.

## Step 1 — derive the starting set from external sources only

Do not start from papers or people you recall. Start from institutions and
programmes, which are checkable:

  a. FUNDING RECORDS. NIH RePORTER for BRAIN Initiative connectomics awards,
     particularly BRAIN CONNECTS. Take the PIs and the publications the awards
     list. Do the same for equivalent European and Japanese programmes (ERC,
     Human Brain Project successors, Brain/MINDS) where they cover connectomics.
  b. PUBLIC DATA PLATFORMS. The dataset and publication listings of BossDB,
     neuPrint, FlyWire, MICrONS/CAVE, DANDI, OpenOrganelle, WormWiring. Take the
     PIs, contributors and dataset papers those pages credit.
  c. LITERATURE SEARCH. Search the major indexes for the defined subject terms
     (connectomics, volume electron microscopy, serial section EM, FIB-SEM,
     SBEM, neural circuit reconstruction, synapse detection, automated
     proofreading, connectome analysis). Take both the most-cited and the most
     recent, separately.

Record for every person and every paper how it entered. Anything with no
derivation path is dropped, however plausible.

## Step 2 — expand by citation graph

Use OpenAlex (free, no key; `api.openalex.org/works/doi:{doi}` resolves a work
and returns authorships, institutions, referenced works and citation counts) or
Semantic Scholar or Crossref. Consult the current API documentation for filter
syntax rather than assuming it.

  a. FORWARD CITATIONS. For each corpus paper, retrieve the works citing it. A
     paper citing five or more corpus papers is a strong candidate.
  b. CO-CITATION. Find papers frequently cited alongside corpus papers.
  c. CENTRALITY. Build the citation graph over the corpus plus its one-hop
     neighbourhood and rank by PageRank. High-scoring papers not yet included
     are candidates — this surfaces connectors, not merely well-cited work.
  d. AUTHOR BRIDGING. Build the co-authorship graph and compute betweenness.
     High-betweenness authors span subcommunities — someone co-authoring with
     both macro-scale network neuroscience and nanoscale EM groups — and their
     work is often the missing link between areas.

Iterate (a)-(d) until a round adds little. Report the round count and what each
round added.

## Step 3 — tier by criteria, not reputation

  Tier 1, field-shapers: last or corresponding author on three or more landmark
    papers; led or co-led a major project; introduced foundational methods or
    terminology.
  Tier 2, key contributors: first or co-first author on a landmark paper;
    developed a broadly adopted tool or method; sustained multi-year technical
    contribution. Often the person who actually built the thing.
  Tier 3, infrastructure builders: built or maintains critical infrastructure;
    frequently middle author but essential to the work.
  Tier 4, emerging: first author on a high-impact paper from 2022 onward; active
    in an emerging subfield.

Assign from retrieved evidence — authorship position, award role, tool
authorship — and state the evidence for every tier-1 assignment.

## Step 4 — coverage

Report the count per area and run targeted searches for any that come back thin:

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
2023-2026 more heavily than citation count alone would — a training corpus goes
stale from the top, and citation counts lag by years.

## Step 5 — self-test against a held-out set

Only after the corpus is complete, check whether it contains these seven papers.
Do not add them if missing, and do not use them to guide the search.

  10.1038/s41586-025-08985-1   light-microscopy connectomic reconstruction, 2025
  10.1038/s41586-024-07558-y   whole adult fly brain wiring diagram, 2024
  10.1038/s41586-025-08790-w   functional connectomics, mouse visual cortex, 2025
  10.1126/science.adk4858      petavoxel human cortex fragment, 2024
  10.7554/eLife.57443          adult Drosophila central brain connectome, 2020
  10.1016/j.cell.2015.06.054   saturated reconstruction of neocortex, 2015
  10.1126/science.add9330      insect brain connectome, 2023

Report how many you found and, for each miss, which step should have surfaced
it. A pipeline missing several of these has a coverage gap worth diagnosing
before the corpus is used.

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
  "areas": ["from the coverage list"],
  "tier": 1,
  "tier_evidence": "why this tier, from what you retrieved",
  "found_via": "funding record {award} | platform {name} | search '{query}' |
                forward citation from {doi} | co-citation | pagerank |
                author bridging",
  "verified": { "doi_resolved": true, "source": "openalex|crossref",
                "date": "YYYY-MM-DD" }
}

Plus five sections:

  1. METHOD — APIs and sources used, date of retrieval, how the starting set was
     derived, graph sizes and round count, and any step you could not complete.
  2. INVESTIGATOR POOL — everyone derived, their tier, and their derivation path.
  3. COVERAGE — per area, per tier, by year; which areas are thin and why.
  4. SELF-TEST — result of Step 5.
  5. UNVERIFIED CANDIDATES — papers you believe belong but could not confirm,
     with what was missing. Expected to be non-empty; an empty section suggests
     the constraints were not applied.
```

---

## Checking what comes back

Do not merge on trust — that is how the current state happened.

1. **`scripts/audit_citations.py`** resolves DOIs and compares real authors against
   claimed ones. Run it before anything else.
2. **Read the SELF-TEST first.** How many of the seven the pipeline found on its own is
   the single best signal of whether the method worked. Several misses means diagnose
   before using, not patch.
3. **Confirm `UNVERIFIED CANDIDATES` is non-empty.** Zero over a corpus this size means
   the constraints were skipped.
4. **Check `found_via` is populated and varied.** If everything reads "search", the
   citation-graph steps did not run and you have search results, not a derived corpus.
5. **Check author lists are complete.** Crossref lists 294 authors for the FlyWire paper
   and 96 for MICrONS; uniformly short lists are the signature of memory.
6. **Check the investigator pool has derivation paths.** A name without one is recall
   leaking back in.

Once the corpus is trustworthy, `scripts/check_curriculum_currency.py` (planned) keys on
its DOIs to report which expert-selected papers the curriculum never cites. That report is
only meaningful on verified DOIs, which is why the reset comes first.
