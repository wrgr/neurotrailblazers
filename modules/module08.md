---
title: "Module 08: Hypothesis Testing in Connectomics"
layout: module
permalink: /modules/module08/
description: "Design and evaluate connectomics hypotheses using measurable outcomes, statistical logic, and explicit limitations."
module_number: 8
difficulty: "Intermediate"
duration: "4 hours"
learning_objectives:
  - "Translate biological questions into testable hypotheses"
  - "Select metrics and null models for structural data"
  - "Interpret outcomes with uncertainty discipline"
  - "Separate supported claims from exploratory signals"
prerequisites: "Modules 01-07"
merit_stage: "Experiment"
compass_skills:
  - "Hypothesis Design"
  - "Statistical Reasoning"
  - "Critical Interpretation"
ccr_focus:
  - "Skills - Hypothesis Testing"
  - "Character - Epistemic Discipline"

# Normalized metadata
slug: "module08"
short_title: "Hypothesis Testing in Connectomics"
status: "active"
audience:
  - "students"
pipeline_stage: "Experiment"
merit_row_focus: "Experiment"
topics:
  - "hypothesis-testing"
  - "null-models"
summary: "Build testable connectomics hypotheses with measurable outputs and robust interpretation boundaries."
key_questions:
  - "What makes a connectomics hypothesis testable?"
  - "Which null model supports this claim?"
slides: []
notebook: []
datasets:
  - "/datasets/workflow"
personas:
  - "/avatars/gradstudent"
related_tools:
  - "/tools/connectome-quality/"
related_frameworks:
  - "research-incubator-model"
prerequisites_list: []
next_modules:
  - "module09"
  - "module10"
references: []
videos: []
downloads: []
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
---

## Capability target
Design one hypothesis test with metric, null model, and interpretation boundary statement.

## Concept set

### 1) What makes a connectomics hypothesis testable?
A testable connectomics hypothesis must specify: (a) a structural feature that can be measured from the reconstructed data (e.g., synapse count, motif frequency, path length), (b) a comparison or null expectation (e.g., "more frequent than in a degree-preserving random graph"), and (c) an interpretation boundary (what the result does and does not prove). Many fascinating biological questions ("How does the cortex generate consciousness?") are not directly testable with connectomics because they lack measurable structural endpoints.

**Good hypothesis example:** "Reciprocal connections between L2/3 pyramidal cells are enriched ≥2× compared to a degree-preserving null model." — Measurable (synapse counts), has a null model, makes a specific quantitative prediction.

**Poor hypothesis example:** "The connectome explains how the brain processes language." — No measurable endpoint, no null model, no interpretation boundary. This is an aspiration, not a hypothesis.

### 2) Choosing the right metric
The metric must match the hypothesis. Common connectomics metrics include:
- **Synapse count** (between specific neuron pairs or classes)
- **Motif frequency** (3-node or 4-node subgraph patterns)
- **Degree distribution** (in-degree, out-degree, or total degree)
- **Path length** (shortest path between neuron pairs)
- **Clustering coefficient** (local circuit density)
- **Convergence/divergence ratio** (fan-in vs fan-out)

**Metric mismatch trap:** Using a global metric (mean degree) to test a local hypothesis (microcircuit-specific wiring rule). The global metric may be normal even if the local pattern is highly abnormal. Always match the metric's spatial and biological scope to the hypothesis.

### 3) Null models are the foundation of interpretation
Every connectomics claim requires comparison to a null model. Without a null, you cannot distinguish specific wiring rules from generic statistical properties.
- **Erdos-Renyi** (same density): Too simple — doesn't preserve degree distribution. Almost everything looks "enriched."
- **Degree-preserving rewiring** (Maslov & Sneppen 2002): Standard baseline. Preserves each neuron's in-degree and out-degree.
- **Spatially constrained**: Preserves distance-dependent connection probability. Critical because nearby neurons connect more often simply due to arbor overlap.
- **Cell-type-stratified**: Preserves E→E, E→I, I→E, I→I connection rates. Important because excitatory-inhibitory structure creates motif biases even without specific wiring rules.
- **Key rule:** Use the most stringent null model that is relevant to your claim. If your finding survives the spatially constrained null but not the degree-preserving null, it may reflect spatial proximity rather than specific wiring.

### 4) Interpretation boundaries: what you can and cannot claim
Structure constrains possible computation but does not determine function. A connectomics result can say "this wiring pattern is consistent with function X" or "this wiring pattern is more common than expected," but it cannot say "this circuit computes X" without functional evidence. Always state both the supported claim and the explicit non-claim.

