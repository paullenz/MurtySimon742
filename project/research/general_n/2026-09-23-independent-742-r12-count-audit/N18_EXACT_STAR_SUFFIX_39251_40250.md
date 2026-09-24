# n=18 exact-star stable-index suffix 39,251--40,250

24 September 2026. Four disjoint exact shards replayed the next 1,000 scalar
candidates after the previously closed prefix through 39,250, using
`screen_exact_star_row.py` and the v4 exact-small-star witness model.

| stable-index range | survivors | closest deficit gap over `Dmax=16` |
|---|---:|---:|
| 39,251--39,500 | 0 | +12 |
| 39,501--39,750 | 0 | +10 |
| 39,751--40,000 | 0 | +11 |
| 40,001--40,250 | 0 | +12 |

Each shard emitted a `FINAL` record and HiGHS returned an optimal solution for
every candidate contributing to its closest row.  There were no timeouts and
no abstract survivors.  Combining this with the inherited exact closure
through stable index 39,250 extends the internal contiguous prefix to 40,250,
apart from the historical index 20,851 `(5,5,5)` case, which the exact
star-five inequality now independently excludes at the assigned-witness
interface.

This is finite profile evidence only.  It does not establish where the full
row ends, graph realizability outside the model, equality, or the general
theorem.  The exact next action is the suffix beginning at stable index 40,251.
