---
title: "Module 14: Computer Vision for EM"
layout: module
permalink: /modules/module14/
description: "Apply computer vision methods to EM imagery for segmentation support, morphology extraction, and quality diagnostics."
module_number: 14
difficulty: "Advanced"
duration: "4-5 hours"
learning_objectives:
  - "Explain how classical and deep CV methods map to connectomics tasks"
  - "Compare model outputs using biologically meaningful error criteria"
  - "Design a validation plan for CV pipelines in EM data"
  - "Report CV limitations with reproducibility safeguards"
prerequisites: "Modules 1-13, Python ML basics"
merit_stage: "Analysis"
compass_skills:
  - "Computer Vision"
  - "Model Evaluation"
  - "Error Analysis"
ccr_focus:
  - "Skills - Computer Vision"
  - "Character - Responsible Interpretation"

# Normalized metadata
slug: "module14"
short_title: "Computer Vision for EM"
status: "active"
audience:
  - "students"
pipeline_stage: "Analysis"
merit_row_focus: "Analysis"
topics:
  - "computer-vision"
  - "em-imagery"
  - "validation"
summary: "Use CV methods for EM analysis with error-aware validation and reproducibility discipline."
key_questions:
  - "Which CV model class is appropriate for each EM task?"
  - "How should CV error be measured for biological use cases?"
  - "What validation evidence is needed before downstream use?"
slides: []
notebook: []
datasets:
  - "/datasets/workflow"
  - "/datasets/mouseconnects"
personas:
  - "/avatars/gradstudent"
  - "/avatars/researcher"
related_tools:
  - "/tools/connectome-quality/"
  - "/tools/ask-an-expert/"
related_frameworks:
  - "research-incubator-model"
  - "education-models"
prerequisites_list:
  - "Image-processing and matrix basics"
  - "Foundational ML familiarity"
next_modules:
  - "module15"
  - "module16"
references:
  - "Januszewski et al. (2018) for segmentation model context."
  - "Recent MICrONS/FlyWire methods for practical CV constraints."
videos: []
downloads: []
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
---

## Capability target
Design and evaluate a CV pipeline for EM imagery that is fit for a specific connectomics task and explicitly bounded by known failure modes. Concretely: choose an architecture from the shape of the task rather than from the benchmark leaderboard, decompose error into merges and splits instead of reporting one score, convert that decomposition into a downstream cost using a ratio your team has actually measured, and write a release gate that says in advance what result would stop the model from shipping.

## Why this module matters
CV is what makes petascale connectomics possible at all: no group will manually trace 10^15 voxels. That leverage is also the risk. A segmentation model applied to a whole volume writes its errors into every downstream product — meshes, skeletons, the synapse table, the connectivity graph — and most of those errors are never seen by a human.

The asymmetry that governs every decision in this module is between the two error types. A split is conspicuous: a neuron ends abruptly, a proofreader sees it, and the repair is local. A merge is invisible in summary statistics. It manufactures connectivity that does not exist, and because motif counting is combinatorial, a small number of spurious edges biases motif counts superlinearly toward denser motifs. A model that trades a large reduction in splits for a modest increase in merges will look better on almost every aggregate metric and be worse for the science.

## Concept set

### 1) Task-model fit
- **Technical:** detection, instance segmentation, denoising, and classification need different objectives, and in EM they also need different data geometry. Affinity prediction with watershed and agglomeration is modular: the dense network runs once over the volume and agglomeration can be re-run cheaply with a new threshold or a learned merge model. Flood-filling networks produce instance labels directly with fewer post-processing stages, at substantially higher compute per volume and less ability to re-run one stage in isolation. Anisotropic data — 4 x 4 x 40 nm is 10:1 — makes z-context weak and pushes some pipelines toward 2D prediction with explicit cross-section linking.
- **Plain language:** pick the model for the job and for the voxel shape, not by popularity.
- **Misconception guardrail:** one architecture solves all EM tasks equally well.

