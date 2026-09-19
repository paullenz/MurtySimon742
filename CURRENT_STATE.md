# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-19  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is **not** the target. The published 2024 D2C graph `X_3` on 12 vertices and 32 edges has `M(12)=31` and remains a mandatory negative control. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not an optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_MINIMAL_RESERVOIR_SLOT_SPHERE_PINCH_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `267d321eb5028c81d9c4492b4c71945b4bdd4de2`

LAST VERIFIED RESULT: `The positive-buffer unloaded common-buffer minimal-reservoir layer m=g+1 now has a rooted-slot / pair-local / Boolean-sphere pinch. Exact r=f+delta=(p-lambda)(p+u)+q+E_U and the rigid-cut local theorem r>=a give q+E_U>=a-(p-lambda)(p+u), plus the parity-explicit imbalance cap lambda^2<=2p^2+2pu+2p+u^2+u-6 (lambda even) or -7 (lambda odd). In m=g+1 the physical U-hole count q<=C(u,2)-C(k+1,2)-k-M and E_U<=C0-Y0-[D(A,M)]_+ give an allocation-sensitive slot gate. Exact pair score also forces X-density: 2(Emax-e(X))<=s+[-D]_+, where s=B_P-H(A,M). The Hamming geometry splits sharply: any extra X-to-d Hamming unit forces r>=a+y; if every X-code is distance one from d, then the X codes are distinct one-bit flips, every internal X-edge has Hamming length two, and r>=a+nu_X. Raw criticality further forces the cheap sphere endpoint A=g, and in fact all g+1 selected outside witnesses are anticomplete to the whole A-layer, giving outside-pair slack at least p(g+1)+k+M and the exact local gate p(g+1)+k+M+[D(g,M)]_+<=C0-sigma_P. On the predecessor bounded abstract box, the first slot gate rejects 45,401 of 110,387 m=g+1 states; the full noncheap/sphere dichotomy rejects 45,830, leaving 64,557. In t=1 all 5,404 states retain a noncheap relaxation, although 1,024 lose the cheap sphere branch. These are parameter diagnostics, not graph counts.`

UNPRESERVED WORK: `None. The new theorem package and checker are preserved under project/research/post_ms/2026-09-19-minimal-reservoir-slot-sphere-v1/.`

DEFERRED ADMIN: `README remains lower-frequency. Refresh reviewer-facing status at the next daily adversarial checkpoint unless repository integrity requires an earlier repair.`

NEXT ACTION: `Stay on m=g+1. The coarse slot-capacity gate has exposed the non-Hamming-cheapest branch as the current bottleneck, especially t=1. Do not open m=g+2 yet. Attack the exact distribution of the extra Hamming units rather than merely using r>=a+y: combine vertexwise r_z lower bounds with the pair-budget X-density theorem and exact Ccap_P, looking first for a forced concentration/dispersion dichotomy among H_M code distances. In the surviving cheap-sphere branch exploit the stronger physical fact that all g+1 selected outside witnesses are anticomplete to A, not merely their aggregate slack. Keep X_3, exact pair-local S_P/Ccap_P and the graph-level audit boundary live.`
<!-- CURRENT-STATUS:END -->

---

## 1. Mandatory audit gate

Before this run, `CURRENT_STATE.md`, root `README.md`, the latest commits, the 19 September daily red-team audit, `SOURCE_PREMISE_REPAIR.md`, and `project/research/post_ms/2026-09-19-rigid-graph-regression-v1/RIGID_GRAPH_LEVEL_REGRESSION.md` were reread.

The binding audit remains

