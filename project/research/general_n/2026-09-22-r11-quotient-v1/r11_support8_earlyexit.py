#!/usr/bin/env python3
"""Bounded early-exit exact supplement search for the 16 support-eight kernels."""
import itertools
import json
import multiprocessing as mp
import time

ROWS = json.load(open("r11_support8_sources_case2.json"))["feasible_rows"]
DEADLINE_SECONDS = 180
NODE_LIMIT = 5_000_000


def solve(item):
    index, row = item
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
    patterns.sort(key=lambda p: (sum(p[1]), -sum(p[0]), p[2]))
    started = time.monotonic()
    nodes = 0
    leaves = 0
    witness = None
    truncated = False

    def supplement_ok(population):
        left_sets = [
            {i for i, state in enumerate(source) if state == 1}
            for source in population
        ]
        for u in range(len(population)):
            for i in left_sets[u]:
                if len(left_sets[u]) == 1:
                    continue
                if not any(
                    w != u
                    and population[w][i] == 0
                    and all(population[w][j] != 0 for j in left_sets[u] if j != i)
                    and all(population[u][j] != 0 for j in left_sets[w])
                    for w in range(len(population))
                ):
                    return False
        return True

    def search(start, rem, covered, chosen):
        nonlocal nodes, leaves, witness, truncated
        nodes += 1
        if nodes > NODE_LIMIT or time.monotonic() - started > DEADLINE_SECONDS:
            truncated = True
            return True
        if not any(rem):
            leaves += 1
            if all(covered[i] >= need[i] for i in range(k)) and supplement_ok(chosen):
                witness = tuple(chosen)
                return True
            return False
        pivot = next(i for i, value in enumerate(rem) if value)
        for q in range(start, len(patterns)):
            zero, left, state = patterns[q]
            if not zero[pivot] or any(zero[i] > rem[i] for i in range(k)):
                continue
            if search(
                q,
                tuple(rem[i] - zero[i] for i in range(k)),
                tuple(covered[i] + left[i] for i in range(k)),
                chosen + [state],
            ):
                return True
        return False

    search(0, residual, (0,) * k, [])
    return {
        "index": index,
        "mask": row["mask"],
        "R": residual,
        "status": "FOUND" if witness is not None else ("TRUNCATED" if truncated else "EXHAUSTED"),
        "nodes": nodes,
        "leaves": leaves,
        "seconds": round(time.monotonic() - started, 6),
        "witness": witness,
    }


if __name__ == "__main__":
    with mp.Pool(8) as pool:
        rows = list(pool.imap_unordered(solve, enumerate(ROWS), chunksize=1))
    rows.sort(key=lambda row: row["index"])
    print(json.dumps({
        "kernels": len(rows),
        "found": sum(row["status"] == "FOUND" for row in rows),
        "exhausted": sum(row["status"] == "EXHAUSTED" for row in rows),
        "truncated": sum(row["status"] == "TRUNCATED" for row in rows),
        "rows": rows,
        "scope": "Exact DFS when EXHAUSTED; FOUND gives an abstract source/supplement witness; TRUNCATED is undecided. Not graph realization.",
    }, indent=2))
