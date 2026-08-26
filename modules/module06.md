---
title: "Module 06: Segmentation 101"
layout: module
permalink: /modules/module06/
description: "Learn core segmentation concepts, error modes, and practical correction workflows for connectomics."
module_number: 6
image: /assets/images/modules/module06.svg
image_alt: "Stylized vector art: a tile mosaic with one region flood-filled across tile boundaries."
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
content_type: path
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

### Misconception guardrails

Each of these is a belief a learner plausibly holds on arriving. Name it, then check your own work against it.

- **Misconception guardrail:** merge and split errors are equally costly, so error counts alone rank corrections.
- **Misconception guardrail:** an object that looks like a plausible neuron is evidence that the segmentation is correct.
- **Misconception guardrail:** the most visually obvious errors are the ones most worth fixing.
- **Misconception guardrail:** a segmentation can be finished, rather than released at a stated level with stated remaining error.

## Worked example: object 8841 and the split you almost fixed first

The numbers below are illustrative — they show the shape of the reasoning, not results from a specific dataset.

You are proofreading a 50x50x50 µm subvolume ahead of a connectivity analysis of layer 2/3 pyramidal cells. Two flagged candidates sit at the top of your queue, and you have about one hour of annotator time: object 8841, flagged for implausible morphology, and object 5510, a dead-end axon fragment flagged as a probable split. The split looks easier and more satisfying to fix. Here is why the expert fixes the other one first.

**Step 1 — Diagnose before editing.** Load 8841's 3D mesh. It has two somata roughly 180 µm apart joined by a single thin process. Two somata in one object is a merge until proven otherwise, so trace the connecting process in 2D: caliber holds near 0.8 µm on both sides, then drops abruptly to about 0.2 µm across three sections that also contain a fold artifact. Abrupt caliber change plus a low-evidence artifact region is the classic merge site — the model had almost nothing to work with there and guessed wrong.

**Step 2 — Estimate graph impact before fixing anything.** Object 8841 carries 212 synapses and 47 synaptic partners. If it is really two neurons, every one of those synapses is currently attributed to a hybrid cell that does not exist, and both halves sit inside your analysis set. Object 5510 is a 40 µm axon fragment with 9 output synapses that dead-ends at a missing section; its parent cell is outside the analysis set. The merge outranks the split on every axis that matters: it corrupts identities you will analyze, while the split truncates a cell you will not.

**Step 3 — Fix with the evidence recorded.** Split 8841 at the identified boundary. Log the object ID, the operation, the coordinates, and the evidence in one line: "two somata; caliber 0.8 to 0.2 µm across fold at z=1140; ribosomes present on one side of the boundary only." The products carry 131 and 81 synapses.

**Step 4 — Verify the fix helped, with numbers.** The hybrid object had 47 partners; the split products have 29 and 19, with one partner genuinely shared. Fourteen neuron pairs just lost an edge that never existed. The hybrid was a volume outlier for its putative type; both products now fall inside the normal L2/3 pyramidal size range. That before/after pair is the difference between "I edited" and "I improved the data."

**Step 5 — Decide about 5510 explicitly, not by default.** Twenty minutes remain. Extending 5510 means tracing through a missing-section region — a 30-40 minute job with a real chance of introducing a new merge under time pressure. Log it as deferred, with the reason. A deferral with a recorded reason is a decision; an unexamined flag is just backlog.

**What this example does not establish.** It does not show the subvolume is now clean, and it does not license the claim that merge errors are gone — only that the highest-impact known error was repaired and measured. Remaining error is unmeasured until someone samples for it, which is exactly what the release note in the studio activity must say.

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
{: #studio-activity}

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
- **Minimum pass**
  - Every flagged candidate carries an error-type label (merge/split/boundary/uncertain), and mislabels affect fewer than 3 of the 25 candidates.
  - At least one correction is executed with the supporting evidence stated in the log before the edit, not reconstructed afterward.
  - The correction log records object ID, operation, location, and the specific visual evidence — a reader could re-find the site from the log alone.
  - Before/after quality indicators are computed for at least one correction, with the direction of change stated.
- **Strong performance**
  - The priority ranking ties each candidate to its expected effect on the downstream connectivity graph, and merges outrank splits of comparable size with the reason stated.
  - Before/after metrics are reported for the whole subvolume, and any metric that moved the wrong way is explained rather than omitted.
  - At least one flagged candidate is explicitly deferred with a recorded reason (cost to fix, ambiguity, outside analysis set) rather than silently skipped.
  - The release note states what remains unexamined and what error types are still expected, not only what was fixed.
- **Common failure to flag**
  - Correction without evidence of quality change — fixing things without checking whether it helped.
  - Ranking by visual conspicuousness rather than by impact on the analysis.
  - A merge introduced while fixing a split, because continuity was assumed from appearance instead of verified across sections.

## Common errors and how to recover

- **You corrected ten errors and cannot say whether the data improved.** Recover by recomputing the same local indicators you would have used beforehand — partner counts, segment size distribution, edge changes — and attaching the before/after pair to each logged correction. If you no longer know the before state, sample five of your corrections and re-derive it from the edit history.
- **You spent the session on the most visible errors.** Visibility and impact are different rankings: a dramatic-looking split on a fragment outside your analysis set is worth less than a subtle merge inside it. Recover by re-sorting the remaining queue by expected effect on the connectivity graph and recording the rank rationale before the next session.
- **You merged two fragments that turned out to be different neurons.** This is the expensive direction — you converted a visible, bounded error into an invisible, unbounded one. Recover by reverting the edit, then adopting the rule that a merge requires positive evidence of continuity across sections (matching caliber, trajectory, and ultrastructure), not merely absence of a visible boundary.
- **Your aggregate metric improved but the segmentation got worse for your question.** A single summary number can improve while merge errors increase, because splits usually dominate the total. Recover by reporting split-type and merge-type disagreement separately, and by re-checking a fixed set of analysis-relevant neurons rather than trusting the aggregate; the formulas are in [Metrics and QA]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}).
- **Two annotators disagree about whether a candidate is an error at all.** Do not resolve it by seniority or by coin flip. Recover by writing down each reader's evidence, checking the site against the ultrastructure cues (a process with ribosomes is not an axon), and if it stays ambiguous, logging it as uncertain and excluding the affected object from analyses that depend on the call.

## What this module does not cover

- **The mathematics of quality metrics.** VI, ERL, and edge precision/recall — including what each is blind to — are worked in detail in [Metrics and QA]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}) and [Technical Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}).
- **Proofreading as a budgeted operation.** Triage weighting, stopping rules, proofreading levels, and effort estimation are [Technical Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}) and [Module 07]({{ '/modules/module07/' | relative_url }}); this module runs one correction cycle, not a campaign.
- **How the segmentation algorithms work.** Affinity prediction, watershed, agglomeration, and flood-filling networks are [Module 14]({{ '/modules/module14/' | relative_url }}); here you only need to know where they structurally fail.
- **The ultrastructure cues behind identity calls.** Organelle evidence for axon-versus-dendrite and neuron-versus-glia decisions is [Technical Unit 05]({{ '/technical-training/05-neuronal-ultrastructure/' | relative_url }}); this module uses those cues but does not teach them.

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
