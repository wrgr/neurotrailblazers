---
title: "Module 05: Electron Microscopy and Image Basics"
layout: module
permalink: /modules/module05/
description: "Understand EM image formation, artifacts, and interpretation basics for reliable connectomics analysis."
module_number: 5
image: /assets/images/modules/module05.svg
image_alt: "Stylized vector art: an electron beam cone scanning a circular imaging field with raster lines."
difficulty: "Intermediate"
duration: "4 hours"
learning_objectives:
  - "Describe core EM acquisition concepts relevant to connectomics"
  - "Identify common image artifacts and likely downstream impact"
  - "Interpret image quality for segmentation readiness"
  - "Document uncertainty and QA decisions"
prerequisites: "Modules 01-04"
merit_stage: "Foundations"
compass_skills:
  - "Imaging Literacy"
  - "Quality Assessment"
  - "Interpretive Discipline"
ccr_focus:
  - "Knowledge - EM Foundations"
  - "Skills - QA Screening"

# Normalized metadata
slug: "module05"
short_title: "Electron Microscopy and Image Basics"
status: "active"
audience:
  - "students"
pipeline_stage: "Foundations"
merit_row_focus: "Foundations"
topics:
  - "em"
  - "image-quality"
  - "artifacts"
summary: "Foundational EM image interpretation and artifact-aware quality control for connectomics workflows."
key_questions:
  - "Which artifacts critically affect reconstruction quality?"
  - "What minimum image quality supports downstream segmentation?"
slides:
  - "/assets/slides/module05/module05-electron-microscopy-and-image-basics.pdf"
notebook: []
datasets:
  - "/datasets/workflow/"
personas:
  - "/avatars/undergradstudent"
  - "/avatars/gradstudent"
related_tools:
  - "/tools/connectome-quality/"
related_frameworks:
  - "research-incubator-model"
prerequisites_list: []
next_modules:
  - "module06"
  - "module07"
references: []
videos: []
downloads: []
last_reviewed: 2026-09-28
maintainer: "NeuroTrailblazers Team"
content_type: path
---

## Capability target

Evaluate EM image patches for artifact risk and issue a justified pass/rework recommendation.

## Why this module matters
Image quality is the one ceiling nobody downstream can raise. A segmentation model separates two neurites by the intensity edge between them; when staining fades or a knife scratch crosses the field, that edge is gone, and the split or merge it causes is repaired one neurite at a time by a proofreader. The scale makes the asymmetry brutal. MICrONS imaged 26,652 sections over about six months on five microscopes (MICrONS Consortium 2025); a staining gradient noticed at section 200 and passed is a gradient on every section after it, and on every neurite that crosses the affected third of the field.

That is why the person looking at pilot images is making a scientific decision, not a clerical one. The studio scenario puts you in that seat: a facility wants to commit 800 more sections and asks whether to proceed. A "go" you cannot defend, or a "stop" that costs a week for a cosmetic artifact, are both errors with a price. This module gives you the vocabulary (artifact type, severity, predicted segmentation consequence), the three escalation levels and the habit of logging every call so it can be audited later.

It is also the module where you learn what an EM image is, which the later modules assume. Module 06 asks you to fix segmentation errors and Module 07 to allocate a proofreading budget; both go faster when you can look at the image and say why the model failed there.

**Where this sits next to Technical Unit 03.** [Technical Unit 03]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}) covers the tissue-to-image chain in depth: fixation and staining chemistry, sectioning, imaging parameters, an artifact catalog with each artifact's downstream cost, the acquisition QA checks that catch problems, and the provenance metadata that must survive, with a 90-minute lab that writes a QA report on a real volume. This module adds the decision: scoring severity consistently across a set of patches, choosing a pass, flag or hard-stop level and saying who is allowed to make that call, and writing a go/no-go memo with conditions to a facility under time pressure. Do the unit for the chain and the catalog; do this module for the decision and the memo.

## Concept set

### Image quality as a scientific constraint

