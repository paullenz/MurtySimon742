# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-19  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is **not** the target. The published 2024 D2C graph `X_3` on 12 vertices and 32 edges has `M(12)=31` and remains a mandatory negative control. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not an optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_MINIMAL_RESERVOIR_E1_SUPPORT_CHANNEL_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `46240212375c7b2de7c254990b9b7ad301e367be`

LAST VERIFIED RESULT: `In the m=g+1 one-defect E=1 branch, support intersection reduces every selected-witness wrong-head adjacency to one of the two coordinates of the unique radius-two defect. The repeated core class must be treated separately: for k>1,d0=g-A=1, J<=k+1+min(2Delta,2); for k>1,d0=0, J<=F_k(Delta), where F_k(0,1,2)=0,2,4 and F_k(Delta)=min(k+2,Delta+1) for Delta>=3; for k=1, J<=min(2d0+2Delta,4). Both directed adjacencies on one defect/radius-one singleton channel are locally compatible with the existing singleton certificates, so the factor two cannot be removed by local criticality alone. Combining the correct support envelope with L_X>=[D+2Delta]_+ gives the refined pair gate p(g+1)+k+M+Psi_{k,d0}(D)<=C0-sigma_P, with closed forms Psi=max(D-(k+1),-(k+3)) for k>1,d0=1 and Psi=max(D-2d0,-4) for k=1, and an exact finite candidate formula for k>1,d0=0. The d0=1/k=1 cases give explicit M intervals and clamped rooted residual optimizers. In the support-saturated d0=1 pattern J=k+3, all k+1 possible zero-Hamming-excess defect/radius-one head edges are forced absent, so every actual X-edge has positive Hamming excess and r>=a+y+1+eta(e(X)); the same strengthened slot conclusion holds for d0=0,Delta=2,J=4. In t=1 every E1 survivor obeys (a+2)^2<=u^2+2pu+2u+6p-2k^2+4k-3-parity(lambda)-2(M+tau_P), tau_P=sigma_P-P0. Corrected bounded replay closes the E1 route in 4,758 abstract states (693 at t=1), reducing E1-feasible states 53,435->48,677 and t=1 E1-feasible states 5,164->4,471; rows fall 1,212,749->1,094,326 and 128,750->111,204 at t=1. The full union remains 64,457 and t=1 remains 5,404 because alternate E>=2 or cheap-sphere routes survive. Pointwise rooted q/E_U lower/upper intersection adds zero further exclusions on all 1,094,326 new E1 rows.`

UNPRESERVED WORK: `None. The corrected theorem and checker are preserved under project/research/post_ms/2026-09-19-one-defect-support-cap-v1/. Commit b1da3e8e0b7c882cf0076fe960be93bb94a91eba preserved an over-strong intermediate d0=0 J<=4 simplification; the immediately following repair supersedes it with the repeated-core-aware F_k(Delta) envelope. The error is intentionally preserved in history rather than hidden.`

DEFERRED ADMIN: `README remains lower-frequency. Refresh reviewer-facing status at the next daily adversarial checkpoint unless repository integrity requires an earlier repair.`

NEXT ACTION: `Stay on m=g+1 and t=1. First exploit the new saturated-support slot theorem in the pair-budget equality/near-equality rows: for d0=1 classify when J=k+3 is forced and combine r>=a+y+1+eta(e(X)) with the exact pair-density lower bound; for d0=0 classify the transition from two singleton bidirected channels to the one-way repeated-core channel. Use the exact d0=1 M interval and WIDTH cap to split imbalance/width regimes. Only after those equality patterns are exhausted should the t=1 abstract states with no E1 route be split into exact E=2 support types. Keep exact S_P/Ccap_P, X_3, the graph-level audit boundary, and the four-exception gate's subordinate status live.`
<!-- CURRENT-STATUS:END -->

---

## 1. Mandatory audit gate

Before forward mathematics this run reread `CURRENT_STATE.md`, root `README.md`, the newest commits, the 19 September daily red-team audit, `project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/SOURCE_PREMISE_REPAIR.md`, and the independent graph-level regression handoff.

