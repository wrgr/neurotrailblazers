---
layout: page
title: "Module 20: model responses"
permalink: /teaching/answers/module20/
slug: module-answers-20
content_type: delivery
description: "Null models, a counted test family, an error band and a cross-dataset check for the Module 20 E-to-I-to-E loop claim, all computed from the Module 11 and Module 10 kits."
---

[Learner worksheet]({{ '/assets/worksheets/module20/module20-activity.md' | relative_url }}) · [Module 11 kit]({{ '/assets/kits/module11/README.md' | relative_url }}) · [Module 10 kit]({{ '/assets/kits/module10/README.md' | relative_url }}) · [Session kit]({{ '/teaching/sessions/module20/' | relative_url }}) · [Module page]({{ '/modules/module20/' | relative_url }}) · [All model responses]({{ '/teaching/answers/' | relative_url }})

This page answers every section of the Module 20 worksheet in order. It uses the two
datasets the studio names, and both are **synthetic teaching data**:

- **Dataset A**, the [Module 11 kit]({{ '/assets/kits/module11/README.md' | relative_url }}):
  200 neurons, 2,979 synapses collapsed to 1,453 directed edges. This is the dataset in
  which the scenario's team reports enrichment.
- **Dataset B**, the [Module 10 kit]({{ '/assets/kits/module10/README.md' | relative_url }}):
  500 neurons, 11,388 directed edges. This is the generalization check.

Every count, null mean, p-value and interval below was computed from the kit files with
Python 3's standard library (`csv`, `random`, `math`). Null distributions are stochastic;
the values are from one run with `random.Random(20)`, 999 null samples for Dataset A and
499 for Dataset B. A rerun with another seed moves null means by a few tenths and leaves
every conclusion unchanged. No value here describes a real brain. This page is public
and suitable for formative assessment.

**Definitions used throughout.**

- **E cells:** `L23_pyr`, `L4_exc`, `L5_pyr`, `L6_pyr`. **I cells:** every other type
  (`basket`, `martinotti`, `vip`, and in Dataset B also `neurogliaform` and `chandelier`).
  Dataset A has 150 E and 50 I cells.
- **Edge:** at least one synapse from pre to post, self-connections excluded. The second
  threshold is at least two synapses for A and at least three for B (the Module 10 kit's
  own second threshold).
- **The estimand:** the number of reciprocal E–I pairs, meaning an E cell and an I cell
  with edges in both directions. That is the two-cell E→I→E feedback loop: the E cell
  excites the I cell, which inhibits the same E cell. A learner who defines the loop as a
  three-cell cycle (E1→I→E2→E1) has made a different, defensible choice and must say so;
  the two estimands are not interchangeable.
- **Effect size:** observed count divided by the null mean. Its interval is the observed
  count divided by the null's 2.5th and 97.5th percentiles. It shows how far the observed
  value sits from the null spread; it is not a bootstrap interval on the observed count.

**Instructor note.** Learners should build their nulls before reading this page. The
Module 11 kit README says how the data were generated, which gives away the answer. That
is deliberate: the task is to show it with a null, not to guess it.

## Before you start

The prerequisites are basic probability and statistics and graph representation. A
learner who cannot yet write an edge-swap null can outline it in pseudocode and use the
values on this page for the inference steps. A good question to bring: “If two null
models disagree, which one do I report?” The answer this module gives is both, with the
hypothesis each one encodes.

## Questions this module answers

1. **Which null model is valid for this connectome hypothesis?** One that preserves
   everything the hypothesis treats as uninteresting. The claim is “loops beyond what cell
   type and proximity explain,” so the null must keep each cell's in- and out-degree, the
   type-to-type edge counts and the dependence of connection on soma distance. In
   Dataset A that null gives a ratio of 0.92: no enrichment.
2. **How should multiplicity be handled across motif families?** Count every test run,
   including every null and threshold tried, and correct against that count. Here that is
   24 tests per dataset. Because reciprocity counts share edges, use permutation inference
   on the maximum statistic within each null, and report Bonferroni alongside it.
