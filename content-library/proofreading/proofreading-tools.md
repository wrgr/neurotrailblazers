---
layout: page
title: "Proofreading Tools for Connectome Reconstruction"
permalink: /content-library/proofreading/proofreading-tools/
description: >
  A detailed instructor reference on the software tools used for connectome
  proofreading, including CAVE, Neuroglancer, Spelunker, NeuTu, and CATMAID.
  Covers architecture, editing operations, tool comparison, and a worked
  example of a merge correction workflow.
topics:
  - CAVE
  - Neuroglancer
  - Spelunker
  - NeuTu
  - CATMAID
  - split operations
  - merge operations
  - supervoxel graphs
  - proofreading workflows
primary_units:
  - proofreading-fundamentals
  - proofreading-workflows
  - tool-proficiency
difficulty: intermediate
---

# Proofreading Tools for Connectome Reconstruction

## Instructor Notes

This document is a standalone instructor script covering the major
software platforms used for connectome proofreading. It provides
architectural details, practical workflow descriptions, and a comparative
framework. Adapt to your audience; students who will use these tools
hands-on need more detail on interface mechanics, while those focused on
analysis need more on how tools affect data provenance.

---

## 1. Overview: The Proofreading Tool Ecosystem

Proofreading connectome data requires specialized software that can:

1. **Render** terabyte-to-petabyte-scale volumetric electron microscopy
   data in real time.
2. **Display** segmentation overlays on top of raw imagery.
3. **Support editing** operations (split, merge, extend, delete) that
   modify the segmentation.
4. **Record** all edits with provenance (who, when, what) for
   reproducibility.
5. **Integrate** with annotation systems (synapse labels, cell type tags,
   compartment labels).

No single tool does all of these perfectly. In practice, most projects use
a combination: a backend system for data management and versioning, a
frontend viewer for visualization, and a workflow layer for task
assignment and quality tracking.

---

## 2. CAVE (Connectome Annotation Versioning Engine)

### 2.1 Architecture

CAVE, described by Dorkenwald et al. (2022), is the backend infrastructure
that makes large-scale collaborative proofreading possible. Its core
innovation is the **chunked supervoxel graph**.

**Supervoxels.** The automated segmentation pipeline produces an
over-segmentation: millions of small, conservatively drawn segments called
supervoxels. Each supervoxel is an atomic unit that is never subdivided
during proofreading. A typical supervoxel might be 1-10 um^3.

**Agglomeration graph.** The pipeline then predicts which supervoxels
belong to the same neuron, creating a graph where nodes are supervoxels
and edges represent "same neuron" predictions. Each connected component
of this graph is a segment (a putative neuron).

**Chunked storage.** The graph is spatially chunked, so edits to one
region do not require rewriting the entire graph. This enables concurrent
editing by multiple proofreaders without global locks.

### 2.2 Editing Model

- **Split operation.** The proofreader identifies a merge error and
  selects the boundary where the split should occur. CAVE removes one or
  more edges from the supervoxel graph, breaking the connected component
  into two segments. The underlying supervoxels and image data are never
  modified.
- **Merge operation.** The proofreader identifies two segments that should
  be one neuron and adds an edge between their supervoxels at the point
  of intended connection.

Because edits modify the graph rather than the image volume, they are
lightweight (a few bytes per edit) and instantaneous.

### 2.3 Materialization

CAVE periodically creates **materialization snapshots**: frozen states of
the segmentation graph plus all associated annotations (synapses, cell
types, etc.) at a specific timestamp. This means:

- Every analysis can cite a specific materialization version.
- Edits made after a materialization do not retroactively change published
  results.
- Reproducibility is built into the system: anyone can query the same
  materialization and get identical data.

### 2.4 Deployments

CAVE is used in:
- **FlyWire** (Princeton): whole Drosophila brain connectome.
- **MICrONS** (Allen Institute/Baylor/Princeton): 1 mm^3 mouse visual
  cortex.
- **Allen Institute** cortical datasets.

### 2.5 Instructor Tip

Emphasize the insight that decoupling proofreading from re-segmentation
was a paradigm shift. Before CAVE, fixing an error often meant re-running
part of the segmentation pipeline. With CAVE, an edit is a graph
operation that takes milliseconds.

---

## 3. Neuroglancer

### 3.1 Overview

Neuroglancer (Google) is a web-based volumetric data viewer that has
become the de facto standard for visualizing connectome data. It runs
entirely in the browser using WebGL for GPU-accelerated rendering.

