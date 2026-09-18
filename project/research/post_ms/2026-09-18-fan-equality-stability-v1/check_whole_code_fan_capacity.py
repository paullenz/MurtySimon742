#!/usr/bin/env python3
"""Independent exact-arithmetic audit for WHOLE_CODE_FAN_CAPACITY_AND_COMPACT_SCORECARD.md.

This checker does not prove the graph-theoretic inputs.  It stress-tests the
integer consequences used after those inputs:

* the whole-code bounded-hole cap against the preceding split cap;
* the full-fan low-hole / beta hybrid cap;
* the compact quadratic fan inequality from the primitive lower/upper bounds
  on total fan-hole mass.

All arithmetic is integer arithmetic apart from no operations at all: square
roots use math.isqrt.
"""

from collections import Counter
from math import isqrt


def max_quad(rhs: int, shift: int) -> int:
    """Largest n>=0 satisfying n(n-shift)<=rhs, rhs,shift>=0."""
    n = (shift + isqrt(shift * shift + 4 * rhs)) // 2
    while (n + 1) * (n + 1 - shift) <= rhs:
        n += 1
    while n * (n - shift) > rhs:
        n -= 1
    return n


def old_cap(k: int, edge_budget: int, q_budget: int) -> int:
    """Capacity used by the preceding split profile."""
    if k == 0:
        return max_quad(2 * q_budget, 1)
    r_a = max_quad(2 * edge_budget, k)
    r_u = max_quad(2 * q_budget, k + 1)
    return r_a + r_u


def whole_low_hole_cap(d: int, k: int, edge_budget: int, q_budget: int) -> int:
    """The new C_x(K;d), including the K=0 root-hole specialization."""
    if d <= 1:
        return d
    t = d - 1 - k
    if t <= 0:
        return d
    r_u = max_quad(2 * q_budget, k + 1)
    m = 2 * edge_budget
    if k == 0:
        return min(d, r_u, m // t)
    return min(d, m // t, (m + r_u) // (t + 1))


def audit_profile_caps(counts: Counter) -> None:
    # 1,494,045 exact cases.
    for d in range(2, 36):
        for k in range(0, d - 1):
            for edge_budget in range(0, 81):
                for q_budget in range(0, 31):
                    new = whole_low_hole_cap(d, k, edge_budget, q_budget)
                    old = old_cap(k, edge_budget, q_budget)
                    assert new <= min(d, old), (
                        "profile cap regression",
                        d,
                        k,
                        edge_budget,
                        q_budget,
                        new,
                        old,
                    )
                    counts["profile_cases"] += 1


def audit_uniform_whole_code_cap(counts: Counter) -> None:
    # The total uniformly bounded-hole witness set has shift K+1, whereas the
    # old A-only cap has shift K.  The total cap can exceed the A-only cap by
    # at most one before any U-budget information is used.
    for k in range(1, 11):
        for edge_budget in range(0, 201):
            total = max_quad(2 * edge_budget, k + 1)
            old_a = max_quad(2 * edge_budget, k)
            assert total <= old_a + 1, (
                "uniform whole-code cap regression",
                k,
                edge_budget,
                total,
                old_a,
            )
            counts["uniform_cases"] += 1


def audit_compact_quadratic(counts: Counter) -> None:
    # Primitive model:
    #   e(W) <= E=floor(V0*S/L), L=lambda+1;
    #   G >= d(d-1)-2E;
    #   G <= S+(d-1)(P-d)-dL.
    # Whenever that interval is nonempty, verify
    #   2d^2-(T+2)d+P <= S+2E, T=P-L.
    for p_plus_u in range(2, 31):
        for lam_plus_one in range(1, p_plus_u + 6):
            t = p_plus_u - lam_plus_one
            for v0 in range(1, 31):
                for slack in range(0, 31):
                    edge_budget = (v0 * slack) // lam_plus_one
                    for d in range(1, p_plus_u + 1):
                        g_lower = max(0, d * (d - 1) - 2 * edge_budget)
                        g_upper = (
                            slack
                            + (d - 1) * (p_plus_u - d)
                            - d * lam_plus_one
                        )
                        if g_lower <= g_upper and g_upper >= 0:
                            lhs = 2 * d * d - (t + 2) * d + p_plus_u
                            rhs = slack + 2 * edge_budget
                            assert lhs <= rhs, (
                                "compact quadratic regression",
                                p_plus_u,
                                lam_plus_one,
                                v0,
                                slack,
                                d,
                                edge_budget,
                                g_lower,
                                g_upper,
                                lhs,
                                rhs,
                            )
                        counts["compact_cases"] += 1


def main() -> None:
    counts = Counter()
    audit_profile_caps(counts)
    audit_uniform_whole_code_cap(counts)
    audit_compact_quadratic(counts)
    total = sum(counts.values())
    print("WHOLE_CODE_FAN_CAPACITY_AUDIT_OK")
    print(f"profile_cases={counts['profile_cases']}")
    print(f"uniform_cases={counts['uniform_cases']}")
    print(f"compact_cases={counts['compact_cases']}")
    print(f"total_checks={total}")
    print("failures=0")


if __name__ == "__main__":
    main()
