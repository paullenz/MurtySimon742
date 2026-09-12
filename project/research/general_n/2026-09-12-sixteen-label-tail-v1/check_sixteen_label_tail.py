#!/usr/bin/env python3
"""Exact verifier for SIXTEEN_LABEL_TAIL.md.

Checks the safe clipping table, all 4,845 max-five terminal quadruples, the
sixteen possible 6->5 equality preimages, and the first inconclusive
independent-interval clipping bound at a=17. No floating point is used.
"""
A = 16


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
    for h in range(2, len(s)):
        vals = [x for x in s if x >= h]
        if vals:
            D += len(vals) - gamma(h, sum(vals))
    return D


def clipping_rows(A0, M):
    rows = []
    for k in range(1, A0 + 1):
        loss = k - gamma(M, M * k)
        if loss <= 0:
            continue
        lo = M * k
        hi = M * k + (M - 1) * (A0 - k)
        gain = 0
        for h in range(2, M):
            gain += min(
                gamma(h, W) - gamma(h, W - k)
                for W in range(lo, hi + 1)
            )
        rows.append((k, loss, gain))
    return rows


def main():
    for h in range(11, A):
        for e in range(A - h + 1):
            assert -e * e + 3 * e + 2 * h - 2 > 0

    expected = {
        10:[(16,1,8)],
        9:[(15,1,5),(16,1,7)],
        8:[(14,1,4),(15,1,6),(16,1,7)],
        7:[(13,1,4),(14,1,5),(15,2,5),(16,2,6)],
        6:[(11,1,1),(12,1,4),(13,1,4),(14,2,4),(15,2,4),(16,3,6)],
    }
    for M in range(10, 5, -1):
        rows = clipping_rows(A, M)
        assert rows == expected[M], (M, rows)
        assert all(g >= l for _, l, g in rows)

    count = 0
    best = -999
    equality = []
    for x in range(A + 1):
        for y in range(x + 1):
            for z in range(y + 1):
                for w in range(z + 1):
                    count += 1
                    W2 = 2*x + y + z + w
                    W3 = 3*y + z + w
                    W4 = 4*z + w
                    W5 = 5*w
                    D = x+y+z+w
                    for h, W in [(2,W2),(3,W3),(4,W4),(5,W5)]:
                        if W:
                            D -= gamma(h, W)
                    if D > best:
                        best = D
                        equality = [(x,y,z,w)]
                    elif D == best:
                        equality.append((x,y,z,w))
    assert count == 4845
    assert best == 13
    assert equality == [(16,16,16,0),(16,16,16,16)]

    vals = []
    for j in range(1, 17):
        vals.append(D_of([5]*(16-j) + [6]*j))
    assert vals == [8,7,8,9,9,10,10,10,9,9,10,10,10,10,9,10]

    # The interval bound is inconclusive; actual compatible clipping is safe.
    rows17 = clipping_rows(17, 6)
    assert (11, 1, 0) in rows17

    print("PASS: sixteen-label arithmetic verified; a=17 interval-bound obstruction reproduced")


if __name__ == "__main__":
    main()
