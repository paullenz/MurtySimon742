# Exact optimistic equality-core census at `r=8`

Trust level: internal exact computation of necessary profile conditions. Candidates are not asserted graph-realizable.

After the previously proved all-unit equality exclusion, unit-cycle exclusion, local selected-demand injection, exact equality slack, and colour-preserving canonicalization, the `r=8`, `f=r` boundary contains 26,838 labelled candidates in **203 exact orbits**:

| Residual partition | labelled candidates | exact orbits |
|---|---:|---:|
| `(5,1,1,1)` | 7 | 3 |
| `(4,1,1,1,1)` | 45 | 5 |
| `(3,2,1,1,1)` | 64 | 21 |
| `(3,1,1,1,1,1)` | 825 | 15 |
| `(2,2,2,1,1)` | 27 | 6 |
| `(2,2,1,1,1,1)` | 2,815 | 95 |
| `(2,1,1,1,1,1,1)` | 23,055 | 58 |

All other partitions have zero candidates. The canonicalizer recomputes vertex-indexed `P`, degrees and selected lower bounds on each canonical edge representative; it does not reuse data from a pre-canonical label order.

This is a finite handoff, not an equality theorem. The next filters are exact physical-source feasibility and supplement forcing; balanced complete bipartite equality at `S=8` remains a mandatory positive control outside any attempted exclusion.
