# Content pass 2: modules 12–25 and the Module 22 retitle

Plan items from `docs/planning/NEXT_CONTENT_PASS.md` §3.2 for modules 12–25. Done 27
September 2026 on branch `compass-workshops`; nothing committed. Files edited:
`modules/module12.md` to `module25.md`, `_data/modules.yml` (Module 22 title only) and
this report. Generated files (`course/decks/marp/modules/module22.marp.md`,
`teaching/sessions/module22.md`, `assets/worksheets/module22/`) still carry the old
Module 22 title and regenerate from the module page; they were not hand-edited.

Hard constraint kept: studio activity task steps, section names and numbers in modules
17, 18, 19, 20, 21, 22 and 25 are unchanged (answer keys exist or are being written).

Method: a first run edited all fourteen pages and was cut off; this pass reviewed every
diff, verified each number against the kit file, paper or web page it cites, checked all
45 DOIs against Crossref (`api.crossref.org/works/<doi>`), and finished what was missing.
Web pages were read on 2026-09-27.

## Per-module log

### Module 12 (Data Systems and Cloud Infrastructure) — 4,081 words

- Verified from the first run: EM compression claim softened to "only a small factor,
  measure it yourself" (the old "2-10x" had no source); the derived-data footprint table
  is labeled this site's planning rule of thumb; run-of-show already in the
  `**MM:SS-MM:SS | Label**` form.
- Fixed: the time-budget sentence claimed "the 90-minute meeting the syllabus maps give
  this kit". Neither map schedules Kit 12 (`teaching/syllabi/16-week.md`, "What this map
  uses and omits": "Kits 12–16 and 18 are left out for time"). Rewritten to say so and to
  offer it as a lab meeting or take-home.
- Heading `## References` renamed `## Academic references` (the form modules 01–03 use).
- Numbers checked: the voxel arithmetic (250,000 × 250,000 × 25,000 = 1.56 × 10^15) and
  chunk-count arithmetic are derivations from the stated 4 × 4 × 40 nm voxel; dataset
  sizes were aligned to `canonical-facts.md` in the earlier audit and are unchanged.
- No new references (the existing six were verified in the earlier audit; all DOIs in the
  file resolve on Crossref, see the list at the end).

### Module 13 (Machine Learning for Connectomics) — 3,722 words

- Verified from the first run: the Unit 09 scope-boundary paragraph (13↔U09) links
  `/technical-training/09-connectome-analysis-neuroai/`, which exists; Unit 09 already
  links back to Module 13 in its "Related modules" line (`technical-training/09-...md:546`),
  so the pair is closed without editing the unit page. Run-of-show already in the labeled
  form. The worked example is labeled illustrative.
- Fixed: time-budget sentence (Kit 13 is not scheduled by either map; same source as
  Module 12). Heading renamed `## Academic references`.

### Module 14 (Deep Learning for EM Segmentation) — 3,832 words

- Verified from the first run: the ERL grounding. Januszewski et al. (2018) *Nat Methods*
  15:605–610, doi:10.1038/s41592-018-0049-4, abstract (read via Europe PMC on 2026-09-27):
  "we achieved a mean error-free neurite path length of 1.1 mm, and we observed only four
  mergers in a test set with a path length of 97 mm. The performance of flood-filling
  networks was an order of magnitude better than that of previous approaches applied to
  this dataset". The page quotes the 1.1 mm and "order of magnitude" phrases verbatim and
  labels the 10 / 100 / 1,000 µm bands "this site's rule of thumb for reading an ERL, not
  a published threshold" (closes owner decision 4 of the site audit).
- Verified: run-of-show converted from bold-time-only lines to `**MM:SS-MM:SS | Label**`
  with the detail on the next line (six steps).
- Fixed: time-budget sentence (Kit 14 unscheduled). Heading renamed.

### Module 15 (LLMs in the Connectomics Workflow) — 3,702 words

