---
layout: page
title: "Data Formats and Representations"
permalink: /content-library/infrastructure/data-formats/
description: "Connectomics data representations — volumes, meshes, skeletons, and graphs — when to use each, format specifications, and conversion tradeoffs."
topics:
  - data-formats
  - volumes
  - meshes
  - skeletons
  - graphs
primary_units:
  - "02"
  - "04"
difficulty: "Intermediate"
tags:
  - infrastructure:data-formats
  - infrastructure:volume-representation
  - infrastructure:mesh-formats
  - infrastructure:skeleton-formats
  - connectomics:graph-storage
  - methodology:data-management
micro_lesson_id: ml-infra-data-formats
reference_images:
  - src: /assets/images/content-library/infrastructure/data-formats/data-representation-hierarchy.png
    alt: "Hierarchy of data representations from voxels to meshes to skeletons to graphs"
    caption: "Data abstraction hierarchy: raw voxels → segmentation labels → 3D meshes → topological skeletons → connectivity graph. Each level trades detail for compactness."
  - src: /assets/images/content-library/infrastructure/data-formats/format-comparison-table.png
    alt: "Table comparing data formats by size, query speed, and supported analyses"
    caption: "Format comparison: Precomputed, N5, Zarr for volumes; OBJ, Neuroglancer mesh for surfaces; SWC, skeleton API for morphology."
  - src: /assets/images/content-library/infrastructure/data-formats/conversion-workflow.png
    alt: "Workflow diagram showing conversion paths between data formats"
    caption: "Format conversion paths: arrows show supported conversions between volume, mesh, skeleton, and graph representations with typical tools."
combines_with:
  - reconstruction-pipeline
  - provenance-and-versioning
  - neuron-type-identification
content_type: core
---

## Overview

A connectomics dataset is not one thing — it is a family of representations at different levels of abstraction. Raw images, segmentation volumes, surface meshes, morphological skeletons, and connectivity graphs each capture different aspects of the same underlying biology. Choosing the right representation for a given task is a core technical skill, because each format has characteristic strengths, blind spots, and computational costs.

---

## The representation hierarchy

```
Raw EM images (voxels)
    ↓ segmentation
Labeled volumes (voxel → segment ID)
    ↓ surface extraction
Meshes (triangulated surfaces)
    ↓ skeletonization
Skeletons (tree graphs with spatial coordinates)
    ↓ synapse assignment
Connectome graph (neurons as nodes, synapses as edges)
```

Each arrow is an information-reducing transformation. You gain computational efficiency and analytical clarity, but you lose spatial detail. The key question is: **what information do you need for your analysis, and what is the cheapest representation that preserves it?**

---

## Volumetric data

### What it is

The most fundamental representation: a 3D array of voxel intensities (raw images) or voxel labels (segmentation). Every spatial position has a value.

### Formats

| Format | Description | Typical use |
|--------|-------------|------------|
| **Neuroglancer precomputed** | Chunked, multiscale image pyramid served over HTTP | Web-based browsing (Neuroglancer, Spelunker) |
| **N5** | Chunked, compressed, hierarchical format (Java/Python) | Pipeline intermediate storage |
| **Zarr** | Python-native chunked array format, cloud-friendly | Analysis, cloud storage (S3, GCS) |
| **HDF5** | Hierarchical Data Format, self-describing | Legacy, local analysis |
| **TIFF stacks** | Uncompressed or LZW-compressed image stacks | Raw microscope output, small datasets |

### Key properties

- **Chunking**: Large volumes are divided into chunks (e.g., 128³ or 256³ voxels). Chunks are the unit of I/O — you load one chunk at a time, not the whole volume. Chunk size affects performance: larger chunks = fewer I/O operations but more wasted bandwidth if you only need a small region.
- **Multi-resolution pyramids**: Store the same volume at multiple resolutions (full res, 2× downsampled, 4×, 8×...). Enables efficient browsing — you see the overview at low resolution and zoom into high resolution on demand.
- **Compression**: Typical compression ratios of 2-10× for EM data (depending on algorithm: gzip, lz4, zstd, JPEG for lossy). Segmentation volumes compress much better than raw images (large uniform regions).

