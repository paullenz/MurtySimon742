# n=18 exact-star continuation from stable index 44,351

24 September 2026, 07:00 scheduled session.  The first four bounded v4 shards
tested stable indices 44,351--44,450.

| stable-index range | survivors | closest deficit gap over `Dmax=16` |
|---|---:|---:|
| 44,351--44,375 | 0 | +15 |
| 44,376--44,400 | 0 | +14 |
| 44,401--44,425 | 0 | +15 |
| 44,426--44,450 | 0 | +16 |

Every shard emitted `FINAL`; there were zero timeouts and zero abstract
survivors.  The contiguous internal prefix therefore reaches 44,450, apart
from historical index 20,851 independently excluded by exact star-five.

This file is an incremental finite necessary-condition ledger.  It is not a
claim of full row closure, graph realizability, equality, or the general
theorem.  The next suffix begins at 44,451.

## Stable indices 44,451--46,450

| stable-index range | survivors | closest deficit gap over `Dmax=16` |
|---|---:|---:|
| 44,451--44,950 | 0 | +10 |
| 44,951--45,450 | 0 | +7 |
| 45,451--45,950 | 0 | +9 |
| 45,951--46,450 | 0 | +10 |

All four 500-candidate shards emitted `FINAL`, with no timeout and no
survivor.  The closest case was stable index 45,226, demand and selected
degree `(3,3,3,3,3)` and `(4,3,3,3,3)`, at minimum deficit 23.  The preserved
contiguous endpoint is 46,450; the next suffix begins at 46,451.
