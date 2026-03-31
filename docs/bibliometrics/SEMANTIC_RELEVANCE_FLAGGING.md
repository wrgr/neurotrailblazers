# Semantic Relevance Flagging: Top 100 Papers & Authors
## Identifying Papers/Authors Potentially Outside Core EM Connectomics

**Date:** 2026-03-31  
**Purpose:** Flag papers and authors in top 100 rankings that may be semantically unrelated to electron microscopy connectomics

---

## 1. UNRELATED PAPERS IN TOP 100

### Papers to Flag (14 total)

**STRONG FLAGS — Likely Unrelated to EM Connectomics:**

| Rank | Title | Year | Issue | Relevance |
|------|-------|------|-------|-----------|
| **5** | Autophagy-Independent Functions of the Autophagy Machinery | 2019 | Cell biology, not connectomics | Remove |
| **8** | Molecular mechanisms of cell death: recommendations of the Nomenclature Committee | 2018 | Cell biology nomenclature, not connectomics | Remove |
| **12** | Fiji: an open-source platform for biological-image analysis | 2012 | General image analysis tool (not connectomics-specific) | Consider removing |
| **29** | Building connectomes using diffusion MRI: why, how and but | 2017 | Functional connectomics (dMRI), not structural EM | Keep (related but different modality) |
| **30** | Brain Networks in Schizophrenia | 2014 | Clinical psychiatry focus, not methodology | Borderline |
| **39** | Graph-based network analysis of resting-state functional MRI | 2010 | fMRI network analysis, not EM | Remove |
| **41** | Deep Learning | 2015 | General ML survey, tangential at best | Remove |
| **45** | ImageNet classification with deep convolutional neural networks | 2017 | Computer vision, not connectomics | Remove |
| **46** | Understanding the Emergence of Neuropsychiatric Disorders With Network... | 2018 | Psychiatric focus via functional MRI | Borderline |
| **47** | Magnetic Resonance Imaging and Graph Theoretical Analysis of Complex Brain Networks | 2011 | MRI-based networks, not EM | Remove |
| **70** | Assessment of system dysfunction in the brain through MRI-based connectomics | 2013 | Clinical MRI focus, not EM | Remove |
| **86** | The Anatomical Distance of Functional Connections Predicts Brain Networks in Schizophrenia | 2012 | Clinical psychiatry + fMRI | Remove |
| **89** | Connectomic Intermediate Phenotypes for Psychiatric Disorders | 2012 | Psychiatric focus, uses term "connectome" but not EM | Remove |
| **100** | Disrupted Modularity and Local Connectivity of Brain Functional Networks | 2010 | Functional connectivity, not structural EM | Remove |

### Recommendation

**Remove from EM connectomics bibliography (likely ranked high due to "connectome" terminology):**
- Ranks: 5, 8, 12, 39, 41, 45, 47, 70, 86, 89, 100
- **Total: 11 papers to filter**

**Keep but note as cross-domain (network analysis methods):**
- Ranks: 29, 30, 46 (2–3 papers, borderline)

---

## 2. UNRELATED AUTHORS IN TOP 100

### Authors Primarily Focused on fMRI/Functional Connectomics (NOT EM Connectomics)

| Rank | Author | Papers | EM Focus | fMRI Focus | Assessment |
|------|--------|--------|----------|-----------|------------|
| **8** | Yong He | 57 | 16 (28%) | 3 (5%) | **BORDERLINE** — Network neuroscience, not EM |
| **14** | Martijn P. van den Heuvel | 50 | 18 (36%) | 6 (12%) | **BORDERLINE** — "Human Connectome" but fMRI-based |
| **16** | Stephen M. Smith | 47 | 21 (45%) | 16 (34%) | **STRONG FLAG** — Human Connectome Project (fMRI/dMRI lead) |
| **20** | Andrew Zalesky | 42 | 13 (31%) | 6 (14%) | **BORDERLINE** — Network psychiatry, not EM |

### Assessment

**These authors work on "connectomics" but in a DIFFERENT sense:**
- They use **fMRI + diffusion MRI** (non-invasive human imaging)
- They analyze **functional/structural connectivity** in living brains
- They focus on **clinical psychiatry** applications
- They are NOT electron microscopy connectomics researchers

**Should they be included in EM connectomics bibliography?**

**Argument for KEEP:**
- Network analysis methods they develop are applicable to EM connectomics
- Graph theory and centrality metrics are field-agnostic
- BrainNet Viewer and other tools used in connectomics community
- Work on connectome at coarse resolution (whole-brain networks)

**Argument for REMOVE:**
- Not working on EM data or structural connectomes
- Different scientific questions (functional vs. structural)
- Using term "connectome" but not in EM sense
- Rankings inflated by citation of "connectome" papers without EM content

### Recommendation

**Keep but flag with asterisk noting "functional connectomics focus":**
- Ranks: 8, 14, 16, 20
- Note in metadata: "fMRI/functional connectivity, not EM connectomics"
- Consider: Separate "network methods" category from "EM connectomics"

---

## 3. CORE EM CONNECTOMICS AUTHORS (Top 100)

For comparison, here are researchers who ARE clearly EM connectomics focused:

