# Compatible-copy staircase-band reach pilot

14 September 2026. **Frozen internal reconnaissance. No whole-state closure is promoted by this note. External review remains OPEN.**

## Provenance

```text
workflow:        scan compatible-copy band Hall reach pilot
run id:          34846952940
head sha:        fe8de49c84e33f6f9882ede75f0f36c860330ff7
conclusion:      success
artifact id:     10349090763
artifact name:   compatible-copy-band-reach-pilot
artifact digest: sha256:ad2b600051843e1f482b9a7a0f89fe2c64d2469911f5e18c2db6115c0c406b2d
```

The run regenerated the same deterministic 15-state `1/256` remainder-16 pilot, rebuilt the canonical antichain scanner from source, added the previously frozen coarse-band instrumentation and then independently added the compatible-copy refinement.

## Exact result

```text
states:                                  15
profiles tested:                201,493,148
exact target-Hall failures:         205,919
coarse-band detected:               205,918
coarse-band passed:                       1
compatible-copy detected:           205,919
compatible-copy passed:                   0
compatible-copy detection fraction:     1.0
```

Thus the fresh integrated scanner reproduces the old coarse-band count exactly and detects **205,919/205,919** exact target-Hall failures after compatible-copy refinement.

The same pilot still has `13` relational-excluded states and `2` relational survivors; those state-level decisions are unchanged by the added instrumentation.

## Interpretation

This single-pass replay is now redundant mathematically but valuable computationally. The separately audited canonical-witness exactness theorem proves that a compatible-copy network constructed from the canonical maximal minimum Hall witness must retain every exact target-Hall failure. This run confirms that the actual integrated C++ research scanner implements that conclusion across the entire 201-million-profile frozen pilot.

## Trust boundary

The result concerns target-Hall failures inside a deterministic 15-state pilot. It promotes no scalar state and does not change the canonical `3,607` frontier. External mathematical review and genuinely independent third-party reproduction remain open.
