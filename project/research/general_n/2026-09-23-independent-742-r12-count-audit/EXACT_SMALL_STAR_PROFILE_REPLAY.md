# Exact small-star profile replay

24 September 2026. Status: internal necessary-condition computation plus
previously proved graph-level obstruction. This closes the five listed leading
`n=18, Delta=10` profiles, not the full row and not the general theorem.

## Model change

`witness_deficit_exact_star_milp.py` is a forward copy of the audited
source-union/right-endpoint-budget model.  It replaces only the old generic
star slack by the independently enumerated exact labelled values

    x                 3   4   5   6   7
    exact slack       4   8  14  21  30.

The separately audited lower bound 35 is retained for `x=8` only in the
`(Delta,rho)=(10,2)` row.  No profile feasibility is promoted to graph
realizability.

## Exact replay of the five leading profiles

Here `Dmax=16`.  HiGHS returned an optimal certificate in every row.

| demand `d` | selected degrees `x` | exact slack | minimum deficit | gap |
|---|---|---:|---:|---:|
| `(8,7)` | `(8,7)` | `(35,30)` | 17 | +1 |
| `(8,7)` | `(8,8)` | `(35,35)` | 16 | 0 |
| `(8,6,1)` | `(8,6,1)` | `(35,21,0)` | 19 | +3 |
| `(8,5,2)` | `(8,5,2)` | `(35,14,1)` | 19 | +3 |
| `(5,5,5)` | `(5,5,5)` | `(14,14,14)` | 19 | +3 |

Thus four of the five profiles exceed the strict-counterexample allowance
inside the graph-derived necessary-condition model.  The sole remaining
abstract optimum is `(d,x)=((8,7),(8,8))`; it is already impossible at the
actual graph interface by the proved singleton-source saturation obstruction
in `2026-09-24-demand15-explicit-C-v1/EXPLICIT_C_CAPACITY_DIAGNOSTIC.md`.
Consequently all five audited leading profiles are closed when the exact
small-star computation is combined with that graph-level lemma.

This is stronger and simpler for `(5,5,5)` than the earlier staged explicit
realization exclusion.  It also removes the earlier transfer ambiguity:
the tuple is now impossible at the assigned-witness necessary-condition
interface itself.

## Trust boundary and next action

The result does **not** show that these are every scalar candidate in the
`n=18, Delta=10` row.  The exact next action is a stable-index replay of the
remaining unclosed scalar suffix with the v4 slack table, followed by a direct
graph-realizability analysis of any survivor.  Equality remains separately
controlled only through `S<=8`; `S<=14` remains computer-assisted; balanced
complete bipartite and `X_3` controls are unchanged.
