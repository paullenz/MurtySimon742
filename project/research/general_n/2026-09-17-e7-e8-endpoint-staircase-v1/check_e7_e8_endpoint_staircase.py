#!/usr/bin/env python3

"""Replay guard for E7_E8_ENDPOINT_STAIRCASE.md."""


def source_allowed(rho, p, q, E):
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


def psi7(z):
    return 6 * (z >= 6) + (z >= 7) + 2 * (z >= 8) + (z >= 9) + (z >= 11)


def psi8(z):
    return 8 * (z >= 6) + 2 * (z >= 7) + 2 * (z >= 8) + (z >= 9) + (z >= 10) + (z >= 11)


def verify(E, psi, r4mult, g1mult, src, lab, expected_gap):
    A, B, Ccoef, D = src
    alpha, beta, gamma, delta = lab

    min_source = {}
    for rho in range(1, 21):
        for p in range(0, min(22, rho + 2) + 1):
            for q in range(0, 21):
                if not source_allowed(rho, p, q, E):
                    continue
                g = max(0, p - rho + 1)
                w = p + q
                omega = r4mult * (rho == 4) + g1mult * (g >= 1) + psi(w)
                slack = omega * q * w - (A * p + B * q - Ccoef * rho - D)
                assert slack >= 0, (E, rho, p, q, slack)
                if rho not in min_source or slack < min_source[rho][0]:
                    min_source[rho] = (slack, p, q)

    min_label = {}
    for s in (4, 5):
        for R in range(0, 20 - s):
            for e in range(E + 1):
                x = s + e
                C = R + x
                if C > 23:
                    continue
                omega = r4mult * (s == 4) + g1mult * (e >= 1) + psi(C)
                slack = alpha + beta * R + gamma * (s == 5) + delta * e - omega * x * C
                assert slack >= 0, (E, s, R, e, slack)
                key = (s, e)
                if key not in min_label or slack < min_label[key][0]:
                    min_label[key] = (slack, R)

    gaps = {}
    for k in range(21):
        r = 76 + k
        Q = 80 + k + E
        lower = (A + B) * Q - Ccoef * r - D * 23
        upper = alpha * 20 + beta * r + gamma * k + delta * E
        gap = lower - upper
        assert gap == expected_gap(k), (E, k, gap, expected_gap(k))
        assert gap > 0
        gaps[k] = gap

    return min_source, min_label, gaps


def main():
    s7, l7, g7 = verify(
        7, psi7, 3, 1,
        (142, 224, 222, 204),
        (48, 84, 69, 392),
        lambda k: 190 - 9 * k,
    )
    s8, l8, g8 = verify(
        8, psi8, 4, 3,
        (206, 308, 309, 312),
        (64, 112, 93, 597),
        lambda k: 4,
    )
    print("PASS_E7_E8_ENDPOINT_STAIRCASE")
    print("E7_source_minima", s7)
    print("E7_label_minima", l7)
    print("E7_gaps", g7)
    print("E8_source_minima", s8)
    print("E8_label_minima", l8)
    print("E8_gaps", g8)


if __name__ == "__main__":
    main()
