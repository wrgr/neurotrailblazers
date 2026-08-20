---
layout: page
title: "04 Volume Reconstruction Infrastructure"
description: "The systems that turn a petabyte of EM tiles into a queryable connectome: chunked storage, the alignment and segmentation pipeline, proofreading-safe versioning, and the materialization model that makes analysis reproducible."
permalink: /technical-training/04-volume-reconstruction-infrastructure/
slug: 04-volume-reconstruction-infrastructure
track: core-concepts-methods
pathways:
  - technical foundation
  - methods depth
level: "Intermediate"
time_estimate: "2 hours reading + 90 minute lab"
prerequisites: "Units 01-03; comfort reading code helps but is not required"
---

## Before you start

| | |
|---|---|
| **Time** | ~2 h, plus a 90 min lab |
| **Prerequisites** | Units 01–03, particularly the data-volume arithmetic |
| **You need** | Python with `caveclient` and `cloud-volume` installed, or a Colab notebook. A free CAVE account for MICrONS access. |
| **You finish with** | A working query against a real petascale volume, pinned to a specific materialization version, plus a capacity plan for a hypothetical new volume |

Connectomics infrastructure exists to solve one problem that has no analogue in most
scientific computing: **the dataset is simultaneously enormous, mutable, and shared.**
A petabyte of images would be easy if nobody edited it. A collaborative editing system
would be easy if the objects were small. Connectomics needs both at once, plus
reproducible analysis on top of an object that changes while you analyse it.

Understanding how that is solved is not optional systems trivia. It determines whether
your analysis is reproducible, and it is the source of the single most common
correctness bug in connectomics papers: results computed against an unpinned,
continuously-edited segmentation.

---

## What you'll be able to do

1. Describe the reference pipeline from raw tiles to queryable graph, and say what each stage's output actually is.
2. Explain why segmentation is stored as an editable graph over immutable supervoxels, and what that buys.
3. Explain what a materialization version is and why analysis must be pinned to one.
4. Query a real petascale dataset and retrieve a neuron's synapses reproducibly.
5. Produce a capacity and cost plan for a new volume, with the dominant cost identified.

---

## 1. The reference pipeline

Each stage below is a real thing that produces a real artifact. Learn what the
artifact *is*, because that is what you will debug.

### Stage 1 — Ingest

**Input:** raw tiles from the microscope, plus acquisition metadata.
**Output:** an immutable, checksummed archive plus a validated tile manifest.

The archive is write-once. Nothing downstream ever modifies it. If a later stage is
wrong, you re-run from here. Treat the raw archive as the only irreplaceable asset in
the project — everything else is recomputable, expensively.

*Common failure:* metadata that is not machine-readable, so tile position, timestamp,
and acquisition parameters cannot be joined to defects found later.

### Stage 2 — Stitching and alignment

**Input:** tiles.
**Output:** a coherent 3D image volume, plus the transform stack that produced it.

Two sub-problems:

- **Stitching (within a section):** place tiles relative to each other using their
  overlap regions. Mostly rigid or affine per tile.
- **Alignment (across sections):** register section *n* to section *n−1*. Hard,
  because sections deform non-rigidly — compression from the knife, folds, stretch —
  and because errors accumulate. A 0.1-voxel-per-section bias over 20,000 sections is
  a 2,000-voxel drift.

Modern pipelines use coarse-to-fine elastic registration with a global relaxation step
that distributes residual error across the whole stack rather than letting it
accumulate in one direction.

**What you must retain:** the transforms, versioned. Any coordinate you record in the
aligned space is meaningless without knowing which alignment version produced it. When
an alignment is revised, every stored annotation coordinate must be re-mapped — this
is a real and painful operation, and it is why alignment revisions are rare and
carefully planned.

*Common failure:* alignment residual reported as a global mean. Report the
distribution and the maximum, per region. See Unit 03 §3.

### Stage 3 — Boundary/affinity prediction

**Input:** aligned image.
**Output:** a per-voxel prediction, same size as the input — either an affinity map
(probability that neighbouring voxel pairs belong to the same object, typically in 3
or more directions) or a boundary map.

This is a dense convolutional network applied over petavoxels. It is the most
compute-intensive stage and it is embarrassingly parallel over blocks, with the
important caveat that blocks must **overlap**, because a network needs context beyond
the region it predicts.

*Common failure:* block-boundary seams in the prediction, visible later as a regular
grid of segmentation errors. The fix is sufficient overlap plus blending, and the way
you detect it is to look for errors whose spatial distribution matches your block grid
— another instance of the Unit 03 "which coordinate system does the defect live in?"
question.

