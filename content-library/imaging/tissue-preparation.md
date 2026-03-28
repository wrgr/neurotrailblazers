---
layout: page
title: "Tissue Preparation"
permalink: /content-library/imaging/tissue-preparation/
description: "Complete guide to tissue preparation for connectomics EM — fixation, staining, embedding, and sectioning. Full instructor script with protocols, decision points, and references."
topics:
  - tissue-preparation
  - fixation
  - staining
  - sectioning
  - embedding
primary_units:
  - "03"
difficulty: "Intermediate"
---

## Overview

The goal of tissue preparation for connectomics is to stabilize biological ultrastructure, make it visible to electrons, and present it in a format compatible with serial imaging. Every step in the preparation chain — fixation, staining, dehydration, embedding, and sectioning — introduces tradeoffs between preservation fidelity, contrast quality, and throughput. Understanding these tradeoffs is essential for anyone who interprets EM data, because preparation choices create the artifact profile that propagates through the entire reconstruction pipeline.

---

## Instructor script: the preparation pipeline

### Step 1 — Fixation

**Purpose:** Halt biological degradation and crosslink macromolecules in place, preserving ultrastructure as close to the living state as possible.

**Primary fixatives for connectomics:**

- **Glutaraldehyde (GA)**: The workhorse fixative for EM. A bifunctional crosslinker that bridges amino groups on adjacent proteins, creating a rigid meshwork. Concentration: typically 2-2.5% in phosphate or cacodylate buffer. Penetration rate: ~1 mm/hour (Bhatt & Bhatt, various). Provides excellent ultrastructural preservation but does not fix lipids — hence the need for subsequent osmium treatment.

- **Paraformaldehyde (PFA)**: A smaller, monofunctional crosslinker that penetrates faster than GA but provides weaker fixation. Often combined with GA (e.g., 4% PFA + 2.5% GA) for rapid initial stabilization followed by thorough crosslinking. PFA alone is insufficient for EM-quality preservation.

- **Fixation route matters enormously:**
  - *Transcardial perfusion* (rodents): Fixative pumped through the vasculature under pressure. Reaches all brain regions simultaneously via capillary beds. Provides the most uniform fixation for whole-brain studies. Standard for mouse/rat connectomics (MICrONS, MouseConnects).
  - *Immersion fixation* (human tissue, invertebrates): Tissue block placed directly in fixative solution. Fixation proceeds from the surface inward — creating a gradient where the surface is well-fixed and the interior may show degradation before fixative arrives. The H01 human cortex dataset (Shapson-Coe et al. 2024) used surgically resected tissue fixed by immersion, which contributed to quality variations across the block.

**Teaching point:** "The best microscope in the world cannot rescue poorly fixed tissue. Fixation quality sets the ceiling on every downstream step."

**Time-critical nature:** Post-mortem delay between tissue death and fixation onset is the single largest variable in human tissue quality. Even 5-10 minutes of ischemia can produce visible ultrastructural degradation (swollen mitochondria, disrupted membranes). For human surgical tissue, the workflow from operating room to fixative must be optimized.

### Step 2 — Post-fixation with osmium tetroxide

**Purpose:** Fix lipid membranes and deposit heavy metal for electron contrast.

**Chemistry:** OsO₄ reacts with unsaturated double bonds in lipid bilayers, crosslinking them and depositing osmium (Z=76, very high atomic number) at membrane sites. This is the primary source of membrane visibility in EM.

**Standard protocol:** 1-2% OsO₄ in buffer for 1-2 hours. For volume EM requiring deep penetration, the rOTO (reduced osmium-thiocarbohydrazide-osmium) protocol repeats the osmium treatment:

1. Reduced osmium (OsO₄ + ferrocyanide) — 1-2 hours
2. Thiocarbohydrazide (TCH) — bridges osmium layers — 20-30 minutes
3. Second OsO₄ treatment — 1-2 hours

The rOTO protocol (Hua et al. 2015) provides much stronger and more uniform membrane contrast throughout large tissue blocks, which is critical for SBEM and FIB-SEM where you cannot post-stain individual sections.

**Key decision point:** rOTO vs standard osmium. rOTO is standard for volume EM. Standard single-osmium may suffice for ssTEM where sections will be post-stained with uranyl acetate and lead citrate.

### Step 3 — En bloc staining (for volume EM)

**Purpose:** Deposit additional heavy metals throughout the block for contrast enhancement, since individual sections cannot be stained after SBEM/FIB-SEM cutting.

**Typical agents:**
- **Uranyl acetate (UA)**: Binds nucleic acids and proteins. Enhances contrast of ribosomes, chromatin, PSDs. Often applied as 1-2% aqueous solution or in 70% ethanol during dehydration. Safety note: uranyl acetate is mildly radioactive and toxic — some labs are shifting to non-radioactive alternatives (e.g., lanthanide-based stains).
- **Lead aspartate**: Enhances general contrast. Applied en bloc after osmication. Walton (1979) protocol adapted for connectomics.

**Penetration challenge:** These stains must penetrate uniformly through blocks that may be 1-3 mm on a side. Incomplete penetration creates the staining gradients described in artifact-taxonomy.md. Protocol optimization (temperature, time, agitation) is critical.

