---
layout: dataset
title: "Getting Started with Data"
description: "The opinionated on-ramp from 'the data is public' to 'I have a DataFrame': a four-level ladder, working snippets, the CAVE token walkthrough, and a failure-signature table for when it breaks."
permalink: /datasets/getting-started/
slug: getting-started
track: research-in-action
pathways:
  - research workflow
  - data fluency
summary: "A four-level ladder from browser exploration to imagery cutouts, with the auth walkthroughs, calibration checks, and failure fixes that the tool documentation leaves out."
modality: "Electron microscopy and derived tables"
species: "Mixed"
scale: "Browser queries to terabyte volumes"
access_level: "Public; some routes need a free account token"
use_cases:
  - Data onboarding
  - First notebook setup
  - Version-pinned analysis
  - Troubleshooting access failures
recommended_modules:
  - module02
  - module04
related_tools:
  - ask-an-expert
  - connectome-quality
related_frameworks:
  - education-models
resource_links: []
image: /assets/images/datasets/datasets-index.jpg
last_reviewed: 2026-08-21
maintainer: TBD
use_layout_hero: false
content_type: core
---

# Getting Started with Data

Connectomics has a strange access problem. The data is genuinely public — more
open than almost any comparable field — and yet "getting the data" is the step
where most new teams stall for weeks. This page exists to close that gap: the
gap between *the data is public* and *I have a DataFrame*.

The barrier is not any one tool. It is that the field's data lives in **five
overlapping ecosystems** (CAVE, neuPrint, BossDB, per-project portals, and plain
file downloads), each with its own client, auth story, and vocabulary — and no
single page that tells you which one your question lives in. BossDB solved
hosting; Codex solved browsing; CAVE solved versioned queries. Nobody solved
*routing*, so every newcomer re-derives it by trial and error. This page is the
router.

It is organized as a ladder. **Climb only as high as your question requires** —
most projects on the [Open Problems]({{ '/open-problems/' | relative_url }})
ramps never need Level 3.

> **Rule zero: you almost never need the images.** The published EM volumes are
> petabytes; the *tables derived from them* — neurons, synapses, types, edges —
> are megabytes to a few gigabytes, and they answer most questions. Reach for
> pixels only when your question is literally about pixels (Levels 0 and 3).
> The most common self-inflicted failure in this field is a new student
> attempting to "download the dataset."

## The ladder at a glance

| Level | You get | Install | Account | Typical time to first result |
|---|---|---|---|---|
| **0 — Browse** | Neurons and imagery in the browser | none | none | 10 minutes |
| **1 — Download tables** | The connectome as CSV/Parquet in pandas | `pip install pandas` | none | 30 minutes |
| **2 — Live queries** | Versioned tables, any subset, always current | `caveclient`, `neuprint-python` | free token | 1–2 hours (token setup) |
| **3 — Imagery** | Raw EM and segmentation cutouts | `cloud-volume`, `intern` | mostly none | 1 hour |

And the reverse index — start from what you want:

| You want | Route |
|---|---|
| See a neuron, show a friend, sanity-check a claim | Level 0 (Codex, Neuroglancer, neuPrint web) |
| Degree distributions, motifs, graph algorithms | Level 1 (snapshot tables) |
| "All synapses onto cell type X," reproducible versioned analysis | Level 2 (CAVE / neuPrint) |
| Look at actual tissue: synapses, artifacts, compression, QA | Level 3 (CloudVolume / intern) + Level 0 to view |
| Morphologies / skeletons | Level 1 or 2, then `navis` |
| Functional (activity) data | Per-project portals: MICrONS functional releases, ZAPBench |

## Level 0 — Browse (10 minutes, no install, no account)

Everything else on this page goes better if you have *seen* the data first.

