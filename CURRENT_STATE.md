# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-19  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is **not** the target. The published 2024 D2C graph `X_3` on 12 vertices and 32 edges has `M(12)=31` and remains a mandatory negative control. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not an optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_MINIMAL_RESERVOIR_E1_SUPPORT_CAP_RESIDUAL_PINCH_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `46240212375c7b2de7c254990b9b7ad301e367be`

LAST VERIFIED RESULT: `In the m=g+1 one-defect E=1 branch, support intersection limits all selected-witness wrong-head incidences to two defect-support channels. With d0=g-A, c0=(k+1)d0 and J0=4+(k-1)d0 for k>1 (while c0=2d0,J0=4 for k=1), the exact safe incidence envelope is J<=min(c0+2Delta,J0). The two directed adjacencies on one defect/radius-one support pair are locally compatible with the existing singleton certificates, so the coefficient 2 cannot be removed from singleton criticality alone. Eliminating Delta exactly gives S-S_P>=p(g+1)+k+M+max(D-c0,-J0), hence an explicit V-shaped E1 pair gate and an integer M-admissible interval. Intersecting that interval with the rooted residual G(M)=E_*+M+ceil([R0-(k+1)M]_+/2) again gives a clamped optimizer. In t=1, every E1 survivor also obeys the exact width cap (a+2)^2<=u^2+2pu+2u+6p-2k^2+4k-3-parity(lambda)-2(M+tau_P), tau_P=sigma_P-P0. Independent bounded arithmetic replay closes the E1 route in 4,761 abstract states (693 at t=1), reducing E1-feasible states 53,435->48,674 and t=1 E1-feasible states 5,164->4,471; the full union remains 64,457 and t=1 remains 5,404 because alternate E>=2 or cheap-sphere routes survive. Pointwise rooted q/E_U lower/upper intersection adds zero further exclusions on all 1,093,262 newly E1-feasible rows.`

UNPRESERVED WORK: `None. The theorem and checker are preserved under project/research/post_ms/2026-09-19-one-defect-support-cap-v1/.`

DEFERRED ADMIN: `README remains lower-frequency. Refresh reviewer-facing status at the next daily adversarial checkpoint unless repository integrity requires an earlier repair.`

NEXT ACTION: `Stay on m=g+1 and t=1. Classify equality/near-equality in the new support-cap gate before opening E=2: for d0=0 analyze the four-incidence pattern requiring two singleton radius-one support channels; for d0=1 analyze the k+3 pattern, where the core-support channel and one singleton channel saturate. Feed the forced defect--radius-one head nonedges from those equality patterns directly into the local rooted-slot/Hamming ledger rather than only through Delta. Use the exact M interval and WIDTH cap to split imbalance/width regimes. Only after those equality patterns are exhausted should the 933 t=1 abstract states with no E1 route be split into exact E=2 support types. Keep exact S_P/Ccap_P, X_3, the graph-level audit boundary, and the four-exception gate's subordinate status live.`
<!-- CURRENT-STATUS:END -->

---

## 1. Mandatory audit gate

Before forward mathematics this run reread `CURRENT_STATE.md`, root `README.md`, the newest commits, the 19 September daily red-team audit, `project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/SOURCE_PREMISE_REPAIR.md`, and the independent graph-level regression handoff.

The binding audit remains:

