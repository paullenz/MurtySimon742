# Murty–Simon / Erdős #742 — live current state

> **Current review entry: [STRUCTURAL_REVIEW.md](STRUCTURAL_REVIEW.md).** The five-label exact block has D>=12. Scope work now has h-index saturation, receiver inflation, the coupled staircase theorem, a clean scalar obstruction to mechanical peeling, and a new global endpoint-orientation cut that excludes that obstruction once the common `q,p` margins are restored.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INTERNAL_GLOBAL_ENDPOINT_ORIENTATION_CUT_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Reassessed the scalar obstruction before following the previous NEXT ACTION mechanically. The highest-value test was to ask whether the obstruction survives the existing exact selected-incidence/orientation bridge when the common source margins are coupled rather than independently maximized. It does not.

**INSPECTED PREDECESSOR:** `e4095858026fede7fdcb1e28206e2751f28fc648`, tree `8329f9a02caaee2bde0c4b8008577b396468c8ac`, confirmed as current `main` before this transaction. The scalar obstruction, staircase theorem, receiver-inflation theorem, h-index saturation theorem, d=5,D>=12 exact-block predecessor and canonical counts remain unchanged.

**LAST RESULT:** derived a candidate general **global endpoint-orientation cut** inside the all-positive-demand canonical selected/residual bridge. For source `u`, let

`P_u^0=min(b-1,rho_u+b-a-1)`

be its incoming ceiling when `q_u=0`, and let

`M_u=max{C_i:0<s_i<=rho_u}`

be the largest endpoint mass of a demand-compatible selected label (omit `M_u` if none exists). Put `B_u=max(P_u^0,M_u)` when a compatible label exists and `B_u=P_u^0` otherwise. If `q_u>0`, an actual selected incidence exists; selected-edge forcing gives `s_i<=rho_u` and endpoint load gives `p_u+q_u<=C_i<=M_u`. If `q_u=0`, the canonical incoming cap gives `p_u<=P_u^0`. Hence every source obeys `p_u+q_u<=B_u`, and the exact orientation identity `sum p=sum q=Q` yields

`2Q <= sum_u B_u`.

This is a genuine non-decoupled common-margin inequality: it links the selected-incidence and missing-pair orientation layers before either source capacity is maximized independently.

**OBSTRUCTION TEST:** for the 17 September scalar witness `a=20,b=23`, `rho=(5^5,4^11,1^7)`, twenty labels with `s=x=4`, and `R=(4^16,3^4)`, one has `C=(8^16,7^4)` and `Q=80`. The source ceilings are `B=8` on the five rho-5 sources, `B=8` on the eleven rho-4 sources, and `B=3` on the seven rho-1 sources. Therefore

`sum B_u=5*8+11*8+7*3=149 < 160=2Q`.

So the earlier scalar witness **cannot extend to the coupled canonical selected-incidence/orientation margins**; the deficiency is 11. This is not a graph-level contradiction to the conjecture and does not prove that every non-square scalar profile is excluded.

**STEP-BACK CONSEQUENCE:** the negative scalar result remains important: repeated staircase/heavy-load algebra alone cannot force the exact block. But the explicit obstruction is not robust once a very cheap common-margin endpoint/orientation cut is restored. This materially strengthens the case for continuing with joint structural information rather than either more scalar threshold summation or immediate abandonment of the route.

**NEW PRIORITY:** generalise/refine the endpoint-orientation cut using selected excess and endpoint-class packing. The current `M_u` deliberately ignores the fact that a source with incoming load `p_u` can use only labels with `e_i>=max(0,p_u-rho_u+1)`. Build an excess-aware source envelope, then test whether it forces an exact block or leaves a substantially narrower explicit obstruction. Only after that, invoke the more expensive pair-choice / target-capacity / selected-incidence Hall systems. A genuine reduced-system peeling operation remains a secondary route.

**AUDIT:** `project/research/general_n/2026-09-17-global-endpoint-orientation-v1/check_global_endpoint_orientation_cut.py` replays the obstruction arithmetic exactly and verifies `2Q=160`, `sum B=149`, deficiency 11. The proof note is `GLOBAL_ENDPOINT_ORIENTATION_CUT.md`. These are internal bridge-level results; external review remains open.

**FIVE-LABEL STATUS:** every actual whole exact block `|T|=|H|=5` satisfies `D>=12`, hence `W>=37` or `W>=57` with extras. Nothing in this unit weakens that theorem.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. No canonical catalogue scan, workflow launch, q-enumeration or promotion in this unit.

**PRESERVATION:** new common-margin cut and checker are in `project/research/general_n/2026-09-17-global-endpoint-orientation-v1/`. The scalar obstruction remains in `project/research/general_n/2026-09-17-staircase-scalar-obstruction-v1/`; staircase peeling, receiver inflation, h-index saturation, d=5 closure and heavy-load artifacts remain at their previously recorded paths.

**UNPRESERVED WORK:** None for this bounded theorem/audit after remote confirmation.

**DEFERRED ADMIN:** older archive transfers, PR #2, unrelated CI/root historical narrative maintenance; external review, novelty and promotion.

**NEXT ACTION:** MATH: derive the excess-aware refinement of the common-margin cut. For a source with positive `q_u`, use selected excess `e_i>=max(0,p_u-rho_u+1)` together with endpoint load `p_u+q_u<=C_i` and demand compatibility `s_i<=rho_u` to define a source-specific feasible `(q,p)` envelope. Sum those envelopes under `sum q=sum p=Q`; test first on abstract non-square profiles before any broad survivor scan. Preserve either a stronger theorem or the next exact obstruction.
<!-- CURRENT-STATUS:END -->
