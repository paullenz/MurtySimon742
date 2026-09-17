#!/usr/bin/env python3
"""Deterministic checks for the independently reconstructed hypercube-face D2C family.

This is project evidence, not an identification certificate for the published
Figure 1. The k=3 member has the same published coarse invariants (n=12,
m=32, primitive, D2C, with a dominating edge).
"""

from itertools import combinations


def build(k):
    r = ("r",)
    A = [("a", i) for i in range(k)]
    B = [("b", x) for x in range(1 << k)]
    V = [r] + A + B
    E = set()

    def add(u, v):
        E.add(frozenset((u, v)))

    for x in range(1 << k):
        for i in range(k):
            y = x ^ (1 << i)
            if x < y:
                add(("b", x), ("b", y))
    for x in range(1 << k):
        add(r, ("b", x))
    for i in range(k):
        for x in range(1 << k):
            if ((x >> i) & 1) == 0:
                add(("a", i), ("b", x))
    return V, E, r, A, B


def adj(E, u, v):
    return frozenset((u, v)) in E


def neigh(V, E, u):
    return {v for v in V if v != u and adj(E, u, v)}


def within2(V, E, u, v):
    if u == v or adj(E, u, v):
        return True
    return bool(neigh(V, E, u) & neigh(V, E, v))


def is_d2c(V, E):
    if not all(within2(V, E, u, v) for u, v in combinations(V, 2)):
        return False
    for e in list(E):
        E2 = E - {e}
        if all(within2(V, E2, x, y) for x, y in combinations(V, 2)):
            return False
    return True


def is_primitive(V, E):
    sig = [frozenset(neigh(V, E, u)) for u in V]
    return len(sig) == len(set(sig))


def dominating_edges(V, E):
    out = []
    allv = set(V)
    for e in E:
        u, v = tuple(e)
        if {u, v} | neigh(V, E, u) | neigh(V, E, v) == allv:
            out.append(e)
    return out


def complement_edges(V, E):
    return {frozenset((u, v)) for u, v in combinations(V, 2) if not adj(E, u, v)}


def quasi_options(V, H, A, pair):
    u, w = tuple(pair)
    opts = []
    for source, exc in ((u, w), (w, u)):
        for a in A:
            if adj(H, source, a):
                if neigh(V, H, source) | neigh(V, H, a) == set(V) - {exc}:
                    opts.append((source, a, exc))
    return opts


def main():
    # Direct edge-deletion replay on several family members. The hand proof in
    # HYPERCUBE_FACE_EXCEPTION.md is the universal argument.
    for k in range(3, 7):
        V, E, r, A, B = build(k)
        n, m = len(V), len(E)
        assert n == (1 << k) + k + 1
        assert m == (k + 1) * (1 << k)
        assert is_d2c(V, E)
        assert frozenset((r, ("b", 0))) in dominating_edges(V, E)

        if k == 3:
            assert n == 12 and m == 32
            assert is_primitive(V, E)
            deg = {u: len(neigh(V, E, u)) for u in V}
            assert sorted(deg.values(), reverse=True) == [8, 7, 6, 6, 6, 5, 5, 5, 4, 4, 4, 4]
            assert deg[r] == 8 and [u for u, d in deg.items() if d == 8] == [r]
            assert len(dominating_edges(V, E)) == 1

            # Canonical root profile.
            F = {e for e in E if set(e) <= set(A)}
            GB = {e for e in E if set(e) <= set(B)}
            assert not F and len(GB) == 12
            delta = len(B) * (n - len(B)) - m
            assert delta == 0

            # Complement H and cross representatives.
            H = complement_edges(V, E)
            hcross = {
                e for e in H
                if len(set(e) & set(A)) == 1 and len(set(e) & set(B)) == 1
            }
            assert len(hcross) == 12
            selected = []
            for pair in GB:
                opts = quasi_options(V, H, A, pair)
                assert len(opts) == 1, (pair, opts)
                selected.append(opts[0])
            assert {frozenset((s, a)) for s, a, exc in selected} == hcross

            q = {u: 0 for u in B}
            p = {u: 0 for u in B}
            x = {a: 0 for a in A}
            for s, a, exc in selected:
                q[s] += 1
                p[exc] += 1
                x[a] += 1
            for u in B:
                bits = u[1]
                assert q[u] == bits.bit_count()
                assert p[u] == k - bits.bit_count()
                assert q[u] + p[u] == k
            assert set(x.values()) == {4}

    print("PASS_HYPERCUBE_FACE_FAMILY_K3_TO_K6")
    print("k=3: n=12 m=32 delta=0 F=empty residual=0 Q=12")


if __name__ == "__main__":
    main()
