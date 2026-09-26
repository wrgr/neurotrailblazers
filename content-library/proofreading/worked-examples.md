---
layout: page
title: "Proofreading Worked Examples"
permalink: /content-library/proofreading/worked-examples/
image: /assets/images/content-library/proofreading/worked-examples.svg
image_alt: "Stylized vector art: a traced process with marked error sites under review."
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
  - "08"
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
combines_with:
  - error-taxonomy
  - proofreading-strategies
  - proofreading-tools
  - metrics-and-qa
use_layout_hero: false
content_type: core
---

# Proofreading Worked Examples

Five step-by-step proofreading scenarios, each modeled on a situation that
comes up in real reconstruction projects. Each one runs from detection through
investigation and correction to validation.

The scenarios are set in **release T75 of a fictional mouse cortex volume**. The
volume, the release, the neuron IDs and every measurement in Scenarios 1 to 5
are invented for teaching. The only real data on this page is the H01 figure
after Scenario 1, and its caption says so.

Button names and keyboard shortcuts differ between viewers and change between
versions, so the steps describe the operation rather than the key to press.

---

## Scenario 1: Merge Error at a Blood Vessel

### Background

Blood vessels are a known site of merge errors in automated segmentation. The
vessel wall adds membrane-like edges of its own, and thin processes pressed
against it can lose the faint boundary between them. When two neurons run
along the same vessel, the segmentation can fuse them into one segment.

### Detection

During a routine check of large reconstructed neurons, a proofreader notices
a suspicious branch in the 3D mesh view. The neuron seems to split into two
major arbors that leave in opposite directions from a single point next to a
blood vessel.

Neurites do branch, and some real branches are T-shaped. What makes this one
suspicious is the combination: two large arbors, mismatched caliber, opposite
directions, and a branch point sitting on a vessel wall.

### Step-by-Step Resolution

**Step 1 -- Identify the junction in 3D.**
Rotate the 3D mesh to isolate the suspicious branch point. Note the coordinates
and the proximity to the blood vessel. Mark the location with an annotation
point for reference.

**Step 2 -- Verify in 2D image slices.**
Navigate to the branch point coordinates in the 2D slice view. Scroll through
consecutive z-sections to observe how
the two processes relate to the vessel wall. Look for a gap in membrane between
the two processes -- if no clear membrane boundary exists in the EM images, the
merge may have occurred because the boundary was genuinely ambiguous.

**Step 3 -- Find the exact merge point.**
Identify the z-sections where the two processes share a single segment label
despite belonging to different neurons. Often this is only a few sections,
where contrast is lowest. Note the section range.

**Step 4 -- Execute the split.**
Use the editing tool your project provides (for example, the FlyWire
interface for FAFB, or Neuroglancer or Spelunker on a CAVE datastack). You
need edit rights: public releases such as MICrONS `minnie65_public` are for
reading, not editing.

In CAVE-based systems:
- Select the segment.
- Place several points of one color on one neuron's process, starting near
  where the merge begins.
- Place several points of the other color on the other neuron's process.
- Preview the split, then submit it. The tool computes a cut in the
  supervoxel graph; the image data do not change.

**Step 5 -- Validate both resulting fragments.**
After the split, inspect each resulting neuron independently:
- Does each neuron have a plausible morphology?
- Do both neurons have cell bodies (or extend to the volume boundary)?
- Are caliber and branching patterns internally consistent?

**Step 6 -- Recheck synapses.**
While the merge stood, every synapse on either neuron was credited to one
merged object. Review the synapses within a few micrometers of the cut to
confirm each lands on the correct pre- and postsynaptic segment.

### Lessons

- Blood vessels, glial wrapping, and fixation artifacts are known sites of
  merge errors.
- Always inspect suspicious branch points in both 3D and 2D.
- After every split, validate synapses near the correction site.

---

