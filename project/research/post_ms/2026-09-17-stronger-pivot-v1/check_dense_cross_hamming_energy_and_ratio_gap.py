#!/usr/bin/env python3
"""Regression checks for DENSE_CROSS_HAMMING_ENERGY_AND_RATIO_GAP.md.

These checks are audit support only.  The mathematical claims in the note rest
on the hand injections and counts, not on finite computation.
"""

from fractions import Fraction
from itertools import product
import json


def hamming_energy(codes):
    p = len(codes[0])
    u = len(codes)
    direct = 0
    for r, x in enumerate(codes):
        for s, y in enumerate(codes):
            if r != s:
                direct += sum(a != b for a, b in zip(x, y))

    H = 0
    for i in range(p):
        u0 = sum(x[i] == 0 for x in codes)
        u1 = u - u0
        H += (u0 - u1) ** 2

    formula = Fraction(p * u * u, 2) - Fraction(H, 2)
    return direct, formula


def F(r):
    return r * (64 * r**3 - 208 * r**2 - 252 * r + 315) / 200


def Fprime(r):
    return (256 * r**3 - 624 * r**2 - 504 * r + 315) / 200


def Fsecond(r):
    return 3 * (32 * r**2 - 52 * r - 21) / 25


summary = {
    "hamming_code_multisets_checked": 0,
    "product_identity_cases_checked": 0,
    "dense_cross_algebra_cases_checked": 0,
    "failures": [],
}

# Exact Hamming-energy identity on all ordered U-code multisets with
# p<=4 and u<=3.
for p in range(1, 5):
    cube = list(product((0, 1), repeat=p))
    for u in range(1, 4):
        for idx in product(range(len(cube)), repeat=u):
            codes = [cube[i] for i in idx]
            direct, formula = hamming_energy(codes)
            summary["hamming_code_multisets_checked"] += 1
            if direct != formula:
                summary["failures"].append(
                    {"kind": "hamming", "p": p, "u": u, "codes": codes,
                     "direct": direct, "formula": str(formula)}
                )

# Exact per-A-vertex product identity and its nonnegative relaxation.
for p in range(1, 8):
    for u in range(1, 10):
        for ell in range(p + 1):
            for c in range(u + 1):
                Z = (p - ell) * (u - c)
                lhs = ell * c
                rhs = u * ell + p * c - p * u + Z
                summary["product_identity_cases_checked"] += 1
                if lhs != rhs or lhs < u * ell + p * c - p * u:
                    summary["failures"].append(
                        {"kind": "product", "p": p, "u": u,
                         "ell": ell, "c": c}
                    )

# Exact simplification from (3.3) to (3.6), over a broad finite box.
for p in range(1, 8):
    for u in range(1, 10):
        for lam in range(-2, 4):
            a = 2 * p + u - lam - 1
            if a < 0:
                continue
            for h_alpha in range(0, min(p * u, 5) + 1):
                B = p * u - h_alpha
                for q in range(0, min(u * (u - 1) // 2, 4) + 1):
                    for E_U in range(0, 5):
                        s = u * (p + u - 1) - 2 * q - E_U
                        for Z in range(0, 4):
                            lhs = (u - p) * B + p * s - p * u * a + Z
                            rhs = (
                                p * u * (u - 2 * p + lam)
                                - (u - p) * h_alpha
                                - 2 * p * q
                                - p * E_U
                                + Z
                            )
                            summary["dense_cross_algebra_cases_checked"] += 1
                            if lhs != rhs:
                                summary["failures"].append(
                                    {"kind": "algebra", "p": p, "u": u,
                                     "lambda": lam, "h_alpha": h_alpha,
                                     "q": q, "E_U": E_U, "Z": Z}
                                )

# Exact endpoint/margin used in the 63/16 ratio gap.
r0 = Fraction(63, 16)
summary["ratio_endpoint"] = str(r0)
summary["F_at_endpoint"] = str(F(r0))
summary["Fprime_at_endpoint"] = str(Fprime(r0))
summary["Fsecond_at_endpoint"] = str(Fsecond(r0))
summary["expected_F_at_endpoint"] = "3969/40960"

if F(r0) != Fraction(3969, 40960):
    summary["failures"].append({"kind": "ratio-endpoint"})
if Fprime(r0) <= 0 or Fsecond(r0) <= 0:
    summary["failures"].append({"kind": "ratio-monotonicity-endpoint"})
if Fsecond(Fraction(4, 1)) <= 0:
    summary["failures"].append({"kind": "ratio-convexity-right-end"})

summary["status"] = "PASS" if not summary["failures"] else "FAIL"
print(json.dumps(summary, indent=2, sort_keys=True, default=str))

if summary["failures"]:
    raise SystemExit(1)
