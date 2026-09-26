# Professional Pathways workshops: series review (September 2026)

Scope: all 31 files under `teaching/pathways/` (the hub plus ten workshops, each with a
plan, a worksheet and model responses), read in order as a facilitator running the whole
series. Branch `compass-workshops`, uncommitted edits.

## Summary

The series holds together well. Every file has matching front matter, section order,
header line, link list, footer and a four-dimension 0–2 rubric with a 6/8 proficiency rule,
a named no-zero dimension, the "local teaching rubric, not a validated assessment
instrument" sentence and a what-not-to-grade note. Every timed plan sums to 90 minutes,
and worksheet minute budgets match the plan blocks in all ten. Answers cover every
worksheet section. Every case is labeled invented. All 61 Liquid link targets resolve to
real permalinks, and every cited heading, anchor, norm number and module claim exists on
the target page. The follow-through chain runs 1 → 10 → hub without a break, and the two
artifacts Future Forward asks for (direction memo, network map) are produced and flagged
"keep this" in workshops 3 and 4.

The real problems were cross-workshop and invisible when each set was drafted alone:

- **Name collisions.** Tomás was a minor student in workshop 3, the sympathetic
  protagonist in workshop 7, and in workshop 8 the senior student who tells an
  undergraduate to falsify completion data. Sam and Priya from workshop 2 reappeared in
  workshop 8 in different roles. Dr. Lindqvist (workshop 7 collaborator) paid a stipend in
  workshop 9. Dr. Brandt was Leila's departing PI in workshop 4 and Hana's PI in workshop 10.
  All renamed.
- **Openers.** Only workshops 5–7 opened by collecting the previous follow-through,
  although every preceding plan promised it. Added to 2, 3, 4, 8, 9 and 10.
- **Hub sequencing.** The hub said the numbered order "follows the stages of MERIT", but
  the MERIT table maps the series through the stages twice and recommends moving 8 and 9
  early. Reworded, and added a line on what to do with the follow-through chain when a
  session is moved. The underlying tension is an owner decision (open item 1).
- Smaller wording, accuracy and voice fixes listed below.

Validators: `ruby scripts/validate_frontmatter.rb` and
`ruby scripts/validate_code_span_paths.rb` both pass.

## Issues

