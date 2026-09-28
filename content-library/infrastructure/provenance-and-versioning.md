---
layout: page
title: "Provenance and Versioning"
permalink: /content-library/infrastructure/provenance-and-versioning/
image: /assets/images/content-library/infrastructure/provenance-and-versioning.svg
image_alt: "Stylized vector art: pipeline stages running above a chunk grid."
description: "What a CAVE materialization version is, why root IDs change and supervoxel IDs do not, which MICrONS versions last, how to query by timestamp, what a methods record must contain, and how version drift fails, worked on the site's MICrONS lab."
topics:
  - provenance
  - versioning
  - reproducibility
  - CAVE
  - materialization
  - root-ids
primary_units:
  - "04"
  - "08"
difficulty: "Advanced"
tags:
  - infrastructure:provenance
  - infrastructure:versioning
  - infrastructure:cave
  - methodology:reproducibility
  - methodology:data-management
  - connectomics:materialization
micro_lesson_id: ml-infra-provenance
combines_with:
  - reconstruction-pipeline
  - data-formats
  - acquisition-qa
content_type: core
---

## Overview

A connectome changes after release. Proofreaders merge and split segments, annotation
tables are added and corrected, and classifiers are rerun. The released MICrONS
segmentation carried 1,046,656 proofreading edits as of 16 September 2024 (MICrONS
Consortium 2025), and editing did not stop there. Every number computed from such a
dataset is a property of one release, not of the animal.

This page is the reference for the versioning model behind that sentence. It defines a
materialization version, explains why root IDs change, lists which MICrONS versions
last and which have expired, shows how to query by timestamp, and works through the
methods record of the site's
[MICrONS real-data lab]({{ '/notebooks/microns-lab/' | relative_url }}) with its real
numbers. The norms this mechanism serves are stated once, on
[Technical Practice]({{ '/hidden-curriculum/technical-practice/' | relative_url }})
(norms 1 to 5), and taught in
[Unit 04 §2]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }})
and its lab. This page does not repeat them. It gives the mechanism and the numbers.

---

## The question provenance answers

This scenario is invented; the release label is fictional. A paper reports that a
circuit motif is enriched 3.2× in a mouse cortex volume at release "Birch". A year later,
another group queries the same volume and finds 1.8×. Is the difference:

(a) a real disagreement about methods;
(b) a change in the data, because proofreading since Birch altered the graph;
(c) a different version of the synapse table;
(d) a software bug in one of the analyses?

Without a recorded version, answering this is detective work and may be impossible.
With one, you can query Birch again (or its timestamp), compare the two graphs, and find
where the results diverged. Unit 04 walks a longer version of this forensics in its
[worked example]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}),
where a caption's input count changes from 1,412 to 1,530 between two fictional
versions because merges attached distal dendrite to the cell.

---

## A materialization version is a snapshot of annotations joined to the segmentation at one timestamp

CAVE, the Connectome Annotation Versioning Engine (Dorkenwald et al. 2025), keeps
three layers apart:

1. **The segmentation** is a graph over immutable supervoxels (below).
2. **Annotations** are rows in database tables. "Every annotation is based on points
   in space (≥1) that serve as spatial anchors." A synapse has a presynaptic point and
   a postsynaptic point; a nucleus has its centroid; a cell-type label has the nucleus
   centroid of the cell it labels. "To associate annotations with segments, the spatial
   points are bound to the underlying supervoxels, which can then be mapped to their
   associated root segment for any point in time using the ChunkedGraph."
3. **Materialization** is the join between the two. The paper introduces "a scheme for
   storing annotations, which binds annotations to segment IDs at specific points in
   time in a process we call 'materialization'." A service "frequently (for example,
   1 per h)" recomputes the root segment under every annotation point. Then, because
   "ongoing proofreading and annotating make the 'live' database unsuitable for
   analysis queries, we create infrequent copies (for example, daily) of it that serve
   as materialized analysis snapshots."

A public materialization version is one of those snapshots, kept and numbered. For the
`minnie65_public` datastack, version 1507 is the snapshot taken at
2025-07-31 08:10:01.117494 UTC. A version is therefore three things at once: a number,
a timestamp, and the set of tables frozen at that timestamp. The number is what you
pass to a client. The timestamp is what you need once the number has expired.

