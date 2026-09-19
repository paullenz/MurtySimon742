# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-19  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is **not** the target. The published 2024 D2C graph `X_3` on 12 vertices and 32 edges has `M(12)=31` and remains a mandatory negative control. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not an optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_MINIMAL_RESERVOIR_LOCAL_SLOT_PINCH_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `bb5487bf01e06f541af1a0ffcf9352dfdaa1675c`

LAST VERIFIED RESULT: `The m=g+1 positive-buffer minimal-reservoir branch now has an exact three-ledger interface. First, disjoint X/Y slack gives the Hall/score currency H(A,M)=A+M+[Q-(2k-1)A-kM]_+ with a closed four-case H_min. Second, exact pair-local score is retained: P_0<=S_P<=C0-O_0-H(A,M); CROWD is dominated by L_Y>=y(p+2), ONE-P follows from exact crossing Ccap_P with margin y(g+2), and sigma_P is the least local score meeting 2xy<=Ccap_P. The pair/Hall-feasible M-values form one interval [M_-,M_+], while rooted residual has free optimizer M_Q=ceil([R_0]_+/(k+1)); hence the exact combined optimizer is M_hat=clamp(M_Q,M_-,M_+). Third, feeding the preserved local witness-slot/Hamming theorem into the rigid complete cut gives the new universal surcharge r_z>=1 for every z in A, hence r>=a and f+delta>=a. In m=g+1, if h_*=d_H(c_*,d) and H_X=k h_*+sum_{h in H_M}d_H(c(h),d), then r>=y ceil(H_X/x)+k ceil(y h_*/(y+A))+g. At A=0 this sharpens to r>=y ceil(H_X/x)+k h_*+g: H_0 isolation converts code distance directly into unused rooted slots. The bounded score diagnostic rejects 13,198 of the previous 123,585 abstract m=g+1 states, leaving 110,387; t=1 leaves 5,404. These are parameter diagnostics only.`

UNPRESERVED WORK: `None. New theorem notes and checker are preserved under project/research/post_ms/2026-09-19-minimal-reservoir-pair-hall-v1/.`

DEFERRED ADMIN: `README remains lower-frequency. Refresh reviewer-facing status at the next daily adversarial checkpoint unless repository integrity requires an earlier repair.`

NEXT ACTION: `Stay on m=g+1 and intersect the local-slot floor with r=f+delta and the explicit clamped allocation (M_hat,A_hat). Test first whether the universal r>=a or the weighted core/Y surcharge closes any of the compatible, Hall-left or Hall-right pinch regimes; if not, retain h_*=1 and all H_M-to-d Hamming distances one as the unique Hamming-cheapest geometry and classify that geometry directly. Preserve exact S_P/Ccap_P. Do not open m=g+2, loaded r_b>0, extra buffer slack, z=2 or the four-exception gate while this line remains live.`
<!-- CURRENT-STATUS:END -->

---

## 1. Mandatory audit gate

The binding audit is still