- **[FlyWire Codex](https://codex.flywire.ai/)** — search the fly connectome by
  cell type, region, or ID; view connectivity and 3D renderings. This is the
  fastest "wow" in the field and the reference you'll calibrate against at
  Level 1.
- **[neuPrint](https://neuprint.janelia.org/)** — Janelia's web interface to the
  hemibrain and male CNS connectomes. The query builder teaches you the data
  model (neurons → ROIs → synapse counts) without writing code.
- **[MICrONS Explorer](https://www.microns-explorer.org/)** — curated
  Neuroglancer views into the mouse cortex volume, EM plus segmentation plus
  annotations.
- **[BossDB project pages](https://bossdb.org/projects)** — each hosted dataset
  has a page with a Neuroglancer link and (important for Level 3) the exact
  `bossdb://` path string for programmatic access.

**Done when:** you can drive Neuroglancer — scroll sections, toggle the
segmentation layer, select a cell — well enough to demonstrate a synapse to
someone else. If Neuroglancer feels alien, [Unit 02]({{ '/technical-training/02-brain-data-across-scales/' | relative_url }})
covers the data model it is showing you.

## Level 1 — Download tables (the level that unblocks most projects)

Several flagship connectomes publish **static snapshot tables**: plain files,
no authentication, load with pandas. If your project is graph analysis,
comparative counts, or anything on the
[Open Problems]({{ '/open-problems/' | relative_url }}) ramps that says
"Level 1," you may never need more than this.

**FlyWire (adult female fly brain).** Codex's
[downloads page](https://codex.flywire.ai/api/download) serves the connectome as
compressed CSVs per release: `connections` (pre ID, post ID, neuropil, synapse
count, predicted transmitter), `classification` (cell classes and types),
`labels` (community annotations), plus coordinates and stats.

```python
import pandas as pd

conn = pd.read_csv("connections.csv.gz")          # one row per connected pair
neurons = pd.read_csv("classification.csv.gz")    # one row per neuron

print(len(neurons))              # neuron count for THIS release
print(conn["syn_count"].sum())   # total synapses in the released edge list
```

**Calibrate before you compute anything novel:** your neuron count should match
what Codex displays for the *same release*. If it doesn't, you are about to
build a semester on a filter you don't understand — usually the synapse-count
threshold (edge lists are commonly filtered to pairs with ≥5 synapses, and the
challenge/paper numbers depend on that choice).

**Other no-auth table sources worth knowing:**

- *C. elegans* — the Witvliet et al. developmental connectomes and the classic
  adult wiring diagrams are supplementary spreadsheets and
  [NemaNode](https://nemanode.org/) downloads; the entire nervous system fits in
  memory a thousand times over. The gentlest possible first dataset.
- *Larval Drosophila* (Winding et al. 2023) — adjacency matrices in the paper's
  supplement; 3,016 neurons, ideal laptop scale.
- *Hemibrain and male CNS* — primarily served through neuPrint (Level 2), but
  released snapshot exports exist; check the
  [Janelia FlyEM](https://www.janelia.org/project-team/flyem) resource pages.
- *Model code with data included* — `flyvis` (the released fly visual-system
  model) and [ZAPBench](https://github.com/google-research/zapbench) ship their
  data loaders; `pip install` / clone is the whole access story.

**The one habit to build at this level** — start every notebook with a
provenance cell, because every number you compute is a property of a release,
not of the animal ([why this matters]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }})):

```python
DATASET  = "flywire"          # what
RELEASE  = "<release id>"     # which version — copy it from the download page
ACCESSED = "2026-08-21"       # when
```

**Loading gotcha:** the fly `connections` table is a few million rows. If a
laptop kernel dies loading it, don't upgrade the laptop — pass
`usecols=` for the columns you need and explicit `dtype=`, or use polars.
Connectome tables are long but narrow; RAM problems are almost always dtype
bloat, not data size.

## Level 2 — Live queries with a token (CAVE and neuPrint)

Snapshots are fixed menus. Level 2 is ordering off-menu: *all inputs to this
one neuron*, *every synapse inside this region*, *the same query at two
proofreading versions* (which is exactly what
[on-ramp 1]({{ '/open-problems/' | relative_url }}#onramp-proofreading-budget)
needs). The price is a one-time authentication setup — **the single most common
place newcomers stall, so here it is start to finish.**

### The CAVE token, start to finish

[CAVE](https://www.caveclient.org/) serves MICrONS, FlyWire, and other
CAVE-hosted datasets. Once, per machine:

```python
# pip install caveclient
from caveclient import CAVEclient

client = CAVEclient()
client.auth.get_new_token()   # prints a URL — open it in a browser
```

1. The URL asks you to log in with a **Google account** and shows a token
   string. (For FlyWire you must also have accepted the dataset's terms with
   that same account — do that at flywire.ai first, or the token will
   authenticate you to nothing.)
2. Save it:

```python
client.auth.save_token(token="PASTE_THE_TOKEN_HERE")
```

3. The token lands in a file under `~/.cloudvolume/secrets/`. That is the whole
   trick — every later `CAVEclient(...)` call reads it from there. **On Google
   Colab that filesystem is wiped between sessions**, so either re-run
   `save_token` per session or store the token in Colab's Secrets and save it
   programmatically in your first cell.

Then, real queries against a public datastack:

```python
client = CAVEclient("minnie65_public")        # MICrONS public release

print(client.materialize.get_versions())      # which snapshots exist
client.version = client.materialize.get_versions()[-1]   # PIN one, explicitly

print(client.materialize.get_tables())        # what's queryable
df = client.materialize.query_table("<table name>", limit=1000)
```

Two rules that prevent 90% of Level 2 grief:

- **Pin the version, in code, every time.** Root IDs change when proofreading
  edits merge or split objects. Two tables pulled at different versions will
  *mostly* join — the silent 2% mismatch is how wrong results happen. One
  version, everywhere, recorded in the provenance cell.
- **Query, don't dump.** `query_table` with filters and limits, not a full-table
  pull "to have it locally." The server is the local copy.

### The neuPrint token (easier)

For the hemibrain and the male CNS: log in at
[neuprint.janelia.org](https://neuprint.janelia.org/) with a Google account,
open your account page, copy the **Auth Token**.

```python
# pip install neuprint-python
from neuprint import Client, fetch_neurons, NeuronCriteria as NC

c = Client("neuprint.janelia.org", dataset="<pick from the site's dataset list>",
           token="PASTE_TOKEN")
neurons, counts_by_roi = fetch_neurons(NC(type="KC.*"))   # e.g. Kenyon cells
```

The dataset string (name:version) is shown in the site's dataset switcher —
copy it exactly, and record it in the provenance cell like any other version.

## Level 3 — Imagery cutouts (pixels, when you actually need pixels)

For synapse-by-eye work, artifact hunting, compression experiments, or training
vision models — the on-ramps for
[Problem 2]({{ '/open-problems/' | relative_url }}#onramp-synapse-generalization)
and [Problem 6]({{ '/open-problems/' | relative_url }}#onramp-data-logistics).

**Do the byte math before you download.** EM imagery is `uint8`: a 512³ cutout
is 512³ ≈ 134 million voxels ≈ **134 MB** uncompressed. A 2048³ cutout is 8.6 GB.
Every volume also ships a **mip pyramid** — mip 0 is full resolution, each
higher mip is downsampled — and browsing questions rarely need mip 0.

```python
# pip install cloud-volume
from cloudvolume import CloudVolume

vol = CloudVolume("precomputed://<volume path>", mip=2,
                  use_https=True, progress=True)
print(vol.shape, vol.resolution)                  # know before you pull
cutout = vol[2000:2512, 2000:2512, 1000:1064]     # xyz voxel ranges at this mip
```

Volume path strings are published, not guessed: MICrONS paths are on
[microns-explorer.org](https://www.microns-explorer.org/), H01's on its
[release site](https://h01-release.storage.googleapis.com/landing.html), and
every [BossDB project page](https://bossdb.org/projects) shows its path with a
copyable `intern` snippet:

```python
# pip install intern
from intern import array
em = array("bossdb://<collection>/<experiment>/<channel>")   # copy from the project page
cutout = em[100:164, 5000:5512, 5000:5512]                   # note: z, y, x order
```

Mind the axis-order difference between the two clients — it is the classic
"my cutout is garbage" cause. Ground-truth training volumes (e.g.
[CREMI](https://cremi.org/)'s fly volumes with synapse annotations) are plain
HTTP downloads of manageable size — often the right Level 3 starting point
because they come *with* labels.

## When it breaks: failure signatures

Symptoms first, because that's what you'll actually have:

| Symptom | Likely cause | Fix |
|---|---|---|
| `401 Unauthorized` from CAVE | No token on this machine, or token from an account that never accepted the dataset's terms | Redo the token walkthrough above; for FlyWire, accept terms at flywire.ai with the *same* Google account |
| Auth worked yesterday, fails today on Colab | Ephemeral filesystem wiped `~/.cloudvolume/secrets/` | Re-save the token each session (first cell), or use Colab Secrets |
| "version not found" / "table not found" | Pinned to a pruned materialization, or typo'd table name | `get_versions()` / `get_tables()` and pin something that exists |
| Joins between two tables silently drop rows | Tables pulled at different materialization versions — root IDs moved | One pinned version for every query in the notebook |
| Your neuron/synapse count ≠ the paper's | Different release, or the paper's threshold filter (e.g. ≥5 synapses/edge) | Match release *and* filters; state both next to the number |
| Kernel dies loading a CSV | dtype bloat, not data size | `usecols=` + explicit `dtype=`, or polars |
| Graph algorithms crawl | NetworkX at 10⁵ nodes / 10⁷ edges | igraph or graph-tool; keep NetworkX for prototyping on subgraphs |
| Download runs forever | Pulling imagery at mip 0, or "downloading the dataset" | Byte math first; higher mip; ask whether you need pixels at all (rule zero) |
| SSL / connection errors only on campus | Institutional proxy or firewall | Try another network to confirm, then ask IT to allow the specific endpoints; don't disable TLS verification |

Two failed attempts on the same step is the threshold: stop, write down exactly
what you ran and what it returned, and bring it to
[Ask an Expert]({{ '/ask-an-expert/' | relative_url }}). Access friction is a
known problem in this field; nobody competent will think less of you.

## The 60-minute first contact

The whole ladder, compressed into one sitting. This is step 2 of every
[Open Problems on-ramp]({{ '/open-problems/' | relative_url }}), done together:

1. **(10 min, Level 0)** Open Codex. Search a cell type. Look at one neuron in
   3D. You have now seen the data.
2. **(15 min, Level 1)** Download the current release's `classification` and
   `connections` tables. Load both in pandas.
3. **(10 min, calibrate)** Count neurons; group by superclass. Match your
   numbers against what Codex shows for the same release. Investigate any
   mismatch until you can name the filter that causes it.
4. **(15 min, first real result)** Plot the out-degree distribution on log-log
   axes. You are now doing connectomics —
   [Network analysis methods]({{ '/content-library/connectomics/network-analysis-methods/' | relative_url }})
   tells you what you're looking at.
5. **(10 min, provenance)** Add the provenance cell — dataset, release, date —
   and save the notebook. This notebook is the seed of your project repository.

**Done when** the notebook runs top to bottom on a machine that isn't yours.

## Where this page stops

- **Notebook link farm** — curated example notebooks per platform live at
  [Accessing Public EM Datasets]({{ '/datasets/access/' | relative_url }});
  this page is the route-picker and failure manual, that one is the collection.
- **Dataset choice** — which dataset fits which scientific question is the
  [Datasets]({{ '/datasets/' | relative_url }}) index's job, and each
  [Open Problems]({{ '/open-problems/' | relative_url }}) ramp names its own.
- **Exact commands drift.** Client APIs, release names, and download URLs change
  faster than any static page. The *shapes* here — the ladder, rule zero,
  version pinning, byte math, the failure table — are stable; when a snippet
  disagrees with the client's own documentation, the documentation wins, and a
  correction to this page is a welcome first contribution.
