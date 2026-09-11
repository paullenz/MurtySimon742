#!/usr/bin/env python3
"""Exact audit for the hand n=30, Delta=16, m=226 profile/row reduction.

This is deliberately a small arithmetic audit, not an exhaustive demand
multiset search. It checks the finite local inequalities and tiny tail-count
tables used by N30_M226_HAND_PROFILE_REDUCTION.md.

No solver, floating point, graph enumeration, or 5,200,300-profile sweep is
used.
"""
from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path
import json

A = 13
B = 16


def cap(h: int, z: int) -> int:
    return (z * (z - 1) + h * (h + 1)) // 2


def g(h: int, W: int) -> int:
    if W == 0:
        return 0
    for z in range(h, B + 1):
        if W <= cap(h, z):
            return z
    raise ValueError((h, W))


def D_of(vals):
    vals = tuple(vals)
    D = 0
    for h in range(2, A):
        Nh = sum(v >= h for v in vals)
        Wh = sum(v for v in vals if v >= h)
        D += Nh - g(h, Wh)
    return D


def tail_hist(zs):
    """Convert z_h=#{rho>=h}, h>=2, with b=16 positive residual vertices."""
    maxh = max(zs, default=1)
    z = {h: zs.get(h, 0) for h in range(2, maxh + 2)}
    counts = {1: B - z.get(2, 0)}
    for h in range(2, maxh + 1):
        counts[h] = z.get(h, 0) - z.get(h + 1, 0)
    return tuple((h, counts[h]) for h in sorted(counts) if counts[h])


