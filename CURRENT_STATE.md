# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-19  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is **not** the target. The published 2024 D2C graph `X_3` on 12 vertices and 32 edges has `M(12)=31` and remains a mandatory negative control. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not an optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_MINIMAL_RESERVOIR_PAIR_RESIDUAL_PINCH_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `bb5487bf01e06f541af1a0ffcf9352dfdaa1675c`

LAST VERIFIED RESULT: `In the positive-buffer unloaded common-buffer minimal-reservoir layer m=g+1, disjoint X/Y slack gives L_A=L_X+L_Y and the exact Hall/score defect currency H(A,M)=A+M+[Q-(2k-1)A-kM]_+. H_min has a closed four-case formula. The outside one-code pair P has the exact local box P_0<=S_P<=C0-O_0-H(A,M); CROWD is strictly dominated by L_Y>=y(p+2), and ONE-P follows with margin y(g+2) from the exact crossing requirement 2xy<=Ccap_P. Defining sigma_P as the least local pair score meeting exact Ccap_P gives H(A,M)<=B_P=C0-O_0-sigma_P. For fixed M the least Hall cost F(M)=M+h_A(Q-kM) is V-shaped, so the exact admissible M-set is one integer interval [M_-,M_+]. The rooted residual term is also V-shaped with free optimizer M_Q=ceil([R_0]_+/(k+1)); consequently the exact pair/residual optimizer is M_hat=clamp(M_Q,M_-,M_+), eliminating the residual scan. Once M_hat is fixed, the least A-allocation is explicit; if Q-kM_hat> (2k-1)g then all g A-defects are forced and positive X-slack remains. The bounded diagnostic before the clamp refinement rejects 13,198 of the prior 123,585 abstract m=g+1 survivors, leaving 110,387; t=1 leaves 5,404. On that bounded box sigma_P=P_0 for every sharpened-score survivor.`

UNPRESERVED WORK: `None. The theorem notes and checker are preserved under project/research/post_ms/2026-09-19-minimal-reservoir-pair-hall-v1/.`

DEFERRED ADMIN: `README remains lower-frequency. Refresh reviewer-facing status at the next daily adversarial checkpoint unless repository integrity requires an earlier repair.`

NEXT ACTION: `Stay on m=g+1. At the explicit extremal allocation (M_hat,A_hat), return to the rooted unused-slot/direct-Hamming ledger. Try to prove that forced z_*--H_M missing adjacencies or the residual positive X-slack consume direct/Hamming resource not yet priced by H(A,M). Treat the compatible, Hall-left and Hall-right pinch regimes separately only if one slot/Hamming lemma does not cover all three. Preserve exact S_P/Ccap_P. Do not open m=g+2, loaded r_b>0, extra buffer slack, z=2 or the four-exception gate while this line remains live.`
<!-- CURRENT-STATUS:END -->

---

## 1. Mandatory audit gate

The latest daily red-team audit remains