| Frozen in a version | Not frozen |
|---|---|
| The root ID under every annotation point (`pt_root_id`, `pre_pt_root_id`, `post_pt_root_id`) | The supervoxels themselves, which never change in any version |
| The contents of every table at that moment | The edit log, which keeps growing |
| Which root IDs exist | Which versions are still served (versions expire; see below) |
| A cell-type label's value in that table | "Living" correction tables at later versions, which add rows as manual review continues (MICrONS v1718 release manifest) |

"Querying these snapshots ensures consistent queries but prohibits a user's ability to
query the data immediately after fixing a segmentation error" (Dorkenwald et al. 2025).
That is the trade: a version is consistent because it is stale.

---

## Root IDs change on every edit; supervoxel IDs never do

The ChunkedGraph "represents cells as connected components in a supervoxel (groups of
voxels) graph," in a hierarchy "where root nodes are individual cell segments, and leaf
nodes are supervoxels" (Dorkenwald et al. 2025). The larger MICrONS subvolume has
112 billion supervoxels. A merge adds an edge between supervoxels. A split removes
edges, found by a maximum-flow minimum-cut between the two sets of points the
proofreader placed. The voxels are never rewritten.

A root ID is the name of one grouping of supervoxels at one moment. From the caveclient
documentation: "A root id is associated with a particular agglomeration of supervoxels
… A new root id is generated for every new change in the chunkedgraph." The MICrONS
documentation says the same for users: the "18-digit segmentation id or `pt_root_id`
of your neuron or microglia or axon etc. will change every time it is proofread."
Old root IDs are not renamed. They expire. "The `pt_root_id` is always associated with
the same collection of supervoxels, and therefore the same mesh and same skeleton. But
if that `pt_root_id` is expired, then you may not find that object in current
Annotation Tables, Synapse Connectivity Tables, and Neuroglancer views of the current
version of the dataset."

Four consequences follow.

**Tables store both keys.** Every bound point carries `pt_supervoxel_id` and
`pt_root_id`. The supervoxel column is the durable key. The root column is the
materialized lookup for that version.

**Some IDs are static.** A `nucleus_id` from `nucleus_detection_v0` or a synapse `id`
from `synapses_pni_2` names an annotation, not a grouping, so it survives edits. The
MICrONS versioning page: "if you use a static annotation label to index your analysis,
for example a `nucleus_id` or a `synapse_id` which do not undergo proofreading, you can
look up the current `pt_root_id` at any time." The site's lab matches cells across
versions on the nucleus supervoxel ID for this reason.

**Edits leave a lineage.** "The changes are tracked in a lineage graph of the altered
roots" (Dorkenwald et al. 2025). The client exposes it:

```python
from caveclient import CAVEclient
client = CAVEclient("minnie65_public", version=1300)

mat_time = client.materialize.get_timestamp()                 # timestamp of the pinned version
client.chunkedgraph.is_latest_roots([old_root], timestamp=mat_time)
client.chunkedgraph.suggest_latest_roots(old_root, timestamp=mat_time)
client.chunkedgraph.get_lineage_graph(old_root)
client.chunkedgraph.get_root_id(supervoxel_id=sv_id, timestamp=mat_time)
```

**Forward mapping is a guess when a cell was split.** The MICrONS page states the
case plainly: "in the case of a multi-soma object that has been manually split. Which
of the two new cells was your original cell of interest?" `suggest_latest_roots()`
"will make its best guess, given supervoxel overlap." Technical Practice norm 2 asks
you to report how many IDs mapped one-to-one, split, or merged, and, when the original
result must be reproduced exactly, to query the old version instead of mapping forward.

---

## MICrONS keeps three versions long-term and expires the rest

The MICrONS team's policy, from the versioning page read on 26 September 2026: "We
will continue to archive and remove materializations at approximately 1 year after
their release." And: "The following are considered major versions and WILL NOT expire,
and will persist for the foreseable future", followed by v117, v943 and v1300. The release manifests
add: "All publicly released annotation data is available as a static download."

