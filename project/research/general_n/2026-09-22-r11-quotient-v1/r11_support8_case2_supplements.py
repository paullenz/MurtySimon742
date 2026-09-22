#!/usr/bin/env python3
"""Exact source-population and one-supplement forcing for 16 r=11 kernels."""
import itertools
import json
import multiprocessing as mp

ROWS = json.load(open("r11_support8_sources_case2.json"))["feasible_rows"]


def run(row):
    residual = tuple(row["R"])
    edges = [tuple(e) for e in row["edges"]]
    k = len(residual)
    neigh = [set() for _ in residual]
    degree = [0] * k
    for i, j in edges:
        neigh[i].add(j)
        neigh[j].add(i)
        degree[i] += 1
        degree[j] += 1
    need = tuple(max(0, degree[i] - residual[i]) for i in range(k))
    patterns = []
    for state in itertools.product(range(3), repeat=k):
        left = {i for i, s in enumerate(state) if s == 1}
        zero = {i for i, s in enumerate(state) if s == 2}
        if not zero:
            continue
        if any(not neigh[i] <= left | zero or len(neigh[i] & left) > residual[i]
               for i in left):
            continue
        patterns.append((
            tuple(int(i in zero) for i in range(k)),
            tuple(int(i in left) for i in range(k)),
            state,
        ))
    populations = []

    def search(start, rem, covered, chosen):
        if not any(rem):
            if all(covered[i] >= need[i] for i in range(k)):
                populations.append(tuple(chosen))
            return
        for q in range(start, len(patterns)):
            zero, left, state = patterns[q]
            if all(zero[i] <= rem[i] for i in range(k)):
                search(
                    q,
                    tuple(rem[i] - zero[i] for i in range(k)),
                    tuple(covered[i] + left[i] for i in range(k)),
                    chosen + [state],
                )

    search(0, residual, (0,) * k, [])

    def supplement_ok(population):
        left_sets = [
            {i for i, state in enumerate(source) if state == 1}
            for source in population
        ]
        for u in range(len(population)):
            for i in left_sets[u]:
                possible = len(left_sets[u]) == 1
                for w in range(len(population)):
                    if w == u:
                        continue
                    forced = {
                        (u, j) for j in left_sets[u] if population[w][j] == 0
                    } | {
                        (w, j) for j in left_sets[w] if population[u][j] == 0
                    }
                    possible |= forced == {(u, i)}
                if not possible:
                    return False
        return True

    survivors = [p for p in populations if supplement_ok(p)]
    return {
        "mask": row["mask"],
        "R": residual,
        "edges": edges,
        "degrees": degree,
        "need": need,
        "patterns": len(patterns),
        "source_multisets": len(populations),
        "supplement_feasible": len(survivors),
        "source_examples": populations[:3],
        "supplement_examples": survivors[:3],
    }


if __name__ == "__main__":
    with mp.Pool(8) as pool:
        rows = list(pool.imap_unordered(run, ROWS, chunksize=1))
    rows.sort(key=lambda row: (row["mask"], row["R"]))
    print(json.dumps({
        "kernels": len(rows),
        "source_multisets": sum(row["source_multisets"] for row in rows),
        "supplement_feasible_kernels": sum(row["supplement_feasible"] > 0 for row in rows),
        "supplement_feasible_multisets": sum(row["supplement_feasible"] for row in rows),
        "rows": rows,
        "scope": "Exact inherited one-supplement forcing test on all source multisets; internal computer-assisted result, not graph realization.",
    }, indent=2))
