# Dense diameter-2-critical research - live current state

> **Active target - 19 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly-Foucaud-Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty-Simon / Erdos #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_NEAR_SATURATION_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `a15c1d4eeb083e3d101f1be1705201e0e84b185f`

LAST VERIFIED RESULT: The 19 September audit-mandated graph-to-Hall/pair-capacity regression has been completed with no graph/formula mismatch, and the authorized rigid one-code line has advanced materially. Pair purity gives `h_P=0`, `k=(x-g_P)_+` complementary unmatched witnesses per outside source, the gamma/U score tradeoff, purified `(ONE-P)`, `(CHAN-P)`, and residual feedback. A new bidirectional-reservoir theorem proves that A/U traffic, same-code `Y--U_d` edges and same-code `U_{bar d}` edges compete for the same physical `Y x U_{bar d}` source/witness pairs, yielding `yk+e_++e_-<=y u_-`, a weighted analogue and a crowding/reservoir cylinder gate. The saturated layer `u_{bar d}=k` is a complete rectangular witness transversal and forces `E_{bar d}>=k(p+k-2)`. The first near-saturated layer `u_{bar d}=k+1` is now classified into exactly two support types. In the common-buffer type, all `k` crossing witnesses form a saturated core, every auxiliary certificate is routed through the unique buffer, the core remains independent and pays `E>=k(p+k-2)`, and each buffer use adds one unit to the rooted A--U defect. In the full-support type, if `rho` is the number of crossing holes and `H=e_++e_-`, then `H<=rho`, `E_- >= (k+1)(p+k-1)-rho+H-2e_-`, and `Z>=k(a-1)+(a-1)-rho+H`; in particular `E_->=[(k+1)(p+k-1)-2y]_+` and `Z>=k(a-1)+(x-1)`. Both branches feed directly into the exact residual `delta=r-f` ledger.

UNPRESERVED WORK: None. No uncommitted theorem is being relied upon.

DEFERRED ADMIN: Root README does not yet list the new 19 September reservoir/z=1 package; refresh it at the next reviewer-facing status or daily-audit checkpoint rather than spending this live theorem session on a large status-only rewrite. Historical Git-LFS checkout warnings for seven legacy ZIP paths remain preserved and non-blocking.

NEXT ACTION: Stay on the exact one-code geometry. For the `z=1` common-buffer branch, combine the one-buffer routing with buffer degree/slack and `(ONE-P)/(CHAN-P)` to determine whether internal-Y traffic, `Y--U_d` traffic and the star `G[U_{bar d}]` can coexist without exceeding `C0`. For the full-support branch, keep the exact variables `rho,H,e_+,e_-` in the paired inequalities `E_- >= (k+1)(p+k-1)-rho+H-2e_-` and `Z>=k(a-1)+(a-1)-rho+H` and eliminate them jointly before relaxing to `y`. Only after the exact `z=1` layer is exhausted should `z=2` or the non-rigid Hall branch be considered. Keep the mixed `{4,5}` ladder closed and the four-exception gate subordinate.

## Mandatory audit reconciliation

The latest daily adversarial audit remains:

- `project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`
- `project/research/post_ms/2026-09-19-daily-red-team-audit-v1/INDEPENDENT_SOURCE_TUPLE_REPROOF.md`

Its required priority order was: repair the two source-tuple premises; build actual-graph regression through the rooted/Hall interface with `X_3`; only then push the exact pair-local one-code branch and feed survivors into the rooted residual ledger. This run followed that order. No mathematical departure from the audit's proposed priorities was made.

## Upstream source-premise repair retained

Package:

- `project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/SOURCE_PREMISE_GRAPH_AUDIT.md`
- `project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/SOURCE_PREMISE_REPAIR.md`
- `project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/check_source_premises_graph_level.py`

P1 is a direct raw-criticality fact at the correct beta orientation: reuse of one physical `(x,y)` at two target fibres would force fixed `N(x) cap N(y)` to equal two distinct singleton tight endpoints. P2 is selected-representative uniqueness for a physical rooted B-edge/source-coordinate obligation, not raw candidate-witness uniqueness. `B_beta` counts the same selected physical obligations. The earlier checker that mislabeled the alpha orientation as beta remains explicitly withdrawn in the correction trail.

## Independent actual-graph regression through pair capacity

Package:

- `project/research/post_ms/2026-09-19-rigid-graph-regression-v1/RIGID_GRAPH_LEVEL_REGRESSION.md`
- `project/research/post_ms/2026-09-19-rigid-graph-regression-v1/check_rigid_graph_level.py`
- `project/research/post_ms/2026-09-19-rigid-graph-regression-v1/RIGID_GRAPH_REGRESSION_SUMMARY.json`