| Issue | File | Severity | Status | Note |
|---|---|---|---|---|
| Tomás used for three different people, including a character pressuring falsification in W8 while the W7 protagonist | charting-your-course-activity/answers, professional-conduct (all three) | High | fixed | W3 Tomás → Kai; W8 Tomás → Marcus. W7 keeps Tomás. |
| Sam and Priya (W2) reused in W8 in different roles | professional-conduct (all three) | Medium | fixed | Sam → Eli, Priya → Noor. |
| Dr. Lindqvist (W7 collaborator) reused as a grant holder | identity-and-purpose-activity.md | Low | fixed | → Dr. Novak. |
| Dr. Brandt used as PI in W4 (moving away) and W10 | future-forward-activity/answers | Medium | fixed | W10 PI → Dr. Castillo. |
| Plans 2, 3, 4, 8, 9, 10 did not open with the previous follow-through, though each preceding plan says "Start X by asking…" | resilient-scholar, charting-your-course, building-your-entourage, professional-conduct, identity-and-purpose, future-forward | Medium | fixed | One sentence added to each 0–10 min block; no timings changed. W9's is conditional ("if this session follows Professional Conduct") and kept procedural. |
| Hub claimed the numbered order follows MERIT stages; the table shows it does not | index.md | Medium | fixed | Reworded; added guidance on the follow-through chain when sessions are reordered. |
| Hub recommends running 8 early and 9 in the first month, but 8 → 9 → 10 is the written chain | index.md, professional-conduct.md, identity-and-purpose.md | Medium | open | Owner decision; see open item 1. |
| W8 outcomes said learners write an error report "about a mistake of their own"; the worksheet uses an invented mistake | professional-conduct.md | Medium | fixed | Now "for an invented mistake", and names the private rung map. |
| W9 model answer told Inés to "ask directly about credit… in writing" without saying whom; read as re-confronting the student who dismissed her | identity-and-purpose-answers.md | Medium | fixed | Now: ask her supervisor once in writing; no need to raise it with the other student again. |
| "labelling" (British) | charting-your-course-answers.md | Low | fixed | → labeling (2×). |
| "autumn" (2×), "15 November" (2×), "my post" | future-forward-answers.md | Low | fixed | → fall, November 15, my position. |
| "Fees" for doctoral programs, ambiguous and often wrong for funded US PhDs | future-forward-answers.md | Low | fixed | → application fees. |
| "Returning to doctoral study later is common", an unhedged prevalence claim | future-forward-answers.md | Low | fixed | → "possible, though harder as pay rises". |
| Proposal said "lab meeting on the 14th"; the stopping rule uses "day 14" | charting-your-course-answers.md | Low | fixed | → "at the end of the two weeks". |
| Draft A listed "the null model" as dropped, but draft A says "vs. null" | communicating-science-1-answers.md | Low | fixed | → "what the null preserves". |
| Worksheet "Peer check" step has no time in the plan (W5 duplicates the cold-reader swap; W6's bank swap is unscheduled) | communicating-science-1-activity.md, communicating-science-2-activity.md | Low | open | Fold W5's peer check into the cold-reader block; take one minute from W6's live round or drop the bank swap. |
| W8 error report (two materialization versions mixed, four-part script) closely echoes W2's bad-week report | professional-conduct-activity.md | Low | open | The script repeats on purpose (lab norms), but the error repeats too. Consider a different error kind in W8, such as a wrong unit or a wrong segment list. |
| Materialization version 1078 appears in W5, W6 and W8 | several | Info | open | Harmless, since Rosa recurs on purpose in W5 and W6. Change W8's numbers if the owner wants cases kept separate. |
| Dr. Brandt (W4) and Dr. Brennan (W7) sound alike | building-your-entourage*, savvy-researcher* | Info | open | Different people; rename one if facilitators mix them up. |
| One em dash in the W7 question | savvy-researcher.md, index.md | Info | open | Copied verbatim from the models page table; left as the canonical wording. |
| "one-to-one", "acknowledgement", "referee" | orientation-activity, identity-and-purpose-activity, savvy-researcher*, future-forward-answers | Info | open | Acceptable in American English and already used across the site; left alone. |

## Checks with no findings

- **Rubrics.** All ten have four dimensions scored 0–2, "at least 6/8 with no zero on
  dimension N", the validated-instrument sentence and a what-not-to-grade paragraph.
- **Timing.** Every plan sums to 90. Worksheet header lines and section minutes match
  the plan blocks.
- **Case details.** Numbers agree between worksheet and answers: W2 1.8→1.2-fold, 22/140
  cells, 9/60 edits, report 126 words (limit 150); W5 58 axons, 1,904 synapses, 2.7×/2.1×,
  v1078; W7 900 segments; W8 60 cells, 9 changed, v1078/1052.
- **Safety.** No section asks anyone to disclose anything aloud. W2, W8 and W9 name
  support by role, tell the facilitator to check reporting obligations, and disclaim
  counseling or ruling on real cases. W6 and W7 point to Conflict and a named person, with
  a reporting check. No model answer advises confronting a harasser. W8 scenario 5 leads
  with a private check-in with Wen and a confidentiality question to the ombuds before
  details.
- **External claims.** These were checked against known definitions and were not
  re-fetched. The ORI/PHS FFP definition and its exclusion of honest error and differences
  of opinion are paraphrased accurately, with a note that local policy may be broader.
  CRediT has 14 roles, and Software, Validation, Investigation and Data curation are real
  roles. ICMJE is hedged as "criteria of the ICMJE type". Reviewer confidentiality is
  hedged as "many journals" plus "check the journal's reviewer policy". The plans quote no
  statistics or citations.
- **Links and anchors.** All targets resolve. Anchors `#professional-pathways-workshops`,
  `#authorship-and-credit`, `#escalation-when-something-is-wrong` and
  `#harassment-and-misconduct` match real headings. Cited items exist: technical-practice
  norms 21–23, meta-learning §6 EXPECTED line, Module 22 concept 7, Module 24's five roles,
  ten-working-day rule and four-to-six-week referee rule, and MERIT stages 4 and 6.

## Per-workshop verdict

| # | Workshop | Verdict |
|---|---|---|
| — | Hub | Needs owner: the sequencing decision (open item 1) |
| 1 | Orientation | Ready |
| 2 | The Resilient STEM Scholar | Ready (opener fixed) |
| 3 | Charting Your Course in Research | Ready (name, spelling, date fixed) |
| 4 | Building Your STEM Entourage | Ready (opener fixed) |
| 5 | Communicating Science I | Ready after listed fixes (peer-check timing) |
| 6 | Communicating Science II | Ready after listed fixes (peer-check timing) |
| 7 | The Savvy Researcher | Ready |
| 8 | Professional Conduct in STEM | Ready after listed fixes (names and outcomes fixed; error-scenario overlap open) |
| 9 | STEM Identity and Purpose | Ready (moment 5 advice and opener fixed) |
| 10 | Future Forward | Ready (names, voice, hedging fixed) |

## Open items for the owner

1. **Sequencing.** Decide whether the hub's advice to run Professional Conduct early and
   Identity and Purpose in the first month is the recommended path, or an exception to a
   default 1–10 order. If the former, consider renumbering so the follow-through chain
   matches the recommended order.
2. **Peer-check minutes in W5 and W6.** Fold or schedule them.
3. **W8 error scenario.** Consider a different error type from W2's version drift.
4. **Optional.** Rename Dr. Brandt or Dr. Brennan, and vary W8's version numbers.
