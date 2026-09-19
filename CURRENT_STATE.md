# Dense diameter-2-critical research - live current state

> **Active target - 19 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly-Foucaud-Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty-Simon / Erdos #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_BIDIRECTIONAL_RESERVOIR_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `a15c1d4eeb083e3d101f1be1705201e0e84b185f`

LAST VERIFIED RESULT: After completing the audit-mandated graph-to-Hall/pair-capacity regression, the rigid one-code branch has been sharpened twice. First, pair purity gives `h_P=0`, at most `g_P` matched crossing witnesses per outside source, `k=(x-g_P)_+` unmatched complementary witnesses, the gamma/U score tradeoff, purified `(ONE-P)`, channel-separated `(CHAN-P)`, and direct residual feedback. Second, the new bidirectional-reservoir theorem observes that the A/U channel, same-code `Y--U_d` edges, and same-code `U_{bar d}` edges compete for the same physical `Y x U_{bar d}` source/witness pairs. This gives exact unweighted/weighted reservoir inequalities, a crowding/reservoir cylinder gate, and an explicit saturated equality model. In the saturated case `u_{bar d}=k>0`, the crossing certificates form a complete rectangular witness transversal and degree counting strengthens the unmatched slack to `E_{bar d}>=k(p+k-2)` and forces `L_Y>=y(p-g_P)`, hence `S>=max(phi(g_P),y(p-g_P))+k(p+k-2)`. The saturated U-slack feeds directly into the rooted residual `delta=r-f` ledger.

UNPRESERVED WORK: None. The first `z=u_{bar d}-k=1` near-saturation classification has been identified as the next local target but no uncommitted theorem is being relied upon.

DEFERRED ADMIN: Root README does not yet list the new 19 September reservoir package; defer that reviewer-facing refresh to the next natural status/daily-audit checkpoint rather than risk a large status-only rewrite during the live mathematics. Historical Git-LFS checkout warnings for seven legacy ZIP paths remain preserved and non-blocking.

NEXT ACTION: Stay on the audit-authorized one-code rigid line. Classify the first near-saturated layer `z=u_{bar d}-k=1`: either the crossing U-witness support has size exactly `k`, yielding a saturated core plus one buffer vertex through which every remaining `Y x U_{bar d}` reservoir use must pass, or all `k+1` complementary U vertices are used and their reuse/slack plus same-code edge mass must be charged jointly. Preserve the exact pair-local variables and feed any survivor through the residual `delta=r-f` ledger. Do not return to the mixed `{4,5}` ladder; keep the four-exception gate subordinate.

## Mandatory audit reconciliation

The most recent daily adversarial audit remains:

- `project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`
- independent conditional re-proof: `project/research/post_ms/2026-09-19-daily-red-team-audit-v1/INDEPENDENT_SOURCE_TUPLE_REPROOF.md`

The audit required, in order, independent repair of the two source-tuple premises, graph-level regression through the rooted/Hall interface with `X_3`, then exact pair-local work on the one-code rigid branch. This run follows that order. No departure from the audit's mathematical priority was made.

### Upstream source-premise repair retained

- `project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/SOURCE_PREMISE_GRAPH_AUDIT.md`
- `project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/SOURCE_PREMISE_REPAIR.md`
- `project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/check_source_premises_graph_level.py`

P1 is now a direct raw-criticality fact at the required beta orientation: reuse of one physical `(x,y)` at two target fibres would force the fixed set `N(x) cap N(y)` to be two different singleton tight endpoints. P2 is selected-representative uniqueness for one physical rooted B-edge/source-coordinate obligation, not raw candidate-witness uniqueness. `B_beta` counts those selected physical obligations. The earlier mislabeled alpha-as-beta checker observation remains withdrawn in the correction trail.

## Independent actual-graph regression now reaches the pair-capacity interface

Package:

- `project/research/post_ms/2026-09-19-rigid-graph-regression-v1/RIGID_GRAPH_LEVEL_REGRESSION.md`
- `project/research/post_ms/2026-09-19-rigid-graph-regression-v1/check_rigid_graph_level.py`
- `project/research/post_ms/2026-09-19-rigid-graph-regression-v1/RIGID_GRAPH_REGRESSION_SUMMARY.json`

The checker independently reconstructs actual D2C graphs through the rooted partition, tight A/U codes, rooted witness slots, direct/non-direct A-edge criticality, matched-foot gamma codes, A/U complementary witnesses, pair-local `L_P,S_P,Z_P,R_P,g_P,h_P`, exact `Ccap_P`, and exact Hall-cut decomposition. Across the recorded three certificate policies there are 3,540 root-policy instances, 114 qualified pair/slack instances, 147 pair-local `Ccap_P` checks, 96 one-sided pair checks, 36 exact Hall-cut decompositions, and zero graph/formula mismatches. A genuine matched-B A-edge positive control is exercised.

The corpus still contains no actual rigid complete Hall cut with `x>=3`. Therefore the rigid singleton-head and one-code theorems remain conditional hand deductions from graph-regressed upstream ingredients, not small-graph empirical claims.

### Mandatory `X_3` hostile control

The graph regression continues to verify the explicit `X_3` fixture:

- `n=12`, `m=32>M(12)=31`;
- diameter two and every edge critical;
- canonical cube root `a=3,b=8,p=4,u=0`;
- `Q=12,r=f=delta=0`;
- no nontrivial rigid complete A-cut.

The companion cube-face theorem gives an infinite D2C family `X_k`, with exact rooted slot saturation for the checked `X_3,X_4,X_5`; only `X_3` is above the target `M(n)` in those controls. Exact residual saturation is therefore not being confused with extremality.

## One-code pair purification retained

Package:

