#!/usr/bin/env python3
"""Exact finite replay of ORIENTATION_TARGET_CAPACITY.md for N34 states 77 and 60.

No optimizer is used.  We enumerate exactly the nondecreasing q-partitions used
by the frozen low-demand scanner at E=0 and test the scalar threshold cut

    Q <= sum_{q_u <= k+1} q_u + sum_{q_w+rho_w > k} P_w

at every integer threshold k, with the exact-demand pointwise p caps P_w.
"""

from collections import Counter


def parts(cnt, mx, total, last=0):
    if cnt == 0:
        if total == 0:
            yield ()
        return
    for x in range(last, min(mx, total) + 1):
        rem = total - x
        slots = cnt - 1
        if rem < x * slots or rem > mx * slots:
            continue
        for tail in parts(slots, mx, rem, x):
            yield (x,) + tail


def profile_cut(q2, q3, r1, Q):
    src = [(0, 1)] * r1 + [(q, 2) for q in q2] + [(q, 3) for q in q3]
    caps = []
    for q, rho in src:
        cap = min(17 - q, rho + 2)
        if q > 0:
            cap = min(cap, rho - 1)
        caps.append(max(0, cap))

    cuts = []
    for k in range(18):
        eligible_out = sum(q for q, _rho in src if q <= k + 1)
        high_target_cap = sum(
            cap for (q, rho), cap in zip(src, caps) if q + rho > k
        )
        cuts.append((eligible_out + high_target_cap, k, eligible_out, high_target_cap))
    return min(cuts)


def scan_state(name, n2, n3, r1, r2, r3, S, expected_profiles, expected_maxcut):
    Q = S
    qmax2 = min(13, n2)
    qmax3 = 12
    total = 0
    passing = 0
    max_mincut = -1
    closest = None
    deficit_counts = Counter()
    threshold_counts = Counter()

    for sum2 in range(min(r2 * qmax2, Q) + 1):
        sum3 = Q - sum2
        if sum3 < 0 or sum3 > r3 * qmax3:
            continue
        for q2 in parts(r2, qmax2, sum2):
            for q3 in parts(r3, qmax3, sum3):
                total += 1
                cut, k, eligible_out, high_cap = profile_cut(q2, q3, r1, Q)
                deficit = Q - cut
                if cut >= Q:
                    passing += 1
                deficit_counts[deficit] += 1
                threshold_counts[k] += 1
                if cut > max_mincut:
                    max_mincut = cut
                    closest = (q2, q3, k, eligible_out, high_cap, deficit)

    assert total == expected_profiles, (name, total, expected_profiles)
    assert passing == 0, (name, passing)
    assert max_mincut == expected_maxcut, (name, max_mincut, expected_maxcut)
    assert Q - max_mincut == 6, (name, Q, max_mincut)

    q2, q3, k, eligible_out, high_cap, deficit = closest
    print(
        f"state={name} profiles={total} passing={passing} Q={Q} "
        f"max_min_cut={max_mincut} minimum_deficit={deficit}"
    )
    print(
        f"closest q2={','.join(map(str,q2))} q3={','.join(map(str,q3))} "
        f"threshold={k} eligible_out={eligible_out} high_target_cap={high_cap}"
    )
    print(
        "threshold_witness_counts "
        + " ".join(f"k{k}={threshold_counts[k]}" for k in sorted(threshold_counts))
    )
    return {
        "state": name,
        "profiles": total,
        "passing": passing,
        "Q": Q,
        "max_min_cut": max_mincut,
        "minimum_deficit": deficit,
    }


def main():
    a = scan_state("77", 7, 8, 7, 4, 7, 38, 201670, 32)
    b = scan_state("60", 8, 7, 7, 5, 6, 37, 253001, 31)
    assert a["passing"] == b["passing"] == 0
    print("E0_ORIENTATION_TARGET_CAPACITY PASS")


if __name__ == "__main__":
    main()