| Rank | Author | Papers | Research Focus |
|------|--------|--------|-----------------|
| **1** | Jeff W. Lichtman | 92 | EM connectomics (Drosophila, Larva) ✓ |
| **2** | Olaf Sporns | 76 | Network neuroscience + connectomics ✓ |
| **3** | Albert Cardona | 72 | Drosophila EM connectomics ✓ |
| **4** | Edward T. Bullmore | 70 | fMRI + network analysis (BORDERLINE) |
| **5** | H. Sebastian Seung | 64 | EM connectomics, AI for segmentation ✓ |
| **7** | Gregory S.X.E. Jefferis | 60 | Drosophila EM connectomics ✓ |
| **9** | Davi D. Bock | 56 | EM connectomics methods ✓ |
| **10** | David C. Van Essen | 53 | Human brain mapping (mostly fMRI) (BORDERLINE) |
| **11** | Philipp Schlegel | 52 | Drosophila EM connectomics ✓ |
| **12** | Edward S. Boyden | 51 | EM techniques development ✓ |
| **13** | Gerald M. Rubin | 51 | Drosophila neurobiology ✓ |
| **15** | Hanspeter Pfister | 48 | EM image analysis + AI ✓ |
| **17** | Sven Dorkenwald | 45 | EM connectomics (Drosophila, Zebrafish) ✓ |
| **18** | Moritz Helmstaedter | 43 | EM connectomics + theory ✓ |
| **19** | Aljoscha Nern | 42 | Drosophila connectomics ✓ |

---

## 4. SUMMARY & FILTERING RECOMMENDATIONS

### Papers to Filter Out (Remove from EM connectomics rankings)

**High-confidence removals (clear non-connectomics):**
1. Rank 5: Autophagy (cell biology)
2. Rank 8: Cell death mechanisms
3. Rank 41: Deep Learning (general ML)
4. Rank 45: ImageNet/CNNs (computer vision)

**Medium-confidence removals (connectomics by fMRI, not EM):**
5. Rank 29: dMRI connectomics (different modality, but related)
6. Rank 39: fMRI network analysis
7. Rank 47: MRI-based networks
8. Rank 70: Clinical MRI connectomics
9. Rank 86: Psychiatric MRI
10. Rank 89: Connectomic phenotypes
11. Rank 100: Functional networks

**Low-confidence removals (tools/general connectomics):**
12. Rank 12: Fiji (general image analysis tool)
13. Rank 30, 46: Clinical/psychiatric focus via connectomics

### Authors to Flag (Not Remove, But Flag)

**Functional connectomics researchers (keep but flag):**
- Rank 8: Yong He
- Rank 14: Martijn P. van den Heuvel
- Rank 16: Stephen M. Smith
- Rank 20: Andrew Zalesky

**Action:** Add "connectomics_modality" field to author_rankings.json:
```json
{
  "name": "Stephen M. Smith",
  "rank": 16,
  "connectomics_modality": "fMRI/dMRI (functional)",
  "note": "Human Connectome Project — not EM connectomics"
}
```

---

## 5. REVISED FILTERING STRATEGY

**Option 1: Conservative (Remove 11 papers)**
- Remove papers clearly off-topic (cell biology, ML, fMRI)
- Keep network methods papers
- Updated ranking: top 90 papers for EM connectomics

**Option 2: Moderate (Remove 4 papers)**
- Remove only obvious off-topic (autophagy, cell death, general ML, vision)
- Keep all connectomics-related papers (including fMRI)
- Updated ranking: top 96 papers

**Option 3: No filtering**
- Keep all papers, but add "connectomics_type" metadata
- Include in outputs but note modality (EM, fMRI, dMRI)
- Most transparent approach

### Recommended: Option 3 (Metadata Flagging)

**Why:** 
- Preserves full ranking while being transparent
- Shows how "connectome" term is used across neuroscience
- Users can filter themselves
- Easier to justify to critics

**Implementation:**
1. Add "connectomics_type" field to papers:
   - "em" = EM microscopy connectomics
   - "functional" = fMRI/functional connectivity
   - "dmri" = diffusion MRI connectomics
   - "network_methods" = methods applicable to connectomics
   - "unrelated" = cell biology, general ML, etc.

2. Add "connectomics_modality" field to authors:
   - "em" = EM connectomics researcher
   - "functional" = fMRI/network neuroscience
   - "mixed" = both EM and functional

3. Filter at visualization layer:
   - Default: show all (including borderline)
   - Toggle: "EM connectomics only" (filters out functional)
   - Toggle: "Core EM researcher only" (filters authors)

---

## 6. ACTION ITEMS

- [ ] Add "connectomics_type" to paper_rankings_all.json
- [ ] Add "connectomics_modality" to author_rankings.json
- [ ] Create filtered versions:
  - paper_rankings_em_only.json (EM connectomics papers)
  - author_rankings_em_only.json (EM connectomics researchers)
- [ ] Update visualizations to support filtering
- [ ] Document filtering rationale in BIBLIOGRAPHY_ANALYSIS_DOCS.md
- [ ] Prepare for methodology review discussion

---

**Note:** This analysis is data-driven (keyword + title analysis). Manual expert review recommended before finalizing filters.

