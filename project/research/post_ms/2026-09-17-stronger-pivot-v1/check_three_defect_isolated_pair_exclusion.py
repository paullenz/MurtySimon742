#!/usr/bin/env python3
"""Regression for THREE_DEFECT_ISOLATED_PAIR_EXCLUSION.md.

Evidence only; the universal matching statements are hand code-class calculations.
Uses only the Python standard library.
"""

import json


def build_sigma(p, t, mask):
    k = 3 + sum(p) + 2 * t
    sigma = [[0] * k for _ in range(k)]
    core_edges = [(0, 1), (0, 2), (1, 2)]
    for bit, (i, j) in enumerate(core_edges):
        if (mask >> bit) & 1:
            sigma[i][j] = sigma[j][i] = 1
    nxt = 3
    for i, cnt in enumerate(p):
        for _ in range(cnt):
            sigma[i][nxt] = sigma[nxt][i] = 1
            nxt += 1
    for _ in range(t):
        sigma[nxt][nxt + 1] = sigma[nxt + 1][nxt] = 1
        nxt += 2
    assert nxt == k
    return sigma


def valid_core(p, mask):
    deg = [0, 0, 0]
    for bit, (i, j) in enumerate(((0, 1), (0, 2), (1, 2))):
        if (mask >> bit) & 1:
            deg[i] += 1
            deg[j] += 1
    return all(p[i] + deg[i] != 1 for i in range(3))


def source_code(sigma, source, target, s):
    k = len(sigma)
    sgm = sigma[target][source]
    out = 0
    for h in range(k):
        if h == source:
            val = 1 - s
        elif h == target:
            val = s ^ sgm
        else:
            val = 1 ^ s ^ sigma[source][h]
        out |= val << h
    return out


def qpair_edges(sigma, i, j):
    out = []
    sgm = sigma[i][j]
    for s in (0, 1):
        u = source_code(sigma, j, i, s)
        ss = s ^ sgm
        v = 0
        for h in range(len(sigma)):
            if h == i:
                val = 1 - ss
            elif h == j:
                val = s
            else:
                val = 1 ^ ss ^ sigma[i][h]
            v |= val << h
        out.append((u, v))
    return out


def leaf_vertices(sigma):
    return [i for i, row in enumerate(sigma) if sum(row) == 1]


def V_LL(sigma):
    leaves = leaf_vertices(sigma)
    out = set()
    for ai in range(len(leaves)):
        for bi in range(ai + 1, len(leaves)):
            i, j = leaves[ai], leaves[bi]
            for u, v in qpair_edges(sigma, i, j):
                out.add(u)
                out.add(v)
    return out


def certifies_matching_outside(sigma, qpairs):
    forbidden = V_LL(sigma)
    seen = set()
    for i, j in qpairs:
        for u, v in qpair_edges(sigma, i, j):
            if u == v or u in forbidden or v in forbidden:
                return False
            if u in seen or v in seen:
                return False
            seen.add(u)
            seen.add(v)
    return True


def B_formula(p):
    return (
        2 * sum(max(x - 1, 0) for x in p)
        + 2 * sum(min(p[i], p[j]) for i in range(3) for j in range(i + 1, 3))
    )


def L_formula(p, t):
    g = sum(x > 0 for x in p)
    return B_formula(p) + 4 * t * g + 2 * t * (t - 1) + 1


def main():
    checked = {"case_A": 0, "case_B": 0, "case_C": 0}

    # Case A: t=1,g=1.  Put the pendant group at c=2.
    # a=0,b=1, d=3, isolated pair begins at 3+z.
    for z in range(1, 101):
        p = (0, 0, z)
        valid_masks = [m for m in range(8) if valid_core(p, m)]
        if z >= 2:
            assert valid_masks == [0, 7], (z, valid_masks)
        for mask in valid_masks:
            sigma = build_sigma(p, 1, mask)
            r = 3 + z
            s = r + 1
            qpairs = [(0, 2), (0, 3), (1, r), (1, s)]
            assert certifies_matching_outside(sigma, qpairs), ("A", z, mask)
            k = 3 + z + 2
            assert L_formula(p, 1) + 8 > 2 * k
            checked["case_A"] += 1

    # Case B: t=1,g=2 with smaller positive attachment y=1 or 2.
    # Put the empty exceptional coordinate at a=0 and groups at 1,2.
    for y in (1, 2):
        for z in range(y, 101):
            p = (0, y, z)
            r = 3 + y + z
            s = r + 1
            for mask in range(8):
                if not valid_core(p, mask):
                    continue
                sigma = build_sigma(p, 1, mask)
                qpairs = [(0, r), (0, s)]
                assert certifies_matching_outside(sigma, qpairs), ("B", y, z, mask)
                k = 3 + y + z + 2
                assert L_formula(p, 1) + 4 > 2 * k
                checked["case_B"] += 1

    # Case C: t=2,g=1.  Put the pendant group at c=2.
    for z in range(1, 101):
        p = (0, 0, z)
        valid_masks = [m for m in range(8) if valid_core(p, m)]
        if z >= 2:
            assert valid_masks == [0, 7], (z, valid_masks)
        r = 3 + z
        for mask in valid_masks:
            sigma = build_sigma(p, 2, mask)
            qpairs = [(0, 2), (1, r)]
            assert certifies_matching_outside(sigma, qpairs), ("C", z, mask)
            k = 3 + z + 4
            assert L_formula(p, 2) + 4 > 2 * k
            checked["case_C"] += 1

    summary = {
        "status": "PASS_THREE_DEFECT_ISOLATED_PAIR_EXCLUSION",
        "z_replay_range": [1, 100],
        "matching_certificate_instances": checked,
        "case_A_matching_size": 8,
        "case_B_matching_size": 4,
        "case_C_matching_size": 4,
        "eventual_threshold": 10,
        "scope": "finite regression evidence only; universal matching certificates are hand forced-code calculations",
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
