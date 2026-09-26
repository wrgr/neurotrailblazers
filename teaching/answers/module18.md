---
layout: page
title: "Module 18: model responses"
permalink: /teaching/answers/module18/
slug: module-answers-18
content_type: delivery
description: "Artifact triage, threshold reasoning, a preprocessing pipeline, QC values computed from the Module 18 kit tables and an exemplar release note."
---

[Learner worksheet]({{ '/assets/worksheets/module18/module18-activity.md' | relative_url }}) · [Module 18 kit]({{ '/assets/kits/module18/README.md' | relative_url }}) · [Session kit]({{ '/teaching/sessions/module18/' | relative_url }}) · [Module page]({{ '/modules/module18/' | relative_url }}) · [All model responses]({{ '/teaching/answers/' | relative_url }})

This page answers every section of the Module 18 worksheet in order. It uses two
sources, kept separate:

- **The scenario's illustrative figures**: 4.2 million synapse rows, 120,000 segments,
  8,400 classified neurons, 12% below confidence 30, 35,000 small segments, 847 boundary
  segments and 23 unmatched IDs. These are not measurements from a MICrONS release.
  The key uses them for policy reasoning and the arithmetic they support.
- **The [Module 18 kit]({{ '/assets/kits/module18/README.md' | relative_url }})**: 30,450
  synapse rows, 2,000 segments and 407 cell-type annotations, all synthetic. These tables
  are the learner's working data. Every histogram, edge count, dashboard value and
  retention figure below was computed from the kit files with Python's standard library.

This page is public and suitable for formative assessment.

## Before you start

The prerequisites are dataframe handling and familiarity with segmentation and
proofreading outputs. A learner without Python can complete every task in pseudocode
and read the kit's CSV files in a spreadsheet.

## Questions this module answers

1. **What preprocessing decisions materially change biological conclusions?** The
   synapse confidence threshold, segment inclusion rules and the boundary policy. Each
   changes graph density, degree and which cells remain.
2. **How do we separate data repair from data distortion?** Tie each step to a named
   artifact, measure what it removed, and check whether it removed one cell type or
   region more than others.
3. **What metadata is required to make preprocessing reproducible?** Input dataset and
   materialization version, every parameter, code commit, run date and operator, and a
   hash or row count for each output.

## The task

### 1. Artifact triage

On the scenario's illustrative figures:

| Issue | Scenario figure | Likely impact | Policy |
|---|---|---|---|
| Low-confidence synapses | 12% of 4,200,000 = **504,000** rows below 30 | High. They add or strengthen edges and change density and motif counts. | Apply a documented confidence threshold. Report the result at a second threshold. |
| Small segments | **35,000** of 120,000 (29.2%) with fewer than 2 synapses | Moderate for node counts and degree distributions; low for edges among proofread cells. | Exclude from the neuron node table. Keep them in a fragment table so synapses onto them are counted as “partner unassigned,” not deleted. |
| Boundary segments | **847** intersect the bounding box | High for per-neuron counts and completeness; truncated arbors have artificially low degree. | Flag, do not delete. Analyze with and without them. |
| Unmatched IDs | **23** IDs in the synapse table but not the segment table | Small in rows, but a blocking integrity failure. It suggests the tables come from different versions. | Stop. Confirm that all three tables were queried at the same materialization. Re-query if not. If mismatches persist, quarantine those rows and report the count. |

The worksheet calls the 23 IDs “orphan IDs.” The module's concept set uses “orphan” for
segments with no synapses. These are different problems: the 23 are missing foreign
keys; orphan fragments are debris. Credit a learner who separates them.

Only 8,400 of 120,000 segments (7%) carry a cell-type label. Any cell-type result
describes that labeled subset.

The kit has the same issues plus three the scenario does not list: **447 exact duplicate
rows and 3 synapse IDs with conflicting versions**, **115 autapses** (pre equals post) and
**56 of 407 neurons (13.8%) with a blank cell-type label**. It also has 300 rows whose
endpoints (286 distinct IDs) are missing from the segment table.

### 2. Threshold justification

**The scenario (illustrative units).** Candidates of 30 and 50. At 30, the scenario
gives the effect: 504,000 rows removed and 3,696,000 retained. The effect at 50 cannot be
computed from the scenario, which states only the fraction below 30. The module text
calls a score above 50 common practice. Neither number is a universal rule, and a
threshold does not transfer between tables with different score scales.