- Verified: run-of-show converted to the labeled form (six steps). Four references, all on
  Crossref; the Ji et al. page range was corrected from "248" to 1–38 (Crossref gives
  1–38 for the article, 248 is its article number). CAVE (Dorkenwald 2025) supports the
  version-pin gate; Schlegel 2024 is the paper the example literature prompt names.
- Fixed: time-budget sentence (Kit 15 unscheduled). Heading renamed.

### Module 16 (Visualization) — 3,881 words (target: above 2,300)

- Verified the worked example against the kit files, not the README: `celltype_synapses.csv`
  has 2,500 cells, median 36, maximum 1,089 at L5_09 → L5_05, 27 zeros; 2,257 cells
  (90.3%) are at or below 146; 3 cells exceed 800. `celltype_connections.csv` has 907
  cells under 10 pairs and a maximum of 433. `morphometry.py --sholl 10` gives 23 / 12 / 7
  intersections at 60 µm for basket / excitatory / chandelier.
- Fixed: the missing-cable sentence listed "0.08, 0.15 and 0.22" after naming the arbors in
  the order basket, excitatory, chandelier, which misassigns them; `neurons.csv` has
  excitatory 0.08, basket 0.15, chandelier 0.22. Each is now named.
- Verified: Concept 5's color-vision prevalence is scoped and cited. Birch (2012) *JOSA A*
  29(3):313, abstract: "the prevalence of deficiency in European Caucasians is about 8% in
  men and about 0.4% in women" (read 2026-09-27). Six references, all on Crossref.
- Verified: "Common errors and how to recover" (7) and "What this module does not cover"
  (6) present; five guardrails in belief form with "Why it fails".
- Fixed: time-budget sentence. The 16-week map does not meet on Kit 16; it lists it as a
  4-hour take-home (`teaching/syllabi/16-week.md:27-28`). Rewritten accordingly. Heading
  renamed.

### Module 17 (Scientific Writing) — 4,204 words

- Verified the worked example against `assets/kits/module16/input_synapses_by_layer.csv`:
  medians L2/3 861.5, L4 1,125.5, L5 1,133, L6 656; ratio 1.306; a 10,000-resample
  bootstrap of the ratio of medians with seed 1 gives a 95% interval of 1.02–1.57 (both
  Python `random` and NumPy seeds round to this).
- Verified: scope boundary with Module 22 present and reciprocal; "Common errors" (7) and
  "What this module does not cover" (7) present; eight guardrails each with "Why it
  fails". Six references, five on Crossref; Gopen & Swan (1990) has no DOI and the page
  says so, pointing to the USENIX-hosted reprint.
- Time budget: both maps schedule Kit 17 (16-week week 13, 10-week week 7), so the
  sentence stands. Heading renamed. Studio activity untouched (answer key exists).

### Module 18 (Data Cleaning and Preprocessing) — 4,145 words

- Verified the worked example directly from `assets/kits/module18/`: 30,450 rows; 447
  exact duplicates; 29,589 after duplicates, missing endpoints and autapses; score bins
  32–39 = 962, 64–71 = 428, 144–151 = 2,288; threshold 64 removes 5,315 (18.0%),
  threshold 96 removes 7,638 (25.8%). These match `teaching/answers/module18.md`.
- Verified: "Common errors" (7), "What this module does not cover" (6), six guardrails with
  "Why it fails". Five references on Crossref. The MICrONS detection figures quoted in the
  reference note (precision 96%, recall 89%) are canonical (`canonical-facts.md:69`).
- Fixed: time-budget sentence (Kit 18 unscheduled). Heading renamed. Studio untouched.

### Module 19 (Peer Review and Scientific Ethics) — 4,158 words

- Verified: worked example is an invented preprint with a fictional "Cortical Wiring
  Consortium" and is labeled as such; "Common errors" (7), "What this module does not
  cover" (6), six guardrails with "Why it fails"; the ethics-and-governance page link
  resolves. Five references on Crossref, plus COPE and ICMJE named as guidelines.