### 2) Error taxonomy over headline metrics
- **Technical:** report VI decomposed into its split and merge components, ERL, and edge or synapse precision and recall — not a single number. VI is size-sensitive, so a single split through a long axon barely registers while boundary drift across many large segments dominates. ERL answers the tracing question directly: roughly, ERL near 10 µm means errors are dense enough that tracing is impractical, near 100 µm means typical dendritic branches can be traced, and near 1,000 µm means most neurons with arbors under 1 mm are essentially complete. The two metrics disagree in informative ways, and a model can win one while losing the other.
- **Plain language:** understand exactly how a model fails, not only how often.
- **Misconception guardrail:** a higher benchmark score means safer downstream use.

### 3) Validation is a release gate with numbers in it
- **Technical:** a release criterion is a statement that can fail. "ERL at or above 120 µm on the held-out ground-truth subvolume, merge component of VI no worse than the incumbent, and no more than 2 merges per mm of traced path in the artifact-heavy region" is a gate. "The segmentation looks good" is not. Write the gate before you see the candidate model's numbers, because thresholds chosen afterwards are chosen to pass.
- **Plain language:** decide the go/no-go rule before you know the answer.
- **Misconception guardrail:** visual plausibility is sufficient validation.

### 4) Ground truth is small, expensive, and biased
- **Technical:** dense ground truth is produced by hand and therefore exists in small volumes, usually drawn from regions that were easy to annotate — well stained, artifact-free, away from blood vessels and folds. A model evaluated only there will report error rates that do not describe the volume it will be run on. Hold out at least one deliberately hard region: near a fold, near a section loss, near a blood vessel, or in the most weakly stained block. Report the metrics separately for the clean and hard regions rather than pooling them, because pooling hides the number you need.
- **Plain language:** your test set is probably the easy part of the dataset.
- **Misconception guardrail:** the held-out ground truth is representative of the volume.

### 5) Augmentation encodes the artifacts you expect to meet
- **Technical:** training data is scarce because annotation is expensive, so augmentation carries real weight: elastic deformation for tissue warping, intensity and contrast variation for staining differences, simulated missing sections so the network learns to bridge gaps, rotation and flipping, and injected artifacts such as knife chatter or charging. The choice is a prediction about the target volume. If you do not simulate section loss, the model will fail at section loss, and it will fail silently by continuing an object through the gap or terminating it.
- **Plain language:** the model handles the damage you taught it to expect.
- **Misconception guardrail:** more augmentation is always better than less.

## Choosing an approach and choosing a metric

| Approach | Best when | What it costs you |
|---|---|---|
| Affinity CNN + watershed + agglomeration | You want modularity and cheap re-runs of the merge stage | Quality depends heavily on boundary prediction; agglomeration errors need their own model and their own ground truth |
| Flood-filling network | Highest instance quality with fewer post-processing stages | Substantially more compute per volume; harder to re-run one stage; less modular to debug |
| 2D segmentation plus cross-section linking | Strongly anisotropic data where z-context is weak | Linking errors accumulate along z; performs poorly across missing sections |
| Learned agglomeration on existing supervoxels | Supervoxels are good and merging is the bottleneck | Requires before/after proofreading correction pairs, which only exist after a proofreading effort |

| Question you are answering | Metric that answers it | Where it misleads |
|---|---|---|
| How volumetrically accurate is the labeling? | VI, reported as split and merge components separately | Size-sensitive; a single long-axon split is nearly invisible |
| Can a person trace a neurite through this? | ERL | Insensitive to boundary drift; depends on skeleton conventions |
| Is the connectivity right? | Edge and synapse precision and recall | Conflates segmentation error with synapse-detection error unless controlled |
| Are membranes placed correctly? | Boundary F1 | Can be high while the topology is wrong; least informative downstream |

## Worked example: two models, and why the better score loses

The numbers below are illustrative — they show the shape of the reasoning, not results from a specific published comparison.

You are choosing between an incumbent model A and a candidate model B for a production segmentation. Evaluation is on a proofread ground-truth subvolume containing 60 skeletonized neurites totaling about 42 mm of traced path.

