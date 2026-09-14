# Murty-specific canonical antichain profile-statistics pilot

14 September 2026. **Reconnaissance only. No whole-state closure is promoted by this note. External review remains OPEN.**

## Purpose

The generic Hall audits showed that a canonical sharp-hardness witness can require multiple incomparable generators, with up to six observed in the broad finite challenge. The question here is whether the much more constrained Murty-Simon frontier lives in a simpler region.

The answer from this pilot is **no**: actual target-Hall-failing profiles in the frozen Murty-Simon state sample require canonical antichains as large as eight.

## Provenance

GitHub Actions run:

```text
run id:    34831697002
head:      d976a4fccb0fb0201ce75498b40909765af6d480
conclusion: success
artifact:  10342124522
artifact digest:
sha256:b0f5596399faf3e273a981a0e8c2929b3c1c2c34bf50047e2be085bf4bb65222
```

The pilot used the same deterministic `1/256`, remainder-16 frontier shard as the earlier single-type and principal-upset reach pilots: 15 ledger-current states, 14 N34-derived and one N35-derived.

The generator [`make_antichain_stats_scanner.py`](make_antichain_stats_scanner.py) transforms the canonical relational scanner without changing its state/q-profile enumeration or mathematical pass/fail screens. Whenever the labelled target flow fails, the generated scanner independently builds the sharp-dominance-closed type quotient, recomputes maximum flow, aborts if the flow value differs, extracts the canonical maximal source-side minimum cut from the residual network, verifies that it is a sharp-hardness up-set/staircase, and records the size of its minimal generator antichain.

Thus every recorded generator count has an exact labelled-flow / quotient-flow equality cross-check. A discrepancy would have failed the workflow rather than being counted.

## Aggregate result

Across the 15 states:

```text
profiles tested:                 201,493,148
target-Hall-failing profiles:        205,919
relationally excluded states:             13
relational survivors:                       2
maximum canonical generators:               8
```

The canonical generator histogram over the `205,919` target-Hall failures is:

| generators | failing profiles |
|---:|---:|
| 1 | 214 |
| 2 | 6,722 |
| 3 | 41,452 |
| 4 | 80,972 |
| 5 | 58,775 |
| 6 | 16,349 |
| 7 | 1,426 |
| 8 | 9 |
| 9+ | 0 |

The modal target-Hall obstruction uses **four generators**, not one or two. Profiles with five generators are also extremely common.

This is a stronger negative result for the bounded-generator route than the synthetic counterexamples alone: the higher-generator phenomenon occurs abundantly inside the actual Murty-Simon relaxation being scanned.

## Layer split

The N34-derived portion accounts for `205,823` target-Hall failures and contains all observed generator counts through eight:

```text
1:     211
2:   6,693
3:  41,405
4:  80,955
5:  58,775
6:  16,349
7:   1,426
8:       9
```

The single N35-derived pilot state contributes 96 target-Hall failures:

```text
1:  3
2: 29
3: 47
4: 17
5+: 0
```

The sample is far too small to infer an N34/N35 theorem from this difference. It is preserved only as a clue for the later layer-comparison programme.

## State-level maximum generator count

| layer | state | target-Hall failures | maximum generators |
|---:|---:|---:|---:|
| N34 | 226 | 64,232 | 7 |
| N34 | 1626 | 63,818 | 7 |
| N34 | 2439 | 48,448 | 7 |
| N34 | 2984 | 1,681 | 7 |
| N34 | 4073 | 13,871 | 7 |
| N34 | 5519 | 477 | 6 |
| N34 | 6085 | 12,260 | **8** |
| N34 | 6998 | 562 | 6 |
| N34 | 7610 | 7 | 6 |
| N34 | 8179 | 253 | 6 |
| N34 | 8727 | 10 | 5 |
| N34 | 9440 | 0 | 0 |
| N34 | 10098 | 0 | 0 |
| N34 | 11007 | 204 | 6 |
| N35 | 429 | 96 | 4 |

The two states with zero target-Hall failures (`9440`, `10098`) are already killed before that stage of the relational stack; zero here does not mean target-flow feasibility is the reason for their whole-state exclusion.

## Research consequence

The data argue strongly against trying to prove that all relevant Hall failures have one, two, or another small constant number of antichain generators. The appropriate object is instead the **entire monotone staircase** established in [`STAIRCASE_THRESHOLD_HALL.md`](STAIRCASE_THRESHOLD_HALL.md), and its relaxed consecutive-band flow in [`STAIRCASE_BAND_HALL.md`](STAIRCASE_BAND_HALL.md).

This changes the symbolic target from

```text
"show one small Hall cut fails"
```

to

```text
"control the aggregate demand/capacity of a monotone staircase
 whose target neighborhoods are intervals of staircase bands."
```

That route can still be compact even when the number of generators grows, because there is at most one generator per integer cross-degree level and the band-neighborhood matrix has the consecutive-ones property on the source-band side.

## Preserved evidence

- [`MURTY_ANTICHAIN_PROFILE_STATS_PILOT_SUMMARY.json`](MURTY_ANTICHAIN_PROFILE_STATS_PILOT_SUMMARY.json) — frozen aggregate.
- [`MURTY_ANTICHAIN_PROFILE_STATS_PILOT.tsv`](MURTY_ANTICHAIN_PROFILE_STATS_PILOT.tsv) — complete state-level counters.
- [`make_antichain_stats_scanner.py`](make_antichain_stats_scanner.py) — deterministic generator for the instrumented scanner.
- Workflow `.github/workflows/scan-antichain-profile-stats-pilot.yml` — exact CI recipe.

The original uploaded Actions artifact additionally preserves the generated C++ scanner, input, input verification and replay log.

## Trust boundary

This is reconnaissance about profiles that already reach the target-Hall stage of the current necessary-condition relaxation. It neither proves nor promotes any whole-state closure. The full `3,607`-state discovery/recovery/two-implementation audit remains the promotion path.
