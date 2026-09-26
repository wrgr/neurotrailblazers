import argparse
from collections import Counter
from fractions import Fraction
import hashlib
from itertools import combinations, permutations
import json
from pathlib import Path
import platform


NODES = ("A", "B", "C", "D")
CONTACTS = {("A", "B"): 3, ("B", "A"): 1, ("A", "C"): 2,
            ("C", "A"): 2, ("B", "C"): 1, ("C", "D"): 3}


def reciprocal_pairs(edges):
    return sum((source, target) in edges and (target, source) in edges
               for source, target in combinations(NODES, 2))


def analyze(threshold):
    if threshold not in (1, 2):
        raise ValueError("The teaching exercise supports thresholds 1 and 2 only.")
    observed = {edge for edge, contacts in CONTACTS.items() if contacts >= threshold}
    possible = tuple(permutations(NODES, 2))
    distribution = Counter(reciprocal_pairs(set(edges))
                           for edges in combinations(possible, len(observed)))
    total = sum(distribution.values())
    pairs = reciprocal_pairs(observed)
    expected = Fraction(sum(count * frequency for count, frequency in distribution.items()), total)
    tail = Fraction(sum(frequency for count, frequency in distribution.items() if count >= pairs), total)
    return {
        "dataset": "synthetic-four-neuron-graph-v1",
        "nodes": NODES,
        "threshold_greater_equal": threshold,
        "edges": sorted(observed),
        "edge_count": len(observed),
        "reciprocal_pairs": pairs,
        "reciprocated_edge_fraction": str(Fraction(2 * pairs, len(observed))),
        "null": "Uniform labeled directed simple graphs with fixed nodes and edge count; no self-loops.",
        "null_graphs": total,
        "null_distribution": dict(sorted(distribution.items())),
        "expected_pairs": str(expected),
        "enrichment_ratio": str(Fraction(pairs, 1) / expected),
        "exact_upper_tail": str(tail),
        "exact_upper_tail_decimal": float(tail),
        "python_version": platform.python_version(),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "limitation": "Toy fixed-edge null; does not preserve degree, distance or cell type.",
    }


def main():
    parser = argparse.ArgumentParser(description="Enumerate a tiny graph null exactly, offline.")
    parser.add_argument("--threshold", type=int, choices=(1, 2), required=True)
    args = parser.parse_args()
    print(json.dumps(analyze(args.threshold), indent=2))


if __name__ == "__main__":
    main()
