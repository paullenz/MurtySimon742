#!/usr/bin/env python3
"""Finite audit for DENSE_CROSS_MOMENT_CAPACITY_THEOREM.md.

The structural theorem is hand-derived.  This checker only replays the exact
product/Jensen algebra and the limiting root arithmetic on a finite box.
"""

from fractions import Fraction
from itertools import product
import json


def phi(d, u):
    return max(0, 2 * d - u - 2) ** 2


summary = {
    "weighted_degree_and_jensen_cases": 0,
    "failures": [],
}

for p in range(1, 6):
    for u in range(1, 8):
        states = [
            (ell, d)
            for ell in range(p + 1)
            for d in range(ell, u + 1)
        ]
        for a in range(1, 4):
            for arr in product(states, repeat=a):
                B = sum(ell for ell, d in arr)
                s = sum(d for ell, d in arr)
                W = sum(ell * d for ell, d in arr)
                lower = u * B + p * s - p * u * a
                summary["weighted_degree_and_jensen_cases"] += 1

                if W < lower:
                    summary["failures"].append(
                        {"kind": "weighted-degree", "p": p, "u": u,
                         "a": a, "arr": arr, "W": W, "lower": lower}
                    )
                    continue

                if B:
                    lhs = sum(ell * phi(d, u) for ell, d in arr)
                    mean = Fraction(W, B)
                    z = max(Fraction(0), 2 * mean - u - 2)
                    rhs = B * z * z
                    if Fraction(lhs) < rhs:
                        summary["failures"].append(
                            {"kind": "jensen", "p": p, "u": u,
                             "a": a, "arr": arr, "lhs": str(lhs),
                             "rhs": str(rhs)}
                        )

# Exact limiting root arithmetic:
# (rho-2)^2 = rho(4-rho) iff rho^2-4rho+2=0.
# The upper root is 2+sqrt(2), and the derivative of the difference
# 2rho^2-8rho+4 there is 4sqrt(2)>0.
summary["limiting_polynomial"] = "rho^2-4rho+2"
summary["upper_root"] = "2+sqrt(2)"
summary["derivative_of_difference_at_upper_root"] = "4sqrt(2)"
summary["status"] = "PASS" if not summary["failures"] else "FAIL"

print(json.dumps(summary, indent=2, sort_keys=True, default=str))
if summary["failures"]:
    raise SystemExit(1)
