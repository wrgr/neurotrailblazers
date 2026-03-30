"""
Configuration for the connectomics bibliometric analysis pipeline.

All seed queries, thresholds, and API settings live here.
Change these and re-run — the pipeline reuses cached API responses.
"""
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR.parent.parent
SEED_PAPERS_DIR = REPO_ROOT / "_data" / "expert_seed_papers"
JOURNAL_PAPERS_YML = REPO_ROOT / "_data" / "journal_papers.yml"
CACHE_DIR = BASE_DIR / "cache"
OUTPUT_DIR = BASE_DIR / "output"

# ── OpenAlex API ───────────────────────────────────────────────────────
OPENALEX_BASE = "https://api.openalex.org"
OPENALEX_EMAIL = "neurotrailblazers@example.com"  # polite pool (10 req/sec)
REQUESTS_PER_SECOND = 9  # stay under 10/sec

# ── Corpus A: Auto-Seed Queries ───────────────────────────────────────
# These build the seed set from OpenAlex with zero human paper curation.
# Each tuple: (search_type, query_or_filter, top_n)
#   search_type: "title" = title.search, "concept" = concepts.id filter,
#                "fulltext" = default.search
AUTO_SEED_QUERIES = [
    ("concept", "C2776102887", 20),          # connectomics concept
    ("title", "connectome", 20),
    ("title", "serial block-face OR FIB-SEM neuron", 10),
    ("title", "synapse detection electron microscopy", 10),
    ("title", "nanoscale neural circuit", 10),
]

# ── Extra manual DOIs (inject specific papers if needed) ──────────────
EXTRA_SEED_DOIS = [
    # Add DOIs here to force-include papers in the seed set
    # e.g. "10.1371/journal.pcbi.0010042"
]

# ── Corpus B: Keyword Search Queries ──────────────────────────────────
KEYWORD_QUERIES = [
    '"connectome" OR "connectomics"',
    '"serial section electron microscopy" neuron',
    '"synapse detection" "electron microscopy"',
    '"flood filling network" OR "neuronal segmentation"',
    '"FlyWire" OR "hemibrain" OR "MICrONS" OR "H01"',
    '"volume electron microscopy" reconstruction',
    '"neural circuit" "dense reconstruction"',
]
KEYWORD_MIN_CITATIONS = 5
KEYWORD_MIN_YEAR = 1985
KEYWORD_MAX_RESULTS_PER_QUERY = 200

# ── Corpus C: Dataset Anchor DOIs ─────────────────────────────────────
# Landmark dataset papers — we fetch all papers that cite these
DATASET_ANCHOR_DOIS = [
    "10.1038/s41586-024-07558-y",   # FlyWire whole-brain
    "10.7554/eLife.57443",           # Hemibrain v1.2
    "10.1101/2023.03.29.534851",    # MICrONS
    "10.1126/science.adk4858",      # H01 human cortex
    "10.1038/nature12346",          # Kasthuri 2015 cortical EM
    "10.1038/nature10011",          # Bock 2011 retina
    "10.1038/nn.2868",              # Briggman 2011 retinal direction selectivity
    "10.1101/2023.06.05.543757",    # FAFB-FlyWire
    "10.1038/s41586-021-03284-x",   # Winding 2023 Drosophila larva
    "10.1016/j.cell.2019.05.026",   # WormAtlas / Cook 2019
]
DATASET_MAX_CITERS = 500  # cap per dataset paper

# ── Expansion Settings ─────────────────────────────────────────────────
EXPANSION_MIN_SEED_CONNECTIONS = 2   # keep if cited by/citing 2+ seeds
EXPANSION_MAX_CITED_BY = 200         # cap forward citations per paper
EXPANSION_MARGINAL_GAIN_THRESHOLD = 0.05  # stop 2nd hop if <5% new papers
MAX_CORPUS_SIZE = 5000               # safety cap

# ── Graph Construction ─────────────────────────────────────────────────
MIN_COCITATION_WEIGHT = 2    # minimum co-citation count for edge
MIN_COUPLING_WEIGHT = 2     # minimum shared references for edge

# ── Adaptive Depth ─────────────────────────────────────────────────────
# If a dimension has fewer than this many papers after 1-hop, expand to 2-hop
DIMENSION_MIN_PAPERS = 20
