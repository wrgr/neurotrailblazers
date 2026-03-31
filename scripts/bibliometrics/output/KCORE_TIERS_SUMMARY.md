# K-Core Filtering: Three Tiers with Color Coding

## Tier Breakdown

| Tier | K-Core | Papers | Color | Use |
|------|--------|--------|-------|-----|
| Ultra-Core | ≥32 | 213 | 🔴 Red | Seminal papers |
| EM Connectomics | ≥25 | 1,064 | 🟠 Orange | **PRIMARY ANALYSIS** |
| Core + Bridge | ≥20 | 2,074 | 🟢 Green | Journal club reference |
| Peripheral | <20 | 5,851 | ⚫ Gray | Excluded |

## Visualization Strategy

- **Map k=32 papers to RED** (#D62728) in all visualizations
- **Map k=25–31 papers to ORANGE** (#FF7F0E) for the core analysis set
- **Map k=20–24 papers to GREEN** (#2CA02C) for optional journal club additions
- **Map k<20 papers to GRAY** (#7F7F7F) for reference/background

This makes the ultra-core visually distinct while maintaining color coherence.

## File Outputs

- `corpus_kcore_32.json` – 213 ultra-core papers (red tier)
- `corpus_kcore_25.json` – 1,064 EM connectomics core (orange tier) ⭐ USE THIS FOR MAIN ANALYSIS
- `corpus_kcore_20.json` – 2,074 core + bridge (green tier)
- `kcore_tiers_annotated.json` – Full mapping with tier labels and colors

## Next Steps

1. ✓ Generate statistics from `corpus_kcore_25.json`
2. ✓ Create field_map.html with color coding
3. ✓ Host k=25 graphs on unlisted page
4. ☐ Review k=20–24 papers for journal club additions
5. ☐ Document which k<25 papers were added and why
