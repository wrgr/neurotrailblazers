---
layout: page
title: "08 Segmentation and Proofreading"
description: "How automated segmentation fails, which metrics reveal which failure, and how to run proofreading as a prioritized, measured, budget-bounded operation rather than an open-ended cleanup."
permalink: /technical-training/08-segmentation-and-proofreading/
slug: 08-segmentation-and-proofreading
track: core-concepts-methods
pathways:
  - technical foundation
  - methods depth
level: "Advanced"
time_estimate: "2.5 hours reading + 2 hour lab"
prerequisites: "Units 03-07"
---

## Before you start

| | |
|---|---|
| **Time** | ~2.5 h, plus a 2 h lab |
| **Prerequisites** | Units 03–07. Unit 06's error-cost reasoning is used heavily here. |
| **You need** | A proofreading-capable viewer (Neuroglancer against a CAVE dataset, or webKnossos) and an account |
| **You finish with** | A proofreading plan with an explicit stopping rule, a triage ranking, and a defended budget |

**The framing that makes this unit different from a tool tutorial.** Proofreading is
not "fixing the segmentation until it is right". Segmentation is never right, and at
petascale nobody will ever look at most of it. Proofreading is an **allocation problem
under a fixed budget**: which corrections, in which order, stopping when.

Teams that treat it as cleanup run out of money with a half-corrected volume and no
defensible claim. Teams that treat it as allocation deliver a specific scientific
result with quantified error bounds. The difference is entirely in how the work is
prioritized and when it is declared finished.

---

## What you'll be able to do

1. Name the error types automated segmentation produces and rank them by cost for a given endpoint.
2. Choose the right metric for a given question and say what each metric hides.
3. Build a triage ranking that prioritizes by effect on the endpoint rather than by conspicuousness.
4. Define a stopping rule that is checkable by someone other than you.
5. Estimate proofreading effort and defend the estimate.

---

## 1. How automated segmentation works, briefly

Enough to reason about its failures. (Full detail: Unit 04 §1 and the content library.)

**The affinity/agglomeration family.** A network predicts, per voxel, the affinity
between neighbouring voxels. Watershed at a conservative threshold produces
**supervoxels** that are deliberately too small. An agglomeration step then merges
supervoxels into objects, using mean affinity, learned agglomeration, or shape-based
descriptors that let the model reason about whether a merge produces a plausible
neurite shape.

**The flood-filling family.** A network iteratively grows one object from a seed,
maintaining a mask and repeatedly asking "does this next voxel belong?" This produces
strong results because the network sees the object it is building, but it is
sequential and expensive.

**Where both fail, structurally:**

- **Thin processes.** A 60 nm spine neck at 40 nm z-resolution may appear in only one
  or two sections. There is very little evidence to work with, so spine necks are a
  perennial source of splits.
- **Steep z-trajectories.** Anisotropy again. A process crossing sections at a shallow
  angle to the imaging plane presents a small, rapidly-moving cross-section.
- **Membrane contact.** Two membranes tightly apposed over many sections may not be
  separable, especially with weak staining (Unit 03).
- **Artifact regions.** Folds, charging, missing sections — the network was not
  trained on tissue that does not exist.
- **Rare morphologies.** Anything under-represented in the training set: unusual cell
  types, developmental stages, pathology, and — importantly — the boundaries of the
  volume.

**The design choice that shapes everything downstream:** the pipeline is deliberately
tuned to over-segment. It prefers splits to merges. That is a decision about which
error is cheaper to repair, and it dictates that proofreading is mostly *joining*.

---

## 2. Error taxonomy and cost

| Error | What it is | Detection difficulty | Cost | Who finds it |
|---|---|---|---|---|
| **Split** | One neuron in multiple pieces | Easy — arbor looks truncated | Bounded, local, visible | Automated heuristics (endpoint detection) and humans |
| **Merge** | Two neurons fused | **Hard** — object looks fine unless you check morphology | Corrupts connectivity; propagates | Humans noticing implausible morphology; cue conflict (Unit 06) |
| **Glia–neuron merge** | Glial process fused to neuron | Hard | High — manufactures local false connectivity (Unit 07 §1) | Humans |
| **Orphan fragment** | A piece belonging to no traced object | Easy to count | Low individually; large in aggregate as unattributed volume | Automated |
| **False synapse** | Detection where no synapse exists | Medium | Inflates degree; worst on weak (1-synapse) connections | Human verification on a sample |
| **Missed synapse** | Real synapse not detected | Hard (you are looking for absence) | Deflates degree, non-uniformly by synapse size | Human verification on a sample |
| **Wrong synapse partner** | Correct cleft, wrong pre- or post- assignment | Hard | Direction/identity error, as in Unit 06 | Human |

