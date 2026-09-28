---
title: "Module 21: Reproducibility and FAIR Principles in Connectomics"
layout: module
permalink: /modules/module21/
description: "Operationalize reproducibility and FAIR principles for connectomics datasets, code, and releases."
module_number: 21
image: /assets/images/modules/module21.svg
image_alt: "Stylized vector art: a pipeline of linked, openly latched stages."
difficulty: "Intermediate to Advanced"
duration: "4-5 hours"
learning_objectives:
  - "Apply FAIR principles to connectomics data products"
  - "Define minimum reproducibility metadata for analysis releases"
  - "Build transparent methods/parameter logs for peer reuse"
  - "Identify hidden-curriculum norms in reproducibility expectations"
prerequisites: "Modules 18-20 or equivalent workflow/inference practice"
merit_stage: "Dissemination"
compass_skills:
  - "Reproducibility"
  - "Research Stewardship"
  - "Documentation"
ccr_focus:
  - "Skills - Reproducible Science"
  - "Character - Accountability"

# Normalized metadata
slug: "module21"
short_title: "Reproducibility and FAIR Principles"
status: "active"
audience:
  - "students"
pipeline_stage: "Dissemination"
merit_row_focus: "Dissemination"
topics:
  - "reproducibility"
  - "fair"
  - "documentation"
summary: "Make connectomics outputs reusable and trustworthy through FAIR metadata, versioning, and transparent methods."
key_questions:
  - "What minimum metadata is needed for third-party reuse?"
  - "How should dataset/code versioning be documented in publications?"
  - "Which reproducibility norms are implicit and must be taught explicitly?"
slides: []
notebook: []
datasets:
  - "/datasets/workflow/"
  - "/datasets/mouseconnects/"
personas:
  - "/avatars/gradstudent"
  - "/avatars/mentor"
related_tools:
  - "/tools/connectome-quality/"
related_frameworks:
  - "research-incubator-model"
  - "education-models"
prerequisites_list:
  - "Basic data-processing workflow familiarity"
  - "Basic manuscript methods section familiarity"
next_modules:
  - "module22"
references:
  - "Wilkinson MD et al. (2016) The FAIR Guiding Principles for scientific data management and stewardship. Scientific Data 3:160018."
  - "Peng RD (2011) Reproducible research in computational science. Science 334(6060):1226-1227."
  - "Sandve GK, Nekrutenko A, Taylor J, Hovig E (2013) Ten simple rules for reproducible computational research. PLoS Computational Biology 9(10):e1003285."
  - "Stodden V et al. (2016) Enhancing reproducibility for computational methods. Science 354(6317):1240-1241."
  - "Lamprecht A-L et al. (2020) Towards FAIR principles for research software. Data Science 3(1):37-59."
  - "Dorkenwald S et al. (2025) CAVE: Connectome Annotation Versioning Engine. Nature Methods 22(5):1112-1120."
videos: []
downloads: []
last_reviewed: 2026-09-28
maintainer: "NeuroTrailblazers Team"
content_type: path
---

## Capability target
Publish a reproducibility-ready connectomics package (data + methods + metadata + limitations) that an external group can audit and reuse.

## Why this module matters
Connectomics studies are technically dense and often impossible to interpret without exact workflow context. A result nobody else can rerun cannot be checked, so FAIR packaging and reproducibility are part of whether the result is valid.

## Concept set
### 1) FAIR as implementation checklist
- **Technical:** findable identifiers, accessible storage, interoperable formats, and reusable metadata each require concrete engineering choices.
- **Plain language:** "FAIR" only counts if someone else can actually find, open, and use your work.
- **Misconception guardrail:** posting files online makes work FAIR.
- **Why it fails:** a file with no persistent identifier, no metadata and no license can be downloaded but not found, cited or legally reused. Each of the four letters is a separate check, and a URL on its own passes none of them.

