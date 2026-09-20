#!/usr/bin/env python3
"""Independent diagnostic checks for the 20 Sep two-X-hole eventual closure.

This script is NOT proof evidence.  It checks the exact algebraic identities and
integer inequalities used by:
  * TWO_X_HOLE_HOLE_CLASS_FORWARD_SURCHARGE.md
  * TWO_X_HOLE_BOUNDED_HOLE_RESOURCE_CLOSURE.md
  * TWO_X_HOLE_EVENTUAL_X16_CLOSURE.md
  * TWO_X_HOLE_FINITE_ORDER_BOUND.md

All theorem conclusions remain hand/analytic statements.
"""

from fractions import Fraction


def check_class_net():
    rows = 0
    for m in range(1, 101):
        for s in range(1, 101):
            if m * s > m + 2 * s:
                continue
            rows += 1
            F = max(0, m * s - 2 * s)
            assert F <= m
            assert 11 * m - 8 * F <= 3 * m + 16
    return rows


def phi0(x, p, w, y, eps, L):
    return (
        8 * L
        - 2 * eps
        + 3 * p * p
        + 2 * p * w
        - 3 * p * y
        - 8 * p
        + w * w
        - 4 * w * x
        + w * y
        - 8 * w
        + 5 * x * x
        - 3 * x * y
        - 10 * x
        + 2 * y * y
        + 4 * y
        + 20
    )


def nprime(x, p, w, M):
    return (
        64 * M
        + 15 * p * p
        + 22 * p * w
        - 18 * p * x
        - 40 * p
        + 7 * w * w
        - 26 * w * x
        - 96 * w
        + 31 * x * x
        - 56 * x
        + 128
    )


def check_square_identity():
    rows = 0
    minimum_gap = None
    minimizer = None
    for x in range(4, 41):
        for p in range(1, 31):
            for w in range(1, 61):
                L = max(x - 2, w)
                # lambda=2p+w-y >= 0
                for y in range(2, min(2 * p + w, 70) + 1):
                    rows += 1
                    # 8*(Phi0-3w) = 16(y-y*)^2 + N'
                    # use 4(y-y*) = 4y-3p+w-3x+4 to stay integral
                    t = 4 * y - 3 * p + w - 3 * x + 4
                    lhs8 = 8 * (phi0(x, p, w, y, 1, L) - 3 * w)
                    rhs8 = t * t + nprime(x, p, w, L)
                    assert lhs8 == rhs8
                    if x >= 16:
                        gap = phi0(x, p, w, y, 1, L) - 3 * w
                        if minimum_gap is None or gap < minimum_gap:
                            minimum_gap = gap
                            minimizer = (x, p, w, y, gap)
    assert minimum_gap is not None and minimum_gap > 32
    return rows, minimum_gap, minimizer


def check_quadratic_floor():
    rows = 0
    worst = None
    for p in range(1, 101):
        for w in range(1, 101):
            for y in range(0, 201):
                rows += 1
                Q = 3*p*p + 2*p*w - 3*p*y + w*w + w*y + 2*y*y
                # 8Q >= 7(p+w)^2
                slack = 8*Q - 7*(p+w)*(p+w)
                assert slack >= 0
                if worst is None or slack < worst[0]:
                    worst = (slack, p, w, y)
    return rows, worst


def check_tail_bound():
    # From 7S^2/8 - 10xS <= 22S and S>0.
    # Verify the integer consequence S<=196 for 4<=x<=15.
    allowed = []
    for x in range(4, 16):
        max_s = 0
        for S in range(1, 500):
            if 7*S*S <= 8*(10*x+22)*S:
                max_s = S
        allowed.append((x, max_s))
    assert max(s for _, s in allowed) == 196
    # n<=2x+y+2p+w+2, y<=2p+w, p+w=S -> n<=2x+4S+2.
    assert 2*15 + 4*196 + 2 == 816
    return allowed


def main():
    crows = check_class_net()
    srows, mingap, minimizer = check_square_identity()
    qrows, qworst = check_quadratic_floor()
    tail = check_tail_bound()
    print({
        "class_route_rows": crows,
        "square_identity_rows": srows,
        "x_ge_16_min_sample_gap_Phi_minus_3omega": mingap,
        "x_ge_16_sample_minimizer": minimizer,
        "quadratic_floor_rows": qrows,
        "quadratic_floor_worst": qworst,
        "tail_max_S_by_x": tail,
        "derived_order_cap": 816,
    })


if __name__ == "__main__":
    main()
