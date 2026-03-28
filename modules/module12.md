---
title: "Module 12: Big Data in Connectomics"
layout: module
permalink: /modules/module12/
description: "Design scalable data storage, querying, and analysis workflows for petascale connectomics datasets."
module_number: 12
difficulty: "Advanced"
duration: "4-5 hours"
learning_objectives:
  - "Describe core architecture patterns for petascale connectomics data"
  - "Plan compute, storage, and indexing strategies for large EM volumes"
  - "Implement query workflows that preserve provenance and reproducibility"
  - "Identify bottlenecks and failure modes in large-scale analysis pipelines"
prerequisites: "Modules 1-11, Python and basic data engineering familiarity"
merit_stage: "Analysis"
compass_skills:
  - "Systems Reasoning"
  - "Data Engineering"
  - "Reproducibility"
ccr_focus:
  - "Knowledge - Large-Scale Data Systems"
  - "Skills - Scalable Analysis"

# Normalized metadata
slug: "module12"
short_title: "Big Data in Connectomics"
status: "active"
audience:
  - "students"
pipeline_stage: "Analysis"
merit_row_focus: "Analysis"
topics:
  - "big-data"
  - "infrastructure"
  - "query-systems"
summary: "Scalable storage, indexing, and reproducible query design for connectomics datasets."
key_questions:
  - "How do we architect data systems for petascale connectomics?"
  - "Which indexing/query decisions drive analysis speed and reliability?"
  - "How do we preserve provenance at scale?"
slides:
  - "/assets/slides/module12/module12-big-data-in-connectomics.pdf"
notebook:
  - "/assets/notebooks/module12/module12-big-data-in-connectomics.ipynb"
  - "/notebooks/intro/DashSynapseExplorer.ipynb"
datasets:
  - "/datasets/mouseconnects"
  - "/datasets/workflow"
personas:
  - "/avatars/gradstudent"
  - "/avatars/researcher"
  - "/avatars/mentor"
related_tools:
  - "/tools/connectome-quality/"
  - "/tools/ask-an-expert/"
related_frameworks:
  - "research-incubator-model"
  - "education-models"
prerequisites_list:
  - "Basic SQL/Python dataframe proficiency"
  - "Familiarity with EM volume structure"
next_modules:
  - "module13"
  - "module14"
references:
  - "H01 human cortical fragment release and infrastructure notes."
  - "MICrONS data platform documentation."
  - "Januszewski et al. (2018) for scalable reconstruction context."
videos: []
downloads:
  - "/notebooks/intro/DashSynapseExplorer.ipynb"
last_reviewed: 2026-03-11
maintainer: "NeuroTrailblazers Team"
---

## Capability target
Produce a scalable, reproducible query-and-analysis plan for a large connectomics dataset, including storage assumptions, indexing strategy, and provenance capture.

## Why this module matters
Connectomics is now data-system-limited as much as algorithm-limited. If learners cannot reason about throughput, storage, and indexing, they cannot execute reliable analyses on real datasets.

## Concept set
### 1) Data architecture is scientific method infrastructure
- **Technical:** storage format, chunking, and indexing influence what questions are tractable.
- **Plain language:** bad architecture can make good science impossible.
- **Misconception guardrail:** compute scale alone does not solve poor data design.

### 2) Query cost is a research variable
- **Technical:** query plans and index locality affect reproducibility, latency, and iteration speed.
- **Plain language:** how you ask the data matters as much as what you ask.
- **Misconception guardrail:** "it runs eventually" is not acceptable for iterative science.

### 3) Provenance must be first-class
- **Technical:** every output should include dataset version, query definition, environment, and transform lineage.
- **Plain language:** if you cannot reconstruct your output path, you cannot defend your result.
- **Misconception guardrail:** notebook history alone is insufficient provenance.

## Hidden curriculum scaffold
- Unwritten engineering expectations in connectomics teams:
  - benchmark before optimizing.
  - record query versions for every figure table.
  - separate exploratory scripts from release pipelines.
- How to teach explicitly:
  - require query provenance fields in assignments.
  - include failure-postmortem mini-reviews.
  - grade reproducibility alongside correctness.

