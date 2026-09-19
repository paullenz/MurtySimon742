# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-19  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is **not** the target. The published 2024 D2C graph `X_3` on 12 vertices and 32 edges has `M(12)=31` and remains a mandatory negative control. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not an optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_MINIMAL_RESERVOIR_NONCHEAP_DISTRIBUTED_HAMMING_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `fd5cab9349310f2435259099e8253ebaefea4bd5`

LAST VERIFIED RESULT: `The m=g+1 non-Hamming-cheapest branch now has a distribution-sensitive rooted-slot theorem. Writing e_v=d_H(c(v),d)-1, E=sum_X e_v>=1, rho_vw=d_H(c(v),c(w))-1 on internal X-edges and tau_v=sum rho_vw, the local slot theorem gives r>=a+y ceil(E/x)+sum_{v in X} ceil((y e_v+tau_v)/(y+d_X(v))). In particular every noncheap state satisfies the strict sharpening r>=a+y+1. If s vertices of X carry positive Hamming excess, the remaining x-s radius-one vertices force an additional support surcharge through dense radius-one/radius-one edges: r>=a+y ceil(E/x)+s+mu([e(X)-C(x,2)+C(x-s,2)]_+). The feasible support sizes s are further restricted by the k-fold common H_0 code. Independently, same-parity excess endpoints force internal Hamming distance at least two; with C_x(E)=max_{m<=min(E,x)}m(x-m), the X surcharge is at least ceil((yE+2[e(X)-C_x(E)]_+)/(a-1)). Combining these gives a row-wise noncheap floor R_N(A,M) after substituting the exact pair-budget density lower bound e_min(A,M). This preserves exact S_P/Ccap_P and intersects directly with the rooted residual upper budget. No new full bounded-box diagnostic is promoted in this checkpoint.`

UNPRESERVED WORK: `None. The new theorem package is preserved under project/research/post_ms/2026-09-19-minimal-reservoir-noncheap-distribution-v1/. A full diagnostic replay was deliberately not promoted before preservation; the next run should implement and independently replay R_N(A,M).`

DEFERRED ADMIN: `README remains lower-frequency. Refresh reviewer-facing status at the next daily adversarial checkpoint unless repository integrity requires an earlier repair.`

NEXT ACTION: `Stay on m=g+1. Implement an independent checker for the new distribution-sensitive noncheap floor R_N(A,M), replay it against the previous 64,557 abstract survivors, and inspect t=1 first. Record which E and support pattern minimize the row floor. If E=1 dominates, classify the unique one-defect matched-head geometry directly; if core defect appears, exploit the automatic +k core surcharge; if larger E survives, use the parity-density term and zero-radius remainder before opening m=g+2. Keep exact S_P/Ccap_P, X_3, the graph-level audit boundary, and the four-exception gate's subordinate status live.`
<!-- CURRENT-STATUS:END -->

---

## 1. Mandatory audit gate

Before forward mathematics this run reread `CURRENT_STATE.md`, root `README.md`, the latest commits, the 19 September daily red-team audit, `project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/SOURCE_PREMISE_REPAIR.md`, and `project/research/post_ms/2026-09-19-rigid-graph-regression-v1/RIGID_GRAPH_LEVEL_REGRESSION.md`.

The binding audit remains

