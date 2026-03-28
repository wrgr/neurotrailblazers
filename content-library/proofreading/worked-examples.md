---
layout: page
title: "Proofreading Worked Examples"
permalink: /content-library/proofreading/worked-examples/
description: "Five detailed step-by-step proofreading scenarios covering merge errors, split errors, false autapses, priority triage, and cross-annotator disagreement resolution in connectomics reconstruction."
topics:
  - proofreading
  - merge errors
  - split errors
  - segmentation quality
  - annotation workflows
  - error triage
  - consensus protocols
primary_units:
  - unit-proofreading-fundamentals
  - unit-error-detection
  - unit-proofreading-workflows
difficulty: intermediate
tags:
  - proofreading:merge-error
  - proofreading:split-error
  - proofreading:error-triage
  - infrastructure:cave
  - infrastructure:neuroglancer
  - methodology:consensus-protocol
  - case-studies:proofreading-scenarios
micro_lesson_id: ml-proof-worked
reference_images:
  - src: /assets/images/content-library/proofreading/worked-examples/merge-before-after.png
    alt: "Before and after views of a merge error correction at a blood vessel"
    caption: "Merge error correction: before (left) two neurons share one segment near a blood vessel; after (right) correctly separated into distinct segments."
  - src: /assets/images/content-library/proofreading/worked-examples/split-before-after.png
    alt: "Before and after views of a split error correction through low-contrast sections"
    caption: "Split error correction: before (left) neuron fragmented at thin axon; after (right) fragments joined into complete morphology."
  - src: /assets/images/content-library/proofreading/worked-examples/autapse-detection-workflow.png
    alt: "Workflow diagram showing how false autapses reveal hidden merge errors"
    caption: "False autapse detection: connectivity analysis flags self-synapses, leading to discovery of a distant merge error 200 um away."
combines_with:
  - error-taxonomy
  - proofreading-strategies
  - proofreading-tools
  - metrics-and-qa
---

# Proofreading Worked Examples

This page presents five detailed, step-by-step proofreading scenarios drawn from
real-world connectomics reconstruction projects. Each scenario walks through the
full cycle of error detection, investigation, correction, and validation. Working
through these examples will prepare you to handle the most common (and some
uncommon) challenges encountered during large-scale proofreading campaigns.

---

## Scenario 1: Merge Error at a Blood Vessel

### Background

Blood vessels are one of the most common sources of merge errors in automated
segmentation. The vascular lumen appears dark in EM images, and thin neuronal
processes that pass close to vessel walls can share similar contrast profiles.
When two neurons course near the same blood vessel, the segmentation algorithm
may incorrectly fuse them into a single segment.

### Detection

During routine quality-control inspection of large reconstructed neurons, a
proofreader notices a suspicious branching pattern in the 3D mesh view. The
neuron appears to split into two major arbors that diverge in opposite
directions from a single point adjacent to a blood vessel. This branching
geometry is biologically implausible: real neurons do not produce symmetric
bifurcations from mid-axon points.

Key clue: the branching angle and caliber of the two arbors are inconsistent
with normal axonal or dendritic branching patterns.

### Step-by-Step Resolution

**Step 1 -- Identify the junction in 3D.**
Rotate the 3D mesh to isolate the suspicious branch point. Note the coordinates
and the proximity to the blood vessel. Mark the location with an annotation
point for reference.

**Step 2 -- Verify in 2D image slices.**
Navigate to the branch point coordinates in the 2D slice view (e.g., in
Neuroglancer or CATMAID). Scroll through consecutive z-sections to observe how
the two processes relate to the vessel wall. Look for a gap in membrane between
the two processes -- if no clear membrane boundary exists in the EM images, the
merge may have occurred because the boundary was genuinely ambiguous.

**Step 3 -- Find the exact merge point.**
Identify the specific z-section(s) where the two processes share a single
segment label despite belonging to different neurons. Often this is just 2-5
sections where contrast is lowest. Note the section range.

