#!/usr/bin/env python3

"""Exact replay guard for HALL_RAMP_ALL_EXCESS.md.

No optimization package is used. The three certificates are hard-coded and
all bounded local source/label states plus all global (E,k) gaps are checked
with integer arithmetic.
"""

BANDS = [
    {
        "range": (10, 15),
        "basis": ((9, 4), (12, 12), (19, 4)),
        "mu": 33,
        "src": (104, 212, 188, 124),
        "lab": (132, 80, 48, 256),
        "gap_formula": lambda E, k: 60 * E - 580,
    },
    {
        "range": (16, 21),
        "basis": ((9, 5), (14, 19)),
        "mu": 40,
        "src": (127, 261, 236, 146),
        "lab": (160, 96, 56, 341),
        "gap_formula": lambda E, k: 47 * E - 750,
    },
    {
        "range": (22, 42),
        "basis": ((8, 6), (15, 24)),
        "mu": 46,
        "src": (153, 333, 311, 150),
        "lab": (184, 120, 56, 439),
        "gap_formula": lambda E, k: 47 * E - k - 1006,
    },
]


def ramp(L, z):
    return max(0, min(z, L) - 4)


def phi(band, z):
    return sum(weight * ramp(L, z) for L, weight in band["basis"])


def source_allowed(rho, p, q, Emax):
    if not (1 <= rho <= 20 and p >= 0 and q >= 0):
        return False
    if p > rho + 2 or p + q > 22:
        return False
    if q > 0:
        if rho < 4 or q + rho > 20:
            return False
        g = max(0, p - rho + 1)
        if q * g > Emax:
            return False
    return True


def check_band(band):
    Emin, Emax = band["range"]
    A, B, Ccoef, D = band["src"]
    l0, lR, lk, le = band["lab"]

    source_min = None
    for rho in range(1, 21):
        for p in range(0, min(22, rho + 2) + 1):
            for q in range(0, 21):
                if not source_allowed(rho, p, q, Emax):
                    continue
                omega = band["mu"] * (rho == 4) + phi(band, p + q)
                slack = omega * q - (A * p + B * q - Ccoef * rho - D)
                assert slack >= 0, ("source", band["range"], rho, p, q, slack)
                rec = (slack, rho, p, q)
                if source_min is None or rec < source_min:
                    source_min = rec

    label_min = None
    for s in (4, 5):
        for R in range(0, 20 - s):
            for e in range(Emax + 1):
                x = s + e
                C = R + x
                if C > 23:
                    continue
                omega = band["mu"] * (s == 4) + phi(band, C)
                slack = l0 + lR * R + lk * (s == 5) + le * e - omega * x
                assert slack >= 0, ("label", band["range"], s, R, e, slack)
                rec = (slack, s, R, e)
                if label_min is None or rec < label_min:
                    label_min = rec

    gap_min = None
    for E in range(Emin, Emax + 1):
        for k in range(21):
            r = 76 + k
            Q = 80 + E + k

            lower = (A + B) * Q - Ccoef * r - D * 23
            upper = l0 * 20 + lR * r + lk * k + le * E
            gap = lower - upper

            expected = band["gap_formula"](E, k)
            assert gap == expected, ("gap_formula", band["range"], E, k, gap, expected)
            assert gap > 0, ("global_gap", band["range"], E, k, gap)

            rec = (gap, E, k)
            if gap_min is None or rec < gap_min:
                gap_min = rec

    return source_min, label_min, gap_min


def main():
    summaries = []
    for band in BANDS:
        summaries.append((band["range"],) + check_band(band))

    # The global incoming cap p_u <= rho_u+2 on 23 sources implies E<=42.
    for k in range(21):
        Q_at_43 = 80 + 43 + k
        r_plus_46 = 76 + k + 46
        assert Q_at_43 > r_plus_46

    print("PASS_HALL_RAMP_ALL_EXCESS")
    for summary in summaries:
        print(summary)
    print("E_MAX_FROM_INCOMING_CAP", 42)


if __name__ == "__main__":
    main()
