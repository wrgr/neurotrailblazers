# Streamlined QA/QC Plan for Connectomics Bibliography

## Overview

This document outlines the post-collection quality-assurance and corpus-enhancement workflow that transforms a raw OpenAlex corpus into a curated reading list. The workflow emphasizes **statistical justification** for every inclusion decision and **transparent documentation** of criteria.

**Key principle:** Accept algorithmic decisions (duplicates, author merges, domain classification) where confidence is high; flag ambiguous cases for human review; only add new papers when they meet quantitative thresholds.

---

## Phase 1: Duplicate Detection & Merging

### Goals
- Consolidate preprint/published pairs
- Merge corrupted/split records
- Prevent citation inflation from multiple DOIs

### Workflow

#### Step 1A: Multi-Signal Duplicate Screening

**Script:** `12_dedup_review.py` (part 1)

**Input:** `output/graphs/citation_graph.json` + `output/corpus_merged.json`

**Method:** For each pair of papers in the corpus, compute 5 weighted signals:

| Signal | Weight | Notes |
|--------|--------|-------|
| Title similarity (fuzzy string match) | 0.35 | Fast, high precision for exact duplicates |
| Citation neighborhood Jaccard | 0.25 | Do they cite/are cited by the same papers? |
| Author overlap | 0.15 | Shared authors (controlling for common names) |
| Mutual non-citation | 0.15 | If A and B have identical years, likely same paper |
| Preprint DOI pattern | 0.10 | `arXiv.org, biorxiv.org` IDs suggest preprint |

**Confidence threshold bins:**
- `≥ 0.70`: AUTO_MERGE — very high confidence (e.g., bioRxiv + published versions)
- `0.50–0.70`: LIKELY_DUP — human review recommended
- `0.40–0.50`: REVIEW — ambiguous, flag for inspection
- `< 0.40`: LOW — probably distinct papers

**Output:** `output/duplicate_review.tsv` (1,425 pairs)
- Columns: paper1_id, paper2_id, score, signal_breakdown, confidence_category, **[decision column (blank for review)]**

**Action:** Use spreadsheet software to review and accept/reject recommendations. Mark decisions in TSV.

#### Step 1B: Apply Duplicate Merges

**Script:** `12_apply_duplicate_merges.py` (to be written)

**Input:** 
- `output/duplicate_review.tsv` (with human decisions)
- `output/corpus_merged.json`
- `output/graphs/citation_graph.json`

**Process:**
1. For each ACCEPTED merge: consolidate to canonical paper (usually the published version)
2. Transfer citation edges: if A→B and A→B' (duplicate), merge to A→canonical_B
3. Sum citation counts and co-authorship weights
4. Update corpus and all derived files (rankings, reading_list, etc.)

**Output:** 
- `output/corpus_deduplicated.json`
- Updated citation graph with merged nodes
- `output/duplicate_merge_log.json` — what was merged, impact on top-500

---

## Phase 2: Author Name Disambiguation

### Goals
- Consolidate author name variants (hyphenation, abbreviations, unicode)
- Fix co-authorship network accuracy
- Elevate prolific authors in rankings

### Workflow

#### Step 2A: Multi-Signal Name Variant Detection

**Script:** `12_dedup_review.py` (part 2)

**Input:** `output/corpus_deduplicated.json` (corpus after duplicate merging)

**Method:** For each pair of author names in corpus, compute 5 weighted signals:

| Signal | Weight | Notes |
|--------|--------|-------|
| Name string similarity (token-level fuzzy match) | 0.25 | "H. Sebastian Seung" vs "H Sebastian Seung" |
| First name / initial compatibility | 0.20 | "Alexander S. Bates" vs "Alexander Shakeel Bates" |
| Co-author set Jaccard | 0.25 | Do they have overlapping collaborators? |
| Citation neighborhood overlap | 0.15 | Do they cite/are cited by the same papers? |
| Shared-paper negative signal | 0.15 | If they co-appear on papers → likely DIFFERENT people |

**Confidence threshold bins:**
- `≥ 0.65`: SAME_PERSON — merge with high confidence
- `0.50–0.65`: LIKELY_SAME — candidate for human review
- `0.35–0.50`: REVIEW — ambiguous boundary case
- `< 0.35`: DIFFERENT_PEOPLE — no merge

