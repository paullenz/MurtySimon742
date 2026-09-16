# Murty–Simon / Erdős #742 — live current state

> Read this first. The incomplete-tight-graph theorem is preserved and verified. Fresh-package replay uncovered and corrected a graph-sidecar unpacking bug after the mathematical decisions already agreed. No theorem or catalogue change in this correction.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `SOURCE_REPAIR_REVIEW_BRANCH_ONLY`.

**WORK MODE:** `RECOVERY`. Source-only review branch; main and mathematical claims unchanged.

**INSPECTED PREDECESSOR:** current main `3353576e458b1ccfd025a38bfb06eb3b5c6e5dc5`, retaining its fresh-directory graph-sidecar replay fix; previous source review commit `2b9a345f3d3e9318806e66afc3fbcb8185468a54`.

**LAST VERIFIED RESULT:** mathematical status unchanged from the main baseline. Original and hardened universal-core replay passed all 11,357 records with the recorded hashes. An earlier 11,281-record incomplete input is rejected explicitly by the new count/hash checks; its cause remains undiagnosed. This branch retains the original byte-preserved implementation, adds a checked implementation, and points the sidecar-aware entry point at it. The status parser already present on current main is retained, with additional mode-format regression tests.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. No promotion or external acceptance.

**UNPRESERVED WORK:** recovered archives, raw evidence and separate new research are excluded from this source-only branch. Their proposed main publication was blocked by automatic approval review; no alternate archive upload is attempted.

**DEFERRED ADMIN:** archive/research publication and remaining historical recovery.

**NEXT ACTION:** review this source-only repair. The original mathematical continuation is the L=beta=0 incomplete-tight-graph boundary; no new mathematical claim is introduced by this branch.
<!-- CURRENT-STATUS:END -->

## Evidence

- [Universal-core theorem](project/research/general_n/2026-09-16-universal-core-defect-v1/UNIVERSAL_CORE_DEFECT.md).
- [Runnable entry point](project/research/general_n/2026-09-16-universal-core-defect-v1/check_universal_core.py), [preserved Python implementation](project/research/general_n/2026-09-16-universal-core-defect-v1/universal_core_impl.py), and [C++ checker](project/research/general_n/2026-09-16-universal-core-defect-v1/check_universal_core.cpp).
- [Original exact summary](project/research/general_n/2026-09-16-universal-core-defect-v1/CHECK_SUMMARY.json) and [fresh-package correction record](project/research/general_n/2026-09-16-universal-core-defect-v1/REPLAY_WRAPPER_FIX.json).
