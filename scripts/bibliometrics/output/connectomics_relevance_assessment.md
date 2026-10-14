# Connectomics Relevance Assessment - PRIMARY Corpus

**Analysis Date:** 2026-04-01  
**Corpus:** 959 papers (K≥25 + In-degree≥2)

---

## Executive Summary

The PRIMARY corpus contains papers across five connectomics relevance tiers:

| Category | Papers | % | Status | Notes |
|----------|--------|---|--------|-------|
| **🟢 Core EM Connectomics** | 288 | 30% | KEEP ALL | Direct nanoscale EM focus |
| **🟡 Secondary Connectomics (fMRI/MRI)** | 178 | 19% | KEEP IF COMPREHENSIVE | Macro-scale, different methods |
| **🔵 Foundational (Methods/Theory)** | 63 | 7% | KEEP ALL | Essential foundations |
| **🟠 General Neuroscience** | 331 | 35% | MIXED | ~50% likely relevant |
| **⚫ Uncertain/Unclassified** | 99 | 10% | REVIEW | Includes C elegans, stats |

---

## Detailed Assessment

### 🟢 CORE EM CONNECTOMICS (288 papers)

**What:** Electron microscopy connectomics at nanoscale

**Profile:**
- Avg rank: Top 100K (by composite score)
- Avg in-degree: 61 citations within corpus
- Landmark papers at top (FlyWire, Hemibrain, MICrONS, H01, Kasthuri)

**Key Authors:**
- H. Sebastian Seung (connectomics pioneer)
- Gregory S.X.E. Jefferis (FlyWire project)
- Moritz Helmstaedter (EM methods)
- Jeff W. Lichtman (connectomics infrastructure)

**Assessment:** These are the core of connectomics. Directly relevant.

**Action:** **KEEP ALL** - This is the primary focus of the field.

---

### 🟡 SECONDARY CONNECTOMICS - fMRI/MRI (178 papers)

**What:** Macro-scale network analysis using diffusion MRI, functional MRI, structural MRI

**Profile:**
- Avg rank: ~Top 13K
- Avg in-degree: 44 citations (lower than core EM)
- Large, active field

**Key Authors:**
- Edward T. Bullmore (41 papers) - network neuroscience pioneer
- Olaf Sporns (37 papers) - complex brain networks
- Danielle S. Bassett (25 papers) - network dynamics
- Yong He (22 papers) - human connectomics

**Why Include:**
- Network analysis methods apply across scales
- Large established field with own literature base
- Many computational methods are shared with EM work

**Why Exclude:**
- Different data type (MRI signal vs. structural reconstruction)
- Different spatial scale (mm vs. nm)
- Different interpretation (functional vs. anatomical)

**Assessment:** SECONDARY to EM connectomics but still connectomics-related.

**Action:** **KEEP IF** pursuing comprehensive connectomics understanding  
**REMOVE IF** focusing narrowly on EM reconstruction

---

### 🔵 FOUNDATIONAL - Methods & Graph Theory (63 papers)

**What:** Graph theory, complex networks, machine learning, computational methods

**Profile:**
- Avg rank: ~Top 3K (high quality)
- Avg in-degree: 103 (highest!) - frequently cited foundation
- Key papers: Small-world networks, scale-free networks, community detection

**Key Authors:**
- Barabási, Strogatz, Newman, Freeman, Batagelj

**Assessment:** These are used across ALL connectomics work. The theoretical and computational foundations.

**Action:** **KEEP ALL** - Essential infrastructure for any connectomics analysis

---

### 🟠 GENERAL NEUROSCIENCE (331 papers)

**What:** Brain structure, function, development, disease, circuits

**Profile:**
- Avg rank: ~Top 12K
- Avg in-degree: 58 citations
- MIXED relevance - some highly relevant, some tangential
- Lowest-ranked papers show poor connectomics signal

**Assessment:** Approximately **50% connectomics-relevant**, 50% tangential

**Connectomics-Relevant Subset:**
- Papers on neural circuits and connectivity
- Brain development and connectome assembly
- Network organization principles
- Examples: C. elegans connectome, connectome-based disease studies

**Tangential Subset:**
- General fMRI studies not connected to connectomics
- Cell biology and molecular neuroscience
- Behavioral neuroscience without network focus
- Disease studies using non-connectomics methods

