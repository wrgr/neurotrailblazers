# Claim audit: Connectomics Ethics and Governance

- **Date:** 2026-09-26
- **Deck:** `course/decks/marp/lectures/ethics-and-governance.marp.md` (31 slides; cover = slide 1)
- **Scope:** every quantitative, historical, licence, policy and regulatory claim on slides and in speaker notes.

## Summary

| Verdict | Count |
|---|---:|
| VERIFIED | 39 |
| CORRECTED | 9 |
| QUALIFIED | 10 |
| HYPOTHETICAL | 2 |
| UNVERIFIED | 2 |

The main findings:

1. **Wrong author on the responsible-reuse reference.** DOI 10.1016/j.neuroimage.2021.118579 is by **Angela R. Laird (2021)**, not "Betzel & Bhatt". Crossref and PubMed (PMID 34536537) both list a single author, and PubMed has no paper co-authored by Betzel and Bhatt. The error also appears in the source content-library page and in `_data/expert_seed_papers/ethics-policy/betzel-2021-open-datasets.json`.
2. **UNESCO adoption date.** The official text says the Recommendation was adopted "on this eleventh day of November 2025". 12 November is the date it entered into force, at the close of the General Conference.
3. **H01 data licence is not unclear.** The release data page says "All released datasets are licensed under a Creative Commons Attribution 4.0 License". Only the landing page has no licence line.
4. **The hemibrain licence conflicts between sources.** Janelia's hemibrain project page links CC BY 4.0. The DataCite record for the v1.0 data deposit that the eLife paper cites (10.25378/janelia.11676099) says CC BY-NC 4.0.
5. **FlyWire's 33 person-years is not the only published effort figure.** Scheffer et al. 2020 report "over 50 person-years of proofreading effort" for the hemibrain. Dorkenwald et al. 2024 cite that figure themselves.
6. **FlyWire Consortium members are indexed by name in PubMed.** PMID 39358518 lists 247 named Investigators (shown as collaborators). The slide said individuals are not indexed by name.

## Claim table

