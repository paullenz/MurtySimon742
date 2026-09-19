# Dense diameter-2-critical research - live current state

> **Active target - 19 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly-Foucaud-Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph `X_3` is a mandatory hostile control. Murty-Simon / Erdos #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_TWO_OMISSION_EXACT_LEDGER_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `33bb526779f65d895274c94864776975e742d7e3`

LATEST THEOREM PACKAGE:

`project/research/post_ms/2026-09-19-two-omission-triangle-slack-v1/TWO_OMISSION_TRIANGLE_SLACK_LEDGER.md`

LAST VERIFIED RESULT: After rereading the current README/state, latest commits and the 19 September daily red-team audit/handoff, the run followed the audit-authorized rigid one-code branch without a priority departure. The already-repaired two source-tuple premises and actual-graph regression (including hostile `X_3`) remain mandatory upstream controls. Starting from the graph-level source-visibility purification, the minimal full-support `z=1`, `h=0` survivor is now described by exact physical correction terms rather than only scalar floors. The two-omission design has `Y=Y_1 disjoint_union Y_2`, omission vertices `o_1,o_2` sharing one duplicated X-head, regular U-witness multiplicity y and omission multiplicities `beta,alpha`. If `nu` counts omitted source--U_- pairs that are nonedges, `U_o=U\U_-`, `H_X,H_Y` count A--U_o nonedges by side, and `M` counts missing `U_- -- U_o` edges, then

`Z=Z0-y+nu+H_X+H_Y`,

`L_Y=y(p-g)+nu+H_Y`,

`E_-=B-y+nu+M`.

The last identity is exact, not a floor. It yields the exact rooted triangle/slack cancellation

`Q+E_-=B-y+nu+(k+1)|U_o|+Q_rest`,

where `Q_rest=Q-e(U_-,U_o)>=0`. Thus moving an edge into `U_- -- U_o` raises rooted triangle count Q by one and lowers U_- slack by one: the sum is invariant. The exact residual equation becomes

`2q+E_U=Dbase+nu+H_X+H_Y`,

and after removing the forced U_- slack,

`2q+(E_U-E_-)=Z0-B-u(p-lambda)+(H_X+H_Y)-M`;

notably `nu` cancels from this peeled residual equation even though it remains expensive in the scorecard. The exact score lower bound is

`S>=B-y+nu+M+max{phi(g), y(p-g)+nu+H_Y}`.

Hence each omitted-pair nonedge costs at least twice at the combined `L_Y+E_-` level. Near scorecard equality the branch is forced toward `nu=0` and `M=0`: omitted pairs are edges and `U_-` is complete to the rest of U.

The pair-local audit obligation is retained exactly. In this purified full-support model `t_P=xy` and

`2xy<=Ccap_P=R_code(S_P)[g+2S_P/L]`.

Substituting the exact `L_Y` into preserved `(ONE-P)` gives only `Ccap_P>=2xy-nu-H_Y`, so the exact crossing-capacity inequality is strictly the cleaner/stronger statement. `(CROWD)` remains a separate aligned lower bound on `S_P`; do not collapse the local correction variables prematurely to total `C0`.

A self-audit correction was preserved explicitly: when `nu=0`, the omitted edge `s-o(s)` and duplicated X-head `x_*` form an ordinary triangle `s-x_*-o(s)`, but this is **not** a rooted-neighbourhood triangle because `s,x_*` lie in A. It must not be credited to `Q=e(G[N(v)])`.

UNPRESERVED WORK: None. The exact ledger, proof derivations, self-correction, pair-capacity reconciliation, trust boundary and next-work proposal are preserved in the theorem package above. The theorem note was corrected after hostile reread so that `(ONE)` substitutes to `Ccap_P>=2xy-nu-H_Y`, and `D0=Z0-u(p-lambda)` is explicitly defined.

DEFERRED ADMIN: Root `README.md` has not yet been expanded with the one-code reservoir / z=1 closure / source-visibility / exact two-omission ledger packages. Refresh it at the next reviewer-facing status or daily-audit checkpoint. Historical Git-LFS warnings for seven legacy ZIP paths remain preserved and non-blocking.

NEXT ACTION: Stay on z=1. First attack the equality/near-equality vector by raw edge-criticality, beginning with `nu=M=0`: every omitted source--U_- pair is then an edge and `U_-` is complete to `U_o`. Determine whether criticality of an omitted edge `s o(s)` can coexist with the duplicated X-head without forcing an extra A--U hole, extra B-edge/rooted triangle, or a forbidden second common neighbour. In parallel solve the exact intersection of `2xy<=Ccap_P`, `(CROWD)`, the score bound above and the refined rooted residual floor while retaining `S_P,H_X,H_Y,M,nu`. Compare the resulting full-support normal form directly with the unloaded common-buffer one-omission model. Only after these two minimal z=1 geometries are exhausted should work move to z=2. Keep the mixed `{4,5}` ladder closed, the four-exception gate subordinate, first-proof priority on Erdos #742 inactive, and `X_3` hostile.

## Mandatory audit reconciliation

Latest daily audit:

- `project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`
- `project/research/post_ms/2026-09-19-daily-red-team-audit-v1/INDEPENDENT_SOURCE_TUPLE_REPROOF.md`

The audit priority order remains: independently verify the two source-tuple premises; maintain actual-graph regression through rooted/Hall/pair-capacity objects with `X_3`; only then push exact pair-local one-code geometry and feed survivors into the residual ledger. Those upstream obligations were reread before this session and remain satisfied at their intended trust boundary. This session is a direct continuation of the audit plan, not a departure.

