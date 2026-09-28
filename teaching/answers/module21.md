---
layout: page
title: "Module 21: model responses"
permalink: /teaching/answers/module21/
slug: module-answers-21
content_type: delivery
description: "An exemplar FAIR metadata sheet, a reproducibility checklist with a clean-room validation log, concrete limitations and a deprecation note, and a reuse friction report for Module 21, built on the Module 03 kit table."
---

[Learner worksheet]({{ '/assets/worksheets/module21/module21-activity.md' | relative_url }}) · [Module 03 kit]({{ '/assets/kits/module03/README.md' | relative_url }}) · [Session kit]({{ '/teaching/sessions/module21/' | relative_url }}) · [Module page]({{ '/modules/module21/' | relative_url }}) · [All model responses]({{ '/teaching/answers/' | relative_url }})

This page answers every section of the Module 21 worksheet in order. The worksheet
asks each learner to package their own analysis, so there is no single correct answer.
The responses below are one **invented learner's** work. Marta Ferreira (invented)
brought no analysis of her own and took the worksheet's fallback: her Module 03
notebook, run on the [Module 03 kit]({{ '/assets/kits/module03/README.md' | relative_url }})'s
offline synapse table, which is synthetic and versioned `synthetic-synapses-v1`. Every
count from that table below was recomputed from the kit file with Python's standard
library. The identifiers a real package carries (commit hash, DOI, run dates, partner's
name) are invented and marked. This page is public and suitable for formative
assessment.

The exemplar is written at the level the content plan calls **Proficient**: it meets
every Minimum line of the kit's rubric and most of the Strong lines, and each annotation
says which. It does not reuse the module's worked example (the March and September counts
against releases T21 and T27); a key that repeated it would reward copying.

In the [16-week map]({{ '/teaching/syllabi/16-week/' | relative_url }}) the package is the
learner's own methods record rather than the Module 03 notebook. The same sheet, checklist
and friction report apply.

## Before you start

Nothing beyond the two prerequisites. An acceptable question to bring is “If my notebook
runs, what else is there to do?” The 30:00 block answers it: a notebook that runs for its
author has been tested by the one person who cannot find its gaps.

## Questions this module answers

1. **What minimum metadata is needed for third-party reuse?** The five provenance
   elements (dataset release identifier, materialization number or its stated
   equivalent, code commit, environment specification, full parameter configuration),
   plus a licence, a stable identifier for the output and a README whose first section
   is the rerun path.
2. **How should dataset/code versioning be documented in publications?** In the methods
   and in every figure legend that carries a number, not only in a repository; with a
   changelog entry whenever one version supersedes another.
3. **Which reproducibility norms are implicit and must be taught explicitly?** Version
   identifiers in legends, excluded samples and failed runs named rather than hidden, a
   limitations section that names failure modes, deprecation without deletion, and the
   rule that “reproducible in principle” is not a claim until someone else has rerun the
   work cold.

## The task

**The package.** Marta's notebook loads `synapses_sample.csv` (3,000 synapses among 300
invented neurons), drops the 76 rows (2.53%) whose `post_cell_type` is blank, groups the
remaining 2,924 rows by presynaptic and postsynaptic type, and exports the ten most
frequent type pairs as `top_pairs.csv` with a bar chart, `top_pairs.png`. That CSV is
the one analysis output the sheet describes.

| Rank | Pre type | Post type | Synapses | Share of kept rows |
|---|---|---|---|---|
| 1 | L23_pyr | L23_pyr | 311 | 10.6% |
| 2 | L23_pyr | L4_exc | 188 | 6.4% |
| 3 | L23_pyr | basket | 182 | 6.2% |
| 4 | L4_exc | L4_exc | 172 | 5.9% |
| 5 | L5_pyr | L5_pyr | 157 | 5.4% |
| 6 | L4_exc | L23_pyr | 141 | 4.8% |
| 7 | L5_pyr | L4_exc | 128 | 4.4% |
| 8 | basket | L23_pyr | 125 | 4.3% |
| 9 | L4_exc | basket | 123 | 4.2% |
| 10 | basket | L4_exc | 122 | 4.2% |

The eleventh and twelfth pairs tie at 107 synapses. A top-ten needs no tie rule; the
sheet records one anyway, because the next person may ask for a top-twelve.

