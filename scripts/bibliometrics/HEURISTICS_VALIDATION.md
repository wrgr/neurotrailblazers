# Heuristics Validation & Sensitivity Analysis

This document addresses a critical question: **Are the multi-signal scoring weights defensible, or just brittle?**

---

## The Problem

We use fixed weights across several classifiers:

### Duplicate Detection
```
score = 0.35 × title_sim + 0.25 × citation_jaccard + 0.15 × author_overlap 
      + 0.15 × mutual_noncite + 0.10 × preprint_pattern
```

### Author Name Dedup
```
score = 0.25 × name_similarity + 0.20 × first_name_compat + 0.25 × coauthor_jaccard
      + 0.15 × citation_neighborhood + 0.15 × shared_paper
```

### Domain Classification
```
Three-layer: journal (strongest) → concepts → keywords
```

**The honest critique:**
- Weights are somewhat arbitrary (not learned from data)
- No ground truth corpus for validation
- "Makes sense" ≠ statistically justified
- Could be brittle to corpus composition changes

---

## Defense Strategy: Multi-Faceted Validation

### 1. Known-Case Validation (Highest Priority)

**Approach:** Apply classifiers to papers we *know* are duplicates/same person.

#### Duplicate Validation Set
Known preprint-published pairs in connectomics:

```json
[
  {
    "preprint_doi": "10.1101/2023.03.29.534851",
    "published_doi": "10.1101/2024.03.29.534851",
    "title_similarity": "very high",
    "known_decision": "DUPLICATE",
    "expected_score": ">0.75"
  },
  {
    "id1": "https://openalex.org/W3005470768",
    "id2": "https://openalex.org/W3005470769",
    "note": "bioRxiv v1 vs v2 (self-plagiarism, different DOI)",
    "known_decision": "DUPLICATE",
    "expected_score": ">0.70"
  }
]
```

**To execute:**
1. Manually identify 20–30 known duplicate pairs (ask field experts)
2. Run classifier on all pairs
3. Compute precision@threshold:
   - At score ≥0.70: what % are actually duplicates?
   - At score ≥0.50: what % are actually duplicates?
   - At score ≥0.40: what % are actually duplicates?
4. **Decision rule:** Only AUTO_MERGE if precision ≥95% at that threshold

#### Author Dedup Validation Set
Known name variants of prolific authors:

```json
[
  {
    "canonical": "H. Sebastian Seung",
    "variant": "H Sebastian Seung",
    "note": "period missing",
    "known_decision": "SAME_PERSON",
    "papers_shared": 142
  },
  {
    "canonical": "Olaf Sporns",
    "variant": "O Sporns",
    "note": "first initial only",
    "known_decision": "SAME_PERSON",
    "papers_shared": 215
  },
  {
    "canonical": "Stephen J Smith",
    "variant": "Stephen M Smith",
    "note": "middle initial different",
    "known_decision": "DIFFERENT_PEOPLE",
    "papers_shared": 0
  }
]
```

**Metric:** Precision (how many SAME_PERSON predictions are correct) at each threshold.

---

### 2. Ablation Analysis: Which Signals Matter Most?

**Approach:** Train logistic regression on validation set to learn signal weights.

```python
# Pseudo-code
from sklearn.linear_model import LogisticRegression

X = np.array([
    [title_sim, citation_jac, author_overlap, mutual_noncite, preprint_pattern],
    ...
])
y = np.array([1, 0, 1, ...])  # 1=duplicate, 0=not

model = LogisticRegression()
model.fit(X, y)

learned_weights = model.coef_[0]
# Compare to our fixed weights: [0.35, 0.25, 0.15, 0.15, 0.10]
```

**Expected outcome:**
- If learned weights ≈ fixed weights → our heuristic is sound
- If learned weights are very different → our heuristic is brittle
- If one signal dominates → others might be noise

**Real validation:** Does the logistic model with learned weights outperform our fixed weights on a held-out test set?

---

### 3. Sensitivity Analysis: How Brittle?

**Approach:** Test robustness to weight perturbations.

For each classifier, run 1000 Monte Carlo trials with randomly perturbed weights:

```python
import numpy as np

def perturb_weights(base_weights, std=0.05):
    """Add Gaussian noise to weights, renormalize."""
    noisy = base_weights + np.random.normal(0, std, len(base_weights))
    return noisy / noisy.sum()

# For each paper pair in corpus:
# - Compute score with base weights
# - Compute score with 1000 perturbed weight sets
# - Track: does final decision (MERGE/REJECT) change?

decisions_base = [score > 0.70 for score in base_scores]
decisions_perturbed = []
for _ in range(1000):
    perturbed_w = perturb_weights(base_weights, std=0.05)
    perturbed_scores = compute_scores_with_weights(papers, perturbed_w)
    decisions_perturbed.append([s > 0.70 for s in perturbed_scores])

# Stability: what % of decisions flip with 5% weight noise?
flips = sum(1 for i in range(len(papers))
            if decisions_base[i] != decisions_perturbed[i])
flip_rate = flips / len(papers)
print(f"Decision flip rate (5% weight noise): {flip_rate:.1%}")
```

