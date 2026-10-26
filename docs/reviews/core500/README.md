# Core 500 publication-source checkpoint — 2026-10-26

All 500 ranked Core records have been reviewed in parallel. The later user instruction expanded the original paper-100 stop to paper 500. No record after rank500 was reviewed or promoted.

- Source-checked records: **500/500**.
- Targeted full-text: **468**.
- Abstract-only: **32**.
- Uncertain / withheld from public contribution notes: **34**.
- Inaccessible at both original-author-abstract and original-text level: **0**.
- Public contribution notes eligible after this pass: **466**.
- Records with a documented local/corpus source issue, including resolved recoveries: **45**.

These are AI-assisted checks of correspondence to original publications, not expert scientific review, independent replication, or factual certification of the whole 2,000-paper corpus. Source-checked includes accessible original author abstracts and source-identity checks on conflicted records. It does not certify a conflicted title–DOI pairing. Full-text means relevant original body, results, methods and limitations were inspected; reviews were checked as literature syntheses. It does not mean every paragraph, supplement, figure, code path or raw dataset was audited.

The full-text count includes one complete bibliographic correction (rank491) and a DOI-resolved original checked to establish a title–DOI conflict (rank211). Neither is promoted as independent scientific evidence for the corpus title. The abstract-only count includes rank500's unresolved identity check. Uncertain overlaps the depth categories, rather than being a third depth.

## Files and membership

[tracker.json](tracker.json) is the canonical evidence tracker, including definitions, exact membership, PDF hashes, source locators and flags. [tracker.csv](tracker.csv) is its matching filterable export. The prior first100 tracker is regenerated as the exact first100 subset; its current depth is95 full-text and5 abstract-only, with6 withheld flags.

Order is the first500 `in_top_500=true` records in `_data/journal_papers.yml`, preserving the earlier rank100 boundary at DOI10.1016/j.cub.2019.03.070. It is not `_data/corpus_500.json` order, a representative sample, or a quality ranking. The corpus file's SHA-256 is pinned in tracker metadata. Rank500 is preserved as recorded, even though its bibliographic pairing is flagged.

Each row records demonstrated contribution or identity-only finding, reported result, test context, limitations, original-source URL/locator, access depth, reviewer/date, uncertainty, dataset evidence, and local/recovered provenance. Incorrect local PDFs, errata, supplements and different versions were not silently treated as target main publications. Full texts remain in the existing local collections; the PR contains paraphrases, hashes, locators and short verification excerpts, with no complete subscription texts or signed download URLs.

## Priority issues for user review

- **211:** corpus title says traumatic brain injury, while the DOI/local original identify a schizophrenia auditory-hallucination connectivity paper. Those findings are not attributed to TBI.
- **500:** the SwarmAI title belongs to [ASEE DOI42515](https://peer.asee.org/a-swarmai-testbed-for-workforce-development-and-collaborative-interdisciplinary-research); recorded DOI42544 identifies a Summer Robotics paper. No scientific contribution is published for that mixed record.
- **491:** recorded DOI is a [published erratum](https://pmc.ncbi.nlm.nih.gov/articles/PMC5997456/), correcting a reference in the original review already represented at493. The stored PDF duplicates that original review. It is not counted as a second scientific review.
- **79:** the dated bioRxivv1 PDF reports3,063 adult/1,020 larval lines, while the publisher API repeats3,060/1,373 across its version entries. Historical abstract correspondence remains unresolved. The dated PDF was used and the note withheld pending reconciliation.
- Remaining flagged records involve wrong publications, different source versions, or supplementary/reporting-summary-only files. Filter `uncertain=true` to inspect all34. Eleven additional source issues were resolved or bounded sufficiently for use, with their history retained.

No bibliography corrections or inclusion/de-duplication decisions have been silently applied to the original corpus. Flagged rows remain available in the tracker and are absent from public evidence. Normal study limitations remain explicit even for unflagged rows.

## Dataset and claim discipline

Named dataset use is recorded only when explicit original Methods, Results or Data availability establishes actual use. Examples include the narrow MICrONS Phase1 attribution at83 and source-supported multi-area MICrONS analyses elsewhere. SEM, organism, tags and citation proximity were never treated as dataset-use evidence. “Not established” means unknown in the reviewed passages, not proof of absence. Resource papers, reviews, models, associations and causal interventions are distinguished in their notes.

The first100 draft abstracts received independent cross-checks. The full500 merge also received targeted independent checks of high-risk identities, versions, errata, numerical claims and named datasets; resulting provenance/wording issues were corrected. This was not a second complete scientific reading of all500.

## Validation

Validation results and the tested revision are recorded in PR194's coverage comment. The checkpoint validator compares exact corpus order, CSV/JSON values, depth/access flags, counts and public-note eligibility. The evidence schema/unit tests and actual Jekyll output checks verify isolation of evidence across2,000 cards/graph records,5,460 recorded directed citations and three safe exports. Browser checks exercise the existing site journeys and publication interfaces.

On macOS only, the local Jekyll configuration excludes the raw `LICENSE` static asset because it collides with the rendered `/license/` directory on a case-insensitive filesystem. The license page remains in the preview. Repository configuration is unchanged; Linux CI uses the normal configuration.

PR remains draft. No merge or production deployment is part of this checkpoint. Stop at500 for user review.