- Time budget: both maps schedule Kit 19 (16-week week 12, 10-week week 7); sentence
  stands. Heading renamed. Studio untouched.

### Module 20 (Statistical Models and Inference) — 3,496 words before this pass (target: above 2,300; five guardrails)

- Verified from the first run: five guardrails (Concepts 1–3 plus two new ones in Concepts
  4 and 5, the threshold and the directional-bias beliefs); the multiplicity decision
  table; the scope boundary with Module 08 (20→08). Module 08 does not yet link back
  (`grep -n module20 modules/module08.md` is empty); Module 08 belongs to the other
  agent's pass. Six references on Crossref; Artzy-Randrup 2004 is the comment on Milo
  2002, which is what the page uses it for.
- Added: "Why it fails" lines under the three older guardrails so all five share the
  16–19 format (the 16 × 0.05 = 0.8 line is arithmetic on the page's own 16-class
  census).
- Fixed: time-budget sentence now names the 16-week map, week 10, and says the 10-week map
  omits the kit. Heading renamed. Studio untouched.

### Module 21 (Reproducibility and FAIR) — 3,220 words before this pass (target: above 2,300; five guardrails)

- Verified from the first run: five guardrails; the five-elements table; Concept 5
  (deprecation path); the Module 17 / 22 split in "What this module does not cover". Six
  references on Crossref, including Wilkinson 2016 (doi:10.1038/sdata.2016.18).
- The worked example's fictional release labels T21 and T27 predate this pass and are
  referenced by `teaching/answers/module21.md`; left as they are (the "avoid" list applies
  to new examples).
- Added: "Why it fails" lines under the three older guardrails.
- Fixed: time-budget sentence (16-week map, week 12; 10-week omits). Heading renamed.
  Studio untouched.

### Module 22 (Scientific Presentation, retitled) — 3,812 words

- Retitle verified: `title: "Module 22: Scientific Presentation"`, `short_title:
  "Scientific Presentation"`, `_data/modules.yml` entry 22; permalink and slug unchanged.
  The page `description` still said "talks and written summaries"; now "talks ... with
  explicit question-handling norms", matching `modules.yml`. Body text never spelled the
  old title. `_data/navigation.yml` and `_data/sequences.yml` do not carry module titles.
  The only remaining spellings of the old title are in generated files
  (`course/decks/marp/modules/module22.marp.md`, `teaching/sessions/module22.md`,
  `assets/worksheets/module22/module22-activity.md`, and the rendered deck under
  `course/decks/marp/out/`), which regenerate from the page.
- Verified: scope boundary with Module 17 (22→17) and Module 17's reciprocal paragraph.
  Four references on Crossref (the two ASEE proceedings DOIs resolve; Crossref carries no
  year for them, the page gives the conference year).
- Time budget: both maps schedule Kit 22 (16-week week 14, 10-week week 8); sentence
  stands. Heading renamed. Studio untouched.

### Module 23 (Posters, Abstracts and Conferences) — 3,829 words

- Verified the venue numbers against the sources named on the page (read 2026-09-27):
  GRC About page, "Each conference is limited to 200 attendees; scientists must apply to
  the conference and be selected by the conference chair"; GRC policies, "a private
  communication from the individual making the contribution and is presented with the
  restriction that such information is not for public use" and "written approval of the
  contributing member must first be obtained"; SfN About page, "SfN's annual meeting
  regularly attracts more than 30,000 attendees". Closes owner decision 6 of the site
  audit. Poster type sizes are labeled this site's rule of thumb.
- Fixed: "About 180 spoken words, at a speaking pace of 120 words a minute" now states
  that 120 words a minute is the pace the module budgets on and tells the reader to time
  themselves. Time-budget sentence rewritten (neither map schedules Kit 23; the 16-week
  map says it overlaps Communicating Science). Heading renamed. Four references on
  Crossref.

### Module 24 (Career Pathways) — 3,982 words