### 2) Reproducibility is layered
- **Technical:** computational reproducibility (same code/data => same result) differs from inferential reproducibility (same conclusion under reasonable variation).
- **Plain language:** rerunning code and trusting conclusions are related but not identical.
- **Misconception guardrail:** a notebook that ran end-to-end once is proof of reproducible science.
- **Why it fails:** it ran once, on one machine, against whatever data version and dependencies were current that day. Reproducibility is a property of a rerun by someone else, from the recorded versions, that gives the same answer.

### 3) Hidden curriculum in reproducibility
- **Technical:** unwritten norms include naming conventions, release etiquette, assumption disclosure, and reviewer-ready method transparency; trainees can only be fairly assessed against these norms after the norms have been taught.
- **Plain language:** many expectations are "known by insiders" unless we teach them directly.
- **Misconception guardrail:** reproducibility norms are common sense that any careful trainee will infer without being taught.
- **Why it fails:** the norms are specific (what to pin, what to name, what to disclose) and they differ between labs. A trainee who has not been told them is being graded on questions that were withheld.

### 4) FAIR applied to connectomics
Each FAIR principle maps to concrete connectomics infrastructure. Findable means assigning DOIs for datasets and providing stable CAVE endpoints that resolve to specific data versions. Accessible means offering open APIs and tools like CloudVolume that allow programmatic data retrieval without manual download. Interoperable means using standard formats such as SWC for neuron morphologies, Zarr for volumetric data, and NWB for neurophysiology so that tools across labs can ingest each other's outputs. Reusable means materialization versioning in CAVE, which lets any researcher retrieve the exact state of the segmentation and annotations at a given point in time.

A practical reproducibility checklist for any connectomics analysis release should include: the dataset version or release identifier, the CAVE materialization number (if applicable), the code commit hash for all analysis scripts, the environment specification (e.g., conda environment file or Docker image), and the full parameter configuration used. Without all five elements, a third party cannot reliably reproduce the analysis, even with access to the same underlying data.

- **Misconception guardrail:** a commit hash and an environment file make a rerun reproducible.
- **Why it fails:** the dataset version and the parameter configuration are the two elements that move most often, and neither lives in the code. The worked example below is a rerun with identical code and a different answer.

### 5) A release is a version, so it needs a deprecation path
- **Technical:** a release that can never be superseded is either never corrected or silently overwritten, and both break every result already published against it. Give each release an identifier, a changelog entry that says what changed and why, and a deprecation note that keeps the old version resolvable and states which results it should no longer be cited for. Version 2 corrects version 1 in public; it does not replace it.
- **Plain language:** fixing a mistake means publishing the fix next to the mistake, not over it.
- **Misconception guardrail:** once a corrected release is out, the old one should be deleted so nobody uses it by accident.
- **Why it fails:** results already published against the old version become unreproducible the moment it disappears. Keep it resolvable, mark it deprecated, and say what the correction changed.

## The five elements, and what breaks without each

| Element | Where it has to appear | What breaks when it is missing |
|---|---|---|
| Dataset release identifier, with a DOI where one exists | Methods, every figure legend, the README | A reader cannot find the data, or two readers analyze different releases and argue about the difference |
| Materialization number or timestamp | Every query, every legend | Root IDs resolve to different objects; the count drifts with no code change, which is the worked example below |
| Code commit hash or release tag | Methods, README, figure caption | The repository link points at code that has changed since the figure was made |
| Environment specification: an exported conda file, a lock file, or a container digest | The repository, next to the code | "Works on my machine"; the first undeclared dependency stops the rerun, and "Python 3.11" is not an environment |
| Parameter configuration, as a file under version control and cited by name | The repository, named in the methods | The rerun uses defaults you did not, and the number changes with no visible cause |

The test for each row is the same: could a stranger, with no channel to ask you questions, rerun the analysis from what is written down?

## Worked example: the number that changed while the code did not

The numbers and release labels below are invented for teaching (fictional releases T21 and T27 of a fictional volume) — they show the shape of the reasoning, not results from any real dataset or release.

In March you report 4,712 synapses between two labeled cell populations. In September a collaborator reruns your notebook, unchanged, and gets 5,103. Nothing in the code changed. Work the five-element checklist as a diagnostic.