`project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

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

Rigid one-code complete cut, positive-buffer unloaded common-buffer first equality, minimal outside reservoir `m=g+1`, and noncheap first layer `E=1`:

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

## 3. New support-channel theorem

For `E=1`, every wrong-head selected-witness adjacency is incident with the unique radius-two defect class and must use one of its two support coordinates.

Put `d0=g-A`. For `k>1`, `d0 in {0,1}` and

`c0=(k+1)d0`, `J0=4+(k-1)d0`.

For `k=1`, `0<=d0<=2` and

`c0=2d0`, `J0=4`.

If J is total selected-witness A-neighbour incidence, then

`J<=min(c0+2Delta,J0)`.

The `2Delta` coefficient is locally sharp under the current singleton relations: both directed wrong-head adjacencies across one defect/radius-one support pair can coexist around the same matched coordinate once the corresponding head-head edge is absent. This is a local hostile incidence gadget only, not a realizable-D2C claim.

---

## 4. Exact support-capped pair gate

Selected-witness slack and Hall slack give

`S-S_P >= p(g+1)+k+M+[D+2Delta]_+-J`.

Exact integer minimization over `Delta>=0` yields

`min{[D+2Delta]_+-min(c0+2Delta,J0)}=max(D-c0,-J0)`.

Hence

> `S-S_P>=p(g+1)+k+M+max(D-c0,-J0)`.

With `S_P>=sigma_P`, every E1 survivor satisfies

> `p(g+1)+k+M+max(D-c0,-J0)<=C0-sigma_P`.

For fixed `d0`, write `D=D0-kM`, `K0=p(g+1)+k`, `T=C0-sigma_P`. The gate is

`max(K0+D0-c0-(k-1)M, K0-J0+M)<=T`.

For `k>1` this is the explicit interval

`ceil((K0+D0-c0-T)/(k-1)) <= M <= T-K0+J0`,

clipped to `0<=M<=N`. For `k=1`, the first affine term is M-independent and the second supplies the upper endpoint.

Thus the old monotone M-escape is gone: once the two support channels saturate, additional M raises the outside-pair bill one-for-one.

---

## 5. Rooted residual intersection

The rooted lower term remains

`G(M)=E_*+M+ceil([R0-(k+1)M]_+/2)`

with free optimizer

`M_Q=ceil([R0]_+/(k+1))`.

Because the refined E1 pair-admissible set is an interval, the exact best rooted lower bound compatible with the pair geometry is attained at

`M_hat=clamp(M_Q,M_-,M_+)`.

Pointwise, any row must also satisfy

`G(M)<=binom(u,2)-binom(k+1,2)-k-M + C0-Y0-[D(A,M)]_+`.

On the bounded predecessor box this pointwise rooted lower/upper intersection adds zero extra exclusions after the support-capped pair gate. This is diagnostic evidence only. It says that another scalar q/E_U relaxation is unlikely to be the next productive move on the tested regime.

---

## 6. t=1 width cap

For `t=1`, `g=p-1`. Put `tau_P=sigma_P-P0>=0`, and let `parity(lambda)` be 0/1 according as lambda is even/odd.

Since the support-capped outside bill is always at least `p^2+M-3`, exact score algebra gives

> `(a+2)^2 <= u^2+2pu+2u+6p-2k^2+4k-3-parity(lambda)-2(M+tau_P)`.

This forces every E1 t=1 survivor into an explicit imbalance / narrow-A regime. Exact pair capacity only strengthens the bound through `tau_P`.

---

## 7. Diagnostic status

The new checker starts from the predecessor bounded abstract box and changes only the E1 pair theorem.

- E1-feasible states: `53,435 -> 48,674`;
- E1 state-route closures: `4,761`;
- E1 rows: `1,212,749 -> 1,093,262`;
- t=1 E1-feasible states: `5,164 -> 4,471`;
- t=1 E1 route closures: `693`;
- t=1 E1 rows: `128,750 -> 111,046`;
- full union: unchanged at `64,457`;
- t=1 union: unchanged at `5,404`;
- rooted q/E_U pointwise failures among the new E1 rows: `0`.

These are abstract arithmetic parameter states, not realizable graph counts.

---

## 8. Preserved package and next work

Primary package:

`project/research/post_ms/2026-09-19-one-defect-support-cap-v1/`

Files:

- `ONE_DEFECT_SUPPORT_CAP_RESIDUAL_PINCH.md`
- `check_one_defect_support_cap.py`

Next: classify equality in the support-channel cap, feed its forced head nonedges directly into the local slot/Hamming ledger, and use the width cap / M interval to split the surviving t=1 E1 geometry. Do not open `m=g+2`, loaded buffer, z=2, or the four-exception gate while this line remains live. Exact E=2 support classification should begin only after the E1 equality geometries have been exhausted.
