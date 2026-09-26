---
layout: page
title: "Ethics and Governance: instructor model responses"
permalink: /teaching/lectures/ethics-and-governance-answers/
slug: ethics-and-governance-answers
content_type: delivery
description: "A worked license audit, human-tissue checks, a proofreading-credit rule and a model data-use statement."
---

[Learner worksheet]({{ '/teaching/lectures/ethics-and-governance-activity/' | relative_url }}) · [Lecture plan]({{ '/teaching/lectures/ethics-and-governance/' | relative_url }})

The team and its release are **invented**; the license facts are real as checked for
this site. None of this is legal advice. Accept other reasoning that states its limits.

## 1. License and terms audit

| Dataset | Data license and where stated | Part A | Part B startup | Release must include |
|---|---|---|---|---|
| MICrONS | CC BY 4.0, microns-explorer.org terms | Yes | Not used | Attribution, modifications marked, license link, no added restrictions; cite MICrONS Consortium et al. (2025) |
| H01 | CC BY 4.0, the release's data page (not its landing page) | Yes | Not used | Attribution; cite Shapson-Coe et al. (2024) |
| FlyWire v783 | CC BY-NC 4.0, flywire.ai/guidelines | Yes, noncommercially | **No** | Attribution; the papers in FlyWire's citation guide; a clear NonCommercial label on derived files |
| Hemibrain | **Unresolved:** Janelia's project page links CC BY 4.0; the v1.0 deposit's DataCite record says CC BY-NC 4.0 | Only after checking; both readings allow noncommercial sharing | **Not until resolved** | Both sources and the version named; cite Scheffer et al. (2020) |

A figure from the FlyWire *Nature* paper falls under the article license, CC BY 4.0.
The connectome falls under the data license. Part B cannot go to the startup while it
contains FlyWire connectivity, whatever the hemibrain answer turns out to be.

For hemibrain, a strong answer does not pick a license. It records both sources and
the version used, asks Janelia FlyEM which terms govern that version, and takes the
question to the institution's compliance or technology transfer office. Until then
it treats the restrictive reading as the working assumption for commercial use.

## 2. Human tissue before reuse

- **Ethics statement:** the main *Science* article carries none. Look in the
  supplementary Materials and Methods, and record the section and date checked. If it
  cannot be found, say so and ask the data providers. Do not cite a landing page as
  evidence of review.
- **Voxels:** a 1 mm³ volume at 4 nm has no face and no direct identifiers. Residual
  risk is contextual and lives in metadata and prose.
- **README:** remove hospital and surgery year, and point to the published provenance
  instead of restating it. Keep region and pathology, which a reuser needs to interpret
  the tissue. The cost is some convenience, not the science.
- **Model training:** open. Whether consent to research use extends to training and
  releasing a model is not settled, and a CC BY license does not answer it. Ask the
  institution's review board or compliance office and the data providers; state the
  question in the release.
- **Rewrite:** “Trained on imagery from about 1 mm³ of middle temporal gyrus from one
  person with drug-resistant epilepsy, and on MICrONS mouse visual cortex, the model
  segments…” Claims about “the human cortex” are out of scope.

## 3. Credit plan

With twelve contributors, named individual authorship with a contributions statement
is workable. An acceptable alternative sets a written threshold for authorship and
gives the rest named acknowledgement plus per-contribution platform credit. Map
proofreading onto one CRediT role, such as *Validation* (where H01 filed it) or
*Data curation*, and write that mapping down. Measure effort from edit histories. Tell everyone
the rule, including the course undergraduates, before they start. Anyone below the
threshold loses authorship, indexing under their own name and citation credit.

## 4. Model governance note

“Derived tables use MICrONS (CC BY 4.0), H01 (CC BY 4.0) and FlyWire v783 (CC BY-NC
4.0); cite the papers each source names. FlyWire-derived files may not be used
commercially. Hemibrain terms are unresolved: Janelia's page states CC BY 4.0 and the
v1.0 deposit states CC BY-NC 4.0, so do not use hemibrain-derived files commercially.
H01 is surgical tissue from one person with drug-resistant epilepsy; results do not
describe human cortex in general. Open question for our compliance office: does the
H01 consent cover releasing a trained model?”

## Feedback guide

Score **0–2 each** for license accuracy, handling of uncertainty, human-tissue scope
and respect, and the credit rule. Two means explicit and correct, one means a
recoverable omission, zero means absent or contradictory. A proficient response has
at least 6/8 and no zero in license accuracy or handling of uncertainty. This is a
local teaching rubric, not a validated assessment instrument.

**Do not reward** a confident legal conclusion, a hemibrain row resolved by assertion,
a claim that H01 carries zero risk or is identifiable from its images, speculation
about the donor, invented statutes or dates, or “acknowledge them” without saying
what the contributor loses. Teaching material: CC BY-SA 4.0, NeuroTrailblazers.
