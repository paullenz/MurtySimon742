# Layered receiver Hall reach pilot

14 September 2026. **Reconnaissance only. No whole-state closure is promoted by this note. External mathematical review remains OPEN.**

## Purpose

This pilot measures how much of the exact canonical target-Hall obstruction remains after applying the verified layered receiver-capacity projection from [`LAYERED_RECEIVER_CAPACITY.md`](LAYERED_RECEIVER_CAPACITY.md). The projection keeps the receiver-capacity layer distribution and compatible-source-count layer distribution but discards their target-by-target correlation.

The experiment uses the same deterministic 15-state, `1/256` remainder-16 frontier sample as the antichain, staircase-band and compatible-copy pilots.

## Provenance

```text
workflow:        scan layered receiver Hall reach pilot
run id:          34848635869
head sha:        53f36783fa5fa83c055e010b0827131a6f45b396
conclusion:      success
artifact id:     10348779261
artifact name:   layered-receiver-reach-pilot
artifact digest: sha256:6221ecb4a20685a1f3c02e3a3bd8ce8d18c729572a504d8a981a2c9ffcd179c0
```

The workflow regenerated the canonical antichain scanner, coarse-band instrumentation, compatible-copy instrumentation and layered receiver instrumentation from the frozen source machinery before running the pilot.

## Baseline reproduction

The pilot reproduced the established Hall counts exactly:

```text
profiles tested:                  201,493,148
exact target-Hall failures:           205,919
coarse staircase-band detected:       205,918
compatible-copy band detected:        205,919
```

Thus the receiver-layer experiment is being measured against the same frozen Hall-failure population as the prior pilots.

## Layered receiver result

The one-dimensional layered receiver projection detected:

```text
205,107 / 205,919 exact target-Hall failures
= 0.9960567019...
= 99.605670%
```

and passed despite exact target-Hall failure on:

```text
812 profiles.
```

For those passing cases the recorded aggregate excess of the layered upper bound over exact receiving capacity had:

```text
sum across passing rows: 368
maximum observed excess:   5
```

The excess statistic is diagnostic only; it is not itself a proof margin.

## Interpretation

The result is strong enough to keep the layered receiver route high priority, but it is not exact. Compared with the compatible-copy canonical representation, the only information discarded here is the correlation between target capacity level and compatible-source-count level. Losing that correlation is sufficient to hide 812 of the 205,919 exact Hall failures in this pilot.

This substantially narrows the next structural question:

> What low-complexity Murty-specific statistic recovers enough of the receiver-capacity/compatibility correlation to eliminate the 812 layered false negatives?

The appropriate next diagnostic is to stratify those 812 profiles by the amount and location of rearrangement slack, canonical staircase generator count, receiver-capacity levels, `q/c/rho` ranges and total excess `E`, rather than returning to arbitrary Hall subsets.

## Trust boundary

This is a deterministic reconnaissance experiment on a finite 15-state frontier sample. It does not change the canonical 3,607-state frontier, does not promote a whole-state exclusion and is not evidence that the layered receiver projection is sufficient in general. The underlying layered inequality is internally audited; its Murty-Simon use inherits the canonical graph-to-constraint bridge and target-capacity definitions.
