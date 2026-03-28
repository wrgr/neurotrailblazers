---
title: "Module 19: Peer Review and Scientific Ethics"
layout: module
permalink: /modules/module19/
description: "Apply peer-review practice and research-ethics decision making to real connectomics workflows, claims, and collaborations."
module_number: 19
difficulty: "Intermediate"
duration: "4 hours"
learning_objectives:
  - "Evaluate connectomics manuscripts for methodological and interpretive rigor"
  - "Identify ethics risks in data handling, authorship, and reporting"
  - "Draft constructive, technically specific peer-review feedback"
  - "Make transparent integrity decisions in ambiguous collaboration scenarios"
prerequisites: "Modules 17-18 or equivalent writing/workflow experience"
merit_stage: "Dissemination"
compass_skills:
  - "Ethical Reasoning"
  - "Critical Review"
  - "Research Integrity"
ccr_focus:
  - "Character - Scientific Ethics"
  - "Meta-Learning - Reflective Practice"

# Normalized metadata
slug: "module19"
short_title: "Peer Review and Scientific Ethics"
status: "active"
audience:
  - "students"
pipeline_stage: "Dissemination"
merit_row_focus: "Dissemination"
topics:
  - "peer-review"
  - "research-ethics"
  - "authorship"
  - "reproducibility"
summary: "Run method-focused peer review and resolve ethics decisions in connectomics research with explicit documentation."
key_questions:
  - "What makes a review technically useful instead of opinion-based?"
  - "Where do integrity risks appear in large-scale connectomics projects?"
  - "How should authorship and credit be managed in consortium settings?"
slides: []
notebook: []
datasets:
  - "/datasets/workflow"
  - "/datasets/mouseconnects"
personas:
  - "/avatars/gradstudent"
  - "/avatars/mentor"
related_tools:
  - "/tools/ask-an-expert/"
  - "/tools/connectome-quality/"
related_frameworks:
  - "research-incubator-model"
  - "education-models"
prerequisites_list:
  - "Ability to interpret methods/results sections"
  - "Basic understanding of reproducibility and QC terms"
next_modules:
  - "module20"
  - "module21"
references:
  - "COPE Core Practices."
  - "ICMJE authorship recommendations."
  - "FAIR principles (Wilkinson et al., 2016)."
videos: []
downloads: []
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
---

## Capability target
Produce a technically rigorous manuscript review and an ethics-risk decision memo for a connectomics study, including actionable recommendations and integrity safeguards. Students will be able to distinguish constructive criticism from destructive criticism, identify the specific ethical challenges that arise in large-scale connectomics collaborations, and make documented decisions when facing ambiguous integrity situations.

## Why this module matters
Connectomics projects are collaborative, data-heavy, and method-sensitive. A single MICrONS or FlyWire paper may involve dozens of contributors spanning multiple institutions, with data collected from human or animal tissue, processed by automated pipelines, proofread by community volunteers, and analyzed by computational teams. Errors in interpretation, reporting, or credit assignment can undermine both scientific validity and team trust. Ethical practice here is operational, not abstract --- it affects real people, real data, and real scientific conclusions.

## Concept set

### 1) What peer reviewers look for in connectomics papers
- **Technical:** effective peer review of connectomics manuscripts requires evaluating several domain-specific dimensions:
  - **Data quality documentation:** does the paper report the segmentation error rate (merge/split metrics), synapse detection precision/recall, and proofreading completeness? Without these, no biological claim is evaluable.
  - **Statistical rigor:** are null models appropriate for the graph structure? Are multiple comparisons handled? Are effect sizes reported alongside p-values? Is there sensitivity analysis for key thresholds?
  - **Interpretation boundaries:** does the paper distinguish confirmed findings from exploratory observations? Are conclusions limited to what the data can actually support (e.g., one brain region in one animal at one developmental time point)?
  - **Data availability:** are the dataset version, CAVE materialization, code repository, and parameters sufficient for reproduction? Can a reader trace every claim to a specific data artifact?
- **Plain language:** a good reviewer checks whether the methods can actually support the claims, whether the statistics are honest, and whether someone else could reproduce the work.
- **Misconception guardrail:** "interesting result" is not a substitute for methodological soundness. A novel finding reported with inadequate methods documentation is worse than an incremental finding reported transparently.