| | Model A (incumbent) | Model B (candidate) |
|---|---|---|
| VI (total) | 0.61 | 0.52 |
| VI split component | 0.44 | 0.19 |
| VI merge component | 0.17 | 0.33 |
| ERL | 142 µm | 118 µm |
| Boundary F1 | 0.89 | 0.93 |
| Splits in the subvolume | 210 | 95 |
| Merges in the subvolume | 24 | 47 |

**The naive reading.** B wins on total VI and on boundary F1, which is the pair of numbers most benchmark tables would show. Ship B.

**What the decomposition says.** B's entire VI advantage comes from splits: 0.44 down to 0.19. Its merge component nearly doubled, 0.17 to 0.33, and its merge count rose from 24 to 47. B is a model that is more willing to join things.

**What ERL says.** A gives 142 µm of expected error-free tracing against B's 118 µm. So on the practical question — can someone follow a dendrite — A is better, and it is better because ERL is broken by both error types while VI is dominated by voxel volume.

**Converting to a decision.** Define *r* as the cost of one merge relative to one split, counting the time to find it as well as to fix it. Then A costs 210 + 24*r* split-equivalents and B costs 95 + 47*r*. Setting these equal: 115 = 23*r*, so *r* = 5. At *r* = 5 the two models are exactly tied. At *r* = 2, B is better (189 against 258). At *r* = 8, A is better (402 against 471). The entire decision rests on one ratio, and most teams have never measured it.

**Naming the assumption.** This arithmetic assumes every merge is eventually found. It is the optimistic case. Merges are invisible in summary statistics and a proofreader is not prompted to look for them, so in practice some fraction survives into the released connectome and manufactures edges. That pushes the effective *r* upward, which favors A. It also means the honest report includes an estimate of the *undetected* merge rate, which cannot be obtained from the same ground truth that trained the comparison.

**The decision and the gate.** Measure *r* on your own team by timing 20 real repairs of each type, including search time. If the measured *r* exceeds 5, keep A. If it is below 5, adopt B but add a merge-focused review pass, and set the release gate to require that B's merge component not exceed A's after that pass. Record both models' numbers in the model card either way, because the next team's *r* will be different.

## Core workflow
1. Write the EM task as a sentence naming the input, the output, and the downstream consumer of that output.
2. Define the acceptable error envelope in decomposed terms: maximum merge rate, minimum ERL, and the region in which those numbers must hold.
3. Select a baseline and at most two candidate approaches, using the approach table and the voxel geometry of your data.
4. Assemble evaluation data that includes at least one deliberately hard region, and keep clean-region and hard-region metrics separate.
5. Evaluate with VI decomposed, ERL, and a connectivity-level metric; never report a single aggregate score alone.
6. Convert the error counts into downstream cost using a merge-to-split ratio your team measured rather than assumed.
7. Review 20-30 failure cases by eye in ambiguous regions and classify each by cause: weak stain, section loss, fold, thin neurite, or genuine ambiguity.
8. Publish a model card with intended use, unsupported uses, the evaluation regions, the metrics with their region breakdown, and the release gate the model passed.

## Pre-class preparation
- Read [metrics and QA]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}) for VI and ERL, and [artifact taxonomy]({{ '/content-library/imaging/artifact-taxonomy/' | relative_url }}) for what the model must survive.
- Bring or download one EM subvolume with visible artifacts.
- Be ready to state which downstream product your segmentation would feed.

## 60-minute tutorial run-of-show
1. **00:00-08:00** task framing + exemplar failure modes. Show one split and one merge in the viewer and ask which is worse; collect reasons before giving the answer.
2. **08:00-20:00** choose metrics tied to downstream biology. Each learner writes the metric they would gate on and the threshold, before seeing any model output.
3. **20:00-34:00** evaluate baseline vs candidate model. Learners compute or are given VI components, ERL, and error counts for two models, then solve for the break-even merge-to-split ratio.
4. **34:00-46:00** error taxonomy and triage discussion. Sample failure cases, classify each by cause, and identify which causes augmentation could have addressed.
5. **46:00-56:00** model card drafting, including at least one unsupported use and the region breakdown of the metrics.
6. **56:00-60:00** competency check: each learner states their release gate as a sentence that could fail.

