---
marp: true
theme: neurotrailblazers
paginate: true
footer: "Module 06 · NeuroTrailblazers"
title: "Module 06: Segmentation 101"
---

<!-- _class: title nanoscale -->
<img class="cover-image" src="../../../../assets/images/content-library/case-studies/h01/10b-segmentation-overlay.jpg" alt="H01 electron microscopy with object segmentation and original 2 µm scale bar">
<span class="eyebrow">NeuroTrailblazers · Module 06</span>

# Segmentation 101
Teaching Deck

<p class="cover-label">Human cortex · H01<br>Object segmentation over electron microscopy</p>
<p class="source">H01 release · Lichtman Lab / Harvard &amp; Connectomics at Google · CC BY 4.0<br>Shapson-Coe et al. (2024) · doi:10.1126/science.adk4858</p>

---

## Learning Objectives
- Explain segmentation goals and constraints
- Identify merges, splits, and boundary errors
- Apply a basic correction workflow
- Report segmentation quality with clear metrics

---

## Session Outcomes
- Learners can complete the module capability target.
- Learners can produce one evidence-backed artifact.
- Learners can state one limitation or uncertainty.

---

## Capability Target
Detect and categorize core segmentation errors and execute one correction cycle with documented quality impact.

---

## Concept Focus
### 1) What segmentation does and why it matters
Segmentation is the computational process of assigning every voxel in an EM volume to a specific object — not just "this is a neuron" but "this is neuron #47,293." This is instance segmentation, and it's the foundation of the entire connectome. Without accurate segmentation, you cannot identify individual neurons, trace their morphology, or determine their synaptic connections. Modern methods (flood-filling networks, U-Net + watershed + agglomeration) achieve "superhuman" accuracy on benchmarks but still make errors at rates that compound across large volumes.

---

## Core Workflow
- Load segmented patch in Neuroglancer or equivalent viewer.
- Identify merge/split candidates by scrolling through z and checking 3D meshes for implausible morphology.
- Apply correction: split merged segments at the boundary, merge split fragments by verifying continuity.
- Recalculate quality indicators: did the correction improve local metrics?
- Log decisions: record what was changed, why, and what evidence supported the decision.

---

## Run of Show (60 min)
- 00:00-08:00 | Segmentation goals
- 08:00-22:00 | Error taxonomy with real examples
- 22:00-36:00 | Guided correction round
- 36:00-48:00 | Quality metric interpretation
- 48:00-60:00 | Debrief and competency check

<!--
Pre-class preparation (10 min async)
  Read the error taxonomy content library entry
  Open a public segmented volume in Neuroglancer ([MICrONS Explorer](https://www.microns-explorer.org/)) and browse the segmentation for 5 minutes
  Minute-by-minute plan

00:00-08:00 | Segmentation goals
  "What would a perfect segmentation look like? Every neuron correctly labeled, every membrane correctly placed."
  Show a well-segmented region side-by-side with raw EM (the H01 pair in Step 6 of [H01, Step by Step](/content-library/case-studies/h01-pipeline/) works). Point out: each color = one neuron.
  Then show the same region with errors highlighted. "This is reality. Our job is to find and fix these."

08:00-22:00 | Error taxonomy with real examples
  Source the merge and split from Scenarios 1 and 2 of the [proofreading worked examples](/content-library/proofreading/worked-examples/), and the boundary error from a `synapse near boundary` row in the [Module 06 kit](/assets/kits/module06/README.md).
  Walk through one merge error: show the 3D mesh with impossible branching, navigate to the merge point in 2D slices, explain why the model failed (low contrast at a blood vessel).
  Walk through one split error: show a dead-end axon fragment, then the continuation 3 sections later. Explain: thin process + poor contrast = model lost it.
  Walk through one boundary error: show a synapse attributed to the wrong neuron because the membrane position is off by 2 pixels.
  For each: "What would this error do to your analysis?"

22:00-36:00 | Guided correction round
  Learners work in pairs on 3 errors chosen from the [Module 06 kit](/assets/kits/module06/README.md) (1 merge, 1 split, 1 ambiguous).
  Instructor circulates, coaching on: "Show me the evidence before you correct." "What would happen if this merge is actually correct — two branches of the same neuron?"

36:00-48:00 | Quality metric interpretation
  Introduce: "How do we know if our corrections actually helped?"
  Brief overview of metrics: edge precision/recall (are the connections right?), segment size distributions (do sizes look biological after correction?).
  Compute metrics before and after the correction round with the kit's `qc_metrics.py`. Did they improve?

48:00-60:00 | Debrief and competency check
  Each learner presents one correction with evidence chain.
  Group discussion: "Which correction had the biggest impact on the graph? Why?"
  Exit ticket: "Name the error type you found hardest to detect and why."
-->

---

## Misconceptions to Watch
- **Misconception guardrail:** merge and split errors are equally costly, so error counts alone rank corrections.
- **Misconception guardrail:** an object that looks like a plausible neuron is evidence that the segmentation is correct.
- **Misconception guardrail:** the most visually obvious errors are the ones most worth fixing.
- **Misconception guardrail:** a segmentation can be finished, rather than released at a stated level with stated remaining error.

---

## Studio Activity
**Scenario:** Your team has a freshly segmented 50x50x50 um subvolume containing approximately 200 neuron fragments. Automated error detection has flagged 25 candidate errors, listed in the [Module 06 kit](/assets/kits/module06/README.md) (synthetic). You have time to fix 10.

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
**Minimum pass**

- Every flagged candidate carries an error-type label (merge/split/boundary/uncertain), and mislabels affect fewer than 3 of the 25 candidates.
- At least one correction is executed with the supporting evidence stated in the log before the edit, not reconstructed afterward.
- The correction log records object ID, operation, location, and the specific visual evidence — a reader could re-find the site from the log alone.
- Before/after quality indicators are computed for at least one correction, with the direction of change stated.

---

## Assessment Rubric
**Strong performance**

- The priority ranking ties each candidate to its expected effect on the downstream connectivity graph, and merges outrank splits of comparable size with the reason stated.
- Before/after metrics are reported for the whole subvolume, and any metric that moved the wrong way is explained rather than omitted.
- At least one flagged candidate is explicitly deferred with a recorded reason (cost to fix, ambiguity, outside analysis set) rather than silently skipped.
- The release note states what remains unexamined and what error types are still expected, not only what was fixed.

---

## Assessment Rubric
**Common failure to flag**

- Correction without evidence of quality change — fixing things without checking whether it helped.
- Ranking by visual conspicuousness rather than by impact on the analysis.
- A merge introduced while fixing a split, because continuity was assumed from appearance instead of verified across sections.

---

## Exit Ticket
Explain when you would defer a correction instead of fixing immediately.

---

## References (Instructor)
- Use module references listed on the module page.

---

## Teaching Materials
- Module page: /modules/module06/
- Session kit: /teaching/sessions/module06/
- Worksheet: /assets/worksheets/module06/module06-activity.md
