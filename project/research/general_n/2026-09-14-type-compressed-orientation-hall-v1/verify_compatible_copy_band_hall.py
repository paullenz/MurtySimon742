#!/usr/bin/env python3
"""Independent finite audit for COMPATIBLE_COPY_BAND_HALL.md.

This file intentionally does not import the earlier Hall or staircase verifiers.
It rebuilds the relevant definitions, labelled max-flow network, staircase bands,
compatible-copy capacities and refined band flow from scratch.
"""
from collections import Counter, deque
from itertools import combinations_with_replacement
from pathlib import Path
import json
import random

SEED = 7420914
HERE = Path(__file__).resolve().parent
OUT = HERE / "COMPATIBLE_COPY_BAND_HALL_VERIFICATION.json"


class Dinic:
    def __init__(self, n):
        self.g = [[] for _ in range(n)]

    def add(self, u, v, cap):
        f = [v, int(cap), None]
        r = [u, 0, f]
        f[2] = r
        self.g[u].append(f)
        self.g[v].append(r)

    def maxflow(self, s, t):
        total = 0
        while True:
            level = [-1] * len(self.g)
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
            it = [0] * len(self.g)

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
                z = dfs(s, 10**18)
                if not z:
                    break
                total += z


def compatible(src, dst):
    qs, cs, _ = src
    qt, ct, _ = dst
    return qs <= ct + 1 and qt <= cs


def sharp_dominates(x, y):
    qx, cx, px = x
    qy, cy, py = y
    return cx <= cy and (qx > qy or (qx == qy and px >= py))


def group_profile(profile):
    count = Counter(profile)
    types = tuple(sorted(count))
    counts = tuple(count[t] for t in types)
    return types, counts


def is_sharp_upset(types, mask):
    for y in range(len(types)):
        if not ((mask >> y) & 1):
            continue
        for x in range(len(types)):
            if x != y and sharp_dominates(types[x], types[y]):
                if not ((mask >> x) & 1):
                    return False
    return True


def minimal_generators(types, mask):
    out = []
    for i in range(len(types)):
        if not ((mask >> i) & 1):
            continue
        if any(
            j != i
            and ((mask >> j) & 1)
            and sharp_dominates(types[i], types[j])
            for j in range(len(types))
        ):
            continue
        out.append(i)
    return sorted(out, key=lambda i: types[i][1])


def build_bands(types, counts, mask):
    gens = minimal_generators(types, mask)
    if mask and not gens:
        raise AssertionError(("nonempty upset has no generator", types, mask))
    h = len(gens)
    band = [-1] * len(types)
    multiplicity = [0] * h
    demand = [0] * h

    for t in range(len(types)):
        if not ((mask >> t) & 1):
            continue
        candidates = [i for i, g in enumerate(gens) if types[t][1] <= types[g][1]]
        if not candidates:
            raise AssertionError(("band assignment failed", types, counts, mask, t, gens))
        i = candidates[0]
        band[t] = i
        multiplicity[i] += counts[t]
        demand[i] += counts[t] * types[t][0]
        q, c, _ = types[t]
        qg, cg, _ = types[gens[i]]
        if not (q >= qg and c <= cg):
            raise AssertionError(("generator containment failed", types, mask, t, gens[i]))

    return gens, band, multiplicity, demand


def expand_labels(counts):
    labels = []
    for t, n in enumerate(counts):
        labels.extend([t] * n)
    return labels


def exact_selected_flow(types, counts, mask):
    labels = expand_labels(counts)
    selected = [u for u, t in enumerate(labels) if (mask >> t) & 1]
    source = 0
    left0 = 1
    right0 = left0 + len(selected)
    sink = right0 + len(labels)
    net = Dinic(sink + 1)

    demand = 0
    for j, u in enumerate(selected):
        t = labels[u]
        q = types[t][0]
        demand += q
        net.add(source, left0 + j, q)
        for w, s in enumerate(labels):
            if u != w and compatible(types[t], types[s]):
                net.add(left0 + j, right0 + w, 1)

    for w, s in enumerate(labels):
        net.add(right0 + w, sink, types[s][2])

    return net.maxflow(source, sink), demand