| Slide # | Claim (short quote) | Verdict | Source (DOI/URL + where in source) | Change made |
|---|---|---|---|---|
| 1 | Cover image "CC BY 4.0 · Shapson-Coe et al. (2024)" | VERIFIED | h01-release.storage.googleapis.com/data.html, "License" section: "All released datasets are licensed under a Creative Commons Attribution 4.0 License" | None |
| 2 | "reviewed under the same frameworks that govern any human-tissue study" | QUALIFIED | The ethics review itself was not located (see slide 9) | "reviewed under" → "subject to" |
| 2 | "nothing published so far identifies anyone" | UNVERIFIED | A claim of absence. No search can prove it | None; owner decision |
| 3 | "Three major portals redistribute under incompatible terms" | CORRECTED | After the audit: MICrONS CC BY 4.0, H01 CC BY 4.0, FlyWire data CC BY-NC 4.0. These are different but not all incompatible, and it is not a set of three | → "Major portals redistribute under different terms" |
| 3 | "Tens of thousands of hours … behind every published connectome" | QUALIFIED | 33 person-years (Dorkenwald 2024) is tens of thousands of hours. MICrONS and H01 publish no effort figure, so "every" was unsupported | → "behind a whole-brain connectome such as FlyWire" |
| 3 | "UNESCO adopted the first global standard in November 2025" | VERIFIED | UNESCO press release "Ethics of neurotechnology: UNESCO adopts the first global standard…"; official text, 11 Nov 2025 | None |
| 4 | "In at least one flagship case, the paper and the data carry different licences" | VERIFIED | FlyWire: the paper is CC BY 4.0 (Nature Rights & permissions); the data is CC BY-NC 4.0 (flywire.ai/guidelines) | None |
| 5 | "Five resources, five licence positions" | QUALIFIED | The table has 5 rows (4 datasets plus 1 paper). After correction they hold 3 distinct positions: CC BY, CC BY-NC, and conflicting | None (roadmap wording); owner decision |
| 6, 15, 21 | Part metadata "Slides 6–14", "15–20", "21–27" | VERIFIED | Counted against the deck's `---` separators | None |
| 7 | 170-µm slab, anterior middle temporal gyrus, 45-year-old female, "just over 1 mm³", removed to reach epileptic focus | VERIFIED | Shapson-Coe et al. 2024, *Science* 384:eadk4858, doi:10.1126/science.adk4858. Results, first paragraph (VoR text via PMC11718559) | None |
| 7 | 5,019 sections, mean 33.9 nm | VERIFIED | Same paper, Results: "5019 sections with a mean thickness of 33.9 nm" | None |
| 7 | Multibeam SEM at 4 × 4 nm | VERIFIED | Same paper: "multibeam scanning EM at 4 × 4 nm² resolution" | None |
| 7 | About 1.4 PB | VERIFIED | Same paper: "yielding a dataset ~1.4 petabytes in size" | None |
| 7 | About 57,000 cells and 150 million synapses | VERIFIED | Same paper, structured abstract: "about 57,000 cells … about 150 million synapses" | None |
| 8 | Quote "from neurosurgical interventions … obstruct access to a pathological site" | VERIFIED | Same paper, Introduction (VoR wording matches) | None |
| 8 | "No tissue was removed for research that would not otherwise have been removed" | VERIFIED | Follows from "removed to gain access to an epileptic focus" | None |
| 9 | Main article has no "consent"/"IRB"/"ethics"/"Institutional Review" | VERIFIED | Full VoR text (PMC11718559) searched: 0 hits for each term | None |
| 9 | Data availability points at the landing page; the licence line covers the article | VERIFIED | Same paper: "Data and materials availability … h01release…/landing.html"; "License information: Copyright © 2024 the authors … exclusive licensee AAAS" | None |
| 9 | "The consent and approval details live in the supplementary Materials and Methods" | UNVERIFIED | The supplement is not accessible: science.org returns 403 and the PMC supplement download is bot-gated. The bioRxiv preprint (10.1101/2021.05.29.446289) Methods have no consent or IRB statement | Slide → "**Look for consent and approval details in the supplementary Materials and Methods.**" Speaker note rewritten to say the location is not confirmed |
| 10 | Quotes "originate in individuals with pathologies…" and "we cannot exclude … long-term epilepsy" | VERIFIED | Shapson-Coe 2024, Results, first paragraph (VoR wording is "individuals"; the accepted manuscript said "patients") | None |
| 10 | "one adult woman with drug-resistant epilepsy" | VERIFIED | Same paper, Methods: "resected as part of treatment for drug-resistant epilepsy" | None |
| 11 | Vertebrate tissue → IACUC approval | VERIFIED | PHS Policy §III: "Animal – Any live, vertebrate animal" (olaw.nih.gov/policies-laws/phs-policy.htm) | None |
| 11 | "No animal-welfare committee requirement in the United States for *Drosophila*" | QUALIFIED | PHS Policy covers vertebrates only. Institutions may set their own rules, so the claim holds only at the federal level | → "No federal animal-welfare committee requirement…" |
| 12 | Defacing of structural MRI is a standard requirement | VERIFIED | OpenNeuro requires facial features removed before upload (Markiewicz et al. 2021, eLife, doi:10.7554/eLife.71774) | None |
| 12 | 1 mm³ at 4 nm has no face or direct identifiers | VERIFIED | Consistent with the HIPAA Safe Harbor identifier list (45 CFR 164.514(b)(2)) and the paper's imaging parameters | None |
| 12 | Metadata risk: 45-year-old, anterior temporal resection, drug-resistant epilepsy, "a named centre" | VERIFIED | bioRxiv preprint Methods: "anonymized 45 year old patient with drug-resistant epilepsy who had a left hippocampal resection via the anterior temporal lobe at Massachusetts General Hospital" | None |
| 13 | "Betzel & Bhatt (2021)" | CORRECTED | doi:10.1016/j.neuroimage.2021.118579 is Laird AR (2021), *NeuroImage* 244:118579 (Crossref; PMID 34536537) | → "Laird (2021)" |
| 13 | "reporting and analytic-flexibility guidance … privacy guidance designed for a modality with a face" | QUALIFIED | The Laird abstract covers reproducible-analysis guidelines and ethics (stigmatization). The full text was paywalled (403), so the privacy and defacing content could not be confirmed | → "Its reproducibility guidance transfers cleanly. **It was written for MRI, a modality with a face in it.**" |
| 13 | UNESCO adopted "12 November 2025" | CORRECTED | Official text (unesco.org/en/legal-affairs/recommendation-ethics-neurotechnology): "Adopts the present Recommendation … on this eleventh day of November 2025". Press release: entry into force 12 November | → "11 November 2025". Speaker note added with both dates and the neural-data definition |
| 13 | Framework for "neural data"; "uniquely sensitive"; non-binding | VERIFIED | Official text, definition 5 ("data about the structure, activity and function of the nervous system gathered through neurotechnology") and para 48 ("uniquely sensitive"). It is a UNESCO Recommendation, not a convention, and it "Recommends that Member States … apply" | None |
| 16 | MICrONS: CC BY 4.0 obligations; citation MICrONS Consortium 2025, *Nature* 640:435–47 | VERIFIED | microns-explorer.org/terms-and-conditions ("available under the Creative Commons Attribution 4.0 International Public Licence"); /citation-policy; Crossref 10.1038/s41586-025-08790-w | None |
| 16 | FlyWire public release v783, October 2023 snapshot, CC BY-NC 4.0; pre-publication community principles | VERIFIED | flywire.ai/guidelines: "made available under license CC BY-NC 4.0 … version 783 which corresponds to a snapshot of the data from October 2023"; "community principles" for use before release | None |
| 16 | FlyWire paper CC BY 4.0 | VERIFIED | Dorkenwald et al. 2024, Rights and permissions | None |
| 16 | Hemibrain: "version not confirmed … presumed permitted, unverified" | CORRECTED | janelia.org/project-team/flyem/hemibrain: "Hemibrain is licensed under CC-BY", linked to creativecommons.org/licenses/by/4.0/. DataCite 10.25378/janelia.11676099 (v1.0 data, cited in the eLife Data Availability section): rights "cc-by-nc-4.0" | Licence cell → "CC BY 4.0 per Janelia's hemibrain page; the v1.0 figshare deposit is tagged CC BY-NC 4.0 — check before redistributing". Commercial → "Permitted per project page; **v1.0 deposit conflicts**". Speaker note rewritten |
| 16 | H01: "No licence statement found … Unclear — verify" | CORRECTED | h01-release.storage.googleapis.com/data.html: "All released datasets are licensed under a Creative Commons Attribution 4.0 License" | Licence → "CC BY 4.0, stated on the release's data page (not its landing page)…". Must do → "Attribute; cite…". Commercial → "**Permitted**". Source line and speaker note updated |
| 16 | *Science* article under AAAS licence, © the authors | VERIFIED | VoR License information line | None |
| 17 | Article CC BY 4.0 vs data CC BY-NC 4.0 | VERIFIED | As above | None |
| 18 | NIH DMS Policy NOT-OD-21-013, effective 25 January 2023; plan required | VERIFIED | grants.nih.gov NOT-OD-21-013 Key Dates: release 29 October 2020, effective 25 January 2023. Scope also covers contracts and intramural research, not only applications | None |
| 18 | "That is why CONNECTS-scale projects release data at all" | QUALIFIED | Causal claim with no source. Flagship releases such as MICrONS and FlyWire predate or sit outside the policy | → "That is one reason…" |
| 18 | Jwa & Poldrack (2022): policies span a spectrum from fully open to restricted | VERIFIED | doi:10.1002/hbm.25803, §4.2: "a wide spectrum of data sharing practices. Some repositories offer fully open sharing … others impose certain restrictions" | None |
| 20 | MICrONS CC BY: attribute, mark modifications, "pass the licence on" | QUALIFIED | CC BY 4.0 §3(a) requires a licence notice or link, not share-alike. "Pass the licence on" could be read as share-alike | → "link the licence" |
| 20 | "Hemibrain presumed permitted … H01's data licence is unclear" | CORRECTED | As slide 16 | Box rewritten: "H01's data page states CC BY 4.0, so yes, with attribution. Hemibrain's project page says CC BY 4.0 but its v1.0 deposit says CC BY-NC 4.0: 'verify before redistributing'." |
| 22 | UNESCO "calls on states to prevent applications that facilitate coercive control…"; "primarily targets devices that read or write brain activity in living people" | QUALIFIED | The text warns against coercion (paras 45, 47), "arbitrary and/or unlawful surveillance" and manipulation (para 18). "Neurotechnology" covers devices that measure or modulate the nervous system, including its *structure* (defs 2, 4). "Coercive control" and "read or write activity" are not in the text | → "warns against coercion, unlawful surveillance and manipulation … framed around devices that measure or modulate the nervous system, not archived surgical EM datasets" |
| 23 | "~1 mm³ of middle temporal gyrus resected from one patient with drug-resistant epilepsy" | VERIFIED | Shapson-Coe 2024 | None |
| 23 (notes) | "the data says 74% excitatory" | QUALIFIED | Shapson-Coe 2024: 111,272,315 of 149,871,669 detected synapses classified excitatory (74.2%). The error-corrected estimate is 102.5 M (67.1%) | Speaker note adds both figures |
| 24 | ~33 person-years; consortium labs, Princeton and Cambridge teams, citizen scientists | VERIFIED | Dorkenwald et al. 2024, *Nature* 634:124–138, doi:10.1038/s41586-024-07558-y, main text | None |
| 24 | 133,700 annotations; 139,255 neurons; 54.5 million synapses | VERIFIED | Same paper: "shared 133,700 annotations of 114,209 neurons"; "139,255 neurons … and 54.5 million synapses" | None |
| 24 | "the only published effort figure of its kind" | CORRECTED | Scheffer et al. 2020, eLife 9:e57443: "over 50 person-years of proofreading effort". The appendix gives "≈ 50–100 proofreading years". Dorkenwald 2024 also cites "50 person-years" | → "**Published effort figures are rare: FlyWire's, and the hemibrain's 'over 50 person-years'.**" Scheffer added to the source line |
| 24 | MICrONS and H01 publish no person-year number | VERIFIED | Neither main paper has one. MICrONS 2025 gives only a rate ("400–600 axon extension edits in a work week") | None |
| 25 | FlyWire Consortium co-author; "the individual is not indexed by name in bibliographic databases"; "invisible to citation metrics" | CORRECTED | PubMed PMID 39358518: CollectiveName "FlyWire Consortium" with 247 named Investigators | → "PubMed lists members as collaborators, not authors"; "largely invisible to citation metrics" |
| 25 | Kim et al. 2014: author list ends "and the EyeWirers"; individuals listed in supplementary information | VERIFIED | Nature 509:331–336, doi:10.1038/nature13240. The author line and the SI description ("list of EyeWirers who reconstructed SACs"). PubMed indexes no individual EyeWirers | None |
| 25 | Codex per-cell credits and labelling leaderboard | VERIFIED | codex.flywire.ai/about_flywire: "see the labeling leaderboard and detailed credits in each cell info page" | None |
| 25 | Shapson-Coe contributions quotes | VERIFIED | Shapson-Coe 2024 author contributions: "(proofreading of neurons)", "(production of ground truth for synapse prediction and excitatory versus inhibitory classification)" | None |
| 25, 27 | "project with 40 contributors"; "undergraduate who proofread 800 segments" | HYPOTHETICAL | Framed as scenario prompts | None needed |
| 26 | CRediT has no proofreading term; nearest are Data curation and Investigation | QUALIFIED | credit.niso.org lists 14 roles, none for proofreading. H01 filed proofreading under **Validation** | → "The nearest terms are *Data curation*, *Investigation* and *Validation* (where H01 filed it); none describes…" |
| 26 | Edit histories make per-contributor effort computable; "33 person-years" | VERIFIED | Dorkenwald 2024: FlyWire tracked edits for attribution; "more than 200 of them contributing more than 100 edits (Supplementary Table 1)" | None |
| 28 | GDPR special-category data, US state genetic-privacy statutes, national neurorights legislation | VERIFIED (existence only) | GDPR Art. 9; Chile Law 21.383 (published 25 Oct 2021, bcn.cl) | None |
| 28 | "hemibrain CC BY version and H01 data licence are marked unverified" | CORRECTED | As slide 16 | → "**Unresolved licence conflicts.** Hemibrain's project page (CC BY 4.0) and its v1.0 data deposit (CC BY-NC 4.0) disagree…" |
| 30 | Reference DOIs (Shapson-Coe, Dorkenwald, MICrONS, Scheffer, Kim, Jwa & Poldrack, NOT-OD-21-013) | VERIFIED | All resolve to the stated works (Crossref) | Added H01 data-terms and hemibrain-terms URLs |
| 30 | UNESCO "adopted 12 November 2025"; "Betzel & Bhatt 2021" | CORRECTED (same as slide 13) | As slide 13 | → "11 November 2025"; → "Laird 2021" |
| 31 | Cover image credit repeated | VERIFIED | As slide 1 | None |

