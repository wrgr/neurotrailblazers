---
layout: page
title: "Journal Papers: Imaging & Sample Preparation"
permalink: /content-library/journal-papers/imaging/
description: "Curated papers on EM imaging methods for connectomics with summaries at beginner, intermediate, and advanced levels."
dimension: imaging
tags:
  - imaging:electron-microscopy
  - imaging:SEM
  - imaging:TEM
  - imaging:FIB-SEM
  - imaging:SBEM
  - imaging:ATUM
  - imaging:serial-section
---

# Imaging & Sample Preparation Journal Papers

Curated papers covering electron microscopy acquisition, sample preparation, and imaging pipelines. Each paper includes summaries at three expertise levels.

---

## 1. Denk & Horstmann (2004) — Serial Block-Face Scanning Electron Microscopy

**Citation:** Denk W, Horstmann H. Serial block-face scanning electron microscopy to reconstruct three-dimensional tissue nanostructure. *PLoS Biology*. 2004;2(11):e329.
**DOI:** [10.1371/journal.pbio.0020329](https://doi.org/10.1371/journal.pbio.0020329)

**Tags:** `imaging:SBEM` `imaging:SEM` `imaging:serial-section` `imaging:electron-microscopy` `methodology:experimental-design`

### Summaries

**Beginner:** This paper invented a new way to image brain tissue in 3D. Instead of cutting tissue into slices and imaging each one separately, the authors built a miniature cutting device inside the microscope itself. After imaging the surface, the device shaves off a thin layer and images the new surface — repeat thousands of times to build a 3D picture. This made 3D brain imaging much faster and more reliable than previous methods.

**Intermediate:** Denk and Horstmann introduced serial block-face SEM (SBEM), where an ultramicrotome mounted inside an SEM chamber iteratively sections and images a resin-embedded tissue block. This approach eliminates the need for section collection and handling, dramatically reducing alignment errors and lost sections. The paper demonstrates the technique on nervous tissue, achieving ~25 nm lateral and ~25-30 nm axial resolution. SBEM became one of the two dominant imaging modalities for large-scale connectomics (alongside ATUM-SEM).

**Advanced:** The key engineering insight was that back-scattered electron imaging of the block face provides sufficient contrast from heavy-metal-stained tissue without requiring transmitted electrons. The resolution-throughput tradeoffs are important: SBEM provides isotropic-ish voxels (good for segmentation) but the sections are destroyed during imaging (no re-imaging possible). Beam damage accumulates in deeper layers. Modern implementations (Gatan 3View, Zeiss Gemini) have improved automation and throughput, but the fundamental tradeoffs identified here persist. Compare with FIB-SEM for true isotropic voxels and ATUM-SEM for section preservation.

**Key figures:** Fig. 1 (SBEM schematic), Fig. 2 (block-face image quality), Fig. 4 (3D neural reconstruction)

**Discussion prompts:**
- What are the tradeoffs between destroying sections (SBEM) versus preserving them (ATUM)?
- How does the choice of SBEM versus FIB-SEM versus ATUM affect downstream segmentation quality?
- What acquisition QA metrics would you add to this workflow if designing it today?

**Related content:** [EM principles](/content-library/imaging/em-principles/), [Tissue preparation](/content-library/imaging/tissue-preparation/)

---

## 2. Knott et al. (2008) — Serial Section Scanning Electron Microscopy of Adult Brain Tissue

**Citation:** Knott G, Marchman H, Wall D, Lich B. Serial section scanning electron microscopy of adult brain tissue using focused ion beam milling. *Journal of Neuroscience*. 2008;28(12):2959-2964.
**DOI:** [10.1523/JNEUROSCI.3189-07.2008](https://doi.org/10.1523/JNEUROSCI.3189-07.2008)

**Tags:** `imaging:FIB-SEM` `imaging:SEM` `imaging:electron-microscopy` `neuroanatomy:synapse` `methodology:experimental-design`

### Summaries

**Beginner:** This paper showed how to use a focused beam of ions (like a tiny sandblaster) to slice brain tissue inside an electron microscope, producing truly cube-shaped 3D pixels. Previous methods cut thicker slices, making the images stretched in one direction. With FIB-SEM, every direction has the same resolution, making it easier to trace thin neural processes that run in any direction.

**Intermediate:** Knott et al. demonstrated FIB-SEM for neural tissue, achieving isotropic voxels (~5-10 nm in all dimensions) by using a gallium ion beam to mill away thin layers between SEM imaging passes. This isotropic resolution is particularly valuable for tracing thin processes (spines, boutons, small-caliber axons) that may be missed or misidentified in anisotropic datasets. The tradeoff is dramatically slower acquisition throughput compared with SBEM or ATUM-SEM.

**Advanced:** FIB-SEM's isotropic resolution eliminates the z-anisotropy that plagues segmentation in serial section datasets, where ~30-50 nm axial resolution versus ~4-8 nm lateral resolution creates directionally biased errors. The Knott et al. implementation achieves ~5 nm isotropic but at volumes orders of magnitude smaller than SBEM datasets. Modern enhanced FIB-SEM (Xu et al., 2017) has pushed volumes to ~10⁶ μm³ while maintaining isotropy. The choice between FIB-SEM and SBEM depends on whether the scientific question requires isotropy (spine morphology, organelle quantification) or volume (circuit mapping).

**Key figures:** Fig. 1 (FIB-SEM geometry), Fig. 2 (isotropic voxel demonstration), Fig. 3 (synapse reconstruction)

**Discussion prompts:**
- For which biological questions is isotropic resolution essential versus merely nice-to-have?
- How does the volume limitation of FIB-SEM affect the kinds of connectomics questions you can ask?

**Related content:** [EM principles](/content-library/imaging/em-principles/), [Acquisition QA](/content-library/imaging/acquisition-qa/)

---

## 3. Zheng et al. (2018) — A Complete Electron Microscopy Volume of the Brain of Adult Drosophila melanogaster

**Citation:** Zheng Z, Lauritzen JS, Perlman E, Robinson CG, Nichols M, Milkie D, et al. A complete electron microscopy volume of the brain of adult *Drosophila melanogaster*. *Cell*. 2018;174(3):730-743.e22.
**DOI:** [10.1016/j.cell.2018.06.019](https://doi.org/10.1016/j.cell.2018.06.019)

**Tags:** `imaging:ATUM` `imaging:serial-section` `imaging:SEM` `case-studies:Drosophila` `case-studies:FAFB` `case-studies:whole-brain` `infrastructure:pipeline`

### Summaries

**Beginner:** This paper describes how scientists imaged an entire adult fruit fly brain at nanometer resolution — about 21 million images stitched together. The fruit fly brain is tiny (smaller than a poppy seed) but contains about 100,000 neurons. Imaging it completely took years of work and produced a dataset that became the foundation for mapping the fly's entire wiring diagram.

**Intermediate:** Zheng et al. produced the FAFB (Full Adult Fly Brain) dataset using ATUM-SEM: serial sections collected on tape, then imaged across multiple SEMs. The dataset spans the entire *Drosophila* brain at ~4x4x40 nm voxels (~21 million tiles, ~50 TB). Key technical achievements include maintaining section continuity over ~7,000 sections, multi-microscope parallelization for throughput, and computational alignment of the complete volume. This dataset enabled the FlyWire collaborative reconstruction project.

**Advanced:** The FAFB acquisition pipeline illustrates the engineering challenges of petascale EM: section loss mitigation (only 36 of ~7,000 sections were unusable), tape-based ATUM collection enabling re-imaging, and the multi-microscope parallelization that made the project feasible within a few years. The anisotropic voxels (4x4x40 nm) create z-resolution limitations for thin-process tracing, partially addressed by FlyWire's flood-filling network segmentation. Compare with the Janelia hemibrain (FIB-SEM, isotropic 8 nm, smaller volume, better z-resolution) to understand how imaging modality choice propagates through reconstruction quality.

**Key figures:** Fig. 1 (whole-brain overview), Fig. 2 (ATUM workflow), Fig. 3 (section quality metrics), S-Fig. 1 (multi-microscope setup)

**Discussion prompts:**
- How does the 10x anisotropy (4 nm xy vs 40 nm z) affect segmentation accuracy for different neurite calibers?
- What would change if this brain were imaged today with current FIB-SEM or enhanced SBEM technology?
- How do you handle the 36 missing sections in downstream reconstruction?

**Related content:** [Acquisition QA](/content-library/imaging/acquisition-qa/), [FlyWire whole-brain](/content-library/case-studies/flywire-whole-brain/), [Reconstruction pipeline](/content-library/infrastructure/reconstruction-pipeline/)

---

## 4. Xu et al. (2017) — Enhanced FIB-SEM Imaging for Cell Biology

**Citation:** Xu CS, Hayworth KJ, Lu Z, Grob P, Hassan AM, García-Cerdán JG, et al. Enhanced FIB-SEM systems for large-volume 3D imaging. *eLife*. 2017;6:e25916.
**DOI:** [10.7554/eLife.25916](https://doi.org/10.7554/eLife.25916)

**Tags:** `imaging:FIB-SEM` `imaging:electron-microscopy` `imaging:resolution` `infrastructure:scalability` `methodology:experimental-design`

### Summaries

**Beginner:** Regular FIB-SEM produces beautiful 3D images with equal resolution in all directions, but can only image tiny volumes. This paper describes engineering improvements — better ion beam control, automated error recovery, longer run times — that increased the imageable volume by more than 100-fold. This made FIB-SEM practical for imaging entire brain regions rather than just tiny patches.

**Intermediate:** Xu et al. describe systematic engineering improvements to FIB-SEM that enable continuous imaging over weeks to months, producing volumes exceeding 10⁶ μm³ at 8 nm isotropic resolution. Key innovations include automated FIB milling error detection and correction, improved beam stability, and sample preparation optimized for long-duration milling. The enhanced platform was used to produce the Janelia hemibrain dataset (*Drosophila* central brain, ~25,000 neurons).

**Advanced:** The engineering contributions here — fault recovery, drift compensation, long-term beam stability — are what enabled the hemibrain project and subsequent FIB-SEM connectomics efforts. The system achieves 4-8 nm isotropic voxels over ~10⁶ μm³, a volume-resolution product previously inaccessible. Compare the tradeoff space: FAFB achieved 10x larger volume at 10x worse z-resolution; the hemibrain achieved 10x better z-resolution at 10x smaller volume. The isotropy advantage is most evident for small-caliber neurites (which represent the majority of wiring), where anisotropic datasets systematically underperform in segmentation accuracy.

**Key figures:** Fig. 1 (enhanced FIB-SEM system), Fig. 3 (volume comparison with conventional FIB-SEM), Fig. 5 (biological samples at isotropic resolution)

**Discussion prompts:**
- At what volume scale does the isotropy advantage of FIB-SEM outweigh the throughput advantage of ATUM-SEM?
- How do you choose between isotropy and volume when designing a connectomics experiment?

**Related content:** [EM principles](/content-library/imaging/em-principles/), [Tissue preparation](/content-library/imaging/tissue-preparation/)

---

## 5. Hayworth et al. (2014) — Ultrathick Sections for Large-Volume ATUM-SEM

**Citation:** Hayworth KJ, Xu CS, Lu Z, Knott GW, Chklovskii DB, Bhola S, et al. Ultrastructurally-smooth thick partitioning and volume stitching for large-scale connectomics. *Nature Methods*. 2015;12(4):319-322.
**DOI:** [10.1038/nmeth.3292](https://doi.org/10.1038/nmeth.3292)

**Tags:** `imaging:ATUM` `imaging:serial-section` `imaging:SEM` `infrastructure:pipeline` `infrastructure:alignment` `methodology:experimental-design`

### Summaries

**Beginner:** Cutting brain tissue into thousands of ultra-thin slices is slow and error-prone. This paper developed a method to cut slightly thicker slices, image them from both sides, and computationally stitch the results together. This approach makes it possible to image larger brain volumes faster, while still getting good enough resolution to trace neural connections.

**Intermediate:** Hayworth et al. address a throughput bottleneck in serial section EM by developing "hot knife" thick-section partitioning. A heated diamond blade cuts resin-embedded brain tissue into ~20 μm thick slabs with minimal surface damage. Each slab is then sectioned conventionally (40 nm) for ATUM-SEM, and the resulting sub-volumes are computationally stitched. This enables parallelized imaging across multiple microscopes and reduces the contiguous-section-series length required from any single sectioning run.

**Advanced:** The volume stitching approach relaxes the single greatest reliability constraint in serial section connectomics — the requirement for unbroken section series spanning the entire volume. By accepting controlled cuts at ~20 μm intervals, the method tolerates lost sections within slabs (since slab-to-slab continuity is established through overlap) and enables multi-microscope parallelism. The surface quality of hot-knife cuts is critical; the paper reports sub-100 nm surface roughness. This approach was subsequently used in the MICrONS mm³ volume acquisition pipeline.

**Key figures:** Fig. 1 (hot knife sectioning), Fig. 2 (slab-to-slab stitching), Fig. 3 (volume reconstruction from stitched slabs)

**Discussion prompts:**
- What are the error modes specific to slab-to-slab stitching that don't exist in continuous serial sections?
- How does this approach change the cost-benefit analysis for very large volumes?

**Related content:** [Reconstruction pipeline](/content-library/infrastructure/reconstruction-pipeline/), [Acquisition QA](/content-library/imaging/acquisition-qa/)

---

## 6. Yin et al. (2020) — A Petascale Automated Imaging Pipeline

**Citation:** Yin W, Brittain D, Bhardwaj J, Ward R, Aung HN, Mader KS, et al. A petascale automated imaging pipeline for mapping neuronal circuits with high-throughput transmission electron microscopy. *Nature Communications*. 2020;11:4949.
**DOI:** [10.1038/s41467-020-18659-3](https://doi.org/10.1038/s41467-020-18659-3)

**Tags:** `imaging:TEM` `imaging:ATUM` `imaging:serial-section` `infrastructure:pipeline` `infrastructure:scalability` `case-studies:MICrONS`

### Summaries

**Beginner:** To map the wiring of even a small piece of mouse brain, you need to take millions of images and assemble them into one continuous 3D volume. This paper describes the industrial-scale imaging system used for the MICrONS project — multiple electron microscopes running simultaneously, automated quality checks, and software to stitch everything together. It's the imaging factory that produced one of the largest connectomics datasets.

**Intermediate:** Yin et al. describe the multi-beam TEM imaging pipeline used for the MICrONS mm³ cortical volume. Key engineering contributions include automated stage control for continuous imaging, real-time QA feedback for detecting focus and contrast issues, parallel operation of multiple TEMs, and computational infrastructure for petabyte-scale image assembly. The pipeline achieved sustained throughput of ~1 megapixel/second per microscope, imaging the full volume in months rather than decades.

**Advanced:** This paper is essential reading for understanding the industrialization of connectomics imaging. The QA architecture — automated focus assessment, contrast monitoring, section damage detection, and real-time re-imaging decisions — represents a mature approach to acquisition reliability at scale. The pipeline handles the full ingest chain from ATUM tape to cloud-stored, aligned, multi-resolution image pyramids. Notable is the choice of multi-beam TEM over SEM for throughput, accepting the additional complexity of transmission imaging setup. The paper provides concrete throughput numbers useful for planning future large-scale acquisitions.

**Key figures:** Fig. 1 (pipeline overview), Fig. 3 (QA dashboard), Fig. 4 (throughput metrics), Fig. 6 (assembled volume quality)

**Discussion prompts:**
- What are the bottlenecks in this pipeline, and which are engineering versus fundamental physics limits?
- How would you design an acquisition QA system for a dataset 10x larger than MICrONS?

**Related content:** [Acquisition QA](/content-library/imaging/acquisition-qa/), [Reconstruction pipeline](/content-library/infrastructure/reconstruction-pipeline/), [MICrONS visual cortex](/content-library/case-studies/microns-visual-cortex/)