EM image quality sets an upper limit on segmentation accuracy, and through it on every connectomic claim built on that segmentation. When membrane contrast falls, the segmentation model loses the intensity edge it uses to separate adjacent neurites, and split errors rise. Every downstream analysis result — synapse counts, path lengths, circuit motifs — inherits the quality ceiling set at acquisition. This means that the person evaluating image quality is making a decision that propagates through the entire pipeline. Treating QA as a clerical step rather than a scientific judgment is one of the most common and costly mistakes in connectomics projects.

Students should internalize a core principle: **you cannot proofread your way out of a bad image**. While proofreading can correct segmentation errors one at a time, systematically degraded images produce error rates that overwhelm any realistic proofreading budget. The goal at acquisition is to produce images where automated segmentation succeeds on the vast majority of the volume, leaving proofreaders to handle only the genuinely ambiguous cases.

### Artifact taxonomy linked to downstream error

Each major EM artifact maps to a specific class of segmentation failure. A QA decision rests on this mapping:

- **Knife chatter** (periodic scratches from ultramicrotome blade imperfections) creates false splits by introducing bright linear artifacts that the segmentation model interprets as membranes.
- **Charging artifacts** (localized brightness shifts from electrostatic charge accumulation) produce false splits at low-contrast boundaries where the charging gradient masks the true membrane signal.
- **Tissue folds** introduce non-recoverable topology gaps — the folded region contains overlapping tissue that cannot be computationally unfolded, creating a permanent hole in the reconstruction.
- **Missing sections** (lost or damaged serial sections) cause neurite breaks proportional to the number of consecutive sections lost. Alignment and segmentation can often bridge a single missing section; each additional consecutive loss severs more of the thin neurites passing through that plane.
- **Staining gradients** (uneven heavy metal penetration across the block face) produce spatially varying error rates, meaning that segmentation quality differs across the field of view in ways that are difficult to detect without systematic sampling.

The [Artifact taxonomy]({{ '/content-library/imaging/artifact-taxonomy/' | relative_url }}) page has representative images and mitigation strategies for each type. Read it before the studio activity and return to it afterward.

### QA gates and escalation logic

Not all imaging quality issues require re-acquisition. The concept of go/no-go checkpoints provides a structured framework for deciding when to stop imaging and fix a problem versus when to proceed and manage the issue downstream. The deciding idea is **cost asymmetry**: a staining problem fixed at acquisition costs imaging time once, while the same problem found at proofreading costs proofreader time on every neurite that crosses the affected region.

QA gates should be defined at three levels:

1. **Hard stop** — artifacts that make reconstruction impossible (severe folds, large-area charging, gross contamination). These require immediate re-acquisition or block re-trimming.
2. **Flag and monitor** — artifacts that degrade quality but remain within the tolerance of current segmentation models (mild knife chatter, minor staining gradients). These are logged, and the affected regions are prioritized for proofreading.
3. **Pass** — the image meets all quality thresholds for the target resolution and analysis goals.

Escalation logic should also specify *who* makes the call at each level. A trainee can pass or flag; only the imaging lead should authorize a hard stop and re-acquisition, because the cost of that decision is significant.

### EM modalities for connectomics

Three primary EM modalities are used in modern connectomics, each with distinct tradeoffs in resolution, throughput, and artifact profiles:

- **Serial-section TEM (ssTEM)**: Ultrathin sections are cut, collected on tape or grids, and imaged in a transmission electron microscope. The two largest ssTEM connectomics volumes were both imaged at 4 nm per pixel: FAFB with sections 35-40 nm thick (Zheng et al. 2018) and MICrONS with a nominal section thickness of 40 nm (MICrONS Consortium 2025). Z resolution is set by section thickness, so it is about ten times coarser than XY. High XY resolution enables confident synapse identification, but the large Z step means small neurites can be lost between sections. Artifacts include section folds, knife chatter, and staining variability between sections.
- **Serial block-face SEM (SBEM)**: A diamond knife inside the SEM chamber removes a thin layer from the block face, which is imaged after each cut. In the first demonstration the sections were 50-70 nm thick (Denk and Horstmann 2004); Hua et al. (2015) imaged a 65 × 51 × 41 µm stack of 1,370 slices at a voxel size of 12 × 12 × 30 nm. No section is ever handled, so acquisition runs unattended, but the coarser XY sampling can make small synapses ambiguous. Artifacts include knife chatter, charging, and surface debris.
- **Focused ion beam SEM (FIB-SEM)**: A gallium ion beam mills the block face between images. The voxels can be isotropic: the Janelia hemibrain was imaged at 8 × 8 × 8 nm (Scheffer et al. 2020), and Xu et al. (2017) report that higher resolution is possible on smaller volumes. Isotropic voxels simplify 3D segmentation and let annotators trace the finest neurites in any direction, but throughput is low. Xu et al. (2017) describe continuously imaged volumes above 10⁶ µm³, about 100 µm on a side; the hemibrain went larger by cutting the tissue into slabs and imaging them in parallel. Artifacts include curtaining (ion beam striping) and re-deposition.

