# Dense diameter-2-critical research - live current state

> **Active target - 19 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly-Foucaud-Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph `X_3` is a mandatory hostile control. Murty-Simon / Erdos #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_OMITTED_EDGE_CRITICALITY_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `33bb526779f65d895274c94864776975e742d7e3`

LATEST THEOREM PACKAGES:

- `project/research/post_ms/2026-09-19-two-omission-triangle-slack-v1/TWO_OMISSION_TRIANGLE_SLACK_LEDGER.md`
- `project/research/post_ms/2026-09-19-two-omission-triangle-slack-v1/OMITTED_EDGE_CRITICALITY_TRICHOTOMY.md`

## Audit reconciliation

Before forward mathematics this run, the current `README.md`, this state file, recent commits, the 19 September daily adversarial audit/handoff and its independent source-tuple reproof were reread. There is **no departure** from the audit priority order.

The trust boundary remains:

1. distinct physical-source identity and global selected `(source,coordinate)` uniqueness are independently re-derived at the raw/selected interface actually used downstream;
2. the finite source-tuple capacity theorem remains stated **conditional on those two named premises**, not as unconditional graph-level closure;
3. the actual-D2C regression through rooted partition, criticality slots, A-codes, Hall objects and pair-capacity quantities remains mandatory, including hostile `X_3`, with zero recorded graph/formula mismatches;
4. only the audit-authorized rigid one-code branch is being pushed, with exact `Ccap_P`, `(ONE)`, `(CROWD)` and rooted residual bookkeeping kept distinct where appropriate.

The closed mixed `{4,5}` selected-excess ladder remains closed. The four-exception gate remains subordinate. First-proof priority on Erdos #742 remains inactive.

## Mandatory negative control

`X_3` remains an explicit hostile control: `n=12`, `m=32>M(12)=31`, diameter two, every edge critical, canonical root `a=3,b=8,p=4,u=0`, `Q=12`, `r=f=delta=0`. The current unmatched-U mechanism is inactive on that canonical root and therefore does not exclude or explain away the published exception.

## Exact two-omission full-support ledger

In the purified rigid one-code `z=1`, `h=0`, full-support branch, write

- `U_-=U_{bar d}`, `|U_-|=k+1`, `k=x-g>0`;
- `U_o=U\U_-`, `u_o=u-k-1`;
- `Y=Y_1 disjoint_union Y_2`, where sources in `Y_i` omit `o_i`;
- `o_1,o_2` share the duplicated X-head `x_*`;
- `nu` = omitted Y--U_- nonedges;
- `H_Y` = Y--U_o nonedges;
- `H_X` = X--U_o nonedges;
- `M=(k+1)u_o-e(U_-,U_o)`;
- `Q_rest=Q-e(U_-,U_o)`;
- `B=(k+1)(p+k-1)`, `Z0=(k+1)(a-1)`, `D0=Z0-u(p-lambda)`, `Dbase=D0-y`.

Source visibility already gives `e(Y)=e(Y,U_d)=e(G[U_-])=0` and every used U_- witness has exactly one X-neighbour.

The exact identities proved this run are

`Z=Z0-y+nu+H_X+H_Y`,

`L_Y=y(p-g)+nu+H_Y`,

`E_-=B-y+nu+M`,

`2q+E_U=Dbase+nu+H_X+H_Y`,

`Q+E_-=B-y+nu+(k+1)u_o+Q_rest`.

Thus an edge moved into `U_- -- U_o` raises rooted triangle count Q by one and lowers U_- slack by one; `Q+E_-` is invariant under that trade.

After peeling off the forced U_- slack,

`2q+(E_U-E_-)=Z0-B-u(p-lambda)+(H_X+H_Y)-M`,

so `nu` cancels exactly from the peeled residual equation even though it remains expensive in the scorecard.

The exact score lower bound is

`S>=B-y+nu+M+max{phi(g), y(p-g)+nu+H_Y}`.

Hence each omitted-pair nonedge costs at least twice at the combined `L_Y+E_-` level. Near score equality pushes toward `nu=0` and `M=0`.

The refined integer residual floor is

`q+E_U >= E0+ceil([D-E0]_+/2)`,

with `E0=B-y+nu+M` and `D=Dbase+nu+H_X+H_Y`.

A hostile reread corrected two points before preservation: `(ONE)` substitutes only to `Ccap_P>=2xy-nu-H_Y`, and an ordinary triangle `s-x_*-o(s)` is **not** a rooted-neighbourhood triangle and must not be counted in Q.

