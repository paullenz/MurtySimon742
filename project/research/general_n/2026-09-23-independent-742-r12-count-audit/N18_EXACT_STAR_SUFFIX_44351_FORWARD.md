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

## Stable indices 46,451--48,450

| stable-index range | survivors | closest deficit gap over `Dmax=16` |
|---|---:|---:|
| 46,451--46,950 | 0 | +8 |
| 46,951--47,450 | 0 | +10 |
| 47,451--47,950 | 0 | +11 |
| 47,951--48,450 | 0 | +12 |

All shards emitted `FINAL`, with no timeout and no survivor.  The preserved
contiguous endpoint is 48,450; the next suffix begins at 48,451.

## Stable indices 48,451--52,450: first new survivor

| stable-index range | survivors | closest deficit gap over `Dmax=16` |
|---|---:|---:|
| 48,451--49,450 | 0 | +10 |
| 49,451--50,450 | 0 | +11 |
| 50,451--51,450 | 1 | 0 |
| 51,451--52,450 | 0 | +5 |

Stable index **50,740** is the first new v4 abstract survivor after 20,851:

    demand d=(8,8), selected degrees x=(8,8), h=(8,8),
    centre deficits=(8,8),
    eight common right endpoints, each of deficit zero,
    total minimum deficit D=16.

This is not the previously excluded `(d,x)=((8,7),(8,8))` case: both demand
entries are now eight and both complement sizes are `|C_i|=Delta-h_i=2`.
The singleton-source saturation obstruction using a unique one-point `C_i`
therefore does not transfer.  Prefix closure stops at 50,739 pending an actual
graph-realizability analysis of this new equality-budget geometry.  The other
three shards closed normally; no timeout occurred.


## Stable indices 52,451--54,450

| stable-index range | survivors | closest deficit gap over `Dmax=16` |
|---|---:|---:|
| 52,451--52,950 | 0 | +8 |
| 52,951--53,450 | 0 | +5 |
| 53,451--53,950 | 0 | +8 |
| 53,951--54,450 | 0 | +9 |

All four 500-candidate shards emitted `FINAL`, with no timeout and no
survivor. The preserved internal prefix now reaches 54,450, except historical
index 20,851 and index 50,740, both separately excluded at graph level. This
remains finite necessary-condition evidence, not full row closure or a general
proof. The next suffix begins at 54,451.
