---
marp: true
theme: default
paginate: true
title: "Module 17: Scientific Writing for Connectomics"
---

# Module 17: Scientific Writing for Connectomics
Teaching Deck

---

## Learning Objectives
- Convert connectomics analyses into coherent claim-evidence writing
- Write figure legends that are reproducible and interpretation-safe
- Draft abstracts that distinguish result, uncertainty, and limitation
- Respond to reviewer critiques with technically grounded revisions

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
Produce a manuscript-ready results section (figures, legends, and claims) where each conclusion is traceable to explicit connectomics evidence and stated limitations. Students will also be able to write methods sections with the level of detail required for connectomics reproducibility and respond to peer review with technically precise, non-defensive language.

---

## Concept Focus
### 1) Structure of a connectomics paper: methods are unusually important
- **Technical:** in most neuroscience papers, the methods section is a reference appendix. In connectomics, it is primary evidence. Readers need to assess: What volume was imaged? At what resolution? What species, age, and preparation? Which segmentation algorithm was used, and what was the merge/split error rate? What proofreading version was the analysis based on? Was CAVE materialization pinned to a specific timestamp? Without these details, no biological claim is evaluable.
- **Plain language:** in connectomics, how you got the data is as important as what the data shows. Your methods section is not boilerplate --- it is where skeptical readers will spend the most time.
- **Misconception guardrail:** treating the methods section as a formality to write last. In connectomics, draft the methods first because they constrain what you can legitimately claim.

---

## Core Workflow
- **Evidence inventory**
- List candidate claims and required supporting figures/metrics.
- Build a claim-evidence matrix: claim, figure panel, statistical test, effect size, dataset version, caveat.
- **Methods drafting (first, not last)**
- Write the dataset description with full provenance.
- Document every preprocessing step, threshold, and parameter.
- Complete the reproducibility checklist.
- **Results drafting**
- Write one paragraph per claim cluster with explicit evidence pointers.
- Use calibrated uncertainty language throughout.
- Separate confirmed findings from exploratory observations.
- **Legend hardening**
- Ensure legends include dataset version, method variant, key parameters, sample sizes, and uncertainty indicators.
- Each legend should be interpretable without reading the main text.
- **Limitation pass**
- Add interpretation bounds (sampling, segmentation error, model assumptions, volume boundary effects).
- Quantify uncertainty where possible rather than using vague qualifiers.
- **Peer-review simulation**
- Exchange sections and produce one methods-focused critique plus one interpretation critique.
- Practice structured reviewer responses.

---

## 60-Minute Run-of-Show
- One mock connectomics figure set (3 panels) with underlying data tables.
- Claim-evidence matrix template (printed or digital).
- Methods reproducibility checklist (one per student).
- Two mock reviewer comments (one valid methodological concern, one partially mistaken interpretation critique).
- Timer visible to all students.
- Every claim in the results paragraph maps to a specific figure panel and metric.
- Methods section passes the reproducibility checklist with no critical gaps.
- Reviewer responses are structured, specific, and non-defensive.

---

## Misconceptions to Watch
- **Misconception guardrail:** treating the methods section as a formality to write last. In connectomics, draft the methods first because they constrain what you can legitimately claim.
- **Misconception guardrail:** writing stronger language does not strengthen weak evidence. Adjectives like "striking," "remarkable," and "clearly" do not substitute for effect sizes and confidence intervals.
- **Misconception guardrail:** uncertainty statements are not weakness; they are reproducibility signals. A paper that acknowledges its limits is more credible than one that ignores them.
- **Misconception guardrail:** assuming readers know which dataset version you used. Even within the same project (e.g., MICrONS), different materialization timestamps produce different connectivity tables.
- **Misconception guardrail:** linking to a GitHub repository is not sufficient if the repository has no tagged release and the methods do not specify which commit was used.
- **Misconception guardrail:** uncertainty statements are not weakness; they are reproducibility signals.
- **Misconception guardrail:** assuming that citing the original EM paper covers all required attributions. Segmentation, proofreading, and annotation are separate contributions that deserve separate citations.
- **Misconception guardrail:** defensive tone weakens technical credibility. Never characterize a reviewer's comment as "wrong" --- instead, provide the evidence that supports your position.

---

## Studio Activity
**Scenario:** You are preparing a short paper section on motif enrichment from a connectome analysis. Your team has identified that reciprocal connections between excitatory and inhibitory neurons in cortical layer 2/3 occur 2.1x more frequently than expected under a degree-preserving null model. The analysis used MICrONS minnie65 data, CAVE materialization v795, with synapse detection via the CAVE synapse table (cleft score threshold > 50). A total of 1,247 reciprocal pairs were observed across 12,891 possible excitatory-inhibitory pairs.

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
- **Minimum pass**
- Claims map to explicit evidence with figure panel references.
- Legends contain enough detail for independent interpretation.
- Methods include dataset version, pipeline, and key parameters.
- Reviewer responses are specific and technically grounded.
- **Strong performance**
- Clearly separates robust findings from tentative interpretations using calibrated language.
- Uses limitation language without weakening valid conclusions.
- Improves reproducibility via concrete method-detail additions.
- Reviewer responses include evidence and specific manuscript revision locations.
- **Common failure modes**
- Narrative claims that cannot be traced to figures.
- Missing dataset/method versioning in captions or methods.
- Reviewer replies that are persuasive but non-technical.
- Methods section written as an afterthought with missing parameters.

---

## Exit Ticket
Write one results paragraph from a connectomics figure and include:
1. one quantitative claim with effect size and confidence interval,
2. one explicit caveat tied to a known data limitation,
3. one sentence on reproducibility assumptions (dataset version, materialization, code),
4. one figure legend sentence that specifies sample size and uncertainty indicator.

---

## References (Instructor)
- Gopen and Swan (1990) - The science of scientific writing.
- White et al. (1986) - foundational connectome reporting style.
- Januszewski et al. (2018) - modern method reporting and performance framing.

---

## Teaching Materials
- Module page: /modules/module17/
- Slide page: /modules/slides/module17/
- Worksheet: /assets/worksheets/module17/module17-activity.md
