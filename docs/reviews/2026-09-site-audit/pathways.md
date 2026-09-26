# Site audit: Professional Pathways workshops (September 2026)

Scope: all 31 files in `teaching/pathways/`, which are the hub plus ten workshops, each
with a plan, a worksheet and model responses. I read every file in full against the
voice exemplars (`orientation*.md`, `hidden-curriculum/lab-norms.md`) and BRAND_GUIDE §2.
I also read the earlier series review (`docs/reviews/2026-09-pathways-workshop-review.md`)
and reversed none of its fixes or the fabrication pass (the Communicating Science cases
still use "a fictional mouse cortex volume, release T12"). Nothing was committed.

## Summary

- Files edited: 26 of 31. Unchanged: `orientation-answers.md`,
  `resilient-scholar-activity.md`, `charting-your-course-activity.md`,
  `building-your-entourage-activity.md`, `future-forward-activity.md`.
- Findings: 45 table rows, all fixed. By primary type, about 20 are accuracy, 13 voice
  and 12 polish; several rows mix types. No missing content needed filling.
- Validators: `validate_frontmatter` and `validate_code_span_paths` both pass. Every one
  of the Liquid `relative_url` targets in the folder resolves to a permalink, and `{{`/`}}`
  are balanced in every file.
- Timings: all ten plans still sum to 90. Worksheet minute budgets match the plan
  blocks. No timing was changed.
- Chain: each plan opens with the follow-through from the session numbered before it.
  Workshops 5, 6 and 7 said "workshop 4/5/6" and now use the workshop name, and each
  opener now says "Take two answers", as the other seven do.
- The series was already in good shape, and the voice was mostly consistent with
  Orientation. The main problems were five internal inconsistencies in model answers
  (a model report asserting something the case had not established, wrong counts),
  two small claims about the real field inside an invented talk, and scattered
  British forms and run-on lines left by earlier inserts.

## External claims checked against the official source

