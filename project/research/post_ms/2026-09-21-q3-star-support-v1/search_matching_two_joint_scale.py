#!/usr/bin/env python3
"""Joint-scale hostile search for the proposed matching-one lemma."""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, "/workspace/scratch/a4369cb67676/deps")
from pysat.solvers import Solver

from check_star_support import d2c, graph
from maxsat_fixed_codes import encode


def run(k):
    base = ["C00", "C01", "C10", "C11", "C20", "C21"]
    base += sum(([s] * k for s in ("S0", "S3", "S5", "S6")), [])
    r = q = k
    codes = base + ["P0"] * r + ["P1"] * q
    offset = len(base)
    x = 6
    rs = [offset, offset + 1]
    ts = [offset + r, offset + r + 1]
    cnf, avars, _ = encode(codes)

    def var(i, j):
        return avars[tuple(sorted((9 + i, 9 + j)))]

    for y in rs + ts:
        cnf.append([var(x, y)])
    for r0, t0 in zip(rs, ts):
        cnf.append([-var(r0, t0)])
        for y in range(len(codes)):
            if y not in (r0, t0, x):
                cnf.append([-var(r0, y), -var(t0, y)])

    start = time.monotonic()
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as solver:
        sat = solver.solve()
        model = solver.get_model() if sat else None
    row = {"joint_multiplicity": k, "sat": sat, "seconds": time.monotonic() - start}
    if sat:
        positive = {v for v in model if v > 0}
        a_edges = [
            (u - 9, v - 9) for (u, v), variable in avars.items()
            if variable in positive
        ]
        adjacency = graph(codes, a_edges)
        assert d2c(adjacency)
        n = len(adjacency)
        m = sum(map(len, adjacency)) // 2
        row.update({
            "codes": codes,
            "A_edges": a_edges,
            "n": n,
            "m": m,
            "M_n": (n - 1) ** 2 // 4 + 1,
            "deficit_from_M": (n - 1) ** 2 // 4 + 1 - m,
            "forced_star_index": x,
            "forced_unique_pairs": list(zip(rs, ts)),
            "direct_D2C_replay": True,
        })
    return row


def main():
    rows = [run(k) for k in range(2, 7)]
    assert not rows[0]["sat"]
    assert all(row["sat"] for row in rows[1:])
    out = {
        "scope": "all six coordinate codes; four even star classes and both parity classes jointly scaled",
        "claim_status": "counterexample to proposed matching-one lemma",
        "rows": rows,
    }
    path = Path(__file__).with_name("PARITY_STAR_MATCHING_TWO_JOINT_SCALE_RESULTS.json")
    path.write_text(json.dumps(out, indent=2) + "\n")
    for row in rows:
        print(row["joint_multiplicity"], row["sat"], row.get("n"), row.get("m"))


if __name__ == "__main__":
    main()
