#!/usr/bin/env python3
"""Audit-only arithmetic replay for ONE_CODE_NEAR_RIGID_WITNESS_CLASS_CROWDING.md.

This does not enumerate D2C graphs.  It independently checks the parity algebra
in the c=0 finite-order theorem and measures the effect of the new physical
witness-class E_U floor on a broad abstract near-rigid parameter box.
"""

from math import floor


def M(n: int) -> int:
    return ((n - 1) * (n - 1)) // 4 + 1


def c0_score_ceiling(p: int, u: int, lam: int) -> int:
    b = 2 * p + u
    n = 2 * b - lam
    D_M = b * (n - b) - M(n)
    return 2 * (D_M - 1) + lam * (p + u) - p


def phi(m: int) -> int:
    return m * (m - 1) if m >= 3 else 0


def ell(p: int, x: int, g0: int, k: int) -> int:
    m = x - k
    if m < 3:
        return 0
    doubled = 2 * x * g0 - 2 * k * m - p
    return max(0, doubled // 2 + 1)


def e_old(p: int, k: int) -> int:
    return k * (p - 1)


def e_class(p: int, y: int, g0: int, k: int) -> int:
    return max(
        e_old(p, k),
        k * (g0 + k - 1) - 2 * (y - 1) * (k - 1),
    )


def near_floor(p: int, x: int, g0: int, c: int, use_class: bool) -> int | None:
    u = x - p + c
    if u < 0:
        return None
    lo = max(0, x - p)
    hi = min(u, x)
    vals = []
    for k in range(lo, hi + 1):
        m = x - k
        if m > p:
            continue
        eu = e_class(p, p - g0, g0, k) if use_class else e_old(p, k)
        vals.append(eu + max(phi(m), ell(p, x, g0, k)))
    return min(vals) if vals else None


def parity_formula(p: int, u: int, lam: int) -> int:
    if lam % 2 == 0:
        r = lam // 2
        return (
            p * p + p * u + u * u
            - (2 * r + 4) * (p + u)
            + 2 * r * r + 2 * r + 4
        )
    r = (lam - 1) // 2
    return (
        p * p + p * u + u * u
        - (2 * r + 5) * (p + u)
        + 2 * r * r + 4 * r + 6
    )


def main() -> None:
    # 1. Exact c=0 parity algebra and endpoint classification.
    checked_c0 = 0
    survivors = []
    for p in range(3, 101):
        for lam in range(0, p - 1):  # y=p-lambda-1 >= 1
            for u in range(0, 301):
                s0 = u * (p + u - 2) + p * (p - 1)
                c0 = c0_score_ceiling(p, u, lam)
                diff = s0 - c0
                assert diff == parity_formula(p, u, lam), (p, u, lam, diff)
                checked_c0 += 1
                if diff <= 0:
                    survivors.append((p, u, lam, 4 * p + 2 * u - lam))

    expected = {
        (3, 0, 1, 11),
        (3, 1, 1, 13),
        (3, 2, 1, 15),
        (4, 0, 2, 14),
        (4, 1, 2, 16),
        (4, 2, 2, 18),
    }
    assert set(survivors) == expected, survivors

    # 2. Broad abstract comparison of predecessor vs witness-class floor.
    checked = improved = newly_over_ceiling = 0
    max_gain = 0
    max_gain_row = None
    for p in range(3, 31):
        for g0 in range(1, p):
            for c in range(0, 31):
                lam = g0 + c - 1
                for x in range(3, 61):
                    u = x - p + c
                    if u < 0:
                        continue
                    old = near_floor(p, x, g0, c, False)
                    new = near_floor(p, x, g0, c, True)
                    if old is None or new is None:
                        continue
                    assert new >= old
                    checked += 1
                    gain = new - old
                    if gain:
                        improved += 1
                    b = 2 * p + u
                    n = 2 * b - lam
                    D_M = b * (n - b) - M(n)
                    C0 = 2 * (D_M - 1) + lam * (p + u) - p
                    if C0 >= 0 and old <= C0 < new:
                        newly_over_ceiling += 1
                    if gain > max_gain:
                        max_gain = gain
                        max_gain_row = (p, g0, c, x, u, old, new)

    print("c=0 parity rows checked:", checked_c0)
    print("c=0 score-feasible tuples:", sorted(survivors))
    print("abstract near-rigid rows checked:", checked)
    print("witness-class floor strictly stronger:", improved)
    print("newly above total C0 in this diagnostic box:", newly_over_ceiling)
    print("maximum floor gain:", max_gain)
    print("max-gain row (p,g0,c,x,u,old,new):", max_gain_row)


if __name__ == "__main__":
    main()
