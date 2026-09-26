# Site audit, September 2026: front door and site shell

*Scope: `index.html`, `about.md`, `start-here.md`, `license.md`, `initiatives.md`,
`initiatives/**`, `connectivity.md`, `kb.md`, `concepts/**`, `open-problems/**`,
`modes/**`, `book/**`, `education/**`, `frameworks/**`, the copy in `_includes/**` and
`_layouts/**`, and `_data/{navigation,modes,core_surfaces,open_problems,concepts,connectivity}.yml`.
Audited 26 September 2026 on `compass-workshops`. Not committed.*

## Summary

23 files edited. 58 issues fixed: 22 accuracy, 17 polish, 14 voice, 5 missing content.

`book/`, `education/` and `frameworks/` hold only redirect stubs to `/neuronauts/` and
`/models/`. They are correct and were left alone.

Real-world facts were checked against primary sources: Crossref records for every DOI
in scope, and the publisher, Nature, FlyWire, UChicago, NIH and JHU/APL pages for
program facts. Site counts were checked against the repository.

Checks after editing: `validate_frontmatter`, `validate_code_span_paths`,
`validate_toggled_classes`, `validate_figure_refs`, `validate_technical_evidence` and
`validate_paper_counts` all pass. The six `_data` files in scope parse as YAML. A
permalink check of every internal link in scope finds no missing targets and no
links to redirect stubs. A full Jekyll build was not run, because other agents are
editing the tree at the same time.

## Most important accuracy fixes

1. **Wrong DOIs.** Four in scope pointed to unrelated papers:
   - The EyeWire "Nature 2014" link resolved to a quantum-optics paper; it now points to Kim et al., `10.1038/nature13240`.
   - The FlyWire link on `initiatives.md` ended in `-9`; it now ends in `-y`.
   - The "X-ray Connectomics, NeuroImage 2020" link resolved to a concussion study and was removed.
   - The Kornfeld and Denk review in the EM imaging callout pointed to an NMDA-receptor paper; it now points to `10.1016/j.conb.2018.04.030`.
2. **MICrONS scale.** The page said ">100,000 neurons". The 2025 Nature paper reports
   more than 200,000 cells, about 0.5 billion synapses, and about 75,000 functionally
   imaged neurons. The "Inhibitory Structure, Cereb. Cortex 2024" milestone was a
   third-party analysis (Reimann et al.) and is replaced by the MICrONS Nature 2025 paper.
3. **Misattributions on `initiatives.md`:**
   - CONFIRMS (a JHU/APL toolkit) was credited to NSF NeuroNex. It now sits on the APL card.
   - X-ray holographic nanotomography was credited to Argonne. It was done at the ESRF (Kuan et al., 2020). The card now separates Argonne microtomography (Dyer et al., 2017) from the ESRF work.
   - DVID was listed as a public NIH data archive and is removed.
   - H01 was listed as a BRAIN CONNECTS milestone. It is now labeled a field paper from Harvard and Google.
   - FlyWire and EyeWire were described as "gamified proofreading completing whole-brain Drosophila connectomes". EyeWire traced mouse retina.
   - The Max Planck card is now credited to the right labs.
4. **PEEM partnership.** The page named Argonne as a partner. The partners are Chicago
   State, UChicago and UIC. The gigahertz pixel rate is now stated as what simulations
   and experiments suggest. An unverified "student pipeline" claim is removed.
5. **EyeWire overclaim.** The page said citizen scientists "discovered the circuit mechanism" for direction selectivity. It now says what the paper reports: a bipolar-to-starburst wiring pattern that supports a wiring model.
6. **Wrong project name.** The homepage said the site is supported "through the Mouse Connectome Project". About, CITATION and the ecosystem page all say HI-MC (UM1NS132250). The homepage and footer now say HI-MC.
7. **Start Here datasets.** "MICrONS: large-scale mouse brain" is now "about 1 mm³ of
   mouse visual cortex". "Kasthuri 2015: mouse visual cortex" is softened to "mouse
   neocortex" (see Outside my area). All three cards now link to their catalog pages.
8. **Stale counts and stale "not yet" text:**
   - The content library holds 35 entries, not 33.
   - The workshop mode said "the track pages are the closest thing to a syllabus". The 10- and 16-week syllabus maps now exist, and the text says so.
   - Start Here's first hour had the Unit 01 lab done in 15 minutes. The lab is 60 minutes, so the step now starts the brief rather than finishing it.

## Changes