- Verified: five references on Crossref (two NASEM reports by DOI, three surveys).
- Fixed: time-budget sentence (neither map holds a meeting on Kit 24; the 16-week map
  uses its decision table as 15 minutes of preparation for Future Forward in week 15).
  Heading renamed.

### Module 25 (Portfolio and Capstone) — 3,626 words

- Verified: two references on Crossref.
- Fixed: the time budget said "the 90-minute meeting", but both maps give Kit 25 two
  meetings (16-week weeks 14B and 15A as parts 1 and 2; 10-week week 9 A and B), so the
  sentence now counts two meetings and 1.5 to 2.5 outside hours, which sums to the
  declared 5 to 6. The reference note's "No published study of them is cited because
  none was found" is now a plain statement that the conventions are this site's teaching
  practice. Heading renamed. Studio untouched.

## Summary table

| Module | Not-cover + Common errors | Guardrails (with "Why it fails") | Academic references (Crossref) | Time budget | Run-of-show form | Words |
|---|---|---|---|---|---|---|
| 12 | present (earlier) | 6 | 6 (earlier) | rewritten: unscheduled | labeled (earlier) | 4,103 |
| 13 | present (earlier) | 5 | 5 (earlier); 13↔U09 boundary added | rewritten: unscheduled | labeled (earlier) | 3,748 |
| 14 | present (earlier) | 5 | 5 (earlier); ERL grounded | rewritten: unscheduled | converted | 3,858 |
| 15 | present (earlier) | 5 | 4 added, verified | rewritten: unscheduled | converted | 3,724 |
| 16 | added, verified | 5 (5) | 6 added, verified | rewritten: take-home | labeled | 3,920 |
| 17 | added, verified | 8 (8) | 6 added (5 Crossref + Gopen & Swan) | stands (both maps) | labeled | 4,205 |
| 18 | added, verified | 6 (6) | 5 added, verified | rewritten: unscheduled | labeled | 4,182 |
| 19 | added, verified | 6 (6) | 5 added, verified + COPE/ICMJE | stands (both maps) | labeled | 4,159 |
| 20 | present (earlier) | 5 (5; 3 added) | 6 added, verified; 20→08 boundary | rewritten: 16-week only | labeled | 3,644 |
| 21 | present (earlier) | 5 (5; 3 added) | 6 added, verified | rewritten: 16-week only | labeled | 3,353 |
| 22 | present (earlier) | 6 | 4 added, verified; retitled; 22↔17 | stands (both maps) | labeled | 3,814 |
| 23 | present (earlier) | 4 | 4 added, verified; venue numbers sourced | rewritten: unscheduled | labeled | 3,858 |
| 24 | present (earlier) | 6 | 5 added, verified | rewritten: unscheduled | labeled | 4,016 |
| 25 | present (earlier) | 6 | 2 added, verified | rewritten: two meetings | labeled | 3,622 |

"Earlier" means present in HEAD from the September site audit. Modules 12–15 and 22–25
keep guardrails without "Why it fails" lines; they were never inverted and the plan did not
ask for the line there.

## Verified reference list (Crossref, 2026-09-27)

All 45 distinct DOIs in `modules/module12.md`–`module25.md` resolve on
`api.crossref.org/works/<doi>` to the cited author, title, container, volume, issue and
pages. Grouped by module (a paper cited on several pages is listed once):

