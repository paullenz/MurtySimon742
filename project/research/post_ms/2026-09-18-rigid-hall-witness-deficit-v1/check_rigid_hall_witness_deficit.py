#!/usr/bin/env python3
"""Independent arithmetic audit for RIGID_HALL_WITNESS_DEFICIT_AND_ONE_CODE_TRAP.md.

This is diagnostic/audit support only.  It does not prove graph-theoretic premises.
"""

import math
import random
from collections import Counter

SEED = 20260918
random.seed(SEED)


def M(n):
    return ((n - 1) ** 2) // 4 + 1


def rand_comp(n, k):
    if k == 1:
        return [n]
    cuts = sorted(random.sample(range(1, n), k - 1))
    out = []
    prev = 0
    for c in cuts + [n]:
        out.append(c - prev)
        prev = c
    return out


def witness_incidence_audit(trials=20000):
    checked = 0
    for _ in range(trials):
        p = random.randint(3, 25)
        u = random.randint(1, 25)
        lam = random.randint(0, max(0, 2 * p + u - 4))
        a = 2 * p + u - lam - 1
        if a < 4:
            continue
        T0 = a - p
        x = random.randint(3, a - 1)
        y = a - x
        mu = random.randint(0, min(p, x))
        k = max(0, x - mu)
        if k == 0 or k > u:
            continue
        hmax = min(y, u // k)
        if hmax < 1:
            continue
        h = random.randint(1, hmax)
        ys = rand_comp(y, h)

        # Give each represented complement U-code class at least k vertices,
        # then distribute a random subset of the unused U-population.
        uds = [k] * h
        for _j in range(u - h * k):
            if random.random() < 0.5:
                uds[random.randrange(h)] += 1

        total_E = 0
        Zx = 0
        Zy = 0
        for yd, ud in zip(ys, uds):
            t = [0] * ud
            # Every source uses k distinct witnesses.
            for _source in range(yd):
                for j in random.sample(range(ud), k):
                    t[j] += 1
            used = [v for v in t if v]
            g = x - T0
            total_E += sum(max(0, g + v - 1) for v in used)
            Zx += len(used) * (x - 1)
            Zy += sum(used)

        assert Zx >= h * k * (x - 1)
        assert Zy >= y * k

        g = x - T0
        if g >= 1:
            E_floor = k * (y + h * (g - 1))
        else:
            E_floor = max(0, y * k - (1 - g) * u)
        assert total_E >= E_floor

        # Actual AU-edge capacity in this abstract witness system is no larger
        # than the theorem's coarser rigid beta ceiling.
        actual_edge_cap = a * u - (Zx + Zy)
        rigid_beta_cap = a * u - k * (y + h * (x - 1))
        assert actual_edge_cap <= rigid_beta_cap
        checked += 1
    return checked


def qe_minimization_audit(trials=100000):
    for _ in range(trials):
        e0 = random.randint(0, 500)
        D = random.randint(-500, 1000)
        brute = 10**18
        for E in range(e0, max(e0, D) + 3):
            q = max(0, math.ceil((D - E) / 2))
            brute = min(brute, q + E)
        formula = e0 + max(0, math.ceil((D - e0) / 2))
        assert brute == formula
    return trials


def rigid_parameter_scan(pmax=18, umax=18):
    stats = Counter()
    for p in range(3, pmax + 1):
        for u in range(1, umax + 1):
            b = 2 * p + u
            for lam in range(0, b - 3):
                a = b - lam - 1
                if a < 4:
                    continue
                n = 2 * b - lam
                D_M = b * (n - b) - M(n)
                C0 = 2 * (D_M - 1) + lam * (p + u) - p
                if C0 < 0:
                    continue
                T0 = a - p
                # Conservative preserved root-imbalance beta floor only.
                Broot = max(0, p * (lam + 1 - 2 * p))
                for x in range(3, a):
                    y = a - x
                    for mu in range(0, min(p, x) + 1):
                        k = max(0, x - mu)
                        if k == 0 or k > u:
                            continue
                        hmax = min(y, u // k)  # old population condition hk<=u
                        for h in range(1, hmax + 1):
                            stats["old_population_admissible"] += 1
                            g = x - T0
                            if g >= 1:
                                E0 = k * (y + h * (g - 1))
                            else:
                                E0 = max(0, y * k - (1 - g) * u)
                            Z0 = k * (y + h * (x - 1))
                            e_ex = E0 > C0
                            b_ex = Broot + Z0 > a * u
                            if e_ex:
                                stats["U_slack_rejected"] += 1
                            if b_ex:
                                stats["beta_deficit_rejected"] += 1
                            if e_ex or b_ex:
                                stats["union_rejected"] += 1
                            if g >= 1 and k * (p - 1) > C0:
                                stats["base_no_rigid_cut"] += 1
    return stats


def main():
    incidence = witness_incidence_audit()
    qe = qe_minimization_audit()
    scan = rigid_parameter_scan()
    print({
        "seed": SEED,
        "witness_incidence_systems": incidence,
        "qe_integer_minimizations": qe,
        "parameter_scan": dict(scan),
        "failures": 0,
        "trust_boundary": "arithmetic/abstract incidence audit only; graph-theoretic claims are hand-derived",
    })


if __name__ == "__main__":
    main()
