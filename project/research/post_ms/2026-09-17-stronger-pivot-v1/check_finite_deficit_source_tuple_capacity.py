#!/usr/bin/env python3
"""Regression/audit support for FINITE_DEFICIT_SOURCE_TUPLE_CAPACITY_AND_RATIO_GAP.md.

The mathematical statements are hand proofs. This script only checks:
  * local r=3 designated-source Hamming geometry on a finite exact family;
  * the exact rational arithmetic behind the 27/14 ratio cutoff;
  * the sign/monotonicity polynomial data used in the note.
"""

from fractions import Fraction
from itertools import combinations, product


def bits(x, p):
    return tuple((x >> i) & 1 for i in range(p))


def local_triple_checks():
    checked = 0
    # Exhaust all centres, target sets with deficit k<=2, assigned triples,
    # and all outside-target bits for the three designated sources, p<=6.
    for p in range(3, 7):
        for centre_int in range(1 << p):
            c = bits(centre_int, p)
            for k in range(0, min(2, p - 3) + 1):
                for missing in combinations(range(p), k):
                    missing = set(missing)
                    I = [i for i in range(p) if i not in missing]
                    for assigned in combinations(I, 3):
                        outside = sorted(missing)
                        for outside_bits in product((0, 1), repeat=3 * len(outside)):
                            src = [list(c) for _ in range(3)]
                            for j, i in enumerate(assigned):
                                src[j][i] ^= 1
                            pos = 0
                            for j in range(3):
                                for i in outside:
                                    src[j][i] = outside_bits[pos]
                                    pos += 1

                            # On every target coordinate other than its own assigned
                            # coordinate, each source agrees with the centre.
                            for j, i in enumerate(assigned):
                                for h in I:
                                    want = c[h] ^ (1 if h == i else 0)
                                    assert src[j][h] == want

                            # T = number of nonconstant coordinates of the triple.
                            T = 0
                            singleton = [0, 0, 0]
                            for h in range(p):
                                vals = [src[j][h] for j in range(3)]
                                if not (vals[0] == vals[1] == vals[2]):
                                    T += 1
                                    for j in range(3):
                                        others = [vals[t] for t in range(3) if t != j]
                                        if others[0] == others[1] and vals[j] != others[0]:
                                            singleton[j] += 1
                            assert T <= k + 3
                            assert all(singleton[j] >= 1 for j in range(3))
                            assert min(singleton) * 3 <= T
                            checked += 1
    return checked


def F_pair(rho):
    gamma = rho * (2 - rho)
    L0 = (rho - (rho + 2) * gamma) / (1 - gamma)
    D0 = rho * (2 - rho) / (rho - 1)
    return L0 - 7 * D0 - Fraction(7, 36) * rho * rho


def F_triple(rho):
    gamma = rho * (2 - rho)
    L0 = (rho - (rho + 2) * gamma) / (1 - gamma)
    D0 = rho * (2 - rho) / (rho - 1)
    return L0 - 6 * D0 - Fraction(12, 125) * rho ** 3


def P(rho):
    return 12 * rho ** 4 - 24 * rho ** 3 - 863 * rho ** 2 + 2250 * rho - 1125


def Pprime(rho):
    return 48 * rho ** 3 - 72 * rho ** 2 - 1726 * rho + 2250


def Psecond(rho):
    return 144 * rho ** 2 - 144 * rho - 1726


def arithmetic_checks():
    rho0 = Fraction(27, 14)
    assert F_triple(rho0) == Fraction(219672, 7245875)
    assert F_triple(rho0) > 0
    assert P(rho0) == Fraction(-4068, 2401)
    assert P(rho0) < 0
    assert Pprime(rho0) < 0
    # P'' is increasing for rho>1/2, so its maximum on [rho0,2] is at 2.
    assert Psecond(Fraction(2, 1)) < 0
    # Exact dense rational grid as a regression on F>0 over [27/14,2].
    grid = 0
    lo = rho0
    hi = Fraction(2, 1)
    for j in range(2001):
        rho = lo + (hi - lo) * Fraction(j, 2000)
        assert F_triple(rho) > 0
        grid += 1
    return grid


def main():
    local = local_triple_checks()
    grid = arithmetic_checks()
    print({
        "status": "ok",
        "local_triple_geometry_cases": local,
        "ratio_grid_points": grid,
        "rho_cutoff": "27/14",
        "rho_cutoff_decimal": float(Fraction(27, 14)),
        "F_at_cutoff": str(F_triple(Fraction(27, 14))),
    })


if __name__ == "__main__":
    main()
