# Murty–Simon / Erdős #742 — live current state

> Read this first. The universal-core theorem extends critical-edge covering to incomplete tight graphs. The derivation, both executable sources and exact summary are preserved. No catalogue promotion.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INTERNAL_UNIVERSAL_CORE_DEFECT_VERIFIED_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Verification and publication of the previously preserved incomplete-tight-graph theorem, not a survivor scan.

**INSPECTED PREDECESSOR:** `963ae4ac78ca0a48a1cbc782b3ab160cc0bbfb59`, tree `cfe656885e71f0bd37dcec9bca3ab5aba40f6838`, freshly re-read before publication preparation. That immutable handoff contains the full derivation before verification. The preceding d=2 closure remains at `6c5c979ea636316f3ad078b313314692e2ea1bbc`.

**LAST VERIFIED RESULT:** internal parameterized hand proof. In an actual exact d-by-d block with d>=3, let g count tight vertices adjacent to every other tight vertex. Then L+beta >= (d-2)max(0,g-1). Thus D=L+beta+2mu >= 2mu+(d-2)max(0,d-2mu-1) >= 2floor(d/2). Exactly one missing tight edge gives D>=2+(d-2)max(0,d-3). Only unmarked universal endpoints use the clique-style replacement paths. The d=2 case of the uniform bound is inherited from the separate singleton closure, not re-proved here.

**SCOPE / EQUALITY:** no positive-surplus, fixed-order or pool-size restriction. At d=5, arbitrary / one-missing-edge / complete tight graphs have defect increments 4 / 8 / 12 and W thresholds 29/49, 33/53, 37/57, with the second entry requiring extra high-source selections. Equality at the generic d=5 increment four forces exactly two disjoint missing tight edges, g=1 and L=beta=0. It is a remaining structural target, NOT yet excluded or realized. Configurations without an exact block remain outside the theorem.

**CHECKS:** Python bitset and C++ explicit-path/row implementations agree on all 11357 exact records. Local graph records: 1399, with 1396 eligible redundant deletions, 431 incomplete tight graphs and 259 cases simultaneously incomplete and using singleton-pool protection. All three graph negative controls have diameter two and a destructive deletion. Incidence records: 9958, including 9957 eligible systems, 7072 incomplete systems and 334 with at least two unmarked universal vertices. One feasible-row control violates the covering premise and the proposed inequality. Numerical envelope checked for d=3,...,99. Final replay succeeded after removal of a cosmetic compiler warning. Both implementations and the proof are by the same assistant; these are local/relaxation tests, not a canonical graph census or independent review.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. Prior 203-key candidate union, 41 strict/equality certificates, 170-candidate audit and state3349 retain their earlier boundaries. No q-enumeration, workflow launch or promotion. External review and novelty assessment OPEN.

**PRESERVATION:** `project/research/general_n/2026-09-16-universal-core-defect-v1/` contains the proof, both runnable native-text verification sources and CHECK_SUMMARY.json. Run `python3 check_universal_core.py` to regenerate and cross-check. The delivered `MurtySimon742_Universal_Core_Defect_2026-09-16.zip` additionally contains complete compressed input/decision/graph streams, negative controls, envelope records, audit notes and checksum manifest. Raw input SHA256 `ab9ed63d9caa99b5fbd237fc6b238f77b69a8dc893ff17a764f96ff5cc9ab4bb`; both-language decision SHA256 `c4859538b56444860b26fdc46e40f68bf21b4c65b68dce2e394b531c621ba82a`. Large raw streams are not claimed separately uploaded to GitHub; both sources are native text, not hand-transcribed base64.

**UNPRESERVED WORK:** no completed mathematical finding or verification source remains only in session memory after remote confirmation. Separate raw-stream GitHub transfer and older attachment transfers remain pending; exact raw bytes are in the delivered package.

**DEFERRED ADMIN:** raw-stream and older source/evidence transfers; root README/reviewer integration; unrelated CI/status work; independent review, novelty assessment and promotion.

**NEXT ACTION:** one bounded original-graph closure attempt at L=beta=0 with incomplete F[T], starting with the d=5, D=4 equality target Q=K5 minus two disjoint edges. Use exact interface counting to test whether a common K-label is forced, then check all short paths affected by a tight-edge deletion using the common/one-hole neighbourhood partition. Determine the correct broader scope; do not claim this boundary excluded until proved. Preserve the first result, failure or remaining family before another unit. Do not revert to scan-first progress metrics.

**PROCESS RULE:** one bounded unit then preservation and one remote confirmation; no background-work claim or automatic promotion.
<!-- CURRENT-STATUS:END -->

## Evidence

- [Universal-core theorem, full argument and limits](project/research/general_n/2026-09-16-universal-core-defect-v1/UNIVERSAL_CORE_DEFECT.md).
- [Python generation and replay](project/research/general_n/2026-09-16-universal-core-defect-v1/check_universal_core.py).
- [Separately structured C++ checker](project/research/general_n/2026-09-16-universal-core-defect-v1/check_universal_core.cpp).
- [Exact check summary](project/research/general_n/2026-09-16-universal-core-defect-v1/CHECK_SUMMARY.json).
- Full pre-verification derivation and priorities: `963ae4ac78ca0a48a1cbc782b3ab160cc0bbfb59:CURRENT_STATE.md`.

The milestone remains a comparatively short structural treatment with explicit coverage and a clear external-review surface. Finite checks support that treatment rather than replacing it.