| Version | Snapshot timestamp (UTC) | Status, 26 September 2026 |
|---|---|---|
| 117 | 2021-06-11 08:10:00 | Available; first public release |
| 343 | 2022-02-24 08:10:00 | Expired |
| 661 | 2023-04-06 20:17:09 | Expired |
| 795 | 2023-08-23 08:10:01 | Expired |
| **943** | 2024-01-22 08:10:01 | **Available; major analysis version** |
| 1078 | 2024-06-05 10:10:01 | Expired |
| 1181 | 2024-09-16 10:10:01 | Expired |
| **1300** | 2025-01-13 10:10:01 | **Available; major analysis version** |
| 1412 | 2025-04-29 10:10:01 | Expired |
| 1507 | 2025-07-31 08:10:01 | See below |
| 1621 | 2025-11-25 10:10:01 | Available |
| 1718 | 2026-03-07 08:10:01 | Available |
| 1822 | 2026-06-27 | Latest; not yet in the status table |

Source: the status table on the MICrONS "Materialization and Versioning" page and the
per-version release manifests. The site's
[canonical facts registry](https://github.com/willgray13/neurotrailblazers/blob/main/docs/reviews/2026-09-site-audit/canonical-facts.md)
records the same table with its conflicts.

**v1507 is the version the site's lab pins, and it is in a gray zone.** Its manifest
says "v1507 will expire July 31, 2026." That date has passed. The live version list
needs a token and was not checked, so whether `CAVEclient("minnie65_public",
version=1507)` still works is not established. What is established: the static CSV
exports of v1507 were still served on 26 September 2026 (every file the lab reads
returned HTTP 200), and the lab verifies each file against a SHA-256 hash before it
analyzes anything. If the provider withdraws or changes a file, the lab fails rather
than reporting a different dataset under the v1507 label.

**What to use.** For a live example, pin 943 or 1300. For anything that must be
rerun in a year, either use a major version or archive the static export and its
hashes with your results. In caveclient, `client.materialize.get_versions()` lists
what exists today, and `get_version_metadata()` returns each version's timestamp and
expiry; the documentation says "Each version has a timestamp it was run on as well as
a date when it will expire" and that "Versions have varying expiration times in order
to support the tradeoff between recency and consistency."

Other datasets version too. CAVE hosts "five published datasets," including FlyWire,
FANC, MICrONS and H01, and "tracks almost 2 billion annotations and has recorded over
4 million edits by over 500 unique users" (Dorkenwald et al. 2025). Their numbering
schemes differ; the rule does not.

---

## A timestamp query reaches any moment, including an expired version

CAVE "combines materialized snapshots with ChunkedGraph-based tracking of neuron edit
histories to facilitate analysis queries for arbitrary time points" (Dorkenwald et al.
2025). The client takes the nearest snapshot, applies the annotation changes since it,
and maps the result "back to the query timestamp using the lineage graph and
supervoxel to root lookups." The paper notes that this "introduces an overhead over
querying materialized analysis snapshots directly."

```python
from datetime import datetime, timezone
from caveclient import CAVEclient

client = CAVEclient("minnie65_public", version=1300)   # a long-lived version

# The proofreading table as it stood at the v1507 snapshot,
# addressed by timestamp rather than by version number.
t_1507 = datetime(2025, 7, 31, 8, 10, 1, 117494, tzinfo=timezone.utc)
proof = client.materialize.query_table("proofreading_status_and_strategy",
                                       timestamp=t_1507)
```

