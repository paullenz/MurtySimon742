# n=18 exact-star stable-index suffix 40,251--42,250

24 September 2026. Four disjoint exact-small-star v4 shards tested the next
2,000 scalar candidates after the prefix through 40,250.

| stable-index range | survivors | closest deficit gap over `Dmax=16` |
|---|---:|---:|
| 40,251--40,750 | 0 | +11 |
| 40,751--41,250 | 0 | +11 |
| 41,251--41,750 | 0 | +8 |
| 41,751--42,250 | 0 | +9 |

All four shards emitted `FINAL`, with no timeout and no abstract survivor.
The closest case in this batch has demand `(4,3,2,2,2,2)`, selected degrees
`(5,4,3,3,3,3)`, and minimum deficit 24.  The internal contiguous prefix now
reaches stable index 42,250, apart from historical index 20,851 independently
excluded by the exact star-five bound.

This remains finite necessary-condition evidence rather than graph
realizability or a proof of the full row.  The next exact suffix begins at
42,251.
