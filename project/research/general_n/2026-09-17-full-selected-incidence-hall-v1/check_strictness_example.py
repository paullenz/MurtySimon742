#!/usr/bin/env python3

"""Replay the E=3 strictness example for FULL_SELECTED_INCIDENCE_HALL.md."""

sources = [
    (3, (1, 3, 0)),
    (2, (4, 6, 1)),
    (5, (4, 3, 5)),
    (1, (4, 3, 7)),
    (7, (4, 3, 8)),
    (5, (5, 7, 1)),
]

labels = [
    (4, (4, 0, 0)),
    (3, (4, 2, 0)),
    (1, (4, 3, 0)),
    (1, (5, 0, 0)),
    (5, (5, 1, 0)),
    (5, (5, 12, 0)),
    (1, (5, 14, 3)),
]


def expanded_sources():
    out = []
    for count, triple in sources:
        out.extend([triple] * count)
    return out


def expanded_labels():
    out = []
    for count, triple in labels:
        out.extend([triple] * count)
    return out


def main():
    ss = expanded_sources()
    ll = expanded_labels()
    assert len(ss) == 23
    assert len(ll) == 20
    assert sum(rho for rho, p, q in ss) == 88
    assert sum(p for rho, p, q in ss) == 95
    assert sum(q for rho, p, q in ss) == 95
    assert sum(1 for rho, p, q in ss if rho >= 5) == 5

    assert sum(1 for s, R, e in ll if s == 5) == 12
    assert sum(R for s, R, e in ll) == 88
    assert sum(e for s, R, e in ll) == 3
    assert sum(s + e for s, R, e in ll) == 95

    for lam, expected_L, expected_W in [
        (0, 940, 940),
        (1, 964, 961),
        (2, 988, 982),
        (3, 1012, 1003),
    ]:
        L = 0
        for s, R, e in ll:
            x = s + e
            C = R + x
            L += x * (C + lam * e)
        W = 0
        for rho, p, q in ss:
            g = max(0, p - rho + 1)
            W += q * (p + q + lam * g)
        assert (L, W) == (expected_L, expected_W)
        assert L >= W

    for h in (1, 2, 3):
        source_load = sum(q for rho, p, q in ss if max(0, p - rho + 1) >= h)
        label_capacity = sum(s + e for s, R, e in ll if e >= h)
        assert source_load == 7
        assert label_capacity == 8
        assert source_load <= label_capacity

    # Local row-packing failure at source (rho,p,q)=(4,3,8).
    rho, p, q = 4, 3, 8
    g = max(0, p - rho + 1)
    w = p + q
    compatible = []
    for idx, (s, R, e) in enumerate(ll):
        x = s + e
        C = R + x
        if s <= rho and e >= g and C >= w:
            compatible.append(idx)
    assert g == 0 and w == 11
    assert compatible == []
    assert q > len(compatible)

    print("PASS_FULL_SELECTED_INCIDENCE_HALL_STRICTNESS")
    print("weighted_ledgers", [(0,940,940),(1,964,961),(2,988,982),(3,1012,1003)])
    print("row_failure", q, "<=", len(compatible), "is false")


if __name__ == "__main__":
    main()
