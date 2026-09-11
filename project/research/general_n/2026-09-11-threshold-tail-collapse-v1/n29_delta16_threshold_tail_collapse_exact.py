#!/usr/bin/env python3
"""Exact demand-only threshold-tail collapse for n=29, Delta=16.

This verifier uses only integer arithmetic after a one-time exact scaling of the
charging function. It exhausts every nondecreasing 12-tuple s_i in {0,...,11}.

Mathematical inputs from the graph-to-model bridge:
  * residual activity for t>0: rho_u >= 1;
  * threshold capacity:
        2 W_h <= z_h^2-z_h+h(h+1);
  * demand ledger: S >= r+2t;
  * residual tail identity:
        r = b + sum_{h=2}^a z_h.

For every demand vector the checker computes the smallest threshold-compatible
lower bound g_h(W_h) on z_h and proves exhaustively that

    Q(s) = S - sum_{h=2}^{11} g_h(W_h) <= 18.

Hence t>=2 would require Q(s)>=16+2t>=20, impossible.
"""
from __future__ import annotations

from argparse import ArgumentParser
from fractions import Fraction
from itertools import combinations_with_replacement
from math import comb
from pathlib import Path
import json

A = 12
B = 16
SCALE = 210


def charging_term(s: int) -> Fraction:
    if not 0 <= s <= A - 1:
        raise ValueError(s)
    return Fraction(s * (A + 1 - 2 * s), A - s)


CHARGE_SCALED = tuple(int(SCALE * charging_term(s)) for s in range(A))
assert CHARGE_SCALED == (
    0, 210, 378, 490, 525, 450, 210, -294, -1260, -3150, -7350, -20790
)


def zmin(W: int, h: int) -> int | None:
    """Smallest possible z_h permitted by threshold capacity."""
    if W == 0:
        return 0
    for z in range(h, B + 1):
        if 2 * W <= z * z - z + h * (h + 1):
            return z
    return None


def threshold_tail_score(s: tuple[int, ...]):
    S = sum(s)
    zmins = {}
    for h in range(2, A):
        W = sum(x for x in s if x >= h)
        if not W:
            continue
        z = zmin(W, h)
        if z is None:
            return None, None
        zmins[h] = z
    return S - sum(zmins.values()), zmins


def main() -> None:
    ap = ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    total = 0
    impossible = 0
    max_q = None
    extremals = []

    for s in combinations_with_replacement(range(A), A):
        total += 1
        q, zmins = threshold_tail_score(s)
        if q is None:
            impossible += 1
            continue

        if max_q is None or q > max_q:
            max_q = q
            extremals = [(s, zmins)]
        elif q == max_q:
            extremals.append((s, zmins))

    expected_extremals = {
        (2,) + (3,) * 11,
        (3,) * 12,
        (3,) + (4,) * 11,
        (4,) * 12,
    }

    got_extremals = {x[0] for x in extremals}
    expected_total = comb(2 * A - 1, A)

    checks = {
        "all_multisets": total == expected_total == 1_352_078,
        "threshold_incompatible_multisets": impossible == 67,
        "maximum_threshold_tail_score": max_q == 18,
        "extremals": got_extremals == expected_extremals,
    }
    status = "PASS" if all(checks.values()) else "FAIL"

    out = {
        "schema": "n29-delta16-threshold-tail-collapse-exact-v2",
        "status": status,
        "scope": {"n": 29, "Delta": 16, "a": A, "b": B},
        "arithmetic": "integer; charging table regression uses exact Fraction arithmetic scaled by 210",
        "solver_used": False,
        "floating_point_used": False,
        "all_nondecreasing_demand_multisets": total,
        "threshold_incompatible_multisets": impossible,
        "maximum_threshold_tail_score": max_q,
        "extremals": [
            {
                "s": list(s),
                "charging_scaled_210": sum(CHARGE_SCALED[x] for x in s),
                "threshold_tail_score": max_q,
                "zmin": {str(h): z for h, z in sorted(zmins.items())},
            }
            for s, zmins in sorted(extremals)
        ],
        "checks": checks,
        "conclusion": (
            "For every s in {0,...,11}^12 up to permutation, "
            "Q(s)=S-sum_h g_h(W_h)<=18. "
            "Any Delta=16 positive-surplus configuration with t>=2 would require "
            "Q(s)>=16+2t>=20, contradiction."
        ),
    }

    text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text, end="")
    if status != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
