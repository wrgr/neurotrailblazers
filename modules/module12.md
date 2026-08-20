---
title: "Module 12: Big Data in Connectomics"
layout: module
permalink: /modules/module12/
description: "Design scalable data storage, querying, and analysis workflows for petascale connectomics datasets."
module_number: 12
difficulty: "Advanced"
duration: "4-5 hours"
learning_objectives:
  - "Describe core architecture patterns for petascale connectomics data"
  - "Plan compute, storage, and indexing strategies for large EM volumes"
  - "Implement query workflows that preserve provenance and reproducibility"
  - "Identify bottlenecks and failure modes in large-scale analysis pipelines"
prerequisites: "Modules 1-11, Python and basic data engineering familiarity"
merit_stage: "Analysis"
compass_skills:
  - "Systems Reasoning"
  - "Data Engineering"
  - "Reproducibility"
ccr_focus:
  - "Knowledge - Large-Scale Data Systems"
  - "Skills - Scalable Analysis"

# Normalized metadata
slug: "module12"
short_title: "Big Data in Connectomics"
status: "active"
audience:
  - "students"
pipeline_stage: "Analysis"
merit_row_focus: "Analysis"
topics:
  - "big-data"
  - "infrastructure"
  - "query-systems"
summary: "Scalable storage, indexing, and reproducible query design for connectomics datasets."
key_questions:
  - "How do we architect data systems for petascale connectomics?"
  - "Which indexing/query decisions drive analysis speed and reliability?"
  - "How do we preserve provenance at scale?"
slides:
  - "/assets/slides/module12/module12-big-data-in-connectomics.pdf"
notebook:
  - "/assets/notebooks/module12/module12-big-data-in-connectomics.ipynb"
  - "/notebooks/intro/DashSynapseExplorer.ipynb"
datasets:
  - "/datasets/mouseconnects"
  - "/datasets/workflow"
personas:
  - "/avatars/gradstudent"
  - "/avatars/researcher"
  - "/avatars/mentor"
related_tools:
  - "/tools/connectome-quality/"
  - "/tools/ask-an-expert/"
related_frameworks:
  - "research-incubator-model"
  - "education-models"
prerequisites_list:
  - "Basic SQL/Python dataframe proficiency"
  - "Familiarity with EM volume structure"
next_modules:
  - "module13"
  - "module14"
references:
  - "H01 human cortical fragment release and infrastructure notes."
  - "MICrONS data platform documentation."
  - "Januszewski et al. (2018) for scalable reconstruction context."
videos: []
downloads:
  - "/notebooks/intro/DashSynapseExplorer.ipynb"
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
---

## Capability target
Produce a scalable, reproducible query-and-analysis plan for a large connectomics dataset, including storage assumptions, indexing strategy, and provenance capture. Concretely, you should finish this module able to size a dataset from its imaging parameters before anyone quotes you a price, choose a chunk and shard layout from the access pattern you actually have rather than from the format everyone else uses, predict which single query will dominate your compute bill, and pin every published number to a segmentation version that a stranger can re-query a year from now.

## Why this module matters
Connectomics is now data-system-limited as much as algorithm-limited. One cubic millimeter of cortex imaged at 4 x 4 x 40 nm is (1,000,000/4) x (1,000,000/4) x (1,000,000/40) = 250,000 x 250,000 x 25,000 voxels, or about 1.56 x 10^15 voxels — roughly 1.5 PB of 8-bit image data before a single derived product exists. MICrONS and H01 are each approximately 1 mm³ and are reported in the 1.4-2 PB range. At that scale the decisions that determine whether a project finishes are made in the first week: chunk size, sharding, where the bytes physically live, and whether analysis tables are pinned to a version. None of those decisions appear in a figure, and all of them are expensive to reverse.

The failure mode is rarely a crash. It is a query that takes eleven hours instead of four minutes, so the postdoc runs it twice a week instead of forty times a day and the science slows to the speed of the infrastructure. It is a cloud invoice dominated by per-request charges rather than by stored bytes. Most often it is a number in a figure that cannot be reproduced, because the segmentation it was computed against no longer exists under that name.

## Concept set

