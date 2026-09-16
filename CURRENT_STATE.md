# Murty–Simon / Erdős #742 — live current state

> Source repair review branch. Existing verification sources and the handoff parser are hardened; main and all mathematical claims are unchanged by this branch.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `SOURCE_REPAIR_REVIEW_BRANCH_ONLY`.

**WORK MODE:** `RECOVERY`. This branch proposes repairs to existing public verification/status source; it does not update main or carry recovered archives.

**INSPECTED PREDECESSOR:** `5fe392cfcaae2750f511451a1b054b2e39495e0a`.

**LAST VERIFIED RESULT:** mathematical claims unchanged in this repair branch. The original universal-core inputs were regenerated with the published input/decision hashes, and both original and hardened C++ replay passed all 11,357 records. An earlier incomplete input had only 11,281 records; its underlying cause remains undiagnosed. The generator now checks completed pending streams before installation, and replay verifies all input/output record counts and input hashes. The status parser accepts the existing bold WORK MODE label; malformed modes remain rejected. The existing legacy status regression also exposed a policy-removal check, now restored.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. No promotion or external acceptance.

**UNPRESERVED WORK:** recovered archives, full replay artifacts and separate new research are not in this review branch. Their proposed main publication was blocked by automatic approval review; no alternate archive upload is attempted. This branch contains only three source/test files and this handoff.

**DEFERRED ADMIN:** archive/research publication and remaining historical recovery obligations.

**NEXT ACTION:** review the source-code repairs; merge only after the publication block is resolved. The original mathematical next target at the baseline remains the L=beta=0 incomplete-tight-graph boundary.

<!-- CURRENT-STATUS:END -->

## Evidence

- [Universal-core theorem, full argument and limits](project/research/general_n/2026-09-16-universal-core-defect-v1/UNIVERSAL_CORE_DEFECT.md).
- [Python generation and replay](project/research/general_n/2026-09-16-universal-core-defect-v1/check_universal_core.py).
- [Separately structured C++ checker](project/research/general_n/2026-09-16-universal-core-defect-v1/check_universal_core.cpp).
- [Exact check summary](project/research/general_n/2026-09-16-universal-core-defect-v1/CHECK_SUMMARY.json).
- Full pre-verification derivation and priorities: `963ae4ac78ca0a48a1cbc782b3ab160cc0bbfb59:CURRENT_STATE.md`.

The milestone remains a comparatively short structural treatment with explicit coverage and a clear external-review surface. Finite checks support that treatment rather than replacing it.