### 2) Ethical issues specific to connectomics
- **Technical:** connectomics raises several domain-specific ethical concerns:
  - **Human tissue consent:** datasets like H01 use surgically resected human brain tissue. Consent processes must cover not only the initial use but also open data sharing, potential re-identification risks (from unique anatomical features), and downstream computational analyses not anticipated at the time of consent. The ethical review must address whether broad consent covers AI/ML applications.
  - **Data sharing obligations:** large publicly funded connectomics projects have data sharing mandates. Balancing open science with privacy, intellectual property for junior researchers, and responsible use requires explicit policies.
  - **Attribution for proofreaders:** in community proofreading projects (e.g., FlyWire Codex, Eyewire), thousands of volunteers contribute proofreading labor that is essential for data quality. Fair attribution practices must go beyond a blanket acknowledgment --- contribution tracking systems should inform authorship decisions, and community members should be credited proportionally.
  - **Responsible AI use:** using connectomics data to train AI models (for segmentation, synapse detection, or circuit prediction) raises questions about model bias, appropriate validation, and downstream applications. Models trained on one species or brain region may not generalize, and overclaiming generality is an ethical as well as scientific problem.
  - **Selective reporting:** the complexity of connectomics data creates many opportunities for selective reporting --- highlighting motifs that are enriched while ignoring those that are not, reporting only the threshold at which results are significant, or presenting one analysis variant while hiding others that gave different results.
- **Plain language:** connectomics has unique ethical challenges because it involves human tissue, massive collaborations with community contributors, and data complex enough to support many different stories depending on how you analyze it.
- **Misconception guardrail:** ethics in connectomics is not just about IRB approval. It extends to data sharing, attribution, responsible AI, and honest reporting throughout the research lifecycle.

### 3) Technical peer review is an engineering audit
- **Technical:** reviews should test evidence-method alignment, not just narrative quality. For each major claim, check: (a) Is the evidence shown in a figure panel? (b) Is the statistical test appropriate for the data structure? (c) Are the preprocessing decisions documented and justified? (d) Are alternative interpretations acknowledged? (e) Could the result be an artifact of a known data limitation (segmentation errors, boundary effects, incomplete proofreading)?
- **Plain language:** ask whether the methods can really support the claims. Read the methods section first, not the abstract.
- **Misconception guardrail:** "interesting result" is not a substitute for methodological soundness.

### 4) Constructive criticism vs destructive criticism
- **Technical:** constructive criticism is specific, evidence-based, actionable, and focused on improving the science. It identifies the problem, explains why it matters, and suggests a concrete path to resolution. Destructive criticism is vague, opinion-based, dismissive, or focused on the authors rather than the work. Examples:
  - **Constructive:** "The null model preserves degree sequence but not spatial constraints. Since connection probability in cortex depends strongly on distance (Ercsey-Ravasz et al., 2013), a spatially constrained null would be more appropriate. The authors could test whether their motif enrichment holds under a distance-dependent Erdos-Renyi model."
  - **Destructive:** "The statistics are unconvincing and the claims are overblown."
  - **Constructive:** "Figure 3 shows a 2x enrichment of reciprocal connections, but the confidence interval overlaps 1.5x. The authors should report the effect size with the CI and discuss whether this enrichment is biologically meaningful at the lower bound."
  - **Destructive:** "The enrichment is probably not real."
- **Plain language:** good criticism tells the authors what is wrong, why it matters, and what they can do about it. Bad criticism just says "this is not good enough."
- **Misconception guardrail:** being harsh is not the same as being rigorous. The most rigorous reviews are also the most specific and constructive.

### 5) Integrity risks are workflow-linked
- **Technical:** risks include silent preprocessing changes (modifying thresholds after seeing results), undocumented QC exceptions (excluding outliers without reporting), selective reporting (showing only the analysis variant that "works"), and ambiguous authorship criteria (adding or removing authors based on politics rather than contribution).
- **Plain language:** ethics problems often start as process shortcuts. The researcher who silently changes a threshold "just to see" and then forgets to report it has created an integrity problem.
- **Misconception guardrail:** compliance checklists alone do not ensure good practice. Integrity requires ongoing attention to workflow transparency.

### 6) Authorship and credit need explicit rules
- **Technical:** large connectomics projects should use contribution tracking (e.g., CRediT taxonomy) and written authorship criteria established before the project produces results. In consortium settings, define: what level of proofreading contribution qualifies for authorship vs acknowledgment? How are computational contributions weighed against experimental ones? Who decides authorship order? These decisions should be documented in a project governance document, not resolved ad hoc when the paper is nearly submitted.
- **Plain language:** decide credit rules before conflicts happen. Put them in writing. Revisit them when roles change.
- **Misconception guardrail:** contribution volume alone does not define authorship role. A person who proofread 10,000 segments may deserve authorship; a person who ran one analysis script may not. The criteria must be explicit and agreed upon in advance.

