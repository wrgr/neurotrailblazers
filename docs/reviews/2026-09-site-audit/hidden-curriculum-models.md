# Site audit, September 2026: hidden curriculum, models, tracks, personas, core, notebooks

Area: `hidden-curriculum/**`, `models.md`, `tracks/**`, `_data/track_catalog.yml`,
`avatars/**`, `core/**`, `notebooks/connectome-quality/`, `notebooks/microns-lab/`,
`CITATION.cff`. Pass date 26 September 2026. Nothing committed.

## Summary

- 19 files edited: 12 accuracy fixes, 9 polish and link fixes, 8 voice edits and 7
  missing-content additions. Some edits count under more than one type.
- The four assigned items are resolved. See (a) to (d) below.
- No `.ipynb` was changed. The archived outputs in `assets/notebooks/` are unchanged, and
  the lab still analyzes v1507.
- Validators: `validate_frontmatter`, `validate_code_span_paths`,
  `validate_toggled_classes` and `validate_technical_evidence` all pass. `track_catalog.yml` loads.

## Assigned items

**(a) MICrONS lab live-query version.** The page no longer uses
`CAVEclient(..., version=1507)` for live queries. It now points to `version=1300` or
`version=943`, the two long-lived analysis versions. It also gives a v1507-equivalent
`timestamp=datetime(2025, 7, 31, 8, 10, 1, 117494, tzinfo=timezone.utc)` and marks that
route as untested. A new note warns that a live query at 1300 or 943 will not reproduce
the v1507 numbers. The "Why this path" paragraph now says:
- the announced 31 July 2026 expiry has passed;
- the static exports still returned HTTP 200 on 26 September 2026;
- if the exports are withdrawn, the archived outputs on the page remain the reference.

The lab's analysis version is still v1507. Re-checked this pass through the GCS JSON
API: `synapses_with_axon_proofreading.csv.gz` exists only under `v1507/`. This settles
the earlier "unverified" note that v1507 is the only version with that export.

**(b) Cervantes et al. ASEE.** Crossref resolves doi:10.18260/1-2--43271 to "Empowering
Trailblazers toward Scalable, Systematized, Research-Based Workforce Development", 2023
ASEE Annual Conference & Exposition Proceedings. The authors are Martha Cervantes,
Sydney Floryanzia, Jackie Sharp, William Gray-Roncal and Erik Johnson, and the DOI
redirects to peer.asee.org/43271. The paper describes the **CIRCUIT** program. The
abstract is in `_data/journal_papers.yml`, and the ASEE listing names eight pillars, from
holistic recruiting to career empowerment. The annotation in `models.md` had said "a
training model for new connectomics researchers". It now says CIRCUIT is a cohort-based
undergraduate research program and names the pillars. The citation keeps "Gray-Roncal"
because the published record uses the hyphen.

**(c) FlyWire "287 / 76 labs".** The number does not appear in this area. The
`lab-norms.md` sentence, already fixed, says the consortium is an author. It adds that
the member list is in the supplementary note. Checked against PMC11446842: the
supplementary note is titled "Full list of authors and affiliations of the FlyWire
Consortium".

**(d) Author name.** `CITATION.cff` now uses `family-names: "Gray Roncal"`, which matches
the lecture credit line "Gray Roncal, W. (2026)". The only other occurrence in this area
is the ASEE citation, and it keeps the published hyphen. See the owner decision below.

## Changes

