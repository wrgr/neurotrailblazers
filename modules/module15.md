---
title: "Module 15: LLMs for Patch Analysis"
layout: module
permalink: /modules/module15/
description: "Use LLM-assisted workflows for patch triage, annotation support, and documentation in connectomics without outsourcing scientific judgment."
module_number: 15
image: /assets/images/modules/module15.svg
image_alt: "Stylized vector art: an EM patch beside chat bubbles of generated analysis."
difficulty: "Advanced"
duration: "4-5 hours"
learning_objectives:
  - "Identify realistic LLM use cases in connectomics patch workflows"
  - "Design prompt/evaluation loops with reliability checks"
  - "Detect hallucination and unsupported inference risks"
  - "Integrate LLM outputs into human-in-the-loop QC"
prerequisites: "Modules 12-14"
merit_stage: "Analysis"
compass_skills:
  - "AI-Assisted Analysis"
  - "Prompt Design"
  - "Verification Practice"
ccr_focus:
  - "Skills - AI Tooling"
  - "Character - Critical Verification"

# Normalized metadata
slug: "module15"
short_title: "LLMs for Patch Analysis"
status: "active"
audience:
  - "students"
pipeline_stage: "Analysis"
merit_row_focus: "Analysis"
topics:
  - "llm"
  - "patch-analysis"
  - "human-in-the-loop"
summary: "Apply LLM support to patch-level workflows with strict verification and quality controls."
key_questions:
  - "Where can LLMs help without introducing unacceptable risk?"
  - "How should outputs be verified before scientific use?"
  - "Which tasks must remain human-adjudicated?"
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
  - "Segmentation and proofreading basics"
  - "Basic scripting and data-table handling"
next_modules:
  - "module16"
references:
  - "LLM reliability and evaluation literature (task-specific)."
  - "Internal patch-analysis workflow guidance."
videos: []
downloads: []
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
content_type: path
---

## Capability target
Implement an LLM-assisted patch-analysis workflow with verification gates, confidence labeling, and explicit human override policies. Concretely: classify every output your workflow produces into named output classes, attach a verification method and a numeric acceptance threshold to each class before any output is used, measure whether the gate costs less than the task it replaces, and log model version, prompt, output, reviewer, and decision so a reader can reconstruct which claims a model touched.

## Why this module matters
LLMs are genuinely useful for triage, drafting, and code assistance, and they fail in ways that are hard to notice precisely because the output is fluent. In connectomics the failures cluster in four places. Current models fabricate quantitative claims — synapse counts, cell counts, metric values — with the same confident phrasing they use for correct ones. They fabricate or misattribute citations. Vision-language models describe EM images plausibly and misidentify structures, calling an astrocytic process an axon or a tangentially cut spine neck a separate profile. And they recombine existing knowledge rather than generating new biological knowledge, so an LLM-produced "hypothesis" is a restatement of the literature, which is useful as a starting point and worthless as evidence.

The consequence is a governance problem, not a prompting problem. Gates, version logging, and override rules have to be defined per output class *before* use. Defined afterwards, they get defined around whatever the model already produced.

## Concept set

### 1) Assistive, not autonomous
- **Technical:** LLMs should support prioritization, summarization, code drafting, and protocol guidance. They should not perform final biological adjudication — whether this profile is a synapse, whether this is a merge error, which cell type this is. The dividing line is whether an error would enter a released data product without a human seeing it. If yes, the task is human-adjudicated regardless of how well the model performs in a pilot.
- **Plain language:** use an LLM to help, not to decide alone.
- **Misconception guardrail:** fluent output means correct output.

### 2) Verification-first design
- **Technical:** enumerate output classes before you start — code, literature summary, image description, ranking, protocol draft, quantitative claim — and attach to each a verification method and an acceptance threshold that can fail. For quantitative claims the threshold is absolute: never accept a number an LLM states, recompute it. For code, the gate is re-running with an explicit version pin and comparing against one maintained known-answer case. For rankings, the gate is precision at *k* on a labeled holdout, compared against the heuristic you already use.
- **Plain language:** decide how you will check the answer before you ask the question.
- **Misconception guardrail:** spot-checking is enough when the output looks unusual.

### 3) The gate must cost less than the task it replaces
- **Technical:** an LLM saves time only when drafting plus verification is cheaper than doing the task directly, and both sides of that comparison have to be measured on your own team. A query that takes 12 minutes to write by hand and 3 minutes to prompt plus 6 minutes to verify is a win. An EM patch description that takes an expert as long to adjudicate as to annotate from scratch is not — the model has moved the work, not reduced it. When the gate costs more than the task, the honest conclusion is that this output class is not yet an LLM task.
- **Plain language:** if checking takes longer than doing, do it yourself.
- **Misconception guardrail:** LLM assistance saves time on every task it can perform.

