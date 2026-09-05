---
layout: page
title: "Ethics and Governance"
permalink: /content-library/connectomics/ethics-and-governance/
image: /assets/images/content-library/connectomics/ethics-and-governance.svg
image_alt: "Stylized vector art: a network graph with one community circled."
description: >
  Connectomics has no current human-subjects problem: its human data is
  discarded surgical tissue and nothing published identifies anyone. What is live
  now is licence compliance and credit for proofreading labour; what is
  prospective — consent framings at whole-brain scale, de-identification, neural-data
  regulation, dual use — is set out here as a discussion rather than a checklist.
topics:
  - research ethics
  - informed consent
  - human tissue
  - de-identification
  - data licences
  - dual use
  - credit and authorship
primary_units:
  - "01"
  - "08"
difficulty: intermediate
tags:
  - methodology:research-ethics
  - methodology:data-governance
  - methodology:reproducibility
  - infrastructure:data-sharing
  - proofreading:attribution
  - case-studies:H01
  - case-studies:FlyWire
  - case-studies:MICrONS
micro_lesson_id: ml-conn-ethics-governance
combines_with:
  - h01-human-cortex
  - provenance-and-versioning
  - flywire-whole-brain
use_layout_hero: false
content_type: core
---

# Ethics and Governance

**Start with the honest assessment: connectomics does not currently have a
human-subjects problem.** Its flagship human dataset is discarded surgical
tissue that was going to be removed regardless, reviewed under the same
frameworks that govern any human-tissue study. Nothing in this field asks a
person to undergo a procedure for research, and nothing published so far
identifies anyone. If you came here expecting a controversy, there isn't one to
report.

Two things are nonetheless live **now**, and they are practical rather than
philosophical:

- **Licence obligations** (§3). Three major portals redistribute under
  incompatible terms, and a reuser who ignores them is simply in breach.
- **Credit for proofreading labour** (§5). Tens of thousands of hours of human
  correction sit behind every published connectome, and how that work is
  credited decides real careers. This is the one section of this page about
  people who are affected today.

The rest is **prospective**, and worth discussing precisely because it is not yet
urgent. Consent framings written for a cubic millimetre of discarded tissue
(§1) were not written for whole-brain human volumes, for datasets that become
machine-learning corpora, or for a regulatory environment now drafting rules
about "neural data" (UNESCO adopted the first global standard in November 2025).
De-identification (§2) is a non-issue at today's volumes and an open question at
tomorrow's. Dual-use arguments (§4) are weak for a field with no pathogens and
should be stated at their real strength, not inflated.

Treat the prospective sections as a seminar, not a compliance checklist. The
right time to reason about them is before a project needs the answer.

This page holds the **facts**. The decisions you make with them — how to review
a manuscript, how to write an authorship policy, how to raise a concern — are
taught in [Module 19]({{ '/modules/module19/' | relative_url }}). Use this page
when you need to check what a licence says or where a dataset came from; use
the module when you need to practise the judgement.

---

## 1. Consent and human brain tissue

### Where H01 came from

The site's human reference volume has a specific and documentable provenance.
Shapson-Coe et al. (2024) describe the sample as a "rapidly preserved,
170-µm-thick slab of human cortex from the anterior part of the middle temporal
gyrus of a 45-year-old female", of "just over 1 mm³", which "was removed to gain
access to an epileptic focus in the underlying hippocampus". It was cut into
5,019 sections of mean thickness 33.9 nm, imaged by multibeam SEM at 4 × 4 nm,
and yielded a dataset of about 1.4 petabytes containing roughly 57,000 cells and
150 million synapses.

The ethical structure follows from that description. The tissue is a **surgical
by-product**: in the authors' framing, human specimens become available "from
neurosurgical interventions for neurological conditions in which pieces of the
cortex are discarded because they obstruct access to a pathological site". No
tissue was removed for research that would not otherwise have been removed.
That is the strongest position human connectomics can currently occupy, and it
is why H01 — rather than any purpose-collected human sample — is the field's
reference volume.

### What the paper does and does not say

Two things are worth knowing before you cite H01 in an ethics context.

