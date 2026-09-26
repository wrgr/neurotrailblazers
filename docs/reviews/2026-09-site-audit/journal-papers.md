# Journal papers audit (September 2026 site audit, wave 2)

Area: `content-library/journal-papers/**`, `_data/journal_papers.yml`, `_data/paper_views/**`,
`_data/expert_seed_papers/**`, `technical-training/journal-club/**`.
Date: 2026-09-26. Sources: Crossref REST API (`api.crossref.org/works/<doi>`, all 2,000 corpus DOIs plus
every DOI cited on a hand-written page), Europe PMC REST (abstracts and full-text figure captions), NCBI PMC
HTML where Europe PMC had no full text.

## Summary counts

| What | Count |
|---|---|
| Hand-written topic pages read in full | 12 (11 topic pages + index), plus methodology and 3 journal-club pages |
| Page citations checked against Crossref (title, first author, year, volume, pages, author order) | 81 DOIs |
| Numbered "Key figures" lists checked against figure captions | 38; 15 corrected, 6 made generic (no open full text), 17 confirmed |
| Corpus records checked against Crossref | 2,000 (full census, not a sample) |
| Corpus records edited in `_data/journal_papers.yml` | 97 (57 author/title fixes, 40 venue fixes) |
| Expert seed JSON files corrected | 69 of 150 |
| Reading-path descriptions corrected (`_data/paper_views/reading_paths.json`) | 2 |
| Pages with a fabricated per-paper block removed | 1 (`graph.md` "Research Ecosystem Preview") |
| Validators | all 7 pass; `journal_papers.yml` parses; edited JSON passes `json.tool` |

## Known items from the brief

