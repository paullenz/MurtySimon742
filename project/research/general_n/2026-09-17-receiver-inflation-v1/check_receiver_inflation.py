#!/usr/bin/env python3
from math import comb


def exact_row_extrema(h, u, k, q):
    """Exact row-load relaxation for N=h+u rows with entries 0..k.

    Among profiles with total selected mass at least k*h, return
    (maximum number of q-light rows, minimum mass on q-heavy rows).
    The two extrema need not be attained by the same profile.
    """
    N = h + u
    max_total = N * k
    neg = -10**9
    inf = 10**9
    max_light = [neg] * (max_total + 1)
    min_heavy = [inf] * (max_total + 1)
    max_light[0] = 0
    min_heavy[0] = 0
    current_max = 0

    for _ in range(N):
        next_light = [neg] * (max_total + 1)
        next_heavy = [inf] * (max_total + 1)
        for total in range(current_max + 1):
            if max_light[total] == neg and min_heavy[total] == inf:
                continue
            for row in range(k + 1):
                nt = total + row
                if max_light[total] != neg:
                    next_light[nt] = max(
                        next_light[nt],
                        max_light[total] + (1 if row <= q else 0),
                    )
                if min_heavy[total] != inf:
                    next_heavy[nt] = min(
                        next_heavy[nt],
                        min_heavy[total] + (row if row >= q + 1 else 0),
                    )
        max_light, min_heavy = next_light, next_heavy
        current_max += k

    feasible = range(k * h, max_total + 1)
    return (
        max(max_light[t] for t in feasible),
        min(min_heavy[t] for t in feasible),
    )


def closed_bounds(h, u, k, q):
    N = h + u
    ell = min(N, (k * u) // (k - q))
    heavy_mass = k * h - q * ell
    y = max(0, heavy_mass - comb(N, 2))
    z = (y + N - 1) // N if y else 0
    penalty = (q - 1) * z
    return ell, heavy_mass, y, z, penalty


def main():
    checks = 0
    best_examples = {}
    for h in range(2, 16):
        for u in range(0, 6):
            for k in range(1, 16):
                best = (0, None)
                for q in range(1, min(h - 1, k - 1) + 1):
                    exact_light, exact_heavy = exact_row_extrema(h, u, k, q)
                    ell, heavy_mass, y, z, penalty = closed_bounds(h, u, k, q)
                    assert exact_light <= ell, (h, u, k, q, exact_light, ell)
                    assert exact_heavy >= heavy_mass, (
                        h, u, k, q, exact_heavy, heavy_mass
                    )
                    if penalty > best[0]:
                        best = (penalty, q)
                    checks += 1
                if k == h and 5 <= h <= 12 and 0 <= u <= 3:
                    best_examples[(h, u)] = best

    assert checks == 6090, checks
    print(f"PASS {checks} parameter/threshold checks")
    print("best receiver penalties for k=h:")
    for h in range(5, 13):
        row = [best_examples[(h, u)][0] for u in range(4)]
        print(h, row)


if __name__ == "__main__":
    main()
