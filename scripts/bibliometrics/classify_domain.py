#!/usr/bin/env python3
"""
Multi-signal domain classification for citation graph nodes.

Replaces brittle title-keyword matching with a layered approach:
  1. Journal name  (available on 97% of graph nodes)
  2. OpenAlex concepts  (available on enriched papers only)
  3. Title keywords  (fallback only)

Classification categories:
  em_connectomics  — nanoscale / synaptic-resolution connectomics (EM, barcoding, ExM)
  mri_connectomics — macro-connectomics (dMRI, fMRI, structural MRI)
  network_science  — graph theory, complex networks, statistical mechanics
  neuroscience     — general neuroscience (not connectomics-specific)
  methods_ml       — computer vision, ML, image processing
  off_topic        — geophysics, cancer statistics, pharmacology, etc.
  unknown          — insufficient signal

Usage:
    from classify_domain import classify_node, classify_graph_nodes
    label = classify_node(node_dict)
    labeled = classify_graph_nodes(nodes_list)
"""

# ── Journal → domain mapping ─────────────────────────────────────────
# Built from empirical analysis of 7,925-node corpus journal distribution.
# Journals not listed here fall through to concept/keyword layers.

JOURNAL_DOMAIN = {
    # ── EM connectomics (strong signal) ──
    "eLife": "em_connectomics",
    "Frontiers in Neural Circuits": "em_connectomics",
    "Frontiers in Neuroanatomy": "em_connectomics",
    "The Journal of Comparative Neurology": "em_connectomics",
    "Journal of Microscopy": "em_connectomics",
    "Frontiers in Neuroinformatics": "em_connectomics",
    "Neuroinformatics": "em_connectomics",
    "Network Neuroscience": "em_connectomics",  # launched by Sporns, mostly connectomics
    "Frontiers in Cellular Neuroscience": "em_connectomics",

    # ── MRI connectomics ──
    "NeuroImage": "mri_connectomics",
    "Human Brain Mapping": "mri_connectomics",
    "Cerebral Cortex": "mri_connectomics",
    "Brain Connectivity": "mri_connectomics",
    "Brain": "mri_connectomics",

    # ── General neuroscience (ambiguous — could be either scale) ──
    "Journal of Neuroscience": "neuroscience",
    "Neuron": "neuroscience",
    "Nature Neuroscience": "neuroscience",
    "Current Biology": "neuroscience",
    "Current Opinion in Neurobiology": "neuroscience",
    "Nature reviews. Neuroscience": "neuroscience",
    "Annual Review of Neuroscience": "neuroscience",
    "Trends in Neurosciences": "neuroscience",
    "Trends in Cognitive Sciences": "neuroscience",
    "Neuroscience & Biobehavioral Reviews": "neuroscience",
    "Frontiers in Neuroscience": "neuroscience",
    "Journal of Neuroscience Methods": "neuroscience",
    "Cell": "neuroscience",  # ambiguous, but in this corpus mostly neuro
    "Cell Reports": "neuroscience",

    # ── Methods / ML ──
    "Nature Methods": "methods_ml",
    "IEEE Transactions on Medical Imaging": "methods_ml",
    "Medical Image Analysis": "methods_ml",
    "Lecture notes in computer science": "methods_ml",  # MICCAI, ECCV, etc.
    "Bioinformatics": "methods_ml",
    "Nature Protocols": "methods_ml",
    "Nucleic Acids Research": "methods_ml",

    # ── Network science ──
    "Physical Review Letters": "network_science",
    "Physical Review E": "network_science",
    "SIAM Review": "network_science",

    # ── Off-topic journals (noise from broad citation chains) ──
    "Geophysical Journal International": "off_topic",
    "Journal of Geophysical Research Solid Earth": "off_topic",
    "Journal of Geophysical Research Atmospheres": "off_topic",
    "Geophysical Research Letters": "off_topic",
    "Reviews of Modern Physics": "off_topic",
    "Analytical Chemistry": "off_topic",
    "The Lancet": "off_topic",
    "New England Journal of Medicine": "off_topic",
    "International Journal of Molecular Sciences": "off_topic",
    "Autophagy": "off_topic",
    "Genes & Development": "off_topic",
    "Cells": "off_topic",
    "Frontiers in Cell and Developmental Biology": "off_topic",

    # ── Neuroscience (additional) ──
    "Biological Psychiatry": "neuroscience",
    "Neuropsychopharmacology": "neuroscience",
    "Frontiers in Human Neuroscience": "neuroscience",
    "Philosophical Transactions of the Royal Society B Biological Sciences": "neuroscience",
    "The Journal of Cell Biology": "neuroscience",
    "Magnetic Resonance in Medicine": "mri_connectomics",

    # ── Methods / ML (additional) ──
    "BMC Bioinformatics": "methods_ml",
    "Scientific Data": "methods_ml",
    "IEEE Transactions on Automatic Control": "off_topic",  # control theory noise
    "European Heart Journal": "off_topic",
    "Advanced Materials": "off_topic",
    "Earth and Planetary Science Letters": "off_topic",
    "Journal of Cell Science": "off_topic",

    # ── More neuroscience ──
    "Frontiers in Systems Neuroscience": "neuroscience",
    "Nature Biotechnology": "methods_ml",

    # ── Broad journals (need second signal) ──
    # Nature, Science, PNAS, Nature Communications, PLoS ONE, Scientific Reports,
    # bioRxiv, arXiv — these publish everything, so journal alone is ambiguous.
}

