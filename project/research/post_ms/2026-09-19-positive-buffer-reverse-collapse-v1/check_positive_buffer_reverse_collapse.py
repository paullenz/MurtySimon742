#!/usr/bin/env python3
"""Arithmetic audit for the positive-buffer r=0 equality repair.

Diagnostic only.  This is not a D2C graph enumerator and does not establish
realizability of any abstract parameter state.  The promoted statements are
the hand criticality arguments in
POSITIVE_BUFFER_REVERSE_COLLAPSE_AND_HEAD_DICHOTOMY.md.

Grid: 3<=p<=18, 1<=u<=18, lambda>=0, all admissible x and positive
buffer slack t=p-g>=1.
"""

from collections import Counter
from math import ceil, floor, sqrt


def M(n):
    return ((n - 1) ** 2) // 4 + 1


def phi(g):
    return g * (g - 1) if g >= 3 else 0


def C0_formula(p, u, lam):
    H = ((lam + 1) ** 2) // 4
    return (lam + 3) * p + (lam + 2) * u - 2 * H - 4


def C0_from_M(p, u, lam):
    b = 2 * p + u
    n = 2 * b - lam
    DM = b * (n - b) - M(n)
    return 2 * (DM - 1) + lam * (p + u) - p


def rcode(S, p, u, lam):
    D0 = 5 * p + 5 * u - 3 * lam - 2
    return floor((D0 + sqrt(D0 * D0 + 12 * S)) / 3)


def ccap(S, p, u, lam, g):
    # One-code purity gives h_P=0.
    L = lam + 1
    return rcode(S, p, u, lam) * (g + 2 * S / L)


def predecessor_floor(p, x, y, g):
    """Safe r=0 equality floor before this repair."""
    k = x - g
    t = p - g
    return k * (p + k - 1) + t + max(phi(g), y * (t + 1))


def repaired_data(p, u, lam, x, y, g):
    """Pure structural consequences after matched-channel collapse."""
    k = x - g
    t = p - g
    assert k > 0 and t > 0

    # Every buffer--X edge is outside-U certified.
    ell = x

    # The g matched-crossing heads have singleton A-code classes, hence their
    # outside witnesses are pairwise distinct and cannot serve a core head.
    # The nonempty k-core needs at least one further witness.
    m = g + 1

    # Every core head is outside certified and forces its own core--outside hole.
    Ecore = k * (p + k)

    # For an outside witness serving tau heads,
    # eps >= [p-x+tau]_+ = [t-k+tau]_+.
    # The g H_M witnesses have tau=1.  The core block has total load k.
    if k <= t:
        Eout = t + g * (t - k + 1)
    else:
        Eout = 0

    LY = y * (p + 2)  # t+1+m = t+g+2 = p+2

    Sfloor = Ecore + t + Eout + max(phi(g), LY)

    # A--U holes:
    # k(x-1) from the core, y(k+1) to core+buffer,
    # y(g+1) to distinct outside witnesses, and x chosen head-witness nonedges.
    Zfloor = k * (x + y) + y * (g + 2) + g

    return {
        "k": k,
        "t": t,
        "ell": ell,
        "m": m,
        "Ecore": Ecore,
        "Eout": Eout,
        "LY": LY,
        "Sfloor": Sfloor,
        "Zfloor": Zfloor,
        "population_ok": u >= x + 2,  # u_o=u-k-1 >= g+1
    }


