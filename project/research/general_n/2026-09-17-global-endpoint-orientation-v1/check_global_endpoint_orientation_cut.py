#!/usr/bin/env python3
"""Exact integer replay for the 17 Sep 2026 global endpoint-orientation cut.

This checks only the arithmetic projection stated in
GLOBAL_ENDPOINT_ORIENTATION_CUT.md.  It does not construct a Murty-Simon graph.
"""


def main() -> None:
    a = 20
    b = 23
    rho = [5] * 5 + [4] * 11 + [1] * 7

    # Twenty selected labels: sixteen have R=4, four have R=3;
    # x=s=4 for every label, hence C=R+x.
    s = [4] * 20
    x = [4] * 20
    R = [4] * 16 + [3] * 4
    C = [rr + xx for rr, xx in zip(R, x)]
    Q = sum(x)

    assert len(rho) == b
    assert sum(rho) == 76
    assert Q == 80
    assert C == [8] * 16 + [7] * 4

    B = []
    rows = []
    for ru in rho:
        P0 = min(b - 1, ru + b - a - 1)
        compatible = [Ci for si, Ci in zip(s, C) if 0 < si <= ru]
        M = max(compatible) if compatible else None
        Bu = P0 if M is None else max(P0, M)
        B.append(Bu)
        rows.append((ru, P0, M, Bu))

    assert rows[:5] == [(5, 7, 8, 8)] * 5
    assert rows[5:16] == [(4, 6, 8, 8)] * 11
    assert rows[16:] == [(1, 3, None, 3)] * 7

    rhs = sum(B)
    lhs = 2 * Q
    gap = lhs - rhs

    assert rhs == 149
    assert lhs == 160
    assert gap == 11
    assert lhs > rhs

    print("PASS global endpoint-orientation cut replay")
    print(f"Q={Q}, 2Q={lhs}, sum B_u={rhs}, deficiency={gap}")
    print("types: rho=5 -> B=8 (x5); rho=4 -> B=8 (x11); rho=1 -> B=3 (x7)")
    print("Conclusion: the scalar staircase witness cannot extend to these coupled canonical margins.")


if __name__ == "__main__":
    main()