`project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

Its requirements remain mandatory:

- distinct physical beta-source identity is established from raw singleton criticality;
- selected `(source,coordinate)` uniqueness is a one-selected-representative statement, not raw-witness uniqueness;
- the finite source-tuple capacity theorem is not promoted to unconditional graph-level closure;
- the independent actual-D2C regression remains at 3,540 root-policy instances, 147 exact pair-capacity checks, 36 Hall decompositions and zero recorded graph/formula mismatches;
- `X_3` passes and remains mandatory;
- no bounded-corpus graph realizes the full rigid complete-cut hypotheses, so the active branch remains a conditional hand implication;
- exact `Ccap_P`, `(ONE-P)` and `(CROWD)` remain mandatory. In the current equality geometry the latter two are proved consequences of stronger physical bills once exact crossing `Ccap_P` is retained;
- the four-exception gate remains subordinate.

There is no departure from the audit's priority order in this checkpoint.

---

## 2. Active geometry retained

Rigid one-code complete cut, positive-buffer unloaded common-buffer first equality, minimal outside reservoir:

- `X--Y` complete, `x>=3`, `y>0`, `a=x+y`;
- Y code `d`; X contains neither `d` nor `bar d`;
- `g=g_P`, `k=x-g>0`, `t=p-g>=1`;
- `U_-=W_0 dotcup {b}`, `|W_0|=k`, `epsilon_b=t`;
- `X=H_M dotcup H_0`, sizes `g,k`;
- H_M codes are pairwise distinct singleton A-code classes;
- `m=g+1` outside witnesses; H_0 has one code `c_*`, is independent, and uses common witness `z_*` of code `bar c_*`;
- `A:=g-d_{H_M}(z_*)`, `M:=(u_o-1)-d_{U_o\{z_*}}(z_*)`;
- `N=u-k-2`, `0<=A<=g`, `0<=M<=N`;
- `epsilon_{z_*}=t+k+A+M`;
- `u>=x+2`, `L_Y>=Y_0:=y(p+2)`.

`X_3` has canonical-root `u=0` and does not enter these hypotheses.

---

## 3. Exact pair/Hall spine retained

Write

`Q_H=x(x-T_0)+k(x-1)+x-g(g-1)+kN`, `T_0=a-p`,

`D(A,M)=Q_H-(2k-1)A-kM`,

`H(A,M)=A+M+[D(A,M)]_+`.

Then

> `L_X>=[D(A,M)]_+`.

For the distinguished outside pair `P={d,bar d}`, let

`O_0=t+k+g[t-k+1]_+`

and let `sigma_P` be the least pair-local score meeting the exact crossing requirement

`2xy<=R_code(S_P)[g+2S_P/(lambda+1)]`.

Then

> `H(A,M)<=B_P:=C0-O_0-sigma_P`.

The pair/Hall-feasible M-values remain one interval and the predecessor clamped residual optimizer remains valid. The present checkpoint adds slot/Hamming information rather than replacing it.

---

## 4. Exact rooted-slot bridge

The preserved residual identities give

> `r=(p-lambda)(p+u)+q+E_U`.

The rigid complete cut gives `r>=a`, hence

> `q+E_U>=a-(p-lambda)(p+u)`.

Using `q<=binom(u,2)` and above-threshold `E_U<=C0` yields the universal rigid-cut imbalance condition

> `lambda^2<=2p^2+2pu+2p+u^2+u-6` for even lambda,
>
> `lambda^2<=2p^2+2pu+2p+u^2+u-7` for odd lambda.

This is a necessary condition only.

In `m=g+1`, physical U-holes sharpen this to

> `q<=binom(u,2)-binom(k+1,2)-k-M`,
>
> `E_U<=C0-Y_0-[D(A,M)]_+`.

Thus every actual allocation must satisfy

> `a <= (p-lambda)(p+u)+binom(u,2)-binom(k+1,2)-k-M`
> `     +C0-Y_0-[D(A,M)]_+`.

---

## 5. Pair budget -> X-density

Exact pair separation gives

> `L_X<=B_P-A-M`.

Combining with the exact Hall identity and physical `Z_X` floor gives

> `2e(X)>=Q_H+g(g-1)-B_P+2A-(k-1)M`.

Star separation gives

> `e(X)<=E_max(A):=binom(g,2)+kA`.

If `s=B_P-H(A,M)`, then

> **`2(E_max(A)-e(X))<=s+[-D(A,M)]_+`.**

So in positive Hall demand, exact pair/Hall saturation forces the star-separation maximum graph on X.

---

## 6. Hamming dichotomy

Let

`h_*=d_H(c_*,d)`, `H_X=k h_*+sum_{h in H_M}d_H(c(h),d)`.

If any distance exceeds one, then `H_X>=x+1`, every Y-vertex pays at least two rooted slots, and

> **`r>=a+y`.**

If all distances equal one, then `c_*` and all H_M codes are distinct one-coordinate flips of d. Every internal X-edge has Hamming length two. If `nu_X` is the number of nonisolated vertices of `G[X]`, then

> **`r>=a+nu_X`.**

Under star separation define

`nu_min(e;g,A,k)=min{h+c:0<=h<=g,0<=c<=k, e<=binom(h,2)+c min(h,A)}`.

The pair-budget X-density lower bound therefore turns directly into a finite support surcharge in the cheap branch.

---

## 7. Cheap sphere classification

In the all-distance-one branch write

`c_*=d xor e_j`, `c(h)=d xor e_i` for `h in H_M`, `i!=j`.

Raw edge-criticality of a hypothetical `z_*--H_M` edge has no possible singleton witness location: B-witnesses collide through the root; Y/H_M witnesses share matched coordinates; H_0/outside-U witnesses collide through b; and a matched reverse witness selected by `z_*` is also adjacent to b. Hence

> **`A=g`.**

The same wrong-head argument applies to every one of the `g+1` selected outside witnesses. Each is complementary to the one-flip code of the head it serves and is in fact anticomplete to all of X; the positive-buffer outside-witness theorem already makes it anticomplete to Y. Therefore

> **all `g+1` selected outside witnesses are anticomplete to A.**

Their outside-pair unmatched slack is at least

> `p(g+1)+k+M`,

where the `k+M` is the exact extra on `z_*` after `A=g`. Thus the cheap sphere branch satisfies the new exact pair-local necessary condition

> **`p(g+1)+k+M+[D(g,M)]_+<=C0-sigma_P`.**

At `t=1`, the selected witness codes are the complete radius-one Boolean sphere around `bar d`, and their slack contribution alone is at least `p^2`.

---

## 8. Diagnostic support

Package:

`project/research/post_ms/2026-09-19-minimal-reservoir-slot-sphere-v1/`.

The companion checker replays the same abstract bounded box as the predecessor (`3<=p<=18`, `u<=18`). Starting from the exact predecessor population of 110,387 `m=g+1` states:

- physical `r>=a` slot capacity alone rejects 45,401;
- the full noncheap / cheap-sphere dichotomy rejects 45,830;
- 64,557 remain;
- in `t=1`, all 5,404 retain a noncheap relaxation, although 1,024 lose the cheap sphere branch.

These are parameter diagnostics only, not graph counts or realizability evidence.

---

## 9. Next action

Remain at `m=g+1`.

1. Treat the non-Hamming-cheapest branch as the bottleneck. Replace the coarse `r>=a+y` by the exact vertexwise distribution of the extra Hamming units and intersect it with pair-budget-forced X-density.
2. Preserve exact `S_P/Ccap_P`; do not donate outside-pair score back to P.
3. In the surviving cheap sphere branch exploit the physical A-anticompleteness of all `g+1` selected outside witnesses, not just the aggregate slack floor.
4. Keep `X_3` live and the full rigid-cut claim conditional on the current graph-level coverage gap.
5. Do not open `m=g+2`, loaded buffer, extra buffer slack, `z=2`, or the four-exception gate while this line remains active.

Promotion level: internal hand structural theorem under rigid one-code hypotheses, with exact arithmetic diagnostic support; not graph-realizability evidence and not an eventual theorem.
