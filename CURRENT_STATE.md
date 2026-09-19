# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-19  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is **not** the target. The published 2024 D2C graph `X_3` on 12 vertices and 32 edges has `M(12)=31` and remains a mandatory negative control. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not an optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_MINIMAL_RESERVOIR_E2_EXACT_SUPPORT_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `b5be3a06e7d197cdf9931883a714ca9d4e25c599`

LAST VERIFIED RESULT: `The exact E=2,k>=3 minimal-reservoir support geometry is now classified at the channel-resource level. For a defect topology with total support incidences s, defect-defect intersection count q, c defect supports containing the repeated-core coordinate, d0 active common-core-witness/defect adjacencies, B=s-c+q and K=k(c-d0), the wrong-head incidence count obeys J<=d0(k+1)+2min(Delta,B)+min(K,[Delta-B]_+). The resulting pair correction has the closed form Phi_{B,0}(D)=max(D,-2B); for K>0, Phi=max(D,-2B) when D>=-2B-1 and Phi=max(ceil(D/2)-B,-(2B+K)) when D<=-2B-2. Thus p(g+1)+k+M-d0(k+1)+Phi<=C0-sigma_P is the exact topology-retaining pair gate. In R3 every X-code has radius 1 or 3, so every actual X-edge has positive Hamming excess and r>=a+y+1+eta(e(X)); the active-core R3 right arm at t=1 has pair bill p^2+M-5<=C0-sigma_P. In R2+R2 the only zero-Hamming X-edges are defect-to-radius-one head edges on defect support coordinates, giving r>=a+y+2+eta_2(j_+). On the fully saturated constant pair arm all such zero-Hamming edges are forced absent, hence r>=a+y+2+eta_2(e(X)). The deepest pair-cheap R2+R2 topology is uniquely h=1,c=2,d0=2 for every k>=3: the two radius-two defects share the repeated-core coordinate and the common core witness is adjacent to both. There B=3,K=0,Jmax=2k+8; at t=1 the deep pair bill is p^2+M-k-8<=C0-sigma_P, while star separation plus support saturation makes every surviving X-edge positive-Hamming. This creates the next explicit pair-cheap/rooted-expensive pinch family.`

UNPRESERVED WORK: `None. The theorem note and independent arithmetic/topology checker are preserved under project/research/post_ms/2026-09-19-e2-exact-support-v1/. No new D2C graph-realizability claim or finite survivor count is promoted.`

DEFERRED ADMIN: `README remains synchronized to the 19 September audit trust boundary and is intentionally lower-frequency. Refresh reviewer-facing status at the next daily adversarial checkpoint unless repository integrity requires earlier repair.`

NEXT ACTION: `Stay on m=g+1,t=1,k>=3. Attack the unique deepest pair-cheap R2+R2 equality family h=1,c=2,d0=2 before opening any broader branch. Intersect p^2+M-k-8<=C0-sigma_P and the exact deep-saturation slot floor r>=a+y+2+eta_2([Emax-floor(-D/2)]_+) with the exact rooted identity r=(p-lambda)(p+u)+q+E_U and the preserved physical q/E_U allocation, retaining M and pair-local S_P rather than collapsing to total score. Classify exact/one-unit pair slack first. If that family survives, treat the non-deep shared-core arm, then R3 near-equality. Do not open k=2, k=1, m=g+2, loaded buffer, z=2, or the four-exception gate while this equality family remains live. Keep X_3 and the graph-level audit boundary explicit.`
<!-- CURRENT-STATUS:END -->

---

## 1. Mandatory audit gate

Before forward mathematics this run reread:

- `CURRENT_STATE.md`;
- root `README.md`;
- latest commits through `b5be3a06e7d197cdf9931883a714ca9d4e25c599`;
- `project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`;
- `project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/SOURCE_PREMISE_REPAIR.md`;
- `project/research/post_ms/2026-09-19-rigid-graph-regression-v1/RIGID_GRAPH_LEVEL_REGRESSION.md`.

The audit requirements remain binding:

- distinct physical beta-source identity is established from raw singleton criticality;
- selected `(source,coordinate)` uniqueness is a one-selected-representative statement, not raw witness uniqueness;
- the finite source-tuple theorem is not promoted to unconditional graph-level closure;
- the independent actual-D2C regression remains the end-to-end premise check and retains `X_3` as the mandatory hostile control;
- the regression recorded 3,540 root-policy instances, 147 exact pair-capacity checks, 36 Hall-cut decompositions and zero graph/formula mismatches;
- no bounded-corpus D2C graph realizes the full rigid complete-cut hypotheses, so the active branch remains a conditional hand implication;
- exact pair-local `S_P/Ccap_P` remains mandatory;
- the four-exception gate remains subordinate.

There is no departure from the audit's priority order in this checkpoint.

---

## 2. Why E=2 is now the live frontier