## Upstream trust boundary

### Source-tuple premises

Package: `project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/`.

P1 remains a raw-criticality physical-source fact at the correct beta orientation. P2 remains selected-representative uniqueness for one physical rooted B-edge/source-coordinate obligation, not raw-witness uniqueness. The finite source-tuple capacity theorem is independently re-derived **conditional on these two named premises**; do not describe it as unconditional graph-level closure.

### Actual graph -> Hall / pair-capacity regression

Package: `project/research/post_ms/2026-09-19-rigid-graph-regression-v1/`.

Recorded coverage remains 3,540 root-policy instances, 114 qualified pair/slack instances, 147 exact `Ccap_P` checks, 96 one-sided-pair checks, 36 exact Hall-cut decompositions, zero recorded graph/formula mismatches, with a genuine matched-B positive control. No actual rigid complete Hall cut with `x>=3` occurs in the bounded corpus, so the rigid one-code theorems remain conditional hand deductions from graph-regressed upstream ingredients rather than empirical graph classification.

### Mandatory `X_3`

The explicit fixture verifies `n=12`, `m=32>M(12)=31`, diameter two, every edge critical, canonical root `a=3,b=8,p=4,u=0`, and `Q=12,r=f=delta=0`. The present mechanism requires unmatched U-witnesses and is inactive on this canonical root. `X_3` is a hostile negative control, never evidence for an eventual theorem.

## Corrected z=1 lineage

Load-bearing corrected predecessor:

`project/research/post_ms/2026-09-19-one-code-reservoir-v1/ONE_CODE_Z1_NEAR_SATURATION_V2.md`.

The first v1 proof that all internal Y-edges selected the A/U channel remains invalid. Do not reuse it.

Source-visibility purification:

`project/research/post_ms/2026-09-19-one-code-source-visibility-v1/`.

If `W` is the crossing U-witness union and `B_U=U_-\W`, every used witness has exactly one X-neighbour and is sterile for auxiliary same-code singleton-common-neighbour certificates with heads outside X. Therefore auxiliary traffic lives on buffers. In z=1 full support there are no buffers, so

`e(Y)=e(Y,U_d)=e(G[U_-])=0`.

At minimal `h=0`, full support has exactly two omission types and one duplicated X-head. One omission type is precisely the common-buffer model.

## Exact two-omission correction ledger

Package:

`project/research/post_ms/2026-09-19-two-omission-triangle-slack-v1/`.

Write `U_o=U\U_-`, `u_o=u-k-1`, and let

- `nu` = omitted Y--U_- nonedges;
- `H_Y` = Y--U_o nonedges;
- `H_X` = X--U_o nonedges;
- `M=(k+1)u_o-e(U_-,U_o)`;
- `Q_rest=Q-e(U_-,U_o)`.

Then the exact identities are

`Z=Z0-y+nu+H_X+H_Y`,

`L_Y=y(p-g)+nu+H_Y`,

`E_-=B-y+nu+M`,

`Q+E_-=B-y+nu+(k+1)u_o+Q_rest`.

The individual U_- slack identity is

`epsilon_w=p-y+k-1+t_w+nu_w+m_w`,

which also yields

`E_->=(k-1)(p+k-1)+[2(p+k-1)-y]_+`

and

`max(epsilon_{o_1},epsilon_{o_2}) >= [p-y+k-1+ceil(y/2)]_+`.

The refined residual constraints are

`2q+E_U=Dbase+nu+H_X+H_Y`,

`q+E_U >= E0+ceil([D-E0]_+/2)`,

with `E0=B-y+nu+M` and `D=Dbase+nu+H_X+H_Y`.

These are structural hand identities/floors inside the already-purified branch, not finite-scan claims.

## Pair-local control

Preserved exact capacity:

`Ccap_P=R_code(S_P)[g+2S_P/L]`.

In the minimal full-support branch:

`C_P=yk`, `P_P=yg`, `t_P=xy`,

so

`2xy<=Ccap_P`.

Preserved `(ONE-P)` is weaker after exact Y-slack substitution:

`Ccap_P>=2xy-nu-H_Y`.

Keep `(CROWD)` alongside the exact capacity, but retain pair-local and physical correction variables. Do not replace everything by a total-score scalar unless the loss is explicitly audited.

## Common buffer retained

The unloaded one-omission/common-buffer branch remains live. For z=1 support of size k there is one unused buffer. Source visibility gives

`H=e(Y)+e(Y,U_d)+e_- <= y`,

and any active buffer has `d_X=0`. The previously preserved loaded-buffer strengthening remains valid: if `H>0`, `Z>=k(a-1)+x+H`, with the positive buffer-slack surcharge. The unloaded `H=0` branch is the minimal one-omission comparator to the two-omission full-support model.

## Trust boundary / stop-pivot rules

- Any actual graph/formula mismatch is an immediate blocker and triggers repair before downstream theory.
- Keep the finite source-tuple theorem conditional on its two named premises.
- Do not treat finite parameter counts as D2C graph counts.
- Do not credit ordinary A-layer triangles to rooted `Q`.
- Exhaust the two-omission duplicated-head model and unloaded common-buffer model before beginning z=2.
- Keep `X_3` hostile, the mixed `{4,5}` ladder closed, the four-exception gate subordinate, and first-proof priority on Erdos #742 inactive.
<!-- CURRENT-STATUS:END -->
