---
layout: page
title: "Proofreading Strategies for Connectome Reconstruction"
permalink: /content-library/proofreading/proofreading-strategies/
image: /assets/images/content-library/proofreading/proofreading-strategies.svg
image_alt: "Stylized vector art: a traced process with marked error sites under review."
description: >
  An instructor reference on the major strategies for proofreading
  automated neural segmentation, from exhaustive local correction to crowd-sourced
  campaigns. Covers when to use each approach, how to combine them, and when to
  stop. Includes a worked campaign-design example and full references.
topics:
  - exhaustive proofreading
  - targeted proofreading
  - skeleton-guided tracing
  - priority-ranked proofreading
  - crowd-sourced proofreading
  - hybrid strategies
  - cost-benefit analysis
primary_units:
  - "08"
difficulty: intermediate
tags:
  - proofreading:exhaustive-proofreading
  - proofreading:targeted-proofreading
  - proofreading:crowd-sourced-proofreading
  - proofreading:priority-ranking
  - methodology:cost-benefit-analysis
  - connectomics:reconstruction-workflow
micro_lesson_id: ml-proof-strategies
combines_with:
  - error-taxonomy
  - metrics-and-qa
  - worked-examples
use_layout_hero: false
content_type: core
---

# Proofreading Strategies for Connectome Reconstruction

## Instructor Notes

This document is a standalone instructor script. It provides the full
narrative, real references, worked examples, and practical decision
frameworks. Adapt depth and pacing to your audience; the material is
intentionally detailed so that nothing needs to be improvised.

---

## 1. Overview: Why Strategy Matters

Starting at one corner of the volume and fixing every error you meet is
almost never the right plan. The strategy you choose sets four things:

- **Cost:** Human proofreading time is the dominant expense in connectomics.
  FlyWire's whole-brain reconstruction took an estimated 33 person-years of
  manual proofreading (Dorkenwald et al., 2024).
- **Quality:** Different strategies produce different error profiles. An
  exhaustive approach minimizes all error types; a targeted approach
  minimizes errors for specific neurons but leaves the rest untouched.
- **Timeline:** A crowd-sourced campaign can parallelize across hundreds of
  annotators; a single-expert targeted approach is inherently serial.
- **Reproducibility:** Some strategies produce versioned, auditable edit
  histories; others do not.

The five major strategies described below are not mutually exclusive. Most
real projects use a hybrid approach, and the worked example at the end of
this document illustrates how to combine them.

---

## 2. Exhaustive Local Proofreading

### 2.1 Definition

Correct every detectable error within a defined subvolume. The goal is a
"saturated" reconstruction: every neurite in the volume is correctly
segmented, every synapse is correctly assigned, and every cell boundary is
accurate.

### 2.2 When to Use

- **Gold-standard reference regions.** You need a ground-truth volume to
  benchmark automated methods or train error detectors.
- **Critical circuit regions.** A small nucleus or layer where every
  connection matters (e.g., a six-column barrel in mouse somatosensory
  cortex).
- **Validation sets.** Before publishing a large dataset, proofread a
  representative subvolume exhaustively to report quality metrics.

### 2.3 How It Works

1. Define a bounding box (typically 10-50 um on a side).
2. Enumerate all segments that have any part inside the box.
3. For each segment, inspect in 2D and 3D. Fix all merge errors (split),
   split errors (merge), and boundary errors (manual painting).
4. Cross-check every synapse annotation within the box for correct pre/post
   assignment.
5. Perform inter-annotator agreement on a subset (typically 10-20 %) to
   estimate residual error rate.

### 2.4 Cost

Kasthuri et al. (2015) described saturated reconstruction of a
1,500 cubic micrometer volume from mouse neocortex, a tiny fraction of even
one cortical column. You can extrapolate the cost yourself, and the arithmetic
is more useful than a quoted figure. A cortical mm^3 holds on the order of
10^5 neurons. At the 2-4 hours per neuron this page assumes for full
single-cell proofreading in the §8 campaign example, exhaustive coverage costs
200,000 to 400,000 person-hours. At 2,000 hours a year, that is 100 to 200 years
of one person's full-time work, and it is why no millimeter-scale volume has
been exhaustively proofread. Substitute your own per-neuron rate, measured on
your pilot, and the conclusion holds: at this scale, exhaustive proofreading
is only practical for small reference regions.