`project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

Its requirements remain mandatory:

- distinct physical beta-source identity is established from raw singleton criticality;
- selected `(source,coordinate)` uniqueness is a one-selected-representative statement, not raw-witness uniqueness;
- the finite source-tuple capacity theorem is not promoted to unconditional graph-level closure;
- the independent actual-D2C regression remains at 3,540 root-policy instances, 147 pair-capacity checks, 36 Hall decompositions and zero recorded graph/formula mismatches;
- `X_3` passes and remains mandatory;
- no bounded-corpus graph realizes the full rigid complete-cut hypotheses, so the active branch remains a conditional hand implication;
- exact `Ccap_P`, `(ONE-P)` and `(CROWD)` remain mandatory, with the latter two treated as consequences only where already proved from stronger physical bills;
- the four-exception gate remains subordinate.

There is no departure from the audit's priority order in this checkpoint.

---

## 2. Active geometry retained

Rigid one-code complete cut, positive-buffer unloaded common-buffer first equality, minimal outside reservoir `m=g+1`:

- `X--Y` complete, `x>=3`, `y>0`, `a=x+y`;
- Y code `d`; X contains neither `d` nor `bar d`;
- `g=g_P`, `k=x-g>0`, `t=p-g>=1`;
- `U_-=W_0 dotcup {b}`, `|W_0|=k`, `epsilon_b=t`;
- `X=H_M dotcup H_0`, sizes `g,k`;
- H_M codes are pairwise distinct singleton A-code classes;
- H_0 has one common code `c_*`, is independent, and uses common outside witness `z_*`;
- exact pair/Hall variables and the predecessor minimal-reservoir pair-local spine remain in force;
- `X_3` has canonical-root `u=0` and does not enter these hypotheses.

---

## 3. New distributional Hamming theorem

Primary note:

`project/research/post_ms/2026-09-19-minimal-reservoir-noncheap-distribution-v1/NONCHEAP_HAMMING_DISTRIBUTION.md`.

For `v in X`, put

`e_v=d_H(c(v),d)-1>=0`,

`E=sum_X e_v`,

and on each internal X-edge `vw` put

`rho_vw=d_H(c(v),c(w))-1>=0`,

`tau_v=sum_{w in N_X(v)}rho_vw`.

Then the preserved local slot/Hamming theorem gives

> `r >= a + y ceil(E/x)`
> `    + sum_{v in X} ceil((y e_v+tau_v)/(y+d_X(v))).`

For the noncheapest branch `E>=1`, this immediately sharpens the previous coarse floor to

> **`r>=a+y+1`.**

The extra `+1` is forced on the X-vertex that actually carries Hamming defect; the defect cannot be paid only on the Y side.

---

## 4. Concentration/dispersion floor

Let `P={v:e_v>0}`, `s=|P|`, and `Z=X\P`. Every edge inside Z joins two distinct one-flip codes and therefore has Hamming distance exactly two. If `mu(j)` is the least q with `C(q,2)>=j`, then

> `r>=a+y ceil(E/x)+s`
> `  +mu([e(X)-C(x,2)+C(x-s,2)]_+).`

The feasible support size s is restricted by the k-fold H_0 code. Writing `q=p-2` and `E=k e_*+sum_i e_i`, the exact relaxed support set `S(E)` is:

- core-cheap: `e_*=0`, with `ceil(E/q)<=s<=min(E,g)` when `E<=gq`;
- core-noncheap: choose `e_* in {1,...,q}`, `R=E-k e_*`; if `R=0`, `s=k`; otherwise `s=k+l` with `ceil(R/q)<=l<=min(R,g)`.

Define

`Gamma(E,e)=min_{s in S(E)} {s+mu([e-C(x,2)+C(x-s,2)]_+)}`.

Then

> `r>=a+y ceil(E/x)+Gamma(E,e(X)).`

If the common H_0 code itself is noncheap (`e_*>0`), all k core heads carry defect and

> **`r>=a+y+k`.**

Thus the cheapest noncheap survivor is pushed toward keeping the core code at distance one and concentrating defect among H_M.

---

## 5. Parity-density floor

If two X-vertices have Hamming excesses of the same parity, any edge between them has positive even code distance and therefore Hamming length at least two.

If m vertices have odd excess, at most `m(x-m)` internal edges can avoid this forced excess. Since `m<=min(E,x)`, define

`C_x(E)=max_{0<=m<=min(E,x)}m(x-m)`

so that `C_x(E)=E(x-E)` for `E<x/2` and `C_x(E)=floor(x^2/4)` thereafter.

Then

> `sum_{vw in E(X)}rho_vw >= [e(X)-C_x(E)]_+`,

and the total X-side extra slot payment is at least

> `ceil((yE+2[e(X)-C_x(E)]_+)/(a-1)).`

Combining with the support floor gives

> `r>=a+y ceil(E/x)`
> ` +max{Gamma(E,e(X)), ceil((yE+2[e(X)-C_x(E)]_+)/(a-1))}`.

---

## 6. Exact pair/Hall feedback

Retain the predecessor pair-local gate

`H(A,M)<=B_P=C0-O_0-sigma_P`

and X-density floor

`2e(X)>=Q_H+g(g-1)-B_P+2A-(k-1)M`.

Define

`e_min(A,M)=max(0,ceil((Q_H+g(g-1)-B_P+2A-(k-1)M)/2))`.

Because the new support and parity floors are monotone in `e(X)`, use `e_min(A,M)` safely. The row-wise noncheap lower bound is

`R_N(A,M)=min_{1<=E<=x(p-2), S(E) nonempty}`

` {a+y ceil(E/x)`

`  +max(Gamma(E,e_min(A,M)),`

`       ceil((yE+2[e_min(A,M)-C_x(E)]_+)/(a-1)))}.`

An actual row must also fit beneath the existing rooted residual upper budget

`(p-lambda)(p+u)+C(u,2)-C(k+1,2)-k-M+C0-Y_0-[D(A,M)]_+`.

This is the current load-bearing noncheap gate. It is structural, keeps exact pair-local score separate, and directly realizes the predecessor's requested concentration/dispersion attack.

---

## 7. Diagnostic status and next work

No new full bounded-box count is promoted at this checkpoint. The previous verified diagnostic remains 64,557 abstract survivors after the noncheap/sphere dichotomy, with all 5,404 `t=1` states retaining the old coarse noncheap relaxation.

The next run should implement `R_N(A,M)` independently, replay it first on the `t=1` slice, and record the minimizing E/support geometry. The highest-value branch after that is whichever equality pattern the optimizer repeatedly selects:

- `E=1`: classify the unique one-defect matched-head geometry;
- core noncheap: exploit the automatic `+k` slot surcharge;
- larger E: combine parity-density and radius-one remainder before any larger-reservoir expansion.

Do not open `m=g+2`, loaded buffer, extra buffer slack, `z=2`, or the four-exception gate while this line remains live.

Promotion level: internal structural theorem under rigid one-code hypotheses; not graph-realizability evidence and not an eventual theorem.
