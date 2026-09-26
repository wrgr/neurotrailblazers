---
layout: page
title: "MICrONS Real-Data Lab"
description: "A version-pinned MICrONS notebook that asks whether reciprocal connections among proofread neurons exceed three nulls. It needs no account, and its archived outputs let you check a rerun."
permalink: /notebooks/microns-lab/
slug: microns-lab
use_layout_hero: false
content_type: path
---

<div class="main-content">

<section class="section" markdown="1">

# MICrONS Real-Data Lab

This is the real-data version of two offline exercises: the pinned-snapshot query in the
[Tools and Methods worksheet]({{ '/teaching/lectures/tools-and-methods-activity/' | relative_url }})
(Session 3) and the reciprocity-versus-null analysis in the
[Algorithms and Applications worksheet]({{ '/teaching/lectures/algorithms-and-applications-activity/' | relative_url }})
(Session 4). The reasoning is the same. What changes is that the data, the version and
the exclusions are all real.

**Question.** Among MICrONS neurons whose axon and dendrite were both proofread, are
reciprocal connections (A→B and B→A) more common than expected under a null that holds
cell classes and soma-to-soma distances fixed?

**Files.**
[Notebook (`microns-lab.ipynb`)]({{ '/notebooks/microns-lab/microns-lab.ipynb' | relative_url }})
· [Pinned requirements]({{ '/notebooks/microns-lab/requirements.txt' | relative_url }})
· [Executed reference notebook]({{ '/assets/notebooks/microns-lab/microns-lab-executed.ipynb' | relative_url }})
· [Archived outputs](#archived-outputs)

> **Data citation, required by the providers.** The MICrONS Consortium et al. (2025),
> "Functional connectomics spanning multiple areas of mouse visual cortex," *Nature*
> 640: 435–447. Data from [www.microns-explorer.org](https://www.microns-explorer.org).
> The proofreading and cell-type tables have their own papers. Cite them from the
> [MICrONS annotation-table reference](https://tutorial.microns-explorer.org/annotation-tables.html)
> if you publish anything from this lab.

</section>

<section class="section" markdown="1">

## Data source and exact version

| Item | Value |
|---|---|
| Dataset | MICrONS cubic millimeter, mouse visual cortex (`minnie65`) |
| Datastack | `minnie65_public` |
| Materialization | **v1507**, timestamp 2025-07-31 08:10:01 UTC |
| Drift comparison | v1412 (2025-04-29), proofreading table only |
| Access | Public static CSV exports on Google Cloud Storage. No account needed. |
| Base URL | `https://storage.googleapis.com/mat_dbs/public/minnie65_phase3_v1/v1507/` |
| URLs checked | 26 September 2026. Every file listed below returned HTTP 200 without credentials. |
| Download size | About 86 MB on the first run, then cached |

The notebook reads four files, plus a small header file for each:

| Table | File | Size | SHA-256 (first 16) |
|---|---|---:|---|
| Synapses from proofread axons | `v1507/synapses_with_axon_proofreading.csv.gz` | 80.2 MB | `3f0841cafb39531e` |
| Proofreading status and strategy | `v1507/proofreading_status_and_strategy_merged.csv.gz` | 69 KB | `d10300976fc3dd5f` |
| Cell information (class, area) | `v1507/aibs_cell_info_merged.csv.gz` | 5.7 MB | `f26299762ef15a78` |
| Proofreading status, earlier version | `v1412/proofreading_status_and_strategy_merged.csv.gz` | 64 KB | `c580c50da233cb8e` |

The full hashes are in the notebook's parameter cell and in the archived
[methods record]({{ '/assets/notebooks/microns-lab/methods_record.json' | relative_url }}).
The notebook stops if a downloaded file does not match its hash. If that happens,
the provider has changed the file, so do not report results under the v1507 label.

**Why this path and this version.** Two routes to MICrONS were checked on 26 September
2026. The live CAVE API
(`minnie.microns-daf.com`, used by `caveclient`) redirected every unauthenticated
request to a login, so it needs a token. The static exports described on the
[MICrONS static-repositories page](https://tutorial.microns-explorer.org/static-repositories.html)
needed nothing. Version 1507 is the only version whose export includes the 80 MB
**synapses-from-proofread-axons** table. At the long-term-support versions (117, 943,
1300), the only synapse export is the full table, about 20 GB compressed, which is too
large for a class. The
[MICrONS versioning page](https://tutorial.microns-explorer.org/materialization-version.html)
announced that v1507 would expire from the live CAVE service on 31 July 2026, and that
date has passed. This lab does not depend on the live service. The v1507 static exports
still downloaded on 26 September 2026 (HTTP 200), but the providers may withdraw them.
If they do, the download or the hash check will fail instead of silently analyzing
something else, and the [archived outputs](#archived-outputs) on this page remain the
reference for the v1507 results.

</section>

<section class="section" markdown="1">

## Account and access requirements

**For the reference run: none.** You do not need a CAVE account, token, Google login
or cloud credentials. You do need outbound HTTPS to `storage.googleapis.com`. Some
campus or corporate networks block it; if yours does, use the offline fallback below.

**Optional extension: live queries with a CAVE token.** Rebuilding the full graph at a
second version, or querying synapses for cells outside this export, requires
`caveclient` and a free token. The route below was not exercised for this lab, so
check it against the
[MICrONS CAVE quickstart](https://tutorial.microns-explorer.org/quickstart_notebooks/00_cave_quickstart.html)
before class:

1. `pip install caveclient`, then in Python: `from caveclient import CAVEclient`.
2. Run `CAVEclient().auth.setup_token(make_new=True)`. It prints a URL. Open it and
   sign in with a Google account to receive a token.
3. Save the token with `CAVEclient().auth.save_token(token="…")`. Never paste a
   token into a shared notebook.
4. Connect with `CAVEclient("minnie65_public", version=1300)`, or `version=943`.
   These are the two versions the MICrONS team keeps as long-lived analysis versions.
   Do not use `version=1507` for live queries: it was scheduled to leave the live
   service on 31 July 2026. To query the live database as it stood at v1507, pass
   `timestamp=datetime(2025, 7, 31, 8, 10, 1, 117494, tzinfo=timezone.utc)` instead of
   a version. Accept the dataset terms of service if you are prompted.

A live query at v1300 or v943 will not reproduce the v1507 numbers below: the
proofread set and the root IDs differ between versions. This lab's analysis version
stays v1507.

If learners need tokens, get them working in the week before the lab, not during it.

</section>

<section class="section" markdown="1">

## Install and run

Tested with Python 3.11 and 3.13. Any Python from 3.11 to 3.13 should work with these
pins.

```bash
python3 -m venv microns-lab-env
source microns-lab-env/bin/activate          # Windows: microns-lab-env\Scripts\activate
pip install -r requirements.txt
jupyter nbconvert --to notebook --execute --output microns-lab-run.ipynb microns-lab.ipynb
```

Run the last command from the folder that contains `microns-lab.ipynb`. The notebook
hashes its own code cells from that file. To work through it interactively, also
install JupyterLab (`pip install jupyterlab`) or open it in VS Code. The interactive
editor is not part of the pinned set and does not affect results.

| Setting | Default | Environment variable |
|---|---|---|
| Download cache | `~/.cache/neurotrailblazers-microns-lab` | `MICRONS_LAB_CACHE` |
| Output folder | `outputs/` beside the notebook | `MICRONS_LAB_OUTPUT` |

On the test machine, an Apple M4 Max, a run took about 40 seconds with an empty
cache and 22 seconds with a warm one. Peak memory was 1.2 GB. Expect several minutes
on an older laptop or a slow connection, and have at least 2 GB of free memory.

</section>

<section class="section" markdown="1">

## What the notebook does

1. **Parameters.** One cell holds the version, thresholds, bin width, seed and
   decision rule. A non-integer version, such as `"latest"`, is refused.
2. **Download and verify** each file against its SHA-256 hash.
3. **Inclusion rules**, applied in order with every exclusion counted:
   1. axon proofread (`status_axon == 't'`);
   2. dendrite proofread (`status_dendrite == 't'`);
   3. proofread state current (`valid_id == pt_root_id`), so the cell was not edited
      after its proofreading was assessed;
   4. exactly one nucleus on the root ID, which drops fragments and merges;
   5. `broad_type` is excitatory or inhibitory.
4. **Graph construction.** Synapses between two included cells are counted per
   ordered pair, and autapses are dropped. An edge needs at least 1 synapse in the
   primary analysis and at least 2 in the declared sensitivity analysis.
5. **Descriptive endpoint.** Fraction of ordered pairs connected, for each E/I class pair.
6. **Primary endpoint.** The count of reciprocal pairs, plus the reciprocated-edge
   fraction. Both are compared with three nulls, using 200 Monte Carlo samples each and
   a fixed seed:
   - a **uniform fixed-edge-count** null, the Session 4 null, which fixes only nodes
     and edge count;
   - a **soft configuration (Chung–Lu)** null, which keeps each cell's in- and
     out-degree in expectation;
   - a **distance × class** null, which keeps the connection probability for each
     class pair in 25 µm soma-distance bins.
7. **Decision rule**, fixed before the nulls were run. Reciprocity counts as
   *enriched* only if the upper-tail p is 0.05 or less under the distance × class null
   at threshold 1, **and** the observed/expected ratio is above 1 at threshold 2.
8. **Second sensitivity analysis.** Repeat the primary analysis on the cells whose
   axons were *fully* extended.
9. **Version drift.** Compare the proofreading table at v1412 and v1507, matching
   cells on nucleus supervoxel ID, which survives edits, instead of root ID, which
   does not.
10. **Methods record and outputs**, written to `outputs/`.

**An honest note on "pre-registered."** The lab author fixed the endpoint and decision
rule before running any null comparison. That was not before opening the data: table
structure and raw counts had already been inspected. Learners should treat the rule
as fixed for their own run. It is not a preregistered scientific hypothesis.

</section>

<section class="section" markdown="1">

## Expected outputs (reference run, 26 September 2026)

### Inclusion

| Step | Cells remaining | Excluded |
|---|---:|---:|
| All rows in the v1507 proofreading table | 2,182 | — |
| 1. Axon proofread | 2,141 | 41 |
| 2. Dendrite proofread | 2,088 | 53 |
| 3. `valid_id == pt_root_id` | 2,070 | 18 |
| 4. Exactly one nucleus | 2,070 | 0 |
| 5. Excitatory or inhibitory | 2,070 | 0 |

The final set has **2,070 cells: 1,732 excitatory and 338 inhibitory**. By area, 1,854
are in V1, 156 in RL, 59 in AL and 1 in LM. The class labels come from four source
tables. A manual V1-column reference supplies 1,341 labels, and classifiers supply the
rest. Among the included cells there are 258,812 synapses; another 31,542 autapses
were dropped.

### Connection fraction by class pair

| Pre → post | Threshold 1 | Threshold 2 |
|---|---:|---:|
| E → E | 0.0137 | 0.0013 |
| E → I | 0.0531 | 0.0166 |
| I → E | 0.0877 | 0.0451 |
| I → I | 0.0986 | 0.0497 |

### Reciprocity against three nulls

| Analysis | Edges | Reciprocal pairs | Reciprocated-edge fraction | Null | Expected | Observed / expected |
|---|---:|---:|---:|---|---:|---:|
| Threshold 1 | 134,753 | 17,022 | 0.253 | Uniform | 2,120 | 8.03 |
| | | | | Chung–Lu | 8,105 | 2.10 |
| | | | | Distance × class | 8,652 | **1.97** |
| Threshold 2 | 45,774 | 5,542 | 0.242 | Uniform | 245 | 22.7 |
| | | | | Chung–Lu | 2,200 | 2.52 |
| | | | | Distance × class | 1,821 | **3.04** |
| Fully extended axons only (232 cells: 111 E, 121 I), threshold 1 | 6,540 | 1,153 | 0.353 | Uniform | 399 | 2.89 |
| | | | | Chung–Lu | 628 | 1.84 |
| | | | | Distance × class | 771 | **1.50** |

In every row, the observed count exceeded all 200 null samples. The upper-tail p is
therefore 1/201, about 0.005, which is the smallest value 200 samples can report. It
is a floor, not an estimate. **Decision: enriched under the distance × class null.**

**What to take from this.** Against the Session 4 uniform null, reciprocity looks
about 8 times enriched. Holding degree or distance and class fixed absorbs most of
that, and the ratio falls to about 2. Choosing the null changed the effect size
fourfold. The question stayed the same. The direction held under both sensitivity
analyses.

**Non-claim.** This does not show that reciprocity is a wiring rule, or that it
serves a computation. The result is conditional on this proofread set, v1507, and
nulls that ignore axon–dendrite overlap, layer and subtype.

### Version drift, v1412 → v1507

These counts use rules 1–3: both compartments proofread, and the proofread state
current.

| Measure | Count |
|---|---:|
| Cells passing at v1412 | 1,953 |
| Cells passing at v1507 | 2,070 |
| Matched on nucleus supervoxel | 1,942 |
| Only at v1412 | 11 |
| Only at v1507 | 128 |
| Matched, but root ID changed | 118 |
| v1412 root IDs absent from the v1507 table | 129 |

A learner who saved 1,953 root IDs from v1412 and joined them to v1507 synapses would
silently lose 129 cells. Nothing would raise an error. This is Session 3's snapshot
drift with real IDs.

</section>

<section class="section" markdown="1">

## Archived outputs

These are the outputs of the reference run, archived so you can diff your own rerun
against them:

- [`results_summary.json`]({{ '/assets/notebooks/microns-lab/results_summary.json' | relative_url }}): every number above.
- [`methods_record.json`]({{ '/assets/notebooks/microns-lab/methods_record.json' | relative_url }}): version, URLs, file hashes, filters, nulls, seed, code hash, package versions, date.
- [`reciprocity_nulls.csv`]({{ '/assets/notebooks/microns-lab/reciprocity_nulls.csv' | relative_url }}),
  [`class_pair_connectivity.csv`]({{ '/assets/notebooks/microns-lab/class_pair_connectivity.csv' | relative_url }}),
  [`inclusion_exclusions.csv`]({{ '/assets/notebooks/microns-lab/inclusion_exclusions.csv' | relative_url }}).
- [Executed notebook]({{ '/assets/notebooks/microns-lab/microns-lab-executed.ipynb' | relative_url }}) with all outputs.
- [Clean-environment rerun log]({{ '/assets/notebooks/microns-lab/rerun-log.txt' | relative_url }}), with the full `pip freeze`.

**How to compare.** Run `diff` on your `outputs/results_summary.json` and the archived
copy. It should match byte for byte. The methods record will differ only in date,
platform and possibly the Python version. The code hash is
`a50d89761feb6371…`. If yours differs, the notebook's code was edited.

### Rerun evidence

On 26 September 2026 (macOS 15.7, Apple silicon), the notebook was run from a fresh
virtual environment built from `requirements.txt`, with an empty download cache,
twice each under Python 3.11.14 and Python 3.13.5. All four runs produced a
byte-identical `results_summary.json`
(SHA-256 `d9a218e1d5153dc8…`). The CSV outputs were also identical. A development run
with newer packages (NumPy 2.5.3, pandas 3.0.6, Python 3.14) gave the same reciprocity
numbers. The rerun has not yet been tested on Linux or Windows.

</section>

<section class="section" markdown="1">

## Limitations

- **Selection.** Proofread cells were not sampled at random. Most are in or near the
  V1 column, which was proofread first. They were chosen for different projects and
  extended with different strategies. Results describe this set, not cortex.
- **Incomplete axons.** 1,714 of the 2,070 axons are *partially extended*. Missing
  branches remove true edges, and a reciprocal pair can be lost from either side. The
  fully extended subset checks direction. It cannot recover the missing edges.
- **Synapse detection.** Synapses are detected automatically. Single-synapse edges
  are the most exposed to false positives, which is why threshold 2 is reported.
- **Class labels.** Excitatory and inhibitory labels combine manual reference calls
  with classifier predictions. A wrong label moves a cell's pairs into the wrong null
  stratum.
- **Autapses.** 31,542 self-synapses were dropped without investigation. Many are
  probably artifacts.
- **Volume boundary.** Cells near the edge of the volume lose arbor, and connections,
  outside it. No correction is applied.
- **Null scope.** The distance × class null ignores degree, axon–dendrite overlap,
  layer and subtype. The Chung–Lu null ignores distance. Neither fixes both.
  Soma-to-soma distance is only a proxy for opportunity to connect.
- **One version.** Everything is conditional on v1507. The static synapse export
  exists only at v1507, so the drift check covers the inclusion table, not the graph.
- **Monte Carlo floor.** With 200 samples, p cannot go below about 0.005. Report it as
  "p ≤ 0.005", not as an exact value.

</section>

<section class="section" markdown="1">

## Running it in a course

The syllabi keep a real-data lab slot, in week 4 of the 10-week map and week 6 of the
16-week map (see the [syllabus hub]({{ '/teaching/syllabi/' | relative_url }})). This
notebook fills the slot as a 60-minute lab, the real-data version of
[Unit 04]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }})
Part A:

- **10 min.** Read the parameters cell and the inclusion rules. Before running, predict
  which rule will exclude the most cells.
- **20 min.** Run the notebook. Reproduce the inclusion table and the threshold-1
  reciprocity row by hand from the printed numbers.
- **15 min.** Explain why the observed/expected ratio falls from 8 to 2 across the
  nulls. Name one structure no null here holds fixed.
- **15 min.** Write a methods record from memory, then check it against
  `methods_record.json`. Circle anything you missed.

Learners submit the diff of their `results_summary.json` against the archive, their
own methods record, and one sentence that begins "This result is conditional on…".
Those are the reproducibility norms named on
[Technical Practice]({{ '/hidden-curriculum/technical-practice/' | relative_url }}).

### Offline fallback

Use the fallback if the network blocks `storage.googleapis.com`, the hash check fails,
or there is no time to install:

1. The [Session 3 offline query]({{ '/teaching/lectures/tools-and-methods-activity/' | relative_url }}):
   pinned snapshots, an inclusion filter, a methods record and version drift, with no
   packages or network.
2. The [Session 4 toy-graph exercise]({{ '/teaching/lectures/algorithms-and-applications-activity/' | relative_url }}):
   reciprocal pairs against an exactly enumerated null, at thresholds 1 and 2.
3. Unit 04 Part B, the capacity plan, which needs no data.

Then hand out the archived outputs above. Learners can do the interpretation step, and
the null-choice discussion, from `reciprocity_nulls.csv` without running anything.

</section>

</div>
