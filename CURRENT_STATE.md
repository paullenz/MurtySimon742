# Murty–Simon / Erdős #742 — live current state

> **Current review entry: [STRUCTURAL_REVIEW.md](STRUCTURAL_REVIEW.md).** The five-label D=11 frontier is closed by combining exact support-cover equality with the residual-union constraint; the scoped bound is now D>=12.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `VERIFIED_INTERNAL_D5_DEFECT11_CLOSED_NOT_PROMOTED`.

**WORK MODE:** `AUDIT`. Completed one bounded equality-closure proof and independent auxiliary enumeration.

**INSPECTED PREDECESSOR:** `73f4a0e20d6a5d0d46da9a8bde5a0f2ffc27b219`, tree `e9e2634b6e394f88b63230e9ac976cad9a27e501`, confirmed main before this transaction. Its D>=11 support-cover theorem remains unchanged and is the prerequisite.

**LAST VERIFIED RESULT:** every actual whole exact block |T|=|H|=5 satisfies D>=12. If D=11, equality throughout the predecessor's support-cover chain forces beta=0 and every non-full K-label to have positive demand. Every cheapest cover of each of the 25 D=11 auxiliary minimizers requires a singleton support. A positive-demand singleton K-label selected from a full pool has deg_F<=5 by residual-union, but R_k>=5 and positive demand require deg_F>=6. Contradiction. Hence W>=37, or W>=57 with extra high-source selections. Internal candidate theorem; external review, novelty, sharpness and D=12 attainability open.

**FRESH CHECK:** Python set-based and C++ bit-mask lexicographic dynamic programmes independently enumerate all 1024 Q and all 31 supports. They agree byte-for-byte on the complete row stream, SHA256 `858941a3e47b59631433e61bd8ced65f6a9e7cb302a0de0281201e6074e0df77`. Exactly 25 Q attain the predecessor's D=11 auxiliary minimum; every cheapest cover requires a singleton, with minimum counts 3 for the mu=1 family and 1 for the mu=2 matching family. This verifies the finite auxiliary classification, not the hand residual-union implication or original-graph realization.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. Previous candidate unions, audits and state3349 retain their trust boundaries. No canonical catalogue scan, workflow launch, q-enumeration or promotion.

**PRESERVATION:** `project/research/general_n/2026-09-17-d5-defect11-closure-v1/` contains the hand proof, both exact enumerators and pinned summary. `STRUCTURAL_REVIEW.md` points to the new result. No prior proof or evidence is removed.

**UNPRESERVED WORK:** None for this bounded theorem or its reported verification after remote confirmation.

**DEFERRED ADMIN:** older archive transfers, PR #2, unrelated CI/root historical narrative maintenance; external review, novelty and promotion.

**NEXT ACTION:** MATH: analyze D=12 by classifying support-cover slack together with beta, exact tight rows and selected-source locations. Do not assume beta=0. Determine whether the first residual tight incidence outside the full pools can actually support every required singleton threat without violating residual-union or row multiplicities. Exact-block coverage remains a separate essential obligation.
<!-- CURRENT-STATUS:END -->