The voxel sizes above are the published values for the named volumes, not limits of the methods; each instrument trades resolution against field size and speed. Sources: Zheng et al. (2018), MICrONS Consortium et al. (2025), Denk and Horstmann (2004), Hua et al. (2015), Scheffer et al. (2020) and Xu et al. (2017), all listed under References.

The choice of modality depends on the scientific question. Large-scale circuit mapping favors throughput: MICrONS used serial-section TEM, and H01 used multibeam SEM of serial sections; ultrastructural studies of specific synaptic features may favor FIB-SEM for its isotropic resolution.

### Misconception guardrails

Each of these is a belief a learner plausibly holds on arriving. Name it, then check your own work against it.

- **Misconception guardrail:** you can proofread your way out of a bad image.
- **Misconception guardrail:** a noisy image is worse for segmentation than a clean image with faint membranes.
- **Misconception guardrail:** artifact severity can be judged from a count, when the spatial distribution matters more.
- **Misconception guardrail:** quality assessment is a clerical checkpoint rather than a scientific judgment that propagates through every downstream claim.

## Core workflow

1. Inspect image quality and artifact signatures.
2. Classify severity and likely impact on segmentation.
3. Decide pass/flag/rework with documented rationale.
4. Log findings in a structured QA record for reproducibility.

## 60-minute tutorial run-of-show

