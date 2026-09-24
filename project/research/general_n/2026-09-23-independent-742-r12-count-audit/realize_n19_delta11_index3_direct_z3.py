#!/usr/bin/env python3
"""Independent direct-deletion Z3 model for n19/Delta11 stable index 3."""

import json
from z3 import And, Bool, If, Implies, Not, Or, PbEq, PbLe, Solver, Sum, sat

N, DELTA, ROOT = 19, 11, 0
B = tuple(range(1, 12))
A = tuple(range(12, 19))
L0, L1 = 12, 13
E = {(u, v): Bool(f"f_{u}_{v}") for u in range(N) for v in range(u + 1, N)}


def ek(u, v):
    return (u, v) if u < v else (v, u)


def e(u, v):
    return False if u == v else E[ek(u, v)]


def deleted(u, v, x, y):
    return False if ek(u, v) == (x, y) else e(u, v)


def build():
    q = Solver()
    q.set(timeout=1_200_000)

    for b in B:
        q.add(e(ROOT, b))
    for a in A:
        q.add(Not(e(ROOT, a)))
    deg = []
    for u in range(N):
        du = Sum([If(e(u, w), 1, 0) for w in range(N) if w != u])
        deg.append(du)
        q.add(du <= DELTA)
    q.add(Sum([DELTA - du for du in deg]) <= 27)

    # The disjoint C-set normalization is proved separately.
    C0, C1 = {1, 2}, {3}
    for b in B:
        q.add(e(L0, b) if b in C0 else Not(e(L0, b)))
        q.add(e(L1, b) if b in C1 else Not(e(L1, b)))

    a1 = {t: Bool(f"b1_{t}") for t in B}
    q.add(Not(a1[3]))
    q.add(PbEq([(a1[t], 1) for t in B], 8))

    def assigned(i, t):
        if i == L0:
            return t not in C0
        return a1[t]

    for i in (L0, L1):
        for t in B:
            a_it = assigned(i, t)
            if a_it is False:
                continue
            common_b = [And(e(i, u), e(t, u)) for u in B if u != t]
            q.add(Implies(a_it, PbEq([(z, 1) for z in common_b], 1)))
            q.add(Implies(a_it, Not(e(i, t))))
            for z in range(N):
                if z not in B and z not in (i, t):
                    q.add(Implies(a_it, Not(And(e(i, z), e(t, z)))))

    for u in B:
        for t in B:
            if u >= t:
                continue
            used = []
            for i in (L0, L1):
                a_it, a_iu = assigned(i, t), assigned(i, u)
                if a_it is not False:
                    used.append(And(a_it, e(i, u), e(u, t)))
                if a_iu is not False:
                    used.append(And(a_iu, e(i, t), e(u, t)))
            q.add(PbLe([(z, 1) for z in used], 1))

    for u in range(N):
        for v in range(u + 1, N):
            q.add(Or(e(u, v), *[And(e(u, w), e(w, v))
                                for w in range(N) if w not in (u, v)]))

    # Literal definition: after deleting a present edge xy, at least one pair
    # has neither an edge nor any two-step path. This deliberately avoids the
    # unique-common-neighbour characterization used by the first model.
    for x in range(N):
        for y in range(x + 1, N):
            far_pairs = []
            for u in range(N):
                for v in range(u + 1, N):
                    no_two_path = [Not(And(deleted(u, w, x, y),
                                           deleted(w, v, x, y)))
                                   for w in range(N) if w not in (u, v)]
                    far_pairs.append(And(Not(deleted(u, v, x, y)),
                                         *no_two_path))
            q.add(Implies(e(x, y), Or(*far_pairs)))
    return q


def main():
    q = build()
    result = q.check()
    out = {"profile": "n19-Delta11-stable-index-3-direct-deletion",
           "status": str(result)}
    if result == sat:
        m = q.model()
        edges = [[u, v] for (u, v), z in E.items() if bool(m.eval(z))]
        out["edge_list"] = edges
        out["edge_count"] = len(edges)
    elif str(result) == "unknown":
        out["reason_unknown"] = q.reason_unknown()
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
