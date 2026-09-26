---
layout: page
title: "Tissue Preparation"
permalink: /content-library/imaging/tissue-preparation/
image: /assets/images/content-library/imaging/tissue-preparation.svg
image_alt: "Stylized vector art: a raster imaging field crossed by artifact marks."
description: "Tissue preparation for connectomics EM: fixation, staining, embedding and sectioning, with an instructor script, protocol decision points, a worked example and references."
topics:
  - tissue-preparation
  - fixation
  - staining
  - sectioning
  - embedding
primary_units:
  - "03"
difficulty: "Intermediate"
tags:
  - imaging:tissue-preparation
  - imaging:fixation
  - imaging:heavy-metal-staining
  - imaging:electron-microscopy
  - methodology:sample-processing
micro_lesson_id: ml-img-tissue-prep
combines_with:
  - em-principles
  - artifact-taxonomy
  - acquisition-qa
content_type: core
---

{% include callouts/em-imaging-visual-note.html %}

## Overview

Tissue preparation for connectomics has three jobs: stabilize the ultrastructure, make it visible to electrons, and put it in a form that can be imaged section after section. Every step (fixation, staining, dehydration, embedding, sectioning) trades preservation against contrast and throughput. If you interpret EM data, you need to know those trades, because preparation choices set the artifact profile that the whole reconstruction pipeline inherits.

---

## Instructor script: the preparation pipeline

### Step 1 — Fixation

**Purpose:** Halt biological degradation and crosslink macromolecules in place, preserving ultrastructure as close to the living state as possible.

**Primary fixatives for connectomics:**

- **Glutaraldehyde (GA)**: The workhorse fixative for EM. A bifunctional crosslinker that bridges amino groups on adjacent proteins, creating a rigid meshwork. Concentration: typically 2-2.5% in phosphate or cacodylate buffer. Penetration is slow and depth-dependent, which is why block size is limited and why perfusion is preferred over immersion where it is possible; treat any single figure you see quoted for it as protocol-specific rather than a constant. Provides excellent ultrastructural preservation but does not fix lipids — hence the need for subsequent osmium treatment.

- **Paraformaldehyde (PFA)**: A smaller, monofunctional crosslinker that penetrates faster than GA but provides weaker fixation. Often combined with GA (e.g., 4% PFA + 2.5% GA) for rapid initial stabilization followed by thorough crosslinking. PFA alone is insufficient for EM-quality preservation.

- **The fixation route matters:**
  - *Transcardial perfusion* (rodents): Fixative pumped through the vasculature under pressure. Reaches all brain regions simultaneously via capillary beds. Provides the most uniform fixation for whole-brain studies. Standard for mouse/rat connectomics (the MICrONS mouse, for example, was perfused).
  - *Immersion fixation* (human tissue, invertebrates): Tissue block placed directly in fixative solution. Fixation proceeds from the surface inward — creating a gradient where the surface is well-fixed and the interior may show degradation before fixative arrives. The H01 human cortex dataset (Shapson-Coe et al. 2024) used surgically resected tissue fixed by rapid immersion; the authors report quality comparable to perfused rodent samples, which shows immersion can work when the tissue reaches fixative quickly.

**Teaching point:** No microscope can rescue poorly fixed tissue. Fixation quality sets the ceiling on every downstream step.

**Time matters:** The delay between loss of blood supply and the arrival of fixative is a major variable in human tissue quality, and the damage shows as swollen mitochondria and disrupted membranes. For H01, a neuropathologist immersed the sample in fixative immediately after excision (Shapson-Coe et al. 2021 preprint, Methods). For human surgical tissue, plan the path from operating room to fixative before the day of surgery.

### Step 2 — Post-fixation with osmium tetroxide

**Purpose:** Fix lipid membranes and deposit heavy metal for electron contrast.

**Chemistry:** OsO₄ reacts with unsaturated double bonds in lipid bilayers, crosslinking them and depositing osmium (Z=76, very high atomic number) at membrane sites. This is the primary source of membrane visibility in EM.

**Standard protocol:** 1-2% OsO₄ in buffer for 1-2 hours. For volume EM requiring deep penetration, the rOTO (reduced osmium-thiocarbohydrazide-osmium) protocol repeats the osmium treatment:

1. Reduced osmium (OsO₄ + ferrocyanide) — 1-2 hours
2. Thiocarbohydrazide (TCH) — bridges osmium layers — 20-30 minutes
3. Second OsO₄ treatment — 1-2 hours

The rOTO protocol builds on the earlier OTO method (Willingham & Rutherford 1984); Hua et al. (2015) modified it to stain blocks about 1 mm across without a staining gradient. It gives stronger and more even membrane contrast through large blocks, which SBEM and FIB-SEM need because individual sections cannot be post-stained.

