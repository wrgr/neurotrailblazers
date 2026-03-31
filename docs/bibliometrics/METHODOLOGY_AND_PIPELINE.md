# EM Connectomics Bibliometrics: Methodology & Pipeline
## Complete Technical Documentation for Team Review

---

## 1. PIPELINE OVERVIEW

### 1.1 High-Level Data Flow

```
OpenAlex Query
    ↓
Raw Data (~8,000 papers)
    ↓
Deduplication (420 duplicates removed)
    ↓
Author Merging (17 name merges applied)
    ↓
Corpus: 7,503 papers, 35,641 authors
    ↓
Citation Network Analysis
    ├─ PageRank computation (2,000 papers)
    ├─ HITS hubs/authorities
    ├─ Betweenness centrality
    ├─ K-core decomposition
    └─ Degree statistics (ALL papers)
    ↓
Paper Role Classification (10 categories)
    ↓
Author Rankings (35,641 authors)
    ↓
Key Experts Analysis (top 50)
    ├─ Career arcs (15 expert trajectories)
    ├─ Synthesis/infrastructure papers
    └─ Important work by role
    ↓
Composite Scoring (80% PageRank + 20% k-core)
    ↓
Journal Club Selection (4 thresholds: 10, 15, 20, 30)
    ↓
Visualizations (6 HTML files + 1 dashboard)
    ↓
Documentation & QA
```

### 1.2 Code Structure

```
scripts/bibliometrics/
├── 01_query_and_fetch.py         (OpenAlex query, raw data)
├── 02_build_graphs.py            (citation network construction)
├── 03_deduplicate_corpus.py      (duplicate removal)
├── 04_compute_metrics.py         (PageRank, HITS, betweenness)
├── 05_generate_full_visualizations.py
├── 06_compute_kcore.py           (k-core decomposition)
├── 07_community_detection.py     (Louvain algorithm)
├── 08_author_rankings.py         (author scoring)
├── 09_generate_journal_club_thresholds.py
├── 10_paper_role_analysis_granular.py
├── 11_extend_metrics_to_all_papers.py
├── 12_composite_scoring.py       (final importance score)
├── 13_synthesis_papers_analysis.py
├── 14_career_arcs_analysis.py
├── 15_apply_author_merges_to_corpus.py
├── 16_key_experts_analysis.py
├── 18_career_arcs_analysis.py
├── 19_seed_list_comparison.py
├── 20_apply_enrichment_decisions.py
└── output/                       (all JSON files, HTML visualizations)
```

---

## 2. METRIC COMPUTATIONS

### 2.1 Citation Network & Basic Metrics

**Network Structure:**
- **Nodes:** 7,503 papers
- **Edges:** 85,589 directed citations (paper A → paper B if A cites B)
- **Edge weight:** None (unweighted network)

**In-Degree:** Citations received
- Range: 0–475 (median: 2)
- Interpretation: How foundational/influential is this paper?
- Example: Drosophila connectome paper (2020) = 475 in-degree

**Out-Degree:** Citations given
- Range: 0–117 (median: 20)
- Interpretation: How broadly scoped is this paper? (synthesis vs. narrow)
- Example: Methods infrastructure papers = high out-degree

### 2.2 PageRank Algorithm

**Implementation:**
- Damping factor: 0.85
- Convergence: 100 iterations
- Computed on: Top 2,000 papers by citation count
- Derived for remaining: Using in/out degree proxy

**Formula:**
```
PR(p) = (1 - d) / N + d * Σ(PR(t) / |t|)
  where:
    d = 0.85 (damping factor)
    N = 7,503 (total papers)
    t = papers that cite p
    |t| = out-degree of t
```

**Interpretation:**
- Papers with high PageRank are highly cited AND cited by important papers
- Captures "importance via link structure"
- Different from citation count alone (which is just in-degree)

**Limitations:**
- Preprints and recent papers may not have accumulated enough citations yet
- Citation patterns are field-specific (connectomics ≠ computer science)

