# Murty–Simon / Erdős #742 — live current state

> Read this first. Critical-edge covering now gives a quadratic clique-defect bound and closes intrinsic defect one for every exact block with d>=3. The d=2 exception remains explicit. No catalogue promotion.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INTERNAL_CRITICAL_EDGE_COVERING_VERIFIED_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Theorem-first priority. This unit verifies and packages the already-preserved structural derivation; it is not a survivor scan.

**INSPECTED PREDECESSOR:** `80a783799a9a671e9b29356284515bad0402a3ce`, tree `8eb802551777876951fea27d27855109a4b51875`. Main was re-read before publication preparation. The full derivation and earlier handoff remain at that immutable predecessor; the zero-defect unit remains at `54f974fcff8acd85870deacc931da15ec4b11069`.

**LAST VERIFIED RESULT:** internal parameterized hand proof. For an actual exact d-by-d block with d>=3 and complete F[T], L+beta>=(d-1)(d-2). Marking tight vertices that have singleton K-neighbours, original edge-criticality forces each K-label to meet at most one unmarked tight vertex. Counting distinct labels together with the exact tight rows proves the bound. If F[T] is incomplete, 2mu>=2 already, so every actual exact d>=3 block has intrinsic defect at least two. The d=2, L=1 singleton-label exception is NOT closed.

**SCOPE / EQUALITY:** no positive pivot-surplus or pool-size restriction. The quadratic term REQUIRES complete F[T]. For d=5 the complete-tight-graph W thresholds are 37 and 57 (with extras); without completeness only 27 and 47 follow. Equality in the clique bound forces one unmarked tight vertex, one positive-demand singleton label at every other tight vertex, beta=0 and zero loss on all other K-labels. Incidence-only equality examples exist; no canonical graph realization is asserted. Configurations without an exact tight block remain outside the theorem.

**CHECKS:** Python and separately structured C++ agree on all 506403 exact records: 10333 local graph records, including 9712 eligible redundant deletions, and 496070 incidence records. The latter include exhaustive d=3 compatible row/pool assignments and 39 equality controls through d=15. All five graph controls have diameter two and a destructive designated deletion. Early bounded combined-driver invocations expired; separate complete replay and the delivered replay-only command succeeded. No interrupted invocation is counted as success. Both implementations and proof are by the same assistant. These are local graph/relaxation checks, NOT a canonical graph census or catalogue replay. External review and novelty assessment OPEN.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. Prior 203-key candidate union, 41 strict/equality certificates, 170-candidate audit and state3349 retain their previous status. No workflow launch, q-enumeration or promotion.

**PRESERVATION:** proof, exact summary, byte-preserved compressed verification sources and a tested hash-checking unpacker are in `project/research/general_n/2026-09-16-critical-edge-covering-v1/`. Decode the source bundle with `python3 unpack_sources.py`; then `python3 check_covering.py` regenerates and checks the finite cases. The complete 17-file attachment `MurtySimon742_Critical_Edge_Covering_2026-09-16.zip`, SHA256 `0b6e0ff62b58d4cfbb0fbe3774af93ebb605ba94b683194a37aaabecec12d72a`, includes original sources, proof, exact raw streams, audit notes, manifest, handoff and the predecessor ZIP unchanged. Every manifested file was checked inside the ZIP. Uncompressed input SHA256 `f3ff6ef23eac4d28bda0e6e4f472b427b5268a83356c63376fda3f366db8c9a0`; decision SHA256 `45633e4ee20f50bce9de4b40d1dd2a0656c1532609fd5d8c73adea67227bf922`. Large raw streams are NOT claimed uploaded by this commit.

**UNPRESERVED WORK:** no completed mathematical finding or verification source remains only in session memory after remote confirmation. Separate raw-stream GitHub transfer and older attachment transfers remain pending; exact bytes and hashes are in the delivered package.

**DEFERRED ADMIN:** raw-stream and older evidence transfers; root README/reviewer integration; unrelated CI/status work; independent review, novelty assessment and promotion.

**NEXT ACTION:** one bounded mathematical unit resolving the isolated d=2 exception using full quasi-edge identities and original criticality. There beta=0 automatically. Write T={t,s}, let c>=2 count common K-labels, and let the unique singleton K-label neighbour only s; exact rows force p_t=c and p_s=c-1. Determine whether its private witness can occur in a full canonical graph, rather than extrapolating from the local eight-vertex control. Preserve the first result or obstruction. A generalization to incomplete F[T] is a separate subsequent task; do not transplant the quadratic bound to mu>0.

**PROCESS RULE:** one bounded unit then preservation and one remote confirmation; no background-work claim or automatic promotion.
<!-- CURRENT-STATUS:END -->

## Evidence

- [Critical-edge covering theorem, complete proof and limits](project/research/general_n/2026-09-16-critical-edge-covering-v1/CRITICAL_EDGE_COVERING.md).
- [Exact check summary](project/research/general_n/2026-09-16-critical-edge-covering-v1/CHECK_SUMMARY.json).
- [Hash-verifying source unpacker](project/research/general_n/2026-09-16-critical-edge-covering-v1/unpack_sources.py) and [byte-preserved source ZIP, base64](project/research/general_n/2026-09-16-critical-edge-covering-v1/SOURCE_BUNDLE.zip.b64).
- Earlier complete derivation and trust boundaries: `80a783799a9a671e9b29356284515bad0402a3ce:CURRENT_STATE.md`.

The main milestone remains a comparatively short structural treatment with explicit coverage and reviewable proofs. Finite checks support that milestone; they do not replace it.
