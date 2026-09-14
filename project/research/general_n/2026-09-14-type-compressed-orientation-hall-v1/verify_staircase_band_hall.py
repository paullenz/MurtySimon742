#!/usr/bin/env python3
"""Independent arithmetic audit for STAIRCASE_BAND_HALL.md."""
from collections import Counter
from itertools import combinations_with_replacement
from pathlib import Path
import json
import random

SEED = 7420914
OUT = Path(__file__).resolve().parent / "STAIRCASE_BAND_HALL_VERIFICATION.json"


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


def audit_upset(types, counts, mask, stats):
    gens = generators(types, mask)
    h = len(gens)
    stats["max_bands"] = max(stats["max_bands"], h)
    if h == 0:
        if mask != 0:
            raise AssertionError(("nonempty upset without generator", types, mask))
        stats["upsets_checked"] += 1
        return

    # Assign every selected type to the first generator cross-degree at or above it.
    band_of = {}
    band_types = [[] for _ in range(h)]
    for t in range(len(types)):
        if not ((mask >> t) & 1):
            continue
        ct = types[t][1]
        candidates = [i for i, g in enumerate(gens) if ct <= types[g][1]]
        if not candidates:
            raise AssertionError(("selected type above last generator", types, mask, t, gens))
        i = candidates[0]
        band_of[t] = i
        band_types[i].append(t)

    M = [sum(counts[t] for t in band_types[i]) for i in range(h)]
    D = [sum(counts[t] * types[t][0] for t in band_types[i]) for i in range(h)]
    qg = [types[g][0] for g in gens]
    cg = [types[g][1] for g in gens]

    for i in range(h):
        if D[i] < qg[i] * M[i]:
            raise AssertionError(("band demand lower bound", types, mask, i, D[i], qg[i], M[i]))
        stats["band_demand_checks"] += 1
        for t in band_types[i]:
            qt, ct, _ = types[t]
            if not (qt >= qg[i] and ct <= cg[i]):
                raise AssertionError(("source interval containment", types, mask, i, t, gens[i]))
            stats["source_interval_containment_checks"] += 1

    # For each target type, compute the consecutive generator-compatible band range.
    I_masks = []
    for s, sigma in enumerate(types):
        idx = [i for i, g in enumerate(gens) if compatible(types[g], sigma)]
        if idx and idx != list(range(idx[0], idx[-1] + 1)):
            raise AssertionError(("nonconsecutive target band neighborhood", types, mask, s, idx, gens))
        stats["target_interval_checks"] += 1
        im = 0
        for i in idx:
            im |= 1 << i
        I_masks.append(im)
        if s in band_of and not ((im >> band_of[s]) & 1):
            raise AssertionError(("selected target missing own band generator compatibility", types, mask, s, band_of[s]))

    # Precompute actual compatible copy counts from each source band to each target type.
    actual_band = [[0] * len(types) for _ in range(h)]
    for i in range(h):
        for t in band_types[i]:
            for s, sigma in enumerate(types):
                if compatible(types[t], sigma):
                    actual_band[i][s] += counts[t]

    total_masks = 1 << h
    demand_sum = [0] * total_masks
    lower_sum = [0] * total_masks
    for J in range(1, total_masks):
        lsb = J & -J
        i = lsb.bit_length() - 1
        prev = J ^ lsb
        demand_sum[J] = demand_sum[prev] + D[i]
        lower_sum[J] = lower_sum[prev] + qg[i] * M[i]

    # Target-specific subset sums keep the all-J audit cheap and exact.
    actual_sub = [[0] * total_masks for _ in types]
    upper_sub = [[0] * total_masks for _ in types]
    for s in range(len(types)):
        for J in range(1, total_masks):
            lsb = J & -J
            i = lsb.bit_length() - 1
            prev = J ^ lsb
            actual_sub[s][J] = actual_sub[s][prev] + actual_band[i][s]
            upper_sub[s][J] = upper_sub[s][prev] + (M[i] if (I_masks[s] >> i) & 1 else 0)

    for J in range(total_masks):
        if lower_sum[J] > demand_sum[J]:
            raise AssertionError(("subset demand lower bound", types, mask, J))
        exact_cap = 0
        band_cap = 0
        for s, sigma in enumerate(types):
            delta = 0
            if s in band_of and ((J >> band_of[s]) & 1):
                delta = 1
            actual = actual_sub[s][J] - delta
            upper = upper_sub[s][J] - delta
            if actual < 0 or upper < 0 or actual > upper:
                raise AssertionError(("band incoming upper failure", types, mask, J, s, actual, upper))
            stats["incoming_upper_checks"] += 1
            exact_cap += counts[s] * min(sigma[2], actual)
            band_cap += counts[s] * min(sigma[2], upper)
        if exact_cap > band_cap:
            raise AssertionError(("band capacity dominance failure", types, mask, J, exact_cap, band_cap))
        stats["capacity_dominance_checks"] += 1
        stats["band_sets_checked"] += 1

    stats["upsets_checked"] += 1


def audit_profile(profile, stats):
    types, counts = grouped(profile)
    for mask in range(1 << len(types)):
        if is_upset(types, mask):
            audit_upset(types, counts, mask, stats)
    stats["profiles"] += 1


def main():
    stats = {
        "profiles": 0,
        "upsets_checked": 0,
        "band_sets_checked": 0,
        "band_demand_checks": 0,
        "source_interval_containment_checks": 0,
        "target_interval_checks": 0,
        "incoming_upper_checks": 0,
        "capacity_dominance_checks": 0,
        "max_bands": 0,
    }
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
    random_profiles = 1500
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
        "schema": "staircase-band-hall-verification-v1",
        "result": "PASS",
        "seed": SEED,
        "exhaustive_universe": [list(x) for x in universe],
        "exhaustive_max_order": 5,
        "exhaustive_profiles": exhaustive,
        "random_profiles": random_profiles,
        **stats,
        "claims_checked": [
            "selected source intervals are contained in their band-generator intervals",
            "target generator-compatible band neighborhoods are consecutive",
            "band demand dominates generator-demand lower bound",
            "actual compatible incoming counts never exceed band upper counts for every band subset",
            "exact Hall target capacity never exceeds staircase-band upper capacity",
        ],
        "external_review": "OPEN",
        "note": "Independent finite arithmetic audit of the staircase-band relaxation; not third-party review of the Murty-Simon bridge.",
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