**The main article carries no consent or IRB statement.** A full-text search of
the published *Science* article for "consent", "IRB", "ethics" and
"Institutional Review" returns nothing; the data-availability statement points
at the release landing page, and the licence line covers the article, not the
data. The consent and approval details live in the supplementary Materials and
Methods. **When you reuse human tissue data, find the ethics statement before
you cite the dataset, and say where you found it.** A citation to a landing page
is not a citation to an ethics review.

**The paper is explicit about the sample's pathology.** It states that human
surgical samples "originate in individuals with pathologies of the nervous
system such as epilepsy, tumors, or neurodegenerative diseases" and that in this
case "we cannot exclude the possibility that long-term epilepsy, or its
pharmacological treatment, had subtle effects on the nanometer-scale structure
of the tissue". This is simultaneously a scientific caveat and an ethical one:
every claim of the form "the human brain does X, as shown by H01" is really a
claim about tissue from one adult woman with drug-resistant epilepsy. Section 4
returns to why that matters beyond the lab.

### The comparison that clarifies it

| Source | Oversight regime | What consent covers |
|---|---|---|
| Human surgical tissue (H01) | Institutional review of human-subjects research; tissue is discarded surgical material | Research use of the specimen; whether "research use" was understood to include indefinite open redistribution and downstream machine-learning use is the live question, not a settled one |
| Vertebrate animal tissue (MICrONS, MouseConnects) | Institutional animal care and use committee approval | Protocol-level: species, numbers, procedures, endpoints |
| Invertebrate tissue (FlyWire, hemibrain) | No animal-welfare committee requirement in the United States for *Drosophila* | Not applicable |

The asymmetry is the point. The dataset with the fewest formal gates —
*Drosophila* — is the one the field proofreads most openly and credits most
carefully. The dataset with the most gates is the one whose ethics statement is
hardest to find.

---

## 2. De-identification: what an EM volume can and cannot reveal

Structural MRI has a well-known re-identification route: a head volume can be
rendered as a face, which is why defacing is a standard preprocessing
requirement. **Nanoscale EM has no equivalent route.** A 1 mm³ block of cortex
imaged at 4 nm contains no face, no skull shape, no name, no date, and none of
the direct identifiers a health-privacy framework enumerates. The image data
carries no genotype: what is released is heavy-metal-stained, resin-embedded
tissue rendered as grayscale voxels.

The residual risk is therefore **contextual, not pictorial**, and it lives in
the metadata rather than the images:

- **Population size.** "A 45-year-old woman who had an anterior temporal
  resection for drug-resistant epilepsy, at a named centre, in a narrow window
  of years" is a small set of people. The identifying power is in the
  description, not the voxels.
- **Linkage.** Dates, site, and clinical detail combine with other records in
  ways no single field does alone.
- **Pathology.** Features in the tissue reflect the donor's condition, and the
  condition is part of why the tissue exists.

Two consequences for practice. First, **de-identification work in EM
connectomics is metadata discipline, not image modification** — there is nothing
to blur. Second, the standard reference on responsible reuse of open human
connectomics data (Betzel & Bhatt, 2021) was written about neuroimaging-scale
datasets, and its treatment of privacy, consent, analytic flexibility and
transparent reporting transfers only partly to nanoscale EM. The reporting and
analytic-flexibility guidance transfers cleanly. The privacy guidance was
designed for a modality with a face in it.

Governance is moving toward the general category rather than the modality. On
12 November 2025 UNESCO's General Conference adopted the **Recommendation on the
Ethics of Neurotechnology**, the first global standard in the area; it
establishes a framework for "neural data", holds that such data is uniquely
sensitive and requires strict safeguards against misuse, and is
non-binding on member states. Whether a volume EM dataset falls inside that
definition of neural data is not settled, and this page does not claim it does.

---

## 3. Licences: what a reuser is actually obliged to do

This is the section people skip and then get wrong. The three flagship datasets
are released under three different regimes, and in at least one case the paper
and the data carry **different licences**.

