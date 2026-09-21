#!/usr/bin/env python3
"""Direct diagnostic for the natural simultaneous-parity five-centre blowup.

This tests one explicit adjacency pattern only: retain the unique one-copy
five-centre model, clone both parity codes, make P0--P1 complete, and keep a
single P1 hub adjacent to all six coordinate vertices.
"""
import json
from pathlib import Path

from check_star_support import d2c, graph


def build(r, q):
    coordinates = ["C00", "C01", "C10", "C11", "C20", "C21"]
    codes = coordinates + ["P0"] * r + ["P1"] * q
    star0 = len(codes)
    codes += ["S0", "S1", "S2", "S4", "S7"]
    p0 = range(6, 6 + r)
    p1 = range(6 + r, 6 + r + q)
    hub = 6 + r
    edges = [(a, b) for a in p0 for b in p1]
    edges += [(i, hub) for i in range(6)]
    edges += [(star0, star0 + 4), (star0 + 1, star0 + 3),
              (star0 + 2, star0 + 3)]
    adjacency = graph(codes, edges)
    return codes, edges, adjacency


def main():
    rows = []
    for r in range(1, 21):
        for q in range(1, 21):
            codes, edges, adjacency = build(r, q)
            n = len(adjacency)
            m = sum(map(len, adjacency)) // 2
            expected = r * q + 4 * (r + q) + 73
            M = (n - 1) ** 2 // 4 + 1
            assert n == 20 + r + q and m == expected and M > m
            rows.append({
                "r": r,
                "q": q,
                "n": n,
                "m": m,
                "M_n": M,
                "deficit_from_M": M - m,
                "direct_D2C_replay": d2c(adjacency),
            })
    out = {
        "scope": "single explicit complete P0--P1 blowup of the unique one-copy five-centre model",
        "rows": rows,
        "feasible": [row for row in rows if row["direct_D2C_replay"]],
        "status": "DIAGNOSTIC_ONLY",
    }
    Path(__file__).with_name("FIVE_CENTRE_PARITY_BLOWUP_PROBE_RESULTS.json").write_text(
        json.dumps(out, indent=2) + "\n"
    )
    print(f"feasible {len(out['feasible'])}/{len(rows)}")
    print(out["feasible"])


if __name__ == "__main__":
    main()
