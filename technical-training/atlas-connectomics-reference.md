---
layout: page
title: "Atlas: Connectomics Reference"
description: "A working reference for the technical track: landmark datasets with specifications and access routes, the software landscape by workflow stage, benchmarks, and the curation schema for adding entries."
permalink: /technical-training/atlas-connectomics-reference/
slug: atlas-connectomics-reference
track: core-concepts-methods
pathways:
  - technical foundation
  - methods depth
level: "Reference"
time_estimate: "Use as needed"
prerequisites: "None; most useful alongside Units 02-04"
content_type: core
---

## How to use this page

This is a **lookup table, not a lesson.** Come here when you need to answer one of:

- *Which public dataset can answer my question?* → §1
- *What tool do I need at this pipeline stage?* → §2
- *How do I evaluate a segmentation method?* → §3
- *How do I add something to this atlas?* → §4

Specifications below are as published and are approximate where releases have been
revised. **Always confirm current figures and access terms against the primary source
before citing them** — dataset sizes in particular change as proofreading continues
(Unit 04 §2).

---

## 1. Landmark datasets

### Invertebrate

| Dataset | Scale | Modality / resolution | What it is good for | Access |
|---|---|---|---|---|
| ***C. elegans*** (White et al. 1986; Cook et al. 2019; Witvliet et al. 2021) | 302 neurons; whole animal; a developmental series across maturation | ssTEM | The complete-nervous-system reference case. Witvliet's series is the best available data on how connectivity changes with development | WormWiring, WormAtlas |
| **Larval *Drosophila* brain** (Winding et al. 2023) | ~3,000 neurons; ~550,000 synapses; whole brain | ssTEM | A whole brain small enough for exhaustive graph analysis; bilateral matching studies | CATMAID instances; published supplements |
| ***Drosophila* hemibrain** (Scheffer et al. 2020) | ~25,000 neurons; ~20 million synapses; central brain | FIB-SEM, near-isotropic 8 nm | Cell-type census; the cleanest large connectome for analysis teaching, because isotropy makes tracing quality high | neuPrint |
| **FAFB / FlyWire** (Zheng et al. 2018; Dorkenwald et al. 2024) | Whole adult brain; ~139,000 neurons; ~54.5 million synapses | ssTEM, 4 × 4 × 40 nm | The first whole-brain connectome of a behaviourally complex animal; community-proofread | FlyWire (registration required); CAVE |
| ***Drosophila* male adult nerve cord (MANC)** | ~23,000 neurons | FIB-SEM | Motor circuits; connecting brain to periphery | neuPrint |

### Vertebrate

| Dataset | Scale | Modality / resolution | What it is good for | Access |
|---|---|---|---|---|
| **Mouse retina (e2198 and relatives)** (Briggman, Helmstaedter, Denk) | ~10⁵–10⁶ µm³ | SBEM | Structure-function in a well-characterized circuit; direction selectivity | Published; some via community portals |
| **Kasthuri saturated reconstruction** (Kasthuri et al. 2015) | ~1,500 µm³ mouse neocortex, densely reconstructed | ssSEM (ATUM) | The reference for what *dense, saturated* reconstruction means and costs | Open Connectome / BossDB |
| **Hippocampal CA1 resource** (Harris et al. 2015) | Dense neuropil volume | ssTEM | Spine and synapse ultrastructure; a standard teaching set for Units 05–06 | Published resource |
| **MICrONS** (Allen Institute, Baylor, Princeton; 2025 release) | ~1 mm³ mouse visual cortex; ~200,000 cells; ~500 million synapses | ssTEM, 4 × 4 × 40 nm, **co-registered with in-vivo two-photon calcium imaging** | The reference functional-connectomics dataset. The co-registration is what makes it unique | CAVE / `caveclient`; MicronsBinder notebooks |
| **H01 human cortex** (Shapson-Coe et al. 2024) | ~1 mm³ human temporal cortex; ~57,000 cells; ~150 million synapses; ~1.4 PB | ssTEM, ~4 × 4 × 30 nm | Human tissue at synapse resolution; species comparison | Google/Lichtman lab public release; Neuroglancer |
| **Larval zebrafish whole brain** (Hildebrand et al. 2017) | Whole brain, larval | ssEM | Whole-vertebrate-brain scale in a tractable organism | Published resource |
| **MouseConnects / HI-MC** (NIH BRAIN CONNECTS) | Scaling toward whole mouse brain | Volume EM | The current flagship scaling effort; see the [case study]({{ '/content-library/case-studies/mouseconnects-himc/' | relative_url }}) | Programme resources |