**Example Low-Relevance Papers:**
- "Electrophysiological correlates of intrinsic brain networks" (Rank 6996)
- "Micro-connectomics: probing neuronal networks..." (Rank 7076)
- "Growing together: sex differences in development" (Rank 7086)

**Action:** **MIXED** - Many are relevant, but corpus could be refined by removing tangential papers

---

### ⚫ UNCERTAIN/UNCLASSIFIED (99 papers)

**What:** Papers without clear domain label

**Profile:**
- Avg rank: ~Top 22K (lower quality signal)
- Avg in-degree: 37 citations (lowest)
- Includes: C. elegans connectome papers, statistical methods, unclassified neuroscience

**Key Papers:**
- "The structure of C. elegans connectome" (Rank 9) - HIGHLY RELEVANT
- "Controlling False Discovery Rate" (Rank 22) - Statistical methods, FOUNDATIONAL
- "Small-world human brain networks" (Rank 15) - Highly relevant, CONNECTOMICS

**Assessment:** ~70-80% likely relevant to connectomics

**Action:** **NEEDS MANUAL REVIEW** - Some are landmark papers (C elegans), others are methods papers

---

## Strategic Options

### Option 1: Pure EM Connectomics (351 papers)
```
Core EM (288) + Foundational (63) = 351 papers
```
**For:** Researchers focused exclusively on nanoscale connectome reconstruction  
**Against:** Misses theoretical context and methods inspiration from macro-scale work

---

### Option 2: Comprehensive Connectomics (959 papers - CURRENT)
```
All categories = 959 papers
```
**For:** Holistic understanding of connectomics field across scales  
**Against:** Includes peripheral general neuroscience papers

---

### Option 3: Connectomics-Focused (529 papers - RECOMMENDED)
```
Core EM (288) + Secondary Connectomics (178) + Foundational (63) = 529 papers
```
**For:** 
- Covers both nanoscale (EM) and macro-scale connectomics
- All major connectomics methodologies included
- Avoids tangential general neuroscience papers
- Cleaner focus while maintaining theoretical breadth

**Against:** Removes general neuroscience context that some projects might need

---

## Michael Milham Analysis

**Profile:** 24 papers as last author in PRIMARY corpus

**Domain Distribution:**
- fMRI/MRI Connectomics: 12 papers (50%)
- General Neuroscience: 7 papers (29%)
- EM Connectomics: 2 papers (8%)
- Methods/ML: 2 papers (8%)

**Assessment:** 
- Milham is a leader in **functional connectomics** (fMRI, human brain networks)
- NOT an EM connectomics person
- His cluster (secondary connectomics) is well-represented in PRIMARY corpus
- Papers validated through in-degree≥2 requirement (multiple citations within corpus)

**Conclusion:** Milham is appropriately included as a secondary connectomics expert. His fMRI work provides important network analysis methodology used in EM connectomics. However, his papers are NOT at the core of the nanoscale EM focus.

---

## Recommendations

1. **For RAG Training:**
   - Recommended: **Option 3 (Connectomics-Focused, 529 papers)**
   - Provides comprehensive methodology with focused relevance
   - Removes tangential general neuroscience papers

2. **For Paper Selection:**
   - **Must Keep:** Core EM (288) + Foundational (63) = 351 papers
   - **Should Consider:** Secondary Connectomics (178) - if training models on network analysis
   - **Can Review/Remove:** Lowest-ranked General Neuroscience papers (rank >5000)

3. **For Emerging Papers Watch List:**
   - All 22 emerging papers are from Core EM or Secondary Connectomics categories
   - Good indicator of field focus

4. **Future Manual Review:**
   - 99 uncertain papers - prioritize top-ranked ones (C elegans, statistical methods)
   - 100-150 lowest-ranked general neuroscience papers could be candidates for removal

---

## Domain-Connectomics Mapping

| Domain | Coverage | Core Relevance | Use Case |
|--------|----------|---|---|
| em_connectomics | 30% | ⭐⭐⭐ High | Primary focus |
| mri_connectomics | 18% | ⭐⭐ Medium | Methods, theory |
| methods_ml | 3% | ⭐⭐⭐ High | Infrastructure |
| network_science | 3% | ⭐⭐⭐ High | Foundations |
| neuroscience | 34% | ⭐ Low-Medium | Context (mixed) |
| unknown | 10% | ⭐⭐ Medium | Some landmarks |
| off_topic | 0.2% | ✗ None | Noise (keep 0) |

