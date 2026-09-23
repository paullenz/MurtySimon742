#!/usr/bin/env python3
"""Hostile aggregate check for the 16 fresh r=12 support-seven shards."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[4]
PACKAGE = ROOT / "project/research/general_n/2026-09-22-r12-quotient-v1"


def identity(row):
    return (int(row["case"]), int(row["mask"]), tuple(map(int, row["R"])))


def digest(identities):
    payload = json.dumps(sorted(identities), separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()


def main():
    paths = [HERE / ("R12_SUPPORT7_SOURCE_REPLAY_SHARD00.json" if i == 0 else
                     f"R12_SUPPORT7_SOURCE_REPLAY_SHARD{i}.json") for i in range(16)]
    shards = [json.loads(path.read_text()) for path in paths]
    assert [row["shard"] for row in shards] == list(range(16))
    assert all(row["shards"] == 16 for row in shards)
    assert shards[0]["range"][0] == 0
    assert shards[-1]["range"][1] == 2179
    assert all(a["range"][1] == b["range"][0] for a, b in zip(shards, shards[1:]))
    fresh = [identity(row) for shard in shards for row in shard["feasible_rows"]]
    saved_rows = json.loads((PACKAGE / "r12_support7_sources.json").read_text())["rows"]
    saved = [identity(row) for row in saved_rows]
    result = {
        "shards": 16,
        "strict_core_orbits": sum(row["strict_core_orbits"] for row in shards),
        "source_feasible": len(fresh),
        "solver_unknown": sum(row["solver_unknown"] for row in shards),
        "fresh_identity_sha256": digest(fresh),
        "saved_identity_sha256": digest(saved),
        "identity_match": sorted(fresh) == sorted(saved),
        "fresh_identities": fresh,
        "scope": "Aggregate of fresh shardable integer replay; exact physical-source necessary condition only, not graph realization.",
    }
    result["pass"] = (
        result["strict_core_orbits"] == 2179 and
        result["source_feasible"] == 2 and
        result["solver_unknown"] == 0 and result["identity_match"])
    assert result["pass"]
    output = HERE / "R12_SUPPORT7_SOURCE_REPLAY_AGGREGATE.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
