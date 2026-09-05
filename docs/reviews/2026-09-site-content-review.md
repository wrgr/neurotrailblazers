# Site content and completeness review

*Reviewed 5 September 2026 against `main` at `e6e8bcb`. Companion documents:
`docs/planning/NEXT_CONTENT_PASS.md` (the work plan derived from this review) and
`docs/brand/BRAND_GUIDE.md` (identity and slide system).*

---

## Method

- Built the site (Jekyll 3.x, 283 rendered pages) and ran the repository's own audits:
  `check_site_links.rb`, `check_anchor_links.rb`, `validate_frontmatter.rb`,
  `validate_figure_refs.rb`, `validate_technical_evidence.rb`, `validate_paper_counts.rb`,
  `check_deck_freshness.rb`, `validate_dictionary.rb`. **All pass.** There are no broken
  internal links, no missing figures, no stale decks.
- Four area audits, each reading the pages in full rather than sampling: the technical
  units and decks; the 25 modules, tracks and teaching material; the content library,
  hidden curriculum, datasets and data files; the front door, navigation and framing pages.
- Every "wrong" finding below was checked against the file, and the two build-dependent
  claims (empty Teaching Hub grid, duplicate `<title>`) were confirmed in the rendered HTML.

Word counts (learner-facing markdown and HTML, excluding generated decks and data):

| Area | Pages | Words |
|---|---:|---:|
| Content library | 49 | 122,800 |
| Modules (25 pages + generated slides pages) | 52 | 76,000 |
| Technical training (9 units, atlas, dictionary, journal club, tutorials, lecture plans) | 27 | 62,300 |
| Teaching (hub, facilitator guide, lectures, 25 session kits) | 34 | 33,700 |
| Hidden curriculum | 8 | 27,200 |
| Neuronauts story and kids portal | 4 | 25,000 |
| Everything else (start here, core, tracks, tools, personas, datasets, side quests, models…) | ~40 | ~35,000 |

---

## Verdict

**The site is structurally complete and mechanically sound, and its two best layers are
excellent. Its problems are now in three places: data that renders wrong, an
instructional layer that was generated but not finished, and a front door that does not
say who the site is for or how to reach anyone.**

By layer:

| Layer | State | Evidence |
|---|---|---|
| Technical units 01–09 | **Strong.** Every unit has outcomes, a worked example, a rubric-backed lab, a "does not cover" statement and a recovery section. Zero broken cross-references. | Unit table below |
| Content library | **Strong reference, uneven coverage.** 35 real reference pages at 1,500–4,800 words; 24 of them have no figures, and several central topics are absent. | §3 |
| Hidden curriculum | **Complete.** Coherent seven-page set; the best-written prose on the site. | — |
| Neuronauts story | **Strong.** ~8,900 words, 54 sources, 100 inline citations, explicit confidence badges. | — |
| Modules 01–25 | **Good pages, broken derivatives.** Pages are 1,900–3,600 words with real scenarios. The worksheets, session kits and decks generated from them ship empty rubrics, broken scenarios and no speaker notes. | §1.B–C |
| Journal club / paper corpus | **Data is corrupt in the rendered file.** `_data/journal_papers.yml` has empty authors on all 2,000 entries, a self-attribution citation template, and 814 wrong years. The clean data exists in `corpus_2000.json`. | §1.A |
| Decks | **Split.** Three graduate-course decks are polished, themed and unlinked from the site. The ten technical-unit decks are unthemed bullet lists with two empty slides. | §1.F |
| Front door and framing | **Weakest layer.** Seven different taglines, no About, no contact, no license, no citation, "About" in the nav points at a frameworks hub, and several counts on the home and core pages are wrong. | §2, §4 |
| Brand | **Three palettes in use, none decided.** Config and legacy CSS use blue/purple/cyan; the 2026 refresh uses teal/amber; the graduate decks use a fourth blue. The favicon is a purple-and-orange brain unrelated to the teal banner. | §5 |

