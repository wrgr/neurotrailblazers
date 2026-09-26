# Expert Seed Papers Collection

## Approach & Justification

### Goal
Build a comprehensive connectomics paper corpus via systematic expert-seeded search,
suitable for a RAG pipeline powering knowledge retrieval across the 11 NeuroTrailblazers
connectomics dimensions.

### Pipeline
1. **Expert seeds** (29 researchers at the start; the folders now cover 67) -> systematic web search (Semantic Scholar, PubMed, Google Scholar)
2. **Per-paper JSON files** in this directory — one file per paper, named `{expert_slug}/{paper_id}.json`
3. **Dedup** against `_data/journal_papers.yml` (102 papers when this collection started; the file now holds 2,000)
4. **Ingest** into knowledge store for RAG retrieval
5. **Enrich** with OCAR summaries, dimension tags, and discussion prompts

### Why Per-Paper JSON?
- Easier to manage incrementally (add/edit/remove individual papers)
- Avoids massive monolithic YAML files
- Simpler deduplication and merge tooling
- Each file is self-contained with all metadata

### Expert Selection Rationale
The 29 experts were selected to cover all 11 connectomics dimensions:
- **Core connectomics**: Sporns, Seung, Lichtman, Helmstaedter, Kasthuri
- **Drosophila connectomics**: Plaza, Rivlin, Scheffer, Cardona, Jefferis
- **Functional connectomics**: Reid, da Costa, Tolias, Briggman
- **Computational/ML**: Jain, Dorkenwald, Shavit, Kording, Boyden
- **Statistical**: Vogelstein, Priebe
- **Infrastructure/tools**: Gray Roncal, Collman, Denk
- **Molecular connectivity**: Zador
- **Specialized circuits**: Spirou, Smith, Harris
- Cross-checked against: bossDB PIs, BRAIN CONNECTS awardees, the 102-paper corpus that existed at the time

### Schema (per paper JSON)
```json
{
  "id": "sporns-2005-human-connectome",
  "title": "...",
  "authors": ["Sporns O", "Tononi G", "Kotter R"],
  "year": 2005,
  "journal": "...",
  "doi": "...",
  "url": "...",
  "abstract": "...",
  "seed_expert": "Olaf Sporns",
  "dimensions": ["connectomics"],
  "tags": ["graph-theory", "connectome"],
  "duplicate_of_existing": null,
  "notes": "Coined the term 'connectome'"
}
```

### Dimensions Key
1. connectomics
2. neuroanatomy
3. cell-types
4. computer-vision-ml
5. proofreading
6. data-infrastructure
7. image-acquisition
8. network-analysis
9. case-studies
10. methodology
11. ethics-society

### Accuracy note (September 2026)
Many author lists in these files were generated rather than copied, and some DOIs pointed
to unrelated papers. In September 2026, 69 files were corrected against Crossref: author
lists replaced with the publisher record, and DOIs, titles and years fixed where the title
matched a Crossref record. About 18 files still have no DOI or a DOI that could not be
matched to their title; treat those entries as unverified until someone checks them by hand.
