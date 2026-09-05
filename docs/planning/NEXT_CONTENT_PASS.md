# Next content pass: work plan

*Derived from `docs/reviews/2026-09-site-content-review.md` (5 September 2026). Written
to be worked through incrementally: every item is a checkbox with a size, a definition of
done, and the files it touches. Tick items here as they land; do not delete them.*

Sizes: **S** under half a day · **M** one to three days · **L** a week or more of focused
work. Sizes assume one person who knows the repository.

Order of the workstreams is deliberate. Workstream 0 is a single afternoon and removes
every verified factual error. Workstream 1 fixes data that renders wrong. Nothing in
workstreams 2–5 should ship before 0 and 1 are done, because they would be building on
numbers and generated files that are currently incorrect.

---

## Workstream 0: quick wins (one afternoon, all S)

Each is a one-line or one-file change with no design decision required.

- [x] `_data/core_surfaces.yml:31`: "191 papers" → 2,000 (tiered 500 / 1,000 / 2,000).
- [x] `_data/core_surfaces.yml:10`: "45 entries across 8 topic areas" → the real count (33 across 7), or state the counting rule.
- [x] `index.html:83`: "25 min" → "about 40 min".
- [x] `initiatives.md:35`: H01 DOI → `10.1126/science.adk4858`.
- [x] `datasets/index.md:217-225`: split the merged Bock/Briggman 2011 card into two correct cards (Bock: visual cortex, ssTEM; Briggman: retina, SBEM).
- [x] `datasets/index.md:106,107,324` and `content-library/case-studies/h01-human-cortex.md:90,176`: one H01 cell count and one synapse count, sourced.
- [x] FlyWire synapse count "50+ million" → ~54.5 M in `datasets/index.md:156,346` and the three journal-paper pages.
- [x] `neuronauts/kids.md:366`: "500 Key Papers" → the 2,000-paper corpus.
- [x] `neuronauts/index.html:2221`: "tell us" → a real contact route (see 2.1; interim: the GitHub issues URL).
- [x] `models.md:67,84`: point the two circular `/frameworks/` links at the sections they describe.
- [x] `teaching/index.md:58`, `modules/index.md:64`: `site.modules` → `site.data.modules` (or delete the block). Verify the Teaching Hub grid renders.
- [x] `_layouts/default.html:6-7`: delete the manual `<title>` and description; `{% seo %}` emits both.
- [x] `_layouts/default.html:17`: `alt=""`, `width`, `height` on the decorative banner.
- [x] `_layouts/redirect.html:12-13`: move the canonical link into the head (or drop it).
- [x] "35 exports came to 88 MB" in 11 `technical-training/slides/*.md` files → 38, or derive from the manifest.
- [x] `technical-training/journal-club/index.md:20,27,62,135`: "12 domains" → 14, or derive from data.
- [x] `course/decks/marp/en585781/README.md:9-13`: slide counts 59 / 56 / 58.
- [x] `technical-training/05-neuronal-ultrastructure.md:14,25`: one time estimate.
- [x] `modules/module12.md:241`: replace the `TBD` cells or drop the row.
- [x] Trailing slashes on `/datasets/mouseconnects` and `/datasets/workflow` links (`datasets/index.md:68,84,85` and ~15 module pages).
- [x] Delete dead files: `_includes/head-custom.html`, `assets/images/neurotrailblazers-banner.png`, `assets/images/nt-favicon.png`, the `avatars` and `datasets` collection declarations in `_config.yml`, the stale nav mirror at `_config.yml:71-95`, `tagline_lines[0]`.
- [x] `core/index.md:80-105`: add the Neuroanatomy for Proofreaders side-quest card.

**Done when:** the build is green, `check_site_links.rb` passes, and a grep for each old
string returns nothing.

---

## Workstream 1: data integrity and generators

### 1.1 Regenerate `_data/journal_papers.yml` from `corpus_2000.json` (M)
- [x] Write `scripts/derive_journal_papers.py`: join on DOI (1,980 match), carry `authors`, correct `year`, full journal name, `abstract`; drop the "NeuroTrailblazers Consortium" citation template in favour of a real first-author citation.
- [x] Rebuild `_data/paper_views/era.json` (the era facet is currently built on wrong years).
- [x] Extend `scripts/validate_paper_counts.rb`: fail if any entry has empty `authors`, a citation containing "Consortium", or a year that disagrees with the corpus.
- [x] Reconcile `content-library/journal-papers/methodology.md:16,69` with what actually ships.