### 1) Storage layout is chosen by access pattern, not by format popularity
- **Technical:** chunked array formats (Zarr, N5, Neuroglancer precomputed) store a volume as independent compressed blocks, commonly 64³ to 256³ voxels. The chunk is the smallest unit of I/O, so you always pay for the whole chunk even when you want one plane of it. Reading a single 512 x 512 pixel section-plane view touches 2 x 2 = 4 chunks at 256³ and 8 x 8 = 64 chunks at 64³ — but the byte cost runs the other way, because each 256³ chunk carries 16.8 million voxels of z-depth you did not ask for. The 256³ layout moves about 67 MB of decompressed data for that view; the 64³ layout moves about 17 MB. Anisotropic chunks such as 128 x 128 x 16 cut plane-oriented reads further and make z-oriented traversal worse. Typical EM compression ratios are 2-10x depending on codec; segmentation label volumes compress far better than raw images because they contain large uniform regions.
- **Plain language:** the chunk is the smallest thing you can read, so shape it like the reads you will actually do.
- **Misconception guardrail:** the format everyone else uses is automatically the right layout for your access pattern.

### 2) Object count is a cost driver independent of byte count
- **Technical:** divide 1.56 x 10^15 voxels by a 128³ chunk (2,097,152 voxels) and the full-resolution level alone is about 7.5 x 10^8 chunks. Downsampled pyramid levels add roughly an eighth, a sixty-fourth, and so on, so the total stays in the same order. Object stores bill per request as well as per stored byte, and a pipeline that touches every chunk a handful of times generates billions of billable operations. On published object-store price sheets, per-request charges at that volume can exceed the cost of storing the same bytes for a year. Sharded formats pack many chunks into a smaller number of large files with an index, which converts most of those requests into byte-range reads inside one object.
- **Plain language:** a billion tiny files costs real money even when the bytes are cheap.
- **Misconception guardrail:** storage cost is the storage line on the invoice.

### 3) Derived data, not raw image, is most of what you will manage
- **Technical:** raw is one line item among many, and several of the derived products are the ones analysts actually touch. The table below gives approximate footprints for a ~1 mm³ project, relative to the raw volume unless stated otherwise.
- **Plain language:** budget for everything the pipeline makes, not for the number in the paper's abstract.
- **Misconception guardrail:** the dataset size is the petabyte figure quoted for the raw imagery.

| Product | Footprint | Persistence |
|---|---|---|
| Raw image tiles | 1x (~1.5 PB) | Irreplaceable; keep forever |
| Aligned, chunked pyramid | +30-50% over raw | Regenerable, but expensively |
| Affinity/boundary maps | ~1x raw | Usually transient; delete after agglomeration |
| Segmentation labels | 0.1-0.5x raw | Regenerable from supervoxels plus edit log |
| Meshes (multi-LOD) | 1-10 TB | Regenerated as segmentation changes |
| Skeletons | 10-100 GB | Cheap; regenerate freely |
| Synapse table (~5 x 10^8 rows) | 50-200 GB | The analyst's primary object |

### 4) Root IDs are not stable, and unpinned analysis is the field's most common silent bug
- **Technical:** in a ChunkedGraph system, supervoxels are immutable and a neuron is a connected component of an editable graph over them. Every proofreading edit produces a new root ID, so a root ID identifies an object as of a moment in time. An ID recorded without a materialization version or timestamp is meaningless. Synapse partners are stored as supervoxel IDs precisely so that assignments survive proofreading; resolving "which neuron does this synapse belong to?" is a lookup from supervoxel to current root at a stated version, which is what a materialization precomputes. Analysis run against an unpinned segmentation is the most common silent correctness bug in the field: the code runs, returns plausible numbers, and answers a different question than it did last month.
- **Plain language:** neuron IDs expire; write down which version yours came from.
- **Misconception guardrail:** an object ID refers to the same neuron next month.

