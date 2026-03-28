---
layout: page
title: "Artifact Taxonomy"
permalink: /content-library/imaging/artifact-taxonomy/
description: "Comprehensive catalog of EM imaging artifacts in connectomics, their causes, visual signatures, downstream impact on segmentation and proofreading, and mitigation strategies."
topics:
  - artifacts
  - image-quality
  - segmentation-impact
  - quality-control
primary_units:
  - "03"
  - "05"
difficulty: "Intermediate"
tags:
  - imaging:artifact-identification
  - imaging:electron-microscopy
  - imaging:quality-control
  - proofreading:segmentation-impact
  - methodology:artifact-mitigation
micro_lesson_id: ml-img-artifacts
reference_images:
  - src: /assets/images/content-library/imaging/artifact-taxonomy/artifact-gallery.png
    alt: "Gallery of common EM artifacts: knife chatter, charging, folds, tears, and section loss"
    caption: "Common EM acquisition artifacts. Each has distinct visual signatures and different impacts on downstream segmentation."
  - src: /assets/images/content-library/imaging/artifact-taxonomy/artifact-impact-segmentation.png
    alt: "Same region showing artifact in EM and resulting segmentation errors"
    caption: "A tissue fold (top) causes the segmentation algorithm to merge two neurons (bottom). Understanding artifacts prevents misinterpreting errors."
  - src: /assets/images/content-library/imaging/artifact-taxonomy/artifact-severity-scale.png
    alt: "Severity scale for EM artifacts from cosmetic to data-destroying"
    caption: "Artifact severity scale: Level 1 (cosmetic, no segmentation impact) through Level 5 (complete data loss requiring re-imaging)."
combines_with:
  - em-principles
  - acquisition-qa
  - tissue-preparation
---

## Overview

Every EM dataset contains artifacts. The question is never "are there artifacts?" but rather "which artifacts are present, how severe are they, and what is their downstream cost?" Annotators and analysts who understand the artifact landscape make better decisions — they avoid over-interpreting corrupted regions, they know when to flag data for re-acquisition vs when to work around it, and they can trace apparent segmentation errors back to their imaging root cause.

This document catalogs the major artifact classes encountered in connectomics EM, organized by their origin in the acquisition pipeline.

---

## Tissue preparation artifacts

### Fixation artifacts

**Cause:** Chemical fixation (typically aldehyde-based: glutaraldehyde + paraformaldehyde) stabilizes ultrastructure by crosslinking proteins. However, fixation is never instantaneous — there is always some delay between tissue death and complete fixation, during which degradation can occur.

**Visual signatures:**
- **Swollen or distorted mitochondria**: Cristae disrupted, matrix pale. Indicates poor fixation or post-mortem delay. This is one of the earliest and most sensitive indicators of fixation quality.
- **Extracted cytoplasm**: Pale, washed-out cytoplasm where soluble proteins were lost. Processes appear "empty" compared to well-fixed tissue.
- **Membrane disruption**: Incomplete or discontinuous membrane profiles. Severe cases show membrane blebbing or fragmentation.
- **Extracellular space expansion**: In well-fixed neuropil, extracellular space is minimal (~20% of volume in vivo, but often <5% in fixed tissue due to shrinkage). Excessive gaps between processes suggest osmotic imbalance during fixation.

**Downstream impact:** Poor fixation degrades membrane contrast globally, increasing both merge and split error rates. Mitochondrial distortion can confuse organelle-based compartment identification.

**Mitigation:** Transcardial perfusion with buffered fixative provides the most uniform fixation for mammalian brain. Immersion fixation of resected tissue (as in human surgical samples like H01) is less uniform — expect a quality gradient from surface to interior.

**Reference:** Bhatt, Bhatt & Bhatt (2009); Bhatt & Bhatt (various); Bhatt DH (2009). For the H01 dataset specifically, see Shapson-Coe et al. (2024) which discusses fixation quality in human surgical tissue.

### Staining artifacts

**Cause:** Heavy-metal staining must penetrate uniformly through the tissue block (for volume EM) or individual sections (for ssTEM). Incomplete penetration, precipitation, or differential binding can create contrast inhomogeneities.

**Visual signatures:**
- **Staining gradients**: Contrast decreases from block edges inward (osmium penetration limit, typically 200-500 μm for standard protocols). Membranes become progressively harder to see.
- **Precipitate deposits**: Dark, irregularly shaped deposits that are not biological structures. Uranyl acetate and lead citrate are both prone to precipitation if pH or concentration is incorrect.
- **Differential staining**: Some structures over-stained relative to others. For example, excessive uranyl acetate can make chromatin so dark that it obscures nuclear detail.

**Downstream impact:** Staining gradients are particularly insidious because they create spatially varying segmentation quality — models trained on well-stained regions perform poorly on under-stained regions, but the transition is gradual and may not be caught by global QA metrics.

**Mitigation:** The rOTO (reduced osmium-thiocarbohydrazide-osmium) protocol (Hua et al. 2015) was specifically developed to improve staining uniformity for volume EM. Pilot imaging of test blocks before committing to full acquisition is essential.

### Embedding and infiltration artifacts

