# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-19  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is **not** the target. The published 2024 D2C graph `X_3` on 12 vertices and 32 edges has `M(12)=31` and remains a mandatory negative control. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not an optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_MINIMAL_RESERVOIR_PAIR_HALL_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `bb5487bf01e06f541af1a0ffcf9352dfdaa1675c`

LAST VERIFIED RESULT: `In the positive-buffer unloaded common-buffer minimal outside-reservoir layer m=g+1, the X- and Y-slack bills are disjoint and therefore additive: L_A=L_X+L_Y. Writing A=A_*, M=M_*, N=u-k-2 and Q=x(x-T0)+k(x-1)+x-g(g-1)+kN, the exact score/Hall defect term is H(A,M)=A+M+[Q-(2k-1)A-kM]_+. Its integer minimum has a closed four-case formula obtained by treating A-defects as unit-cost Hall-relief capacity 2k-1 and M-defects as unit-cost capacity k. This yields S>=E_*+y(p+2)+H_min. Pair-local score is retained exactly: for P={d,bar d}, S_P>=P_0=k(p+k)+t+y(p+2), while compulsory score outside P is at least O_0+H(A,M), O_0=t+k+g[t-k+1]_+. Thus above threshold P_0<=S_P<=C0-O_0-H(A,M). In this geometry CROWD is strictly implied by L_Y>=y(p+2), because 3y-D_code=p-2u-3x-1, and ONE-P is implied with margin y(g+2) once the exact crossing capacity 2xy<=Ccap_P is imposed. Defining sigma_P as the least local score meeting exact Ccap_P gives the compact pair gate H(A,M)<=C0-O_0-sigma_P. The admissible M-values are then intersected with QE-MR rather than optimized independently. The bounded diagnostic rejects 13,198 of the previous 123,585 abstract m=g+1 survivors, leaving 110,387; in the t=1 slice it rejects 116 of 5,520, leaving 5,404. On that bounded box sigma_P=P_0 for every new survivor, so exact Ccap adds no further finite rejection there.`

UNPRESERVED WORK: `None. The theorem note and diagnostic checker are preserved under project/research/post_ms/2026-09-19-minimal-reservoir-pair-hall-v1/.`

DEFERRED ADMIN: `README remains lower-frequency. Refresh reviewer-facing status at the next daily adversarial checkpoint unless repository integrity requires an earlier repair.`

NEXT ACTION: `Stay on m=g+1. Use the exact admissible-M set M_adm={M: M+h_A(Q-kM)<=C0-O_0-sigma_P} together with QE-MR to classify the low-score/low-residual intersection. The key tension is now explicit: score/Hall prefers the more efficient A-defects when k>1, whereas rooted residual relief sees only M-defects and therefore prefers M. Feed the forced A/M allocation into the rooted unused-slot/Hamming ledger and direct/Hamming credit before opening m=g+2. Keep loaded r_b>0, extra buffer slack, z=2 and the four-exception gate subordinate.`
<!-- CURRENT-STATUS:END -->

---

## 1. Mandatory audit gate

The latest daily red-team audit remains

