# r=12 support-ten helper-aware screen

Status: `VERIFIED_INTERNAL_NOT_PROMOTED`.

The corrected 32 saved source-feasible kernels for residual partition
`(2,2,1^8)` were screened by the preserved helper-aware MILP.  All 32 returned
HiGHS status 2 / model status infeasible; there were zero feasible and zero
solver-unknown rows.  Every kernel had exactly one admissible residual-free
type, the all-zero type, and it discharged no supplement obligation.  Thus the
residual-free-helper relaxation does not reopen any saved support-ten kernel.

This closes the supplement stage for the **saved 32-row source set** at the
abstract profile layer.  It does not independently reimplement the source
MILP, establish graph realizability, externally verify the bridge, or by itself
authorize `S<=14`.  A clean full source-stage replay remains mandatory before
promotion.

Execution: 02:03:44--02:13:07 BST, nine workers, exit code 0.  Full aggregate
metadata and trust limits are in `R12_SUPPORT10_HELPER_SCREEN_RESULT.json`.
