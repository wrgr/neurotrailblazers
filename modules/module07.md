---
title: "Module 07: Proofreading and Quality Control"
layout: module
permalink: /modules/module07/
description: "Develop proofreading strategies that prioritize high-impact corrections and maintain reproducible QC standards."
module_number: 7
difficulty: "Intermediate"
duration: "4 hours"
learning_objectives:
  - "Prioritize proofreading tasks by scientific impact"
  - "Apply consistent adjudication rules"
  - "Use quality metrics to support release decisions"
  - "Document uncertainty and unresolved issues"
prerequisites: "Modules 01-06"
merit_stage: "Question"
compass_skills:
  - "Proofreading"
  - "QC Decision-Making"
  - "Documentation"
ccr_focus:
  - "Skills - Quality Control"
  - "Character - Rigor"

# Normalized metadata
slug: "module07"
short_title: "Proofreading and Quality Control"
status: "active"
audience:
  - "students"
pipeline_stage: "Question"
merit_row_focus: "Question"
topics:
  - "proofreading"
  - "qc"
  - "triage"
summary: "Impact-weighted proofreading with reproducible quality-control decisions."
key_questions:
  - "Which errors most affect biological conclusions?"
  - "What thresholds justify release versus rework?"
slides:
  - "/assets/slides/module07/module07-proofreading-and-quality-control.pdf"
notebook:
  - "/assets/notebooks/module07/module07-proofreading-and-quality-control.ipynb"
datasets:
  - "/datasets/workflow"
personas:
  - "/avatars/gradstudent"
  - "/avatars/researcher"
related_tools:
  - "/tools/connectome-quality/"
related_frameworks:
  - "research-incubator-model"
prerequisites_list: []
next_modules:
  - "module08"
references: []
videos: []
downloads: []
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
---

## Capability target
Execute a proofreading triage cycle that ranks corrections by impact and issues a transparent QC decision.

## Hidden curriculum scaffold
- Norms often unstated: prioritize by scientific consequence, not visual annoyance. A merge error that creates a false connection between two neurons in your circuit of interest is more important than a split error in a fragment at the edge of the volume.
- Require explicit rationale for deferred corrections: "I chose not to fix this because..." is more valuable than silently ignoring it.
- Proofreading is collaborative: in projects like FlyWire, 287 people contributed corrections. The quality of the final product depends on consistent standards across annotators.
- Release decisions are scientific judgments: "Is this segmentation good enough for the analysis we want to do?" is a question about fitness-for-purpose, not perfection.
- Error fatigue is real: after hours of proofreading, annotators start missing errors or making new ones. Build in breaks and use inter-annotator agreement checks as a safeguard.
- The best proofreading policy is one that is written down before proofreading begins, reviewed by the team, and followed consistently.

## Concept set

### 1) Impact-weighted triage
Not all errors are worth fixing. A merge error on a large interneuron with 500 synapses is far more impactful than a split error on a tiny axon fragment with 2 synapses. Impact factors include: (a) size of the affected segment (larger = more connections affected), (b) position in the analysis region of interest, (c) error type (merges corrupt the graph more directly than splits), (d) confidence of the error detection (is it definitely wrong or ambiguous?).

A practical triage matrix assigns each error a composite score. For example, a merge error on a neuron within the analysis region that has high synapse count and clear evidence of incorrectness scores 4/4 and goes to the top of the queue. A possible boundary error on a small fragment outside the region of interest scores 1/4 and can be deferred or ignored entirely. The key insight is that proofreading time is a limited resource, and spending it on low-impact corrections means higher-impact errors persist in the final dataset. Teams should establish their triage criteria before beginning a proofreading campaign, not invent them ad hoc as errors appear.

### 2) Proofreading strategies
Each strategy trades off thoroughness against scalability. The choice depends on the scientific question, available labor, and volume size.

- **Exhaustive local**: Fix every error in a defined subvolume. Used to create gold-standard reference regions. Cost: 10-100x the time of automated segmentation. Best for: validation regions where you need ground truth to benchmark automated methods.
- **Targeted/skeleton-guided**: Follow specific neurons of interest and fix errors along their path. Most common for circuit-focused questions. You trace each neuron from soma to axon terminals, correcting merges and splits as you encounter them. This produces high-quality reconstructions for specific cells but leaves the rest of the volume uncorrected.
- **Priority-ranked**: Use automated error detection to rank candidates by impact. Fix top-N. Most efficient for large volumes where exhaustive proofreading is infeasible. Automated detectors flag likely merge and split sites, and human proofreaders work through the list in priority order.
- **Crowd-sourced**: The FlyWire model -- 287 proofreaders with consensus mechanisms. Scales to whole-brain but requires social infrastructure: training materials, inter-annotator agreement checks, conflict resolution protocols, and community management.

In practice, most projects combine strategies. A team might use priority-ranked proofreading across the full volume, then switch to exhaustive local correction within specific subregions that are central to their analysis. The important thing is to document which strategy was applied where, so downstream users know the expected quality level in different parts of the dataset.