**Done when:** the journal club renders real author names, sorts by correct year, and the validator would catch a regression.

### 1.2 Fix the teaching-material generator (S code, then regenerate) 
- [x] `scripts/generate_module_teaching_materials.rb:89` (`rubric_lines`): keep indented criteria under each tier; emit them nested in worksheets and decks.
- [x] `:83` (`inline_labelled`): also accept a `### Scenario` heading; reject kramdown IAL captures.
- [x] Resolve Liquid `relative_url` filters at generation time so worksheets contain plain paths.
- [x] Normalise the Studio activity block in modules 01, 02, 03, 05 to the inline `**Scenario:**` + numbered steps form.
- [x] Regenerate; diff one worksheet by eye (module 13 is a good test: 11 criteria should reappear).

**Done when:** all 25 worksheets show rubric criteria, none contains `{: #` or `{{`, and module 05's go/no-go scenario is back.

### 1.3 Reconcile the three module metadata sources (M)
- [x] `_data/track_catalog.yml`: add modules 06 and 07 to a Research-in-Action step (`:133`), module 02 to a Career & Community step (`:195-211`); replace the 15 h and 20 h budgets with sums of module `duration:` front matter or split into "taught" vs "self-study" hours. *(Chose total learner hours throughout: every step `hours:` is now the same quantity module `duration:` front matter declares. Module-bearing steps carry `modules:` and `module_hours:`; the three `time_estimate` ranges were raised to match. Convention documented at the head of the data file.)*
- [x] Fix the Unit 08 and Unit 09 course-link mismatches against `_data/technical_track.yml` (see review §1.A.5). *(The data file was right in both cases; the pages were corrected.)*
- [x] Extend `scripts/validate_frontmatter.rb`: every `module_numbers` entry appears in a sequence step; step hours reconcile with declared durations; `technical_capabilities.yml` entries match unit pages. *(Track-catalogue gates in `validate_frontmatter.rb`; the unit-page gates — Course links ↔ `technical_track.yml`, `technical_capabilities.yml` ↔ unit pages — in `validate_technical_evidence.rb`, which already owns that data file.)*

**Done when:** a learner following any track sees hours that match the pages, and CI fails on the next drift.

### 1.4 Datasets as a real collection (M)
- [x] Create `_datasets/` with one file per dataset and a fixed schema: species, region, volume, neurons, synapses, size, resolution, modality, portal, paper DOI, access tier, release year, site pages using it. Start with H01, MICrONS, FlyWire, Hemibrain, MANC, BANC, C. elegans, larval zebrafish, MouseConnects. *(14 records created, covering everything the page already described. Schema documented at the collection declaration in `_config.yml`; permalink `/datasets/catalog/:name/` to avoid colliding with the hand-written guides. MANC, BANC and larval zebrafish are NOT yet in the catalogue — adding them means sourcing their numbers from the papers, and inventing them was the failure mode this workstream exists to fix. See the follow-up below.)*
- [x] Migrate the hand-written cards out of `datasets/index.md`; render Featured and Timeline from the collection so numbers cannot diverge. *(597 lines to 194. Featured grid, timeline and each dataset page now read one record.)*
- [x] Make the home page "5+ datasets" stat read the collection length. *(Now renders 14.)*

**Done when:** `datasets/index.md` contains no dataset numbers as literals. *(Done.)*

- [x] **Follow-up, now done:** `_datasets/manc.md`, `_datasets/banc.md`, `_datasets/fanc.md`
  and `_datasets/larval-zebrafish.md` added, sourced from the papers in this project's own
  `_data/corpus_2000.json`. FANC carries its published counts (14,600 cell bodies, ~45 M
  synapses, Azevedo et al. 2024). MANC, BANC and larval zebrafish deliberately carry **no**
  neuron or synapse counts: the corpus abstracts do not state them, and each record says so
  in its `source:` field rather than asserting a number it cannot cite. Anyone with the
  papers to hand should fill those in. The catalogue now holds 18 datasets.

---

## Workstream 2: front door and framing