### When to use volumetric data

- Raw image inspection and quality control
- Running segmentation or synapse detection models (need voxel-level input)
- Proofreading (need to see images + segmentation overlay)
- Any analysis requiring spatial context that meshes or skeletons don't preserve

### Limitations

- **Storage**: A 1 mm³ volume at 4 nm resolution is ~10^13 voxels, ~10 TB at 8-bit. With segmentation (32-bit or 64-bit labels), double or quadruple that.
- **Query efficiency**: "Which neurons are within 10 μm of this synapse?" requires scanning voxels unless you also maintain a spatial index.

---

## Surface meshes

### What they are

Triangulated surfaces that represent the boundary of each segmented object. Each mesh is a set of vertices (3D points) and faces (triangles connecting vertices).

### How they're generated

Marching cubes algorithm (or variants) applied to the segmentation volume. For each segment, extract the isosurface at the boundary between that segment and its neighbors. The result is a watertight mesh (ideally).

### Formats

| Format | Description |
|--------|-------------|
| **OBJ** | Simple text format, widely supported |
| **PLY** | Binary or text, supports vertex attributes (colors) |
| **STL** | Binary triangle format, common in 3D printing |
| **Neuroglancer mesh** | Chunked, multi-resolution mesh format for web rendering |
| **DRACO** | Google's compressed mesh format, used in Neuroglancer |

### Key properties

- **Level of detail (LOD)**: Store meshes at multiple simplification levels. Full-resolution meshes for a large neuron can have millions of triangles — impractical for real-time rendering. Decimated meshes (10K-100K triangles) are used for overview visualization.
- **Vertex attributes**: Meshes can carry per-vertex data (e.g., distance from soma, local curvature, synapse density) for visualization and analysis.

### When to use meshes

- 3D visualization of neuron morphology
- Surface area and volume measurements
- Spine detection (local curvature analysis on dendritic surfaces)
- Spatial proximity analysis between neurons
- Proofreading — 3D mesh view reveals impossible morphology (merge errors) that is hard to see in 2D slices

### Limitations

- Lose internal structure (organelle distributions, cytoplasmic features)
- Mesh topology errors (self-intersections, holes) can arise from noisy segmentation boundaries
- Large storage for complex neurons (a single pyramidal cell mesh can be >100 MB at full resolution)

---

## Skeletons

### What they are

Tree-graph representations of neuron morphology. Each skeleton is a set of nodes (3D coordinates along the neurite centerline) connected by edges (parent-child relationships). The root is typically the soma, and branches represent dendrites and axons.

### How they're generated

- **From volumes**: Thinning/skeletonization algorithms (e.g., TEASAR — Sato et al. 2000) reduce the volumetric segment to its medial axis.
- **From meshes**: Contract the mesh surface to extract the centerline.
- **Manual tracing**: Historically, skeletons were traced manually in tools like CATMAID.

### Formats

| Format | Description |
|--------|-------------|
| **SWC** | Standard text format for neuron morphologies. Each line: ID, type, x, y, z, radius, parent_ID. Widely supported by morphology tools (NeuroM, Neurolucida, NEURON simulator). |
| **JSON skeleton** | Used by Neuroglancer and CloudVolume |
| **CATMAID skeleton** | Database-backed skeleton with annotations |

### Key properties

- **Compact**: A neuron that occupies millions of voxels in volumetric form is represented by thousands of skeleton nodes (~KB vs GB).
- **Topologically explicit**: Branch points, terminal points, and path lengths are directly readable.
- **Morphometric analysis**: Cable length, branch order, Strahler number, bifurcation angles, tortuosity — all computed directly from skeletons.
- **Radius information**: SWC format includes radius at each node, preserving approximate process caliber.

### When to use skeletons

- Morphological analysis (total cable length, branch complexity, Sholl analysis)
- Cell-type classification based on morphology
- Path-length measurements between synapses
- Input to biophysical simulation (NEURON, Brian)
- Efficient error detection (skeleton shows impossible topology)

### Limitations

