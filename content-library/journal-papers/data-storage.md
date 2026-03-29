---
layout: page
title: "Journal Papers: Data Storage & Pipelines"
permalink: /content-library/journal-papers/data-storage/
description: "Curated papers on connectomics data management, annotation systems, file formats, and pipeline engineering, with summaries at beginner, intermediate, and advanced levels."
dimension: data-storage
tags:
  - data-storage:pipeline
  - data-storage:CAVE
  - data-storage:neuroglancer
  - data-storage:data-format
  - data-storage:provenance
  - data-storage:cloud-storage
---

# Data Storage & Pipelines Journal Papers

Curated papers on connectomics data management, annotation systems, file formats, versioning infrastructure, and pipeline engineering. Each paper includes summaries at three expertise levels.

---

## 1. Dorkenwald et al. (2023) — CAVE: Connectome Annotation Versioning Engine

**Citation:** Dorkenwald S, McKellar CE, Macrina T, Kemnitz N, Lee K, Lu R, et al. CAVE: Connectome Annotation Versioning Engine. *bioRxiv*. 2023.
**DOI:** [10.1101/2023.07.26.550598](https://doi.org/10.1101/2023.07.26.550598)

**Tags:** `data-storage:CAVE` `data-storage:provenance` `data-storage:versioning` `data-storage:pipeline` `proofreading:proofreading-tools` `methodology:reproducibility`

### Summaries

**Beginner:** When hundreds of people are correcting a brain map at the same time, you need a system to keep track of every change — who fixed what, when, and why. CAVE is like a version control system (similar to Google Docs' history or Git for code) but designed specifically for connectomics. It lets researchers go back to any previous version of the brain map and ensures that published analyses can always be reproduced.

**Intermediate:** CAVE provides a versioned, materialized annotation infrastructure for large-scale connectomics. It tracks the complete history of proofreading edits (merges, splits) and spatial annotations (synapse labels, cell types) in a chunked graph structure that supports efficient historical queries. "Materialization" produces timestamped snapshots that freeze a consistent state of the connectome for analysis and publication. CAVE powers both the FlyWire and MICrONS annotation systems.

**Advanced:** CAVE's architecture solves the reproducibility crisis in collaborative connectomics: when thousands of users continuously edit a shared segmentation, any analysis must be tied to a specific materialization timestamp to be reproducible. The chunked graph representation enables O(1) edit operations (rather than full-graph recomputation), the materialization pipeline produces denormalized tables for fast analytical queries, and the versioning system maintains complete edit provenance. Key design decisions include the separation of segmentation graph structure from spatial annotations, the use of supervoxel-level granularity for undo operations, and the CAVE client API that abstracts version management for downstream analysts.

**Key figures:** Fig. 1 (CAVE architecture), Fig. 2 (materialization pipeline), Fig. 3 (edit history and provenance)

**Discussion prompts:**
- How does CAVE's versioning model compare to general-purpose version control (Git)? What features are specific to the spatial nature of connectomics data?
- What happens to published analyses when new proofreading edits change the connectome after publication?
- How should citation practices evolve to reference specific CAVE materializations?

**Related content:** [Provenance and versioning](/content-library/infrastructure/provenance-and-versioning/), [Proofreading tools](/content-library/proofreading/proofreading-tools/)

---

## 2. Macrina et al. (2021) — Petascale Neural Circuit Reconstruction: Automated Methods

**Citation:** Macrina T, Lee K, Lu R, Turner NL, Wu J, Popovych S, et al. Petascale neural circuit reconstruction: automated methods. *bioRxiv*. 2021.
**DOI:** [10.1101/2021.08.04.455162](https://doi.org/10.1101/2021.08.04.455162)

**Tags:** `data-storage:pipeline` `data-storage:data-format` `data-storage:cloud-storage` `case-studies:MICrONS` `infrastructure:alignment` `methodology:benchmark`

### Summaries

**Beginner:** Turning a million electron microscopy images into a wiring diagram of the brain requires a massive computational pipeline — like a factory assembly line for data. This paper describes the complete pipeline used for the MICrONS project: aligning images, finding neuron boundaries, stitching neurons across sections, detecting synapses, and packaging everything for analysis. It is the engineering blueprint for modern large-scale connectomics data processing.

**Intermediate:** Macrina et al. describe the full automated reconstruction pipeline for the MICrONS cubic-millimeter cortical volume. From a data-engineering perspective, the paper details how ~2 petabytes of raw imagery are ingested, aligned (cross-section and cross-slab registration), processed through affinity-based segmentation and supervoxel agglomeration, and then stored and indexed for downstream analysis. The pipeline's orchestration across cloud compute resources, the intermediate data representations at each stage, and the quality-control checkpoints provide a reference architecture for petascale neuroscience data processing.

**Advanced:** This paper is the definitive systems-engineering reference for petascale connectomics pipelines. From a data-management standpoint, key contributions include: the multi-resolution alignment approach with its intermediate storage of displacement fields; the cloud-based orchestration that managed millions of GPU-hours of computation; the intermediate data representations (affinity maps, supervoxel graphs, agglomeration tables) and their storage formats; and the pipeline's stage-by-stage quality metrics that enable systematic debugging. The honest accounting of computational costs provides essential data for capacity planning of future large-volume projects. The pipeline's output feeds directly into CAVE for versioned annotation management.

**Key figures:** Fig. 1 (pipeline overview and data flow), Fig. 3 (segmentation quality checkpoints), Fig. 7 (error rate analysis across pipeline stages)

**Discussion prompts:**
- How do the intermediate data representations at each pipeline stage affect storage requirements and downstream reprocessing flexibility?
- What would a cost-optimal cloud architecture look like for running this pipeline today?
- How do the computational costs scale with volume size, and where are the bottlenecks?

**Related content:** [MICrONS visual cortex](/content-library/case-studies/microns-visual-cortex/), [Data formats](/content-library/infrastructure/data-formats/), [CAVE paper (this page, #1)](#1-dorkenwald-et-al-2023--cave-connectome-annotation-versioning-engine)

---

## 3. Scheffer et al. (2020) — A Connectome and Analysis of the Adult Drosophila Central Brain

**Citation:** Scheffer LK, Xu CS, Januszewski M, Lu Z, Takemura SY, Hayworth KJ, et al. A connectome and analysis of the adult *Drosophila* central brain. *eLife*. 2020;9:e57443.
**DOI:** [10.7554/eLife.57443](https://doi.org/10.7554/eLife.57443)

**Tags:** `data-storage:pipeline` `data-storage:data-format` `case-studies:Drosophila` `data-storage:neuroglancer` `proofreading:proofreading-strategy`

### Summaries

**Beginner:** This paper describes the "hemibrain" — a map of about half the fruit fly brain, containing roughly 25,000 neurons and 20 million synaptic connections. Beyond the biological results, the paper is a landmark in connectomics data management: the entire dataset was made publicly available through the neuPrint database, allowing anyone to query the connectome. The data release strategy and tooling set the standard for open connectomics data sharing.

**Intermediate:** Scheffer et al. present the hemibrain connectome from a FIB-SEM volume of *Drosophila* central brain at 8 nm isotropic resolution. From a data infrastructure perspective, the paper demonstrates the end-to-end pipeline from FIB-SEM acquisition through FFN-based segmentation, extensive proofreading (~50 person-years), synapse detection, and neuron type assignment. The dataset release via neuPrint — with structured metadata, graph query capabilities, and programmatic access — established a template for how large connectomics datasets should be packaged and shared with the community.

**Advanced:** The hemibrain project's data infrastructure decisions have had lasting impact. The proofreading strategy prioritized neurons by downstream analytical importance rather than spatial completeness, requiring a metadata framework to track per-neuron confidence scores. The neuPrint graph database representation encodes neurons as nodes and weighted connections as edges, enabling Cypher-based queries that support both exploratory analysis and systematic circuit enumeration. The dataset's size (~25k neurons, ~20M synapses) pushed the boundaries of what could be served through a web-accessible query interface. Limitations from a data perspective include boundary effects (incomplete neurons at volume edges) and heterogeneous proofreading completeness across brain regions, both of which require careful metadata annotation.

**Key figures:** Fig. 1 (hemibrain volume and data pipeline), Fig. 3 (reconstruction quality metrics), Fig. 5 (connectivity data organization)

**Discussion prompts:**
- How does the neuPrint graph database design affect which biological questions are easy vs. hard to answer?
- What metadata standards are needed to communicate reconstruction completeness and confidence to downstream users?
- How should data releases handle the tension between early access and quality assurance?

**Related content:** [FlyWire whole-brain](/content-library/case-studies/flywire-whole-brain/), [neuPrint paper (this page, #5)](#5-clements-et-al-2020--neuprint-an-open-access-tool-for-em-connectome-analysis)

---

## 4. Berger et al. (2018) — VAST: Volume Annotation and Segmentation Tool

**Citation:** Berger DR, Seung HS, Lichtman JW. VAST (Volume Annotation and Segmentation Tool): Efficient manual and semi-automatic labeling of large 3D image stacks. *Frontiers in Neural Circuits*. 2018;12:88.
**DOI:** [10.3389/fncir.2018.00088](https://doi.org/10.3389/fncir.2018.00088)

**Tags:** `data-storage:neuroglancer` `data-storage:data-format` `proofreading:proofreading-tools` `methodology:ground-truth`

### Summaries

**Beginner:** Before you can train a computer to find neurons in images, humans need to manually label example images to create "ground truth" data. VAST is a desktop tool designed for this manual labeling work. It lets annotators paint over neurons in 3D image stacks, assign labels, and track their work efficiently. Good annotation tools are the foundation of every connectomics data pipeline.

**Intermediate:** VAST provides a desktop annotation environment optimized for large-scale manual and semi-automatic segmentation of EM volumes. Features include multi-resolution rendering, efficient label management for thousands of objects, undo/redo with full history, and export to standard formats (TIFF stacks, HDF5). VAST was used to produce ground truth annotations for several landmark datasets including Kasthuri et al. (2015). Its design emphasizes annotation throughput and data consistency for creating training data.

**Advanced:** While cloud-based tools (Neuroglancer, CAVE) now dominate production proofreading workflows, VAST remains relevant for ground truth creation where precise manual control and deterministic performance are needed. The tool's architecture — local rendering with on-disk storage rather than cloud streaming — provides consistent performance independent of network conditions and avoids cloud storage costs for iterative annotation work. Its paint-based annotation model (rather than supervoxel-based editing) is well-suited for creating dense ground truth that does not inherit biases from automated pre-segmentation. For benchmark creation and segmentation validation, VAST's pixel-precise annotations remain the gold standard. The tool's data export formats (TIFF, HDF5) interface cleanly with standard training pipelines.

**Key figures:** Fig. 1 (VAST interface and annotation modes), Fig. 2 (annotation workflow), Fig. 4 (ground truth output examples)

**Discussion prompts:**
- When should you use desktop tools (VAST) versus cloud tools (Neuroglancer/CAVE) for annotation work?
- How does the choice of annotation tool and its data format affect the quality and biases of ground truth data?
- What data format considerations arise when moving annotations between local and cloud-based systems?

**Related content:** [Proofreading tools](/content-library/proofreading/proofreading-tools/), [Metrics and QA](/content-library/proofreading/metrics-and-qa/)

---

## 5. Clements et al. (2020) — neuPrint: An Open Access Tool for EM Connectome Analysis

**Citation:** Clements J, Dolafi T, Umayam L, Neubarth NL, Berg S, Scheffer LK, Plaza SM. neuPrint: Analysis tools for EM connectomics. *bioRxiv*. 2020.
**DOI:** [10.1101/2020.01.16.909465](https://doi.org/10.1101/2020.01.16.909465)

**Tags:** `data-storage:CAVE` `data-storage:neuroglancer` `data-storage:data-format` `data-storage:cloud-storage` `connectomics:graph-theory`

### Summaries

**Beginner:** Once you have a brain wiring diagram with tens of thousands of neurons, you need a way to search through it and ask questions like "which neurons connect to this one?" neuPrint is a database and web interface that lets researchers explore connectome data without writing complex code. It stores neurons, their connections, and metadata in a graph database that supports powerful queries through a simple interface.

**Intermediate:** neuPrint provides a Neo4j-based graph database and web interface for querying and exploring connectome data. Neurons are represented as nodes with properties (type, size, brain region) and connections as weighted edges (synapse counts). The system supports Cypher queries for complex graph traversals, prebuilt "find neurons" and "find connections" interfaces for common operations, and a plugin architecture for custom analyses. neuPrint serves as the primary data access layer for the hemibrain and other HHMI Janelia connectome datasets.

**Advanced:** neuPrint's design reflects deliberate tradeoffs in connectomics data representation. The choice of a property graph model (Neo4j) over a relational or RDF model enables flexible schema evolution as new annotation types are added, but requires careful index management for performant queries on graphs with millions of edges. The system's "ROI" (region of interest) intersection weights on edges enable brain-region-specific connectivity analysis without spatial queries. The REST API and Python client (neuprint-python) support programmatic access for batch analyses. Key architectural decisions include the materialization of synapse counts as edge weights (trading storage for query speed), the hierarchical ROI system, and the separation of the query engine from visualization (delegated to Neuroglancer). Scalability limitations become apparent with whole-brain datasets where the full graph exceeds single-server memory.

**Key figures:** Fig. 1 (neuPrint architecture and data model), Fig. 2 (web interface for neuron queries), Fig. 3 (Cypher query examples and results)

**Discussion prompts:**
- What are the tradeoffs of a graph database versus a relational database for connectomics data?
- How does neuPrint's data model handle the evolution of neuron type classifications over time?
- What query patterns are easy vs. difficult in neuPrint's current architecture?

**Related content:** [Hemibrain paper (this page, #3)](#3-scheffer-et-al-2020--a-connectome-and-analysis-of-the-adult-drosophila-central-brain), [Graph analysis](/content-library/connectomics/graph-analysis/)

---

## 6. Saalfeld et al. (2012) — CATMAID: Collaborative Annotation Toolkit for Massive Amounts of Image Data

**Citation:** Saalfeld S, Cardona A, Hartenstein V, Tomancak P. CATMAID: Collaborative annotation toolkit for massive amounts of image data. *Bioinformatics*. 2009;25(15):1984-1986.
**DOI:** [10.1093/bioinformatics/btt529](https://doi.org/10.1093/bioinformatics/btt529)

**Tags:** `data-storage:neuroglancer` `data-storage:pipeline` `data-storage:cloud-storage` `proofreading:proofreading-tools` `methodology:collaboration`

### Summaries

**Beginner:** CATMAID is one of the earliest web-based tools for collaborative neuron tracing. Instead of requiring each researcher to download huge image files, CATMAID streams image tiles through a web browser and lets multiple people trace neurons simultaneously over the internet. It pioneered the idea that connectomics annotation should be collaborative, web-based, and centrally managed — principles that underpin all modern connectomics platforms.

**Intermediate:** CATMAID provides a web-based collaborative environment for skeleton tracing and annotation of large EM image volumes. Its tile-based image streaming architecture enables browsing of terabyte-scale datasets without local storage. Users trace neuron skeletons as nodes and edges, add annotations (tags, connectors for synapses), and review each other's work. CATMAID's PostgreSQL backend stores all tracing data with full edit history and user attribution. The platform was central to the *Drosophila* larval connectome and numerous other tracing projects.

**Advanced:** CATMAID's architecture established the foundational design patterns for collaborative connectomics annotation. The tile-serving approach (pre-rendered image pyramids served via HTTP) decoupled data storage from visualization and enabled browser-based access without plugins. The skeleton data model (nodes with 3D coordinates linked by edges) is fundamentally different from the volumetric segmentation model used by later tools (CAVE, Neuroglancer), with implications for data representation, storage efficiency, and the types of analyses that are natural to perform. CATMAID's contribution tracking (per-node user attribution, review status) was an early implementation of annotation provenance. The REST API enabled programmatic access and spawned an ecosystem of analysis tools (e.g., catpy, pymaid/navis). Limitations include the skeleton-only representation (no volumetric segmentation), the single-server architecture that limits scalability, and the manual-tracing paradigm that does not integrate well with automated segmentation outputs.

**Key figures:** Fig. 1 (CATMAID web interface), Fig. 2 (tile-streaming architecture), Fig. 3 (collaborative tracing workflow)

**Discussion prompts:**
- How did CATMAID's architectural decisions influence the design of later tools like Neuroglancer and CAVE?
- What are the tradeoffs of skeleton-based versus volumetric annotation for different scientific questions?
- How should collaborative annotation platforms handle conflicting edits from simultaneous users?

**Related content:** [Proofreading tools](/content-library/proofreading/proofreading-tools/), [Provenance and versioning](/content-library/infrastructure/provenance-and-versioning/)

---

## 7. Ackerman et al. (2022) — BossDB: A Cloud-Native Approach for Petascale Neuroscience Data Management

**Citation:** Ackerman W, Matelsky J, Wester B, Miller M, Vega A, Roncal WG, et al. BossDB: A cloud-native approach for petascale neuroscience data management. *Frontiers in Neuroinformatics*. 2022.
**DOI:** [10.3389/fninf.2021.828787](https://doi.org/10.3389/fninf.2021.828787)

**Tags:** `data-storage:cloud-storage` `data-storage:data-format` `data-storage:pipeline` `methodology:open-data` `infrastructure:scalability`

### Summaries

**Beginner:** Brain imaging datasets can be enormous — sometimes hundreds of terabytes for a single experiment. BossDB (Brain Observatory Storage Service and Database) is a cloud-based system designed to store, organize, and serve these massive datasets over the internet. Think of it as a specialized cloud storage service for neuroscience images that lets researchers upload, share, and access brain data without needing their own expensive storage infrastructure.

**Intermediate:** BossDB provides a cloud-native storage platform for volumetric neuroscience data, built on AWS services (S3 for object storage, DynamoDB for metadata, Lambda for serverless compute). The system supports multi-resolution image pyramids, spatial cutout queries (retrieve arbitrary 3D subvolumes), and both image and annotation channels. BossDB hosts several major public datasets and provides a REST API and Python client (intern) for programmatic access. The architecture separates storage (S3) from indexing (spatial database) to enable cost-effective scaling to petabyte volumes.

**Advanced:** BossDB's architecture addresses the specific challenges of volumetric neuroscience data at scale. The spatial indexing system (Morton/Z-order curve-based chunking in S3) enables efficient cutout queries without a traditional database for the spatial dimension. The multi-resolution support uses a precomputed image pyramid stored as chunked objects, similar to the cloud volume format used by Neuroglancer. Key design decisions include: serverless ingest pipelines that scale with data volume, IAM-based access control for dataset-level permissions, and the separation of image data from annotation data to enable independent versioning. The system's cost model (primarily S3 storage and egress) makes it economical for hosting public datasets but requires careful management of access patterns to control costs. BossDB's REST API influenced the design of CloudVolume and other programmatic access libraries used across connectomics.

**Key figures:** Fig. 1 (BossDB cloud architecture), Fig. 2 (spatial indexing and cutout queries), Fig. 3 (hosted datasets and access patterns)

**Discussion prompts:**
- What are the tradeoffs of cloud-native storage (BossDB) versus self-hosted solutions for neuroscience data?
- How do cloud egress costs affect the practical accessibility of "open" datasets?
- What metadata standards are needed to make volumetric neuroscience data FAIR (Findable, Accessible, Interoperable, Reusable)?

**Related content:** [Data formats](/content-library/infrastructure/data-formats/), [OME-Zarr paper (this page, #8)](#8-moore-et-al-2021--ome-zarr-a-cloud-optimized-bioimaging-file-format)

---

## 8. Moore et al. (2021) — OME-Zarr: A Cloud-Optimized Bioimaging File Format

**Citation:** Moore J, Allan C, Beber S, Bradbury C, Kyoda K, Lai L, et al. OME-Zarr: a cloud-optimized bioimaging file format with international community support. *bioRxiv*. 2021.
**DOI:** [10.1101/2021.03.31.437929](https://doi.org/10.1101/2021.03.31.437929)

**Tags:** `data-storage:data-format` `data-storage:cloud-storage` `data-storage:pipeline` `methodology:open-data` `methodology:standards`

### Summaries

**Beginner:** When scientists produce large 3D images of brains, they need a file format that works well for storing, sharing, and viewing the data. Traditional formats like TIFF were not designed for cloud storage or for viewing just a small piece of a huge dataset over the internet. OME-Zarr is a new file format designed from the ground up for cloud storage — it breaks large images into small chunks that can be individually downloaded, supports multiple resolution levels for fast browsing, and stores rich metadata alongside the images.

**Intermediate:** OME-Zarr combines the Zarr chunked array storage format with OME (Open Microscopy Environment) metadata standards to create a cloud-optimized format for multi-dimensional bioimaging data. Key features include: chunk-based storage enabling parallel reads of arbitrary subregions, multi-resolution pyramids (similar to image tile pyramids but generalized to N-D), rich metadata via OME-XML, and compatibility with cloud object stores (S3, GCS) and local filesystems alike. The format is supported by a growing ecosystem of viewers (Neuroglancer, napari, Fiji/BigDataViewer) and I/O libraries (zarr-python, z5, tensorstore).

**Advanced:** OME-Zarr represents a convergence of the bioimaging and cloud computing communities around a common data format. The technical design follows the "analysis-ready, cloud-optimized" (ARCO) pattern from geoscience: data is stored as independently-addressable chunks in an object store, eliminating the need for a file server or database to mediate access. The multi-resolution specification (OME-NGFF) defines a hierarchy of arrays with associated coordinate transformations, enabling viewers to load appropriate resolution levels dynamically. For connectomics specifically, OME-Zarr addresses limitations of earlier formats: N5 (lacked standardized metadata), Precomputed (Neuroglancer-specific), and HDF5 (poor cloud and parallel-access performance). The format's adoption across tools (napari, Neuroglancer, FIJI) reduces format conversion overhead in multi-tool workflows. Open challenges include standardization of label/segmentation representations, efficient handling of sparse annotations, and the metadata governance model for community extensions.

**Key figures:** Fig. 1 (OME-Zarr format structure and chunk layout), Fig. 2 (multi-resolution pyramid specification), Fig. 3 (ecosystem of compatible tools)

**Discussion prompts:**
- How does the choice of file format (HDF5 vs. N5 vs. Zarr vs. Precomputed) affect the cost and performance of connectomics data access?
- What are the implications of moving from file-based storage (HDF5 on a file system) to object-based storage (Zarr on S3)?
- How should the community govern format extensions to balance flexibility with interoperability?

**Related content:** [BossDB paper (this page, #7)](#7-ackerman-et-al-2022--bossdb-a-cloud-native-approach-for-petascale-neuroscience-data-management), [Data formats](/content-library/infrastructure/data-formats/)