{% include figure.html
   src="/assets/images/content-library/em/proofreading-before-after.jpg"
   alt="Three panels of the same human cortex field: raw electron microscopy; the automated segmentation showing one object in green with a wrongly attached region in red; and the proofread result with only the green object remaining."
   caption="A real merge error, before and after a human fixed it. Left: raw EM. Middle: the automated segmentation calls all of this one cell. Green is part of the cell; red is a separate process it absorbed. Right: the proofread version, with those 11,038 voxels of this section removed. Look at the raw panel again and ask whether you would have caught it. The boundary the algorithm crossed is a real membrane, but a faint one, and the absorbed process would pass as a branch. This is why merges are hard to see."
   credit="H01 human cortex, Lichtman Lab (Harvard) &amp; Connectomics at Google, CC BY 4.0. Shapson-Coe et al., <em>Science</em> 384, eadk4858 (2024). Automated segmentation is H01&#39;s <code>c2</code>; the corrected version is one of its 104 manually proofread cells. Rendered by <code>scripts/render_em_figures.py</code>." %}

## Scenario 2: Split Neuron Through Low-Contrast Sections

### Background

Thin axons, around 150 nm across, are prone to split errors. When an axon passes through a region of poor staining, low
contrast, or sectioning artifact spanning multiple consecutive z-sections, the
segmentation algorithm may lose track of the process and terminate the segment.
The continuation on the other side becomes an orphan fragment.

### Detection

While tracing a pyramidal neuron's axon, the proofreader encounters a dead end.
The axon ends abruptly, well inside the volume, with no terminal bouton or
synaptic specialization: just a clean cut. That points to a split error.
Nearby, the proofreader notices a small orphan fragment with similar caliber
and trajectory, offset by 3 z-sections.

### Step-by-Step Resolution

**Step 1 -- Confirm the dead end is not biological.**
Check that the ending is not at the edge of the volume, then look for a
terminal bouton, a vesicle cluster, or accumulated mitochondria. A real axon
ending usually shows these. A bare, blunt ending in the middle of the volume
suggests a segmentation break.

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
- Caliber: should be similar. Boutons and varicosities make axon caliber vary
  along its length, so compare a few sections on each side rather than one.
- Position: extrapolate the trajectory; the fragment should lie along the
  expected path.
- Organelle content: mitochondria, microtubules, vesicles.

**Step 5 -- Execute the merge.**
Select the parent segment (the main axon) and the orphan fragment. In
CAVE-based tools you connect a point on each and submit the merge; the system
adds an edge between the two supervoxels and joins them into one segment.

**Step 6 -- Validate the merge.**
Scroll through the repaired region to confirm continuity. Check that the merged
neuron has a plausible morphology and that no unrelated processes were
accidentally included.

### Lessons

- Thin axons are especially prone to split errors. How common splits are
  relative to merges depends on the pipeline's agglomeration threshold (see
  [Error taxonomy]({{ '/content-library/proofreading/error-taxonomy/' | relative_url }})).
- A dead end inside the volume with no synaptic specialization is usually a
  segmentation break. Dendrites also end, so judge a dendritic tip by its
  taper, not by the absence of a bouton.
- Adjust brightness and contrast when working with low-quality
  sections.

---

## Scenario 3: False Autapse from a Merge Error

### Background

An autapse is a synapse a neuron makes onto itself. Autapses are real: they
are well documented on some cortical inhibitory interneurons (Tamás et al.,
1997). So a single self-synapse proves nothing. A cluster of them on one cell,
especially a cell type where they are not expected, is a reason to look for a
merge error in the segmentation.

### Detection

During connectivity analysis of release T75, a computational neuroscientist
finds that neuron 48372, a layer 2/3 pyramidal cell, appears to form 12
autapses. That is enough to send it to proofreading.

### Step-by-Step Resolution

**Step 1 -- Navigate to a flagged autapse.**
Select one of the 12 candidate autapses and navigate to its coordinates in the
viewer. First check that it is a synapse at all: identify the presynaptic bouton
(with vesicles) and the postsynaptic density (PSD). A false synapse detection
is a second way to get an apparent autapse.

