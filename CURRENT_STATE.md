# Murty–Simon / Erdős #742 — live current state

> **Current review entry: [STRUCTURAL_REVIEW.md](STRUCTURAL_REVIEW.md).** The five-label exact block has D>=12. The scope programme now has three general bridges: h-index saturation, receiver inflation, and a new coupled demand/residual staircase theorem that converts the k<h escape into either a large scalar loss or forced lower-level residual-tail growth.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INTERNAL_STAIRCASE_PEELING_BRIDGE_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Stepped back from the recorded instruction to build a new h/h-1 routing theorem from scratch. Re-read the canonical threshold-capacity theorem and recognized that, in tail coordinates, it already supplies the missing multi-level coupling. Extracted the exact staircase system and its first adjacent-level peeling corollary.

**INSPECTED PREDECESSOR:** `4612d874bb3e195ec7a3e1369da297779fbbbc37`, tree `4f8d22142024233a429b590f1f1605a1cf2a9497`, confirmed main before this transaction. Its receiver-inflation theorem, the h-index saturation theorem, the verified d=5,D>=12 exact-block predecessor and all canonical counts remain unchanged.

**LAST RESULT:** for demand tails `K_d=#{s_i>=d}` and residual tails `N_d=#{rho_u>=d}`, positive surplus gives the exact layer-cake ledger `2t<=sum_d(K_d-N_d)`. The canonical threshold-capacity theorem rewrites as the pure staircase inequality

`d K_d + sum_{j>d} K_j <= d N_d + C(N_d-d,2)`.

For residual h-index h>=3, writing `k=K_h`, `K=K_{h-1}`, `N=N_h`, `M=N_{h-1}`, one gets

`b+2t <= a(h-2)+K+k-(h-2)M-N`

and

`(h-1)K+k <= (h-1)M+C(M-h+1,2)`.

If the top level is non-square (`k<=h-1`), define

`K_*(M)=min(a, M-1+floor(C(M-h+1,2)/(h-1)))`.

Then

`b+2t <= a(h-2)-1+K_*(M)-(h-2)M`.

In particular, if `N_h=N_{h-1}=h`, any non-square top level satisfies

`b+2t <= (h-2)(a-h+1)`.

Thus with `N_h=h` and larger target, either the exact square block occurs or the residual staircase must grow immediately below h. At h=5: `N_5=5` and `b+2t>3a-12` force `K_5=5` or `N_4>=6`.

**STEP-BACK CONSEQUENCE:** the previous "mass can migrate from h to h-1" obstruction was too coarse. The h-1 migration is not free: threshold pair capacity either sharply reduces the demand sum or forces growth of the residual tail. The scope problem is now naturally a recursive staircase problem, not a single top-level branch.

**ARITHMETIC AUDIT:** `check_staircase.py` brute-forces the Section 5 integer elimination for 50,076 `(h,a,M)` triples over `3<=h<=15`, `h<=a<=60`, `h<=M<=min(3a,100)`, plus 676 flat-tail cases. No failures. This checks the integer elimination only, not the inherited hand graph theorem.

**FIVE-LABEL STATUS:** every actual whole exact block `|T|=|H|=5` satisfies `D>=12`, hence `W>=37` or `W>=57` with extras. The new staircase theorem gives a direct scope dichotomy feeding into that exact-block result, but does not prove that every graph reaches the block.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. Previous candidate unions, audits and state3349 retain their trust boundaries. No canonical catalogue scan, workflow launch, q-enumeration or promotion.

**PRESERVATION:** new theorem and audit are in `project/research/general_n/2026-09-17-staircase-peeling-v1/`. Receiver inflation remains at `project/research/general_n/2026-09-17-receiver-inflation-v1/`; h-index saturation at `project/research/general_n/2026-09-17-hindex-saturation-v1/`; d=5 closure at `project/research/general_n/2026-09-17-d5-defect11-closure-v1/`; older heavy-load theorem at `project/research/general_n/2026-09-12-heavy-load-family-v1/`.

**UNPRESERVED WORK:** None for this bounded theorem or arithmetic audit after remote confirmation.

**DEFERRED ADMIN:** older archive transfers, PR #2, unrelated CI/root historical narrative maintenance; external review, novelty and promotion.

**NEXT ACTION:** MATH: make the staircase recursive. Combine the full family `SC_d` with receiver-inflation and the preserved heavy-load tail inequalities on the branch where `N_{h-1}>h`. Aim to prove that repeated peeling either reaches a square exact block at some level or accumulates enough residual-tail area to violate `2t<=sum_d(K_d-N_d)`. Preserve either a genuine recursive bound or a clean obstruction; do not mechanically return to exact-block D=12 grinding.
<!-- CURRENT-STATUS:END -->
