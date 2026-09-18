#!/usr/bin/env python3
"""Finite audit for A/U witness overlap capacity.

The proof in AU_WITNESS_OVERLAP_CAPACITY_AND_COMPLETE_CYLINDER_FEASIBILITY.md
is primary.  This checker exhausts small code-class bipartite source/witness
slack tables.  For fixed slacks it takes every eligible source/witness pair;
this maximizes the left side, so every subcollection is automatically covered.
"""

from itertools import product
import json

summary = {
    "weighted_code_class_cases": 0,
    "failures": 0,
}

for L in range(1, 4):
    for n_sources in range(4):
        for n_witnesses in range(4):
            for source_slacks in product(range(L + 1), repeat=n_sources):
                for witness_slacks in product(range(L + 1), repeat=n_witnesses):
                    summary["weighted_code_class_cases"] += 1

                    eligible = [
                        (i, j)
                        for i, e_source in enumerate(source_slacks)
                        for j, e_witness in enumerate(witness_slacks)
                        if e_source + e_witness >= L
                    ]

                    C = len(eligible)
                    rhs = (
                        n_witnesses * sum(source_slacks)
                        + n_sources * sum(witness_slacks)
                    )

                    # AUC1 and AUC3.
                    if C > n_sources * n_witnesses:
                        summary["failures"] += 1
                    if L * C > rhs:
                        summary["failures"] += 1

summary["total_checks"] = summary["weighted_code_class_cases"]

print(json.dumps(summary, indent=2, sort_keys=True))