- **Lose surface geometry**: Spine morphology, surface area, local curvature not captured
- **Lose volume information**: Can't compute volume-based measurements
- **Skeletonization errors**: Thin processes may be skipped, branch points mislocated, spurious branches created from noisy segmentation
- **Radius approximation**: SWC radius is a single value per node (circular cross-section assumption), which doesn't capture irregular shapes

---

## Connectome graphs

### What they are

The highest-level representation: neurons as nodes, synaptic connections as edges. This is the "connectome" — the wiring diagram.

### How they're constructed

1. Each segmented neuron = one node
2. Each detected synapse → identify pre-synaptic and post-synaptic segments → create directed edge from pre to post
3. Aggregate: multiple synapses between the same pair → edge weight = synapse count (or sum of cleft areas)

### Formats

| Format | Description |
|--------|-------------|
| **Edge list** (CSV/TSV) | Simple: pre_id, post_id, weight, synapse_count |
| **Adjacency matrix** (NumPy/sparse) | N×N matrix, good for linear algebra |
| **GraphML / GEXF** | XML-based, supports node/edge attributes |
| **NetworkX pickle** | Python-native, good for analysis |
| **Neo4j / graph database** | Queryable graph store for large connectomes |

### Node attributes

- Cell type (morphological or transcriptomic classification)
- Soma position (x, y, z)
- Morphological features (cable length, spine density, arbor volume)
- Functional properties (tuning curves from calcium imaging, if available)

### Edge attributes

- Synapse count
- Total cleft area or PSD area
- Synapse type (excitatory/inhibitory)
- Spatial locations of individual synapses
- Confidence score

### When to use graphs

- Connectivity analysis (degree distributions, clustering, motifs)
- Circuit identification (find all neurons in a pathway)
- Comparison across datasets or conditions
- Input to network models (spiking simulations, dynamical systems)

### Limitations

- **Lose all spatial information** (unless node/edge positions are stored as attributes)
- **Lose morphological detail** — a graph edge between two neurons doesn't tell you whether the synapse is on a proximal dendrite or a distal spine
- **Thresholding dependence** — decisions about minimum synapse count for an "edge" dramatically affect graph structure
- **Error amplification** — segmentation and synapse detection errors both corrupt the graph

---

## Worked example: choosing a representation

**Question:** "Do inhibitory interneurons preferentially target the perisomatic region of pyramidal cells in layer 2/3?"

**Analysis needs:**
1. Identify inhibitory and excitatory neurons → need cell-type labels (graph node attributes)
2. Find synapses between inhibitory → pyramidal pairs → need connectome graph edges
3. Determine synapse location on the pyramidal cell (perisomatic vs distal dendrite) → need synapse spatial coordinates mapped onto the pyramidal cell morphology

**Representation choice:** This question requires the **connectome graph** (for connectivity) plus **skeletons** (for distance-from-soma measurement at each synapse location). Neither the graph alone (no spatial synapse info) nor the volume alone (too expensive for the network-level query) would suffice.

---

## Skeletonization: the method changes the answer

Every skeleton is an approximation of a shape, and different approximations
disagree. This matters more than it sounds, because morphology statistics are
computed *from the skeleton*, not from the neuron — so path length, branch
count and tortuosity are properties of a method as much as of a cell.

| Approach | How it works | What it is good at | What it loses |
|---|---|---|---|
| **TEASAR-family** (kimimaro and relatives) | Repeated shortest-path extraction through a distance-transformed segmentation, with penalties that push the path toward the object's center | Robustness on noisy segmentation; deterministic; scales to whole volumes | Tends to over-penetrate into spine heads or shave them off entirely, depending on the invalidation radius |
| **Mesh contraction** | Iteratively collapse a surface mesh toward its medial axis, then extract a curve skeleton | Follows fine geometry closely; good radius estimates | Sensitive to mesh defects; expensive; a hole in the mesh can reroute a branch |
| **Manual tracing** (CATMAID-style) | A human places and connects nodes | The gold standard for topology; annotator judgment handles ambiguity | Slow, and carries the annotator's systematic biases |