The predecessor exhausted the useful E=1 equality/near-equality scalar line in the difficult `t=1` slice. Exactly 933 bounded `t=1` union survivors had no E1 route, and all 933 already possessed an `E=2` route under the retained distribution-sensitive relaxation. For `k>=3`, exact total excess two has only two code-block types:

1. `R3`: one radius-three singleton matched head;
2. `R2+R2`: two radius-two singleton matched heads.

The repeated core cannot carry excess when `k>=3`.

---

## 3. Unified E=2 support ledger

For either E=2 type define:

- `s`: total defect-support incidences (`3` for R3, `4` for R2+R2);
- `q`: intersecting defect-pair count (`0` for R3, `h in {0,1}` for R2+R2);
- `c`: number of defect supports containing the repeated-core coordinate;
- `d0`: number of those defects adjacent to the common core witness;
- `B=s-c+q`;
- `K=k(c-d0)`.

Then

`J <= d0(k+1)+2min(Delta,B)+min(K,[Delta-B]_+)`.

The first term is the already-priced active repeated-core channel; `B` counts bidirected singleton-type channels; `K` is the remaining one-way repeated-core capacity.

With `D=D(A,M)`, exact Hall accounting gives the pair correction

`Phi_{B,0}(D)=max(D,-2B)`,

and for `K>0`,

`Phi=max(D,-2B)` when `D>=-2B-1`,

`Phi=max(ceil(D/2)-B,-(2B+K))` when `D<=-2B-2`.

Hence

`p(g+1)+k+M-d0(k+1)+Phi_{B,K}(D)<=C0-sigma_P`.

This is the topology-retaining exact E2 pair gate now in force.

---

## 4. R3 branch

R3 codes have radius one or three from `d`. Distinct X-code classes therefore have even Hamming distance at least two; `H_0` is independent. Consequently every X-edge has positive Hamming excess and

`r>=a+y+1+eta(e(X))`.

For the active-core topology `c=d0=1`, `B=2,K=0`, so

`Psi=max(D-(k+1),-(k+5))`.

On the right arm `D<=-4`, at `t=1`,

`p^2+M-5<=C0-sigma_P`.

With pair slack `s_P`,

`Delta<=floor((s_P-D)/2)`,

hence

`r>=a+y+1+eta([Emax-floor((s_P-D)/2)]_+)`.

---

## 5. R2+R2 branch

The two radius-two supports are distinct, so their overlap `h` is 0 or 1.

The only possible zero-Hamming X-edges are defect-to-radius-one head edges on a defect support coordinate. Every defect-defect edge and every radius-one/radius-one edge has positive Hamming excess.

If `j_+` is the number of positive-Hamming internal X-edges and `eta_2(j)` is the least `q>=0` with `binom(q+2,2)>=j`, then

`r>=a+y+2+eta_2(j_+)`.

On the fully saturated constant pair arm, every support channel is saturated, so every possible zero-Hamming defect/radius-one edge is absent. Thus

`r>=a+y+2+eta_2(e(X))`,

and exact pair equality gives

`r>=a+y+2+eta_2([Emax-floor(-D/2)]_+)`.

---

## 6. Dominant shared-core equality geometry

For R2+R2,

`Jmax=8+2h+c(k-2)+d0`.

For every `k>=3` this is uniquely maximized by

`h=1,c=2,d0=2`.

So the two radius-two defects share exactly the repeated-core coordinate and the common core witness is adjacent to both defect heads. Then

`B=3`, `K=0`, `Jmax=2k+8`.

At `t=1`, the fully saturated exact pair bill is

`p^2+M-k-8<=C0-sigma_P`.

At the same time:

- all `2k` defect-core zero-Hamming edges are absent by star separation;
- the two private defect-singleton zero-Hamming edges are absent at support saturation;
- the defect-defect edge is also absent if its bidirected channel is saturated;
- every surviving X-edge is positive-Hamming;
- `A=g-2` and `Emax=binom(g,2)+k(g-2)`.

This is the present load-bearing equality family.

---

## 7. Preserved package

`project/research/post_ms/2026-09-19-e2-exact-support-v1/`

Files:

- `EXACT_E2_SUPPORT_CHANNELS.md`
- `check_e2_support_channels.py`

The checker is an arithmetic/topology audit only, not a D2C graph enumerator.

---

## 8. Next work

Remain in `m=g+1,t=1,k>=3`.

1. Work first on `R2+R2`, `h=1,c=2,d0=2`.
2. Combine the exact pair bill with the exact rooted identity and physical `q/E_U` allocation while retaining `M`.
3. Classify exact and one-unit pair slack; convert the forced `Delta` range into an explicit rooted-slot surcharge.
4. If the deep shared-core family survives, treat its non-deep V-arm before moving to R3 near equality.
5. Only after those are exhausted should `k=2` or `k=1` E2 placements be opened.

Do not open `m=g+2`, loaded buffer, `z=2`, or the four-exception gate while this line remains live.