## Exact pair-local control

In this minimal full-support branch,

`C_P=yk`, `P_P=yg`, `t_P=xy`,

and the exact purified pair bill is

`2xy<=Ccap_P=R_code(S_P)[g+2S_P/L]`.

The preserved `(ONE-P)` inequality becomes only

`Ccap_P>=2xy-nu-H_Y`,

so it is weaker after the exact crossing count is known. `(CROWD)` remains an independent aligned lower bound on `S_P`. Do not collapse `S_P,H_X,H_Y,M,nu` prematurely to total `C0`.

## New raw-criticality reduction

The omitted-edge theorem package now proves the following without assuming any unverified B-degree bound.

A critical edge `uv` lying in a triangle must have an external damaged vertex z in one of the two singleton-common-neighbour orientations. Apply this to an omitted edge `s o_i` under `nu=0`.

If `|Y_i|>=2`, the orientation based at `o_i` is impossible: its witness must lie in X, but then every member of `Y_i` is a common neighbour of that X-witness and `o_i`, contradicting singleton common neighbourhood.

Therefore every source `s` in every non-singleton omission class has an opposite-orientation certificate with `o_i z` an edge, `s z` a nonedge and

`N(s) intersect N(z)={o_i}`.

The witness z is forced into exactly one of three physical locations:

1. **ROOT:** `z=v`, which is equivalent to `N_B(s)={o_i}` and hence `d_B(s)=1`;
2. **OUT:** `z in U_o`, forcing a Y--U_o nonedge and therefore `H_Y>0`, with `d_X(z)=0`;
3. **MATCHED:** z lies in the matched B-layer, forcing an edge counted by `Q_rest>0`, again with `d_X(z)=0`.

Witnesses may be shared, so no per-source additive count is claimed.

Consequently, if `nu=H_Y=Q_rest=0`, every source in every non-singleton omission class must satisfy `N_B(s)={o_i}`. Since `alpha+beta=y` with both omission classes nonempty, if `y>=3` at least one whole omission class is forced into B-degree one.

This converts the cheapest algebraic equality vector into a sharply localized definition-level question: **can a tight-code one-code source in this rigid branch have B-degree one?** No answer is assumed until that fact is independently recovered from the foundational A-code definitions or rederived from raw criticality.

## Common-buffer comparator

The unloaded one-omission/common-buffer branch remains live. For z=1 support of size k there is one unused buffer. Source visibility gives

`H=e(Y)+e(Y,U_d)+e_- <= y`,

and any active buffer has `d_X=0`. If `H>0`, the preserved loaded-buffer strengthening gives `Z>=k(a-1)+x+H` plus a positive buffer-slack surcharge. The unloaded `H=0` branch remains the minimal comparator to the two-omission full-support model.

## Next action

Stay on z=1 and preserve the audit ordering.

1. Recover or independently rederive the exact foundational relationship between a tight A-code source and its B-neighbourhood. In particular, determine rigorously whether `d_B(s)=1` is possible in this rigid branch. Do **not** infer this from notation or from a scalar floor.
2. If tight-code sources necessarily have at least two B-neighbours, the new trichotomy immediately excludes the strict zero-correction full-support equality vector for every `y>=3`. Preserve that as a theorem only after the premise is verified.
3. If B-degree one is allowed, classify the sparse ROOT alternative directly by raw criticality and feed its forced geometry into `H_X,H_Y,M,Q_rest`.
4. Then solve the exact equality/near-equality intersection of `2xy<=Ccap_P`, `(CROWD)`, the score bound and residual floor while retaining local correction variables.
5. Compare the resulting two-omission full-support normal form with the unloaded common-buffer one-omission model. Only after both minimal z=1 geometries are exhausted should work move to z=2.

## Stop / pivot rules

- Any actual graph/formula mismatch is an immediate repair blocker.
- Keep the source-tuple theorem conditional on its two named premises.
- Do not treat finite parameter counts as D2C graph counts.
- Do not credit ordinary A-layer triangles to rooted Q.
- Do not count criticality witnesses per source without an injectivity proof.
- Keep `X_3` hostile, mixed `{4,5}` closed, four-exception subordinate and Erdos #742 first-proof priority inactive.

UNPRESERVED WORK: None. The exact ledger, hostile corrections and omitted-edge criticality trichotomy are committed. The only unfinished line is the explicitly identified foundational B-degree-one question.
<!-- CURRENT-STATUS:END -->
