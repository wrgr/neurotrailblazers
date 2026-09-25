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
- [x] `about.md`: who runs the site, the BRAIN CONNECTS context with award numbers (from the currently unused `_data/connects_learning_map.yml`), how to contact (render `site.email`), how to report an error. *(Complete. HI-MC's own award, `UM1NS132250`, was looked up in NIH RePORTER — NINDS, 2023-09-08 to 2028-08-31, PI Jeff W. Lichtman, Harvard — and its dates corroborate the site's existing "2023–2028" for MouseConnects. It is now on the page, in `CITATION.cff` and in `connects_learning_map.yml`, whose `hi_mc` entry was the only one without an award. Contributors: Will Gray-Roncal and Sydney Floryanzia, plus an open invitation. No role or affiliation is published for anyone whose role has not been stated.)*
- [x] `LICENSE` (recommend CC BY 4.0 for content, MIT for code) and a short `license.md` page; state it in the footer.
- [x] `CITATION.cff` and a "Cite this site" block on `about.md` and the journal-club page.
- [x] `CONTRIBUTING.md` on the deployed branch (move or summarise the content standard from `holding/internal-planning`).
- [x] Footer: links to About, Contact, Licence, GitHub, Accessibility; keep it to one line of links.
- [x] Nav: "About" → `/about/`.

**Done when:** a stranger can find out who made the site, on what terms they may reuse it, and how to tell someone it is wrong, within two clicks of any page.