3. **What claims are robust versus exploratory?** Robust: the raw excess of E–I loops
   over degree-only nulls, which holds in both datasets and at both thresholds. Not
   supported: that the excess reflects a wiring rule beyond type and distance. That
   claim fails under the distance-preserving null in both datasets.

## The task

### 1. Four null models, each tied to what it treats as uninteresting

The task asks for at least two. This key builds four, because the drop in effect size
from one to the next is the finding.

| Null | Preserves | Randomizes | Hypothesis it tests | How it was built |
|---|---|---|---|---|
| **ER** | Node count and edge count (1,453) | Everything else | “Loops exceed a graph with no structure at all.” | Draw 1,453 distinct ordered pairs uniformly |
| **DEG** | Each cell's in- and out-degree | Who connects to whom | “Loops exceed what hub cells alone produce.” | Directed double-edge swaps, 10 attempts per edge |
| **DEG+TYPE** | Degrees and the count of edges from each cell to each target cell type | Partner identity within a type | “Loops exceed what degree and type preferences produce.” | Swaps accepted only when the two targets share a cell type |
| **DEG+TYPE+DIST** | Degrees, type counts and each edge's soma distance to within 25 µm | Partner identity among same-type cells at similar distance | “Loops exceed what degree, type and proximity produce.” | Swaps accepted only when the targets share a type and both new edges keep their length to within 25 µm; 30 attempts per edge |

The core of the swap null, as used for the last three rows:

```python
# edges: set of (pre, post); cond decides which swaps the null allows
a, b = el[i]; c, d = el[j]
if len({a, b, c, d}) == 4 and (a, d) not in s and (c, b) not in s and cond(a, b, c, d):
    s -= {(a, b), (c, d)}; s |= {(a, d), (c, b)}
```

**Justification.** ER is the wrong null for this claim and is included only to show how
wrong. DEG answers a question nobody asked. DEG+TYPE is probably the null behind the
team's claim. DEG+TYPE+DIST is the one the hypothesis requires, because the claim is
about wiring beyond proximity, and cells that are close connect more in both directions.

**Mixing check.** After swapping, the fraction of observed edges still in place was
6.2% for DEG, 14.9% for DEG+TYPE and 71.6% for DEG+TYPE+DIST. The distance constraint
rejects most swaps, so that null stays close to the data and could be too conservative.
Two reruns tested this. With 100 attempts per edge (48.1% of edges kept), the null mean was
45.9 and the ratio 0.89. With a 50 µm tolerance (41.7% kept), the null mean was 43.6 and
the ratio 0.94. The conclusion does not depend on the mixing. Credit a learner who
reports a mixing check; most do not.

### 2. A multiplicity-aware test plan across the motif set

**The test family, counted in full.** Reciprocal pairs in three classes (EE, EI, II),
under four nulls, at two thresholds: **24 tests** in Dataset A and 24 in Dataset B. A
learner who reports only the EI test under their favored null has run 24 and is
reporting 1.

**Correction, chosen before running.** The three class counts share every edge, so
they are dependent. The module's decision table points to permutation inference on the
maximum statistic: for each null sample, take the largest z-score across the three
classes, and compare each observed z to that distribution. Bonferroni across all 24
(threshold 0.05 / 24 = 0.0021) and Benjamini–Hochberg are reported alongside. With 999
samples the smallest attainable p is 0.001, just below the Bonferroni line; with 99 samples it
would be 0.01, and no test could survive. Check that before choosing the sample count.

**Dataset A, EI reciprocal pairs (observed 41 at ≥1 synapse, 13 at ≥2):**

| Null | Threshold | Null mean (95% range) | Ratio (interval) | z | p | Max-statistic p |
|---|---|---|---|---|---|---|
| ER | ≥1 | 9.97 (4–16) | 4.11 (2.56–10.25) | 9.96 | 0.001 | 0.001 |
| DEG | ≥1 | 16.63 (9–25) | 2.47 (1.64–4.56) | 6.18 | 0.001 | 0.001 |
| DEG+TYPE | ≥1 | 29.93 (20–41) | 1.37 (1.00–2.05) | 2.14 | 0.029 | 0.060 |
| DEG+TYPE+DIST | ≥1 | 44.75 (37–53) | 0.92 (0.77–1.11) | −0.86 | 0.841 | 0.997 |
| ER | ≥2 | 2.63 (0–6) | 4.95 | 6.29 | 0.001 | 0.001 |
| DEG | ≥2 | 4.32 (1–9) | 3.01 | 4.27 | 0.001 | 0.001 |
| DEG+TYPE | ≥2 | 8.19 (3–14) | 1.59 (0.93–4.33) | 1.75 | 0.067 | 0.233 |
| DEG+TYPE+DIST | ≥2 | 13.56 (9–19) | 0.96 (0.68–1.44) | −0.23 | 0.656 | 0.998 |