- Alley & Neeley 2005, ASEE, 10.18260/1-2--14488 (22)
- Artzy-Randrup et al. 2004, *Science* 305:1107, 10.1126/science.1099334 (20)
- Bassett, Zurn & Gold 2018, *Nat Rev Neurosci* 19:566–578, 10.1038/s41583-018-0038-8 (20)
- Benjamini & Hochberg 1995, *JRSS B* 57:289–300, 10.1111/j.2517-6161.1995.tb02031.x (20)
- Birch 2012, *JOSA A* 29(3):313, 10.1364/JOSAA.29.000313 (16)
- Borland & Taylor 2007, *IEEE CG&A* 27(2):14–17, 10.1109/MCG.2007.323435 (16)
- Bourne 2007, *PLoS Comput Biol* 3(4):e77, 10.1371/journal.pcbi.0030077 (22, 23)
- Bourne & Korngreen 2006, *PLoS Comput Biol* 2(9):e110, 10.1371/journal.pcbi.0020110 (19)
- Brand et al. 2015, *Learned Publishing* 28(2):151–155, 10.1087/20150211 (19)
- Crameri, Shephard & Heron 2020, *Nat Commun* 11:5444, 10.1038/s41467-020-19160-7 (16)
- Dorkenwald et al. 2024, *Nature* 634:124–138, 10.1038/s41586-024-07558-y (17, 19)
- Dorkenwald et al. 2025, CAVE, *Nat Methods* 22:1112–1120, 10.1038/s41592-024-02426-z (15, 18, 21)
- Erren & Bourne 2007, *PLoS Comput Biol* 3(5):e102, 10.1371/journal.pcbi.0030102 (23)
- Fuhrmann et al. 2011, *CBE Life Sci Educ* 10(3):239–249, 10.1187/cbe.11-02-0013 (24)
- Garner et al. 2011, ASEE, 10.18260/1-2--17510 (22)
- Gibbs et al. 2014, *PLoS ONE* 9(12):e114736, 10.1371/journal.pone.0114736 (24)
- Hattie & Timperley 2007, *Rev Educ Res* 77(1):81–112, 10.3102/003465430298487 (25)
- Januszewski et al. 2018, *Nat Methods* 15:605–610, 10.1038/s41592-018-0049-4 (14, 18)
- Ji et al. 2023, *ACM Comput Surv* 55(12):1–38, 10.1145/3571730 (15)
- Lamprecht et al. 2020, *Data Science* 3(1):37–59, 10.3233/DS-190026 (21)
- Leininger et al. 2021, *PLOS Comput Biol* 17(7):e1009133, 10.1371/journal.pcbi.1009133 (23)
- Mayer & Moreno 2003, *Educ Psychol* 38(1):43–52, 10.1207/S15326985EP3801_6 (22)
- Mensh & Kording 2017, *PLOS Comput Biol* 13(9):e1005619, 10.1371/journal.pcbi.1005619 (17)
- Michaut 2011, *PLoS Comput Biol* 7(10):e1002232, 10.1371/journal.pcbi.1002232 (23)
- MICrONS Consortium 2025, *Nature* 640:435–447, 10.1038/s41586-025-08790-w (17, 18)
- Milo et al. 2002, *Science* 298:824–827, 10.1126/science.298.5594.824 (20)
- NASEM 2018, 10.17226/25038; NASEM 2019, 10.17226/25568 (24)
- Nicol & Macfarlane-Dick 2006, *Stud Higher Educ* 31(2):199–218, 10.1080/03075070600572090 (25)
- Nosek et al. 2018, *PNAS* 115(11):2600–2606, 10.1073/pnas.1708274114 (20)
- Peng 2011, *Science* 334:1226–1227, 10.1126/science.1213847 (18, 21)
- Rougier, Droettboom & Bourne 2014, *PLoS Comput Biol* 10(9):e1003833, 10.1371/journal.pcbi.1003833 (16)
- Sandve et al. 2013, *PLoS Comput Biol* 9(10):e1003285, 10.1371/journal.pcbi.1003285 (21)
- Sauermann & Roach 2012, *PLoS ONE* 7(5):e36307, 10.1371/journal.pone.0036307 (24)
- Schlegel et al. 2024, *Nature* 634:139–152, 10.1038/s41586-024-07686-5 (15)
- Shapson-Coe et al. 2024, *Science* 384:eadk4858, 10.1126/science.adk4858 (19)
- Simmons, Nelson & Simonsohn 2011, *Psychol Sci* 22(11):1359–1366, 10.1177/0956797611417632 (19)
- Song et al. 2005, *PLoS Biol* 3(3):e68, 10.1371/journal.pbio.0030068 (20)
- Stodden et al. 2016, *Science* 354:1240–1241, 10.1126/science.aah6168 (21)
- Walters & Wilder 2023, *Sci Rep* 13:14045, 10.1038/s41598-023-41032-5 (15)
- Wasserstein & Lazar 2016, *Am Stat* 70(2):129–133, 10.1080/00031305.2016.1154108 (17)
- Weissgerber et al. 2015, *PLoS Biol* 13(4):e1002128, 10.1371/journal.pbio.1002128 (16)
- White et al. 1986, *Phil Trans R Soc B* 314:1–340, 10.1098/rstb.1986.0056 (17)
- Wilkinson et al. 2016, *Sci Data* 3:160018, 10.1038/sdata.2016.18 (18, 21)
- Wong 2011, *Nat Methods* 8(6):441, 10.1038/nmeth.1618 (16)

