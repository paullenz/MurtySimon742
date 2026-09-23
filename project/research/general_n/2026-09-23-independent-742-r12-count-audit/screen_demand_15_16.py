import json
import sys


def partitions(total, max_part=None):
    if total == 0:
        yield ()
        return
    if max_part is None or max_part > total:
        max_part = total
    for first in range(max_part, 0, -1):
        for rest in partitions(total - first, first):
            yield (first,) + rest


def f(x, rho):
    return x * (rho + 1) + x * (x - 1) // 2


def best_pattern(part, Delta, rho, Dmax):
    base = sum(f(d, rho) for d in part)
    best = None
    # For fixed h_max, additive slack is minimized by leaving every label at
    # x_i=d_i except one label which attains h_max.
    for hmax in range(max(part), Delta + 1):
        for j, d in enumerate(part):
            if (hmax - d) % 2:
                continue
            x = (hmax + d) // 2
            # Positive witness count requires a B-source, hence h_i<Delta.
            if not (d <= x and 2 * x - d <= Delta - 1):
                continue
            if x > (Delta - hmax) * (Delta - 2):
                continue
            rhs = base - f(d, rho) + f(x, rho)
            margin = hmax * Dmax - rhs
            item = {
                "partition": list(part), "h_max": hmax,
                "attaining_part_index": j, "attaining_demand": d,
                "attaining_x": x, "rhs": rhs,
                "X": sum(part) - d + x,
                "lhs_budget": hmax * Dmax, "margin": margin,
            }
            if best is None or margin > best["margin"]:
                best = item
    return best


def main():
    nmax = int(sys.argv[1])
    p15 = list(partitions(15))
    p16 = [p for p in partitions(16) if min(p) >= 2]
    rows = []
    first_survivor = None
    all_excluded_through = 0
    for n in range(6, nmax + 1):
        n_has = False
        for Delta in range(n // 2 + 1, n):
            if 429 * Delta >= 250 * n:
                continue
            rho = 2 * Delta - n
            Dmax = n * rho // 2 - 2 if n % 2 == 0 else (n * rho - 3) // 2
            survivors = []
            for total, pats in ((15, p15), (16, p16)):
                for p in pats:
                    a = n - 1 - Delta
                    if len(p) > a:
                        continue
                    b = best_pattern(p, Delta, rho, Dmax)
                    if (b is not None and b["margin"] >= 0
                            and b["X"] <= Delta * (Delta - 1) // 2):
                        survivors.append({"total": total, **b})
            row = {
                "n": n, "Delta": Delta, "rho": rho, "Dmax": Dmax,
                "survivor_count": len(survivors),
                "best_survivors": sorted(
                    survivors, key=lambda z: z["margin"], reverse=True
                )[:8],
            }
            rows.append(row)
            if survivors:
                n_has = True
                if first_survivor is None:
                    first_survivor = row
        if not n_has and first_survivor is None:
            all_excluded_through = n
    result = {
        "screen": "demand-15/16 plus multiplicity-compressed multi-star inequality",
        "n_range": [6, nmax],
        "partition_counts": {"15": len(p15), "16_no_ones": len(p16)},
        "all_live_strip_rows_excluded_through_n": all_excluded_through,
        "first_survivor": first_survivor,
        "rows": rows,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
