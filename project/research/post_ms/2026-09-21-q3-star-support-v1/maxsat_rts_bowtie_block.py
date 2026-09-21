#!/usr/bin/env python3
"""Exact parity/star-block maximum for the smallest saved RTS control."""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, "/workspace/scratch/a4369cb67676/deps")
from pysat.examples.rc2 import RC2
from pysat.formula import WCNF

from check_star_support import d2c, graph
from maxsat_fixed_codes import encode


def main():
    k, r, q = 3, 4, 2
    codes = ["C00", "C01", "C10", "C11", "C20", "C21"]
    codes += sum(([name] * k for name in ("S0", "S3", "S5", "S6")), [])
    codes += ["P0"] * r + ["P1"] * q
    x = 6
    offset = 18
    R = list(range(offset, offset + r))
    T = list(range(offset + r, offset + r + q))
    S = list(range(6, 18))
    r0, r1 = R[:2]
    t0, t1 = T
    cnf, avars, _ = encode(codes)

    def var(i, j):
        return avars[tuple(sorted((9 + i, 9 + j)))]

    for a, b in ((x, r0), (x, r1), (x, t0), (x, t1), (r0, t0)):
        cnf.append([var(a, b)])
    for a, b in ((r0, t1), (r1, t0)):
        cnf.append([-var(a, b)])
        for y in range(len(codes)):
            if y not in (a, b, x):
                cnf.append([-var(a, y), -var(b, y)])

    block = set(R + T + S)
    weighted = WCNF()
    for clause in cnf.clauses:
        weighted.append(clause)
    soft = []
    for (u, v), variable in avars.items():
        i, j = u - 9, v - 9
        if i in block and j in block:
            weighted.append([variable], weight=1)
            soft.append(variable)

    start = time.monotonic()
    with RC2(weighted, solver="cadical195") as rc2:
        model = rc2.compute()
        cost = rc2.cost
    elapsed = time.monotonic() - start
    positive = {v for v in model if v > 0}
    A_edges = [
        (u - 9, v - 9)
        for (u, v), variable in avars.items()
        if variable in positive
    ]
    adjacency = graph(codes, A_edges)
    assert d2c(adjacency)
    maximum = len(soft) - cost
    assert maximum == r * q + len(S) + 1 == 21
    out = {
        "scope": "six coordinates; three copies per even star class; r=4,q=2; forced RTS bow-tie",
        "status": "exact block maximum and actual counterexample to B<=rq+s",
        "maximum_parity_star_block_edges": maximum,
        "rq_plus_s": r * q + len(S),
        "excess": maximum - (r * q + len(S)),
        "seconds": elapsed,
        "codes": codes,
        "A_edges": A_edges,
        "n": len(adjacency),
        "m": sum(map(len, adjacency)) // 2,
        "direct_D2C_replay": True,
    }
    path = Path(__file__).with_name("RTS_BOWTIE_BLOCK_MAXSAT_RESULTS.json")
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(f"PASS: exact block max {maximum}=rq+s+1 in {elapsed:.3f}s")


if __name__ == "__main__":
    main()
