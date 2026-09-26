import argparse
import hashlib
import json
import platform
from pathlib import Path


SNAPSHOTS = {
    "snapshot-a": [
        {"id": "s1", "post": 101, "region": "core", "score": 0.95},
        {"id": "s2", "post": 101, "region": "core", "score": 0.80},
        {"id": "s3", "post": 101, "region": "core", "score": 0.60},
        {"id": "s4", "post": 101, "region": "outside", "score": 0.99},
        {"id": "s5", "post": 102, "region": "core", "score": 0.90},
    ],
    "snapshot-b": [
        {"id": "s1", "post": 101, "region": "core", "score": 0.95},
        {"id": "s2", "post": 101, "region": "core", "score": 0.80},
        {"id": "s3", "post": 101, "region": "core", "score": 0.90},
        {"id": "s4", "post": 101, "region": "outside", "score": 0.99},
        {"id": "s5", "post": 102, "region": "core", "score": 0.90},
        {"id": "s6", "post": 101, "region": "core", "score": 0.85},
    ],
}


def query(version):
    rows = SNAPSHOTS[version]
    selected = sorted(
        row["id"] for row in rows
        if row["post"] == 101 and row["region"] == "core" and row["score"] >= 0.80
    )
    return {
        "dataset": "synthetic-teaching-only",
        "snapshot": version,
        "filters": {"post": 101, "region": "core", "score_greater_equal": 0.80},
        "matching_ids": selected,
        "count": len(selected),
        "input_rows": len(rows),
        "excluded_rows": len(rows) - len(selected),
        "python_version": platform.python_version(),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "limitation": "Synthetic labels and scores; not a biological measurement or CAVE query.",
    }


def main():
    parser = argparse.ArgumentParser(description="Query invented, versioned teaching data offline.")
    parser.add_argument("--version", required=True, choices=sorted(SNAPSHOTS))
    args = parser.parse_args()
    print(json.dumps(query(args.version), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