**The practical consequence:** a morphology statistic is only comparable within
one skeletonization method, at one parameter setting. If you compare branch
counts between two datasets skeletonized differently, you are partly measuring
the difference between the algorithms. State the method and its parameters
alongside any morphometric result, exactly as you would state a proofreading
level alongside a connectivity result.

Spines are where the methods diverge most, and they are also where the
biological question usually is. If spines matter to your analysis, check what
your skeletonizer does to them on a handful of cells you have looked at by eye
before trusting it on ten thousand you have not.

---

## What each conversion loses

The representations are not interchangeable, and the pipeline between them is
one-way. Knowing which direction you are traveling tells you what you can
still ask.

| From → to | What is preserved | What is gone for good |
|---|---|---|
| **Volume → mesh** | Surface geometry, volume, surface area | Interior structure, image intensity, every organelle cue from Units 05-07 |
| **Mesh → skeleton** | Topology, path length, radius | Surface detail, spine head shape, membrane apposition — you can no longer ask whether two processes touch |
| **Skeleton → graph** | Connectivity, synapse counts | All geometry. Distance-dependent nulls become impossible unless you kept soma positions |
| **Volume → graph** (the full pipeline) | The connectivity claim | Everything you would need to check that claim against the images |

The last row is the important one. By the time you are working with an
adjacency matrix, every judgment made upstream — segmentation, agglomeration,
synapse detection, proofreading — has been baked in and is invisible. That is
why provenance metadata is not bureaucracy: it is the only remaining link
between a number and the evidence for it.

**A round trip is not lossless.** Meshing a segmentation and re-voxelizing the
mesh does not return the original labels; the surface has been resampled and
smoothed. If you need the voxels, keep the voxels.

---

## Storage, in proportion

Format choices look abstract until they meet a storage budget. For a
mm³-scale volume, the orders of magnitude are roughly as Unit 04 §2 sets them
out: raw and aligned imagery in the petabytes, segmentation labels in the
hundreds of terabytes with label-aware compression, meshes in the low
terabytes, and skeletons in the tens of gigabytes.

The ratio worth remembering is the last one: **skeletons are around five orders
of magnitude smaller than the imagery they came from.** That is why skeletons
get archived and shared while imagery gets left in the bucket it was
reconstructed in, and why a great deal of comparative morphology work is
possible for anyone with a laptop.

Chunk size is the other lever, and there is no correct value. Small chunks make
random access cheap and multiply the number of objects, which object stores
handle badly; large chunks reverse both. Pick from your access pattern — a
viewer paging through xy planes and an analysis streaming along z want
different shapes — and expect to shard the result.

---

## Common misconceptions

| Misconception | Reality |
|---|---|
| "The mesh and the segmentation are the same thing." | The mesh is derived from the segmentation and is regenerated whenever an edit changes it. Two people looking at the same mesh URL after an edit are looking at different objects. |
| "Skeletons are just simplified meshes." | They are a different kind of object: a graph with radii, not a surface. You cannot recover a mesh from a skeleton, and the statistics you compute from each are not comparable. |
| "Path length is a property of the neuron." | It is a property of the neuron *and* the skeletonization method. Report the method. |
| "Zarr, N5 and Precomputed are basically interchangeable." | All three are chunked multiscale layouts, but the metadata conventions differ and a reader for one will not open another without conversion. |
| "If I keep the graph, I can always go back to the images." | Only if you also kept the dataset name, the segmentation version and the query. The graph alone contains no route back. |
| "Compression choice is a performance detail." | Lossy compression on segmentation labels is not a performance detail; it changes object boundaries. Label data needs lossless, label-aware codecs. |

---

## References

- Dorkenwald S et al. (2024) "CAVE: Connectome Annotation Versioning Engine." *Nature Methods*. doi:10.1038/s41592-024-02426-z.
- Sato M et al. (2000) "TEASAR: Tree-structure extraction algorithm for accurate and robust skeletons." *Proc. Pacific Conference on Computer Graphics and Applications*.
- Rubinov M, Sporns O (2010) "Complex network measures of brain connectivity: Uses and interpretations." *NeuroImage* 52(3):1059-1069.
- Scheffer LK et al. (2020) "A connectome and analysis of the adult *Drosophila* central brain." *eLife* 9:e57443.