### 5) Query cost is a research variable
- **Technical:** iteration speed determines how many hypotheses you test. A query plan that scans a 5 x 10^8-row synapse table once per neuron of interest is quadratic in disguise; the same question answered by one filtered scan into a pre-joined extract is linear. Profile before optimizing: run the query on a 0.1% sample, measure, and extrapolate — if the sample takes 40 seconds, the full run will take on the order of eleven hours, and you have learned that for 40 seconds instead of eleven hours.
- **Plain language:** how you ask the data matters as much as what you ask.
- **Misconception guardrail:** "it runs eventually" is acceptable for iterative science.

### 6) Provenance is a field in the output, not a habit
- **Technical:** every released table and every figure should carry dataset identifier, materialization version or timestamp, query text or its hash, thresholds applied, code commit, environment specification, and run date. These belong in the artifact itself — a sidecar JSON or a metadata header — because notebooks get re-run, cells get executed out of order, and kernel history is not a record anyone else can read.
- **Plain language:** if you cannot reconstruct how the file was made, you cannot defend the result.
- **Misconception guardrail:** notebook history is sufficient provenance.

## Worked example: sizing and costing a project before you design it

A collaborator asks whether your group can host and analyze a new 1 mm³ mouse cortex volume imaged at 4 x 4 x 40 nm. They want an answer this week. Here is the reasoning, in the order it should happen.

**Step 1 — Convert imaging parameters to voxels.** 1 mm = 10^6 nm on each axis. Dividing by the voxel dimensions gives 250,000 x 250,000 x 25,000 = 1.5625 x 10^15 voxels. At 8 bits per voxel that is 1.5625 x 10^15 bytes, about 1.5 PB, or roughly 1.4 PiB. This matches the 1.4-2 PB range reported for MICrONS and H01, which is the check that tells you the arithmetic is right.

**Step 2 — Add the derived products, not just the raw.** Using the table above: the aligned pyramid adds 30-50%, so budget another 0.5-0.75 PB. Affinity maps are about 1x raw but are transient; if you plan to delete them after agglomeration you need the peak capacity, not the steady-state capacity, and those are different numbers. Segmentation labels land at 0.15-0.75 PB. Meshes, skeletons, and the synapse table together are under 20 TB — negligible in bytes and yet the only products most of your analysts will ever open. Steady state: roughly 2.5-3 PB. Peak during reconstruction: closer to 4 PB. Quote both.

**Step 3 — Count objects, not only bytes.** At 128³ chunks the full-resolution level alone is about 7.5 x 10^8 objects. A pipeline pass that reads and writes each chunk once is 1.5 x 10^9 billable requests. This is the number that turns an apparently affordable storage plan into an unaffordable one, and it is why the answer is to shard: pack chunks into large indexed files so most reads become byte-range requests inside one object.

**Step 4 — Ask where the compute is.** If the bytes sit in cloud object storage and your analysis runs on the university cluster, every pass pulls the data across an egress boundary. Egress for a single full-volume pass can cost more than a year of storing the same bytes. This single question — is compute co-located with the data? — changes the architecture more than any format choice. If compute cannot be moved, the design must be "download derived products, never voxels": skeletons, meshes, and the synapse table total under 20 TB and answer most connectivity questions.

**Step 5 — Name the dominant query before writing it.** For a weekly motif report the dominant operation is joining the synapse table to a current neuron identity for every edge. Doing that per neuron against the live ChunkedGraph is hundreds of thousands of round trips. Doing it once, against a pinned materialization, produces an extract you can query locally in seconds for the rest of the week.

**What the estimate does not tell you.** It does not tell you the project cost, because proofreading labor — not compute and not storage — is usually the dominant line item, and this module does not size it. It also assumes 8-bit imagery and no lossy compression; if the group compresses to JPEG at 2-4x, the raw figure moves but the object count and the egress question do not.

## Storage and query decision tables

Use these as starting positions, then justify any departure.

| Where the data lives | Best when | What it costs you |
|---|---|---|
| Cloud object store, cloud compute | Bursty, parallel, multi-institution access | Ongoing storage bill; per-request charges if unsharded; vendor lock-in of formats and tooling |
| On-prem storage, on-prem compute | Steady single-site load, existing cluster | Capital cost, capacity planning, and you own the failure modes; hard to share externally |
| Cloud store, on-prem compute with local cache | Analysts need derived products only | Egress on every cache miss; cache invalidation becomes your problem when segmentation updates |
| Full local mirror of derived products only | Analysis-only groups with no pipeline role | You cannot regenerate anything; you inherit whatever upstream decided, including its errors |

