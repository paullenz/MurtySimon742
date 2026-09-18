#!/usr/bin/env python3
"""Independent abstract audit for Hall cut/decomposition algebra.

This is NOT a D2C proof or graph enumeration.  It generates arbitrary finite
A-graphs partitioned into complementary-pair classes, chooses direct edges and
one source endpoint on every non-direct edge, and then manufactures L/Z and
R/p variables so that the exact local degree/direct-credit identities hold.
It checks the derived cut identities on every subset of pair classes.
"""

from __future__ import annotations

import argparse
import random


def one_trial(rng: random.Random):
    a = rng.randint(2, 14)
    p = rng.randint(1, a)
    T0 = a - p
    k = rng.randint(1, min(6, a))

    cuts = sorted(rng.sample(range(1, a), k - 1)) if k > 1 else []
    sizes = []
    prev = 0
    for c in cuts + [a]:
        sizes.append(c - prev)
        prev = c

    cls = []
    for i, s in enumerate(sizes):
        cls.extend([i] * s)

    edges = []
    for u in range(a):
        for v in range(u + 1, a):
            if rng.random() < 0.45:
                edges.append((u, v))

    direct = {
        e for e in edges
        if cls[e[0]] == cls[e[1]] and rng.random() < 0.35
    }
    source = {e: rng.choice(e) for e in edges if e not in direct}

    deg = [0] * a
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    degP = [0] * k
    for v in range(a):
        degP[cls[v]] += deg[v]

    L, Z, D, t, j, kappa, Rdiv = [], [], [], [], [], [], []
    for i in range(k):
        # Exact local degree identity requires L_i-Z_i=a_i*p-deg(A_i,A).
        diff = sizes[i] * p - degP[i]
        off = rng.randint(max(0, -diff), max(0, -diff) + 4)
        L.append(off + max(diff, 0))
        Z.append(off + max(-diff, 0))

        di = sum(1 for e in direct if cls[e[0]] == i)
        D.append(di)
        ti = sum(1 for e, s in source.items() if cls[s] == i)
        t.append(ti)

        ji = rng.randint(0, 4)
        j.append(ji)
        Rdiv.append(2 * di + ji)  # R_i/p
        kappa.append(rng.randint(0, 4))

    J = sum(j)
    wall = 2 * sum(t) + sum(L) - sum(Z) + sum(Rdiv)
    assert wall == a * p + J

    checked = 0
    for mask in range(1 << k):
        X = [i for i in range(k) if mask >> i & 1]
        x = sum(sizes[i] for i in X)

        eint = sum(1 for u, v in edges if cls[u] in X and cls[v] in X)
        N = sum(
            1 for e in edges
            if e not in direct and cls[e[0]] in X and cls[e[1]] in X
        )
        tX = sum(t[i] for i in X)
        EX = tX - N
        cut = sum(
            1 for u, v in edges
            if (cls[u] in X) ^ (cls[v] in X)
        )
        MX = x * (a - x) - cut
        LX = sum(L[i] for i in X)
        ZX = sum(Z[i] for i in X)
        JX = sum(j[i] for i in X)
        RdivX = sum(Rdiv[i] for i in X)
        wX = 2 * tX + LX - ZX + RdivX

        # Exact degree/cut identity.
        assert 2 * eint == x * (x - T0) - LX + ZX + MX

        # Exact Hall decomposition.
        sigma = wX - x * (x - T0)
        assert sigma == 2 * EX + MX + JX

        # Capacity lift with Ccap=2t+kappa.
        kapX = sum(kappa[i] for i in X)
        WX = wX + kapX
        assert WX - x * (x - T0) == sigma + kapX

        # Dual Hall sandwich.
        assert x * (x - T0) <= wX <= x * (a + p - x) + J

        # Complement conservation.
        xb = a - x
        wb = wall - wX
        sigb = wb - xb * (xb - T0)
        assert sigma + sigb == 2 * x * (a - x) + J

        checked += 1

    return k, checked


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--trials", type=int, default=50_000)
    ap.add_argument("--seed", type=int, default=74218)
    args = ap.parse_args()

    rng = random.Random(args.seed)
    pair_instances = 0
    subset_checks = 0
    for _ in range(args.trials):
        k, checked = one_trial(rng)
        pair_instances += k
        subset_checks += checked

    print(f"trials={args.trials}")
    print(f"pair_class_instances={pair_instances}")
    print(f"subset_checks={subset_checks}")
    print("failures=0")


if __name__ == "__main__":
    main()