**Step 4 -- Execute the split.**
Using the proofreading tool (e.g., CAVE/Spelunker for MICrONS, FlyWire for
FAFB), place a split point on one side of the merge and a second split point on
the other side. The tool will recompute the segmentation graph and separate the
two neurons.

In CAVE-based systems:
- Select the segment.
- Place red (foreground) points on one neuron's process.
- Place blue (background) points on the other neuron's process.
- Submit the split operation.

**Step 5 -- Validate both resulting fragments.**
After the split, inspect each resulting neuron independently:
- Does each neuron have a plausible morphology?
- Do both neurons have cell bodies (or extend to the volume boundary)?
- Are caliber and branching patterns internally consistent?

**Step 6 -- Recheck synapses.**
Automated synapse detection may have assigned synapses to the wrong partner
neuron due to the merge. Review synapses within 5 micrometers of the split point
to confirm they are assigned to the correct pre- and post-synaptic segments.

### Lessons

- Blood vessels, glial wrapping, and fixation artifacts are the top three causes
  of merge errors (Dorkenwald et al., 2024).
- Always inspect suspicious branch points in both 3D and 2D.
- After every split, validate synapses near the correction site.

---

## Scenario 2: Split Neuron Through Low-Contrast Sections

### Background

Thin axons (approximately 150 nm diameter) are particularly vulnerable to
split errors. When an axon passes through a region of poor staining, low
contrast, or sectioning artifact spanning multiple consecutive z-sections, the
segmentation algorithm may lose track of the process and terminate the segment.
The continuation on the other side becomes an orphan fragment.

### Detection

While tracing a pyramidal neuron's axon, the proofreader encounters a dead end.
The axon terminates abruptly without a terminal bouton or any synaptic
specialization -- just a clean cut. This is a strong indicator of a split error.
Nearby, the proofreader notices a small orphan fragment with similar caliber
and trajectory, offset by 3 z-sections.

### Step-by-Step Resolution

**Step 1 -- Confirm the dead end is not biological.**
Check for terminal boutons, synaptic vesicle clusters, or mitochondria
accumulation at the terminal. A true axon terminal will typically show synaptic
specializations. A bare, blunt ending strongly suggests a segmentation break.

**Step 2 -- Scroll through the bad sections.**
Navigate through the 2D slices in the region of the break. Note the image
quality: look for staining gaps, section folds, knife marks, or charging
artifacts. In this case, 3 consecutive sections show notably reduced contrast.

**Step 3 -- Find the faint continuation.**
Even in low-contrast sections, faint membrane outlines may be visible. Adjust
brightness and contrast settings in the viewer. The axon may appear as a barely
visible gray circle of approximately 150 nm diameter.

**Step 4 -- Verify caliber and trajectory match.**
Measure the cross-sectional diameter of the axon on the last good section before
the break and the first good section after. Compare:
- Caliber: should be within 20-30% (axons taper gradually).
- Position: extrapolate the trajectory; the fragment should lie along the
  expected path.
- Organelle content: mitochondria density, microtubule orientation.

**Step 5 -- Execute the merge.**
Select the parent segment (the main axon) and the orphan fragment. In
CAVE-based tools, this typically involves selecting both segments and submitting
a merge operation. The system will join them into a single segment.

**Step 6 -- Validate the merge.**
Scroll through the repaired region to confirm continuity. Check that the merged
neuron has a plausible morphology and that no unrelated processes were
accidentally included.

### Lessons

- Split errors in thin axons are the most common error type in cortical EM
  datasets (Plaza et al., 2014).
- Dead ends without synaptic specialization are almost always segmentation
  breaks.
- Brightness/contrast adjustment is essential when working with low-quality
  sections.

---

## Scenario 3: False Autapse from a Merge Error

### Background

An autapse is a synapse in which a neuron synapses onto itself. While autapses
do occur in biology, they are extremely rare in mammalian cortex. When automated
analysis of a connectome flags a large number of autapses, or autapses on
neurons where they are not expected, the most likely explanation is a merge error
in the underlying segmentation.

### Detection

During connectivity analysis, a computational neuroscientist discovers that
neuron #48372 appears to form 12 autapses. This is highly unusual for a layer
2/3 pyramidal neuron. The finding is flagged for proofreading investigation.

