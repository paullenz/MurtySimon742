#!/usr/bin/env python3

"""Replay guard for E5_EXCESS_RESTRICTED.md."""

E = 5


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


def source_weight(rho: int, p: int) -> int:
    g = max(0, p - rho + 1)
    return 12 + 2 * (rho == 4) + (g >= 1)


def source_slack(rho: int, p: int, q: int) -> int:
    return source_weight(rho, p) * q * (p + q) - (
        141 * p + 213 * q - 177 * rho - 246
    )


def label_weight(s: int, e: int) -> int:
    return 12 + 2 * (s == 4) + (e >= 1)


def label_slack(s: int, R: int, e: int) -> int:
    x = s + e
    C = R + x
    return 224 + 57 * R + 118 * (s == 5) + 421 * e - label_weight(s, e) * x * C


def main() -> None:
    source_mins = {}
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
                if cat not in source_mins or slack < source_mins[cat][0]:
                    source_mins[cat] = (slack, (rho, p, q))

    label_mins = {}
    for s in (4, 5):
        for R in range(0, 20 - s):
            for e in range(E + 1):
                x = s + e
                C = R + x
                if C > 23:
                    continue
                slack = label_slack(s, R, e)
                assert slack >= 0, (s, R, e, slack)
                key = (s, e)
                if key not in label_mins or slack < label_mins[key][0]:
                    label_mins[key] = (slack, R)

    gaps = {}
    for k in range(21):
        r = 76 + k
        Q = 85 + k
        source_lower = 354 * Q - 177 * r - 246 * 23
        label_upper = 224 * 20 + 57 * r + 118 * k + 421 * E
        gap = source_lower - label_upper
        assert gap == 63 + 2 * k
        assert gap > 0
        gaps[k] = gap

    print("PASS_E5_EXCESS_RESTRICTED")
    print("source_minima", source_mins)
    print("label_minima", label_mins)
    print("gaps", gaps)


if __name__ == "__main__":
    main()