Not on Crossref, stated as such on the page: Gopen & Swan 1990 (17). Guidelines, not
papers: COPE Core Practices and ICMJE Recommendations (19).

## Sources for numbers

| Page | Number | Source |
|---|---|---|
| 14 | ERL 1.1 mm; "order of magnitude" | Januszewski 2018 abstract (Europe PMC, doi above) |
| 14 | 10 / 100 / 1,000 µm bands | labeled this site's rule of thumb |
| 16 | 8% of men, 0.4% of women | Birch 2012 abstract |
| 16 | heatmap and Sholl figures | `assets/kits/module16/*.csv`, `morphometry.py` (recomputed) |
| 17 | medians, ratio 1.31, CI 1.02–1.57 | `assets/kits/module16/input_synapses_by_layer.csv` (recomputed, seed 1) |
| 18 | all row counts and percentages | `assets/kits/module18/*.csv` (recomputed); match the answer key |
| 18 | MICrONS precision 96%, recall 89% | `canonical-facts.md:69` |
| 20 | 16 × 0.05 = 0.8 | arithmetic on the page's own 16-class census |
| 23 | GRC 200-attendee limit; no-publication policy | grc.org/about/ and grc.org/about/grc-policies-and-legal-disclaimers/ |
| 23 | SfN "more than 30,000 attendees" | sfn.org/about |
| 23 | 120 words a minute | stated as the module's budgeting assumption |
| 12–25 | meeting counts and weeks in time budgets | `teaching/syllabi/16-week.md`, `10-week.md` (tables and "What this map uses and omits") |

## Validators

- `ruby scripts/validate_frontmatter.rb`: no problems found.
- `ruby scripts/validate_code_span_paths.rb`: OK (261 permalinks, 513 files).
- `ruby -ryaml -e 'YAML.load_file("_data/modules.yml")'`: loads; entry 22 is "Scientific Presentation".
- Every `relative_url` target in modules 12–25 (74 distinct) resolves to a permalink or a
  file, checked by grep.

## Outside this pass (for the owner or the other agent)

- **Reference heading.** Modules 01–03 use `## Academic references`; 04–11 still use
  `## References`. This pass moved 12–25 to `## Academic references` as instructed.
  Modules 04–11 belong to the other agent's pass.
- **08→20 cross-reference.** Module 20 now states its boundary with Module 08. Module 08
  has no link to Module 20 (other agent's file).
- **Generated Module 22 files** carry the old title until the generator and renderer are
  run: `course/decks/marp/modules/module22.marp.md`, `teaching/sessions/module22.md`,
  `assets/worksheets/module22/module22-activity.md`, `course/decks/marp/out/modules/module22.html`.
  The 16-week and 10-week maps also describe Kit 22 as "scientific writing and
  presentation" in their week narratives (`16-week.md:449`, `10-week.md:284`); those pages
  were not in this pass's edit list.
- **Pedagogical budgets left unsourced by design:** Module 22's 8-minutes-of-speech in a
  10-minute slot and the 15-second "so what" test; Module 23's word budget per abstract
  section and 250-word assumption. They are the module's own design choices, not claims
  about the world.
