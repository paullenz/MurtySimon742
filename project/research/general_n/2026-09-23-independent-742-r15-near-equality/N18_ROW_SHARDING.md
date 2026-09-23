# Exact scalar sharding for the n=18 strengthened row

The row driver now supports `--resume-scalar A --stop-scalar B`. It scans the deterministic scalar index, solves exactly the inclusive range `A+1,...,B`, and emits `range_complete: true` only after attempting every candidate in that range.

Validation command:

`python -u screen_witness_row.py 18 10 --stop-first --skip-known-n18 --resume-scalar 8850 --stop-scalar 8900`

Validation result: range 8,851-8,900 complete; zero survivors; closest minimum deficit 25 against `Dmax=16` (gap 9). Full pattern index reached 11,865 when the stopping sentinel was encountered.

Together with the preceding serial checkpoints, scalar prefix 1-8,900 is closed with zero abstract survivors. This is not full-row closure.