## Core workflow: scalable query planning
1. Define analysis question and required data granularity.
2. Select storage/index strategy aligned to access pattern.
3. Prototype baseline query and profile bottlenecks.
4. Add provenance logging and version controls.
5. Validate reproducibility and publish query package.

## 60-minute tutorial run-of-show
1. **00:00-08:00 | Architecture framing and failure examples**
2. **08:00-20:00 | Access-pattern to index mapping exercise**
3. **20:00-34:00 | Query profiling and bottleneck diagnosis**
4. **34:00-46:00 | Provenance logging implementation**
5. **46:00-56:00 | Team review of reproducibility gaps**
6. **56:00-60:00 | Competency check and next-step assignment**

## Studio activity: petascale query design lab
**Scenario:** Your team must deliver a weekly motif-analysis report from a multi-terabyte connectomics store.

**Tasks**
1. Propose storage/index layout for expected query patterns.
2. Write or outline two critical queries and estimate performance risk.
3. Define minimum provenance fields for outputs.
4. Produce one optimization proposal and one reproducibility safeguard.

**Expected outputs**
- Query architecture sketch.
- Baseline vs optimized query plan.
- Provenance checklist.

## Assessment rubric
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

## Scale context: real-world numbers

To ground the abstract concepts, here are the data scales learners will encounter:

| Dataset | Raw volume | Neurons | Synapses | Storage |
|---------|-----------|---------|----------|---------|
| MICrONS (minnie65) | 1 mm³ mouse V1 | ~80,000 | ~500M | ~2 PB |
| H01 | ~1 mm³ human temporal cortex | ~57,000 cells | ~150M | ~1.4 PB |
| FlyWire | Whole adult Drosophila brain | ~139,255 | ~54.5M | ~100 TB |
| MouseConnects (planned) | ~10 mm³ mouse hippocampus | TBD | TBD | >10 PB |

**Teaching point:** "When your synapse table has 500 million rows, a poorly written query doesn't just run slowly — it may not finish at all. Architecture decisions determine whether your science is feasible."

## Key tools and formats

| Tool/Format | Purpose | When to use |
|------------|---------|-------------|
| **Zarr/N5** | Chunked array storage | Volumetric data, cloud-friendly |
| **Neuroglancer precomputed** | Multiscale image pyramids | Web browsing of EM/segmentation |
| **CAVEclient** | Python API for CAVE tables | Synapse queries, annotation access |
| **CloudVolume** | Python API for volumetric data | Image/segmentation chunk access |
| **pandas/Dask** | Tabular data manipulation | Synapse tables, annotation analysis |
| **BigQuery/DuckDB** | SQL on large tables | Complex joins on synapse/annotation tables |

## Content library references
- [Reconstruction pipeline]({{ '/content-library/infrastructure/reconstruction-pipeline/' | relative_url }}) — End-to-end pipeline architecture
- [Data formats and representations]({{ '/content-library/infrastructure/data-formats/' | relative_url }}) — Volumes, meshes, skeletons, graphs; format specs
- [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}) — CAVE materialization, reproducibility
- [MICrONS visual cortex]({{ '/content-library/case-studies/microns-visual-cortex/' | relative_url }}) — Real-world petascale dataset

## Teaching resources
- Workflow context: [Connectomics Workflow]({{ '/datasets/workflow' | relative_url }})
- Dataset context: [MouseConnects]({{ '/datasets/mouseconnects' | relative_url }})
- Notebook: [Dash Synapse Explorer]({{ '/notebooks/intro/DashSynapseExplorer.ipynb' | relative_url }})
- Quality context: [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})

## References
- Dorkenwald S et al. (2022) "CAVE: Connectome Annotation Versioning Engine." *bioRxiv*.
- Januszewski M et al. (2018) "High-precision automated reconstruction of neurons with flood-filling networks." *Nature Methods* 15(8):605-610.
- Shapson-Coe A et al. (2024) "A petavoxel fragment of human cerebral cortex." *Science* 384(6696):eadk4858.
- Turner NL et al. (2022) "Reconstruction of neocortex." *Cell* 185(6):1082-1100.

## Quick practice prompt
Document one query you use with:
1. data source/version,
2. expected runtime class,
3. one provenance field you currently miss.