### 2.1 About, contact, licence, citation (M)
- [x] `about.md`: who runs the site, the BRAIN CONNECTS context with award numbers (from the currently unused `_data/connects_learning_map.yml`), how to contact (render `site.email`), how to report an error.
- [x] `LICENSE` (recommend CC BY 4.0 for content, MIT for code) and a short `license.md` page; state it in the footer.
- [x] `CITATION.cff` and a "Cite this site" block on `about.md` and the journal-club page.
- [x] `CONTRIBUTING.md` on the deployed branch (move or summarise the content standard from `holding/internal-planning`).
- [x] Footer: links to About, Contact, Licence, GitHub, Accessibility; keep it to one line of links.
- [x] Nav: "About" → `/about/`.

**Done when:** a stranger can find out who made the site, on what terms they may reuse it, and how to tell someone it is wrong, within two clicks of any page.

### 2.2 One message, one name per thing (S–M)
- [ ] Choose the site line. Recommended: **"Mapping connections. Making connections."** (see `docs/brand/BRAND_GUIDE.md` §2 for the alternatives). Retire "Illuminating Pathways for Trailblazing Neuroscience Research(ers)" from title, footer, config.
- [ ] Choose the positioning sentence: "IC3 and APEX organize and expose the science. NeuroTrailblazers organizes the learning." Move it from `core/connects-ecosystem.md` to the home page mission block and `about.md`.
- [ ] Home hero: eyebrow, H1, body and mission should name the same audience in the same order (students → mentors → programs).
- [ ] `start-here.md:4`: "computational neuroscience" → "nanoscale connectomics".
- [ ] One label for the technical course everywhere. Recommended: **"Technical Course"** in nav and buttons, "Unit NN" for the parts. Apply in `_data/navigation.yml`, `technical-training/index.md`, `index.html`, `_data/track_catalog.yml`, `teaching/index.md`, `initiatives/outreach.md`.
- [ ] One name for the Neuronauts story across `neuronauts/index.html:3`, nav, home and `/book/`. Recommended: **"The Neuronauts Expedition"**.
- [ ] One title pattern for pages: bare noun phrase; move SEO tails into `description`.
- [ ] Persona names: one form in front matter, H1 and start-here cards ("Julian, first-generation undergraduate").

### 2.3 Collapse the frameworks / models triplication (M)
- [x] Merge `frameworks/index.md`, `models.md` and `education/models.md` into one `/models/` page with MERIT, Professional Pathways and CCR as sections. *(The operational playbook from `education/models.md` became `/models/`; the summary page it duplicated is gone.)*
- [x] Redirect the other seven paths; delete the five existing redirect stubs that pointed into the old structure. *(Stubs kept, not deleted: `_includes/ui/related-content.html` generates `/frameworks/<slug>/` URLs from `related_frameworks` front matter, so they are load-bearing. All seven now point at `/models/`, and twelve pages were repointed to link there directly rather than hop through a redirect.)*
- [x] Remove the six pasted `ui/learning-tracks.html` blocks from pages where they are filler (`avatars/index.md`, `tools/index.md`, `frameworks/index.md`, `models.md`, `education/models.md`, `datasets/index.md`). *(Two went with the merge; the other four removed. The include had no remaining callers and was deleted — the tracks are in the nav and on `/tracks/`.)*

### 2.4 Navigation and tools (S)
- [x] Add `/modes/`, `/concepts/`, `/kb/` and the ecosystem page to the nav (Tracks and Core dropdowns respectively).
- [ ] Give `/tools/` an honest identity: list the site's own interactives (citation graph, KB visualisations, concept explorer, module labs, kids quiz) and move "Ask an Expert" under a Help heading with a human fallback (the contact route from 2.1).
- [ ] Add `aria-hidden="true"` to every `.card-icon`; strip emoji from headings and buttons in `neuronauts/kids.md` and `initiatives/outreach.md` (replace with the line icons from the brand guide when available).

### 2.5 Make the personas load-bearing (S)
- [ ] Home pathway cards name a persona and link `/avatars/`.
- [ ] Each `tracks/*.md` page opens with "This track is for Julian and Maya" style callouts.
- [ ] Kids portal: link back to the story, deep-link each of the five story cards to its paper, surface the 3D-print assets, link the 25-minute classroom activity.

---

## Workstream 3: instructional layer

### 3.1 Finish the module derivatives (M)
- [ ] `_data/module_interactives.yml`: author per-module quiz and microtask for modules 10–25 (16 modules; keep the documented `correct_index` distribution).
- [ ] Speaker notes as HTML comments in all 25 `course/decks/marp/modules/*.marp.md` (the generator should emit a notes block from the run-of-show).
- [ ] Either build or delete the three phantom resources in `teaching/module22-public-engagement.md` ("Atlas vs. Connectome", "BRAIN Grant Detective", "Public Impact Wall").
- [ ] Add `track:` front matter to `teaching/module22-public-engagement.md` and `teaching/projectome-to-synapse.md`.
- [ ] Delete `modules/slides/*.md` (25 link-wrapper pages) once the session kits carry the same four links.