**Output:** `output/author_dedup_review.tsv` (980 pairs)
- Columns: name1, name2, score, signal_breakdown, confidence_category, **[decision column (blank for review)]**

**Action:** Review and mark decisions. Known confirmed merges (from README Step 10) pre-marked as ACCEPTED.

#### Step 2B: Apply Author Merges

**Script:** `10_apply_merges.py` (updated to read dedup review decisions)

**Input:**
- `output/author_dedup_review.tsv` (with human decisions)
- `output/corpus_deduplicated.json`
- Author co-authorship graph

**Process:**
1. For each ACCEPTED merge: rewrite author IDs in corpus
2. Recompute author rankings (weighted degree, betweenness, PageRank on coauthorship)
3. Update composite scores for affected papers (author diversity metric)

**Output:**
- `output/author_merge_map.json` — canonical → alias mapping
- Updated corpus, author rankings
- `output/author_merge_log.json` — who was merged, impact on rankings

---

## Phase 3: Domain Classification & Noise Filtering

### Goals
- Label papers by domain (em_connectomics, mri_connectomics, network_science, methods, etc.)
- Identify and flag off-topic papers (cancer statistics, geophysics, etc.)
- Maintain transparency on how papers are classified

### Workflow

#### Step 3A: Multi-Signal Domain Classification

**Script:** `classify_domain.py`

**Input:** `output/graphs/citation_graph.json` (all 7,925 papers)

**Method:** 3-layer classification (strongest signal first):

| Layer | Coverage | Signal | Action |
|-------|----------|--------|--------|
| **Journal name** | 97% | Map `journal` field to domain | Most reliable |
| **OpenAlex concepts** (if available) | ~30% | "Drosophila", "connectomics", "complex networks" | Used as tiebreaker |
| **Title keywords** | 100% (fallback) | em_connectomics={connectom, synapse, ...}, mri={fmri, ...} | Last resort |

**Output classifications:**
- `em_connectomics` — 28% of corpus (2,227 papers)
- `neuroscience` — 18% (1,464 papers)
- `mri_connectomics` — 6% (465 papers)
- `methods_ml` — 4% (323 papers)
- `network_science` — 2% (167 papers)
- `off_topic` — 5% (377 papers) — marked for removal
- `unknown` — 37% (2,902 papers) — big-tent journal papers; inspect case-by-case

**Output:** `output/domain_labels.json` — openalex_id → domain

**No human review needed** unless off_topic threshold needs adjustment.

#### Step 3B: Update Strategic Audit with Domain Labels

**Script:** `11_strategic_audit.py` (updated)

**Changes:**
- Section C2 now shows domain labels instead of binary "neuro signal"
- Off-topic papers (domain="off_topic") flagged automatically
- Unknown papers with high scores reviewed individually

---

## Phase 4: Review-Cited Gap Analysis

### Goals
- Examine citations in 6 major 2024–2025 reviews
- Identify high-impact papers cited by reviews but outside top-500
- Include only if they meet statistical criteria

### Workflow

#### Step 4A: Fetch Review Citations (if OpenAlex access available)

**Script:** `13_review_citations.py` (to be written)

**Input:** 6 major review DOIs (from strategic audit):
- Helmstaedter 2025 (Nat. Rev. Neurosci.)
- Bock 2025 (Nat. Rev. Neurosci.)
- Khajeh & Lee 2025 (Nat. Methods)
- Lichtman et al. 2014 (Nat. Neurosci.)
- And 2–3 others TBD

**Process:**
1. Check cache first (`cache/review_citations_*.json`)
2. For each review DOI, fetch `referenced_works` from OpenAlex
3. For each cited paper, check:
   - Is it in corpus?
   - What rank does it have?
   - How many external citations does it have?
   - What domain does it belong to?

**Output:** `output/review_citations.json`
```json
{
  "review_doi": "10.1038/nrn.2025.xxx",
  "review_title": "Synaptic connectomics...",
  "cited_papers": [
    {
      "doi": "...",
      "title": "...",
      "in_corpus": true/false,
      "rank": 150,
      "composite_score": 0.45,
      "external_citations": 2500,
      "domain": "em_connectomics"
    },
    ...
  ]
}
```

