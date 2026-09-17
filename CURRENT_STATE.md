# Murty–Simon / Erdős #742 — live current state

> **Current review entry: [STRUCTURAL_REVIEW.md](STRUCTURAL_REVIEW.md).** The five-label exact block has D>=12. The scope programme now has two general bridges: h-index saturation and a new receiver-inflation theorem that charges high selected load which cannot fit through high-high B-pairs.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INTERNAL_RECEIVER_INFLATION_BRIDGE_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Stepped back from the recorded excess-source action, reviewed the exact-block, h-index and older heavy-routing mechanisms, and extracted a complementary destination-capacity theorem.

**INSPECTED PREDECESSOR:** `71b73a58ae0801a3ec0f8406a8d7818cee12464c`, tree `8102a7a9a66ab5b4303bc6a98e4d2f4515c122fa`, confirmed main before this transaction. Its h-index saturation theorem and the verified d=5,D>=12 predecessor remain unchanged.

**LAST RESULT:** let h be the residual h-index, N=h+u the number of sources with rho>=h, and k the number of demand-h labels. For each threshold q<h, the total omission budget bounds the number of q-light high sources; distinct high-high B-pairs bound how many q-heavy selected incidences can have high destinations; overflow forces distinct low receivers of residual degree at least q. Writing `ell_q=min(N,floor(ku/(k-q)))`, `Y_q=max(0,kh-q ell_q-C(N,2))`, `z_q=ceil(Y_q/N)`, one obtains `r>=b+h(h-1)+u(h-1)+(q-1)z_q` and therefore `b+2t<=(a-h-u)(h-1)+k-(q-1)z_q`. Hand graph theorem with exact arithmetic audit; external review and novelty open.

**STEP-BACK CONSEQUENCE:** attacking u>0 alone is too narrow. Receiver inflation penalizes the excess-source branch, but the scalar optimizer can also evade the exact square face by moving demand from h to h-1 when k<h. The next structural target should therefore be a multi-level/peeling inequality coupling the top level to the h-1 level, preferably combining receiver inflation with the preserved heavy-load/routing tail theorem. Do not return automatically to D=12 exact-block grinding unless this broader analysis requires it.

**ARITHMETIC AUDIT:** `check_receiver_inflation.py` exactly solves the row-load relaxation for 6090 `(h,u,k,q)` parameter/threshold combinations over 2<=h<=15, 0<=u<=5, 1<=k<=15 and confirms the closed light-row and heavy-mass bounds. This checks the finite arithmetic relaxation, not the hand graph implications.

**FIVE-LABEL STATUS:** every actual whole exact block |T|=|H|=5 satisfies D>=12, hence W>=37 or W>=57 with extras. External review, novelty, sharpness and D=12 attainability remain open.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. Previous candidate unions, audits and state3349 retain their trust boundaries. No canonical catalogue scan, workflow launch, q-enumeration or promotion.

**PRESERVATION:** `project/research/general_n/2026-09-17-receiver-inflation-v1/` contains the full new derivation and exact row-relaxation checker. The h-index saturation theorem remains at `project/research/general_n/2026-09-17-hindex-saturation-v1/`; the d=5 proof/check package remains at `project/research/general_n/2026-09-17-d5-defect11-closure-v1/`; the older general heavy-load theorem remains at `project/research/general_n/2026-09-12-heavy-load-family-v1/`.

**UNPRESERVED WORK:** None for this bounded theorem or arithmetic audit after remote confirmation.

**DEFERRED ADMIN:** older archive transfers, PR #2, unrelated CI/root historical narrative maintenance; external review, novelty and promotion.

**NEXT ACTION:** MATH: derive a two-level staircase/peeling inequality. Start from the exact top-level omission/receiver accounting and quantify what is forced at demand h-1 when k<h or when receiver overflow vanishes. Compare the result directly with the existing heavy-load tail inequalities before choosing a further branch. Preserve either a genuine coupled bound or a clean obstruction; do not mechanically follow a stale next-action line.
<!-- CURRENT-STATUS:END -->