def explicit_pair_count(types, counts, mask, band, i, sigma):
    labels = expand_labels(counts)
    total = 0
    for u, t in enumerate(labels):
        if not ((mask >> t) & 1) or band[t] != i:
            continue
        for w, s in enumerate(labels):
            if s == sigma and u != w and compatible(types[t], types[s]):
                total += 1
    return total


def refined_band_flow(types, counts, mask, stats):
    gens, band, multiplicity, band_demand = build_bands(types, counts, mask)
    h = len(gens)
    if not h:
        return 0, 0, gens, band, {}

    source = 0
    band0 = 1
    target0 = band0 + h
    sink = target0 + len(types)
    net = Dinic(sink + 1)
    total_demand = sum(band_demand)

    for i in range(h):
        net.add(source, band0 + i, band_demand[i])

    capacities = {}
    for i in range(h):
        for sigma in range(len(types)):
            compatible_copies = sum(
                counts[t]
                for t in range(len(types))
                if ((mask >> t) & 1)
                and band[t] == i
                and compatible(types[t], types[sigma])
            )
            delta = 1 if (((mask >> sigma) & 1) and band[sigma] == i) else 0
            refined = counts[sigma] * (compatible_copies - delta)
            if refined < 0:
                raise AssertionError(("negative refined capacity", types, counts, mask, i, sigma))

            labelled = explicit_pair_count(types, counts, mask, band, i, sigma)
            if refined != labelled:
                raise AssertionError((
                    "compatible-copy formula differs from explicit labelled pair count",
                    types, counts, mask, i, sigma, refined, labelled,
                ))
            stats["labelled_pair_capacity_checks"] += 1

            coarse = 0
            if compatible(types[gens[i]], types[sigma]):
                coarse = counts[sigma] * (multiplicity[i] - delta)
            if refined > coarse:
                raise AssertionError((
                    "refinement exceeds coarse capacity",
                    types, counts, mask, i, sigma, refined, coarse,
                ))
            stats["coarse_monotonicity_checks"] += 1

            capacities[(i, sigma)] = refined
            if refined:
                net.add(band0 + i, target0 + sigma, refined)

    for sigma in range(len(types)):
        net.add(target0 + sigma, sink, counts[sigma] * types[sigma][2])

    return net.maxflow(source, sink), total_demand, gens, band, capacities


def audit_upset(profile, mask, stats):
    types, counts = group_profile(profile)
    if not is_sharp_upset(types, mask):
        raise AssertionError(("audit called on non-upset", types, mask))

    exact_flow, exact_demand = exact_selected_flow(types, counts, mask)
    refined_flow, refined_demand, gens, band, _ = refined_band_flow(
        types, counts, mask, stats
    )

    if exact_demand != refined_demand:
        raise AssertionError(("demand mismatch", types, counts, mask, exact_demand, refined_demand))
    if exact_flow > refined_flow:
        raise AssertionError((
            "exact flow exceeds refined relaxation",
            types, counts, mask, exact_flow, refined_flow, exact_demand,
        ))
    if exact_flow == exact_demand and refined_flow != refined_demand:
        raise AssertionError((
            "exact feasibility failed to imply refined feasibility",
            types, counts, mask, exact_flow, refined_flow, exact_demand,
        ))

    stats["upsets_checked"] += 1
    stats["max_generators"] = max(stats["max_generators"], len(gens))
    stats["exact_to_refined_flow_order_checks"] += 1
    if exact_flow == exact_demand:
        stats["exact_feasible_upsets"] += 1
    if refined_flow < refined_demand:
        stats["refined_infeasible_upsets"] += 1


def audit_profile(profile, stats):
    types, _ = group_profile(profile)
    for mask in range(1 << len(types)):
        if is_sharp_upset(types, mask):
            audit_upset(profile, mask, stats)
    stats["profiles_checked"] += 1


