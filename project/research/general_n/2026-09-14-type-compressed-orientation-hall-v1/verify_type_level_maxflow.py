#!/usr/bin/env python3
"""Exact finite audit for TYPE_LEVEL_MAXFLOW_COROLLARY.md."""
from collections import defaultdict, Counter, deque
from itertools import product
from pathlib import Path
import json
import random

HERE = Path(__file__).resolve().parent
OUT = HERE / "TYPE_LEVEL_MAXFLOW_VERIFICATION.json"

SMALL_TYPES = (
    (0, 0, 0),
    (0, 1, 1),
    (1, 1, 0),
    (1, 2, 1),
    (2, 2, 1),
    (2, 3, 2),
)


class Dinic:
    def __init__(self, n):
        self.g = [[] for _ in range(n)]

    def add(self, u, v, cap):
        a = [v, cap, None]
        b = [u, 0, a]
        a[2] = b
        self.g[u].append(a)
        self.g[v].append(b)

    def flow(self, s, t):
        total = 0
        n = len(self.g)
        while True:
            level = [-1] * n
            level[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                for e in self.g[u]:
                    if e[1] and level[e[0]] < 0:
                        level[e[0]] = level[u] + 1
                        q.append(e[0])
            if level[t] < 0:
                return total
            it = [0] * n

            def dfs(u, f):
                if u == t:
                    return f
                while it[u] < len(self.g[u]):
                    e = self.g[u][it[u]]
                    if e[1] and level[e[0]] == level[u] + 1:
                        z = dfs(e[0], min(f, e[1]))
                        if z:
                            e[1] -= z
                            e[2][1] += z
                            return z
                    it[u] += 1
                return 0

            while True:
                z = dfs(s, 10**9)
                if not z:
                    break
                total += z


def compatible(a, b):
    qa, ca, _ = a
    qb, cb, _ = b
    return qa <= cb + 1 and qb <= ca


def labelled_flow(profile):
    n = len(profile)
    s, left, right, t = 0, 1, 1 + n, 1 + 2 * n
    f = Dinic(t + 1)
    for u, (q, _, _) in enumerate(profile):
        f.add(s, left + u, q)
    for u in range(n):
        for w in range(n):
            if u != w and compatible(profile[u], profile[w]):
                f.add(left + u, right + w, 1)
    for w, (_, _, p) in enumerate(profile):
        f.add(right + w, t, p)
    return f.flow(s, t)


def grouped(profile):
    ct = Counter(profile)
    types = tuple(sorted(ct))
    counts = tuple(ct[t] for t in types)
    return types, counts


def quotient_flow(profile):
    types, counts = grouped(profile)
    k = len(types)
    s, left, right, t = 0, 1, 1 + k, 1 + 2 * k
    f = Dinic(t + 1)
    for i, (typ, n) in enumerate(zip(types, counts)):
        q, _, _ = typ
        f.add(s, left + i, n * q)
    for i, (a, na) in enumerate(zip(types, counts)):
        for j, (b, nb) in enumerate(zip(types, counts)):
            if not compatible(a, b):
                continue
            cap = na * (na - 1) if i == j else na * nb
            if cap:
                f.add(left + i, right + j, cap)
    for j, (typ, n) in enumerate(zip(types, counts)):
        p = typ[2]
        f.add(right + j, t, n * p)
    return f.flow(s, t)


def margin_formula(types, counts, mask):
    demand = 0
    capacity = 0
    for i, (typ, n) in enumerate(zip(types, counts)):
        if mask >> i & 1:
            demand += n * typ[0]
    for j, (sigma, ns) in enumerate(zip(types, counts)):
        incoming_per_target = 0
        for i, (tau, nt) in enumerate(zip(types, counts)):
            if not (mask >> i & 1) or not compatible(tau, sigma):
                continue
            incoming_per_target += (nt - 1) if i == j else nt
        capacity += ns * min(sigma[2], incoming_per_target)
    return capacity - demand


def margin_direct_whole_type(profile, types, counts, mask):
    chosen_types = {types[i] for i in range(len(types)) if mask >> i & 1}
    chosen = [u for u, typ in enumerate(profile) if typ in chosen_types]
    demand = sum(profile[u][0] for u in chosen)
    capacity = 0
    for w in range(len(profile)):
        incoming = sum(
            u != w and compatible(profile[u], profile[w])
            for u in chosen
        )
        capacity += min(profile[w][2], incoming)
    return capacity - demand


def all_margins(profile):
    types, counts = grouped(profile)
    vals = []
    for mask in range(1 << len(types)):
        a = margin_formula(types, counts, mask)
        b = margin_direct_whole_type(profile, types, counts, mask)
        if a != b:
            raise AssertionError(("margin formula mismatch", profile, mask, a, b))
        vals.append(a)
    return types, counts, vals


def check_submodularity(vals, k):
    checks = 0
    for s in range(1 << k):
        for t in range(1 << k):
            if vals[s & t] + vals[s | t] > vals[s] + vals[t]:
                raise AssertionError(("submodularity failure", s, t, vals[s & t], vals[s | t], vals[s], vals[t]))
            checks += 1
    return checks


def verify_profile(profile, check_all_pairs=True):
    q_total = sum(x[0] for x in profile)
    lf = labelled_flow(profile)
    qf = quotient_flow(profile)
    if lf != qf:
        raise AssertionError(("flow mismatch", profile, lf, qf))
    types, counts, vals = all_margins(profile)
    min_margin = min(vals)
    predicted = q_total + min_margin
    if predicted != lf:
        raise AssertionError(("min-cut value mismatch", profile, q_total, min_margin, predicted, lf))
    if (lf == q_total) != (min_margin >= 0):
        raise AssertionError(("feasibility/margin mismatch", profile, lf, q_total, min_margin))
    subchecks = check_submodularity(vals, len(types)) if check_all_pairs else 0
    return len(vals), subchecks, lf == q_total


def exhaustive_suite():
    stats = Counter()
    # Orders through four keep the all-pairs submodularity audit comfortably small
    # while still exhausting repeated and mixed-type patterns.
    for n in range(1, 5):
        for profile in product(SMALL_TYPES, repeat=n):
            margins, subchecks, feasible = verify_profile(profile, check_all_pairs=True)
            stats["profiles"] += 1
            stats["type_set_margins"] += margins
            stats["submodular_pairs"] += subchecks
            stats["feasible_profiles"] += int(feasible)
    return stats


def random_suite(seed=7420914, profiles=5000):
    rng = random.Random(seed)
    stats = Counter()
    for _ in range(profiles):
        n = rng.randint(1, 9)
        palette = []
        for _ in range(rng.randint(1, min(6, n))):
            q = rng.randint(0, n - 1)
            rho = rng.randint(0, 5)
            c = q + rho
            p = rng.randint(0, n - 1)
            palette.append((q, c, p))
        profile = tuple(rng.choice(palette) for _ in range(n))
        margins, subchecks, feasible = verify_profile(profile, check_all_pairs=True)
        stats["profiles"] += 1
        stats["type_set_margins"] += margins
        stats["submodular_pairs"] += subchecks
        stats["feasible_profiles"] += int(feasible)
    stats["seed"] = seed
    return stats


def main():
    exhaustive = exhaustive_suite()
    random_stats = random_suite()
    result = {
        "schema": "type-level-maxflow-verification-v1",
        "status": "PASS",
        "exhaustive_small_type_universe": {
            "orders": [1, 2, 3, 4],
            "types": [list(t) for t in SMALL_TYPES],
            **dict(exhaustive),
        },
        "deterministic_broad_random": dict(random_stats),
        "claims_checked": [
            "labelled maximum flow equals quotient-type maximum flow",
            "maximum flow equals Q plus the minimum complete-type Hall margin",
            "quotient feasibility is equivalent to nonnegative minimum type-set margin",
            "closed submodular margin formula equals direct labelled complete-type cut",
            "Hall margin is submodular on the type set",
        ],
        "arithmetic": "exact integers only",
        "external_review": "OPEN",
        "note": "Finite audit supports but does not replace the hand proof.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