### Step-by-Step Resolution

**Step 1 -- Navigate to a flagged autapse.**
Select one of the 12 candidate autapses and navigate to its coordinates in the
viewer. Examine the synapse: identify the presynaptic bouton (with vesicles) and
the postsynaptic density (PSD).

**Step 2 -- Check the segment IDs.**
Verify that the presynaptic and postsynaptic structures are both labeled as
neuron #48372. Visually, they should appear as distinct processes -- typically
an axon (presynaptic) and a dendrite (postsynaptic) that happen to share the
same segment label.

**Step 3 -- Trace back from the postsynaptic process.**
Follow the postsynaptic dendrite away from the synapse, back toward what should
be its cell body. If neuron #48372 is a merge of two neurons, at some point the
dendrite will pass through a merge site where it was incorrectly joined to the
other neuron's arbor.

**Step 4 -- Find the distant merge point.**
The merge point may be far from the autapse itself -- sometimes hundreds of
micrometers away. Look for the same signs as in Scenario 1: suspicious branch
points, caliber changes, or proximity to blood vessels or other artifacts. In
this example, the merge point is found 200 micrometers away, near a section
fold.

**Step 5 -- Execute the split.**
Split neuron #48372 at the identified merge point, creating two separate neurons.
The "autapses" should now become normal synapses between two different neurons.

**Step 6 -- Verify resolution.**
After splitting:
- Confirm that the 12 autapses are now distributed as synapses between two
  distinct neurons.
- Verify that both resulting neurons have plausible morphologies.
- Check that any remaining self-synapses (if any) are biologically plausible.

### Lessons

- Apparent autapses are a powerful computational signal for detecting merge
  errors (Berger et al., 2018).
- The merge point may be far from the synapse that revealed the error.
- Automated screens for biological implausibility are valuable quality-control
  tools.

---

## Scenario 4: Priority Triage for a Large Proofreading Campaign

### Background

A freshly segmented cortical volume has been processed through the automated
pipeline. The error-detection algorithms have flagged approximately 10,000
candidate errors. The proofreading team has a budget of 2 hours for an initial
triage session. How should they prioritize?

### Triage Strategy

**Step 1 -- Establish ranking criteria.**

Rank errors by expected scientific impact:

1. **Large segments over small fragments.** Errors in neurons with extensive
   arbors affect more downstream analyses (connectivity, morphometry) than
   errors in tiny orphan fragments.
2. **Errors in the region of interest (ROI) over those outside.** If the
   scientific question concerns layer 4 barrel cortex, prioritize errors in
   that region.
3. **Merge errors over split errors.** Merges corrupt two neurons at once and
   distort connectivity matrices more severely. Splits affect one neuron's
   completeness but typically do not create false connections.
4. **Errors near synapses over those in bare neuropil.** Corrections near
   synaptic sites directly improve connectivity data quality.

**Step 2 -- Sort the error queue.**
Use the error-detection output to sort candidates by a composite priority score.
Many proofreading platforms allow custom sorting. Apply the criteria above to
generate a ranked list.

**Step 3 -- Work top-down.**
Begin with the highest-priority error. For each candidate:
- Inspect in 2D and 3D (allocate 3-5 minutes per error).
- If the error is confirmed, correct it immediately.
- If the candidate is a false positive, dismiss it.
- Log the outcome (true positive, false positive, deferred).

**Step 4 -- Track metrics in real time.**
After each correction, note:
- Time spent.
- Error type (merge, split, false positive).
- Segment size affected.

**Step 5 -- Monitor for plateau.**
As you move down the priority list, the impact per correction decreases. When
the rate of true positives drops below 30%, or average segment size affected
drops below a threshold, consider stopping. The remaining errors likely have
minimal impact on downstream analyses.

**Step 6 -- Report and plan.**
At the end of the 2-hour session, summarize:
- Total errors reviewed.
- Total corrections made.
- Estimated impact (e.g., number of synapses affected).
- Recommendation for additional proofreading time, if needed.