**The kit (cleft score 0–255).** The kit makes the point concrete. After the integrity
steps in section 3, the score histogram is bimodal. A low mode peaks at scores 32–39
(962 rows), a high mode peaks at 144–151 (2,288 rows), and the trough is at **64–71 (428
rows)**. The scenario's 30 and 50 would cut inside the low mode: 6.8% and 14.4% of rows
fall below them, and most of the low mode survives.

- **Candidate 64**, the trough: removes 5,315 of 29,589 rows (18.0%). The graph among the
  407 neurons keeps 2,231 directed edges. The low mode is concentrated on debris: rows
  touching a segment under 1 µm³ drop from 2,905 to 178.
- **Candidate 96**, conservative: removes 7,638 rows (25.8%) and keeps 2,013 edges,
  **9.8% fewer** than at 64. It cuts into the high mode, so true synapses with moderate
  scores are lost.
- **Preferred: 64**, placed at the trough with its histogram shown, with 96 reported as a
  sensitivity run. A learner who prefers the higher value for motif analysis, where false
  positives do the most harm, is also correct if the reason is stated.

**Segment inclusion.** The scenario uses fewer than 2 synapses (35,000 segments). Each
such segment has at most one synapse participation, so excluding all of them affects
**at most 35,000 rows**, about 0.83% of 4.2 million. The signal lost is partner identity
for synapses onto unreconstructed pieces of real cells, not small neurons.

In the kit, that synapse-count rule catches only 16 of 2,000 segments. The debris tail is
visible in volume instead: **663 segments are under 1 µm³**, and none has a soma. The
smallest soma-bearing segment is 201 µm³; the largest segment without a soma is 98.7 µm³.
A volume rule of 1 µm³ removes debris without touching any neuron here. On real data,
check that compact interneurons survive whatever volume rule is used.

### 3. Preprocessing pipeline

```text
0. Record: dataset, materialization version, query date, code commit, operator.
1. Ingest: load synapse, segment and cell-type tables at the same version.
   Check schemas, row counts and checksums.
   a. drop exact duplicate rows                       (kit: 447)
   b. resolve conflicting rows for one synapse ID by rule:
      keep the version whose endpoints exist and differ (kit: 3 IDs)
   GATE A: every synapse endpoint exists in the segment table
           (scenario: 23 IDs; kit: 298 rows after steps a-b) -> STOP, re-query,
           then quarantine and log any remainder.
   GATE B: no duplicate synapse IDs; no conflicting cell-type labels.
2. Screen: plot the score histogram and find the trough; plot segment volume on a
   log scale; flag boundary contact; tabulate cell types, including blanks.
3. Clean, logging rows removed per step:
   a. remove autapses from the graph and report them  (kit: 113 after step 1)
   b. drop synapses with score below T_conf           (kit: primary 64; sensitivity 96)
   c. move debris segments to a fragment table        (kit: volume < 1 um^3, 663)
   d. mark boundary segments (keep, with flag)        (kit: 88 of 407 neurons)
   e. convert voxel coordinates to nm using the dataset's resolution metadata
4. QC: compare pre/post synapse rows, edges, mean degree, density, synapses per
   neuron and cell-type fractions.
   GATE C: no cell type's retained fraction differs from the overall retained
           fraction by more than 3 percentage points; otherwise flag, do not drop.
5. Package: cleaned tables, fragment and quarantine tables, decision log, QC report,
   release note, code commit and output hashes.
```

The autapse policy is a stated choice. In a segmentation, pre equal to post more often
signals a merge or a detection error than a biological autapse, so removing them from
the graph and reporting the count is defensible. Keeping them as flagged rows is also
defensible if the policy says so.

### 4. QC comparison

**Scenario arithmetic** (illustrative figures):

| Metric | Pre | Post | Note |
|---|---|---|---|
| Synapse rows | 4,200,000 | 3,696,000 at threshold 30 | 504,000 removed (12%). At most 35,000 more lose partner identity when small segments move to the fragment table. |
| Segments in node table | 120,000 | 85,000 | 35,000 moved to the fragment table. 847 boundary segments flagged, not removed. |
| Mean synapse participations per segment | 2 × 4,200,000 / 120,000 = **70** | — | Each synapse has two partners. This is not a graph degree. |