**Key decision point:** rOTO vs standard osmium. rOTO is standard for volume EM. Standard single-osmium may suffice for ssTEM where sections will be post-stained with uranyl acetate and lead citrate.

### Step 3 — En bloc staining (for volume EM)

**Purpose:** Deposit additional heavy metals throughout the block for contrast enhancement, since individual sections cannot be stained after SBEM/FIB-SEM cutting.

**Typical agents:**
- **Uranyl acetate (UA)**: Binds nucleic acids and proteins. Enhances contrast of ribosomes, chromatin, PSDs. Often applied as 1-2% aqueous solution or in 70% ethanol during dehydration. Safety note: uranyl acetate is mildly radioactive and toxic — some labs are shifting to non-radioactive alternatives (e.g., lanthanide-based stains).
- **Lead aspartate**: Enhances general contrast. Applied en bloc after osmication. Walton (1979) protocol adapted for connectomics.

**Penetration challenge:** These stains must penetrate evenly through blocks that may be 1-3 mm on a side. Incomplete penetration creates the staining gradients described in [Artifact taxonomy]({{ '/content-library/imaging/artifact-taxonomy/' | relative_url }}). Temperature, time and agitation all have to be tuned for the block size.

### Step 4 — Dehydration

**Purpose:** Remove water from the tissue to allow infiltration with hydrophobic embedding resin.

**Standard approach:** Graded ethanol or acetone series (30%, 50%, 70%, 90%, 100%, 100%). Each step typically 10-30 minutes. The gradual replacement minimizes osmotic shock that could distort ultrastructure.

**Artifact risk:** Dehydration extracts some lipids (even after osmium fixation) and shrinks the tissue. The amount depends on the protocol; published corrections include a 16% linear reduction (Kalimo 1976) and 15% along each axis (Kinney et al. 2013), both as cited by Korogod et al. (2015). Chemical fixation also collapses the extracellular space: Korogod et al. measured 15.4% extracellular volume in cryo-fixed mouse neocortex against 2.47% after aldehyde perfusion. Account for both when comparing EM measurements to in vivo dimensions.

### Step 5 — Embedding

**Purpose:** Replace the dehydrant with a rigid resin that can be sectioned at nanometer precision.

**Common resins:**
- **Epon 812 (or equivalent)**: The standard embedding resin for EM. Polymerizes at 60°C over 24-48 hours. Produces hard, uniform blocks suitable for ultrathin sectioning.
- **Durcupan**: Alternative epoxy resin, sometimes preferred for its sectioning properties.
- **Spurr's resin**: Lower viscosity, better penetration for dense tissue, but more brittle.

**Infiltration:** Gradual replacement of dehydrant with resin (25%, 50%, 75%, 100% resin in solvent). Incomplete infiltration leaves voids or soft spots that cause sectioning artifacts.

**Block trimming:** After polymerization, the resin block is trimmed to expose the tissue face with the target region. Precise trimming determines the field of view and affects sectioning quality.

### Step 6 — Sectioning

Three major approaches for connectomics, each with different tradeoffs:

**Ultramicrotomy (for ssTEM):**
- Diamond knife cuts ultrathin sections (40-70 nm) from the block face
- Sections float onto water trough and are collected on grids or ATUM tape
- Produces the thinnest sections (best z-resolution per section) but introduces mechanical artifacts (compression, chatter, folds)
- ATUM (automated tape-collecting ultramicrotome — Hayworth et al. 2006) enables automated collection of thousands of sections on continuous tape

**Serial block-face SEM (SBEM) sectioning:**
- Diamond knife inside the SEM chamber shaves the block face
- Cut thickness: 25-30 nm (limited by mechanical precision)
- Advantages: automatic z-alignment, no section handling
- Disadvantages: knife wear, chatter artifacts, cannot re-image

**FIB milling:**
- Gallium ion beam ablates the block face
- Milling thickness: 4-8 nm (finest z-resolution available)
- Advantages: isotropic voxels, no mechanical sectioning artifacts
- Disadvantages: slow, small field of view, Ga implantation at surface

---

## Worked example: choosing a preparation protocol for a cortical connectomics project

**Scenario (a teaching example, not a published protocol):** You are planning a connectomics study of mouse barrel cortex layer 4, targeting a 200×200×200 μm volume. You want to identify all synapses between thalamocortical axons and layer 4 stellate cells.

**Decision sequence:**

1. **Fixation:** Transcardial perfusion with 2.5% GA + 2% PFA in 0.1M sodium cacodylate buffer. Perfusion ensures uniform fixation across the target region. Post-fix in same solution for 12-24 hours at 4°C.

2. **Vibratome sectioning:** Cut 200 μm thick sections on vibratome. Select the section containing barrel cortex L4 using cytochrome oxidase staining of adjacent sections (barrels are visible as dense staining).

