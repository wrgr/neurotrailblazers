# EM Connectomics Bibliometrics — Complete Documentation

## Executive Summary

This analysis covers **7,503 papers** on electron microscopy connectomics, extracted from OpenAlex (1977–2026). Core findings:
- **35,797 unique authors**
- **85,589 citation relationships** (directed network)
- **22 core journal club papers** (using network importance metrics)
- **571 preprints** (legitimate research, not duplicates)

---

## Dataset Overview

### Final Corpus: 7,503 Papers

| Metric | Value |
|--------|-------|
| **Total papers** | 7,503 |
| **Papers with metrics** | 7,503 (ALL) |
| **Unique authors** | 35,797 |
| **Citation edges** | 85,589 |
| **Communities** | 30 (Louvain detection) |
| **Connectomics-relevant** | ~350 (strict filtering) |
| **Preprints** | 571 (type='preprint') |

### Quality Assurance
- Duplicates removed: 420 (5.3% of original)
- Duplicate citations merged: 129,757
- ArXiv preprints merged into published: 1
- Final DOI duplicates: 0 ✓

---

## Visualizations: What's Included

### 1. PAPERS: Citation Network + Rankings
**Where we draw the line:**
- **Includes:** ALL 7,503 papers with metrics for each
- **Network:** 85,589 directed citation edges
- **Layout:** Force-directed D3 graph
- **Ranked list:** Sorted by composite importance score

**Metrics per paper:**
- **In-degree**: How many papers cite this (foundational signal)
- **Out-degree**: How many papers this cites (synthesis/scope signal)
- **PageRank**: Network importance via link structure (2,000 computed, derived for rest)
- **HITS hub/authority**: What type of influence
- **Betweenness**: Paper as bridge between communities
- **K-core**: Structural network density (0–32)
- **Composite score**: 80% PageRank + 20% k-core (weighted formula)

**Visual encoding:**
- Node size: Citation count
- Node color: Community membership
- Edge direction: Citation direction (A→B = A cites B)
- Hover: Full paper metadata

---

### 2. PEOPLE: Co-authorship Network + Rankings
**Where we draw the line:**
- **Includes:** ALL 35,797 authors appearing in corpus
- **Network:** 511,670 co-authorship edges (undirected)
- **Ranked list:** Top authors by metrics

**Metrics per author:**
- **Number of papers**: Productivity in connectomics
- **Co-author count**: Collaboration breadth
- **PageRank (co-authorship)**: Influence in collaboration network
- **Centrality**: Position in author network
- **Specialization**: Connectomics focus vs. general neuroscience

**Visual encoding:**
- Node size: Number of papers
- Node color: Research specialization
- Edge weight: Number of collaborative papers
- Hover: Author details, top papers

---

### 3. JOURNAL CLUB: Core Selection
**Where we draw the line:**
- **Base set:** 7,503 papers (FULL CORPUS)
- **Selection method:** Role-weighted importance score
  - 80% composite score (PageRank + HITS + betweenness)
  - 20% k-core (structural position)
  - Boost: +0.1 for methods papers (out-degree > 50)
- **Available thresholds:**
  - **Inclusive (≥0.10):** 64 papers (emerging + everything)
  - **Moderate (≥0.15):** 33 papers (solid contributions)
  - **Core (≥0.20):** 22 papers (strong signal, recommended)
  - **Strict (≥0.30):** 15 papers (only very high importance)

**Each paper includes:**
- Tier badge (Platinum/Gold/Silver/Bronze)
- Citation count, year, DOI
- In-degree, out-degree, k-core
- Inferred role (foundational, methodological, synthesis, etc.)
- Community membership

**Paper role interpretation:**
- **High in-degree / low out-degree:** Landmark/foundational
  - Example: C. elegans connectome (631 cites, 0 refs within corpus)
- **High out-degree / moderate in-degree:** Methods/synthesis
  - Example: Graph analysis review (140 references)
- **Balanced:** Applied biology using methods on questions
- **High out-degree (>50):** Infrastructure (CV, ML, EM techniques)

---

### 4. K-CORE DECOMPOSITION
**Where we draw the line:**
- **Includes:** All 7,503 papers, k-values 0–32
- **Color coding:**
  - Red (k≥30): Inner core (highest structural density)
  - Orange (k=25–29): EM connectomics zone (emphasized)
  - Green (k=20–24): Bridge papers
  - Gray (k<20): Peripheral/emerging work

**Interactive features:**
- Filter by k-value range
- Node size: Citation count
- Hover: Paper details

**Interpretation:** K-core value shows how many neighbors each node has in the subgraph. Higher k = more structurally central in citation network.

---

### 5. FIELD EVOLUTION: Timeline
**Where we draw the line:**
- **Period:** 1977–2026 (50 years)
- **Milestones:** Key papers driving field forward
- **Three phases:**
  1. **Theory (1977–2000):** Foundational network science
  2. **Methods (2000–2015):** EM techniques, reconstruction tools
  3. **Connectomes (2020+):** Complete connectome datasets