| Resource | Licence | What you must do | Commercial use |
|---|---|---|---|
| MICrONS (microns-explorer.org) | Creative Commons Attribution 4.0 International | Retain creator identification and copyright notice, indicate modifications, and include the licence text or a link to it; impose no further restrictions downstream. Follow the site's citation policy — the named publication is MICrONS Consortium et al. (2025), *Nature* 640: 435–47 | **Permitted** |
| FlyWire public release (v783, an October 2023 snapshot) | Creative Commons Attribution-**NonCommercial** 4.0 | Attribute, and cite the papers named in FlyWire's citation guide. Pre-publication data carries separate community-principles obligations | **Not permitted** |
| FlyWire's flagship *paper* (Dorkenwald et al., 2024, *Nature*) | Creative Commons Attribution 4.0 | Attribute | Permitted |
| Hemibrain / neuPrint | Creative Commons Attribution (version not confirmed from the primary source — check before redistributing) | Attribute; cite Scheffer et al. (2020) | Presumed permitted, unverified |
| H01 | No licence statement was found on the release landing page; the *Science* article is under the AAAS journal licence, © the authors. Data availability points at the public Google Cloud bucket, open with no registration | Cite Shapson-Coe et al. (2024) and check terms before redistributing | Unclear — verify |

**The FlyWire row is the one that catches people.** Reusing a figure from the
Nature paper and reusing the connectome are governed by different instruments:
the article is CC BY, the data is CC BY-NC. A commercial product built on
FlyWire connectivity is a licence problem; a commercial product built on MICrONS
connectivity is not.

Two more layers sit above the per-dataset licence.

**Funder obligations bind the producer, not the reuser.** The NIH Data
Management and Sharing Policy (NOT-OD-21-013) took effect on 25 January 2023 and
requires every NIH application that will generate scientific data to include a
data management and sharing plan, and to comply with it. That is why
CONNECTS-scale projects release data at all — but it grants a reuser nothing
beyond what the dataset's own licence grants.

**Repository policies span a spectrum.** Jwa & Poldrack (2022) surveyed data
sharing policies across neuroimaging repositories and found that the level of
access control and the restrictions placed on secondary use vary widely, from
fully open repositories where data may be downloaded and reanalysed without
constraint, through to controlled access requiring verified credentials and
limiting what secondary analyses are permitted. The practical lesson is that
"the data is public" is not a licence statement.

### A decision table

| You want to… | Check |
|---|---|
| Put a published figure in your paper or slides | The **article** licence, not the data licence |
| Redistribute a derived table (e.g. an edge list) | The **data** licence plus its attribution requirements |
| Train a model on the imagery | The data licence; a NonCommercial clause reaches the model if the model is commercial |
| Build a product or a paid service | Whether any NC clause applies — FlyWire yes, MICrONS no |
| Publish a reanalysis | The portal's citation policy: cite the papers it names, not only the URL |
| Quote a number in a lecture | Nothing — but pin the release version, per [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }}) |

---

## 4. Dual use, honestly

Connectomics has none of the hazards the classic dual-use frameworks were built
for: there is no pathogen, no agent, no enhancement of transmissibility. Saying
otherwise inflates the field's risk profile and wastes the reader's attention.
Three concerns are real, and only one of them is currently governed.

**Governed: neural-data misuse.** The UNESCO Recommendation (§2) situates
neurotechnology within a human-rights framework — dignity, freedom of thought,
mental privacy, autonomy — and calls on states to prevent applications that
facilitate coercive control, unlawful surveillance, or manipulation. It is not
binding, and it primarily targets devices that read or write brain activity in
living people, not post-mortem or surgical structural datasets.

**Arguable, undocumented: method transfer.** The segmentation, tracking and
instance-association methods developed for connectomics are general computer
vision, and general computer vision has surveillance applications. This is an
argument from capability, not from any documented case; it is recorded here as
an argument and not as a finding.

**Actual, and the one a student is likely to commit: over-claiming from a single
sample.** "H01 shows that the human brain does X" is a sentence about tissue
from one person with epilepsy (§1). Extended into difference or disease
narratives, a claim of that shape is a scientific integrity failure with social
consequences well outside the lab. The mitigation is not a policy: it is
writing the sample description into the claim, every time, and the
[review practice in Module 19]({{ '/modules/module19/' | relative_url }}) is
where that gets drilled.

---

## 5. Credit for proofreading labour

### The scale