| Claim | Source fetched | Result |
|---|---|---|
| FFP definition, and that it excludes honest error and differences of opinion (W8 plan, worksheet) | ori.hhs.gov/definition-research-misconduct | Matches. The worksheet's falsification gloss was loose ("manipulating ... data"). It now follows ORI's wording. |
| Requirements for a formal finding (W8 answers) | ori.hhs.gov/federal-research-misconduct-policy | The page listed only "intent, knowledge or recklessness". It now gives all three elements: significant departure, intentional/knowing/reckless, preponderance of evidence. |
| CRediT has 14 roles; Software, Validation, Investigation, Data curation are roles (W7) | credit.niso.org | Matches. |
| "Criteria of the ICMJE type": substantial contribution, drafting or revising, final approval, accountability (W7 plan) | icmje.org recommendations PDF (the HTML page returns 403) | Matches. The pathways files never quote ICMJE directly, and the hedge is accurate. |
| Reviewers must consult the editor before involving a colleague (W7 answers) | Nature Portfolio peer-review policy (via curl; COPE's page returns 403) | Supported. Kept "many journals" and added Nature Portfolio as a verified example. |

## Site-structure claims checked in the repo

All cited headings exist verbatim: belonging (*The distinction that does all the work*,
*The test*, *When the answer is that the environment is bad*, *What this page does not
cover*), meta-learning §6 EXPECTED line and §7, technical-practice Family 5 and norms
21–23, career-mechanics §§1, 2, 3, 5 (seven-line memo, the ghost-writing line, "don't
worry"), reading-and-judging Level 2 and *How to disagree proportionately*, conflict
`#harassment-and-misconduct`, lab-norms anchors. MERIT stage content on `models.md`
(stage 4 "information rather than verdict", "rehearse the hard question"; stage 5
"mentor asset"; stage 6 single-path assumption and learning outside a structured
program). Module 22 concepts 2, 6 and 7, the 4-slide/3-minute studio, and the
over-conceding line. Module 24's five roles, reversibility questions, the 4–6-week referee
rule, the ten-working-day rule and the visa/adviser line. Module 23's 90-second pitch.
The `module22-public-engagement` sentence. Unit 01 bins A–C. Personas Julian (first-gen)
and Amir (industry). The syllabus counts (3 workshops in 10 weeks, 8 in 16).

## Findings and fixes

| File | Issue | Type | Fix |
|---|---|---|---|
| resilient-scholar-answers.md | The model report said the 22 changed IDs were "mostly in the region where the large merge was fixed". The case never establishes that, and the table lists checking it as the *next check*. | Accuracy | The report now cites what Sam knows ("Priya says the new version fixed a large merge in my region"). Still 128 words, under the 150 limit. |
| resilient-scholar-answers.md | "Tuesday also reflects a process gap: no EXPECTED lines and no pinned version": pinning is Monday's problem | Accuracy | "Monday and Tuesday also point to a process gap" |
| resilient-scholar-answers.md | "It is a result, not a failure of Sam's" | Voice | Two plain sentences |
| resilient-scholar.md | Sources said two MERIT stages "ask that a first real failure be framed as information"; only stage 4 says it | Accuracy | Attributed to stage 4 |
| resilient-scholar.md | 0–10 block broken mid-sentence by an earlier insert; "afterwards" | Polish | Rewrapped; "afterward" |
| charting-your-course-answers.md | "Two of its three big unknowns": the table lists four unknowns for C, three of them knowable in two weeks | Accuracy | "Three of its four unknowns" |
| charting-your-course-answers.md | Stacked "not X" antitheses; overlong line in the proposal quote | Voice/Polish | Split into short sentences; rewrapped |
| charting-your-course.md | "Excitement is not evidence of fit. Safety is not evidence of value." (a mirrored pair); 0–10 run-on line; "afterwards" | Voice/Polish | Plainer wording; rewrapped; "afterward" |
| building-your-entourage.md | "each specific, each with..., each offering..." (anaphoric triad) | Voice | One plain sentence |
| building-your-entourage.md | Caution opened with a "not going around" denial | Voice | Reworded to name the worry, then answer it |
| building-your-entourage.md | 0–10 run-on line; "afterwards" | Polish | Rewrapped; "afterward" |
| building-your-entourage-answers.md | "Empty roles: sponsor, since only Dr. Brandt advocates" missed the point that he is leaving | Polish | Added "and he is leaving" |
| building-your-entourage-answers.md | The channel-row paragraph slightly misquoted lab norms ("public record") | Accuracy | Now "public channel", as the page says |
| communicating-science-1.md | Opener said "workshop 4" and skipped "Take two answers" | Polish | Named, and aligned with the other openers |
| communicating-science-1-activity.md | "A fictional mouse cortex volume (one electron-microscopy volume, ...)" repeated "volume" | Polish | "Fictional mouse cortex EM volume, layer 2/3, release T12." |
| communicating-science-1-activity.md | Time line said "a cold-reader swap" with no minutes; "Exit ticket" heading followed by "Exit ticket:" | Polish | "an 8-minute cold-reader swap"; "Finish both sentences:" |
| communicating-science-1-answers.md | Adjacent-scientist non-claim "whether these synapses change when the partner fires" was ambiguous | Accuracy | "affect when, or whether, the partner fires" |
| communicating-science-1-answers.md | Public version repeated "what they do / what the neighbors do"; "C, but not because of" | Voice | Rewritten; still four sentences and one number |
| communicating-science-2.md | Opener said "workshop 5"; "Module 22 ... answers two assigned questions" (Module 22 says audience questions) | Polish/Accuracy | Named; "two audience questions" |
| communicating-science-2.md | "the chair owns the clock" in a group of three with no chair | Accuracy | "The timekeeper owns the clock"; rewrapped; "afterward" |
| communicating-science-2-answers.md | Rosa's invented opener said "almost nobody has counted it at synapse resolution", and the outline said location is "rarely counted". Both are claims about the real field, and they are not true. | Accuracy | "Circuit models assume an answer. I counted them, synapse by synapse, in one volume ..." |
| communicating-science-2-answers.md | Scope repair said "one mouse cortex" | Accuracy | "one mouse cortex volume" |
| communicating-science-2-activity.md | "Exit ticket" duplicated | Polish | "Finish the sentence:" |
| savvy-researcher.md | Opener said "workshop 6"; "It is undocumented." | Polish/Voice | Named; "Nobody writes it down for students." |
| savvy-researcher-answers.md | Reviewer-confidentiality line unverified | Accuracy | Verified; Nature Portfolio added as an example |
| savvy-researcher-activity.md, -answers.md | "acknowledgement(s)" ×6 | Polish | American "acknowledgment(s)" |
| professional-conduct.md | ORI link pointed at the homepage; bold on FFP duplicated the worksheet | Accuracy/Polish | Linked to the definition page, used ORI's exact scope wording, removed the bold. 0–10 block rewrapped. "1–3" → "1 to 3" |
| professional-conduct-activity.md | Falsification gloss "manipulating materials, processes or data" departs from ORI | Accuracy | Now ORI's wording: materials, equipment or processes; changing or omitting data or results |
| professional-conduct-answers.md | A finding was said to require only intent, knowledge or recklessness | Accuracy | All three federal elements |
| professional-conduct-answers.md | Eli's option "checked 140, 60 remaining" used numbers not in the case | Accuracy | "report how many are checked and how many are not" |
| professional-conduct-answers.md | "record it in the notebook header, as in Technical practice": that page has no voxel-size norm | Accuracy | Points to the notebook header block that page describes |
| identity-and-purpose-answers.md | "five of six moments are gaps": the table has four gaps, one environment signal and one *cannot tell yet* | Accuracy | Corrected |
| identity-and-purpose-answers.md | "Her extra preparation is unpaid labor": odd framing for a student | Voice | "Five hours of preparation is a cost she can drop." |
| identity-and-purpose-answers.md | Dev paragraph was compressed and vague ("the field will notice") | Voice | Concrete consequence stated |
| identity-and-purpose-answers.md | Moment 5 advice ran two clauses together with a semicolon, around a quoted "touchy" | Voice | Short sentences |
| identity-and-purpose.md | "it cannot be installed by someone else. Specificity helps; reassurance does not." | Voice | Plainer, and ties back to the named gap. 0–10 block rewrapped |
| identity-and-purpose-activity.md | "one-to-one" | Polish | "one-on-one" |
| future-forward-answers.md | "two people have watched her work for two years, which takes two years to build" was circular, and less precise than the source | Accuracy/Voice | Paraphrases career mechanics (a letter needs someone who watched decisions over months), then the case fact: two such people, neither asked |
| future-forward-answers.md, future-forward.md | Overlong memo line; 0–10 run-on; "1–3" | Polish | Rewrapped; "1 to 3" |
| orientation.md | "none of the three is written in any lab handbook", a universal claim that cannot be checked | Accuracy | "labs rarely write any of the three down"; "afterward" |
| orientation-activity.md | "one-to-one"; "what have I got wrong?" | Polish | "one-on-one"; "what have I gotten wrong?" |
| index.md | "Modules 01, 02, 17, 19 and 22–25 already have session kits" implied the others do not; all 25 do | Accuracy | "cover overlapping themes, and each has a session kit" |
| index.md | "Orientation assumes the Module 02 playbook exists or is built first" contradicted Orientation's "this session stands alone" | Accuracy | "works best after ... but it also runs on its own" |
| index.md | Bold on "ten 90-minute workshops" | Voice | Plain sentence |

## Open items from the earlier review, rechecked

- W5 and W6 peer-check minutes: resolved before this pass. The W5 cold-reader swap is
  the peer check (64–72), and the W6 bank swap takes the first 2 of the 20 live-round
  minutes.
- W8 error scenario overlap with W2: resolved before this pass (now a voxel-size error).
- W8 version numbers: resolved, since the case no longer uses versions.

## Needs owner decision

1. **Sequencing** (carried over). The hub recommends running Professional Conduct early
   and Identity and Purpose in the first month, but the follow-through chain is written
   for 1 → 10. The hub's reordering sentence covers the gap. Renumbering would be cleaner.
2. **Em dash in the W7 question** ("How does the system actually work — funding, ...").
   Kept because it matches `models.md` verbatim. If the owner wants a colon, change
   `models.md`, `index.md` and `savvy-researcher.md` together.
3. **W2 question wording.** The hub and plan say "how do I tell a failing project from a
   failing me?"; `models.md` says "tell the difference between a failing project and a
   failing me". Pick one.
4. **Dr. Brandt (W4) and Dr. Brennan (W7)** still sound alike. This is optional.
5. **Unfillable.** Nothing required new content. The plans deliberately leave local
   specifics blank: the names of counseling, ombuds and research-integrity offices, and
   the facilitator's reporting status. Only the running institution can fill them.

## Outside my area

- `hidden-curriculum/lab-norms.md`: the week-four script says "what have I got wrong?",
  and the page uses "one-to-one", "acknowledgement" and "afterwards". Orientation now
  uses American forms, so the exemplar and the workshop no longer quote identically.
  Align lab norms, or accept the small divergence.
- `hidden-curriculum/lab-norms.md` also uses em dashes heavily (for example the
  escalation rungs and "What it does not do — because a worksheet cannot —"). It is the
  voice exemplar, but its punctuation does not match the house rule.
- `modules/module02.md` line 138 still says "the FlyWire Consortium (287 researchers plus
  volunteers)". The modules audit reports fixing the "287" elsewhere in Module 02. This
  one may remain.
- `modules/module24.md` decision table: "Returning to a doctoral program later is common".
  This is an unhedged prevalence claim. The Future Forward answers use "possible, though
  harder as pay rises".
- `models.md`: see owner items 2 and 3.