### 3.2 Key Features

**Multi-panel layout.** By default, Neuroglancer shows four panels:
- XY (axial) view
- XZ (coronal) view
- YZ (sagittal) view
- 3D perspective view with mesh rendering

Users can customize the layout, hide panels, or add additional panels.

**Data sources.** Neuroglancer supports multiple data formats:
- Precomputed (CloudVolume format): chunked multi-resolution image and
  segmentation volumes stored in cloud storage (Google Cloud, AWS S3).
- N5 and Zarr: alternative chunked array formats.
- BOSS (Block Object Storage Service): the format used by some NIH-funded
  projects.

**Segmentation overlays.** Segmentation layers are rendered as colored
overlays on top of the grayscale EM data. Each segment gets a unique
color. Selected segments are highlighted; others can be dimmed or hidden.

**Annotation layers.** Points, lines, and bounding boxes can be added as
annotation layers. Synapse locations, cell body positions, and error
candidates are commonly displayed this way.

**3D mesh rendering.** Segment meshes (precomputed or generated on the
fly) are displayed in the 3D panel. Users can rotate, zoom, and inspect
morphology. Mesh quality depends on the resolution of the underlying mesh
computation.

### 3.3 Editing Integration

When connected to a CAVE backend, Neuroglancer supports direct
proofreading:
- **Split mode:** The user selects supervoxels on each side of the desired
  split boundary. CAVE computes the minimum graph cut and executes the
  split.
- **Merge mode:** The user selects a point on each of the two segments to
  be merged. CAVE adds the corresponding edge.

### 3.4 Shareable State

Every Neuroglancer view is encoded as a JSON state object. This state can
be serialized to a URL, enabling:
- **Reproducible navigation:** Share a link that opens Neuroglancer at
  exactly the same location, zoom level, and layer configuration.
- **Error reporting:** "Here is a link to a suspected merge error at
  coordinates (12045, 8823, 1456)."
- **Programmatic access:** The Python `nglui` library can generate
  Neuroglancer state URLs from data queries.

### 3.5 Python API

The `caveclient` and `nglui` Python packages allow programmatic
interaction:
- Query CAVE for segment IDs, synapse tables, and annotations.
- Generate Neuroglancer URLs that highlight specific neurons or synapses.
- Batch-generate links for proofreading task lists.

---

## 4. Spelunker

### 4.1 Overview

Spelunker is a proofreading interface developed collaboratively by
Princeton University and the Allen Institute for Brain Science. It is
built on top of CAVE and Neuroglancer but adds a workflow management
layer.

### 4.2 Key Features

- **Task management.** Proofreading tasks (e.g., "proofread neuron X" or
  "verify synapse Y") are assigned to annotators through a queue system.
- **Guided workflows.** Annotators follow structured protocols: navigate
  to a location, make a decision (correct / needs split / needs merge),
  execute the edit, move to the next task.
- **Quality tracking dashboards.** Supervisors can monitor: tasks
  completed per annotator, time per task, agreement rates on
  double-annotated tasks, and per-region quality metrics.
- **Integration.** Because it uses CAVE and Neuroglancer under the hood,
  all edits are version-controlled and all state is shareable.

### 4.3 When to Use

Spelunker is designed for organized proofreading campaigns with multiple
annotators. It is less suited for ad hoc exploration by individual
researchers (for that, plain Neuroglancer with CAVE is sufficient).

---

## 5. NeuTu

### 5.1 Overview

NeuTu is a desktop application developed at Janelia Research Campus
(Howard Hughes Medical Institute) for 3D proofreading. It was used
extensively in the Drosophila hemibrain project (Scheffer et al., 2020).

### 5.2 Key Features

- **Skeleton-based editing.** NeuTu emphasizes skeleton representations:
  each neuron is represented as a tree of connected nodes. Proofreaders
  navigate along the skeleton and fix errors.
- **Real-time 3D mesh updates.** When an edit is made (split or merge),
  the 3D mesh updates immediately, giving visual feedback.
- **Body annotation.** Neurons can be tagged with cell type labels,
  compartment labels (axon, dendrite, soma), and status flags (traced,
  needs review, orphan).
- **Desktop performance.** As a native application, NeuTu can achieve
  smoother rendering than browser-based tools for very large meshes.

### 5.3 Split and Merge in NeuTu