### 1. FAIR metadata sheet for one analysis output

| Field | Entry | Which principle or element it serves |
|---|---|---|
| Output | `top_pairs.csv` (10 rows; columns `pre_cell_type`, `post_cell_type`, `synapse_count`, `share_of_kept_rows`) and `top_pairs.png` | The unit of release is one output, not a folder |
| Title | Ten most frequent cell-type pairs in the Module 03 synthetic synapse table, version `synthetic-synapses-v1` | Findable: the title carries the data version |
| Stable identifier | Package tag `v1.0`; DOI to be minted through the institutional repository at release and written back into this sheet and the README | Findable |
| Dataset release ID (element 1) | `synthetic-synapses-v1`, file `synapses_sample.csv`, 175,514 bytes, sha256 beginning `f8bd40f456ca` as listed in the site's `assets/kits/manifest.json` | The number is meaningful only against this file |
| Materialization number (element 2) | Not applicable: a static file, not a live segmentation. The equivalent pin is the version string in `synapses_sample.meta.json` plus the file hash above. Written in the field, not left blank | A stated equivalent is an answer; an empty cell is a gap |
| Code commit (element 3) | Repository URL in the README; tag `v1.0`; commit `7d3e41af` (invented for this exemplar; the learner writes the real one) | Without it the URL points at code that keeps changing |
| Environment (element 4) | `environment.yml` exported from the run: `python=3.11.9`, `pandas=2.2.2`, `matplotlib=3.9.1`, build strings removed (see friction F2) | “Python 3.11” is not an environment |
| Parameters (element 5) | Exclusion: rows with blank `post_cell_type` dropped (76 of 3,000). Grouping key: (`pre_cell_type`, `post_cell_type`). N = 10, sorted by count, descending. Tie rule: alphabetical by pre then post type (not needed at N = 10; the 11th and 12th tie at 107). No random seed: the pipeline has no stochastic step. `size_vx` unused: no size threshold applied | Every value the result depends on, including the ones left at default |
| Access | Public repository; data and figures under the site's content licence (CC BY 4.0, per the repository `LICENSE`), code under MIT | Accessible: a licence is part of access |
| Formats | CSV with a header row, UTF-8; PNG; JSON metadata; `environment.yml` | Interoperable: nothing proprietary |
| Machine-readable metadata | `top_pairs.meta.json`: dataset version and hash, parameters, run date (2026-09-14, invented), operator, commit | Reusable |
| Provenance chain | Kit README → `synapses_sample.meta.json` → notebook header cell → `make_top_pairs.py` → output and its metadata | Reusable: each link names the next |
| Limitations | Section 3 of this package, five lines | Reusable: says what the output cannot support |
| Changelog | `CHANGELOG.md`; entry for `v1.0` and a deprecation note for `v0.9` | Reusable across versions |

**Why this meets the rubric.** All five provenance elements are present (Minimum line 1),
and the one that does not literally apply says what stands in for it and why. An external
reader can find every element from the README alone, because the README's first section
is the rerun path and its second is this sheet (Strong line 4). Version identifiers go
into the figure caption, not only the metadata file (Strong line 2). **ID churn** is not
exercised: the package pins one static version, so no identifier crosses versions, and the
sheet says so. If the analysis were rerun against a later kit version, the sheet would
report how many of the 300 `pre_root_id` and `post_root_id` values map one to one
(Strong line 3, stated rather than demonstrated).

**A weak version, and what is missing.**

> Data: the synapse table (latest). Code: see the repository. Environment: Python 3.
> Parameters: defaults. Licence: not stated.

“Latest” makes the number undated. “See the repository” points at moving code. “Python 3”
names no package versions. “Defaults” hides the exclusion rule that removed 76 rows. Four
of the five elements are absent, so this fails Minimum line 1 before anyone tries to rerun
it.

### 2. Reproducibility checklist with pass/fail criteria, and the validation log

Each check has a criterion a peer can apply without asking the author. The two result
columns are the release candidate and the release.