### 2.3 HITS (Hyperlink-Induced Topic Search)

**Hubs:** Papers that cite many important papers (high out-degree to authorities)
- Example: Reviews, survey papers, synthesis work

**Authorities:** Papers cited by important hubs (high in-degree from hubs)
- Example: Landmark papers, foundational work

**Usage:**
- Identifies two types of influence simultaneously
- Helps distinguish between "broad synthesis" (hubs) vs. "foundational" (authorities)

### 2.4 Betweenness Centrality

**Definition:** How many shortest paths between other papers pass through this paper?

**Interpretation:**
- High betweenness = "bridge paper" connecting different communities
- Example: Paper linking connectomics ↔ network neuroscience
- Values: 0–0.032 (very sparse in citation networks)

**Limitations:**
- Citation networks are directed acyclic (mostly)
- Shortest paths are trivial in many cases
- Less informative than in undirected collaboration networks

### 2.5 K-Core Decomposition

**Definition:** Maximal subgraph where every node has degree ≥ k within the subgraph

**Process:**
1. Remove all nodes with degree < 1
2. Remove all nodes with degree < 2 (in remaining graph)
3. Continue until no more removals possible
4. Each node's k-value = last iteration it survived

**Range:** 0–32 (empirically observed in our network)

**Interpretation:**
- **k=0–5:** Periphery (foundational/method papers with few internal connections)
- **k=10–15:** Mid-tier (active research area)
- **k=20–32:** Core (highly interconnected papers, likely in same community)

**Usage in Pipeline:**
- 20% of composite score
- Structural network density indicator
- Complements PageRank (citation importance)

### 2.6 Composite Importance Score

**Formula:**
```
composite_score = 0.80 × normalized_pagerank + 0.20 × normalized_kcore
```

**Normalization:**
- Each component scaled to [0, 1]
- Min-max normalization on actual values

**Role-Based Boost:**
```
if out_degree > 37 (top 5% threshold):
    composite_score += 0.10  (methods/infrastructure boost)
```

**Rationale:**
- PageRank dominates (80%) because it captures network-wide importance
- K-core (20%) adds structural density information
- Methods papers boost corrects for bias toward pure citation count
- Top 5% threshold = data-driven (empirical distribution analysis)

**Result Distribution:**
- Mean: 0.15
- Median: 0.08
- Max: 0.91 (Drosophila connectome paper)
- Min: 0.01

---

## 3. PAPER ROLE CLASSIFICATION

### 3.1 Ten Granular Roles

**Role Assignment Logic:**

| Role | In-Degree | Out-Degree | % of Corpus | Interpretation |
|------|-----------|-----------|------------|-----------------|
| **landmark_influential** | ≥150 | Any | 0.3% | Most cited, foundational |
| **landmark_connectome** | ≥300 | <20 | 0.0% | Connectome papers only, narrow |
| **foundational** | 50–149 | <37 | 1.6% | Cited heavily, not broad synthesis |
| **methods_infrastructure** | <50 | ≥37 | 1.6% | High citations given, implementation focus |
| **well_cited** | 30–49 | <37 | 3.2% | Moderately cited, specific |
| **synthesis_integration** | 20–29 | 20–36 | 5.4% | Integrative work, medium breadth |
| **cited_technical** | 20–29 | <20 | 7.7% | Technical papers, narrow scope |
| **balanced_contribution** | 10–19 | 10–19 | 7.9% | Even influence both directions |
| **methodological_focus** | 10–19 | Any | 24.0% | Active research, methods-oriented |
| **active_contributor** | 1–9 | Any | 45.4% | Emerging/narrow work, limited impact yet |
| **orphaned_paper** | 0 | Any | 2.9% | No citations received (data artifact?) |

### 3.2 Rationale for Thresholds

**In/Out-degree cutoffs (10 minimum):**
- Captures "active research" papers that have measurable impact
- Excludes orphaned papers and citation artifacts
- Data-driven: 10 = empirical percentile in active community

