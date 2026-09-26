---
marp: true
theme: frontiers
paginate: true
title: "Connectomics Ethics and Governance"
description: "A NeuroTrailblazers graduate lecture. What is live now in connectomics ethics (licence compliance, credit for proofreading labour) and what is prospective (consent at scale, de-identification, neural-data regulation, dual use), stated at its real strength."
---
<!-- _class: cover nanoscale -->
<!-- _paginate: false -->

<img class="cover-image" src="../../../../assets/images/content-library/case-studies/h01/10b-segmentation-overlay.jpg" alt="H01 electron microscopy with object segmentation and original 2 µm scale bar">

# Connectomics Ethics and Governance

### A graduate lecture from the NeuroTrailblazers reference layer

**NeuroTrailblazers** · neurotrailblazers.org

<p class="roadmap">Part A — Human tissue: consent and de-identification<br>Part B — Licences: what a reuser must do<br>Part C — Dual use and credit for proofreading</p>

<p class="cover-label">Human cortex · H01<br>Object segmentation over electron microscopy</p>

<p class="src">H01 release · Lichtman Lab / Harvard &amp; Connectomics at Google<br>Image: CC BY 4.0 · Shapson-Coe et al. (2024) · doi:10.1126/science.adk4858<br>Lecture: CC BY-SA 4.0 · neurotrailblazers.org</p>

<!--
This lecture is built from one page of the NeuroTrailblazers content library,
"Ethics and Governance", and every fact on these slides comes from that page and the
documents it cites. It holds facts, not decisions: practising the judgement -- how to
review a manuscript, write an authorship policy, raise a concern -- belongs to the
site's peer-review and scientific-ethics module, not to this hour.

Set expectations early: this is not a lecture about a scandal. There isn't one.
-->

---

<!-- _class: claim -->

## Start with the honest assessment:

## connectomics does not currently have a human-subjects problem.

Its flagship human dataset is discarded surgical tissue that was going to be removed regardless, subject to the same frameworks that govern any human-tissue study. Nothing in this field asks a person to undergo a procedure for research, and nothing published so far identifies anyone.

<p class="ask">If you came expecting a controversy, there isn't one to report. So what is this hour for?</p>

---

## What is live now, and what is prospective

<div class="cols">
<div>

**Live now — practical, not philosophical**

**Licence obligations** (Part B). Major portals redistribute under different terms, and a reuser who ignores them is simply in breach.

**Credit for proofreading labour** (Part C). Tens of thousands of hours of human correction sit behind a whole-brain connectome such as FlyWire, and how that work is credited decides real careers. **The one topic here about people affected today.**

</div>
<div>

**Prospective — worth discussing because it is not yet urgent**

- Consent framings written for a cubic millimetre of discarded tissue, not for whole-brain human volumes or machine-learning corpora
- De-identification: a non-issue at today's volumes, an open question at tomorrow's
- Neural-data regulation: UNESCO adopted the first global standard in November 2025
- Dual use: weak for a field with no pathogens, and should be stated at its real strength

</div>
</div>

<div class="box box--good">

**Treat the prospective material as a seminar, not a compliance checklist.** The right time to reason about it is before a project needs the answer.

</div>

---

## Learning objectives

### By the end of this lecture you will be able to:

**1** — **Locate** the provenance and ethics statement of a human-tissue connectomics dataset before citing it.

**2** — **Explain** where the residual re-identification risk in a nanoscale EM volume actually lives.

**3** — **Determine** what a dataset's licence obliges a reuser to do, and whether a planned use is permitted.

**4** — **Distinguish** governed, arguable and actual dual-use concerns, at their real strength.

**5** — **Compare** credit models for proofreading labour, and state what each costs the contributor.

<div class="box">

Objective 3 is the material people skip and then get wrong. In at least one flagship case, the paper and the data carry different licences.

</div>

---

## Roadmap

<div class="cols">
<div>

**Part A — Human tissue** *(prospective)* Where H01 came from; what its paper does and does not say; oversight regimes compared; what an EM volume can and cannot reveal; the UNESCO Recommendation.