### 3.2 Close the module content gaps (L)
- [ ] Worked examples for modules 02, 03, 05, 07, 16, 17, 18, 19 (07 Proofreading and 18 Data Cleaning first).
- [ ] Bring modules 20 and 21 to five misconception guardrails; bring 02, 03, 16, 20, 21 above 2,300 words with content, not padding.
- [ ] Add "Why this module matters" to 04–11; "What this module does not cover" and "Common errors" to 02, 03, 05, 07, 16, 17, 18, 19; references to 15–25.
- [ ] Retitle module 22 to "Scientific Presentation"; add scope-boundary cross-references 17↔22, 08↔20, and module↔unit pairs (01↔U01, 05↔U03, 06+07↔U08, 12↔U04, 04↔U05–07, 10+13↔U09).
- [ ] One run-of-show heading form; state where the other 2–4 declared hours go on every module page.

### 3.3 Technical units (M)
- [ ] Self-checks: bring units 04, 06, 07, 08 to three questions each, in the existing `<details>` pattern.
- [ ] Figures: use the 21 unused extracted assets (five each for units 03 and 04 first); raise unit 07 above three figures for three glial classes.
- [ ] One duration model per unit: "self-study N h; taught session 90 min; deck 60 min" stated in one place and propagated.
- [ ] One heading for the graded artefact ("Lab") or make `technical-capability-brief.html:33` read the unit's own term.
- [ ] `technical-training/index.md`: badge the atlas as Reference (or filter it from the unit grid); surface `time_estimate`, `level`, `prerequisites` per card and the ~31 h total; link the proofreading tutorials from the CTA row.
- [ ] `proofreading-tutorials.md`: add the figures the title promises (false merge, false split, orphan, at minimum) and remove the inline-style/emoji formatting.

### 3.4 Course shell (M)
- [ ] `teaching/syllabus.md`: 16-week, 10-week and 2-day mappings of modules + units + lectures onto sessions.
- [ ] Pacing notes: which modules pair into one session, which need two, what to cut for a workshop.
- [ ] Assessment bank: an item pool per unit beyond the inline quiz; a calibration instrument, since the facilitator guide calls calibration "the metric that matters".
- [ ] Answer keys or model responses for the 25 worksheets (one exemplar each, marked at the "Proficient" level).
- [ ] Instructor FAQ (the questions students actually ask about EM, segmentation error, nulls).
- [ ] The "artifact reference card" module 05 refers to.

### 3.5 One runnable notebook (M)
- [ ] Build one Colab notebook against the MICrONS public release from the Step 3 code already in `notebooks/connectome-quality/index.md`; pin the materialization version; link it from units 04, 08, 09 and open problem 1.
- [ ] Delete `assets/notebooks/module*/` `.gitkeep` directories.

---

## Workstream 4: reference layer

New pages, each written to the `docs/CONTENT_REVIEW.md` standard (numbers, worked
judgement, what the page does not cover, go-deeper links). Seed papers already exist in
`_data/expert_seed_papers/` for all of them.

- [ ] `content-library/infrastructure/synapse-detection.md` (L). Cleft prediction, partner assignment, E/I classification, benchmarks, cross-dataset degradation. Repoint `_data/open_problems.yml:53`.
- [ ] `content-library/connectomics/ethics-and-governance.md` (M). Consent for human tissue, de-identification, dual use, data licences, credit for proofreaders. Module 19 links here instead of owning the material.
- [ ] `content-library/case-studies/microns-visual-cortex.md` rewrite (M): co-registration, functional-unit matching, what calcium data does and does not license.
- [ ] `content-library/connectomics/comparative-connectomics.md` (M): what transfers across worm, fly, mouse, human and what does not.
- [ ] `content-library/imaging/beyond-em.md` (M): expansion microscopy, X-ray nanotomography, barcoding (MAPseq, BARseq), array tomography, LICONN, with the one-slide contrast case from the graduate decks as the framing.
- [ ] `content-library/infrastructure/provenance-and-versioning.md` expansion (S): it is the thinnest page and the most-linked norm.
- [ ] `content-library/cell-types/neuron-type-identification.md` figures and expansion (S).
- [ ] Figures on all four `imaging/` pages, `artifact-taxonomy.md` first (M; the H01 render pipeline exists). Then clear the 32 pages' `reference_images:` front matter of figures that will not be produced.
- [ ] `content-library/index.md:166-177`: real destinations for the three orphaned domains; link `computer-vision-ml.md`; decide whether `mri-connectomics.md` stays given `methodology.md:44`.
- [ ] Datasets timeline: add BANC, MANC, larval zebrafish, whole-mouse-brain efforts (after 1.4).
- [ ] `hidden-curriculum/career-mechanics.md` companion: the funding and jobs landscape (S–M).
- [ ] `_data/concepts.yml`: grow from 12 concepts to cover the units and library (M; the explorer UI is already built).

