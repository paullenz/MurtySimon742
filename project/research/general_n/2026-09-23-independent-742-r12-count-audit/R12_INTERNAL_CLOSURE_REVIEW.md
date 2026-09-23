# r=12 internal closure review

Status: `FROZEN_BY_2026-09-24_AUDIT`; not externally verified.

Audit correction, 24 September 2026: the source-stage replay and corrected
32-row count remain valid internal evidence, but the load-bearing support-ten
helper screen did not reproduce. A fresh run of the identical script SHA with
its committed 180-second per-row limit returned 32 solver timeouts/UNKNOWN and
zero proved infeasibilities. The saved earlier run claims 32 infeasibilities;
it is preserved, not declared false. This promotion is frozen until decisive
independent reproduction or checkable infeasibility certificates exist. The
retained audited edge-bound range is `S<=13`.

## Conclusion (superseded by the 24 September audit)

The audited promotion to strict residual closure through `r=12` is **not
currently justified**.  The source stage reaches 32 support-ten rows, but the
load-bearing helper stage is unresolved because a fresh same-script replay
timed out on every row.  The retained internally supported edge-bound range is
therefore `S<=13`; the proposed `S<=14` promotion remains frozen.  Equality
remains proved only through `S<=8`.

This does not prove Murty--Simon in the remaining positive-demand strip, lower
the `250/429` candidate threshold, or establish the full equality theorem.

## Coverage ledger

- Supports at most five: 47 residual partitions, 12 strict cores and zero
  source survivors in `r12_support_le5.json`.
- Support six: three saved source survivors; all three are infeasible in the
  optimistic residual-free-helper MILP.
- Support seven: two saved source survivors; both are infeasible in the same
  helper-aware system.
- Support eight: the five partitions of 12 at support eight are all covered.
  Cases 0 and 1 have 11 and 387 strict cores and zero source survivors in the
  earlier canonical package.  Their mask subsets are byte-identical to cases
  0 and 1 in the expanded package.  Case 2 has zero survivors; cases 3 and 4
  have four each.  All eight saved survivors remain helper-aware infeasible.
- Support nine: cases 0 and 1 have zero source survivors; case 2 has 36.  All
  36 remain helper-aware infeasible.
- Support ten: partition `(3,1^9)` has zero source survivors.  For
  `(2,2,1^8)`, a fresh replay of all 6,386 strict kernels reproduced exactly
  32 distinct survivors with per-shard counts `[10,11,0,0,6,5,0,0]`, zero
  unknowns and exact saved identities.  The saved helper result classifies all
  32 as infeasible, but a fresh replay classified all 32 as UNKNOWN after the
  committed time limit.  Their helper-aware status is therefore unresolved.
- The audited predecessor identifies this support-ten partition as the sole
  remaining r=12 obstruction; the analytic high-support lemmas continue to
  handle supports eleven and twelve.

Across supports six through nine, 49 saved source survivors were freshly
screened under optimistic residual-free-helper semantics and all 49 are
infeasible with zero unknowns.  The additional 32 support-ten rows have a saved
infeasible classification but yielded 32 UNKNOWN timeouts in the fresh audit
replay.  Residual-free types discharge 604 obligations in the support-six
through-nine screens, so that reproduced part of the hostile extension is
substantive rather than a vacuous rerun.

## Trust boundary

The support-ten source stage was freshly rerun but reuses the committed MILP
encoding; it is not an independent reimplementation.  The other source/orbit
stages are saved internal evidence, not newly reimplemented here.  The finite
systems are necessary-condition systems and exclude graphs only through the
internally audited graph-to-profile bridge.  No finite feasible profile would
constitute graph realizability.  Balanced complete bipartite graphs of both
parities and `X_3` remain mandatory controls; no external `e+disj+X` proof is
used.
