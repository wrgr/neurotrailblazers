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
use_layout_hero: false
content_type: core
---

# Data Storage & Pipelines Journal Papers

Curated papers on connectomics data management, annotation systems, file formats, versioning infrastructure, and pipeline engineering. Each paper includes summaries at three expertise levels.

---

## 1. Dorkenwald et al. (2025) — CAVE: Connectome Annotation Versioning Engine

**Citation:** Dorkenwald S, Schneider-Mizell CM, Brittain D, Halageri A, Jordan C, Kemnitz N, et al. CAVE: Connectome Annotation Versioning Engine. *Nature Methods*. 2025;22(5):1112-1120.
**DOI:** [10.1038/s41592-024-02426-z](https://doi.org/10.1038/s41592-024-02426-z)

**Tags:** `data-storage:CAVE` `data-storage:provenance` `data-storage:versioning` `data-storage:pipeline` `proofreading:proofreading-tools` `methodology:reproducibility`

### Summaries

**Beginner:** When hundreds of people are correcting a brain map at the same time, you need a system to keep track of every change — who fixed what, when, and why. CAVE is like a version control system (similar to Google Docs' history or Git for code) but designed specifically for connectomics. It lets researchers go back to any previous version of the brain map and ensures that published analyses can always be reproduced.

**Intermediate:** CAVE provides a versioned, materialized annotation infrastructure for large-scale connectomics. It tracks the complete history of proofreading edits (merges, splits) and spatial annotations (synapse labels, cell types) in a chunked graph structure that supports efficient historical queries. "Materialization" produces timestamped snapshots that freeze a consistent state of the connectome for analysis and publication. CAVE powers both the FlyWire and MICrONS annotation systems.

**Advanced:** CAVE addresses a reproducibility problem in collaborative connectomics: when many users continuously edit a shared segmentation, any analysis must be tied to a specific materialization timestamp to be reproducible. The ChunkedGraph representation keeps each edit local to the affected chunks rather than requiring full-graph recomputation, the materialization pipeline produces denormalized tables for fast analytical queries, and the versioning system maintains complete edit provenance. Key design decisions include the separation of segmentation graph structure from spatial annotations, the use of supervoxel-level granularity for undo operations, and the CAVE client API that abstracts version management for downstream analysts.

**Key figures:** Fig. 2 (scaling the ChunkedGraph to petascale datasets), Fig. 4 (annotations bound to segments through materialization), Fig. 5 (querying the dataset for any time point), Extended Data Fig. 3 (overview of the core CAVE services)

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

**Beginner:** Turning a million electron microscopy images into a wiring diagram of the brain requires a massive computational pipeline — like a factory assembly line for data. This paper describes the complete pipeline used for the MICrONS project: aligning images, finding neuron boundaries, stitching neurons across sections, detecting synapses, and packaging everything for analysis. It is a detailed engineering description of a large-scale connectomics pipeline.

**Intermediate:** Macrina et al. describe the full automated reconstruction pipeline for the MICrONS cubic-millimeter cortical volume. From a data-engineering perspective, the paper details how more than a petabyte of raw serial-section imagery is aligned with convolutional nets that handle cracks and folds, processed through boundary detection and mean affinity agglomeration, and then stored and indexed for downstream analysis. The pipeline's orchestration across cloud compute resources, the intermediate data representations at each stage, and the quality-control checkpoints provide a reference architecture for petascale neuroscience data processing.

**Advanced:** This paper is a systems-engineering reference for petascale connectomics pipelines. From a data-management standpoint, key contributions include: the convolutional-net alignment that computes nonsmooth transformations across sections with cracks and folds; the divide-and-conquer orchestration across distributed and cloud computing; the intermediate data representations (affinity maps, supervoxel graphs, agglomeration tables) and their storage formats; and the practice of holding intermediate results in cloud storage where they can be viewed as images, which aids debugging. The pipeline's output feeds directly into CAVE for versioned annotation management.

**Key figures:** Look for the overall pipeline diagram, the examples of alignment across cracks and folds, and the description of how work is split across cloud machines.

**Discussion prompts:**
- How do the intermediate data representations at each pipeline stage affect storage requirements and downstream reprocessing flexibility?
- What would a cost-optimal cloud architecture look like for running this pipeline today?
- How do the computational costs scale with volume size, and where are the bottlenecks?

**Related content:** [MICrONS visual cortex](/content-library/case-studies/microns-visual-cortex/), [Data formats](/content-library/infrastructure/data-formats/), [CAVE paper (this page, #1)](#1-dorkenwald-et-al-2025--cave-connectome-annotation-versioning-engine)

---

## 3. Scheffer et al. (2020) — A Connectome and Analysis of the Adult Drosophila Central Brain

**Citation:** Scheffer LK, Xu CS, Januszewski M, Lu Z, Takemura SY, Hayworth KJ, et al. A connectome and analysis of the adult *Drosophila* central brain. *eLife*. 2020;9:e57443.
**DOI:** [10.7554/eLife.57443](https://doi.org/10.7554/eLife.57443)

**Tags:** `data-storage:pipeline` `data-storage:data-format` `case-studies:Drosophila` `data-storage:neuroglancer` `proofreading:proofreading-strategy`

### Summaries

**Beginner:** This paper describes the "hemibrain", a map of a large part of the fruit fly's central brain with about 25,000 neurons and about 20 million synapses. Beyond the biology, the paper matters for data management: the whole dataset was released through the neuPrint database, so anyone can query the connectome. Its release strategy and tooling became a model for open connectomics data.

**Intermediate:** Scheffer et al. present the hemibrain connectome from a FIB-SEM volume of *Drosophila* central brain at 8 nm isotropic resolution. From a data infrastructure perspective, the paper demonstrates the end-to-end pipeline from FIB-SEM acquisition through FFN-based segmentation, extensive proofreading (over 50 person-years), synapse detection, and neuron type assignment. The dataset release via neuPrint — with structured metadata, graph query capabilities, and programmatic access — became a template for packaging and sharing large connectomics datasets.

**Advanced:** The hemibrain project's data infrastructure decisions shaped later releases. Proofreading was guided by synapse predictions and aimed at the highest reconstruction completeness possible in the time available, so neurons differ in how completely they were traced and the release needs metadata that records each neuron's reconstruction status. The neuPrint graph database representation encodes neurons as nodes and weighted connections as edges, enabling Cypher-based queries that support both exploratory analysis and systematic circuit enumeration. At about 25,000 neurons and 20 million synapses, it was a large dataset to serve through a web query interface at the time. Limitations from a data perspective include boundary effects (incomplete neurons at volume edges) and heterogeneous proofreading completeness across brain regions, both of which require careful metadata annotation.

**Key figures:** Fig. 1 (the hemibrain and basic statistics), Fig. 5 (precision and recall of synapse prediction), Fig. 17 (overview of data representations), Fig. 18 (neo4j graph schema)

**Discussion prompts:**
- How does the neuPrint graph database design affect which biological questions are easy vs. hard to answer?
- What metadata standards are needed to communicate reconstruction completeness and confidence to downstream users?
- How should data releases handle the tension between early access and quality assurance?

**Related content:** [FlyWire whole-brain](/content-library/case-studies/flywire-whole-brain/), [neuPrint paper (this page, #5)](#5-plaza-et-al-2022--neuprint-an-open-access-tool-for-em-connectomics)

---

## 4. Berger et al. (2018) — VAST: Volume Annotation and Segmentation Tool

**Citation:** Berger DR, Seung HS, Lichtman JW. VAST (Volume Annotation and Segmentation Tool): Efficient manual and semi-automatic labeling of large 3D image stacks. *Frontiers in Neural Circuits*. 2018;12:88.
**DOI:** [10.3389/fncir.2018.00088](https://doi.org/10.3389/fncir.2018.00088)

**Tags:** `data-storage:neuroglancer` `data-storage:data-format` `proofreading:proofreading-tools` `methodology:ground-truth`

### Summaries

**Beginner:** Before you can train a computer to find neurons in images, humans need to manually label example images to create "ground truth" data. VAST is a desktop tool designed for this manual labeling work. It lets annotators paint over neurons in 3D image stacks, assign labels, and track their work efficiently. Good annotation tools are the foundation of every connectomics data pipeline.

**Intermediate:** VAST provides a desktop annotation environment optimized for large-scale manual and semi-automatic segmentation of EM volumes. Features include multi-resolution rendering, hierarchical label management for large numbers of segments, masked painting, merge and split operations for proofreading automatic segmentations, and import and export of image and segmentation stacks (for example PNG and TIFF). An early version of VAST was used for the manual annotation in Kasthuri et al. (2015). Its design emphasizes annotation throughput and data consistency for creating training data.

**Advanced:** While cloud-based tools (Neuroglancer, CAVE) now dominate production proofreading workflows, VAST remains relevant for ground truth creation where precise manual control and deterministic performance are needed. The tool's architecture — local rendering with on-disk storage rather than cloud streaming — provides consistent performance independent of network conditions and avoids cloud storage costs for iterative annotation work. Its paint-based annotation model (rather than supervoxel-based editing) is well-suited for creating dense ground truth that does not inherit biases from automated pre-segmentation. For benchmark creation and segmentation validation, pixel-precise annotation of this kind is still common. Its image-stack export interfaces with standard training pipelines.

**Key figures:** Fig. 1 (VAST user interface), Fig. 4 (masked painting), Fig. 7 (internal program structure and control flow)

**Discussion prompts:**
- When should you use desktop tools (VAST) versus cloud tools (Neuroglancer/CAVE) for annotation work?
- How does the choice of annotation tool and its data format affect the quality and biases of ground truth data?
- What data format considerations arise when moving annotations between local and cloud-based systems?

**Related content:** [Proofreading tools](/content-library/proofreading/proofreading-tools/), [Metrics and QA](/content-library/proofreading/metrics-and-qa/)

---

## 5. Plaza et al. (2022) — neuPrint: An Open Access Tool for EM Connectomics

**Citation:** Plaza SM, Clements J, Dolafi T, Umayam L, Neubarth NN, Scheffer LK, Berg S. neuPrint: an open access tool for EM connectomics. *Frontiers in Neuroinformatics*. 2022;16:896292. Preprint: Clements J, et al. neuPrint: analysis tools for EM connectomics. *bioRxiv* 2020, [doi:10.1101/2020.01.16.909465](https://doi.org/10.1101/2020.01.16.909465).
**DOI:** [10.3389/fninf.2022.896292](https://doi.org/10.3389/fninf.2022.896292)

**Tags:** `data-storage:CAVE` `data-storage:neuroglancer` `data-storage:data-format` `data-storage:cloud-storage` `connectomics:graph-theory`

### Summaries

**Beginner:** Once you have a brain wiring diagram with tens of thousands of neurons, you need a way to search through it and ask questions like "which neurons connect to this one?" neuPrint is a database and web interface that lets researchers explore connectome data without writing complex code. It stores neurons, their connections, and metadata in a graph database that you can query through a web interface or code.

**Intermediate:** neuPrint provides a Neo4j-based graph database and web interface for querying and exploring connectome data. Neurons are represented as nodes with properties (type, size, brain region) and connections as weighted edges (synapse counts). The system supports Cypher queries for complex graph traversals, prebuilt "find neurons" and "find connections" interfaces for common operations, and a plugin architecture for custom analyses. neuPrint serves as the primary data access layer for the hemibrain and other HHMI Janelia connectome datasets.

**Advanced:** neuPrint's design reflects deliberate tradeoffs in connectomics data representation. The choice of a property graph model (Neo4j) over a relational or RDF model enables flexible schema evolution as new annotation types are added, but requires careful index management for performant queries on graphs with millions of edges. The system's "ROI" (region of interest) intersection weights on edges enable brain-region-specific connectivity analysis without spatial queries. The REST API and Python client (neuprint-python) support programmatic access for batch analyses. Key architectural decisions include the materialization of synapse counts as edge weights (trading storage for query speed), the hierarchical ROI system, and the separation of the query engine from visualization (delegated to Neuroglancer).

**Discussion prompts:**
- What are the tradeoffs of a graph database versus a relational database for connectomics data?
- How does neuPrint's data model handle the evolution of neuron type classifications over time?
- What query patterns are easy vs. difficult in neuPrint's current architecture?

**Related content:** [Hemibrain paper (this page, #3)](#3-scheffer-et-al-2020--a-connectome-and-analysis-of-the-adult-drosophila-central-brain), [Network analysis methods](/content-library/connectomics/network-analysis-methods/)

---

## 6. Saalfeld et al. (2009) — CATMAID: Collaborative Annotation Toolkit for Massive Amounts of Image Data

**Citation:** Saalfeld S, Cardona A, Hartenstein V, Tomancak P. CATMAID: Collaborative annotation toolkit for massive amounts of image data. *Bioinformatics*. 2009;25(15):1984-1986.
**DOI:** [10.1093/bioinformatics/btp266](https://doi.org/10.1093/bioinformatics/btp266)

**Tags:** `data-storage:neuroglancer` `data-storage:pipeline` `data-storage:cloud-storage` `proofreading:proofreading-tools` `methodology:collaboration`

### Summaries

**Beginner:** CATMAID is one of the earliest web-based tools for collaborative annotation of huge image stacks. Inspired by online maps, it streams image tiles through a web browser instead of requiring each researcher to download huge image files, and lets multiple people browse and annotate the same data over the internet. Neuron tracing tools were added to CATMAID in later versions. It helped establish that connectomics annotation can be collaborative, web-based, and centrally managed, which most later platforms also assume.

**Intermediate:** The 2009 paper presents CATMAID as a decentralized web interface for navigating arbitrarily large image stacks, annotating them collaboratively, sharing regions of interest by bookmark, and navigating multiple registered datasets in sync (for example light and electron microscopy). A central server stores metadata about datasets, users and annotations in a PostgreSQL database. Skeleton tracing (nodes, edges, synapse connectors) and review tools were added in later versions, and the platform became central to the *Drosophila* larval connectome and numerous other tracing projects.

**Advanced:** CATMAID's architecture set design patterns that later collaborative annotation tools reused. The tile-serving approach (pre-rendered image pyramids served via HTTP) decoupled data storage from visualization and enabled browser-based access without plugins. The skeleton data model added in later CATMAID versions (nodes with 3D coordinates linked by edges) is fundamentally different from the volumetric segmentation model used by later tools (CAVE, Neuroglancer), with implications for data representation, storage efficiency, and the types of analyses that are natural to perform. Later CATMAID versions' contribution tracking (per-node user attribution, review status) was an early implementation of annotation provenance. The REST API enabled programmatic access and spawned an ecosystem of analysis tools (e.g., catpy, pymaid/navis). Limitations include the skeleton-only representation (no volumetric segmentation), the single-server architecture that limits scalability, and the manual-tracing paradigm that does not integrate well with automated segmentation outputs.

**Key figures:** Fig. 1 (information flow between the central data server, the client-side interface and the image servers)

**Discussion prompts:**
- How did CATMAID's architectural decisions influence the design of later tools like Neuroglancer and CAVE?
- What are the tradeoffs of skeleton-based versus volumetric annotation for different scientific questions?
- How should collaborative annotation platforms handle conflicting edits from simultaneous users?

**Related content:** [Proofreading tools](/content-library/proofreading/proofreading-tools/), [Provenance and versioning](/content-library/infrastructure/provenance-and-versioning/)

---

## 7. Hider et al. (2022) — BossDB: A Cloud-Native Approach for Petascale Neuroscience Data Management

**Citation:** Hider R Jr, Kleissas D, Gion T, Xenes D, Matelsky J, Pryor D, et al. The Brain Observatory Storage Service and Database (BossDB): a cloud-native approach for petascale neuroscience discovery. *Frontiers in Neuroinformatics*. 2022;16:828787.
**DOI:** [10.3389/fninf.2022.828787](https://doi.org/10.3389/fninf.2022.828787)

**Tags:** `data-storage:cloud-storage` `data-storage:data-format` `data-storage:pipeline` `methodology:open-data` `infrastructure:scalability`

### Summaries

**Beginner:** Brain imaging datasets can be enormous — sometimes hundreds of terabytes for a single experiment. BossDB (Brain Observatory Storage Service and Database) is a cloud-based system designed to store, organize, and serve these massive datasets over the internet. Think of it as a specialized cloud storage service for neuroscience images that lets researchers upload, share, and access brain data without needing their own expensive storage infrastructure.

**Intermediate:** BossDB provides a cloud-native storage platform for volumetric neuroscience data, built on AWS services (S3 for object storage, DynamoDB for metadata, Lambda for serverless compute). The system supports multi-resolution image pyramids, spatial cutout queries (retrieve arbitrary 3D subvolumes), and both image and annotation channels. BossDB hosts several major public datasets and provides a RESTful API and Python client (intern) for programmatic access. The architecture keeps image cuboids in S3 and spatial and annotation indices in DynamoDB tables, which lets it scale to datasets over a petabyte in size.

**Advanced:** BossDB's architecture addresses the specific challenges of volumetric neuroscience data at scale. The spatial indexing system (cuboids stored in S3 and indexed with a Morton-order space-filling curve) enables efficient cutout queries without a traditional database for the spatial dimension. The multi-resolution support uses a precomputed image pyramid stored as chunked objects, similar to the cloud volume format used by Neuroglancer. Key design decisions include: serverless ingest pipelines (AWS Lambda and Step Functions) that scale with data volume, single sign-on with roles and permissions that let a dataset stay private or be shared, and the separation of image channels from annotation channels. The system's cost model (primarily S3 storage and egress) makes it economical for hosting public datasets but requires careful management of access patterns to control costs.

**Key figures:** Fig. 1 (high-level schematic of the platform), Fig. 4 (cuboid storage indexed by a z-order curve), Fig. 7 (architecture as deployed on Amazon Web Services), Fig. 9 (volumetric ingest throughput)

**Discussion prompts:**
- What are the tradeoffs of cloud-native storage (BossDB) versus self-hosted solutions for neuroscience data?
- How do cloud egress costs affect the practical accessibility of "open" datasets?
- What metadata standards are needed to make volumetric neuroscience data FAIR (Findable, Accessible, Interoperable, Reusable)?

**Related content:** [Data formats](/content-library/infrastructure/data-formats/), [OME-Zarr paper (this page, #8)](#8-moore-et-al-2023--ome-zarr-a-cloud-optimized-bioimaging-file-format)

---

## 8. Moore et al. (2023) — OME-Zarr: A Cloud-Optimized Bioimaging File Format

**Citation:** Moore J, Basurto-Lozada D, Besson S, Bogovic J, Bragantini J, Brown EM, et al. OME-Zarr: a cloud-optimized bioimaging file format with international community support. *Histochemistry and Cell Biology*. 2023;160(3):223-251.
**DOI:** [10.1007/s00418-023-02209-1](https://doi.org/10.1007/s00418-023-02209-1)

The format was first proposed in Moore J, Allan C, Besson S, Burel JM, Diel E, Gault D, et al. OME-NGFF: a next-generation file format for expanding bioimaging data-access strategies. *Nature Methods*. 2021;18(12):1496-1498. DOI: [10.1038/s41592-021-01326-w](https://doi.org/10.1038/s41592-021-01326-w)

**Tags:** `data-storage:data-format` `data-storage:cloud-storage` `data-storage:pipeline` `methodology:open-data` `methodology:standards`

### Summaries

**Beginner:** When scientists produce large 3D images of brains, they need a file format that works well for storing, sharing, and viewing the data. Traditional formats like TIFF were not designed for cloud storage or for viewing just a small piece of a huge dataset over the internet. OME-Zarr is a new file format designed from the ground up for cloud storage — it breaks large images into small chunks that can be individually downloaded, supports multiple resolution levels for fast browsing, and stores rich metadata alongside the images.

**Intermediate:** OME-Zarr combines the Zarr chunked array storage format with OME (Open Microscopy Environment) metadata standards to create a cloud-optimized format for multi-dimensional bioimaging data. Key features include: chunk-based storage enabling parallel reads of arbitrary subregions, multi-resolution pyramids (similar to image tile pyramids but generalized to N-D), rich metadata stored as JSON alongside the arrays (following the OME-NGFF specification), and compatibility with cloud object stores (S3, GCS) and local filesystems alike. The format is supported by a growing ecosystem of viewers (Neuroglancer, napari, Fiji/BigDataViewer) and I/O libraries (zarr-python, z5, tensorstore).

**Advanced:** OME-Zarr brings the bioimaging and cloud computing communities onto a common data format. The technical design follows the "analysis-ready, cloud-optimized" (ARCO) pattern from geoscience: data is stored as independently-addressable chunks in an object store, eliminating the need for a file server or database to mediate access. The multi-resolution specification (OME-NGFF) defines a hierarchy of arrays with associated coordinate transformations, enabling viewers to load appropriate resolution levels dynamically. For connectomics specifically, OME-Zarr addresses limitations of earlier formats: N5 (lacked standardized metadata), Precomputed (Neuroglancer-specific), and HDF5 (poor cloud and parallel-access performance). The format's adoption across tools (napari, Neuroglancer, FIJI) reduces format conversion overhead in multi-tool workflows. Open challenges include standardization of label/segmentation representations, efficient handling of sparse annotations, and the metadata governance model for community extensions.

**Key figures:** Fig. 1 (a common format serving diverse use cases), Fig. 2 (hierarchy of arrays, multiscale pyramid and chunking), Fig. 6 (Neuroglancer rendering an OME-Zarr dataset)

**Discussion prompts:**
- How does the choice of file format (HDF5 vs. N5 vs. Zarr vs. Precomputed) affect the cost and performance of connectomics data access?
- What are the implications of moving from file-based storage (HDF5 on a file system) to object-based storage (Zarr on S3)?
- How should the community govern format extensions to balance flexibility with interoperability?

**Related content:** [BossDB paper (this page, #7)](#7-hider-et-al-2022--bossdb-a-cloud-native-approach-for-petascale-neuroscience-data-management), [Data formats](/content-library/infrastructure/data-formats/)
