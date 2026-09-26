---
layout: page
title: "Proofreading Tools for Connectome Reconstruction"
permalink: /content-library/proofreading/proofreading-tools/
image: /assets/images/content-library/proofreading/proofreading-tools.svg
image_alt: "Stylized vector art: a traced process with marked error sites under review."
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
  - "08"
  - "04"
difficulty: intermediate
tags:
  - proofreading:edit-operations
  - infrastructure:cave
  - infrastructure:neuroglancer
  - infrastructure:spelunker
  - infrastructure:catmaid
  - connectomics:supervoxel-graph
  - methodology:proofreading-workflow
micro_lesson_id: ml-proof-tools
combines_with:
  - error-taxonomy
  - proofreading-strategies
  - worked-examples
use_layout_hero: false
content_type: core
---

# Proofreading Tools for Connectome Reconstruction

## Instructor Notes

This is a standalone instructor script on the main software used for
connectome proofreading: how each tool stores edits, what a split and a
merge look like in it, and where it fits. Students who will edit data
need more time on interface mechanics. Students who will only analyze
data need more on how the tool shapes provenance, because it decides
which IDs and versions they will cite.

Interfaces change faster than this page. Button names and keyboard
shortcuts are left out on purpose; send students to the current
documentation for the viewer their project uses.

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

No single tool does all five. Most projects combine a backend that
stores the segmentation and its edit history, a browser or desktop viewer,
and some separate way to hand out tasks and track quality.

---

## 2. CAVE (Connectome Annotation Versioning Engine)

### 2.1 Architecture

CAVE (Dorkenwald et al., 2025) is a set of web services for proofreading
and annotating large EM datasets while many people edit them at once. Its
core is the **chunked supervoxel graph** (the ChunkedGraph), first used for
FlyWire (Dorkenwald et al., 2022).

**Supervoxels.** The automated segmentation pipeline produces an
over-segmentation: millions of small, conservatively drawn segments called
supervoxels. Each supervoxel is an atomic unit that is never subdivided
during proofreading.

**Agglomeration graph.** The pipeline then predicts which supervoxels
belong to the same neuron, creating a graph where nodes are supervoxels
and edges represent "same neuron" predictions. Each connected component
of this graph is a segment (a putative neuron).

**Chunked storage.** The graph is split into spatial chunks, so an edit
rewrites only the chunks it touches, not the whole graph. That is what lets
many proofreaders edit the same dataset at the same time.

### 2.2 Editing Model

- **Split operation.** The proofreader marks points on each side of a
  merge error. The ChunkedGraph treats the supervoxels under those points
  as sources and sinks, runs a max-flow/min-cut, and removes the edges the
  cut finds, breaking the connected component into two segments. The
  underlying supervoxels and image data are never modified.
- **Merge operation.** The proofreader identifies two segments that should
  be one neuron and adds an edge between their supervoxels at the point
  of intended connection.

Because edits change the graph rather than the image volume, an edit
does not rewrite voxels. It still changes the cell identity of every voxel
and annotation on the affected object, which is why CAVE tracks IDs over
time.

After an edit, the affected object gets new root IDs: the old root ID is
retired, and each resulting segment receives a new one. This is why code
that stores a root ID can silently point at an outdated object later.

### 2.3 Materialization

Annotations such as synapses are stored as points bound to supervoxels,
so CAVE can say which root ID each point belonged to at any time. CAVE
periodically creates **materialization snapshots**: copies of the
annotation tables with every point mapped to its root ID at one timestamp.
This means:

- An analysis can cite a materialization version (or a timestamp).
- Edits made after that version do not change results computed from it.
- Anyone who queries the same version gets the same tables, **while that
  version is still served**. Versions are not permanent. MICrONS, for
  example, keeps a few major analysis versions (943 and 1300) available
  long-term and archives most others; v1507 was scheduled to leave the
  live service on 31 July 2026. Record the version and keep a copy of the
  tables you used.

### 2.4 Deployments

The CAVE paper (Dorkenwald et al., 2025) lists five published datasets
proofread or analyzed with it:
- **FlyWire**: whole adult *Drosophila* brain.
- **FANC**: *Drosophila* ventral nerve cord.
- **MICrONS phase 1** and the **MICrONS cubic millimeter** (minnie65):
  mouse visual cortex.
- **H01**: human temporal cortex.

### 2.5 Instructor Tip

The point to land is timing. The CAVE authors note that earlier tools and
workflows offered only static exports once proofreading was finished.
With CAVE, people can run analyses while proofreading is still going on,
and still say exactly which state of the data they used. The price is
that IDs change under you, so every result needs a version or timestamp.

