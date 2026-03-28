---
title: "Module 06: Segmentation 101"
layout: module
permalink: /modules/module06/
description: "Learn core segmentation concepts, error modes, and practical correction workflows for connectomics."
module_number: 6
difficulty: "Intermediate"
duration: "4 hours"
learning_objectives:
  - "Explain segmentation goals and constraints"
  - "Identify merges, splits, and boundary errors"
  - "Apply a basic correction workflow"
  - "Report segmentation quality with clear metrics"
prerequisites: "Modules 01-05"
merit_stage: "Question"
compass_skills:
  - "Segmentation Literacy"
  - "Error Diagnosis"
  - "Workflow Execution"
ccr_focus:
  - "Skills - Segmentation"
  - "Knowledge - Error Taxonomy"

# Normalized metadata
slug: "module06"
short_title: "Segmentation 101"
status: "active"
audience:
  - "students"
pipeline_stage: "Question"
merit_row_focus: "Question"
topics:
  - "segmentation"
  - "error-modes"
  - "correction"
summary: "Core segmentation workflow, error taxonomy, and correction strategy for connectomics datasets."
key_questions:
  - "How do segmentation errors affect biological interpretation?"
  - "Which corrections should be prioritized first?"
slides: []
notebook: []
datasets:
  - "/datasets/workflow"
  - "/datasets/mouseconnects"
personas:
  - "/avatars/gradstudent"
related_tools:
  - "/tools/connectome-quality/"
related_frameworks:
  - "research-incubator-model"
prerequisites_list: []
next_modules:
  - "module07"
  - "module08"
references: []
videos: []
downloads: []
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
---

## Capability target
Detect and categorize core segmentation errors and execute one correction cycle with documented quality impact.

## Concept set

### 1) What segmentation does and why it matters
Segmentation is the computational process of assigning every voxel in an EM volume to a specific object — not just "this is a neuron" but "this is neuron #47,293." This is instance segmentation, and it's the foundation of the entire connectome. Without accurate segmentation, you cannot identify individual neurons, trace their morphology, or determine their synaptic connections. Modern methods (flood-filling networks, U-Net + watershed + agglomeration) achieve "superhuman" accuracy on benchmarks but still make errors at rates that compound across large volumes.

### 2) Error taxonomy: merge, split, boundary, identity
- **Merge errors**: Two distinct neurons incorrectly joined. Causes: touching membranes with low contrast, blood vessel boundaries, glial wrapping. Impact: false connections in the connectivity graph, inflated cell size. Visual signature: impossible branching in 3D, sudden caliber changes.
- **Split errors**: One neuron broken into fragments. Causes: thin processes (<100 nm), low contrast, missing sections, alignment errors. Impact: missing connections, underestimated arbor, fragmented cells counted as multiple neurons. Visual signature: dead-end processes that should continue.
- **Boundary errors**: Membrane position shifted. Impact: synapse misattribution, morphology distortion. Less dramatic but insidious.
- **Identity errors**: Correct boundary but wrong label propagated. Rare but catastrophic.

### 3) Correction priority: not all errors are equal
The key insight for beginners: fix errors that change your biological conclusions, not errors that look ugly. A merge error connecting two neurons in your circuit of interest is far more important than a split error in a distant fragment you'll never analyze. Impact-weighted triage is essential.

## Core workflow
1. Load segmented patch in Neuroglancer or equivalent viewer.
2. Identify merge/split candidates by scrolling through z and checking 3D meshes for implausible morphology.
3. Apply correction: split merged segments at the boundary, merge split fragments by verifying continuity.
4. Recalculate quality indicators: did the correction improve local metrics?
5. Log decisions: record what was changed, why, and what evidence supported the decision.

## 60-minute tutorial run-of-show (full instructor version)

### Pre-class preparation (10 min async)
- Read the error taxonomy content library entry
- Open the practice dataset in Neuroglancer and browse for 5 minutes

