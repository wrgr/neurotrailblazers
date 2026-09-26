# Site audit — 26 September 2026

A full pass over the site for accuracy, polish, voice and missing content, run under the
owner's rule **"Nothing fabricated"**: no invented number, result, quote, figure number or
claim may be attributed to a real dataset, release, paper, lab, person, organization or
tool. Invented teaching data is labeled synthetic and uses fictional names (releases carry a
"T" prefix, such as release T18).

Two fabrication audits ran first (`../2026-09-fabrication-audit-pages.md`,
`../2026-09-fabrication-audit-modules.md`). A verified registry of dataset facts followed
([canonical-facts.md](canonical-facts.md)); every later pass aligned to it. The area passes
then ran in parallel, each writing its own report.

| Area | Report | Main findings |
|---|---|---|
| Front door and site shell | [front-door.md](front-door.md) | Four DOIs resolving to unrelated papers; misattributed initiatives; wrong funding project name |
| Neuronauts and side quests | [neuronauts-side-quests.md](neuronauts-side-quests.md) | Wrong NEURD citation; EyeWire counts and findings; arithmetic errors in scale comparisons |
| Datasets and tools | [datasets-tools.md](datasets-tools.md) | MouseConnects method and unsourced named leads; dead access links; licenses added |
| Modules (25) | [modules.md](modules.md) | Misconceptions printed as correct beliefs in 22 worksheet and kit lines; nonexistent citations |
| Graduate and unit decks | [decks.md](decks.md) | A 1,000× storage error on the template; merge-error direction aligned; British spellings |
| Technical course | [technical-course.md](technical-course.md) | Merge-error claims; dictionary definitions stated backwards; arithmetic in worked examples |
| Content library, group 1 | [content-library-1.md](content-library-1.md) | MICrONS imaging modality and proofreading tools; H01 "first" claims; staining gradients |
| Content library, group 2 | [content-library-2.md](content-library-2.md) | About 350 fixes; new comparative-connectomics page; invented CAVE schema and igraph call |
| Journal papers and paper data | [journal-papers.md](journal-papers.md) | Invented "Key figures" lists; invented co-author names in the 2,000-paper data |
| Corpus propagation | [corpus-propagation.md](corpus-propagation.md) | Fixes carried into the corpus so a rebuild no longer reverts them; 117 years corrected |
| Hidden curriculum, models, tracks, notebooks | [hidden-curriculum-models.md](hidden-curriculum-models.md) | Invented "mentorship model"; a nonexistent *Cell* reference; MICrONS lab live-query version |
| Teaching | [teaching.md](teaching.md) | Outside-hours claim in the syllabi; lab timing; kit omissions now stated as choices |
| Pathways workshops | [pathways.md](pathways.md) | Model answers contradicting their own cases; ORI finding requirements |

Removed site-wide: 31 `reference_images` front-matter blocks that pointed at images that
never existed and no layout rendered, several with captions asserting results.

## Verification

All ten content validators, the full Jekyll build, the internal-link audit, the
cross-page anchor audit, the browser smoke suite, the layout suite at 320–1440 px, and a
rendered-slide check of all decks (no text outside slide bounds, no broken images) pass.

## Needs owner decision

Collected from the area reports; each report has the detail.

1. ~~**Hemibrain license.**~~ *Decided 26 September: be conservative.* The site treats
   the hemibrain as CC BY-NC 4.0 (noncommercial) until Janelia confirms which license
   governs, and still names both sources.
2. ~~**Your name.**~~ *Decided 26 September: keep the hyphen.* The site's own credit
   lines (`CITATION.cff`, lectures, decks, license files) use "Gray-Roncal"; published
   citation records keep the form the publisher printed. Still open: "Will" or
   "William R." as the given name in `CITATION.cff`.
3. **MouseConnects roles.** Named leads without a public source were removed. Restore any you
   can cite; choose "Johns Hopkins APL" or "Johns Hopkins University" for your own card.
4. **Funding links on /connectivity/.** NIH redirects the BRAIN Training, K99 (diversity) and
   R25 deep links to a landing page; confirm whether those programs still exist.
5. **Templated paper notes.** The OCAR notes on journal-club cards are one of 12 texts per
   domain, now labeled as such. Keep, hide, or regenerate per paper.
6. **Corpus scope.** Some macroscale papers remain in the 2,000-paper corpus despite the
   methodology's screen; two DOIs do not match their titles (`10.1016/j.nicl.2018.06.018`,
   `10.18260/1-2--42544`); 18 expert-seed files could not be verified.
7. **Stale upstream sources.** `scripts/corpus_curation/final_selection.json` and
   `scripts/journal_papers_v2_staging.yml` still carry the old authors and years; regenerating
   from them would reintroduce errors.
8. **Figures and permissions.** Third-party figures (Sheng & Kim 2011 Fig. 3 in Unit 06; a
   SynapseWeb image in Unit 07) need reuse permission confirmed; Pat Rivlin credits unverified.
9. **Unsourced typical values** remain labeled as rules of thumb (proofreading hours per cell,
   inference passes, some textbook ranges). Cite or keep.
10. **MICrONS lab dependency.** v1507 has left the live service; its static exports still
    download. If they are withdrawn, the lab falls back to its archived outputs.
11. **Unit lecture durations.** Six unit lecture plans do not sum to their stated lengths
    (see technical-course.md).
12. **Workshop sequencing.** The Pathways hub suggests running Professional Conduct and
    Identity and Purpose early; the follow-through chain assumes the 1–10 order.