**Step 1: dataset version and materialization.** The notebook queries "latest." Proofreading continued for six months, so the segmentation your query resolves against today is not the one you analyzed in March. Root IDs are only meaningful as of a version; querying latest silently re-asks the question against a different brain state. This failure is silent: the code runs and the number looks plausible. The mechanics are [Technical Unit 04]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}) and [provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}).

**Step 2: quantify the drift instead of guessing.** Map your 214 stored root IDs forward with the platform's ID-lineage facility: 183 map 1:1, 24 split into two or more objects, 7 merged into other cells. So 31 of 214 objects changed under you. That churn number belongs in your methods, because it tells every reader how much proofreading moved the ground.

**Step 3: reproduce and update — as two separate acts.** To reproduce March: query release T21 explicitly, and recover 4,712 exactly. To update: rerun against release T27 and get 5,103, which is now a statement about proofreading progress, not a bug. Both acts are legitimate; the error was conflating them by letting "latest" decide which one you were performing.

**Step 4: pin the remaining four elements.** Code commit hash (eight characters in the figure caption), environment specification (an exported conda file or Docker digest — "Python 3.11" is not an environment), the full parameter configuration (synapse threshold of 3, the inclusion radius, every default you touched), and the dataset release identifier with its DOI. The test for each: could a stranger rerun this with no channel to ask you questions?

**Step 5: prove it in a clean room.** A labmate reruns the package from the README alone. Friction log: an undeclared plotting dependency, a hard-coded path into your home directory, and a parameter cell that was edited after the figure was exported. Three fixes, one afternoon. The friction log is the deliverable — a package that has never been rerun cold is "reproducible in principle," which means unverified.

**What gets released.** The data slice with a DOI, the materialization number in every figure caption, the commit hash, the environment file, the parameter configuration, a limitations note naming the excluded samples and any failed runs — and a changelog entry, so that version 2 can deprecate version 1 without erasing it.

**What this example does not establish:** that the September number is wrong. Both numbers are right about different states of the reconstruction; the failure was that the March release could not say which state it described.

## Hidden curriculum scaffold
- What senior reviewers expect but rarely state:
  - Dataset and code version IDs in figure legends/methods.
  - Explicit handling of failed runs and excluded samples.
  - A short "known limitations" section with concrete failure modes.
- How to make these norms visible to trainees:
  - Provide reproducibility checklists before assignments.
  - Share annotated examples of strong/weak method reporting.
  - Require mentorship feedback on documentation, not only results.

## Core workflow: FAIR/reproducibility release
1. Define release scope (dataset slice, code commit, parameter set).
2. Add machine-readable metadata and provenance fields.
3. Validate rerun path in a clean environment.
4. Write methods/limitations notes for external users.
5. Publish with changelog and deprecation policy.

## Time budget
The declared 4 to 5 hours are: the 15-minute pre-class reading below and about 30 minutes on the concept set, the 90-minute meeting the [16-week syllabus map]({{ '/teaching/syllabi/16-week/' | relative_url }}) gives this kit in week 12 (the 60-minute run-of-show below plus the opening of the studio activity; the 10-week map leaves this kit out), and 2 to 3 hours outside class completing the clean-environment rerun and the studio package, the quick practice prompt, and the linked readings.

## 60-minute tutorial run-of-show

### Pre-class preparation (15 min async)
- Bring one analysis you have run, in whatever state it is in. It does not need to be tidy; untidy is more useful here.
- Read section 2 of [Technical Unit 04]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}), on materialization versions and root-ID instability.

### Minute-by-minute plan
1. **00:00-06:00 | Framing: the silent bug**
   - Prompt: "Your notebook ran fine last month and gives a different number today. Nothing in your code changed. What happened?"
   - Establish that analysis against an unpinned segmentation fails silently: no error, a plausible number, a different question.
2. **06:00-16:00 | The five-element checklist, modeled**
   - Instructor walks one real analysis through: dataset release ID, materialization number, code commit hash, environment specification, parameter configuration.
   - Show what breaks when each one is missing, in turn.
