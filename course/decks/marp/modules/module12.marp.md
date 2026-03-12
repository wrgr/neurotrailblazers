---
marp: true
theme: default
paginate: true
title: "Module 12: Big Data in Connectomics"
---

# Module 12: Big Data in Connectomics
Teaching Deck

---

## Learning Objectives
- Describe core architecture patterns for petascale connectomics data
- Plan compute, storage, and indexing strategies for large EM volumes
- Implement query workflows that preserve provenance and reproducibility
- Identify bottlenecks and failure modes in large-scale analysis pipelines

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
Produce a scalable, reproducible query-and-analysis plan for a large connectomics dataset, including storage assumptions, indexing strategy, and provenance capture.

---

## Concept Focus
### 1) Data architecture is scientific method infrastructure
- **Technical:** storage format, chunking, and indexing influence what questions are tractable.
- **Plain language:** bad architecture can make good science impossible.
- **Misconception guardrail:** compute scale alone does not solve poor data design.

---

## Core Workflow
- See module page for details.

---

## 60-Minute Run-of-Show
- **00:00-08:00 | Architecture framing and failure examples**
- **08:00-20:00 | Access-pattern to index mapping exercise**
- **20:00-34:00 | Query profiling and bottleneck diagnosis**
- **34:00-46:00 | Provenance logging implementation**
- **46:00-56:00 | Team review of reproducibility gaps**
- **56:00-60:00 | Competency check and next-step assignment**

---

## Misconceptions to Watch
- **Misconception guardrail:** compute scale alone does not solve poor data design.
- **Misconception guardrail:** "it runs eventually" is not acceptable for iterative science.
- **Misconception guardrail:** notebook history alone is insufficient provenance.

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
- Query design matches analysis goal and data shape.
- Provenance requirements are explicit and actionable.
- Bottlenecks are identified with one realistic mitigation.
- **Strong performance**
- Separates exploratory and production query paths.
- Quantifies tradeoffs (latency, cost, reproducibility).
- Anticipates failure recovery and rollback needs.
- **Common failure modes**
- Index choices disconnected from query workload.
- Missing version metadata in outputs.
- Optimization attempts without benchmark baseline.

---

## Exit Ticket
Document one query you use with:
1. data source/version,
2. expected runtime class,
3. one provenance field you currently miss.

---

## References (Instructor)
- H01 human cortical fragment release and infrastructure notes.
- MICrONS data platform documentation.
- Januszewski et al. (2018) for scalable reconstruction context.

---

## Teaching Materials
- Module page: /modules/module12/
- Slide page: /modules/slides/module12/
- Worksheet: /assets/worksheets/module12/module12-activity.md