| # | Check | Pass criterion | How tested | `v1.0-rc1` | `v1.0` |
|---|---|---|---|---|---|
| 1 | Dataset pinned | Version string and hash in README and `top_pairs.meta.json`; `shasum -a 256` on the file matches | Peer runs the command | Pass | Pass |
| 2 | Code pinned | Tag and commit in README; `git describe` on the checkout matches | Peer runs the command | **Fail**: README named the branch, not a commit | Pass |
| 3 | Environment builds | `conda env create -f environment.yml` succeeds on a different operating system | Peer builds it | **Fail**: macOS build strings | Pass, after re-export with `--no-builds` |
| 4 | Rerun from README alone | Peer produces `top_pairs.csv` and `diff` against the shipped file is empty | Cold rerun | **Fail**: path assumed the working directory | Pass |
| 5 | Parameters complete | Every rule and threshold in `top_pairs.meta.json`; the script reads them from that file, not from literals | Peer reads the script | Pass | Pass |
| 6 | Row counts logged | Script prints rows loaded (3,000), dropped (76), kept (2,924); log matches | Peer compares | Pass | Pass |
| 7 | Version in the legend | Caption carries `synthetic-synapses-v1` and the commit | Peer reads the caption | **Fail** | Pass |
| 8 | Limitations concrete | Names excluded rows, failed runs and the one parameter the result is most sensitive to | Peer reads | Pass | Pass |
| 9 | Changelog and deprecation | Entry for this version; policy for the superseded one | Peer reads | Pass | Pass |
| 10 | Cold rerun by someone else | Friction log attached, with fixes ordered by cost | This log | Pass (Tomas Petrov, invented, 2026-09-16) | Pass |

**Validation log** (the partner's clean-environment rerun of `v1.0-rc1`; every entry is
invented to show the form):

| Friction | Cost to fix | What happened | Remediation |
|---|---|---|---|
| F1 | 5 min | The README's rerun command assumed the working directory was the package root. Run from elsewhere, `FileNotFoundError` | Resolve the data path relative to the script's own location; add the `cd` line |
| F2 | 20 min | `environment.yml` carried macOS build strings; `conda env create` failed on Linux | Re-export with `--no-builds`, keeping exact versions |
| F3 | 30 min | “Run the notebook” did not say which kernel, or that the metadata cell must run before the export cell | Move the steps into `make_top_pairs.py`; keep the notebook as narrative; the README names the script |
| F4 | Not fixed, logged | The PNG regenerated with a different font on Linux; CSV byte-identical, PNG not | Reproducibility criterion is on the CSV; the figure check is visual. Recorded in check 4 as a stated choice |

Remediations were applied in cost order, F1 to F3. F4 is a decision, not a gap: the
checklist says what the byte-identity criterion covers and what it does not.

**Why this meets the rubric.** The rerun instructions were tested by a peer who could not
contact the author (Minimum line 2). The rerun was actually attempted, and the friction
log is ordered by cost (Strong line 1). Three of ten checks failed on the release
candidate, which is the honest result the module predicts for a first audit.

**A weak version, and what is missing.** “Checklist: the notebook runs end to end from a
restarted kernel: yes.” One check, run by the author, on the author's machine. No
criterion a peer can apply, no second person, no record of what failed. It is the
misconception that a notebook that ran once is proof of reproducible science, written as
a checklist.

### 3. “Known limitations” section and one deprecation note

**Known limitations (five lines).**

1. The table is synthetic teaching data; the kit's README says no result computed from it
   is a finding about a brain. This package exists to show the packaging, and its numbers
   should not be quoted as biology.
2. 76 rows (2.53%) with a blank postsynaptic type were excluded. The largest excluded
   group, 22 rows presynaptic from `L23_pyr`, is far below the tenth-ranked pair's 122,
   so no excluded group would enter the top ten under any labeling.
3. Ranks 9 and 10 are one synapse apart (123 and 122), and ranks 11 and 12 tie at 107. A
   single-row change to the table could swap the last two ranks. The headline pair
   (311) is not sensitive.
4. The ranking is by synapse count, not by connected neuron pairs. In this table almost
   every synapse sits on its own neuron pair (311 synapses on 300 pairs for the top type
   pair), so the two rankings coincide; on real data they would not, and the CSV does not
   report the pair count.
5. One run was discarded (2026-09-12, invented): the exclusion rule was applied after
   grouping instead of before, producing a `L23_pyr → (blank)` row. The failed run and
   its log are kept under `runs/failed/`, and this line is why the script now filters
   before grouping.