def audit_state_226(stats):
    profile = (
        [(0, 1, 3)] * 7
        + [(2, 4, 4)] * 1
        + [(2, 5, 5)] * 3
        + [(4, 6, 2)] * 1
        + [(5, 9, 4)] * 1
        + [(6, 9, 3)] * 5
    )
    types, counts = group_profile(profile)
    expected_types = (
        (0, 1, 3),
        (2, 4, 4),
        (2, 5, 5),
        (4, 6, 2),
        (5, 9, 4),
        (6, 9, 3),
    )
    if types != expected_types:
        raise AssertionError(("state 226 type order changed", types))

    mask = (1 << 3) | (1 << 4) | (1 << 5)
    if not is_sharp_upset(types, mask):
        raise AssertionError("state 226 selected witness is not a sharp upset")

    exact_flow, exact_demand = exact_selected_flow(types, counts, mask)
    refined_flow, refined_demand, gens, band, capacities = refined_band_flow(
        types, counts, mask, stats
    )

    if gens != [3, 4]:
        raise AssertionError(("state 226 generator mismatch", gens))
    if band[3:] != [0, 1, 1]:
        raise AssertionError(("state 226 band assignment mismatch", band))
    if exact_demand != 39 or refined_demand != 39:
        raise AssertionError(("state 226 demand mismatch", exact_demand, refined_demand))
    if exact_flow != 38 or refined_flow != 38:
        raise AssertionError(("state 226 flow mismatch", exact_flow, refined_flow))

    # Target type 1 is (q,c,P,n)=(2,4,4,1). Band 1 must contribute
    # only its generator copy, not the five incompatible (6,9,3) copies.
    if capacities[(1, 1)] != 1:
        raise AssertionError(("state 226 corrected band1->target1 capacity", capacities[(1, 1)]))

    stats["state_226_fixture_checks"] += 1
    return {
        "selected_demand": refined_demand,
        "exact_selected_flow": exact_flow,
        "refined_band_flow": refined_flow,
        "generators": gens,
        "band_assignment_selected_types": band[3:],
        "corrected_band1_target1_pair_capacity": capacities[(1, 1)],
    }


def main():
    stats = {
        "profiles_checked": 0,
        "upsets_checked": 0,
        "labelled_pair_capacity_checks": 0,
        "coarse_monotonicity_checks": 0,
        "exact_to_refined_flow_order_checks": 0,
        "exact_feasible_upsets": 0,
        "refined_infeasible_upsets": 0,
        "state_226_fixture_checks": 0,
        "max_generators": 0,
    }

    universe = [
        (0, 0, 0),
        (0, 1, 1),
        (1, 1, 0),
        (1, 2, 1),
        (1, 3, 2),
        (2, 2, 1),
        (2, 3, 0),
    ]

    exhaustive_profiles = 0
    for n in range(1, 7):
        for profile in combinations_with_replacement(universe, n):
            audit_profile(profile, stats)
            exhaustive_profiles += 1

    rng = random.Random(SEED)
    random_profiles = 1000
    for _ in range(random_profiles):
        n = rng.randint(1, 9)
        profile = []
        for __ in range(n):
            q = rng.randint(0, 7)
            rho = rng.randint(0, 7)
            p = rng.randint(0, 9)
            profile.append((q, q + rho, p))
        audit_profile(tuple(profile), stats)

    fixture = audit_state_226(stats)

    report = {
        "schema": "compatible-copy-band-hall-verification-v1",
        "result": "PASS",
        "seed": SEED,
        "exhaustive_universe": [list(x) for x in universe],
        "exhaustive_max_order": 6,
        "exhaustive_profiles": exhaustive_profiles,
        "random_profiles": random_profiles,
        **stats,
        "state_226": fixture,
        "claims_checked": [
            "compatible-copy band edge capacity equals explicit labelled compatible-pair count",
            "compatible-copy edge capacities never exceed coarse staircase-band capacities",
            "exact selected-source maximum flow never exceeds compatible-copy band maximum flow",
            "exact selected-source feasibility implies compatible-copy band feasibility",
            "state 226 has selected demand 39 and compatible-copy band flow 38",
        ],
        "external_review": "OPEN",
        "note": (
            "Independent dependency-free finite audit of the compatible-copy band theorem. "
            "It does not independently validate the upstream Murty-Simon graph-to-constraint bridge."
        ),
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