---

## 3. Neuroglancer

### 3.1 Overview

Neuroglancer, developed at Google, is a browser-based viewer for
volumetric data. Most large public connectomes can be opened in it. It
renders on the GPU through WebGL and needs no installation.

### 3.2 Key Features

**Multi-panel layout.** The default four-panel layout shows three
orthogonal cross-sections (XY, XZ and YZ) and a 3D view with meshes. These
are the volume's own axes, not anatomical planes: whether XZ is coronal
depends on how the tissue was cut. The layout can be changed to a single
panel or other arrangements.

**Data sources.** Neuroglancer supports multiple data formats:
- Precomputed (CloudVolume format): chunked multi-resolution image and
  segmentation volumes stored in cloud storage (Google Cloud, AWS S3).
- N5 and Zarr: alternative chunked array formats.
- BossDB (Block and Object Storage Service): a cloud archive for
  volumetric neuroimaging data.

**Segmentation overlays.** Segmentation layers are drawn as colored
overlays on the grayscale EM. Each segment gets its own color, and
selected segments can be shown alone.

**Annotation layers.** Points, lines, and bounding boxes can be added as
annotation layers. Synapse locations, cell body positions, and error
candidates are commonly displayed this way.

**3D mesh rendering.** Segment meshes are shown in the 3D panel. Mesh
detail depends on the resolution the meshes were computed at, and a mesh
can lag behind a recent edit, so check 2D slices before trusting a thin
bridge you see in 3D.

### 3.3 Editing Integration

When connected to a CAVE backend (a "graphene" segmentation source),
Neuroglancer supports direct proofreading:
- **Split (multicut):** The user places points of one color on one side of
  the merge and points of a second color on the other side. CAVE computes a
  minimum cut between them, shows a preview, and executes the split.
- **Merge:** The user draws a connector between a point on each of the two
  segments. CAVE adds an edge between the supervoxels under those points.

### 3.4 Shareable State

Every Neuroglancer view is encoded as a JSON state object. This state can
be serialized to a URL, enabling:
- **Reproducible navigation:** Share a link that opens Neuroglancer at
  the same location, zoom level, and layer configuration. The link stores
  segment IDs, so after an edit it may show an outdated object.
- **Error reporting:** "Here is a link to a suspected merge error at
  voxel (12045, 8823, 1456)." Always give the voxel resolution with the
  coordinates.
- **Programmatic access:** The Python `nglui` library can build
  Neuroglancer states from data queries.

### 3.5 Python API

The `caveclient` and `nglui` Python packages cover the same ground from
code:
- Query CAVE for segment IDs, synapse tables, and annotations.
- Generate Neuroglancer URLs that highlight specific neurons or synapses.
- Batch-generate links for proofreading task lists.

---

## 4. Spelunker

### 4.1 Overview

Spelunker (`spelunker.cave-explorer.org`) is a build of Neuroglancer for
proofreading and annotating large EM datasets through CAVE. It is a viewer,
not a separate backend: edits go to the same CAVE ChunkedGraph as any other
CAVE-connected client.

### 4.2 Key Features

- **Proofreading in the viewer.** Split and merge operations are carried
  out directly in the Neuroglancer interface, largely through key presses.
- **Integration.** Because it uses CAVE and Neuroglancer under the hood,
  all edits are version-controlled and all state is shareable.

### 4.3 When to Use

Use Spelunker when a CAVE datastack's documentation points you to it for
proofreading. Task assignment and progress tracking for a campaign are
handled outside the viewer, by whatever tools the project provides (for
example, lists of Neuroglancer links generated with `nglui`).

---

## 5. NeuTu

### 5.1 Overview

NeuTu is a desktop application developed at Janelia Research Campus
(Howard Hughes Medical Institute) for collaborative, segmentation-based
proofreading (Zhao et al., 2018). Its authors report that it supported the
fly medulla and mushroom body reconstructions, and Janelia's proofreading
tools were used in the *Drosophila* hemibrain project (Scheffer et al., 2020).
The CAVE authors describe NeuTu as supporting neuron-based proofreading at
scale for a restricted group of proofreaders, in contrast to CAVE's open
community model (Dorkenwald et al., 2025).

### 5.2 Key Features

- **Segmentation-based editing.** NeuTu works on a voxel segmentation
  rather than on hand-placed skeletons: proofreaders correct the labels of
  bodies in the volume.
- **2D and 3D views.** Proofreaders work in both image slices and 3D body
  renderings.