---

## Workstream 5: decks and brand rollout

See `docs/brand/BRAND_GUIDE.md` for the system. The Marp theme
(`course/decks/marp/theme/neurotrailblazers.css`), template deck
(`course/decks/marp/neurotrailblazers-template.marp.md`) and PowerPoint template
(`assets/brand/NeuroTrailblazers-slide-template.pptx`) ship with this plan.

- [ ] Link the three `en585781` decks from `technical-training/slides/index.md` and from units 01–04, 08, 09 (S). Highest value-per-minute item in the whole plan.
- [ ] Rebuild the ten technical-unit decks on the `neurotrailblazers` theme from the unit pages, with speaker notes and a source line per figure; fill or delete the empty slides in 04, 07 and the atlas (L). Rename the `en585781/module0N-*` files so they do not collide with curriculum module numbers.
- [ ] Move the 25 module decks from `theme: default` to `theme: neurotrailblazers` in the generator; re-render (S).
- [ ] Port `frontiers.css` to the brand palette or retire it in favour of the shared theme (S).
- [ ] Web: import `assets/brand/brand-tokens.css`; migrate the 70 legacy `--neural-blue` / `--cerebral-purple` / `--axon-cyan` uses and the 60-plus hardcoded Tailwind hex values to `--nt-*` tokens; delete the legacy `:root` block and the `colors:` block in `_config.yml` (M).
- [ ] Replace `favicon.ico` with `assets/brand/nt-favicon.svg` (plus a 32 px PNG fallback); add `<link rel="icon">` to the layout; add the social card as `og:image` (S).
- [ ] Header: replace the text logo with `nt-lockup-horizontal.svg`; consider dropping the full-width banner image from interior pages (S).
- [ ] Drop the unused Plus Jakarta Sans from the font request; add Barlow Condensed 700 for display headings (S).
- [ ] Replace emoji icons with the line-icon set described in the brand guide (M, after 2.4).

---

## Workstream 6: lock it in (CI)

- [ ] Validator: no empty `authors`, no "Consortium" citation, year agrees with corpus (1.1).
- [ ] Validator: track `module_numbers` ⊆ sequenced modules; hours reconcile (1.3).
- [ ] Validator: `technical_capabilities.yml` ↔ unit pages; in-page "Course links" ↔ `technical_track.yml` (1.3).
- [ ] Validator: no `{{` or `{: #` in generated worksheets; every worksheet rubric has criteria (1.2).
- [ ] Validator: every `*.marp.md` under `course/decks/marp/` declares a theme; no slide body is empty (5).
- [ ] Validator: stat literals on the home page and `core_surfaces.yml` are derived from data, not typed.
- [ ] Render `last_reviewed` on pages (it is set on 40 pages and shown on none), and add a "what's new" page fed from git history or a changelog file.

---

## Suggested sequencing

| Sprint | Contents | Outcome |
|---|---|---|
| 1 | Workstream 0; 1.1; 1.2; 5 (link en585781 decks, favicon, tokens import) | No known wrong numbers; journal club correct; worksheets usable; brand visible |
| 2 | 1.3; 2.1; 2.2; 2.4 | Site says one thing, is reachable, is citable |
| 3 | 3.1; 3.3; 1.4; 2.3; 2.5 | Teaching material teachable by someone other than its author |
| 4 | 4 (synapse detection, ethics, MICrONS first); 3.4; 3.5 | Reference layer covers the mission's own open problems |
| 5 | 5 (deck rebuild, CSS migration); 3.2; 6 | One visual system; drift caught in CI |
