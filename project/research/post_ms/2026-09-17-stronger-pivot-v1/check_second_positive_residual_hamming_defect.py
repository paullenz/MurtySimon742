#!/usr/bin/env python3
"""Finite arithmetic regression for SECOND_POSITIVE_RESIDUAL_HAMMING_DEFECT.md.

Evidence only. The universal statements are proved by hand in the companion note.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "SECOND_POSITIVE_RESIDUAL_HAMMING_CHECK_SUMMARY.json"


def M(n: int) -> int:
    return ((n - 1) ** 2) // 4 + 1


def main() -> None:
    failures = []
    pointwise_records = 0

    for k in range(17, 5001):
        coeff = 15 / 4 if k in (17, 18) else k / 5

        # Once 2^R-1 >= k, g_k(R)=k forever, so checking a little past
        # ceil(log2(k+1)) covers every change of the pointwise envelope.
        rmax = math.ceil(math.log2(k + 1)) + 2
        for R in range(rmax + 1):
            g = min(k, (1 << R) - 1)
            pointwise_records += 1
            if g > coeff * R + 1e-12:
                failures.append(
                    {
                        "kind": "pointwise_majorant",
                        "k": k,
                        "R": R,
                        "g": g,
                        "rhs": coeff * R,
                    }
                )
                break
        if failures:
            break

        if k in (17, 18):
            f_bound = math.floor(15 * k / 4)
        else:
            f_bound = math.floor(k * k / 5)

        m_bound = 2 * k * k + 2 * k + f_bound
        target = M(3 * k + 2)
        if not m_bound < target:
            failures.append(
                {
                    "kind": "second_extremal_comparison",
                    "k": k,
                    "m_bound": m_bound,
                    "M": target,
                    "f_bound": f_bound,
                }
            )
            break

    summary = {
        "status": (
            "PASS_SECOND_POSITIVE_RESIDUAL_HAMMING_DEFECT"
            if not failures
            else "FAIL_SECOND_POSITIVE_RESIDUAL_HAMMING_DEFECT"
        ),
        "date": "2026-09-17",
        "scope": "finite arithmetic regression only; Hamming-degree and second-extremal statements are hand proofs",
        "k_range_checked": [17, 5000],
        "k_values_checked": 5000 - 17 + 1,
        "pointwise_majorant_records": pointwise_records,
        "boundary_values": {
            "k17": {"f_bound": 63, "m_bound": 675, "M": M(53)},
            "k18": {"f_bound": 67, "m_bound": 751, "M": M(56)},
        },
        "failures": failures,
        "negative_controls": {
            "k4_X3": "outside theorem scope; residual-zero 12/32 hostile control remains allowed",
            "k2_H5": "outside theorem scope; classical six-vertex boundary remains allowed",
        },
    }

    OUT.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(summary["status"])
    print(json.dumps(summary, indent=2))

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