**Step 2 -- Check the segment IDs.**
Verify that the presynaptic and postsynaptic structures are both labeled as
neuron 48372. Visually, they should appear as distinct processes -- typically
an axon (presynaptic) and a dendrite (postsynaptic) that happen to share the
same segment label.

**Step 3 -- Trace back from the postsynaptic process.**
Follow the postsynaptic dendrite away from the synapse, back toward what should
be its cell body. If neuron 48372 is a merge of two neurons, at some point the
dendrite will pass through a merge site where it was incorrectly joined to the
other neuron's arbor.

**Step 4 -- Find the distant merge point.**
The merge point may be far from the autapse itself -- sometimes hundreds of
micrometers away. Look for the same signs as in Scenario 1: suspicious branch
points, caliber changes, or proximity to blood vessels or other artifacts. In
this example, the merge point is found 200 micrometers away, near a section
fold.

**Step 5 -- Execute the split.**
Split neuron 48372 at the identified merge point, creating two separate neurons.
The "autapses" should now become normal synapses between two different neurons.

**Step 6 -- Verify resolution.**
After splitting:
- Confirm that the 12 autapses are now synapses between two distinct neurons.
  In CAVE-based systems both pieces get new root IDs, so query by the new IDs.
- Verify that both resulting neurons have plausible morphologies.
- Check that any remaining self-synapses (if any) are biologically plausible.

### Lessons

- Apparent autapses are a useful computational signal for detecting merge
  errors.
- The merge point may be far from the synapse that revealed the error.
- Automated screens for biological implausibility are valuable quality-control
  tools.

---

## Scenario 4: Priority Triage for a Large Proofreading Campaign

### Background

A freshly segmented cortical volume has been processed through the automated
pipeline. The error-detection algorithms have flagged approximately 10,000
candidate errors. The proofreading team has a budget of 2 hours for an initial
triage session.

Do the arithmetic first. At 3 to 5 minutes per candidate, 2 hours covers 24 to
40 candidates: at most 0.4% of the queue. The session cannot clear the queue,
so the question is which 40 to look at.

### Triage Strategy

**Step 1 -- Establish ranking criteria.**

Rank errors by expected scientific impact:

1. **Large segments over small fragments.** Errors in neurons with extensive
   arbors affect more downstream analyses (connectivity, morphometry) than
   errors in tiny orphan fragments.
2. **Errors in the region of interest (ROI) over those outside.** If the
   scientific question concerns layer 4 of barrel cortex, prioritize errors in
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
As you move down the priority list, the impact per correction should fall. Set a
stopping rule before you start, for example when the true-positive rate over
the last 10 candidates drops below 30%, or the segments affected fall below a
size you choose. The 30% is a team choice, not a published standard. The rule
does not tell you how many errors remain below the cut; only an audit of a
random sample does that.

**Step 6 -- Report and plan.**
At the end of the 2-hour session, summarize:
- Total errors reviewed.
- Total corrections made.
- Estimated impact (e.g., number of synapses affected).
- Recommendation for additional proofreading time, if needed.

### Lessons

- With a sorted queue, the first hour of proofreading usually buys more than
  the tenth.
- Decide the stopping rule before the session, not during it.
- Log every outcome, including false positives. The false-positive rate is how
  you judge the detector next time.

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
- Spines: does spine density change abruptly at the junction?
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

- Disagreements are normal. They point to the ambiguous cases that need
  written guidelines.
- Combine the evidence (morphology, organelles, synapse patterns); no single
  cue settles a hard case.
- Recalibrate the team regularly, because drift between annotators is slow and
  easy to miss.

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

## Further reading

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

- Tamás, G., Buhl, E. H., & Somogyi, P. (1997). Massive autaptic
  self-innervation of GABAergic neurons in cat visual cortex. *Journal of
  Neuroscience*, 17(16), 6352-6364.
