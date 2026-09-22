#!/usr/bin/env python3
"""Exact physical-source feasibility for every r=8 strict core orbit."""
import itertools
import json
from functools import lru_cache
from pathlib import Path


data = json.loads(Path("R8_CORE_ORBITS.json").read_text())
out = {}
for partition, entry in data.items():
    if not entry["orbit_representatives"]:
        continue
    R = tuple(int(x.strip()) for x in partition.strip("()").split(",") if x.strip())
    k = len(R)
    rows = []
    for q, rep in enumerate(entry["orbit_representatives"], 1):
        neighbors = [set() for _ in R]
        for i, j in rep["edges"]:
            neighbors[i].add(j)
            neighbors[j].add(i)
        P = set(rep["P"])
        need = tuple(rep["selected_lower_bounds"])
        patterns = []
        for state in itertools.product(range(3), repeat=k):
            L = {i for i, s in enumerate(state) if s == 1}
            Z = {i for i, s in enumerate(state) if s == 2}
            if any(not neighbors[i] <= L | Z or len(neighbors[i] & L) > R[i] for i in L):
                continue
            if not Z:
                assert not (L & P)
                continue
            patterns.append((
                tuple(int(i in Z) for i in range(k)),
                tuple(int(i in L) for i in range(k)),
                state,
            ))

        @lru_cache(None)
        def solve(rem, x):
            if not any(rem):
                return () if all(x[i] >= need[i] for i in range(k)) else None
            for a, (z, l, state) in enumerate(patterns):
                if all(z[i] <= rem[i] for i in range(k)):
                    nr = tuple(rem[i] - z[i] for i in range(k))
                    nx = tuple(min(need[i], x[i] + l[i]) for i in range(k))
                    tail = solve(nr, nx)
                    if tail is not None:
                        return (a,) + tail
            return None

        witness = solve(R, tuple(0 for _ in R))
        rows.append({
            "orbit": q,
            "canonical_mask": rep["mask"],
            "source_feasible": witness is not None,
            "single_source_patterns": len(patterns),
            "memo_states": solve.cache_info().currsize,
            "source_witness_states": [list(patterns[a][2]) for a in witness] if witness is not None else None,
        })
    out[partition] = {
        "orbits_tested": len(rows),
        "source_feasible_orbits": sum(r["source_feasible"] for r in rows),
        "rows": rows,
        "scope": "Exact physical-source necessary condition on colour-preserving core orbits; not graph realizability.",
    }

print(json.dumps(out, indent=2))