| Query strategy | Best when | What it gives up |
|---|---|---|
| Live ChunkedGraph / API lookups per object | Small, interactive, current-state questions | Latency per call; unreproducible unless you record the timestamp; falls over at 10^5+ objects |
| Query a pinned materialization version | Any analysis that will be published | Numbers are as of that version, so they will differ from the live state, and you must say so |
| One-time extract into local DuckDB/Parquet | Repeated slicing of the same subset all week | The extract goes stale silently; needs a version stamp in the filename and a refresh policy |
| Distributed scan (Dask/BigQuery) over the full table | Whole-dataset statistics, one-off | Cost scales with bytes scanned; easy to burn a budget on an exploratory typo |

## Hidden curriculum scaffold
- Unwritten engineering expectations in connectomics teams, stated plainly:
  - Benchmark on a 0.1-1% sample and extrapolate before optimizing anything.
  - Record the materialization version in the same commit as the figure it produced.
  - Keep exploratory notebooks and release pipelines in separate directories with separate review rules; a notebook is never the artifact.
  - Write outputs to version-stamped paths so a re-run cannot overwrite the file a figure was made from.
- How to teach it explicitly:
  - Require a provenance block in every submitted analysis, and reject submissions missing the version field rather than commenting on them.
  - Run a failure postmortem on one real slow query per cohort, with the profile output shown.
  - Grade reproducibility separately from correctness, and weight it equally.

## Core workflow: scalable query planning
1. Write the analysis question as a sentence naming the table, the filter, and the unit of the answer — for example, "count synapses between layer 2/3 pyramidal cells and basket cells, per neuron pair, at cleft score above threshold."
2. Estimate the working set: how many rows, how many objects, how many bytes must move, and whether that fits in memory on the machine you have.
3. Choose storage and index strategy from the access pattern — chunk shape for volumetric reads, sharding if object counts exceed roughly 10^6, a pre-joined extract if the same join recurs.
4. Pin the segmentation: record the materialization version or timestamp, and refuse to proceed if it is unknown.
5. Prototype on a 0.1% sample, profile, and extrapolate the full runtime before running it once at full scale.
6. Add provenance fields to the output artifact itself, not to the surrounding notebook.
7. Validate reproducibility by having a second person re-run the query package from the recorded version and compare row counts and summary statistics.

## Pre-class preparation
- Read the [data formats]({{ '/content-library/infrastructure/data-formats/' | relative_url }}) and [provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}) library pages.
- Bring one query you have actually run, with its runtime and its data source.
- Have a calculator or notebook open; the first exercise is arithmetic, not code.

## 60-minute tutorial run-of-show
1. **00:00-08:00 | Architecture framing and failure examples**
   Open with two real failure shapes: the eleven-hour query and the unreproducible figure. State the module's claim — that both are design decisions made before any analysis, not accidents.
2. **08:00-20:00 | Access-pattern to index mapping exercise**
   Learners size a 1 mm³ volume from imaging parameters by hand, then compute chunk counts at 64³, 128³, and 256³ and the byte cost of one 512 x 512 plane view at each. Instructor challenge: "Which of these is right? What did you have to assume about how people will read this volume?"
3. **20:00-34:00 | Query profiling and bottleneck diagnosis**
   Run a supplied query on a 0.1% sample, record the wall time, extrapolate, then run the pre-joined version and compare. Learners write down the ratio.
4. **34:00-46:00 | Provenance logging implementation**
   Each learner adds a provenance block — dataset, version, query hash, thresholds, commit, date — to one of their own outputs and shows it to a neighbor.
5. **46:00-56:00 | Team review of reproducibility gaps**
   Pairs swap query packages and attempt to state, from the artifact alone, which segmentation version produced it. Any package that fails this test is marked and repaired.
6. **56:00-60:00 | Competency check and next-step assignment**
   Each learner names the single query that will dominate their own project's cost, and the mitigation they will try first.