## Core workflow: review and ethics decision process
1. **Pre-review framing**
   - Identify manuscript claim types (descriptive, predictive, explanatory).
   - Note the dataset, methods pipeline, and stated limitations.
2. **Methods-evidence audit**
   - Check dataset versioning, preprocessing transparency, QC thresholds, and statistical controls.
   - Verify that each claim maps to a specific figure panel and statistical test.
3. **Interpretation audit**
   - Flag overclaiming, underreported uncertainty, and missing limitations.
   - Check whether conclusions are bounded by the data (one brain region, one species, one time point).
4. **Ethics-risk scan**
   - Evaluate authorship clarity, disclosure statements, data-governance assumptions, and consent coverage.
   - Check for signs of selective reporting (missing negative results, single-threshold analyses).
5. **Actionable response package**
   - Write revision requests prioritized by scientific impact and integrity risk.
   - Use constructive language: problem, evidence, suggestion.

## 60-minute tutorial run-of-show

### Materials needed
- One mock connectomics preprint (2-3 pages: abstract, key methods paragraph, two result figures with legends, and discussion excerpt). Pre-seeded with 4 issues: one methods gap, one overclaim, one ethics concern (ambiguous authorship), and one example of selective reporting.
- Structured review form template (one per student).
- Ethics-risk checklist (human tissue, attribution, data sharing, selective reporting).
- Two examples of real reviewer comments: one constructive, one destructive.

### Timing and instructor script

**00:00-08:00 | Constructive vs destructive criticism**
Instructor displays two real (anonymized) reviewer comments for the same paper. One is specific, evidence-based, and actionable; the other is vague and dismissive. Students identify which is which and explain why. Key script line: "The most rigorous reviewer is not the harshest one. Rigor means specificity. Vague criticism is lazy, not tough."

**08:00-12:00 | What reviewers look for in connectomics**
Instructor presents a checklist of connectomics-specific review criteria: data quality metrics, appropriate null models, reproducibility metadata, interpretation boundaries, and data availability. Brief discussion of how these differ from standard neuroscience review criteria.

**12:00-28:00 | Methods-evidence audit exercise**
Students read the mock preprint individually. Using the structured review form, each student identifies: (a) one methods gap with specific missing information, (b) one overclaim where the language exceeds the evidence, (c) one figure panel where uncertainty is insufficiently represented. Instructor circulates, prompting: "Can you point to the exact sentence that overclaims? What would the bounded version say?"

**28:00-38:00 | Ethics-risk scan**
Students use the ethics-risk checklist to scan the mock preprint. They identify: (a) the authorship ambiguity (the mock paper lists "the consortium" as an author without specifying individual contributions), (b) the selective reporting concern (only one of three tested motifs is discussed in results). Students draft a one-paragraph ethics memo for each issue with a concrete mitigation recommendation.

**38:00-50:00 | Decision memo drafting**
In pairs, students draft a complete review decision memo: (a) summary of the paper's contribution, (b) major concerns (methods, interpretation, ethics) with evidence, (c) minor concerns, (d) recommendation (accept with revisions, major revisions, or reject) with explicit rationale. Students must ensure their recommendation is consistent with their documented concerns.

**50:00-58:00 | Peer review of reviews**
Pairs swap decision memos and evaluate: Is the review specific and evidence-based? Is the recommendation consistent with the concerns? Is the tone constructive? Each pair writes one improvement suggestion.

**58:00-60:00 | Competency check**
Each student submits their structured review form and decision memo. Instructor collects for after-session review.

### Success criteria for this session
- Review comments reference specific manuscript locations (figure panels, paragraph numbers, methods details).
- Ethics concerns are tied to concrete workflow practices, not abstract principles.
- Recommendations are consistent with documented findings.
- All feedback uses constructive language (problem, evidence, suggestion).

## Studio activity: connectomics review board simulation

**Scenario:** Your team is acting as reviewers for a connectomics preprint claiming a novel circuit motif --- a specific three-neuron feed-forward inhibitory loop --- with translational implications for understanding epilepsy. The preprint uses MICrONS minnie65 data (CAVE materialization v661) and reports 3.5x enrichment of this motif relative to a degree-preserving random graph null model (p < 0.001 after Bonferroni correction across 13 three-node motif classes). The methods section does not report the synapse confidence threshold, does not mention boundary neuron handling, and lists "MICrONS Consortium" as a co-author without individual contribution details. The discussion section states that "this motif likely plays a causal role in seizure propagation."