**Where the 4 hours go.** The 60-minute tutorial and the roughly 60-minute studio are the taught part. The rest is the pre-class reading (EM principles and the artifact taxonomy), the post-class assignment of three QA log entries from a public volume, the quick practice prompt and, for the instructor, building the patch set before class. Neither course map schedules this kit; the [16-week map]({{ '/teaching/syllabi/16-week/' | relative_url }}#what-this-map-uses-and-omits) keeps its studio only as the week 4 fallback for the Unit 03 viewer lab, so the hours beyond the session are unscheduled — lab meeting or take-home.

### Pre-class preparation (5-10 min async)

Before the session, students should:

- Review the [EM principles]({{ '/content-library/imaging/em-principles/' | relative_url }}) page, focusing on image formation and contrast.
- Preview the artifact gallery on the [Artifact taxonomy]({{ '/content-library/imaging/artifact-taxonomy/' | relative_url }}) page and find three examples: one clean image, one with moderate knife chatter, and one with a tissue fold. For each, note initial impressions of quality.

### Materials needed

- Projected EM image gallery (8-10 patches at varying quality levels) from the instructor's patch set; see *Building the patch set* under the studio activity
- Printed or digital QA decision worksheet (one per student): the [learner worksheet]({{ '/assets/worksheets/module05/module05-activity.md' | relative_url }})
- Timer visible to the class
- Artifact reference card (single page, double-sided): print the severity classification section of the [Artifact taxonomy]({{ '/content-library/imaging/artifact-taxonomy/' | relative_url }}) page

### Minute-by-minute schedule

**00:00-08:00 | EM basics refresher**
- *Instructor cue*: "We are going to start with a fast review. I will show four images — tell me which modality produced each one and why you think so."
- Show four images: three from public volumes acquired by different methods (each dataset's release page names the instrument) and one intentionally ambiguous. Cold-call students for modality identification and reasoning.
- Briefly review how contrast arises from heavy metal staining and electron scattering. Emphasize that membrane visibility depends on staining protocol, not microscope settings alone.

**08:00-20:00 | Artifact recognition walkthrough**
- *Instructor cue*: "Now I am going to show you five artifacts that cause many segmentation failures. For each one, I want you to predict: will this cause a merge error, a split error, or a topology break?"
- Walk through knife chatter, charging, folds, missing sections, and staining gradients with the annotated examples on the [Artifact taxonomy]({{ '/content-library/imaging/artifact-taxonomy/' | relative_url }}) page.
- Where your patch set has an example of the artifact, turn on the public viewer's segmentation layer over it so students can see the predicted error type realized in practice.
- *Formative check*: After the third artifact, pause and ask students to classify the next one independently before revealing the answer.

**20:00-34:00 | Learner triage round**
- *Instructor cue*: "You have 14 minutes. Work in pairs. Each pair receives six image patches from the patch set. For each patch, fill in the QA worksheet: artifact type, severity (1-3), predicted segmentation impact, and your pass/flag/rework decision."
- Circulate and listen for common misconceptions. Note which artifact types cause the most disagreement.
- *Formative check*: At 30:00, ask one pair to share their most difficult call and explain their reasoning.

**34:00-46:00 | QA threshold debate**
- *Instructor cue*: "Pair A said this patch is a pass. Pair B said rework. Both of you, defend your position."
- Facilitate structured debate on 2-3 patches where pairs disagreed. Push students to articulate the cost tradeoff: what is the cost of re-acquiring versus the cost of proofreading the resulting errors?
- Introduce the concept of escalation levels (hard stop, flag and monitor, pass) and ask students to re-classify their six patches using this framework.

**46:00-56:00 | Decision logging practice**
- *Instructor cue*: "A QA decision that is not logged does not exist. You are now going to write a QA log entry for your hardest patch."
- Students write a structured QA entry: image ID, artifact type, severity, decision, rationale, and any conditions (e.g., "pass if proofreading budget is allocated to rows 12-18").
- Show an example of a well-written and a poorly-written QA entry for comparison.

**56:00-60:00 | Competency check**
- *Instructor cue*: "Final check. I am showing one new patch. You have two minutes to write your QA verdict on an index card. Include artifact type, severity, decision, and one sentence of rationale."
- Collect index cards. Review after class to identify students who need follow-up.

### Formative assessment checkpoints

- **08:00**: Can students distinguish EM modalities from image appearance?
- **20:00**: Can students predict segmentation error type from artifact type?
- **34:00**: Can students apply severity ratings consistently across patches?
- **46:00**: Can students articulate cost tradeoffs in QA decisions?
- **56:00**: Can students write a structured QA log entry?

### Post-class assignment

Select three locations in a public volume ([MICrONS](https://www.microns-explorer.org/) or [H01](https://h01-release.storage.googleapis.com/explore.html)) that were not covered in class, and record their coordinates. For each patch, write a complete QA log entry (artifact type, severity, predicted segmentation impact, pass/flag/rework decision, rationale). Submit as a single document. At least one patch should involve an artifact type the student finds personally difficult to assess — include a brief reflection on what makes it challenging.

## Studio activity
{: #studio-activity}

**Scenario:** Your team has received pilot images from a new ssTEM acquisition of mouse visual cortex. The imaging facility reports that initial sections looked good, but they encountered intermittent knife chatter starting around section 200 and a possible staining gradient in the lateral third of the field of view. Before the facility commits to imaging the remaining 800 sections, your team must evaluate the pilot data and deliver a go/no-go recommendation with conditions.

**Task sequence:**
1. **Survey (10 min):** Open the six image patches from the instructor's patch set (three from a clean region, three from regions showing the reported problems). For each patch, independently record: modality confirmation, visible artifacts, and an initial severity impression.
2. **Artifact classification (15 min):** Using the artifact reference card, formally classify each artifact by type and assign a severity score (1 = minor, cosmetic; 2 = moderate, segmentation-affecting; 3 = severe, reconstruction-blocking). Map each artifact to its expected segmentation consequence (merge, split, or topology break).
3. **Spatial pattern analysis (10 min):** Arrange the patches by their spatial position in the volume. Determine whether the artifacts are spatially correlated (e.g., staining gradient affecting one side consistently) or random. Spatially correlated artifacts require different mitigation than random ones.
4. **Cost-benefit analysis (10 min):** For each artifact, estimate the downstream cost if the facility proceeds without fixing it. Consider: how many proofreading hours per affected section? How many sections are likely affected? Compare this to the cost of pausing acquisition for knife replacement or re-staining.
5. **Recommendation memo (15 min):** Write a one-page memo to the imaging facility with your team's recommendation. The memo must include: (a) a summary table of artifacts found, (b) your go/no-go decision with conditions, (c) specific remediation steps if you recommend pausing, and (d) a monitoring plan if you recommend proceeding.

**Expected outputs:**
- Completed QA worksheet for all six patches
- Spatial artifact map (annotated sketch or diagram)
- One-page recommendation memo with summary table

**Time estimate:** Approximately 60 minutes for the full activity. Steps 1-2 can be done individually; Steps 3-5 should be done as a team of 3-4 students.

### Building the patch set (instructor, before class)

The site does not publish EM image patches; build the set from a public volume so
that every patch has a recorded location.

- Use [MICrONS Explorer](https://www.microns-explorer.org/) or the [H01 release](https://h01-release.storage.googleapis.com/explore.html). Choose locations by a rule you state in advance, as in the [Technical Unit 03 lab]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}); browsing for striking images gives a set with no clean baseline.
- Screenshot each location at one fixed zoom and keep a key of coordinates and your own severity call.
- You need 8-10 patches for the gallery, six per pair for the triage round and studio (three clean, three showing chatter, a fold, charging or a contrast gradient), and one unseen patch for the competency check.
- Tell learners the six studio patches stand in for the pilot images in the scenario; they come from a finished public volume, not a new acquisition.
- If the volume you sample has no clear example of an artifact type, use that type's annotated example on the [Artifact taxonomy]({{ '/content-library/imaging/artifact-taxonomy/' | relative_url }}) page and say so.

## Assessment rubric

- **Minimum (pass)**: Accurate identification of major artifacts across all patches, correct mapping to segmentation error type, and a defensible pass/flag/rework decision for each patch.
- **Strong (merit)**: Clear articulation of cost tradeoffs, consistent severity thresholds across patches, spatially aware analysis, and a well-structured recommendation memo with specific conditions.
- **Failure**: Artifact labels assigned without reference to downstream segmentation implications, or QA decisions made without documented rationale.

## Common errors and how to recover

- **Your severity scores drifted across the round.** The first patch got a 2 for chatter you would have called a 1 by the sixth, because your threshold moved as you saw more images. Recover by writing the threshold sentence for each score before you look at any patch ("2 means the model will lose membranes here"), then re-scoring the first patch last and reconciling.
- **You named the artifact but not the failure.** "Knife chatter, severity 2" is half a record. The rubric fails a label that does not say what the segmentation will do with it. Recover by adding the consequence to every row: merge, split or topology break, and where in the field.
- **You costed the fix and not the proceed.** A knife change is hours once; chatter that starts at section 200 and is left alone is proofreader time on every neurite that crosses the remaining 800 sections. Recover by filling both columns of the cost table, in the same unit (hours), before you choose.
- **Your memo has a decision but no conditions.** "Proceed" with nothing attached, or "stop" with no remediation step, gives the facility nothing to act on. Recover with the four parts the memo requires: the artifact table, the decision, the remediation steps if you stop, and the monitoring plan (what is checked, how often, by whom) if you go.
- **You authorized a hard stop from the trainee seat.** Re-acquisition is the imaging lead's call because its cost is high. Recover by escalating with the evidence (patch IDs, coordinates, severity, predicted consequence) and a recommendation, and by recording who made the final decision in the log.
- **Your QA entry cannot be found again.** An entry with no image ID and no coordinates cannot be revisited when the segmentation comes back. Recover by starting every entry with the location, and treating a decision that is not logged as one that did not happen.

## What this module does not cover

- **Tissue preparation and sectioning.** Fixation, heavy-metal staining, embedding and cutting, and the artifacts each step causes, are [Technical Unit 03]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }}) and [Tissue preparation]({{ '/content-library/imaging/tissue-preparation/' | relative_url }}); here you judge the image, not the block.
- **Choosing a modality or running an instrument.** The modality section above is for recognizing what kind of image you are looking at. Imaging parameters and acquisition design are Unit 03; this module does not teach you to set up a microscope.
- **Stitching and alignment.** Registering tiles and sections, alignment versions and the residuals they leave are [Technical Unit 04]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}) and [Acquisition QA]({{ '/content-library/imaging/acquisition-qa/' | relative_url }}).
- **Fixing the errors an artifact causes.** Detecting and correcting merges and splits in the segmentation is [Module 06]({{ '/modules/module06/' | relative_url }}); this module predicts the error, it does not repair it.
- **Allocating proofreading around flagged regions.** Turning a flag-and-monitor decision into a proofreading budget and stopping rule is [Module 07]({{ '/modules/module07/' | relative_url }}) and [Technical Unit 08]({{ '/technical-training/08-segmentation-and-proofreading/' | relative_url }}).
- **Automated QA at scale.** Focus, contrast and alignment metrics computed on every tile are [Acquisition QA]({{ '/content-library/imaging/acquisition-qa/' | relative_url }}); the studio uses your eyes on six patches.
- **Acquisition provenance.** Which metadata must travel with the image stack for the volume to be usable later is Unit 03's provenance section.

## Content library references

- [EM principles]({{ '/content-library/imaging/em-principles/' | relative_url }})
- [Artifact taxonomy]({{ '/content-library/imaging/artifact-taxonomy/' | relative_url }})
- [Tissue preparation]({{ '/content-library/imaging/tissue-preparation/' | relative_url }})
- [Acquisition QA]({{ '/content-library/imaging/acquisition-qa/' | relative_url }})
- [MICrONS visual cortex]({{ '/content-library/case-studies/microns-visual-cortex/' | relative_url }})

## Teaching resources

- [Technical Unit 03]({{ '/technical-training/03-em-prep-and-imaging/' | relative_url }})
- [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})