### 2.5 Instructor Tip

Ask students: "If exhaustive proofreading is so expensive, why do it at
all?" The answer: without at least some exhaustive ground truth, you
cannot measure the quality of any other strategy. Exhaustive proofreading
of small regions is the yardstick against which everything else is
calibrated.

---

## 3. Targeted / Skeleton-Guided Proofreading

### 3.1 Definition

Select specific neurons of interest and proofread only those neurons,
following each branch from soma to tip and fixing errors along the way.
The rest of the volume remains uncorrected.

### 3.2 When to Use

- **Circuit-focused studies.** You want the complete morphology and
  connectivity of a defined population (e.g., all Purkinje cells in a
  cerebellar volume, all chandelier cells in a cortical column).
- **Cell-type characterization.** You need accurate morphology for
  classification, but only for candidate neurons.
- **Following up on automated cell-type predictions.** A classifier flags
  50 candidate neurons of a rare type; you proofread each to confirm.

### 3.3 How It Works

1. **Start at the soma.** Identify the cell body of your target neuron.
2. **Trace the primary arbor.** Follow the main dendrite or axon in 3D,
   scrolling through 2D slices to verify continuity.
3. **At each branch point, push one branch onto a stack** and continue
   along the other. Process branches depth-first or breadth-first
   depending on preference.
4. **When you encounter a merge error:** The segment suddenly includes
   processes that do not belong to your neuron. Split the merge. Continue
   tracing your neuron on the correct fragment.
5. **When you encounter a split error:** Your neuron's segment ends
   abruptly. Search for a continuation fragment nearby (same caliber,
   same trajectory, within a few sections). Merge the fragments. Continue.
6. **When you encounter a dead end:** Determine whether it is a true
   biological termination (terminal bouton with vesicles, or a dendrite
   tip) or a split error. If uncertain, flag for review.
7. **Record all edits** in the annotation system for auditability.

### 3.4 Handling Ambiguous Continuations

The hardest judgment call in targeted proofreading is: "Is this orphan
fragment the continuation of my neuron, or a different neuron?" Criteria
to evaluate:

- **Caliber match.** The fragment should have approximately the same
  diameter as the process you are tracing.
- **Trajectory match.** The fragment should continue in a direction
  consistent with the process's trajectory.
- **Organelle content.** Mitochondria density, vesicle presence, and
  cytoplasm darkness should be consistent.
- **Distance.** The gap should be explainable (e.g., one damaged section =
  ~30-50 nm gap; two missing sections = ~60-100 nm).
- **Exclusion.** Check that the fragment is not already assigned to another
  proofread neuron.

If two or more fragments are plausible candidates, flag the ambiguity
rather than guessing. A wrong merge is worse than a documented gap.

### 3.5 Cost

Targeted proofreading of a single neuron in dense neuropil typically takes
30 minutes to several hours, depending on arbor complexity and error
density. A pyramidal cell with an extensive axonal arbor spanning hundreds
of micrometers may require 4-8 hours. This is far cheaper than exhaustive
proofreading of the same volume, but scales linearly with the number of
neurons of interest.

---

{% include figure.html
   src="/assets/images/content-library/em/proofreading-before-after.jpg"
   alt="Three panels of the same human cortex field: raw electron microscopy; the automated segmentation showing one object in green with a wrongly attached region in red; and the proofread result with only the green object remaining."
   caption="The product of targeted proofreading. The automated segmentation (middle) attached a neighboring process, shown in red, to this cell; a proofreader removed it (right). H01 ships 104 cells corrected this way against roughly 16,000 neurons in the volume &mdash; which is the cost argument of this entry in a single image. Note also where the error is <em>not</em>: at the cell body the automated result needs no correction at all. The corrections live in thin neurites, and that is what makes them expensive to find."
   credit="H01 human cortex, Lichtman Lab (Harvard) &amp; Connectomics at Google, CC BY 4.0. Shapson-Coe et al., <em>Science</em> 384, eadk4858 (2024). Automated segmentation is H01&#39;s <code>c2</code>; the corrected version is one of its 104 manually proofread cells. Rendered by <code>scripts/render_em_figures.py</code>." %}

