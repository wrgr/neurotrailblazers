"""Profile one query two ways on synthetic tables (Module 12 kit).

The tables are generated in memory from a fixed seed, with the shape of the
Module 12 studio scenario: a synapse table scaled from 5 x 10^8 rows, a
120,000-row segment table, and cell types for 8,400 neurons. They are synthetic
teaching data, not a sample of any real dataset. Python 3, standard library only.

    python3 profile_join.py --fraction 0.001

The question: how many synapses connect each pair of cell types?
  1. join at query time: segment -> neuron -> cell type, looked up per synapse;
  2. pre-joined: the cell types were written onto each synapse row in advance.
Times are wall-clock for this laptop and in-memory Python. They show the method
(sample, check linear scaling, extrapolate, compare designs), not the cost of a
query against cloud object storage.
"""

import argparse
import hashlib
import json
import platform
import random
import time
from collections import Counter
from pathlib import Path

FULL_SYNAPSES = 500_000_000
SEGMENTS = 120_000
NEURONS = 8_400
TYPES = ["L23_pyr", "L4_exc", "L5_pyr", "L6_pyr", "basket", "martinotti", "vip", "other"]


def build(fraction, seed=1212):
    rng = random.Random(seed)
    neuron_type = {n: rng.choice(TYPES) for n in range(NEURONS)}
    # Most segments belong to a neuron; the rest are orphans with no cell type.
    segment_neuron = {s: (rng.randrange(NEURONS) if rng.random() < 0.7 else None) for s in range(SEGMENTS)}
    n = int(FULL_SYNAPSES * fraction)
    synapses = [(rng.randrange(SEGMENTS), rng.randrange(SEGMENTS)) for _ in range(n)]
    return neuron_type, segment_neuron, synapses


def join_at_query_time(neuron_type, segment_neuron, synapses):
    counts = Counter()
    for pre, post in synapses:
        a, b = segment_neuron[pre], segment_neuron[post]
        if a is None or b is None:
            continue
        counts[(neuron_type[a], neuron_type[b])] += 1
    return counts


def prejoin(neuron_type, segment_neuron, synapses):
    seg_type = {s: (neuron_type[n] if n is not None else None) for s, n in segment_neuron.items()}
    return [(seg_type[a], seg_type[b]) for a, b in synapses]


def query_prejoined(rows):
    counts = Counter()
    for a, b in rows:
        if a is not None and b is not None:
            counts[(a, b)] += 1
    return counts


def timed(fn, *args):
    t0 = time.perf_counter()
    out = fn(*args)
    return out, time.perf_counter() - t0


def main():
    ap = argparse.ArgumentParser(description="Time a join-at-query-time count against a pre-joined one.")
    ap.add_argument("--fraction", type=float, default=0.001, help="fraction of the 5e8-row table (default 0.001)")
    args = ap.parse_args()
    if not 0 < args.fraction <= 0.01:
        ap.error("use a fraction between 0 and 0.01; larger samples will not fit in memory comfortably")

    neuron_type, segment_neuron, synapses = build(args.fraction)
    joined, t_join = timed(join_at_query_time, neuron_type, segment_neuron, synapses)
    rows, t_build = timed(prejoin, neuron_type, segment_neuron, synapses)
    pre, t_pre = timed(query_prejoined, rows)
    assert joined == pre, "the two designs must give the same answer"
    scale = 1 / args.fraction
    print(json.dumps({
        "dataset": "synthetic-teaching-only",
        "fraction": args.fraction,
        "synapse_rows_sampled": len(synapses),
        "join_at_query_time_s": round(t_join, 3),
        "prejoined_query_s": round(t_pre, 3),
        "prejoin_build_once_s": round(t_build, 3),
        "extrapolated_full_join_at_query_time_s": round(t_join * scale, 1),
        "extrapolated_full_prejoined_query_s": round(t_pre * scale, 1),
        "speedup_per_query": round(t_join / t_pre, 2) if t_pre else None,
        "top_pairs": [[f"{a}->{b}", c] for (a, b), c in pre.most_common(3)],
        "assumption": "Time scales linearly with rows. Check it by halving --fraction.",
        "python_version": platform.python_version(),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "limitation": "In-memory Python on synthetic tables; says nothing about cloud I/O cost.",
    }, indent=2))


if __name__ == "__main__":
    main()
