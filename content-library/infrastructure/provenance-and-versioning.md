---
layout: page
title: "Provenance and Versioning"
permalink: /content-library/infrastructure/provenance-and-versioning/
image: /assets/images/content-library/infrastructure/provenance-and-versioning.svg
image_alt: "Stylized vector art: pipeline stages running above a chunk grid."
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
tags:
  - infrastructure:provenance
  - infrastructure:versioning
  - infrastructure:cave
  - methodology:reproducibility
  - methodology:data-management
  - connectomics:materialization
micro_lesson_id: ml-infra-provenance
combines_with:
  - reconstruction-pipeline
  - data-formats
  - acquisition-qa
content_type: core
---

## Overview

A connectome changes after release. Proofreaders correct errors, new segmentation models are applied, annotations are added, and analyses reveal regions that need another look. Without version control and provenance tracking you cannot reproduce a published result, diagnose an unexpected finding, or compare analyses run at different times.

This document covers the principles and practical systems for maintaining data lineage in connectomics.

---

## Instructor script: why provenance matters

### The reproducibility challenge

Consider this invented scenario: A paper reports that a specific circuit motif is enriched 3.2× in a fictional mouse cortex volume, release T32. A year later, another group queries the same volume and finds only 1.8× enrichment. Is the difference:

(a) A real scientific disagreement about methods?
(b) A change in the underlying data — proofreading corrections since release T32 altered the graph?
(c) A difference in which version of the synapse detection was used?
(d) A software bug in one of the analyses?

Without provenance, answering this takes detective work and may be impossible. With provenance, you can see which data version, segmentation version and synapse detection version each analysis used, and find where the results diverged.

### The FAIR principle applied to connectomics

Connectomics data should be **F**indable, **A**ccessible, **I**nteroperable, and **R**eusable (Wilkinson et al. 2016). Reuse depends on rich provenance, and provenance is also the backbone of reproducibility:

- **Every analysis result** should cite the exact dataset version used
- **Every dataset version** should record the processing pipeline that created it
- **Every processing pipeline** should record its code version, model version, and parameters
- **Every proofreading edit** should record who made it, when, and why

---

## CAVE: Connectome Annotation Versioning Engine

### Core architecture

CAVE (Dorkenwald et al. 2025) is the versioning system behind FlyWire, MICrONS and H01. It provides:

1. **Chunked segmentation graph**: The segmentation is stored as a graph of supervoxels (small, atomically correct fragments). Proofreading edits (merges and splits) are graph operations — adding or removing edges between supervoxels. The segmentation volume itself is never rewritten.

2. **Annotation tables**: Synapses, cell-type labels, and other annotations are stored in database tables with spatial coordinates. Each annotation records which segment it belongs to (via the supervoxel it falls within).

3. **Materialization**: Periodically (on a schedule set for each dataset), CAVE takes a snapshot ("materialization") that freezes the state of the segmentation graph and all annotation tables. A materialization version is a complete, self-consistent view of the connectome at a specific point in time.

### How materialization works

When you "materialize" at version N:
- The segmentation graph is resolved: every supervoxel's current root segment ID is computed by traversing the edit history up to version N.
- All annotations are updated: each annotation's segment ID is recomputed based on the version-N segmentation.
- The result is a table where every synapse, every cell label, and every segment is consistent — as if the entire dataset were re-segmented from scratch with all proofreading edits applied.

Materialization decouples the time of analysis from the time of proofreading. While a materialization version is available, a query against it returns the same results. Versions do not last forever: MICrONS archives most versions after a year or two and keeps a few "major analysis versions" (943 and 1300 for `minnie65_public`) longer. The static exports of a version outlive its live CAVE service.

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