### Stage 4 — Supervoxel generation

**Input:** affinities.
**Output:** **supervoxels** — small, over-segmented fragments, deliberately smaller
than real objects.

This is a design decision with far-reaching consequences. Watershed (or similar) is
run at a threshold that guarantees over-segmentation: a supervoxel may be a piece of a
neurite, but it should almost never span two neurites. The pipeline accepts many
splits in order to avoid merges, because — as Unit 03 argued — merges are the
expensive error.

**Supervoxels are immutable.** They are the atoms of everything above them. This is
the key to the whole architecture and the next section explains why.

### Stage 5 — Agglomeration

**Input:** supervoxels + affinities (+ increasingly, learned agglomeration models).
**Output:** the segmentation — an assignment of supervoxels to objects.

Agglomeration merges supervoxels into neurons. Approaches include mean-affinity
agglomeration, learned agglomeration using local shape descriptors, and flood-filling
networks that grow objects iteratively from seeds. What matters architecturally is
that the output is *a grouping of immutable atoms*, not a new voxel labelling.

### Stage 6 — Derived geometry

**Input:** segmentation.
**Output:** meshes (multi-LOD, for 3D viewing), skeletons (for morphometry and path
distance), and per-object statistics (volume, surface area, bounding box).

These are regenerated when the segmentation changes, which is constantly. Design them
as cheap, incremental, and per-object.

### Stage 7 — Synapse detection

**Input:** aligned image (and often the segmentation).
**Output:** a synapse table: coordinates, pre/post supervoxel IDs, confidence,
size/area, and often cleft segmentation.

Modelled as a separate detection problem, usually with its own network. **Store
partner identity as supervoxel IDs, not object IDs.** Supervoxel IDs are immutable, so
when proofreading changes which neuron an object is, the synapse assignment follows
automatically. Storing object IDs would require rewriting the synapse table on every
edit — a design mistake that is easy to make and painful to undo.

### Stage 8 — Annotation and serving

**Input:** everything above.
**Output:** interactive viewing (Neuroglancer), proofreading, spatial and relational
queries, and versioned annotation tables.

---

## 2. The core idea: an editable graph over immutable atoms

Naive design: store the segmentation as a labelled volume. Then a proofreader merges
two neurons and you rewrite… potentially gigabytes of voxels. With hundreds of
proofreaders editing concurrently, this is unworkable.

**The ChunkedGraph solution.** Store supervoxels once, immutably. Represent the
segmentation as a *graph* whose nodes are supervoxels and whose edges are "these are
the same object". An object is a connected component of that graph. Then:

- **A merge is adding an edge.** Microseconds, not gigabytes.
- **A split is removing edges** — specifically, finding a minimum cut separating two
  user-specified points.
- **The graph is hierarchical and chunked**, so connected-component queries over
  millions of supervoxels stay fast: the hierarchy lets you answer "what object
  contains this supervoxel?" without traversing the whole graph.
- **Every edit is an entry in an append-only log**, with author, timestamp, and
  operation. Nothing is destroyed; state at any past time is recoverable.
- **Concurrent editing works**, because edits are small graph operations that can be
  applied and reconciled independently.

Systems in production use: **CAVE** (Connectome Annotation Versioning Engine, used for
MICrONS and FlyWire), **DVID**, **webKnossos**, **CATMAID** (which solved a related
problem for skeleton-based tracing), and **neuPrint** (a Neo4j-backed graph service
for released, frozen connectomes).

### Why this matters to you, the analyst

Because **object IDs are not stable.** In a ChunkedGraph system, the ID of a neuron
changes every time it is edited. A "root ID" identifies an object *as of a moment in
time*.

This has a hard consequence: **an object ID in your notebook, your paper, or your
figure caption is meaningless without a timestamp or version.** This is the number-one
reproducibility failure in connectomics analysis, and it is silent — your code runs
fine, it just answers a different question than it did last week.

### Materialization

To make analysis possible at all, the system periodically produces a
**materialization**: a frozen snapshot in which every annotation (synapses, cell-type
labels, manual annotations) has been joined to the segmentation state at a specific
timestamp, and written into queryable tables.

- Analyses run **against a materialization version**, e.g. version 943.
- The version number is a **first-class part of your methods section**, exactly like a
  software version or a genome build.
- Re-running the same analysis on a later version *will* give different numbers,
  because proofreading continued. That is correct behaviour, not a bug — but it must
  be visible.

> **Rule.** Every figure you produce records the materialization version, the query
> code, and the date. Every paper states the version. If your collaborator cannot
> reproduce your number, the first question is always "which version?"

### Check yourself

