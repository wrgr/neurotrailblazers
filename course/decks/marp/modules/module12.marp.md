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
Produce a scalable, reproducible query-and-analysis plan for a large connectomics dataset, including storage assumptions, indexing strategy, and provenance capture. Concretely: size a dataset from its imaging parameters before anyone quotes you a price, choose a chunk and shard layout from your actual access pattern rather than from the format everyone else uses, predict which query will dominate your bill, and pin every published number to a segmentation version a stranger can re-query a year from now.

---

## Concept Focus
### 1) Storage layout is chosen by access pattern, not by format popularity
- **Technical:** chunked formats (Zarr, N5, Neuroglancer precomputed) store a volume as independent compressed blocks, commonly 64³ to 256³ voxels. The chunk is the unit of I/O, so you pay for the whole chunk even when you want one plane of it. A 512 x 512 section-plane view touches 4 chunks at 256³ and 64 at 64³, yet moves about 67 MB against about 17 MB, because each 256³ chunk carries z-depth you did not ask for. Anisotropic chunks such as 128 x 128 x 16 improve plane reads and worsen z-traversal. EM compresses 2-10x; label volumes compress far better.
- **Plain language:** the chunk is the smallest thing you can read, so shape it like the reads you will actually do.
- **Misconception guardrail:** the format everyone else uses is automatically the right layout for your access pattern.

---

## Core Workflow
- Write the analysis question as a sentence naming the table, the filter, and the unit of the answer — for example, "count synapses between layer 2/3 pyramidal cells and basket cells, per neuron pair, at cleft score above threshold."
- Estimate the working set: how many rows, how many objects, how many bytes must move, and whether that fits in memory on the machine you have.
- Choose storage and index strategy from the access pattern — chunk shape for volumetric reads, sharding if object counts exceed roughly 10^6, a pre-joined extract if the same join recurs.
- Pin the segmentation: record the materialization version or timestamp, and refuse to proceed if it is unknown.
- Prototype on a 0.1% sample, profile, and extrapolate the full runtime before running it once at full scale.
- Add provenance fields to the output artifact itself, not to the surrounding notebook.
- Validate reproducibility by having a second person re-run the query package from the recorded version and compare row counts and summary statistics.

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
- **Misconception guardrail:** the format everyone else uses is automatically the right layout for your access pattern.
- **Misconception guardrail:** storage cost is the storage line on the invoice.
- **Misconception guardrail:** the dataset size is the petabyte figure quoted for the raw imagery.
- **Misconception guardrail:** an object ID refers to the same neuron next month.
- **Misconception guardrail:** "it runs eventually" is acceptable for iterative science.
- **Misconception guardrail:** notebook history is sufficient provenance.

---

## Studio Activity
**Scenario:** Your team delivers a weekly motif-analysis report from a store holding a ~5 x 10^8-row synapse table, a 120,000-row segment table, and cell-type annotations for about 8,400 neurons. The volume is ~1 mm³, the bytes live in cloud object storage, and your analysis cluster is on-premises. The report is regenerated every Monday and will be cited in a manuscript. Last week's run took nine hours and produced numbers that do not match the report from three weeks ago; nobody knows why.

---

## Activity Output Checklist
- Evidence-linked artifact submitted.
- At least one limitation or uncertainty stated.
- Revision point captured from feedback.

---

## Assessment Rubric
- **Minimum pass**
- Query design matches analysis goal and data shape, with at least one quantitative estimate.
- Provenance requirements are explicit, actionable, and attached to the artifact rather than the notebook.
- Bottlenecks are identified with one realistic mitigation.
- **Strong performance**
- Separates exploratory and production query paths and says which rules apply to each.
- Quantifies tradeoffs across latency, dollar cost, and reproducibility, and names the assumption behind each number.
- Identifies version drift as the first hypothesis for the discrepancy, before code bugs.
- Anticipates failure recovery and rollback needs, including what happens when a materialization is superseded mid-analysis.
- **Common failure modes**
- Index choices disconnected from query workload.
- Missing version metadata in outputs.
- Optimization attempts without a benchmark baseline.
- Sizing that counts only the raw volume and ignores derived products and egress.

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
