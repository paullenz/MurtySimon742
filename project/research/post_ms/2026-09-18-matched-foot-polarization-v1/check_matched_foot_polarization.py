#!/usr/bin/env python3
"""Finite algebra audit for matched-foot polarization/self-pricing.

The hand proofs in MATCHED_FOOT_POLARIZATION_SELF_PRICING_AND_CYLINDER_SPILL.md
are primary.  This checker only exhausts small integer instances of the new
algebraic reductions.
"""

from itertools import product
from math import ceil, floor, sqrt
import json

summary = {
    "paired_slack_cases": 0,
    "complement_pair_capacity_cases": 0,
    "self_pricing_cases": 0,
    "inverse_live_cap_cases": 0,
    "failures": 0,
}

# PT1: t0*e1+t1*e0 >= L*min(t0,t1), with e0+e1=L.
for L in range(1, 9):
    for e0 in range(L + 1):
        e1 = L - e0
        for t0 in range(9):
            for t1 in range(9):
                summary["paired_slack_cases"] += 1
                if t0 * e1 + t1 * e0 < L * min(t0, t1):
                    summary["failures"] += 1

# CP4: for one complementary gamma pair on g fibres,
# total traffic <= g*max(n0,n1)+sum min(t0_i,t1_i).
for g in range(1, 4):
    for n0 in range(4):
        for n1 in range(4):
            choices = [
                (t0, t1)
                for t0 in range(n0 + 1)
                for t1 in range(n1 + 1)
            ]
            for loads in product(choices, repeat=g):
                summary["complement_pair_capacity_cases"] += 1
                M = sum(t0 + t1 for t0, t1 in loads)
                paired = sum(min(t0, t1) for t0, t1 in loads)
                if M > g * max(n0, n1) + paired:
                    summary["failures"] += 1

# MSP1 counting step: if M <= mu*a then ceil(M/a) <= mu.
for a in range(1, 21):
    for mu in range(1, 11):
        for M in range(mu * a + 1):
            summary["self_pricing_cases"] += 1
            if ceil(M / a) > mu:
                summary["failures"] += 1

# MSP2 inverse live cap.  For mu>=3, only instances satisfying the
# zero-signed payment LA>=mu(mu-1) are admissible.
for LA in range(101):
    R_A = max(2, floor((1 + sqrt(1 + 4 * LA)) / 2))
    for mu in range(1, 21):
        if mu <= 2 or LA >= mu * (mu - 1):
            summary["inverse_live_cap_cases"] += 1
            if mu > R_A:
                summary["failures"] += 1

summary["total_checks"] = sum(
    value for key, value in summary.items() if key != "failures"
)

print(json.dumps(summary, indent=2, sort_keys=True))
