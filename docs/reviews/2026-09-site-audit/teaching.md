# Site audit: teaching area

*Audited 26 September 2026 on branch `compass-workshops`. Scope: `teaching/index.md`,
`teaching/sequence.md`, `teaching/lectures/**`, `teaching/answers/**`,
`teaching/assessment/**`, `teaching/syllabi/**`, `teaching/facilitator-guide.md`,
`teaching/module22-public-engagement.md`, `teaching/projectome-to-synapse.md`,
`teaching/sessions/index.md` and the text of `assets/worksheets/lectures/*.py`. Decks were
read, not edited. No Jekyll build was run; links were checked against permalinks and
heading anchors in the repository.*

## Summary

| Count | |
|---|---|
| Files read | All in scope (31 pages, 2 scripts), plus the 5 decks and the Module 01, 07 and 18 worksheets and kits |
| Files edited | 24 |
| Issues fixed | 39 (rows below; several rows cover more than one edit) |
| Items for an owner decision | 4 |
| Cross-area items | 6 |

**What was checked and holds.** Every timed plan sums to 90 minutes (Introduction,
Synapse Detection, Tools and Methods, Algorithms and Applications, Ethics). Each plan's
worksheet sections fit its activity block. Every cited slide number shows the content the
plan describes, and the Synapse Detection and Ethics plans' selected and optional lists
cover every slide exactly (39 and 31). Sequence totals are right: 195, 300, 405 and 510
minutes. Every weekly outside-hours figure on both syllabi equals its "before" plus
"after" minutes, and the weeks sum to the stated 1,825 minutes (10-week) and 2,665 minutes
(16-week). All arithmetic in the five lecture keys, the three module keys and the 20
assessment items was recomputed in Python: the Module 07 values by running the kit's
`qc_metrics.py`, the Module 18 values from the kit CSVs, and the A3 null censuses by full
enumeration. Every value matches. Both lecture scripts produce byte-identical output
before and after this pass; neither `.py` file was edited, because any text change would
alter the `source_sha256` they print. All five validators pass.

**Plan item 6 (syllabus maps and the repaired kits).** Done. Both maps and the overview
now state each omitted kit's reason as time or overlap, not a missing file. Kit 07 is
offered as an in-class swap for the Unit 08 Part B meeting, and Kits 07 and 10 as
take-homes. Contact hours are unchanged (30 and 48). The extension lists now carry
honest totals.

## Issues and fixes