Dorkenwald et al. (2024) estimate that FlyWire's brain reconstruction took
**around 33 person-years of manual proofreading**, distributed across consortium
labs, centralised teams at Princeton and Cambridge, and citizen scientists
worldwide; community members shared **133,700 annotations**. The product was
139,255 proofread neurons and 54.5 million synapses.

That is the only published effort figure of its kind this page could source.
MICrONS and H01 do not publish an equivalent person-year number. **The absence
is itself a finding**: the largest single labour input to a connectome is
routinely unquantified in the paper that reports the connectome.

### Four credit models actually in use

| Model | Example | What a contributor can put on a CV | Failure mode |
|---|---|---|---|
| **Consortium co-authorship** | "The FlyWire Consortium" as a co-author of Dorkenwald et al. (2024) | Membership of a named group; the individual is not indexed by name in bibliographic databases | Hard to claim in a job application or a tenure case; invisible to citation metrics |
| **Collective acknowledgement in the author line** | Kim et al. (2014), *Nature* — the author list ends "and the EyeWirers", with the individual EyeWirers who reconstructed the cells listed in supplementary information | A verifiable named appearance, but in supplementary material | Not authorship; disappears from every automated record |
| **Per-contribution platform attribution** | FlyWire Codex shows per-cell credits and a labelling leaderboard | A durable, checkable link to specific work | Not a publication; depends on the platform continuing to exist |
| **Named individual authorship with a contributions statement** | Shapson-Coe et al. (2024) names individuals for "proofreading of neurons", "production of ground truth for synapse prediction and excitatory versus inhibitory classification", and each other task | Full authorship plus a specific, quotable role | Only workable when the contributor count is small |

### What to do about it

Three things this page can state without hedging.

1. **CRediT has no term for proofreading.** The nearest contributor-role terms
   are Data curation and Investigation, and neither describes segment-level
   error correction. If your project uses CRediT, write down which term you are
   mapping proofreading onto, before results exist.
2. **The threshold has to be written before the work.** "How much proofreading
   earns authorship?" answered after a paper is drafted is answered under
   pressure. The four models above are the menu; pick one and publish the rule.
3. **Effort is measurable, so measure it.** FlyWire's 33 person-years exists
   because someone counted. Edit histories in CAVE-backed datasets make
   per-contributor effort computable. A project that does not report it has
   chosen not to.

---

## Self-check

1. You want to build a paid teaching product around a connectome. Which of
   MICrONS and FlyWire can you use, and why?
2. Why is "we removed the patient's name" not the whole of de-identification for
   H01 — and what *is* the residual risk?
3. A colleague says an undergraduate who proofread 800 segments should be
   "acknowledged, not an author". Which credit model is that, and what does the
   contributor lose?

**Answers.**

1. MICrONS: it is CC BY 4.0, which permits commercial use provided you
   attribute, mark modifications and pass the licence on. FlyWire's data release
   is CC BY-NC 4.0, so a paid product is outside the licence — even though
   FlyWire's *Nature* paper is CC BY and its figures are reusable.
2. Because the volume never contained a name, or a face, or any direct
   identifier — there is nothing in the image to remove. The residual risk is
   contextual: the clinical description (age, sex, procedure, site, approximate
   date) picks out a small population, and it lives in metadata and prose, not
   in voxels.
3. Collective acknowledgement — the Eyewire model. The contributor loses
   authorship, indexing under their own name in bibliographic databases, and
   any citation credit; they gain a named appearance that most automated records
   will never see. That may be the right call; it should be the *stated* call,
   made before the work, not after.

---

## What this page does not cover

- **Legal advice, and jurisdiction-specific law.** GDPR special-category data,
  US state genetic-privacy statutes and national neurorights legislation are
  real and consequential; none is analysed here, and nothing on this page is a
  substitute for your institution's research-compliance office.
- **Publication ethics in general.** COPE Core Practices and the ICMJE
  authorship criteria are the operative documents and are applied in
  [Module 19]({{ '/modules/module19/' | relative_url }}).
- **Animal welfare procedure.** IACUC protocol design, the 3Rs, and species
  scope are named in §1 and not developed.
- **Licence details that could not be confirmed from a primary source.** The
  hemibrain/neuPrint CC BY *version* and the H01 *data* licence are marked as
  unverified in the table rather than guessed. Confirm both before
  redistributing either dataset.