### The asymmetry, stated once more

**Splits are visible and bounded. Merges are invisible and unbounded.** A split leaves
evidence of itself — a neuron that stops in mid-neuropil. A merge leaves an object
that looks like a neuron and is not. The whole architecture of the field, from
watershed thresholds to proofreading protocols to quality metrics, is organized around
this asymmetry.

---

## 3. Metrics: what each one is blind to

The content library has the mathematics; this section is about *choosing*.

| Metric | Measures | Blind to | Use when |
|---|---|---|---|
| **Variation of Information (VI)** | Total disagreement between two segmentations, decomposable into split and merge components | Object size — a merge of two tiny fragments and a merge of two full neurons contribute very differently, and not in the way you might want | Comparing segmentation versions on the same volume |
| **Expected Run Length (ERL)** | Mean error-free path length along skeletons | Merges, unless explicitly penalized; also insensitive to small dangling fragments | Tracing-oriented questions: "how far can I follow a neurite before hitting an error?" |
| **Edge precision / recall** | Correctness of connections in the derived graph | Weights all edges equally, so a 1-synapse and a 50-synapse connection count the same | Graph-level claims |
| **Synapse precision / recall** | Correctness of detected synapses | Assumes correct segmentation underneath — a synapse assigned to a merged object scores as correct | Synapse-level claims |
| **Completeness (per neuron)** | Fraction of a neuron actually reconstructed | Says nothing about correctness of what is there | Per-cell claims like input counts |

> **Use at least two metrics from different rows, and always report VI's split and
> merge components separately.** A single VI number can improve while merges get worse,
> because the split component dominates. That is a real and common way to ship a
> regression.

### The metric that actually matters

None of the above. **The metric that matters is the effect on your endpoint.**

Concretely: if your result is "cell type A makes 3× more synapses onto type B than
onto type C", then the question is not "what is our VI?" It is: *how much would the
observed 3× change under a plausible correction of the remaining errors?*

Procedure:

1. Take a random sample of the cells in the analysis — 20 is often enough to be
   informative.
2. Proofread them exhaustively, to a standard well above your production standard.
3. Recompute the endpoint on that sample, before and after.
4. Report the shift. "Exhaustive proofreading of a 20-cell sample changed the ratio
   from 3.1 to 2.8" is a far stronger statement about data quality than any VI value,
   and reviewers understand it immediately.

This costs a few dozen person-hours and it converts "we proofread the data" into a
quantified error bound. It is the single highest-value practice in this unit.

### Check yourself

<details markdown="1">
<summary>Version B of your segmentation has lower total VI than version A, and your
team wants to ship it. What do you check first?</summary>

**Decompose VI into split and merge components.**

Total VI is dominated by whichever component is larger, and in an over-segmented
pipeline that is usually splits. Version B may have reduced splits (perhaps by more
aggressive agglomeration) while *increasing* merges — and the total would still
improve.

Since merges are the expensive error, a "better" total VI with worse merges is a
regression for connectomics purposes, even though the headline number improved.

Also check: ERL (does tracing actually get easier?), and — decisively — recompute
the endpoint metric on a fixed evaluation set of neurons. Ship on the endpoint, not
on the aggregate score.
</details>

---

## 4. The production proofreading loop

```
1. SEED       Select target cells by scientific priority, not by convenience
                or by which segment happens to be biggest.
2. TRIAGE     Rank candidate corrections by expected effect on the endpoint.
3. CORRECT    Apply merges/splits with evidence recorded (Unit 05 evidence chains).
4. VERIFY     Independent second pass on a sample; measure agreement.
5. MEASURE    Recompute quality metrics AND the endpoint metric.
6. STOP       Apply the stopping rule. Record the state as a release.
```