The independent checker reconstructs actual D2C graphs through rooted partition, tight A/U codes, rooted witness slots, direct/non-direct A-edge criticality, matched-foot gamma codes, A/U complementary witnesses, pair-local `L_P,S_P,Z_P,R_P,g_P,h_P`, exact `Ccap_P`, and exact Hall-cut decomposition. The recorded three certificate policies contain 3,540 root-policy instances, 114 qualified pair/slack instances, 147 pair-local `Ccap_P` checks, 96 one-sided pair checks, 36 exact Hall-cut decompositions and zero mismatches. A genuine matched-B A-edge positive control is exercised.

No actual rigid complete Hall cut with `x>=3` was found in the bounded corpus. Therefore the rigid singleton-head and one-code theorems below remain conditional hand deductions from graph-regressed upstream ingredients, not empirical graph claims.

### Mandatory `X_3` hostile control

The regression still verifies:

- `n=12`, `m=32>M(12)=31`;
- diameter two and every edge critical;
- canonical cube root `a=3,b=8,p=4,u=0`;
- `Q=12,r=f=delta=0`;
- no nontrivial rigid complete A-cut.

The companion cube-face family shows exact rooted slot saturation is scalable but does not imply above-`M(n)` density. Nothing in the new one-code mechanism suppresses `X_3`.

## One-code purification retained

Package:

- `project/research/post_ms/2026-09-19-rigid-graph-regression-v1/ONE_CODE_PAIR_PURIFICATION.md`
- `project/research/post_ms/2026-09-19-rigid-graph-regression-v1/check_one_code_pair_purification.py`

For one outside code `d`, pair purity gives `A_{bar d}=emptyset`. If `g=g_P`, every outside source has at most `g` matched crossing witnesses and therefore at least

`k=(x-g)_+`

witnesses in `U_{bar d}`. The two-sided matched-foot term vanishes exactly: `h_P=0`.

The retained key inequalities are

`S>=phi(g)+(x-g)_+(p-1)` for `p-y>=1`,

`R_code(S_P)[g+2S_P/L]+L_Y >= y(p+x+k)` (`ONE-P`),

and, for `g<=x`,

`L_Y+2(u_bar L_Y+yE_bar)/L >= y(p+2x-3g)` (`CHAN-P`).

## Bidirectional one-code reservoir

Package:

- `project/research/post_ms/2026-09-19-one-code-reservoir-v1/ONE_CODE_BIDIRECTIONAL_RESERVOIR.md`
- `project/research/post_ms/2026-09-19-one-code-reservoir-v1/check_one_code_bidirectional_reservoir.py`
- `project/research/post_ms/2026-09-19-one-code-reservoir-v1/ONE_CODE_BIDIRECTIONAL_RESERVOIR_AUDIT_SUMMARY.json`
- `project/research/post_ms/2026-09-19-one-code-reservoir-v1/SATURATED_RESERVOIR_REFINEMENT.md`

Put `U_+=U_d`, `U_-=U_{bar d}`, `e_+=e(G[Y union U_+])`, `e_-=e(G[U_-])`. Because `A_{bar d}=emptyset`, `U_+` is independent. Three certificate families inject into the same physical `Y x U_-` pair set: A/U traffic `C_P`, same-code `Y--U_+` edges, and same-code `U_---U_-` edges. Cross-family collision is impossible because the fixed singleton common-neighbour set would have to have heads in disjoint vertex classes. Thus

`C_P+e(Y,U_+)+e_- <= y u_-`,

and using the crossing demand,

`yk+e_++e_- <= y u_-`,

`e_++e_- <= y(u_--k)`.

The weighted version is

`L[yk+e_++e_-] <= u_-L_Y+yE_-`.

Combining with coded-layer crowding gives the exact cylinder gate

`[(y+u_+)(y+u_+-T0)-u_+-(L_Y+E_+)]_+`
` +[u_-(u_--T0-1)-E_-]_+ <= 2y(u_--k)`.

A deliberately relaxed arithmetic audit rejected 17,877 of 106,368 old-population states versus 16,967 from the prior shared gamma/U floor: 910 additional robust arithmetic exclusions. This is diagnostic only.

### Saturated layer `z=u_--k=0`

At `u_-=k>0`, the reservoir is fully exhausted by crossing witnesses. The crossing certificate system is a complete rectangular product: every source uses all `g` relevant matched feet and all `k` unmatched complementary witnesses, and those `g+k=x` witness objects are in bijection with the heads in `X`. Exact degree counting yields

`E_- >= k(p+k-2)`,

`L_Y >= y(p-g+u_+) >= y(p-g)`,

and therefore