`project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

It was reread before this run, together with the latest handoff and commits. Its verified findings, invalidations, confidence changes and stop/pivot rules remain binding.

### Source-tuple premises

`project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/SOURCE_PREMISE_REPAIR.md` was reread. It establishes the two named premises at the exact level used:

1. distinct physical beta-source identity follows from raw unique-common-neighbour criticality;
2. global selected `(source,coordinate)` uniqueness is a selected-representative convention for one physical obligation, not raw witness uniqueness.

The finite source-tuple theorem is still not promoted as unconditional graph-level closure; it remains conditional on the broader rooted selected-obligation construction.

### Independent actual-D2C regression

`project/research/post_ms/2026-09-19-rigid-graph-regression-v1/RIGID_GRAPH_LEVEL_REGRESSION.md` was reread. Recorded run: 3,540 root-policy instances, 147 pair-capacity checks, 36 exact Hall-cut decompositions, zero graph/formula mismatches. `X_3` passes.

Coverage limitation remains explicit: no bounded-corpus graph realizes the full rigid complete Hall cut with `x>=3`, `M_X=E_X=0`. All active one-code rigid deductions remain conditional hand implications.

Exact pair-local `Ccap_P`, `(ONE-P)` and `(CROWD)` remain mandatory. In the present equality geometry, `(CROWD)` and `(ONE-P)` have now been proved consequences of stronger physical bills once exact crossing `Ccap_P` is retained; they are not silently omitted.

The four-exception gate remains subordinate.

---

## 2. Closed / superseded lines

Do not reopen:

- mixed `{4,5}` selected-excess ladder;
- zero-buffer `g=p` common-buffer branch;
- invalid positive-buffer matched reverse Orientation B or reverse-deficit scalarizations depending on it.

`X_3` remains a hostile control: canonical root `u=0`, so it never enters the active positive-buffer/minimal-reservoir hypotheses.

---

## 3. Active minimal-reservoir geometry

Rigid one-code complete cut:

- `X--Y` complete, `x>=3`, `y>0`;
- Y has code `d`; X contains neither `d` nor `bar d`;
- `g=g_P`, `k=x-g>0`, `t=p-g>=1`;
- `U_-=W_0 dotcup {b}`, `|W_0|=k`;
- `e(Y)=e(Y,U_d)=e(G[U_-])=0`;
- unloaded buffer and first equality: `epsilon_b=t`, `b--X`, `b--U_o` complete;
- `X=H_M dotcup H_0`, sizes `g,k`;
- H_M heads have distinct singleton A-codes;
- all buffer--X edges are outside-U certified;
- `m=g+1` forces all H_0 heads to one code `c_*` and one common outside witness `z_*` of code `bar c_*`;
- H_0 is independent;
- `u>=x+2`, `L_Y>=y(p+2)`;
- `A=g-d_{H_M}(z_*)`, `M=(u_o-1)-d_{U_o\{z_*}}(z_*)`;
- `epsilon_{z_*}=t+k+A+M`.

Put

`N=u-k-2`, `s_1=[t-k+1]_+`,

`E_*=k(p+k)+2t+k+g s_1`, `Y_0=y(p+2)`,

`Q=x(x-T_0)+k(x-1)+x-g(g-1)+kN`.

---

## 4. Pair/Hall defect currency

Primary note:

`project/research/post_ms/2026-09-19-minimal-reservoir-pair-hall-v1/MINIMAL_RESERVOIR_PAIR_HALL_ALLOCATION.md`.

Exact Hall feedback:

> `L_X>=[Q-(2k-1)A-kM]_+`.

Since `L_A=L_X+L_Y`,

> `S>=E_*+Y_0+H(A,M)`,
>
> `H(A,M)=A+M+[Q-(2k-1)A-kM]_+`.

Let `c_A=2k-1`, `c_M=k`, `C_A=c_A g`, `C_T=c_A g+c_M N`. Then

- `H_min=0` if `Q<=0`;
- `H_min=ceil(Q/c_A)` if `0<Q<=C_A`;
- `H_min=g+ceil((Q-C_A)/c_M)` if `C_A<Q<=C_T`;
- `H_min=g+N+Q-C_T` if `Q>C_T`.

This is a justified refinement of the prior `A=0` handoff: rooted residual alone prefers `A=0`, but score/Hall prefers A-defects when `k>1` because they buy `2k-1` units of Hall relief per score unit versus k for M-defects.

---

## 5. Exact pair-local gate

For `P={d,bar d}`,

`K_P=k(p+k)+t`, `P_0=K_P+Y_0`, `O_0=t+k+g s_1`, with `E_*=K_P+O_0`.

Above threshold:

> `P_0<=S_P<=C0-O_0-H(A,M)`.

Define `D_code=5p+5u-3lambda-2` and

`R_code(s)=max(0,floor((D_code+sqrt(D_code^2+12s))/3))`.

Let

> `sigma_P=min{s>=P_0: R_code(s)[g+2s/(lambda+1)]>=2xy}`.

Then

> `H(A,M)<=B_P:=C0-O_0-sigma_P`.

Mandatory-trio simplification is proved, not assumed:

- `3y-D_code=p-2u-3x-1`, so `L_Y>=y(p+2)` dominates `(CROWD)` by margin `y(2u+3x+3)` when CROWD is positive;
- exact crossing `Ccap_P>=2xy` plus `L_Y>=y(p+2)` implies `(ONE-P)` with margin `y(g+2)`.

Thus exact crossing `Ccap_P` is the independent local pair gate in this geometry.

---

## 6. Exact pair/residual pinch

Continuation note:

`project/research/post_ms/2026-09-19-minimal-reservoir-pair-hall-v1/MINIMAL_RESERVOIR_PAIR_RESIDUAL_PINCH.md`.

For fixed M define

`h_A(D)=0` if `D<=0`;

`h_A(D)=ceil(D/(2k-1))` if `0<D<=(2k-1)g`;

`h_A(D)=g+D-(2k-1)g` if `D>(2k-1)g`.

Then

> `F(M)=M+h_A(Q-kM)`

is V-shaped, so

> `M_adm={M:F(M)<=B_P}=[M_-,M_+] cap Z`

whenever nonempty.

The rooted residual term

`G(M)=E_*+M+ceil([R_0-(k+1)M]_+/2)`

is also V-shaped, with free optimizer

> `M_Q=ceil([R_0]_+/(k+1))`.

Therefore the exact combined optimizer is

> `M_hat=clamp(M_Q,M_-,M_+)`,

and

> `q+E_U>=E_*+M_hat+ceil([R_0-(k+1)M_hat]_+/2)`.

At `M_hat`, the least A-allocation is explicit from `h_A(Q-kM_hat)`. If `Q-kM_hat>(2k-1)g`, all g possible A-defects are forced and positive X-slack remains.

Three regimes are now explicit: compatible (`M_Q` inside the interval), Hall-left (`M_Q<M_-`) and Hall-right (`M_Q>M_+`).

---

## 7. Diagnostic support

Checker:

`project/research/post_ms/2026-09-19-minimal-reservoir-pair-hall-v1/check_minimal_reservoir_pair_hall.py`.

It verifies the closed H-minimum against brute integer minimization and replays the coarse parameter scan.

From the preceding 123,585 abstract `m=g+1` survivors:

- 13,198 rejected;
- 110,387 remain.

`t=1`: 116 of 5,520 rejected, 5,404 remain.

On this bounded scan every sharpened-score survivor has `sigma_P=P_0`; exact Ccap therefore adds no further finite rejection in that box. This is diagnostic only, not a theorem of redundancy.

These are abstract parameter states, not graph counts.

---

## 8. Next action

Stay at `m=g+1` and the explicit `(M_hat,A_hat)` geometry.

1. Attack the rooted unused-slot/direct-Hamming ledger with the forced `z_*--H_M` missing adjacencies and/or surviving positive X-slack.
2. Seek one lemma valid across compatible, Hall-left and Hall-right regimes; split only if necessary.
3. Preserve exact local `S_P` and `Ccap_P`; do not revert to total `C0` capacity.
4. If this allocation survives, classify its graph geometry before `m=g+2`.
5. Keep loaded buffer `r_b>0`, extra buffer slack, `z=2` and four-exception work subordinate.

Promotion level remains: internal hand structural theorem conditional on rigid one-code hypotheses, supported by exact arithmetic diagnostics; not graph-realizability evidence and not an eventual theorem.