### Triage: ranking corrections

Rank by **expected change in the endpoint per unit of annotator time**, not by error
conspicuousness. In practice this means scoring candidates on:

- **Proximity to the endpoint.** An error on a cell in your analysis set outranks an
  identical error on a cell that is not.
- **Error type.** Merges outrank splits at equal size, because merges corrupt rather
  than truncate.
- **Size.** A split that truncates 60% of an arbor outranks one that loses a 3 µm
  twig — but note that a *small* merge can be worse than a *large* split, so size
  ranks within type, not across types.
- **Path centrality.** An error on the primary neurite near the soma disconnects
  everything distal to it. Errors near the root are worth far more than errors at the
  tips.
- **Cost to fix.** A correction requiring 40 minutes of careful tracing through a fold
  may lose to five 5-minute corrections elsewhere.

**Automated candidate generation** feeds this queue: endpoint detectors (a neurite
that stops without tapering to a natural ending is a split candidate), morphology
implausibility detectors (an object with two somata; an object with both ribosomes and
presynaptic vesicle clusters — the Unit 06 alarm), and agglomeration-confidence
thresholds. Humans then adjudicate a *ranked* queue rather than browsing.

### Stopping rules

This is where most projects fail, because "keep going until it looks good" has no
termination condition and no defensible reporting.

A stopping rule must be **stated in advance**, **measurable**, and **tied to the
endpoint**. Examples of usable rules:

- **Convergence:** "Stop when a second independent proofreading pass over a 20-cell
  sample changes the endpoint metric by less than 5%." *This is the strongest general
  rule* — it directly measures whether more effort would change the answer.
- **Budget with declared coverage:** "Proofread to level N on 200 cells; report per-cell
  proofreading level with every result; make no claims about cells below level N."
- **Threshold:** "Every cell in the analysis set has ≥ 95% of its dendritic arbor
  recovered relative to a manually traced reference on a validation subset."

**Levels are the practical mechanism.** Rather than a binary proofread/not-proofread,
define levels — e.g. *L0 raw*, *L1 gross merges removed*, *L2 dendrite complete*,
*L3 axon extended*, *L4 exhaustive* — with written criteria for each. Then:

- Cells carry their level as metadata.
- Analyses state the required level and exclude cells below it.
- Effort is directed at raising specific cells to a specific level, which is a
  plannable task with an estimable cost.

> **The reporting rule.** Every connectomics result should state the proofreading
> level of the cells it rests on, and the criteria defining that level. A result that
> does not is uninterpretable, because the reader cannot tell whether a low measured
> connection count reflects biology or incompleteness.

---

## 5. Human factors, because this is a labour operation

At petascale, proofreading is a workforce, and it behaves like one.

**Training and calibration.** New annotators need a calibration set with known
answers, and periodic recalibration — drift is real and it is gradual. Run the Unit 05
consensus round and the Unit 06 calibration lab as onboarding, then repeat quarterly.

**Measure agreement, not just throughput.** Throughput alone rewards speed over
correctness, and it will get you exactly that. Track: inter-annotator agreement on a
shared subset, and per-annotator error rate on gold-standard tasks seeded invisibly
into the normal queue. Discuss agreement openly; treat disagreement as protocol
feedback rather than individual failure.

**Fatigue is a data-quality variable.** Error rates rise across a long session.
Structure work in bounded blocks and rotate task types.

**Community proofreading works, with structure.** The FlyWire whole-brain connectome
was completed with millions of edits from a large distributed community over several
years — an existence proof that this scales beyond a single lab. What made it work was
not enthusiasm but infrastructure: task queues, automated candidate generation, tiered
permissions, edit provenance, expert adjudication for hard cases, and clear
attribution.

**The tooling requirement that follows.** Every edit records who, when, what, and
ideally why. This is not surveillance; it is what lets you (a) roll back a bad batch,
(b) identify a training gap when one annotator's edits are systematically different,
and (c) reconstruct the state of an analysis at any past time (Unit 04 §2).

---

