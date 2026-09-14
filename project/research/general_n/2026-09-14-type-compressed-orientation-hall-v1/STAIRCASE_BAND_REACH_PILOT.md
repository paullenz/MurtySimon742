# Staircase-band Hall reach pilot

14 September 2026. **Reconnaissance only. No whole-state closure is promoted by this note. External review remains OPEN.**

## Purpose

[`STAIRCASE_BAND_HALL.md`](STAIRCASE_BAND_HALL.md) is a verified necessary relaxation of exact target Hall. It replaces the exact `(q,c,P)` source types in the canonical Hall witness by its staircase bands, keeping only generator-compatible interval neighborhoods. The key empirical question is how much target-Hall exclusion power survives that deliberate loss of within-band compatibility information.

## Provenance

GitHub Actions run:

```text
run id:    34832806900
head:      2189b02ee088df612563d421788506d7bec5cb31
conclusion: success
artifact:  10342812913
artifact digest:
sha256:f4bb08d4cbe6b80ea2558caa18080aeb7c44b54a902f62e5ff8efef90a440708
```

The run used the same deterministic 15-state, `1/256` remainder-16 frontier pilot as the single-type, principal-upset and canonical-antichain statistics experiments.

For every labelled target-Hall failure the scanner first recomputed the sharp-dominance-closed quotient maximum flow and aborted if its value differed from the labelled flow. It then extracted the canonical maximal minimum-cut staircase and constructed the verified band relaxation for exactly that witness.

## Result

Across

```text
201,493,148 profiles tested,
205,919 exact target-Hall failures,
```

the band relaxation itself was infeasible on

```text
205,918 profiles.
```

Only

```text
1 profile
```

passed the band flow despite failing exact target Hall.

Therefore the observed band-retention rate is

```text
205,918 / 205,919
= 0.9999951437...
= 99.999514%.
```

This is exceptionally high empirical retention, but it is **not** a theorem that the band relaxation is exact on Murty-Simon profiles.

## Generator distribution among band-detected failures

```text
1:      214
2:    6,721
3:   41,452
4:   80,972
5:   58,775
6:   16,349
7:    1,426
8:        9
9+:       0
```

Comparing with the exact target-Hall generator histogram shows that the unique band false-negative is a **two-generator** exact Hall failure. All target-Hall failures using 1 or 3–8 canonical generators in this pilot were also detected by the band relaxation.

## State-level location of the exception

The only discrepancy occurs in N34-derived **state 226**:

```text
target-Hall failures: 64,232
band-detected:        64,231
band-passed:               1
```

Every other pilot state has exact equality between its target-Hall failure count and band-detected count.

That makes state 226 the immediate diagnostic target. The next experiment should recover the exact `(E,rho,q)` profile, canonical two-generator staircase, exact type-level minimum cut and feasible band flow for the unique exception. The goal is to identify the single piece of within-band information lost by the relaxation.

## Interpretation

This changes the priority of the Hall attack materially.

The earlier Murty-specific antichain pilot showed that exact Hall failures often need 4–6 generators and can need 8, ruling out a small-generator strategy. The present pilot shows that **after aggregating those generators into the staircase-band flow, almost all exact target-Hall failures survive the compression**.

So the promising symbolic target is not the raw generator antichain. It is the much smaller band system:

```text
band demands D_i,
band multiplicities M_i,
contiguous target-band intervals I_sigma,
target capacities P_sigma,
self-deletion corrections.
```

If the unique state-226 exception can be explained by one additional low-complexity statistic, there is a realistic route to an almost-exact—and perhaps Murty-specific exact—aggregate Hall theorem.

## Preserved evidence

- [`STAIRCASE_BAND_REACH_PILOT_SUMMARY.json`](STAIRCASE_BAND_REACH_PILOT_SUMMARY.json)
- [`make_band_reach_scanner.py`](make_band_reach_scanner.py)
- workflow `.github/workflows/scan-staircase-band-reach-pilot.yml`
- original Actions artifact preserving full TSV, generated scanner, replay and exact input verification.

## Trust boundary

This experiment measures a necessary relaxation on profiles already inside the post-pair relational scan. It promotes no state and does not change the canonical frontier. The full `3,607`-state discovery/recovery/two-implementation audit remains the only current route to new promoted whole-state exclusions.