| Item | Status |
|---|---|
| (a) Consistency read of every journal-papers page | Done. Citation format is uniform (Vancouver-style, `*Journal*. Year;Vol(Issue):Pages`); "Key figures" lists checked (table below); per-entry `**Tags:**` lines are display text only (the front-matter `tags:` feed `_includes/ui/entry-meta.html`, first 6 shown as pills; nothing else reads them). No `flood-filling` tag remains on any FlyWire entry; the one inaccurate tag found (`case-studies:retina` on the fly medulla paper) is fixed. |
| (b) NEURD first author | Fixed. `_data/journal_papers.yml` now lists all 58 Crossref authors starting "Celii B; Papadopoulos S; Ding Z …", citation "Celii et al. (2025) … Nature", and the OCAR Action line names Celii B. The old 12-name list had the wrong first author, the wrong order, and one person (McKellar CE) who is not an author. |
| (c) Lappalainen 2024 duplicate | Full entry kept on `neuroai.md` (#8), which gained the "what does mouse cortex lack" prompt and the Unit 09 §5 link. `network-analysis.md` #10 replaced by an un-numbered "Also read" note that keeps the statistical point and links to the anchor. Index count for Network Analysis 10 → 9, total 96 → 95. |
| (d) `validate_paper_counts.rb` | Passes: "95 authored across 11 dimensions, 2000 in corpus". Years in `journal_papers.yml` were deliberately not changed, because the validator requires them to equal `_data/corpus_2000.json`. |

## Error rates in `_data/journal_papers.yml` (full census against Crossref)

All 2,000 DOIs were queried; 1,991 returned Crossref metadata (9 are arXiv/DataCite DOIs or not indexed).

| Field | Records wrong | Rate | Pattern | Fixed? |
|---|---|---|---|---|
| Author names not in the publisher record (ignoring diacritics/transliteration) | 36 | 1.8% | 24 of the 65 records whose authors are in "Surname Initials" form carry invented names ("Bhatt AN", "Bharioke A", "Fitber A", "Prber S", "Grez P" …); 12 other records have a wrong list (Chunkflow lists a Galaxy/EBI paper's authors; *Science* 1087160 lists six people who did not write it), an institution as an author ("W. M. Keck"), or a split name ("Surya; Ganguli") | Yes. All 65 "Surname Initials" records plus the 17 others were rebuilt from Crossref (57 records changed; truncated lists became complete lists) |
| First author wrong in the rendered citation | 9 | 0.45% | NEURD (Celii), Sst types (Gamlin), inhibitory census (Schneider-Mizell), Pallotto 2015, Tavakoli 2025, Harris 2015 *Sci Data*, Chunkflow (Wu), Igneous (Silversmith), Silver 2003 | Yes |
| Title wrong | 5 | 0.25% | Placeholder "OUP accepted manuscript"; an "INAUGURAL ARTICLE …" prefix; an obsolete title for Hofer 2011; a title from a different paper (see owner decisions) | 4 fixed, 1 flagged |
| Venue wrong | 40 | 2.0% | 38 published papers listed as "bioRxiv" (DOI is the journal version); 2 IEEE conference names expanded wrongly | Yes (venue, citation and the venue named inside the OCAR text) |
| Year matches no Crossref date | 117 | 5.9% | 96 off by one year (mostly preprint year on a journal DOI), 21 off by 2–6 years (e.g. Krizhevsky *ImageNet* CACM listed 2012 vs 2017; Pedigo *eLife* 2022 vs 2025) | **No**: locked to `corpus_2000.json` by the validator. See "Outside my area" |
| DOI points to a different paper | 2 | 0.1% | See owner decisions | Title aligned to DOI for one; one flagged |

A 40-record random sample would have shown roughly the same picture (the census rate for any error in
authors, title or venue is 4.1% before fixes and about 0.1% after; year errors remain at 5.9%).

## Systematic content problem: templated per-paper text

Of the fields shown on every journal-club card, only title, authors, year, venue, DOI, abstract and citation
links are specific to the paper. Across 2,000 records there are only **12 distinct** texts each for OCAR
Opportunity, Challenge, Resolution and Future Work, the Beginner and Advanced summaries, and the discussion
prompt sets (one per research domain; `scripts/corpus_curation/generate_ocar_all_2000.py` writes them from
the domain label). The Action line is per-paper only in that it inserts the first author and title. The
index and methodology pages had described these as "verified 5-part OCAR research cards". Within my area I:

- rewrote the index, methodology and journal-club copy to say what is per paper and what is per domain;
- added a one-line caveat above the OCAR block in the graph drawer;
- relabelled the OCAR block in both AI-prompt builders as "Domain-level OCAR notes (generic to the research
  domain)" and told the assistant to rely on the paper and to say "not reported" rather than guess;
- removed the graph drawer's "Research Ecosystem Preview", which invented a dataset ("FlyWire / FAFB /
  hemibrain" for any fly paper), a tool stack, and a five-step "Analysis Protocol Breakdown (How Conducted)"
  (high-pressure freezing, OsO₄/uranyl/lead staining, affinity nets, proofreading) for every paper, including
  MRI and theory papers.

The card itself (`_includes/cards/journal-paper-card.html`) is outside my area; see below.

## Fix table

| File | Issue | Type | Fix (source) |
|---|---|---|---|
| `_data/journal_papers.yml` | NEURD authors invented; first author given as Schneider-Mizell | Accuracy | 58 authors from Crossref, citation "Celii et al. (2025)", Action line updated (Crossref 10.1038/s41586-025-08660-5) |
| `_data/journal_papers.yml` | 65 "Surname Initials" author lists, 24 with invented names | Accuracy | Rebuilt from Crossref for all 65 |
| `_data/journal_papers.yml` | 17 other wrong/garbled author lists (Chunkflow, Igneous, Silver 2003, Niell 2008, Ohki 2007, Zador 2023, Lin 2020, Uytiepo 2024, Zhao 2025, Liu 2025 (Yi Zhong replaced by an unrelated Japanese name), 5 transliterated to Cyrillic/Greek/Hangul) | Accuracy | Crossref author lists |
| `_data/journal_papers.yml` | 4 wrong titles | Accuracy | Crossref titles; citation lines rebuilt |
| `_data/journal_papers.yml` | 40 wrong venues | Accuracy | Crossref container-title |
| `_data/paper_views/reading_paths.json` | Said Turaga 2010, Sheridan 2023, Bullmore & Sporns 2009 and Rubinov & Sporns 2010 "are not in this catalog"; all four are | Accuracy | Descriptions and uuids corrected; unresolvable `work_eccb…` id replaced with Plaza 2014's DOI |
| `_data/expert_seed_papers/**` (69 files) | Invented author names in 57 files; 12 DOIs pointing to other papers or not resolving (NEURD, Funke TPAMI, MANC ×2, network statistics, Hayworth GCIB, annotation standards ×2, Kaynig, DotMotif, BossDB/Harris titles) | Accuracy | Crossref authors; DOI/title/year corrected where the title matched a Crossref record exactly |
| `_data/expert_seed_papers/README.md` | Stale counts (29 experts, 102-paper corpus) | Stale count | Dated; accuracy note added |
| `index.md` | "verified" claims, "Welcome", emoji headings, "5,460+" (exact count is 5,460), Network Analysis 10, total 96 | Accuracy / voice / count | Rewritten; counts 9 and 95; per-paper vs per-domain note added |
| `methodology.md` | "verified 5-part OCAR cards"; "macroscale … filtered out" (some remain); target shares presented as if met | Accuracy | Rewritten to state what is templated and that targets are met only in the Top 500 |
| `case-studies.md` | MICrONS cited as 2021 bioRxiv; "0.5 billion synapses"; "most comprehensive" | Accuracy / canonical | *Nature* 2025;640:435-447 with preprint note; 524 million; structure-function claims attributed to Ding et al. 2025 (Crossref, Europe PMC abstract) |
| `case-studies.md` | Invented figure numbers for Kasthuri, MICrONS, FlyWire, Cook, Takemura, Bock, Witvliet | Fabricated figure refs | Replaced with captions read from PMC (or made generic where no full text) |
| `case-studies.md` | Witvliet authors "Meiber Y, Chisholm R, Wang Y" | Accuracy | "Meirovitch Y, Berger DR, Wu Y" (Crossref) |
| `case-studies.md` | Kasthuri volume "roughly one dendritic field" | Accuracy | "a cube about 11 μm on a side" |
| `case-studies.md` | H01 "fixation was delayed" | Unsupported | Immersion vs perfusion fixation, stated neutrally |
| `case-studies.md` | White 1986 "started connectomics", "If you read one paper…", "explicit accounting of reconstruction confidence" | Voice / unsupported | Removed; canonical 302 / 118 classes / 5,000 / 2,000 / 600 wording |
| `case-studies.md` | Takemura "resolved"; "later tested genetically"; `case-studies:retina` tag on fly medulla | Overclaim / tag | "suggested"; Maisak 2013 described by what it recorded; `case-studies:optic-lobe` |
| `case-studies.md`, `connectomics.md` | FlyWire "54.5 million synaptic connections", "cell type annotation for all neurons", "quality metrics framework" | Accuracy | "synapses"; annotations credited to Schlegel et al.; 826-neuron F1 99.2% check (Europe PMC full text) |
| `connectomics.md` | "Bae et al. (2021)" = MICrONS preprint; invented "modest correlations", "fiducial-based co-registration" findings | Accuracy | Renamed to MICrONS Consortium 2025; findings attributed to Ding et al. 2025 abstract |
| `connectomics.md` | Bullmore & Sporns title "…structural and functional connectomics" | Citation | "…structural and functional systems" (Crossref) |
| `connectomics.md` | Winding "about 3,000 neurons"; wrong figure list | Canonical / figures | 3,016; captions from PMC |
| `connectomics.md` | H01 "roughly a third … neurons" | Accuracy | "about 16,000 of them neurons; glia outnumber neurons about two to one" (canonical-facts §2) |
| `cell-types.md` | Schneider-Mizell cited as 2023 bioRxiv with wrong author order; invented classification pipeline | Accuracy | *Nature* 2025;640:448-458; description from the abstract |
| `cell-types.md` | Wrong figure lists (Gouwens, Tasic, Schlegel, BICCN); unverifiable (Zeng & Sanes, Markram) | Fabricated figure refs | Corrected from PMC captions; made generic |
| `cell-types.md` | "most comprehensive … ever made", "gold standard", Loomba "connectivity signatures differ" | Voice / unsupported | Toned down or removed |
| `data-storage.md` | neuPrint cited as 2020 bioRxiv | Citation | Plaza et al. 2022 *Front Neuroinform* 16:896292, preprint noted; anchor link updated |
| `data-storage.md` | Hemibrain "about half the fly brain", "20 million synaptic connections", "~50 person-years" | Canonical | "large part of the central brain", "about 20 million synapses", "over 50 person-years" |
| `data-storage.md` | Macrina "thousands of cloud GPUs" and figure numbers (no full text) | Unverifiable | Removed / made generic |
| `data-storage.md` | neuPrint "exceeds single-server memory" claim | Unsupported | Removed |
| `imaging.md` | Yin 2020 "six TEMs" for MICrONS | Accuracy | Five imaged the mm³; platform later six (PMC full text) |
| `imaging.md` | SBEM "isotropic-ish voxels", "beam damage accumulates", "Zeiss Gemini" | Accuracy | Corrected |
| `imaging.md` | Xu 2017 heading "Enhanced FIB-SEM Imaging for Cell Biology" | Citation | Real title |
| `imaging.md` | Zheng "about 100,000 neurons … took years" | Attribution | Attributed to the paper's estimate, FlyWire's 139,255 added; "years" removed |
| `computer-vision-ml.md` | "merge errors cost far more" stated as universal; several "clearest/best" superlatives; Buhmann "tens of millions" | Overclaim | Softened |
| `mri-connectomics.md` | `---` directly after a paragraph (renders as a setext H2) | Broken Markdown | Blank line added |
| `mri-connectomics.md` | Sporns 2005 "coined the word"; "directly motivated the HCP"; HCP "highest-quality ever" | Attribution / hype | Hagmann's independent 2005 coinage noted; softened |
| `network-analysis.md` | Winding "550,000 connections" | Canonical FIX | 3,016 neurons, about 548,000 synapses |
| `network-analysis.md` | Lappalainen duplicate | Dedupe | See item (c) |
| `neuroai.md` | Saxe et al. summary attributed claims not in the paper | Accuracy | Rewritten from the abstract; our inference labelled as ours |
| `neuroai.md` | Bassett Fig. 4 "generative models" | Figure ref | Fig. 3 validity, Fig. 4 bridging model types (PMC captions) |
| `proofreading.md` | Matejek pages missing | Citation | 2084-2093 (Crossref) |
| `technical-training/journal-club/graph.md` | Fabricated per-paper dataset/tool/protocol box | Fabrication | Removed (with its CSS) |
| `technical-training/journal-club/graph.md`, `index.md` | "self-organizing organic force", "Flagship/Landmark", "milestone" in prompts, OCAR presented as the paper's findings | Voice / accuracy | Plain copy, tier labels "Top 500/1,000/2,000", caveats in prompts |

## Needs owner decision

1. **Templated OCAR notes, summaries and prompts on 2,000 cards.** Options: (a) hide OCAR/summaries/prompts on
   the card and show the abstract instead; (b) regenerate them per paper from the abstract, with review;
   (c) keep them, labelled as domain notes (the current state after this pass). The card include is
   outside my area.
2. **`10.1016/j.nicl.2018.06.018`** (tier 500, health): the record claimed "The structural connectome in
   traumatic brain injury", but the DOI and abstract are a schizophrenia dynamic-fMRI paper. Title now matches
   the DOI; the paper is macroscale fMRI and probably out of scope. Remove or replace.
3. **`10.18260/1-2--42544`** (tier 500, training-outreach): title "A SwarmAI Testbed…" (2024) but the DOI is
   "Board 176: Summer Robotics Program for High School Students" (ASEE 2023), and the abstract fits neither
   well. Left unchanged; verify by hand or remove.
4. **Off-scope papers in the corpus.** The methodology says macroscale work was screened out; at least the two
   records above plus the 2 `mri`-dimension records remain. Decide whether to prune.
5. **Expert seed files with no verifiable source** (18): `jain-2016-ffn-arxiv`, `kebschull-2025-mapseq2`,
   `kording-2015-rosetta-brains`, `lee-2017-superhuman`, `seung-2017-superhuman`,
   `maitin-shepard-2021-neuroglancer`, `markowitz-2023-brain-initiative`, `priebe-2017-drosophila-spectral`,
   `saalfeld-2023-n5-zarr`, `seung-2012-connectome-book`, `silversmith-2021-cloud-volume`,
   `spirou-2014-calyx-development` (DOI does not resolve), `spirou-2023-bushy-cell-convergence` (DOI is a
   different Spirou paper), `tolias-2021-microns-functional` (DOI does not resolve), `vogelstein-rj-2014-iarpa-microns`,
   `vogelstein-2018-rdpg-survey`, `vogelstein-2019-graspy`, `yendiki-2024-brain-connects-linc`. Several titles
   ("BRAIN Initiative connectomics program direction and strategy", "IARPA MICrONS program management and
   connectomics strategy") look invented. These files are not rendered anywhere; delete or source them.
6. **White 1986, Kasthuri 2015, Bullmore & Sporns, Zeng & Sanes, Markram, Macrina "Key figures"**: made generic because no open full text was
   available. Restore numbered figures only after checking the PDFs.

## Outside my area

- **`_data/corpus_2000.json`, `_data/corpus_1000.json`, `_data/corpus_500.json`, and the downloadable copies in
  `data/`**: carry the same invented author lists, wrong venues and wrong titles fixed here in
  `journal_papers.yml`. `scripts/derive_journal_papers.py` rewrites `authors`, `journal` and `citation` in
  `journal_papers.yml` from `corpus_2000.json`, so **re-running it would undo these fixes**. Apply the same
  corrections to the corpus JSON (the 97 DOIs are recoverable from `git diff _data/journal_papers.yml`), then
  fix the 117 years there (21 are off by 2–6 years, e.g. 10.1145/3065386, 10.7554/elife.85300,
  10.1038/s41586-024-07088-7, 10.1371/journal.pcbi.1001066 Varshney 2011 listed as 2009,
  10.3389/fcomp.2021.613981, 10.1093/cercor/bhae405, 10.1093/cercor/bhaf073) and re-run the derive script,
  which also rebuilds `paper_views/era.json` and `year.json`.
- **`_includes/cards/journal-paper-card.html`**: shows the templated OCAR notes as if paper-specific; needs a
  caveat or the owner decision in item 1.
- **`technical-training/journal-club/graph-data.json`** is fine, but it maps `organism` to `p.tags`, so values
  like `none` and `tier_500` appear as organisms in the graph filter/tooltip. The tag-to-organism mapping
  should filter to organism tags.
- **`_data/paper_views/tier.json`** and **`era.json`** labels ("Core Flagships", "Contemporary Surge",
  "State of the Art") are generated by scripts in `scripts/`; tone them down at the source.
- The remaining em-dash density on the topic pages (about one per ten lines, mostly paired parentheticals) is
  within the brand guide but could be thinned in a later voice pass.