## 4. Priority-Ranked Proofreading

### 4.1 Definition

Use automated error detection to generate a ranked list of candidate
errors, sorted by estimated downstream impact. Fix the highest-ranked
candidates first, working down the list until a quality target or time
budget is reached.

### 4.2 When to Use

- **Large volumes where exhaustive proofreading is infeasible.** You want
  to maximize quality improvement per hour of human effort.
- **Dataset-wide quality improvement.** Rather than perfecting individual
  neurons, you raise the overall quality floor.
- **Iterative release cycles.** Fix the worst errors before each public
  data release.

### 4.3 Automated Error Detection

Machine learning models can be trained to flag likely errors using features
such as:

- **Contact area at a merge boundary.** A merge that occurs at a single
  point of contact (small area) is more suspicious than one with a broad,
  smooth boundary.
- **Segment size ratio.** A very large segment merged with a very small one
  is more likely an error than two similar-sized segments joining.
- **Shape descriptors.** Sudden changes in curvature, tortuosity, or
  cross-section shape at a boundary suggest a false merge.
- **Agglomeration score.** The automated pipeline's own confidence at each
  merge point. Low-confidence merges are more likely wrong.

Classifiers trained on these features detect merge errors well enough to be
worth running and not well enough to be trusted alone. Zung et al. (2017)
trained 3D convolutional networks that take the image and a candidate object
mask, mark likely split and merge errors in the object, and then prune the
mask toward the true object. Take the precision and recall figures
from the detector you are actually running, on data resembling yours, and
report them alongside your results. A detector's performance on a benchmark
does not transfer to your tissue and your pipeline.

Compartment identity is another cue. Li et al. (2020) trained 3D
convolutional networks to label fragments as axon, dendrite or soma, and used
those labels to find merges between compartment classes. They report
detecting 90.6% of such inter-class merges at a 2.7% false-positive rate, on
their own data. An object that is part thick spiny dendrite and part thin
varicose axon, joined at a single point, is a classic false merge.

### 4.4 Ranking Heuristics

Once candidate errors are detected, rank them by impact:

1. **Large neurons first.** Errors on neurons with extensive arbors affect
   more synapses and more downstream analyses.
2. **High-connectivity errors.** A merge that adds 50 false synapses is
   worse than one that adds 2.
3. **Region of interest.** If the scientific question focuses on layer 4,
   errors in layer 4 rank higher.
4. **Error type.** Merge errors generally rank above split errors because
   they corrupt connectivity more severely.

### 4.5 Instructor Tip

Draw an analogy to triage in emergency medicine: you cannot treat every
patient simultaneously, so you prioritize by severity and treatability.
Similarly, you cannot fix every segmentation error, so you prioritize by
impact and confidence.

---

## 5. Crowd-Sourced Proofreading

### 5.1 The FlyWire Model

Dorkenwald et al. (2024) described the FlyWire project, which produced a
whole-brain connectome of *Drosophila melanogaster*. The authors estimate
that the reconstruction took around 33 person-years of manual proofreading.
Key features they report:

- **Two phases of labor.** In the initial phase, much of the proofreading
  was done by a distributed community of *Drosophila* research groups in
  the FlyWire Consortium, focused on neurons of interest to those groups.
  In the later phase, centralized teams at Princeton and Cambridge
  proofread most of the remaining neurons, with contributions from citizen
  scientists worldwide.
- **Community annotation.** Community members shared 133,700 annotations
  of 114,209 neurons.
- **Accuracy check by re-proofreading.** To estimate remaining error, the
  authors subjected 826 randomly chosen central-brain neurons to a further
  round of proofreading. Measured against that extra round, the released
  reconstructions scored an average F1 of 99.2% by volume.