- `project/research/post_ms/2026-09-19-rigid-graph-regression-v1/ONE_CODE_PAIR_PURIFICATION.md`
- `project/research/post_ms/2026-09-19-rigid-graph-regression-v1/check_one_code_pair_purification.py`

For one outside code `d`, pair purity gives `A_{bar d}=emptyset`. If `g=g_P` is the number of matching gamma fibres, each outside source has at most `g` matched crossing witnesses and therefore at least

`k=(x-g)_+`

witnesses in `U_{bar d}`. The two-sided matched-foot term vanishes exactly:

`h_P=0`.

The key preserved inequalities are

`S>=phi(g)+(x-g)_+(p-1)` for `p-y>=1`,

`R_code(S_P)[g+2S_P/L]+L_Y >= y(p+x+k)`  (`ONE-P`),

and, for `g<=x`,

`L_Y+2(u_bar L_Y+yE_bar)/L >= y(p+2x-3g)` (`CHAN-P`).

The finite arithmetic diagnostic showed the useful gain comes from gamma/U resource competition and channel separation rather than a coarse total-score version of `(ONE-P)`.

## New bidirectional-reservoir theorem

Package:

- `project/research/post_ms/2026-09-19-one-code-reservoir-v1/ONE_CODE_BIDIRECTIONAL_RESERVOIR.md`
- `project/research/post_ms/2026-09-19-one-code-reservoir-v1/check_one_code_bidirectional_reservoir.py`
- `project/research/post_ms/2026-09-19-one-code-reservoir-v1/ONE_CODE_BIDIRECTIONAL_RESERVOIR_AUDIT_SUMMARY.json`
- `project/research/post_ms/2026-09-19-one-code-reservoir-v1/SATURATED_RESERVOIR_REFINEMENT.md`

Put `U_+=U_d`, `U_-=U_{bar d}`, with sizes `u_+,u_-`, and

`e_+=e(G[Y union U_+])`, `e_-=e(G[U_-])`.

Because `A_{bar d}=emptyset`, `U_+` is independent. Three certificate families all inject into the same physical `Y x U_-` pair set:

1. A/U traffic `C_P`;
2. same-code `Y--U_+` edges;
3. same-code `U_---U_-` edges.

Cross-family collisions are impossible because the fixed singleton common-neighbour set would have to be a head in three disjoint vertex classes. Therefore

`C_P+e(Y,U_+)+e_- <= y u_-`,

and hence

`yk+e_++e_- <= y u_-`,

`e_++e_- <= y(u_--k)`.

The weighted version is

`L[yk+e_++e_-] <= u_-L_Y+yE_-`.

Combining the reservoir with coded-layer crowding gives

`[(y+u_+)(y+u_+-T0)-u_+-(L_Y+E_+)]_+`
` +[u_-(u_--T0-1)-E_-]_+ <= 2y(u_--k)`.

The scorecard-relaxed `Theta` gate derived from this rejected 17,877 of 106,368 bounded old-population states, versus 16,967 from the previous shared gamma/U floor: 910 additional robust arithmetic exclusions despite deliberately giving the whole `C0` scorecard to the crowding deficits.

### Saturated equality geometry

Let `z=u_--k`. At `z=0`, `k>0`:

- `Y`, `U_+`, and `U_-` are independent in the relevant aligned layers;
- `C_P=yk` and `P_P=yg`;
- every physical `Y x U_-` pair is used;
- every outside source uses all `g` gamma-`d` matched feet and all `k` unmatched complementary witnesses;
- the `g+k=x` witness objects are in bijection with the heads in `X`.

Degree counting then gives the new exact penalties

`E_- >= k(p+k-2)`,

`L_Y >= y(p-g+u_+) >= y(p-g)`,

hence

`S >= max(phi(g),y(p-g))+k(p+k-2)`.

In the same bounded diagnostic, 89,400 states had a `k>0` saturated gamma choice surviving the older shared gamma/U score floor; only 66,402 survive this exact saturated score floor, eliminating 22,998 saturation-compatible states. This is diagnostic support, not graph enumeration.

The strengthened saturated U-slack feeds into

`q+E_U >= E_sat+ceil([k(a-1)-u(p-lambda)-E_sat]_+/2)`,

with `E_sat=k(p+k-2)`, and therefore directly raises the forced A-edge mass `f` in the rooted residual ledger.

## Trust boundary

- Source-tuple finite capacity: abstract theorem independently re-derived; P1/P2 repaired at the exact raw/selected levels used.
- `B_beta`: selected physical-obligation semantics audited.
- Actual graph -> rooted/Hall/pair-capacity interface: independently reconstructed on a substantial bounded D2C corpus with zero mismatches; `X_3` remains mandatory.
- Rigid-cut existence/realizability: no positive actual-graph fixture with `x>=3` has been found; downstream rigid theorems remain conditional.
- One-code purification and bidirectional reservoir: hand-derived structural theorems with arithmetic diagnostics; not external review and not a global eventual theorem.
- Four-exception gate: supported but not load-bearing here.

## Stop / pivot criteria

1. Any actual D2C mismatch with the graph-to-pair interface is an immediate blocker and forces proof repair.
2. Do not count abstract parameter survivors/rejections as D2C graphs.
3. Continue exact local geometry while `z=u_--k` is small; do not erase pair information with another total scalar unless it provably closes a branch.
4. If `z=1,2` leave an asymptotic family after exact local use, feed that family through `delta=b(n-b)-m=r-f`, `Q=e(G[N(v)])`, and the residual ledger before adding new inequalities.
5. Keep `X_3` as a hostile control and do not promote an all-order statement.
6. Keep the mixed `{4,5}` ladder closed and do not optimize for first-proof priority on Erdos #742.
<!-- CURRENT-STATUS:END -->
