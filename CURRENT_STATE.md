# Murty–Simon / Erdős #742 — live current state

> **Current review entry: [STRUCTURAL_REVIEW.md](STRUCTURAL_REVIEW.md).** The five-label support-threat problem is now solved exactly as a weighted finite cover, strengthening the scoped exact-block bound from D>=8 to D>=11.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `VERIFIED_INTERNAL_D5_EXACT_SUPPORT_COVER_NOT_PROMOTED`.

**WORK MODE:** `AUDIT`. Completed the bounded d=5 support-cover theorem and cross-implementation enumeration.

**INSPECTED PREDECESSOR:** `bdb297f2ff3e91ea329c8763e85d84c45cdc2662`, tree `13bad05475755e2e80b6e594dfa6269dd299baac`, confirmed main before this transaction. Its checked pair-coverage/support-charge theorem remains unchanged and is the prerequisite.

**LAST VERIFIED RESULT:** for an actual whole exact block |T|=|H|=5, D>=11. The proof uses the predecessor's pair coverage and necessity of the support-threat cover. Every K support S costs at least max(0,4-|S|) units of L; every off-pool residual support costs at least as much beta. Exact weighted set cover over all 1024 labelled tight graphs gives min_Q(2mu+tau(Q))=11. Hence W>=36, or W>=56 with extra high-source selections. This is an internal candidate theorem within the exact-block scope; external review, novelty, sharpness and attainability remain open.

**FRESH CHECK:** Python set-based and C++ bit-mask implementations independently enumerate all 1024 Q, all 31 nonempty supports and the exact subset dynamic programme. Their full row streams agree byte-for-byte; SHA256 `80aa3a20b985dab08080c5d645bdf44cadb9498ec3be636219a670e35e4943c9`. The minimum is attained by 10 labelled Q with mu=1 and degree sequence (3,3,4,4,4), and 15 labelled Q with mu=2 and degree sequence (3,3,3,3,4). These are auxiliary graphs, not original realizations.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. Previous candidate unions, audits and state3349 retain their trust boundaries. No canonical catalogue scan, workflow launch, q-enumeration or promotion.

**PRESERVATION:** `project/research/general_n/2026-09-17-d5-exact-cover-v1/` contains the theorem, both exact enumerators and pinned summary. `STRUCTURAL_REVIEW.md` points to the new result. No prior proof or evidence is removed.

**UNPRESERVED WORK:** None for this bounded theorem or its reported enumeration after remote confirmation.

**DEFERRED ADMIN:** older archive transfers, PR #2, unrelated CI/root historical narrative maintenance; external review, novelty and promotion.

**NEXT ACTION:** MATH: analyze the two D=11 auxiliary minimum families using the full exact tight-row equations, K-support multiplicities, demand types and receiver-pool counts. Determine whether either weighted cover can be realized by the original selected-representative system. Exact-block coverage beyond this scoped theory remains a separate essential obligation.
<!-- CURRENT-STATUS:END -->
