# Teaching-layer gaps: FAQ, unit items, two-day map, pacing notes

Date: 2026-09-27. Branch `compass-workshops`. Source: `docs/planning/NEXT_CONTENT_PASS.md` §3.4
(pacing notes, assessment bank per unit, instructor FAQ) and the two-day syllabus mapping.

Files created or edited (nothing committed):

- `teaching/faq.md` (new, `/teaching/faq/`)
- `teaching/assessment/units.md` (new, `/teaching/assessment/units/`)
- `teaching/assessment/units-answers.md` (new, `/teaching/assessment/units-answers/`)
- `teaching/assessment/index.md` (link and paragraph)
- `teaching/syllabi/two-day.md` (new, `/teaching/syllabi/two-day/`)
- `teaching/syllabi/index.md` (two-day link, Pacing notes section)
- `teaching/facilitator-guide.md` (one Related line)

## 1. Instructor FAQ

`teaching/faq.md`, 35 questions in eight themes (EM and tissue 5; scale and data size 3;
segmentation and proofreading errors 5; synapse detection 5; graphs, nulls and
statistics 5; versions and reproducibility 3; ethics and credit 4; running the
sessions 5). Every answer links the page and section it is drawn from; anchors follow
the site's kramdown convention as used in `_data/concepts.yml` (numbered headings keep
their digit, punctuation dropped, spaces to hyphens).

Where each question came from:

| Theme | Question (short) | Source of the question |
|---|---|---|
| EM | Why not confocal | Introduction lecture notes ("nanoscale is the serious scale"); Unit 01 §1 check-yourself |
| EM | Is a measured length real | Unit 03 §1.3 (not a kit misconception; asked in every prep session) |
| EM | Noise vs faint membranes | Module 05 kit: "A noisy image is worse for segmentation than a clean image with faint membranes" |
| EM | Proofread out of a bad image | Module 05 kit: "You can proofread your way out of a bad image" |
| EM | Fading toward block center | Tools and Methods lecture notes (staining-gradient case); Unit 03 §1 check-yourself |
| Scale | 1.6 PB vs 2 PB; storage as main cost | Module 12 kit: "The dataset size is the petabyte figure quoted for the raw imagery"; "Storage cost is the storage line on the invoice" |
| Scale | Why not always EM | Introduction lecture notes (decision rule) |
| Scale | Whole mouse brain | Unit 01 §2 table; asked whenever the table is shown |
| Errors | Merges worse than splits | Module 06 kit: "Merge and split errors are equally costly"; Facilitator Guide question stem |
| Errors | Plausible neuron as evidence; empty merge queue | Module 06 kit: "An object that looks like a plausible neuron is evidence…"; Unit 08 §2 check-yourself |
| Errors | "All cells were proofread" | Module 07 kit: "A result can be reported without stating the proofreading level" |
| Errors | Glia merge before obvious split | Module 06 kit: "The most visually obvious errors are the ones most worth fixing" |
| Errors | Is "uncertain" acceptable | Facilitator Guide checklist ("decided what uncertain earns"); Module 01 kit: "Good annotators never make errors" |
| Synapses | Detector accuracy; quoting the paper's number | Synapse Detection lecture cautions ("Do not call an F1 score accuracy"; "Do not transfer a paper's performance estimate") |
| Synapses | E/I ratio wrong despite high precision | Synapse Detection timed plan, minutes 20–30 ("unequal recall") |
| Synapses | Recall from a sample of rows | Synapse Detection timed plan, minutes 65–80; assessment bank S5 |
| Synapses | Asymmetric means excitatory; count means strength | Module 11 kit: both misconceptions verbatim |
| Synapses | Synapse vs dark membrane | Facilitator Guide opening paragraph (tangentially cut membrane) |
| Graphs | 2.9× over random | Module 08 kit: "A significant result against a random-graph null…"; Module 10 kit: Erdős–Rényi |
| Graphs | Which null | Module 08 kit: "The statistical test is the scientific step, when the choice of null model is" |
| Graphs | Synapse threshold | Module 10 kit: "The synapse threshold is a technical detail that does not need reporting" |
| Graphs | Errors as noise | Module 11 kit: "Reconstruction errors add symmetric noise"; Algorithms lecture notes; Unit 06 §4 check-yourself |
| Graphs | Sixteen tests | Module 08 kit: "Reporting the tests that worked is sufficient…" |
| Versions | Count changed on rerun; same count reproduced | Module 12 kit: "An object ID refers to the same neuron next month"; Tools lecture plan 30–40 min |
| Versions | Methods record; repository link | Module 17 kit: "A link to the code repository makes the analysis reproducible"; Module 21 kit: "A notebook that ran end-to-end once…" |
| Versions | Which MICrONS version | Canonical facts §10; the lab page's access section |
| Ethics | Public data, no ethics question | Module 02 kit: "If the data is publicly available, there are no ethical considerations"; Module 17 kit on attribution |
| Ethics | Hemibrain license | Ethics lecture cautions |
| Ethics | H01 donor identification | Ethics lecture cautions and timed plan 10–22 min |
| Ethics | Credit for proofreading | Module 19 kit: "Contribution volume alone decides authorship" |
| Running | Accounts, downloads, Python | Sequence page; MICrONS lab; both maps' "Technical work omitted" |
| Running | Running long | Sequence page "Preparation and pacing"; Facilitator Guide (Unit 09 §4 vs §2) |
| Running | Lecturing Units 05–07 | Facilitator Guide failure modes 1–3 |
| Running | Public keys and grading | Syllabus maps, Assessment |
| Running | Calibration round | Facilitator Guide "Run a calibration round"; Unit 03 lab instructor note |