The binding audit remains `project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

Its requirements remain mandatory:

- distinct physical beta-source identity is established from raw singleton criticality;
- selected `(source,coordinate)` uniqueness is a one-selected-representative statement, not raw-witness uniqueness;
- the finite source-tuple capacity theorem is not promoted to unconditional graph-level closure;
- the independent actual-D2C regression remains the end-to-end premise check and retains `X_3` as mandatory hostile control;
- no bounded-corpus graph realizes the full rigid complete-cut hypotheses, so the active branch remains a conditional hand implication;
- exact pair-local `S_P/Ccap_P` remains mandatory; `(ONE-P)` and `(CROWD)` are consequences only where already proved from stronger physical bills;
- the four-exception gate remains subordinate.

There is no departure from the audit's priority order in this checkpoint.

---

## 2. Active geometry

Rigid one-code complete cut, positive-buffer unloaded common-buffer first equality, minimal outside reservoir `m=g+1`, noncheap first layer `E=1`:

- `X--Y` complete, `x>=3`, `y>0`, `a=x+y`;
- Y code `d`; X contains neither `d` nor `bar d`;
- `g=g_P`, `k=x-g>0`, `t=p-g>=1`;
- `X=H_M dotcup H_0`, sizes `g,k`;
- `H_M` codes are pairwise distinct singleton A-code classes;
- `H_0` has one common code, is independent, and uses one common outside witness;
- `A=g-d_{H_M}(z_*)`, `M=(u_o-1)-d_{U_o\{z_*}}(z_*)`, `N=u-k-2`;
- `D(A,M)=Q_H-(2k-1)A-kM`, `Delta=E_max(A)-e(X)`;
- exact pair-local `sigma_P/Ccap_P`, rooted q/E_U residual budget and local slot/Hamming theorem remain in force;
- `X_3` has canonical-root `u=0` and does not enter these hypotheses.

---

## 3. Correct support-channel incidence theorem

For `E=1`, every wrong-head selected-witness adjacency is incident with the unique radius-two defect class. Let `d0=g-A`.

### `k>1,d0=1`

The repeated core support is one defect coordinate and the common core witness is adjacent to the defect. Star separation already forbids all k defect--core head edges, so the core channel supplies at most k+1 incidences without further Delta; the other coordinate is at most one singleton bidirected channel:

`J<=k+1+min(2Delta,2)`.

### `k>1,d0=0`

If neither defect coordinate is the repeated core support, at most two singleton channels give `J<=min(2Delta,4)`. If one coordinate is the repeated core support, that channel is one-way and each defect-witness/core-head incidence costs its own missing defect--core head edge, while the other coordinate can be one singleton bidirected channel. Thus

`J<=F_k(Delta)`,

where `F_k(0)=0`, `F_k(1)=2`, `F_k(2)=4`, and `F_k(Delta)=min(k+2,Delta+1)` for `Delta>=3`.

### `k=1`

`J<=min(2d0+2Delta,4)`.

An intermediate attempt in this run to cap the whole `d0=0` branch by four incidences was too strong because the defect witness can meet multiple core heads when one defect coordinate equals the repeated core support. The mistake was caught adversarially and repaired before this handoff.

---

## 4. Local two-way hostile gadget

Both directed wrong-head adjacencies across one defect/radius-one singleton support pair can coexist with the existing singleton relations around the same matched d-endpoint, provided the corresponding defect--radius-one head edge is absent. This is a local incidence gadget, not a D2C graph construction.

Therefore one missing singleton head edge can genuinely support two selected-witness incidences. The factor two is locally sharp on singleton channels; further progress must use global structure rather than a false local incompatibility claim.

---

## 5. Refined pair gate

Selected-witness slack plus Hall slack gives

`S-S_P>=p(g+1)+k+M+Psi_{k,d0}(D)`.

For `k>1,d0=1`,

`Psi=max(D-(k+1),-(k+3))`.

For `k=1`,

`Psi=max(D-2d0,-4)`.

For `k>1,d0=0`,

`Psi=min_Delta {[D+2Delta]_+-F_k(Delta)}`,

and a minimum is attained among at most six candidates

`{0,1,2,k+1,clamp(floor(-D/2),3,k+1),clamp(ceil(-D/2),3,k+1)}`.

Every row must satisfy

`p(g+1)+k+M+Psi_{k,d0}(D(A,M))<=C0-sigma_P`.

For `d0=1,k>1`, writing `D=D0-kM`, `K0=p(g+1)+k`, `T=C0-sigma_P`, the exact M interval is

`ceil((K0+D0-(k+1)-T)/(k-1)) <= M <= T-K0+k+3`,

clipped to `0<=M<=N`. For `k=1`, the first affine condition is M-independent and the second gives the upper endpoint.

---

## 6. Rooted residual and saturated-support feedback

The rooted lower term remains

`G(M)=E_*+M+ceil([R0-(k+1)M]_+/2)`

with free optimizer `M_Q=ceil([R0]_+/(k+1))`. On the explicit M-interval cases the best compatible rooted lower bound is attained at `clamp(M_Q,M_-,M_+)`.

Pointwise every row must also satisfy

`G(M)<=binom(u,2)-binom(k+1,2)-k-M+C0-Y0-[D(A,M)]_+`.

The bounded replay finds zero failures of this pointwise rooted lower/upper test after the corrected support gate. This is diagnostic evidence only and suggests that another scalar q/E_U relaxation is not the immediate bottleneck.

A stronger structural feedback appears at support saturation. If `k>1,d0=1,J=k+3`, the k defect--core edges and the one defect--singleton edge on the second support coordinate are all absent; these are exactly all possible zero-Hamming-excess internal edges. Hence every actual X-edge has positive Hamming excess and

`r>=a+y+1+eta(e(X))`.

The same strengthened slot conclusion holds for `k>1,d0=0,Delta=2,J=4`: equality then uses two singleton bidirected channels, so both zero-excess defect--singleton edges are absent.

---

## 7. t=1 width cap

For `t=1`, `g=p-1`, put `tau_P=sigma_P-P0>=0` and let `parity(lambda)` be 0/1 for even/odd lambda.

Every E1 survivor satisfies

`(a+2)^2 <= u^2+2pu+2u+6p-2k^2+4k-3-parity(lambda)-2(M+tau_P)`.

Thus the one-defect t=1 branch is forced into an explicit imbalance / narrow-A regime before the finer D-dependent gate is used.

---

## 8. Diagnostic status

Corrected support-envelope replay on the predecessor abstract box:

- E1-feasible states: `53,435 -> 48,677`;
- E1 state-route closures: `4,758`;
- E1 rows: `1,212,749 -> 1,094,326`;
- t=1 E1-feasible states: `5,164 -> 4,471`;
- t=1 E1 route closures: `693`;
- t=1 E1 rows: `128,750 -> 111,204`;
- full union: unchanged at `64,457`;
- t=1 union: unchanged at `5,404`;
- rooted q/E_U pointwise failures among new E1 rows: `0`.

These are abstract arithmetic parameter states, not realizable graph counts.

---

## 9. Preserved package and next work

Primary package:

`project/research/post_ms/2026-09-19-one-defect-support-cap-v1/`

Files:

- `ONE_DEFECT_SUPPORT_CAP_RESIDUAL_PINCH.md`
- `check_one_defect_support_cap.py`

Next: classify equality / near-equality in the corrected support-channel envelopes, especially the `d0=1` `k+3` saturation pattern and the `d0=0` repeated-core/singleton transition; feed the resulting specific head nonedges into the local slot/Hamming ledger and exact pair-density lower bound; use the width cap and exact M interval to split surviving t=1 E1 geometry. Do not open `m=g+2`, loaded buffer, z=2, or the four-exception gate while this line remains live. Exact E=2 support classification begins only after these E1 equality geometries have been exhausted.