# Journals that are ambiguous and need a second signal
AMBIGUOUS_JOURNALS = {
    "Nature", "Science", "Nature Communications",
    "Proceedings of the National Academy of Sciences",
    "PLoS ONE", "PLoS Biology", "PLoS Computational Biology",
    "Scientific Reports", "Science Advances",
    "bioRxiv (Cold Spring Harbor Laboratory)", "arXiv (Cornell University)",
    "Communications Biology", "iScience",
}

# ── Concept-based classification ─────────────────────────────────────
# OpenAlex concept names that strongly indicate domain.
# Used when journal is ambiguous or missing.

EM_CONCEPTS = {
    "connectome", "connectomics", "synapse", "electron microscopy",
    "drosophila melanogaster", "caenorhabditis elegans", "neuropil",
    "serial section", "neurite", "axon", "dendrite",
}
MRI_CONCEPTS = {
    "neuroimaging", "functional magnetic resonance imaging", "fmri",
    "diffusion mri", "resting state", "tractography", "brain mapping",
    "voxel", "white matter", "structural connectivity",
}
NETSCI_CONCEPTS = {
    "complex network", "scale-free network", "small-world network",
    "graph theory", "network topology", "modularity",
    "random graph", "power law", "centrality",
}

# ── Title keyword fallback ───────────────────────────────────────────
# Only used when both journal and concepts are insufficient.

EM_TITLE_KW = {
    "connectom", "synapse", "synaptic", "electron microscopy", "neural circuit",
    "neuron reconstruction", "axon", "dendrite", "neuropil",
    "fib-sem", "serial section", "segmentation", "proofreading",
    "catmaid", "flywire", "hemibrain", "drosophila", "c. elegans",
    "microns", "bossdb", "expansion microscopy", "volume em",
    "dense reconstruction", "nanoscale", "wiring", "retina",
    "optic lobe", "mushroom body", "direction selectiv",
    "neuroanatom", "reconstruct", "fluorescen", "brainbow",
    "stochastic labeling", "cell type", "interneuron",
    "mapseq", "barseq", "barcod",
}
MRI_TITLE_KW = {
    "fmri", "diffusion mri", "tractography", "resting state",
    "functional connectivity", "brain mapping", "parcellation",
    "structural mri", "cortical thickness", "voxel",
}
NETSCI_TITLE_KW = {
    "scale-free", "small-world", "complex network", "power law",
    "random graph", "network topology", "community detection",
    "modularity", "centrality", "graph theory",
}


def _concept_names(node):
    """Extract lowered concept names from a node dict."""
    concepts = node.get("concepts", [])
    if isinstance(concepts, list):
        return {c.get("name", "").lower() for c in concepts if isinstance(c, dict)}
    return set()


def _title_kw_score(title_lower, keyword_set):
    """Count how many keywords appear in the title."""
    return sum(1 for kw in keyword_set if kw in title_lower)


