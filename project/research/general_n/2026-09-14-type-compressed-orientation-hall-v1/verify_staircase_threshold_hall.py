#!/usr/bin/env python3
"""Independent finite audit for STAIRCASE_THRESHOLD_HALL.md."""
from collections import Counter
from itertools import combinations_with_replacement
from pathlib import Path
import json
import random

SEED = 7420914
OUT = Path(__file__).resolve().parent / "STAIRCASE_THRESHOLD_HALL_VERIFICATION.json"


def compatible(a, b):
    qa, ca, _ = a
    qb, cb, _ = b
    return qa <= cb + 1 and qb <= ca


def dominates(x, y):
    qx, cx, px = x
    qy, cy, py = y
    return cx <= cy and (qx > qy or (qx == qy and px >= py))


def grouped(profile):
    ct = Counter(profile)
    types = tuple(sorted(ct))
    counts = tuple(ct[t] for t in types)
    return types, counts


def is_upset(types, mask):
    for y in range(len(types)):
        if not ((mask >> y) & 1):
            continue
        for x in range(len(types)):
            if x != y and dominates(types[x], types[y]) and not ((mask >> x) & 1):
                return False
    return True


def generators(types, mask):
    out = []
    for i in range(len(types)):
        if not ((mask >> i) & 1):
            continue
        if any(
            j != i and ((mask >> j) & 1) and dominates(types[i], types[j])
            for j in range(len(types))
        ):
            continue
        out.append(i)
    return sorted(out, key=lambda i: types[i][1])


def staircase_membership(types, gens, idx):
    q, c, p = types[idx]
    chosen = None
    for g in gens:
        qg, cg, pg = types[g]
        if c <= cg:
            chosen = (qg, cg, pg)
            break
    if chosen is None:
        return False
    qg, _, pg = chosen
    return q > qg or (q == qg and p >= pg)


def direct_margin(types, counts, mask):
    demand = 0
    cap = 0
    for i, (typ, n) in enumerate(zip(types, counts)):
        if (mask >> i) & 1:
            demand += n * typ[0]
    for j, (sigma, ns) in enumerate(zip(types, counts)):
        incoming = 0
        for i, (tau, nt) in enumerate(zip(types, counts)):
            if (mask >> i) & 1 and compatible(tau, sigma):
                incoming += nt - 1 if i == j else nt
        cap += ns * min(sigma[2], incoming)
    return cap - demand


def staircase_margin(types, counts, gens):
    selected = [staircase_membership(types, gens, i) for i in range(len(types))]
    demand = sum(
        n * typ[0]
        for typ, n, use in zip(types, counts, selected)
        if use
    )
    capacity = 0
    for j, (sigma, ns) in enumerate(zip(types, counts)):
        qs, cs, ps = sigma
        m = 0
        for tau, nt, use in zip(types, counts, selected):
            if not use:
                continue
            qt, ct, _ = tau
            if ct >= qs and qt <= cs + 1:
                m += nt
        if selected[j]:
            m -= 1
        if m < 0:
            raise AssertionError(("negative staircase incoming", types, gens, j, m))
        capacity += ns * min(ps, m)
    return capacity - demand


def audit_profile(profile, stats):
    types, counts = grouped(profile)
    k = len(types)
    for mask in range(1 << k):
        if not is_upset(types, mask):
            continue
        stats["upsets_checked"] += 1
        gens = generators(types, mask)
        stats["max_generators"] = max(stats["max_generators"], len(gens))
        stats["generator_histogram"][len(gens)] += 1

        cs = [types[g][1] for g in gens]
        if len(cs) != len(set(cs)) or cs != sorted(cs):
            raise AssertionError(("generator cross-degree failure", profile, mask, gens))
        stats["distinct_c_checks"] += 1

        for a, b in zip(gens, gens[1:]):
            qa, ca, pa = types[a]
            qb, cb, pb = types[b]
            if not ca < cb or not qa <= qb:
                raise AssertionError(("staircase q/c ordering failure", profile, mask, types[a], types[b]))
            if qa == qb and not pa < pb:
                raise AssertionError(("staircase P plateau failure", profile, mask, types[a], types[b]))
            stats["generator_step_checks"] += 1

        rebuilt = 0
        for i in range(k):
            use = staircase_membership(types, gens, i)
            if use:
                rebuilt |= 1 << i
            stats["membership_checks"] += 1
        if rebuilt != mask:
            raise AssertionError(("staircase reconstruction failure", profile, mask, gens, rebuilt))
        stats["reconstruction_checks"] += 1

        dm = direct_margin(types, counts, mask)
        sm = staircase_margin(types, counts, gens)
        if dm != sm:
            raise AssertionError(("staircase margin failure", profile, mask, gens, dm, sm))
        stats["rectangle_margin_checks"] += 1

    stats["profiles"] += 1


def new_stats():
    return {
        "profiles": 0,
        "upsets_checked": 0,
        "distinct_c_checks": 0,
        "generator_step_checks": 0,
        "membership_checks": 0,
        "reconstruction_checks": 0,
        "rectangle_margin_checks": 0,
        "max_generators": 0,
        "generator_histogram": Counter(),
    }


def serialise(stats):
    d = dict(stats)
    d["generator_histogram"] = {
        str(k): v for k, v in sorted(stats["generator_histogram"].items())
    }
    return d


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
            p = rng.randint(0, 8)
            profile.append((q, q + rho, p))
        audit_profile(tuple(profile), stats)

    report = {
        "schema": "staircase-threshold-hall-verification-v1",
        "result": "PASS",
        "seed": SEED,
        "exhaustive_universe": [list(x) for x in universe],
        "exhaustive_max_order": 5,
        "exhaustive_profiles": exhaustive,
        "random_profiles": random_profiles,
        **serialise(stats),
        "claims_checked": [
            "sharp-upset generators have distinct cross degrees",
            "generator q is nondecreasing with increasing c",
            "generator P strictly increases along equal-q plateaus",
            "moving (q,P) threshold reconstructs every sharp hardness up-set exactly",
            "staircase rectangle-count formula equals direct complete-type Hall margin",
        ],
        "external_review": "OPEN",
        "note": "Independent finite arithmetic audit of the staircase representation; not third-party review of the Murty-Simon bridge.",
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
