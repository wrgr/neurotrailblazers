# Multi-Signal Inclusion Criteria for Papers Outside Top-500

This document extends the inclusion decision framework with two additional signals:
**Graph position (k-core)** and **Expert authorship**.

---

## The Problem

Papers outside top-500 may be important but underrank due to:
- **Young papers** — not yet accumulated citations (but written by top experts)
- **Niche but central** — high in-degree within corpus but low overall citations
- **Infrastructure papers** — foundational tools (CATMAID, webKnossos) with specialized impact
- **Recent breakthroughs** — just published, led by prolific experts

Current signals miss these cases. We add two structural/authorship signals.

---

## Signal 1: Graph Position (K-Core)

**What it measures:** Where does the paper sit in citation network topology?

**Why it matters:** Papers with k-core ≥ 25 are in the EM connectomics nucleus—deeply embedded in the research community's citations.

**Scoring:**

| K-Core | Interpretation | Score | Include If... |
|--------|---|---|---|
| k ≥ 30 | Inner core (highest structural importance) | 1.0 | Any other signal (review + k≥30 = INCLUDE) |
| k = 25–29 | EM connectomics zone (moderately central) | 0.8 | Any secondary signal (review OR expert author) |
| k = 20–24 | Bridge papers (connect subfields) | 0.6 | Combine with 2+ other signals |
| k = 15–19 | Important but peripheral | 0.4 | Requires 3+ supporting signals |
| k = 10–14 | Very peripheral | 0.2 | Only if expert first author + review cited |
| k < 10 | Extremely niche or very new | 0.0 | Requires special case (breakthrough + top-author) |

**Real example:**
- "Statistical mechanics of complex networks" (k=32, rank 350): Very high structural importance despite low composite score. If mentioned by review → INCLUDE.
- "Connectome fingerprinting" (k=27, rank 242): In EM zone but ranked below 500. Expert nominated → PROMOTE to top-200.

---

## Signal 2: Expert First/Last Authorship

**What it measures:** Is the paper **first-authored or last-authored** by a top-100 prolific expert?

**Why it matters:** 
- Top-100 experts are field leaders; their new work is likely important
- **First author** = primary researcher, originated the work
- **Last author** = senior researcher, group leader, corresponding author, takes intellectual responsibility
- Lean toward inclusion when top experts lead or mentor on a paper (even if not yet highly cited)
- **Note:** We only score first/last authors, not all co-authors (avoids gaming signal by casual collaboration)

**Scoring:**

| Position | Expert Tier | Score | Justification |
|----------|---|---|---|
| First author | Top-50 by citations | 1.0 | Primary author is field leader |
| Last author | Top-50 by citations | 0.9 | Senior/corresponding author is field leader |
| First author | Top-51–100 | 0.7 | Important researcher, likely high quality |
| Last author | Top-51–100 | 0.6 | Senior author from respected group |
| Co-author (top-3 or last-2) | Top-100 | 0.4 | Involved with top researcher but not leading |
| Any co-author | Top-100 | 0.2 | Collaboration signal, weak |
| No top-100 authors | — | 0.0 | No expert signal |

**Real examples:**
- Dorkenwald et al. "FlyWire" (2024): Dorkenwald is top-50 author, even if paper very new → high inclusion priority
- Gray-Roncal et al. (infrastructure): Top author in BossDB/tools → lean toward inclusion of technical papers

---

## Combined Decision Framework

### Decision Matrix: Which papers to promote/add?

```
                    Review-cited    Expert-Authored    k-core≥25    Decision
─────────────────────────────────────────────────────────────────────────────
1. Review + K-core≥25              ✓          -            ✓      → INCLUDE
2. Review + Expert author          ✓          ✓            -      → INCLUDE
3. Review + K-core≥20              ✓          -           ~✓      → INCLUDE (high conf)
4. Expert nominated + K-core≥25    -          ✓            ✓      → INCLUDE
5. Expert authored + K-core≥20     -          ✓           ~✓      → INCLUDE (med conf)
6. Any 2+ signals                  ~          ~            ~      → REVIEW (medium)
7. Any 1 signal                    ?          ?            ?      → REVIEW (low)
8. Domain = off_topic              —          —            —      → SKIP
```

### Inclusion Decision Algorithm

```python
def inclusion_recommendation(paper, review_cited, expert_nominated, 
                             expert_author_score, kcore_score):
    """
    Multi-signal inclusion decision for papers outside top-500.
    """
    signals = []
    confidence = 0
    
    # Signal 1: Review mentions
    if review_cited:
        signals.append("review")
        confidence += 0.25
    
    # Signal 2: Expert nomination
    if expert_nominated:
        signals.append("expert_nominated")
        confidence += 0.25
    
    # Signal 3: Graph position
    if kcore_score >= 0.8:  # k >= 25
        signals.append("kcore_high")
        confidence += 0.20
    elif kcore_score >= 0.6:  # k >= 20
        signals.append("kcore_moderate")
        confidence += 0.10
    elif kcore_score < 0.2:  # k < 10
        confidence -= 0.10  # Penalty for very peripheral
    
    # Signal 4: Expert authorship
    if expert_author_score >= 0.8:  # First author top-50
        signals.append("expert_first_author")
        confidence += 0.20
    elif expert_author_score >= 0.5:  # Co-author with top-50
        signals.append("expert_coauthor")
        confidence += 0.10
    
    # Decision logic
    if confidence >= 0.50:
        return "INCLUDE"
    elif confidence >= 0.35:
        return "REVIEW_HIGH"
    elif confidence >= 0.20:
        return "REVIEW_MEDIUM"
    else:
        return "SKIP"
```