- **Repository-by-repository policy counts.** Jwa & Poldrack's survey is cited
  for its spectrum finding, not for per-repository figures, which were not
  recovered from the primary source.
- **Consent for future AI training uses.** Whether broad consent to "research
  use" of surgical tissue extends to training foundation models on the resulting
  images is an open question. No settled answer exists to report, and inventing
  one would be worse than saying so.
- **Community conduct and inclusion.** Codes of conduct, harassment policy and
  mentoring obligations are ethics too, and belong to the
  [hidden curriculum]({{ '/hidden-curriculum/' | relative_url }}) rather than here.

---

## Go deeper

- [Module 19: peer review and scientific ethics]({{ '/modules/module19/' | relative_url }})
  — where these facts become decisions, with a review-board simulation.
- [H01 human cortex]({{ '/content-library/case-studies/h01-human-cortex/' | relative_url }})
  — the dataset behind §1, including its pathology caveats.
- [FlyWire whole-brain connectome]({{ '/content-library/case-studies/flywire-whole-brain/' | relative_url }})
  — the community whose labour §5 counts.
- [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }})
  — pinning the release version you actually used, which is the reproducibility
  half of governance.
- [Synapse detection]({{ '/content-library/infrastructure/synapse-detection/' | relative_url }})
  — why "the data says 74% excitatory" is a claim about a detector, and an
  example of the bounded-claim discipline §4 asks for.
- [Datasets]({{ '/datasets/' | relative_url }}) — access routes and per-dataset
  terms.

---

## References

- Betzel, R. F., & Bhatt, D. H. (2021). Large, open datasets for human
  connectomics research: considerations for reproducible and responsible data
  use. *NeuroImage*.
  [10.1016/j.neuroimage.2021.118579](https://doi.org/10.1016/j.neuroimage.2021.118579)
- Dorkenwald, S., Matsliah, A., Sterling, A. R., Schlegel, P., et al., and the
  FlyWire Consortium (2024). Neuronal wiring diagram of an adult brain.
  *Nature*, 634, 124–138.
  [10.1038/s41586-024-07558-y](https://doi.org/10.1038/s41586-024-07558-y)
- FlyWire citation and credit guidelines.
  [flywire.ai/guidelines](https://flywire.ai/guidelines)
- Jwa, A. S., & Poldrack, R. A. (2022). The spectrum of data sharing policies in
  neuroimaging data repositories. *Human Brain Mapping*, 43(8), 2707–2721.
  [10.1002/hbm.25803](https://doi.org/10.1002/hbm.25803)
- Kim, J. S., Greene, M. J., Zlateski, A., Lee, K., et al., and the EyeWirers
  (2014). Space–time wiring specificity supports direction selectivity in the
  retina. *Nature*, 509, 331–336.
  [10.1038/nature13240](https://doi.org/10.1038/nature13240)
- MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple
  areas of mouse visual cortex. *Nature*, 640, 435–447.
  [10.1038/s41586-025-08790-w](https://doi.org/10.1038/s41586-025-08790-w)
  Terms and conditions at
  [microns-explorer.org/terms-and-conditions](https://www.microns-explorer.org/terms-and-conditions).
- NIH (2020). Final NIH policy for data management and sharing, NOT-OD-21-013;
  effective 25 January 2023.
  [grants.nih.gov](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-21-013.html)
- Scheffer, L. K., et al. (2020). A connectome and analysis of the adult
  *Drosophila* central brain. *eLife*, 9, e57443.
  [10.7554/eLife.57443](https://doi.org/10.7554/eLife.57443)
- Shapson-Coe, A., Januszewski, M., Berger, D. R., et al. (2024). A petavoxel
  fragment of human cerebral cortex reconstructed at nanoscale resolution.
  *Science*, 384, eadk4858.
  [10.1126/science.adk4858](https://doi.org/10.1126/science.adk4858)
- UNESCO (2025). Recommendation on the ethics of neurotechnology. Adopted by the
  General Conference, 12 November 2025.
  [unesco.org](https://www.unesco.org/en/legal-affairs/recommendation-ethics-neurotechnology)