## Studio activity
{: #studio-activity}
**Scenario:** Compare two segmentation-support CV models for an EM subvolume. You are given the model outputs, a proofread ground-truth subvolume of roughly 40 mm of traced path drawn from a clean region, and a second, smaller ground-truth patch from a region containing a partial fold and two lost sections. Your team maintains the production segmentation and must recommend one model.

**Tasks**
1. Compute or tabulate VI with its split and merge components, ERL, and error counts for both models, reported separately for the clean and the artifact-heavy region.
2. Solve for the merge-to-split cost ratio at which the two models tie, and state which side of that ratio your team is on and how you know.
3. Sample at least 15 failure cases across both models and classify each by cause.
4. Write a release gate: a numeric criterion, decided before looking at the winner, that the chosen model must pass.
5. Draft the model card limitation statement, including one use you would refuse to support.

**Outputs**
- metric table with biological interpretation, split by region,
- failure-case log with causes tallied,
- break-even ratio calculation with the assumption behind it named,
- model-card limitation statement.

## Assessment rubric
- **Minimum pass:** clear task-model rationale, biologically relevant metrics reported with merge and split separated, explicit limitations naming at least one unsupported use.
- **Strong performance:** robust failure analysis by cause, a release gate written before the result was known, and a downstream cost argument that names the merge-to-split ratio as a measured quantity rather than an assumption.
- **Failure modes:** metric-only reasoning, pooling clean and artifact-heavy regions into one number, weak split design, no deployment boundaries, thresholds chosen after seeing which model they would favor.

## Key architectures for EM connectomics

### U-Net (Ronneberger et al. 2015)
Encoder-decoder architecture with skip connections. The encoder downsamples the image to extract features; the decoder upsamples to produce pixel-level predictions; skip connections preserve fine-grained spatial detail. Originally designed for biomedical image segmentation. In connectomics, 3D U-Nets predict boundary/affinity maps at each voxel.

**Why it works for EM:** EM images have consistent texture and contrast patterns. The encoder learns to detect membranes, vesicles, and other structures; the decoder produces a per-voxel prediction map.

**Practical constraint:** the network is applied blockwise over petavoxels, and blocks must overlap, because a network needs context beyond the region it predicts. Insufficient overlap produces block-boundary seams that appear later as a regular grid of segmentation errors — diagnosable because their spatial distribution matches your block grid.

### Flood-Filling Networks (Januszewski et al. 2018)
An iterative approach: a CNN predicts whether each neighboring voxel belongs to the same object as the current seed, and the segment "grows" outward. FFNs produce instance segmentation directly (each neuron gets a unique ID) without the separate watershed + agglomeration step.

**When to use:** FFNs are computationally expensive but produce high-quality segmentation with fewer post-processing stages. Used in FlyWire and other Google-based reconstructions.

### Affinity prediction + watershed + agglomeration
The standard two-stage pipeline: (1) A 3D CNN predicts pairwise affinity between neighboring voxels (probability they belong to the same segment). (2) Watershed transform produces an over-segmentation of millions of supervoxels. (3) Agglomeration merges supervoxels based on affinity scores at boundaries.

**When to use:** More modular and parallelizable than FFN. Standard in academic pipelines (Funke et al. 2019).

**Why the watershed threshold is set to over-segment:** supervoxels are the immutable atoms every later stage is built on, so a supervoxel that spans two neurites is an error no amount of downstream proofreading can repair cleanly. The pipeline deliberately accepts many splits to avoid that.

### Data augmentation for EM
Training data is expensive (manual annotation). Augmentation expands the effective training set:
- **Elastic deformations**: simulate tissue warping
- **Intensity variations**: simulate staining differences
- **Missing section simulation**: randomly drop sections during training so the model learns to handle gaps
- **Rotation/flipping**: standard geometric augmentations
- **Artifact injection**: add synthetic knife chatter or charging patterns

## Common errors and how to recover

- **The candidate model wins on total VI and you are about to ship it.** Recover by decomposing VI before making the decision. If the merge component rose, compute the break-even merge-to-split ratio and compare it to a ratio your team has measured. Ship only if the measurement, not the intuition, supports it.
- **Segmentation errors form a regular grid across the volume.** This is block-boundary seaming from insufficient inference overlap. Recover by increasing block overlap and blending predictions in the overlap region, then re-running the affected blocks; the grid pattern in the error map is how you confirm the fix worked.
- **Metrics are excellent and proofreaders say the segmentation is bad.** Your ground truth is from the easy part of the volume. Recover by annotating a small hard-region patch — near a fold, a section loss, or the weakest stain — and reporting the metrics separately. Expect the hard-region numbers to be much worse; that gap is the finding.
- **The model terminates or wildly extends objects at missing sections.** Recover by adding missing-section simulation to augmentation and retraining, and in the interim by flagging all sections adjacent to a known loss so downstream consumers can exclude them rather than silently trust them.
- **ERL improved but the connectome got worse.** Check whether the ERL gain came from merges joining separate neurites into long false runs. Recover by recomputing ERL with merge-induced runs excluded, or by reporting merge-ERL and split-ERL separately.
- **You cannot reproduce last quarter's evaluation.** Recover by pinning three things explicitly: the model weights hash, the ground-truth version, and the segmentation version the ground truth was aligned against. Any of the three changing will move the numbers.
- **A downstream group used your model outside its evaluated domain.** Recover by publishing the model card next to the weights rather than in a paper appendix, naming the evaluated domain and the unsupported uses, and adding a domain check that refuses to run on data whose intensity statistics fall far outside the training distribution.

## What this module does not cover

- **Proofreading practice and triage.** How humans find and fix these errors, and how to prioritize by endpoint impact, is [Module 07]({{ '/modules/module07/' | relative_url }}), [Technical Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}), and [proofreading strategies]({{ '/content-library/proofreading/proofreading-strategies/' | relative_url }}).
- **The imaging that produces the artifacts.** Staining, sectioning, dose, and the artifact taxonomy are [Technical Unit 03]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}) and [artifact taxonomy]({{ '/content-library/imaging/artifact-taxonomy/' | relative_url }}).
- **General ML validity — leakage, splits, and base rates.** That is [Module 13]({{ '/modules/module13/' | relative_url }}), and it applies here too.
- **Infrastructure for running inference at petascale.** Chunking, sharding, and cost are [Module 12]({{ '/modules/module12/' | relative_url }}) and [Technical Unit 04]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}).
- **Training-loop engineering.** Loss functions, schedules, mixed precision, and distributed training are assumed background rather than taught here.
- **Synapse detection as a modeling problem in its own right.** It is treated here only as a consumer of segmentation quality; see [Module 11]({{ '/modules/module11/' | relative_url }}) and [synapse classification]({{ '/content-library/neuroanatomy/synapse-classification/' | relative_url }}).