- **Version control.** Edits were recorded in the ChunkedGraph backend
  that CAVE (Connectome Annotation Versioning Engine) is built on, so any
  past state of the segmentation can be recovered (Dorkenwald et al.,
  2025).

### 5.2 The EyeWire Model

The Seung lab's EyeWire project (Kim et al., 2014) demonstrated that
citizen scientists with no neuroscience background could contribute
meaningful proofreading for retinal connectomics. Key innovations:

- **Game-like interface.** Tracing neurites was presented as a 3D puzzle.
- **Redundancy.** Each task was completed by multiple players; consensus
  determined the final segmentation.
- **Scale.** When the paper appeared, the EyeWire project reported a
  community of about 120,000 players from nearly 150 countries (EyeWire
  blog, 2014). By March 2025 the project reported 350,000 players over
  thirteen years (EyeWire blog, 2025). The two numbers are different dates,
  not a conflict.

### 5.3 When to Use

- **Whole-brain or very large datasets.** The number of errors exceeds
  what a small team can handle.
- **Community engagement.** When building a public resource, crowd-sourcing
  creates a user community invested in the data.
- **Parallelizable tasks.** Proofreading individual neurons is inherently
  parallelizable; different annotators can work on different neurons
  simultaneously with minimal conflict.

### 5.4 Challenges

- **Quality control overhead.** Training, monitoring, and adjudicating
  disagreements requires significant expert time.
- **Coordination.** Preventing conflicting edits when two annotators
  proofread overlapping regions.
- **Attrition.** Volunteer motivation wanes over time; maintaining
  engagement requires active community management.
- **Inter-annotator variability.** Different annotators may apply different
  standards for what constitutes an error.

---

## 6. Hybrid Strategies

Most real-world projects combine multiple strategies. A common recipe:

1. **Priority-ranked pass (weeks 1-4).** Run automated error detection on
   the full volume. Fix the top 1,000 highest-impact candidate errors.
   This raises the overall quality floor quickly.
2. **Targeted pass (weeks 5-12).** For each neuron in the scientific study,
   perform skeleton-guided proofreading. This ensures the specific neurons
   of interest are correct.
3. **Exhaustive pass on focal region (weeks 13-16).** In the core region
   of the study (e.g., a 50 x 50 x 50 um cube), proofread exhaustively
   to produce a gold-standard reference.
4. **Metrics and iteration (ongoing).** Compute quality metrics (VI, ERL)
   on the exhaustive region. If metrics are below target, iterate.

### 6.1 The FlyWire Hybrid

FlyWire combined some of these elements rather than following the recipe
above: automated segmentation, then neuron-by-neuron proofreading first by
a distributed research community and later by centralized teams, then a
further round of proofreading on a sample of neurons to estimate accuracy
(Dorkenwald et al., 2024).

---

## 7. When to Stop Proofreading

### 7.1 Diminishing Returns

Proofreading effort shows diminishing returns. If you rank errors by
impact, the first hours fix the errors that move the metrics most. After
that, each remaining error is harder to find and changes less when fixed.
Plot your own metric against hours spent; the curve tells you when the
next hour is buying little.

### 7.2 Quality Targets

Define stopping criteria before starting:

- **ERL target.** "We will proofread until Expected Run Length exceeds
  100 um for neurons in our region of interest."
- **Edge F1 target.** "We will proofread until edge F1 in the connectivity
  graph exceeds 0.90."
- **Time budget.** "We have allocated 500 person-hours for proofreading.
  We will prioritize within that budget."

### 7.3 Cost-Benefit Analysis

At some point, the cost of finding and fixing the next error exceeds the
benefit of correcting it. This threshold depends on the scientific
question. A study of rare cell types tolerates lower overall quality if
those specific cells are correct. A study of network-wide statistics
needs higher overall quality but can tolerate errors on individual neurons.

### 7.4 Instructor Tip

