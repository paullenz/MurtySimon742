#!/usr/bin/env python3

"""Replay guard for E6_ENDPOINT_STAIRCASE.md."""

E = 6


def psi(z: int) -> int:
    return 3 * (z >= 5) + 3 * (z >= 7) + 2 * (z >= 8) + (z >= 9) + (z >= 11)


def source_allowed(rho: int, p: int, q: int) -> bool:
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


def source_weight(rho: int, p: int, q: int) -> int:
    g = max(0, p - rho + 1)
    w = p + q
    return 3 * (rho == 4) + (g >= 1) + psi(w)


def source_slack(rho: int, p: int, q: int) -> int:
    return source_weight(rho, p, q) * q * (p + q) - (
        134 * p + 210 * q - 214 * rho - 188
    )


def label_weight(s: int, R: int, e: int) -> int:
    C = R + s + e
    return 3 * (s == 4) + (e >= 1) + psi(C)


def label_slack(s: int, R: int, e: int) -> int:
    x = s + e
    C = R + x
    return 48 + 77 * R + 53 * (s == 5) + 362 * e - label_weight(s, R, e) * x * C


def main() -> None:
    min_source = {}
    for rho in range(1, 21):
        for p in range(0, min(22, rho + 2) + 1):
            for q in range(0, 21):
                if not source_allowed(rho, p, q):
                    continue
                slack = source_slack(rho, p, q)
                assert slack >= 0, (rho, p, q, slack)
                if rho not in min_source or slack < min_source[rho][0]:
                    min_source[rho] = (slack, p, q)

    min_label = {}
    for s in (4, 5):
        for R in range(0, 20 - s):
            for e in range(E + 1):
                C = R + s + e
                if C > 23:
                    continue
                slack = label_slack(s, R, e)
                assert slack >= 0, (s, R, e, slack)
                key = (s, e)
                if key not in min_label or slack < min_label[key][0]:
                    min_label[key] = (slack, R)

    gaps = {}
    for k in range(21):
        r = 76 + k
        Q = 86 + k
        lower = 344 * Q - 214 * r - 188 * 23
        upper = 48 * 20 + 77 * r + 53 * k + 362 * E
        gap = lower - upper
        assert gap == 12
        gaps[k] = gap

    print("PASS_E6_ENDPOINT_STAIRCASE")
    print("source_minima", min_source)
    print("label_minima", min_label)
    print("gaps", gaps)


if __name__ == "__main__":
    main()