### 4) Auditability
- **Technical:** log model name and version, the exact prompt including any system prompt, the raw output, the verification result, the reviewer, and the final decision — as structured records tied to the artifact, not as chat history. Model versions change under the same product name, so a result you cannot tie to a specific version cannot be reproduced or contested. Disclose LLM assistance in the methods section, naming which output classes were assisted.
- **Plain language:** keep records specific enough that someone can re-run what you ran.
- **Misconception guardrail:** chat history is sufficient traceability.

### 5) Human override is unconditional
- **Technical:** any annotator can override any LLM suggestion without justification, and the human decision is authoritative. This has to be stated as policy, because the failure it prevents is social rather than technical: when a model's suggestion appears first in the interface, annotators anchor on it and their disagreement rate falls. Measure this. If annotator disagreement with model suggestions drops over the first weeks without a corresponding improvement in the model, you are seeing anchoring, and the fix is to hide the suggestion until the annotator has recorded an independent call.
- **Plain language:** the person decides, and the interface must let them decide first.
- **Misconception guardrail:** showing the model's answer first speeds annotators up without changing their judgment.

## Output classes, gates, and what each gate costs

Fill this table for your own project before any LLM output is used. The thresholds below are starting positions.

| Output class | Verification gate | Ship when | What the gate costs |
|---|---|---|---|
| Code or query drafts | Re-run with an explicit materialization version pin; compare against one maintained known-answer case | Result matches the known-answer case exactly | A few minutes per query, plus maintaining the known-answer case |
| Literature summaries | Every citation's DOI resolves and the claimed finding appears in the abstract or a named figure | 100% of citations verified; no exceptions | 2-5 minutes per citation, scaling with reference count |
| EM patch descriptions | Expert adjudication against the image | Only as a search hint; never written into an annotation table | Expert time roughly equal to annotating the patch — the gate costs as much as the task |
| Queue triage or ranking | Precision at *k* on a labeled holdout, against the current heuristic | Beats the existing heuristic by a margin you set in advance | A labeled holdout that must be refreshed as the segmentation changes |
| Protocol or SOP drafts | Team calibration on 10 real cases | Two reviewers independently reach the same decision on all 10 | One calibration session per revision |
| Quantitative claims | Recompute from the data | Never — the recomputed number is the claim | Cheap, and must be non-negotiable |

## Worked example: reviewing one day of LLM output

The numbers below are illustrative — they show how the gates behave, not measurements from a specific system.

**Output 1, a CAVEclient query.** You asked for all synapses onto a given neuron. The generated code runs without error and returns 1,240 rows, which is plausible. The gate for code is: re-run with an explicit version pin. Doing so against materialization version 943 returns 1,197 rows. The 43-row difference is not a bug — it is proofreading that happened between version 943 and the live state the unpinned query silently used. The generated code was *correct* and *unreproducible*, which is the harder failure to see, and it is the specific failure this gate exists to catch. Recovery: pin the version, re-run, record 1,197 with the version number, and add the version argument to the prompt template so the next draft includes it.

**Output 2, a patch description.** A vision-language model describes a patch as "a myelinated axon with an adjacent astrocytic process." The gate for image descriptions is expert adjudication. The expert calls the second profile a tangentially cut dendritic spine neck, not glia. Because one disagreement proves nothing, you run a 50-patch pilot: the model agrees with the expert on structure identity in 31 of 50 patches. That is far below any threshold at which a description could enter an annotation table. It is also not zero, so the model retains one legitimate use — surfacing patches that mention a feature you are searching for, with a human confirming each hit. Note what the pilot cost: the expert reviewed 50 patches, which is roughly what annotating 50 patches would have cost. That measurement is the argument for restricting this output class, and it is worth making once rather than assuming either way.

**Output 3, a literature summary with four citations.** The gate is that every DOI resolves and the claimed finding appears in the abstract or a named figure. Three check out. The fourth pairs real author names with a title that does not exist. Recovery: delete the citation, and record the event in the risk register — because the operative conclusion is about the class, not the instance. A model that fabricated one citation in four cannot be used to produce reference lists at all. It can still be used to locate candidate papers that you then verify, which is a different output class with a different gate.

