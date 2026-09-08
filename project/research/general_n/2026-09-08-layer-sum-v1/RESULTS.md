# Recorded checks — layer-sum continuation

8 September 2026. Fresh local executions in this response, not recovery of an earlier claimed run.

**Mathematics: candidate; internal finite replay: REPRODUCED; independent mathematical review: OPEN.**

The candidate implication is `n>=6 and Delta>=13n/22 => m<floor(n^2/4)`. The hand proof, not sample extrapolation, supplies the all-order argument.

| Check | Recorded result |
|---|---:|
| Labelled graphs considered, 3<=n<=6 | 33,864 |
| Independent criticality-implementation comparisons | 33,864, all agree |
| Critical labelled graphs found in that domain | 608 |
| Selected systems from all roots/choices in that domain | 920 |
| Additional systems from ten saved seven-vertex graphs | 32 |
| Systems from forty deterministic larger graph samples | 107 |
| Total selected systems | 1,059 |
| Threshold tests on these systems | 2,119 |
| Nonempty threshold tests | 13, from 12 systems |
| Positive-surplus systems | 0 |
| Abstract demand multisets | 2,353 |
| Scalar-identity cases | 10,200 |
| Malformed-selection negative controls | 3 rejected |
| Small-order boundary control | K(2,3) rejects overbroad strict n>=4 scope |

The new replay's ordered system digest is `c51748bf92ec98d2f4cf3c7acee55e1f612175b9d7c04641d2111f72dfa09cf3`.

The inherited threshold program also passed: 99 rounding cases, 2,550 integer maximisations, and 1,728,186 admitted checks on 59,809 oriented graphs. Its exact rational contradiction margin is 2071/2000000.

Both programs exited zero on Python 3.13.5. The new run took 1.4646568590000015 seconds and the inherited run 2.352237387999992 seconds in this environment. Timings are local observations, not a performance guarantee. Complete commands, environment, graph masks, sampled graph inputs and parsed results are in [EVIDENCE.json](EVIDENCE.json), alongside both programs and history. No optimisation solver or network is needed for replay.

The graph predicates are separate implementations by the same assistant, not independent researcher reproduction. Only twelve systems have nonzero demand and none has positive surplus. Larger graph samples are not exhaustive; their first/last selections are not every possible selection. Abstract multisets and orientations are not critical graphs. No Lean verification, external mathematical review or remote CI execution of this new result is claimed.
