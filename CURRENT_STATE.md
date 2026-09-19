# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-19  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is **not** the target. The published 2024 D2C graph `X_3` on 12 vertices and 32 edges has `M(12)=31` and remains a mandatory negative control. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not an optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_MINIMAL_RESERVOIR_E1_PAIR_EQUALITY_SLOT_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `71e2b3ee8f912c7bb5b882c5d13201c5a51fb716`

LAST VERIFIED RESULT: `The m=g+1 E=1 equality/near-equality geometry is now sharper. For d0=g-A=1, star separation already deletes all k defect-core zero-Hamming-excess edges, so at most one zero-excess X-edge remains and universally r>=a+y+1+eta([e(X)-1]_+). On the D<=-2 right arm, pair slack s<=1 forces the second singleton support channel active, hence all X-edges have positive Hamming excess and Delta<=floor((s-D)/2); at t=1 the right-arm pair bill is exactly p^2+M-3<=C0-sigma_P, so M=M_+ and M_+-1 are literal support-saturation/near-saturation rows. Exact d0=1 equality gives j_+>=[Emax-max(1,floor(-D/2))]_+. For d0=0,k>1 the previously finite-candidate correction closes to Psi=max(D,-4) for D>=-7 and Psi=max(ceil(D/2)-1,-(k+2)) for D<=-8. Exact equality has a two-singleton zone D=-3,-4,-5 with j_+=Emax-2 and a deep repeated-core zone, uniformly j_+>=[Emax-max(k+1,floor(-D/2))]_+. These j_+ floors feed directly into r>=a+y+1+eta(j_+). Bounded replay removes 261 E1 rows and 5 E1-route states (48,677->48,672), but no t=1 state: t=1 E1 rows 111,204->111,197 and E1 states remain 4,471; full union remains 64,457 and t=1 union 5,404. Exactly 933 t=1 union survivors have no E1 route, and all 933 already have an E=2 route under the retained R_N relaxation. The exact E=2 block types are now classified: for k>=3 only one R3 matched-head defect or two R2 matched-head defects; k=2 additionally allows a common-core R2; k=1 has matched R3, matched R2+R2, mixed core/matched R2, or core R3.`

UNPRESERVED WORK: `None. The theorem note and independent arithmetic replay are preserved under project/research/post_ms/2026-09-19-one-defect-pair-equality-slot-v1/. The earlier over-strong d0=0 J<=4 intermediate remains visibly superseded in history by 71e2b3ee...; this checkpoint uses only the repaired repeated-core-aware envelope.`

DEFERRED ADMIN: `README remains lower-frequency and is already synchronized to the 19 September audit trust boundary. Refresh reviewer-facing status at the next daily adversarial checkpoint unless repository integrity requires an earlier repair.`

NEXT ACTION: `Stay on m=g+1,t=1 and move from exhausted E1 equality geometry to exact E=2 support classification, because all 933 bounded t=1 no-E1 survivors already have an E=2 route. For k>=3 first split R3 (one radius-three matched-head defect) from R2+R2 (two radius-two matched-head defects). Derive support-channel incidence envelopes before any scalar minimization: in R3 separate the three defect support coordinates into repeated-core versus singleton bidirected channels; in R2+R2 classify support overlap/disjointness and shared singleton channels. Then intersect each exact support type with pair-local S_P/Ccap_P and the rooted slot/Hamming ledger. Only afterward handle the k=2 Core-R2 type and the k=1 special placements. Do not open m=g+2, loaded buffer, z=2, or the four-exception gate while this E=2 frontier remains live. Keep X_3 and the graph-level audit boundary explicit.` 
<!-- CURRENT-STATUS:END -->

---

## 1. Mandatory audit gate

Before forward mathematics this run reread:

- `CURRENT_STATE.md`;
- root `README.md`;
- latest commits through `71e2b3ee8f912c7bb5b882c5d13201c5a51fb716`;
- `project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`;
- `project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/SOURCE_PREMISE_REPAIR.md`;
- `project/research/post_ms/2026-09-19-rigid-graph-regression-v1/RIGID_GRAPH_LEVEL_REGRESSION.md`.

The audit requirements remain binding:

- distinct physical beta-source identity is established from raw singleton criticality;
- selected `(source,coordinate)` uniqueness is a one-selected-representative statement, not raw witness uniqueness;
- the finite source-tuple theorem is not promoted to unconditional graph-level closure;
- the independent actual-D2C regression remains the end-to-end premise check and retains `X_3` as the mandatory hostile control;
- that regression recorded 3,540 root-policy instances, 147 exact pair-capacity checks, 36 Hall-cut decompositions and zero graph/formula mismatches;
- no bounded-corpus D2C graph realizes the full rigid complete-cut hypotheses, so the active branch remains a conditional hand implication;
- exact pair-local `S_P/Ccap_P` remains mandatory;
- the four-exception gate remains subordinate.

There is no departure from the audit's priority order in this checkpoint.

---

## 2. Active geometry

Rigid one-code complete cut, positive-buffer unloaded common-buffer first equality, minimal outside reservoir `m=g+1`.

For the completed first noncheap layer `E=1`:

- `X--Y` complete, `x>=3`, `y>0`, `a=x+y`;
- Y code `d`; X contains neither `d` nor `bar d`;
- `g=g_P`, `k=x-g>0`, `t=p-g>=1`;
- `X=H_M dotcup H_0`, sizes `g,k`;
- `H_M` codes are singleton classes;
- `H_0` has one common radius-one code and one common outside witness;
- there is one unique radius-two defect head;
- `A=g-d_{H_M}(z_*)`, `d0=g-A`;
- `M=(u_o-1)-d_{U_o\{z_*}}(z_*)`, `N=u-k-2`;
- `D(A,M)=Q_H-(2k-1)A-kM`;
- `Delta=E_max(A)-e(X)`;
- exact pair-local `sigma_P/Ccap_P`, rooted q/E_U residual budget and local slot/Hamming theorem remain in force.

The corrected support theorem from the predecessor is retained exactly:

- `k>1,d0=1`: `J<=k+1+min(2Delta,2)`;
- `k>1,d0=0`: `J<=F_k(Delta)`, with `F_k(0,1,2)=0,2,4` and `F_k(Delta)=min(k+2,Delta+1)` for `Delta>=3`;
- `k=1`: `J<=min(2d0+2Delta,4)`.

The local two-way singleton-channel hostile gadget remains a live negative control: the factor two cannot be removed from local criticality alone.

---

## 3. New d0=1 zero-edge theorem

In `E=1,d0=1`, the repeated core support is one coordinate of the radius-two defect. The common core witness is adjacent to the defect, so star separation already forbids all k defect--core head edges.

The only other possible zero-Hamming-excess internal X-edge is the defect edge to a singleton radius-one class on the second defect coordinate. Hence:

`# zero-rho X-edges <=1`.

Therefore

`r>=a+y+1+eta([e(X)-1]_+)`.

If `J>=k+2`, the second singleton support channel is active and its head edge is also forced absent. Then every actual X-edge has positive Hamming excess and

`r>=a+y+1+eta(e(X))`.

This improvement is unconditional within the `d0=1,E=1` branch; it does not require exact pair saturation.

---

## 4. d0=1 exact / near pair pinch

For `D<=-2`, the exact pair correction is `-(k+3)`. If `s` is slack above the pair minimum, then

`[D+2Delta]_+ + (k+3-J) <= s`.

Thus for `s<=1`:

- `J>=k+2`;
- all actual X-edges have positive Hamming excess;
- `Delta<=floor((s-D)/2)`.

At exact equality:

`j_+ >= [Emax-max(1,floor(-D/2))]_+`,

where

`Emax=binom(g,2)+k(g-1)`.

Hence

`r>=a+y+1+eta([Emax-max(1,floor(-D/2))]_+)`.

For `D<=-2` with one pair-slack unit:

`j_+ >= [Emax-floor((1-D)/2)]_+`.

In the `t=1` slice, `g=p-1`, and the right-arm pair bill simplifies exactly to

`p^2+M-3<=T`, `T=C0-sigma_P`.

So

`M_+=T-p^2+3`;

`M=M_+` is support-saturated and `M=M_+-1` is already in the all-positive-edge regime.

---

## 5. Closed d0=0 pair correction

For every `k>1`,

`Psi_{k,0}(D)=min_Delta {[D+2Delta]_+-F_k(Delta)}`

has the exact closed form

`Psi_{k,0}(D)=max(D,-4)` for `D>=-7`,

and