### 3) Quality metrics for release decisions
No single metric captures all aspects of segmentation quality. Use multiple metrics and understand what each one measures.

- **Variation of Information (VI)**: Information-theoretic measure of segmentation quality. Split into merge-VI and split-VI components. Merge-VI captures how much information is lost by incorrectly combining segments; split-VI captures information lost by incorrectly separating them. Lower is better for both. Requires ground-truth labels for computation, which limits its use to regions where manual annotation exists.
- **Expected Run Length (ERL)**: Average distance along a neurite before encountering an error. More biologically interpretable: "you can trace X um before hitting a mistake." ERL of 100 um means you can follow a typical dendrite through several branch points before the reconstruction goes wrong. This metric weights errors by the length of neurite they affect, so errors on long neurites count more than errors on short fragments.
- **Synapse-centric F1**: Precision and recall of synaptic connections. The metric most directly relevant to connectome accuracy. A false positive connection (due to a merge) or a missed connection (due to a split at a synaptic site) directly corrupts the connectivity graph that downstream analyses depend on. This metric requires both segmentation and synapse detection to be evaluated together.
- **Release threshold**: Define in advance -- "we will release this region when ERL > 50 um and synapse F1 > 0.85." Transparent thresholds prevent both premature release and infinite proofreading. The threshold should be calibrated to the sensitivity of the planned analysis: a study counting total synapse number tolerates more error than one analyzing specific motifs.

When metrics disagree -- for example, ERL is above threshold but synapse F1 is below -- the resolution depends on the scientific question. If the analysis is primarily topological (which neurons connect?), synapse F1 dominates. If the analysis is morphological (what do neurons look like?), ERL matters more. This is why release decisions are scientific judgments, not mechanical threshold checks.

### 4) Documentation and reproducibility
Every correction should be logged: what was changed, why, when, and by whom. CAVE's materialization system (see content library) provides this automatically -- each edit is a versioned operation, and materialization snapshots freeze the state for reproducible analysis.

Without versioned documentation, two researchers analyzing the "same" dataset at different times may get different results because proofreading edits changed the segmentation between their queries. Materialization versions solve this: you pin your analysis to a specific version number, and anyone can reproduce your results by querying that same version. This is the connectomics equivalent of specifying which genome assembly build you used for a genomics analysis.

Good correction logs also serve a pedagogical function. When new proofreaders join a project, they can review past correction decisions to learn the team's standards. Entries like "Merged fragments 847291 and 847305 because continuous membrane visible in z-slices 4021-4035; confirmed by checking orthogonal views" teach both the decision criteria and the verification process.

## Core workflow
1. **Classify** errors by type (merge/split/boundary) and estimated impact (high/medium/low). Use the error taxonomy from the content library as a reference checklist.
2. **Prioritize** correction queue: high-impact merges first, then splits in the region of interest, then boundary errors. Defer or discard low-impact errors outside the analysis region.
3. **Apply** corrections using Neuroglancer/CAVE split and merge operations. For each correction, note the supervoxel IDs involved and the evidence that motivated the edit.
4. **Verify** each correction: check that the fix didn't introduce new errors. Splitting a merge sometimes creates an orphan fragment that needs re-merging elsewhere. Merging a split sometimes absorbs a nearby fragment that shouldn't be included. Always inspect the result in at least two orthogonal views.
5. **Record** QC decision: compute metrics, compare to release thresholds, issue go/rework recommendation. If the recommendation is "rework," specify which error categories need further attention and estimate the additional effort required.

## 60-minute tutorial run-of-show

### Pre-class preparation (10 min async)
- Read the proofreading strategies content library entry
- Review the worked examples content library entry (at least Scenario 1 and 4)

### Minute-by-minute plan
1. **00:00-10:00 | Triage philosophy**
   - Open with: "You have 100 errors flagged in your volume and time to fix 20. Which 20 do you choose?"
   - Discuss: visual salience does not equal scientific importance. The ugliest error (a weird tentacle from a merge) may be less important than a subtle split in a key neuron.
   - Introduce impact-weighting framework.
   - Show a concrete example: two errors side by side, one visually dramatic but low-impact, one subtle but high-impact. Ask learners which they would fix first and why.

2. **10:00-24:00 | Queue classification exercise**
   - Present 12 pre-identified errors with brief descriptions. Learners work in pairs to:
     - Classify each by type (merge/split/boundary)
     - Estimate impact (high/medium/low) based on segment size and analysis relevance
     - Rank the top 5 for correction
   - Debrief: compare rankings across pairs. Where do teams disagree? Disagreements often reveal implicit assumptions about what matters.

3. **24:00-38:00 | Correction sprint**
   - Learners fix their top 5 errors in the practice dataset.
   - Instructor circulates: "Show me why you think this is a merge error." "What evidence did you check before splitting?"
   - Emphasis on verification after each correction.
   - Common pitfall to watch for: learners who split a merge but forget to re-merge the orphaned fragment with the correct parent segment.

