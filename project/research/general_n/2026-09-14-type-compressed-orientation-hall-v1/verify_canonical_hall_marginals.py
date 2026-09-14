#!/usr/bin/env python3
"""Independent finite audit for CANONICAL_HALL_MARGINALS.md."""
from collections import Counter
from itertools import combinations_with_replacement
from pathlib import Path
import json
import random

SEED = 742091402
OUT = Path(__file__).resolve().parent / "CANONICAL_HALL_MARGINALS_VERIFICATION.json"


def compat(x, y):
    qx, cx, _ = x
    qy, cy, _ = y
    return qx <= cy + 1 and qy <= cx


def grouped(profile):
    ct = Counter(profile)
    types = tuple(sorted(ct))
    counts = tuple(ct[t] for t in types)
    return types, counts


def y_counts(types, counts, mask):
    ys = []
    for s, sigma in enumerate(types):
        y = sum(counts[t] for t, tau in enumerate(types) if ((mask >> t) & 1) and compat(tau, sigma))
        if (mask >> s) & 1:
            y -= 1
        if y < 0:
            raise AssertionError(("negative y", types, counts, mask, s))
        ys.append(y)
    return ys


def capacity(types, counts, mask):
    ys = y_counts(types, counts, mask)
    return sum(counts[s] * min(types[s][2], ys[s]) for s in range(len(types)))


def demand(types, counts, mask):
    return sum(counts[t] * types[t][0] for t in range(len(types)) if (mask >> t) & 1)


def margin(types, counts, mask):
    return capacity(types, counts, mask) - demand(types, counts, mask)


def extremal_minimizers(types, counts):
    vals = [margin(types, counts, m) for m in range(1 << len(types))]
    best = min(vals)
    mins = [m for m, v in enumerate(vals) if v == best]
    mp = 0
    mm = (1 << len(types)) - 1
    for m in mins:
        mp |= m
        mm &= m
    if margin(types, counts, mp) != best or margin(types, counts, mm) != best:
        raise AssertionError(("minimizer lattice failure", types, counts, best, mp, mm))
    return best, mp, mm


def k_inc(types, counts, t, s):
    return counts[t] * int(compat(types[t], types[s])) - int(t == s)


def compatible_degree_per_copy(types, counts, t):
    d = 0
    for s in range(len(types)):
        if compat(types[t], types[s]):
            d += counts[s]
    return d - 1


def audit(profile, stats):
    types, counts = grouped(profile)
    best, mp, mm = extremal_minimizers(types, counts)
    y = y_counts(types, counts, mp)
    h = capacity(types, counts, mp)

    for t in range(len(types)):
        nt, qt = counts[t], types[t][0]
        if not ((mp >> t) & 1):
            mp2 = mp | (1 << t)
            direct_gain = capacity(types, counts, mp2) - h
            formula_gain = 0
            for s in range(len(types)):
                k = k_inc(types, counts, t, s)
                if k < 0:
                    raise AssertionError(("negative addition k", types, counts, t, s, k))
                formula_gain += counts[s] * (min(types[s][2], y[s] + k) - min(types[s][2], y[s]))
            if direct_gain != formula_gain:
                raise AssertionError(("addition formula", profile, t, direct_gain, formula_gain))
            fdiff = margin(types, counts, mp2) - best
            if fdiff < 1 or direct_gain < nt * qt + 1:
                raise AssertionError(("strict exterior marginal", profile, t, best, fdiff, direct_gain, nt * qt))
            slack_gain = 0
            for s in range(len(types)):
                k = k_inc(types, counts, t, s)
                slack = max(0, types[s][2] - y[s])
                slack_gain += counts[s] * min(k, slack)
            if slack_gain != direct_gain:
                raise AssertionError(("slack gain identity", profile, t, slack_gain, direct_gain))
            d = compatible_degree_per_copy(types, counts, t)
            if d < qt + 1:
                raise AssertionError(("exterior raw degree corollary", profile, t, d, qt))
            stats["exterior_types_checked"] += 1
            stats["minimum_exterior_gap"] = min(stats["minimum_exterior_gap"], fdiff)
        else:
            mp2 = mp & ~(1 << t)
            direct_loss = h - capacity(types, counts, mp2)
            formula_loss = 0
            for s in range(len(types)):
                k = k_inc(types, counts, t, s)
                if k < 0 or y[s] < k:
                    raise AssertionError(("bad removal k", types, counts, t, s, k, y[s]))
                formula_loss += counts[s] * (min(types[s][2], y[s]) - min(types[s][2], y[s] - k))
            if direct_loss != formula_loss:
                raise AssertionError(("removal formula", profile, t, direct_loss, formula_loss))
            if direct_loss > nt * qt:
                raise AssertionError(("interior marginal", profile, t, direct_loss, nt * qt))
            if (mm >> t) & 1 and direct_loss > nt * qt - 1:
                raise AssertionError(("M- strict removal", profile, t, direct_loss, nt * qt, mm))
            stats["interior_types_checked"] += 1
            stats["mminus_types_checked"] += int((mm >> t) & 1)

    stats["profiles"] += 1
    stats["infeasible_profiles"] += int(best < 0)
    stats["feasible_profiles"] += int(best >= 0)
    stats["max_types"] = max(stats["max_types"], len(types))


def main():
    universe = [
        (0, 0, 0), (0, 1, 1),
        (1, 1, 0), (1, 2, 1), (1, 3, 2),
        (2, 2, 1), (2, 3, 2), (2, 4, 3),
    ]
    stats = {
        "profiles": 0,
        "infeasible_profiles": 0,
        "feasible_profiles": 0,
        "exterior_types_checked": 0,
        "interior_types_checked": 0,
        "mminus_types_checked": 0,
        "minimum_exterior_gap": 10**9,
        "max_types": 0,
    }
    exhaustive = 0
    for n in range(1, 6):
        for p in combinations_with_replacement(universe, n):
            audit(p, stats)
            exhaustive += 1

    rng = random.Random(SEED)
    random_profiles = 1200
    for _ in range(random_profiles):
        n = rng.randint(1, 7)
        p = []
        for __ in range(n):
            q = rng.randint(0, 4)
            rho = rng.randint(0, 4)
            cap = rng.randint(0, 5)
            p.append((q, q + rho, cap))
        audit(tuple(p), stats)

    if stats["minimum_exterior_gap"] == 10**9:
        stats["minimum_exterior_gap"] = None
    report = {
        "schema": "canonical-hall-marginals-verification-v1",
        "result": "PASS",
        "seed": SEED,
        "exhaustive_profiles": exhaustive,
        "random_profiles": random_profiles,
        **stats,
        "claims_checked": [
            "complete-type addition/removal incoming-count formulas",
            "strict positive integer marginal for every type outside M+",
            "exterior target-capacity gain is at least n_tau*q_tau+1",
            "exterior gain equals the compatible unsaturated-slack formula",
            "every exterior source copy has directed-compatible degree at least q_tau+1",
            "interior target-capacity loss is at most n_tau*q_tau",
            "types in M- satisfy the strict removal inequality",
        ],
        "external_review": "OPEN",
        "note": "Independent finite audit of local optimality identities for the canonical maximal Hall minimizer.",
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