| File | Issue | Type | Fix |
|---|---|---|---|
| index.html | "cubic millimeters of mouse and human cortex"; "maps exist for ... a fly" | accuracy | About 1 mm³ each; "adult fly brain" |
| index.html | Method of the Year claim | accuracy | Verified (Nature Methods, EM-based connectomics, 2025); wording tightened |
| index.html | "Supported ... through the Mouse Connectome Project" | accuracy | HI-MC (MouseConnects), linked to About |
| index.html | "AI colors in every neuron and finds every synapse"; "settle decades-old debates"; "seamless" | voice/accuracy | Plain, bounded wording that states the models make mistakes and what wiring cannot show |
| index.html | "Why This Work Matters": three generic, adjective-led claims | voice | Replaced with checkable claims: graded labs, 25 kits, ten workshops, syllabus maps, CC BY/MIT |
| index.html | Em-dash chain in the story lede; "quietly become an industry" | voice | Split into short sentences; hype removed |
| about.md | "neighbouring", "practises", "licence page" | polish | American spelling |
| about.md | HI-MC described twice (Where this sits / Who runs it) | polish | Second instance trimmed |
| about.md | Teaching bullet omits Pathways workshops and syllabus maps | missing | Linked |
| about.md | braininitiative.nih.gov now 301-redirects to nih.gov/brain | polish | Link updated |
| start-here.md | "Two things a page cannot give you" above three cards | polish | Reworded |
| start-here.md | First-hour step 4 implied the 60-minute lab fits in 15 minutes | accuracy | Now "start the artifact" and links the lab |
| start-here.md | Kasthuri "visual cortex"; MICrONS "large-scale mouse brain" | accuracy | Corrected; cards link to catalog pages; dataset catalog linked |
| start-here.md | Both framework links went to /models/; "evidence-based" asserted | polish/accuracy | One models link; Pathways workshops linked; evidence left to the models page |
| start-here.md | "embark on your neuroscience adventure!"; "relatable entry point for diverse learners" | voice | Rewritten; closing CTA points to "Your first hour" |
| start-here.md | Hyphen ranges "0-10 min" | polish | En dashes |
| license.md, nav, footer | "Licence" | polish | "License" (American English) |
| _layouts/default.html | "Proudly developed ...", "NeuroTrailblazers.org" | voice/accuracy | Footer names HI-MC and the licenses |
| initiatives.md | Wrong DOIs, misattributions, MICrONS scale (see above) | accuracy | Rewritten card by card; every DOI checked on Crossref |
| initiatives.md | "powering the corpus", "that built modern connectomics", "Pioneering", "empowering trailblazing" | voice | Removed; intro links to Training Elsewhere |
| initiatives.md | CIRCUIT "for first-generation and underrepresented students" (unverified) | accuracy | Replaced with the verified program structure |
| initiatives/outreach.md | EyeWire DOI and overclaim; ">250,000 players" | accuracy | Correct DOI; bounded claim; "200,000+" (Nature, Oct 2024: over 225,000) |
| initiatives/outreach.md | FlyWire "280+ researchers, 76 labs, 139,000 neurons" | accuracy | 287 researchers, 76+ labs, 33 person-years, 139,255 neurons |
| initiatives/outreach.md | BigNeuron "standardized metrics across thousands of neurons" (unsourced) | accuracy | Replaced with the Nature Methods 2023 citation; noted it is a benchmark, not citizen science |
| initiatives/outreach.md | Janelia card claims scholars work with FlyEM teams | accuracy | Softened: depends on the host lab |
| initiatives/outreach.md | MBL "legendary", "connectomics graph theory", "EM bootcamps" | accuracy/voice | Real course name and scope; links Training Elsewhere |
| initiatives/outreach.md | NWB "seamless co-registration of connectomes" | accuracy | States what NWB does and does not store |
| initiatives/outreach.md | NeuroTrailblazers card: "research-incubator network", "OCAR graph", "capstone pathways" | accuracy | Replaced with what exists: nine units, 2,000-paper journal club, 25 kits, ten workshops |
| connectivity.md, _data/connectivity.yml | programme, neighbour, modelling, catalogue, behaviour, judgement, labour | polish | American spelling. The proper name "CAJAL ... Training Programme" is kept |
| _data/connectivity.yml | Hyphens used as dashes; "n/a - this is funding" | polish | Parentheses; "Not applicable" |
| _data/connectivity.yml | K99 entry named without "to Promote Diversity", which its URL points to; "the standard route" | accuracy | Real award name; states that earlier announcements are listed as expired |
| _data/connectivity.yml | Unquoted colon broke YAML after the edit | polish | Quoted |
| kb.md | iframes used root-absolute `/assets/...` (breaks under a baseurl); no titles | polish | `relative_url`; `title` attributes |
| kb.md | Description in internal jargon; page ends with no next step or limits | voice/missing | Plain description; new "What these maps do not show" section with next links |
| concepts/index.md | "Modules remain available as delivery objects, but discovery is concept-first" | voice | Explains what a card gives and links the module library |
| _data/concepts.yml | Five links to /frameworks/ redirect stubs (irrelevant to the concepts); two without a trailing slash | polish | Pointed to provenance, reconstruction-pipeline and journal club pages |
| _data/concepts.yml | Hidden-curriculum and mentoring cards pointed "activity" to /start-here/ and "slides" to non-slide pages | accuracy/missing | Now the Orientation and Building Your STEM Entourage workshop plans and worksheets, Lab Norms and the facilitator guide |
| _includes (concept card, need explorer) | "User need(s):" labels | voice | "Useful when:" and "What you are trying to do:" |
| _includes/callouts/em-imaging-visual-note.html | Kornfeld and Denk DOI wrong | accuracy | Corrected |
| _includes/ui (lesson map, teaching materials, evidence pack, interactive lab) | "realistic outputs", "verify competency", "classroom-ready", "canonical ... required preparation" | voice | Plain verbs |
| _data/modes.yml | Workshop limit: "track pages are the closest thing to a syllabus" | accuracy (stale) | Points to the syllabus maps and the short sequence |
| _data/core_surfaces.yml | "33 entries" | accuracy | 35 |
| _data/open_problems.yml | "localisation"; "the field's central open question"; the hook generalized a fly-only result | polish/voice/accuracy | "localization"; "one of"; the hook is scoped to the fly visual system as the deep dive sources it |

