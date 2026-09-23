# n=18, Delta=10 strengthened row resumption through scalar 7,700

A deterministic `--resume-scalar N` option was added. It traverses the same demand partitions and scalar filters, but skips MILP solves for the already certified prefix.

Command:

`python -u screen_witness_row.py 18 10 --stop-first --skip-known-n18 --resume-scalar 7400`

The scan reproduced the saved boundary: scalar 7,000 at full pattern 9,738 and scalar 7,400 at full pattern 10,202. It then solved scalar candidates 7,401 through 7,700, reaching full pattern 10,544.

Result for the new segment: zero abstract survivors. Its local minimum gap above `Dmax=16` was 3. The earlier global minimum gap 1 remains the correct prefix-wide value.

This is a partial replay checkpoint, not row closure. Resume at scalar 7,700.
