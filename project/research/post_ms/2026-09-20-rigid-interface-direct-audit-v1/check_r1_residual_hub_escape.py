#!/usr/bin/env python3
"""Arithmetic replay for ONE_CODE_R1_RESIDUAL_HUB_CRITICALITY.md.

Diagnostic only. The structural theorem is the hand proof; this script checks the
closed-form specialization on the exact residual-one escape family.
"""

from math import ceil


def row(t: int):
    assert t >= 2
    c = p = 2 * t
    y = 1
    g0 = 2 * t - 1
    lam = 4 * t - 2
    u = x = 3 * t
    k = t + 1
    d = c - 1

    # RH-LXINT, first branch of the max (it dominates on this ray).
    lx = 8 * t * t - 3 * t + 2 * ceil((t + 1) / 2)
    ew = k * (p + k - 2)
    c0 = 12 * t * t + 6 * t - 4

    score_margin = c0 - (lx + ew)

    lhs_q = k * (x + y - 1) + lx
    rhs_q = u * (p - lam) + 2 * d * u - d * (d + 1) + c0
    q_margin = rhs_q - lhs_q

    # Closed forms from the note.
    assert ew == 3 * t * t + 2 * t - 1
    assert score_margin == t * t + 7 * t - 3 - 2 * ceil((t + 1) / 2)
    assert q_margin == 3 * t * t + 8 * t - 4 - 2 * ceil((t + 1) / 2)
    assert score_margin > 0
    assert q_margin > 0

    return {
        "t": t,
        "n": 10 * t + 2,
        "L_X_floor": lx,
        "E_W_floor": ew,
        "score_margin": score_margin,
        "rooted_Q_margin": q_margin,
    }


def main():
    rows = [row(t) for t in range(2, 1001)]
    print("checked", len(rows), "escape-ray rows")
    print("first", rows[0])
    print("last", rows[-1])


if __name__ == "__main__":
    main()