Verified and left unchanged:
- Counts: 9 units, 25 modules, 25 session kits, ten Pathways workshops, 127 dictionary terms, 2,000 papers in three tiers, 8 hidden-curriculum pages, 7 open problems.
- Each module deck carries an instructor-script comment, so Start Here's "a deck with speaker notes" holds.
- Award numbers, and HI-MC PI and scope.
- Hemibrain, FAFB, SBF-SEM, Helmstaedter 2013, Oh 2014, BigNeuron, the ASEE 2023 and Current Protocols 2025 DOIs, and syGlass arXiv.
- EN.585.781 lectures 7–9.

## Needs owner decision

1. **NIH funding links in `_data/connectivity.yml`.** All of `braininitiative.nih.gov`
   now 301-redirects to the `nih.gov/brain` landing page, so the BRAIN Training Program
   and K99 deep links no longer reach their pages. The "verified 2026-09-15" stamp on
   those entries could not be reproduced (the NIH pages return 403 to automated checks).
   The K99 entry is the award "to Promote Diversity", and the NINDS R25 is the diversity
   R25. The current status of both after NIH's 2025 changes to diversity-focused
   programs could not be confirmed. Decide whether to keep, re-link or remove the three
   funding entries.
2. **Author name.** It is spelled "Gray-Roncal" 19 times (About, CITATION.cff) and "Gray Roncal" 33 times (lecture citations, the eNeuro paper's own byline). Pick one for site copy.
3. **EyeWire player count.** Sources range from over 225,000 (Nature, October 2024) to about 350,000 (Wikipedia, 2025). The page now says "200,000+". Replace it if you have an official figure.
4. **The research-intensive mode.** It remains "not built". The copy is honest. Decide whether it stays on the mode picker or moves off the front door until it exists.

## Outside my area

- `_datasets/kasthuri-2015.md`: `region: "Visual cortex (neocortex)"`. Kasthuri et al. 2015 is described by BossDB and secondary sources as mouse somatosensory cortex. Verify against the paper's methods and correct it; Start Here now says only "mouse neocortex".
- `_config.yml` line 93 (`grant: "Mouse Connectome Project"`) and `_data/track_catalog.yml` line 27 ("Mouse Connectome Project ... datasets"): these conflict with HI-MC / MouseConnects everywhere else.
- `LICENSE` uses "licence" throughout; the site standard is American English. It is a legal text, so change it only deliberately.
- `scripts/corpus_curation/classify_engine.py` line 23 uses `10.1038/s41586-024-07558-9` for FlyWire. The correct DOI is `...-07558-y`.
- `_includes/cards/concept-card.html` prints the raw track slug ("core-concepts-methods") where the track title belongs. This is a small Liquid lookup, left alone because template restructuring is out of scope.
- `content-library/index.md` still says "Entries also carry older `reference_images` front matter ... being replaced". Check whether that is stale.
