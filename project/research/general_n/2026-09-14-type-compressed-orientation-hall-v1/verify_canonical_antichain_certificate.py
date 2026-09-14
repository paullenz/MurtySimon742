#!/usr/bin/env python3
"""Independent finite audit for CANONICAL_ANTICHAIN_CERTIFICATE.md.

This verifier is self-contained.  It enumerates complete-type Hall margins,
constructs the sharp dominance poset, and independently builds the
closure-augmented quotient max-flow network.
"""
from collections import Counter, deque
from itertools import combinations_with_replacement
from pathlib import Path
import json
import random

SEED = 7420914
OUT = Path(__file__).resolve().parent / "CANONICAL_ANTICHAIN_CERTIFICATE_VERIFICATION.json"


def compatible(a, b):
    qa, ca, _ = a
    qb, cb, _ = b
    return qa <= cb + 1 and qb <= ca


def dominates(x, y):
    """Sharp hardness x >=_* y on distinct type triples."""
    qx, cx, px = x
    qy, cy, py = y
    return cx <= cy and (qx > qy or (qx == qy and px >= py))


def grouped(profile):
    ct = Counter(profile)
    types = tuple(sorted(ct))
    counts = tuple(ct[t] for t in types)
    return types, counts


def margin(types, counts, mask):
    demand = sum(
        counts[i] * types[i][0]
        for i in range(len(types))
        if (mask >> i) & 1
    )
    capacity = 0
    for j, (sigma, ns) in enumerate(zip(types, counts)):
        incoming = 0
        for i, (tau, nt) in enumerate(zip(types, counts)):
            if not ((mask >> i) & 1) or not compatible(tau, sigma):
                continue
            incoming += nt - 1 if i == j else nt
        capacity += ns * min(sigma[2], incoming)
    return capacity - demand


def is_upset(types, mask):
    k = len(types)
    for y in range(k):
        if not ((mask >> y) & 1):
            continue
        for x in range(k):
            if x != y and dominates(types[x], types[y]) and not ((mask >> x) & 1):
                return False
    return True


def generators(types, mask):
    """Minimal (least-hard) elements of a sharp-hardness up-set."""
    out = []
    for i in range(len(types)):
        if not ((mask >> i) & 1):
            continue
        # i is not minimal if it dominates a distinct selected easier element.
        if any(
            j != i and ((mask >> j) & 1) and dominates(types[i], types[j])
            for j in range(len(types))
        ):
            continue
        out.append(i)
    return out


def upclosure(types, gens):
    mask = 0
    for x in range(len(types)):
        if any(x == g or dominates(types[x], types[g]) for g in gens):
            mask |= 1 << x
    return mask


class Dinic:
    def __init__(self, n):
        self.g = [[] for _ in range(n)]

    def add(self, u, v, cap):
        a = [v, cap, None]
        b = [u, 0, a]
        a[2] = b
        b[2] = a
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
                    if e[1] > 0 and level[e[0]] < 0:
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
                    if e[1] > 0 and level[e[0]] == level[u] + 1:
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

    def can_reach_sink(self, t):
        """Vertices with a directed residual path to t."""
        rev = [[] for _ in self.g]
        for u, edges in enumerate(self.g):
            for e in edges:
                if e[1] > 0:
                    rev[e[0]].append(u)
        seen = [False] * len(self.g)
        seen[t] = True
        q = deque([t])
        while q:
            v = q.popleft()
            for u in rev[v]:
                if not seen[u]:
                    seen[u] = True
                    q.append(u)
        return seen


def closure_quotient(profile):
    types, counts = grouped(profile)
    k = len(types)
    Q = sum(n * typ[0] for typ, n in zip(types, counts))
    s, left, right, t = 0, 1, 1 + k, 1 + 2 * k
    F = Dinic(t + 1)

    for i, (typ, n) in enumerate(zip(types, counts)):
        F.add(s, left + i, n * typ[0])
    for i, (tau, nt) in enumerate(zip(types, counts)):
        for j, (sigma, ns) in enumerate(zip(types, counts)):
            if not compatible(tau, sigma):
                continue
            cap = nt * (nt - 1) if i == j else nt * ns
            if cap:
                F.add(left + i, right + j, cap)
    for j, (typ, n) in enumerate(zip(types, counts)):
        F.add(right + j, t, n * typ[2])

    # Capacity Q+1 makes violating a closure relation strictly more expensive
    # than every ordinary s-t cut, whose capacity is at most Q.
    for x in range(k):
        for y in range(k):
            if x != y and dominates(types[x], types[y]):
                F.add(left + y, left + x, Q + 1)

    value = F.flow(s, t)
    can_t = F.can_reach_sink(t)
    max_source_side = [not x for x in can_t]
    if not max_source_side[s] or max_source_side[t]:
        raise AssertionError(("bad maximal residual cut", profile, value))
    mask = 0
    for i in range(k):
        if max_source_side[left + i]:
            mask |= 1 << i
    return types, counts, Q, value, mask