**Out-degree >= 37 (methods/infrastructure):**
- Top 5% by out-degree in citation distribution
- Papers citing 37+ references = comprehensive synthesis
- Corrects for "methods papers might be under-cited but important"

**Example Classifications:**
- Lichtman lab connectomics papers: foundational or landmark_influential
- Sporns network neuroscience reviews: synthesis_integration or methods_infrastructure
- FlyEM papers: foundational (high in-degree) + methods (high out-degree if review)

### 3.3 Known Biases

1. **Recency bias:** New papers have low in-degree even if impactful
   - Mitigation: Use recent_pagerank for papers <3 years old
   
2. **Field bias:** Connectomics papers often narrower scope than reviews
   - Mitigation: In/out-degree captures scope independently of field
   
3. **Preprint treatment:** Some preprints not yet cited widely
   - Mitigation: Keep preprints in corpus, but flag in role assignment
   
4. **Citation patterns:** Different fields cite differently (E&M vs. CS)
   - Limitation: Pipeline assumes uniform citation patterns
   - Accepted: This is inherent to cross-domain analysis

---

## 4. AUTHOR MERGING STRATEGY

### 4.1 Why Merge?

**Problem:** Same author appears under multiple name variants
- William Gray-Roncal, Will Gray-Roncal, W. Gray-Roncal
- Name changes, abbreviations, character encoding issues

**Solution:** Apply 17 explicit merges based on domain knowledge

### 4.2 Merge Table

| Canonical Name | Aliases | Papers | Merged Count |
|---|---|---|---|
| William Gray-Roncal | Will Gray-Roncal, W. Gray-Roncal, Gray-Roncal William | 28 | ✓ |
| H. Sebastian Seung | Seung HS, Sebastian Seung, H.S. Seung | 64 | ✓ |
| Gregory S.X.E. Jefferis | Jefferis G.S.X.E., G. Jefferis, Gregory Jefferis | 60 | ✓ |
| Shin-ya Takemura | Takemura Shin-ya, Takemura S., Shinichi Takemura | 39 | ✓ |
| Davi D. Bock | Bock DD, Davi Bock, D.D. Bock | 56 | ✓ |
| Moritz Helmstaedter | Helmstaedter M., Moritz H., M. Helmstaedter | 43 | ✓ |
| (and 11 others) | — | — | ✓ |

### 4.3 Implementation

**Script:** `15_apply_author_merges_to_corpus.py`

**Process:**
1. Load corpus_final.json (7,503 papers)
2. For each paper, for each author, apply merge table
3. Update author names and co-author networks
4. Recompute author rankings with merged names
5. Save corpus_merged.json and author_rankings_merged.json

**Impact:**
- Author count: 35,797 → 35,641 (156 merged)
- Top authors more accurately represented
- Will Gray-Roncal: consolidated to rank #65 (28 papers)

### 4.4 Known Limitations

- Merges are manual, not automated
- May miss some aliases (e.g., Chinese name → Western name)
- No automated name similarity scoring yet
- Future work: Implement fuzzy matching + validation

---

## 5. JOURNAL CLUB SELECTION STRATEGY

### 5.1 Philosophy

**Goal:** Identify "core papers" that best represent the field's knowledge

**NOT based on:**
- K-core membership alone
- Random representative sampling
- Author subjective importance

**BASED on:**
- Composite importance score (derived from network metrics)
- Paper role classification (captures type of contribution)
- Citation impact + network density

### 5.2 Threshold Selection

**Four thresholds (10, 15, 20, 30):**

| Threshold | Papers | Platinum | Gold | Silver | Bronze | Philosophy |
|-----------|--------|----------|------|--------|--------|-----------|
| **10** | 64 | 10 | 5 | 7 | 42 | Very inclusive, all active research |
| **15** | 33 | 10 | 5 | 7 | 11 | Selective, high impact |
| **20** | 22 | 10 | 5 | 7 | 0 | **RECOMMENDED** — hand-curated feel |
| **30** | 15 | 10 | 5 | 0 | 0 | Ultra-core, elite papers only |

