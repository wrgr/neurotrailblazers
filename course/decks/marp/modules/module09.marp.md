---
marp: true
theme: default
paginate: true
title: "Module 09: Neuron Morphology and Skeletonization"
---

# Module 09: Neuron Morphology and Skeletonization
Teaching Deck

---

## Learning Objectives
- Generate skeleton representations from reconstructed neurites
- Compute core morphology descriptors
- Relate morphology metrics to biological interpretation
- Report morphology uncertainty and classification limits

---

## Session Outcomes
- Learners can complete the module capability target.
- Learners can produce one evidence-backed artifact.
- Learners can state one limitation or uncertainty.

---

## Agenda (60 min)
- 0-10 min: Frame and model
- 10-35 min: Guided practice
- 35-50 min: Debrief and misconception correction
- 50-60 min: Competency check + exit ticket

---

## Capability Target
Produce a skeleton-based morphology summary with at least three descriptors and one explicit limitation.

---

## Concept Focus
### 1) What is skeletonization and why do we need it?
A segmented neuron occupies millions of voxels in the EM volume. To analyze its morphology efficiently, we reduce it to a **skeleton**: a tree graph where nodes represent points along the neurite centerline and edges represent the path between them. Skeletons compress a neuron's 3D structure from gigabytes to kilobytes while preserving topology (branching pattern, path lengths, connectivity).

---

## Core Workflow
- Build skeleton from volumetric segmentation using TEASAR or equivalent algorithm.
- Quality-check the skeleton: prune spurious branches, verify branch points, check for disconnected fragments.
- Compute descriptors: cable length, branch points, Strahler number, Sholl profile, spine density.
- Compare against reference patterns: does this neuron match the expected morphology for its putative cell type?
- Report interpretation confidence: which descriptors are robust, which are affected by reconstruction quality?

---

## 60-Minute Run-of-Show
- Review the data formats content library entry (skeletons section)
- Install/check NeuroM or equivalent morphology analysis package
- **00:00-10:00 | Morphology overview**
- "Why do we care about neuron shape?" — Shape constrains function: a neuron's dendritic arbor determines what inputs it can receive; its axonal arbor determines where it can send output.
- Show 3 neuron types (pyramidal, basket, Martinotti) and their characteristic morphologies.
- "Today you'll learn to quantify these shapes from EM data."
- **10:00-24:00 | Skeleton extraction demo**
- Live demo: take a segmented neuron, run skeletonization, visualize result in Neuroglancer.
- Walk through SWC format: "Each line is a node. Parent ID tells you the tree structure."
- Common pitfall: show a skeleton with spurious branches from noisy segmentation. Demonstrate pruning.
- **24:00-38:00 | Descriptor calculation**
- Hands-on: learners compute 5 descriptors for one neuron using NeuroM or provided scripts.
- Compare results across the group: did everyone get the same numbers? Discuss sources of variation.
- Introduce Sholl analysis with live visualization.
- **38:00-50:00 | Interpretation and caveats**
- "Your neuron has total cable length of 2,100 μm and 47 branch points. Is that a lot?" — Compare to published values for the putative cell type.
- Discussion: which descriptors are robust to reconstruction errors? (Cable length is sensitive to splits; branch count is sensitive to both splits and spurious branches; spine density is robust if the segmentation boundary is accurate.)
- "What if 30% of the arbor is outside the volume? How does that change your interpretation?"
- **50:00-60:00 | Competency check**
- Each learner submits their morphology descriptor table with:
- At least 3 descriptors with values
- Putative cell-type classification based on morphology
- One explicit limitation of the measurement
- Exit ticket: "Name one morphology feature that could be confounded by reconstruction quality."

---

## Misconceptions to Watch
- **Misconception guardrail:** a skeleton is a lossless summary of a neuron rather than a representation that discards surface geometry and spine shape.
- **Misconception guardrail:** morphological measurements are comparable across cells that were proofread to different levels.
- **Misconception guardrail:** total dendritic length is a property of the neuron rather than a property of the reconstruction of that neuron.
- **Misconception guardrail:** a cell type assigned from morphology alone needs no corroboration from connectivity or molecular identity.

---

## Studio Activity
**Scenario:** You have skeletons for 10 neurons in L2/3 of mouse visual cortex. Your task is to classify them as pyramidal vs interneuron based on morphology alone, then validate against synapse-based classification (excitatory vs inhibitory output synapses).

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
- **Minimum pass**: Valid skeleton and descriptor set for all neurons. At least 3 descriptors.
- **Strong performance**: Robust interpretation linking descriptors to cell-type identity. Explicit uncertainty framing for borderline cases. Investigation of mismatches.
- **Common failure to flag**: Descriptor list without biological context — reporting numbers without explaining what they mean for the neuron's identity.

---

## Exit Ticket
Explain one morphology feature that could be confounded by reconstruction quality.

---

## References (Instructor)
- Use module references listed on the module page.

---

## Teaching Materials
- Module page: /modules/module09/
- Slide page: /modules/slides/module09/
- Worksheet: /assets/worksheets/module09/module09-activity.md
