#!/usr/bin/env python3
"""Independent exact arithmetic red-team for the N29 reviewer-v4 hand proof.

This script is intentionally small and separately specified. It does not import
project verifier modules. It checks:
  * the full 12-demand threshold-tail domain and max Q;
  * global monotonicity of every clipping map used in the hand proof;
  * threshold-capacity algebra over all finite parameter values in scope;
  * the Delta=15 witness-budget maxima quoted in the manuscript;
  * the Delta=17 pointwise bound;
  * the Delta=18..27 residual-h-index scalar contradictions at m=210.

All arithmetic is exact; no solver, floating point, or project certificate is used.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations_with_replacement
from math import comb
import json

A = 12
B = 16


def cap(h: int, z: int) -> int:
    return (z * (z - 1) + h * (h + 1)) // 2


def g(h: int, W: int) -> int | None:
    if W == 0:
        return 0
    for z in range(h, B + 1):
        if W <= cap(h, z):
            return z
    return None


def demand_D(s: tuple[int, ...]) -> int | None:
    total = 0
    for h in range(2, 12):
        W = sum(x for x in s if x >= h)
        gh = g(h, W)
        if gh is None:
            return None
        N = sum(x >= h for x in s)
        total += N - gh
    return total


def demand_Q(s: tuple[int, ...]) -> int | None:
    D = demand_D(s)
    if D is None:
        return None
    p = sum(x > 0 for x in s)
    return p + D


def clipped(s: tuple[int, ...], stage: str) -> tuple[int, ...]:
    if stage == "gt6_to6":
        return tuple(sorted(min(x, 6) for x in s))
    if stage == "6_to5":
        return tuple(sorted(5 if x == 6 else x for x in s))
    if stage == "5_to4":
        return tuple(sorted(4 if x == 5 else x for x in s))
    if stage == "4_to3":
        return tuple(sorted(3 if x == 4 else x for x in s))
    raise ValueError(stage)


def audit_demands() -> dict:
    total = comb(23, 12)
    compatible = 0
    incompatible = 0
    max_q = -10**9
    maximisers: list[tuple[int, ...]] = []

    # Full-domain exact check.
    for s in combinations_with_replacement(range(12), 12):
        q = demand_Q(s)
        if q is None:
            incompatible += 1
            continue
        compatible += 1
        if q > max_q:
            max_q = q
            maximisers = [s]
        elif q == max_q:
            maximisers.append(s)

    assert total == 1_352_078
    assert compatible + incompatible == total
    assert incompatible == 67
    assert max_q == 18
    expected = [
        (2,) + (3,) * 11,
        (3,) * 12,
        (3,) + (4,) * 11,
        (4,) * 12,
    ]
    assert maximisers == expected

    # Stronger-than-manuscript monotonicity sweep: check every compatible source
    # state in each bounded stage, not just the exceptional endpoint cases.
    clip_specs = [
        ("gt6_to6", range(12)),
        ("6_to5", range(7)),
        ("5_to4", range(6)),
        ("4_to3", range(5)),
    ]
    clip_report = {}
    for stage, values in clip_specs:
        checked = 0
        bad = 0
        for s in combinations_with_replacement(values, 12):
            D0 = demand_D(s)
            if D0 is None:
                continue
            t = clipped(s, stage)
            D1 = demand_D(t)
            assert D1 is not None
            checked += 1
            if D1 < D0:
                bad += 1
        assert bad == 0
        clip_report[stage] = {"checked": checked, "counterexamples": bad}

    return {
        "total_multisets": total,
        "threshold_compatible": compatible,
        "threshold_incompatible": incompatible,
        "max_Q": max_q,
        "maximisers": [list(x) for x in maximisers],
        "clipping": clip_report,
    }


def audit_threshold_algebra() -> dict:
    checked = 0
    for h in range(1, 13):
        for z in range(h, B + 1):
            q = z - h
            for j in range(0, z + 1):
                lhs = h * z + q * (q - 1) // 2
                rhs = (z - j) * h + j * z - j * (j + 1) // 2
                diff2 = (q - j) * (q - j - 1) // 2
                assert lhs - rhs == diff2
                assert diff2 >= 0
                checked += 1
    return {"integer_parameter_checks": checked, "status": "PASS"}


def witness_maxima(T: int) -> list[int]:
    vals = []
    for h in range(T // 2 + 1):
        o = min(29 - h, T - 2 * h)
        vals.append(h * (h - 1) // 2 + h * (29 - h) + o * (o - 1))
    return vals


def audit_delta15() -> dict:
    t13 = witness_maxima(13)
    t15 = witness_maxima(15)
    assert t13 == [156, 138, 127, 123, 126, 136, 153]
    assert t15 == [210, 184, 165, 153, 148, 150, 159, 175]
    assert t15[0] == 210 and all(x < 210 for x in t15[1:])
    return {"T13": t13, "T15": t15, "status": "PASS"}


def audit_delta17() -> dict:
    vals = []
    for s in range(0, 11):
        f = Fraction(s * (12 - 2 * s), 11 - s)
        vals.append((s, f))
        assert f <= Fraction(16, 7)
    mx = max(f for _, f in vals)
    arg = [s for s, f in vals if f == mx]
    assert mx == Fraction(16, 7)
    assert arg == [4]
    assert 11 * mx == Fraction(176, 7) < 29
    return {"max_term": str(mx), "argmax": arg, "eleven_label_max": str(11 * mx), "status": "PASS"}


def audit_hindex() -> dict:
    rows = []
    for b in range(18, 28):
        a = 28 - b
        t = 210 - b * (29 - b)
        lhs = b + 2 * t
        rhs = ((a + 1) ** 2) // 4
        assert t > 0
        assert lhs > rhs
        rows.append({"Delta": b, "a": a, "t_at_210": t, "lhs": lhs, "rhs": rhs})
    return {"rows": rows, "status": "PASS"}


def main() -> None:
    out = {
        "schema": "n29-reviewer-v4-independent-exact-redteam-v1",
        "status": "PASS",
        "arithmetic": "exact integer/rational",
        "solver_used": False,
        "floating_point_used": False,
        "demand_audit": audit_demands(),
        "threshold_capacity_algebra": audit_threshold_algebra(),
        "delta15_witness_budget": audit_delta15(),
        "delta17_pointwise": audit_delta17(),
        "delta18_27_hindex": audit_hindex(),
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