**Threshold 20 is recommended because:**
- ~22 papers = "manageable journal club size"
- Balances inclusivity with rigor
- Aligns with typical journal club scope
- Includes all Platinum/Gold tiers (elite papers)

### 5.3 Tier Assignment

**Tier Logic:**
```
if composite_score >= 0.8:  Platinum (elite)
elif composite_score >= 0.5:  Gold (high impact)
elif composite_score >= 0.3:  Silver (solid contribution)
else:  Bronze (foundational/supporting)
```

**Platinum Papers (10):**
- Scores ≥ 0.8
- Landmark connectomics papers
- Examples: Drosophila connectome, C. elegans connectome

**Gold Papers (5):**
- Scores 0.5–0.8
- High-impact methods, network analysis
- Examples: Small-world networks (Watts & Strogatz), connectome analysis reviews

**Silver Papers (7):**
- Scores 0.3–0.5
- Important technical contributions
- Examples: EM reconstruction methods, image analysis

**Bronze Papers:**
- Scores < 0.3
- Foundational or supporting work
- Examples: Older foundational papers, supporting methodology

### 5.4 In-Degree/Out-Degree Inclusion

**Why both directions matter:**
- **In-degree (received citations):** Paper was influential/correct
- **Out-degree (given citations):** Paper was comprehensive/synthetic

**Example use:**
- Methods papers have high out-degree (they cite everything)
- Landmark papers have high in-degree (everything cites them)
- A good journal club needs both

---

## 6. VISUALIZATION DESIGN

### 6.1 Main Visualizations

#### **index.html** — Unified Dashboard
- Statistics: 7,503 papers, 35,641 authors, 85,589 edges
- Navigation buttons to all 5 visualizations
- Metadata: last update, methodology links

#### **field_map_full.html** — Citation Network
- **Nodes:** All 7,503 papers
- **Edges:** 85,589 citation relationships
- **Layout:** D3 force-directed (physical simulation)
- **Features:**
  - Zoom/pan enabled
  - Click nodes for paper details
  - Top 200 papers ranked list on side
  - Toggle citation ↔ co-authorship networks
  - Color by composite score (red = high importance)
  - Node size by in-degree

**Design Rationale:**
- Force-directed layout reveals natural community structure
- Zoom enables both macro (field structure) and micro (local communities) views
- Dual-network toggle shows citation vs. collaboration patterns

#### **coauthor_map_full.html** — Collaboration Network
- **Nodes:** 35,641 authors
- **Edges:** 511,670 undirected co-authorships
- **Layout:** D3 force-directed
- **Features:**
  - Top 200 authors ranked list
  - Color by composite score (co-authorship impact)
  - Node size by paper count
  - Highlights major research clusters

**Design Rationale:**
- Undirected (collaborations are mutual)
- Shows which researchers work together
- Geographic and thematic clustering visible

#### **kcore_map.html** — Structural Density
- **Coloring by k-value:**
  - Red: k ≥ 30 (core)
  - Orange: k = 25–29
  - Green: k = 20–24
  - Gray: k < 20
- **Interpretation:** Reveals tightly-interconnected research communities

#### **evolution_graph_full.html** — Field Timeline
- **Visualization:** Stacked area chart, 1977–2026
- **Y-axis:** Publication count by year
- **Colors:** 30 communities
- **Features:**
  - Hover to see community detail
  - Shows field growth trajectory

### 6.2 Design Principles

**1. All papers included (not limited to top 500)**
- Reason: No single threshold captures all important work
- Visualizations are interactive → users can filter/zoom
- Missing papers would bias view of field

**2. Force-directed layouts over hierarchical**
- Reason: No single hierarchy fits citation networks
- Communities emerge naturally from forces
- Better for exploratory analysis

**3. Directed vs. undirected edges**
- Citation network: Directed (A cites B is asymmetric)
- Co-authorship: Undirected (collaboration is mutual)
- Biological networks: Mostly undirected (synapses)

