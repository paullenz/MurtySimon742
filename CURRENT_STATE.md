# Dense diameter-2-critical research - live current state

> **Active target - 19 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly-Foucaud-Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty-Simon / Erdos #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_EXACT_ELIMINATION_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `a15c1d4eeb083e3d101f1be1705201e0e84b185f`

LAST VERIFIED RESULT: The audit-mandated source-premise repair and independent actual-graph regression now reach the exact Hall/pair-capacity interface with no graph/formula mismatch and with `X_3` retained as a hostile control. The authorized rigid one-code branch has then been sharpened through pair purification, a bidirectional physical-pair reservoir, exact saturated geometry, and a complete first near-saturated (`z=u_{bar d}-k=1`) support dichotomy. In the common-buffer branch the `k` crossing witnesses form a saturated core; every auxiliary certificate is forced through the single buffer; the core pays `E>=k(p+k-2)`; and actual buffer use adds both defect and buffer slack. In the full-support branch the crossing-hole variables admit an exact normal form. Writing `j=rho-H`, `B=(k+1)(p+k-1)`, and `Z0=(k+1)(a-1)`, one has `E_- >= B-j-2e_-`, `Z>=Z0-j`, and `j+e_-<=y`. Hence, in the regime `B>=2y`, with `Ebase=B-2y` and `D0=Z0-u(p-lambda)`, the hole/edge tradeoff cancels exactly in the residual minimization: `q+E_U >= Ebase+ceil([D0-Ebase]_+/2)`. This removes `rho,H,e_-` without the coarse losses from bounding them separately and feeds directly into the forced A-edge mass `f`.

UNPRESERVED WORK: None. No uncommitted theorem or diagnostic is being relied upon.

DEFERRED ADMIN: Root `README.md` has not yet been expanded with the new reservoir / `z=1` package. Refresh it at the next reviewer-facing status or daily-audit checkpoint; the live mathematical handoff is complete here. Historical Git-LFS warnings for seven legacy ZIP paths remain preserved and non-blocking.

NEXT ACTION: Finish the exact `z=1` layer before considering `z=2`. For the common-buffer branch, combine the used-buffer surcharge `epsilon_b >= [p-y+k+e_+]_+`, the aggregate source/buffer bound, `Z>=k(a-1)+H`, and `(ONE-P)/(CHAN-P)` to isolate the zero-auxiliary equality model from the genuinely loaded buffer cases. For full support, use the new hole-free residual floor against the available A-edge/direct-edge structure; the only unresolved strip requiring separate handling is where `B=(k+1)(p+k-1)<2y`, because there the non-negativity truncation can interrupt the exact cancellation. Preserve pair-local variables until those two subcases are resolved. Keep the mixed `{4,5}` ladder closed and the four-exception gate subordinate.

## Mandatory audit reconciliation

Latest daily adversarial audit:

- `project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`
- `project/research/post_ms/2026-09-19-daily-red-team-audit-v1/INDEPENDENT_SOURCE_TUPLE_REPROOF.md`

The audit required: (1) repair the two source-tuple premises from raw/selected criticality semantics; (2) build actual-graph regression through rooted/Hall objects with `X_3`; (3) only then push exact pair-local one-code geometry and feed survivors into the rooted residual ledger. This run follows that order with no mathematical departure.

## Upstream trust boundary

### Source-tuple premises

Package: `project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/`.

P1 is now a direct raw-criticality fact at the correct beta orientation: reuse of one physical `(x,y)` at two target fibres would force the fixed set `N(x) cap N(y)` to be two different singleton tight endpoints. P2 is selected-representative uniqueness for one physical rooted B-edge/source-coordinate obligation, not raw-witness uniqueness. `B_beta` counts those selected physical obligations. The earlier checker that mislabeled alpha orientation as beta is explicitly withdrawn in the correction trail.

### Actual graph -> Hall / pair-capacity regression