---

## 1. Wrong or broken (verified)

Ordered by blast radius. File references are to the repository root.

### A. Data integrity

1. **`_data/journal_papers.yml` is corrupt and it is the file the site renders.**
   All 2,000 entries have `authors: ''`. All 2,000 `citation` strings read
   "NeuroTrailblazers Consortium (YEAR)", attributing every paper in the field to the
   site. 814 of 1,980 DOI-matchable entries carry a `year` that disagrees with
   `_data/corpus_2000.json` (spot checks: `10.1038/nature11614` listed 2017, actual 2012;
   `10.1016/j.cell.2011.08.053` listed 2020, actual 2011). Journal names are truncated at
   40 characters (66 entries read "Proceedings of the National Academy of S"). No abstract
   field. `content-library/journal-papers/methodology.md:69` promises "complete author
   list" and `:16` promises "100% full multi-paragraph abstracts"; the corpus JSON has both
   on 2,000/2,000 records, so this is a re-derivation, not new authorship.
2. **`_data/core_surfaces.yml:31` says "191 papers with discussion prompts".** The
   corpus is 2,000. Rendered on `/core/` and `/tracks/`.
3. **`_data/core_surfaces.yml:10` says "45 entries across 8 topic areas".** Actual leaf
   entries excluding journal-paper stubs: 33 across 7 directories.
4. **Track hours contradict module pages.** `_data/track_catalog.yml:55` budgets 15 h for
   modules 1, 3–11, whose front matter sums to 39.5 h. Line 133 budgets 20 h for modules
   declaring 44 h. Modules 06 and 07 are listed on the Research-in-Action card (`:112`) but
   appear in no sequence step; module 02 is listed on Career & Community (`:190`) and never
   sequenced.
5. **Unit-to-module mappings disagree.** Unit 08's "Course links" names modules 07 and 12
   (`technical-training/08-segmentation-and-proofreading.md:525`); `_data/technical_track.yml`
   maps it to 06 and 07. Unit 09 names 09 and 15 (`…/09-connectome-analysis-neuroai.md:534`);
   the data file maps 10, 13, 14, 15, 20.
6. **Unit 05 disagrees with itself on time**: front matter `:14` vs. the Before-you-start
   table `:25` (one adds a 60-minute tutorial).
7. **`_data/connects_learning_map.yml`** is referenced nowhere; it holds the award numbers
   (U24NS139927, U24NS140384) that appear nowhere on the site.

### B. Generated teaching material

8. **All 25 worksheets ship an empty rubric.** `scripts/generate_module_teaching_materials.rb:89`
   selects rubric lines with `^-\s+\*\*`, which matches the three tier labels
   ("Minimum pass", "Strong performance", "Common failure modes") and drops every indented
   criterion beneath them. Learners are told to score themselves against three headings.
   The deck generator (`:154`) uses a different helper that keeps the criteria but flattens
   the nesting.
9. **Four worksheets and four session kits print a literal broken scenario line.**
   `**Scenario:** {: #studio-activity}` in `assets/worksheets/module0{1,2,3,5}/…-activity.md:41`
   and `teaching/sessions/module0{1,2,3,5}.md`. Modules 01–03 structure the studio as
   `### Part A/B/C/D`; module 05 uses a `### Scenario` heading; the regex caught the
   kramdown attribute list instead. These are the first three modules a learner opens.
10. **16 of 25 module pages have no interactive layer at all.** `_data/module_interactives.yml`
    defines content for modules 01–09 only. *(Corrected on 5 September 2026 while fixing it:
    the review originally said the include falls back to a generic `default` quiz. It does
    not — `_includes/ui/module-interactive-lab.html` suppresses the whole section when the
    module key is absent, so modules 10–25 rendered no lab rather than a filler one. The
    `default` block is still load-bearing for `progress_steps`, which every module uses.)*
