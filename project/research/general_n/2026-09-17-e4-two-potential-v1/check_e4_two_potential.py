#!/usr/bin/env python3

"""Replay guard for E4_TWO_POTENTIAL.md."""


def source_allowed(rho: int, p: int, q: int) -> bool:
    if not (1 <= rho <= 20 and p >= 0 and q >= 0):
        return False
    if p > rho + 2 or p + q > 22:
        return False
    if q > 0:
        if rho < 4 or q + rho > 20:
            return False
        g = max(0, p - rho + 1)
        if q * g > 4:
            return False
    return True


def source_slack_A(rho: int, p: int, q: int) -> int:
    w = 6 + (1 if rho == 4 else 0)
    return w * q * (p + q) - (70 * p + 112 * q - 98 * rho - 112)


def source_slack_B(rho: int, p: int, q: int) -> int:
    w = 6 + (1 if rho == 4 else 0)
    return w * q * (p + q) - (60 * p + 102 * q - 79 * rho - 108)


def label_slack_A(s: int, R: int, e: int) -> int:
    x = s + e
    C = R + x
    lhs = (6 + (1 if s == 4 else 0)) * x * C
    rhs = 112 + 28 * R + 66 * (1 if s == 5 else 0) + 189 * e
    return rhs - lhs


def label_slack_B(s: int, R: int, e: int) -> int:
    x = s + e
    C = R + x
    lhs = (6 + (1 if s == 4 else 0)) * x * C
    rhs = 112 + 30 * R + 38 * (1 if s == 5 else 0) + 182 * e
    return rhs - lhs


def main() -> None:
    mins_A = {}
    mins_B = {}
    for rho in range(1, 21):
        for p in range(0, min(22, rho + 2) + 1):
            for q in range(0, 21):
                if not source_allowed(rho, p, q):
                    continue
                a = source_slack_A(rho, p, q)
                b = source_slack_B(rho, p, q)
                assert a >= 0, ("A", rho, p, q, a)
                assert b >= 0, ("B", rho, p, q, b)
                if q == 0:
                    cat = ("q0", "rho4" if rho == 4 else ("rho>=5" if rho >= 5 else "rho<4"))
                else:
                    g = max(0, p - rho + 1)
                    cat = (f"g{g}", "rho4" if rho == 4 else "rho>=5")
                if cat not in mins_A or a < mins_A[cat][0]:
                    mins_A[cat] = (a, (rho, p, q))
                if cat not in mins_B or b < mins_B[cat][0]:
                    mins_B[cat] = (b, (rho, p, q))

    for s in (4, 5):
        for R in range(0, 20 - s):
            for e in range(0, 5):
                # d=R+s<=19 automatically from range; C can be at most 23 here.
                assert label_slack_A(s, R, e) >= 0, ("LA", s, R, e, label_slack_A(s,R,e))
                assert label_slack_B(s, R, e) >= 0, ("LB", s, R, e, label_slack_B(s,R,e))

    covered = set()
    gaps_A, gaps_B = {}, {}
    for k in range(21):
        r = 76 + k
        Q = 84 + k
        source_A = 182 * Q - 98 * r - 2576
        label_A = 2996 + 28 * r + 66 * k
        gap_A = source_A - label_A
        assert gap_A == 140 - 10 * k
        gaps_A[k] = gap_A
        if gap_A > 0:
            covered.add(k)

        source_B = 162 * Q - 79 * r - 2484
        label_B = 2968 + 30 * r + 38 * k
        gap_B = source_B - label_B
        assert gap_B == 15 * k - 128
        gaps_B[k] = gap_B
        if gap_B > 0:
            covered.add(k)

    assert covered == set(range(21)), sorted(set(range(21)) - covered)
    assert all(gaps_A[k] > 0 for k in range(14))
    assert all(gaps_B[k] > 0 for k in range(9,21))

    print("PASS_E4_TWO_POTENTIAL")
    print("A_source_minima", mins_A)
    print("B_source_minima", mins_B)
    print("A_gap", gaps_A)
    print("B_gap", gaps_B)


if __name__ == "__main__":
    main()