def audit_profile(profile, stats):
    types, counts = grouped(profile)
    k = len(types)
    vals = [margin(types, counts, m) for m in range(1 << k)]
    stats["type_set_margins"] += len(vals)
    minimum = min(vals)
    minimizers = [m for m, v in enumerate(vals) if v == minimum]

    mplus = 0
    mall = (1 << k) - 1
    mminus = mall
    for m in minimizers:
        mplus |= m
        mminus &= m

    if vals[mplus] != minimum or vals[mminus] != minimum:
        raise AssertionError(("extremal minimizer failure", profile, minimum, mminus, mplus))
    stats["lattice_extremal_checks"] += 2

    # Direct closure under union/intersection, independently of the proof.
    for a in minimizers:
        for b in minimizers:
            if vals[a | b] != minimum or vals[a & b] != minimum:
                raise AssertionError(("minimizer lattice failure", profile, a, b))
            stats["minimizer_lattice_pair_checks"] += 1

    max_card = max(m.bit_count() for m in minimizers)
    max_card_minimizers = [m for m in minimizers if m.bit_count() == max_card]
    if max_card_minimizers != [mplus]:
        raise AssertionError(("Mplus not unique maximum-cardinality minimizer", profile, max_card_minimizers, mplus))
    stats["unique_maximum_minimizer_checks"] += 1

    if not is_upset(types, mplus):
        raise AssertionError(("Mplus not sharp upset", profile, mplus, minimum))
    stats["sharp_upset_checks"] += 1

    gens = generators(types, mplus)
    if upclosure(types, gens) != mplus:
        raise AssertionError(("generator reconstruction failure", profile, gens, mplus))
    stats["generator_reconstruction_checks"] += 1

    for i, g in enumerate(gens):
        for h in gens[i + 1:]:
            if dominates(types[g], types[h]) or dominates(types[h], types[g]):
                raise AssertionError(("generator antichain failure", profile, g, h))
            stats["generator_antichain_pair_checks"] += 1

            qg, cg, pg = types[g]
            qh, ch, ph = types[h]
            # Sort this pair by q, then c, only for the claimed staircase tests.
            if qg < qh:
                if not cg < ch:
                    raise AssertionError(("different-demand staircase failure", profile, types[g], types[h]))
                stats["different_demand_staircase_checks"] += 1
            elif qh < qg:
                if not ch < cg:
                    raise AssertionError(("different-demand staircase failure", profile, types[h], types[g]))
                stats["different_demand_staircase_checks"] += 1
            else:
                if cg < ch:
                    if not pg < ph:
                        raise AssertionError(("equal-demand staircase failure", profile, types[g], types[h]))
                    stats["equal_demand_staircase_checks"] += 1
                elif ch < cg:
                    if not ph < pg:
                        raise AssertionError(("equal-demand staircase failure", profile, types[h], types[g]))
                    stats["equal_demand_staircase_checks"] += 1

    qt, qc, Q, flow_value, flow_mplus = closure_quotient(profile)
    if qt != types or qc != counts:
        raise AssertionError("grouping disagreement")
    if flow_value != Q + minimum:
        raise AssertionError(("closure quotient mincut value failure", profile, flow_value, Q, minimum))
    if flow_mplus != mplus:
        raise AssertionError(("residual maximal mincut projection failure", profile, flow_mplus, mplus))
    stats["closure_flow_value_checks"] += 1
    stats["residual_maximal_cut_checks"] += 1

    stats["profiles"] += 1
    if minimum < 0:
        stats["negative_profiles"] += 1
        stats["negative_generator_histogram"][len(gens)] += 1
        stats["max_negative_generators"] = max(stats["max_negative_generators"], len(gens))
    stats["max_generators_all_profiles"] = max(stats["max_generators_all_profiles"], len(gens))


def new_stats():
    return {
        "profiles": 0,
        "negative_profiles": 0,
        "type_set_margins": 0,
        "lattice_extremal_checks": 0,
        "minimizer_lattice_pair_checks": 0,
        "unique_maximum_minimizer_checks": 0,
        "sharp_upset_checks": 0,
        "generator_reconstruction_checks": 0,
        "generator_antichain_pair_checks": 0,
        "different_demand_staircase_checks": 0,
        "equal_demand_staircase_checks": 0,
        "closure_flow_value_checks": 0,
        "residual_maximal_cut_checks": 0,
        "negative_generator_histogram": Counter(),
        "max_negative_generators": 0,
        "max_generators_all_profiles": 0,
    }


def serialise_stats(stats):
    out = dict(stats)
    out["negative_generator_histogram"] = {
        str(k): v for k, v in sorted(stats["negative_generator_histogram"].items())
    }
    return out


def main():
    stats = new_stats()
    universe = [
        (0, 0, 0), (0, 1, 1),
        (1, 1, 0), (1, 2, 1), (1, 3, 2),
        (2, 2, 1), (2, 3, 0), (2, 4, 2),
    ]

    exhaustive = 0
    for n in range(1, 6):
        for profile in combinations_with_replacement(universe, n):
            audit_profile(profile, stats)
            exhaustive += 1

    rng = random.Random(SEED)
    random_profiles = 3000
    for _ in range(random_profiles):
        n = rng.randint(1, 8)
        profile = []
        for __ in range(n):
            q = rng.randint(0, 6)
            rho = rng.randint(0, 6)
            P = rng.randint(0, 8)
            profile.append((q, q + rho, P))
        audit_profile(tuple(profile), stats)

    report = {
        "schema": "canonical-antichain-certificate-verification-v1",
        "result": "PASS",
        "seed": SEED,
        "exhaustive_universe": [list(x) for x in universe],
        "exhaustive_max_order": 5,
        "exhaustive_profiles": exhaustive,
        "random_profiles": random_profiles,
        **serialise_stats(stats),
        "claims_checked": [
            "minimum Hall-margin type sets are closed under union and intersection",
            "unique minimal and maximal minimizers exist",
            "the maximal minimizer is the unique maximum-cardinality minimizer",
            "the maximal minimizer is a sharp-hardness up-set",
            "minimal generators form an antichain and reconstruct the maximal minimizer",
            "generator boundary obeys the q/c/P staircase restrictions",
            "closure-augmented quotient max-flow value equals Q plus minimum Hall margin",
            "residual vertices unable to reach sink project to the canonical maximal minimizer",
        ],
        "arithmetic": "exact integers only",
        "external_review": "OPEN",
        "note": "Independent finite arithmetic audit of the target-Hall theorem package; not third-party review of the Murty-Simon bridge.",
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
