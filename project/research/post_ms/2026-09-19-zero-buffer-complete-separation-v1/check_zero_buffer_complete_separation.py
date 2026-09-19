#!/usr/bin/env python3
"""Arithmetic audit for ZERO_BUFFER_COMPLETE_SEPARATION_AND_CLOSURE.md.

Hand criticality proofs are primary. This script checks only the score-gap
identity and a bounded integer diagnostic over the theorem's parameter domain.
It is not a graph-realizability proof.
"""

import json

summary = {
    "identity_checks": 0,
    "bounded_states": 0,
    "nonpositive_gaps": 0,
    "minimum_gap": None,
    "minimum_gap_state": None,
}

for p in range(4, 21):
    for rho in range(p + 2, 31):
        for k in range(1, 16):
            u = k + rho
            x = p + k
            for lam in range(0, p + rho - 1):
                y = p + rho - lam - 1
                assert y >= 1
                H = ((lam + 1) ** 2) // 4

                S = (
                    (u - 1) * (p + u - 2)
                    + rho * y
                    + x * lam
                    + k * (x - 1)
                )
                C0 = (lam + 3) * p + (lam + 2) * u - 2 * H - 4

                bracket = (
                    H
                    + (k - 1) * (k + p + rho - 2)
                    + (rho - p - 2)
                    + rho * (y - 2)
                    + 3
                )
                gap = S - C0
                assert gap == 2 * bracket
                summary["identity_checks"] += 1
                summary["bounded_states"] += 1

                if gap <= 0:
                    summary["nonpositive_gaps"] += 1

                if summary["minimum_gap"] is None or gap < summary["minimum_gap"]:
                    summary["minimum_gap"] = gap
                    summary["minimum_gap_state"] = {
                        "p": p,
                        "rho": rho,
                        "k": k,
                        "lambda": lam,
                        "y": y,
                        "H_lambda": H,
                    }

assert summary["nonpositive_gaps"] == 0
print(json.dumps(summary, indent=2, sort_keys=True))