**4. Color schemes**
- Composite score: Gradient (white to red)
- K-core: Categorical (red, orange, green, gray)
- Communities: Categorical (30 distinct colors)

### 6.3 Performance & Scale

**File Sizes:**
- field_map_full.html: ~67 MB (7,503 nodes, 85,589 edges)
- coauthor_map_full.html: ~58 MB (35,641 nodes, 511,670 edges)

**Optimization Techniques:**
- Precomputed node positions (force-directed done server-side)
- JSON compression (minified)
- Lazy edge loading (first 1,000 edges, expand on demand)

**Browser Requirements:**
- Chrome/Firefox 80+
- 8+ GB RAM recommended
- WebGL support for smooth rendering

---

## 7. KNOWN LIMITATIONS & BIASES

### 7.1 Data Limitations

**1. OpenAlex Coverage**
- Not 100% of all connectomics literature
- Some books/chapters not included
- Preprints may have varying metadata quality

**2. Citation Counting**
- Self-citations included
- Citations ≠ influence (citation inflation in some fields)
- Citation lag (recent papers under-cited by nature)

**3. Author Name Normalization**
- 17 merges done manually, not exhaustive
- Chinese names may have multiple romanizations
- Institutional email parsing may create false duplicates

### 7.2 Methodological Biases

**1. PageRank Bias**
- Favors densely-connected subgraphs
- Early adopters of citing patterns score higher
- Doesn't account for field-specific citation norms

**2. K-Core Bias**
- Biased toward large clusters
- Small but important communities may have lower k-values
- Undirected transformation loses citation directionality

**3. Journal Club Selection**
- Composite score formula (80/20) may be sub-optimal
- Thresholds chosen empirically, not theoretically justified
- May miss important recent work (recency bias)

**4. Paper Role Classification**
- Threshold values (10, 37, etc.) are data-driven but arbitrary
- Different fields have different publication/citation patterns
- Method papers underrepresented in traditional metrics

### 7.3 How We Mitigate

**1. Multiple Metrics**
- Use PageRank + k-core + HITS + betweenness
- No single metric tells complete story

**2. Role Classification**
- 10 roles instead of 3 (more nuance)
- In/out-degree captures paper type independently
- Methods papers get explicit boost

**3. Expert Validation**
- Compare top papers against hand-curated seed list
- 185/200 seed papers in corpus (92.5% coverage)
- Career arcs show expected trajectories for known experts

**4. Transparency**
- Document all thresholds and formulas
- Flag assumptions in outputs
- Prepare for critical review

---

## 8. QUALITY ASSURANCE CHECKLIST

### Before "Ready for Review"

- [ ] All 7,503 papers have computed metrics
- [ ] Author merges applied correctly (Gray-Roncal unified to 28 papers)
- [ ] Spot-check: Top 10 papers ranked correctly
- [ ] Spot-check: Lichtman papers present and ranked highly
- [ ] Journal club at threshold 0.20 has ~22 papers
- [ ] Visualizations load without errors (test in Chrome + Firefox)
- [ ] Dashboard links all functional
- [ ] Career arcs show expected trajectories
- [ ] Seed list comparison: 185/200 papers found (92.5%)
- [ ] No missing in-degree/out-degree values
- [ ] K-core decomposition values reasonable (0–32)
- [ ] Community detection returned 30 communities
- [ ] No NaN or Inf values in composite scores

### Ongoing Validation

- **Monthly:** Update corpus with new papers
- **Quarterly:** Recompute PageRank and metrics
- **Yearly:** Review threshold choices and role assignments
- **As needed:** Add author merges as new variants discovered

---

## 9. FUTURE IMPROVEMENTS

### 9.1 Short-Term (Next Sprint)

1. **Automated Author Merging**
   - Implement fuzzy name matching (edit distance < 2)
   - Validate matches against co-authorship patterns
   - Flag ambiguous cases for manual review

2. **Temporal Metrics**
   - Compute PageRank at yearly snapshots
   - Track metric evolution over time
   - Identify "rising stars" vs. "established leaders"