## Studio activity: petascale query design lab
**Scenario:** Your team must deliver a weekly motif-analysis report from a connectomics store holding a ~5 x 10^8-row synapse table, a 120,000-row segment table, and a cell-type annotation table for about 8,400 classified neurons. The volume is approximately 1 mm³, the bytes live in cloud object storage, and your analysis cluster is on-premises. The report must be regenerated every Monday and cited in a manuscript in preparation. Last week's report took nine hours and produced numbers that do not match the version from three weeks ago; nobody knows why.

**Tasks**
1. Propose a storage and index layout for the expected query patterns, stating chunk shape, sharding decision, and which products you would mirror locally with byte estimates for each.
2. Write or outline the two queries that will dominate cost, estimate their runtime from a sampled measurement, and name the specific operation you expect to be the bottleneck.
3. Define the minimum provenance fields for the weekly output, and state what happens operationally when one is missing.
4. Diagnose the three-week discrepancy: list the candidate causes in the order you would check them, and say what evidence would distinguish them.
5. Produce one optimization proposal with an expected speedup and its cost, and one reproducibility safeguard that a person could execute without your help.

**Expected outputs**
- Query architecture sketch with byte and object-count estimates.
- Baseline vs optimized query plan with measured or sampled runtimes.
- Provenance checklist with a stated failure action for each field.
- A one-paragraph diagnosis of the version discrepancy naming the most likely cause first.

## Assessment rubric
- **Minimum pass**
  - Query design matches analysis goal and data shape, with at least one quantitative estimate.
  - Provenance requirements are explicit, actionable, and attached to the artifact rather than the notebook.
  - Bottlenecks are identified with one realistic mitigation.
- **Strong performance**
  - Separates exploratory and production query paths and says which rules apply to each.
  - Quantifies tradeoffs across latency, dollar cost, and reproducibility, and names the assumption behind each number.
  - Identifies version drift as the first hypothesis for the discrepancy, before code bugs.
  - Anticipates failure recovery and rollback needs, including what happens when a materialization is superseded mid-analysis.
- **Common failure modes**
  - Index choices disconnected from query workload.
  - Missing version metadata in outputs.
  - Optimization attempts without a benchmark baseline.
  - Sizing that counts only the raw volume and ignores derived products and egress.

## Scale context: real-world numbers

To ground the abstract concepts, here are the data scales learners will encounter:

| Dataset | Raw volume | Neurons | Synapses | Storage |
|---------|-----------|---------|----------|---------|
| MICrONS (minnie65) | 1 mm³ mouse V1 | ~80,000 | ~500M | ~2 PB |
| H01 | ~1 mm³ human temporal cortex | ~57,000 cells | ~150M | ~1.4 PB |
| FlyWire | Whole adult Drosophila brain | ~139,255 | ~54.5M | ~100 TB |
| MouseConnects (planned) | ~10 mm³ mouse hippocampus | TBD | TBD | >10 PB |

**Teaching point:** "When your synapse table has 500 million rows, a poorly written query doesn't just run slowly — it may not finish at all. Architecture decisions determine whether your science is feasible."

## Key tools and formats

| Tool/Format | Purpose | When to use |
|------------|---------|-------------|
| **Zarr/N5** | Chunked array storage | Volumetric data, cloud-friendly |
| **Neuroglancer precomputed** | Multiscale image pyramids | Web browsing of EM/segmentation |
| **CAVEclient** | Python API for CAVE tables | Synapse queries, annotation access |
| **CloudVolume** | Python API for volumetric data | Image/segmentation chunk access |
| **pandas/Dask** | Tabular data manipulation | Synapse tables, annotation analysis |
| **BigQuery/DuckDB** | SQL on large tables | Complex joins on synapse/annotation tables |

## Common errors and how to recover