### Lessons

- Prioritization is essential: not all errors are equally important
  (Dorkenwald et al., 2022).
- Diminishing returns are real. The first hour of proofreading typically
  produces more scientific value than the tenth.
- Metrics-driven stopping criteria prevent wasted effort.

---

## Scenario 5: Cross-Annotator Disagreement

### Background

Two experienced proofreaders, Annotator A and Annotator B, are independently
reviewing the same region of a cortical dataset. They disagree about whether a
particular dendritic process belongs to one neuron or represents two merged
neurons. Annotator A believes it is a single neuron with an unusual morphology.
Annotator B believes it is a merge error.

### Resolution Protocol

**Step 1 -- Each annotator presents their evidence.**

Annotator A's case for a single neuron:
- The process has consistent caliber throughout.
- Microtubule orientation is uniform.
- The branching pattern, while unusual, is within the range of normal variation
  for this cell type.

Annotator B's case for a merge error:
- At one point, the process passes very close to a blood vessel.
- The synapse types on one branch are exclusively excitatory, while the other
  branch receives exclusively inhibitory synapses -- unusual for a single
  dendrite.
- A slight caliber change occurs near the vessel.

**Step 2 -- Check organelle and synaptic cues.**
Together, the annotators examine:
- Mitochondrial morphology: are mitochondria consistent throughout, or do they
  change character at the disputed junction?
- Endoplasmic reticulum: continuity of smooth ER is a strong indicator of a
  single process.
- Synaptic input patterns: statistically unusual distributions may indicate a
  merge.

**Step 3 -- Inspect in 3D.**
Render the disputed segment as a 3D mesh. Rotate to examine the junction from
multiple angles. Look for:
- Pinch points (narrowing at the junction) suggestive of a merge artifact.
- Smooth, natural-looking transitions suggestive of a real branch point.

**Step 4 -- Reach consensus or escalate.**
Based on the combined evidence:
- If both annotators agree after discussion, apply the correction (or confirm
  the segment is correct).
- If disagreement persists, escalate to a senior proofreader or domain expert.
  Provide all evidence, including screenshots and coordinates.

**Step 5 -- Update team calibration.**
Regardless of the outcome, document the case as a calibration example:
- Add it to the team's training materials.
- If the disagreement revealed an ambiguous morphological feature, develop
  explicit guidelines for handling similar cases in the future.
- Review inter-annotator agreement metrics and schedule recalibration sessions
  if disagreement rates are rising.

### Lessons

- Disagreements are normal and healthy -- they reveal ambiguous cases that need
  explicit guidelines (Berger et al., 2018).
- Multiple lines of evidence (morphology, organelles, synapse patterns) should
  be combined, not relied upon individually.
- Calibration is an ongoing process, not a one-time event.

---

## Summary Table

| Scenario | Error Type | Key Detection Signal | Primary Tool/View |
|----------|-----------|---------------------|-------------------|
| 1. Blood vessel merge | Merge | Impossible branching in 3D | 3D mesh + 2D slices |
| 2. Low-contrast split | Split | Dead end without bouton | 2D slices with contrast adjustment |
| 3. False autapse | Merge | Biologically implausible self-synapse | Connectivity analysis + 2D |
| 4. Triage | Multiple | Automated error detection | Priority queue + metrics |
| 5. Disagreement | Ambiguous | Annotator conflict | Multi-evidence protocol |

---

## References

- Berger, D. R., Seung, H. S., & Lichtman, J. W. (2018). VAST (Volume
  Annotation and Segmentation Tool): Efficient manual and semi-automatic
  labeling of large 3D image stacks. *Frontiers in Neural Circuits*, 12, 88.

- Dorkenwald, S., et al. (2022). FlyWire: Online community for whole-brain
  connectomics. *Nature Methods*, 19(1), 119-128.

- Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain.
  *Nature*, 634, 124-138.

- Plaza, S. M., Scheffer, L. K., & Chklovskii, D. B. (2014). Toward
  large-scale connectome reconstructions. *Current Opinion in Neurobiology*,
  25, 201-210.