## Core workflow
1. Define question and estimand: what structural feature would constrain or inform the biological question?
2. Choose measurable outputs: specific metric(s) computed from the connectome graph.
3. Select null model: the most stringent null relevant to the claim.
4. Test and interpret results: compute metric, compare to null distribution, compute z-score and p-value.
5. Document supported vs unsupported claims: what the result proves, what it doesn't, and what additional evidence would be needed.

## 60-minute tutorial run-of-show

### Pre-class preparation (10 min async)
- Read the motif analysis content library entry (focus on null models section)
- Draft one biological question you'd like to test with connectomics data

### Minute-by-minute plan
1. **00:00-08:00 | Framing: good vs bad hypotheses**
   - Show 4 example hypotheses (2 good, 2 poor). Group identifies which are testable and why.
   - Key criteria: measurable endpoint, specified null, interpretation boundary.

2. **08:00-20:00 | Hypothesis drafting**
   - Each learner drafts a hypothesis using a template:
     - "In [dataset/region], [structural feature] is [comparison] compared to [null model]."
     - "This would support [interpretation] but would NOT prove [over-claim]."
   - Peer review: partner evaluates whether the hypothesis is testable.

3. **20:00-34:00 | Metric and null model selection**
   - For each drafted hypothesis, select the appropriate metric and null model.
   - Instructor walks through one example end-to-end: hypothesis → metric → null → expected result → interpretation.
   - Discussion: "What happens if you use the wrong null model?" Show how the same data looks significant or non-significant depending on null choice.

4. **34:00-46:00 | Interpretation workshop**
   - Present 3 pre-computed results (with p-values and z-scores). For each, learners write:
     - Supported claim (what the data shows)
     - Explicit non-claim (what the data does NOT show)
     - One confound that could explain the result
   - Group discussion of each result.

5. **46:00-60:00 | Competency check**
   - Each learner submits their final hypothesis with metric, null model, and interpretation boundaries.
   - Exit ticket: "Write one claim and one explicit non-claim from the same test outcome."

## Studio activity: hypothesis design and peer critique (60-75 minutes)

**Scenario:** Your lab is planning a study of feedforward vs feedback connectivity in mouse visual cortex using the MICrONS dataset. You need to design three testable hypotheses about the circuit architecture.

**Task sequence:**
1. Draft 3 hypotheses (one about feedforward connections, one about feedback connections, one about reciprocal connections).
2. For each: specify the metric, null model, required dataset version, and analysis code outline.
3. For each: write the supported claim and explicit non-claim.
4. Exchange with a partner. Critique their null model choices and interpretation boundaries.
5. Revise based on peer feedback.

**Expected outputs:**
- 3 hypothesis sheets (hypothesis, metric, null, interpretation boundary, non-claim).
- Peer critique notes (minimum 2 substantive comments per hypothesis).
- Revised hypotheses incorporating feedback.

## Assessment rubric
- **Minimum pass**: Coherent hypothesis/metric/null trio for at least 2 of 3 hypotheses.
- **Strong performance**: Clear uncertainty and non-claim statements. Null model choice justified. Peer critique identifies genuine issues.
- **Common failure to flag**: Vague hypothesis without measurable endpoint ("we will study connectivity patterns") or missing null model.

## Content library references
- [Motif analysis]({{ '/content-library/connectomics/motif-analysis/' | relative_url }}) — Null models, statistical testing, DotMotif
- [Network analysis methods]({{ '/content-library/connectomics/network-analysis-methods/' | relative_url }}) — Metrics for graph analysis
- [Graph representations]({{ '/content-library/connectomics/graph-representations/' | relative_url }}) — How to construct the graph you'll test
- [NeuroAI bridge]({{ '/content-library/connectomics/neuroai-bridge/' | relative_url }}) — Structure-function boundaries
- [Connectome history]({{ '/content-library/connectomics/connectome-history/' | relative_url }}) — Lessons from prior hypothesis-driven studies

## Teaching resources
- [Technical Unit 01]({{ '/technical-training/01-why-map-the-brain/' | relative_url }})
- [Technical Unit 09]({{ '/technical-training/09-connectome-analysis-neuroai/' | relative_url }})

## References
- Bargmann CI, Marder E (2013) "From the connectome to brain function." *Nature Methods* 10(6):483-490.
- Maslov S, Sneppen K (2002) "Specificity and stability in topology of protein networks." *Science* 296:910-913.
- Milo R et al. (2002) "Network motifs: simple building blocks of complex networks." *Science* 298:824-827.
- Song S et al. (2005) "Highly nonrandom features of synaptic connectivity." *PLoS Biology* 3(3):e68.
- Perin R et al. (2011) "A synaptic organizing principle for cortical neuronal groups." *PNAS* 108(13):5419-5424.

## Quick practice prompt
Write one claim and one explicit non-claim from the same test outcome.
