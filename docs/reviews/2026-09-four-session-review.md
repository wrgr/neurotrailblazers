# Four-session connectomics path: learner and instructor review

*Reviewed 26 September 2026 on branch `compass-workshops` (base `ebf5e02`). Scope:
`teaching/sequence.md`, the four session plans, the four worksheets, the four answer keys,
the two offline Python scripts and, read-only, the four slide sources. No Jekyll build was
run; link targets were checked against permalinks in the repository.*

---

## Summary

The path is in good shape. Every timed plan sums to 90 minutes, every cited slide
number shows the content its plan describes, every answer-key number recomputes
exactly, and both Python scripts reproduce their keys. The sequence's half-day,
three-session and four-session timing claims are correct.

The main learner-view defect was a broken artifact chain at Session 2. The sequence
promised that learners revise their Session 1 brief, and Session 3 asked them to bring
it, but neither the worksheet nor the timed plan contained that step. This is now fixed
with a three-minute carry-forward step in the debrief. Four smaller defects were also
fixed. The largest remaining issue is a design judgment: Sessions 3 and 4 ask learners
to bring prior artifacts, but their worksheets work only on synthetic fixtures and never
use those artifacts.

## Issues

| Issue | Page | Severity | Status | Note |
|---|---|---|---|---|
| Session 1 brief revision promised in the sequence ("They then revise their Session 1 brief...") and required by Session 3 ("Bring the revised study brief"), but absent from the Session 2 worksheet and timed plan | `teaching/lectures/synapse-detection-activity.md`, `synapse-detection.md` | major | fixed | Added a "Carry forward (3 minutes, during the debrief)" step to the worksheet, and added it to the 80–90 min block of the plan. This is in-session, so the sequence's "no additional homework" claim still holds. |
| Plan says "Pause the deck so learners can see the input counts", but the worksheet counts are on no slide | `synapse-detection.md` | minor | fixed | Now reads "Pause the deck; the input counts are on the worksheet, not the slides." A grep of the deck source confirmed the counts are absent. |
| Terminology drift: Session 4 plan says "provenance record"; the sequence and Session 3 call the artifact the "methods record" | `connectomics-03-algorithms-and-applications.md` | minor | fixed | Changed to "methods record". |
| Analysis card asks for a "graph version", but paper-route learners were never given one (only the script prints `synthetic-four-neuron-graph-v1`, which the key uses) | `algorithms-and-applications-activity.md` | minor | fixed | Stated the graph version in the data contract. |
| Plans say "collect" briefs, audits and records, yet learners must bring them to the next session | `teaching/sequence.md` | minor | fixed | Added one sentence under Preparation and pacing: photograph or return collected work. |
| Carry-forward is nominal in Sessions 3 and 4. The Session 3 methods record and the Session 4 analysis card both concern synthetic fixtures. Neither worksheet asks learners to apply them to their own brief's endpoint. The Session 3 plan's "Carry the endpoint and its provenance into Algorithms and Applications" has no worksheet step. | `tools-and-methods-activity.md`, `algorithms-and-applications-activity.md` | major | open | Design choice. Options: add a two-minute "apply to your brief" line to each worksheet, or soften the sequence's chain language ("study brief → audit → methods record → analysis card"). |
| The Session 3 processing-grid prompt (10–20 min) is best supported by slide 31 ("How pipeline errors present downstream"), which is not selected. Slide 19 covers tile-seam grids only partly. | `connectomics-02-tools-and-methods.md` | minor | open | Consider adding slide 31 to the 10–20 min block. |
| The between-session reading is about 4,800 words, which is tight for 20 minutes | `sequence.md`, reading page | minor | open | "Focusing on" implies skimming. Consider naming sections 1, 5 and 7 explicitly. |
| Session 2 worksheet section 1 (six metrics, accuracy question, 108/120 interpretation) in 10 minutes is tight. The 80–90 block now also holds the debrief, a 3-minute revision and the exit ticket. | `synapse-detection-activity.md`, `synapse-detection.md` | minor | open | Watch pacing in a first run. The minute-55 check is the natural place to extend. |
| The Session 1 plan navigates non-sequentially (18–22, then 28–29 and 35, then back to 23–24) | `connectomics-01-introduction.md` | minor | open | Appears deliberate. Instructors should note the jumps or reorder the 20–30 and 30–40 blocks. |
| Series overview says "A 90-minute slot takes Parts A and B" (about 100 minutes of material). This competes with the selected-slide 90-minute routes. | `teaching/lectures/index.md` | minor | open | Outside the four-session path. Consider pointing 90-minute users to the sequence. |

## Verified

**Timing**

- Session 1 blocks: 5+15+10+10+25+15+10 = 90. Worksheet 5+8+12 = 25 min plus 10 min peer review matches 40–65 and 65–80 (10 exchange + 5 compare).
- Session 2 blocks: 10+10+10+10+25+15+10 = 90. Worksheet 10+10+5+10 = 35. Sections 1–3 (25 min) match 40–65; section 4 (10) + exchange (5) match 65–80.
- Session 3 blocks: 10+10+10+10+35+10+5 = 90. Worksheet 15+10+10 = 35 matches the plan's "15, 10 and 10".
- Session 4 blocks: 10+10+10+10+35+10+5 = 90. Worksheet 10+10+5+10 = 35 matches the plan.
- Sequence half-day: 2×90 + 15 = 195 min. First three: 270 + 2×15 = 300 min = 5 h. All four: 360 + 3×15 = 405 min = 6 h 45 min.

