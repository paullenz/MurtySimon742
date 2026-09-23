# Post-(5,5,5) stable-index sharded replay

The row driver now supports `--continue-past-555`. It keeps the original scalar indices, records the separately audited `d=x=(5,5,5)` survivor as `GRAPH_EXCLUDED_SURVIVOR`, and continues without treating it as a live abstract survivor.

## Exact closures

- Prefix 1-18,900 is resolved with zero live survivors. Scalar 14,440 is the sole encountered abstract survivor in that prefix and is separately excluded by the staged/audited graph-level D2C UNSAT result.
- Range 20,901-22,900 completed with zero survivors (closest gap 5).
- Range 12,901-14,900 independently reclosed with one graph-excluded survivor and zero live survivors.
- Range 10,901-12,900 emitted `range_complete` with zero survivors, but its terminal observation was after the forward cutoff; it is retained as mathematical evidence without contributing post-cutoff research time.

## Interrupted exact boundaries

The cutoff interrupted these workers:

- 18,901-20,900: progress output through scalar 20,850, zero survivors;
- 22,901-24,900: progress output through scalar 24,850, zero survivors;
- 24,901-26,900: progress output through scalar 26,850, zero survivors.

These observations do not close their declared ranges. Resume the small tails or rerun the bounded shards.

## Timing limitation

Three workers were still active when termination was issued at 15:54:13, 35 seconds after the 15:53:38 research cutoff. No post-cutoff duration is credited. This is a timing-compliance failure, not a mathematical invalidation of completed exact solver results.
