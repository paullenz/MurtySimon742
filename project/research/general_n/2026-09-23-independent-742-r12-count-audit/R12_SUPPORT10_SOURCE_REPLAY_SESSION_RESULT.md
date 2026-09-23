# r=12 support-ten source replay: session result

Status: `VERIFIED_INTERNAL_PARTIAL_REPLAY`.

Fresh source-stage executions completed shards 2, 3 and 6: 2,395 strict
kernels, zero feasible rows, zero solver-unknown rows, and exact agreement with
the saved empty survivor sets.  A broader run over shards 2, 3, 6 and 7 was
terminated by workspace re-entry after its last durable 2,400/3,194 progress
mark; it has no credited completion result.

Static review also found that the replay driver's scope text said "all 6,386"
even for a partial-shard invocation.  This did not affect tasks, counts, solver
models or identity comparison.  The driver now reports the selected shards and
actual task count.

This is an internal replay of the committed encoding, not an independent
reimplementation or graph-realizability result.  Shards 0, 1, 4, 5 and 7 still
require a fresh completed replay.  Consequently the helper-screen result and
this partial source replay do **not** authorize `S<=14`.