4. **38:00-50:00 | Threshold-based release decisions**
   - Compute metrics before and after the correction sprint.
   - Introduce release thresholds: "If ERL > 30 um and synapse F1 > 0.80, we release. If not, more proofreading."
   - Group discussion: are we above threshold? If not, what would we fix next?
   - Key teaching moment: the threshold should be set before proofreading begins, not adjusted after seeing the results. Moving the goalposts undermines the purpose of having thresholds.

5. **50:00-60:00 | Competency check**
   - Each learner writes a 4-sentence "release recommendation memo":
     - Current quality metrics
     - What was fixed
     - What remains unfixed and why
     - Go/no-go recommendation
   - Exit ticket: "One rule for when an error MUST be fixed before release."

## Studio activity: release decision simulation (60-75 minutes)

**Scenario:** You are the QC lead for a 100x100x100 um subvolume that will be used in a paper analyzing reciprocal connectivity between L2/3 pyramidal cells. The segmentation has been through one round of automated error detection. You need to decide: is this subvolume ready for analysis?

**Task sequence:**
1. Review the automated error report: 45 flagged errors (18 merges, 20 splits, 7 uncertain).
2. Triage: classify each by impact on the reciprocal connectivity analysis. Which errors could create false reciprocal connections? Which could hide real ones?
3. Fix the top 15 errors, documenting each correction with a one-line rationale.
4. Compute before/after metrics (provided metric computation script).
5. Write a 1-page release recommendation memo with: metrics summary, corrections summary, remaining risks, and go/no-go recommendation with explicit reasoning.

**Guidance for triage step:** A merge error between two L2/3 pyramidal cells that are both pre- and post-synaptic to each other could create a spurious reciprocal connection or mask a real one -- this is maximally damaging for the planned analysis. A split error on a glial process has zero impact on the reciprocal connectivity question. Errors on inhibitory interneurons fall in between: they don't directly affect pyramidal-to-pyramidal reciprocal connections but could corrupt the broader circuit context. Learners should articulate this kind of reasoning for each error in their triage table.

**Time management:** Learners often spend too long on the triage step and run out of time for the correction sprint. Suggest a time budget: 20 minutes for triage, 30 minutes for corrections, 15 minutes for metrics and memo writing. The memo is the most important deliverable -- a rushed memo undermines the entire exercise.

**Expected outputs:**
- Triage table with impact ratings and one-line justifications.
- Correction log with before/after segment IDs and rationale for each fix.
- Metrics comparison table (pre- and post-proofreading).
- Release recommendation memo with explicit go/no-go decision.

## Assessment rubric
- **Minimum pass**: Consistent queueing by type and impact. Release decision justified by metrics. Correction log present.
- **Strong performance**: Impact reasoning explicitly tied to the scientific question (reciprocal connectivity). Uncertainty handling is transparent -- learner acknowledges what they could not determine and explains how that uncertainty affects the release decision. Memo is clear and actionable.
- **Common failure to flag**: Ad hoc corrections without policy -- fixing whatever looks wrong rather than systematically prioritizing by impact. Another common failure is issuing a release recommendation without referencing specific metric values.

## Content library references
- [Error taxonomy]({{ '/content-library/proofreading/error-taxonomy/' | relative_url }}) -- Merge, split, boundary, identity error details
- [Proofreading strategies]({{ '/content-library/proofreading/proofreading-strategies/' | relative_url }}) -- Exhaustive, targeted, priority, crowd-sourced
- [Proofreading tools]({{ '/content-library/proofreading/proofreading-tools/' | relative_url }}) -- CAVE, Neuroglancer, editing operations
- [Metrics and QA]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}) -- VI, ERL, synapse F1 with formulas
- [Proofreading worked examples]({{ '/content-library/proofreading/worked-examples/' | relative_url }}) -- Step-by-step correction scenarios
- [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}) -- CAVE materialization for reproducible QC
- [FlyWire whole-brain]({{ '/content-library/case-studies/flywire-whole-brain/' | relative_url }}) -- Collaborative proofreading at scale

## Teaching resources
- [Technical Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}) -- Covers segmentation algorithms and proofreading tool mechanics in depth
- [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }}) -- Interactive metric computation and threshold visualization

## References
- Dorkenwald S et al. (2022) "CAVE: Connectome Annotation Versioning Engine." *bioRxiv*.
- Dorkenwald S et al. (2024) "Neuronal wiring diagram of an adult brain." *Nature* 634:124-138.
- Funke J et al. (2017) "A benchmark for evaluation of large-scale reconstruction methods." *Frontiers in Computational Neuroscience*.
- Meila M (2007) "Comparing clusterings -- an information based distance." *Journal of Multivariate Analysis* 98(5):873-895.
- Plaza SM et al. (2014) "Annotating synapses in large EM datasets." *arXiv:1409.1801*.

## Quick practice prompt
Write one rule for when an error must be fixed before release. Your rule should specify: (1) the type of error, (2) the condition under which it is mandatory to fix, and (3) why that condition matters for downstream analysis. Example format: "A [type] error must be fixed before release when [condition], because [scientific reasoning]."
