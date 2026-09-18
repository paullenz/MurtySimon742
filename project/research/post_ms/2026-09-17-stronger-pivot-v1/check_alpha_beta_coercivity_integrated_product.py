#!/usr/bin/env python3
from fractions import Fraction
from math import comb, floor, ceil, sqrt
import itertools


def audit_fibre_coercivity():
    cases = 0
    for u in range(17):
        for u0 in range(u + 1):
            u1 = u - u0
            m = min(u0, u1)
            for h0 in range(u0 + 1):
                for h1 in range(u1 + 1):
                    h = h0 + h1
                    P = h0 * (u1 + 1) + h1 * (u0 + 1)
                    for lam in range(8):
                        for e0 in range(lam + 2):
                            e1 = lam + 1 - e0
                            r0 = u0 - h0
                            r1 = u1 - h1
                            T = r0 * e1 + r1 * e0
                            cases += 1
                            assert P >= (m + 1) * h
                            assert T >= (lam + 1) * max(0, m - h)
                            assert (Fraction(P, 1)
                                    + Fraction(m + 1, lam + 1) * T
                                    >= m * (m + 1))
    return cases


def audit_hamming_rhs():
    cases = 0
    for p in range(1, 6):
        for u in range(8):
            for u0s in itertools.product(range(u + 1), repeat=p):
                ds = [2 * u0 - u for u0 in u0s]
                ms = [min(u0, u - u0) for u0 in u0s]
                H = sum(d * d for d in ds)
                S = sum(m * (m + 1) for m in ms)
                exact = (Fraction(p * u * u, 4)
                         + Fraction(p * u, 2)
                         + Fraction(H, 4)
                         - Fraction(u + 1, 2) * sum(abs(d) for d in ds))
                assert S == exact
                z = u - sqrt(H / p)
                assert S + 1e-10 >= p * z * (z + 2) / 4
                cases += 1
    return cases


def caphat(p, u, r, K):
    return floor(Fraction(K + r, r)
                 * Fraction(comb(u, r), comb(p - K, r)))


def Phi(p, u, r, N):
    return sum(max(0, N - caphat(p, u, r, K))
               for K in range(p - r + 1))


def audit_tail_integration():
    cases = 0
    for p in range(3, 8):
        for u in range(3, min(2 * p, 8) + 1):
            for r in range(3, min(p, u, 4) + 1):
                for a in range(1, 6):
                    for ks in itertools.combinations_with_replacement(
                            range(p + 1), a):
                        if any(sum(k <= K for k in ks)
                               > caphat(p, u, r, K)
                               for K in range(p - r + 1)):
                            continue
                        pref = 0
                        for N in range(1, a + 1):
                            pref += ks[N - 1]
                            assert pref >= Phi(p, u, r, N)
                            cases += 1
    return cases


def audit_load_threshold():
    cases = 0
    for p in range(2, 7):
        for a in range(1, 6):
            for ells in itertools.product(range(p + 1), repeat=a):
                B = sum(ells)
                for j in range(p):
                    actual = sum(ell > j for ell in ells)
                    lower = max(0, ceil(Fraction(B - a * j, p - j)))
                    assert actual >= lower
                    cases += 1
    return cases


def audit_cylinder_bookkeeping():
    # Abstract integer replay of the exact degree/cylinder count.
    cases = 0
    for p in range(2, 15):
        for u in range(15):
            for ell in range(1, p + 1):
                k = p - ell
                for eps in range(0, 2 * p + u + 1):
                    for dU in range(ell, u + 1):
                        dA = p + u - eps - dU
                        if dA < 0:
                            continue
                        centralU = dU - ell
                        centralTotal = dA + centralU
                        assert centralTotal == u + k - eps
                        assert dA >= p - eps
                        cases += 1
    return cases


if __name__ == "__main__":
    out = {
        "fibre_coercivity_cases": audit_fibre_coercivity(),
        "hamming_rhs_cases": audit_hamming_rhs(),
        "tail_integration_cases": audit_tail_integration(),
        "load_threshold_cases": audit_load_threshold(),
        "cylinder_bookkeeping_cases": audit_cylinder_bookkeeping(),
    }
    out["total_cases"] = sum(out.values())
    print(out)