- **Split:** The user places "seeds" on the two sides of the desired
  split. NeuTu computes a cleave plane through the supervoxel graph and
  shows a preview. The user confirms or adjusts.
- **Merge:** The user selects two bodies and confirms the merge. NeuTu
  adds the appropriate edge to the backend graph (DVID, the Janelia
  data service).

### 5.4 When to Use

NeuTu is best suited for projects that use the Janelia/DVID
infrastructure and prefer a desktop application. Its skeleton-centric
design is particularly effective for tracing individual neurons.

---

## 6. CATMAID

### 6.1 Overview

CATMAID (Collaborative Annotation Toolkit for Massive Amounts of Image
Data), described by Saalfeld et al. (2009), is one of the earliest
collaborative annotation platforms for connectomics. It is a web-based
tool focused on skeleton tracing.

### 6.2 Historical Significance

CATMAID was central to several landmark connectomics studies:
- The Drosophila larval connectome (Ohyama et al., 2015).
- Early Drosophila adult brain circuit studies (Zheng et al., 2018).
- Numerous studies of smaller circuits in various organisms.

### 6.3 Key Features

- **Skeleton tracing.** Users place nodes and connect them to build a
  skeleton tree representing each neuron.
- **Collaborative.** Multiple annotators work on the same dataset
  simultaneously, with edits synchronized through a central server.
- **Annotation-rich.** Nodes can be tagged with labels (synapse,
  branch point, uncertain continuation). Connectors link pre- and
  postsynaptic partners.
- **Review workflow.** A reviewer can follow a skeleton node by node,
  confirming or correcting each placement.

### 6.4 Limitations

- **Manual skeleton placement.** Unlike CAVE-based tools that operate on
  automated segmentation, CATMAID historically required manual node
  placement. This is slower but can be more accurate in regions where
  automated segmentation fails.
- **No native volumetric segmentation editing.** CATMAID skeletons are
  annotations on top of the image; they do not directly modify a
  segmentation volume.
- **Scalability.** For very large datasets (petabyte scale), CATMAID's
  server architecture can become a bottleneck.

### 6.5 Modern Use

CATMAID is still actively maintained and used, particularly for projects
that rely on skeleton-based analysis or that started before CAVE-based
tools became available. Some projects use CATMAID for initial tracing
and then transfer skeletons to CAVE-integrated systems.

---

## 7. Editing Operations in Detail

Regardless of the tool used, proofreading involves a small set of core
operations.

### 7.1 Split

**Goal:** Separate two incorrectly merged neurons into distinct segments.

**Procedure (supervoxel graph systems):**
1. Identify the merge point in 2D slices.
2. Place selection points (seeds) on each side of the merge -- one on
   supervoxels belonging to neuron A, one on supervoxels belonging to
   neuron B.
3. The system computes a graph cut: the minimum set of edges to remove
   from the supervoxel graph so that the two seed sets are in different
   connected components.
4. The system shows a preview: two colored regions representing the
   proposed split.
5. The proofreader verifies that the split is correct (each side is a
   single, biologically plausible neuron) and confirms.

**Common pitfall:** Placing seeds too close to the merge point can result
in an ambiguous cut. Place seeds well away from the error, on regions you
are confident belong to different neurons.

### 7.2 Merge

**Goal:** Join two fragments that belong to the same neuron.

**Procedure:**
1. Identify the two fragments (e.g., an upstream segment ending at a dead
   end and a downstream orphan fragment).
2. Select a point on each fragment, ideally at the location where they
   should connect.
3. The system adds an edge between the supervoxels at those points,
   joining the two connected components into one segment.
4. Verify that the merged segment has continuous, plausible morphology.

**Common pitfall:** Merging the wrong fragment. Always verify caliber,
trajectory, and organelle content before confirming.

### 7.3 Extend (Manual Paint)

**Goal:** Fill in a gap where no supervoxels exist (e.g., a damaged
section where the tissue was lost).

**Procedure:**
1. Navigate to the gap.
2. Using a paint tool, manually draw the neurite's cross-section in each
   missing section.
3. The painted voxels are assigned to the appropriate segment.

This operation is rarer and more time-consuming than split/merge. It is
used only when the automated pipeline produced no supervoxels at all in
a region.

### 7.4 Delete (False Segment Removal)

**Goal:** Remove a segment that does not correspond to any real
biological structure (e.g., an artifact from a staining precipitate or
a dust particle on the section).