**What the day produced.** Two usable outputs and one restricted class. The workflow's value is not that the model was right; it is that each failure was caught by a gate defined in advance, at a cost you can state. Had the gates been written afterwards, the unpinned query would have looked like a success — it ran, and the number was plausible.

## Core workflow
1. Enumerate the candidate LLM tasks in your project and sort them into named output classes.
2. For each class, write the verification method and a numeric acceptance threshold that can fail, before generating any output.
3. Estimate, then measure, the cost of the gate against the cost of doing the task directly; drop any class where the gate costs more.
4. Create prompt templates with an explicit output schema, and include the fields that gates depend on — for code, the version pin; for summaries, the citation list.
5. Define the human override policy and the interface rule that prevents anchoring: independent human call recorded before the suggestion is shown.
6. Pilot on a small set — 20 to 50 items per class — and log every failure with its cause.
7. Set the logging fields: model name and version, prompt, raw output, verification result, reviewer, decision, timestamp.
8. Refine prompts and thresholds from the pilot, then state in your methods which output classes were LLM-assisted.

## Pre-class preparation
- Read [proofreading tools]({{ '/content-library/proofreading/proofreading-tools/' | relative_url }}) so you know what the human-in-the-loop workflow currently is.
- Bring one real task from your own work you were considering handing to an LLM.
- Be ready to estimate how long that task takes you by hand.

## 60-minute tutorial run-of-show
1. **00:00-08:00** scope boundaries and failure examples. Show the unpinned-query failure first, because it is the one that looks like a success.
2. **08:00-20:00** prompt template design, including the schema fields each gate depends on.
3. **20:00-34:00** run sample outputs and score reliability against a known answer; record agreement counts rather than impressions.
4. **34:00-46:00** define verification and override rules per output class, and estimate the cost of each gate.
5. **46:00-56:00** produce governance checklist and risk register, with one class explicitly marked as not yet usable.
6. **56:00-60:00** competency check: each learner states one output class they would refuse to gate, and why.

