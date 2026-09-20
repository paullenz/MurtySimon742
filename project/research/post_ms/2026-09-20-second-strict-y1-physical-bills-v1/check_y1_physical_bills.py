#!/usr/bin/env python3
"""Necessary-condition diagnostic for the large-head mixed y=1 physical bills.

This scans an abstract parameter box only. Rows are not D2C graphs and no
finite count is used as proof. The exceptional-Fz formulas include the later
structural theorem that kills all D--E outside cross-class edges.
"""

from math import ceil

P_MAX = 20
X_MAX = 30
OMEGA_MAX = 24


def common(p, x, g, omega):
    k = x - g
    if not (1 <= k and 1 <= g and omega >= 2):
        return None
    u = k + 1 + omega
    a = x + 1
    b = 2 * p + u
    n = 1 + a + b
    lam = b - a - 1
    if lam < 0:
        return None
    M = ((n - 1) ** 2) // 4 + 1
    D_M = b * (n - b) - M
    C0 = 2 * (D_M - 1) + lam * (p + u) - p
    E_core = k * (p + k - 1)
    eps_b = p - g + 2
    return k, u, lam, C0, E_core, eps_b


def necessary(case, p, x, g, omega):
    base = common(p, x, g, omega)
    if base is None:
        return None
    k, u, lam, C0, E_core, eps_b = base

    if case == "R":
        L_X = x * (p + k)
        eps_y = p - g + 1 + omega
        eps_z = p + omega - 2
        E_ord = (omega - 2) * max(0, p - x + omega) + max(
            0, p - x + omega - 1
        )
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
        # The exceptional head requires both ordinary outside code classes,
        # so omega>=3.  The cross-class closure proves all of U_o independent.
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
    return score_margin, rooted_margin


def main():
    counts = {case: 0 for case in ("R", "Fz0", "Fx", "Fz1")}
    tested = {case: 0 for case in counts}

    for p in range(2, P_MAX + 1):
        for x in range(5, X_MAX + 1):
            for g in range(1, x):
                for omega in range(2, OMEGA_MAX + 1):
                    for case in ("R", "Fz0", "Fx", "Fz1"):
                        out = necessary(case, p, x, g, omega)
                        if out is None:
                            continue
                        tested[case] += 1
                        if out[0] >= 0 and out[1] >= 0:
                            counts[case] += 1

    print(f"box=p:2..{P_MAX}, x:5..{X_MAX}, omega:2..{OMEGA_MAX}, 1<=g<x")
    for case in ("R", "Fz0", "Fx", "Fz1"):
        print(f"{case}: tested={tested[case]} survivors={counts[case]}")


if __name__ == "__main__":
    main()