**Tasks**
1. Write one methods critique (specific: what is missing, why it matters, what the authors should add) and one interpretation critique (specific: which sentence overclaims, what the bounded version would say).
2. Identify two ethics risks: (a) the authorship/attribution concern and (b) one additional concern (selective reporting, consent, data sharing, or responsible AI). For each, draft a concrete mitigation recommendation.
3. Draft a decision memo: accept with revisions, major revisions, or reject. Justify your recommendation by referencing your specific concerns.
4. Propose one concrete integrity policy improvement for the project team (e.g., a contribution tracking system, a preregistration requirement, a threshold sensitivity analysis mandate).

**Expected outputs**
- Structured review form (claims, methods audit, evidence gaps, interpretation audit).
- Ethics-risk memo with two identified risks and concrete mitigations.
- Decision memo with recommendation and traceable rationale.
- One-paragraph integrity policy proposal.

## Assessment rubric
- **Minimum pass**
  - Review comments are specific and evidence-linked (referencing figure panels, methods details, or specific sentences).
  - Ethics risks are identified with concrete mitigations tied to workflow practices.
  - Recommendation is consistent with documented findings.
- **Strong performance**
  - Distinguishes fixable technical issues from fundamental validity failures.
  - Balances rigor with constructive tone and practical revision advice.
  - Uses transparent criteria for authorship/integrity judgments.
  - Anticipates author responses and pre-addresses potential objections.
- **Common failure modes**
  - Generic critique with no evidence references ("the statistics are weak").
  - Ethics discussion disconnected from actual workflow practices.
  - Inconsistent recommendation versus identified risks (e.g., listing major concerns but recommending accept with minor revisions).
  - Destructive tone that undermines the credibility of valid criticisms.

## Content library cross-references
- [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}) --- the versioning infrastructure that reviewers should expect papers to document.
- [H01 human cortex]({{ '/content-library/case-studies/h01-human-cortex/' | relative_url }}) --- a case study raising ethical questions about human tissue consent, open data sharing, and attribution in large collaborations.

## Teaching resources
- Review practice context: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Workflow integrity context: [Workflow overview]({{ '/datasets/workflow' | relative_url }})
- QC context: [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})
- Mentorship/escalation context: [Ask-an-Expert]({{ '/tools/ask-an-expert/' | relative_url }})

## Evidence anchors from connectomics practice

### Key papers to use in this module
- [White, J.G. et al. (1986). "The Structure of the Nervous System of the Nematode *Caenorhabditis elegans*."](https://doi.org/10.1098/rstb.1986.0056) --- study as an example of thorough methods reporting in connectomics.
- [Kasthuri, N. et al. (2015). "Saturated Reconstruction of a Volume of Neocortex." *Cell*, 162(3), 648-661.](https://doi.org/10.1016/j.cell.2015.06.054) --- review the methods section for reconstruction quality documentation.
- [MICrONS Consortium (2025). Visual cortex reconstruction. *Nature.*](https://www.nature.com/articles/s41586-025-08790-w) --- exemplary large-collaboration authorship and methods documentation.
- [Shapson-Coe, A. et al. (2024). H01 human cortical fragment. *Science.*](https://www.science.org/doi/10.1126/science.adk4858) --- ethical considerations for human tissue connectomics and open data.
- [COPE (Committee on Publication Ethics). Core Practices.](https://publicationethics.org/core-practices) --- ethical guidelines for peer review and publication.
- [ICMJE. Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work.](https://www.icmje.org/recommendations/) --- authorship criteria.
- [Dorkenwald, S. et al. (2024). "Neuronal wiring diagram of an adult brain." *Nature*, 634, 124-138.](https://doi.org/10.1038/s41586-024-07558-y) --- FlyWire whole-brain connectome with community proofreading attribution model.

### Key datasets to practice on
- [MICrONS Explorer](https://www.microns-explorer.org/)
- [H01 dataset](https://h01-release.storage.googleapis.com/landing.html)
- [FlyWire](https://flywire.ai/)
- [Workflow overview]({{ '/datasets/workflow' | relative_url }})

### Competency checks
- Can you identify one overclaim in a connectomics abstract and rewrite it with evidence boundaries?
- Can you map one ethics risk to a concrete workflow control (not just a policy statement)?
- Can you justify your editorial recommendation with traceable criteria referenced to specific manuscript locations?
- Can you distinguish constructive from destructive criticism in your own review draft?
- Can you articulate the specific ethical obligations associated with using community-proofread data?

## Quick practice prompt
Choose a connectomics abstract (from a real paper or the mock preprint) and produce:
1. One high-priority methods concern (what is missing, why it matters, what should be added).
2. One interpretation concern (which sentence overclaims, what the bounded version would say).
3. One ethics/integrity concern (tied to a specific workflow practice, not an abstract principle).
4. One actionable revision request for each of the above, written in constructive language.