- **Versioned backend.** NeuTu is a client of DVID, Janelia's distributed,
  versioned, image-oriented data service.
- **Desktop application.** NeuTu runs as a native program rather than in
  the browser.

### 5.3 Split and Merge in NeuTu

- **Split:** The user paints seeds of different colors on the regions
  that belong to different neurons, in 2D or 3D. NeuTu runs a seeded
  watershed on the grayscale data to separate the bodies, with a local
  preview.
- **Merge:** The user selects the bodies to join. DVID assigns one ID to
  all their voxels.

### 5.4 When to Use

NeuTu is best suited for projects that use the Janelia/DVID
infrastructure and prefer a desktop application.

---

## 6. CATMAID

### 6.1 Overview

CATMAID (Collaborative Annotation Toolkit for Massive Amounts of Image
Data), described by Saalfeld et al. (2009), is one of the earliest
collaborative annotation platforms for connectomics. It runs in the
browser and is built around skeleton tracing.

### 6.2 Where it has been used

CATMAID was the tracing tool for several major fly studies:
- Larval *Drosophila* circuit studies (e.g., Ohyama et al., 2015) and the
  complete larval brain connectome, 3,016 neurons (Winding et al., 2023).
- The first circuit reconstructions in the whole adult fly brain volume,
  FAFB (Zheng et al., 2018).

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

- **Manual skeleton placement.** Unlike CAVE-based tools that edit an
  automated segmentation, classic CATMAID tracing places every node by
  hand. It is slower, but it does not depend on the segmentation being
  right.
- **No volumetric segmentation editing.** CATMAID skeletons are
  annotations on top of the image; they do not change a segmentation
  volume, so they give no neuron volumes or surface areas.
- **Throughput.** The limit is annotator time rather than image size:
  FAFB (about 106 TB) was traced in CATMAID, but hand tracing a whole
  brain's neurons this way would take far more person-hours than
  proofreading an automated segmentation.

### 6.5 Modern Use

CATMAID is still maintained and used, especially by projects built on
skeleton analysis and by projects that started before CAVE existed.

---

## 7. Editing Operations in Detail

Regardless of the tool used, proofreading involves a small set of core
operations.

### 7.1 Split

**Goal:** Separate two incorrectly merged neurons into distinct segments.

**Procedure (supervoxel graph systems):**
1. Identify the merge point in 2D slices.
2. Place selection points (seeds) on each side of the merge: some on
   supervoxels belonging to neuron A, some on supervoxels belonging to
   neuron B.
3. The system computes a graph cut: the minimum set of edges to remove
   from the supervoxel graph so that the two seed sets are in different
   connected components.
4. The system shows a preview: two colored regions representing the
   proposed split.
5. The proofreader verifies that the split is correct (each side is a
   single, biologically plausible neuron) and confirms.

**Common pitfall:** Too few seeds, placed far from the merge, leave the
cut free to fall in the wrong place. FlyWire's own guide says to scroll to
near where the merge begins and place a number of points on each side,
working in 2D when the branches are intertwined (FlyWire 101,
blog.flywire.ai, 2022). Put every seed on a profile you are sure of, and
check the preview before confirming.

### 7.2 Merge

**Goal:** Join two fragments that belong to the same neuron.

**Procedure:**
1. Identify the two fragments (e.g., an upstream segment ending at a dead
   end and a downstream orphan fragment).
2. Select a point on each fragment, ideally at the location where they
   should connect.
3. The system adds an edge between the supervoxels under those points,
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

This is rarer and slower than split or merge, and not every tool offers
it. CAVE's ChunkedGraph edits only the graph of existing supervoxels, so it
cannot paint new voxels; voxel-painting tools such as VAST (Berger et al.,
2018) can.

### 7.4 Delete (False Segment Removal)

**Goal:** Remove a segment that does not correspond to any real
biological structure (e.g., an artifact from a staining precipitate or
a dust particle on the section).

**Procedure:**
1. Identify the artifactual segment.
2. Mark it as "false" or "artifact" in the project's annotation tables.
   In graph-based systems the supervoxels usually stay; the label is what
   removes the object from analysis.
3. Downstream queries exclude it only if they filter on that label, so
   say so in the analysis methods.

---

## 8. Comparing Tools