**Interpretation:**
- flip_rate < 2% → robust (weights don't matter much)
- flip_rate 2–5% → moderate robustness
- flip_rate > 10% → brittle (sensitive to weights)

**Threshold:** Only trust AUTO_MERGE if flip_rate < 2%.

---

### 4. Signal Independence Check: Correlation Matrix

**Approach:** Ensure the 5 signals aren't redundant.

```python
import pandas as pd

# For a sample of 1000 paper pairs:
signals_df = pd.DataFrame({
    'title_similarity': [...],
    'citation_jaccard': [...],
    'author_overlap': [...],
    'mutual_noncitation': [...],
    'preprint_pattern': [...],
})

correlation_matrix = signals_df.corr()
print(correlation_matrix)
```

**Expected pattern:**
```
                     title  citation author mutual preprint
title               1.00    0.15     0.10   0.12   0.30
citation            0.15    1.00     0.25   0.05   0.08
author              0.10    0.25     1.00   0.10   0.05
mutual              0.12    0.05     0.10   1.00   0.20
preprint            0.30    0.08     0.05   0.20   1.00
```

**Interpretation:**
- If |correlation| > 0.6 between any pair → signals are redundant, simplify
- If all correlations < 0.3 → signals are independent and additive (good)
- If all correlations ≈ 0 → signals may not be connected to truth

---

### 5. Domain Classification Cross-Validation

**Approach:** Validate journal-based classification against manual samples.

1. **Sample 100 papers randomly** from each confidence bin:
   - Top-100 papers (should be em_connectomics)
   - Papers ranked 200–300 (mixed)
   - Papers ranked 400–500 (should be mostly em_connectomics)
   - Papers ranked 501–2000 (off-topic expected)

2. **Manual annotation:** Have 2 experts independently label:
   - "Definitely em_connectomics", "Probably em_connectomics", "Unclear", "Probably not", "Definitely not"

3. **Compute metrics:**
   - Precision: of papers labeled em_connectomics, how many experts agree?
   - Recall: of papers experts label em_connectomics, how many did classifier catch?
   - Inter-rater agreement: do the two experts agree?

4. **Decision rule:** Only filter by domain if precision ≥90%.

---

## Empirical Validation: What We Need To Do

### Minimum Viable Validation (2–3 hours)

1. **Known-case testing** (30 min)
   - Manually collect 20 known duplicate pairs
   - Run classifier, compute precision@0.70 and @0.50
   - If precision ≥95% at 0.70 → safe for AUTO_MERGE at 0.70
   - If precision ≥90% at 0.50 → can lower threshold to 0.50

2. **Domain classification spot-check** (20 min)
   - Sample 50 papers marked "off-topic"
   - Read titles, check if truly off-topic
   - If >90% truly off-topic → classifier is good

3. **Signal correlation check** (10 min)
   - Compute correlation matrix on 1000 random pairs
   - Check for redundancy
   - If any pair >0.6 → consider dropping one signal

### Comprehensive Validation (full analysis)

Add:
- Ablation study (train logistic regression)
- Sensitivity analysis (1000 weight perturbations)
- Expert annotation (100+ samples with 2+ raters)

---

## Conservative Decision Thresholds (Until Validated)

**Until we have known-case validation:**

| Category | Current Threshold | Conservative Threshold | Justification |
|----------|-------------------|----------------------|---|
| Duplicate AUTO_MERGE | ≥0.70 | ≥0.80 | Err on side of keeping both |
| Author SAME_PERSON | ≥0.65 | ≥0.75 | Err on side of separate authors |
| Domain: Filter off-topic | ≥0.5 | Require spot-check first | Domain classification unvalidated |

**Auto-review rules (no human TSV review):**
- Duplicates ≥0.80 → AUTO_MERGE (log all decisions)
- Duplicates 0.50–0.79 → FLAG for human review (require TSV)
- Authors ≥0.75 → AUTO_MERGE (log all decisions)
- Authors 0.50–0.74 → FLAG for human review

---

## Recommended Workflow Until Validation

### Phase A: Validation (1–2 days)

1. Collect known duplicates and author variants (ask field experts)
2. Run classifiers on validation set
3. Compute precision@threshold
4. Decide: what thresholds are safe for AUTO_MERGE?

### Phase B: Auto-Review (Only for High-Confidence)

Use conservative thresholds (0.80 for duplicates, 0.75 for authors):
- Decisions ≥threshold → apply automatically, log all
- Decisions < threshold → flag for human TSV review

### Phase C: Sensitivity Testing (Optional, but Recommended)

Run weight perturbation study to assess brittle-ness.

### Phase D: Final Commit

Once precision ≥95% at chosen threshold, apply all decisions and rerank.

---

## Red Flags: When NOT to Trust These Heuristics

- ❌ Applying to a **different field** (connectomics-specific tuning)
- ❌ **Corpus composition changed drastically** (10× larger, new source)
- ❌ **OpenAlex indexing rules changed** (different DOI assignment)
- ❌ **No validation on known cases** (purely heuristic)
- ❌ **Thresholds tuned to specific results** (overfitting to data)

---

## Conclusion

The heuristics "make sense" because:
1. Title similarity is fast and precise for exact duplicates
2. Citation neighborhood captures structural similarity
3. Author overlap handles co-authorship clusters
4. Journal name is a proven strong signal (domain classification)

BUT we should not treat them as gospel until:
1. ✅ Validated on known cases (precision ≥95%)
2. ✅ Shown to be robust to weight perturbations
3. ✅ Signals verified to be independent (not redundant)

**Recommended action:** Run minimum viable validation (known-case testing + spot-checks) before AUTO_MERGE.

**Timeline:** 2–4 hours for validation, then safe to proceed.