Across all 24 Dataset A tests, Bonferroni keeps 4 (EI under ER and DEG at both
thresholds) and Benjamini–Hochberg keeps 5 (those four plus II under ER at ≥1, p =
0.003). The DEG+TYPE result for EI (p = 0.029) survives neither. The other two classes
at ≥1 synapse: EE 8 and II 7 observed; under DEG+TYPE+DIST their null means are 7.37
and 5.91 (p = 0.479 and 0.303).

**Dataset B, EI reciprocal pairs** (object 20432 excluded, see section 4): 554 observed
at ≥1 synapse; ratios 5.79 (ER), 3.41 (DEG), 1.69 (DEG+TYPE, interval 1.54–1.89, p =
0.002) and 1.01 (DEG+TYPE+DIST, interval 0.97–1.06, p = 0.340). At ≥3 synapses: 26
observed; ratios 1.72 (DEG+TYPE, p = 0.006) and 0.93 (DEG+TYPE+DIST, p = 0.768).

### 3. Results summary, exploratory and confirmatory kept apart

> **Exploratory (Dataset A, 24 tests, hypothesis-generating).** Reciprocal E–I pairs
> number 41, 4.1 times a density-matched random graph and 2.5 times a degree-preserving
> null (both p = 0.001, surviving Bonferroni across 24 tests). Once cell-type targeting
> is preserved, the excess shrinks to 1.37 times (interval 1.00–2.05, uncorrected p =
> 0.029, family-wise p = 0.060). Once soma distance is also preserved, it disappears
> (0.92 times, interval 0.77–1.11). Most loops involve basket cells (34 of 41; 6 involve
> Martinotti cells and 1 a VIP cell), and loop partners sit closer together than E→I
> partners in general (median soma distance 119.1 µm against 183.1 µm over all 430 E→I
> edges). These observations suggest proximity and basket-cell targeting as
> explanations. They were found in this dataset and are not tested by it.
>
> **Confirmatory (Dataset B, one test declared before looking).** Test: EI reciprocal
> pairs at ≥1 synapse against the DEG+TYPE+DIST null, one-sided, α = 0.05. Result: 554
> observed against a null mean of 548.3, ratio 1.01 (interval 0.97–1.06), p = 0.340.
> The enrichment beyond type and proximity is **not supported** in Dataset B.
>
> **What the team's claim becomes.** “E-to-I-to-E loops are enriched” is true against
> degree-only nulls in both datasets and is explained by cell type and distance in both.
> The enrichment generalizes; the claim that it reflects a specific wiring rule does not.

The confirmatory label is honest only if the test was written down before Dataset B
was opened. A learner who ran all 24 tests on B first and then picked one is back in
the exploratory block.

### 4. One robustness check for cross-dataset comparability

The two datasets differ in ways that could make the comparison unfair. Dataset A covers
L2/3 and L4 with five cell types; Dataset B covers L1–L6 with nine. Their densities also
differ (0.0365 in A; 0.0450 in B).

**Check: restrict B to A's layers and types, and rerun the same estimand and nulls.**
Keep B's L2/3 and L4 cells of the five types A contains (`L23_pyr`, `L4_exc`,
`basket`, `martinotti`, `vip`). That leaves 248 cells and 4,363 edges.

| | Dataset A | Dataset B, full | Dataset B, matched |
|---|---|---|---|
| Cells / edges | 200 / 1,453 | 499 / 11,194 | 248 / 4,363 |
| EI reciprocal pairs | 41 | 554 | 195 |
| Ratio, DEG+TYPE | 1.37 (1.00–2.05) | 1.69 (1.54–1.89) | 1.42 (1.25–1.65) |
| Ratio, DEG+TYPE+DIST | 0.92 (0.77–1.11) | 1.01 (0.97–1.06) | 1.03 (0.95–1.12) |