**Cause:** After staining, tissue is dehydrated and infiltrated with resin (typically Epon or Durcupan). Incomplete infiltration creates voids; differential shrinkage distorts geometry.

**Visual signatures:**
- **Resin voids**: Light areas with no biological structure, often with sharp edges. Distinct from extracellular space (which has biological boundaries).
- **Shrinkage**: Tissue contracts ~10-30% during processing. Anisotropic shrinkage distorts cell shapes and distances. Neuropil appears denser than in vivo.
- **Chattering during sectioning**: If resin is too hard or soft, the diamond knife vibrates, creating periodic thickness variations visible as alternating light/dark bands.

---

## Sectioning artifacts

### Knife marks and chatter

**Cause:** Diamond knife vibration during ultrathin sectioning creates periodic thickness variations (chatter) or score marks (knife lines) across the section face.

**Visual signatures:**
- **Chatter**: Alternating bright/dark bands perpendicular to the cutting direction, with periodicity of 0.5-5 μm. Superimposed on biological detail.
- **Knife lines**: Thin streaks parallel to the cutting direction. Usually less disruptive than chatter unless severe.

**Downstream impact:** Chatter creates false boundaries that segmentation algorithms may interpret as membranes, generating split errors. The periodic pattern can also create coherent artifacts across multiple sections, making them harder to distinguish from real structures.

**Mitigation:** Optimize cutting speed, knife angle, and block trimming geometry. Replace diamond knife when signs of wear appear. For SBEM, chatter is a persistent challenge because the knife operates inside the vacuum chamber.

### Section compression

**Cause:** The diamond knife compresses the section in the cutting direction, typically by 10-30%. This creates anisotropic distortion — features are shortened along the cutting axis.

**Visual signatures:** Circular profiles appear elliptical. Grid-like patterns (if present) show directional distortion. The compression axis is consistent within a section but may vary between sections.

**Downstream impact:** Compression distorts morphological measurements (soma size, spine dimensions) and complicates registration between sections. If uncorrected, 3D reconstructions show systematic stretching artifacts.

**Mitigation:** Computational correction during section registration. Estimating compression ratio from circular structures (blood vessels, myelinated axons in cross-section) and applying inverse transform.

### Folds, tears, and wrinkles

**Cause:** Ultrathin sections (40-70 nm) are mechanically fragile. Handling during collection on grids or tapes can introduce folds (section doubled over), tears (section ripped), or wrinkles (local buckling).

**Visual signatures:**
- **Folds**: Region where two layers of section overlap, appearing as a dark band with doubled features. Borders are sharp, linear.
- **Tears**: Missing region with sharp edges, usually irregular. No data available within the tear.
- **Wrinkles**: Gentle undulations causing out-of-focus regions. Features appear blurred or show focus gradient.

**Downstream impact:** Folds create false double-membrane appearances that can be mistaken for cell boundaries. Tears create complete data gaps — any neurite crossing a tear is lost at that z-level, causing splits. Wrinkles degrade resolution locally.

**Severity hierarchy:** Tears > folds > wrinkles in terms of downstream damage. Tears are non-recoverable; folds can sometimes be computationally flattened; wrinkles rarely cause segmentation errors.

### Missing sections

**Cause:** Section lost during collection, or section too damaged to image. Creates a gap in the z-stack.

**Visual signatures:** Jump in z — structures appear to teleport between adjacent surviving sections. Registration metrics show anomalous displacement.

**Downstream impact:** Missing sections are the most common cause of split errors in neurite tracing. A thin axon (~100 nm) in a dataset with 30 nm z-resolution spans only 3-4 sections. One missing section means 25-33% of the local z-information is lost, which can be enough to lose the axon entirely.

**Mitigation:** ATUM-based collection has reduced missing-section rates to <0.1% for well-optimized protocols. SBEM and FIB-SEM inherently avoid this problem because sections are not physically collected. Computational approaches: interpolation of the missing section, or explicit "uncertain gap" annotation.

---

## Imaging artifacts

### Charging

**Cause:** Electron beam deposits charge in non-conductive regions of the specimen. If charge cannot dissipate fast enough (through conductive coating or staining), the accumulated charge deflects the beam, distorting the image.

**Visual signatures:**
- **Bright streaks or halos**: Charge buildup creates abnormal brightness patterns, often at edges of structures or near poorly stained regions.
- **Image drift/distortion**: Accumulated charge creates local electric fields that deflect the beam, causing spatial distortion.
- **Contrast inversion**: In severe cases, charged regions can appear with inverted contrast.

**Downstream impact:** Charging creates false contrast patterns that segmentation models may interpret as biological boundaries. Spatial distortion degrades registration accuracy.

**Mitigation:** Adequate heavy-metal staining provides conductivity. Conductive coating (carbon, gold-palladium) of block face or section surface. Reducing beam current or dwell time (at cost of SNR). Variable-pressure SEM modes help but reduce resolution.

### Beam damage

**Cause:** Cumulative electron dose degrades the specimen. Organic material is particularly sensitive — the radiation damage threshold for biological specimens is ~10-100 electrons/Å² for high-resolution structural preservation.