- **Your figure's neuron IDs no longer resolve.** Recover by finding the materialization version from the query log, the notebook environment, or the file's creation date; if it is genuinely unknown, re-run against a current pinned version, map the old IDs forward with the platform's lineage facility, and report the churn — how many mapped 1:1, how many split, how many merged. Put the version in the figure caption so this cannot recur.
- **A query that worked on 10,000 rows never finishes on 5 x 10^8.** Recover by killing it and re-running on a 0.1% sample with profiling on. Identify whether the cost is per-row lookups (fix: pre-join once into an extract), unfiltered scans (fix: push the filter server-side), or data movement (fix: move compute to the data). Extrapolate before re-launching.
- **The cloud bill is dominated by requests, not storage.** Recover by counting objects: divide the volume by the chunk size. If the count exceeds roughly 10^6, re-write the layout into sharded files and add a local cache for the subvolumes analysts open repeatedly.
- **An egress charge appears after someone downloads a full segmentation.** Recover by revoking bulk-download access, publishing the derived products (skeletons, meshes, synapse table — under 20 TB combined) as the supported download path, and moving batch compute into the same region as the store.
- **Two collaborators report different synapse counts for the same neuron pair.** Recover by diffing the version pins first, then the cleft-score thresholds, then the code. In practice the first two explain most discrepancies, and debugging code first wastes days.
- **A pipeline re-run silently overwrote the file a published figure was made from.** Recover by restoring from the storage system's versioning or snapshot if enabled; then make outputs immutable by writing to version-stamped paths and treating the output directory as append-only.
- **A materialization is superseded mid-analysis and the old one is scheduled for deletion.** Recover by exporting the specific tables your analysis reads into your own archive with the version in the filename, before the deletion date, and record that archive path in the methods.

## What this module does not cover

- **Imaging and alignment.** How the tiles are produced and registered, and why alignment revisions force re-mapping of every stored coordinate, is [Technical Unit 03]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}) and [Technical Unit 04]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}).
- **The segmentation algorithms themselves.** Affinity prediction, watershed, agglomeration, and flood-filling are [Module 14]({{ '/modules/module14/' | relative_url }}) and [Technical Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}).
- **Proofreading labor and its cost model.** Proofreading time per neuron is heavy-tailed, which makes median-based budgets under-estimate systematically; see [proofreading strategies]({{ '/content-library/proofreading/proofreading-strategies/' | relative_url }}) and [Module 07]({{ '/modules/module07/' | relative_url }}).
- **Statistical inference on the resulting graph.** Null models, motif significance, and effect-size interpretation are [Module 10]({{ '/modules/module10/' | relative_url }}) and [Module 20]({{ '/modules/module20/' | relative_url }}).
- **Cluster operations.** Scheduler configuration, container images, secrets handling, and cost negotiation with vendors are outside scope; this module stops at the architecture decision and its estimated consequence.
- **Specific vendor pricing.** Prices change and differ by contract. The module teaches the shape of the cost — bytes, requests, egress — and expects you to fill in current numbers from the provider you actually use.

## Content library references
- [Reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }}) — End-to-end pipeline architecture
- [Data formats and representations]({{ '/content-library/infrastructure/data-formats/' | relative_url }}) — Volumes, meshes, skeletons, graphs; format specs
- [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}) — CAVE materialization, reproducibility
- [MICrONS visual cortex]({{ '/content-library/case-studies/microns-visual-cortex/' | relative_url }}) — Real-world petascale dataset
- [Journal papers: data storage]({{ '/content-library/journal-papers/data-storage/' | relative_url }}) — Primary literature on formats and scale

## Teaching resources
- Workflow context: [Connectomics Workflow]({{ '/datasets/workflow' | relative_url }})
- Dataset context: [MouseConnects]({{ '/datasets/mouseconnects' | relative_url }})
- Notebook: [Dash Synapse Explorer]({{ '/notebooks/intro/DashSynapseExplorer.ipynb' | relative_url }})
- Quality context: [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})

## References
- Dorkenwald S et al. (2022) "CAVE: Connectome Annotation Versioning Engine." *bioRxiv*.
- Januszewski M et al. (2018) "High-precision automated reconstruction of neurons with flood-filling networks." *Nature Methods* 15(8):605-610.
- Shapson-Coe A et al. (2024) "A petavoxel fragment of human cerebral cortex." *Science* 384(6696):eadk4858.
- Turner NL et al. (2022) "Reconstruction of neocortex." *Cell* 185(6):1082-1100.

## Quick practice prompt
Document one query you use with:
1. data source/version,
2. expected runtime class,
3. one provenance field you currently miss.