#### Step 4B: Identify Candidates for Inclusion

**Criteria for promotion or addition:**

1. **Already in corpus, ranked 201–500:**
   - Criteria: cited by ≥2 reviews + composite_score > 0.10
   - Action: PROMOTE to top-200 consideration
   - Example: Lichtman 2014 (86 in-degree, 2,780 ext. cites, but k-core boundary)

2. **NOT in corpus but cited by ≥2 reviews:**
   - Criteria: ≥2,000 external citations + domain matches (not off_topic)
   - Action: ADD to corpus via `EXTRA_SEED_DOIS`
   - Requires re-running `01_harvest.py` with expanded seeds

3. **Cited by 1 review only:**
   - Criteria: composite_score would exceed 0.20 if added, + domain match
   - Action: FLAG for human review
   - Example: Tools (CATMAID, webKnossos) — high impact but niche

**Output:** `output/review_cited_candidates.json`
- Section "promote": papers to lift into top-200
- Section "add": DOIs to add to EXTRA_SEED_DOIS
- Section "flag": borderline cases

---

## Phase 5: Expert List Gap Analysis

### Goals
- Cross-check 66+ researcher seed lists against top-500
- Identify expert-curated papers not recovered by automation
- Include only if missing for explainable reasons

### Workflow

#### Step 5A: Validate Expert Papers (already in strategic audit)

**Script:** `09_graph_analysis.py` (existing expert gap computation)