| File | Issue | Type | Fix |
|---|---|---|---|
| `teaching/syllabi/10-week.md` | "To reach a two-to-one ratio, add…" listed about 4 hours; 2:1 needs about 60 outside hours against 30.4 | Accuracy (hours) | Lists each addition with hours (4 + 8 + 4.5); states the total reaches about 47 h and the gap remains |
| `teaching/syllabi/16-week.md` | Same claim; 2:1 needs about 96 h against 44.4. Also listed Unit 03 §§3–4, which week 3 already assigns (double count), and put the rest of Unit 09 at "about 2 hours" (it is 45 minutes) | Accuracy (hours) | Rewritten: Unit 09 §§4–5 (45 min), Unit 09 lab (2 h), Module 16 (4 h), Kits 07 and 10 (4 h each): about 15 h, total about 59 h |
| `10-week.md` week 4B, `16-week.md` week 6A | MICrONS lab steps summed to 75 of 90 minutes | Timing | Added a 15-minute install check and pairing step |
| `16-week.md` week 1A | 60 + 20 minutes in a 90-minute meeting | Timing | Last 10 minutes start the navigation document |
| `10-week.md`, `16-week.md`, `syllabi/index.md` | Said kits 03–07 and 09–11 name files the site does not publish; they now resolve | Stale | Each omission restated as time or overlap, kit by kit (16-week lists all 17); Kit 07 swap for Unit 08 Part B; Kits 07 and 10 as take-homes |
| `16-week.md` week 4B | Fallback "Module 05 kit with patches you supply" | Stale | Points to the patch-set recipe on the module page |
| `10-week.md`, `16-week.md` | "Python 3.11 or later … the run takes about a minute" | Accuracy | Lab page says 3.11–3.13, 2 GB free memory, under a minute on the test machine and several minutes on older laptops; matched |
| `syllabi/index.md` | Real-data lab paragraph omitted v1507's scheduled CAVE retirement; rerun claim unspecific | Accuracy | Added the 31 July 2026 schedule, static exports resolving on 26 September 2026, and four reruns on Python 3.11 and 3.13 (canonical-facts §10; lab rerun log) |
| `16-week.md` week 12B | "week 6 query note" names no artifact that exists | Naming | "the week 6 MICrONS methods record" |
| `sequence.md`, both syllabi | 20 minutes for a 4,800-word reading (four-session review, open item) | Timing | Names the opening section and sections 1, 2 and 7 (about 1,700 words) |
| `sequence.md` | "Model answers for all 25 modules remain separate work" | Stale | Keys exist for 01, 07, 18; links the answers page and its order |
| `sequence.md` | "a proofreading exercise" with no link | Dead end | Links the Module 07 kit |
| Hub, sequence, 10 lecture pages | "short lecture series", "short teaching sequence", "teaching sequence", "short sequence", "four-session block" for one thing | Naming | "four-session block" throughout (13 places) |
| `lectures/index.md`, three lecture pages | `use_layout_hero: false` with no H1 in the body, so the pages rendered no H1 | Polish (accessibility) | Removed the flag; dropped each lecture's "What this lecture covers" paragraph, which repeated the description now shown under the H1 |
| `module22-public-engagement.md`, `projectome-to-synapse.md` | Body `#` heading plus the layout H1: two H1s | Polish | Removed the body H1 |
| `connectomics-01-introduction.md` | "The cold open pays off eleven slides later": slides 10 → 22 is twelve | Accuracy | Twelve, with both slide numbers |
| `connectomics-01-introduction.md` | "about a third accept the third": an unsourced audience statistic | Fabrication risk | Removed the number |
| `connectomics-01-introduction.md` | "million-fold error in data volume" | Numbers over adjectives | "about 1.5 million times" the voxels at 4 × 4 × 40 nm vs 1 µm (10⁹ / 640) |
| `connectomics-02-tools-and-methods.md` | "essentially nobody adopts it until they have been burned once"; "rubric awards points" | Unverifiable | Softened; cites the slide 52 assignment table, which grades the header |
| `connectomics-02-tools-and-methods.md` | The 10–20 min processing-grid prompt lacked slide 31 (four-session review, open item) | Slide citation | Added slide 31 and what it shows |
| `connectomics-03-algorithms-and-applications.md` | "slightly boring, which is usually the sign that it is right" | Voice | States the deck's position and cites slides 47–49 |
| `lectures/index.md` | "The lecture 2 assignment does [need a login]", with no alternative | Missing content | Names why (neuPrint and CAVE tokens) and the no-account MICrONS lab |
| `lectures/index.md` | "They cite published work" after an image-credit sentence | Grammar | "The lectures cite…" |
| Lecture pages, index | Em-dash separators, "Part A — …" headings, "— or built a version…" | Voice | Colons, full stops and commas |
| 11 files | British spellings: licence (and `#licence` anchors), labour, centrepiece, practising, judgement | American English | Converted; `#licence` links updated to `#license` in the same pass |
| `ethics-and-governance-activity.md` | "Can a 4 nm voxel volume identify the donor?" H01 voxels are 4 × 4 × ~33 nm | Accuracy | "an EM volume imaged at 4 nm pixels" |
| `ethics-and-governance-answers.md` | "*Data curation* or *Validation* (as H01 did)" reads as if H01 used both | Accuracy | "*Validation* (where H01 filed it) or *Data curation*" (deck slide 26) |
| `answers/module01.md` | "the landscape segment": Block 2 is now "Three projects, three driving questions" | Stale | Names Block 2 and its three projects |
| `answers/module18.md` | "The module text calls a score above 50 common practice": `modules/module18.md` no longer says so | Stale | Module now says to use the dataset's documented value; its run of show uses 50 as a challenge value |
| `answers/module18.md` | Five misconception headings no longer matched the regenerated worksheet | Inconsistent terms | Matched word for word |
| `answers/index.md` | "kits … 03–06 and 09–11 depend on sample files or patch sets" (implying missing) | Stale | Lists which backlog modules have kit folders (03, 06, 09–14, 16, 19) and which use a patch set (04, 05) |
| `teaching/index.md` | Em-dash button label; "assembled from pieces that used to live in five different places"; "new practice items"; generic hero line | Voice, counts | "Run a module session"; history dropped; "20 practice items"; hero line names what the hub holds |
| `teaching/sessions/index.md` | History narration and em-dash chains; no mention of kit data or keys | Voice, missing content | Rewritten; notes synthetic kit folders, patch-set recipes and the three keys |
| `facilitator-guide.md` | Unverifiable generalizations: learners calibrate "almost entirely" by watching experts; spread "shrinks sharply"; null models are "where most published errors in this field live"; "most facilitators lose the session"; "changes behavior within one session" | Unverifiable | Softened or turned into instructions |
| `facilitator-guide.md` | Calls a rubric "the assessment instrument" (the site says its rubrics are not validated instruments); 84%/90% example unlabeled; em-dash chains | Accuracy, voice | "the rubric"; example labeled as an illustration; about 20 sentence edits |
| `module22-public-engagement.md` | The 0–10 minute block assigned the 25–40 minute Projectome activity | Timing | Uses only the ladder step (about 10 minutes) and says the full activity can run as its own session |
| `module22-public-engagement.md` | Quoted Module 22's rule in paraphrase | Accuracy | Exact text from `modules/module22.md` |
| `module22-public-engagement.md` | "programme"; Codex and RePORTER unlinked; link to Module 22 missing | Polish | Fixed and linked |
| `projectome-to-synapse.md` | Asked learners to order a list already printed in answer order; APEX modality list vaguer than `core/connects-ecosystem.md` | Teaching defect, accuracy | Shuffled cards, list labeled as the answer; APEX and IC3 lines aligned to the core page |