3. **16:00-30:00 | Guided practice: audit your own work**
   - Learners score their brought-in analysis against the five elements. Most will fail two or three; say so in advance to make that safe.
   - Produce a remediation list ordered by how cheap each fix is.
4. **30:00-40:00 | Clean-environment rerun**
   - Attempt a rerun of a partner's analysis from their instructions alone, without asking them questions.
   - Log every point of friction. The friction log is the deliverable, not the successful rerun.
5. **40:00-50:00 | Known limitations, written honestly**
   - Each learner drafts a limitations paragraph naming concrete failure modes, excluded samples, and failed runs — not generic caveats.
   - Discuss why this is a hidden-curriculum norm: reviewers expect it, and almost nobody is taught to write it.
6. **50:00-57:00 | Competency check**
   - Submit: completed five-element record, friction report on a partner's package, and one limitations paragraph.
7. **57:00-60:00 | Exit ticket**
   - "One thing in my current work that another person could not reproduce today."

### Formative checkpoints
- **At 30 minutes:** every learner has identified at least one missing element in their own work. A learner reporting five out of five has probably not audited honestly — check.
- **At 50 minutes:** limitations paragraphs name specific failure modes rather than generic hedges.

## Studio activity: reproducibility hardening sprint
{: #studio-activity}
**Scenario:** Your lab plans to release a connectomics analysis package to collaborators at another institution, who will rerun it without being able to ask you questions. The package is the analysis you brought to this session; if you have none, use your Module 03 notebook.

**Tasks**
1. Build a FAIR metadata sheet for one analysis output.
2. Create a reproducibility checklist with pass/fail criteria.
3. Draft a "known limitations" section and one deprecation note.
4. Peer-test another team's package for reuse friction.

**Expected outputs**
- FAIR metadata form.
- Reproducibility checklist + validation log.
- Reuse friction report with remediation recommendations.

## Assessment rubric
- **Minimum pass**
  - All five provenance elements present: dataset release ID, materialization number, code commit hash, environment specification, parameter configuration.
  - Re-run instructions testable by a peer without contacting the author.
  - Limitations name concrete failure modes, excluded samples, and failed runs rather than generic hedges.
- **Strong performance**
  - Clean-environment rerun actually attempted, with a friction log and remediations ordered by cost.
  - Hidden norms made explicit: version identifiers in figure legends, a changelog, and a deprecation note.
  - ID churn quantified whenever identifiers cross versions, and reported in the methods.
  - Documentation is audit-friendly: an external reader can locate every provenance element from the README alone.
- **Common failure modes**
  - Missing version identifiers for data or code.
  - Methods that omit key parameters or the environment specification.
  - "Reproducible in principle" claims without a validation rerun.
  - Limitations sections written as boilerplate rather than as concrete guidance.

## Common errors and how to recover

- **Root IDs stored without a version.** Six months later they resolve to different objects, or to nothing. Recover by finding the original timestamp (query logs, file dates), mapping the IDs forward through the lineage facility, and reporting the churn. If the timestamp is unrecoverable, the analysis must be rerun on a pinned version and the paper must say so.
- **"It works on my machine."** The environment lives only in your shell history. Recover by exporting the environment specification and rerunning in a fresh container; treat every undeclared dependency the rerun exposes as a bug fix, not an embarrassment.
- **Metadata complete, limitations generic.** "Results may be affected by reconstruction errors" guides no one. Recover by rewriting the limitations to name the excluded samples, the failed runs, and the single parameter the headline result is most sensitive to.
- **Files posted but unusable.** No stable identifier, no license, a proprietary format. Recover by minting a DOI or stable ID, converting to standard formats (SWC, Zarr, NWB), attaching a license, and adding a README whose first section is the rerun path.
- **Provenance reconstructed after the paper was written.** Retroactive provenance is guesswork wearing a checklist. Recover partially by auditing which elements can still be verified and flagging the rest; prevent the recurrence by capturing all five elements at analysis time — a recording cell at the top of every notebook costs five lines.

## What this module does not cover

- **The versioning infrastructure itself.** ChunkedGraph mechanics, materialization, and root-ID lineage are [Technical Unit 04]({{ '/technical-training/04-volume-reconstruction-infrastructure/' | relative_url }}) and [provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}).
- **Format specifications.** What SWC, Zarr, and NWB actually contain and when to use each is [data formats and representations]({{ '/content-library/infrastructure/data-formats/' | relative_url }}).
- **Whether the pinned analysis is statistically sound.** Reproducing a result exactly does not make it right; inference validity is [Module 20]({{ '/modules/module20/' | relative_url }}).
- **Storage, cost, and query infrastructure.** Sizing and operating the systems that hold the data is [Module 12]({{ '/modules/module12/' | relative_url }}).
- **Writing and presenting the released work.** The manuscript is [Module 17]({{ '/modules/module17/' | relative_url }}); the talk is [Module 22]({{ '/modules/module22/' | relative_url }}).
- **Data governance and sharing agreements.** Licensing law, embargoes, and consortium policy are institution-specific and handled outside this curriculum; this module covers only what a release must contain to be reusable.