**Visual signatures:**
- **Mass loss**: Specimen appears to thin or develop holes with prolonged exposure.
- **Bubbling**: Volatile decomposition products create bubbles within the resin.
- **Contrast loss**: Staining patterns fade with repeated imaging.

**Downstream impact:** In serial imaging (SBEM, FIB-SEM), the beam affects not just the imaged surface but also several hundred nanometers below, potentially degrading sections that will be exposed by future cuts. This creates a "pre-damage" effect.

**Mitigation:** Optimize dose: use the minimum beam current and dwell time that produce adequate SNR. Single-pass imaging (no repeat imaging of the same area). For SBEM/FIB-SEM, accelerating voltage affects the depth of beam penetration and thus pre-damage.

### Drift and jitter

**Cause:** Mechanical or thermal instabilities in the microscope stage cause the specimen to move during imaging. Fast drift = jitter (within a single tile), slow drift = systematic displacement between tiles.

**Visual signatures:**
- **Jitter**: Horizontal or vertical line-by-line offsets within a single image, giving a "sheared" appearance.
- **Drift**: Systematic offset between adjacent tiles in a mosaic, or between consecutive sections. Visible as seams in stitched images.

**Downstream impact:** Jitter degrades local resolution. Drift creates tile-boundary artifacts that segmentation may misinterpret, and complicates inter-section registration.

---

## Computational/alignment artifacts

### Stitching seams

**Cause:** Large areas are imaged as tile mosaics and computationally stitched. Imperfect tile registration creates visible seams — brightness discontinuities, small spatial offsets, or duplicated/missing strips at tile boundaries.

**Visual signatures:** Linear brightness changes or offset patterns at regular intervals matching the tile grid.

**Downstream impact:** Seams create false boundaries. Segmentation algorithms may split neurites at seam locations. Even after intensity normalization, subtle spatial offsets can persist.

### Section-to-section misalignment

**Cause:** Even with automated registration, residual misalignment between consecutive sections (1-10 nm) can accumulate over many sections.

**Visual signatures:** Structures appear to oscillate or drift when scrolling through z. Fine processes may appear to jump discontinuously.

**Downstream impact:** Misalignment creates false branch points and false terminations. For thin processes (<200 nm), even 1-pixel (4-8 nm) misalignment can shift the process outside its own boundary in the next section, causing a split.

---

## Artifact severity classification for proofreading triage

| Severity | Examples | Action |
|----------|----------|--------|
| **Critical** (blocks reconstruction) | Missing sections, large tears, severe misalignment | Flag for re-acquisition or exclude region |
| **Major** (increases error rate significantly) | Staining gradients, charging, persistent chatter | Run pilot segmentation; quantify error rate penalty; consider targeted re-imaging |
| **Minor** (manageable in proofreading) | Occasional knife lines, mild compression, small wrinkles | Proceed with awareness; include in proofreading QA checks |
| **Cosmetic** (no downstream impact) | Slight focus variation, minor brightness non-uniformity | No action needed |

---

## Worked example: diagnosing a region with elevated split errors

**Scenario:** A proofreader notices that a specific 20×20×20 μm subvolume has 3× the normal split error rate. The segmentation model is the same one used across the entire volume.

**Diagnostic steps:**

1. **Inspect raw images in the subvolume.** Look for: contrast changes, staining differences, artifacts.
2. **Finding:** The subvolume is near the edge of the tissue block. Membrane contrast is visibly reduced compared to the center — classic staining gradient from incomplete osmium penetration.
3. **Verify:** Plot mean membrane contrast (e.g., using membrane probability maps from the segmentation model) as a function of distance from block edge. Confirm gradient.
4. **Root cause:** Under-stained membranes → lower model confidence at membrane predictions → more split errors where model fails to detect thin, low-contrast membranes.
5. **Decision:** (a) Flag region as reduced-quality in metadata. (b) Consider re-running segmentation with lower boundary threshold (accepting more merge errors in exchange for fewer splits). (c) Allocate extra proofreading time to this region. (d) Report to the acquisition team for future protocol adjustment.

---

## References

- Briggman KL, Bock DD (2012) "Volume electron microscopy for neuronal circuit reconstruction." *Current Opinion in Neurobiology* 22(1):154-161.
- Denk W, Horstmann H (2004) "Serial block-face scanning electron microscopy to reconstruct three-dimensional tissue nanostructure." *PLoS Biology* 2(11):e329.
- Hayworth KJ et al. (2014) "Ultrastructurally smooth thick partitioning and volume stitching for large-scale connectomics." *Nature Methods* 12:319-322.
- Hua Y, Laserstein P, Bhatt M (2015) "Large-volume en-bloc staining for electron microscopy-based connectomics." *Nature Communications* 6:7923.
- Kasthuri N et al. (2015) "Saturated reconstruction of a volume of neocortex." *Cell* 162(3):648-661.
- Shapson-Coe A et al. (2024) "A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution." *Science* 384(6696):eadk4858.
- Xu CS et al. (2021) "Enhanced FIB-SEM systems for large-volume 3D imaging." *eLife* 10:e65541.
