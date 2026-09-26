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
use_layout_hero: false
content_type: core
---

# Imaging & Sample Preparation Journal Papers

Curated papers covering electron microscopy acquisition, sample preparation, and imaging pipelines. Each paper includes summaries at three expertise levels.

---

## 1. Denk & Horstmann (2004) — Serial Block-Face Scanning Electron Microscopy

**Citation:** Denk W, Horstmann H. Serial block-face scanning electron microscopy to reconstruct three-dimensional tissue nanostructure. *PLoS Biology*. 2004;2(11):e329.
**DOI:** [10.1371/journal.pbio.0020329](https://doi.org/10.1371/journal.pbio.0020329)

**Tags:** `imaging:SBEM` `imaging:SEM` `imaging:serial-section` `imaging:electron-microscopy` `methodology:experimental-design`

### Summaries

**Beginner:** This paper invented a new way to image brain tissue in 3D. Instead of cutting tissue into slices and imaging each one separately, the authors built a miniature cutting device inside the microscope itself. After imaging the surface, the device shaves off a thin layer and images the new surface — repeat thousands of times to build a 3D picture. Because the block never leaves the microscope, the images come out already in register.

**Intermediate:** Denk and Horstmann introduced serial block-face SEM (SBEM), where an ultramicrotome mounted inside an SEM chamber iteratively sections and images a resin-embedded tissue block. This removes section collection and handling, and with them most alignment errors and lost sections. The paper demonstrates the technique on nervous tissue, with stacks of several hundred sections 50-70 nm thick and resolution sufficient to trace the thinnest axons and identify synapses. SBEM became one of the main imaging methods for large-scale connectomics.

**Advanced:** The key engineering insight was that back-scattered electron imaging of the block face provides sufficient contrast from heavy-metal-stained tissue without requiring transmitted electrons. The tradeoffs matter: SBEM stacks are self-registered (good for segmentation), but z-resolution is set by the cut thickness, and each slice is destroyed once cut, so nothing can be re-imaged. Commercial systems such as the Gatan 3View have improved automation and throughput; the basic tradeoffs remain. Compare with FIB-SEM for true isotropic voxels and ATUM-SEM for section preservation.

**Key figures:** Fig. 1 (resolution and contrast from the backscattered electron signal), Fig. 2 (principle of SEM microtomy), Fig. 3 (five slices from a 3D dataset), Fig. 5 (energy dependence of depth resolution)

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

**Beginner:** This paper showed how to use a focused beam of ions (like a tiny sandblaster) to shave very thin layers off brain tissue inside an electron microscope, imaging the fresh surface after each layer. Because the ion beam can remove much thinner layers than a diamond knife can cut, the approach opened the way to 3D images with nearly the same resolution in every direction, which makes it easier to trace thin neural processes that run in any direction.

**Intermediate:** Knott et al. demonstrated FIB-SEM for adult rodent neuropil, using an ion beam to mill away thin layers between backscattered-electron imaging passes of the block face. They milled 40 nm layers, tested milling as thin as 15 nm, and imaged at 4 nm per pixel, showing that a conventional TEM fixation, staining and embedding procedure gives enough membrane contrast to follow all neurites and their synapses. Thin milling makes near-isotropic voxels possible, which is particularly valuable for tracing thin processes (spines, boutons, small-caliber axons) that may be missed or misidentified in anisotropic datasets. The cost is much slower acquisition than SBEM or ATUM-SEM.

**Advanced:** FIB-SEM's isotropic resolution eliminates the z-anisotropy that plagues segmentation in serial section datasets, where ~30-50 nm axial resolution versus ~4-8 nm lateral resolution creates directionally biased errors. The Knott et al. implementation imaged volumes orders of magnitude smaller than SBEM datasets. Enhanced FIB-SEM (Xu et al., 2017) later reached continuously imaged volumes larger than 10⁶ μm³ at isotropic resolution. The choice between FIB-SEM and SBEM depends on whether the scientific question requires isotropy (spine morphology, organelle quantification) or volume (circuit mapping).

**Key figures:** Fig. 1 (ion beam arrangement and block orientation), Fig. 3 (membrane contrast at 5 keV versus 2 keV), Fig. 4 (serial images of asymmetric and symmetric synapses)

**Discussion prompts:**
- For which biological questions is isotropic resolution essential versus merely nice-to-have?
- How does the volume limitation of FIB-SEM affect the kinds of connectomics questions you can ask?

**Related content:** [EM principles](/content-library/imaging/em-principles/), [Acquisition QA](/content-library/imaging/acquisition-qa/)

---

## 3. Zheng et al. (2018) — A Complete Electron Microscopy Volume of the Brain of Adult Drosophila melanogaster

**Citation:** Zheng Z, Lauritzen JS, Perlman E, Robinson CG, Nichols M, Milkie D, et al. A complete electron microscopy volume of the brain of adult *Drosophila melanogaster*. *Cell*. 2018;174(3):730-743.e22.
**DOI:** [10.1016/j.cell.2018.06.019](https://doi.org/10.1016/j.cell.2018.06.019)

**Tags:** `imaging:TEM` `imaging:serial-section` `case-studies:Drosophila` `case-studies:FAFB` `case-studies:whole-brain` `infrastructure:pipeline`

### Summaries

**Beginner:** This paper describes how scientists imaged an entire adult fruit fly brain at nanometer resolution — about 21 million images stitched together. The fruit fly brain is smaller than a poppy seed; the paper estimated it holds about 100,000 neurons (FlyWire later counted 139,255). The dataset became the foundation for mapping the fly's entire wiring diagram.

**Intermediate:** Zheng et al. produced the FAFB (Full Adult Fly Brain) dataset using serial-section transmission EM: 7,062 sections about 40 nm thick were collected on slot grids and imaged with custom high-throughput TEM systems (TEMCA2 and the ATPS). The dataset spans the entire *Drosophila* brain at ~4x4x40 nm voxels (~21 million images, ~106 TB). Key technical achievements include maintaining section continuity over the whole series, parallel high-throughput TEM imaging, and computational alignment of the complete volume. This dataset enabled the FlyWire collaborative reconstruction project.

**Advanced:** The FAFB acquisition pipeline illustrates the engineering challenges of large-scale EM: section loss mitigation (12 sections were lost before full-resolution imaging, and 99.83% of targeted section data were acquired), grid-based collection that allowed selected regions to be re-imaged at higher resolution, and the high-throughput TEM imaging that made the project feasible in a reasonable amount of calendar time. The anisotropic voxels (4x4x40 nm) create z-resolution limitations for thin-process tracing that later automated segmentations of FAFB, including FlyWire's, had to contend with. Compare with the Janelia hemibrain (FIB-SEM, isotropic 8 nm, smaller volume, better z-resolution) to understand how imaging modality choice propagates through reconstruction quality.

**Key figures:** Fig. 1 (target volume and EM acquisition infrastructure), Fig. 2 (reconstructed image volume), Fig. S2 (TEMCA2, Fast Stage and ATPS for high-throughput imaging), Fig. S5 (re-imaging, montaging and assessment of volume quality)

**Discussion prompts:**
- How does the 10x anisotropy (4 nm xy vs 40 nm z) affect segmentation accuracy for different neurite calibers?
- What would change if this brain were imaged today with current FIB-SEM or enhanced SBEM technology?
- How do you handle lost or damaged sections in downstream reconstruction?

**Related content:** [Acquisition QA](/content-library/imaging/acquisition-qa/), [FlyWire whole-brain](/content-library/case-studies/flywire-whole-brain/), [Reconstruction pipeline](/content-library/infrastructure/reconstruction-pipeline/)

---

## 4. Xu et al. (2017) — Enhanced FIB-SEM Systems for Large-Volume 3D Imaging

**Citation:** Xu CS, Hayworth KJ, Lu Z, Grob P, Hassan AM, García-Cerdán JG, et al. Enhanced FIB-SEM systems for large-volume 3D imaging. *eLife*. 2017;6:e25916.
**DOI:** [10.7554/eLife.25916](https://doi.org/10.7554/eLife.25916)

**Tags:** `imaging:FIB-SEM` `imaging:electron-microscopy` `imaging:resolution` `infrastructure:scalability` `methodology:experimental-design`

### Summaries

**Beginner:** Standard FIB-SEM produces 3D images with nearly equal resolution in all directions, but only of tiny volumes. This paper describes engineering improvements — better ion beam control, automated error recovery, longer run times — that let the system run for months and image continuous volumes larger than 10⁶ μm³. That made FIB-SEM practical for whole brain regions rather than small patches.

**Intermediate:** Xu et al. describe engineering improvements to FIB-SEM that let it run for months, producing volumes exceeding 10⁶ μm³ at 8 nm isotropic resolution. Key innovations include automated FIB milling error detection and correction, improved beam stability, and sample preparation optimized for long-duration milling. The enhanced platform was later used to image the Janelia hemibrain (*Drosophila* central brain, about 25,000 neurons; Scheffer et al. 2020).

**Advanced:** The engineering contributions here — fault recovery, drift compensation, long-term beam stability — are what enabled the hemibrain project and subsequent FIB-SEM connectomics efforts. The system images volumes larger than 10⁶ μm³ at 8 nm isotropic voxels, with 4 nm voxels possible on smaller volumes. Compare the tradeoff space: FAFB covers a whole fly brain at 40 nm section thickness, while the hemibrain covers part of the central brain at 8 nm isotropic voxels. The paper argues that the isotropy advantage matters most for tracing small neuronal processes and can reduce proofreading effort.

**Key figures:** Fig. 1 (3D imaging technologies compared by resolution and total volume), Fig. 2 (isotropic 4 nm voxels versus emulated 4x4x40 nm voxels), Fig. 5 (ultrathick partitioning and imaging results), Fig. 9 (failure modes and customized solutions for long-term reliability)

**Discussion prompts:**
- At what volume scale does the isotropy advantage of FIB-SEM outweigh the throughput advantage of ATUM-SEM?
- How do you choose between isotropy and volume when designing a connectomics experiment?

**Related content:** [EM principles](/content-library/imaging/em-principles/), [Tissue preparation](/content-library/imaging/tissue-preparation/)

---

## 5. Hayworth et al. (2015) — Ultrathick Sectioning and Volume Stitching for Large-Volume FIB-SEM

**Citation:** Hayworth KJ, Xu CS, Lu Z, Knott GW, Fetter RD, Tapia JC, Lichtman JW, Hess HF. Ultrastructurally smooth thick partitioning and volume stitching for large-scale connectomics. *Nature Methods*. 2015;12(4):319-322.
**DOI:** [10.1038/nmeth.3292](https://doi.org/10.1038/nmeth.3292)

**Tags:** `imaging:FIB-SEM` `imaging:serial-section` `imaging:SEM` `infrastructure:pipeline` `infrastructure:alignment` `methodology:experimental-design`

### Summaries

**Beginner:** FIB-SEM gives excellent 3D images but can only handle small blocks of tissue at a time. This paper developed a way to cut a larger block into thick slabs (20 μm) with surfaces smooth enough to lose almost nothing, image each slab separately on several microscopes, and computationally stitch the results back together. This makes it possible to image larger brain volumes while keeping the resolution needed to trace neural connections.

**Intermediate:** Hayworth et al. address the volume limit of FIB-SEM by developing "hot knife" ultrathick sectioning. A heated, lubricated diamond knife cuts resin-embedded tissue into 20 μm thick chunks sized and mounted for efficient FIB-SEM imaging. Each chunk is imaged separately by FIB-SEM, and the resulting sub-volumes are "volume stitched" back together into a dataset suitable for connectome tracing. This enables parallel imaging across multiple FIB-SEMs.

**Advanced:** The volume stitching approach relaxes a key constraint of block-face imaging — that one microscope must mill and image the whole volume in a single uninterrupted run. By accepting controlled cuts at 20 μm intervals, the method bounds the damage from any single failure to one slab and enables multi-microscope parallelism. The surface quality of hot-knife cuts is critical, because neurites must be traced across each cut. An improved version of this procedure was subsequently used to partition the *Drosophila* hemibrain into slabs for FIB-SEM imaging (Scheffer et al., 2020).

**Key figures:** Fig. 1 (overview of ultrathick sectioning), Fig. 2 (volume stitching results on mouse cortex), Fig. 3 (volume stitching results on fly brain)

**Discussion prompts:**
- What are the error modes specific to slab-to-slab stitching that don't exist in a single continuous block-face run?
- How does this approach change the cost-benefit analysis for very large volumes?

**Related content:** [Reconstruction pipeline](/content-library/infrastructure/reconstruction-pipeline/), [Acquisition QA](/content-library/imaging/acquisition-qa/)

---

## 6. Yin et al. (2020) — A Petascale Automated Imaging Pipeline

**Citation:** Yin W, Brittain D, Borseth J, Scott ME, Williams D, Perkins J, et al. A petascale automated imaging pipeline for mapping neuronal circuits with high-throughput transmission electron microscopy. *Nature Communications*. 2020;11:4949.
**DOI:** [10.1038/s41467-020-18659-3](https://doi.org/10.1038/s41467-020-18659-3)

**Tags:** `imaging:TEM` `imaging:ATUM` `imaging:serial-section` `infrastructure:pipeline` `infrastructure:scalability` `case-studies:MICrONS`

### Summaries

**Beginner:** To map the wiring of even a small piece of mouse brain, you need millions of images assembled into one continuous 3D volume. This paper describes the imaging system built for the MICrONS project: transmission electron microscopes running around the clock (five imaged the cubic millimeter; the platform later grew to six), automated quality checks, and software to track every image.

**Intermediate:** Yin et al. describe the parallel transmission EM imaging pipeline (piTEAM) used for the MICrONS mm³ cortical volume. Key engineering contributions include a reel-to-reel stage that locates sections on GridTape by barcode for 24/7 autonomous imaging, real-time quality control of tile overlap and focus, parallel operation of multiple TEMs, and data infrastructure for petabyte-scale acquisition. More than 26,500 sections were imaged in less than 6 months, yielding more than 2 petabytes; with six microscopes in parallel, the combined burst rate was 3 gigapixels per second and the net rate 600 megapixels per second.

**Advanced:** Read this for how connectomics imaging became a production process. The real-time quality control — template matching to detect tile overlap problems and an FFT-based focus score for every tile — is a worked approach to acquisition reliability at scale. The pipeline handles the chain from sections on GridTape to a managed image record database. Note the choice of camera-based TEM over SEM for throughput, accepting the need to collect sections on electron-transparent film. The paper provides concrete throughput numbers useful for planning future large-scale acquisitions.

**Key figures:** Fig. 1 (experimental pipeline from sample preparation to imaging), Fig. 2 (piTEAM architecture and workflow), Fig. 3 (real-time quality control), Fig. 4 (imaging a cubic millimeter of mouse cortex), Fig. 5 (imaging rate scaling roadmap)

**Discussion prompts:**
- What are the bottlenecks in this pipeline, and which are engineering versus fundamental physics limits?
- How would you design an acquisition QA system for a dataset 10x larger than MICrONS?

**Related content:** [Acquisition QA](/content-library/imaging/acquisition-qa/), [Reconstruction pipeline](/content-library/infrastructure/reconstruction-pipeline/), [MICrONS visual cortex](/content-library/case-studies/microns-visual-cortex/)

---

## 7. Lichtman & Denk (2011) — The big and the small: Challenges of imaging the brain's circuits

**Citation:** Lichtman JW, Denk W. The big and the small: challenges of imaging the brain's circuits. *Science*. 2011;334(6056):618-623.
**DOI:** [10.1126/science.1209168](https://doi.org/10.1126/science.1209168)

**Tags:** `imaging:electron-microscopy` `imaging:resolution` `methodology:experimental-design` `imaging:correlative-imaging`

### Summaries

**Beginner:** This paper is a readable overview of why imaging the brain's wiring is hard. The brain contains structures at vastly different scales — from entire brain regions (centimeters) down to individual synapses (nanometers). No single imaging method can capture all of these at once. The authors explain the fundamental gap between light microscopy (which can see large areas but not fine details) and electron microscopy (which can see fine details but only in tiny volumes), and discuss strategies for bridging this gap.

**Intermediate:** Lichtman and Denk present a perspective on the multi-scale imaging challenge in neuroscience, framing it as a problem of simultaneously achieving the resolution needed to identify synapses (~10 nm) and the field of view needed to follow neural circuits (~mm to cm). They compare the strengths and limitations of light microscopy, serial section EM, SBEM, and FIB-SEM, and introduce the concept of correlative imaging — combining modalities to span scales. The paper also discusses the data volume challenges that synaptic-resolution imaging of large volumes creates.

**Advanced:** This perspective is still one of the clearest statements of the resolution-volume tradeoff that governs connectomics experimental design. Lichtman and Denk discuss the imaging throughput that mammalian connectomics demands and why it depends on advances in automation and parallelization. Their analysis of the "data bottleneck" — where imaging speed exceeds analysis speed — anticipated the current state of the field. The discussion of correlative light-electron microscopy (CLEM) as a strategy for targeting EM acquisition to functionally characterized regions is directly relevant to the MICrONS project design and similar functional connectomics efforts.

**Discussion prompts:**
- Has the resolution-volume tradeoff described in 2011 been substantially altered by subsequent technology development?
- What role should correlative imaging play in connectomics experimental design versus purely EM-based approaches?
- How do the data volume concerns raised in this paper compare with actual dataset sizes from recent connectomics projects?

**Related content:** [EM principles](/content-library/imaging/em-principles/), [Acquisition QA](/content-library/imaging/acquisition-qa/), [Tissue preparation](/content-library/imaging/tissue-preparation/)

---

## 8. Briggman & Bock (2012) — Volume electron microscopy for neuronal circuit reconstruction

**Citation:** Briggman KL, Bock DD. Volume electron microscopy for neuronal circuit reconstruction. *Current Opinion in Neurobiology*. 2012;22(1):154-161.
**DOI:** [10.1016/j.conb.2011.10.022](https://doi.org/10.1016/j.conb.2011.10.022)

**Tags:** `imaging:electron-microscopy` `imaging:SBEM` `imaging:FIB-SEM` `imaging:ATUM` `methodology:experimental-design`

### Summaries

**Beginner:** This review compares the three main ways scientists create 3D images of brain tissue at the nanometer scale: serial block-face SEM (SBEM, which shaves and images layers inside the microscope), focused ion beam SEM (FIB-SEM, which uses an ion beam to remove layers for the highest resolution), and serial section collection methods like ATUM (which collect physical slices on tape for imaging). Each method has different strengths, and this paper explains when to use which one.

**Intermediate:** Briggman and Bock provide a practical comparison of volume EM methods — SBEM, FIB-SEM, and ATUM-SEM/TEM — for neural circuit reconstruction. For each method, they evaluate resolution (lateral and axial), achievable volume, throughput, whether sections are preserved or destroyed, and suitability for different biological questions. Key comparisons include SBEM's automated workflow versus ATUM's ability to re-image sections, and FIB-SEM's isotropic voxels versus the anisotropy inherent in serial section approaches. The review also covers sample preparation requirements specific to each method.

**Advanced:** This review is still a useful reference for experimental design. Briggman and Bock evaluate how each volume EM modality's technical parameters propagate through the reconstruction pipeline: anisotropic voxels from ATUM/SBEM create directionally biased segmentation errors, FIB-SEM's isotropy improves small-caliber neurite tracing but limits volume, and section preservation in ATUM enables iterative re-imaging for quality recovery. The framework for matching imaging modality to scientific question — circuit mapping (maximize volume) versus ultrastructural analysis (maximize resolution) — continues to guide project planning.

**Discussion prompts:**
- How has the landscape of volume EM modalities changed since 2012, and which of the tradeoffs described here have been overcome?
- For a new connectomics project in mammalian cortex, how would you use this framework to choose an imaging modality?
- What role does section preservation (ATUM) versus section destruction (SBEM/FIB-SEM) play in quality assurance and error recovery?

**Related content:** [EM principles](/content-library/imaging/em-principles/), [Tissue preparation](/content-library/imaging/tissue-preparation/), [Acquisition QA](/content-library/imaging/acquisition-qa/)
