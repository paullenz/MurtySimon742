# Strengthened n=18, Delta=10 row replay: cutoff checkpoint

## Scope

This is a deterministic partial replay of the corrected witness-deficit row after separately excluding the four leading tuples documented in this session. It uses the strengthened exact model:

- strict star slack `binom(x,2)+1` for every assigned star with `x>=3`;
- the certified n=18 certificate floors: slack at least 30 for x=7 and at least 35 for x=8;
- the graph-source capacity bound and centre constraint `delta_i<=h_i`;
- total deficit allowance `Dmax=16`.

The skipped tuples are not silently omitted: each has a separate proof or exact strengthened minimum in the preceding session artifacts.

## Closed tested prefix

Command:

`python -u screen_witness_row.py 18 10 --stop-first --skip-known-n18`

Observed interval: 2026-09-23T14:24:30+01:00 through 2026-09-23T14:53:19+01:00.

At the cutoff boundary:

- scalar candidates tested: **7,400**;
- complete deficit patterns tested: **10,202**;
- abstract survivors: **0**;
- smallest tested deficit excess above `Dmax=16`: **1**.

The process was interrupted deliberately at the forward-research cutoff. This file claims only the tested prefix. It does **not** claim complete row closure, and it does not infer anything about the untested suffix.

## Consequence and next action

The strengthened constraints eliminate a large additional prefix and bring the nearest tested abstract pattern to deficit 17. Resume the deterministic replay from a durable checkpoint if supported, or rerun it and continue past this exact boundary. Any future abstract survivor must still pass graph-level D2C source geometry; abstract feasibility alone is not realizability.