Mean degree, density and cell-type fractions need an edge list and a label breakdown,
which the scenario does not supply. The kit does.

**Kit QC dashboard** (policy of section 3, threshold 64):

| Metric | Before | After | Gate | Pass/fail |
|---|---|---|---|---|
| Synapse rows | 30,450 | 24,274 (79.7%) | — | — |
| Duplicate rows | 447 exact, plus 3 conflicting IDs | 0 | 0 | Pass after cleaning |
| Autapses | 115 | 0 in graph | stated policy | Pass |
| Endpoints not in segment table | 300 rows (286 IDs) | 0 (298 quarantined) | 0 | **Fail at ingest**; pass only after quarantine is reported |
| Segments below debris threshold (1 µm³) | 663 | 0 in node table | stated policy | Pass |
| Neurons touching the boundary | 88 of 407 | 88, flagged | stated policy | Pass (flagged) |
| Mean synapses per neuron | 36.5 | 30.8 | — | — |
| Directed edges among 407 neurons | 2,485 (plus 32 self-loops) | 2,231 | — | — |
| Mean out-degree | 6.11 | 5.48 | — | — |
| Density, E / (N(N − 1)) | 0.0150 | 0.0135 | — | — |
| Fraction of each cell type remaining | — | 100% under the flag policy | Gate C | Pass |

Mean synapses per neuron counts rows with a neuron on either side, divided by 407. The
raw graph counts the 32 autapse pairs as self-loops, which the density formula
excludes. Report the definition with the number.

**Why boundary cells are flagged, not dropped.** If the 88 boundary neurons were
excluded, the retained fractions would be:

| Class | Before | After exclusion | Retained |
|---|---|---|---|
| L2/3 pyramidal | 96 | 81 | 84.4% |
| Martinotti | 39 | 32 | 82.1% |
| VIP | 21 | 17 | 81.0% |
| Basket | 44 | 35 | 79.5% |
| L4 excitatory | 74 | 57 | 77.0% |
| Blank label | 56 | 42 | 75.0% |
| L5 pyramidal | 77 | 55 | **71.4%** |
| All neurons | 407 | 319 | 78.4% |

L5 pyramidal retention is 7.0 points below the overall rate, and L2/3 is 6.0 above.
Exclusion fails Gate C and would change the composition being analyzed.

### 5. Release note