## Content library references
- [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}) — CAVE materialization and pipeline lineage
- [Data formats and representations]({{ '/content-library/infrastructure/data-formats/' | relative_url }}) — Standard formats for interoperability
- [Proofreading tools]({{ '/content-library/proofreading/proofreading-tools/' | relative_url }}) — CAVE as a model for versioned science

## Teaching resources
- Workflow context: [Connectomics workflow]({{ '/datasets/workflow/' | relative_url }})
- Reference context: [Atlas Connectomics Reference]({{ '/technical-training/atlas-connectomics-reference/' | relative_url }})
- Quality context: [Connectome Quality tool]({{ '/tools/connectome-quality/' | relative_url }})
- Mentorship support: [Ask an Expert]({{ '/ask-an-expert/' | relative_url }})

## Evidence anchors from connectomics practice
### Key datasets/platforms
- [H01 dataset landing page](https://h01-release.storage.googleapis.com/landing.html)
- [MICrONS Explorer](https://www.microns-explorer.org/)
- [FlyWire](https://flywire.ai/)
- [Workflow overview]({{ '/datasets/workflow/' | relative_url }})

### Competency checks
- Can an external learner rerun your result with your documentation alone?
- Are dataset and code versions explicit in every core artifact?
- Are your known limitations concrete enough to guide interpretation?

## Academic references
- Wilkinson MD et al. (2016) "The FAIR Guiding Principles for scientific data management and stewardship." *Scientific Data* 3:160018. doi:10.1038/sdata.2016.18. The four principles Concept 1 turns into engineering choices.
- Peng RD (2011) "Reproducible research in computational science." *Science* 334(6060):1226-1227. doi:10.1126/science.1213847. The reproducibility spectrum, from a description of the method to code plus data; Concept 2's layers.
- Sandve GK, Nekrutenko A, Taylor J, Hovig E (2013) "Ten simple rules for reproducible computational research." *PLoS Computational Biology* 9(10):e1003285. doi:10.1371/journal.pcbi.1003285. Version everything, record every parameter, keep the raw data; the rules behind the five elements.
- Stodden V et al. (2016) "Enhancing reproducibility for computational methods." *Science* 354(6317):1240-1241. doi:10.1126/science.aah6168. Why journals ask for the data, code and environment, not a promise of them.
- Lamprecht A-L et al. (2020) "Towards FAIR principles for research software." *Data Science* 3(1):37-59. doi:10.3233/DS-190026. FAIR applied to the code rather than the data, including identifiers and versioning for software.
- Dorkenwald S et al. (2025) "CAVE: Connectome Annotation Versioning Engine." *Nature Methods* 22(5):1112-1120. doi:10.1038/s41592-024-02426-z. Materialization versions and root-ID lineage: the mechanism behind the worked example.

## Quick practice prompt
Take one prior analysis output and add:
1. provenance metadata,
2. reproducibility instructions,
3. a 5-line limitations section.
