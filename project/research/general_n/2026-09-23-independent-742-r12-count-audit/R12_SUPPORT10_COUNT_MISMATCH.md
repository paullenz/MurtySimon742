# r=12 support-ten source-count mismatch

Status: `COUNT_MISMATCH_FREEZE`.

The eight committed source-screen shards for the support-ten partition
`(2,2,1^8)` cover the 6,386 strict kernels without gaps or overlaps.  Their
saved feasible counts are

`[10, 11, 0, 0, 6, 5, 0, 0]`,

which sum to **32**, not the 42 stated in the 23 September audit and the prior
22:00 session handoff.  The 32 saved rows have 32 distinct kernel identities,
all have residual partition `(2,2,1^8)` and `t_upper=1`, and no shard records a
solver-unknown row.

This is a load-bearing independent count mismatch.  In accordance with the
standing freeze rule, no r=12 supplement-screen closure or `S<=14` consequence
is authorized until the source stage is reconciled.  The likely arithmetic
explanation is that the initial shard's 10 survivors were counted twice when a
running total was reported as 42, but that explanation is not itself proof that
the saved source rows are complete.  The next bounded step is an independent
replay or reimplementation of the source stage, followed by a supplement screen
over the reconciled survivor set.

Evidence: `check_support10_case1_aggregate.py`.  This checker validates the
saved shard ranges and payloads; it does not independently rerun their MILPs.

## First fresh replay attempt

A fresh full-stage replay was launched with 16 worker processes.  At the
observed five-minute boundary it had completed 800 of 6,386 kernels, finding 10
feasible rows and no solver-unknown rows.  Its measured rate projected too close
to the research cutoff to finish and preserve safely, so it was interrupted at
that exact progress checkpoint.  This partial result is not used to certify the
aggregate count.  The bounded pivot is to replay the four survivor-bearing
saved shards first, then the four zero-survivor shards, preserving each group.