## Needs owner decision

1. **Slide 9, where H01's consent and IRB approval are documented.** I could not open the *Science* supplementary Materials and Methods (403 from science.org; the PMC supplement download is bot-gated). The preprint Methods have no ethics statement. The slide now says "Look for…" rather than "live in…". Someone with journal access should confirm the supplement's ethics paragraph. If it is there, restore the stronger wording and cite the section.
2. **Slide 2, "nothing published so far identifies anyone".** This is a claim of absence and cannot be verified. Keep it as a framing assertion, or soften it to "no known re-identification has been reported".
3. **Slide 16, hemibrain licence conflict.** Janelia's project page says CC BY 4.0. The v1.0 DataCite record says CC BY-NC 4.0. I did not check later versions (v1.1, v1.2.1), and the figshare page itself returned 403. The owner should decide whether to ask Janelia FlyEM, and which licence to teach as governing.
4. **Slide 5, "Five resources, five licence positions".** After the corrections there are five rows but only about three distinct positions. Consider "Five resources, three licence positions".
5. **Slide 13, Laird (2021) characterization.** I could not access the full text, so the "reproducibility guidance transfers cleanly" wording rests on the abstract. Confirm against the paper.
6. **Upstream errors outside this deck, which I did not edit.** `content-library/connectomics/ethics-and-governance.md` repeats the Betzel & Bhatt misattribution (lines ~168, ~388), the 12 November date (~175, ~421), the "unverified" hemibrain row (~195) and the H01 "unclear" wording. `_data/expert_seed_papers/ethics-policy/betzel-2021-open-datasets.json` gives authors "Betzel RF, Bhatt DH" and a PII URL (…S1053811921008697) that differs from the DOI's real PII (S1053811921008521). Its abstract text does not match the published abstract. The rendered `course/decks/marp/out/lectures/ethics-and-governance.html` is stale until someone re-renders it.

## Image credits

- There is one image in the deck: the cover (slide 1), `assets/images/content-library/case-studies/h01/10b-segmentation-overlay.jpg`. It keeps an image-specific credit on slide 1 ("H01 release · Lichtman Lab / Harvard & Connectomics at Google · Image: CC BY 4.0 · Shapson-Coe et al. (2024)") and again on slide 31. The CC BY 4.0 claim is now confirmed by the H01 release data page. **No missing credits.**