## Quick practice prompt

Pick one artifact and explain how it could create a merge or split error later. Then estimate: if this artifact appears on 5% of sections, how many additional proofreading hours would it add to a 1000-section volume?

## Academic references
- Briggman, K. L., & Bock, D. D. (2012). Volume electron microscopy for neuronal circuit reconstruction. *Current Opinion in Neurobiology*, 22(1), 154-161.
- Denk, W., & Horstmann, H. (2004). Serial block-face scanning electron microscopy to reconstruct three-dimensional tissue nanostructure. *PLoS Biology*, 2(11), e329.
- Hua, Y., Laserstein, P., & Helmstaedter, M. (2015). Large-volume en-bloc staining for electron microscopy-based connectomics. *Nature Communications*, 6, 7923.
- Peters, A., Palay, S. L., & Webster, H. deF. (1991). *The Fine Structure of the Nervous System: Neurons and Their Supporting Cells* (3rd ed.). Oxford University Press.
- Hayworth, K. J., Morgan, J. L., Schalek, R., Berger, D. R., Hildebrand, D. G. C., & Lichtman, J. W. (2014). Imaging ATUM ultrathin section libraries with WaferMapper: A multi-scale approach to EM reconstruction of neural circuits. *Frontiers in Neural Circuits*, 8, 68.
- Zheng, Z., et al. (2018). A complete electron microscopy volume of the brain of adult *Drosophila melanogaster*. *Cell*, 174(3), 730-743. doi:10.1016/j.cell.2018.06.019
- MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*, 640, 435-447. doi:10.1038/s41586-025-08790-w
- Scheffer, L. K., et al. (2020). A connectome and analysis of the adult *Drosophila* central brain. *eLife*, 9, e57443. doi:10.7554/eLife.57443
- Xu, C. S., et al. (2017). Enhanced FIB-SEM systems for large-volume 3D imaging. *eLife*, 6, e25916. doi:10.7554/eLife.25916