Ask students: "You have fixed 95 % of detected errors and your ERL is
120 um. Your collaborator wants you to keep going. How do you decide?"
This opens a discussion about opportunity cost, statistical power, and
the difference between "perfect data" and "data good enough to answer the
question."

---

## 8. Worked Example: Designing a Proofreading Campaign

### 8.1 Scenario

You have a freshly segmented 200 x 200 x 100 um volume of mouse visual
cortex (V1, layers 2/3-4). Your scientific goal is to characterize the
connectivity of 100 inhibitory interneurons of four subtypes (PV, SST,
VIP, Lamp5). You have a team of 5 proofreaders and 3 months.

### 8.2 Campaign Design

**Phase 1: Automated triage (week 1)**
- Run automated error detection on the full volume.
- Generate a ranked list of ~15,000 candidate errors.
- Identify the 100 target interneurons using cell-type markers or
  morphological classification.

**Phase 2: Priority-ranked global cleanup (weeks 2-4)**
- Each proofreader processes ~200 high-ranked errors per week.
- Target: fix the top 3,000 errors (those affecting the largest segments
  and the densest connectivity).
- Expected outcome: overall ERL improves from ~20 um to ~60 um.

**Phase 3: Targeted neuron proofreading (weeks 5-10)**
- Assign each proofreader 20 interneurons.
- For each neuron: trace from soma through all dendrites and the local
  axon. Fix all errors encountered.
- Estimated time: 2-4 hours per neuron, 40-80 hours per proofreader.
- Expected outcome: each target neuron is fully reconstructed.

**Phase 4: Connectivity verification (weeks 11-12)**
- For each target neuron, examine all synapses and verify pre/post
  assignment.
- Cross-check: any target neuron forming a synapse with another target
  neuron is verified from both sides.
- Flag autapses and other unusual motifs for expert review.

**Phase 5: Exhaustive benchmark (week 13)**
- Select a 30 x 30 x 30 um cube that contains at least 5 target neurons.
- Proofread exhaustively.
- Compute VI, ERL, and edge F1 against this benchmark.
- Report metrics alongside the published data.

### 8.3 Milestones and Decision Points

- After Phase 2: if ERL < 40 um, extend the priority-ranked phase.
- After Phase 3: if any neuron has more than 3 unresolved ambiguities,
  escalate to expert.
- After Phase 5: if edge F1 < 0.85, return to Phase 3 for additional
  targeted corrections.

---

## 9. References

- Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult
  brain. *Nature*, 634, 124-138. doi:10.1038/s41586-024-07558-y.
- Dorkenwald, S., Schneider-Mizell, C. M., et al. (2025). CAVE: Connectome
  Annotation Versioning Engine. *Nature Methods*, 22, 1112-1120.
  doi:10.1038/s41592-024-02426-z.
- EyeWire. (2014). EyeWire's first scientific discovery and Nature paper.
  EyeWire blog. https://blog.eyewire.org/eyewires-first-scientific-discovery-and-nature-paper/
- EyeWire. (2025, March 31). Announcing EyeWire II. EyeWire blog.
  https://blog.eyewire.org/announcing-eyewire-ii/
- Kasthuri, N., et al. (2015). Saturated reconstruction of a volume of
  neocortex. *Cell*, 162(3), 648-661. doi:10.1016/j.cell.2015.06.054.
- Kim, J. S., et al. (2014). Space-time wiring specificity supports
  direction selectivity in the retina. *Nature*, 509, 331-336.
  doi:10.1038/nature13240.
- Li, H., Januszewski, M., Jain, V., & Li, P. H. (2020). Neuronal
  subcompartment classification and merge error correction. In *Medical
  Image Computing and Computer Assisted Intervention (MICCAI 2020)*,
  Lecture Notes in Computer Science, pp. 88-98.
  doi:10.1007/978-3-030-59722-1_9.
- Zung, J., Tartavull, I., Lee, K., & Seung, H. S. (2017). An error
  detection and correction framework for connectomics. *Advances in
  Neural Information Processing Systems (NeurIPS)*, 30.

---

*End of instructor script: Proofreading Strategies for Connectome Reconstruction*