Rules from the caveclient documentation: passing `timestamp=` to `query_table` "will
call `live_query` automatically"; all timestamps are UTC; the query "will raise an
`ValueError` exception if the IDs passed in your filters are not valid at the timestamp
given." The MICrONS versioning page shows the same pattern against the timestamp of
v661, a version that has expired. The live route needs a token, and the site's lab did
not exercise it, so check the
[MICrONS CAVE quickstart](https://tutorial.microns-explorer.org/quickstart_notebooks/01-caveclient-setup.html)
before you rely on it in class.

---

## The reproducibility header is five lines, stated once on the site

Unit 04's lab (Part A, step 6) asks for a five-line header on every notebook:
dataset, version, client library version, date, query author. Technical Practice
norm 1 adds where it goes: the version, the query code and the date belong in the
notebook header *and* in the figure caption. The
[dataset getting-started page]({{ '/datasets/getting-started/' | relative_url }})
gives the three-line version for static downloads. One block satisfies all three:

```python
DATASET   = "MICrONS cubic millimeter (minnie65)"
DATASTACK = "minnie65_public"
VERSION   = 1507                                   # never "latest"
TIMESTAMP = "2025-07-31T08:10:01.117494+00:00"     # what a timestamp query needs
TABLES    = ["synapses_with_axon_proofreading", "proofreading_status_and_strategy", "aibs_cell_info"]
CLIENT    = "static CSV exports; pandas 2.3.3, numpy 2.3.5, Python 3.13.5"
RUN_DATE  = "2026-09-26"
AUTHOR    = "your name"
```

The header is the minimum. Norms 2 to 5 on Technical Practice extend it: report ID
churn when you carry IDs across versions (2), record the six graph-construction
decisions (3), emit provenance as structured data from every pipeline stage (4), and
archive the representation one step richer than your endpoint needs (5). The full
form is the methods record, worked next.

---

## Worked example: the MICrONS lab's methods record

The lab asks whether reciprocal connections among proofread MICrONS neurons exceed
three nulls. Its
[`methods_record.json`]({{ '/assets/notebooks/microns-lab/methods_record.json' | relative_url }})
and
[`results_summary.json`]({{ '/assets/notebooks/microns-lab/results_summary.json' | relative_url }})
are archived on the site. The numbers below are read from those files and from the
executed notebook.

**What it pins.** Datastack `minnie65_public`, materialization version 1507,
timestamp 2025-07-31T08:10:01.117494+00:00, accessed as "public static CSV exports,
no account or token." Four data files, each with URL, size in bytes and SHA-256:

| Table | Version | Bytes | SHA-256 (first 16) |
|---|---|---:|---|
| `synapses_with_axon_proofreading` | 1507 | 80,191,720 | `3f0841cafb39531e` |
| `proofreading_status_and_strategy` | 1507 | 69,077 | `d10300976fc3dd5f` |
| `aibs_cell_info` | 1507 | 5,696,726 | `f26299762ef15a78` |
| `proofreading_status_and_strategy` | 1412 | 63,838 | `c580c50da233cb8e` |

The synapse export holds 2,089,627 synapse rows from 2,141 presynaptic cells. The
cell-info export holds 144,120 nucleus rows.

**What it counts.** Inclusion rules in order, with every exclusion counted: 2,182 rows
in the v1507 proofreading table; 2,141 after requiring a proofread axon (41 out);
2,088 after a proofread dendrite (53 out); 2,070 after requiring `valid_id ==
pt_root_id`, that is, no edit since the proofreading was assessed (18 out); 2,070
after requiring exactly one nucleus on the root (0 out); 2,070 after requiring an
excitatory or inhibitory class label (0 out). The final set is 2,070 cells, 1,732
excitatory and 338 inhibitory, with 258,812 synapses among them and 31,542 autapses
dropped. At threshold 1 the graph has 134,753 directed edges and 17,022 reciprocal
pairs, 1.97× the distance × class null's expectation of 8,652.

**What drifted between v1412 and v1507.** The lab compares the proofreading table at
the two versions (93 days apart), matching cells on nucleus supervoxel ID:

| Measure | Count |
|---|---:|
| Cells passing rules 1 to 3 at v1412 | 1,953 |
| Cells passing rules 1 to 3 at v1507 | 2,070 |
| Matched on nucleus supervoxel | 1,942 |
| Only at v1412 (dropped) | 11 |
| Only at v1507 (new) | 128 |
| Matched, but root ID changed | 118 |
| v1412 root IDs absent from the v1507 table | 129 |

The arithmetic is the lesson. 1,942 + 11 = 1,953 and 1,942 + 128 = 2,070, so the
supervoxel match is complete. The 129 absent root IDs are the 11 dropped cells plus the
118 cells that were edited between the snapshots and received new root IDs. A learner
who saved the 1,953 root IDs from v1412 and joined them to the v1507 synapse table
would silently lose 129 cells, 6.6% of the list. No error is raised. The 118 are the
cells that Technical Practice norm 2 tells you to count and report.

**What the rerun showed.** From a fresh virtual environment with an empty cache, the
notebook was run twice each under Python 3.11.14 and 3.13.5 on 26 September 2026. All
four runs produced a byte-identical `results_summary.json` (SHA-256
`d9a218e1d5153dc8…`). The methods record differs across runs only in date, platform
and Python version, which is what a methods record is for: it separates the parts that
should change from the parts that must not. The code hash of the notebook's code
cells, `a50d89761feb6371…`, is in the record too. If yours differs, the code was
edited.

---

## A methods record must contain seven groups of fields

The lab's record is one instance of a general shape. Anything you publish from a
versioned connectome should carry all seven groups, in a machine-readable file next
to the results, not only in prose.

| Group | Fields | In the lab's record |
|---|---|---|
| 1. Data identity | Dataset, datastack, version number, snapshot timestamp, table names | `minnie65_public`, 1507, `2025-07-31T08:10:01.117494+00:00`, three tables |
| 2. Access and integrity | Route (live client or static export), URL per file, bytes, hash, whether the hash was checked | Static exports; SHA-256 per file; `hash_checked: true` for the four data files |
| 3. Selection | Inclusion rules in order with counts excluded at each step; the proofreading level required and its written criteria (norms 12 and 13) | Five rules; 41 / 53 / 18 / 0 / 0 excluded; axon and dendrite status `TRUE`, state current |
| 4. Construction | The six graph decisions (norm 3): detection confidence, synapse threshold, weighting, direction, inclusion, boundary handling; units | Edge if ≥ T synapses, T = 1 primary and 2 sensitivity; directed; autapses dropped; 4 × 4 × 40 nm voxels; no boundary correction |
| 5. Statistics | Every null tried, number of samples, seed, decision rule fixed before running (norm 21), number of tests | Three nulls; 200 samples; seed 20250731; rule stated in the record |
| 6. Code and environment | Commit hash or code hash, package versions, Python version, platform, run date | Code-cell SHA-256; numpy 2.3.5, pandas 2.3.3, Python 3.13.5; macOS 15.7.9 arm64; `run_started_utc` |
| 7. Claim boundary | Data citation and license terms, and the non-claim sentence (norm 7) | Citation string; the lab page's "Non-claim" paragraph |

Sentence templates, with the bracketed parts yours to fill: "All analyses used
`[datastack]`, materialization version `[N]` (snapshot `[timestamp UTC]`), read from
`[route]`; file hashes are in `[methods record]`." "Cells were included if
`[rules, in order]`; `[n]` of `[N]` remained." "A directed edge required ≥ `[T]`
synapses; the result at `[T′]` is in `[table]`." "Code at `[commit]`, run on
`[date]` with `[package versions]`." Session 3 of the four-session teaching block has learners
[repair a methods record]({{ '/teaching/lectures/tools-and-methods-activity/' | relative_url }})
written without these fields, and
[Module 21]({{ '/modules/module21/' | relative_url }}) carries the rubric row.

---

## Version drift fails silently, in these ways

| Failure | What happens | How you notice | What to do |
|---|---|---|---|
| Query against "latest" | The same code answers a different question each week | Usually only when a reviewer or collaborator cannot reproduce a number | Pin a version; put it in the header and the caption (Unit 04 §2) |
| Stale root IDs joined to a newer table | Rows vanish from the join with no error; the lab's case is 129 of 1,953 | Only if you count the join | Match on a static key (nucleus supervoxel, `nucleus_id`, synapse `id`); report the churn (norm 2) |
| Forward mapping across a split | `suggest_latest_roots()` guesses by supervoxel overlap; the other fragment is lost | The lineage graph shows a split | Query the old version or timestamp when the original result must be reproduced exactly |
| Proofread state stale | A cell edited after assessment keeps `status_axon = TRUE` but `valid_id ≠ pt_root_id` | Only if you check the column; 18 cells at v1507 | Filter on `valid_id == pt_root_id`, as the lab does |
| Tables from different snapshots | Root IDs in a synapse table from one version do not match a cell table from another | Empty joins, or worse, partial ones | Take every table from one version, or key on static IDs |
| Version expired | `CAVEclient(..., version=N)` fails, or the version is gone from `get_versions()` | At the next rerun, possibly a year later | Use a major version (943, 1300), a timestamp query, or an archived static export with hashes |
| File changed under the same label | A "v1507" CSV is silently different | Only with a hash check | Hash every input; stop on mismatch, as the lab does |
| Living label tables | Correction tables "will be added as more changes arise from continued manual efforts" (MICrONS v1718 manifest), so a cell's class can change at the same nucleus ID | Compare label tables across versions | Record the table name, its version, and the label source per cell |
| Environment drift | A dependency changes numeric behavior | Byte-level diff of outputs | Pin versions; the lab's outputs were byte-identical across Python 3.11 and 3.13, and a development run with newer packages gave the same reciprocity numbers |

---

## Pipeline provenance: what each stage records

The rules above cover analysis. Upstream, every stage of the reconstruction pipeline
has its own provenance, and Technical Practice norm 4 asks that it be emitted as
structured data and tested like code.
[Unit 04 §4]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }})
lists the fields every stage output records (input IDs, commit, parameters, model hash,
container digest, seeds); the table below is where each stage keeps them.