### 2.2 One message, one name per thing (S–M)
- [x] Choose the site line. Recommended: **"Mapping connections. Making connections."** (see `docs/brand/BRAND_GUIDE.md` §2 for the alternatives). Retire "Illuminating Pathways for Trailblazing Neuroscience Research(ers)" from title, footer, config. *(The line was already in `_config.yml`, the home `<title>` and the footer; the last remnant was the unused `tagline_lines` block, which still carried the retired research-incubator framing and the word "audacious" that the brand voice forbids. No template read it, so it is deleted rather than rewritten.)*
- [x] Choose the positioning sentence: "IC3 and APEX organize and expose the science. NeuroTrailblazers organizes the learning." Move it from `core/connects-ecosystem.md` to the home page mission block and `about.md`. *(`about.md` already carried it. The home mission block now leads with it and its heading states the claim instead of reading "Our Mission"; the paragraph beneath says what "organizing the learning" concretely means — a course, a reference layer, session kits — and links the ecosystem page. It stays on `core/connects-ecosystem.md` too, which is where a reader arrives asking the question it answers.)*
- [x] Home hero: eyebrow, H1, body and mission should name the same audience in the same order (students → mentors → programs). *(The hero already did; the mission block did not name an audience at all. It now runs students → mentors → programs in that order.)*
- [x] `start-here.md:4`: "computational neuroscience" → "nanoscale connectomics". *(Already corrected; verified no "computational neuroscience" remains as a description of this program.)*
- [~] One label for the technical course everywhere. Recommended: **"Technical Course"** in nav and buttons, "Unit NN" for the parts. Apply in `_data/navigation.yml`, `technical-training/index.md`, `index.html`, `_data/track_catalog.yml`, `teaching/index.md`, `initiatives/outreach.md`. *(All six named files done, plus the drift they did not list: `_data/technical_track.yml` (`name:` was "Technical Connectomics Track"), `_includes/ui/technical-track-roadmap.html`, the atlas page's "Technical Training hub", and `avatars/index.md`. "Technical Unit NN" is now "Unit NN" throughout `track_catalog.yml`. The "Technical Track Journal Club" label — 26 pages — is now just "Journal Club": the journal club is its own surface, not a sub-brand of the course. `_includes/ui/track-progression.html` was deleted; it duplicated the roadmap include and had zero callers.* ***Still open:*** *`modules/module22.md:63` still reads "Technical Training: Nanoscale Connectomics". The ten Marp decks carried the same label on their title slides; the Workstream 5 authoring pass replaced it with "Technical Course · Unit NN" and re-rendered.)*
- [x] One name for the Neuronauts story across `neuronauts/index.html:3`, nav, home and `/book/`. Recommended: **"The Neuronauts Expedition"**. *(Already consistent in all four: both page titles, the nav dropdown entry and the two home buttons. The nav's top-level "Neuronauts" is the section, not the story, and is left as is.)*
- [~] One title pattern for pages: bare noun phrase; move SEO tails into `description`. *(The genuine SEO tails are gone: `tools/index.md` "Technical Connectomics Tools" → "Tools", `tools/ask-an-expert.md` "Ask An Expert: Dr. Jeff Lichtman" → "Ask an Expert", `proofreading-tutorials.md` dropped "& Community Practice Guide", and `atlas-connectomics-reference.md` "Atlas: Connectomics Reference" → "Connectomics Reference Atlas", which is what the nav already called it. Two of those descriptions were rewritten in the same pass: the Ask an Expert one claimed insight "straight from the source" from what the page itself discloses is an AI chatbot, and the tutorials one opened with "Master".* ***Still open:*** *the `Type: Name` prefix convention — 25 `Session Kit: Module NN: …` titles, three `Track: …`, two `Side Quest: …`, eleven `Journal Papers: …`. Those are a prefix, not a tail, and the session kits are generator output, so changing them is a generator change plus a regeneration rather than an edit.)*
- [x] Persona names: one form in front matter, H1 and start-here cards ("Julian, first-generation undergraduate"). *(Front matter and the start-here cards already agreed. The divergence was `teaching/facilitator-guide.md`, which used an em-dash form with its own descriptors — "Maya — graduate student bridging computation and biology", "Dr. Nguyen — faculty mentor". All four headings now carry the canonical comma form; the extra nuance was already in the body text beneath each.)*

### 2.3 Collapse the frameworks / models triplication (M)
- [x] Merge `frameworks/index.md`, `models.md` and `education/models.md` into one `/models/` page with MERIT, Professional Pathways and CCR as sections. *(The operational playbook from `education/models.md` became `/models/`; the summary page it duplicated is gone.)*
- [x] Redirect the other seven paths; delete the five existing redirect stubs that pointed into the old structure. *(Stubs kept, not deleted: `_includes/ui/related-content.html` generates `/frameworks/<slug>/` URLs from `related_frameworks` front matter, so they are load-bearing. All seven now point at `/models/`, and twelve pages were repointed to link there directly rather than hop through a redirect.)*
- [x] Remove the six pasted `ui/learning-tracks.html` blocks from pages where they are filler (`avatars/index.md`, `tools/index.md`, `frameworks/index.md`, `models.md`, `education/models.md`, `datasets/index.md`). *(Two went with the merge; the other four removed. The include had no remaining callers and was deleted — the tracks are in the nav and on `/tracks/`.)*

- [x] **Follow-up, now done:** `_data/track_catalog.yml` still listed a "Frameworks" resource
  pointing at `/frameworks/` in two of its three track sections, hopping the redirect the merge
  left behind. Both now point at `/models/` and are titled "Program Models" — which exposed that
  one of the two sections was listing the same page twice under both names, so the duplicate is
  gone.

### 2.4 Navigation and tools (S)
- [x] Add `/modes/`, `/concepts/`, `/kb/` and the ecosystem page to the nav (Tracks and Core dropdowns respectively).
- [x] Give `/tools/` an honest identity: list the site's own interactives (citation graph, KB visualisations, concept explorer, module labs, kids quiz) and move "Ask an Expert" under a Help heading with a human fallback (the contact route from 2.1). *(The page now separates the three things that get called a tool: the seven interactives that run here, the third-party software you will actually run (pointing at the atlas and the access guide), and help. "Ask an Expert" is out of the tool grid and under "Getting help", stated as an AI chatbot that is not Dr. Lichtman and needs a ChatGPT account, above the human route — `site.email` and the issues tracker from 2.1. Title is now "Tools".)*
- [x] Add `aria-hidden="true"` to every `.card-icon`; strip emoji from headings and buttons in `neuronauts/kids.md` and `initiatives/outreach.md` (replace with the line icons from the brand guide when available). *(All nine `.card-icon` divs already carried `aria-hidden`. Emoji removed from every heading and button on both pages: three hero buttons, four section headings, nine quiz option buttons and three sub-headings on the kids page; three section headings, six card headings, the closing sub-heading and three footer buttons on the outreach page. Kept deliberately: the five Neuronaut character avatars, the story tags and the inline analogy markers on the kids page, which are illustration for that audience rather than heading or button furniture. No line-icon set has been drawn yet — the brand guide names Lucide or Phosphor but `assets/brand/` ships none — so headings simply lose the emoji, which is what §6 asks for regardless.)*
- [x] **Also in this pass:** one name and one route for Ask an Expert. Eight pages wrote it
  "Ask-an-Expert", and seven of those linked `/tools/ask-an-expert/` — a redirect stub — rather
  than the page itself. All now read "Ask an Expert" and link `/ask-an-expert/` directly. The nav
  called the atlas "Atlas & Reference" in the Core dropdown and "Connectomics Reference Atlas" in
  the Technical Course dropdown; both now use the latter, which is also the page's new title.

### 2.6 Connectivity: the outward training landscape (S, added after the fact)

- [x] **New page `/connectivity/`, not in the original plan.** The review's §2 missing-pages
  list has "Events", and Workstream 4 wants a funding-and-jobs landscape, but nothing on the
  site told a learner what training exists *elsewhere*. Three pages were adjacent and none
  of them answered it: `core/connects-ecosystem.md` is the programme structure this site is
  funded inside, `initiatives.md` is the research consortia, `initiatives/outreach.md` is
  citizen science. Twelve entries across four categories — connectome-data training, intensive
  schools, open platforms, funding routes — each with an explicit `boundary:` field saying what
  it covers that this site does not. Neuromatch, CAJAL, INCF, MBL, CSHL, FlyWire Academy and the
  Allen educators' workshop appeared nowhere in the repository before this.
  *(Built to the `community_resources.yml` verification rule: every entry checked against the
  provider's own site, `verified:` records the date, and the date renders on each card. The
  file carries no deadlines or session dates — a `cadence:` field says when to look instead,
  because a stale date is worse than no date. The page header names the three neighbouring
  pages and what each one owns, so this does not become the frameworks/models triplication
  that 2.3 just finished collapsing. The entry count in the opening sentence is summed from
  the data in Liquid rather than typed, per the open Workstream 6 stat-literal item.
  `connectivity.md` was added to `validate_frontmatter.rb`'s globs so it is gated like the
  rest.)*
  ***Still open:*** *this covers the funding half of the Workstream 4
  `hidden-curriculum/career-mechanics.md` companion — who funds the next step — but not the
  jobs half: where a trained proofreader actually goes. That item stays open.*

### 2.5 Make the personas load-bearing (S)
- [x] **Persona Pathfinder, added after the fact:** `start-here.md` carried four bare cards —
  a persona name in an `<h3>` and nothing else — which is about as un-load-bearing as a persona
  can be. They are now a four-tab pathfinder, one tab per persona, each opening with the
  decision that persona's own page says they face and then four concrete steps with links.
  Rebuilt rather than ported from `graphrev`, which had a version of this idea built on an
  invented learner/researcher/educator/developer taxonomy that would have put a second set of
  personas on the site. Proper `tablist` semantics with arrow/Home/End keys, no emoji, colours
  from the existing `:root` variables so it migrates with workstream 5 rather than adding to
  the hex backlog. Every link target and every factual claim in it was checked — including
  "a deck with speaker notes", which only became true with 3.1 above.
- [x] Home pathway cards name a persona and link `/avatars/`. *(Three of the five audience cards already named their persona and deep-linked the avatar page; the other two — "Just Curious" and "For Programs & Funders" — have no persona to name, and inventing one would be worse than the gap. The section now links `/avatars/` from its standfirst, which was previously the marketing line "Purpose-built experiences for the people who move neuroscience forward".)*
- [x] Each `tracks/*.md` page opens with "This track is for Julian and Maya" style callouts. *(Already present on all three track pages as a **Who this is for** paragraph naming two personas each, with links. Verified rather than rewritten.)*
- [x] Kids portal: link back to the story, deep-link each of the five story cards to its paper, surface the 3D-print assets, link the 25-minute classroom activity. *(All four done. The story link and the 3D-print assets were the two that were genuinely missing — the STLs existed and only `neuronauts/index.html` linked them, so a kid arriving at the Junior Lab could not find them. Each of the five story cards now links its named papers by DOI, and says which are free to read: seven of the nine are open access, and the two that are not — Januszewski et al. 2018 and White et al. 1986 — are labelled "behind a paywall" rather than linked as if a reader could open them. The 25-minute activity was already linked from the teacher card. Two fixes found in passing: the stories section still advertised the "500 Key Papers" collection that Workstream 0 corrected at line 366 but not here, and the page title carried an SEO tail ("Neuronauts Junior Lab: Connectomics for Kids & Young Explorers").)*

---

## Workstream 3: instructional layer

### 3.1 Finish the module derivatives (M)
- [x] `_data/module_interactives.yml`: author per-module quiz and microtask for modules 10–25 (16 modules; keep the documented `correct_index` distribution). *(64 new items; correct_index 21/21/22, and no module has all four answers at one index. Note the review's diagnosis was wrong and is corrected there: the include suppressed the section entirely rather than showing filler, so those 16 pages had no interactive layer at all.)*
- [x] Speaker notes as HTML comments in all 25 `course/decks/marp/modules/*.marp.md` (the generator should emit a notes block from the run-of-show). *(The generator now splits the run-of-show into its two levels: the timing spine goes on the slide, the instructor script goes in the note. This was not only a missing-notes problem — module 01's run-of-show slide was a nineteen-bullet wall of verbatim script against a four-bullet deck standard. All 25 spines are now 5-7 bullets and 23 of 25 carry a note; modules 14 and 15 write the whole step on one line with nothing beneath it, so there is genuinely no third level to move, and they get a split at the first sentence instead. Two related defects fixed in the same pass: the "Agenda (60 min)" slide was hardcoded identically on all 25 decks and contradicted each module's real timings, so it is gone and the run-of-show slide carries the real one; and that slide was titled "60-Minute Run-of-Show" on every deck including modules 01-03, whose own pages head the section "Detailed run-of-show (90 minutes)" — the length is now read off the page.)*
- [x] Either build or delete the three phantom resources in `teaching/module22-public-engagement.md` ("Atlas vs. Connectome", "BRAIN Grant Detective", "Public Impact Wall"). *(Already resolved: none of the three names appears anywhere in the repository outside this plan and the review that raised it. Verified rather than rewritten.)*
- [x] Add `track:` front matter to `teaching/module22-public-engagement.md` and `teaching/projectome-to-synapse.md`. *(Already present on both — `track: career-and-community`. Verified rather than rewritten.)*
- [x] Delete `modules/slides/*.md` (25 link-wrapper pages) once the session kits carry the same four links. *(Precondition verified first: the session kit at `/teaching/sessions/moduleNN/` carries the same four links — rendered deck, Markdown source, worksheet, module page — alongside the prep, timing, misconceptions and rubric that make it worth opening. The 25 wrappers are gone and the generator no longer emits them. `/modules/slides/` survives as a redirect to the session kits index so nothing that linked it 404s, but the 25 per-module URLs are removed outright rather than stubbed. Five referrers repointed: the deck footer and the worksheet footer in the generator, `_includes/ui/module-teaching-materials.html` (which now offers the session kit where it offered the wrapper), `_includes/cards/teaching-module-card.html` (the wrapper link dropped; it already listed the rendered deck and the source beside it), and the generator-output tables in `README.md` and `CONTRIBUTING.md`. The nav lost its "Module Slides" entry: it sat directly beneath "Session Kits" under Teaching, pointing at a second index of the same 25 modules. The worksheet footers cited the dead path inside backticks, which is why `check_site_links.rb` did not flag them — worth knowing about that gate.)*

### 3.2 Close the module content gaps (L)
- [ ] Worked examples for modules 02, 03, 05, 07, 16, 17, 18, 19 (07 Proofreading and 18 Data Cleaning first).
- [ ] Bring modules 20 and 21 to five misconception guardrails; bring 02, 03, 16, 20, 21 above 2,300 words with content, not padding.
- [ ] Add "Why this module matters" to 04–11; "What this module does not cover" and "Common errors" to 02, 03, 05, 07, 16, 17, 18, 19; references to 15–25.
- [ ] Retitle module 22 to "Scientific Presentation"; add scope-boundary cross-references 17↔22, 08↔20, and module↔unit pairs (01↔U01, 05↔U03, 06+07↔U08, 12↔U04, 04↔U05–07, 10+13↔U09).
- [ ] One run-of-show heading form; state where the other 2–4 declared hours go on every module page.

### 3.3 Technical units (M)
- [x] Self-checks: bring units 04, 06, 07, 08 to three questions each, in the existing `<details>` pattern. *(Seven new questions, each placed at the end of the section it tests and closing on a generalizable principle like the ones already there. 04 §5: a one-layout storage plan, answered from the §3 access-pattern table and the §5 cost traps. 06 §4: "direction errors only add noise, so our enrichment is conservative" — it is a bias toward the finding. 07 §1: which results move when a glia merge is removed; 07 §3: "OPC, not sure" as a label standing in for a confidence level. 08 §2: an empty merge queue measures the detector, not the segmentation; 08 §4: rewriting "all 200 cells were proofread" into a level, a stopping rule and an endpoint shift. Every number in the answers is one the unit page already states.* ***Not in scope but noticed:*** *units 03 and 09 are still at two each.)*
- [~] Figures: use the 21 unused extracted assets (five each for units 03 and 04 first); raise unit 07 above three figures for three glial classes. *(Counted fresh: 22 files under `assets/images/technical-training/` were embedded on no unit page, four of them byte-identical copies of another file. Seventeen are now placed, each viewed first and captioned for what it actually shows, tied to a numbered section of its unit: five on unit 03 (4 → 9), five on unit 04 (4 → 9), two on 02, one each on 01 and 08, three on the atlas. Unit 07 goes from 3 to 6 with three H01 renders via `figure.html` — an astrocytic process under the astrocyte table, the myelin mask under the oligodendrocyte section, a vessel after the worked example — each located by H01's own label layers, not by eye, so all three glial classes now have at least one figure.* ***Left unplaced, deliberately:*** *the stock "brain on a chip" image (two copies; no teaching content), two duplicates of images now shown on unit 03, and `FIG-RIV-ULTRA-S23-01` (labels F, D, S and asterisks with no surviving legend, so it cannot be captioned without guessing). Still open: microglia has only the one RIV thumbnail, and no oligodendrocyte soma is shown anywhere — `render_em_figures.py` would need a nucleus-mask query for one.)*
- [x] One duration model per unit: "self-study N h; taught session 90 min; deck 60 min" stated in one place and propagated. *(The "Before you start" Time row on all nine units now states all three: self-study, summed from `time_estimate` (2.5–4.5 h); the taught session, from that unit's lecture plan (85–100 min, not a flat 90); and the Marp deck, 60 min on all nine, noted as not following the plan slide for slide, which is what the lecture plans themselves say. `_data/technical_track.yml` and `technical_capabilities.yml` carry no durations, so there was nothing to contradict there. `validate_technical_evidence.rb` now fails if a unit's Time row disagrees with its `time_estimate` or the estimate stops parsing; both fault-injected. The atlas has no Time row and is left without one, being reference.* ***Found, not fixed:*** *six of the ten lecture plans' per-slide minutes do not sum to their own stated lecture length (04 sums to 76 against 80, 05 to 80 against 75, 06 to 76 against 75, 07 to 76 against 70, 09 to 80 against 85, atlas to 60 against 55). Which number is right is a teaching-design call, so it is left for whoever owns the plans.)*
- [x] One heading for the graded artefact ("Lab") or make `technical-capability-brief.html:33` read the unit's own term. *(Took the include route. Renaming 05's "Studio activity" and 07's "Drill" to "Lab" would have broken the deep links in `_data/concepts.yml` that point at those headings, and lost two descriptions that are accurate — a consensus round is a studio, a timed confusion-matrix exercise is a drill. Units 05, 07 and the atlas now carry `graded_exercise:` front matter; the include reads it with "lab" as the default, and its own h3 is now "Capability exercise" so it no longer repeats unit 05's heading. `validate_technical_evidence.rb` fails if a page's `graded_exercise` term matches none of its headings.)*
- [x] `technical-training/index.md`: badge the atlas as Reference (or filter it from the unit grid); surface `time_estimate`, `level`, `prerequisites` per card and the ~31 h total; link the proofreading tutorials from the CTA row. *(The badge, time and level were already on the cards. Added prerequisites, read from each unit's front matter like the others, and a "Proofreading Tutorials" button in the CTA row. The hardcoded "31 hours" is now summed in Liquid from the nine `time_estimate` strings, so the total cannot drift from the cards; rendered with the vendored Liquid 4.0.4 to confirm it still produces 31.)*
- [~] `proofreading-tutorials.md`: add the figures the title promises (false merge, false split, orphan, at minimum) and remove the inline-style/emoji formatting. *(Rewritten as Markdown sections on the site's existing hero and section classes: zero `style=` attributes and zero emoji, down from 113 and 16. False merge has a confirmed example — H01's before/after, where the right answer comes from one of its 104 proofread cells. Also fixed in the rewrite: the page had merges and splits labelled the wrong way round ("False Merges (Over-Segmentation)"), synapse numbers that disagreed with Unit 05 (now Unit 05's), a table-of-contents link to a section that did not exist, a FlyWire Academy description that contradicted the verified `connectivity.yml` entry, and three unsourced figures — detector false-positive rate "5–15%", webKnossos at "up to 1 mm/hour", a "<60°" hairpin rule — which are removed rather than sourced. The Neuroglancer key-binding list is also gone: bindings differ between deployments, and nothing in the repo let the list be checked against any of them.* ***Still open:*** *the false-split figure is H01's c2-vs-c3 pair, which shows the merge-or-split decision but not a confirmed split, because H01 does not say which call is right for that object, and the caption says so. The orphan figure shows where orphans come from (a spine across a thin neck), not a confirmed one. Both need a new render from `proofread_104` against `c2`: a proofread cell that `c2` holds in two or more segments is a confirmed split, and the pieces are confirmed orphans. `tensorstore` is not installed here, so that render was not attempted.)*

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

- [x] `content-library/infrastructure/synapse-detection.md` (L). Cleft prediction, partner assignment, E/I classification, benchmarks, cross-dataset degradation. Repoint `_data/open_problems.yml:53`. *(~4,500 words. Every number sourced; the CREMI weighting formula, gap-junction figures and MICrONS detector accuracy are named as unsourced in the page's own does-not-cover section rather than asserted.)* *(Reframed after review by the site owner: detection is a solved problem, and the page now opens by saying so. The three residuals it is actually about are asymmetric recall — H01 missed 35% of inhibitory synapses — partner assignment in polyadic cases, and cross-dataset transfer, which is why the site's own open problem is titled "synapse detection **that generalizes**".)*
- [x] `content-library/connectomics/ethics-and-governance.md` (M). Consent for human tissue, de-identification, dual use, data licences, credit for proofreaders. Module 19 links here instead of owning the material. *(~3,250 words. H01's provenance from the Science full text, with the ethics statement located in the supplementary methods rather than implied absent; portal licences with the obligations each imposes; FlyWire's 33 person-years and consortium authorship as the credit worked example.)* *(Reframed after review by the site owner: connectomics has no current human-subjects problem, and the page now says that first. Live today are licence compliance and credit for proofreading labour; consent at whole-brain scale, de-identification, neural-data regulation and dual use are set out as a prospective seminar rather than a compliance checklist.)*
- [ ] `content-library/case-studies/microns-visual-cortex.md` rewrite (M): co-registration, functional-unit matching, what calcium data does and does not license.
- [ ] `content-library/connectomics/comparative-connectomics.md` (M): what transfers across worm, fly, mouse, human and what does not.
- [ ] `content-library/imaging/beyond-em.md` (M): expansion microscopy, X-ray nanotomography, barcoding (MAPseq, BARseq), array tomography, LICONN, with the one-slide contrast case from the graduate decks as the framing.
- [ ] `content-library/infrastructure/provenance-and-versioning.md` expansion (S): it is the thinnest page and the most-linked norm.
- [ ] `content-library/cell-types/neuron-type-identification.md` figures and expansion (S).
- [ ] Figures on all four `imaging/` pages, `artifact-taxonomy.md` first (M; the H01 render pipeline exists). Then clear the 32 pages' `reference_images:` front matter of figures that will not be produced.
- [x] `content-library/index.md:166-177`: real destinations for the three orphaned domains; link `computer-vision-ml.md`; decide whether `mri-connectomics.md` stays given `methodology.md:44`. *(Every domain now links to a journal-club filter that really contains its papers; six filter links had used dimension values absent from the data and silently did nothing. All 13 topic pages linked. `mri-connectomics.md` stays, relabelled as a bridge out of the library for readers arriving from the macroscale side.)*
- [x] Datasets timeline: add BANC, MANC, larval zebrafish, whole-mouse-brain efforts (after 1.4). *(BANC, MANC, FANC and larval zebrafish added in 1.4; whole-mouse-brain efforts are still open.)*
- [ ] `hidden-curriculum/career-mechanics.md` companion: the funding and jobs landscape (S–M).
- [ ] `_data/concepts.yml`: grow from 12 concepts to cover the units and library (M; the explorer UI is already built).

---

## Workstream 5: decks and brand rollout

See `docs/brand/BRAND_GUIDE.md` for the system. The Marp theme
(`course/decks/marp/theme/neurotrailblazers.css`), template deck
(`course/decks/marp/neurotrailblazers-template.marp.md`) and PowerPoint template
(`assets/brand/NeuroTrailblazers-slide-template.pptx`) ship with this plan.

- [x] Link the three `en585781` decks from `technical-training/slides/index.md` and from units 01–04, 08, 09 (S). Highest value-per-minute item in the whole plan.
  *(Completed 24 September 2026: each of the six unit pages now carries a "Graduate lecture"
  line in its Course links section, pointing at the rendered deck and Markdown source that
  cover it — module07 (Introduction to Connectomics) for units 01–02, module08 (Tools and
  Methods) for units 03–04, module09 (Algorithms and Applications) for units 08–09, matching
  the pairing the decks themselves describe. `validate_technical_evidence.rb` and
  `validate_code_span_paths.rb` re-run clean.)*
- [~] Rebuild the ten technical-unit decks on the `neurotrailblazers` theme from the unit pages, with speaker notes and a source line per figure; fill or delete the empty slides in 04, 07 and the atlas (L). Rename the `en585781/module0N-*` files so they do not collide with curriculum module numbers. *(Partly done: all ten now declare the brand theme, carry a title-class opener and a per-unit footer, use the `figure` class where a slide is heading-plus-image, and the two empty slides are filled with real content. **Authoring pass done 24 September 2026:** all 66 embedded figures now carry a `<p class="source">` line. The 17 H01 renders cite the release, CC BY 4.0 and Shapson-Coe et al. 2024 as `_data/em_figures.yml` does; the 43 `RIV-*`, `Module1N L*` and Techtalk extractions cite their source deck in the unit pages' own attribution wording ("Pat Rivlin training materials (MICrONS proofreading deck)", "assets_outreach source decks", 2021 techtalk, historical/context); the six Wikimedia/PLOS images cite file page and licence from `assets/images/external/ATTRIBUTION.md`. 107 speaker-note blocks, in the HTML-comment convention of the module decks, carry the unit pages' worked examples and numbers. The 20 slides that ran off the frame — measured in headless Chrome, not guessed; the worst, 07's Wikimedia glia diagram, ended at y=1576 of 720 — are now two-column or figure-with-caption, and the same measure puts all 175 slides inside the frame with the source line clear of the content. 04's heading-only "pipeline overview" slide now carries Module14 L1 S04; 06's one-bullet "High-complexity edge case" was folded into the protocol slide. Headings that contradicted their image were retitled from what the image shows: 05's "dendritic context" is a soma (the unit page already said so), 06's "continuity check case" is a PSD scaffold schematic, 09's "analysis workflow overview" is a simulated legged agent. Three images that did not belong went: 02's stock brain-on-a-chip and fused-car pictures gave way to the H01 four-scale ladder, and 08's unrelated raw-EM "metrics" image became the unit's metric blind-spot table. The "External paper figure slots (add in final teaching run)" placeholders are reading lists with DOIs from the atlas references. Title slides now read "Technical Course · Unit NN".* ***Provenance trace, 24 September 2026:*** *two of the five flagged figures are now
confirmed, by citation search, to be copyrighted third-party work with no open licence —
this is the one item on this list that is a rights question, not a documentation one.
RIV-AXDEN-S18 is Figure 3 of Sheng M, Kim E (2011), "The Postsynaptic Organization of
Synapses," *Cold Spring Harb Perspect Biol* 3(12):a005678, doi:10.1101/cshperspect.a005678
— caption text matched verbatim — © Cold Spring Harbor Laboratory Press, all rights
reserved. It is used three places, not one: the 06 deck slide, `technical-training/06-axons-and-dendrites.md:353`,
and `technical-training/08-segmentation-and-proofreading.md:410` (the last under a caption
that describes a different image, confirming the mismatch this list already noted). RIV-GLIA-S03
is a screenshot of synapseweb.clm.utexas.edu/astrocytes (SynapseWeb, Kristen M. Harris Lab, UT
Austin), byline "by Rachel E. Ventura" confirmed on the live page — © The University of
Texas at Austin, no reuse licence stated. Both deck source lines now carry the full citation
and a "confirm permission before this deck is shared outside the course" caveat rather than
the vague "historical/context" framing; **the two unit-page embeds are unchanged and still
need the same decision** (replace, seek permission, or restrict to internal use) — that is
a call for whoever owns external relationships for this course, not one to make unilaterally.
RIV-ULTRA S04 and S20 and Module14 L3 S13 remain unconfirmed after a real attempt — S13's
panel layout (network graph, ΔF/F traces, EM-to-graph pipeline, four synapse examples,
an excitatory connectivity matrix) matches the hallmark figure of Lee et al. 2016, *Nature*
532:370–374, "Anatomy and function of an excitatory network in the visual cortex," but the
paper is paywalled and this was not confirmed panel-for-panel; treat that as a lead, not a
citation. All three, plus the Techtalk and Module12 framing images, need either reverse-image-search
tooling or a person who recognizes the original 2021 techtalk / Module12 source decks — text
search cannot confirm an image with no legible caption.* ***Resolved, not a bug:*** *the
byte-identical `FIG-RIV-ULTRA-S11-01` / `FIG-RIV-AXDEN-S11-01` pair is a deliberate dual
extraction, not a mislabel — `course/units/figures/06-axons-and-dendrites-selected-v1.md:6`
and `08-segmentation-and-proofreading-selected-v1.md:8` independently select it for each unit
under a different topical framing ("axon-related classification cue" vs. "vesicle/organelle
features"), meaning Pat Rivlin's original training materials reused the same image on slide 11
of both the axon/dendrite deck and the ultrastructure deck. Both IDs are correct.* ***Fixed:***
*`ATTRIBUTION.md` now names Holly Fischer (source: open.umich.edu "Second Look Series") for
`glial-cell-types.png` and Wikimedia user Marashie for `feed-forward-motif.gif`, and both
decks' on-slide source lines now carry that author credit, which CC BY 3.0 / CC BY-SA 3.0
require and the previous "Wikimedia Commons" wording did not supply.* ***Still open:*** *the
unit-page caption fixes noted above, and the en585781 rename.)*
- [x] **Found while rendering, now fixed:** `scripts/render_marp.sh` produced
  machine-dependent output. Marp derives the `<html lang>` attribute from the process
  locale, so CI's `LC_ALL=C.UTF-8` stamped `lang="POSIX"` into all 39 committed decks —
  not a valid BCP 47 tag, so assistive technology cannot select a voice from it — while
  any developer machine with a real locale emitted `en-US`. Re-rendering with sources
  untouched therefore churned 848 lines across every deck, in whichever direction the
  last person's locale pointed, burying real content changes. The script now pins
  `LANG`/`LC_ALL`, so the output is a function of the sources alone, and the decks carry
  a correct `lang`. Still unpinned, and noted in the script: marp-cli stamps its own
  version into every output, and the repo installs it with `--no-save` and no
  `package.json`, so a CLI upgrade rewrites all 39 files.
- [ ] Move the 25 module decks from `theme: default` to `theme: neurotrailblazers` in the generator; re-render (S).
- [ ] Port `frontiers.css` to the brand palette or retire it in favour of the shared theme (S).
- [ ] Web: import `assets/brand/brand-tokens.css`; migrate the 56 legacy `--neural-blue` / `--cerebral-purple` / `--axon-cyan` uses (70 when this plan was written; the count drifts with every stylesheet edit, so re-count before starting) and the 60-plus hardcoded Tailwind hex values to `--nt-*` tokens; delete the legacy `:root` block and the `colors:` block in `_config.yml` (M).
- [ ] Replace `favicon.ico` with `assets/brand/nt-favicon.svg` (plus a 32 px PNG fallback); add `<link rel="icon">` to the layout; add the social card as `og:image` (S).
- [ ] Header: replace the text logo with `nt-lockup-horizontal.svg`; consider dropping the full-width banner image from interior pages (S).
- [ ] Drop the unused Plus Jakarta Sans from the font request; add Barlow Condensed 700 for display headings (S).
- [ ] Replace emoji icons with the line-icon set described in the brand guide (M, after 2.4).

---

## Workstream 6: lock it in (CI)

- [x] Validator: no empty `authors`, no "Consortium" citation, year agrees with corpus (1.1). *(Delivered with 1.1 in `validate_paper_counts.rb`.)*
- [x] Validator: track `module_numbers` ⊆ sequenced modules; hours reconcile (1.3). *(Delivered with 1.3 in `validate_frontmatter.rb`.)*
- [x] Validator: `technical_capabilities.yml` ↔ unit pages; in-page "Course links" ↔ `technical_track.yml` (1.3). *(Delivered with 1.3 in `validate_technical_evidence.rb`.)*
- [x] Validator: no `{{` or `{: #` in generated worksheets; every worksheet rubric has criteria (1.2). *(`scripts/validate_generated_materials.rb`, wired into CI. Accepts both rubric forms in use — criteria inline after the tier label, or nested beneath it — and fails when a tier has neither. Both failure modes fault-injected.)*
- [x] Validator: every `*.marp.md` under `course/decks/marp/` declares a theme; no slide body is empty (5). *(Same script. It immediately caught the ten unthemed technical decks and the two committed empty slides, which are fixed rather than exempted.)*
- [x] **Validator, added after 3.1:** site paths written inside backtick code spans resolve
  to a real page (`scripts/validate_code_span_paths.rb`). `check_site_links.rb` scans only
  `href=` and `src=`, so a path written as prose-with-monospace is invisible to it — deleting
  the 25 `modules/slides/moduleNN` pages left all 25 worksheet footers citing the dead path
  in a code span and the link audit still passed. Scope is narrow on purpose: only strings
  with both a leading and trailing slash count as site URLs, so repo paths (`scripts/foo.rb`)
  and asset references are ignored, and an `NN`/`<placeholder>` marks a pattern rather than a
  link. Zero findings on current content. Verified by injecting the original fault and
  confirming this gate fails while `check_site_links` stays green, plus a bogus path and a
  placeholder to check both directions.
- [x] **Interaction defect, found and fixed after the fact: the AI synthesis modal covered
  the whole site.** `technical-training/journal-club/index.md:104` ships the modal with
  `class="... hidden"` and an inline `style="position:fixed; inset:0; display:flex;
  z-index:1000"`. The only `.hidden` rule in the entire stylesheet was `.jc-card.hidden`,
  so the class matched nothing on this element: the overlay rendered on page load, before
  anyone asked for a prompt, and swallowed every click on the site nav underneath it. Its
  close button added a class no rule listened to, so it could not be dismissed — the page
  was unusable without a reload. Three other elements had the same defect and were also
  permanently visible: `jc-empty` ("No papers match your filters") sat under a full grid of
  results, and both copy-confirmation toasts were always on screen.
  *(Fixed with one global `.hidden { display: none !important; }` utility.* ***The
  `!important` is load-bearing, not defensive:*** *a normal author declaration cannot
  override an inline `display:flex`, and an important one can, so this is the only form of
  the rule that actually closes the modal. Verified in headless Chrome: with the rule
  removed the modal computes `display:flex` and `elementFromPoint` over the nav returns the
  overlay; with it, the modal is `none` and the nav is hit-testable again. The modal also
  gained Escape and backdrop-click dismissal plus `role="dialog"`/`aria-modal`, and all six
  dismissal cases — including "a click inside must NOT close" — pass in the browser.)*
- [x] **Second instance of the same class, fixed:** `technical-training/dictionary/index.md`
  toggles `is-active` on its 8 category filter buttons and no rule for it existed anywhere,
  so the 127-term dictionary filtered correctly while giving no indication of which category
  was selected. `.dict-cat.is-active` added, with a `:focus-visible` ring.
- [x] **Validator: a class that JS toggles must have a CSS rule somewhere.** Both defects
  above are the same failure and neither was catchable by any existing gate — every
  validator in CI reads text, and nothing has ever opened a page in a browser.
  `scripts/validate_toggled_classes.rb`, wired into the scripts job.
  *(The check is* ***specificity-aware, not a name grep****, which is the whole difficulty: a
  grep for "is `hidden` in the stylesheet?" passes the modal defect, because `.jc-card.hidden`
  contains the name. So for every element carrying a toggled class in its markup, some
  compound selector mentioning that class must have all of its classes present on that
  element — `.hidden` satisfies anything, `.jc-card.hidden` only satisfies a card. A class
  with no static carrier (JS builds the element) falls back to "does any rule mention it",
  which is all that is knowable without running the page. Both original faults were
  re-injected and confirmed to fail the gate.)*
- [x] **Third instance, found by the new gate and fixed.** The AI synthesis modal's four
  prompt-mode buttons — on both `journal-club/index.md` and `journal-club/graph.md` —
  toggled an `active` class that no rule anywhere matched, and carried their selected state
  as inline `background`/`color`/`font-weight` that the click handler rewrote on every
  button on every click. Not a rendering fault like the other two, since the inline styles
  did paint: a dead class next to eleven lines of JS doing a stylesheet's job, in a file
  whose sibling `.jcg-tier-btn.active` and `.jc-tab.active` had always done it in CSS.
  `.jc-pmode-btn.active` and `.jcg-pmode-btn.active` now own the state, the inline `style`
  attributes are gone from all eight buttons, and each handler is one line.
  *(Verified in headless Chrome on both pages: exactly one button selected, selected and
  unselected distinguishable in background and weight, and a click moving the selection.
  The three findings the gate reported alongside these were false positives from the first
  draft and are the reason it now understands that `toggle(cls, force)`'s second argument is
  a condition, not a class — `toggle('active', type === 'citation')` had it demanding a
  `.citation` rule.)*
- [ ] **The stronger version, still open:** no smoke test loads a real page, clicks the
  interactive controls and asserts the nav is still reachable. The gate above is a static
  approximation of it. `puppeteer-core` is in `node_modules` and was used by hand for the
  verification above, but nothing in CI opens a browser — and note that the Jekyll build
  cannot currently be run on this machine at all (`bundle` wants 2.6.9 against the system
  Ruby 2.6), so any browser gate has to live in the build job, not the scripts job.
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
