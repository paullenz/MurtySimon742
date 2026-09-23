# r=12 support-eight/nine residual-free-helper audit

Status: `VERIFIED_INTERNAL_NOT_PROMOTED`.

The optimistic helper-aware MILP rejects all 44 saved r=12 source survivors:
8 at support eight and 36 at support nine, with zero solver-unknown rows.
Residual-free helpers are non-vacuous here: four kernels have two free types and
the free types discharge 500 supplement obligations in total.  Nevertheless no
kernel becomes feasible.

The first driver attempt named absent zero-survivor case files and failed before
solving; the corrected manifest discovers the committed case files and completed
successfully.  This audit reuses saved source rows and the support-ten helper
MILP.  It is not an independent source-stage reimplementation, graph
realizability evidence, or by itself an `S<=14` theorem.