`S >= max(phi(g),y(p-g))+k(p+k-2)`.

The strengthened U-slack feeds into

`q+E_U >= E_sat+ceil([k(a-1)-u(p-lambda)-E_sat]_+/2)`,

`E_sat=k(p+k-2)`,

and hence directly raises forced A-edge mass `f`. In the bounded diagnostic, 22,998 states that had a saturated gamma choice under the older shared floor lose that choice under the exact saturated score floor.

## First near-saturated layer `z=1`

Package:

- `project/research/post_ms/2026-09-19-one-code-reservoir-v1/ONE_CODE_Z1_NEAR_SATURATION.md`
- `project/research/post_ms/2026-09-19-one-code-reservoir-v1/check_one_code_z1_near_saturation.py`
- `project/research/post_ms/2026-09-19-one-code-reservoir-v1/ONE_CODE_Z1_NEAR_SATURATION_AUDIT_SUMMARY.json`

Assume `u_-=k+1`, `k>0`. The union of complementary unmatched crossing witnesses has size exactly `k` or `k+1`; there is no intermediate case.

### Common-buffer branch

If only `k` vertices are used, every source uses the same `k`-set `W_0` and the remaining vertex `b` is a common buffer. Every `Y x W_0` physical pair is already consumed by a crossing certificate. Therefore:

- `W_0` is independent;
- every `U_-` edge is incident with `b` and must be sourced at `b`;
- every selected auxiliary object counted by `H=e_++e_-` is routed through a distinct pair in `Y x {b}`;
- each core witness still satisfies `epsilon_w>=p+k-2`, so `E_- >= k(p+k-2)`;
- each actual buffer use is a new Y--U nonedge, giving
  `Z>=k(a-1)+H`.

Thus with `E_core=k(p+k-2)` and `D_core=k(a-1)+H-u(p-lambda)`,

`q+E_U >= E_core+ceil([D_core-E_core]_+/2)`.

### Full-support branch

If all `k+1` vertices are used, let `rho` be the number of source rows with one crossing hole, so crossing incidence count is `I=yk+y-rho`. Every auxiliary object must use a crossing hole, hence `H<=rho`. Writing `e_-=e(G[U_-])`, degree counting on the `k+1` used witnesses gives

`E_- >= (k+1)(p+k-1)-rho+H-2e_-`.

Equivalently, since `H=e_++e_-`,

`E_- >= (k+1)(p+k-1)-rho+e_+-e_-`.

The safe pure floor is

`E_- >= [(k+1)(p+k-1)-2y]_+`.

The defect simultaneously strengthens to

`Z>=k(a-1)+(a-1)-rho+H`,

and hence

`Z>=k(a-1)+(x-1)`.

These are deliberately kept as paired exact inequalities because the same hole budget `rho` controls both possible slack relief and residual defect.

### `z=1` diagnostic

Across the same bounded comparison box:

- old one-code population states: `106,368`;
- states admitting a `k>0`, `k+1<=u` gamma choice under the older shared floor: `86,820`;
- common-buffer gate survivors: `76,463`;
- full-support gate survivors: `77,310`;
- survivors of either support type: `78,167`.

So the exact first-near-saturation score floors eliminate `8,653` states that previously admitted a `z=1` choice. These are parameter diagnostics, not graph counts.

## Trust boundary

- Source-tuple finite capacity: abstract theorem independently re-derived; P1/P2 repaired at the exact raw/selected levels used.
- `B_beta`: selected physical-obligation semantics audited.
- Actual graph -> rooted/Hall/pair-capacity interface: independently reconstructed on a bounded D2C corpus with zero mismatches; `X_3` remains mandatory.
- Rigid-cut existence/realizability: no positive actual-graph fixture with `x>=3` has been found; downstream rigid theorems remain conditional.
- One-code purification, reservoir, saturation and `z=1` classification: hand-derived structural mathematics with arithmetic diagnostics; not external review and not a global eventual theorem.
- Four-exception gate: supported but not load-bearing here.

## Stop / pivot criteria

1. Any actual D2C mismatch with the graph-to-pair interface is an immediate blocker and forces proof repair.
2. Do not count abstract parameter survivors/rejections as D2C graphs.
3. Exhaust the exact `z=1` variables before relaxing to `y` or proceeding to `z=2`.
4. If `z=1,2` leave an asymptotic family after exact local use, feed it through `delta=b(n-b)-m=r-f`, `Q=e(G[N(v)])`, and the exact residual ledger before adding new global inequalities.
5. Keep `X_3` as a hostile control and do not promote an all-order statement.
6. Keep the mixed `{4,5}` ladder closed and do not optimize for first-proof priority on Erdos #742.
<!-- CURRENT-STATUS:END -->
