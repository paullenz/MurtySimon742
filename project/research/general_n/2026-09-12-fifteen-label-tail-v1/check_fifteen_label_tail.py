#!/usr/bin/env python3
"""Exact verifier for FIFTEEN_LABEL_TAIL.md.

Proof-relevant checks:
- high-level nonpositivity arithmetic;
- every safe clipping interval for 9->...->4;
- all 816 terminal (N2,N3,N4) triples;
- equality preimages immediately before 5->4.

No floating point or external solver is used.
"""
from collections import defaultdict

A = 15


def cap(h, z):
    return (z * (z - 1) + h * (h + 1)) // 2


def gamma(h, W):
    if W <= 0:
        return 0
    z = h
    while W > cap(h, z):
        z += 1
    return z


def D_of(s):
    D = 0
    for h in range(2, A):
        vals = [x for x in s if x >= h]
        if vals:
            D += len(vals) - gamma(h, sum(vals))
    return D


def clipping_rows(M):
    rows = []
    for k in range(1, A + 1):
        loss = k - gamma(M, M * k)
        if loss <= 0:
            continue
        lo = M * k
        hi = M * k + (M - 1) * (A - k)
        gain = 0
        for h in range(2, M):
            mindrop = min(
                gamma(h, W) - gamma(h, W - k)
                for W in range(lo, hi + 1)
            )
            gain += mindrop
        rows.append((k, loss, gain))
    return rows


def main():
    # High levels h>=10 are nonpositive in the proof algebra.
    for h in range(10, A):
        for e in range(0, A - h + 1):
            assert -e * e + 3 * e + 2 * h - 2 > 0

    expected = {
        9: [(15, 1, 7)],
        8: [(14, 1, 6), (15, 1, 7)],
        7: [(13, 1, 5), (14, 1, 5), (15, 2, 5)],
        6: [(11, 1, 2), (12, 1, 4), (13, 1, 4), (14, 2, 4), (15, 2, 5)],
        5: [(10, 1, 2), (11, 1, 3), (12, 2, 3), (13, 2, 3), (14, 3, 3), (15, 3, 4)],
    }
    for M in range(9, 4, -1):
        rows = clipping_rows(M)
        assert rows == expected[M], (M, rows)
        assert all(gain >= loss for _, loss, gain in rows)

    # Terminal 816 triples.
    by_z = {}
    equality = []
    count = 0
    for x in range(A + 1):
        for y in range(x + 1):
            for z in range(y + 1):
                count += 1
                W2 = 2 * x + y + z
                W3 = 3 * y + z
                W4 = 4 * z
                D = (
                    x + y + z
                    - (gamma(2, W2) if W2 else 0)
                    - (gamma(3, W3) if W3 else 0)
                    - (gamma(4, W4) if W4 else 0)
                )
                if z not in by_z or D > by_z[z][0]:
                    by_z[z] = (D, x, y)
                if D == 11:
                    equality.append((x, y, z))

    assert count == 816
    assert equality == [(15, 15, 13), (15, 15, 15)]
    expected_by_z = {
        0:(10,15,14),1:(7,15,15),2:(8,15,15),3:(9,15,15),
        4:(9,15,14),5:(9,15,15),6:(9,15,15),7:(8,15,14),
        8:(8,15,14),9:(9,15,14),10:(9,15,15),11:(10,15,15),
        12:(10,15,15),13:(11,15,15),14:(10,15,14),15:(11,15,15),
    }
    assert by_z == expected_by_z

    # Equality preimages just before 5->4.
    pre1 = []
    base1 = [3, 3] + [4] * 13
    for j in range(1, 14):
        s = base1.copy()
        for idx in [i for i, x in enumerate(s) if x == 4][-j:]:
            s[idx] = 5
        s.sort()
        pre1.append(D_of(s))
    assert pre1 == [6,7,8,7,8,8,8,8,8,9,9,9,9]

    pre2 = []
    base2 = [4] * 15
    for j in range(1, 16):
        s = base2.copy()
        for idx in range(15-j, 15):
            s[idx] = 5
        s.sort()
        pre2.append(D_of(s))
    assert pre2 == [7,7,8,9,10,9,9,9,9,9,9,10,9,10,10]

    print("PASS: fifteen-label clipping, 816 terminal triples, and equality preimages verified exactly")


if __name__ == "__main__":
    main()