## Visual training set
<div class="cards-grid">
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-RIV-ULTRA-S06-01.png' | relative_url }}" alt="Segmentation proofreading visual: neuronal structure orientation" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S06:</strong> orientation cue for robust proofreading context.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-RIV-ULTRA-S09-01.png' | relative_url }}" alt="Segmentation proofreading visual: synapse identification cues" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S09:</strong> synapse-oriented features relevant to correction decisions.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-RIV-ULTRA-S11-01.png' | relative_url }}" alt="Segmentation proofreading visual: ultrastructural feature panel" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-ULTRA S11:</strong> vesicle and organelle cues for ambiguity resolution.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-RIV-AXDEN-S13-01.png' | relative_url }}" alt="Segmentation proofreading visual: axon versus dendrite comparison" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-AXDEN S13:</strong> axon-vs-dendrite differentiation for identity checks.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-RIV-AXDEN-S18-01.png' | relative_url }}" alt="Segmentation proofreading visual: edge-case process morphology" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-AXDEN S18:</strong> edge-case morphology for high-risk correction review.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-RIV-AXDEN-S22-01.png' | relative_url }}" alt="Segmentation proofreading visual: advanced morphology cue set" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>RIV-AXDEN S22:</strong> advanced cue set for difficult boundary calls.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-SRC-MODULE14_LESSON2-S03-01.png' | relative_url }}" alt="Segmentation proofreading visual: method overview context" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module14 L2 S03:</strong> method overview context for processing/QC integration.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-SRC-MODULE14_LESSON2-S08-01.png' | relative_url }}" alt="Segmentation proofreading visual: graph and pipeline transition" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module14 L2 S08:</strong> graph/pipeline transition context.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-SRC-MODULE14_LESSON2-S09-01.png' | relative_url }}" alt="Segmentation proofreading visual: automated detection context" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module14 L2 S09:</strong> automated detection context for human-machine workflows.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-SRC-MODULE14_LESSON2-S10-01.png' | relative_url }}" alt="Segmentation proofreading visual: processing-stage quality context" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module14 L2 S10:</strong> quality-relevant processing stage.</p>
  </article>
  <article class="card">
    <img src="{{ '/assets/images/technical-training/08-segmentation-and-proofreading/FIG-SRC-MODULE14_LESSON2-S13-01.png' | relative_url }}" alt="Segmentation proofreading visual: evaluation and metrics context" style="width:100%; border-radius:8px;">
    <p class="card-description"><strong>Module14 L2 S13:</strong> evaluation/metrics context for QC reporting.</p>
  </article>
</div>

<p><small>Attribution: Pat Rivlin training materials for `RIV-*` visuals; outreach visuals from module14 lesson2 extraction. Some planned IDs were unavailable in extracted thumbnails and were replaced with nearest available alternatives.</small></p>

---

## Lab: proofreading plan with a defended budget (2 hours)

**Part A — hands on (60 min).**

In a proofreading-capable viewer on a public dataset:

1. Pick a neuron with visible errors. Trace its arbor and **log every error you find**:
   type, location, estimated size of the affected arbor fraction, and estimated fix
   time.
2. Fix the three highest-impact errors by your own ranking, and record your ranking
   rationale *before* fixing.
3. After fixing, recount the neuron's input synapses. Report the change from before.
   This number is your personal demonstration of why proofreading level must be
   reported with results.
4. Note one error you chose *not* to fix, and why.

**Part B — the plan (60 min).**

Your project needs 200 proofread layer-2/3 pyramidal cells to test a cell-type
targeting hypothesis. Write a two-page proofreading plan:

1. **Endpoint metric**, stated precisely, with units.
2. **Proofreading levels**, defined with written criteria a new annotator could apply.
   State which level each part of your analysis requires and why.
3. **Triage ranking rule**, with the factors from §4 and their relative weights. Give
   a worked example applying it to two competing candidate corrections.
4. **Stopping rule**, stated so that a person who is not you could determine whether it
   has been met.
5. **Budget:** person-hours, derived from your own Part A timing extrapolated with
   stated assumptions. Show the arithmetic.
6. **Quality plan:** which metrics, on what sample, at what frequency; how you will
   measure inter-annotator agreement; and the endpoint-shift measurement from §3.
7. **What you will report** in the eventual paper about data quality — write the
   actual methods paragraph.

### Rubric