> **Input.** The scenario's export, cited as its stated materialization. Its figures are
> illustrative; the worked values come from the synthetic Module 18 kit tables
> (`noisy_synapses.csv`, `segments.csv`, `cell_types.csv`), identified by file hash.
>
> **Transforms and parameters.** Exact duplicates removed (447); 3 conflicting synapse
> IDs resolved to their valid version; 113 autapses removed from the graph and reported;
> 298 rows with missing endpoints quarantined; cleft score at least 64, the histogram
> trough (sensitivity run at 96); 663 segments under 1 µm³ moved to a fragment table;
> 88 boundary neurons flagged and retained.
>
> **Code.** Repository and commit hash recorded at run time. [This key does not invent a
> hash; the learner's note must carry the real one.]
>
> **QC calls.** Gate A (endpoints): **fail** at ingest. Release proceeds only with the
> 298 quarantined rows reported, and would be blocked on real data until a re-query
> explains them. Gate B (duplicates): pass after cleaning. Low-confidence screen: 18.0%
> of rows fall below the chosen threshold, above the module's 5% investigate trigger, so
> the histogram was inspected before a threshold was chosen. Gate C (cell-type
> retention): pass under the flag policy; the exclusion alternative fails.
>
> **Residual risks.** Boundary neurons have truncated arbors, so their degrees are
> underestimated. Synapses onto debris lack a partner cell. The threshold removes some
> true synapses from the low tail of the high mode. 56 neurons have no cell-type label,
> so type-level results cover 351 of 407 neurons.

## Working checklist

The five stages map to the pipeline: ingest and integrity (steps 0–1), screening
(step 2), cleaning transforms (step 3), QC and drift checks (step 4) and release
packaging (step 5).

## Evidence and reasoning

| # | Claim | Evidence | Limitation / what would change my mind |
|---|---|---|---|
| 1 | The export is not release-ready as received. | 300 synapse rows (286 IDs) have endpoints missing from the segment table; in the scenario, 23 IDs. | A re-query at one version that resolves them lifts the block. |
| 2 | Excluding boundary neurons would bias composition. | L5 pyramidal retention would be 71.4% against 78.4% overall. | Flagging keeps them but leaves their degrees underestimated. |
| 3 | The confidence threshold materially changes the graph. | Moving from 64 to 96 removes 9.8% of edges among neurons. | The kit has no reference annotation, so which threshold is closer to the truth is not measured. |

**Confidence:** Medium. The kit values are exact for these files, but the kit is
synthetic and has no independent reference for synapse truth.

**Alternative considered and rejected:** drop the rows with missing endpoints and
continue. Rejected because a version mismatch would also affect rows that happen to
match.

## Misconception self-check

Feedback for each error:

- **“Raw data is always better.”** Ask: “Which artifact in the raw table would change
  your density estimate?” The question is how to clean transparently.
- **There is one correct threshold.** Ask for the result at a second threshold. A
  conclusion that holds at only one value is fragile. The scenario's 30 does not even
  land in the kit's trough.
- **More filtering is always better.** Point to the retention table. Excluding boundary
  cells changed composition.
- **Git notes are enough.** Ask: “Which data version did this commit process?” Code
  history without data lineage cannot reproduce the table.
- **Documenting afterward is fine.** Ask for the row counts removed at each step. A
  reconstructed log usually lacks them.
- **Metrics without thresholds are QC.** Ask what action each metric triggers.

## Session timing (facilitator reference)

This section has no learner task. The 08:00–18:00 demonstration can use the kit's score
histogram to show the bimodal shape and the trough at 64–71, and the volume histogram to
show the debris tail.

## Rubric

A self-assessment that matches this exemplar:

- **Strongest part:** every gate names an action, and the threshold sits at a trough
  shown in the histogram.
- **Weakest part:** no reference annotation exists to say which threshold is closer to
  the truth. **Next action:** state that as a limitation rather than implying the
  threshold is validated.

## Exit prompt

Using the kit's tables:

1. **Cleaning rules.** Drop synapses with cleft score below 64 because the low mode of
   the bimodal histogram is concentrated on debris. Move segments under 1 µm³ to a
   fragment table because the volume tail is segmentation debris with no somata. Remove
   autapses from the graph because pre equal to post usually signals a merge or
   detection error.
2. **QC thresholds.** Zero rows with missing endpoints, or stop and re-query, because a
   version mismatch corrupts partner identities. No cell type's retention more than 3
   points from the overall rate, or flag instead of drop, because uneven loss changes
   the composition being studied.
3. **Sensitivity, ±20% on the primary threshold of 64.** At 51: 2,284 edges (+2.4%). At
   64: 2,231. At 77: 2,165 (−3.0%). Report whether the main conclusion survives across
   that range.
4. **Remaining limitation.** Degrees of the 88 flagged boundary neurons are
   underestimated, so any comparison of degree by position is confounded with distance
   from the volume edge.

## Peer review (swap worksheets)

A reviewer should rerun the partner's threshold on the kit tables and check that the
row and edge counts match. A good question: “If you had kept the scenario's threshold of
30, how much of the low mode would remain?”

## Feedback guide

This key follows the kit's own tiers.

- **Minimum pass:** explicit, justified, reproducible cleaning decisions; QC metrics
  with thresholds tied to actions; version, commit and parameters in the release.
- **Strong:** separates low-risk cleanup from biologically sensitive transforms;
  includes a sensitivity analysis; states what signal may have been lost.
- **Common failures:** silent edits with no log; filtering that removes real variation
  without saying so; metrics with no thresholds; no version or commit.

Do not reward a clean-looking release that dropped the rows with missing endpoints
without comment. Do not reward copying the scenario's threshold of 30 onto the kit's
0–255 score without looking at the histogram. Accept any defensible threshold with a
stated reason and a sensitivity run. Small differences in row counts are acceptable when
a learner's duplicate or autapse rule differs and says so. This is a local teaching
rubric, not a validated assessment instrument.

See [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }})
for version records. Teaching material: CC BY-SA 4.0, NeuroTrailblazers.
