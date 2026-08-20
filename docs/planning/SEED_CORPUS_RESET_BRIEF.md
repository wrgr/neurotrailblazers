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

Examples, each verified:

- `boyden-2025-liconn` lists seven authors. The LICONN paper
  (`10.1038/s41586-025-08985-1`) is by Tavakoli, Lyudchik, Januszewski and ten others.
  **None of the seven listed names is on it.**
- `dorkenwald-2024-neurd` carries a DOI that resolves to a subcellular-architecture
  imaging paper.
- `plaza-2023-manc` and `rivlin-2023-manc` — the same paper, twice — both carry a DOI
  that resolves to a cardiomyocyte drug-safety study.
- `10.1109/TPAMI.2018.2835451`, cited for the Funke structured-loss paper, does not exist.

**Titles are mostly correct. That is what made it dangerous** — the corpus looks checked,
and nothing in it flags that only the titles are trustworthy.

### The methodology was sound; the execution never happened

`discovery_strategy.json` specifies a real pipeline: tiered authors, forward-citation and
co-citation expansion, "Semantic Scholar API: /paper/{id}/citations". `expert_seed_list.json`
cross-checks 29 experts against BossDB PIs and BRAIN CONNECTS awards.

None of that appears to have been run. The outputs carry the signature of generation
rather than retrieval: plausible author lists that are wrong, plausible DOIs that resolve
elsewhere, and a manifest claiming 137 records where 150 exist.

So the fix is not a better strategy. **It is executing the existing strategy against real
APIs, with verification as a hard gate rather than an afterthought.** That is what the
brief below enforces.

---

## The query

Paste this whole block into the deep research tool.

```
Build a verified seed bibliography of 120-180 papers for a nanoscale connectomics
training curriculum aimed at undergraduates through early-career researchers.

## Hard constraints — read these first

These override everything else in this brief. A shorter, honest list beats a
complete-looking one.

1. RETRIEVE, NEVER RECALL. Every paper must come from a search result or a
   citation record you actually fetched in this session. Do not add a paper
   because you know it exists.
2. EVERY DOI MUST RESOLVE. Verify each one by resolving it (Crossref
   api.crossref.org/works/{doi}, or the publisher). A DOI you did not resolve
   does not go in the output.
3. METADATA IS COPIED, NOT WRITTEN. Title, full author list, year, journal and
   DOI must be transcribed from the resolved record. Never reconstruct an
   author list from memory, and never abbreviate one to "et al." in the data.
4. IF YOU CANNOT VERIFY IT, LEAVE IT OUT. Put it in a separate
   "unverified_candidates" list with the reason. Do not guess a DOI to make a
   record complete.
5. DO NOT FILL COVERAGE GAPS BY INVENTION. If a dimension below is thin because
   you could not find qualifying work, report it as thin. An under-covered
   dimension named honestly is useful; a padded one is not.

Why this is spelled out: the corpus this replaces was assembled from memory. Its
titles were largely right and almost everything else was wrong — plausible
author lists that belonged to no such paper, DOIs resolving to unrelated work,
and several DOIs that do not exist. It looked verified, which is precisely what
made it unusable.

## Known-answer check — run this before anything else

Retrieve these seven DOIs and confirm your pipeline reproduces the metadata
exactly. If any comes back different, stop and report the discrepancy rather
than proceeding.

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

## Selection method

Start from these field-shaping investigators and expand by citation graph, not
by recall:

  Seung, Lichtman, Denk, Helmstaedter, Jain, Januszewski, Sporns, Vogelstein JT,
  Bock, Cardona, Jefferis, Plaza, Scheffer, Saalfeld, Funke, Turaga, Harris KM,
  Kasthuri, Hayworth, Xu CS, Collman, Reid, Tolias, Zeng, Briggman, Kording,
  Zador, Priebe, Pfister, Murthy, Wilson RI, Samuel, Yendiki, Shapson-Coe,
  Dorkenwald, Schneider-Mizell, Gray Roncal, Wester, Matelsky, Boyden

For each: retrieve their connectomics-relevant publications, then expand via
(a) forward citations — papers citing several corpus papers are strong
candidates — and (b) co-citation — papers frequently cited alongside corpus
papers. Report which expansion produced each addition.

Tier every paper:
  1 — field-shaping. Defined a subfield, led a landmark project, or introduced a
      method the field now depends on.
  2 — key contribution. First-author landmark work, or a widely adopted method
      or tool paper.
  3 — useful supporting work: benchmarks, datasets, reviews, negative results.

## Coverage required

Aim for balance across these, and report the count per dimension:

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
  - ethics, data sharing, open science, and community/citizen-science efforts

Include foundational older work (pre-2010) where it is still load-bearing, and
weight recent work (2023-2026) more heavily than a citation count alone would,
since the field is moving fast and a training corpus goes stale from the top.

## Output format

One JSON object per paper:

{
  "title": "exact title from the resolved record",
  "authors": ["Family Initials", "..."],   // complete, in order, from the record
  "year": 2024,
  "journal": "container title from the record",
  "doi": "10.xxxx/xxxxx",
  "url": "publisher or open-access URL you actually visited",
  "abstract_summary": "2-3 sentences, your own words, on what the paper
                       established and what it did not",
  "dimensions": ["from the coverage list above"],
  "tier": 1,
  "seed_expert": "which investigator's work led you here",
  "found_via": "direct search | forward citation from {doi} | co-citation with {doi}",
  "verified": {
    "doi_resolved": true,
    "source": "crossref",
    "date": "YYYY-MM-DD"
  }
}

Plus three summary sections:

  1. METHOD — what you searched, which APIs and databases, date of retrieval,
     and how you expanded from the seed authors.
  2. COVERAGE — count per dimension, count per tier, distribution by year, and
     any dimension you consider under-covered and why.
  3. UNVERIFIED CANDIDATES — papers you believe belong but could not confirm,
     each with what you were missing. This section is expected to be non-empty;
     an empty one suggests the constraints were not applied.
```

---

## After it comes back

Do not merge the output on trust — that is how the current state happened. Run the
existing tooling against it first:

1. **`scripts/audit_citations.py`** already resolves DOIs and compares real authors
   against cited ones. Point it at the new records before anything else.
2. **Spot-check the known-answer seven** in the returned data by hand.
3. **Check the unverified-candidates list is non-empty.** If a research pass over
   ~150 papers reports zero it could not confirm, the constraints were ignored.
4. **Verify author lists are complete**, not truncated to three names plus "et al." —
   FlyWire has 294 authors and MICrONS 96, so a uniformly short list is a signal.
5. Only then write the records, and keep the `verified` block as shipped provenance.

Once the corpus is trustworthy, `scripts/check_curriculum_currency.py` (planned) can
key on its DOIs to report which expert-selected papers the curriculum never cites —
the signal that prompted this whole thread. That report is only meaningful on verified
DOIs, which is why the reset comes first.