<details markdown="1">
<summary>Why store synapse partners as supervoxel IDs rather than neuron IDs?</summary>

Because supervoxel IDs are immutable and neuron (root) IDs are not.

A synapse is physically attached to a small piece of tissue — a supervoxel. That
attachment never changes, no matter how proofreaders regroup supervoxels into
neurons. So the synapse table is written once and stays correct forever.

If you stored neuron IDs instead, then every merge and split would invalidate rows
in a table with hundreds of millions of entries, and any stale copy of the table
would be silently wrong. Resolving "which neuron does this synapse belong to?"
becomes a lookup from supervoxel → current root at a given version — which is
exactly what the materialization precomputes.

**Generalizable principle:** in a system with mutable groupings, store foreign keys
against the immutable layer and resolve upward at query time.
</details>

<details markdown="1">
<summary>Your collaborator sends a list of 200 neuron IDs from six months ago. What do
you do before using them?</summary>

Do not query them directly against the current segmentation. Some will no longer
exist; others will have been merged or split, and a stale ID may silently resolve to
something, or to nothing.

The correct procedure:

1. Ask which materialization version or timestamp the IDs came from. If your
   collaborator does not know, that is itself an important finding about the
   analysis's reproducibility.
2. Use the platform's ID-lineage facility to map the old root IDs forward to current
   root IDs, which will be a one-to-many or many-to-one mapping wherever edits
   occurred.
3. **Report the churn.** How many IDs mapped 1:1? How many split into several? How
   many merged together? That number tells you and your collaborator how much
   proofreading changed the objects, and it belongs in the methods.
4. If the original analysis must be exactly reproduced, query the *old* version
   directly rather than mapping forward.
</details>

---

## 3. Storage layout, and why chunk shape is a real decision

Petascale volumes are stored as **chunked, multi-resolution arrays** — the
Neuroglancer precomputed format, N5, Zarr / OME-Zarr, and similar. The recurring
elements:

- **Chunks:** the volume is divided into blocks (commonly 64³ to 512³ voxels) stored
  as individual objects. You fetch only the chunks you need.
- **Resolution pyramid:** progressively downsampled copies. Zooming out fetches a
  coarse level rather than a million fine chunks. The pyramid costs about 30–50% extra
  storage and is what makes interactive viewing possible.
- **Sharding:** millions of tiny objects are slow and expensive in object stores, so
  chunks are bundled into larger shard files with an index. This is a pure
  cost/latency optimization and it matters a lot at petascale.
- **Compression:** lossy (JPEG) for image data, where a little compression noise is
  acceptable; lossless and label-aware (e.g. compressed segmentation) for label data,
  where a single flipped bit changes an object's identity.

**Chunk shape is an access-pattern decision, and the two main consumers want opposite
things:**

| Consumer | Access pattern | Wants |
|---|---|---|
| Proofreader in a viewer | Scrolls through z at one xy location, then pans | Chunks elongated in z, or at least isotropic in index space |
| Analysis job | Reads a whole neuron's bounding box, or a whole section | Large chunks, sequential layout |
| Synapse query | Random access to scattered small regions | Small chunks, good spatial index |

You cannot optimize for all three with one layout. Production systems store **multiple
representations** — the image pyramid for viewing, the segmentation graph for editing,
and materialized tables for analysis — precisely so each consumer gets a layout suited
to it. When someone asks "why is this stored three times?", that is the answer.

---

## 4. Reproducibility requirements

A reconstruction pipeline that cannot reproduce its own output is not a scientific
instrument. The requirements are not exotic; they are just rarely all satisfied.

**Every stage output records:** input artifact IDs, code revision (a commit hash),
full parameter set, model artifact hash and framework version, container image digest,
random seeds, and wall-clock/resource usage.

**Idempotency.** Re-running a stage on the same inputs with the same parameters
produces the same output. This sounds trivial and is not: GPU non-determinism,
unpinned dependencies, and unseeded randomness all break it. Pin them explicitly and
test that a re-run matches.

**Region-scoped invalidation.** When a region is re-processed, only downstream
artifacts *for that region* should be invalidated. A pipeline whose only recovery
option is "re-run everything" cannot fix a local defect at petascale, so this is a
structural requirement, not a nicety.

**Release candidates.** Segmentation is versioned and released like software: a
candidate is produced, quality metrics are computed (Unit 08), it is reviewed, and it
is either promoted or rejected. Analyses cite the release.

---

## 5. Capacity and cost, worked

For a 1 mm³ volume at 4 × 4 × 40 nm (~1.5 × 10¹⁵ voxels):