| Stage | Record |
|---|---|
| Raw ingest | Instrument ID, acquisition date, operator, imaging parameters, per-tile timestamps (see [acquisition QA]({{ '/content-library/imaging/acquisition-qa/' | relative_url }})) |
| Alignment | Input section IDs, software version (commit hash), transform parameters, registration residuals as a distribution with its maximum |
| Segmentation | Input volume version, model artifact hash, inference parameters, software version |
| Agglomeration | Segmentation version, thresholds, software version |
| Synapse detection | Input volume and segmentation version, model ID, detection parameters, software version |
| Proofreading | Editor, timestamp, operation (merge or split), affected supervoxels; CAVE's edit log records these |
| Analysis | The methods record above |

Three implementation patterns coexist: inline metadata on each output (HDF5 or Zarr
attributes, JSON sidecars), a central provenance database, and a workflow manager
(Nextflow, Snakemake, Airflow) that records inputs, outputs and execution metadata.
Production pipelines usually combine them. The
[reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }})
page covers the stages themselves.

---

## Version control for analysis code

Every script or notebook behind a published figure should be under git with the commit
hash recorded next to the result, dependency-pinned (`requirements.txt`, an environment
file, or a container digest), parameterized so that thresholds, seeds and versions are
configuration rather than literals, and deterministic given the same inputs. Unseeded
randomness and non-deterministic GPU operations break the last property; pin seeds and
say when determinism was not achievable.