Package: `project/research/post_ms/2026-09-19-rigid-graph-regression-v1/`.

The independent checker reconstructs actual D2C graphs through rooted partition, tight A/U codes, rooted witness slots, direct/non-direct A-edge criticality, matched-foot gamma codes, A/U complementary witnesses, pair-local `L_P,S_P,Z_P,R_P,g_P,h_P`, exact `Ccap_P`, and exact Hall-cut decomposition. Recorded coverage: 3,540 root-policy instances, 114 qualified pair/slack instances, 147 pair-local `Ccap_P` checks, 96 one-sided pair checks, 36 exact Hall-cut decompositions, zero mismatches. A genuine matched-B positive control is exercised.

No actual rigid complete Hall cut with `x>=3` was found in the bounded corpus. The rigid one-code theorems therefore remain conditional hand deductions from graph-regressed upstream ingredients.

### Mandatory `X_3` control

The explicit fixture still verifies `n=12`, `m=32>M(12)=31`, diameter two, every edge critical, canonical cube root `a=3,b=8,p=4,u=0`, and `Q=12,r=f=delta=0`. There is no nontrivial rigid complete A-cut at that root. None of the new one-code results suppresses the known exception.

## One-code purification

Package: `project/research/post_ms/2026-09-19-rigid-graph-regression-v1/ONE_CODE_PAIR_PURIFICATION.md`.

For one outside code `d`, pair purity gives `A_{bar d}=emptyset`; with `g=g_P`, every outside source has at most `g` matched crossing witnesses and at least

`k=(x-g)_+`

witnesses in `U_{bar d}`. Also `h_P=0`. Key retained inequalities include

`S>=phi(g)+(x-g)_+(p-1)` (when `p-y>=1`),

`R_code(S_P)[g+2S_P/L]+L_Y >= y(p+x+k)` (`ONE-P`),

and

`L_Y+2(u_bar L_Y+yE_bar)/L >= y(p+2x-3g)` (`CHAN-P`).

## Bidirectional physical-pair reservoir

Package: `project/research/post_ms/2026-09-19-one-code-reservoir-v1/ONE_CODE_BIDIRECTIONAL_RESERVOIR.md` plus its checker/summary.

Put `U_+=U_d`, `U_-=U_{bar d}`, `e_+=e(G[Y union U_+])`, `e_-=e(G[U_-])`. Because `A_{bar d}=emptyset`, `U_+` is independent. A/U traffic `C_P`, same-code `Y--U_+` edges, and same-code `U_---U_-` edges all inject into the same physical `Y x U_-` pair set. Cross-family collision is impossible because one fixed physical pair has one fixed singleton common-neighbour head. Therefore

`yk+e_++e_- <= y u_-`,

`e_++e_- <= y(u_--k)`,

and the weighted form is

`L[yk+e_++e_-] <= u_-L_Y+yE_-`.

Coded-layer crowding then gives

`[(y+u_+)(y+u_+-T0)-u_+-(L_Y+E_+)]_+`
` +[u_-(u_--T0-1)-E_-]_+ <= 2y(u_--k)`.

A deliberately relaxed arithmetic diagnostic rejects 17,877 of 106,368 old-population states, versus 16,967 from the previous shared gamma/U floor (910 additional robust arithmetic exclusions). Diagnostic only, not graph counts.

## Saturated layer `z=u_--k=0`

Package: `SATURATED_RESERVOIR_REFINEMENT.md`.

For `u_-=k>0`, the crossing certificate system is a complete rectangular product: every outside source uses all `g` relevant matched feet and all `k` unmatched complementary witnesses, and those `g+k=x` witness objects are in bijection with the heads in `X`. Exact degree counting gives

`E_- >= k(p+k-2)`,

`L_Y >= y(p-g+u_+) >= y(p-g)`,

so

`S >= max(phi(g),y(p-g))+k(p+k-2)`.