## Needs owner decision

1. **Two-to-one outside hours.** Neither map can reach two outside hours per contact hour
   from existing materials. The best case is about 47 of 60 hours (10-week) and about 59
   of 96 (16-week). Decide whether to present the maps as roughly 1:1 courses, which is
   honest now, or to commission a larger final project.
2. **House spelling of "licence".** The brief says American English, so this area now
   uses "license" and "labor". The decks (read-only here), the ethics content page and
   the content library still use "licence" and "labour". Pick one site-wide.
3. **Kit 07 as a swap for Unit 08 Part B.** Both maps now offer it. It trades a
   labor-budget exercise for a metric computation that has a public key. Confirm this is
   the swap you want, or keep Unit 08 Part B as the only option.
4. **v1507 in the syllabi.** Both maps pin the real-data lab to v1507, which was scheduled
   to leave live CAVE on 31 July 2026. The lab reads static exports, which still resolve.
   If those exports are withdrawn, both maps' week 4 or week 6 meeting falls back to the
   archived notebook.

## Outside my area

- `docs/planning/NEXT_CONTENT_PASS.md` item 6 can be ticked. Both maps now state every
  kit omission as time or overlap.
- `assets/worksheets/module01/module01-activity.md`, "Session timing" table: the generator
  put Block 2's three numbered case studies into the Time column, so the table reads
  "C. elegans (White et al., 1986) | the first complete connectome…". The source is
  `modules/module01.md` Block 2 and `scripts/generate_module_teaching_materials.rb`, which
  seems to treat numbered bold items as timing rows. Check the other worksheets for the
  same pattern.
- `assets/kits/module07/error_report.csv`: `detector_note` gives z as a section index
  ("z=259"), while `z_um` is in micrometers (24.7). Label the unit in the note or the README.
- `docs/reviews/2026-09-four-session-review.md` line 81 names the `#licence` anchor. It is
  now `#license`. Also, its open items on slide 31, the reading length and Session 3/4
  carry-forward are resolved: the worksheets now have brief-update steps, and this pass
  added slide 31 and named the reading sections.
- Decks `course/decks/marp/en585781/*.marp.md` and `course/decks/marp/lectures/*.marp.md`
  use "licence", "labour" and "centralised" (British).
- `teaching/sessions/module0N.md` kits are generated. Kits 07 and 10 are now linked from
  both syllabi, so a change to their permalinks or activity length should update the maps.