## Content library references
- [Reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }}) — End-to-end segmentation architecture
- [Metrics and QA]({{ '/content-library/proofreading/metrics-and-qa/' | relative_url }}) — VI, ERL, boundary F1 for evaluation
- [Artifact taxonomy]({{ '/content-library/imaging/artifact-taxonomy/' | relative_url }}) — What CV models must handle
- [Error taxonomy]({{ '/content-library/proofreading/error-taxonomy/' | relative_url }}) — Merge/split/boundary errors from CV
- [Journal papers: computer vision and ML]({{ '/content-library/journal-papers/computer-vision-ml/' | relative_url }}) — Primary literature

## Teaching resources
- [Technical Unit 08: Segmentation and Proofreading]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
- [Technical Unit 09: Connectome Analysis and NeuroAI]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})
- [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})

## References
- Ronneberger O et al. (2015) "U-Net: Convolutional Networks for Biomedical Image Segmentation." *MICCAI* 2015.
- Januszewski M et al. (2018) "High-precision automated reconstruction of neurons with flood-filling networks." *Nature Methods* 15(8):605-610.
- Funke J et al. (2019) "Large scale image segmentation with structured loss." *IEEE TPAMI* 41(7):1669-1680.
- Lee K et al. (2019) "Superhuman accuracy on the SNEMI3D connectomics challenge." *arXiv:1706.00120*.

## Quick practice prompt
Document one CV result with one supported use case and one forbidden use case.