`project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

Its verified findings, invalidations, confidence changes and stop/pivot rules remain binding.

### Source-tuple premises

`project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/SOURCE_PREMISE_REPAIR.md` was reread before the present extension. It establishes the two named upstream premises at the exact level used:

1. distinct physical beta-source identity follows directly from raw unique-common-neighbour criticality;
2. global selected `(source,coordinate)` uniqueness is a selected-representative convention for one physical obligation, not raw witness uniqueness.

The finite source-tuple capacity theorem remains conditional on the broader rooted selected-obligation model and is not promoted as unconditional graph-level closure.

### Independent actual-D2C regression

`project/research/post_ms/2026-09-19-rigid-graph-regression-v1/RIGID_GRAPH_LEVEL_REGRESSION.md` was also reread. The recorded actual-graph run has 3,540 root-policy instances, 147 pair-capacity checks, 36 exact Hall-cut decompositions and zero graph/formula mismatches. `X_3` passes.

Coverage limitation remains explicit: no graph in the bounded corpus realizes the full rigid complete Hall cut with `x>=3`, `M_X=E_X=0`. All one-code rigid deductions therefore remain conditional hand implications, not empirical graph classifications.

The exact one-code `Ccap_P`, `(ONE-P)` and `(CROWD)` obligations remain mandatory. In the present minimal-reservoir equality geometry, the new theorem proves that `(CROWD)` and `(ONE-P)` are consequences of stronger physical bills once exact crossing `Ccap_P` is retained; they are not silently dropped.

The four-exception gate remains subordinate.

---

## 2. Closed / superseded material

Do not reopen:

- the mixed `{4,5}` selected-excess ladder;
- the zero-buffer `g=p` common-buffer branch, closed in `2026-09-19-zero-buffer-complete-separation-v1`;
- the invalid positive-buffer matched reverse Orientation B and any reverse-deficit scalarization that depended on it.

The repaired positive-buffer theorem is

`project/research/post_ms/2026-09-19-positive-buffer-reverse-collapse-v1/POSITIVE_BUFFER_REVERSE_COLLAPSE_AND_HEAD_DICHOTOMY.md`.

---

## 3. Active branch

Rigid one-code complete cut:

- `X--Y` complete, `x>=3`, `y>0`;
- Y has code `d`; X contains neither `d` nor `bar d`;
- `g=g_P`, `k=x-g>0`, `t=p-g>=1`;
- `U_-=W_0 dotcup {b}`, `|W_0|=k`;
- `e(Y)=e(Y,U_d)=e(G[U_-])=0`;
- unloaded buffer `r_b=0` and first buffer equality `epsilon_b=t`, so `b--X` and `b--U_o` are complete;
- `X=H_M dotcup H_0`, `|H_M|=g`, `|H_0|=k`;
- H_M heads have pairwise distinct singleton A-code classes;
- every buffer--X edge is outside-U certified;
- minimal outside-reservoir `m=g+1` forces all H_0 heads to share code `c_*` and common outside witness `z_*` of code `bar c_*`;
- H_0 is independent;
- `u>=x+2` and `L_Y>=y(p+2)`;
- `A=A_*=g-d_{H_M}(z_*)`, `M=M_*=(u_o-1)-d_{U_o\{z_*}}(z_*)`;
- `epsilon_{z_*}=t+k+A+M`.

The mandatory negative control `X_3` has `u=0` and never enters these hypotheses.

---

## 4. New pair/Hall allocation theorem

Primary note:

`project/research/post_ms/2026-09-19-minimal-reservoir-pair-hall-v1/MINIMAL_RESERVOIR_PAIR_HALL_ALLOCATION.md`.

Put

`N=u-k-2`, `s_1=[t-k+1]_+`,

`E_*=k(p+k)+2t+k+g s_1`, `Y_0=y(p+2)`,

`B_X=x(x-T_0)+k(x-1)+x-g(g-1)`, `Q=B_X+kN`.

The star separation and exact Hall identity give

> `L_X>=[Q-(2k-1)A-kM]_+`.

Because X and Y partition A,

> `L_A=L_X+L_Y`.

Hence

> `S>=E_*+Y_0+H(A,M)`,
>
> `H(A,M)=A+M+[Q-(2k-1)A-kM]_+`.

### Exact defect-currency elimination

Let `c_A=2k-1`, `c_M=k`, `C_A=c_A g`, `C_T=c_A g+c_M N`. Then

`H_min=0` for `Q<=0`;

`H_min=ceil(Q/c_A)` for `0<Q<=C_A`;

`H_min=g+ceil((Q-C_A)/c_M)` for `C_A<Q<=C_T`;

`H_min=g+N+Q-C_T` for `Q>C_T`.

Thus

> `S>=E_*+Y_0+H_min`.

This corrects an optimization asymmetry in the previous handoff: `A=0` is preferred by the rooted residual ledger, but for `k>1` an A-defect buys `2k-1` Hall-relief units while an M-defect buys only k. Score/Hall can therefore prefer `A>0`. The line is not abandoned; the two ledgers must be intersected.

---

## 5. Exact pair-local allocation

For the outside pair `P={d,bar d}`,

`K_P=k(p+k)+t`,

> `S_P>=P_0:=K_P+Y_0`.

Put

`O_0=t+k+g s_1`, so `E_*=K_P+O_0`.

All X-slack and the remaining compulsory unmatched slack lie outside P, so above threshold

> `P_0<=S_P<=C0-O_0-H(A,M)`.

This is the local score box used for capacity; no replacement `S_P=C0` is allowed.

Let

`D_code=5p+5u-3lambda-2`,

`R_code(s)=max(0,floor((D_code+sqrt(D_code^2+12s))/3))`.

Define

> `sigma_P=min{s>=P_0: R_code(s)[g+2s/(lambda+1)]>=2xy}`.

Then every survivor must satisfy

> `H(A,M)<=B_P:=C0-O_0-sigma_P`,

and therefore

> `H_min<=B_P`.

### Mandatory trio reconciliation

The crowding term has

`3y-D_code=p-2u-3x-1`,

so `L_Y>=y(p+2)` exceeds the positive `(CROWD)` right side by `y(2u+3x+3)`.

Further, exact crossing capacity `Ccap_P>=2xy` plus `L_Y>=y(p+2)` implies `(ONE-P)` with margin `y(g+2)`.

Thus exact crossing `Ccap_P` is the independent pair gate in this equality layer, while `(ONE-P)` and `(CROWD)` remain explicitly checked consequences.

---

## 6. Pair/residual intersection

For fixed M, define `D=Q-kM`, `c_A=2k-1`, and

`h_A(D)=0` if `D<=0`;

`h_A(D)=ceil(D/c_A)` if `0<D<=c_A g`;

`h_A(D)=g+D-c_A g` if `D>c_A g`.

Then

> `M_adm={0<=M<=N: M+h_A(Q-kM)<=B_P}`

is exactly the set of M-values which can be completed by some A-value without violating the pair-local score/capacity gate.

The rooted residual must now be minimized only over this set:

> `q+E_U >= min_{M in M_adm}`
> `{E_*+M+ceil([R_0-(k+1)M]_+/2)}`.

This is the live structural pinch: Hall/score tends to spend A, rooted residual tends to spend M.

---

## 7. Diagnostic support

Checker:

`project/research/post_ms/2026-09-19-minimal-reservoir-pair-hall-v1/check_minimal_reservoir_pair_hall.py`.

It brute-force verifies the closed `H_min` formula on a finite integer box and replays the same coarse parameter scan as the preceding diagnostic.

Starting from the preceding 123,585 abstract `m=g+1` survivors:

- 13,198 are rejected by the additive Hall score;
- 110,387 remain.

For `t=1`:

- 116 of 5,520 are rejected;
- 5,404 remain.

In this bounded scan, every sharpened-score survivor has `sigma_P=P_0`, so the exact pair gate adds no further rejection. This is diagnostic only and must not be promoted to a general theorem.

These are abstract integer parameter states, not graph counts.

---

## 8. Next action

Remain at `m=g+1`.

1. Classify `M_adm` and the minimizers of the intersected `QE-MR` bound, especially the transition where Hall wants A-defects but residual wants M-defects.
2. Feed the resulting forced A/M allocation into the rooted unused-slot/Hamming/direct-credit ledger; this is now more promising than another total-score relaxation.
3. Preserve exact pair-local `S_P` and `Ccap_P` throughout.
4. If the low-score/low-residual intersection survives, classify its graph geometry before opening `m=g+2`.
5. Keep loaded buffer `r_b>0`, extra buffer slack, `z=2` and the four-exception gate subordinate.

Promotion level remains: internal hand structural theorem conditional on the rigid one-code hypotheses, with exact arithmetic diagnostics; not graph-realizability evidence and not an eventual theorem.