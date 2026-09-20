#!/usr/bin/env python3
"""Independent algebraic replay for SECOND_STRICT_X3_CLOSURE.md.

This reconstructs the exact rooted margin from the base definitions rather than
calling the historical large-head checker, then verifies the completed-square
identities used in the proof. It also prints the residual necessary-condition
rows after the score gate. Those rows are diagnostics only, not graphs and not
proof of realizability/nonrealizability.
"""

from math import ceil


def common_exact(p, x, g, omega):
    k = x - g
    u = k + 1 + omega
    a = x + 1
    b = 2 * p + u
    n = 1 + a + b
    lam = b - a - 1
    M = ((n - 1) ** 2) // 4 + 1
    D_M = b * (n - b) - M
    C0 = 2 * (D_M - 1) + lam * (p + u) - p
    return k, u, n, lam, C0


def row(case, p, g, omega):
    x = 3
    k, u, n, lam, C0 = common_exact(p, x, g, omega)
    if k < 1 or g < 1 or omega < 2:
        return None

    eps_b = p - g + 2
    if eps_b < 0:
        return None
    E_core = k * (p + k - 1)

    if case == "R":
        L_X = x * (p + k)
        eps_y = p - g + 1 + omega
        eps_z = p + omega - 2
        E_ord = (omega - 2) * max(0, p - x + omega) + max(0, p - x + omega - 1)
        q_max = (k + 1) * omega
        r_low = x + 1
    elif case == "Fz0":
        L_X = x * (p + k)
        eps_y = p - g + omega
        eps_z = p + omega - 2
        E_ord = (omega - 1) * max(0, p - x + omega)
        q_max = (k + 1) * omega - 1
        r_low = x + 1
    elif case == "Fx":
        L_X = x * (p + k) + omega - 2
        eps_y = p - g + omega
        eps_z = p + omega - 2
        E_ord = (omega - 1) * max(0, p - x + omega)
        q_max = (k + 1) * omega - 1
        r_low = x + p - 2 + ceil((x + p - 2) / x)
    elif case == "Fz1":
        if omega < 3:
            return None
        L_X = x * (p + k)
        eps_y = p - g + omega
        eps_z = p + k + omega - 2
        E_ord = (omega - 1) * max(0, p - x + omega)
        q_max = (k + 1) * (omega - 1)
        r_low = x + 2
    else:
        raise ValueError(case)

    L_A = L_X + eps_y
    S_min = E_core + eps_b + eps_z + E_ord + L_A
    score_margin = C0 - S_min
    r_max = (p - lam) * (p + u) + q_max + C0 - L_A
    rooted_margin = r_max - r_low
    eps = (n - 1) & 1

    if case in ("R", "Fz0"):
        two_bmax = eps + 4 * g - k * k - 2 * k * p + 6 * k - p * p + 2 * p - 4
        predicted_two_B = two_bmax - (omega - (5 - p)) ** 2
        assert predicted_two_B == 2 * rooted_margin
    elif case == "Fz1":
        two_bmax = eps + 4 * g - k * k - 2 * k * p + 4 * k - p * p + 2 * p - 6
        predicted_two_B = two_bmax - (omega - (5 - p)) ** 2
        assert predicted_two_B == 2 * rooted_margin
    else:
        # Fx formula in the note uses r_low >= x+p-1.  The exact ceiling can
        # only decrease B.  Verify the precise gap.
        two_bmax_relaxed = eps + 2 * g - k * k - 2 * k * p + 4 * k - p * p + 2 * p + 1
        relaxed_two_B = two_bmax_relaxed - (omega - (4 - p)) ** 2
        exact_gap = 2 * (ceil((p + 1) / 3) - 1)
        assert relaxed_two_B - 2 * rooted_margin == exact_gap

    return score_margin, rooted_margin, n


def main():
    cases = ("R", "Fz0", "Fx", "Fz1")
    survivors = {c: [] for c in cases}
    checked = 0
    for p in range(2, 20):
        for g in (1, 2):
            for omega in range(2, 30):
                for case in cases:
                    out = row(case, p, g, omega)
                    if out is None:
                        continue
                    checked += 1
                    A, B, n = out
                    if A >= 0 and B >= 0:
                        survivors[case].append((p, g, omega, n, A, B))

    print(f"exact/completed-square identity checks: {checked}")
    for case in cases:
        rows = survivors[case]
        print(case, "diagnostic survivors", len(rows), "max_n", max((r[3] for r in rows), default=None))
        for r in rows:
            print(" ", r)


if __name__ == "__main__":
    main()
