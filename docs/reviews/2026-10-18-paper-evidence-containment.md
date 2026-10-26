# Paper evidence: first containment pass

Scope: partial implementation for #190; related to #191. Base: main at 4ae3596bfee1a8bbfd0c8c947218965cb594c4f5. Not a completed release-readiness audit.

## Findings corrected and confirmed

- Current graph.md already states that species never determines a dataset or protocol. Its drawer shows dataset/software as not recorded. The earlier assessment of the legacy ecosystem preview was stale for this source revision; do not treat it as a newly fixed defect.
- scripts/corpus_curation/fast_ocar_generator.py assigns claims by category. For example, the pipeline branch asserts improved segmentation accuracy without testing the paper's supporting text. Category templates are not publication-specific findings.
- The paper-card template exposed legacy streams and generated notes without a per-claim source gate. The graph JSON also delivered legacy generated summaries and OCAR fields.

## Changes in this patch

The shared DOI-specific evidence gate requires a contribution, reported result, test context, limitations, source URL and location, evidence basis, checker and check date. Missing or mismatched records fail closed; variables reset for each paper.

The public paper card no longer renders legacy OCAR, three-level summaries, guessed figures or stream-based dataset/method attributes and chips. Bibliographic information, abstracts, publication links and recorded citation relationships remain. Browse tags are secondary and explicitly not evidence of dataset use or methods.

The graph payload emits null for legacy generated annotations and uses only a source-checked contribution record for its optional summary. It retains papers and citation edges. This is output containment, not deletion or full regeneration of the corpus.

One source-checked example is included for Januszewski et al. (2018), DOI 10.1038/s41592-018-0049-4, using the publisher abstract at https://www.nature.com/articles/s41592-018-0049-4. This is transparently AI-assisted source checking, not expert review or full-text review.

## Verification and release status

Local command: python3 scripts/check_paper_evidence.py

PASS: one evidence record, two publication surfaces and 15 eligibility fixtures. These checks inspect source/schema and negative policy cases; they do not execute Liquid or establish scientific correctness. Full Jekyll build, rendered JSON/card checks, browser regression and production verification remain required. Local network access and the full Jekyll dependency environment were unavailable in this session.

## Still open

- Complete the 30-paper stratified source audit and record dispositions; do not mark #190 closed.
- Replace/retire category-template producers and inspect other exports and static content-library notes.
- Simplify graph.md's remaining unverified-note container and index page reading-note/expertise copy; legacy content is suppressed at the data boundary but the old interface labels remain.
- Add real Liquid/Jekyll fixture tests including sequential papers, then integrate checks with CI.
- Complete #191 citation semantics and metadata reconciliation, #192 browser/accessibility checks, and #193 editorial/visual review.
- Verify the candidate in CI before merge. No deployment is part of this patch.
