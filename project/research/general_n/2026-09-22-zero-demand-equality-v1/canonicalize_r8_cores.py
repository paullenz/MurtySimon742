#!/usr/bin/env python3
"""Exact colour-preserving isomorphism quotient of optimistic r=8 cores.

Vertices may only be permuted within equal residual-mass classes.  The output
therefore retains precisely the labelled information relevant to R.
"""
import itertools
import json


def parts(n, hi=None):
    if n == 0:
        yield ()
        return
    hi = min(n, hi or n)
    for x in range(hi, 0, -1):
        for tail in parts(n - x, x):
            yield (x,) + tail


def survivor(R, pairs, mask):
    k = len(R)
    deg = [0] * k
    neigh = [[] for _ in R]
    edges = []
    for q, (i, j) in enumerate(pairs):
        if mask >> q & 1:
            edges.append((i, j))
            deg[i] += 1
            deg[j] += 1
            neigh[i].append(j)
            neigh[j].append(i)
    P = [i for i in range(k) if deg[i] > R[i]]
    N = [i for i in range(k) if i not in P]
    if any((deg[i] - R[i]) ** 2 > sum(R[j] for j in neigh[i]) for i in P):
        return None
    eP = sum(i in P and j in P for i, j in edges)
    eN = sum(i in N and j in N for i, j in edges)
    slack = sum(1 for i in N if R[i] == 1 and deg[i] == 0)
    t = eP - eN - sum(R[i] for i in P) - slack
    if t <= 0:
        return None
    return edges, deg, P, N, t


def colour_permutations(R):
    groups = []
    for value in sorted(set(R), reverse=True):
        groups.append(tuple(i for i, x in enumerate(R) if x == value))
    for choices in itertools.product(*(itertools.permutations(g) for g in groups)):
        p = list(range(len(R)))
        for g, image in zip(groups, choices):
            for i, j in zip(g, image):
                p[i] = j
        yield tuple(p)


def canonical_mask(mask, pairs, pair_index, perms):
    best = None
    for p in perms:
        image = 0
        for q, (i, j) in enumerate(pairs):
            if mask >> q & 1:
                a, b = sorted((p[i], p[j]))
                image |= 1 << pair_index[(a, b)]
        if best is None or image < best:
            best = image
    return best


out = {}
for R in parts(8):
    k = len(R)
    pairs = list(itertools.combinations(range(k), 2))
    pair_index = {e: q for q, e in enumerate(pairs)}
    perms = list(colour_permutations(R))
    reps = {}
    labelled = 0
    if not all(x == 1 for x in R):
        for mask in range(1 << len(pairs)):
            data = survivor(R, pairs, mask)
            if data is None:
                continue
            labelled += 1
            cm = canonical_mask(mask, pairs, pair_index, perms)
            if cm not in reps:
                # Recompute all vertex-indexed data on the canonical mask.
                # The originating labelled representative may use a different
                # ordering inside an equal-R colour class.
                edges, deg, P, N, t = survivor(R, pairs, cm)
                reps[cm] = {
                    "mask": cm,
                    "edges": [list(e) for e in pairs if cm >> pair_index[e] & 1],
                    "degrees": deg,
                    "P": P,
                    "N": N,
                    "t_upper": t,
                    "selected_lower_bounds": [max(0, deg[i] - R[i]) for i in range(k)],
                }
    out[str(R)] = {
        "support": k,
        "colour_preserving_permutations": len(perms),
        "strict_survivors_labelled": labelled,
        "strict_survivor_orbits": len(reps),
        "orbit_representatives": list(reps.values()),
        "scope": "Exact quotient under permutations preserving residual masses R.",
    }

print(json.dumps(out, indent=2))
