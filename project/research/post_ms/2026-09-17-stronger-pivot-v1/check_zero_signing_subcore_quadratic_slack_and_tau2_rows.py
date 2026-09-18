#!/usr/bin/env python3
"""Regression for ZERO_SIGNING_SUBCORE_QUADRATIC_SLACK_AND_TAU2_ROWS.md.

Checks finite restricted-sphere bookkeeping and exact arithmetic equivalence.
It does not replace the D2C clique-private-foot/slack proof.
"""

from __future__ import annotations

import math


def singleton(j: int) -> int:
    return 1 << j


def cosingleton(s: int, j: int) -> int:
    return ((1 << s) - 1) ^ (1 << j)


def support_regression() -> tuple[int, int]:
    checks = 0
    minimum_margin = 10**9

    for s in range(3, 10):
        coords = list(range(s))
        for omitted_singleton in [-1, *coords]:
            singles = {
                singleton(j) for j in coords if j != omitted_singleton
            }
            for omitted_cosingleton in [-1, *coords]:
                cosingles = {
                    cosingleton(s, j)
                    for j in coords
                    if j != omitted_cosingleton
                }
                support = singles | cosingles

                for source in coords:
                    others = [j for j in coords if j != source]
                    for mask in range(1, 1 << len(others)):
                        targets = [
                            others[r]
                            for r in range(len(others))
                            if (mask >> r) & 1
                        ]
                        t = len(targets)

                        if t == 1:
                            margin = 0
                        else:
                            candidates = []
                            for j0 in targets:
                                if singleton(j0) not in support:
                                    continue
                                excluded = {singleton(j0)}
                                for k in targets:
                                    if k == j0:
                                        continue
                                    ck = cosingleton(s, k)
                                    if ck in support:
                                        excluded.add(ck)
                                candidates.append(len(excluded) - (t - 1))
                            assert candidates
                            margin = max(candidates)

                        assert margin >= 0
                        checks += 2  # Q and Q' are symmetric.
                        minimum_margin = min(minimum_margin, margin)

    return checks, minimum_margin


def arithmetic_regression() -> int:
    checks = 0

    # k=0,1,2 correspond to subcore sizes s=p, p-1, p-2.
    for k in (0, 1, 2):
        for p in range(max(3, k + 3), 101):
            s = p - k
            slack_floor = s * (s - 1)
            for u in range(1, 201):
                for lam in range(-1, min(u + 1, 20) + 1):
                    c_lam = math.ceil(lam * (lam + 2) / 2)
                    s_req = (
                        p * lam
                        + 3 * p
                        + u * lam
                        + 2 * u
                        - c_lam
                        - 2
                    )
                    direct = slack_floor >= s_req - 1
                    rhs = (
                        (p - k) * (p - k - 1)
                        - p * (lam + 3)
                        + c_lam
                        + 3
                    )
                    rearranged = (lam + 2) * u <= rhs
                    assert direct == rearranged
                    checks += 1

    return checks


def main() -> None:
    support_checks, minimum_margin = support_regression()
    arithmetic_checks = arithmetic_regression()
    print(
        {
            "support_checks": support_checks,
            "minimum_support_margin": minimum_margin,
            "support_failures": 0,
            "arithmetic_checks": arithmetic_checks,
            "arithmetic_failures": 0,
        }
    )


if __name__ == "__main__":
    main()