11. **Raw Liquid in four learner-facing worksheets.** `assets/worksheets/module1{2,3,4,5}/`
    contain unprocessed `{{ '/content-library/…' | relative_url }}` because the generator
    injects the pre-class-preparation bullets unescaped and the files have no front matter.
12. **Zero speaker notes in all 25 module decks**, although `teaching/lectures/connectomics-01-introduction.md:31`
    and `_data/track_catalog.yml:72-73` tell instructors the decks carry them.
13. **Phantom resources in an instructor kit.** `teaching/module22-public-engagement.md`
    tells facilitators to use "Atlas vs. Connectome", "BRAIN Grant Detective" and
    "Public Impact Wall". None exists anywhere in the repository. Two of four 60-minute
    segments point at nothing.
14. **`modules/module12.md:241`**: `| MouseConnects (planned) | … | TBD | TBD | >10 PB |`.

### C. Rendering and layout

15. **The Teaching Hub's main block renders empty.** `teaching/index.md:58` and
    `modules/index.md:64` loop over `site.modules`. `_config.yml:17` declares that
    collection but no `_modules/` directory exists (module pages are regular pages under
    `modules/`). Confirmed in the build: the "Module Teaching Kits" grid contains no cards
    under a promise of four links per module. `modules/index.md` survives only because it
    also includes `module-index.html`, which reads `site.data.modules`. The `avatars` and
    `datasets` collections are declared and equally empty.
16. **Every page ships two `<title>` and two `<meta name="description">` tags.**
    `_layouts/default.html:6-7` writes them by hand and `:12` calls `{% seo %}`, which
    writes them again.
17. **`_layouts/redirect.html:12-13`** places the canonical link in the body, where search
    engines ignore it. Affects all seven redirect pages.
18. **Decorative banner on every page has non-empty alt and no dimensions**
    (`_layouts/default.html:17`).

### D. Factual errors in content

19. **`datasets/index.md:217-225`**: the 2011 card titled "Bock et al. — Mouse Retinal
    Circuits" (region: retina, method: SBEM) describes Bock et al. 2011, which is visual
    cortex by ssTEM. The card merges Bock with Briggman et al. 2011.
20. **`initiatives.md:35`**: H01 cited as `10.1126/science.abk1256`. Correct DOI is
    `10.1126/science.adk4858`, used everywhere else on the site.
21. **Numbers for the same dataset differ across pages.** H01 cells: 50,000 (`datasets/index.md:106`)
    vs. 57,000 (`:323`, `content-library/case-studies/h01-human-cortex.md:90`). H01
    synapses: 130 M (`datasets/index.md:107,324`) vs. 150 M (`h01-human-cortex.md:90,176`).
    FlyWire synapses: "50+ million" in six places vs. ~54.5 M in two.
22. **`index.html:83`**: "Read the Full Story (25 min)". The story is ~8,900 words; 40–45
    minutes at normal reading speed.
23. **`neuronauts/kids.md:366`** cites the "500 Key Papers" corpus; the corpus is 2,000.
24. **"35 exports came to 88 MB"** repeated in 11 files (`technical-training/slides/*.md`);
    there are 38 decks. **"12 research domains"** in four places on
    `technical-training/journal-club/index.md`; the data has 14. **en585781 README**
    slide counts are off by one on all three decks.

### E. Dead ends

25. **`neuronauts/index.html:2221`**: "If you find an error, tell us" links to
    `/frameworks/`. The site's only correction channel lands on a framework hub.
26. **`models.md:67,84`**: "MERIT framework summary" and "Professional Pathways guide
    summary" link to `/frameworks/`, which contains neither.
27. **`neuronauts/kids.md:89,115,141,167,193`**: five different stories, five identical
    "Read the real research paper cards" links to the generic journal-club URL.
