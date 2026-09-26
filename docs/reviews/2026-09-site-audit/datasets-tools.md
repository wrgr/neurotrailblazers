# Site audit: datasets and tools — 26 September 2026

Scope: `datasets/*.md` (5 pages), `_datasets/*.md` (18 records), `tools/*.md` (4 pages),
`_data/community_resources.yml`, `_data/technical_capabilities.yml`. The Ask an Expert and
Connectome Quality pages live under `tools/` (permalinks `/ask-an-expert/`,
`/tools/connectome-quality/`); `tools/ask-an-expert-route.md` is a redirect stub and was left
alone.

Sources were read directly: Crossref for all 17 dataset DOIs, Europe PMC and PMC full text
(Bock 2011, MICrONS 2025, hemibrain 2020, FlyWire 2024, Wildenberg 2023, Phelps 2021,
Hildebrand 2017, BANC 2026), the live BossDB project metadata
(`bossdb-metadata-snapshot.s3.amazonaws.com/mongo-data.json`) and collection API, NIH RePORTER
for UM1NS132250, the Harvard Gazette and Google Research posts of 26 September 2023, the
H01 release data page, Emmons (2015) for *C. elegans* counts, and Motta et al. (bioRxiv) for
the Kasthuri volume. `docs/reviews/2026-09-site-audit/canonical-facts.md` was followed for
MICrONS, H01, FlyWire and hemibrain numbers.

## Summary

54 table rows below, many covering several related fixes on one page. Counted by the type
tags in the table (a row can carry two tags):

| Type | Rows |
|---|---:|
| Accuracy | 31 |
| Missing content | 11 |
| Polish | 9 |
| Voice | 9 |

Files edited: 28 (18 dataset records, 5 dataset pages, 3 tools pages, 2 data files).