**Pass/fail criteria, set before the run.** Pass if, under the declared null, (a) the
matched subset and Dataset A agree in direction and (b) their ratio intervals overlap.
Fail if the matched subset shows an effect the full dataset does not, which would mean
layer or type composition drives the result. **Result: pass.** Both sit at a ratio near
1 under DEG+TYPE+DIST, and both sit near 1.4 under DEG+TYPE. Matching composition
brought B's DEG+TYPE ratio down from 1.69 to 1.42, so part of the full-B excess comes
from layers and types that A does not contain.

**Pre-processing step for Dataset B.** Object 20432 is a basket cell with `soma_count` 2,
a merge. It was excluded before any count, as the Module 10 kit README asks. That leaves 499
cells and 11,194 edges; the kit's 11,388 includes this object's edges.

### What you hand in

- **Inference design sheet.** Estimand: reciprocal E–I pairs. Nulls: the four in
  section 1, with DEG+TYPE+DIST declared as the one the hypothesis requires. Tests: 24
  per dataset. Correction: max-statistic permutation within each null, with Bonferroni
  and Benjamini–Hochberg reported.
- **Claim calibration summary.** The two blocks in section 3.
- **Robustness plan.** The matched-subset check in section 4, the threshold rerun in
  section 2 and the error band below, each with its pass/fail rule stated.

**Error-sensitivity band.** The kits carry no measured merge or split rates, so this
key uses the module's illustrative 2% merge and 6% split and labels them as assumed.
Splits were simulated by deleting 6% of edges at random. Merges were simulated by
copying 30% of a nearby cell's edges (one of its five nearest neighbors) onto a cell
until the added edges reached 2% of the total. Over 200 perturbed copies of Dataset A:

| Perturbation | EI reciprocal pairs, mean (95% range) |
|---|---|
| None (observed) | 41 |
| Splits only | 36.5 (32–40) |
| Merges only | 42.4 (41–45) |
| Both | 38.1 (33–42) |

Splits lower the count; merges raise it, toward the enrichment claim. Against the
unperturbed DEG+TYPE+DIST null mean of 44.75, the combined band gives ratios of 0.74 to
0.94. It never reaches 1, so no enrichment appears at these rates. The null was not
re-drawn for each perturbed copy. That is an approximation, stated as one.

## Working checklist

The five stages map to the task: question-to-test mapping (the estimand and the
hypothesis column of the null table), null-model design (section 1), inference
execution (section 2), robustness checks (section 4 and the error band) and claim
calibration (section 3). A learner who skips the mixing check should write why, for
example “no time; the DIST null may be conservative.” That is a decision. A silent skip
is a gap.

## Evidence and reasoning

| # | Claim | Evidence | Limitation / what would change my mind |
|---|---|---|---|
| 1 | The E–I loop excess in Dataset A is explained by cell type and soma distance. | Ratio 0.92 (0.77–1.11) under DEG+TYPE+DIST, against 2.47 under DEG; holds at both thresholds and with stronger mixing. | A null that preserved distance more tightly still found no excess. A spatial null with a fitted distance curve that did find one would reopen the question. |
| 2 | The pattern generalizes to Dataset B in the same form. | B gives 1.69 under DEG+TYPE and 1.01 under DEG+TYPE+DIST; the matched subset gives 1.42 and 1.03. | Both kits come from one generator with type and distance rules built in, so agreement is expected. Real volumes from two labs would be a stronger test. |
| 3 | Reconstruction error at the assumed rates does not create enrichment here. | Combined band 33–42 loops, ratio 0.74–0.94 against the DIST null. | The rates are the module's illustrative values, not measured on these kits. At a higher merge rate the band would move up. |

**Confidence:** High for claim 1 within these kits. Two independent lines agree: the
null series in Dataset A and the declared test in Dataset B. Neither line can say
anything about a real brain.

**Alternative considered and rejected:** report the DEG+TYPE result (1.37 times,
p = 0.029) as the finding. Rejected because it fails correction across the 24 tests
run, and because the hypothesis is about wiring beyond proximity, which that null does
not hold fixed.