`project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

This run reread it, `README.md`, the latest commits, `SOURCE_PREMISE_REPAIR.md`, and `RIGID_GRAPH_LEVEL_REGRESSION.md` before advancing the mathematics.

The two named source premises remain established at their repaired levels: physical beta-source distinctness from raw singleton criticality; selected `(source,coordinate)` uniqueness from the one-representative convention. The finite source-tuple theorem is not promoted to unconditional graph-level closure.

The independent actual-D2C regression remains at 3,540 root-policy instances, 147 pair-capacity checks, 36 exact Hall decompositions and zero recorded graph/formula mismatches. `X_3` passes. No bounded-corpus graph realizes the full rigid complete-cut hypotheses, so the active results remain conditional hand implications.

Exact `Ccap_P`, `(ONE-P)` and `(CROWD)` remain mandatory. In the current equality geometry `(ONE-P)` and `(CROWD)` are now proved consequences of stronger physical bills once exact crossing `Ccap_P` is kept; they are not omitted. The four-exception gate remains subordinate.

---

## 2. Active geometry

Rigid one-code complete cut:

- `X--Y` complete, `x>=3`, `y>0`;
- Y code `d`; X contains neither `d` nor `bar d`;
- `g=g_P`, `k=x-g>0`, `t=p-g>=1`;
- `U_-=W_0 dotcup {b}`, `|W_0|=k`;
- unloaded first buffer equality `epsilon_b=t`, with `b--X` and `b--U_o` complete;
- `e(Y)=e(Y,U_d)=e(G[U_-])=0`;
- `X=H_M dotcup H_0`, sizes `g,k`;
- H_M codes are singleton A-code classes;
- all buffer--X edges use outside unmatched witnesses;
- minimal reservoir `m=g+1` forces H_0 to one code `c_*`, one common witness `z_*` of code `bar c_*`, and H_0 is independent;
- `A=g-d_{H_M}(z_*)`, `M=(u_o-1)-d_{U_o\{z_*}}(z_*)`;
- `epsilon_{z_*}=t+k+A+M`;
- `u>=x+2`, `L_Y>=y(p+2)`.

`X_3` has canonical-root `u=0` and never enters these hypotheses.

---

## 3. Pair/Hall currency

Primary note:

`project/research/post_ms/2026-09-19-minimal-reservoir-pair-hall-v1/MINIMAL_RESERVOIR_PAIR_HALL_ALLOCATION.md`.

Put

`N=u-k-2`, `s_1=[t-k+1]_+`,

`E_*=k(p+k)+2t+k+g s_1`, `Y_0=y(p+2)`,

`Q=x(x-T_0)+k(x-1)+x-g(g-1)+kN`.

Then

> `L_X>=[Q-(2k-1)A-kM]_+`,
>
> `S>=E_*+Y_0+H(A,M)`,
>
> `H(A,M)=A+M+[Q-(2k-1)A-kM]_+`.

The exact H-minimum treats A as unit-cost capacity `2k-1` and M as unit-cost capacity k. For `k>1`, score/Hall can prefer `A>0` even though rooted residual alone prefers `A=0`; this is a justified refinement of the previous handoff.

---

## 4. Exact pair-local gate

For `P={d,bar d}`,

`K_P=k(p+k)+t`, `P_0=K_P+Y_0`, `O_0=t+k+g s_1`.

Above threshold:

> `P_0<=S_P<=C0-O_0-H(A,M)`.

Define

`D_code=5p+5u-3lambda-2`,

`R_code(s)=max(0,floor((D_code+sqrt(D_code^2+12s))/3))`,

> `sigma_P=min{s>=P_0:R_code(s)[g+2s/(lambda+1)]>=2xy}`.

Then

> `H(A,M)<=B_P=C0-O_0-sigma_P`.

Also

`3y-D_code=p-2u-3x-1`,

so the Y-slack floor dominates positive `(CROWD)` by `y(2u+3x+3)`. Exact crossing capacity plus Y-slack implies `(ONE-P)` with margin `y(g+2)`.

---

## 5. Pair/residual pinch

Continuation:

`project/research/post_ms/2026-09-19-minimal-reservoir-pair-hall-v1/MINIMAL_RESERVOIR_PAIR_RESIDUAL_PINCH.md`.

For fixed M, let `h_A(D)` be the least A-cost. Then

> `F(M)=M+h_A(Q-kM)`

is V-shaped, hence

> `M_adm={M:F(M)<=B_P}=[M_-,M_+] cap Z`

when nonempty.

The rooted residual term is V-shaped with free optimizer

> `M_Q=ceil([R_0]_+/(k+1))`.

Thus

> `M_hat=clamp(M_Q,M_-,M_+)`

and the exact intersected lower bound is

> `q+E_U>=E_*+M_hat+ceil([R_0-(k+1)M_hat]_+/2)`.

The least A-allocation at `M_hat` is explicit from `h_A(Q-kM_hat)`.

---

## 6. New local-slot surcharge

New note:

`project/research/post_ms/2026-09-19-minimal-reservoir-pair-hall-v1/RIGID_CUT_LOCAL_SLOT_SURCHARGE.md`.

The preserved local theorem is

`sum_{w in N_A(z)}d_H(c(w),c(z))<=r_z d_A(z)`, with `sum_z r_z=r`.

Because every vertex on either side of the complete X--Y cut has a neighbour of a different code,

> **`r_z>=1` for every `z in A`, hence `r>=a`.**

Using `r=f+delta`,

> `f+delta>=a`.

For the active minimal reservoir put

`h_*=d_H(c_*,d)>=1`,

`H_X=k h_*+sum_{h in H_M}d_H(c(h),d)>=x`.

Since `e(Y)=0`, each Y vertex has A-degree x, giving

> `r_y>=ceil(H_X/x)`.

Star separation and H_0 independence give `d_A(x_0)<=y+A` for every core head, hence

> `r_{x_0}>=ceil(y h_*/(y+A))`.

Together with `r_h>=1` on H_M,

> **`r>=y ceil(H_X/x)+k ceil(y h_*/(y+A))+g`.**

At `A=0`, H_0 is isolated in X, so

> **`r>=y ceil(H_X/x)+k h_*+g`.**

Thus the Hamming-cheapest equality geometry is forced toward `h_*=1` and all H_M-to-d distances one; any larger distance pays extra local residual immediately.

---

## 7. Diagnostic support

Checker:

`project/research/post_ms/2026-09-19-minimal-reservoir-pair-hall-v1/check_minimal_reservoir_pair_hall.py`.

On the same coarse bounded box, the new additive Hall floor rejects 13,198 of the prior 123,585 abstract `m=g+1` survivors, leaving 110,387. In `t=1`, 116 of 5,520 are rejected, leaving 5,404. Every bounded sharpened-score survivor has `sigma_P=P_0`, so exact Ccap adds no extra rejection there. These are abstract parameter diagnostics, not graph counts.

---

## 8. Next action

Remain at `m=g+1`.

1. Intersect the local-slot floor with `r=f+delta` and the explicit `(M_hat,A_hat)` allocation.
2. Test whether `r>=a` or the weighted slot surcharge closes any of the compatible / Hall-left / Hall-right regimes.
3. If not, classify the unique Hamming-cheapest geometry `h_*=1`, all H_M-to-d distances one, before any enlargement to `m=g+2`.
4. Preserve pair-local `S_P` and exact `Ccap_P` throughout.
5. Keep loaded `r_b>0`, extra buffer slack, `z=2`, and four-exception work subordinate.

Promotion level: internal hand structural theorem conditional on rigid one-code hypotheses, supported by exact arithmetic diagnostics; not graph-realizability evidence and not an eventual theorem.