**Part B — Licences** *(live now)* Five resources, five licence positions; the FlyWire row; funder and repository layers; a decision table.

</div>
<div>

**Part C — Dual use and credit** *(one prospective, one live)* Three dual-use concerns at their real strength; the scale of proofreading labour; four credit models in use; what to do about it.

<div class="box box--good">

**Bring to each part:** a connectomics dataset you have used or plan to use. By the end you should know where its ethics statement is, what its licence lets you do, and how its proofreaders were credited.

</div>

</div>
</div>

---

<!-- _class: part -->

# Part A

### Human tissue: consent and de-identification

- Where H01 came from, and what its paper says
- Three oversight regimes, compared
- What an EM volume can and cannot reveal

<div class="meta">Slides 6–14</div>

---

## Where H01 came from

### The site's human reference volume has a specific and documentable provenance

Shapson-Coe et al. (2024) describe the sample as a "rapidly preserved, 170-µm-thick slab of human cortex from the anterior part of the middle temporal gyrus of a 45-year-old female", of "just over 1 mm³", which "was removed to gain access to an epileptic focus in the underlying hippocampus".

| Step | Figure |
|---|---|
| Sections | 5,019, mean thickness 33.9 nm |
| Imaging | Multibeam SEM at 4 × 4 nm |
| Dataset | About 1.4 petabytes |
| Content | Roughly 57,000 cells and 150 million synapses |

<p class="src">Shapson-Coe et al. 2024, <em>Science</em> 384, eadk4858 (10.1126/science.adk4858).</p>

---

## A surgical by-product

### The strongest position human connectomics can currently occupy

<div class="cols">
<div>

In the authors' framing, human specimens become available "from neurosurgical interventions for neurological conditions in which pieces of the cortex are discarded because they obstruct access to a pathological site".

**No tissue was removed for research that would not otherwise have been removed.**

</div>
<div>

<div class="box box--good">

**That is why H01 — rather than any purpose-collected human sample — is the field's reference volume.**

The ethical structure follows directly from the provenance description on the previous slide.

</div>

</div>
</div>

---

## What the paper does and does not say

<div class="cols">
<div>

**The main article carries no consent or IRB statement.**

A full-text search of the published *Science* article for "consent", "IRB", "ethics" and "Institutional Review" returns nothing. The data-availability statement points at the release landing page, and the licence line covers the article, not the data.

**Look for consent and approval details in the supplementary Materials and Methods.**

</div>
<div>

<div class="box box--warn">

**The practice to adopt.**

When you reuse human tissue data, **find the ethics statement before you cite the dataset, and say where you found it.**

A citation to a landing page is not a citation to an ethics review.

</div>

</div>
</div>