3. **Cross-Validation**
   - Compare rankings against citation counts alone
   - Compare against human expert rankings
   - Sensitivity analysis on weights (80/20 optimal?)

### 9.2 Medium-Term (Next Quarter)

1. **Methods Paper Weighting**
   - Should methods papers be weighted differently in PageRank?
   - Consider temporal discount (older methods less important)
   - Boost infrastructure papers empirically

2. **Community Detection Robustness**
   - Try alternative algorithms (Leiden, GN modularity)
   - Compare community assignments
   - Validate against hand-labeled communities

3. **Seed List Enrichment**
   - Add 15 missing papers (when ready)
   - Verify bioRxiv preprints are published
   - Update metrics and visualizations

### 9.3 Long-Term (Methodology Review)

1. **Composite Score Optimization**
   - Grid search over weights (0–100% PageRank vs. k-core)
   - Optimize against expert rankings
   - Document trade-offs

2. **Role Classification Refinement**
   - Unsupervised clustering of papers by in/out degree
   - Compare to hand-assigned roles
   - Adjust thresholds based on findings

3. **Field-Specific Normalization**
   - Should connectomics papers be scored differently?
   - Account for field size and citation norms
   - Implement per-field PageRank

---

## 10. REFERENCES & DOCUMENTATION

### Key Papers on Methodology

- **PageRank:** Brin & Page (1998), "The Anatomy of a Large-Scale Hypertextual Web Search Engine"
- **HITS:** Kleinberg (1999), "Authoritative sources in a hyperlinked environment"
- **K-core:** Batagelj & Zaversnik (2003), "An O(m) algorithm for cores decomposition"
- **Louvain:** Blondel et al. (2008), "Fast unfolding of communities in large networks"

### Data Sources

- **OpenAlex:** https://openalex.org/ (free, CC0 license)
- **Citation metadata:** Extracted via OpenAlex API
- **Corpus:** `scripts/bibliometrics/output/corpus_final.json`

### Configuration

**Global Parameters:**
```python
DAMPING_FACTOR = 0.85           # PageRank
PAGERANK_ITERATIONS = 100
KCORE_ITERATIONS = 1000
COMPOSITE_WEIGHT_PAGERANK = 0.80
COMPOSITE_WEIGHT_KCORE = 0.20
METHODS_PAPER_THRESHOLD_OUTDEGREE = 37  # Top 5%
IN_OUT_DEGREE_MINIMUM = 10              # Active research threshold
```

---

## Appendix: Data Dictionary

### corpus_final.json
```json
{
  "openalex_id": "string (unique paper ID)",
  "doi": "string (DOI, may be null)",
  "title": "string",
  "year": "integer (1977–2026)",
  "authors": [{
    "name": "string",
    "author_position": "string (first, middle, last)",
    "ror": "string (institution ID, may be null)"
  }],
  "cited_by_count": "integer",
  "publication_date": "string (ISO 8601)",
  "type": "string (journal-article, preprint, etc.)",
  "concepts": [{
    "display_name": "string",
    "level": "integer"
  }]
}
```

### paper_rankings_all.json
```json
[{
  "openalex_id": "string",
  "title": "string",
  "year": "integer",
  "rank": "integer (1–7503)",
  "composite_score": "float (0–1)",
  "pagerank": "float",
  "hits_hub": "float",
  "hits_authority": "float",
  "betweenness": "float",
  "in_degree": "integer",
  "out_degree": "integer",
  "k_core": "integer (0–32)",
  "inferred_role": "string (10 categories)",
  "total_citations": "integer"
}]
```

### author_rankings.json
```json
[{
  "name": "string",
  "rank": "integer (1–35641)",
  "paper_count": "integer",
  "co_author_count": "integer",
  "composite_score": "float",
  "merged": "boolean (was name merged?)"
}]
```

---

**Last Updated:** 2026-03-31  
**Pipeline Version:** 2.0 (end-to-end, all papers, all metrics)  
**Status:** Ready for team review and methodology discussion