A container pins the software environment, not the data:

```dockerfile
FROM python:3.11-slim
RUN pip install caveclient==5.14.0 networkx==3.2.1 numpy==1.26.2
COPY analysis/ /app/analysis/
ENTRYPOINT ["python", "/app/analysis/run_motif_search.py"]
```

The pins above show the pattern; pin the versions you ran (caveclient 8.2.1 was the
latest on PyPI on 26 September 2026). Record the image digest with the results. The
image does not keep a materialization version alive, which is why the methods record
carries the data identity separately.

---

## Check yourself

<details markdown="1">
<summary>A colleague's figure caption reads "n = 1,953 proofread neurons, root IDs in Supplementary Table 1." What is missing, and what would you ask for first?</summary>

The version and its timestamp. Root IDs name a grouping of supervoxels at one moment,
and 1,953 is the lab's count at v1412, so the caption is reproducible only if the
reader knows to query v1412 (which has expired) or its timestamp
(2025-04-29 10:10:01 UTC). Ask for the materialization version first. Then ask for the
nucleus IDs, which survive edits, so the cells can be found at any later version. If
the colleague does not know the version, that is itself a finding about the analysis.
</details>

<details markdown="1">
<summary>You rerun the lab in a year and the v1507 download fails. Which of the archived numbers can you still check, and which route gets you the data again?</summary>

All of them, against the archived `results_summary.json`, because the numbers are
frozen with their version. To get the data again: a timestamp query at
2025-07-31 08:10:01.117494 UTC through the live client with a token, or the archived
static export if you kept one with its hashes. Pinning 1300 instead does not
reproduce the v1507 numbers; the proofread set and the root IDs differ, which is
exactly what the drift table measures.
</details>

<details markdown="1">
<summary>Why does the lab match cells across versions on nucleus supervoxel ID rather than on root ID, and why does 11 + 118 = 129 matter?</summary>