## Misconception self-check

Feedback for each error:

- **A generic random graph is an adequate null for a connectome.** Show the ER row: 4.1
  times enrichment, which is 4.5 times larger than the distance-null ratio. Ask, “What
  does ER treat as uninteresting that your hypothesis does not?”
- **A small p-value speaks for itself, regardless of how many tests were run.** The
  DEG+TYPE p of 0.029 was one of 24. Ask the learner to count the tests they ran,
  including the ones they dropped, before quoting any p-value.
- **A hypothesis found in the data can be confirmed by the same data.** The basket-cell
  observation (34 of 41 loops) came from Dataset A. Testing it on Dataset A again would
  confirm nothing. Ask for the dataset and the single test that would confirm it.

## Session timing (facilitator reference)

This section has no learner task. The 06:00–18:00 worked example (reciprocity across
nulls, from Technical Unit 09) has the same shape as section 1 here. A facilitator can
show the Dataset A null series (4.11, 2.47, 1.37, 0.92) as a second case in the 18:00–30:00
guided practice.

## Rubric

A self-assessment that matches this exemplar:

- **Strongest part:** the null series, because each null's preserved constraints are
  named and the effect size is shown shrinking step by step.
- **Weakest part:** the error band uses assumed rates. **Next action:** obtain measured
  merge and split rates from a validation set (Module 14) before calling the band final.

## Exit prompt

> The hypothesis is that E-to-I-to-E loops are more common than cell type and proximity
> predict. The estimand is the number of reciprocal E–I pairs at ≥1 synapse. The null
> preserves each cell's in- and out-degree, the edge count to each target cell type and
> each edge's soma distance to within 25 µm. It randomizes partner identity among
> same-type cells at similar distance. I ran 24 tests per dataset and controlled
> family-wise error with a max-statistic permutation test, reporting Bonferroni
> alongside it. What survives: loops exceed degree-only nulls in both kits (ratio 2.47
> in A), and the excess disappears once distance is preserved (0.92 in A, 1.01 in B).
> What remains uncertain is how reconstruction error would move this, because no
> measured merge rate exists for these kits.

## Peer review (swap worksheets)

A reviewer should rerun the partner's preferred null on Dataset A and check the
observed count of 41 and a null mean within a few tenths of the partner's value. A
good question: “Which of your tests did you run and not report?”

## Feedback guide

This key follows the kit's own tiers.

- **Minimum pass:** the null is justified and the constraints it preserves are listed
  in terms of what the hypothesis treats as uninteresting; the total test count,
  including unreported tests, is documented and a named correction applied against
  it; claims are split into exploratory and confirmatory blocks in different language.
- **Strong:** results at two preprocessing choices (here, two synapse thresholds, and
  the exclusion of the two-soma object in Dataset B); effect sizes with intervals
  beside every significance statement; an error band at stated merge and split rates,
  with the direction of merge bias named; a generalization boundary naming dataset and
  region.
- **Common failures:** a null chosen without reference to the question (ER alone); a
  single significant test shown and the other 23 uncounted; an exploratory observation
  such as the basket-cell share written up as a result; analytic p-values from a normal
  approximation used on dependent counts.

**Strong and weak patterns.** A strong response reports the whole null series and
reads meaning from the drop. A weak one reports only the null that gave the smallest
p-value, or only ER. A strong response counts tests before correcting; a weak one
corrects across the three motif classes and forgets it tried four nulls. A strong
response says that agreement between two kits built by one generator is weak evidence
of generality. A weak one calls the pattern “universal.”

Do not reward a large number of nulls for its own sake; two, justified, meet the
minimum. Do not reward a p-value of 0.001 from a run of 999 samples as if it were
smaller than that; it is the floor. Accept a three-cell loop estimand or different
thresholds when the learner states them and counts every resulting test. Accept null
means that differ from this key by sampling error. This is a local teaching rubric,
not a validated assessment instrument.

See [motif analysis]({{ '/content-library/connectomics/motif-analysis/' | relative_url }})
for null-model detail. Teaching material: CC BY 4.0, NeuroTrailblazers.
