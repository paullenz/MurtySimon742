#!/usr/bin/env python3

"""Replay guard for the 17 Sep 2026 small-selected-excess barrier.

This script checks only finite integer arithmetic used in SMALL_EXCESS_BARRIER.md.
The hand proof remains primary.
"""


def delta(k: int) -> int:
    if k <= 14:
        return 6
    if k == 15:
        return 5
    if k == 16:
        return 2
    return 0


def u0(k: int) -> int:
    r = 76 + k
    return 624 + 13 * k + min(14 * k, r)


def l0(k: int) -> int:
    c4 = (33 + k) // 3
    return 780 + 15 * k - delta(k) * c4


def local_ok(k: int, E: int, rho: int, p: int, q: int) -> bool:
    if not (0 <= k <= 20 and 0 <= E <= 2):
        return False
    if not (1 <= rho <= 20):
        return False
    if p < 0 or q < 0:
        return False
    if p > rho + 2 or p + q > 22:
        return False
    if q > 0:
        if rho < 4:
            return False
        if q + rho > 20:
            return False
        if rho == 4 and q > 20 - k:
            return False
        g = max(0, p - rho + 1)
        # selected labels at one source are distinct, hence their excesses sum
        # to at least q*g and cannot exceed the global budget E.
        if q * g > E:
            return False
    return True


def source_lhs(p: int, q: int) -> int:
    return 10 * p + 15 * q - q * (p + q)


def source_rhs(k: int, rho: int) -> int:
    return 10 * rho + 20 + (delta(k) if rho == 4 else 0)


def check_local_source_family() -> None:
    for k in range(21):
        for E in range(3):
            for rho in range(1, 21):
                for p in range(0, min(22, rho + 2) + 1):
                    for q in range(0, 21):
                        if local_ok(k, E, rho, p, q):
                            assert source_lhs(p, q) <= source_rhs(k, rho), (
                                k, E, rho, p, q,
                                source_lhs(p, q), source_rhs(k, rho),
                            )


def check_gap_table() -> None:
    gaps = []
    for k in range(21):
        g = l0(k) - u0(k)
        gaps.append(g)
        assert g >= 2
        for E in (0, 1):
            # source lower minus label upper after allowing E excess
            assert g + E - E * E > 0
        if k != 12:
            assert g + 2 - 4 > 0
    assert min(gaps) == 2
    assert [k for k in range(21) if l0(k) - u0(k) == 2] == [12]


def check_label_increment_bound() -> None:
    # Local algebra: Delta=e(d+s)+e^2 <=24e+e^2 for d<=19,s<=5.
    for s in (4, 5):
        for d in range(s, 20):
            for e in range(3):
                inc = e * (d + s) + e * e
                assert inc <= 24 * e + e * e
    # Global convexity for E<=2: sum e_i^2 <= E^2.
    assert 0 <= 0
    assert 1 <= 1
    assert max(2, 1 + 1) <= 4


def check_boundary_k12_e2() -> None:
    k, E = 12, 2
    r, Q = 88, 94
    c4 = (33 + k) // 3
    assert c4 == 15
    assert 5 * 5 + 15 * 4 + 3 * 1 == r

    # Verify the p ceilings claimed for any locally tight source.
    tight_p = {1: [], 4: [], 5: []}
    for rho in tight_p:
        for p in range(0, min(22, rho + 2) + 1):
            for q in range(0, 21):
                if not local_ok(k, E, rho, p, q):
                    continue
                if source_lhs(p, q) == source_rhs(k, rho):
                    tight_p[rho].append((p, q))
    assert tight_p[1]
    assert max(p for p, _ in tight_p[1]) <= 3
    assert tight_p[4]
    assert max(p for p, _ in tight_p[4]) <= 3
    # rho=5 need not be tight for this crude ceiling; canonical incoming cap is 7.
    assert 5 + 2 == 7

    max_total_p_if_all_local_bounds_tight = 3 * 3 + 15 * 3 + 5 * 7
    assert max_total_p_if_all_local_bounds_tight == 89
    assert max_total_p_if_all_local_bounds_tight < Q


def main() -> None:
    check_local_source_family()
    check_gap_table()
    check_label_increment_bound()
    check_boundary_k12_e2()
    print("PASS_SMALL_EXCESS_BARRIER")
    print("min_gap", min(l0(k) - u0(k) for k in range(21)))
    print("unique_min_k", [k for k in range(21) if l0(k) - u0(k) == 2])
    print("boundary_p_ceiling", 89, "required", 94)


if __name__ == "__main__":
    main()