Numbers in the FAQ and where they come from: MICrONS ~2 PB raw, 96% / 89% / 98%
detection figures, and the "EM dataset" and "Automated reconstruction" section names
(canonical facts §1c, §1d, MICrONS Consortium 2025 doi:10.1038/s41586-025-08790-w);
H01 1.4 PB aligned / 1.8 PB raw, donor description (canonical §2, Shapson-Coe 2024
doi:10.1126/science.adk4858); FlyWire 33 person-years (canonical §3c, Dorkenwald 2024
doi:10.1038/s41586-024-07558-y); hemibrain >50 person-years and the license conflict
(canonical §4, Scheffer 2020 doi:10.7554/eLife.57443; DataCite record for
doi:10.25378/janelia.11676099); mouse brain 508.9 ± 23.4 mm³ (canonical §7, Badea 2007
doi:10.1016/j.neuroimage.2007.05.046) and ~800 PB / ~1 EB (canonical §7, Abbott 2020
doi:10.1016/j.cell.2020.08.010); BRAIN CONNECTS 11 awards, 26 September 2023 (canonical
§8); MICrONS versions 943 / 1300 / 1507 and the 31 July 2026 expiry (canonical §10);
Korogod 2015 shrinkage (Unit 03 §1.1, doi:10.7554/eLife.05793). The H01 11% / 35%
false-negative and 3.2% / 2.7% FDR figures are quoted as the synapse-detection reference
page states them (§7 table); I did not re-read the H01 paper for them.

## 2. Unit assessment items

Progress (written one unit at a time): Unit 01 done (5 items, U1.1–U1.5). Unit 02 done (6 items). Unit 03 done (5 items). Unit 04 done (5 items). Unit 05 done (5 items). Unit 06 done (5 items; the skeleton's heading "Synapse
identification" corrected to the unit's real title, "Axons and dendrites"). Unit 07 done (5 items; heading shortened to the unit's title,
"Glia"). Unit 08 done (5 items). Unit 09 done (5 items). "Running a calibration round" written.

Totals: **46 items** (Units 01–09: 5, 6, 5, 5, 5, 5, 5, 5, 5), each tagged `Un-k` to one
outcome in the unit's "What you'll be able to do" list, each with a variant template,
and each with a worked answer and per-error feedback in `units-answers.md`. Mix:
calculations U1.2, U1.3, U2.3, U2.4, U2.5, U3.3, U3.4, U4.1(g), U4.3, U4.5, U5.2 (PSD
sections), U5.5, U6.3, U6.4, U7.3, U7.5, U8.2, U8.4(b), U8.5, U9.1–U9.4; claim sorting or
labeling U1.4, U2.6, U5.3, U9.5; the rest short answer, matching or triage.

Every number is synthetic and chosen to differ from the unit's worked examples and
check-yourself questions and from `teaching/assessment/index.md`. Fictional names
(Wren, Sparrow, Finch, Plover, Heron, Kite, Rook, Lark, Vireo, Tern, Egret, Gannet,
Dunlin, Knot) avoid the reserved labels. Every calculation was recomputed in python3,
using `fractions` where exact values matter (U4.5 pyramid 625/24 TB, U4.3 31/150,
U9.1 56/65, U9.2 p = 1/8); BH in U9.3 was checked over all 16 ranks. The only
published-work citation in the answers is Lappalainen et al. 2024 in U9.5, as the unit
itself cites it.

