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

The survivor-bearing replay of shards 0, 1, 4 and 5 subsequently reached a
durable in-progress checkpoint at 1,200 of 3,192 kernels: 11 feasible and zero
solver-unknown.  This is an execution heartbeat, not a completed-shard claim;
the same run continues toward the exact identity comparison.


## Accounting-layer reconciliation

The discrepancy is now resolved as a bookkeeping error, not as evidence of ten
missing kernels.  The preceding 21:00 session recorded shard 0 with 10
survivors.  The 22:00 continuation recorded shards 1--7 with
`11+0+0+6+5+0+0=22` survivors.  Hence the canonical saved total is
`10+22=32`.  The erroneous 42 is exactly obtained by counting the initial ten
a second time.  All eight saved shard payloads and their individual unit records
agree with 32, cover 6,386 kernels, and record no solver-unknown row.

This repairs the count only.  It does not independently reimplement the source
MILP and does not authorize `S<=14`.  The legacy supplement wrapper loads rows
dynamically, so the prose error did not omit ten kernels from its attempted
screen.  However, that wrapper reuses a solver which excludes residual-free
helper types.  The newly preserved `screen_support10_case1_helpers.py` includes
them under the audit's optimistic semantics and is therefore the required next
screen over the corrected 32-row set.

The fresh survivor-bearing replay reached a durable checkpoint at 1,200/3,192
kernels (11 feasible, zero unknown).  A later transient observation reached
2,400/3,192 (27 feasible, zero unknown), but workspace re-entry destroyed the
process boundary and final output; that observation is disclosed but is not
credited as a result.  A clean rerun remains required before promotion.
