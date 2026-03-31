# K-Core Filtering Strategy: Tiered Approach

## Three Filtering Tiers

### TIER 1: Ultra-Core (k ≥ 32) – Seminal Papers
- **Papers:** 213
- **% of corpus:** 2.7%
- **Use case:** Essential foundational work, landmark datasets
- **Profile:** Highest citation density, well-established methods
- **Risk:** Too narrow; misses emerging subfields and recent advances

### TIER 2: EM Connectomics Core (k ≥ 25) ⭐ PRIMARY
- **Papers:** 1,064
- **% of corpus:** 13.4%
- **Use case:** Main analysis corpus for statistics, graphs, unlisted page
- **Profile:** 
  - Natural inflection point in CDF
  - Balances structural rigor with field completeness
  - Includes early bridge papers
- **Characteristics:** Dense core + emerging connections
- **Risk:** May underrepresent very recent work (2023+)

### TIER 3: Core + Bridge (k ≥ 20) – Emerging Work
- **Papers:** 2,074
- **% of corpus:** 26.2%
- **Use case:** Reference set for journal club, emerging technique discovery
- **Profile:**
  - Adds all bridge papers between subfields
  - Better representation of recent/emerging work
  - More technique diversity
- **Risk:** Includes some peripheral work; less structurally coherent

## Statistical Tradeoffs

| Metric | k≥32 | k≥25 ⭐ | k≥20 |
|--------|------|---------|------|
| **Structural Density** | Highest | High | Medium |
| **Field Representation** | Narrow | Good | Better |
| **Recent Work (2021+)** | Poor | Moderate | Good |
| **Technique Diversity** | Limited | Good | Excellent |
| **Author Representation** | Key only | Key + rising | Inclusive |
| **Citation Signal** | Strong | Strong | Moderate |

## Recommended Usage

### For Main Analysis (Statistics & Graphs on Unlisted Page)
✓ **Use TIER 2 (k ≥ 25): 1,064 papers**
- Principled topology-based selection
- Natural CDF inflection point
- Good balance between rigor and completeness
- Sufficient for robust statistics

### For Journal Club Selection
**Start with TIER 2 (k ≥ 25) as base, then add strategic papers from TIER 3 (k=20–24):**

#### Criteria for Adding Papers from k=20–24 Bridge Zone:
1. **Emergence signal:** First paper on a novel technique/hardware
2. **Field gap:** Technique not represented in k≥25 set
3. **High-impact venue:** Nature, Science, eLife, PNAS (establishes importance)
4. **Citation velocity:** Recent papers being rapidly cited
5. **Author diversity:** Rising authors, new labs in connectomics

#### Criteria to EXCLUDE Even if Structurally Relevant:
- Purely methodological (image processing, ML) with no connectomics application
- Tangential to connectomics (general neuroscience, cell biology)
- Redundant technique coverage (5th paper on same method)

## Implementation

1. **Start:** Load `corpus_kcore_25.json` (1,064 papers) for main analysis
2. **Enhance:** Review `corpus_kcore_20.json` (2,074 papers) for journal club additions
3. **Document:** Track why each k=20–24 paper was added to journal club
4. **Communicate:** Make tradeoffs explicit on website ("Primary corpus: k≥25 structural core; 
   journal club includes emerging work from k≥20 with documented rationale")

## Key Insight

The **CDF shows a natural breakpoint at k=25** (1,064 papers):
- Below k=25: smooth gradient (no dramatic changes)
- Above k=25: steep rise (213→548→939→1,064 at k=32→27→26→25)
- This inflection point makes k=25 the principled choice

For journal club, adding carefully-selected papers from the k=20–24 band captures emerging 
work while maintaining the structural rigor of the core.
