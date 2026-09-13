#!/usr/bin/env python3
"""Independent exhaustive small-system check of the mixed endpoint Hall bound.

This does not verify the whole Murty-Simon bridge.  It checks only the finite
bipartite counting routine added to ENDPOINT_CLASS_PACKING.md: for small source
systems, the threshold lower bound must never exceed the exact minimum endpoint
mass over all simple incidence assignments.
"""
from itertools import combinations, combinations_with_replacement

INF = 10**9


def hall_ok(src, a, b, lam):
    for i in range(a + 1):
        for j in range(b + 1):
            if i == 0 and j == 0:
                continue
            cap = 0
            for q, rho, load in src:
                if q <= 0 or rho < 2:
                    continue
                if lam and load >= lam:
                    continue
                if rho == 2:
                    cap += min(q, i)
                else:
                    cap += min(q, i + j)
            if 2 * i + 3 * j > cap:
                return False
    return True


def joint_lb(src, z2, z3):
    if z2 == 0 and z3 == 0:
        return 0
    if not hall_ok(src, z2, z3, 0):
        return INF
    lb = 2 * z2 + 3 * z3
    max_load = max([3] + [load for q, rho, load in src if q > 0 and rho >= 2])

    # lambda=3 contributes only above the demand-two baseline 2.
    low2 = max(a for a in range(z2 + 1) if hall_ok(src, a, 0, 3))
    lb += z2 - low2

    # lambda>=4 contributes for both demand classes.
    for lam in range(4, max_load + 2):
        low = 0
        for a in range(z2 + 1):
            for b in range(z3 + 1):
                if hall_ok(src, a, b, lam):
                    low = max(low, a + b)
        lb += z2 + z3 - low
    return lb


def exact_min_mass(src, z2, z3):
    n = len(src)
    choices = []
    for _ in range(z2):
        choices.append((2, [c for c in combinations(range(n), 2)
                            if all(src[u][1] >= 2 and src[u][0] > 0 for u in c)]))
    for _ in range(z3):
        choices.append((3, [c for c in combinations(range(n), 3)
                            if all(src[u][1] >= 3 and src[u][0] > 0 for u in c)]))
    if any(not cands for _, cands in choices):
        return INF

    use = [0] * n
    best = INF

    def dfs(k, total):
        nonlocal best
        if total >= best:
            return
        if k == len(choices):
            best = total
            return
        demand, cands = choices[k]
        for cand in cands:
            if all(use[u] < src[u][0] for u in cand):
                for u in cand:
                    use[u] += 1
                endpoint = max([demand] + [src[u][2] for u in cand])
                dfs(k + 1, total + endpoint)
                for u in cand:
                    use[u] -= 1

    dfs(0, 0)
    return best


def main():
    # Canonical small source options: rho in {2,3}, q in {1,2,3},
    # p in [0,rho-1], and endpoint source load L=q+p.
    options = []
    for rho in (2, 3):
        for q in (1, 2, 3):
            for p in range(rho):
                options.append((q, rho, q + p))

    checked = feasible = 0
    for n in range(3, 6):
        # Source order is irrelevant, so enumerate multisets.
        for idxs in combinations_with_replacement(range(len(options)), n):
            src = [options[i] for i in idxs]
            for z2 in range(3):
                for z3 in range(3):
                    if z2 + z3 == 0 or z2 + z3 > 3:
                        continue
                    checked += 1
                    exact = exact_min_mass(src, z2, z3)
                    bound = joint_lb(src, z2, z3)
                    if exact < INF:
                        feasible += 1
                        if bound > exact:
                            raise AssertionError(
                                f"unsound bound: src={src} z2={z2} z3={z3} "
                                f"bound={bound} exact={exact}"
                            )

    print("JOINT_ENDPOINT_HALL_SMALL_CHECK_OK")
    print("systems", checked)
    print("feasible_systems", feasible)


if __name__ == "__main__":
    main()
