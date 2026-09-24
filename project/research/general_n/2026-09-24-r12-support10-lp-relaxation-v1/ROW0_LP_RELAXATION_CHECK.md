# r=12 support-ten helper screen: row-0 LP-relaxation checkpoint

Timestamped research interval: 2026-09-24T01:12:36+01:00 to 2026-09-24T01:13:40+01:00.

Scope: internal exact-model diagnostic only. This does **not** establish graph realizability, external verification, S<=14, or the Murty-Simon theorem.

## Independent encoding check

Using the first saved support-ten source survivor (identity `unit_graph=5179456, heavy_edge=0, a_mask=11, b_mask=19`, residual `(2,2,1,1,1,1,1,1,1,1)`), I independently rebuilt the helper-aware constraints from the committed mathematical semantics but set all integrality flags to continuous. This is a strict relaxation of the saved integer MILP: if the LP relaxation is infeasible, then the integer helper model is also infeasible.

The reconstructed row has degrees `(3,3,3,3,2,3,3,2,2,2)`, need `(1,1,2,2,1,2,2,1,1,1)`, 3,558 nonempty-zero patterns, one residual-free type (the all-right state), and 4,481 helper constraints. No helper constraint is discharged by the residual-free type.

A continuous feasibility solve (`scipy.optimize.milp` with zero integrality, HiGHS backend) returned status 2, `The problem is infeasible (HiGHS Status 8)`, in about 2.0 seconds on the recovery runtime. A source-only LP without helper constraints is feasible, so the contradiction is genuinely introduced by the helper system rather than by a transcription error in the source-cover equations.

This is materially stronger computationally than relying on branch-and-bound for this row and suggests the 32 timeout cases should be retried as **LP relaxations / independently encoded linear feasibility systems**. It is still the same HiGHS backend and therefore is not yet the requested independent solver certificate. The next action is to regenerate the strict support-ten kernels from the committed orbit generator, recover all 32 source survivors, and test the LP-relaxation encoding across all 32. If all 32 LPs are infeasible, preserve the full row table and then seek exact Farkas-style or rationally checkable certificates before thawing S<=14.
