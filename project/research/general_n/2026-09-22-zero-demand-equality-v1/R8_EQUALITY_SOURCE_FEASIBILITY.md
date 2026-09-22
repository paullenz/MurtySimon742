# Boolean physical-source screen of the `r=8` equality boundary

Trust level: internal exact computation of a necessary condition; not graph realizability and not yet an equality theorem.

Exact physical-source feasibility reduces the 203 equality-core orbits to **39 source-feasible orbits**:

| Residual partition | core orbits | source-feasible |
|---|---:|---:|
| `(5,1,1,1)` | 3 | 3 |
| `(4,1,1,1,1)` | 5 | 0 |
| `(3,2,1,1,1)` | 21 | 9 |
| `(3,1,1,1,1,1)` | 15 | 1 |
| `(2,2,2,1,1)` | 6 | 4 |
| `(2,2,1,1,1,1)` | 95 | 13 |
| `(2,1,1,1,1,1,1)` | 58 | 9 |

The memoized DP enforces exact residual-column sums, selected lower bounds for every `P` label, local `F`-neighbour containment and the per-source selected-neighbour injection cap. It records one physical-source witness for each feasible orbit.

This screen is deliberately boolean. It does not enumerate all source populations and does not apply B-layer supplement forcing. Those are the next finite steps. Balanced complete-bipartite equality at `S=8` remains the mandatory positive control and must not be excluded by any graph-level conclusion.