| File | Issue | Type | Fix (source) |
|---|---|---|---|
| notebooks/microns-lab/index.md | Live queries pointed at v1507, which is past its announced expiry | Accuracy | Now 1300/943, or a timestamp; withdrawal note added (canonical-facts §10; MICrONS versioning page; HEAD 200 on 26 Sep 2026) |
| notebooks/microns-lab/index.md | "analysing" | Polish | "analyzing" |
| notebooks/connectome-quality/index.md | CloudVolume `x = 240000` is outside the volume at mip 0 (the `em` x range is 13,824–226,816 at 8 nm) | Accuracy | Now `x = 120000`, with a note that CAVE positions are 4 nm (info files at gs://iarpa_microns/minnie/minnie65/*) |
| notebooks/connectome-quality/index.md | Flat `seg` is the v117 segmentation, but step 3 pins v1300, so the root IDs would not match | Accuracy | Now `seg_m1300` (info file confirmed, has a mesh) |
| notebooks/connectome-quality/index.md | `perturb()` takes `split_p` but never splits | Accuracy | Comment added that splits are left to the learner |
| notebooks/connectome-quality/index.md | "written against the current APIs" implied the code was tested | Accuracy | Now "not run for this page" |
| notebooks/connectome-quality/index.md | Unsupported superlatives ("most common silent bug", "almost no analysis", "most common reason", "among the strongest") | Voice | Softened to what the page can support |
| notebooks/connectome-quality/index.md | Meta-history of removed stubs; no pointer to a runnable notebook | Missing | Points to the MICrONS Real-Data Lab |
| models.md | CIRCUIT citation annotation did not match the paper | Accuracy | Rewritten from the ASEE abstract (Crossref, ASEE PEER) |
| models.md | "well-documented problem", "largely immune to coaching", "exactly where curricula are thinnest" | Accuracy | Softened |
| models.md | "The value is not the names; it is…", "not behind — they are exactly…", em-dash chains, "COMPASS naming … pathways support layer" | Voice | Rewritten as plain sentences; headings now state claims |
| models.md | CCR not expanded; Related list missing Pathways and the Hidden Curriculum | Polish/Missing | Expanded; links added |
| hidden-curriculum/belonging.md | Link to `/education/models/` (a redirect stub) | Polish | `/models/#evidence-base` |
| hidden-curriculum/index.md | Unit 08 quote did not match Unit 08 line 566 | Accuracy | Quote corrected |
| hidden-curriculum/index.md | "Pathways table lists the questions each page here answers" (it lists workshop questions) | Accuracy | Corrected |
| hidden-curriculum/index.md | No link to the syllabus maps | Missing | Pathways and syllabi bullet added |
| hidden-curriculum/reading-and-judging.md | "Roughly two-thirds of the effect was degree heterogeneity" (Unit 09's numbers give 77/137 = 56%) | Accuracy | Now states 77 of 137 excess pairs, plus 35 from distance |
| hidden-curriculum/{index,career-mechanics,lab-norms,meta-learning}.md | Page called "Education Models"; its title is "Program Models" | Polish | Renamed in links |
| hidden-curriculum/career-mechanics.md | "Dr Nguyen" | Polish | "Dr. Nguyen" (American English) |
| _data/track_catalog.yml | "grounded in the NIH BRAIN CONNECTS mentorship model" (no such published model) | Accuracy | Now "grounded in the MERIT stages and the Pathways workshops" |
| _data/track_catalog.yml | Ask an Expert described as "support from Dr. Jeff Lichtman" (it is an AI chatbot) | Accuracy | Now matches tools/ask-an-expert.md |
| _data/track_catalog.yml | "Resources connect directly to the MouseConnects dataset" (not yet released) | Accuracy | Now names the MICrONS lab; the Datasets summary says MouseConnects is unreleased |
| _data/track_catalog.yml | Research in Action did not include the MICrONS lab | Missing | Added to the Unit 09 step (+1 h, total 76 h, within 70–80) and to resources |
| _data/track_catalog.yml | Em dash and "education models page" | Polish | Fixed |
| avatars/mentor.md | Attributed a claim to the models page ("leading a lab well … is the science") that the page does not make | Accuracy | Removed; replaced with a plain statement |
| avatars/{mentor,gradstudent}.md | "models-in-practice playbook" | Polish | "Program Models page" |
| avatars/gradstudent.md | "Connectome Quality notebooks" linked to the tool page | Polish | Now links to /notebooks/connectome-quality/ |
| avatars/undergradstudent.md | Said the personas page is where the path to mentorship runs | Accuracy | Now the Career track and the MERIT stages |
| avatars/researcher.md | "this was the next frontier" | Voice | Plain sentence |
| avatars/*.md | Nav label "All Avatars" while the section is called personas | Polish | "All personas" |
| avatars/index.md | Jargon intro and description | Voice | Plain intro that says the personas are invented; link to the Facilitator Guide |
| core/index.md | "around 17,000 words" of proofreading reference (the five pages total about 15,200 words including markup) | Accuracy | "about 15,000 words" |
| core/index.md | "Pick a mode" linked to /start-here/ | Polish | /modes/ |
| core/index.md | Em-dash aside "(eventually)" | Voice | States the third mode is described but not built |
| core/connects-ecosystem.md | Did not list syllabi, the assessment bank, answer keys, Pathways or the MICrONS lab | Missing | Added to the relevant bullets |
| tracks/index.md | "not because it is built" construction | Voice | Rewritten |
| CITATION.cff | Surname hyphen inconsistent with the lecture credit line | Polish | "Gray Roncal" |

Also verified with no change needed:
- Award numbers UM1NS132250, U24NS139927 and U24NS140384 (NIH RePORTER).
- The ten Pathways workshops, the twenty-six technical-practice norms and the nine units' ~31 h.
- All 25 modules have session kits, and each kit has a "Naming the norm" section.
- The Unit 01/04/05/09 quotes and the Module 02 Parts A–D claims.
- Lopatto 2007, Duckworth 2007 and Fadel et al. 2015.

## Needs owner decision

1. **Surname site-wide.** Published papers use both forms: Crossref has "Gray-Roncal"
   (ASEE 2023) and older papers have "Gray Roncal". The lectures, the decks and now
   `CITATION.cff` use "Gray Roncal". `tools/connectome-quality.md:85`,
   `neuronauts/index.html:2291` and `datasets/mouseconnects.md:183` use "Gray-Roncal".
   Pick one form for the site's own credit lines. Published references should keep
   whatever the publisher printed.
2. **CITATION.cff given name.** It says "Will". A formal citation may want "William R.".
3. **MERIT expansion.** "Mentoring Exceptional Researchers to Innovate and Thrive" has no
   external source this pass could find. Confirm it is the program's own name.
4. **CIRCUIT and NeuroTrailblazers.** `models.md` cites the CIRCUIT paper but does not
   say how the two programs are related. Add one sentence if there is a lineage.
5. **Live timestamp route for v1507.** The MICrONS lab now suggests a `timestamp=` query.
   Nobody has tested whether the public datastack serves live queries at that timestamp
   to an ordinary token.

## Outside my area

- `tools/connectome-quality.md:85`, `neuronauts/index.html:2291` and
  `datasets/mouseconnects.md:183`: surname form (see decision 1).
- `course/units/09-connectome-analysis-neuroai.md:98` lists `/education/models/`, which
  is a redirect. Use `/models/`.
- `teaching/facilitator-guide.md` and other pages may still call the page "education
  models" or "models-in-practice playbook". Its title is "Program Models".
- `_data/journal_papers.yml:24967` (CIRCUIT abstract) contains "cutting-edge". That is a
  verbatim abstract, so leave it unless abstracts are being edited.
- `notebooks/microns-lab/requirements.txt` says "Tested with Python 3.13". The page says
  3.11 and 3.13. The file is in my area but was left alone to keep the pinned artifact
  byte-stable. Update it at the next rerun.