def scan():
    stats = Counter()
    rejection_examples = []
    q_examples = []

    for p in range(3, 19):
        for u in range(1, 19):
            b = 2 * p + u
            for lam in range(0, b - 3):
                a = b - lam - 1
                if a < 4:
                    continue

                C0 = C0_formula(p, u, lam)
                assert C0 == C0_from_M(p, u, lam)
                if C0 < 0:
                    continue

                D0 = 5 * p + 5 * u - 3 * lam - 2

                for x in range(3, a):
                    y = a - x

                    for g in range(0, p):  # t=p-g>=1
                        k = x - g
                        t = p - g
                        if k <= 0 or k + 1 > u:
                            continue

                        old = predecessor_floor(p, x, y, g)
                        if old > C0:
                            continue

                        stats["predecessor_positive_buffer_r0_possible"] += 1
                        if t == 1:
                            stats["predecessor_t1_possible"] += 1

                        data = repaired_data(p, u, lam, x, y, g)

                        if not data["population_ok"]:
                            stats["rejected_by_unmatched_population"] += 1
                            if t == 1:
                                stats["t1_rejected_by_unmatched_population"] += 1
                            if len(rejection_examples) < 12:
                                rejection_examples.append(
                                    {
                                        "reason": "u<x+2",
                                        "p": p, "u": u, "lambda": lam,
                                        "x": x, "y": y, "g": g,
                                        "k": k, "t": t, "C0": C0,
                                    }
                                )
                            continue

                        if data["Sfloor"] > C0:
                            stats["rejected_by_repaired_score_floor_after_population"] += 1
                            if t == 1:
                                stats["t1_rejected_by_score_after_population"] += 1
                            if len(rejection_examples) < 12:
                                rejection_examples.append(
                                    {
                                        "reason": "Sfloor>C0",
                                        "p": p, "u": u, "lambda": lam,
                                        "x": x, "y": y, "g": g,
                                        "k": k, "t": t, "C0": C0,
                                        "old_floor": old,
                                        "new_floor": data["Sfloor"],
                                    }
                                )
                            continue

                        stats["repaired_structural_survivors"] += 1
                        if t == 1:
                            stats["t1_repaired_structural_survivors"] += 1

                        # Rooted-triangle feedback using E_U<=C0.
                        D = data["Zfloor"] - u * (p - lam)
                        qmin = max(0, ceil((D - C0) / 2))
                        if qmin > 0:
                            stats["survivors_forcing_positive_q"] += 1
                            stats["max_forced_q"] = max(stats["max_forced_q"], qmin)
                            if len(q_examples) < 12:
                                q_examples.append(
                                    {
                                        "p": p, "u": u, "lambda": lam,
                                        "x": x, "y": y, "g": g,
                                        "k": k, "t": t,
                                        "D": D, "C0": C0, "q_min": qmin,
                                    }
                                )

                        # Exact relaxed intersection with the audit-mandated
                        # local pair inequalities.  Eout lies outside P, so
                        # S_P<=C0-Eout.  Ccap and the maximum possible L_Y are
                        # monotone in S_P; testing this upper endpoint is exact
                        # for this relaxed local system.
                        Sbar = C0 - data["Eout"]
                        pair_base = data["Ecore"] + t
                        assert Sbar >= pair_base + data["LY"]
                        cap = ccap(Sbar, p, u, lam, g)

                        crossing_ok = 2 * x * y <= cap + 1e-12
                        one_ok = (
                            cap + (Sbar - pair_base)
                            >= y * (p + x + k) - 1e-12
                        )
                        crowd_rhs = max(0, y * (3 * y - D0))
                        crowd_ok = Sbar >= crowd_rhs

                        if crossing_ok and one_ok and crowd_ok:
                            stats["pair_relaxation_survivors"] += 1
                        else:
                            stats["additional_pair_relaxation_rejections"] += 1

    expected = {
        "predecessor_positive_buffer_r0_possible": 320525,
        "predecessor_t1_possible": 20178,
        "rejected_by_unmatched_population": 146603,
        "t1_rejected_by_unmatched_population": 12307,
        "rejected_by_repaired_score_floor_after_population": 40087,
        "t1_rejected_by_score_after_population": 2056,
        "repaired_structural_survivors": 133835,
        "t1_repaired_structural_survivors": 5815,
        "survivors_forcing_positive_q": 7274,
        "max_forced_q": 48,
        "pair_relaxation_survivors": 133835,
        "additional_pair_relaxation_rejections": 0,
    }

    mismatches = {
        key: {"expected": value, "actual": stats[key]}
        for key, value in expected.items()
        if stats[key] != value
    }

    print(
        {
            "scan": dict(stats),
            "expected_mismatches": mismatches,
            "rejection_examples": rejection_examples,
            "positive_q_examples": q_examples,
            "failures": len(mismatches),
            "trust_boundary": (
                "integer diagnostic only; no graph-realizability claim. "
                "The no-reverse theorem, total matched-channel collapse, "
                "head-code singleton theorem, outside-witness population bound, "
                "core-hole bill and residual inequalities are hand proofs."
            ),
        }
    )


if __name__ == "__main__":
    scan()
