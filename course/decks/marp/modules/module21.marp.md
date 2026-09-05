---
marp: true
theme: default
paginate: true
title: "Module 21: Reproducibility and FAIR Principles in Connectomics"
---

# Module 21: Reproducibility and FAIR Principles in Connectomics
Teaching Deck

---

## Learning Objectives
- Apply FAIR principles to connectomics data products
- Define minimum reproducibility metadata for analysis releases
- Build transparent methods/parameter logs for peer reuse
- Identify hidden-curriculum norms in reproducibility expectations

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
Publish a reproducibility-ready connectomics package (data + methods + metadata + limitations) that an external group can audit and reuse.

---

## Concept Focus
### 1) FAIR as implementation checklist
- **Technical:** findable identifiers, accessible storage, interoperable formats, and reusable metadata each require concrete engineering choices.
- **Plain language:** "FAIR" only counts if someone else can actually find, open, and use your work.
- **Misconception guardrail:** posting files online makes work FAIR.

---

## Core Workflow
- Define release scope (dataset slice, code commit, parameter set).
- Add machine-readable metadata and provenance fields.
- Validate rerun path in a clean environment.
- Write methods/limitations notes for external users.
- Publish with changelog and deprecation policy.

---

## 60-Minute Run-of-Show
- Bring one analysis you have run, in whatever state it is in. It does not need to be tidy; untidy is more useful here.
- Read Technical Unit 04, section 2, on materialization versions and root-ID instability.
- **00:00-06:00 | Framing: the silent bug**
- Prompt: "Your notebook ran fine last month and gives a different number today. Nothing in your code changed. What happened?"
- Establish that analysis against an unpinned segmentation is the most common silent correctness failure in this field.
- **06:00-16:00 | The five-element checklist, modeled**
- Instructor walks one real analysis through: dataset release ID, materialization number, code commit hash, environment specification, parameter configuration.
- Show what breaks when each one is missing, in turn.
- **16:00-30:00 | Guided practice: audit your own work**
- Learners score their brought-in analysis against the five elements. Most will fail two or three; say so in advance to make that safe.
- Produce a remediation list ordered by how cheap each fix is.
- **30:00-40:00 | Clean-environment rerun**
- Attempt a rerun of a partner's analysis from their instructions alone, without asking them questions.
- Log every point of friction. The friction log is the deliverable, not the successful rerun.
- **40:00-50:00 | Known limitations, written honestly**
- Each learner drafts a limitations paragraph naming concrete failure modes, excluded samples, and failed runs — not generic caveats.
- Discuss why this is a hidden-curriculum norm: reviewers expect it, and almost nobody is taught to write it.
- **50:00-57:00 | Competency check**
- Submit: completed five-element record, friction report on a partner's package, and one limitations paragraph.
- **57:00-60:00 | Exit ticket**
- "One thing in my current work that another person could not reproduce today."
- **At 30 minutes:** every learner has identified at least one missing element in their own work. A learner reporting five out of five has probably not audited honestly — check.
- **At 50 minutes:** limitations paragraphs name specific failure modes rather than generic hedges.

---

## Misconceptions to Watch
- **Misconception guardrail:** posting files online makes work FAIR.
- **Misconception guardrail:** a notebook that ran end-to-end once is proof of reproducible science.
- **Misconception guardrail:** reproducibility norms are common sense that any careful trainee will infer without being taught.

---

## Studio Activity
**Scenario:** Your lab plans to release a connectomics analysis package to collaborators.

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
**Minimum pass**

- All five provenance elements present: dataset release ID, materialization number, code commit hash, environment specification, parameter configuration.
- Re-run instructions testable by a peer without contacting the author.
- Limitations name concrete failure modes, excluded samples, and failed runs rather than generic hedges.

---

## Assessment Rubric
**Strong performance**

- Clean-environment rerun actually attempted, with a friction log and remediations ordered by cost.
- Hidden norms made explicit: version identifiers in figure legends, a changelog, and a deprecation note.
- ID churn quantified whenever identifiers cross versions, and reported in the methods.
- Documentation is audit-friendly: an external reader can locate every provenance element from the README alone.

---

## Assessment Rubric
**Common failure modes**

- Missing version identifiers for data or code.
- Methods that omit key parameters or the environment specification.
- "Reproducible in principle" claims without a validation rerun.
- Limitations sections written as boilerplate rather than as concrete guidance.

---

## Exit Ticket
Take one prior analysis output and add:
1. provenance metadata,
2. reproducibility instructions,
3. a 5-line limitations section.

---

## References (Instructor)
- Wilkinson et al. (2016) - FAIR Guiding Principles.
- Peng (2011) - Reproducible Research in Computational Science.
- Project-specific release documentation for H01/MICrONS/FlyWire.

---

## Teaching Materials
- Module page: /modules/module21/
- Slide page: /modules/slides/module21/
- Worksheet: /assets/worksheets/module21/module21-activity.md