def classify_node(node):
    """
    Classify a single graph node into a domain category.

    Args:
        node: dict with keys like title, journal, concepts (optional), type

    Returns:
        str: one of em_connectomics, mri_connectomics, network_science,
             neuroscience, methods_ml, off_topic, unknown
    """
    journal = (node.get("journal") or "").strip()
    title = (node.get("title") or "").lower()

    # Layer 1: Journal lookup (strong signal)
    if journal in JOURNAL_DOMAIN:
        return JOURNAL_DOMAIN[journal]

    # For ambiguous journals, fall through to layers 2-3
    needs_second_signal = journal in AMBIGUOUS_JOURNALS or not journal

    if needs_second_signal:
        # Layer 2: OpenAlex concepts (if available)
        cnames = _concept_names(node)
        if cnames:
            em_score = len(cnames & EM_CONCEPTS)
            mri_score = len(cnames & MRI_CONCEPTS)
            ns_score = len(cnames & NETSCI_CONCEPTS)
            best = max(em_score, mri_score, ns_score)
            if best >= 2:
                if em_score == best:
                    return "em_connectomics"
                if mri_score == best:
                    return "mri_connectomics"
                if ns_score == best:
                    return "network_science"
            if best == 1:
                # Single concept match — use as tiebreaker with title
                pass  # fall through to title

        # Layer 3: Title keywords (fallback)
        em_t = _title_kw_score(title, EM_TITLE_KW)
        mri_t = _title_kw_score(title, MRI_TITLE_KW)
        ns_t = _title_kw_score(title, NETSCI_TITLE_KW)

        # Combine concept score (layer 2) with title score (layer 3)
        cnames = _concept_names(node)
        em_total = em_t + len(cnames & EM_CONCEPTS)
        mri_total = mri_t + len(cnames & MRI_CONCEPTS)
        ns_total = ns_t + len(cnames & NETSCI_CONCEPTS)
        best_total = max(em_total, mri_total, ns_total)

        if best_total >= 1:
            if em_total == best_total:
                return "em_connectomics"
            if mri_total == best_total:
                return "mri_connectomics"
            if ns_total == best_total:
                return "network_science"

        # Generic neuroscience title patterns
        neuro_kw = {"brain", "cortex", "neuron", "neural", "cortical", "hippocampal"}
        if any(kw in title for kw in neuro_kw):
            return "neuroscience"

        return "unknown"

    # Journal present but not in any mapping — classify by title
    em_t = _title_kw_score(title, EM_TITLE_KW)
    mri_t = _title_kw_score(title, MRI_TITLE_KW)
    ns_t = _title_kw_score(title, NETSCI_TITLE_KW)
    best = max(em_t, mri_t, ns_t)
    if best >= 1:
        if em_t == best:
            return "em_connectomics"
        if mri_t == best:
            return "mri_connectomics"
        if ns_t == best:
            return "network_science"

    return "unknown"


def classify_graph_nodes(nodes):
    """
    Classify all nodes and return a dict: openalex_id -> domain.

    Args:
        nodes: list of node dicts (from citation_graph.json)

    Returns:
        dict mapping node id to domain string
    """
    return {n["id"]: classify_node(n) for n in nodes}


def enrich_and_classify(papers, graph_nodes):
    """
    Classify papers using graph node metadata as fallback.
    Useful when reading_list.json has empty journal but graph has it.

    Args:
        papers: list of paper dicts (e.g. from reading_list.json)
        graph_nodes: list of graph node dicts (from citation_graph.json)

    Returns:
        dict mapping openalex_id to domain string
    """
    graph_lookup = {n["id"]: n for n in graph_nodes}
    result = {}
    for p in papers:
        pid = p.get("openalex_id") or p.get("id", "")
        # Merge: prefer paper fields, fall back to graph node
        merged = dict(graph_lookup.get(pid, {}))
        merged.update({k: v for k, v in p.items() if v})  # non-empty values win
        result[pid] = classify_node(merged)
    return result


def domain_summary(nodes):
    """Print classification distribution."""
    from collections import Counter
    labels = [classify_node(n) for n in nodes]
    counts = Counter(labels)
    total = len(nodes)
    print(f"\nDomain classification ({total} nodes):")
    for domain, count in counts.most_common():
        print(f"  {domain:20s}  {count:5d}  ({100*count/total:.1f}%)")
    return counts


if __name__ == "__main__":
    import json
    from config import OUTPUT_DIR
    with open(OUTPUT_DIR / "graphs" / "citation_graph.json") as f:
        g = json.load(f)
    domain_summary(g["nodes"])