**Procedure:**
1. Identify the artifactual segment.
2. Mark it as "false" or "artifact" in the annotation system.
3. The segment is excluded from downstream analysis.

---

## 8. Comparing Tools

| Feature | CAVE + Neuroglancer | Spelunker | NeuTu | CATMAID |
|---|---|---|---|---|
| Platform | Web (browser) | Web (browser) | Desktop | Web (browser) |
| Backend | CAVE (supervoxel graph) | CAVE | DVID | PostgreSQL |
| Editing model | Graph split/merge | Graph split/merge | Graph split/merge | Skeleton node placement |
| 3D rendering | WebGL meshes | WebGL meshes | Native OpenGL meshes | Limited (skeleton only) |
| Task management | Manual (URLs) | Built-in queue | Limited | Review workflow |
| Version control | Materialization snapshots | Materialization snapshots | DVID versioning | Action log |
| Best for | General-purpose proofreading, exploration | Organized campaigns | Janelia ecosystem, skeleton tracing | Legacy projects, manual tracing |
| Scalability | Petabyte-scale | Petabyte-scale | Large datasets | Moderate |

---

## 9. Worked Example: Correcting a Merge Error in Neuroglancer/CAVE

### 9.1 Scenario

You are examining a pyramidal cell in the MICrONS dataset. In 3D, you
notice that one dendrite appears to branch into a process that suddenly
becomes much thinner and heads in an implausible direction. You suspect
a merge with a nearby axon.

### 9.2 Step-by-Step Workflow

1. **Navigate in 3D.** Rotate the mesh to identify the suspicious branch
   point. Note the approximate coordinates.

2. **Switch to 2D.** Click the suspicious region to center the 2D panels
   on that location. The XY panel shows the cross-section of the
   dendrite and the putative merged axon.

3. **Scroll through z.** Move through consecutive sections (z-1, z, z+1,
   etc.) to find the section(s) where the two processes touch. In this
   example, sections z=1023 to z=1025 show the dendrite and axon
   profiles merging into a single label.

4. **Activate split mode.** In Neuroglancer's toolbar, select the split
   tool (or use the keyboard shortcut, typically 'S' in CAVE-enabled
   Neuroglancer).

5. **Place seeds.** Click on a supervoxel that clearly belongs to the
   dendrite (e.g., at z=1020, well away from the merge). Then click on a
   supervoxel that clearly belongs to the axon (e.g., at z=1028, on the
   thin process after the branch point).

6. **Preview.** CAVE computes the graph cut and displays a preview: the
   dendrite in blue, the axon in red (or similar color scheme). Inspect
   both sides: does the blue segment look like a complete, plausible
   dendrite? Does the red segment look like a complete axon?

7. **Confirm.** If the preview looks correct, confirm the split. CAVE
   removes the offending edges from the supervoxel graph. The segment
   ID of the original neuron now refers only to the dendrite side; the
   axon side receives a new segment ID.

8. **Verify in 3D.** Refresh the mesh. The dendrite should now have
   smooth, continuous morphology without the implausible branch. The
   axon should appear as a separate segment.

9. **Check synapses.** Any synapses that were located on the now-separated
   axon are automatically re-assigned to the new segment ID. Verify that
   no synapses near the merge point were incorrectly assigned.

10. **Document.** The edit is automatically logged in CAVE with your user
    ID, timestamp, and the specific graph edges removed.

---

## 10. References

- Dorkenwald, S., et al. (2022). FlyWire: Online community for whole-brain
  connectomics. *Nature Methods*, 19, 119-128.
- Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult
  brain. *Nature*, 634, 124-138.
- Saalfeld, S., Cardona, A., Hartenstein, V., & Tomancak, P. (2009).
  CATMAID: Collaborative annotation toolkit for massive amounts of image
  data. *Bioinformatics*, 25(15), 1984-1986.
- Scheffer, L. K., et al. (2020). A connectome and analysis of the adult
  Drosophila central brain. *eLife*, 9, e57443.
- Ohyama, T., et al. (2015). A multilevel multimodal circuit enhances
  action selection in Drosophila. *Nature*, 520, 633-639.
- Zheng, Z., et al. (2018). A complete electron microscopy volume of the
  brain of adult Drosophila melanogaster. *Cell*, 174(3), 730-743.

---

*End of instructor script: Proofreading Tools for Connectome Reconstruction*