### Step 4 — Dehydration

**Purpose:** Remove water from the tissue to allow infiltration with hydrophobic embedding resin.

**Standard approach:** Graded ethanol or acetone series (30%, 50%, 70%, 90%, 100%, 100%). Each step typically 10-30 minutes. The gradual replacement minimizes osmotic shock that could distort ultrastructure.

**Artifact risk:** Dehydration extracts some lipids (even after osmium fixation) and causes tissue shrinkage (typically 10-20% linear). This shrinkage is largely irreversible and must be accounted for when comparing EM measurements to in vivo dimensions.

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
- ATUM (automated tape-collecting ultramicrotome — Hayworth et al. 2014) enables automated collection of thousands of sections on continuous tape

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

**Scenario:** You are planning a connectomics study of mouse barrel cortex layer 4, targeting a 200×200×200 μm volume. You want to identify all synapses between thalamocortical axons and layer 4 stellate cells.

**Decision sequence:**

1. **Fixation:** Transcardial perfusion with 2.5% GA + 2% PFA in 0.1M sodium cacodylate buffer. Perfusion ensures uniform fixation across the target region. Post-fix in same solution for 12-24 hours at 4°C.

2. **Vibratome sectioning:** Cut 200 μm thick sections on vibratome. Select the section containing barrel cortex L4 using cytochrome oxidase staining of adjacent sections (barrels are visible as dense staining).

3. **Post-fixation and staining:** rOTO protocol for uniform en bloc contrast (planning to use SBEM). OsO₄-ferrocyanide → TCH → OsO₄ → UA in ethanol → lead aspartate.

4. **Embedding:** Epon resin, standard infiltration. Flat-embed to orient barrel columns perpendicular to the sectioning plane.

5. **Imaging modality choice:** SBEM at 8×8×25 nm voxel size. Rationale: need to resolve synapses (requires <10 nm XY) over a 200 μm cube (too large for FIB-SEM); 25 nm z is adequate for tracing most axons; SBEM provides automatic z-alignment.

6. **Estimated data volume:** 200 μm ÷ 8 nm = 25,000 pixels per side (XY) × (200 μm ÷ 25 nm = 8,000 sections). Total: ~5 teravoxels → ~5 TB at 8-bit per voxel.

---

## Protocol comparison table

| Parameter | ssTEM (ATUM) | SBEM | FIB-SEM |
|-----------|-------------|------|---------|
| Section thickness | 30-50 nm | 25-30 nm | 4-8 nm |
| XY resolution | 1-4 nm | 8-12 nm | 4-8 nm |
| Volume range | mm³ | 500 μm per side | 50-100 μm per side |
| Sectioning artifacts | Compression, folds, tears | Knife chatter | Ga curtaining |
| Re-imaging possible? | Yes | No (destructive) | No (destructive) |
| En bloc staining required? | Optional (post-stain OK) | Required | Required |
| Alignment | Requires computational registration | Inherent (block face) | Inherent (block face) |
| Typical project duration | 6-18 months imaging | 3-12 months | 1-6 months |

---

## Common misconceptions

| Misconception | Reality | Teaching note |
|---|---|---|
| "Standard fixation is good enough for EM" | PFA-only fixation (common for immunohistochemistry) is insufficient for ultrastructural preservation | EM requires glutaraldehyde-based fixation with osmium post-fixation |
| "Staining is just for visibility" | Heavy metals also crosslink membranes (osmium), providing additional structural stabilization | Staining and fixation serve overlapping purposes |
| "Tissue looks the same as in vivo" | Processing shrinks tissue 10-30% and extracts some components | Always state that EM measurements are from fixed/processed tissue |
| "FIB-SEM is always better" | FIB-SEM has the best resolution but the smallest field of view — it's not suitable for large-circuit mapping | Match modality to question |

---

## References

- Denk W, Horstmann H (2004) "Serial block-face scanning electron microscopy." *PLoS Biology* 2(11):e329.
- Hayworth KJ et al. (2014) "Ultrastructurally smooth thick partitioning and volume stitching for large-scale connectomics." *Nature Methods* 12:319-322.
- Hua Y, Laserstein P, Bhatt M (2015) "Large-volume en-bloc staining for electron microscopy-based connectomics." *Nature Communications* 6:7923.
- Knott G et al. (2008) "Serial section scanning electron microscopy of adult brain tissue using focused ion beam milling." *Journal of Neuroscience* 28(12):2959-2964.
- Peters A, Palay SL, Webster HdeF (1991) *The Fine Structure of the Nervous System: Neurons and Their Supporting Cells*. 3rd ed. Oxford University Press.
- Shapson-Coe A et al. (2024) "A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution." *Science* 384(6696):eadk4858.
- Walton J (1979) "Lead aspartate, an en bloc contrast stain particularly useful for ultrastructural enzymology." *Journal of Histochemistry and Cytochemistry* 27:1337-1342.
- Xu CS et al. (2021) "Enhanced FIB-SEM systems for large-volume 3D imaging." *eLife* 10:e65541.