### Choosing among them

| If your question is about… | Start with |
|---|---|
| Whole-brain graph structure in a behaving animal | FlyWire, or larval *Drosophila* for exhaustive analysis |
| Cell types and their connectivity, with clean tracing | Hemibrain |
| Structure–function relationships | MICrONS |
| Human-specific features | H01 |
| Development of connectivity | *C. elegans* developmental series |
| What dense reconstruction actually requires | Kasthuri 2015 |
| Teaching ultrastructure reading | Harris CA1 resource; any of the above in Neuroglancer |

> **Before proposing new acquisition, check this table.** A large fraction of good
> connectomics questions can be answered by re-analysis of existing public data, and
> re-analysis is roughly five orders of magnitude cheaper. See Unit 02's common errors.

---

## 2. Software, by workflow stage

| Stage | Tool | What it does |
|---|---|---|
| **Viewing** | Neuroglancer | The standard browser-based viewer for petascale volumes, meshes, and annotations |
| | webKnossos | Viewing, annotation, and proofreading with collaborative features |
| **Data access** | CloudVolume | Python access to precomputed/chunked volumes |
| | `caveclient` | Client for CAVE — segmentation, synapse tables, materialization versions |
| | `neuprint-python` | Client for neuPrint (hemibrain, MANC) |
| | `intern` | Client for BossDB-hosted volumes |
| **Storage formats** | Precomputed, N5, Zarr / OME-Zarr | Chunked, multiresolution array formats (Unit 04 §3) |
| **Annotation / proofreading** | CATMAID | Collaborative skeleton tracing; the system behind FAFB-era tracing |
| | VAST | Manual volume annotation |
| | CAVE / ChunkedGraph | Versioned, concurrent proofreading over immutable supervoxels |
| **Segmentation** | Flood-filling networks | Iterative single-object growth |
| | Affinity + agglomeration stacks (e.g. `gunpowder`-based pipelines, PyTorch Connectomics) | The dominant production family |
| | Ilastik | Interactive pixel classification for smaller volumes and prototyping |
| **Morphology** | `navis`, `natverse` | Neuron morphology analysis in Python and R |
| | `meshparty` | Meshes and skeletons from segmentations |
| **Graph analysis** | `networkx` | General graph analysis, triad census |
| | `graspologic` | Statistical graph analysis: embeddings, graph matching, two-sample testing |
| | DotMotif | Declarative subgraph/motif queries over connectomes |
| **Hosting** | BossDB | Community archive for volumetric neuroscience data |

---

## 3. Benchmarks and evaluation

| Benchmark | What it evaluates | Notes |
|---|---|---|
| **SNEMI3D** | 3D neurite segmentation | Long-standing reference challenge; small volume |
| **CREMI** | Neuron segmentation and synaptic partner identification in *Drosophila* EM | Includes synaptic partner assignment, which most benchmarks omit |
| **ISBI 2012** | 2D membrane segmentation | Historical; useful for teaching, not representative of current difficulty |

**Caution when reading benchmark results.** Scores on small, well-prepared benchmark
volumes systematically overstate performance on production data, which contains
artifacts (Unit 03), rare morphologies, and volume boundaries that benchmarks exclude.
When evaluating a method for your project, the question is not its leaderboard
position but its error rate *on your tissue* — which means running it on a
representative sub-volume of your own data (Unit 03 §3, the pilot reconstruction rule).

Report metrics as described in Unit 08 §3: at minimum VI decomposed into split and
merge components, plus one tracing-oriented metric such as ERL, plus the effect on
your endpoint.

---

## 4. Contributing an entry

### Required metadata

Every atlas entry carries:

- `citation` — standardized citation string, with DOI
- `workflow_stage` — `acquisition` | `reconstruction` | `proofreading` | `analysis` | `cross-cutting`
- `species`, `brain_region`
- `modality`, `effective_resolution`
- `dataset_or_code_access` — URL plus access constraints (open / registration / request)
- `maturity` — `concept` | `validated prototype` | `production-validated`
- `known_limits` — one concise sentence on the technical boundary
- `mapped_units` — technical-track unit slugs this supports

The `known_limits` field is the one most often left blank and the one most worth
filling. An atlas of tools without limits is advertising.

### Curation policy

1. Add only resources with a clear technical contribution or benchmark value.
2. Mark superseded methods as historical rather than deleting them, when they remain
   pedagogically useful — the history of a method often explains its assumptions.
3. Prefer resources with reproducible artifacts: data, code, or an explicit protocol.
4. Re-review on schedule; retire stale links.
5. Every entry links to at least one unit, so the atlas stays connected to teaching
   rather than becoming an orphaned bibliography.

### Quality-control checks

- Link health check on every external URL
- Metadata completeness against the required schema
- Duplicate detection (the same method published across multiple venues)
- Coverage audit, so no single workflow stage dominates

---

## Visual context set

This page is a lookup table and this panel is deck context, not reference material — nothing here should be cited. Use it instead to rehearse the habit §1 asks for: confirm every specification against the primary source, because dataset sizes and cell counts change as proofreading continues.

<div class="cards-grid">
  <article class="card">
    <img src="{{ '/assets/images/technical-training/atlas-connectomics-reference/FIG-SRC-MODULE14_LESSON3-S03-02.png' | relative_url }}" alt="Atlas references opener visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module14 L3 S03-02:</strong> The opening of the source deck’s reference stream. Treat any figure it carries as provisional — volume sizes, cell counts, and synapse counts in this field are release-dependent, so check them against the primary source before citing (Unit 04 §2).</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/atlas-connectomics-reference/FIG-SRC-MODULE14_LESSON3-S10-01.png' | relative_url }}" alt="Atlas mid-reference stream visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module14 L3 S10:</strong> Mid-stream references. Use it to test the curation standard in §4: for each resource named, ask whether you could write its <code>known_limits</code> sentence. That field is the one most often left blank, and an atlas of tools without limits is advertising.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/atlas-connectomics-reference/FIG-SRC-MODULE14_LESSON3-S19-01.png' | relative_url }}" alt="Atlas closing references visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module14 L3 S19:</strong> Closing references. Check them against the choosing table in §1 before proposing new acquisition — a large share of good connectomics questions can be answered by re-analysis of existing public data, at roughly five orders of magnitude less cost.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/atlas-connectomics-reference/FIG-SRC-21_02388_X_TECHTALK_-S44-01.png' | relative_url }}" alt="Developmental motifs reference context visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Techtalk S44:</strong> Developmental motif comparison, cross-referenced here from Unit 09. Use it as the pointer into the <em>C. elegans</em> developmental series in §1 — the dataset to reach for when the question is how connectivity changes with maturation rather than what it is in one adult.</p>
  </article>
</div>

<p><small>Attribution: module14 lesson3 and neuroAI source decks (historical/context visuals).</small></p>

---

## Mini-lab: curate one entry (30 minutes)

Add one resource to the atlas. Produce:

1. All required metadata fields, complete.
2. One sentence on the technical contribution — what can you now do that you could not?
3. One sentence on the limitation or failure context — when does this *not* work?
4. The unit or units it supports, with a sentence on how.

**Rubric.** *Proficient:* all fields present and accurate. *Strong:* the limitation
sentence is specific enough that a reader could predict a failure case from it, and
the unit mapping identifies where in that unit's workflow the resource fits.

---

## Related

- [Technical Training hub]({{ '/technical-training/' | relative_url }})
- [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }}) — the reading list
- [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }}) — shared vocabulary
- [Dataset access guide]({{ '/datasets/access/' | relative_url }}) — clients and starter notebooks
- [Case studies]({{ '/content-library/' | relative_url }}) — extended treatments of MICrONS, FlyWire, H01, *C. elegans*, and MouseConnects
- Lecture plan: [Atlas Connectomics Reference lecture plan]({{ '/technical-training/slides/atlas-connectomics-reference/' | relative_url }})
