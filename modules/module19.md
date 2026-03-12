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
Produce a technically rigorous manuscript review and an ethics-risk decision memo for a connectomics study, including actionable recommendations and integrity safeguards.

## Why this module matters
Connectomics projects are collaborative, data-heavy, and method-sensitive. Errors in interpretation, reporting, or credit assignment can undermine both scientific validity and team trust. Ethical practice here is operational, not abstract.

## Concept set
### 1) Technical peer review is an engineering audit
- **Technical:** reviews should test evidence-method alignment, not just narrative quality.
- **Plain language:** ask whether the methods can really support the claims.
- **Misconception guardrail:** "interesting result" is not a substitute for methodological soundness.

### 2) Integrity risks are workflow-linked
- **Technical:** risks include silent preprocessing changes, undocumented QC exceptions, selective reporting, and ambiguous authorship criteria.
- **Plain language:** ethics problems often start as process shortcuts.
- **Misconception guardrail:** compliance checklists alone do not ensure good practice.

### 3) Authorship and credit need explicit rules
- **Technical:** large projects should use contribution tracking and written authorship criteria early.
- **Plain language:** decide credit rules before conflicts happen.
- **Misconception guardrail:** contribution volume alone does not define authorship role.

## Core workflow: review and ethics decision process
1. **Pre-review framing**
   - Identify manuscript claim types (descriptive, predictive, explanatory).
2. **Methods-evidence audit**
   - Check dataset versioning, preprocessing transparency, QC thresholds, and statistical controls.
3. **Interpretation audit**
   - Flag overclaiming, underreported uncertainty, and missing limitations.
4. **Ethics-risk scan**
   - Evaluate authorship clarity, disclosure statements, and data-governance assumptions.
5. **Actionable response package**
   - Write revision requests prioritized by scientific impact and integrity risk.

## Studio activity: connectomics review board simulation
**Scenario:** Your team is acting as reviewers for a connectomics preprint claiming a novel circuit motif with translational implications.

**Tasks**
1. Write one methods critique and one interpretation critique with evidence.
2. Identify two ethics risks (for example: selective reporting, unclear authorship).
3. Draft a decision memo: accept with revisions, major revisions, or reject.
4. Propose one concrete integrity policy improvement for the project team.

**Expected outputs**
- Structured review form (claims, methods, evidence gaps).
- Ethics-risk memo with mitigation actions.
- Final recommendation with rationale.

## Assessment rubric
- **Minimum pass**
  - Review comments are specific and evidence-linked.
  - Ethics risks are identified with concrete mitigations.
  - Recommendation is consistent with documented findings.
- **Strong performance**
  - Distinguishes fixable technical issues from fundamental validity failures.
  - Balances rigor with constructive tone and practical revision advice.
  - Uses transparent criteria for authorship/integrity judgments.
- **Common failure modes**
  - Generic critique with no evidence references.
  - Ethics discussion disconnected from actual workflow practices.
  - Inconsistent recommendation versus identified risks.

## Teaching resources
- Review practice context: [Technical Track Journal Club]({{ '/technical-training/journal-club/' | relative_url }})
- Workflow integrity context: [Workflow overview]({{ '/datasets/workflow' | relative_url }})
- QC context: [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})
- Mentorship/escalation context: [Ask-an-Expert]({{ '/tools/ask-an-expert/' | relative_url }})

## Evidence anchors from connectomics practice
### Key papers to use in this module
- [White et al. (1986)](https://doi.org/10.1098/rstb.1986.0056)
- [Kasthuri et al. (2015)](https://doi.org/10.1016/j.cell.2015.06.054)
- [MICrONS visual cortex reconstruction (Nature, 2025)](https://www.nature.com/articles/s41586-025-08790-w)

### Key datasets to practice on
- [MICrONS Explorer](https://www.microns-explorer.org/)
- [H01 dataset](https://h01-release.storage.googleapis.com/landing.html)
- [Workflow overview]({{ '/datasets/workflow' | relative_url }})

### Competency checks
- Can you identify one overclaim and rewrite it with evidence boundaries?
- Can you map one ethics risk to a concrete workflow control?
- Can you justify your editorial recommendation with traceable criteria?

## Quick practice prompt
Choose a connectomics abstract and produce:
1. one high-priority methods concern,
2. one interpretation concern,
3. one ethics/integrity concern,
4. one actionable revision request for each.
