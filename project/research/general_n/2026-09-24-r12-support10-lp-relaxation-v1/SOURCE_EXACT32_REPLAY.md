# r=12 support-ten source stage: exact replay on independently regenerated LP survivor set

Observed research interval: 2026-09-24T01:21:49+01:00 to 2026-09-24T01:22:53+01:00.

The independent continuous source-LP prefilter of all survivor-bearing shards left exactly 32 kernels. I then rebuilt the original integer source-cover model independently and solved it only on that complete LP-survivor set.

Result: **32/32 integer-feasible; 0 infeasible; 0 unknown**. Solver wall time for this exact 32-row stage was 62.06 seconds with four workers. Pattern counts range from 3,478 to 4,017, matching the saved source/helper input range.

Because integer source feasibility implies source-LP feasibility, the preceding LP prefilter proves that no integer-feasible source kernel exists outside these 32 among the independently regenerated strict kernels. Thus `LP prefilter over the complete strict universe + exact integer replay on every LP survivor` independently reproduces the audited **32-row source stage** without having to branch-and-bound all 6,386 strict kernels.

This closes the current source-stage replay concern for the survivor-bearing shards at the internal-computation level. It does **not** prove graph realizability, does not by itself thaw `S<=14`, and does not address the load-bearing helper infeasibility claim. The helper stage remains the active gate.
