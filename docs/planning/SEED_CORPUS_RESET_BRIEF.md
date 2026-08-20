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

**Assumed prior knowledge.** Earlier drafts assumed the reader knew what nanoscale
connectomics is, where its boundary against macro-scale/MRI connectomics falls, what the
pipeline stages are, and why metadata precision matters in this field specifically. A
clean model has none of that, and the boundary question in particular decides the run —
without it, the enormous fMRI network-neuroscience literature swamps the corpus. The
query now opens with a BACKGROUND section supplying all of it, including the search
vocabulary.

**No size cap.** An earlier draft asked for 120–180 papers. That contradicts this project's
own stated design philosophy — *"Overcomplete > undercomplete. We can filter to find cores…
Better to have the full network and prune than to miss important people."* Inclusion
criteria decide membership; the count is an output, not a target.

---

## The query

Complete and self-contained. Paste the whole block.

```
# TASK

Build a verified bibliography of nanoscale connectomics research, to serve as
the reading corpus behind a training curriculum.

This is a retrieval and verification task, not a recall task. The method matters
more than the result, and a smaller honest corpus beats a larger confident one.

Read the BACKGROUND section first — it defines the field boundary, and getting
that boundary wrong is the most likely way this run fails.

# BACKGROUND

## What the field is

Connectomics is the mapping of neural connectivity. This corpus covers the
*nanoscale* branch: reconstructing individual neurons and the synapses between
them, at a resolution where a synapse is directly visible. In practice that
means volume electron microscopy, at voxel sizes of a few nanometres.

**This is a different field from macro-scale connectomics** — diffusion MRI
tractography, resting-state functional connectivity, network neuroscience over
brain regions. That literature is enormous and it is NOT the target. Include a
macro-scale paper only where it bears directly on the nanoscale story: a
modality comparison, a methodological contrast, a shared analysis technique, or
an argument about what each scale can establish. If more than roughly one paper
in ten is MRI-based, the boundary has been drawn wrong.

Adjacent fields with the same caution: general microscopy methods, general
computer vision, general graph theory. Include the specific papers the
connectomics literature actually builds on; exclude the parent literatures.

## The pipeline, which structures everything

Nanoscale connectomics runs a long pipeline, and each stage has its own
literature, its own failure modes, and its own key papers:

  tissue preparation and staining -> sectioning or block-face milling ->
  EM acquisition -> image alignment -> automated segmentation ->
  agglomeration -> human proofreading -> synapse detection ->
  graph construction -> analysis

A trainee needs papers from every stage. A corpus weighted only toward the
famous reconstruction results, with nothing on staining chemistry or data
infrastructure, is a corpus that cannot support teaching.

## The scale, which explains why infrastructure matters

A cubic millimetre of cortex imaged at roughly 4 x 4 x 40 nm is on the order of
a petabyte of image data, containing perhaps 10^5 neurons and 10^8 synapses.
Reconstruction consumes GPU-years; proofreading consumes human-years. This is
why papers on chunked storage formats, versioned annotation systems, cloud
serving and distributed pipelines belong in a connectomics corpus — they are
not peripheral engineering, they are what makes the science possible.

## The landmark datasets

These anchor much of the literature, and papers describing, releasing,
proofreading or analysing them are core:

  - C. elegans — the original complete nervous system, and later whole-animal
    and developmental series
  - Drosophila — the hemibrain, the full adult brain (FAFB / FlyWire), the
    larval brain, the male ventral nerve cord
  - Mouse — retina, and cortical volumes including functionally co-registered
    ones
  - Human — cortical fragments from surgical tissue
  - Zebrafish larva, and other whole-brain vertebrate efforts

## Why metadata precision is non-negotiable here

This field version-pins its data. A reconstruction is edited continuously, so a
result is only interpretable if it states which dataset version, which
materialization, and what level of proofreading it rests on. A citation without
a resolvable identifier is, by the field's own standards, not a citation.

The corpus should therefore meet the standard the field practises. That is the
principle behind the hard constraints below — not bureaucracy.

## What makes a paper belong

Include a paper if a working connectomics researcher would expect a trainee to
have encountered it, because it:

  - established a result that changed what people believe,
  - introduced a method, algorithm or tool that is now in use,
  - released a dataset that others analyse,
  - defines the current state of an active argument, or
  - is the clearest available explanation of something a trainee must
    understand — good reviews, tutorials and benchmark papers count, even when
    their citation counts do not stand out.

The audience is undergraduates through early-career researchers. Pedagogical
value is a real inclusion criterion here, not only impact.

## Search vocabulary

Terms that identify this literature: connectomics; connectome; volume electron
microscopy; serial section electron microscopy; ssTEM; ssSEM; SBEM; serial
block-face; FIB-SEM; ATUM; GridTape; multibeam SEM; en bloc staining; rOTO;
neural circuit reconstruction; dense reconstruction; saturated reconstruction;
neuron segmentation; flood-filling network; affinity prediction; agglomeration;
supervoxel; proofreading; split and merge errors; synapse detection; synaptic
partner assignment; skeletonization; neuroglancer; connectome annotation;
electron microscopy alignment; expansion microscopy connectomics;
X-ray holographic nano-tomography; connectome analysis; motif analysis;
network null model; connectome-constrained model.

# HARD CONSTRAINTS

These override everything else.

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

# ON SIZE

There is no target count and no cap. Include every paper meeting the inclusion
criteria; stop when the citation graph stops yielding new qualifying work, not
at a round number. Overcomplete is preferred to undercomplete — it is easy to
prune a verified corpus and impossible to recover what was never found. Report
the count you arrive at and why it settled there.

# STEP 1 — derive the starting set from external sources only

Do not start from papers or people you recall. Start from institutions and
programmes, which are checkable:

  a. FUNDING RECORDS. NIH RePORTER for BRAIN Initiative connectomics awards,
     particularly BRAIN CONNECTS. Take the PIs and the publications the awards
     list. Do the same for equivalent European and Japanese programmes (ERC,
     Human Brain Project successors, Brain/MINDS) where they cover connectomics.
  b. PUBLIC DATA PLATFORMS. The dataset and publication listings of BossDB,
     neuPrint, FlyWire, MICrONS/CAVE, DANDI, OpenOrganelle, WormWiring. Take the
     PIs, contributors and dataset papers those pages credit.
  c. LITERATURE SEARCH. Search the major indexes for the vocabulary listed in
     BACKGROUND. Take both the most-cited and the most recent, separately, so
     recency is not crushed by citation lag.

Record for every person and every paper how it entered. Anything with no
derivation path is dropped, however plausible it looks.

# STEP 2 — expand by citation graph

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

## If you cannot execute code

Steps 2c and 2d require computation over a graph, not just retrieval. If you
cannot run code:

  - Say so plainly in METHOD. Do not approximate these steps by judgement and
    do not silently skip them — a ranked list produced by intuition rather than
    by the algorithm is exactly the failure this brief exists to prevent.
  - Still do 2a and 2b, which are retrieval, and complete everything else.
  - Additionally emit a CITATION EDGES section: for every corpus paper, the DOIs
    it cites that are also in the corpus, plus the DOIs of works citing it that
    you retrieved. Raw edges, no ranking. The graph analysis can then be run
    separately on that edge list.

Your job is the retrieval. That is the part that must not come from memory.

# STEP 3 — tier by criteria, not reputation

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

# STEP 4 — coverage

Report the count per area and run targeted searches for any that come back thin.
The areas follow the pipeline described in BACKGROUND:

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

# STEP 5 — self-test against a held-out set

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

# OUTPUT

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

Plus these sections:

  1. METHOD — APIs and sources used, date of retrieval, how the starting set was
     derived, graph sizes and round count, and any step you could not complete.
  2. INVESTIGATOR POOL — everyone derived, their tier, and their derivation path.
  3. COVERAGE — per area, per tier, by year; which areas are thin and why.
  4. SELF-TEST — result of Step 5.
  5. UNVERIFIED CANDIDATES — papers you believe belong but could not confirm,
     with what was missing. Expected to be non-empty; an empty section suggests
     the constraints were not applied.
  6. CITATION EDGES — only if you could not run Step 2c/2d, per the note above.
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
