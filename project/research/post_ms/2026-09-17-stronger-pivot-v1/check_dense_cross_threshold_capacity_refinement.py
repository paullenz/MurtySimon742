#!/usr/bin/env python3
"""Audit arithmetic for DENSE_CROSS_THRESHOLD_CAPACITY_REFINEMENT.md.

Finite regression only; the theorem is proved by the hand inequalities in the
note.
"""

from fractions import Fraction
import json


def G(r):
    return (
        r * (125 * r**3 - 675 * r**2 + 595 * r + 567)
        / (10 * (25 * r**2 - 100 * r + 49))
    )


def N(r):
    return 125 * r**3 - 675 * r**2 + 595 * r + 567


def Nprime(r):
    return 5 * (75 * r**2 - 270 * r + 119)


r0 = Fraction(31, 8)
summary = {
    "ratio_endpoint": str(r0),
    "G_at_endpoint": str(G(r0)),
    "N_at_endpoint": str(N(r0)),
    "Nprime_at_endpoint": str(Nprime(r0)),
    "threshold_theta": "7/5",
    "threshold_capacity_integer_cases": 0,
    "failures": [],
}

if G(r0) != Fraction(54343, 503680):
    summary["failures"].append("G endpoint mismatch")
if N(r0) != Fraction(5259, 512):
    summary["failures"].append("N endpoint mismatch")
if Nprime(r0) <= 0 or Nprime(Fraction(4, 1)) <= 0:
    summary["failures"].append("N monotonicity endpoint failure")

# Pure integer capacity inequality behind (1.6)--(1.9).
# For arbitrary beta loads ell_x in [0,p], set J=j and L={ell_x>j};
# verify B <= |L|p+(a-|L|)j and the consequent lower bound on |L|.
for p in range(2, 9):
    for a in range(1, 8):
        for j in range(0, p):
            # Test representative load vectors exhaustively for a<=4 and a
            # deterministic extremal family for larger a.
            vectors = []
            if a <= 4:
                from itertools import product
                vectors = product(range(p + 1), repeat=a)
            else:
                vectors = [
                    tuple([0] * a),
                    tuple([j] * a),
                    tuple([p] * a),
                    tuple(([p, j] * ((a + 1) // 2))[:a]),
                ]
            for loads in vectors:
                B = sum(loads)
                L = sum(e > j for e in loads)
                summary["threshold_capacity_integer_cases"] += 1
                if B > L * p + (a - L) * j:
                    summary["failures"].append(
                        {"kind": "capacity", "p": p, "a": a, "j": j,
                         "loads": list(loads)}
                    )
                if B > a * j:
                    lower = Fraction(B - a * j, p - j)
                    if L < lower:
                        summary["failures"].append(
                            {"kind": "lower-bound", "p": p, "a": a,
                             "j": j, "loads": list(loads),
                             "lower": str(lower), "L": L}
                        )

summary["status"] = "PASS" if not summary["failures"] else "FAIL"
print(json.dumps(summary, indent=2, sort_keys=True))
if summary["failures"]:
    raise SystemExit(1)
