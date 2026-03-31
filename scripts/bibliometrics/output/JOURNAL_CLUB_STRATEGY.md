# Journal Club Selection Strategy: Topic Diversity + Importance

## Key Insight

**K-core alone is not the right filter for journal club.** Instead: 
- Pick representative papers from each **topic community**
- Within each community, rank by **computed importance** (composite score)
- This ensures **breadth** (all subtopics) AND **depth** (best-in-class for each)

## Seven Connectomics-Relevant Communities

### Community 9: Network Neuroscience & Graph Theory
- **Size:** 1,613 papers | **In k≥25:** 9
- **Role:** Foundational theory for connectomics analysis
- **Key papers:** AAL atlas, network topology analysis, cortical organization
- **Select:** 2-3 papers (many already in k≥25)

### Community 265: Network Science & Graph Algorithms
- **Size:** 532 papers | **In k≥25:** 2
- **Role:** Mathematical foundations (motifs, community detection)
- **Key papers:** Random graphs, network motifs, visualization tools
- **Select:** 2-3 papers (some in k≥25)

### Community 267: Drosophila Circuits & Connectomics
- **Size:** 1,173 papers | **In k≥25:** 2
- **Role:** Landmark connectome studies + circuit analyses
- **Key papers:** Circadian clock connectome, mushroom body circuits
- **Select:** 2-3 papers (mostly k=20-24 bridge zone)

### Community 268: Systems Neuroscience & General Biology
- **Size:** 1,967 papers | **In k≥25:** 1
- **Role:** Broader brain imaging & behavioral context
- **Key papers:** Brain atlases, reinforcement learning, cell classification
- **Select:** 1-2 papers (emerging work, k=20-24)

### Community 266: Brain Mapping & Neuroanatomy
- **Size:** 402 papers | **In k≥25:** 0
- **Role:** Large-scale brain reconstruction & mapping
- **Key papers:** Multi-scale brain mapping, neuroanatomy tools
- **Select:** 1-2 papers (k=20-24 bridge zone)

### Community 11: Imaging & Experimental Methods
- **Size:** 484 papers | **In k≥25:** 0
- **Role:** Imaging technologies & sample preparation
- **Key papers:** Expansion sequencing, optical visualization, staining methods
- **Select:** 2-3 papers (cutting-edge methods, k=20-24)

### Community 269: Sensory Systems (Retina & Vision)
- **Size:** 274 papers | **In k≥25:** 0
- **Role:** Complete connectome of sensory circuits
- **Key papers:** Retinal cell atlas, retinal microcircuits
- **Select:** 1-2 papers (model system, k=20-24)

## Selection Strategy

**For each of the 7 communities:**
1. Start with the top-ranked paper by composite score
2. If already in k≥25, include it (structurally validated)
3. If not in k≥25 but in k=20-24, evaluate:
   - Does it move the field forward?
   - Is it methods-heavy or insight-heavy?
   - Does it fill a genuine gap?
4. Skip papers that are:
   - Too specialized/tangential
   - Redundant (we already have X papers on this technique)
   - Methods papers without connectomics application

## Expected Outcome

- **Total papers:** 20-30 papers (2-3 per community, some overlap)
- **Breadth:** All major connectomics subfields represented
- **Depth:** Best-in-class papers within each subtopic
- **Quality:** Combination of k≥25 (structurally core) + k=20-24 (emerging)

## Advantages Over Pure K-Core

| Criterion | K-Core Only | Community-Based |
|-----------|------------|-----------------|
| **Topic Coverage** | Biased toward highly-cited topics | Balanced across all topics |
| **Interpretability** | "Top 200 by score" | "Best papers in each subtopic" |
| **Teaching Value** | Mixed - some off-topic | High - clear story per community |
| **Emerging Work** | Underrepresented | Well-represented via k=20-24 |
| **Noise Filtering** | Poor (catches some noise) | Excellent (excludes 17 noise communities) |

## Implementation

1. **Review the 7 communities** (see above)
2. **Select 1-3 papers per community** using the importance ranking
3. **Document selection rationale** for each paper ("Why did we pick this?")
4. **Total target:** 20-30 papers for journal club
5. **Caveat on OCAR:** Papers from k=20-24 get "TBD" OCAR entries as planned

## Excluded Noise Communities

These 17 communities are off-topic and automatically filtered:
- Geology (seismic tomography)
- Chemistry & Materials Science (perovskites, graphene, etc.)
- Physics (astronomy, quantum computing)
- Computer Science (5G networks)
- Econometrics
- Medicine (Japanese gastric cancer, niche specialties)
- Environmental Science

**Benefit:** The community detection found these automatically through citation chasing, but they're not relevant to connectomics and are now easy to identify and exclude.
