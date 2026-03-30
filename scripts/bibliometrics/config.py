"""
Configuration for the connectomics bibliometric analysis pipeline.

All seed queries, thresholds, and API settings live here.
Change these and re-run — the pipeline reuses cached API responses.

Scope: Nanoscale / synaptic-resolution connectomics (EM, barcoding, ExM, X-ray).
Excludes macro-connectomics (dMRI/fMRI) unless bridging to nanoscale.
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
# Build the seed set from OpenAlex with zero human paper curation.
# Each tuple: (search_type, query_or_filter, top_n)
#   search_type: "title" = title.search, "concept" = concepts.id filter,
#                "fulltext" = default.search
#
# NOTE: OpenAlex is deprecating Concepts in favor of Topics.
# If concept queries fail, the pipeline falls back to title/keyword.

AUTO_SEED_QUERIES = [
    # Core connectomics (field-defining)
    ("concept", "C2776102887", 20),                                    # connectomics concept (verify at runtime)
    ("title", 'connectome synapse OR nanoscale OR reconstruction', 20),
    ("title", "connectomics", 20),

    # Volume EM (dominant technique family)
    ("title", "serial block-face OR SBF-SEM OR SBEM", 10),
    ("title", "FIB-SEM OR focused ion beam brain", 10),
    ("title", "serial section TEM OR electron microscopy neuron", 10),
    ("title", "volume electron microscopy reconstruction", 10),
    ("title", "multi-beam SEM OR multibeam brain", 5),
    ("title", "ATUM OR GridTape OR automated tape-collecting", 5),

    # Non-EM nanoscale techniques
    ("title", "MAPseq OR BARseq OR barcoding connectivity brain", 10),
    ("title", "expansion microscopy synapse OR connectom", 5),
    ("title", "X-ray nanotomography OR nano-CT OR micro-CT neuron", 5),
    ("title", "array tomography synapse OR neuron", 5),

    # Segmentation & reconstruction
    ("title", "synapse detection OR neuron segmentation", 10),
    ("title", "flood-filling network OR dense reconstruction neural", 10),

    # Graph theory / network analysis (bridges both scales)
    ("title", "connectome graph theory OR network analysis", 10),
]

# ── Extra manual DOIs (inject specific papers if needed) ──────────────
EXTRA_SEED_DOIS = [
    # Add DOIs here to force-include papers in the seed set
    # e.g. "10.1371/journal.pcbi.0010042"
]

# ── Macro-Connectomics Exclusion Filter ───────────────────────────────
# Papers matching these terms are removed UNLESS they also match keep terms.
MACRO_EXCLUSION_TERMS = [
    "diffusion mri", "dmri", "fmri", "resting state", "resting-state",
    "tractography", "bold", "functional connectivity",
    "diffusion tensor", "diffusion weighted",
]
NANOSCALE_KEEP_TERMS = [
    "electron microscopy", "synapse", "nanoscale", "connectome",
    "graph theory", "network analysis", "segmentation",
    "barcod", "mapseq", "barseq",  # partial match for barcoding
]

# ── Corpus B: Keyword Search Queries ──────────────────────────────────
KEYWORD_QUERIES = [
    # Core field terms
    '"connectome" OR "connectomics"',
    '"neural circuit" "dense reconstruction"',
    '"connectome" "graph theory" OR "network analysis"',

    # Volume EM
    '"serial section electron microscopy" neuron',
    '"volume electron microscopy" reconstruction',
    '"serial block-face SEM" OR "FIB-SEM" brain',
    '"multi-beam SEM" OR "multibeam SEM" neuron',
    '"ATUM" OR "GridTape" electron microscopy',

    # Non-EM nanoscale
    '"MAPseq" OR "BARseq" connectivity',
    '"expansion microscopy" synapse',
    '"array tomography" synapse OR neuron',
    '"X-ray nanotomography" OR "nano-CT" neuron',

    # Segmentation & tools
    '"synapse detection" "electron microscopy"',
    '"flood filling network" OR "neuronal segmentation"',

    # Dataset names
    '"FlyWire" OR "hemibrain" OR "MICrONS" OR "H01"',
]
KEYWORD_MIN_CITATIONS = 5
KEYWORD_MIN_YEAR = 1985
KEYWORD_MAX_RESULTS_PER_QUERY = 200

# ── Corpus C: Dataset Anchor DOIs ─────────────────────────────────────
# Landmark dataset papers + key tool/infrastructure papers.
# We fetch all papers that cite these.
DATASET_ANCHOR_DOIS = [
    # ── Connectome datasets ──
    "10.1038/s41586-024-07558-y",   # FlyWire whole-brain (Dorkenwald 2024)
    "10.7554/eLife.57443",           # Hemibrain v1.2 (Scheffer 2020)
    "10.1016/j.cell.2018.06.019",   # FAFB (Zheng 2018)
    "10.1126/science.add9330",      # Larval Drosophila (Winding 2023)
    "10.1101/2023.03.29.534851",    # MICrONS
    "10.1126/science.adk4858",      # H01 human cortex
    "10.1038/nature12346",          # Kasthuri 2015 cortical EM
    "10.1038/nature10011",          # Bock 2011 retina
    "10.1038/nn.2868",              # Briggman 2011 retinal direction selectivity
    "10.1038/s41586-021-03778-8",   # C. elegans developmental (Witvliet 2021)
    "10.1016/j.cell.2019.05.026",   # Cook C. elegans 2019
    "10.1101/2024.04.16.589741",    # Optic lobe (Nern 2024)

    # ── Tools & infrastructure ──
    "10.1093/bioinformatics/btp266",  # CATMAID (Saalfeld 2009)
    "10.1038/nmeth.4331",             # webKnossos (Boergens 2017)
    "10.1038/s41592-024-02426-z",     # CAVE (2024)
    "10.1101/2020.01.16.909465",      # neuPrint (Clements 2020)
    "10.3389/fninf.2022.828787",      # BossDB (Hider 2022)
    "10.1038/s41592-018-0049-4",      # Flood-filling networks (Januszewski 2018)
]
DATASET_MAX_CITERS = 500  # cap per anchor paper

# ── Technique Families (for coverage checking) ────────────────────────
# Used by 04_validate.py to verify all technique families are represented.
# Values are title/abstract keywords to grep for.
TECHNIQUE_FAMILIES = {
    "volume_em": [
        "electron microscopy", "SEM", "TEM", "FIB-SEM", "SBEM",
        "serial block-face", "serial section", "multibeam", "multi-beam",
    ],
    "atum_gridtape": ["ATUM", "GridTape", "automated tape"],
    "barcoding": ["MAPseq", "BARseq", "BRICseq", "barcod"],
    "expansion_microscopy": ["expansion microscopy", "ExM"],
    "xray": ["X-ray", "nanotomography", "nano-CT", "micro-CT", "synchrotron"],
    "array_tomography": ["array tomography"],
    "graph_theory": ["graph theory", "network analysis", "network neuroscience"],
}

# ── Expansion Settings ─────────────────────────────────────────────────
EXPANSION_MIN_SEED_CONNECTIONS = 2   # keep if cited by/citing 2+ seeds
EXPANSION_MAX_CITED_BY = 200         # cap forward citations per paper
EXPANSION_MARGINAL_GAIN_THRESHOLD = 0.05  # stop 2nd hop if <5% new papers
MAX_CORPUS_SIZE = 5000               # safety cap

# ── Graph Construction ─────────────────────────────────────────────────
MIN_COCITATION_WEIGHT = 2    # minimum co-citation count for edge
MIN_COUPLING_WEIGHT = 2     # minimum shared references for edge

# ── Adaptive Depth ─────────────────────────────────────────────────────
# If a technique family has fewer than this many papers after 1-hop, expand
TECHNIQUE_MIN_PAPERS = 5