**Input:** 
- `_data/expert_seed_papers/*.md` (66 researchers' lists)
- `output/reading_list.json` (top-500)

**Output:** `output/expert_list_gaps.json`

Two categories:

1. **In corpus, ranked below 500 (20 papers)**
   - Examples: "Functional connectome fingerprinting" (2,967 ext. cites), "Network-based statistic" (2,779)
   - These likely have valid reasons (low in-corpus citation = specialized topic)
   - Action: REVIEW for promotion if domain=em_connectomics

2. **Not in corpus (28 papers)**
   - These are NOT in OpenAlex corpus despite expert nomination
   - Missing because: not indexed, preprint, tool paper (no DOI), etc.
   - Action: Manual CHECK — is paper indexable? If yes, add DOI to EXTRA_SEED_DOIS

#### Step 5B: Create Inclusion Decision Log

**Script:** `13_inclusion_decisions.py` (to be written)

**Output:** `output/inclusion_decisions.json`

```json
{
  "promote_from_tail": {
    "papers": [...],
    "criteria": "expert_curated + in_corpus + external_cites > 500 + domain=em_connectomics",
    "count": 8
  },
  "add_missing_expert": {
    "papers": [...],
    "criteria": "expert_nominated + indexable + not_in_openAlex",
    "count": 3
  },
  "review_from_reviews": {
    "papers": [...],
    "criteria": "cited_by_2plus_reviews + (not_in_corpus OR rank_201_500) + composite_would_exceed_0.15",
    "count": 5
  },
  "flag_ambiguous": {
    "papers": [...],
    "criteria": "cited_by_1_review + is_infrastructure_paper + domain=not_off_topic",
    "count": 4
  }
}
```

---

## Phase 6: Update & Re-rank

### Goals
- Incorporate all accepted decisions
- Recompute metrics and rankings
- Re-generate reading list

### Workflow

**Script:** `14_update_corpus_and_rerank.py` (to be written)

**Input:** All decisions from phases 1–5

**Process:**
1. Apply duplicate merges → `corpus_v2.json`
2. Apply author merges → recompute author rankings
3. Add papers from EXTRA_SEED_DOIS + inclusion_decisions.json → `corpus_v2_expanded.json`
4. Rebuild all four graphs
5. Recompute metrics (PageRank, betweenness, community detection)
6. Re-rank papers and authors
7. Regenerate reading list with new top-500
8. Re-run strategic audit
9. Tag papers with "source" metadata (corpus_a/b/c, added_via_review, added_via_expert, added_via_inclusion)

**Output:**
- `output/corpus_v2_final.json`
- `output/paper_rankings_v2.json`
- `output/reading_list_v2.json`
- Updated `strategic_audit_v2.md`
- `output/inclusion_metadata.json` — why each paper is in top-500 (corpus origin + inclusion decision)

---

## Decision Log Format

All decisions documented in TSV with consistent columns:

### Duplicate decisions

```
paper1_id	paper2_id	confidence	signal_breakdown	decision	notes
...			AUTO_MERGE	ACCEPT	bioRxiv + published
...			LIKELY_DUP	REJECT	different papers, similar title
```

### Author merge decisions

```
name1	name2	confidence	coauthor_overlap	decision	notes
...			SAME_PERSON	ACCEPT	same person
...			LIKELY_SAME	REJECT	different people, name collision
```

### Inclusion decisions

```
doi	title	source	criteria	decision	external_cites	composite_score	domain	notes
...	...	review_cited	cited_by_2_reviews	INCLUDE	2500	0.18	em_connectomics	...
...	...	expert_gap	not_in_corpus	ADD_SEED	1200	NA	neuroscience	...
```

---

## Cache Strategy

**Critical:** Before making any OpenAlex API calls, check cache:

```python
# Example from 01_harvest.py
cache_file = CACHE_DIR / f"work_{openalex_id}.json"
if cache_file.exists():
    with open(cache_file) as f:
        return json.load(f)

# Only if cache miss, fetch
response = fetch_from_openalex(openalex_id)
with open(cache_file, 'w') as f:
    json.dump(response, f)
return response
```

**Cache locations:**
- `scripts/bibliometrics/cache/` — indexed by openalex_id
- `scripts/bibliometrics/cache/review_citations_*.json` — by review DOI
- `scripts/bibliometrics/cache/expert_papers_*.json` — by researcher name

---

## Execution Sequence

### Recommended order (one phase per session):

1. **Phase 1:** Duplicate detection & merging (no API calls)
2. **Phase 2:** Author disambiguation (no API calls)
3. **Phase 3:** Domain classification (uses existing data)
4. **Phase 4:** Review citations (needs OpenAlex IF not cached)
5. **Phase 5:** Expert gap analysis (uses existing expert_list_gaps.json)
6. **Phase 6:** Final update & re-rank (orchestration script)

### Without OpenAlex access:

- Phases 1, 2, 3 proceed normally
- Phase 4 skipped or using cached review citations
- Phase 5 uses existing gaps analysis
- Phase 6 still runs, but omits fetch-based additions

---

## Documentation & Transparency

For every top-500 paper in final reading list, document:

```json
{
  "openalex_id": "...",
  "title": "...",
  "rank": 42,
  "composite_score": 0.456,
  "inclusion_source": {
    "corpus": "a",           // which corpus(a/b/c) found it
    "promoted_from": 350,     // if promoted from tail
    "added_via": "review_cited", // or "expert_gap", "dedup_merge", null
    "inclusion_criteria": "cited by 2+ reviews + external_cites > 2000",
    "decision_date": "2025-03-31"
  },
  "merged_from": null,  // if consolidated with another paper
  "domain": "em_connectomics"
}
```

This allows readers to understand *why* each paper is in the list and builds trust in the curation process.

---

## Success Criteria

After completing all phases:

✓ Duplicate pairs: ≥95% agreement with manual inspection of sample  
✓ Author merges: ≥90% correctness (spot-check top-50 authors)  
✓ Domain labels: ≥85% precision on em_connectomics (vs. manual sample)  
✓ Off-topic removal: <5 off-topic papers remaining in top-500  
✓ Review-cited: ≥80% of expert-curated papers recovered or flagged  
✓ Inclusion transparency: every paper documented with source + criteria  

---

## Next Steps

1. Implement Phase 1 script: `12_apply_duplicate_merges.py`
2. Implement Phase 4 script: `13_review_citations.py`
3. Implement Phase 5 / 6 scripts: `13_inclusion_decisions.py`, `14_update_corpus_and_rerank.py`
4. Test end-to-end on cached data (no API calls)
5. Run full update when OpenAlex access available
6. Document results and publish updated reading list