### Minute-by-minute plan
1. **00:00-08:00 | Segmentation goals**
   - "What would a perfect segmentation look like? Every neuron correctly labeled, every membrane correctly placed."
   - Show a well-segmented region side-by-side with raw EM. Point out: each color = one neuron.
   - Then show the same region with errors highlighted. "This is reality. Our job is to find and fix these."

2. **08:00-22:00 | Error taxonomy with real examples**
   - Walk through one merge error: show the 3D mesh with impossible branching, navigate to the merge point in 2D slices, explain why the model failed (low contrast at a blood vessel).
   - Walk through one split error: show a dead-end axon fragment, then the continuation 3 sections later. Explain: thin process + poor contrast = model lost it.
   - Walk through one boundary error: show a synapse attributed to the wrong neuron because the membrane position is off by 2 pixels.
   - For each: "What would this error do to your analysis?"

3. **22:00-36:00 | Guided correction round**
   - Learners work in pairs on 3 pre-identified errors (1 merge, 1 split, 1 ambiguous).
   - Instructor circulates, coaching on: "Show me the evidence before you correct." "What would happen if this merge is actually correct — two branches of the same neuron?"

4. **36:00-48:00 | Quality metric interpretation**
   - Introduce: "How do we know if our corrections actually helped?"
   - Brief overview of metrics: edge precision/recall (are the connections right?), segment size distributions (do sizes look biological after correction?).
   - Compute metrics before and after the correction round. Did they improve?

5. **48:00-60:00 | Debrief and competency check**
   - Each learner presents one correction with evidence chain.
   - Group discussion: "Which correction had the biggest impact on the graph? Why?"
   - Exit ticket: "Name the error type you found hardest to detect and why."

## Studio activity: correction triage simulation (60-75 minutes)

**Scenario:** Your team has a freshly segmented 50x50x50 um subvolume containing approximately 200 neuron fragments. Automated error detection has flagged 25 candidate errors. You have time to fix 10.

**Task sequence:**
1. Review all 25 flagged candidates and classify each by error type (merge/split/boundary/uncertain).
2. Rank by estimated impact: which corrections would most change the connectivity graph?
3. Fix the top 10 in priority order, documenting each correction.
4. Compute before/after metrics for the subvolume.
5. Write a 3-sentence "release note" summarizing what was fixed and what remains.

**Expected outputs:**
- Ranked error list with type classifications and impact estimates.
- Correction log with before/after evidence for each fix.
- Metric summary table.
- Release note.

## Assessment rubric
- **Minimum pass**: Correct error labels and at least one valid correction with evidence.
- **Strong performance**: Correction prioritization explicitly tied to downstream analysis impact. Metrics show measurable improvement.
- **Common failure to flag**: Correction without evidence of quality change — fixing things without checking whether it helped.

## Content library references
- [Error taxonomy]({{ '/content-library/proofreading/error-taxonomy/' | relative_url }}) — Detailed merge/split/boundary/identity error descriptions
- [Proofreading strategies]({{ '/content-library/proofreading/proofreading-strategies/' | relative_url }}) — Exhaustive, targeted, priority-ranked approaches
- [Proofreading tools]({{ '/content-library/proofreading/proofreading-tools/' | relative_url }}) — CAVE, Neuroglancer, editing operations
- [Metrics and QA]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}) — VI, ERL, edge F1 formulas and interpretation
- [Reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }}) — Where segmentation fits in the pipeline

## Teaching resources
- [Technical Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
- [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})

## References
- Januszewski M et al. (2018) "High-precision automated reconstruction of neurons with flood-filling networks." *Nature Methods* 15(8):605-610.
- Lee K et al. (2019) "Superhuman accuracy on the SNEMI3D connectomics challenge." *arXiv:1706.00120*.
- Funke J et al. (2019) "Large scale image segmentation with structured loss." *IEEE TPAMI* 41(7):1669-1680.
- Dorkenwald S et al. (2024) "Neuronal wiring diagram of an adult brain." *Nature* 634:124-138.

## Quick practice prompt
Explain when you would defer a correction instead of fixing immediately.
