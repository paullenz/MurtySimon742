#!/usr/bin/env python3
"""Polynomial all-frontier screen from TOTAL_EXCESS_AGGREGATE_DP.md.

This is a state-level necessary-condition scan. It hash-verifies the canonical
compatible-routing survivor stream, removes the 16 already recorded N34
whole-state closures, and checks every admissible total excess layer using a
small integer DP over source degrees.

A state labelled AGGREGATE_EXCLUDED has no surviving E layer under the retained
necessary conditions. A surviving state is merely triage, not graph feasible.
"""
from collections import Counter, defaultdict
from pathlib import Path
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
CAT = HERE.parent / "2026-09-12-compatible-routing-catalogue-v1"
sys.path.insert(0, str(CAT))
from evidence_io import read_bytes  # noqa: E402

CLOSED_N34 = {227, 279, 588, 526, 382, 519, 230, 282, 385, 153, 122, 283, 154, 231, 77, 60}
INF = 10**9


def source_penalty(rho, q, *, a, b, E, z):
    """Penalty relative to p<=rho+D for one source-degree choice."""
    D = b - a - 1
    universal = rho + D
    pcap = min(universal, b - 1 - q)
    if q > 0:
        kstar = min(z, q, E)
        if q > kstar:
            extra = (E - kstar) // (q - kstar)
            pcap = min(pcap, rho + extra - 1)
    if pcap < 0:
        return None
    assert pcap <= universal
    return universal - pcap


def layer_dp(row, E):
    s = list(row["s"])
    rhos = list(row["rho"])
    a, b = row["a"], row["b"]
    S = sum(s)
    Q = S + E
    D = b - a - 1
    U = sum(rhos) + b * D
    z = sum(x == 0 for x in s)

    counts = Counter(rhos)
    classes = []
    for rho in sorted(counts):
        qmax = min(a - rho, sum(d <= rho for d in s))
        classes.append((rho, counts[rho], qmax))

    # dp[j] = minimum incoming-capacity penalty after processed sources.
    dp = [INF] * (Q + 1)
    dp[0] = 0
    processed = 0
    for rho, cnt, qmax in classes:
        choices = []
        for q in range(qmax + 1):
            pen = source_penalty(rho, q, a=a, b=b, E=E, z=z)
            if pen is not None:
                choices.append((q, pen))
        if not choices:
            return None

        for _ in range(cnt):
            ndp = [INF] * (Q + 1)
            for used, val in enumerate(dp):
                if val >= INF:
                    continue
                for q, pen in choices:
                    nu = used + q
                    if nu <= Q and val + pen < ndp[nu]:
                        ndp[nu] = val + pen
            dp = ndp
            processed += 1

        # Every label with base demand > rho must place all of its base
        # incidences on unprocessed higher-rho sources.
        forced_later = sum(d for d in s if d > rho)
        prefix_max = Q - forced_later
        if prefix_max < Q:
            for used in range(max(0, prefix_max + 1), Q + 1):
                dp[used] = INF

    rmin = dp[Q]
    slack = U - Q
    return {
        "E": E,
        "Q": Q,
        "U": U,
        "slack": slack,
        "rmin": None if rmin >= INF else rmin,
        "survives": rmin < INF and rmin <= slack,
    }


def scan_state(row):
    s, rhos = list(row["s"]), list(row["rho"])
    a, b = row["a"], row["b"]
    S = sum(s)
    D = b - a - 1
    U = sum(rhos) + b * D
    qmax_total = sum(min(a - rho, sum(d <= rho for d in s)) for rho in rhos)
    Qmax = min(qmax_total, U, b * (b - 1) // 2)

    layers = []
    if Qmax >= S:
        for E in range(Qmax - S + 1):
            rec = layer_dp(row, E)
            if rec is not None:
                layers.append(rec)

    live = [r for r in layers if r["survives"]]
    return {
        "layer": row["layer"],
        "state_id": row["state_id"],
        "a": a,
        "b": b,
        "S": S,
        "R": sum(rhos),
        "D": D,
        "U": U,
        "Qmax": Qmax,
        "Emax": max(-1, Qmax - S),
        "status": "SURVIVES_AGGREGATE" if live else "AGGREGATE_EXCLUDED",
        "surviving_E": [r["E"] for r in live],
        "min_surviving_E": min((r["E"] for r in live), default=None),
        "layer_records": layers,
    }


def main():
    raw = read_bytes("survivors.json")
    rows = json.loads(raw)
    combined = [r for r in rows if r["combined_survives"]]
    assert len(combined) == 4584
    active = [
        r for r in combined
        if not (r["layer"] == "n34-m289" and r["state_id"] in CLOSED_N34)
    ]
    assert len(active) == 4568
    active.sort(key=lambda r: (r["layer"], r["state_id"]))

    results = [scan_state(r) for r in active]
    excluded = [r for r in results if r["status"] == "AGGREGATE_EXCLUDED"]
    survived = [r for r in results if r["status"] == "SURVIVES_AGGREGATE"]

    layer_counts = Counter()
    surviving_layer_counts = Counter()
    first_E = Counter()
    for r in results:
        layer_counts[r["layer"]] += 1
        if r["status"] == "SURVIVES_AGGREGATE":
            surviving_layer_counts[r["layer"]] += 1
            first_E[r["min_surviving_E"]] += 1

    narrow = sorted(
        survived,
        key=lambda r: (len(r["surviving_E"]), r["Emax"], r["layer"], r["state_id"]),
    )[:100]

    summary = {
        "schema": "total-excess-aggregate-dp-scan-v1",
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "canonical_input_states": len(active),
        "input_layers": dict(sorted(layer_counts.items())),
        "aggregate_excluded": len(excluded),
        "survives_aggregate": len(survived),
        "aggregate_excluded_by_layer": dict(sorted(Counter(r["layer"] for r in excluded).items())),
        "surviving_by_layer": dict(sorted(surviving_layer_counts.items())),
        "first_surviving_E_histogram": {str(k): v for k, v in sorted(first_E.items())},
        "aggregate_excluded_keys": [
            {"layer": r["layer"], "state_id": r["state_id"]} for r in excluded
        ],
        "narrowest_survivors": [
            {
                "layer": r["layer"],
                "state_id": r["state_id"],
                "S": r["S"],
                "Emax": r["Emax"],
                "surviving_E_count": len(r["surviving_E"]),
                "surviving_E": r["surviving_E"],
            }
            for r in narrow
        ],
        "proof_scope": (
            "AGGREGATE_EXCLUDED means every admissible total-excess layer fails "
            "the integer source-capacity DP in TOTAL_EXCESS_AGGREGATE_DP.md. "
            "This is a candidate whole-scalar-state exclusion under the retained "
            "canonical bridge lemmas; external review remains open."
        ),
        "survival_scope": (
            "SURVIVES_AGGREGATE is only triage. It does not assert a q-profile, "
            "selected incidence system, orientation, or graph exists."
        ),
        "external_review": "OPEN",
    }

    (HERE / "TOTAL_EXCESS_AGGREGATE_DP_SCAN.json").write_text(
        json.dumps(summary, indent=2) + "\n"
    )
    # Full per-layer records are useful for exact replay but kept separate.
    (HERE / "TOTAL_EXCESS_AGGREGATE_DP_FULL.json").write_text(
        json.dumps(results, indent=2) + "\n"
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
