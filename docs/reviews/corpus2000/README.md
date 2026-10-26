# Full 2,000-record original-source review checkpoint — 2026-10-26

The authorized review now covers all 2,000 corpus records. The earlier first 500 checkpoint was committed before this extension and is preserved exactly. The additional 1,500 were reviewed in parallel independent batches using local original PDFs and publication-source recovery where needed.

## Coverage

All 2,000 records: **1999 source-checked**, **1889 targeted full-text**, **110 abstract-only**, **114 uncertain/withheld**, **1 inaccessible**, **1886 eligible public contribution notes**.

New 1,500 records only: **1499 source-checked**, **1421 targeted full-text**, **78 abstract-only**, **80 uncertain/withheld**, **1 inaccessible**, **1420 eligible public notes**.

Prior 500 remain **468 targeted full-text**, **32 abstract-only**, **34 uncertain/withheld**. Uncertain overlaps review depth; it is not an additional depth category. Local/corpus source issues are documented on **167 records**, including resolved recoveries and harmless neighboring journal material.

Source-checked includes original-author abstracts and source-identity checks on conflicted records. Rank 1902 explicitly uses a verified author-preprint companion abstract with target-conference bibliographic identity checked, because the final IEEE abstract/body were unavailable; that version uncertainty remains flagged and withheld. It does not certify a mixed title–DOI pairing. Full-text means targeted relevant original body, results, methodological context and limitations were inspected, not exhaustive reading of all paragraphs, supplements, figures, code or raw data. Full-text counts include complete corrections and original sources inspected to establish identity conflicts; those are not new independent scientific studies. These are AI-assisted correspondence checks, not expert review or independent replication.

## Evidence files and order

[tracker.json](tracker.json) is canonical and [tracker.csv](tracker.csv) is its matching filterable export. Each row records contribution or identity-only finding, reported result, test context, limitations, source URL/locator, access depth, reviewer/date, uncertainty and dataset evidence. Provenance includes original local PDF checksums, extraction correspondence and recovered-source information where applicable.

Review order preserves the original first 500 `in_top_500=true` records in `_data/journal_papers.yml` order, followed by the other 1,500 in their original corpus order. The source corpus SHA-256 is pinned. Review rank is a tracker locator, not a quality ranking. [First 500 checkpoint](../core500/README.md) and [first 100 checkpoint](../core500-first100/tracker.json) remain historical exact subsets.

## Source and claim discipline

- Original headers/title/authors/DOIs were checked against requested records; filenames, cached metadata and PDF checksums alone do not establish article identity.
- Cached PDF-object data and missing text were bypassed using direct PDF extraction. Stale extracts were checked against actual PDF bytes. Unreadable artifacts are not treated as full-text evidence.
- Wrong articles, supplements, reporting checklists, earlier/later versions and duplicate-file substitutions retain source flags. Correct original-author abstracts support conservative explicitly abstract-only fallbacks when original main text cannot be reviewed.
- A repeated PDF can be authentic for one DOI and wrong for another. A multipaper journal file can support a targeted review if the correct original portion is identified and isolated.
- Missing local PDFs are recorded separately from inaccessible original publications. Author abstracts can establish abstract-only source access even when local main text is absent.
- Normal study limitations remain explicit for eligible notes. Reviewer cautions are distinguished from limitations explicitly stated by authors. Resource/tool demonstrations, review syntheses, model predictions, structural associations and causal interventions are not interchangeable.

Named dataset attribution requires explicit original Methods, Results or Data availability establishing actual use. SEM, organism, topic tags, citations, funding and distance units do not establish MICrONS use. The small P36L2/3 volume is distinguished from the later multi-area mm3 resource, and hosting/deployment is distinguished from scientific analysis. “Not established” means unknown in reviewed passages, not evidence of absence. Targeted independent checks caught and corrected dataset/provenance omissions; no second complete scientific reading of all 2,000 is claimed.

Filter `uncertain=true` for all unresolved rows. Earlier priority flags include rank 211's TBI/schizophrenia title–DOI conflict, rank 500's SwarmAI/ASEE mismatch, rank 491's correction-only/duplicate artifact and rank 79's historical-preprint abstract disagreement. New issues include rank 1597’s complete correction notice under the main-study title, wrong scientific articles under target filenames, preprint/journal substitutions, supplement-only files and absent/truncated bibliographic titles. Original bibliography and inclusion decisions are retained for user review, without silently replacing entries.

Only eligible DOI-specific contribution notes enter `_data/paper_evidence.json`; all uncertain/inaccessible records remain withheld. Existing metadata/abstract display remains governed by the PR's earlier containment policy. Original full texts stay in local collections. The PR contains paraphrases, hashes, locators and short verification quotations, without full subscription texts or signed download URLs.

## Original papers and corrections

Verified reciprocal links connect original papers with their correction notices, with full-text and PDF links where available. These bibliographic relationships appear on cards, the citation graph, review prompts and safe exports, including correction records whose scientific contribution notes are withheld. Imported main-paper abstracts are not presented as correction abstracts. An unchanged open-access correction PDF is included with its source license and checksum; the original study PDF is linked through the NSF Public Access Repository. Additional correction notices outside the 2,000 selected records are linked for context, not counted as newly reviewed corpus records. Publication relationship data are included in tracker.json and `_data/paper_publication_links.json`.

## Validation and boundary

The checkpoint validator checks all 2,000 exact members/order, CSV/JSON equality, access-depth/status flags, counts, provenance fields, publication eligibility and exact preservation of the first 500/100. Evidence schema/unit tests and actual Jekyll rendering audit all 2,000 cards/graph records, 5,460 recorded directed citation links and three safe exports. Browser, layout and link checks exercise the existing publication interfaces and site journeys. Test results and exact final revision are recorded in the follow-up draft PR's final coverage comment.

The macOS local build excludes the raw `LICENSE` static asset because it collides with the rendered `/license/` directory on a case-insensitive filesystem. The license page remains; Linux CI uses normal repository configuration. Ruby 3.1.6 CI build jobs use compatible Ubuntu 22.04 runners.

Stop after the 2,000 corpus records for user review. PR #194 was merged externally while this extension was in progress. The remaining 1,500 reviews and correction links are submitted in a follow-up draft PR; this extension includes no main-branch merge or production deployment.
