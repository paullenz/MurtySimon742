#!/usr/bin/env python3
"""Exact graph model for the leading n19/Delta11 two-label profiles."""

import argparse
import json
from z3 import And, Bool, If, Implies, Not, Or, PbEq, PbLe, Solver, Sum, sat

N, DELTA, ROOT = 19, 11, 0
B = tuple(range(1, 12))
A = tuple(range(12, 19))
L0, L1 = 12, 13


def solve_profile(x1, h1, intersection):
    E = {(u, v): Bool(f"e_{u}_{v}")
         for u in range(N) for v in range(u + 1, N)}

    def edge(u, v):
        if u == v:
            return False
        return E[(u, v) if u < v else (v, u)]

    def unique_common(a, z, w):
        return And(Not(edge(a, z)), edge(a, w), edge(z, w),
                   *[Not(And(edge(a, q), edge(z, q)))
                     for q in range(N) if q not in (a, z, w)])

    q = Solver()
    q.set(timeout=300_000)
    for b in B:
        q.add(edge(ROOT, b))
    for a in A:
        q.add(Not(edge(ROOT, a)))
    deg = []
    for u in range(N):
        du = Sum([If(edge(u, z), 1, 0) for z in range(N) if z != u])
        deg.append(du)
        q.add(du <= DELTA)
    q.add(Sum([DELTA - du for du in deg]) <= 27)

    C0 = {1, 2}
    c1_size = DELTA - h1
    if intersection not in (0, 1) or intersection > c1_size:
        raise ValueError("only the incomparable intersection sizes 0 or 1 are supported")
    C1 = ({1} if intersection == 1 else set())
    C1.update(range(3, 3 + c1_size - intersection))
    for b in B:
        q.add(edge(L0, b) if b in C0 else Not(edge(L0, b)))
        q.add(edge(L1, b) if b in C1 else Not(edge(L1, b)))

    a1 = {t: Bool(f"a1_{t}") for t in B}
    for t in B:
        if t in C1:
            q.add(Not(a1[t]))
    q.add(PbEq([(a1[t], 1) for t in B], x1))

    def assigned(i, t):
        return (t not in C0) if i == L0 else a1[t]

    for i in (L0, L1):
        for t in B:
            ai = assigned(i, t)
            if ai is False:
                continue
            cb = [And(edge(i, u), edge(t, u)) for u in B if u != t]
            q.add(Implies(ai, PbEq([(z, 1) for z in cb], 1)))
            q.add(Implies(ai, Not(edge(i, t))))
            for z in range(N):
                if z not in B and z not in (i, t):
                    q.add(Implies(ai, Not(And(edge(i, z), edge(t, z)))))

    for u in B:
        for t in B:
            if u >= t:
                continue
            uses = []
            for i in (L0, L1):
                ai_t, ai_u = assigned(i, t), assigned(i, u)
                if ai_t is not False:
                    uses.append(And(ai_t, edge(i, u), edge(u, t)))
                if ai_u is not False:
                    uses.append(And(ai_u, edge(i, t), edge(u, t)))
            q.add(PbLe([(z, 1) for z in uses], 1))

    for u in range(N):
        for v in range(u + 1, N):
            q.add(Or(edge(u, v), *[And(edge(u, w), edge(w, v))
                                  for w in range(N) if w not in (u, v)]))
    for x in range(N):
        for y in range(x + 1, N):
            witnesses = [And(*[Not(And(edge(x, w), edge(y, w)))
                               for w in range(N) if w not in (x, y)])]
            for z in range(N):
                if z not in (x, y):
                    witnesses += [unique_common(x, z, y), unique_common(y, z, x)]
            q.add(Implies(edge(x, y), Or(*witnesses)))
    result = q.check()
    out = {"x": [9, x1], "h": [9, h1], "C0": sorted(C0),
           "C1": sorted(C1), "intersection": intersection,
           "status": str(result)}
    if result == sat:
        m = q.model()
        edges = [[u, v] for (u, v), z in E.items() if bool(m.eval(z))]
        out.update(edge_count=len(edges), deficit=N * DELTA - 2 * len(edges),
                   edge_list=edges)
    elif str(result) == "unknown":
        out["reason_unknown"] = q.reason_unknown()
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--x1", type=int, required=True)
    p.add_argument("--h1", type=int, required=True)
    p.add_argument("--intersection", type=int, required=True)
    a = p.parse_args()
    print(json.dumps(solve_profile(a.x1, a.h1, a.intersection),
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
