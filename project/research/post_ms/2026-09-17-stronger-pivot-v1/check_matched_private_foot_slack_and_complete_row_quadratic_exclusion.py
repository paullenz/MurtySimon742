#!/usr/bin/env python3
"""Regression for MATCHED_PRIVATE_FOOT_SLACK_AND_COMPLETE_ROW_QUADRATIC_EXCLUSION.md.

This checks only finite Boolean-support bookkeeping and arithmetic rearrangement.
It does not prove the D2C private-foot lemmas.
"""

from __future__ import annotations

import math


def singleton(j: int) -> int:
    return 1 << j


def cosingleton(p: int, j: int) -> int:
    return ((1 << p) - 1) ^ (1 << j)


def support_exclusion_regression() -> tuple[int, int]:
    checks = 0
    minimum_margin = 10**9

    for p in range(3, 11):
        coords = list(range(p))
        for omitted_singleton in [-1, *coords]:
            singles = {
                singleton(j) for j in coords if j != omitted_singleton
            }
            for omitted_cosingleton in [-1, *coords]:
                cosingles = {
                    cosingleton(p, j)
                    for j in coords
                    if j != omitted_cosingleton
                }
                support = singles | cosingles

                # Q side: source feet are co-singletons.  For |T|>=2 choose
                # a realised singleton base j0 and count t-1 realised support
                # codes in H^1_{j0}\H^1_T.
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
                                    if (
                                        k != j0
                                        and cosingleton(p, k) in support
                                    ):
                                        excluded.add(cosingleton(p, k))
                                candidates.append(len(excluded) - (t - 1))
                            assert candidates
                            margin = max(candidates)
                        assert margin >= 0
                        checks += 1
                        minimum_margin = min(minimum_margin, margin)

                # Q' side: symmetric, with a realised co-singleton base and
                # singleton exclusions for the remaining targets.
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
                                if cosingleton(p, j0) not in support:
                                    continue
                                excluded = {cosingleton(p, j0)}
                                for k in targets:
                                    if k != j0 and singleton(k) in support:
                                        excluded.add(singleton(k))
                                candidates.append(len(excluded) - (t - 1))
                            assert candidates
                            margin = max(candidates)
                        assert margin >= 0
                        checks += 1
                        minimum_margin = min(minimum_margin, margin)

    return checks, minimum_margin


def arithmetic_regression() -> int:
    checks = 0
    for p in range(3, 101):
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
                direct = p * (p - 1) >= s_req - 1
                rearranged = (
                    (lam + 2) * u
                    <= p * p - (lam + 4) * p + c_lam + 3
                )
                assert direct == rearranged
                checks += 1
    return checks


def main() -> None:
    support_checks, minimum_margin = support_exclusion_regression()
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