# This query returns the same results for as long as version 943 stays
# available, regardless of subsequent proofreading edits.
# Check client.materialize.get_versions() before relying on a version.
```

### Projects using CAVE

- **FlyWire** (Dorkenwald et al. 2024): the whole adult *Drosophila* brain, 139,255 neurons
- **MICrONS** (`minnie65_public`): about 1 mm³ of mouse visual cortex
- **H01** (Shapson-Coe et al. 2024): about 1 mm³ of human temporal cortex, where CAVE hosts community proofreading

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

**Recommended practice:** Combine all three: a workflow manager for execution tracking, inline metadata for self-describing outputs, and a database for cross-pipeline queries.

---

## Version control for analysis code

### The minimum standard

Every analysis script, notebook, or pipeline used to generate a figure or result in a publication should be:

1. **Under git version control** — with the exact commit hash recorded alongside the result
2. **Dependency-pinned** — exact versions of all libraries (requirements.txt, conda environment.yml, or Docker image hash)
3. **Parameterized** — all parameters (thresholds, random seeds, dataset versions) as explicit configuration, not hardcoded values
4. **Deterministic** — same inputs + same parameters + same code → same outputs. Pin random seeds. Avoid non-deterministic GPU operations (or document them).

### Docker/container reproducibility

To pin the whole environment, package the analysis as a Docker container. The
versions below show the pattern; pin the ones you actually ran (caveclient 8.2.1 was
the latest on PyPI on 26 September 2026):

```dockerfile
FROM python:3.11-slim
RUN pip install caveclient==5.14.0 networkx==3.2.1 numpy==1.26.2
COPY analysis/ /app/analysis/
ENTRYPOINT ["python", "/app/analysis/run_motif_search.py"]
```

Record the Docker image hash alongside results. Anyone with the image can rebuild the same software environment later. The data is a separate question: the image does not keep a materialization version alive.

---

## Worked example: publishing a reproducible connectomics result

**Scenario:** You're writing a paper on whether reciprocal connections between layer 2/3 pyramidal cells are enriched relative to a degree-preserving null model. The sentences below are templates for wording, not reported results; the dataset, version and table names are real, and the bracketed parts are yours to fill.

**Reproducibility checklist:**

1. **Dataset version:** "All analyses used MICrONS minnie65_public, CAVE materialization version 943 (released January 2024; give the exact timestamp your client reports)."
2. **Cell selection:** "Pyramidal cells identified using cell-type labels from the aibs_metamodel_celltypes_v661 table, version 943."
3. **Synapse source:** "Synapses from the synapses_pni_2 table, materialized at version 943."
4. **Thresholds:** "We defined connected pairs as those with ≥3 synapses (sensitivity analysis for thresholds 1-10 in [supplementary figure])."
5. **Null model:** "Degree-preserving random rewiring (Maslov & Sneppen 2002), 10,000 randomizations, random seed 42."
6. **Code:** "Analysis code available at github.com/lab/reciprocal-motifs, commit abc123."
7. **Environment:** "Docker image lab/reciprocal-motifs:v1.0, sha256:def456."

With this information, anyone who can still reach version 943 or its static export can reproduce the result. Drop any one element and they cannot.

---

## Common misconceptions

| Misconception | Reality | Teaching note |
|---|---|---|
| "The connectome is finished" | Proofreading and annotation continue after release, often for years | Always cite a specific version |
| "Git for code is enough" | Code version means nothing without data version and environment version | Track all three together |
| "Provenance is overhead" | Provenance prevents far more expensive problems: irreproducible results, retracted papers, wasted re-analysis | Build it into the pipeline from day one |
| "We can always re-run the analysis" | If the data version has changed and you didn't record which version you used, re-running gives different results | Pin versions at analysis time, not after |

---

## References

- Dorkenwald S et al. (2025) "CAVE: Connectome Annotation Versioning Engine." *Nature Methods* 22:1112-1120. doi:10.1038/s41592-024-02426-z.
- Dorkenwald S et al. (2024) "Neuronal wiring diagram of an adult brain." *Nature* 634:124-138.
- Wilkinson MD et al. (2016) "The FAIR Guiding Principles for scientific data management and stewardship." *Scientific Data* 3:160018.
- Maslov S, Sneppen K (2002) "Specificity and stability in topology of protein networks." *Science* 296(5569):910-913.
- Turner NL et al. (2022) "Reconstruction of neocortex: Organelles, compartments, cells, circuits, and activity." *Cell* 185(6):1082-1100.