FAQ fix (coordinator's nav crawl): the Synapse Detection link now uses the heading's
explicit id `#start-here-this-is-a-solved-problem-with-three-residuals` (the page sets
it with `{: #… }` under "Detection performance depends on the claim").

## 3. Two-day map

`teaching/syllabi/two-day.md` complete: eight 90-minute slots, four a day.
Day 1: Orientation, Sessions 1–3. Day 2: Session 4, MICrONS lab (Module 07 kit as the
one-kit swap), Ethics (optional), revision studio. Totals follow `teaching/sequence.md`:
360 teaching minutes plus three 15-minute breaks = 6 h 45 min a day excluding lunch;
Day 2 without Ethics = 270 + 30 = 5 h 0 min. Advance work: 45 timed minutes (lab norms
25, Synapse Detection reading 20) plus the Orientation case and the lab install (no
time stated on the lab page, so none given). Evening: 20 (methods record, the 10-week
allowance) + 25 (Ethics reading). MICrONS step timings (15/35/25/15) are the 10-week
map's; the Module 07 run of show is the kit's 60 minutes. The only new structure is the
closing studio (15/20/30/25 minutes), labeled on the page as having no packaged plan and
reusing the Introduction rubric. Sections: At a glance, Day 1, Day 2, uses and omits,
what two days cannot do, suggested feedback.

## 4. Pacing notes

`teaching/syllabi/index.md` now links the two-day map (list entry; the closing line now
reads "All three are drafts") and has a `## Pacing notes` section (id `pacing-notes`,
which the FAQ's link at line ~455 targets). Sources: the 25 module `duration` fields and
the 25 kits' "At a glance" durations (they match exactly); the kits' run-of-show tables
(90 minutes for Modules 01–03, 60 minutes for 04–25); each module page's "Where the N
hours go" / "The declared N hours are" paragraph (Modules 04–11: 60-minute tutorial plus
a 60–75 minute studio, Module 05 about 60; Modules 12–24: one 90-minute meeting, with
2–3 h outside, about 2 h for 16, 19, 22–24, 2–4 h for 20; Module 25: two meetings);
the sequence page's cutting rule; and the unit lab headings (01 60, 02 75, 03 90, 04 90,
05 75, 06 90, 07 60, 08 2 h, 09 2 h). The "no two modules pair into one 90-minute
meeting" note is arithmetic on those figures, not a new timing.

## 5. Assessment index and Facilitator Guide

`teaching/assessment/index.md`: one paragraph after the "public and formative" note
linking `/teaching/assessment/units/` and `/teaching/assessment/units-answers/`, with
the item count (46). `teaching/facilitator-guide.md`: one **Related** line to
`/teaching/faq/` at the end of the Preparation checklist.

FAQ spot-check (this run): five answers checked against their sources, all consistent:
mouse brain 508.9 ± 23.4 mm³ and ~800 PB (canonical facts §7 arithmetic gives 795 PB);
MICrONS 96% / 89% / 98% (microns-visual-cortex case study, canonical §1d); H01 11% / 35%
false negatives (synapse-detection §4 table); FlyWire 33 person-years (flywire case study);
MICrONS versions 943 / 1300 / 1507 (lab page; the lab also lists 117 as long-term
support, which the FAQ omits without error). One anchor fixed, as noted in §2.

## Links needed (not made here)

- `teaching/sequence.md` "What comes next" names the 10- and 16-week maps but not the
  two-day map; one clause would do.
- The nine unit pages' "Course links" sections could link `/teaching/assessment/units/`
  for practice items.
- `teaching/faq.md` could point its "Public keys and grading" answer at the unit pool.
- The Teaching Hub already links the two-day map, the unit pool and the FAQ. It calls the
  FAQ "Teaching FAQ" and describes it as covering "accounts and data, timing,
  licensing"; the page is titled "Instructor FAQ" and is mostly content questions.
  Worth aligning.

## Judgment calls

- **Two-day slot 8.** The block, Ethics, Orientation and the lab make seven 90-minute
  slots. Two 6.5–7 h days need eight, so Day 2 ends with a revision studio built only
  from existing rubrics, labeled on the page as having no packaged plan. The Module 07
  kit is the "one module kit" option as a swap for the lab, not an addition.
- **Break arithmetic.** I followed the sequence page: four slots, three 15-minute
  breaks, lunch excluded, 6 h 45 min.
- **Install time.** The lab page gives no install time, so the map gives none.
- **Item count.** Five per unit, six for Unit 02 (five outcomes, one extra for the
  anisotropy calculation). Every outcome of every unit (41 outcomes) has at least one
  item; U4-4 ("query a volume") is assessed through a methods record rather than a
  live query, since the pool needs no account.
- **Unit 06 and 07 headings.** The skeleton titled Unit 06 "Synapse identification" and
  Unit 07 "Glia and non-neuronal cells"; the unit pages are "Axons and Dendrites" and
  "Glia", so the pool uses those.

## Validation

- `ruby scripts/validate_frontmatter.rb`: no problems found.
- `ruby scripts/validate_code_span_paths.rb`: OK (262 permalinks, 514 files).
- A local link check over the seven edited teaching files (every `relative_url` path
  against front-matter permalinks, every `#anchor` against kramdown heading ids and
  explicit `{: #id}` ids): 0 broken. The checker was confirmed to flag a planted bad
  anchor and a planted bad path.
- No Jekyll build was run in this pass.
- Footers on `units.md` and `units-answers.md` changed to "CC BY 4.0" per the
  coordinator (site content is CC BY 4.0; BY-SA is for the lecture decks only).