| Item | Estimate | Notes |
|---|---|---|
| Raw archive | ~1.5 PB | Written once, read rarely; cold storage |
| Aligned pyramid | ~2 PB | Base + ~30–50% for the pyramid; hot |
| Affinity/boundary maps | ~1.5 PB | Often transient — delete after supervoxel generation |
| Supervoxels + segmentation | ~0.2–0.8 PB | Label-aware compression helps a lot |
| Meshes (all LODs) | 1–10 TB | Regenerated on edit |
| Skeletons | 10–100 GB | Cheap; archive them (see Unit 02) |
| Synapse table | 50–200 GB | ~5 × 10⁸ rows; the hottest analytical table |
| Edit history | Grows monotonically | Must be curated, never deleted |

**GPU cost, order of magnitude.** Suppose a segmentation network processes ~10⁷
voxels/second/GPU end-to-end including I/O. For 1.5 × 10¹⁵ voxels:

```
1.5e15 / 1e7 = 1.5e8 GPU-seconds ~= 1,736 GPU-days
```

On 500 GPUs that is roughly 3.5 days of wall clock — and you will run it more than
once, because the first model version is never the last. Budget for 3–5 full inference
passes over the project lifetime.

**But the dominant cost is none of the above.** It is **proofreading labour**. At
even a modest few hours of skilled human attention per fully-proofread neuron, a study
needing 1,000 complete neurons is thousands of person-hours. Compute and storage are
line items you can negotiate with a cloud vendor. Proofreading is a hiring, training,
retention, and quality-management problem, and it is the reason Unit 08 spends its
time on triage and prioritization rather than on algorithms.

**Cost traps specific to this domain:**

- **Egress.** Moving a petabyte out of a cloud region can cost more than storing it
  for a year. Co-locate compute with data; give collaborators compute *next to* the
  data rather than copies of it.
- **Small-object overhead.** Billions of unsharded chunks incur per-request charges
  and listing costs that can exceed storage costs. Shard.
- **Forgotten intermediates.** Affinity maps are the size of the raw data. Delete them
  after supervoxel generation, or set a lifecycle policy — but only once you are
  confident you will not need to re-agglomerate.
- **Idle hot storage.** Move the raw archive to cold tiers immediately after ingest
  validation.

---

## Visual context set

Read these as architecture sketches to check your own mental model against. For each one, ask where the immutable layer sits and where the mutable one does — the whole design in §2 follows from freezing supervoxels and letting only the grouping change.

<div class="cards-grid">
  <article class="card">
    <img src="{{ '/assets/images/technical-training/04-volume-reconstruction-infrastructure/FIG-SRC-MODULE14_LESSON1-S04-01.png' | relative_url }}" alt="High-level architecture visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module14 L1 S04:</strong> A high-level architecture view. Map the eight stages of §1 onto it and name the artifact each stage actually produces, because the artifact is the thing you debug. A stage whose output you cannot name is a stage you do not yet understand.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/04-volume-reconstruction-infrastructure/FIG-SRC-MODULE14_LESSON1-S07-01.png' | relative_url }}" alt="Workflow API integration visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module14 L1 S07:</strong> Workflow and API integration. Ask what a query crossing these boundaries returns and whether it is pinned: a root ID carries no meaning without a materialization version or timestamp (§2), and this layer is where that omission quietly enters an analysis.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/04-volume-reconstruction-infrastructure/FIG-SRC-MODULE14_LESSON1-S12-01.png' | relative_url }}" alt="Service decomposition visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module14 L1 S12:</strong> Service decomposition. Match each service to the consumers in §3 — proofreader, analysis job, synapse query — which want mutually incompatible chunk layouts. Storing the same data in several representations is the answer to “why is this here three times?”, not redundancy.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/04-volume-reconstruction-infrastructure/FIG-SRC-MODULE13_LESSON1-S08-01.png' | relative_url }}" alt="Scalable analytics context visual" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module13 L1 S08:</strong> Scalable analytics. Weigh whatever scaling story it tells against the cost table in §5: compute and storage are line items you can negotiate with a vendor, and proofreading labour is the dominant cost that no architecture removes.</p>
  </article>
</div>

<p><small>Attribution: assets_outreach source decks (historical/context visuals).</small></p>

---

## Lab: query a petascale volume reproducibly (90 minutes)

**Part A — make a reproducible query (45 min).**

Using `caveclient` against the MICrONS public release (or `neuprint-python` against
hemibrain, or the FlyWire client, whichever you have access to):

1. Connect, and **print the available materialization versions.** Pick one and pin to
   it explicitly in your code. Record the version number in a comment at the top of
   your notebook.
