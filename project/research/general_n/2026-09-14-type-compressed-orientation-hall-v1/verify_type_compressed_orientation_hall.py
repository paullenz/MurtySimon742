#!/usr/bin/env python3
"""Finite audit for TYPE_COMPRESSED_ORIENTATION_HALL.md.

This verifier is deliberately separate from the C++ relational scanners. It
checks the cut identities directly by labelled subset enumeration, then checks
that the minimum Hall margin is attained by a union of complete (q,c,P) type
classes. It also checks coordinatewise discrete concavity of the compressed
margin on a deterministic broad random suite.
"""
from collections import Counter, defaultdict
from itertools import product
from pathlib import Path
import json
import random

HERE = Path(__file__).resolve().parent
OUT = HERE / "TYPE_COMPRESSED_ORIENTATION_HALL_VERIFICATION.json"

# Small canonical-ish universe used exhaustively through labelled order five.
SMALL_TYPES = (
    (0, 0, 0),
    (0, 1, 1),
    (1, 1, 0),
    (1, 2, 1),
    (2, 2, 1),
    (2, 3, 2),
)


def compatible(source, target):
    q, c, _ = source
    qw, cw, _ = target
    return q <= cw + 1 and qw <= c


def labelled_margin(profile, mask):
    n = len(profile)
    chosen = [u for u in range(n) if mask >> u & 1]
    demand = sum(profile[u][0] for u in chosen)
    capacity = 0
    for w in range(n):
        incoming = sum(
            u != w and compatible(profile[u], profile[w])
            for u in chosen
        )
        capacity += min(profile[w][2], incoming)
    return capacity - demand


def grouped(profile):
    groups = defaultdict(list)
    for i, typ in enumerate(profile):
        groups[typ].append(i)
    types = tuple(sorted(groups))
    counts = tuple(len(groups[t]) for t in types)
    return types, counts, groups


def count_vector(profile, mask, types, groups):
    return tuple(sum(mask >> i & 1 for i in groups[t]) for t in types)


def compressed_margin(types, counts, xs):
    demand = sum(t[0] * x for t, x in zip(types, xs))
    capacity = 0
    for j, sigma in enumerate(types):
        m = sum(
            x for tau, x in zip(types, xs) if compatible(tau, sigma)
        )
        # Canonical c=q+rho>=q makes same-type numerical compatibility true.
        if not compatible(sigma, sigma):
            raise AssertionError(("same type unexpectedly incompatible", sigma))
        n_sigma = counts[j]
        x_sigma = xs[j]
        p_sigma = sigma[2]
        capacity += (n_sigma - x_sigma) * min(p_sigma, m)
        capacity += x_sigma * min(p_sigma, m - 1)
    return capacity - demand


def whole_type_min(profile, types, counts):
    best = None
    best_x = None
    for bits in product((0, 1), repeat=len(types)):
        xs = tuple(n if bit else 0 for bit, n in zip(bits, counts))
        value = compressed_margin(types, counts, xs)
        if best is None or value < best:
            best, best_x = value, xs
    return best, best_x


def check_coordinate_concavity(types, counts):
    checked = 0
    for j, n_j in enumerate(counts):
        others = [range(n + 1) for i, n in enumerate(counts) if i != j]
        for fixed in product(*others):
            base = []
            it = iter(fixed)
            for i in range(len(types)):
                base.append(None if i == j else next(it))
            values = []
            for x in range(n_j + 1):
                xs = tuple(x if i == j else base[i] for i in range(len(types)))
                values.append(compressed_margin(types, counts, xs))
            diffs = [values[i + 1] - values[i] for i in range(len(values) - 1)]
            if any(diffs[i + 1] > diffs[i] for i in range(len(diffs) - 1)):
                raise AssertionError((
                    "coordinate concavity failure", types, counts, j, fixed,
                    values, diffs,
                ))
            checked += 1
    return checked


def verify_profile(profile, do_concavity=True):
    types, counts, groups = grouped(profile)
    n = len(profile)
    all_min = None
    all_min_mask = None
    formula_checks = 0
    for mask in range(1 << n):
        direct = labelled_margin(profile, mask)
        xs = count_vector(profile, mask, types, groups)
        compressed = compressed_margin(types, counts, xs)
        if direct != compressed:
            raise AssertionError((
                "labelled/compressed mismatch", profile, mask, xs,
                direct, compressed,
            ))
        formula_checks += 1
        if all_min is None or direct < all_min:
            all_min, all_min_mask = direct, mask

    vertex_min, vertex_x = whole_type_min(profile, types, counts)
    if all_min != vertex_min:
        raise AssertionError((
            "whole-type minimum mismatch", profile, types, counts,
            all_min, all_min_mask, vertex_min, vertex_x,
        ))

    concavity_checks = check_coordinate_concavity(types, counts) if do_concavity else 0
    return formula_checks, concavity_checks, all_min < 0


def exhaustive_suite():
    stats = Counter()
    for n in range(1, 6):
        for profile in product(SMALL_TYPES, repeat=n):
            f, c, bad = verify_profile(profile, do_concavity=True)
            stats["profiles"] += 1
            stats["formula_checks"] += f
            stats["concavity_lines"] += c
            stats["profiles_with_hall_violation"] += int(bad)
    return stats


def random_suite(seed=7420914, profiles=5000):
    rng = random.Random(seed)
    stats = Counter()
    for _ in range(profiles):
        n = rng.randint(1, 8)
        palette = []
        for _ in range(rng.randint(1, min(5, n))):
            q = rng.randint(0, n - 1)
            rho = rng.randint(0, 4)
            c = q + rho
            p = rng.randint(0, n - 1)
            palette.append((q, c, p))
        profile = tuple(rng.choice(palette) for _ in range(n))
        f, c, bad = verify_profile(profile, do_concavity=True)
        stats["profiles"] += 1
        stats["formula_checks"] += f
        stats["concavity_lines"] += c
        stats["profiles_with_hall_violation"] += int(bad)
    stats["seed"] = seed
    return stats


def main():
    exhaustive = exhaustive_suite()
    random_stats = random_suite()
    result = {
        "schema": "type-compressed-orientation-hall-verification-v1",
        "status": "PASS",
        "exhaustive_small_type_universe": {
            "types": [list(t) for t in SMALL_TYPES],
            **dict(exhaustive),
        },
        "deterministic_broad_random": dict(random_stats),
        "claims_checked": [
            "labelled subset margin equals compressed type-count formula",
            "minimum over all subsets equals minimum over unions of complete types",
            "compressed Hall margin is coordinatewise discretely concave",
        ],
        "arithmetic": "exact integers only",
        "external_review": "OPEN",
        "note": "Finite audit supports but does not replace the hand proof.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
