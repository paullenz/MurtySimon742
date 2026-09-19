#!/usr/bin/env python3
"""Independent finite audits for FULL_SUPPORT_SOURCE_VISIBILITY_PURIFICATION.md.

This checks the integer residual elimination and the finite omission-map
classification only. It is not a D2C graph enumerator.
"""
from collections import Counter
from itertools import product
from math import ceil


def M(n):
    return ((n - 1) ** 2) // 4 + 1


def phi(g):
    return g * (g - 1) if g >= 3 else 0


def brute_residual(B, y, D0):
    best = None
    for rho in range(y + 1):
        Emin = max(0, B - rho)
        for E in range(Emin, max(Emin, D0 - rho) + 2):
            q = max(0, ceil((D0 - rho - E) / 2))
            val = E + q
            if best is None or val < best:
                best = val
    return best


def closed_residual(B, y, D0):
    Ebase = max(0, B - y)
    Dbase = D0 - y
    return Ebase + ceil(max(0, Dbase - Ebase) / 2)


def audit_residual():
    checks = 0
    for B in range(70):
        for y in range(1, 15):
            for D0 in range(-10, 80):
                b = brute_residual(B, y, D0)
                f = closed_residual(B, y, D0)
                checks += 1
                if b != f:
                    return checks, {"B": B, "y": y, "D0": D0, "brute": b, "closed": f}
    return checks, None


def audit_omission_maps(max_k=5):
    qualifying = 0
    for k in range(1, max_k + 1):
        W = range(k + 1)
        H = range(k)
        for image in product(H, repeat=k + 1):
            good = []
            for o in W:
                vals = [image[w] for w in W if w != o]
                if len(set(vals)) == k:
                    good.append(o)
            if len(good) >= 2:
                qualifying += 1
                if len(good) != 2:
                    return qualifying, {"k": k, "image": image, "good_omissions": good}
                a, b = good
                if image[a] != image[b]:
                    return qualifying, {"k": k, "image": image, "good_omissions": good}
                other_vals = [image[w] for w in W if w not in good]
                if len(set(other_vals)) != k - 1 or image[a] in set(other_vals):
                    return qualifying, {"k": k, "image": image, "good_omissions": good}
    return qualifying, None


def scan(pmax=18, umax=18):
    stats = Counter()
    for p in range(3, pmax + 1):
        for u in range(1, umax + 1):
            b = 2 * p + u
            for lam in range(0, b - 3):
                a = b - lam - 1
                if a < 4:
                    continue
                n = 2 * b - lam
                DM = b * (n - b) - M(n)
                C0 = 2 * (DM - 1) + lam * (p + u) - p
                if C0 < 0:
                    continue
                T0 = a - p
                for x in range(3, a):
                    y = a - x
                    if max(0, x - p) > u:
                        continue
                    old = False
                    common = False
                    full_cap = False
                    full_visibility = False
                    for g in range(p + 1):
                        k = max(0, x - g)
                        if k <= 0 or k + 1 > u:
                            continue
                        A0 = phi(g)
                        g0 = x - T0
                        Eold = k * (p - 1) if g0 >= 1 else max(0, y * k - (1 - g0) * u)
                        if A0 + Eold <= C0:
                            old = True

                        Ecore = k * (p + k - 2)
                        if A0 + Ecore <= C0:
                            common = True

                        B = (k + 1) * (p + k - 1)
                        # Predecessor cap-only gate, included to measure the delta.
                        K = k * (k + 1) // 2
                        if A0 + max(0, B - y - min(K, y)) <= C0:
                            full_cap = True

                        # New graph-level full-support floor, minimized at h=0,u_+=0.
                        if max(A0, y * (p - g)) + max(0, B - y) <= C0:
                            full_visibility = True

                    if old:
                        stats["older_shared_floor_z1_possible"] += 1
                    if full_visibility:
                        stats["full_support_visibility_possible"] += 1
                    if common or full_cap:
                        stats["predecessor_cap_union"] += 1
                    if common or full_visibility:
                        stats["visibility_union"] += 1
    return stats


def main():
    residual_checks, residual_failure = audit_residual()
    omission_checks, omission_failure = audit_omission_maps()
    stats = scan()
    print({
        "residual_checks": residual_checks,
        "residual_failure": residual_failure,
        "omission_map_qualifying_checks": omission_checks,
        "omission_map_failure": omission_failure,
        "scan": dict(stats),
        "failures": int(residual_failure is not None) + int(omission_failure is not None),
        "trust_boundary": (
            "integer/combinatorial audit only; graph-level source-visibility theorem is hand-derived"
        ),
    })


if __name__ == "__main__":
    main()