28. **`content-library/index.md:166-177`** maps twelve corpus domains onto nine pages;
    three domains ("Physiological Validation", "Synthesis & Reviews", "Workforce Training")
    route to `methodology/`, a page about how the corpus was built. "Health, Disease &
    Translation" routes to a diffusion-MRI reading list. `computer-vision-ml.md` (3,354
    words) is linked from the index zero times.
29. **`_data/open_problems.yml:53`** sends open problem 2 (synapse detection) to
    `neuroanatomy/synapse-classification/`, a synapse *biology* page. There is no synapse
    *detection* page (see §3).

### F. Decks

30. **`course/decks/marp/07-glia.marp.md:63`** ("Oligodendrocyte-associated cue context")
    and **`atlas-connectomics-reference.marp.md` slide 7** are empty slides in committed,
    site-linked decks. `04-…marp.md` slide 5 is titled "Visual context" and has no image.
    `07-glia.marp.md:66` is a one-line note-to-self rendered as a slide.
31. **The ten technical-unit decks declare no theme** (the 25 module decks use `default`,
    the three graduate decks use `frontiers`). They are 300–530 words of bullets, no
    cover, no license, no attribution.
32. **The three graduate decks (`course/decks/marp/en585781/`, 56–59 slides, ~9,000 words
    each, DOI-pinned, CC BY-SA) are linked from nowhere on the site.**
33. **21 extracted figure assets are unused**, including five each for units 03 and 04.

---

## 2. Missing entirely

### Framing pages (none of these exist)