**Slide citations** (cover = slide 1, split on `---` after front matter)

- Module 7 (59 slides, matching "59 slides"): 1 cover, 4 objectives, 10 three claims, 7 connectome defined, 11–14 resolution/overlap/EM/synapse criteria, 18–22 bins and return to cold open, 28–29 three scales and decision rule, 35 scale leakage, 23–24 repaired research question, 25–26 sizing the claim and Part A checkpoint, 56 assignment, 58–59 references and credit.
- Synapse Detection (39 slides): 1–3 cover, detector framing and objectives; 9 three problems; 13–15 evaluation units, aggregation and check; 17–18 CREMI; 21–23 sign and H01 asymmetry; 26–29 H01 count correction; 33–34 table checklist and afternoon audit; 35–37 check, scope and next steps; 38–39 references and credit. The selected and optional lists together cover all 39 slides exactly.
- Module 8 (56 slides): 1–3, 6 cover, where we left off, objectives and pipeline map; 9–10 staining and failures (depth gradient); 19 artifact catalog; 21–22 QA and gates; 26–27 eight-stage pipeline and ingest; 33–35 chunked storage, chunk shape and capacity; 40, 42–46 silent version failure, root IDs, the 1,412/1,530 worked example, header, requirements and environments; 51 reproducibility audit; 52 assignment; 54 what to bring; 55–56 references and credit.
- Module 9 (58 slides): 1–4 and 12 cover through objectives, plus error taxonomy; 16, 19–21 endpoint metric and triage worked example; 25–28 construction choices, threshold and basic statistics; 29–30, 34 null framing, null table and distance-null objection; 36–38, 40 merge bias, sensitivity check, multiple testing and provenance block; 52 communicating without overclaiming; 54 lab; 55 assignment and Test 3; 57–58 references and credit.

**Arithmetic, recomputed independently**

- Session 1: total 6+2+0+4 = 12; connected 3/4 = 75%; 12/4 = 3 per eligible pair; 12/3 = 4 per connected pair.
- Session 2 E: precision 80/85 = 94.1%, recall 80/100 = 80.0%, F1 160/185 = 86.5%.
- Session 2 I: precision 40/45 = 88.9%, recall 40/80 = 50.0%, F1 80/125 = 64.0%.
- Session 2 partners and correction: 120 TP = 80+40; 108/120 = 90%; reference total 100+80 = 180; 108/180 = 60%. Observed E 85/130 = 65.4%; corrected 100 and 80; 100/180 = 55.6%; change 9.8 percentage points.
- Session 3 snapshot counts: A = {s1, s2}, n = 2; B = {s1, s2, s3, s6}, n = 4. Under strict `>`: 1 and 3.
- Session 3 capacity: 10,000 × 10,000 × 1,000 = 10¹¹ voxels = 100 GB; 300 GB for three copies; 10¹¹ / 10⁸ = 1,000 s ≈ 16.7 min.
- Session 4 graph: threshold one gives m = 6, R = 2, 2R/m = 2/3. Threshold two drops B→A and B→C, giving m = 4, R = 1, 1/2. Removing B→A gives m = 5, R = 1, 2/5.
- Session 4 nulls, enumerated separately from the provided script: C(12,6) = 924 with census 64/480/360/20; mean 15/11; ratio 22/15; tail 380/924 = 95/231 ≈ 0.411. C(12,4) = 495 with census 240/240/15; mean 6/11; ratio 11/6; tail 255/495 = 17/33 ≈ 0.515. For reference, the five-edge null (not in the key) has census 192/480/120, and its tail for R ≥ 1 is 25/33.

**Scripts** (run with `python3` 3.14.7)

- `tools-and-methods-query.py --version snapshot-a` returns count 2 [s1, s2], 3 excluded. `--version snapshot-b` returns count 4 [s1, s2, s3, s6], 2 excluded. Both match the key.
- `--version latest` and a missing `--version` are both refused, as the worksheet states. The output includes filters, IDs, counts, Python version and SHA-256, as the worksheet states.
- `algorithms-and-applications-query.py --threshold 1` and `--threshold 2` reproduce every edge list, census, mean, ratio and tail in the key. The dataset label is `synthetic-four-neuron-graph-v1`.

**Other checks**

- Every worksheet labels its data as invented or synthetic. Every key restates this.
- Rubrics have four 0–2 dimensions, each mapping to worksheet sections, with a stated proficiency rule.
- Prerequisites, materials, preparation and "no accounts" statements are present on all four plans.
- These link targets exist as permalinks: `/content-library/infrastructure/synapse-detection/`, `/teaching/sessions/`, `/technical-training/slides/`, `/teaching/`, `/teaching/lectures/`, `/technical-training/journal-club/` and all eight worksheet and key pages.
- `#teach-a-90-minute-session`, `#formats` and `#licence` headings exist. The HTML decks exist under `course/decks/marp/out/`, and `site.deck_source_base` is defined.
- The sequence's course-mapping notes are consistent with the lecture pages: Session 3 = Lecture 2 / Module 8, Session 4 = Lecture 3 / Module 9, and Synapse Detection is not Module 8.