**Deprecation note** (from `CHANGELOG.md`):

> **v1.0 (2026-09-16) supersedes v0.9.** v0.9 was the notebook-only draft shared on
> 2026-09-10. It remains available at its tag and is not deleted. Do not cite it: its
> README did not state the exclusion rule, its figure caption carried no version, and its
> environment file carried build strings that do not resolve off macOS. Its output CSV is
> identical to v1.0's. What changed is what the package can prove about itself.

**Why this meets the rubric.** Every limitation names a concrete failure mode, an
excluded sample or a failed run (Minimum line 3). The changelog and deprecation note are
present and the old version is kept rather than erased (Strong line 2).

**A weak version, and what is missing.** “Results may be affected by data quality and
should be interpreted with caution.” No excluded row, no failed run, no sensitive
parameter, no number. It guides no one, and it is the boilerplate the rubric's failure
list names.

### 4. Peer-test another team's package for reuse friction

Marta's friction report on Tomas's package (invented). His Module 03 notebook computes a
per-neuron synapse-count histogram from the same kit table.

**What reproduced.** The summary statistic in his notebook, a mean of 10.0 synapses per
presynaptic neuron (median 10, maximum 19, 300 neurons), matched a cold rerun exactly.
The exported CSV matched byte for byte.

**What did not, ordered by cost to fix.**

| # | Cost | Friction | Recommendation |
|---|---|---|---|
| 1 | 2 min | The header cell records the dataset as “synthetic kit” with no version string | Write `synthetic-synapses-v1` and the file hash from the manifest into the header and the metadata JSON |
| 2 | 5 min | `requirements.txt` pins pandas but not matplotlib | Pin it; a different matplotlib default changed the bin rendering |
| 3 | 15 min | The histogram's bin count lives in a cell edited after the PNG was exported: the shipped figure has 20 bins, a rerun produces 15 | Move the bin count to the parameter cell, re-export, and record it in the metadata |
| 4 | 20 min | The README has no rerun section; the order of cells is the only instruction | Add a “Rerun” section as the first heading: environment, command, expected outputs |

**Verdict.** Reproducible after items 1 to 4, none of which needs the author. The
figure discrepancy (item 3) is the one that would have misled a reader: the shipped PNG
is not the output of the shipped code.

