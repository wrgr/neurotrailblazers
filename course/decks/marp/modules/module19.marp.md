---
marp: true
theme: default
paginate: true
title: "Module 19: Peer Review and Scientific Ethics"
---

# Module 19: Peer Review and Scientific Ethics
Teaching Deck

---

## Learning Objectives
- Evaluate connectomics manuscripts for methodological and interpretive rigor
- Identify ethics risks in data handling, authorship, and reporting
- Draft constructive, technically specific peer-review feedback
- Make transparent integrity decisions in ambiguous collaboration scenarios

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
Produce a technically rigorous manuscript review and an ethics-risk decision memo for a connectomics study, including actionable recommendations and integrity safeguards. Students will be able to distinguish constructive criticism from destructive criticism, identify the specific ethical challenges that arise in large-scale connectomics collaborations, and make documented decisions when facing ambiguous integrity situations.

---

## Concept Focus
### 1) What peer reviewers look for in connectomics papers
- **Technical:** effective peer review of connectomics manuscripts requires evaluating several domain-specific dimensions:
  - **Data quality documentation:** does the paper report the segmentation error rate (merge/split metrics), synapse detection precision/recall, and proofreading completeness? Without these, no biological claim is evaluable.
  - **Statistical rigor:** are null models appropriate for the graph structure? Are multiple comparisons handled? Are effect sizes reported alongside p-values? Is there sensitivity analysis for key thresholds?
  - **Interpretation boundaries:** does the paper distinguish confirmed findings from exploratory observations? Are conclusions limited to what the data can actually support (e.g., one brain region in one animal at one developmental time point)?
  - **Data availability:** are the dataset version, CAVE materialization, code repository, and parameters sufficient for reproduction? Can a reader trace every claim to a specific data artifact?
- **Plain language:** a good reviewer checks whether the methods can actually support the claims, whether the statistics are honest, and whether someone else could reproduce the work.
- **Misconception guardrail:** "interesting result" is not a substitute for methodological soundness. A novel finding reported with inadequate methods documentation is worse than an incremental finding reported transparently.

---

## Core Workflow
- **Pre-review framing**
- Identify manuscript claim types (descriptive, predictive, explanatory).
- Note the dataset, methods pipeline, and stated limitations.
- **Methods-evidence audit**
- Check dataset versioning, preprocessing transparency, QC thresholds, and statistical controls.
- Verify that each claim maps to a specific figure panel and statistical test.
- **Interpretation audit**
- Flag overclaiming, underreported uncertainty, and missing limitations.
- Check whether conclusions are bounded by the data (one brain region, one species, one time point).
- **Ethics-risk scan**
- Evaluate authorship clarity, disclosure statements, data-governance assumptions, and consent coverage.
- Check for signs of selective reporting (missing negative results, single-threshold analyses).
- **Actionable response package**
- Write revision requests prioritized by scientific impact and integrity risk.
- Use constructive language: problem, evidence, suggestion.

---

## 60-Minute Run-of-Show
- One mock connectomics preprint (2-3 pages: abstract, key methods paragraph, two result figures with legends, and discussion excerpt). Pre-seeded with 4 issues: one methods gap, one overclaim, one ethics concern (ambiguous authorship), and one example of selective reporting.
- Structured review form template (one per student).
- Ethics-risk checklist (human tissue, attribution, data sharing, selective reporting).
- Two examples of real reviewer comments: one constructive, one destructive.
- Review comments reference specific manuscript locations (figure panels, paragraph numbers, methods details).
- Ethics concerns are tied to concrete workflow practices, not abstract principles.
- Recommendations are consistent with documented findings.
- All feedback uses constructive language (problem, evidence, suggestion).

---

## Misconceptions to Watch
- **Misconception guardrail:** "interesting result" is not a substitute for methodological soundness. A novel finding reported with inadequate methods documentation is worse than an incremental finding reported transparently.
- **Misconception guardrail:** ethics in connectomics is not just about IRB approval. It extends to data sharing, attribution, responsible AI, and honest reporting throughout the research lifecycle.
- **Misconception guardrail:** "interesting result" is not a substitute for methodological soundness.
- **Misconception guardrail:** being harsh is not the same as being rigorous. The most rigorous reviews are also the most specific and constructive.
- **Misconception guardrail:** compliance checklists alone do not ensure good practice. Integrity requires ongoing attention to workflow transparency.
- **Misconception guardrail:** contribution volume alone does not define authorship role. A person who proofread 10,000 segments may deserve authorship; a person who ran one analysis script may not. The criteria must be explicit and agreed upon in advance.

---

## Studio Activity
{: #studio-activity}

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
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

---

## Exit Ticket
Choose a connectomics abstract (from a real paper or the mock preprint) and produce:
1. One high-priority methods concern (what is missing, why it matters, what should be added).
2. One interpretation concern (which sentence overclaims, what the bounded version would say).
3. One ethics/integrity concern (tied to a specific workflow practice, not an abstract principle).
4. One actionable revision request for each of the above, written in constructive language.

---

## References (Instructor)
- COPE Core Practices.
- ICMJE authorship recommendations.
- FAIR principles (Wilkinson et al., 2016).

---

## Teaching Materials
- Module page: /modules/module19/
- Slide page: /modules/slides/module19/
- Worksheet: /assets/worksheets/module19/module19-activity.md