3. **Post-fixation and staining:** rOTO protocol for uniform en bloc contrast (planning to use SBEM). OsO₄-ferrocyanide → TCH → OsO₄ → UA in ethanol → lead aspartate.

4. **Embedding:** Epon resin, standard infiltration. Flat-embed to orient barrel columns perpendicular to the sectioning plane.

5. **Imaging modality choice:** SBEM at 8×8×25 nm voxel size. Rationale: need to resolve synapses (requires <10 nm XY) over a 200 μm cube (too large for FIB-SEM); 25 nm z is adequate for tracing most axons; SBEM provides automatic z-alignment.

6. **Estimated data volume:** 200 μm ÷ 8 nm = 25,000 pixels per side (XY) × (200 μm ÷ 25 nm = 8,000 sections). Total: ~5 teravoxels → ~5 TB at 8-bit per voxel.

---

## Protocol comparison table

| Parameter | Serial sections (TEM on grids; SEM on ATUM tape) | SBEM | FIB-SEM |
|-----------|-------------|------|---------|
| Section thickness | 30-50 nm | 25-30 nm | 4-8 nm |
| XY resolution | 1-4 nm | 8-12 nm | 4-8 nm |
| Volume range | mm³ | 500 μm per side | 50-100 μm per side |
| Sectioning artifacts | Compression, folds, tears | Knife chatter | Ga curtaining |
| Re-imaging possible? | Yes | No (destructive) | No (destructive) |
| En bloc staining required? | Optional (post-stain OK) | Required | Required |
| Alignment | Requires computational registration | Inherent (block face) | Inherent (block face) |
| Imaging time, order of magnitude | Months to a year for mm³ (MICrONS about 6 months; H01 326 days) | Months | Weeks to months |

---

## Common misconceptions

| Misconception | Reality | Teaching note |
|---|---|---|
| "Standard fixation is good enough for EM" | PFA-only fixation (common for immunohistochemistry) is insufficient for ultrastructural preservation | EM requires glutaraldehyde-based fixation with osmium post-fixation |
| "Staining is just for visibility" | Heavy metals also crosslink membranes (osmium), providing additional structural stabilization | Staining and fixation serve overlapping purposes |
| "Tissue looks the same as in vivo" | Processing shrinks tissue (around 15% per axis in published corrections), collapses extracellular space, and extracts some components | Always state that EM measurements are from fixed/processed tissue |
| "FIB-SEM is always better" | FIB-SEM has the best z-resolution but the smallest field of view, so it does not suit large-circuit mapping | Match modality to question |

---

## References

- Denk W, Horstmann H (2004) "Serial block-face scanning electron microscopy." *PLoS Biology* 2(11):e329.
- Hayworth KJ, Kasthuri N, Schalek R, Lichtman JW (2006) "Automating the collection of ultrathin serial sections for large volume TEM reconstructions." *Microscopy and Microanalysis* 12(Suppl 2):86-87.
- Hayworth KJ et al. (2015) "Ultrastructurally smooth thick partitioning and volume stitching for large-scale connectomics." *Nature Methods* 12:319-322.
- Hua Y, Laserstein P, Helmstaedter M (2015) "Large-volume en-bloc staining for electron microscopy-based connectomics." *Nature Communications* 6:7923.
- Knott G et al. (2008) "Serial section scanning electron microscopy of adult brain tissue using focused ion beam milling." *Journal of Neuroscience* 28(12):2959-2964.
- Korogod N, Petersen CCH, Knott GW (2015) "Ultrastructural analysis of adult mouse neocortex comparing aldehyde perfusion with cryo fixation." *eLife* 4:e05793. [10.7554/eLife.05793](https://doi.org/10.7554/eLife.05793)
- Peters A, Palay SL, Webster HdeF (1991) *The Fine Structure of the Nervous System: Neurons and Their Supporting Cells*. 3rd ed. Oxford University Press.
- Shapson-Coe A et al. (2021) "A connectomic study of a petascale fragment of human cerebral cortex." *bioRxiv* 2021.05.29.446289. [10.1101/2021.05.29.446289](https://doi.org/10.1101/2021.05.29.446289)
- Shapson-Coe A et al. (2024) "A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution." *Science* 384(6696):eadk4858.
- Walton J (1979) "Lead aspartate, an en bloc contrast stain particularly useful for ultrastructural enzymology." *Journal of Histochemistry and Cytochemistry* 27(10):1337-1342.
- Willingham MC, Rutherford AV (1984) "The use of osmium-thiocarbohydrazide-osmium (OTO) and ferrocyanide-reduced osmium methods to enhance membrane contrast and preservation in cultured cells." *Journal of Histochemistry and Cytochemistry* 32(4):455-460.
- Xu CS et al. (2017) "Enhanced FIB-SEM systems for large-volume 3D imaging." *eLife* 6:e25916.
