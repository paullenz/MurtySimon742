#!/usr/bin/env python3
"""Uniform certificate for the repeated-S7 five-centre family."""
import json
from pathlib import Path

from check_star_support import CODES, d2c, graph
from check_five_centre_two_parameter_family import labels, lost_pairs


def build(k):
    codes = ["C00", "C01", "C10", "C11", "C20", "C21", "P1",
             "S0", "S1", "S2", "S4"] + ["S7"] * k
    edges = [(i, 6) for i in range(6)]
    edges += [(8, 9), (8, 10), (7, 11)]
    for w in range(12, 11 + k):
        edges += [(w, 8), (w, 11)]
    return codes, edges, graph(codes, edges)


def main():
    codes, _, seed = build(1)
    names = labels(codes)
    hazard = set(CODES["S7"]) | {9 + 8, 9 + 11}
    seed_certs = []
    for x in range(len(seed)):
        for y in sorted(seed[x]):
            if x >= y:
                continue
            safe = [p for p in lost_pairs(seed, (x, y)) if not (set(p) <= hazard)]
            assert safe
            a, b = safe[0]
            seed_certs.append({"edge": [names[x], names[y]],
                               "future_twin_safe_witness": [names[a], names[b]]})
    assert len(seed_certs) == 77

    codes2, _, first = build(2)
    names2 = labels(codes2)
    new_vertex = len(first) - 1
    new_certs = []
    for y in sorted(first[new_vertex]):
        safe = [p for p in lost_pairs(first, (new_vertex, y)) if not (set(p) <= hazard)]
        assert safe
        a, b = safe[0]
        new_certs.append({"edge": [names2[new_vertex], names2[y]],
                          "future_twin_safe_witness": [names2[a], names2[b]]})

    rows = []
    for k in range(1, 51):
        _, _, G = build(k)
        n, m = len(G), sum(map(len, G)) // 2
        assert n == 20 + k and m == 6 * n - 49 and d2c(G)
        rows.append({"k": k, "n": n, "m": m, "direct_D2C_replay": True})
    out = {
        "formula": {"n": "20+k", "m": "6n-49"},
        "seed_safe_certificates": seed_certs,
        "first_new_twin_safe_certificates": new_certs,
        "direct_replay_rows": rows,
        "status": "PASS",
    }
    Path(__file__).with_name("FIVE_CENTRE_S7_TWIN_FAMILY_RESULTS.json").write_text(
        json.dumps(out, indent=2) + "\n"
    )
    print("PASS: uniform S7-twin certificate; 50 direct family replays")


if __name__ == "__main__":
    main()