| Feature | CAVE + Neuroglancer | Spelunker | NeuTu | CATMAID |
|---|---|---|---|---|
| Platform | Web (browser) | Web (browser) | Desktop | Web (browser) |
| Backend | CAVE (supervoxel graph) | CAVE | DVID | PostgreSQL |
| Editing model | Graph split/merge | Graph split/merge | Seeded-watershed split, label merge | Skeleton node placement |
| 3D rendering | WebGL meshes | WebGL meshes | Native desktop rendering | Limited (skeleton only) |
| Task management | Manual (URLs) | Manual (URLs) | Limited | Review workflow |
| Version control | Materialization snapshots | Materialization snapshots | DVID versioning | Action log |
| Best for | General-purpose proofreading, exploration | CAVE datastacks that recommend it | Janelia/DVID ecosystem | Skeleton-based projects, manual tracing |
| Largest published use | ~1 mm³ volumes (MICrONS, H01) | Same backend as CAVE | Hemibrain (26 teravoxels) | FAFB (~106 TB) |

---

## 9. Worked Example: Correcting a Merge Error in Neuroglancer/CAVE

### 9.1 Scenario

You are examining a pyramidal cell in release T77 of a fictional mouse
cortex volume, served through a CAVE-backed Neuroglancer. The volume, the
release and the section numbers are invented for this exercise. In 3D, you
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

4. **Activate split mode.** Select the split (multicut) tool. The control
   and any keyboard shortcut differ between Neuroglancer builds, so check
   the documentation for the one your project uses.

5. **Place seeds.** Place several points on profiles that clearly belong
   to the dendrite, from z=1020 up to z=1023 where the merge begins. Then
   place several points of the other color on the axon, from z=1025 to
   z=1028 on the thin process past the branch point. Seeds near the merge
   pin the cut there; seeds farther out stop it from taking a shortcut
   elsewhere.

6. **Preview.** CAVE computes the graph cut and displays a preview of the
   two sides in different colors. Inspect both sides: does the dendrite
   side look like a complete, plausible dendrite? Does the axon side look
   like a complete axon?

7. **Confirm.** If the preview looks correct, confirm the split. CAVE
   removes the offending edges from the supervoxel graph. The original
   root ID is retired, and both the dendrite side and the axon side
   receive new root IDs.

8. **Verify in 3D.** Reload the meshes. The dendrite should now have
   smooth, continuous morphology without the implausible branch. The
   axon should appear as a separate segment.

9. **Check synapses.** Synapse annotations are bound to supervoxels, so
   live queries and the next materialization attribute them to the new
   root IDs without manual reassignment. Check the synapses near the cut:
   if a supervoxel itself straddled the two processes, its synapses can
   still land on the wrong side.

10. **Document.** CAVE logs the operation with your user ID and a
    timestamp. Add a note in the project's tracking sheet or annotation
    table saying why you split, since the log records what changed but
    not your reasoning.

---

## 10. References

- Berger, D. R., Seung, H. S., & Lichtman, J. W. (2018). VAST (Volume
  Annotation and Segmentation Tool): Efficient manual and semi-automatic
  labeling of large 3D image stacks. *Frontiers in Neural Circuits*, 12, 88.
- Dorkenwald, S., et al. (2022). FlyWire: Online community for whole-brain
  connectomics. *Nature Methods*, 19, 119-128.
- Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult
  brain. *Nature*, 634, 124-138.
- Dorkenwald, S., Schneider-Mizell, C. M., et al. (2025). CAVE: Connectome
  Annotation Versioning Engine. *Nature Methods*, 22, 1112-1120.
  doi:10.1038/s41592-024-02426-z.
- Zhao, T., Olbris, D. J., Yu, Y., & Plaza, S. M. (2018). NeuTu: Software
  for collaborative, large-scale, segmentation-based connectome
  reconstruction. *Frontiers in Neural Circuits*, 12, 101.
- Saalfeld, S., Cardona, A., Hartenstein, V., & Tomancak, P. (2009).
  CATMAID: Collaborative annotation toolkit for massive amounts of image
  data. *Bioinformatics*, 25(15), 1984-1986.
- Scheffer, L. K., et al. (2020). A connectome and analysis of the adult
  Drosophila central brain. *eLife*, 9, e57443.
- Ohyama, T., et al. (2015). A multilevel multimodal circuit enhances
  action selection in Drosophila. *Nature*, 520, 633-639.
- Zheng, Z., et al. (2018). A complete electron microscopy volume of the
  brain of adult Drosophila melanogaster. *Cell*, 174(3), 730-743.
- Winding, M., et al. (2023). The connectome of an insect brain.
  *Science*, 379, eadd9330.
- FlyWire (2022). FlyWire 101. FlyWire Blog,
  <https://blog.flywire.ai/2022/04/22/flywire-101/> (read 26 September 2026).

---

*End of instructor script: Proofreading Tools for Connectome Reconstruction*