2. Pick any neuron. Retrieve its input synapses and its output synapses.
3. Report: total input count, total output count, and the number of distinct
   presynaptic partners.
4. Compute the distribution of synapses per partner. Note that it is heavy-tailed —
   most partners contribute one synapse, a few contribute many. Plot it on log axes.
5. **Now re-run steps 2–4 against a different materialization version.** Report how
   the numbers changed and explain why.
6. Write a five-line "reproducibility header" for your notebook: dataset, version,
   client library version, date, query author.

**Part B — capacity plan (45 min).**

Your institute proposes imaging 5 mm³ of mouse hippocampus at 4 × 4 × 40 nm. Produce a
one-page plan:

1. Raw data volume, computed.
2. Full storage table (all stages, as in §5), with a stated retention policy for each
   line — what is kept forever, what is transient, what is cold.
3. GPU-days for one full segmentation pass, with your assumed throughput stated. Then
   multiply by your assumed number of passes and justify the number.
4. Proofreading estimate: neurons needed for a stated scientific goal × hours per
   neuron × cost per hour. State every assumption.
5. Identify the dominant cost and defend the ranking.
6. Name **two** design decisions that would reduce the dominant cost, and the
   scientific price of each.

### Rubric

| | Not yet | Proficient | Strong |
|---|---|---|---|
| **Version discipline** | No version recorded | Version pinned and reported | Cross-version comparison performed and the difference explained |
| **Query correctness** | Runs, unclear result | Correct counts with units | Handles autapses/self-loops, filters by synapse confidence, states the filter |
| **Storage plan** | Raw only | All stages, with sizes | Retention policy per line, with cold/hot tiering and egress considered |
| **Compute estimate** | Absent | GPU-days computed | Multiple passes justified; failure/re-run budget included |
| **Labour estimate** | Absent | Included | Identified as dominant, with assumptions stated and sensitivity noted |
| **Tradeoffs** | Generic | Two decisions named | Scientific cost of each decision stated concretely |

<details markdown="1">
<summary>Hint for Part A step 4, if the distribution surprises you</summary>

You should see something close to a power-law-ish, heavy-tailed distribution: a
large majority of partners connect via a single synapse, with a small number of
partners connecting via five, ten, or more.

This shape matters for analysis. Single-synapse connections are exactly the ones
most vulnerable to false-positive synapse detection and to merge errors, so the
"weak" tail of the connectivity distribution is also its least reliable part. Many
analyses therefore apply a threshold (e.g. ≥ 2 or ≥ 3 synapses to call a
connection) — which is a defensible choice that **must be stated**, because it
changes graph density substantially and it changes it non-uniformly across cell
types. Unit 09 returns to this.
</details>

---

## Common errors and how to recover

**Unpinned analysis.** Recover: pin the materialization version; put it in the
notebook header and the figure caption. Re-run one old analysis with an explicit
version to check you can reproduce it.

**Stale object IDs.** Recover: map IDs through the lineage service and report churn.

**Isotropic assumptions in derived geometry.** Recover: check that skeleton path
lengths and distance transforms use physical voxel spacing. Test with a synthetic
object of known dimensions.

**Storing derived data keyed on mutable IDs.** Recover: re-key to supervoxels, or to
(root ID, version) pairs. Never to a bare root ID.

**A pipeline that can only be re-run whole.** Recover: introduce region-scoped
artifact keys before you need them. You will need them.

---

## What this unit does not cover

Segmentation model architectures and proofreading practice (Unit 08), the metrics used
to accept a release (Unit 08), and analysis on the resulting graph (Unit 09).
Deployment specifics for any one platform are out of scope — the ideas here transfer
across CAVE, DVID, webKnossos, and neuPrint even though the APIs do not.

---

## Go deeper

- [Reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }}) — stage-by-stage detail
- [Data formats]({{ '/content-library/infrastructure/data-formats/' | relative_url }}) — precomputed, N5, Zarr, sharding
- [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}) — the versioning model in depth
- [Data storage and pipelines reading list]({{ '/content-library/journal-papers/data-storage/' | relative_url }}) — CAVE, CATMAID, BossDB, OME-Zarr papers
- [Dataset access guide]({{ '/datasets/access/' | relative_url }}) — clients and starter notebooks

## Course links

- Reading list: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Shared vocabulary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})
- Related modules: [Module 12]({{ '/modules/module12/' | relative_url }}), [Module 18]({{ '/modules/module18/' | relative_url }})
- Lecture plan: [Volume Reconstruction Infrastructure lecture plan]({{ '/technical-training/slides/04-volume-reconstruction-infrastructure/' | relative_url }})
- **Next unit:** [05 Neuronal Ultrastructure]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }})
