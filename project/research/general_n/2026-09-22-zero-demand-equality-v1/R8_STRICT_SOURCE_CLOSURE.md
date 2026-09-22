# Exact physical-source closure of strict `r=8`

Trust level: internally checked, computer-assisted necessary-condition exclusion. This remains inside the independent complement/residual/profile route and is not an externally reviewed proof of the full conjecture.

## Result

Exact colour-preserving quotienting leaves 68 optimistic strict-surplus core orbits. Exact physical-source feasibility eliminates 67 of them. The sole source-feasible orbit is the unique `(2,2,2,1,1)` core, already excluded by exact supplement forcing in `R8_EXAMPLE_AND_22211.md`. Hence the internal finite pipeline now gives

`r=8  =>  t<=0`.

Together with the previously checked `r<=7` strict closure, a strict counterprofile must have `r>=9`. Under the audited edge-translation lemma this extends the internal computer-assisted edge bound from residual demand `S<=9` to **`S<=10`**. This does not settle the live strip or actual graph realizability globally.

## Exact census

| Residual partition | exact core orbits | source-feasible |
|---|---:|---:|
| `(3,2,1,1,1)` | 2 | 0 |
| `(3,1,1,1,1,1)` | 5 | 0 |
| `(2,2,2,1,1)` | 1 | 1 (supplement-infeasible) |
| `(2,2,1,1,1,1)` | 29 | 0 |
| `(2,1,1,1,1,1,1)` | 31 | 0 |

The source DP assigns each physical source a ternary state at every residual label (absent/selected/residual), enforces exact residual-column sums, the selected lower bounds on `P`, local `F`-neighbour containment, and the source-demand injection cap. It memoizes on remaining residual masses and capped selected counts.

## Validation and repair

The full 68-orbit result reproduces the earlier bounded probe: only the unique `(2,2,2,1,1)` representative is source-feasible. During this unit, an index-provenance defect was found in the newly written canonicalizer: a canonical edge mask was initially paired with vertex-indexed degree/`P` data from its pre-canonical labelled representative. The script now recomputes all vertex-indexed data on the canonical mask. Orbit counts are unchanged; the corrected JSON is the only version used by the full source screen.