Supervoxels are immutable and a nucleus stays in the same supervoxel across edits, so
the match is exact. Root IDs change on every edit, so 118 of the matched cells have
different root IDs at v1507 even though they are the same cells. Add the 11 cells that
left the proofread set and you get the 129 v1412 root IDs that are absent from the
v1507 table. A join on root IDs would drop all 129 without an error. The equation is
the audit: it shows that every missing ID is accounted for by either an edit or an
exclusion, not by a bug.
</details>

---

## Common misconceptions

| Misconception | Reality | Teaching note |
|---|---|---|
| "The connectome is finished" | Proofreading and annotation continue after release, for years | Always cite a version and its timestamp |
| "A root ID identifies a neuron" | It identifies one grouping of supervoxels at one moment; it expires on the next edit | Key on nucleus or synapse IDs; report churn when you carry root IDs forward |
| "Git for code is enough" | Code version means nothing without data version and environment version | Track all three in the methods record |
| "Versions last forever" | MICrONS archives most versions about a year after release; 343, 661, 795, 1078, 1181 and 1412 have expired | Use 943 or 1300 for live examples; archive static exports with hashes |
| "We can always rerun the analysis" | If the version was not recorded, a rerun answers a different question | Pin at analysis time, not after |
| "Provenance is overhead" | The lab's record is one JSON file; its absence costs an afternoon of forensics per question, or the result | Build it into the notebook before the first analysis cell |

---

## Related

- [Unit 04: Volume reconstruction infrastructure]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}), the ChunkedGraph and materialization in the course, with the lab that asks for the five-line header
- [Technical Practice]({{ '/hidden-curriculum/technical-practice/' | relative_url }}), norms 1 to 5, stated once
- [MICrONS real-data lab]({{ '/notebooks/microns-lab/' | relative_url }}) and its archived outputs, the worked example above
- [Tools and methods worksheet]({{ '/teaching/lectures/tools-and-methods-activity/' | relative_url }}), the offline methods-record exercise
- [Module 21: Reproducibility and FAIR principles]({{ '/modules/module21/' | relative_url }})
- [Dataset getting started]({{ '/datasets/getting-started/' | relative_url }}) and [dataset access]({{ '/datasets/access/' | relative_url }}), the provenance cell for static downloads
- [Graph representations]({{ '/content-library/connectomics/graph-representations/' | relative_url }}), the six construction decisions
- [Reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }}) and [data formats]({{ '/content-library/infrastructure/data-formats/' | relative_url }})
- [Neuron type identification]({{ '/content-library/cell-types/neuron-type-identification/' | relative_url }}), why the label source belongs in the same sentence as the count
- [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }}): supervoxel, ChunkedGraph, root ID, materialization, provenance

---

## References

- Dorkenwald S, Schneider-Mizell CM, Brittain D, et al. (2025) "CAVE: Connectome Annotation Versioning Engine." *Nature Methods* 22(5):1112-1120. [10.1038/s41592-024-02426-z](https://doi.org/10.1038/s41592-024-02426-z). PMC12074985.
- MICrONS Consortium et al. (2025) "Functional connectomics spanning multiple areas of mouse visual cortex." *Nature* 640:435-447. [10.1038/s41586-025-08790-w](https://doi.org/10.1038/s41586-025-08790-w).
- MICrONS Explorer tutorial, "Materialization and Versioning" (<https://tutorial.microns-explorer.org/materialization-version.html>) and the release manifests for v1412, v1507, v1621 and v1718 (<https://tutorial.microns-explorer.org/release_manifests/>), read 26 and 27 September 2026.
- CAVEclient documentation, "Materialization" and "ChunkedGraph" guides (<https://caveclient.readthedocs.io/en/latest/>), read 27 September 2026.
- Dorkenwald S et al. (2024) "Neuronal wiring diagram of an adult brain." *Nature* 634:124-138. [10.1038/s41586-024-07558-y](https://doi.org/10.1038/s41586-024-07558-y).
- Wilkinson MD et al. (2016) "The FAIR Guiding Principles for scientific data management and stewardship." *Scientific Data* 3:160018. [10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18).
- NeuroTrailblazers MICrONS real-data lab, archived outputs `methods_record.json`, `results_summary.json`, the executed notebook and the rerun log, run 26 September 2026.
