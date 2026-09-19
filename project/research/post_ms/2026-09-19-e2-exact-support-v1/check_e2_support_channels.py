#!/usr/bin/env python3
"""Arithmetic/topology audit for EXACT_E2_SUPPORT_CHANNELS.md.

This is not a D2C graph enumerator and makes no graph-realizability claim.
It checks only the finite channel-allocation and pair-correction formulas.
"""
import math


def channel_bound(k, s, q, c, d0, Delta):
    B = s - c + q
    K = k * (c - d0)
    return d0 * (k + 1) + 2 * min(Delta, B) + min(K, max(0, Delta - B))


def channel_bruteforce(k, s, q, c, d0, Delta):
    B = s - c + q
    K = k * (c - d0)
    best = -1
    for b in range(B + 1):
        for z in range(K + 1):
            if b + z <= Delta:
                best = max(best, d0 * (k + 1) + 2*b + z)
    return best


def phi_closed(B, K, D):
    if K == 0:
        return max(D, -2*B)
    if D >= -2*B - 1:
        return max(D, -2*B)
    return max(math.ceil(D / 2) - B, -(2*B + K))


def phi_brute(B, K, D):
    def f(Delta):
        return 2*min(Delta, B) + min(K, max(0, Delta-B))
    # Once Delta > B+K and D+2Delta > 0 the expression increases.
    top = max(B + K + 10, (-D)//2 + 10, 20)
    return min(max(0, D + 2*Delta) - f(Delta) for Delta in range(top + 1))


def r3_special(k, c, d0, D):
    B = 3 - c
    K = k * (c - d0)
    return -d0*(k+1) + phi_closed(B, K, D)


def r3_expected(k, c, d0, D):
    if (c, d0) == (0, 0):
        return max(D, -6)
    if (c, d0) == (1, 1):
        return max(D-(k+1), -(k+5))
    assert (c, d0) == (1, 0)
    if D >= -5:
        return max(D, -4)
    return max(math.ceil(D/2)-2, -(k+4))


def allowed_r22_topologies():
    out = []
    for h in (0, 1):
        cs = (0, 1) if h == 0 else (0, 1, 2)
        for c in cs:
            for d0 in range(c + 1):
                out.append((h, c, d0))
    return out


def jmax_formula(k, s, q, c, d0):
    B = s - c + q
    K = k * (c - d0)
    direct = d0*(k+1) + 2*B + K
    simple = 2*s + 2*q + c*(k-2) + d0
    assert direct == simple
    return direct


def main():
    channel_checks = 0
    phi_checks = 0
    r3_checks = 0

    for k in range(3, 30):
        # R3 layouts.
        for c in (0, 1):
            for d0 in range(c + 1):
                for Delta in range(0, 40):
                    got = channel_bound(k, 3, 0, c, d0, Delta)
                    brute = channel_bruteforce(k, 3, 0, c, d0, Delta)
                    assert got == brute, ("R3-J", k, c, d0, Delta, got, brute)
                    channel_checks += 1
                for D in range(-120, 121):
                    got = r3_special(k, c, d0, D)
                    exp = r3_expected(k, c, d0, D)
                    assert got == exp, ("R3-PHI", k, c, d0, D, got, exp)
                    r3_checks += 1

        # R2+R2 layouts.
        for h, c, d0 in allowed_r22_topologies():
            for Delta in range(0, 50):
                got = channel_bound(k, 4, h, c, d0, Delta)
                brute = channel_bruteforce(k, 4, h, c, d0, Delta)
                assert got == brute, ("R22-J", k, h, c, d0, Delta, got, brute)
                channel_checks += 1

        # General Phi checker over all B,K needed here and more.
        for B in range(0, 8):
            for K in range(0, 2*k + 1):
                for D in range(-120, 121):
                    got = phi_closed(B, K, D)
                    brute = phi_brute(B, K, D)
                    assert got == brute, ("PHI", k, B, K, D, got, brute)
                    phi_checks += 1

        # Unique cheapest deep R2+R2 topology for k>=3.
        vals = []
        for h, c, d0 in allowed_r22_topologies():
            vals.append((jmax_formula(k, 4, h, c, d0), h, c, d0))
        best = max(v[0] for v in vals)
        winners = [(h, c, d0) for val, h, c, d0 in vals if val == best]
        assert winners == [(1, 2, 2)], (k, best, winners)
        assert best == 2*k + 8, (k, best)

    print({
        "channel_allocation_checks": channel_checks,
        "phi_closed_form_checks": phi_checks,
        "r3_specialization_checks": r3_checks,
        "r22_topology_count": len(allowed_r22_topologies()),
        "unique_deep_cheapest_r22": "h=1,c=2,d0=2 for every k>=3",
        "failures": 0,
        "trust": "arithmetic/topology audit only; no D2C graph-realizability claim",
    })


if __name__ == "__main__":
    main()