| | Not yet | Proficient | Strong |
|---|---|---|---|
| **Endpoint** | Vague | Precise with units | Precise, and the required proofreading level is derived *from* it rather than asserted |
| **Levels** | Binary done/not-done | Levels defined | Criteria are operational — two annotators would assign the same level |
| **Triage** | "Fix the big ones" | Multi-factor ranking | Weights justified, worked example given, cost-to-fix included |
| **Stopping rule** | Absent or unfalsifiable | Stated and measurable | Convergence-based, tied to the endpoint, checkable by a third party |
| **Budget** | Guessed | Derived from measured timing | Assumptions stated, sensitivity considered, and a contingency for the hard tail |
| **Quality plan** | Metrics named | Metrics with sampling plan | Includes endpoint-shift measurement and inter-annotator agreement |
| **Reporting** | Not attempted | Mentions proofreading | A methods paragraph a reviewer would accept, with per-cell level reported |

<details markdown="1">
<summary>The estimation trap in step 5 — read after drafting your budget</summary>

Almost everyone underestimates, and almost always the same way: by extrapolating
from the *median* neuron.

Proofreading time per neuron is heavy-tailed. Most cells are quick; a minority
consume many times the median because they sit in an artifact region, have an
unusually extensive axon, or are tangled with a neighbour across many sections. If
you budget median × 200, you will be short — and the shortfall will land at the end
of the project, when it is most damaging.

Better practice:

- Estimate from the **mean**, and estimate the mean from a sample large enough to
  include tail cases (in practice, don't trust a sample of fewer than ~10–15 cells).
- Or: budget median × N, and add an explicit contingency for the tail, stated as a
  separate line item.
- Or best: define your stopping rule so that pathological cells are *excluded by
  policy* after a stated time cap, and report the exclusion rate. A stated 6%
  exclusion rate is honest and cheap; an unbudgeted tail is neither.

This is also a good illustration of why the stopping rule and the budget must be
designed together rather than sequentially.
</details>

---

## Common errors and how to recover

**Proofreading without a stopping rule.** Recover: write one now, tie it to the
endpoint, and get someone else to confirm they could evaluate it.

**Optimizing the aggregate metric.** Recover: fix an evaluation set of neurons and an
endpoint metric; ship on those.

**Triage by conspicuousness.** Recover: score candidates on a written rubric; audit a
sample of decisions against it.

**Unreported proofreading level.** Recover: attach level metadata per cell; filter
analyses by level; state it in the methods.

**Rewarding throughput alone.** Recover: publish agreement statistics alongside
throughput and discuss them as protocol feedback.

**Assuming the error rate is uniform.** It is not — it is much higher near volume
boundaries, in artifact regions, and for thin processes. Recover: report error rate
by region and by process calibre, and let that drive both triage and the caveats.

---

## What this unit does not cover

Segmentation model architecture and training in depth, and the statistical analysis of
the resulting graph (Unit 09). Tool-specific keyboard workflows change too fast to
document here; use the vendor documentation and record your team's conventions in your
own protocol.

---

## Go deeper

- [Error taxonomy]({{ '/content-library/proofreading/error-taxonomy/' | relative_url }}) — full catalogue with examples
- [Metrics and QA]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}) — VI, ERL, and precision/recall worked in detail
- [Proofreading strategies]({{ '/content-library/proofreading/proofreading-strategies/' | relative_url }}) — seeding, extension, and triage patterns
- [Proofreading tools]({{ '/content-library/proofreading/proofreading-tools/' | relative_url }}) — the platform landscape
- [Worked examples]({{ '/content-library/proofreading/worked-examples/' | relative_url }}) — annotated correction cases
- [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }}) — hands-on quality exploration

## Course links

- Reading list: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Shared vocabulary: [Connectomics Dictionary]({{ '/technical-training/dictionary/' | relative_url }})
- Related modules: [Module 07]({{ '/modules/module07/' | relative_url }}), [Module 12]({{ '/modules/module12/' | relative_url }})
- Slide plan: [Segmentation and Proofreading deck]({{ '/technical-training/slides/08-segmentation-and-proofreading/' | relative_url }})
- **Next unit:** [09 Connectome Analysis and NeuroAI]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})