---

## Practical Examples

### Example 1: New Tool Paper (low citations, top expert)

**Paper:** "webKnossos: Open-source tool for 3D image annotation"  
**Year:** 2017  
**Metrics:**
- External citations: 800 (good for tools, but lower than landmark results)
- Composite score: 0.12 (ranked ~450)
- K-core: 22 (moderate, in methods zone)
- First author: Boergens (top-50 infrastructure expert)

**Signals:**
- Review cited? Maybe (tools reviewed in connectomics papers) → +0.25
- Expert nominated? Likely (tool landmark) → +0.25
- K-core ≥ 20? Yes → +0.10
- Expert first author? Yes → +0.20
- **Total confidence:** 0.80

**Decision:** ✅ **INCLUDE** (high confidence)  
**Justification:** Infrastructure paper from top expert; structurally central in citation network; likely underranked due to specialized impact.

---

### Example 2: Young Breakthrough (2024, top author)

**Paper:** "XXXX connectome at single-synapse resolution"  
**Year:** 2024  
**Metrics:**
- External citations: 50 (new)
- Composite score: 0.05 (below threshold)
- K-core: 5 (very new, hasn't integrated into network yet)
- First author: Dorkenwald (top-30 author)

**Signals:**
- Review cited? Likely (if released before review deadline) → +0.25
- Expert nominated? Possibly → +0.20 (uncertain)
- K-core ≥ 25? No → 0
- Expert first author? Yes → +0.20
- **Total confidence:** 0.40–0.65

**Decision:** ❓ **REVIEW** (high confidence)  
**Justification:** Very new paper from major author; wait 1–2 years for citation history to establish structural position. For now: flag for next edition.

---

### Example 3: Highly-Cited Review (well-ranked, even better with signals)

**Paper:** "The connectomics of brain disorders"  
**Year:** 2015  
**Metrics:**
- External citations: 1,757 (very high)
- Composite score: 0.18 (ranked ~280)
- K-core: 29 (very central)
- First author: Fornito (top-100 expert)

**Signals:**
- Review cited? Yes → +0.25
- Expert nominated? Yes (Fornito is expert) → +0.25
- K-core ≥ 25? Yes → +0.20
- Expert first author? Yes → +0.20
- **Total confidence:** 0.90

**Decision:** ✅ **PROMOTE TO TOP-200**  
**Justification:** All signals fire; should be top-200 despite current rank.

---

## Integration with Existing Workflow

### When to Apply These Signals

**Step 13: Inclusion Decisions**
```python
# In 13_inclusion_decisions.py:

from authorship_signal import expert_author_signal, kcore_signal

for paper in candidates_under_review:
    # Existing signals
    review_cited = paper['review_mentions'] >= 2
    expert_nominated = paper['in_expert_gaps']
    
    # New signals
    expert_score = expert_author_signal(paper, top_100_authors)
    kcore_score = kcore_signal(paper, reading_list_enriched)
    
    # Combined decision
    recommendation = inclusion_recommendation(
        paper, review_cited, expert_nominated, 
        expert_score, kcore_score
    )
```

### Expected Impact

- **Papers promoted to top-200:** ~5–10 (mostly expert-authored infrastructure papers)
- **Papers added from below 500:** ~10–15 (review-cited + structurally central)
- **Papers skipped:** ~200–300 (off-topic, very peripheral, no signals)

---

## Risks & Mitigations

**Risk:** Gaming signal by adding collaborators with top experts
- **Mitigation:** Score based on first/last author only, not all co-authors

**Risk:** K-core signal outdated if corpus changes significantly
- **Mitigation:** Recompute k-core after any duplicate merges (step 12)

**Risk:** Expert author list may be incomplete (missing emerging leaders)
- **Justification:** Conservative approach; update list quarterly based on new publications

**Risk:** Young papers never reach inclusion threshold until they accumulate citations
- **Mitigation:** Acceptable; new breakthroughs should wait 1–2 years before ranking high. Top-author signal still captures high-quality work.

---

## Conclusion

Adding **k-core position** and **expert authorship** signals enables:
- ✅ Inclusion of structurally-important papers (bridges, tools, recent breakthroughs)
- ✅ Ranking that respects expert judgment (top authors' papers get boost)
- ✅ More transparent, multi-faceted inclusion criteria
- ✅ Better coverage of infrastructure and foundational work

These signals are **supplementary** (not primary) and **defensible** (based on citation topology + domain expertise).

**Next step:** Implement in step 13 (`13_inclusion_decisions.py`) and test on flagged candidates.
