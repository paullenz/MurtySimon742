#!/usr/bin/env python3

"""Replay guard for E9_HALL_MAJORIZATION.md."""

E = 9


def phi(z):
    return (
        2 * (z >= 6)
        + (z >= 7)
        + 2 * (z >= 8)
        + (z >= 9)
        + (z >= 10)
        + (z >= 11)
        + (z >= 12)
        + (z >= 13)
        + (z >= 14)
        + (z >= 16)
        + (z >= 18)
    )


def source_allowed(rho, p, q):
    if not (1 <= rho <= 20 and p >= 0 and q >= 0):
        return False
    if p > rho + 2 or p + q > 22:
        return False
    if q > 0:
        if rho < 4 or q + rho > 20:
            return False
        g = max(0, p - rho + 1)
        if q * g > E:
            return False
    return True


def source_slack(rho, p, q):
    w = p + q
    omega = 2 * (rho == 4) + phi(w)
    return omega * q - (9 * p + 16 * q - 17 * rho - 10)


def label_slack(s, R, e):
    x = s + e
    C = R + x
    omega = 2 * (s == 4) + phi(C)
    return 8 + 5 * R + 3 * (s == 5) + 18 * e - omega * x


def main():
    source_min = {}
    for rho in range(1, 21):
        for p in range(0, min(22, rho + 2) + 1):
            for q in range(0, 21):
                if not source_allowed(rho, p, q):
                    continue
                slack = source_slack(rho, p, q)
                assert slack >= 0, (rho, p, q, slack)
                if rho not in source_min or slack < source_min[rho][0]:
                    source_min[rho] = (slack, p, q)

    label_min = {}
    for s in (4, 5):
        for R in range(0, 20 - s):
            for e in range(E + 1):
                C = R + s + e
                if C > 23:
                    continue
                slack = label_slack(s, R, e)
                assert slack >= 0, (s, R, e, slack)
                key = (s, e)
                if key not in label_min or slack < label_min[key][0]:
                    label_min[key] = (slack, R)

    gaps = {}
    for k in range(21):
        r = 76 + k
        Q = 89 + k
        lower = 25 * Q - 17 * r - 10 * 23
        upper = 8 * 20 + 5 * r + 3 * k + 18 * E
        gap = lower - upper
        assert gap == 1
        gaps[k] = gap

    print("PASS_E9_HALL_MAJORIZATION")
    print("source_minima", source_min)
    print("label_minima", label_min)
    print("gaps", gaps)


if __name__ == "__main__":
    main()
