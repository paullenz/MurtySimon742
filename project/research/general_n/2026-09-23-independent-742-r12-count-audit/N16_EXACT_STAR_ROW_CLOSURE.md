# n=16, Delta=9 exact-small-star v4 row ledger

24 September 2026, 08:00 scheduled session. This is an incremental finite
necessary-condition ledger. It is not a graph-realizability theorem or a
proof of the general Murty--Simon conjecture.

## Stable indices 1--200

The previously interrupted prefix was replayed to a `FINAL` record:

| stable-index range | survivors | closest deficit gap over `Dmax=14` |
|---|---:|---:|
| 1--200 | 0 | +5 |

All 200 scalar-pass candidates completed with no timeout. The closest case
was stable index 1, with `d=(7,7,1)`, `x=(7,7,1)`, `h=(7,7,1)`, and exact
minimum deficit 19. Combined with the earlier durable ranges 201--3,200, the
contiguous v4 prefix now reaches 3,200. The next untested suffix begins at
3,201.

## Stable indices 3,201--5,200

| stable-index range | survivors | closest deficit gap over `Dmax=14` |
|---|---:|---:|
| 3,201--3,700 | 0 | +8 |
| 3,701--4,200 | 0 | +7 |
| 4,201--4,700 | 0 | +9 |
| 4,701--5,200 | 0 | +10 |

All four 500-candidate shards emitted `FINAL`, with no timeout and no
survivor. The contiguous v4 prefix now reaches 5,200; the next suffix begins
at 5,201.