The saturated U-slack feeds into the exact residual ledger. The bounded diagnostic eliminates 22,998 states that had a saturated gamma choice under the older shared score floor.

## First near-saturated layer `z=1`

Main package:

- `ONE_CODE_Z1_NEAR_SATURATION.md`
- `check_one_code_z1_near_saturation.py`
- `ONE_CODE_Z1_NEAR_SATURATION_AUDIT_SUMMARY.json`
- `ONE_CODE_Z1_EXACT_ELIMINATION.md`

Assume `u_-=k+1`, `k>0`. The union of crossing witnesses has size exactly `k` or `k+1`.

### Common buffer

If only `k` are used, every source uses the same saturated core `W_0` and the remaining vertex `b` is a common buffer. Every `Y x W_0` pair is occupied by a crossing certificate. Therefore `W_0` is independent, every `U_-` edge is incident with `b`, and every auxiliary selected object is routed through a distinct pair in `Y x {b}`. The core pays

`E_core>=k(p+k-2)`.

If `H=e_++e_-`, then

`Z>=k(a-1)+H`.

If `H>0`, the buffer cannot have an X-neighbour and satisfies

`epsilon_b >= [p-y+k+H-e_-]_+=[p-y+k+e_+]_+`.

The exact Y-degree identity also yields the aggregate source/buffer relation recorded in `ONE_CODE_Z1_EXACT_ELIMINATION.md`; in particular internal-Y traffic cannot create free scorecard relief by moving all payment onto the buffer.

### Full support

If all `k+1` complementary U vertices are used, let `rho` be the number of crossing holes and `H=e_++e_-` the number of auxiliary hole uses. Then `H<=rho`. With

`j=rho-H`,

one has the exact normal form

`E_- >= B-j-2e_-`,

`Z>=Z0-j`,

`j+e_-<=y`,

where

`B=(k+1)(p+k-1)`,

`Z0=(k+1)(a-1)`.

Thus, if `B>=2y`, put

`Ebase=B-2y`,

`D0=Z0-u(p-lambda)`.

The same hole variable raises the U-slack floor by one and lowers the residual-defect floor by one. This cancels exactly in the integer minimization, giving the hole-free result

`q+E_U >= Ebase+ceil([D0-Ebase]_+/2)`.

Consequently

`f >= (p-lambda)(p+u)+Ebase+ceil([D0-Ebase]_+/2)-delta`.

The remaining full-support strip is `B<2y`, where the zero truncation in the U-slack floor requires separate treatment.

### `z=1` diagnostic

In the standard bounded comparison box, 86,820 states admit a `k>0`, `k+1<=u` gamma choice under the older shared floor; 78,167 retain at least one of the two exact `z=1` support types after the new score floors. Thus 8,653 previously `z=1`-compatible parameter states are removed. Diagnostic only.

## Trust boundary and stop/pivot criteria

- Source-tuple finite capacity: independently re-derived conditional theorem; P1/P2 repaired at required raw/selected levels.
- Actual graph -> rooted/Hall/pair-capacity interface: independently reconstructed on bounded D2C graphs with zero mismatches; `X_3` mandatory.
- Rigid-cut existence: no positive actual-graph fixture with `x>=3`; downstream rigid theorems remain conditional.
- One-code purification, reservoir, saturation, `z=1`, and exact hole elimination: hand-derived structural mathematics with arithmetic diagnostics; not external review and not a global eventual theorem.
- Any actual D2C graph/formula mismatch is an immediate blocker.
- Do not interpret abstract parameter counts as graph counts.
- Exhaust common-buffer loaded/equality cases and the `B<2y` full-support strip before `z=2`.
- Feed all survivors through `delta=b(n-b)-m=r-f`, `Q=e(G[N(v)])`, and the exact rooted residual ledger before adding a new global scalar relaxation.
- Keep `X_3` as hostile control, the mixed `{4,5}` ladder closed, and first-proof priority on Erdos #742 inactive.
<!-- CURRENT-STATUS:END -->
