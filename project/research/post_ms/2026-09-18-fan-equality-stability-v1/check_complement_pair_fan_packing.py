#!/usr/bin/env python3
"""Exact arithmetic audit for COMPLEMENT_PAIR_FAN_PACKING.md.

The graph-theoretic input is the already proved pair-local fan inequality.
This script checks the promoted pair-slack concentration consequence over a
large finite integer grid using exact arithmetic only.
"""

from collections import Counter


def main() -> None:
    counts = Counter()
    for lam_plus_one in range(1, 21):
        for pair_max_population in range(1, 51):
            for pair_slack in range(0, 101):
                edge_budget = (
                    pair_max_population * pair_slack // lam_plus_one
                )
                for t in range(-5, 21):
                    for d in range(1, 31):
                        j = d * (2 * d - t - 1)
                        if j <= pair_slack + 2 * edge_budget:
                            counts["primitive_feasible"] += 1
                            if j > 0:
                                assert (
                                    lam_plus_one * j
                                    <= (lam_plus_one + 2 * pair_max_population)
                                    * pair_slack
                                ), (
                                    "pair concentration regression",
                                    lam_plus_one,
                                    pair_max_population,
                                    pair_slack,
                                    t,
                                    d,
                                    edge_budget,
                                    j,
                                )
    print("COMPLEMENT_PAIR_FAN_PACKING_AUDIT_OK")
    print(f"primitive_feasible={counts['primitive_feasible']}")
    print("failures=0")


if __name__ == "__main__":
    main()