<!--
Be precise about what this slide claims. It does not say H01 lacks ethics approval.
It says the main article does not carry an ethics statement (checked against the
published text; the bioRxiv preprint's Methods also have none). Where approval is
documented -- presumably the supplementary methods -- has not been confirmed for this
deck, which is the point: check before citing. A reader who stops at the article or
the landing page has not seen any approval details. The failure it warns against is
citing without looking.
-->

---

## The paper is explicit about the sample's pathology

Human surgical samples "originate in individuals with pathologies of the nervous system such as epilepsy, tumors, or neurodegenerative diseases". In this case, "we cannot exclude the possibility that long-term epilepsy, or its pharmacological treatment, had subtle effects on the nanometer-scale structure of the tissue".

<div class="box box--warn">

**This is simultaneously a scientific caveat and an ethical one.**

Every claim of the form *"the human brain does X, as shown by H01"* is really a claim about **tissue from one adult woman with drug-resistant epilepsy**.

</div>

Part C returns to why that matters beyond the lab.

---

## Three oversight regimes, compared

<!-- _class: dense -->

| Source | Oversight regime | What consent covers |
|---|---|---|
| **Human surgical tissue** (H01) | Institutional review of human-subjects research; tissue is discarded surgical material | Research use of the specimen. Whether "research use" was understood to include **indefinite open redistribution and downstream machine-learning use** is the live question, not a settled one |
| **Vertebrate animal tissue** (MICrONS, MouseConnects) | Institutional animal care and use committee approval | Protocol-level: species, numbers, procedures, endpoints |
| **Invertebrate tissue** (FlyWire, hemibrain) | No federal animal-welfare committee requirement in the United States for *Drosophila* | Not applicable |

<div class="box box--good">

**The asymmetry is the point.** The dataset with the fewest formal gates — *Drosophila* — is the one the field proofreads most openly and credits most carefully. The dataset with the most gates is the one whose ethics statement is hardest to find.

</div>

---

## De-identification: what an EM volume can and cannot reveal

<div class="cols">
<div>

**Structural MRI has a well-known re-identification route.** A head volume can be rendered as a face, which is why defacing is a standard preprocessing requirement.

**Nanoscale EM has no equivalent route.** A 1 mm³ block of cortex imaged at 4 nm contains no face, no skull shape, no name, no date, and none of the direct identifiers a health-privacy framework enumerates.

The image data carries no genotype: what is released is heavy-metal-stained, resin-embedded tissue rendered as grayscale voxels.

</div>
<div>

**The residual risk is contextual, not pictorial** — and it lives in the metadata, not the images:

- **Population size.** "A 45-year-old woman who had an anterior temporal resection for drug-resistant epilepsy, at a named centre, in a narrow window of years" is a small set of people.
- **Linkage.** Dates, site and clinical detail combine with other records in ways no single field does alone.
- **Pathology.** Features in the tissue reflect the donor's condition, and the condition is part of why the tissue exists.

</div>
</div>

---

## Two consequences for practice, and where governance is moving

<div class="cols">
<div>

**1 — De-identification in EM connectomics is metadata discipline, not image modification.** There is nothing to blur.

**2 — The standard reference transfers only partly.** Laird (2021) on responsible reuse of open human connectomics data was written about neuroimaging-scale datasets. Its reproducibility guidance transfers cleanly. **It was written for MRI, a modality with a face in it.**

</div>
<div>

**UNESCO Recommendation on the Ethics of Neurotechnology** — adopted by the General Conference on **11 November 2025**, the first global standard in the area.

- establishes a framework for "neural data"
- holds that such data is uniquely sensitive and requires strict safeguards against misuse
- is **non-binding** on member states

<div class="box box--warn">

**Whether a volume EM dataset falls inside that definition of neural data is not settled**, and this lecture does not claim it does.

</div>

</div>
</div>

<!--
Dates, from the official text (unesco.org/en/legal-affairs/recommendation-ethics-neurotechnology):
the General Conference "Adopts the present Recommendation ... on this eleventh day of
November 2025" in Samarkand; UNESCO's press release gives entry into force as 12 November,
at the close of the session. Why the question is open: the text defines neural data as data
"about the structure, activity and function of the nervous system gathered through
neurotechnology" -- structure is named, but so is the neurotechnology route.
-->

---

## Check yourself

### Why is "we removed the patient's name" not the whole of de-identification for H01 — and what *is* the residual risk?

<div class="cols">
<div>

**Because the volume never contained a name** — or a face, or any direct identifier. There is nothing in the image to remove.

</div>
<div>

**The residual risk is contextual.** The clinical description — age, sex, procedure, site, approximate date — picks out a small population, and it lives in **metadata and prose, not in voxels**.

</div>
</div>

<p class="ask">Follow-up: which details of H01's provenance description — age, sex, procedure, site — would you leave out of a public dataset record, and what would a reuser lose if you did?</p>

<!--
There is no single right answer to the follow-up, and that is intentional -- this is
the seminar half of the lecture. The tension to surface: the same clinical detail that
narrows the population is the detail a scientist needs to interpret the tissue (the
pathology caveat two slides back).
-->

---

<!-- _class: part -->

# Part B

### Licences: what a reuser is actually obliged to do

- Five resources, five licence positions
- The row that catches people
- Funder and repository layers, and a decision table

<div class="meta">Slides 15–20</div>

---

## The section people skip and then get wrong

<!-- _class: dense tight -->

| Resource | Licence | What you must do | Commercial use |
|---|---|---|---|
| **MICrONS** (microns-explorer.org) | Creative Commons Attribution 4.0 International | Retain creator identification and copyright notice, indicate modifications, include the licence text or a link; impose no further restrictions downstream. Follow the site's citation policy — MICrONS Consortium et al. (2025), *Nature* 640: 435–47 | **Permitted** |
| **FlyWire public release** (v783, an October 2023 snapshot) | Creative Commons Attribution-**NonCommercial** 4.0 | Attribute, and cite the papers named in FlyWire's citation guide. Pre-publication data carries separate community-principles obligations | **Not permitted** |
| **FlyWire's flagship *paper*** (Dorkenwald et al., 2024, *Nature*) | Creative Commons Attribution 4.0 | Attribute | Permitted |
| **Hemibrain / neuPrint** | CC BY 4.0 per Janelia's hemibrain page; the v1.0 figshare deposit is tagged CC BY-NC 4.0 — **check before redistributing** | Attribute; cite Scheffer et al. (2020) | Permitted per project page; **v1.0 deposit conflicts** |
| **H01** | CC BY 4.0, stated on the release's data page (not its landing page); the *Science* article is under the AAAS journal licence, © the authors. Data sit in a public Google Cloud bucket, open with no registration | Attribute; cite Shapson-Coe et al. (2024) | **Permitted** |

<p class="src">In at least one case the paper and the data carry different licences. The hemibrain row is flagged as conflicting rather than resolved by guesswork.</p>

<!--
Do not tidy the hemibrain row up. Janelia's hemibrain project page links CC BY 4.0
(janelia.org/project-team/flyem/hemibrain), but the v1.0 data deposit the eLife paper
cites (doi:10.25378/janelia.11676099) is registered as CC BY-NC 4.0 in its DataCite
metadata. A reuser must resolve that before redistributing. Presenting a guess as a
licence is worse than presenting the gap.

H01: the release data page (h01-release.storage.googleapis.com/data.html) states "All
released datasets are licensed under a Creative Commons Attribution 4.0 License"; the
landing page itself carries no licence line, which is why it is easy to miss.
-->

---

## The FlyWire row is the one that catches people

<div class="cols">
<div>

**Reusing a figure from the *Nature* paper** and **reusing the connectome** are governed by different instruments.

| | Licence |
|---|---|
| The article | CC BY 4.0 |
| The data release | CC BY-**NC** 4.0 |

</div>
<div>

<div class="box box--warn">

**A commercial product built on FlyWire connectivity is a licence problem.**

**A commercial product built on MICrONS connectivity is not.**

</div>

</div>
</div>

<p class="ask">Your lab spins out a company that sells a connectome-constrained model trained on FlyWire. Which licence governs, and what does it say?</p>

<!--
Answer: the data licence, CC BY-NC 4.0. The paper being CC BY does not help; the
product is built on FlyWire connectivity, not on the article. The decision table two
slides on has the rows for this: "build a product or a paid service" (FlyWire's NC
clause applies) and "train a model" (an NC clause reaches the model if the model is
commercial).
-->

---

## Two more layers above the per-dataset licence

<div class="cols">
<div>

**Funder obligations bind the producer, not the reuser.**

The **NIH Data Management and Sharing Policy** (NOT-OD-21-013) took effect on **25 January 2023**. Every NIH application that will generate scientific data must include a data management and sharing plan, and comply with it.

That is one reason CONNECTS-scale projects release data at all — **but it grants a reuser nothing beyond what the dataset's own licence grants.**

</div>
<div>

**Repository policies span a spectrum.**

Jwa & Poldrack (2022) surveyed data-sharing policies across neuroimaging repositories. Access control and restrictions on secondary use **vary widely** — from fully open, download-and-reanalyse without constraint, to controlled access requiring verified credentials and limiting permitted secondary analyses.

<div class="box box--good">

**The practical lesson: "the data is public" is not a licence statement.**

</div>

</div>
</div>

<!--
Jwa & Poldrack is cited here for its spectrum finding only. Per-repository policy
counts were not recovered from the primary source, so none are quoted.
-->

---

## A decision table

### What to check, by what you want to do

| You want to… | Check |
|---|---|
| Put a published figure in your paper or slides | The **article** licence, not the data licence |
| Redistribute a derived table (e.g. an edge list) | The **data** licence plus its attribution requirements |
| Train a model on the imagery | The data licence; a NonCommercial clause reaches the model if the model is commercial |
| Build a product or a paid service | Whether any NC clause applies — FlyWire yes, MICrONS no |
| Publish a reanalysis | The portal's citation policy: cite the papers it names, not only the URL |
| Quote a number in a lecture | Nothing — but pin the release version you used |

<div class="box">

**Note the last row.** Licensing is not the only obligation that travels with a number. Pinning the release version is the reproducibility half of governance.

</div>

---

## Check yourself

### You want to build a paid teaching product around a connectome. Which of MICrONS and FlyWire can you use, and why?

<div class="cols">
<div>

**MICrONS — yes.** It is CC BY 4.0, which permits commercial use provided you attribute, mark modifications, and link the licence.

</div>
<div>

**FlyWire's data — no.** The data release is CC BY-NC 4.0, so a paid product is outside the licence — **even though FlyWire's *Nature* paper is CC BY and its figures are reusable.**

</div>
</div>

<div class="box box--warn">

**And H01 or hemibrain?** H01's data page states CC BY 4.0, so yes, with attribution. Hemibrain's project page says CC BY 4.0 but its v1.0 deposit says CC BY-NC 4.0: "verify before redistributing".

</div>

---

<!-- _class: part -->

# Part C

### Dual use and credit for proofreading

- Three concerns, at their real strength
- The scale of proofreading labour
- Four credit models, and what to do about it

<div class="meta">Slides 21–27</div>

---

## Dual use, honestly

### Connectomics has none of the hazards the classic dual-use frameworks were built for

There is no pathogen, no agent, no enhancement of transmissibility. Saying otherwise inflates the field's risk profile and wastes the reader's attention. **Three concerns are real, and only one of them is currently governed.**

<!-- _class: tight -->

| Status | Concern | At its real strength |
|---|---|---|
| **Governed** | **Neural-data misuse** | The UNESCO Recommendation situates neurotechnology within a human-rights framework — dignity, freedom of thought, mental privacy, autonomy — and warns against coercion, unlawful surveillance and manipulation. **Not binding**, and it is framed around devices that measure or modulate the nervous system, not archived surgical EM datasets |
| **Arguable, undocumented** | **Method transfer** | Segmentation, tracking and instance-association methods developed for connectomics are general computer vision, which has surveillance applications. **An argument from capability, not from any documented case** — recorded as an argument, not a finding |
| **Actual** | **Over-claiming from a single sample** | The one a student is likely to commit. Next slide |

---

## The actual one: over-claiming from a single sample

<div class="cols">
<div>

*"H01 shows that the human brain does X"* is a sentence about **tissue from one person with epilepsy** (Part A).

Extended into difference or disease narratives, a claim of that shape is a **scientific integrity failure with social consequences well outside the lab**.

</div>
<div>

<div class="box box--good">

**The mitigation is not a policy.**

It is writing the sample description into the claim, **every time**.

</div>

**Weak:** *"The human cortex shows X."*

**Defensible:** *"In ~1 mm³ of middle temporal gyrus resected from one patient with drug-resistant epilepsy, we observe X."*

</div>
</div>

<!--
The defensible phrasing uses only facts from the provenance slide in Part A. Point out
that it is longer and less exciting, and that it is also the only version of the
sentence that is true as written.

If the room has seen the synapse-detection lecture, connect it: "the data says 74%
excitatory" is a claim about a detector, and needs the same bounded-claim discipline.
(74% is the raw classifier output, 111.3 M of 149.9 M detected synapses; the paper's own
error-corrected estimate is 67.1% -- Shapson-Coe et al. 2024, synapse section.)
-->

---

## Credit for proofreading labour: the scale

<div class="cols">
<div>

Dorkenwald et al. (2024) estimate that FlyWire's brain reconstruction took **around 33 person-years of manual proofreading**, distributed across consortium labs, centralised teams at Princeton and Cambridge, and citizen scientists worldwide.

| | |
|---|---:|
| Community annotations shared | **133,700** |
| Proofread neurons | **139,255** |
| Synapses | **54.5 million** |

</div>
<div>

<div class="box box--warn">

**Published effort figures are rare: FlyWire's, and the hemibrain's "over 50 person-years".** MICrONS and H01 do not publish an equivalent person-year number.

**The absence is itself a finding:** the largest single labour input to a connectome is routinely unquantified in the paper that reports the connectome.

</div>

</div>
</div>

<p class="src">Dorkenwald et al. 2024, <em>Nature</em> 634, 124–138 (10.1038/s41586-024-07558-y). Scheffer et al. 2020, <em>eLife</em> 9, e57443.</p>

---

## Four credit models actually in use

<!-- _class: dense -->

| Model | Example | What a contributor can put on a CV | Failure mode |
|---|---|---|---|
| **Consortium co-authorship** | "The FlyWire Consortium" as a co-author of Dorkenwald et al. (2024) | Membership of a named group; PubMed lists members as collaborators, not authors | Hard to claim in a job application or a tenure case; largely invisible to citation metrics |
| **Collective acknowledgement in the author line** | Kim et al. (2014), *Nature* — the author list ends "and the EyeWirers", with the individuals who reconstructed the cells listed in supplementary information | A verifiable named appearance, but in supplementary material | Not authorship; disappears from every automated record |
| **Per-contribution platform attribution** | FlyWire Codex shows per-cell credits and a labelling leaderboard | A durable, checkable link to specific work | Not a publication; depends on the platform continuing to exist |
| **Named individual authorship with a contributions statement** | Shapson-Coe et al. (2024) names individuals for "proofreading of neurons", "production of ground truth for synapse prediction and excitatory versus inhibitory classification", and each other task | Full authorship plus a specific, quotable role | Only workable when the contributor count is small |

<p class="ask">Every model has a failure mode. Which one would you choose for a project with 40 contributors, and what would you tell them before they started?</p>

---

## What to do about it

### Three things that can be stated without hedging

**1 — CRediT has no term for proofreading.** The nearest terms are *Data curation*, *Investigation* and *Validation* (where H01 filed it); none describes segment-level error correction. If your project uses CRediT, **write down which term you are mapping proofreading onto, before results exist.**

**2 — The threshold has to be written before the work.** "How much proofreading earns authorship?" answered after a paper is drafted is answered under pressure. The four models are the menu; **pick one and publish the rule.**

**3 — Effort is measurable, so measure it.** FlyWire's 33 person-years exists because someone counted. Edit histories in CAVE-backed datasets make per-contributor effort computable. **A project that does not report it has chosen not to.**

---

## Check yourself

### A colleague says an undergraduate who proofread 800 segments should be "acknowledged, not an author". Which credit model is that, and what does the contributor lose?

<div class="cols">
<div>

**The model:** collective acknowledgement — the EyeWire model.

**What the contributor loses:** authorship, indexing under their own name in bibliographic databases, and any citation credit.

**What they gain:** a named appearance that most automated records will never see.

</div>
<div>

<div class="box box--good">

**That may be the right call.**

It should be the **stated** call, made before the work — not after.

</div>

</div>
</div>

---

## What this lecture does not cover

### Boundaries stated deliberately, as the source page states them

<div class="cols">
<div>

- **Legal advice and jurisdiction-specific law.** GDPR special-category data, US state genetic-privacy statutes and national neurorights legislation are real and consequential; none is analysed here. **Nothing here substitutes for your institution's research-compliance office.**
- **Publication ethics in general.** COPE Core Practices and the ICMJE authorship criteria are the operative documents, applied in the site's peer-review and ethics module.
- **Animal welfare procedure.** IACUC protocol design, the 3Rs and species scope are named and not developed.

</div>
<div>

- **Unresolved licence conflicts.** Hemibrain's project page (CC BY 4.0) and its v1.0 data deposit (CC BY-NC 4.0) disagree; this lecture flags that rather than guessing. Confirm before redistributing.
- **Repository-by-repository policy counts.** Jwa & Poldrack is cited for its spectrum finding only.
- **Consent for future AI training uses.** Whether broad consent to "research use" of surgical tissue extends to training foundation models on the resulting images is open. **No settled answer exists, and inventing one would be worse than saying so.**
- **Community conduct and inclusion** — codes of conduct, harassment policy, mentoring obligations.

</div>
</div>

---

## Where to go next

<div class="cols">
<div>

**The source page.** *Ethics and Governance* in the NeuroTrailblazers content library — the facts in this lecture, with every document linked.

**Practising the judgement.** The site's peer-review and scientific-ethics module, with a review-board simulation — where these facts become decisions.

**Neighbouring pages.** The H01 case study (its pathology caveats); the FlyWire case study (the community whose labour Part C counts); Provenance and versioning (pinning the release you used); Synapse detection (a worked example of bounded claims); Datasets (access routes and per-dataset terms).

</div>
<div>

<div class="box box--good">

**The one idea to carry forward.**

The live obligations are unglamorous: **read the licence that actually governs, find the ethics statement before you cite, write the sample into the claim, and settle credit before the work.**

The prospective questions are real — and the time to reason about them is before a project needs the answer.

</div>

</div>
</div>

---

## References and sources

<!-- _class: refs -->

**Datasets and their papers.** Shapson-Coe et al. 2024 (10.1126/science.adk4858, H01); Dorkenwald et al. 2024, and the FlyWire Consortium (10.1038/s41586-024-07558-y, FlyWire); MICrONS Consortium et al. 2025 (10.1038/s41586-025-08790-w), with terms at microns-explorer.org/terms-and-conditions; H01 data terms at h01-release.storage.googleapis.com/data.html; Scheffer et al. 2020 (10.7554/eLife.57443, hemibrain; terms at janelia.org/project-team/flyem/hemibrain); Kim et al. 2014, and the EyeWirers (10.1038/nature13240).

**Governance and policy.** UNESCO (2025), Recommendation on the Ethics of Neurotechnology, adopted 11 November 2025 (unesco.org); NIH (2020), Final NIH Policy for Data Management and Sharing, NOT-OD-21-013, effective 25 January 2023 (grants.nih.gov); FlyWire citation and credit guidelines (flywire.ai/guidelines).

**Responsible reuse.** Laird 2021 (10.1016/j.neuroimage.2021.118579, open human connectomics datasets); Jwa & Poldrack 2022 (10.1002/hbm.25803, the spectrum of data-sharing policies).

**Source page.** NeuroTrailblazers content library, *Ethics and Governance* (/content-library/connectomics/ethics-and-governance/). <https://neurotrailblazers.org>

---

<!-- _class: refs -->

## Use, adapt, and credit

### These slides are openly licensed for community use

<div class="cols">
<div>

**Licence: CC BY-SA 4.0**
Creative Commons Attribution-ShareAlike 4.0 International.
<https://creativecommons.org/licenses/by-sa/4.0/>

**You may** teach from these slides anywhere, including commercially; copy and redistribute them in any medium; and **re-cut, shorten, translate, restyle, or merge them into your own material** — and distribute the result. No permission needed.

**Two conditions.** *Attribution* — credit the original, link the licence, and say if you changed anything. *ShareAlike* — distribute your adapted version under this same licence, so it stays as open as what it came from.

</div>
<div>

**How to credit**

NeuroTrailblazers (2026). *Connectomics Ethics and Governance* (graduate lecture, NeuroTrailblazers reference layer). CC BY-SA 4.0. neurotrailblazers.org/technical-training/slides/

For an adaptation, prefix with *"Adapted from"* and note what you changed.

**Editable source.** The Marp markdown is in the repository — the exported PowerPoint renders each slide as an image, so the markdown is the thing to edit. <https://github.com/wrgr/neurotrailblazers>

**Improved something?** The project would like to hear about it — open an issue.

</div>
</div>

<p class="src">Cover image: H01 release, Lichtman Lab / Harvard &amp; Connectomics at Google, CC BY 4.0. Shapson-Coe et al. (2024), doi:10.1126/science.adk4858. The image retains its own licence. Cited papers carry their own licences; citation is not reproduction.</p>
