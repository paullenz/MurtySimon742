#!/usr/bin/env python3
"""Independent finite audit for DOMINANCE_UPSET_HALL.md.

This verifier does not import or call the C++ relational scanners.  It works
from the labelled Hall-margin definition directly.
"""
from itertools import combinations_with_replacement
import json
import random
from pathlib import Path

SEED = 7420914


def compatible(u, w):
    qu, cu, _ = u
    qw, cw, _ = w
    return qu <= cw + 1 and qw <= cu


def dominates(x, y):
    qx, cx, px = x
    qy, cy, py = y
    return qx >= qy and cx <= cy and px >= py


def intervals_compatible(u, w):
    qu, cu, _ = u
    qw, cw, _ = w
    # [qu,cu] intersects [qw,cw+1]
    return max(qu, qw) <= min(cu, cw + 1)


def build_D(profile):
    n = len(profile)
    return [[i != j and compatible(profile[i], profile[j]) for j in range(n)] for i in range(n)]


def margin(profile, D, mask):
    n = len(profile)
    total = 0
    for w in range(n):
        P = profile[w][2]
        incoming = sum(1 for u in range(n) if (mask >> u) & 1 and D[u][w])
        total += min(P, incoming)
    total -= sum(profile[u][0] for u in range(n) if (mask >> u) & 1)
    return total


def is_upset(profile, mask):
    n = len(profile)
    for y in range(n):
        if not ((mask >> y) & 1):
            continue
        for x in range(n):
            if x != y and dominates(profile[x], profile[y]) and not ((mask >> x) & 1):
                return False
    return True


def check_profile(profile, counters):
    n = len(profile)
    D = build_D(profile)

    # Interval identity, before deleting the diagonal.
    for u in range(n):
        for w in range(n):
            if compatible(profile[u], profile[w]) != intervals_compatible(profile[u], profile[w]):
                raise AssertionError(("interval_identity", profile, u, w))
            counters["interval_checks"] += 1

    values = [margin(profile, D, mask) for mask in range(1 << n)]
    counters["margin_evaluations"] += 1 << n

    # Local two-element form of submodularity.
    for S in range(1 << n):
        missing = [x for x in range(n) if not ((S >> x) & 1)]
        for ai in range(len(missing)):
            a = missing[ai]
            for bi in range(ai + 1, len(missing)):
                b = missing[bi]
                lhs = values[S | (1 << a)] + values[S | (1 << b)]
                rhs = values[S] + values[S | (1 << a) | (1 << b)]
                if lhs < rhs:
                    raise AssertionError(("submodularity", profile, S, a, b, lhs, rhs))
                counters["submodularity_checks"] += 1

    # Exchange inequality for every dominance pair and every background set.
    for x in range(n):
        for y in range(n):
            if x == y or not dominates(profile[x], profile[y]):
                continue
            base_bits = [z for z in range(n) if z not in (x, y)]
            for sub in range(1 << len(base_bits)):
                T = 0
                for j, z in enumerate(base_bits):
                    if (sub >> j) & 1:
                        T |= 1 << z
                dx = values[T | (1 << x)] - values[T]
                dy = values[T | (1 << y)] - values[T]
                if dx > dy:
                    raise AssertionError(("exchange", profile, x, y, T, dx, dy))
                counters["exchange_checks"] += 1

    m = min(values)
    minimizers = [mask for mask, v in enumerate(values) if v == m]
    max_card = max(mask.bit_count() for mask in minimizers)
    max_card_minimizers = [mask for mask in minimizers if mask.bit_count() == max_card]
    if not max_card_minimizers:
        raise AssertionError("no minimizer")
    if any(not is_upset(profile, mask) for mask in max_card_minimizers):
        bad = [mask for mask in max_card_minimizers if not is_upset(profile, mask)][0]
        raise AssertionError(("max_card_not_upset", profile, m, bad))

    upset_values = [values[mask] for mask in range(1 << n) if is_upset(profile, mask)]
    if min(upset_values) != m:
        raise AssertionError(("upset_minimum_mismatch", profile, m, min(upset_values)))

    counters["profiles"] += 1
    counters["profiles_with_negative_margin"] += int(m < 0)
    counters["max_card_minimizers"] += len(max_card_minimizers)
    counters["upset_sets_checked"] += sum(is_upset(profile, mask) for mask in range(1 << n))


def main():
    counters = {
        "profiles": 0,
        "profiles_with_negative_margin": 0,
        "interval_checks": 0,
        "margin_evaluations": 0,
        "submodularity_checks": 0,
        "exchange_checks": 0,
        "max_card_minimizers": 0,
        "upset_sets_checked": 0,
    }

    # Exhaustive small universe.  combinations_with_replacement is sufficient:
    # every labelled permutation gives an isomorphic set-function instance.
    universe = [
        (0, 0, 0),
        (0, 1, 1),
        (1, 1, 0),
        (1, 2, 1),
        (1, 3, 2),
        (2, 2, 1),
        (2, 3, 0),
        (2, 4, 2),
    ]
    exhaustive_profiles = 0
    for n in range(1, 6):
        for profile in combinations_with_replacement(universe, n):
            check_profile(profile, counters)
            exhaustive_profiles += 1

    # Deterministic broad challenge.  Canonical-shaped intervals satisfy c=q+rho.
    rng = random.Random(SEED)
    random_profiles = 3000
    for _ in range(random_profiles):
        n = rng.randint(1, 8)
        profile = []
        for _ in range(n):
            q = rng.randint(0, 6)
            rho = rng.randint(0, 6)
            c = q + rho
            P = rng.randint(0, 8)
            profile.append((q, c, P))
        check_profile(tuple(profile), counters)

    report = {
        "schema": "dominance-upset-hall-verification-v1",
        "result": "PASS",
        "seed": SEED,
        "exhaustive_universe": [list(x) for x in universe],
        "exhaustive_max_order": 5,
        "exhaustive_profiles": exhaustive_profiles,
        "random_profiles": random_profiles,
        **counters,
        "claims_checked": [
            "interval identity",
            "labelled Hall-margin submodularity",
            "dominance exchange inequality",
            "maximum-cardinality minimizers are hardness up-sets",
            "unrestricted minimum equals minimum over hardness up-sets",
        ],
        "external_review": "OPEN",
        "note": "Independent finite arithmetic audit; not independent mathematical review of the Murty-Simon bridge.",
    }
    Path("DOMINANCE_UPSET_HALL_VERIFICATION.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
