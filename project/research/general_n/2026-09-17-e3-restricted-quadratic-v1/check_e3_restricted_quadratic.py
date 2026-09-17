#!/usr/bin/env python3

"""Replay guard for E3_RESTRICTED_QUADRATIC.md.

Checks the complete local integer domains for the source and label potentials and
replays the final symbolic arithmetic for k=0,...,20. The hand proof is primary.
"""


def source_slack(rho: int, p: int, q: int) -> int:
    weight = 6 + (1 if rho == 4 else 0)
    return weight * q * (p + q) - (60 * p + 102 * q - 79 * rho - 104)


def source_allowed(rho: int, p: int, q: int) -> bool:
    if not (1 <= rho <= 20 and p >= 0 and q >= 0):
        return False
    if p > rho + 2 or p + q > 22:
        return False
    if q > 0:
        if rho < 4 or q + rho > 20:
            return False
        g = max(0, p - rho + 1)
        if q * g > 3:
            return False
    return True


def label_slack(s: int, R: int, e: int) -> int:
    x = s + e
    C = R + x
    lhs = (6 + (1 if s == 4 else 0)) * x * C
    rhs = 112 + 30 * R + 38 * (1 if s == 5 else 0) + 172 * e
    return rhs - lhs


def main() -> None:
    mins = {}
    for rho in range(1, 21):
        for p in range(0, min(22, rho + 2) + 1):
            for q in range(0, 21):
                if not source_allowed(rho, p, q):
                    continue
                slack = source_slack(rho, p, q)
                assert slack >= 0, (rho, p, q, slack)
                if q == 0:
                    cat = ("q0", "rho4" if rho == 4 else ("rho>=5" if rho >= 5 else "rho<4"))
                else:
                    g = max(0, p - rho + 1)
                    cat = (f"g{g}", "rho4" if rho == 4 else "rho>=5")
                if cat not in mins or slack < mins[cat][0]:
                    mins[cat] = (slack, (rho, p, q))

    expected_active_mins = {
        ("g0", "rho4"): 6,
        ("g1", "rho4"): 21,
        ("g2", "rho4"): 60,
        ("g3", "rho4"): 7,
        ("g0", "rho>=5"): 7,
        ("g1", "rho>=5"): 37,
        ("g2", "rho>=5"): 79,
        ("g3", "rho>=5"): 25,
    }
    for cat, expected in expected_active_mins.items():
        assert mins[cat][0] == expected, (cat, mins[cat], expected)

    label_mins = {}
    for s in (4, 5):
        for R in range(0, 20 - s):
            for e in range(0, 4):
                if R + s + e > 23:
                    continue
                slack = label_slack(s, R, e)
                assert slack >= 0, (s, R, e, slack)
                key = (s, e)
                if key not in label_mins or slack < label_mins[key][0]:
                    label_mins[key] = (slack, R)

    expected_label_mins = {
        (4, 0): 0,
        (4, 1): 34,
        (4, 2): 24,
        (4, 3): 0,
        (5, 0): 0,
        (5, 1): 22,
        (5, 2): 32,
        (5, 3): 30,
    }
    for key, expected in expected_label_mins.items():
        assert label_mins[key][0] == expected, (key, label_mins[key], expected)

    gaps = []
    for k in range(21):
        r = 76 + k
        Q = 83 + k
        source_lower = 162 * Q - 79 * r - 2392
        label_upper = 2756 + 30 * r + 38 * k
        gap = source_lower - label_upper
        assert gap == 14 + 15 * k
        assert gap > 0
        gaps.append(gap)

    print("PASS_E3_RESTRICTED_QUADRATIC")
    print("source_active_min_slacks", expected_active_mins)
    print("label_min_slacks", expected_label_mins)
    print("gaps", gaps)


if __name__ == "__main__":
    main()
