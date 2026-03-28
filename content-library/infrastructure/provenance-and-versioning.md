---
layout: page
title: "Provenance and Versioning"
permalink: /content-library/infrastructure/provenance-and-versioning/
description: "Data lineage, version control, and reproducibility infrastructure for connectomics — CAVE materialization, pipeline provenance, and best practices for traceable science."
topics:
  - provenance
  - versioning
  - reproducibility
  - CAVE
  - materialization
primary_units:
  - "04"
  - "08"
difficulty: "Advanced"
---

## Overview

A connectome is not a static object. It evolves continuously as proofreaders correct errors, new segmentation models are applied, annotations are added, and analyses reveal regions needing further review. Without rigorous version control and provenance tracking, it becomes impossible to reproduce a published result, diagnose an unexpected finding, or compare analyses performed at different times.

This document covers the principles and practical systems for maintaining data lineage in connectomics.

---

## Instructor script: why provenance matters

### The reproducibility challenge

Consider this scenario: A paper published in 2024 reports that a specific circuit motif is enriched 3.2× in mouse visual cortex. In 2025, another group queries the same dataset and finds only 1.8× enrichment. Is the difference:

(a) A real scientific disagreement about methods?
(b) A change in the underlying data — proofreading corrections since 2024 altered the graph?
(c) A difference in which version of the synapse detection was used?
(d) A software bug in one of the analyses?

Without provenance, answering this question requires extensive detective work. With provenance, you can immediately identify which data version, segmentation version, and synapse detection version each analysis used, and pinpoint where results diverged.

### The FAIR principle applied to connectomics

Connectomics data should be **F**indable, **A**ccessible, **I**nteroperable, and **R**eproducible (Wilkinson et al. 2016). Provenance is the backbone of reproducibility:

- **Every analysis result** should cite the exact dataset version used
- **Every dataset version** should record the processing pipeline that created it
- **Every processing pipeline** should record its code version, model version, and parameters
- **Every proofreading edit** should record who made it, when, and why

---

## CAVE: Connectome Annotation Versioning Engine

### Core architecture

CAVE (Dorkenwald et al. 2022) is the most widely used versioning system for large-scale connectomics. It provides:

1. **Chunked segmentation graph**: The segmentation is stored as a graph of supervoxels (small, atomically correct fragments). Proofreading edits (merges and splits) are graph operations — adding or removing edges between supervoxels. The segmentation volume itself is never rewritten.

2. **Annotation tables**: Synapses, cell-type labels, and other annotations are stored in database tables with spatial coordinates. Each annotation records which segment it belongs to (via the supervoxel it falls within).

3. **Materialization**: Periodically (daily to weekly), CAVE takes a snapshot ("materialization") that freezes the state of the segmentation graph and all annotation tables. A materialization version is a complete, self-consistent view of the connectome at a specific point in time.

### How materialization works

When you "materialize" at version N:
- The segmentation graph is resolved: every supervoxel's current root segment ID is computed by traversing the edit history up to version N.
- All annotations are updated: each annotation's segment ID is recomputed based on the version-N segmentation.
- The result is a table where every synapse, every cell label, and every segment is consistent — as if the entire dataset were re-segmented from scratch with all proofreading edits applied.

**Key insight:** Materialization decouples the time of analysis from the time of proofreading. You can always go back to a specific materialization version and get the exact same results.

### Practical usage

```
# Pseudocode for reproducible analysis
client = CAVEclient("minnie65_public")

# Pin to a specific materialization version
mat_version = 943  # the version used in my paper

# Query the connectivity graph at that exact version
synapses = client.materialize.synapse_query(
    pre_ids=[my_neuron_id],
    materialization_version=mat_version
)

# This query will return the same results today, tomorrow, and in 5 years
# regardless of subsequent proofreading edits
```

### Projects using CAVE

- **FlyWire** (Dorkenwald et al. 2024): Entire Drosophila brain, ~140K neurons
- **MICrONS** (minnie65, minnie35): Mouse visual cortex volumes
- **Allen Institute** datasets: Multiple mouse brain regions

---

## Pipeline provenance

### What to record at each stage

For every computational step in the reconstruction pipeline:

| Stage | Required provenance |
|-------|-------------------|
| **Raw ingest** | Microscope instrument ID, acquisition date, operator, imaging parameters (see acquisition-qa.md) |
| **Alignment** | Input section IDs, alignment software version (git hash), transform parameters, registration residuals |
| **Segmentation** | Input volume version, model artifact ID (hash of trained weights), inference parameters (threshold, chunk size), software version |
| **Agglomeration** | Segmentation version, agglomeration parameters (size threshold, affinity threshold), software version |
| **Synapse detection** | Input volume + segmentation version, synapse model ID, detection parameters, software version |
| **Proofreading** | Editor ID, timestamp, operation type (merge/split), affected supervoxels, before/after state |
| **Analysis** | All input data versions (materialization number), analysis code version, parameters, random seeds |

