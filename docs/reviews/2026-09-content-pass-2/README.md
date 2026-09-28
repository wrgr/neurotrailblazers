# Content pass 2 — 27–28 September 2026

Authoring the missing content from the work plan, grounding the claims the September audit
left open, and smoothing navigation. Same rule as the audit: **nothing fabricated**. Every
page's sources are logged in the report beside it.

| Area | Report | What landed |
|---|---|---|
| New reference pages | [content-library-finish.md](content-library-finish.md), [microns-case-study.md](microns-case-study.md) | Beyond EM (ExM, LICONN, X-ray nanotomography, array tomography, MAPseq/BARseq, diffusion MRI); MICrONS case study rewritten (co-registration, unit matching, what calcium data licenses); provenance-and-versioning and neuron-type identification expanded, the worked example using the MICrONS lab's real archived outputs |
| Hidden curriculum | [funding-and-jobs.md](funding-and-jobs.md) | New Funding and jobs page, every figure quoted from a dated official source (NIH activity codes, NRSA stipend notice NOT-OD-26-044, RePORTER, NSF, ERC, HHMI, Wellcome) |
| Modules | [modules-01-11.md](modules-01-11.md), [modules-12-25.md](modules-12-25.md) | "Why this module matters", "does not cover" and "common errors" sections; five misconceptions for 20–21; Crossref-verified reference lists; Module 22 retitled *Scientific Presentation*; scope cross-links between modules and units; where each module's declared hours go |
| Answer keys | [answers-batch-2.md](answers-batch-2.md) | Eleven module keys now (02, 08, 17, 19, 20, 21, 22, 25 added), every computed value rerun from the kit files |
| Teaching | [teaching-gaps.md](teaching-gaps.md) | Instructor FAQ (35 questions), 46 unit assessment items with answers, a two-day workshop map, pacing notes |
| Concept Explorer | [concepts.md](concepts.md) | 12 → 61 concepts covering the units, library and teaching layer; fact-checked against target pages |
| Grounding | [grounding-sweep.md](grounding-sweep.md) | 45 open items closed: 13 sourced, 14 relabeled with their basis, 2 removed, 13 confirmed, 3 left for the owner |
| Navigation | [navigation.md](navigation.md) | Menus regrouped; breadcrumb and previous/next on every sequence; "Last reviewed" dates from git history; What's New page; crawl found no dead ends |

Also: notebook placeholder folders removed; teaching footers aligned to the repository
LICENSE (CC BY 4.0; CC BY-SA only for the lecture decks that carry their own LICENSE).

## Verification

All ten content validators, the full build, internal links, 499 cross-page anchors, the
browser smoke suite (including the new menu items, breadcrumb and previous/next), the
layout suite on 58 pages at 320–1440 px, and 841 rendered slides pass.

## Needs owner decision

1. **Lecture page licenses.** `teaching/lectures/*` still say CC BY-SA 4.0 for the lecture
   *and its worksheet and answers*. The decks are CC BY-SA by their own LICENSE files; the
   worksheets and answers are site content, which the repository LICENSE puts under CC BY
   4.0. Pick one for those pages.
2. **Third-party figures.** Sheng & Kim 2011 Fig. 3 (© CSHL Press) and the SynapseWeb
   astrocyte image (no license stated) are labeled honestly; seek permission, replace, or
   keep for internal teaching only.
3. **Kasthuri 2015 volume.** The site now says "up to about 1,500 µm³ (as cited by Motta et
   al. 2019)"; replace with Kasthuri's own figure if someone can read the *Cell* full text.
4. **CIRCUIT.** Its acronym expansion and an evaluation-toolkit description had no source
   and were removed; restore only with a citation.
5. **Pat Rivlin credits.** Marked "attribution as given in the source deck; not
   independently verified"; confirm.
6. **NIH funding links on /connectivity/.** Two redirect to a landing page and one could
   not be confirmed; now caveated. Keep, repoint or remove.
7. **Tutorial figures.** A confirmed false split and orphan still need rendering.
8. **Two-day map, last slot.** Filled with a revision studio that has no packaged plan.
