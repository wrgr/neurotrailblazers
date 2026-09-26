# Connectomics Corpus Curation Strategy

**Generated:** 2026-04-01T04:18:23.480153

## Core Corpus Definition

**Filtering Criteria:**
- Minimum total degree: ≥5 (cited at least 5 times in corpus or cites at least 5)
- Minimum in-degree: ≥2 (cited by at least 2 other papers in corpus)

**Rationale:**
- Degree ≥5: Ensures papers are integrated into the citation network
- In-degree ≥2: Validates papers are recognized/cited by multiple others
- Result: High-confidence, mutually-validated core literature

## Core Corpus Statistics

**Size & Coverage:**
- Total papers: 3808 (48% of full corpus)
- With direct PDF links: 3035 (79%)
- In top 500 ranked papers: 411

**Network Metrics:**
- Nodes: 3809
- Edges: 57414 (60% of original)
- Average in-degree: 0.0
- Average out-degree: 0.0

## Up and Coming Watch List

**Selection Criteria:**
- Same degree/in-degree filters as core BUT in-degree < 2
- Only papers ranked in top 500
- Age ≤ 2 years (2024-2026)
- Rationale: High-potential emerging work not yet validated by citations

**Papers:** 27
- With PDF links: 22
- Average citations to corpus: 49.7
- Average age: 1.1 years

**Top Examples:**

- **Rank 31 (2025)**: Synaptic-resolution connectomics: towards large brains and connectomic...
  - Cites 117 papers in corpus
  - Cited by 1 papers in corpus
  - Global citations: 2

- **Rank 107 (2025)**: Connectome architecture favours within-module diffusion and between-mo...
  - Cites 55 papers in corpus
  - Cited by 0 papers in corpus
  - Global citations: 1

- **Rank 109 (2026)**: Long-range axon branching: contributions to brain network plasticity a...
  - Cites 68 papers in corpus
  - Cited by 0 papers in corpus
  - Global citations: 0

- **Rank 142 (2025)**: Exploring the transmission of cognitive task information through optim...
  - Cites 49 papers in corpus
  - Cited by 0 papers in corpus
  - Global citations: 0

- **Rank 194 (2025)**: On analogies in vertebrate and insect visual systems...
  - Cites 64 papers in corpus
  - Cited by 0 papers in corpus
  - Global citations: 3


## Update Strategy

**Periodic Updates (e.g., quarterly):**
1. Re-run citation graph construction
2. Check up-and-coming papers for in-degree ≥2
3. Promote validated papers to core corpus
4. Generate new up-and-coming list

**Example Promotion:**
- Paper starts at in-degree = 1 (cited by 1 other paper)
- After 6 months, now cited by 2+ papers
- Promote from watch list to core corpus
- Update graph and RAG index

## Files Generated

- `paper_rankings_core_corpus.json` - All core papers with metadata
- `papers_up_and_coming.json` - Watch list sorted by rank
- `citation_graph_core_corpus.json` - Filtered graph (nodes & edges)

## Usage for RAG

**Build RAG from:**
- Core corpus papers: 3808 papers
- PDF links available: 3035 papers (79%)

**Keep separate:**
- Up and coming list: Monitor, promote when validated
- Excluded papers: Lower-connectivity papers for future review

## Quality Metrics

✅ **Inclusion Signal:** In-degree ≥2 = multiple citations within corpus
✅ **Engagement Signal:** Out-degree ≥5 = multiple citations to corpus papers  
✅ **Recency:** Up and coming list tracks emerging work
✅ **Coverage:** 3035/3808 papers directly accessible

---

**Corpus Strategy:** High-confidence core with emerging work pipeline
**Purpose:** Clean, validated connectomics literature for RAG pipelines
**Maintainability:** Update quarterly to promote emerging papers
