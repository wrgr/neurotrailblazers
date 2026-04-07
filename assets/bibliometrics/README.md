# Bibliometrics Assets (Generated)

`assets/bibliometrics` is the canonical data bundle consumed by the
neurotrailblazers website.

Source of truth:
- Graph construction, scoring, and JSON export are owned by `connectome-kb`.
- This repo only syncs and visualizes the exported artifacts.

Sync workflow:
```bash
# from neurotrailblazers/
bash scripts/sync_from_kb.sh
```

Default upstream path:
- `../connectome-kb/outputs/website`

Expected files:
- `graphs/citation_graph.json`
- `graphs/cocitation_graph.json`
- `graphs/coupling_graph.json`
- `graphs/coauthorship_graph.json`
- `paper_rankings.json`
- `author_rankings.json`
- `communities.json`
- `lineage_data.json`
- `corpus_canonical.json`
- `strategic_audit.json` and `strategic_audit.md` (when present)
- `manifest.json` (when present)