### Implementation patterns

**Option 1: Inline metadata** — Each output file/chunk carries its provenance as attributes (HDF5 attributes, Zarr metadata, JSON sidecar files). Simple but can become unwieldy for complex pipelines.

**Option 2: Provenance database** — A central database records every processing step with inputs, outputs, parameters, and timestamps. Query-friendly but requires infrastructure.

**Option 3: Workflow managers** — Tools like Nextflow, Snakemake, or Airflow automatically track input/output dependencies and record execution metadata. Best for reproducible pipeline execution.

**Recommended practice:** Combine all three. Workflow manager for execution tracking, inline metadata for self-describing outputs, and a database for cross-pipeline queries.

---

## Version control for analysis code

### The minimum standard

Every analysis script, notebook, or pipeline used to generate a figure or result in a publication should be:

1. **Under git version control** — with the exact commit hash recorded alongside the result
2. **Dependency-pinned** — exact versions of all libraries (requirements.txt, conda environment.yml, or Docker image hash)
3. **Parameterized** — all parameters (thresholds, random seeds, dataset versions) as explicit configuration, not hardcoded values
4. **Deterministic** — same inputs + same parameters + same code → same outputs. Pin random seeds. Avoid non-deterministic GPU operations (or document them).

### Docker/container reproducibility

For maximum reproducibility, package the entire analysis environment as a Docker container:

```dockerfile
FROM python:3.11-slim
RUN pip install caveclient==5.15.0 networkx==3.2.1 numpy==1.26.2
COPY analysis/ /app/analysis/
ENTRYPOINT ["python", "/app/analysis/run_motif_search.py"]
```

Record the Docker image hash alongside results. Anyone can re-run the analysis years later with the exact same environment.

---

## Worked example: publishing a reproducible connectomics result

**Scenario:** You're writing a paper showing that reciprocal connections between layer 2/3 pyramidal cells are 4.2× enriched relative to a degree-preserving null model.

**Reproducibility checklist:**

1. **Dataset version:** "All analyses used MICrONS minnie65_public, CAVE materialization version 943 (2025-01-15)."
2. **Cell selection:** "Pyramidal cells identified using cell-type labels from the minnie65_public nucleus detection table, version 943."
3. **Synapse source:** "Synapses from the synapses_pni_2 table, materialized at version 943."
4. **Thresholds:** "We defined connected pairs as those with ≥3 synapses (sensitivity analysis for thresholds 1-10 in Supplementary Figure S3)."
5. **Null model:** "Degree-preserving random rewiring (Maslov & Sneppen 2002), 10,000 randomizations, random seed 42."
6. **Code:** "Analysis code available at github.com/lab/reciprocal-motifs, commit abc123."
7. **Environment:** "Docker image lab/reciprocal-motifs:v1.0, sha256:def456."

With this information, anyone can reproduce the exact result. Without any single element, reproducibility is compromised.

---

## Common misconceptions

| Misconception | Reality | Teaching note |
|---|---|---|
| "The connectome is finished" | Connectomes are living datasets — proofreading and annotation continue indefinitely | Always cite a specific version |
| "Git for code is enough" | Code version means nothing without data version and environment version | Track all three together |
| "Provenance is overhead" | Provenance prevents far more expensive problems: irreproducible results, retracted papers, wasted re-analysis | Build it into the pipeline from day one |
| "We can always re-run the analysis" | If the data version has changed and you didn't record which version you used, re-running gives different results | Pin versions at analysis time, not after |

---

## References

- Dorkenwald S et al. (2022) "CAVE: Connectome Annotation Versioning Engine." *bioRxiv*. doi:10.1101/2023.07.26.550598.
- Dorkenwald S et al. (2024) "Neuronal wiring diagram of an adult brain." *Nature* 634:124-138.
- Wilkinson MD et al. (2016) "The FAIR Guiding Principles for scientific data management and stewardship." *Scientific Data* 3:160018.
- Maslov S, Sneppen K (2002) "Specificity and stability in topology of protein networks." *Science* 296(5569):910-913.
- Turner NL et al. (2022) "Reconstruction of neocortex: Organelles, compartments, cells, circuits, and activity." *Cell* 185(6):1082-1100.
