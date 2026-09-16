# Murty–Simon / Erdős #742 — live current state

> Read this first. The incomplete-tight-graph theorem is preserved and verified. Fresh-package replay uncovered and corrected a graph-sidecar unpacking bug after the mathematical decisions already agreed. No theorem or catalogue change in this correction.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INTERNAL_UNIVERSAL_CORE_DEFECT_VERIFIED_REPLAY_CORRECTED_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Final verification-package correction within the same bounded theorem unit, not a new survivor scan.

**INSPECTED PREDECESSOR:** `5fe392cfcaae2750f511451a1b054b2e39495e0a`, tree `eba30ddc8e07694e905a547e67fa80d5da4208e1`, confirmed still main immediately before this transaction. Its complete theorem/check handoff is preserved unchanged at that immutable commit. The pre-verification derivation remains at `963ae4ac78ca0a48a1cbc782b3ab160cc0bbfb59`; the d=2 closure remains at `6c5c979ea636316f3ad078b313314692e2ea1bbc`.

**LAST VERIFIED RESULT:** mathematics unchanged. For an actual exact d-by-d block, d>=3, g universal tight vertices imply L+beta >= (d-2)max(0,g-1). Hence D=L+beta+2mu >= 2mu+(d-2)max(0,d-2mu-1) >= 2floor(d/2). One missing tight edge gives D>=2+(d-2)max(0,d-3). At d=5, arbitrary / one-missing-edge / complete tight graphs have increments 4 / 8 / 12 and W thresholds 29/49, 33/53, 37/57, second entry requiring extras. The d=2 uniform expression is inherited from its separate closure. No positive-surplus, fixed-order or pool-size assumption; exact-block coverage remains a hypothesis.

**EQUALITY TARGET:** for d=5, D=4 forces two disjoint missing tight edges, g=1 and L=beta=0. This configuration is neither excluded nor realized here. The old clique bound is not applied unchanged to missing-edge endpoints.

**CHECKS:** the preceding Python/C++ verification agrees on all 11357 records: 1399 local graph records and 9958 incidence records. Eligible graph deletions include 431 incomplete tight graphs and 259 simultaneously incomplete with singleton-pool replacement; eligible incidence systems include 7072 incomplete and 334 with at least two unmarked universal vertices. Three graph controls and one incidence control retain essential-premise failures. The numerical envelope was checked for d=3,...,99. Both implementations and proof are by the same assistant; no fresh canonical graph census or independent review.

**REPLAY CORRECTION:** a fresh-directory --replay-only test failed with FileNotFoundError for GRAPH_RECORDS.json during final recompression, AFTER all 11357 mathematical decisions had agreed. It unpacked input and expected decisions but not the graph sidecar. The exact tested implementation is now byte-preserved as universal_core_impl.py (blob 8b9124fc5bc384c4388a0f2d92c1f9be80425ff2). A thin check_universal_core.py entry point expands the graph sidecar first, then delegates unchanged. Fresh-directory replay now completes with byte-identical decisions AND CHECK_SUMMARY.json. This is an actual executed replay, not an inferred fix. Failure/fix records are preserved; no platform diagnosis is inferred.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. Prior 203-key candidate union, 41 strict/equality certificates, 170-candidate audit and state3349 retain their prior boundaries. No q-enumeration, workflow launch or promotion. External review and novelty OPEN.

**PRESERVATION:** `project/research/general_n/2026-09-16-universal-core-defect-v1/` contains the full theorem, Python entry point, byte-preserved Python implementation, C++ implementation, exact summary and replay-fix record. Run `python3 check_universal_core.py` to regenerate. The delivered `MurtySimon742_Universal_Core_Defect_2026-09-16.zip` additionally preserves full compressed input/decision/graph streams, controls, envelopes, audit notes and manifest. Input SHA256 `ab9ed63d9caa99b5fbd237fc6b238f77b69a8dc893ff17a764f96ff5cc9ab4bb`; decision SHA256 `c4859538b56444860b26fdc46e40f68bf21b4c65b68dce2e394b531c621ba82a`. Separate large raw-stream GitHub transfer is not claimed.

**UNPRESERVED WORK:** no completed mathematical finding, verification implementation or replay correction remains only in session memory after remote confirmation. Raw-stream and older evidence transfers remain pending, with exact delivered bytes preserved.

**DEFERRED ADMIN:** raw and older source/evidence transfers; root README/reviewer integration; unrelated CI/status work; independent review, novelty and promotion.

**NEXT ACTION:** one bounded original-graph closure attempt at L=beta=0 with incomplete F[T], starting with d=5, D=4 and Q=K5 minus two disjoint edges. Test common-label forcing by exact interface counting, then cover every affected short path after deleting a tight edge under the common/one-hole neighbourhood partition. Determine the justified broader scope; do not claim the boundary excluded before proving it. Preserve the first result or obstruction before another unit. The milestone remains a short structural treatment, not incremental survivor counts.

**PROCESS RULE:** one bounded unit then preservation and one remote confirmation. No background-work claim or automatic promotion.
<!-- CURRENT-STATUS:END -->

## Evidence

- [Universal-core theorem](project/research/general_n/2026-09-16-universal-core-defect-v1/UNIVERSAL_CORE_DEFECT.md).
- [Runnable entry point](project/research/general_n/2026-09-16-universal-core-defect-v1/check_universal_core.py), [preserved Python implementation](project/research/general_n/2026-09-16-universal-core-defect-v1/universal_core_impl.py), and [C++ checker](project/research/general_n/2026-09-16-universal-core-defect-v1/check_universal_core.cpp).
- [Original exact summary](project/research/general_n/2026-09-16-universal-core-defect-v1/CHECK_SUMMARY.json) and [fresh-package correction record](project/research/general_n/2026-09-16-universal-core-defect-v1/REPLAY_WRAPPER_FIX.json).
