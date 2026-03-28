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

## References

- Dorkenwald S et al. (2022) "CAVE: Connectome Annotation Versioning Engine." *bioRxiv*.
- Sato M et al. (2000) "TEASAR: Tree-structure extraction algorithm for accurate and robust skeletons." *Proc. Pacific Conference on Computer Graphics and Applications*.
- Rubinov M, Sporns O (2010) "Complex network measures of brain connectivity: Uses and interpretations." *NeuroImage* 52(3):1059-1069.
- Scheffer LK et al. (2020) "A connectome and analysis of the adult *Drosophila* central brain." *eLife* 9:e57443.