Checks after editing: `validate_frontmatter`, `validate_code_span_paths`,
`validate_toggled_classes` and `validate_technical_evidence` pass. A full Jekyll build (in a
case-sensitive scratch image, not the repo's `_site`) succeeded, and `check_site_links.rb` and
`check_anchor_links.rb` pass against it.

## Most important accuracy fixes

1. **MouseConnects imaging method was wrong.** The workflow tour said HI-MC cuts 30–50 nm
   sections onto ATUM tape. The NIH award abstract describes semithin sections imaged by
   multibeam SEM with ion-beam milling between images. Step 2 and the MouseConnects page
   now say so.
2. **MouseConnects collaborators and aims were partly unsourced.** Removed: David Tank,
   Hongkui Zeng and Gregory Jefferis as named leads with roles, "4,000+ Patch-seq recordings",
   "whole-brain fMOST", "tape-based section collection", "C57BL/6", and "Flagship Project".
   Kept only what a source states: Lichtman as PI (RePORTER), Jain leading Google's ML work
   (Gazette), Seung and Fiete (The Transmitter, May 2025), the seven institutions (Google),
   two 91-beam SEMs at Harvard and Princeton (Gazette), the aims (RePORTER abstract).
   Data size is now labeled a projection, with each source quoted: ~10,000 TB (Gazette),
   ~25 PB and "10–15 cubic mm" (Google), "may exceed tens of petabytes" (NIH).
3. **MouseConnects funding status added.** The award was terminated in April 2025 with other
   Harvard grants; RePORTER shows budget-year awards in August 2025 and August 2026 and lists
   it active to August 2028.
4. **FlyWire segmentation was misattributed.** Workflow and MouseConnects pages said
   flood-filling networks were used for FlyWire. FlyWire used the Seung lab pipeline; FFNs
   were used for H01. Now "used for H01".
5. **Access page pointed to nonexistent or wrong resources.** The two "PyChunkedGraph"
   notebooks 404 on GitHub (Colab returns 200 for any path). MICrONS was said to download via
   `allensdk`; it uses `caveclient`. H01 was lumped with FlyWire under "Google Research ...
   caveclient"; H01 is served from Google Cloud Storage via TensorStore/Neuroglancer. All
   replaced with provider links checked on 26 September 2026, plus each platform's license.
6. **Ask an Expert.** The "Jeff Lichtman: Wired Brains" YouTube link is a David Eagleman TED
   talk; replaced with the iBiology series and TEDxCaltech talk (titles checked via oEmbed).
   Removed "HHMI Investigator" (no source; the HHMI profile URL 404s). "Since April 2024,
   Dean of Science" corrected to appointed April 2024, effective July 2024.
7. **Dataset record numbers corrected against papers:** Bock 2011 size (~12 TB → 36 TB raw,
   ~10 TB stitched); hemibrain size (~100 TB → 26 teravoxels); FlyWire size (~50 TB → ~106 TB
   FAFB) and "8,453 cell types" (from Schlegel, not Dorkenwald → "more than 8,400");
   MICrONS dimensions, 523 → 524 million synapses, 1.6 → ~2 PB raw; H01 1.4 PB labeled
   aligned (1.8 PB raw), 16,087 neurons, 5,019 sections at 33.9 nm; Kasthuri region
   (visual → somatosensory neocortex), volume (~1,700 → ~1,500 μm³), size (~1 TB → ~660 GB),
   modality (TEM → ATUM + SEM); *C. elegans* "<1 GB" removed and synapse count split into
   5,000 chemical / 2,000 NMJ / 600 gap junctions.
8. **Portals.** Briggman 2011 is not on BossDB (checked against the live project list);
   portal removed. Added BossDB portals for BANC and the larval zebrafish. FANC's portal was
   a Harvard page not specific to FANC; now the FANC access repository. The claim-audit
   open question on BossDB hosting is partly answered: MICrONS (`microns_minnie2021`) and
   Kasthuri 2015 are on BossDB; H01 is not.
9. **Licenses added to records:** H01 CC BY 4.0, MICrONS CC BY 4.0, FlyWire data CC BY-NC 4.0,
   hemibrain conflict stated, zebrafish Open Database License.
10. **Unsourced numbers removed or labeled on the workflow tour:** 1,700 GPU-days/mm³,
    "three to five inference passes", "a few hours per proofread neuron" (replaced with the
    published 50 and 33 person-year figures), 5–20% shrinkage, the egress-versus-storage cost
    claim, "~2 PB for the pyramid", the fixative recipe (now the verified Hua 2015 / MICrONS
    recipe, attributed), "eighteen-month project" (now 326 days, attributed to the 2021 H01
    preprint).

## Changes by file

| File | Issue | Type | Fix |
|---|---|---|---|
| `_datasets/banc.md` | No portal; author missing; source carried DOI that the layout repeats | accuracy, polish | BossDB portal added; Bates et al. and preprint DOI cited |
| `_datasets/banc.md` | British spellings; "untraceable" overstated | polish, voice | American spelling; "traced end to end" |
| `_datasets/bock-2011.md` | "~12 TB" not in paper | accuracy | 36 TB raw, ~10 TB stitched; volume and 14 imaged cells added |
| `_datasets/bock-2011.md` | Body did not state the finding | missing | Inhibitory convergence result added |
| `_datasets/briggman-2011.md` | BossDB portal does not exist | accuracy | Removed; access note says not listed |
| `_datasets/briggman-2011.md` | Easily confused with Kim 2014 (claim audit) | missing | One-line disambiguation |
| `_datasets/c-elegans-white.md` | "<1 GB" wrong for images (~32 GB on BossDB); "7,000 synapses" conflates types | accuracy | Removed size; 5,000/2,000/600 per Emmons 2015 |
| `_datasets/c-elegans-white.md` | Missing that the diagram is a composite of several animals | missing | Added to "does not support" |
| `_datasets/fanc.md` | Portal not FANC-specific; access unstated | accuracy | FANC_auto_recon repo; CAVE with token |
| `_datasets/flywire.md` | ~50 TB; 8,453 cell types attributed to wrong paper; "thousands of hours" | accuracy | ~106 TB (Zheng 2018); ">8,400 (Schlegel)"; 33 person-years |
| `_datasets/flywire.md` | No license | missing | CC BY-NC 4.0 data, CC BY paper |
| `_datasets/h01.md` | "largest published volume" superlative, unverifiable as of 2026 | accuracy | Removed |
| `_datasets/h01.md` | Size unqualified; no license; neurons count missing | accuracy, missing | Canonical figures; CC BY 4.0; not on BossDB |
| `_datasets/helmstaedter-2013.md` | No neuron count | missing | 950 neurons |
| `_datasets/hemibrain.md` | "~100 TB" not in paper | accuracy | 26 teravoxels |
| `_datasets/hemibrain.md` | License conflict not shown | missing | Stated in access and body |
| `_datasets/kasthuri-2015.md` | Wrong region, volume, size, modality | accuracy | Per paper, BossDB and Motta |
| `_datasets/larval-zebrafish.md` | No portal; extent unstated | missing | BossDB; "anterior quarter of the larva"; ODbL |
| `_datasets/lee-2016.md` | Vague region; generic "null model" claim | accuracy | V1 L2/3; the proximity finding from the abstract |
| `_datasets/manc.md` | Cited only the preprint; claimed MANC+FANC isolate sex effects | accuracy | eLife reviewed preprint DOI; sex, individual and method confounded |
| `_datasets/microns.md` | Explorer dimensions, 523M, 1.6 PB; co-registration "biased toward surface" unsupported | accuracy | Paper figures; depth caveat the paper actually makes |
| `_datasets/microns.md` | No link to the site's MICrONS lab; no license | missing | Both added |
| `_datasets/mouseconnects.md` | Unsourced strain; ">10 PB" as fact; misleading "Open the data portal" button to an internal page | accuracy, polish | Quoted sources; projection label; portal removed, body links added |
| `_datasets/phelps-2021.md` | "limb motor neurons" vs paper; unsourced "bottleneck" claim | accuracy | "all 507 leg and wing"; reworded |
| `_datasets/wildenberg-2023.md` | Region "cortical synapses"; finding absent | accuracy, missing | V1 and S1; isochronic result; ages from BossDB |
| `_datasets/witvliet-2020.md` | "Whole brain" loose | polish | Nerve ring; quote from paper |
| `_datasets/*` (all) | DOI repeated in `source` and by the layout | polish | DOIs removed from `source` strings |
| `datasets/index.md` | Title/description hype; "groundbreaking" | voice | Plain title and description |
| `datasets/index.md` | "Forty years" (1986 → 2024 is 38) | accuracy | Thirty-eight |
| `datasets/index.md` | "By Resolution" card listed non-resolutions; human "tens of thousands of neurons" (H01 has ~16,000) | accuracy | Replaced with completeness categories drawn from the records |
| `datasets/index.md` | Duplicate guide cards; H01 button to storage root; "FlyWire Codex" linked to flywire.ai | polish | Removed duplicates; fixed links; added neuPrint and MICrONS lab |
| `datasets/access.md` | Dead notebooks; wrong clients; H01 misfiled | accuracy | Rewritten, see above |
| `datasets/access.md` | `# heading` inside raw HTML div rendered as literal text | polish | `markdown="1"`, h2 |
| `datasets/getting-started.md` | "silent 2% mismatch", "90% of grief" invented stats | accuracy | Removed |
| `datasets/getting-started.md` | "strange", "genuinely", "wow", "nobody competent"; em-dash chains | voice | Rewritten |
| `datasets/getting-started.md` | 60-minute section called itself "step 2 of every on-ramp"; on-ramps use different levels | accuracy | Reworded |
| `datasets/getting-started.md` | No mention of MICrONS no-account exports | missing | Added, linked to MICrONS lab |
| `datasets/getting-started.md` | `NC(type="KC.*")` without `regex=True` | accuracy | Added |
| `datasets/workflow.md` | Sectioning, FFN/FlyWire, leadership, recipe, unsourced numbers | accuracy | See items 1, 4, 10 |
| `datasets/workflow.md` | "scanning electron microscopes" (MICrONS used TEM) | accuracy | "TEM or SEM" |
| `datasets/workflow.md` | "not the images — it is the graph", em-dash chains | voice | Rewritten |
| `datasets/mouseconnects.md` | Hero button used a bare `/datasets/workflow/` href | polish | `relative_url` |
| `datasets/mouseconnects.md` | "Complete Hippocampal Connectome", "Explore the Data" for unreleased data | voice, accuracy | "in progress", "Data status" |
| `datasets/mouseconnects.md` | Methods, people, aims, size | accuracy | See items 1–3 |
| `tools/connectome-quality.md` | Description hype ("most ambitious", "critical", "robust") | voice | Plain description |
| `tools/connectome-quality.md` | "split component usually dominates" VI; ERL "does not penalize merges" | accuracy | Softened to what is generally true |
| `tools/connectome-quality.md` | "about 20 cells" presented as fact | accuracy | Labeled a rule of thumb (claim-audit item 2) |
| `tools/ask-an-expert.md` | Wrong video; HHMI; dean date | accuracy | See item 6 |
| `tools/ask-an-expert.md` | Em-dash lists; "GPT" jargon in disclaimer | voice | Rewritten |
| `tools/index.md` | "at the foot of each module page" (labs sit near the top) | accuracy | Fixed; "25 module pages" verified |
| `tools/index.md` | British spellings; redundant opener | polish | Fixed |
| `_data/community_resources.yml` | DotMotif article number 12525 (Crossref: 13045); Hider volume missing | accuracy | Fixed |
| `_data/community_resources.yml` | "de facto", "virtually every", "Leading", "High-profile" | voice | Plain notes |
| `_data/technical_capabilities.yml` | "robust" in two capability statements | voice | Replaced |

## Needs owner decision

1. **MouseConnects roles.** David Tank (Princeton), Hongkui Zeng (Allen) and Gregory Jefferis
   (Cambridge) were listed with roles; no public source found names them on this award, so
   their names were removed and the Allen and Cambridge cards show the institution only.
   Restore any you can source. Your own card (Johns Hopkins, "connectome quality
   assurance, community training, and data dissemination") is kept on your authority; the
   original said "Johns Hopkins APL", Google's list says "Johns Hopkins University" — choose.
2. **CIRCUIT** on `/tools/connectome-quality/` ("Connectome Integrity and Reliability through
   Quantitative and Iterative Training"). No independent source found; kept as your own
   project. Add a citation or link if one exists.
3. **"About 20 cells"** (Unit 08 and the quality page) is labeled a rule of thumb. Cite or keep.
4. **H01 imaging time (326 days)** is now attributed to the 2021 preprint on the workflow page,
   per the canonical-facts file. The "61-beam" detail rests on Collins et al. (2025).
5. **Hemibrain license conflict** remains unresolved (Janelia page CC BY 4.0 vs v1.0 deposit
   CC BY-NC 4.0); the record now states both.
6. **MANC and BANC counts** are deliberately absent; neither abstract states them.
7. **Whether to mention the April 2025 termination** on the MouseConnects page. It is stated
   neutrally with the RePORTER record; remove if you prefer not to.

## Outside my area

- `_layouts/dataset-entry.html`: the internal-link test `page.portal.first == '/'` does not work
  on strings in Liquid, so internal portals open in a new tab. (Moot now that the MouseConnects
  record has no portal, but the bug remains.) `_includes/cards/dataset-card.html` emits the
  portal without `relative_url`.
- `content-library/case-studies/mouseconnects-himc.md` repeats the errors fixed here: "the
  same core technology used for FlyWire" (FFNs), CAVE as HI-MC's backend, and "CA1, CA3 and
  dentate gyrus" as the defined volume (the award says hippocampal formation), and it does not
  mention the semithin-section / ion-milling method.
- `content-library/case-studies/microns-visual-cortex.md:41` caption says "about 523 million";
  canonical is 524 million.
- `content-library/case-studies/c-elegans-revisited.md:42` "~7,000 chemical synapses" (see
  canonical-facts §5).
- `notebooks/microns-lab/index.md` `CAVEclient(..., version=1507)` is past its CAVE expiry
  (canonical-facts §10).
- `about.md` lists the owner as "Will Gray-Roncal"; `mouseconnects.md` and the quality page
  use "William Gray-Roncal"; git uses "William Gray Roncal". Pick one public form.
