# Murty–Simon / Erdős #742 — live current state

> **Current review entry: [STRUCTURAL_REVIEW.md](STRUCTURAL_REVIEW.md).** The five-label exact block has `D>=12`. Scope work now retains the complete selected-incidence matrix: a weighted endpoint/excess ledger, an `E>=3` barrier for the mixed demand-4/5 near-Turán band, and a full capacitated Hall theorem using all exact selected row/column degrees.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INTERNAL_FULL_SELECTED_INCIDENCE_HALL_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Continued directly from the small-selected-excess barrier. The first aggregate `E=3` obstruction survived the weighted endpoint/excess ledgers, so the step-back question was what exact canonical information had still been projected away. The missing object was the whole simple selected-incidence matrix, not another scalar inequality.

**INSPECTED PREDECESSOR:** `e18e7b2db35ef92be7ca295b119870f8f0d724ab`, whose hand theorem rules out total selected excess `E=0,1,2` in the mixed `{4,5}`, `h>=5`, `(a,b,t)=(20,23,2)` scope. All earlier quadratic endpoint, Hall, common-margin, staircase/heavy-load and exact-block work remains preserved.

**GENERAL LAST RESULT — FULL SELECTED-INCIDENCE HALL:** define for every source

`g_u=max(0,p_u-rho_u+1)`, `w_u=p_u+q_u`.

A label `i` can be selected at source `u` only if

`s_i<=rho_u`, `e_i>=g_u`, `C_i=R_i+x_i>=w_u`.

The actual selected incidences form a **simple bipartite graph** inside this eligibility graph, with exact source degrees `q_u` and exact label degrees `x_i`. Therefore, for every source subset `S`,

`sum_{u in S} q_u <= sum_i min(x_i, |{u in S: i is eligible at u}|)`.

This is the exact capacitated Hall/max-flow condition for realizing the selected-incidence matrix inside the eligibility graph. In particular, every individual source satisfies the cheap row-packing condition

`q_u <= #{i: s_i<=rho_u, e_i>=g_u, C_i>=p_u+q_u}`.

Thus a source of selected degree `q_u` needs `q_u` **distinct** compatible labels. One favourable label, or one witness per active source, is not enough.

A threshold projection is also immediate: if `U(d,g,w)` is any source collection with `rho_u<=d`, `g_u>=g`, and `p_u+q_u>=w`, then

`sum_{u in U}q_u <= sum_{i:s_i<=d,e_i>=g,C_i>=w} min(x_i,|U|)`.

The earlier pure excess cut `sum_{g_u>=h}q_u <= sum_{e_i>=h}x_i` is a weaker projection of this system.

**STRICTNESS TEST AT E=3:** an explicit aggregate profile at `k=12,E=3,r=88,Q=95` has source classes

`3x(1,3,0), 2x(4,6,1), 5x(4,3,5), 1x(4,3,7), 7x(4,3,8), 5x(5,7,1)`

and label classes `(s,R,e)`

`4x(4,0,0), 3x(4,2,0), 1x(4,3,0), 1x(5,0,0), 5x(5,1,0), 5x(5,12,0), 1x(5,14,3)`.

It passes the weighted endpoint/excess ledgers:

`lambda=0: 940>=940`, `lambda=1:964>=961`, `lambda=2:988>=982`, `lambda=3:1012>=1003`,

and passes pure excess thresholds `7<=8` for `h=1,2,3`. But a source `(rho,p,q)=(4,3,8)` needs eight distinct labels with `s<=4` and `C>=11`; the eight demand-four labels have endpoint masses only `4,6,7`, so there are zero eligible labels. Row Hall reads `8<=0` and rejects immediately.

This establishes that the full selected-incidence theorem adds genuine information beyond the aggregate quadratic/weighted ledgers and the earlier one-witness Hall theorem.

**SMALL-EXCESS STATUS:** the preceding hand theorem remains: in the mixed `{4,5}`, `h>=5`, `(20,23,2)` scope, every actual bridge must have total selected excess `E>=3`. The `E<=2` theorem and checker remain unchanged.

**E=3 DIAGNOSTIC:** a bounded integer transport model retaining exact margins, weighted/endpoint ledgers, excess threshold capacities and the new local row-packing condition has rejected the aggregate `E=3` obstruction patterns tested so far, including all three excess partitions at the difficult `k=9,10,12,13,14` values. This is diagnostic evidence only at this checkpoint; a complete hand closure or frozen exhaustive certificate has not yet been promoted.

**AUDIT:** `project/research/general_n/2026-09-17-full-selected-incidence-hall-v1/FULL_SELECTED_INCIDENCE_HALL.md` contains the theorem and strictness example. `check_strictness_example.py` independently replays all margins, weighted ledgers, excess thresholds and the row-packing failure; local replay returned `PASS_FULL_SELECTED_INCIDENCE_HALL_STRICTNESS`. The `E<=2` proof/checker remain in `2026-09-17-small-excess-quadratic-v1/`. External mathematical review remains open.

**STEP-BACK CONSEQUENCE:** the correct hierarchy is now clearer: exact selected row/column multiplicities -> endpoint/excess eligibility -> full simple-incidence Hall -> only then projected scalar envelopes or finite screens. The next task is not to add another aggregate inequality before testing this exact incidence bottleneck.

**FIVE-LABEL STATUS:** every actual whole exact block `|T|=|H|=5` still satisfies `D>=12`, hence `W>=37` or `W>=57` with extras.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. No canonical catalogue scan, q-enumeration or theorem promotion.

**PRESERVATION:** full selected-incidence Hall theorem/checker are in `project/research/general_n/2026-09-17-full-selected-incidence-hall-v1/`; small-excess barrier is in `2026-09-17-small-excess-quadratic-v1/`; quadratic endpoint and all earlier structural/audit packages remain preserved.

**UNPRESERVED WORK:** the exploratory integer transport screen for complete `E=3` closure has not yet been frozen as a proof package; do not claim `E>=4` from it yet.

**DEFERRED ADMIN:** older archive transfers, PR #2, unrelated CI/root historical narrative maintenance; external review, novelty and promotion.

**NEXT ACTION:** MATH: finish `E=3` at the selected-incidence level. Split the three excess partitions `(3)`, `(2,1)`, `(1,1,1)`. The latter two already look hand-closable from the small-excess source inequality plus exact excess capacities; for `(3)`, use row-packing/endpoint-tail capacity of the unique excess label and the demand-four endpoint tails. Aim for a compact hand proof of `E>=4`; if a true incidence-level survivor remains, freeze the smallest one instead. Do not broaden to `E>=4` until `E=3` is resolved.
<!-- CURRENT-STATUS:END -->