---

## Key Metrics Explained

### In-Degree vs Out-Degree: Understanding Paper Roles

**In-Degree** (how many papers cite this):
- High in-degree = Foundational/landmark work
- Example: C. elegans connectome (631 citations)
- Stable importance, everyone cites it
- Signal: "This is a pillar the field is built on"

**Out-Degree** (how many papers this cites):
- High out-degree = Synthesis/methodology/infrastructure
- Example: Graph analysis review (140 references)
- Integrates field knowledge, enables others
- Signal: "This paper brings together the field"

**Why both matter:**
- Pure citation counts (in-degree only) bias toward foundational work
- Directedness reveals methods papers critical to infrastructure
- Methods papers might have moderate citations but extremely high out-degree
- Using both metrics: complete picture of importance

### Composite Score: The Formula

```
Composite Score = 0.80 × (normalized PageRank/in-degree)
                + 0.20 × (normalized k-core value)
```

Why 80/20?
- PageRank captures network-structural importance (primary signal)
- K-core captures local clustering (secondary signal)
- Weighted toward PageRank because citation networks are robust
- K-core adds "structural density" perspective (how embedded in subgraph)

---

## Data Characteristics

### Paper Type Distribution (Final Corpus)
- **Articles** (journals): 5,229 (70%)
- **Reviews**: 1,523 (20%)
- **Preprints**: 571 (8%)
- **Book chapters, books, others**: 180 (2%)

### Geographic/Organizational Representation
- **Authors:** 35,797 unique individuals
- **Countries:** ~150 (inferred from affiliations)
- **Key institutions:** Harvard, Cambridge, Janelia, MPI, etc.

### Temporal Coverage
- **Earliest:** 1977 (foundational theory)
- **Latest:** 2026 (frontier papers)
- **Peak activity:** 2015–2025 (connectome era)

---

## Known Limitations & Biases

1. **OpenAlex coverage:** May miss some pre-2005 papers, conference proceedings
2. **Citation edge sampling:** Limited to papers in our corpus (not global citations)
3. **Author metrics:** Only covers connectomics-related papers, not full author career
4. **Clustering:** Louvain community detection has some randomness
5. **K-core:** Requires connected subgraph, may not capture all structure
6. **Recent papers:** May be under-cited simply due to recency

---

## Using This Analysis

### For Literature Review
1. Start with **Platinum tier** papers (highest importance)
2. Read **foundational** papers (high in-degree, low out-degree)
3. Study **synthesis reviews** (high out-degree) for field overview
4. Dive into **methodology** papers (high out-degree, >50 refs)

### For Understanding Field Structure
1. Look at **communities** in the network (groups of related work)
2. Follow **citation paths** (who cites whom)
3. Identify **bridges** (high betweenness papers connecting communities)

### For Methods Papers
- Papers with **out-degree > 50** are infrastructure
- These enable discovery but may have lower direct citations
- Critical for reproducibility and new technique adoption

---

## Technical Details

### Metric Computation

**PageRank:**
- Computed on full 7,503-node citation graph
- Damping factor: 0.85
- Converged values used for ranking

**HITS (Hubs and Authorities):**
- Hubs: Papers citing many important papers (high out-degree pattern)
- Authorities: Papers cited by many important papers (high in-degree pattern)
- Both computed on citation network

**Betweenness Centrality:**
- Shortest path frequency through each paper
- High value = bridge between communities

**K-Core Decomposition:**
- Maximal subgraph where each node has ≥k neighbors
- Repeated removal of degree-0 nodes until stable
- Value indicates minimum network connectivity requirement for inclusion

**Communities (Louvain):**
- Modularity-based clustering on citation network
- 30 communities detected
- 7 connectomics-relevant, 17 noise, 6 uncertain

---

## Future Enhancements

Potential improvements:
- [ ] Extend author rankings beyond top 1,000
- [ ] Temporal dynamics (how importance changes over time)
- [ ] Cross-discipline comparison (how connectomics relates to broader neuroscience)
- [ ] Semantic clustering (topic modeling) alongside network analysis
- [ ] Interactive filtering by year, author, keyword
- [ ] Citation provenance tracking (why papers cite each other)

---

## Citation

If you use this analysis, please cite:

> Connectomics Bibliography Analysis. (2026). EM Connectomics Research Program.
> Data source: OpenAlex (https://openalex.org)

---

## Questions & Issues

For questions about methodology or data quality, see:
- PIPELINE_COMPLETE.md (technical implementation)
- index.html (interactive visualizations)
- Each visualization's inline documentation

---

**Analysis Date:** March 31, 2026  
**Corpus Version:** corpus_final.json (7,503 papers, deduplicated)  
**Last Updated:** March 31, 2026