## Studio activity
{: #studio-activity}
**Scenario:** Build an LLM-assisted triage helper for proofreading queues. Reviewers can inspect about 500 segments per week; the current heuristic ranks candidates by segment size and produces roughly 40% true errors in the top 500. Your team wants to know whether an LLM-assisted ranker, drawing on segment statistics and free-text QC notes, should replace it. You have a labeled holdout of 300 segments and one expert available for four hours.

**Tasks**
1. Enumerate the output classes this helper will produce and name the one that carries the most risk.
2. Write the verification gate and numeric acceptance threshold for each class, before generating any output.
3. Estimate the cost of each gate and compare it with the cost of the task it replaces; mark any class where the gate loses.
4. Design the pilot: how many items per class, who adjudicates, and what result would cause you to abandon the helper.
5. Specify the logging schema and the human override policy, including the interface rule that prevents anchoring.
6. Write the risk register: for each output class, the failure mode, its detection method, and the fallback if the gate fails.

**Outputs**
- prompt + schema pack,
- verification rubric with numeric thresholds per output class,
- gate-cost comparison table,
- risk register and override policy.

## Assessment rubric
- **Minimum pass:** clear task boundaries, verification logic with thresholds that can fail, and logging fields including model version and prompt.
- **Strong performance:** robust failure-mode handling, an actionable governance plan, a measured or defensibly estimated gate cost for each output class, and at least one class explicitly declared not yet usable.
- **Failure modes:** unbounded scope, no confidence policy, missing audit trail, thresholds written after seeing the outputs, and gates whose cost was never compared with the task they replace.

## Practical LLM use cases in connectomics

### Where LLMs add value today
| Use case | Example prompt | Verification method |
|----------|---------------|-------------------|
| **Literature summarization** | "Summarize the key findings of Dorkenwald et al. 2024 regarding cell-type diversity" | Cross-check against paper abstract and figures |
| **Code assistance** | "Write a CAVEclient query to find all synapses onto neuron X at materialization version 943" | Run the code and verify output matches manual check |
| **EM patch description** | "Describe the ultrastructural features visible in this EM image" (multimodal) | Expert annotator review of description accuracy |
| **Hypothesis brainstorming** | "Given that reciprocal connections are 4× enriched, what functional hypotheses could explain this?" | Evaluate against literature; treat as starting points, not conclusions |
| **Protocol drafting** | "Draft a proofreading SOP for merge error correction" | Expert review and team calibration before adoption |

### Where LLMs fail or mislead
- **Quantitative claims**: LLMs may confidently state incorrect numbers (synapse counts, cell counts, metric values). Always verify against the actual data.
- **Visual interpretation**: Current vision-language models can describe EM images but may misidentify structures (e.g., calling an astrocytic process an axon). Expert verification is mandatory.
- **Citation accuracy**: LLMs may fabricate references or misattribute findings. Always check cited papers exist and say what the LLM claims.
- **Novel biological claims**: LLMs cannot generate new biological knowledge — they can only recombine and rephrase existing knowledge.

### Governance framework
For any LLM-assisted workflow in a connectomics project:
1. **Define scope**: Which tasks are LLM-assisted? Which require human-only decisions?
2. **Version control**: Log the model name/version, prompt text, and output for every LLM interaction used in analysis.
3. **Verification gates**: Every LLM output category has a defined verification method and acceptance threshold.
4. **Human override**: Any LLM suggestion can be overridden by a human annotator without justification. The human decision is authoritative.
5. **Transparency**: In publications, disclose any LLM assistance in methods section.

## Common errors and how to recover

- **Generated code runs, returns a plausible number, and has no version pin.** Recover by re-running against an explicit materialization version, recording the pinned result, and comparing the two counts — the difference is proofreading, not a bug, but only the pinned number is citable. Then add the version field to the prompt template so subsequent drafts carry it.
- **A citation in an LLM-drafted section does not exist.** Recover by removing it and re-verifying every other citation in the same output, not just that one. Record the failure rate for the output class; a class that fabricates at any measurable rate cannot produce reference lists, only candidate paper leads.
- **A model's EM description was written into an annotation table.** Recover by identifying every row sourced from that output class using the logs, marking those rows provisional, and re-adjudicating them by expert before any analysis uses them. If the logs do not identify them, the correct action is to invalidate the whole table for that field — which is why the logging schema exists.
- **Annotator disagreement with model suggestions falls steadily with no model change.** This is anchoring. Recover by changing the interface so the annotator records an independent call before the suggestion is shown, then re-measure the disagreement rate on a fresh sample.
- **The helper saves no time despite good accuracy.** Recover by measuring both sides directly — time to do the task by hand, and time to prompt plus verify — on 10 real items. If the gate is the larger number, retire that output class and say so; it is a legitimate result, not a failure of effort.
- **Nobody can reconstruct which claims a model touched.** Recover by treating every artifact produced during the ungoverned period as unverified, and re-verifying the specific claims that appear in the manuscript. Then move logging into the tool itself, since a logging step that depends on someone remembering will not be done.
- **The model version changed under the same product name and results shifted.** Recover by pinning the version identifier in the request where the provider supports it, recording it where they do not, and re-running the pilot for each affected output class when the version moves. Do not carry old acceptance thresholds forward without re-measurement.

## What this module does not cover

- **Prompt engineering as a technique.** Templates appear here only as carriers for the fields gates depend on; this module is about governance, not phrasing.
- **Model selection, fine-tuning, and cost.** Which model to use and what it costs change quickly, and any number here would be stale; establish the gates first, then evaluate candidates against them.
- **The computer-vision models that actually perform segmentation and detection.** Those are [Module 14]({{ '/modules/module14/' | relative_url }}) and [Technical Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}). An LLM is not a substitute for them.
- **ML validity generally** — leakage, splits, base rates, calibration: [Module 13]({{ '/modules/module13/' | relative_url }}).
- **Authorship, disclosure norms, and research ethics beyond a methods statement.** See [Module 19]({{ '/modules/module19/' | relative_url }}).
- **Whether the underlying biology in a model's output is correct.** Verify against the anatomy references, particularly [neuron type identification]({{ '/content-library/cell-types/neuron-type-identification/' | relative_url }}) and [synapse classification]({{ '/content-library/neuroanatomy/synapse-classification/' | relative_url }}).

## Content library references
- [NeuroAI bridge]({{ '/content-library/connectomics/neuroai-bridge/' | relative_url }}) — AI tools for neuroscience and vice versa
- [Neuron type identification]({{ '/content-library/cell-types/neuron-type-identification/' | relative_url }}) — What correct classification looks like (for verifying LLM calls)
- [Proofreading tools]({{ '/content-library/proofreading/proofreading-tools/' | relative_url }}) — The human-in-the-loop tools LLMs would augment
- [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}) — Why an unpinned query is unreproducible

## Teaching resources
- [Module 14]({{ '/modules/module14/' | relative_url }})
- [Technical Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }})
- [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})

## Quick practice prompt
For one LLM output type, define: acceptance threshold, verification method, and human override trigger.
