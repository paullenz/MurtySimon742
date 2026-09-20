#!/usr/bin/env python3
"""Scope-correct replay for the large-head exact-second-strict mixed y=1 tail.

This preserves the case formulas from check_y1_physical_bills.py but restores
the inherited positive-buffer branch condition t0=p-g>=1, i.e. g<=p-1.
Rows are abstract necessary-condition rows, not graphs.  The analytic proof in
SECOND_STRICT_SCOPE_REPAIR_AND_Y1_CLOSURE.md is the closure; this is only a
replay/audit companion.
"""

from math import ceil

P_MAX = 20
X_MAX = 30
OMEGA_MAX = 24


def common(p, x, g, omega):
    k = x - g
    if not (1 <= k and 1 <= g and omega >= 2):
        return None
    # Restored branch scope inherited from the positive-buffer setup.
    if p - g < 1:
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
    assert eps_b >= 3
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
    cases = ("R", "Fz0", "Fx", "Fz1")
    counts = {case: 0 for case in cases}
    tested = {case: 0 for case in cases}
    max_rooted = {case: None for case in cases}
    max_row = {case: None for case in cases}

    for p in range(2, P_MAX + 1):
        for x in range(5, X_MAX + 1):
            for g in range(1, min(x, p)):
                for omega in range(2, OMEGA_MAX + 1):
                    for case in cases:
                        out = necessary(case, p, x, g, omega)
                        if out is None:
                            continue
                        tested[case] += 1
                        score_margin, rooted_margin = out
                        if max_rooted[case] is None or rooted_margin > max_rooted[case]:
                            max_rooted[case] = rooted_margin
                            max_row[case] = (p, x, g, omega, score_margin, rooted_margin)
                        if score_margin >= 0 and rooted_margin >= 0:
                            counts[case] += 1

    print(
        f"box=p:2..{P_MAX}, x:5..{X_MAX}, omega:2..{OMEGA_MAX}, "
        "1<=g<=min(x-1,p-1)"
    )
    for case in cases:
        print(
            f"{case}: tested={tested[case]} survivors={counts[case]} "
            f"max_rooted_margin={max_rooted[case]} row={max_row[case]}"
        )

    assert counts == {"R": 0, "Fz0": 0, "Fx": 0, "Fz1": 0}
    assert tested == {"R": 97980, "Fz0": 97980, "Fx": 97980, "Fz1": 93720}
    assert max_rooted == {"R": -4, "Fz0": -4, "Fx": -6, "Fz1": -6}


if __name__ == "__main__":
    main()