About or team · Contact (the configured `info@neurotrailblazers.org` renders nowhere;
zero `mailto:` links) · License or reuse terms (the home page promises "reusable
materials") · How to cite (no `CITATION.cff`) · Contributing (README points to a file on
another branch) · Changelog · FAQ · Accessibility statement · Privacy (Google Fonts and
third-party iframes are embedded) · Acknowledgements with award numbers · Outcomes or
evidence of impact · Events · Any way to find another learner ("the single highest-value
thing you can add is one other person", `_data/modes.yml:36`, with no mechanism).

### Reference topics absent from the content library, ranked by centrality

1. **Synapse detection as a method.** The site's own open problem 2; the whole treatment
   is five bullets in `infrastructure/reconstruction-pipeline.md:113-117`. Seed papers
   (Funke 2018, SynEM 2017) are already in `_data/expert_seed_papers/`.
2. **Functional–structural integration (MICrONS calcium + EM).** The flagship example of
   why connectomics matters; `microns-visual-cortex.md` is tied for thinnest case study and
   "two-photon" appears in three library files.
3. **Ethics, consent and data governance.** Zero library pages; H01 is human surgical
   tissue. Content exists only inside `modules/module19.md`, inverting the site's
   reference-then-teach architecture.
4. **Comparative connectomics across species.** The mission is fly → mouse → human;
   cross-species comparison appears incidentally in three files.
5. **Non-EM methods**: expansion microscopy, X-ray nanotomography, barcoding (MAPseq,
   BARseq), array tomography, LICONN. All absent; all have seed papers curated.
6. **BANC** appears nowhere on the site; MANC and larval zebrafish appear only in the
   atlas. The datasets timeline stops at MICrONS 2025.
7. **Careers and the funding landscape** as a map (who funds, what the jobs are, where a
   trained proofreader goes). Career *mechanics* are well covered; the landscape is not.

### Instructional material absent

Semester syllabus or course shell (nothing maps 25 modules + 9 units + 3 lectures onto
weeks) · Pacing guides for 16-week, 10-week and 2-day shapes · Assessment bank beyond the
three-question inline quiz · Answer keys or model responses for any of the 25 worksheets ·
Instructor FAQ · Student reference cards (module 05 instructs "using the artifact
reference card"; it does not exist) · Rubric norming material · Placement diagnostic ·
Worked examples in eight modules (02, 03, 05, 07, 16, 17, 18, 19) · Runnable notebooks
(zero `.ipynb` in the repository; `assets/notebooks/module*/` are empty `.gitkeep`
directories) · Figures on all four `imaging/` pages and on `proofreading-tutorials.md`,
a page teaching visual diagnosis with zero images.

### Structural

A real `_datasets/` collection. The layout and config exist; the data does not. ~19
datasets are hand-written HTML in one 580-line file, several described twice with
different numbers.

---

## 3. Inconsistent

**Messaging.** Eleven distinct one-line descriptions of what NeuroTrailblazers is, leading
with six different audiences (`_config.yml:3,105-107`, `index.html:3,4,11,13,16,55`,
`_layouts/default.html:56`, `README.md:3`, `start-here.md:4`, `core/connects-ecosystem.md:13`).
`start-here.md:4` calls the field "computational neuroscience"; nothing else does. The
best positioning sentence on the site ("IC3 and APEX organize and expose the science.
NeuroTrailblazers organizes the learning.") is on a page with one inbound link.
`tagline_lines[0]` in config never renders.

**Naming.** The technical course has four labels (Technical Course, Technical Training,
technical units, Technical Training Course Hub). The Neuronauts story has four names. The
two program-model pages have three naming systems across title, nav and inbound links.
Persona names differ across front matter, H1 and the start-here cards. Page titles follow
three patterns.

**Information architecture.** `/frameworks/`, `/models/` and `/education/models/` are one
topic across three URLs plus five redirect stubs and two circular links. `/modes/`,
`/kb/`, `/concepts/` and `/core/connects-ecosystem/` are not in the navigation. `/tools/`
lists two entries, neither an interactive tool of the site's own, while the real
interactives (citation graph, KB visualisations, concept explorer, module labs) live
elsewhere. Six pages paste the same `ui/learning-tracks.html` block with a content-free
intro. `_config.yml:71-95` is a stale mirror of the nav.

**Durations.** Each unit carries three incompatible figures: page (150–270 min), lecture
plan (85–95 min), deck (60 min). Modules declare 4–6 h and specify about 2 h.

**Headings.** The graded artifact is "Lab" (7 units), "Studio activity" (05), "Drill"
(07), "Mini-lab" (atlas); `_includes/ui/technical-capability-brief.html:33` hardcodes
"lab". Run-of-show headings drift across three forms in the modules. The technical
training index says "nine units" and renders ten cards.

**Accessibility.** Raw emoji without `aria-hidden` inside headings and buttons
(`neuronauts/kids.md`, `initiatives/outreach.md`, home `.card-icon`), alongside the
correct `aria-hidden` entity pattern used on `start-here.md` and `core/index.md`.

---

## 4. Brand state

- **Palette.** `_config.yml:110-115` and the top of `assets/css/site-styles.css` define
  neural blue `#2563eb`, cerebral purple `#7c3aed`, axon cyan `#06b6d4`; the 2026
  refresh block at `:1170` defines teal `#006d6b`, amber `#e8820c`, ink `#0d1117`. The
  legacy tokens are still used 70 times; the refresh tokens 20 times; and 60-plus
  hardcoded hex values (Tailwind blues and violets: `#1e40af`, `#5b21b6`, `#dbeafe`,
  `#ede9fe`) sit outside both systems. The graduate deck theme uses a fourth palette
  (`#1f6fb2`).
- **Type.** Plus Jakarta Sans is loaded from Google Fonts on every page and used nowhere.
- **Marks.** The banner (teal-navy, silhouettes walking dendrite trails, condensed caps
  wordmark) is the only coherent brand artefact. The favicon is a purple-and-orange brain
  on a gradient; `assets/images/nt-favicon.png` (2.4 MB) and the PNG banner (1.3 MB) are
  unreferenced. There is no vector mark, no lockup, no clear-space rule, no social card.
- **Iconography.** Emoji as icons on the home page and in headings.
- **Decks.** No shared theme. The graduate decks' `frontiers.css` is the only considered
  slide design and it is not the site's palette.

`docs/brand/BRAND_GUIDE.md` resolves this: one palette derived from the banner, a vector
mark and lockups, a Marp theme, a PowerPoint template, and a migration table from the
legacy tokens.

---

## 5. Per-unit and per-module state

### Technical units

| Unit | Words | Self-checks | Figures | Graded artefact | Note |
|---|---:|---:|---:|---|---|
| 01 Why Map the Brain | 3,799 | 3 | 4 | Lab 60 min | — |
| 02 Brain Data Across Scales | 3,989 | 3 | 4 | Lab 75 min | Only unit with a sample answer for a lab step |
| 03 EM Prep and Imaging | 4,438 | 2 | 4 | Lab 90 min | Most visual topic, four figures; five unused assets on disk |
| 04 Volume Reconstruction | 4,453 | 2 | 4 | Lab 90 min | Eight-stage pipeline, two self-checks |
| 05 Neuronal Ultrastructure | 3,722 | 3 | 7 | Studio 75 min | Time contradiction (§1.A.6) |
| 06 Axons and Dendrites | 3,822 | 2 | 6 | Lab 90 min | — |
| 07 Glia | 3,246 | 1 | 3 | Drill 60 min | Thinnest unit on every axis |
| 08 Segmentation & Proofreading | 4,653 | 1 | 10 | Lab 2 h | Longest unit, one self-check |
| 09 Connectome Analysis / NeuroAI | 4,653 | 2 | 19 | Lab 2 h | Three figures reused from Unit 01 |
| Atlas (reference) | 2,381 | 0 | 4 | Mini-lab 30 min | Rendered as a tenth "unit" card |

Dictionary: 127 terms, complete. Journal club data fields populated on 2,000/2,000 except
`pdf_url` (1,725). Cross-references: zero broken.

### Modules

Median 2,401 words. All 25 have the generator-required headings. Thin tail: 02 (1,907),
03 (2,089), 21 (2,158), 20 (2,190), 16 (2,262); 20 and 21 carry three misconception
guardrails against a median of five. Section coverage tracks authoring generation rather
than pedagogy: "Why this module matters" missing from 04–11 (the technical core);
"What this module does not cover" and "Common errors" missing from 02, 03, 05, 07, 16,
17, 18, 19; no references section in 15–25. Scope collisions: 17 vs 22 (both titled
"Scientific Writing…"; 22 is about talks), 08 vs 20 (hypothesis testing vs. inference,
no cross-reference), and every module vs. its technical unit, unacknowledged on the
module page.

### Content library

35 reference pages, 1,513–4,835 words. Strongest: `connectomics/open-problems-undergrad.md`,
`case-studies/h01-pipeline.md`, `proofreading/worked-examples.md`. Thinnest and most
load-bearing: `infrastructure/provenance-and-versioning.md` (1,513 words, the destination
for the norm the site repeats most), `cell-types/neuron-type-identification.md` (1,862,
landing page for open problem 3), `imaging/tissue-preparation.md` (1,853). 24 of 35 pages
have no figures; 32 carry `reference_images:` front matter describing figures never
produced. `journal-papers/mri-connectomics.md` is off-mission by the corpus's own
methodology (`methodology.md:44` filters macroscale MRI out).

---

## 6. What to keep doing

The authoring standard in `docs/CONTENT_REVIEW.md` (holding branch) works. Where it was
applied, the pages are good: observable competencies, worked examples with the reasoning
shown, self-checks with real answers, three-level rubrics, honest scope statements. The
CI validators catch the drift they were built to catch. The Neuronauts story's sourcing
discipline (confidence badges, numbered receipts) is the model the rest of the site should
follow. The plan in `docs/planning/NEXT_CONTENT_PASS.md` is about applying the existing
standard to the layers that were generated or framed rather than authored.