def main():
    ap = ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    checks = {}

    # High tails h>=8 have d_h<=0 for thirteen labels.
    high_tail = []
    for h in range(8, 13):
        defects = []
        for e in range(0, 14 - h):
            defect2 = -e * e + 3 * e + 2 * h - 2
            defects.append(defect2)
            assert defect2 > 0
        high_tail.append({"h": h, "twice_capacity_defects": defects})
    checks["high_tail_h_ge_8"] = True

    # Clip 7 -> 6. Only k=13 has positive d_7, and g_6 drops by one.
    clip7 = []
    for k in range(1, 14):
        d7 = k - g(7, 7 * k)
        if k <= 12:
            assert d7 <= 0
        else:
            assert d7 == 1
            assert g(6, 7 * k) - g(6, 6 * k) >= 1
        clip7.append({"k": k, "d7": d7})
    checks["clip_7_to_6"] = True

    # Clip 6 -> 5. Only k=11,12,13 have positive d_6.
    clip6 = []
    for k in range(1, 14):
        d6 = k - g(6, 6 * k)
        if d6 <= 0:
            continue
        assert k in (11, 12, 13) and d6 == 1
        for l in range(0, 14 - k):
            drop5 = g(5, 6 * k + 5 * l) - g(5, 5 * (k + l))
            assert drop5 >= 1
            clip6.append({"k": k, "l": l, "d6": d6, "g5_drop": drop5})
    checks["clip_6_to_5"] = True

    # Clip 5 -> 4. g4 pays all positive d5 except one extra unit for k=12,13,
    # where g3 supplies the remaining unit.
    clip5 = []
    for k in range(1, 14):
        d5 = k - g(5, 5 * k)
        if d5 <= 0:
            continue
        assert k in (10, 11, 12, 13)
        for l in range(0, 14 - k):
            drop4 = g(4, 5 * k + 4 * l) - g(4, 4 * (k + l))
            extra = 0
            if k == 12 and l == 0:
                extra = min(
                    g(3, 60 + (3 if v == 3 else 0))
                    - g(3, 48 + (3 if v == 3 else 0))
                    for v in (2, 3)
                )
            elif k == 12 and l == 1:
                extra = g(3, 64) - g(3, 52)
            elif k == 13:
                extra = g(3, 65) - g(3, 52)
            assert drop4 + extra >= d5
            clip5.append(
                {
                    "k": k,
                    "l": l,
                    "d5": d5,
                    "g4_drop": drop4,
                    "guaranteed_g3_drop": extra,
                }
            )
    checks["clip_5_to_4"] = True

    # At cap 4, every entry is 2,3,4. Let y=N3 and z=N4.
    cap4_rows = []
    high_pairs = []
    for y in range(14):
        for z in range(y + 1):
            W2 = 26 + y + z
            W3 = 3 * y + z
            W4 = 4 * z
            gs = (g(2, W2), g(3, W3) if W3 else 0, g(4, W4) if W4 else 0)
            D = (13 - gs[0]) + (y - gs[1]) + (z - gs[2])
            row = {"N3": y, "N4": z, "D": D, "g2_g3_g4": list(gs)}
            cap4_rows.append(row)
            if D >= 7:
                high_pairs.append(row)

    expected_pairs = [
        (11, 0, 7, (9, 8, 0)),
        (12, 0, 7, (9, 9, 0)),
        (13, 0, 8, (9, 9, 0)),
        (13, 9, 7, (10, 10, 8)),
        (13, 11, 7, (11, 10, 9)),
        (13, 12, 7, (11, 10, 10)),
        (13, 13, 7, (11, 11, 10)),
    ]
    got_pairs = [
        (r["N3"], r["N4"], r["D"], tuple(r["g2_g3_g4"])) for r in high_pairs
    ]
    assert got_pairs == expected_pairs
    checks["cap4_105_tail_pairs"] = True

    # A cap-5 preimage of one of the four high-z cap4 profiles cannot contain
    # a five while retaining D>=7.
    preimage_max = {}
    for z in (9, 11, 12, 13):
        vals_D = []
        for k in range(1, z + 1):
            vals = [3] * (13 - z) + [4] * (z - k) + [5] * k
            vals_D.append({"fives": k, "D": D_of(vals)})
        preimage_max[z] = max(x["D"] for x in vals_D)
        assert preimage_max[z] <= 6
    assert preimage_max == {9: 4, 11: 5, 12: 6, 13: 6}
    checks["cap5_preimages_with_fives"] = True

    # Therefore these are exactly the original D>=7 profiles.
    profiles = [
        (2,) * 2 + (3,) * 11,
        (2,) + (3,) * 12,
        (3,) * 13,
        (3,) * 4 + (4,) * 9,
        (3,) * 2 + (4,) * 11,
        (3,) + (4,) * 12,
        (4,) * 13,
    ]
    profile_rows = []
    for vals in profiles:
        D = D_of(vals)
        Q = 13 + D
        zmin = {}
        for h in range(2, 13):
            W = sum(v for v in vals if v >= h)
            if W:
                zmin[h] = g(h, W)
        profile_rows.append(
            {
                "s": list(vals),
                "D": D,
                "Q": Q,
                "zmin": {str(h): z for h, z in zmin.items()},
            }
        )
    assert [x["D"] for x in profile_rows] == [7, 7, 8, 7, 7, 7, 7]
    assert [x["Q"] for x in profile_rows] == [20, 20, 21, 20, 20, 20, 20]
    checks["seven_original_profiles"] = True

    # Convert tight threshold tails to residual rows. Six Q=20 profiles are
    # completely tight. For 3^13, one unit of slack yields exactly three tail
    # sequences: ledger slack, z2+1, or a new z4=1.
    residual_rows = []

    for vals in profiles:
        if vals == (3,) * 13:
            continue
        zs = {}
        for h in range(2, 13):
            W = sum(v for v in vals if v >= h)
            if W:
                zs[h] = g(h, W)
        hist = tail_hist(zs)
        r = sum(h * m for h, m in hist)
        residual_rows.append((vals, hist, r))

    s333 = (3,) * 13
    for zs in ({2: 9, 3: 9}, {2: 10, 3: 9}, {2: 9, 3: 9, 4: 1}):
        hist = tail_hist(zs)
        r = sum(h * m for h, m in hist)
        residual_rows.append((s333, hist, r))

    def key(row):
        vals, hist, r = row
        return (vals, hist, r)

    residual_rows = sorted(residual_rows, key=key)
    expected_residual = sorted(
        [
            ((2,) * 2 + (3,) * 11, ((1, 7), (2, 1), (3, 8)), 33),
            ((2,) + (3,) * 12, ((1, 7), (3, 9)), 34),
            ((3,) * 13, ((1, 7), (3, 9)), 34),
            ((3,) * 13, ((1, 7), (3, 8), (4, 1)), 35),
            ((3,) * 13, ((1, 6), (2, 1), (3, 9)), 35),
            ((3,) * 4 + (4,) * 9, ((1, 6), (3, 2), (4, 8)), 44),
            ((3,) * 2 + (4,) * 11, ((1, 5), (2, 1), (3, 1), (4, 9)), 46),
            ((3,) + (4,) * 12, ((1, 5), (2, 1), (4, 10)), 47),
            ((4,) * 13, ((1, 5), (3, 1), (4, 10)), 48),
        ],
        key=key,
    )
    assert residual_rows == expected_residual
    checks["exact_nine_residual_rows"] = True

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": "n30-m226-hand-profile-reduction-exact-v1",
        "status": status,
        "scope": {"n": 30, "Delta": 16, "m": 226, "a": 13, "b": 16, "t": 2},
        "solver_used": False,
        "floating_point_used": False,
        "full_5200300_profile_sweep_used": False,
        "checks": checks,
        "high_tail": high_tail,
        "clip6_table": clip6,
        "clip5_table": clip5,
        "cap4_high_pairs": high_pairs,
        "cap5_preimage_max_D": {str(k): v for k, v in preimage_max.items()},
        "seven_profiles": profile_rows,
        "nine_residual_rows": [
            {
                "s": list(vals),
                "rho_histogram": {str(h): m for h, m in hist},
                "r": r,
            }
            for vals, hist, r in residual_rows
        ],
        "conclusion": (
            "The local clipping obligations, the 105 cap-4 tail pairs, the "
            "cap-5 preimage exclusions, the seven Q>=20 profiles, and the "
            "nine residual rows all match the hand reduction."
        ),
    }
    text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text, end="")
    if status != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