**Why this meets the rubric.** The report is specific enough to act on without a
conversation, and the recommendations are ordered by cost (Strong line 1 applied to
someone else's work).

## Working checklist

Define release scope: the package section above (one output, one tag, one parameter set).
Machine-readable metadata: `top_pairs.meta.json` in the sheet. Validate the rerun path:
checklist rows 3, 4 and 10, with the friction log. Methods and limitations notes: section 3.
Publish with changelog and deprecation policy: the `CHANGELOG.md` entry. No step was
skipped; the step that did not literally apply (materialization number) says why.

## Evidence and reasoning

| # | Claim | Evidence | Limitation / what would change my mind |
|---|---|---|---|
| 1 | A stranger can regenerate `top_pairs.csv` from the README alone. | Tomas's cold rerun of `v1.0` produced a byte-identical CSV after the F1–F3 fixes. | One rerun on one other operating system. A Windows rerun could expose a path or line-ending problem. |
| 2 | All five provenance elements are present. | The sheet fills each, and the materialization field states its equivalent. | A reviewer might not accept a file hash as an equivalent to a materialization pin; the sheet should then cite the kit's `manifest.json` entry directly. |
| 3 | The ranking is insensitive to the exclusion rule. | The largest excluded group (22 rows) is below the tenth-ranked count (122). | Only true for a top-ten. A top-thirty would be affected, and the limitations say so. |

**Confidence:** Medium. The main claim rests on one strong line of evidence, a single
cold rerun, and the package has not yet been rerun on a third machine.

**Alternative considered and rejected:** shipping the notebook alone with a “run all
cells” instruction. Rejected because friction F3 showed that cell order and kernel are
instructions only the author knows.

## Misconception self-check

Feedback for each error:

- **Posting files online makes work FAIR.** Ask: “Which file would a stranger open first,
  and what would it tell them to run?” A folder is findable; a package is reusable.
- **A notebook that ran end-to-end once is proof of reproducible science.** Point to
  checklist rows 2, 3 and 4, which failed on the release candidate. The notebook had run
  end to end for its author the same day.
- **Reproducibility norms are common sense that any careful trainee will infer without
  being taught.** Ask which of the ten checks the learner had applied before this session.
  A learner who names version-in-legend or deprecation-without-deletion as new has
  answered honestly.

## Session timing (facilitator reference)

This section has no learner task.

- **16:00–30:00, audit your own work.** The exemplar's `v0.9` scores two of five: the
  version string was in the header cell and the parameters were in code. Missing were
  the commit, the environment file and any stated exclusion rule. Say in advance that
  two or three missing is the expected result; a five-of-five self-audit is the one to
  check.
- **30:00–40:00, clean-environment rerun.** The friction log in section 2 shows the form:
  what happened, cost to fix, remediation. Insist that the log records the failure even
  when the partner can guess the fix.
- **40:00–50:00, limitations.** Line 5 of the exemplar (the discarded run) is the one
  learners most often omit. Ask each learner for one failed run by name.

## Rubric

A self-assessment that matches this exemplar:

- **Strongest part:** the checklist, because three of its checks failed on the release
  candidate and the log shows what fixed them.
- **Weakest part:** ID churn is stated as not applicable rather than demonstrated, and
  the package has been rerun once. **Next action:** rerun `v1.0` on a third operating
  system, and, if the kit is ever reissued, map the 300 IDs across versions and report the
  churn.

## Exit prompt

Applied to a second output, the figure `top_pairs.png`:

1. **Provenance metadata.** Caption line: “Ten most frequent cell-type pairs,
   `synthetic-synapses-v1` (sha256 `f8bd40f4…`), 2,924 rows after excluding 76 with a
   blank postsynaptic type; package `v1.0`, commit `7d3e41af` (invented).”
2. **Reproducibility instructions.** Three steps: `conda env create -f environment.yml`;
   `python make_top_pairs.py --params top_pairs.meta.json`; compare `top_pairs.csv` with
   the shipped file using `diff`. The PNG is checked by eye.
3. **Limitations.** (i) Synthetic data; no biological reading. (ii) 76 rows excluded; no
   excluded group reaches the top ten. (iii) Ranks 9 and 10 differ by one synapse.
   (iv) Synapse count, not connected-pair count. (v) The PNG is not byte-reproducible
   across operating systems; the CSV is.

## Peer review (swap worksheets)

A reviewer of this exemplar should rerun `make_top_pairs.py` on the kit file and check
that the ten counts match the table above. A good question to ask its author: “If the
kit were reissued with the blank labels filled in, which of your ten ranks could change,
and how would you report the ID mapping?”

## Feedback guide

This key follows the kit's own tiers rather than a numeric score. In this key,
**Proficient** means every Minimum line met and at least half the Strong lines met, with
the remaining Strong lines named in the self-assessment as next actions.

- **Minimum pass:** all five provenance elements present, with any non-applicable element
  replaced by a stated equivalent; rerun instructions a peer tested without contacting the
  author; limitations that name excluded samples, failed runs and concrete failure modes.
- **Strong performance:** a clean-environment rerun actually attempted, with a friction
  log ordered by cost; version identifiers in figure legends, a changelog and a deprecation
  note; ID churn quantified whenever identifiers cross versions; every element locatable
  from the README alone.
- **Common failure modes:** missing version identifiers for data or code; methods that
  omit parameters or the environment; “reproducible in principle” with no rerun;
  boilerplate limitations.

Do not reward a package that passes all ten checks on the author's own machine only. Do
not reward a limitations section that is longer than the exemplar's but names nothing.
Do not penalize a learner whose materialization field says “not applicable” with a stated
equivalent, and do not accept one that is blank. Do reward a friction log that records a
failure the partner could have guessed past. This is a local teaching rubric, not a
validated assessment instrument.

See [Provenance and versioning]({{ '/content-library/infrastructure/provenance-and-versioning/' | relative_url }})
for version records and [Data formats and representations]({{ '/content-library/infrastructure/data-formats/' | relative_url }})
for the interoperable formats. Teaching material: CC BY 4.0, NeuroTrailblazers.
