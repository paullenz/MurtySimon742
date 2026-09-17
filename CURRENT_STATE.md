# Murty–Simon / Erdős #742 — live current state

> **Current review entry: [STRUCTURAL_REVIEW.md](STRUCTURAL_REVIEW.md).** The five-label exact block has D>=12. Scope work now has h-index saturation, receiver inflation, the coupled staircase theorem, and a new clean obstruction showing that mechanical scalar peeling cannot by itself force the exact square block.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INTERNAL_SCALAR_STAIRCASE_OBSTRUCTION_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Critically reassessed the proposed recursive staircase action before iterating it. Found that a lower-level square face cannot arise on the same unreduced residual tails (`N_d>=N_h=h>d` for every `d<h`), and then built an explicit abstract scalar witness showing that the current staircase and heavy-load inequalities can all hold while demand stabilizes one level below the residual h-index.

**INSPECTED PREDECESSOR:** `55c490cbeac06f05388ce779a83ccb91bc73bc4b`, tree `182d381301926bc24d8a5a0c08e52136d0160a7e`, confirmed main before this transaction. Its staircase theorem, receiver-inflation theorem, h-index saturation theorem, d=5,D>=12 exact-block predecessor and canonical counts remain unchanged.

**LAST RESULT:** the proposed implication “repeat `SC_d` until a square block or contradiction” is false at the level of the current aggregated relaxation. A concrete abstract profile at `a=20,b=23,n=44,t=2,m=485=floor(n^2/4)+1` has all 20 demands equal to 4 and residual degrees `(5^5,4^11,1^7)`. Then `S=80`, `r=76`, `r+2t=S`, residual h-index `h=5`, but `K_5=0`. The tails are

`K=(20,20,20,20,0,...)`

and

`N=(23,16,16,16,5,0,...)`.

All nontrivial staircase-capacity inequalities hold with slacks 174,43,46,50; the layer-cake ledger is exact; h-index saturation and both canonical charging inequalities hold. An exact audit of the restricted heavy-load source-capacity theorem verifies every integer cutoff: finite minima are positive (114,98,84,48 for h=1..4), and an analytic linear tail bound closes all larger cutoffs. Basic F and residual-bipartite degree sequences are also graphical. This is **not** a graph realization or a Murty–Simon counterexample; it is a feasible point of the current scalar relaxation.

**STEP-BACK CONSEQUENCE:** the staircase theorem remains a genuine top-level narrowing, but its lower-level branch cannot be closed by algebraically recombining the same tail inequalities. In the original graph, `N_d>d` automatically for `d<h`, so reaching a lower exact square would require an actual reduced/peeled representative system. The explicit witness also survives the current heavy-load aggregation. The missing information is therefore likely joint selected-orientation structure lost when endpoint/source constraints are maximized independently.

**NEW PRIORITY:** attack the joint endpoint-load/orientation system before scalar decoupling. Use `R_i+x_i>=q_u+p_u`, `sum q=sum p`, pair uniqueness, source capacities, demand compatibility and supplement containment together. Aim for a global inequality that couples outgoing selected load with incoming supplement load, or define a genuine reduced graph/representative peeling operation whose residual h-index can fall. Do not spend the next unit merely summing more `SC_d` inequalities.

**AUDIT:** `project/research/general_n/2026-09-17-staircase-scalar-obstruction-v1/check_scalar_obstruction.py` exactly checks the concrete witness, staircase family, charging bounds, graphical degree sequences and the full restricted heavy-load cutoff family. Result is `PASS`. The audit is about the abstract relaxation only.

**FIVE-LABEL STATUS:** every actual whole exact block `|T|=|H|=5` satisfies `D>=12`, hence `W>=37` or `W>=57` with extras. Nothing in this unit weakens that theorem; it shows only that present scalar scope bridges do not force entry into the block.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. Previous candidate unions, audits and state3349 retain their trust boundaries. No canonical catalogue scan, workflow launch, q-enumeration or promotion.

**PRESERVATION:** new obstruction and audit are in `project/research/general_n/2026-09-17-staircase-scalar-obstruction-v1/`. Staircase peeling remains at `project/research/general_n/2026-09-17-staircase-peeling-v1/`; receiver inflation at `project/research/general_n/2026-09-17-receiver-inflation-v1/`; h-index saturation at `project/research/general_n/2026-09-17-hindex-saturation-v1/`; d=5 closure at `project/research/general_n/2026-09-17-d5-defect11-closure-v1/`; heavy-load theorem at `project/research/general_n/2026-09-12-heavy-load-family-v1/`.

**UNPRESERVED WORK:** None for this bounded obstruction/audit after remote confirmation.

**DEFERRED ADMIN:** older archive transfers, PR #2, unrelated CI/root historical narrative maintenance; external review, novelty and promotion.

**NEXT ACTION:** MATH: derive a non-decoupled endpoint/orientation inequality. Start from selected incidences before applying independent local source maxima: sum endpoint-load obligations across selected edges, exploit `sum q=sum p`, pair uniqueness and the low incoming capacity of residual-light sources, and test whether the scalar obstruction profile is killed. Preserve either a genuine coupled theorem or the next exact obstruction. A separate alternative is to formalize an honest reduced-system peeling operation; do not call ordinary lower thresholds a recursion unless the h-index actually changes.
<!-- CURRENT-STATUS:END -->
