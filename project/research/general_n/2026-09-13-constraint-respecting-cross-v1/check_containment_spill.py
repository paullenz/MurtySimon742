#!/usr/bin/env python3
"""Standard-library checks for the receiver-containment spill inequality."""
from pathlib import Path
from random import Random
import json

HERE = Path(__file__).resolve().parent
PARENT_INPUTS = HERE.parent / "2026-09-12-arc-realisation-pilot-v1" / "pilot_inputs.json"


def random_selected(rec, rng):
    a, b, s, rho = rec["a"], rec["b"], rec["s"], rec["rho"]
    S = [set() for _ in range(b)]
    for i in sorted(range(a), key=lambda i: (-s[i], i)):
        need = s[i]
        eligible = [
            u
            for u in range(b)
            if rho[u] >= s[i] and len(S[u]) < a - rho[u]
        ]
        assert len(eligible) >= need
        scored = [
            (len(S[u]) + 2.5 * rng.random() - 0.05 * rho[u], u)
            for u in eligible
        ]
        for _, u in sorted(scored)[:need]:
            S[u].add(i)
    return S


def spill_source(rec, S, u):
    a, b, s, rho = rec["a"], rec["b"], rec["s"], rec["rho"]
    q = [len(z) for z in S]
    n = [q[v] + rho[v] for v in range(b)]
    Q = sum(q)
    nu = n[u]
    h = a - nu

    candidates = [
        v
        for v in range(b)
        if v != u
        and n[v] >= q[u] - 1
        and q[v] <= nu
        and rho[v] + b - a - 1 >= 1
    ]
    if len(candidates) < q[u]:
        return False, {
            "reason": "candidate_count",
            "candidate_count": len(candidates),
            "q": q[u],
        }

    g = {v: min(q[v], h) for v in range(b) if v != u}
    leave_contained = sorted(g[v] for v in candidates)[: q[u]]
    G = sum(g.values()) - sum(leave_contained)

    S_total = sum(s)
    S_top = sum(sorted(s, reverse=True)[:nu])
    eligibility = [sum(rho[v] >= s[i] for v in range(b)) for i in range(a)]
    E_top = sum(sorted(eligibility, reverse=True)[:nu])
    lam = max(0, S_total - S_top, Q - E_top)

    return lam <= G, {
        "reason": "spill",
        "lambda": lam,
        "G": G,
        "n_u": nu,
        "candidate_count": len(candidates),
        "q": q[u],
    }


def check_strictness_example():
    # A labels 0..4. Source 0 selects 0..3 and has residual label 4.
    # The other six B rows are the six pairs on labels 0..3.
    S = [{0, 1, 2, 3}] + [set() for _ in range(6)]
    pairs = [{0, 1}, {0, 2}, {0, 3}, {1, 2}, {1, 3}, {2, 3}]
    R = [{4}] + pairs
    N = [S[v] | R[v] for v in range(7)]
    D = [sum(i in N[v] for v in range(7)) for i in range(5)]
    assert D[:4] == [4, 4, 4, 4]
    assert all(D[i] >= 4 for i in S[0])
    pair_moment = sum(len(N[v]) * (len(N[v]) - 1) // 2 for v in range(7))
    required = 6 * 3
    assert pair_moment == 16 < required == 18
    return {
        "selected_label_degrees": D[:4],
        "endpoint_load_required": 4,
        "actual_pair_moment": pair_moment,
        "trace_pair_moment_required": required,
    }


def main():
    records = json.loads(PARENT_INPUTS.read_text())["sample"]
    sampled = []
    for idx, rec in enumerate(records):
        rng = Random(20000 + idx)
        patterns = 2000
        bad_patterns = 0
        source_violations = 0
        for _ in range(patterns):
            S = random_selected(rec, rng)
            violations = 0
            for u in range(rec["b"]):
                if S[u] and not spill_source(rec, S, u)[0]:
                    violations += 1
            if violations:
                bad_patterns += 1
                source_violations += violations
        sampled.append(
            {
                "record_index": idx,
                "layer": rec["layer"],
                "state_id": rec["state_id"],
                "seed": 20000 + idx,
                "patterns": patterns,
                "violating_patterns": bad_patterns,
                "source_violations": source_violations,
            }
        )

    assert [x["violating_patterns"] for x in sampled] == [0, 0, 173, 0, 0, 0]
    assert [x["source_violations"] for x in sampled] == [0, 0, 183, 0, 0, 0]

    out = {
        "status": "PASS",
        "strictness_example": check_strictness_example(),
        "sampled_spill_test": sampled,
        "scope": (
            "The strictness example is exact abstract cross data. The 2,000-pattern-per-state "
            "test is deterministic reconnaissance, not exhaustive state coverage."
        ),
    }
    (HERE / "CONTAINMENT_SPILL_CHECK.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