`Psi_{k,0}(D)=max(ceil(D/2)-1,-(k+2))` for `D<=-8`.

This supersedes only the *presentation* of the earlier safe finite-candidate minimization; it agrees with that repaired theorem.

Exact equality regimes:

- `D>=0`: `Delta=0,1,2`;
- `D=-1,-2`: `Delta=1,2`;
- `D=-3,-4,-5`: uniquely `Delta=2,J=4`, necessarily two singleton bidirected channels;
- `D=-6,-7`: transition/tie;
- `D<=-8,k>=3`: repeated-core support is necessary.

Let

`Emax=binom(g,2)+kg`.

At exact equality,

`j_+ >= [Emax-max(k+1,floor(-D/2))]_+`.

In the sharper zone `-5<=D<=-3`,

`j_+=Emax-2`.

Thus

`r>=a+y+1+eta(j_+)`.

When `D<=-2k-2`, the repeated-core support envelope is saturated and, at `t=1`, the deep pair bill becomes

`p^2+M-2<=T`.

---

## 6. Diagnostic status

The companion checker preserves the predecessor's abstract scan and changes only the newly proved rooted-slot floors.

Results:

- support-capped E1 rows: `1,094,326 -> 1,094,065`;
- row eliminations: `261`;
  - d0=1 universal one-zero-edge: 199;
  - d0=1 exact equality: 28;
  - d0=1 one-unit right pinch: 1;
  - d0=0 exact equality: 33;
- E1-feasible states: `48,677 -> 48,672`;
- E1-route closures: `5`;
  - t=4: 2;
  - t=8: 1;
  - t=9: 1;
  - t=11: 1;
- t=1 E1 rows: `111,204 -> 111,197`;
- t=1 E1 states: unchanged at `4,471`;
- full union: unchanged at `64,457`;
- t=1 union: unchanged at `5,404`.

These are abstract arithmetic parameter states, not realizable graph counts.

The t=1 nonmovement is itself useful: the E1 equality line is now structurally sharper, but it is no longer the right place to spend another scalar relaxation.

---

## 7. Exact E=2 frontier

Among the bounded t=1 union survivors, exactly 933 have no E1 route. Every one of those 933 has an E=2 route under the retained distribution-sensitive `R_N` relaxation.

k-distribution:

`k=1:223, 2:201, 3:146, 4:104, 5:82, 6:60, 7:53, 8:47, 9:17`.

The exact E=2 block types are:

### k>=3

Only:

1. R3 — one singleton H_M head has excess 2 / radius 3;
2. R2+R2 — two singleton H_M heads each have excess 1 / radius 2.

The repeated core cannot carry excess because one unit would contribute at least k>2 total excess.

### k=2

Add:

3. Core-R2 — common H_0 code has excess 1, contributing both units.

### k=1

Four placements:

1. matched R3;
2. matched R2+R2;
3. mixed core R2 + matched R2;
4. core R3.

This is the next live classification problem.

---

## 8. Preserved package

Primary package:

`project/research/post_ms/2026-09-19-one-defect-pair-equality-slot-v1/`

Files:

- `ONE_DEFECT_PAIR_EQUALITY_SLOT_FEEDBACK.md`
- `check_one_defect_pair_equality_slot.py`

The checker is explicitly an abstract arithmetic diagnostic, not a D2C graph enumerator.

---

## 9. Next work

Remain in `m=g+1,t=1`.

First attack `E=2,k>=3`:

1. R3: one radius-three matched-head defect. There are three defect support coordinates; derive the exact selected-witness incidence envelope by separating a possible repeated-core one-way channel from singleton bidirected channels. Only then minimize against exact pair-local `Ccap_P`.
2. R2+R2: classify whether the two radius-two supports are disjoint, meet in one coordinate, or coincide in forbidden/allowed ways under distinct singleton A-codes; determine how many singleton channels can be shared before pricing missing head edges.
3. Feed each surviving support geometry into the local rooted-slot/Hamming ledger and exact q/E_U residual allocation.
4. Then handle k=2 Core-R2.
5. Handle k=1 special placements last.

Do not open `m=g+2`, loaded buffer, `z=2`, or the four-exception gate while this exact E=2 line remains live.

Keep `X_3`, the actual-graph regression trust boundary, and exact pair-local `S_P/Ccap_P` explicit throughout.
