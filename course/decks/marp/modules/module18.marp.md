---
marp: true
theme: default
paginate: true
title: "Module 18: Data Cleaning and Preprocessing"
---

# Module 18: Data Cleaning and Preprocessing
Teaching Deck

---

## Learning Objectives
- Diagnose common connectomics data-quality issues before analysis
- Apply reproducible preprocessing steps with documented decision rules
- Quantify preprocessing impact with auditable QC metrics
- Produce an analysis-ready dataset package with provenance metadata

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
Produce a reproducible preprocessing release that transforms raw or intermediate connectomics outputs into analysis-ready data, with explicit quality gates and full provenance.

---

## Concept Focus
### 1) Cleaning vs distortion
- **Technical:** preprocessing should reduce known artifacts/noise while preserving biologically meaningful structure.
- **Plain language:** fix mistakes, do not "polish away" the biology.
- **Misconception guardrail:** more filtering is not always better.

---

## Core Workflow
- See module page for details.

---

## 60-Minute Run-of-Show
- One noisy connectomics table (missing values, duplicated IDs, inconsistent units).
- Shared preprocessing decision sheet.
- QC dashboard template (pre/post metrics).
- **00:00-08:00 | Setup and target**
- Define release objective and non-negotiable quality gates.
- **08:00-18:00 | Instructor modeling**
- Live demonstration of ingest checks and anomaly triage logic.
- **18:00-32:00 | Team preprocessing design**
- Teams draft cleaning rules and escalation criteria.
- **32:00-44:00 | QC pass**
- Teams compute/estimate pre-post metrics and decide release/no-release.
- **44:00-54:00 | Cross-team review**
- Teams audit each other's transform logs for reproducibility gaps.
- **54:00-60:00 | Competency checkpoint**
- Submit one release note with provenance, thresholds, and residual risk.
- Cleaning decisions are deterministic and documented.
- QC thresholds are tied to operational actions.
- Release note exposes at least one unresolved interpretation risk.

---

## Misconceptions to Watch
- **Misconception guardrail:** more filtering is not always better.
- **Misconception guardrail:** version-control notes alone are insufficient without data lineage.
- **Misconception guardrail:** reporting metrics without thresholds is not quality control.

---

## Studio Activity


---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
- **Minimum pass**
- Cleaning decisions are explicit and reproducible.
- QC metrics include thresholds tied to actions.
- Release package includes provenance metadata.
- **Strong performance**
- Distinguishes low-risk cleanup from biologically sensitive transforms.
- Quantifies and explains pre/post changes clearly.
- Documents limitations and unresolved risks transparently.
- **Common failure modes**
- Silent ad-hoc edits with no transform log.
- Aggressive filtering that removes biologically meaningful variation.
- Metrics reported without operational thresholds.

---

## Exit Ticket
Take one connectomics table (real or mock) and write:
1. Three cleaning rules with rationale.
2. Two QC thresholds and associated actions.
3. One limitation that remains after preprocessing.

---

## References (Instructor)
- Wilkinson et al., 2016. The FAIR Guiding Principles for scientific data management and stewardship.
- Peng, 2011. Reproducible Research in Computational Science.
- MICrONS and related connectomics workflow documentation.

---

## Teaching Materials
- Module page: /modules/module18/
- Slide page: /modules/slides/module18/
- Worksheet: /assets/worksheets/module18/module18-activity.md
