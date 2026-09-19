# Minimal-reservoir pair/Hall allocation and defect-currency theorem

Date: 2026-09-19

Status: **internal structural theorem package** for the eventual / sufficiently-large dense diameter-2-critical second-extremal programme around

`M(n)=floor((n-1)^2/4)+1`.

Nothing here claims the false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3. The published order-12, size-32 graph `X_3` remains a mandatory hostile control.

## 1. Audit reconciliation

Before this extension the live `CURRENT_STATE.md`, root `README.md`, recent commits, the 19 September daily red-team audit, `SOURCE_PREMISE_REPAIR.md`, and `RIGID_GRAPH_LEVEL_REGRESSION.md` were reread.

The audit boundary is unchanged:

- distinct physical beta-source identity is established from raw rooted criticality;
- global `(source,coordinate)` uniqueness is used only at the selected-representative level;
- the finite source-tuple theorem is not treated as unconditional graph-level closure;
- the independent actual-D2C regression still reports zero graph/formula mismatches and keeps `X_3` live;
- no bounded-corpus graph realizes the full rigid cut hypotheses, so the present one-code deductions remain conditional hand implications;
- exact pair-local `Ccap_P`, `(ONE-P)` and `(CROWD)` must be retained rather than replaced by total `C0`;
- the four-exception gate remains subordinate.

The previous handoff requested an `A_*=0` attack first. That attack is carried out below. It exposes a further fact: although the **rooted residual** minimization prefers `A_*=0`, the **score/Hall** minimization can prefer `A_*>0`, because one `A_*` defect buys more Hall relief than one `M_*` defect when `k>1`. This is a mathematically necessary refinement of the handoff, not a return to an invalidated line.

---

## 2. Setup

Stay in the positive-buffer unloaded common-buffer equality branch and in the minimal outside-reservoir layer `m=g+1`.

Use the preserved notation:

- `X--Y` is complete, `x=|X|>=3`, `y=|Y|>0`;
- `Y=A_d`, while `X` contains neither `d` nor `bar d`;
- `g=g_P`, `k=x-g>0`, `t=p-g>=1`;
- `U_-=U_{bar d}=W_0 dotcup {b}`, `|W_0|=k`;
- `epsilon_b=t`, `b--X` and `b--U_o` are complete;
- `X=H_M dotcup H_0`, `|H_M|=g`, `|H_0|=k`;
- the `H_M` heads have pairwise distinct singleton A-codes;
- all `H_0` heads have one code `c_*`, are independent, and use one common outside witness `z_*` of code `bar c_*`;
- `u_o=u-k-1` and put

> `N:=u_o-1=u-k-2`.

The minimal-reservoir classification gives `N>=g`.

Write

> `A:=A_*=g-d_{H_M}(z_*)`,
>
> `M:=M_*=(u_o-1)-d_{U_o\{z_*}}(z_*)`,

so `0<=A<=g`, `0<=M<=N`, and

> `epsilon_{z_*}=t+k+A+M`.

Put

> `s_1=[t-k+1]_+`,
>
> `E_*:=k(p+k)+2t+k+g s_1`,
>
> `Y_0:=y(p+2)`.

The preserved unmatched-slack and Y-slack floors are

> `E_U>=E_*+A+M`,                                        `(2.1)`
>
> `L_Y>=Y_0`.                                             `(2.2)`

Let `T_0=a-p`. The star-separation theorem and exact Hall identity give

`L_X >= [x(x-T_0)+k(x-1)+x+A+k(N-M)-g(g-1)-2kA]_+`.

Define

> `B_X:=x(x-T_0)+k(x-1)+x-g(g-1)`,
>
> `Q:=B_X+kN`.

Then this becomes the clean two-defect form

> **`L_X >= [Q-(2k-1)A-kM]_+`.**                         `(LX)`

---

## 3. Unit I — the X- and Y-slack bills are additive

The previous minimal-reservoir scorecard used the safe relaxation `L_A>=max(L_X,L_Y,...)`. In the present rigid cut, however, `X` and `Y` are a partition of the A-layer, and the Hall notation is literally

`L_X=sum_{z in X}epsilon_z`, `L_Y=sum_{z in Y}epsilon_z`.

Therefore

> **`L_A=L_X+L_Y`.**                                      `(ADD0)`

Combining `(2.1)`, `(2.2)` and `(LX)` gives the stronger structural score floor

> **`S=E_U+L_A`**
>
> `>=E_*+Y_0+A+M+[Q-(2k-1)A-kM]_+`.                     `(ADD)`

No witness multiplicity is counted here. The three contributions are on disjoint scorecard pieces: unmatched-vertex slack, X-vertex slack and Y-vertex slack.

This is already a strict strengthening whenever both the Y-source bill and the Hall X-bill are positive.

---

## 4. Unit II — exact defect-currency minimization

Define

> `H(A,M):=A+M+[Q-(2k-1)A-kM]_+`.                        `(H)`

The two physical defects have a transparent exchange rate:

- one missing `z_*--H_M` adjacency (`A`) costs one unit of unmatched slack and removes `2k-1` units from the Hall X-demand;
- one missing `z_*--(U_o\{z_*})` adjacency (`M`) costs one unit of unmatched slack and removes `k` units from the Hall X-demand.

Thus `A` is the more efficient Hall-relief currency when `k>1`.

Let

`c_A=2k-1`, `c_M=k`, `C_A=c_A g`, `C_T=c_A g+c_M N`.

### Theorem 4.1 — exact minimum of the two-defect score term

The integer minimum

`H_min(Q;k,g,N)=min_{0<=A<=g,0<=M<=N} H(A,M)`

is

> `0`, if `Q<=0`;
>
> `ceil(Q/c_A)`, if `0<Q<=C_A`;
>
> `g+ceil((Q-C_A)/c_M)`, if `C_A<Q<=C_T`;
>
> `g+N+Q-C_T`, if `Q>C_T`.                              `(HMIN)`

Consequently every minimal-reservoir survivor satisfies

> **`S>=E_*+Y_0+H_min(Q;k,g,N)`.**                        `(S-HALL)`

### Proof

Think of the `g` available A-defects as unit-cost resources of capacity `2k-1`, and the `N` available M-defects as unit-cost resources of capacity `k`. For a fixed number of purchased resources, the uncovered positive Hall demand is minimized by taking the larger-capacity A-resources first. While uncovered demand is positive, buying any resource of capacity at least one never worsens the objective; if its capacity is at least two it strictly improves the objective unless only one uncovered unit remains. Hence the optimum is the minimum number of sorted resources needed to cover Q, unless total resource capacity is insufficient, in which case every resource is used and the remaining uncovered demand is paid directly. The four displayed cases follow. For `k=1`, both capacities equal one and the same formula reduces identically to `[Q]_+`. `square`

### Interpretation

The earlier rooted-residual calculation correctly found that `A` cancels from `Z-E_U` and therefore prefers `A=0`. The new score/Hall calculation sees a different objective: for `k>1`, `A` buys `2k-1` units of Hall relief for one score unit, versus only `k` for `M`. Thus the two ledgers exert **opposite pressure** on the equality geometry. This opposition is now load-bearing and should be exploited rather than optimizing either ledger in isolation.

---

## 5. Unit III — exact pair-local score separation

Return to the outside one-code pair

`P={d,bar d}`.

The core witnesses `W_0` and the buffer `b` lie in `U_{bar d}`. The exact core floor and buffer equality give

> `E_{bar d}>=K_P:=k(p+k)+t`.                             `(P-E)`

Together with `L_Y>=Y_0` and `A_bar d=emptyset`,

> **`S_P>=P_0:=K_P+Y_0`.**                                `(P-LOW)`

This is a genuinely pair-local lower bound, not `S_P<=S<=C0` used backwards.

All remaining compulsory unmatched slack in `E_*` lies outside P. Put

> `O_0:=t+k+g s_1`,

so that

> `E_*=K_P+O_0`.

The A-vertices in X also lie outside P. Therefore `(LX)` gives the disjoint complementary score payment

> `S-S_P>=O_0+A+M+[Q-(2k-1)A-kM]_+`
> `        =O_0+H(A,M)`.                                  `(P-OUT)`

For an above-`M(n)` candidate, `S<=C0`. Hence the exact local interval is

> **`P_0 <= S_P <= C0-O_0-H(A,M)`.**                     `(P-BOX)`

This is the required preservation of pair-local slack. The outside-pair payment is not donated back to P as fictitious certificate capacity.

---

## 6. Unit IV — `(CROWD)` is automatically discharged in this geometry

The one-code crowding requirement is

`S_P>=y(3y-D_code)` whenever `3y>=D_code`, where

> `D_code=5p+5u-3lambda-2`.

Using

`y=2p+u-lambda-1-x`,

we get the exact cancellation

> `3y-D_code=p-2u-3x-1`.                                 `(C-ID)`

But the Y-degree bill alone is `Y_0=y(p+2)`. If the crowding right side is positive, then

`Y_0-y(3y-D_code)`

`=y[(p+2)-(p-2u-3x-1)]`

> `=y(2u+3x+3)>0`.                                       `(C-MARG)`

Hence `(CROWD)` is strictly implied by the already-forced Y-slack bill in this minimal-reservoir branch. It remains part of the audit checklist, but it is no longer an independent obstruction here.

---

## 7. Unit V — `(ONE-P)` reduces to exact crossing capacity

Every one of the `xy` crossing A-edges is non-direct: Y has code d, while X contains neither d nor `bar d`. Rigid orientation selects the source in Y. Therefore the exact pair traffic satisfies

> `t_P>=xy`,

and exact pair capacity requires

> **`2xy <= Ccap_P`**
> `=R_code(S_P)[g+2S_P/(lambda+1)]`.                     `(PAIR)`

Now `(ONE-P)` asks

`Ccap_P+L_Y >= y(p+2x-g)`.

The right side differs from `2xy` by

`y(p+2x-g)-2xy=y(p-g)=yt`.

But

`L_Y>=Y_0=y(p+2)=yt+y(g+2)`.

Therefore `(PAIR)` implies

> `Ccap_P+L_Y >= y(p+2x-g)+y(g+2)`.                      `(ONE-MARG)`

So `(ONE-P)` is automatically satisfied, with strict margin, once the exact crossing-capacity inequality `(PAIR)` and the physical Y-degree bill are enforced.

This does **not** discard pair-local capacity. It identifies the exact crossing demand `(PAIR)` as the only independent member of the `Ccap_P` / `(ONE-P)` / `(CROWD)` trio on this particular equality geometry.

---

## 8. Unit VI — exact pair-capacity threshold and the local feasibility gate

For integer `s>=0`, define

> `R_code(s)=max(0,floor((D_code+sqrt(D_code^2+12s))/3))`.

The exact capacity function

> `F_P(s):=R_code(s)[g+2s/(lambda+1)]`

is nondecreasing in s. Define the **minimal local pair budget**

> `sigma_P:=min{s in Z_{>=P_0}: F_P(s)>=2xy}`.            `(SIGMA)`

If no such integer exists below the total score ceiling, the branch is impossible.

Combining `(P-BOX)` and `(SIGMA)` gives the compact necessary condition

> **`H(A,M) <= B_P:=C0-O_0-sigma_P`.**                   `(PAIR-GATE)`

Eliminating A and M with `(HMIN)` gives the parameter-only necessary condition

> **`H_min(Q;k,g,N)<=B_P`.**                              `(PAIR-ELIM)`

This is the requested exact pair-local synthesis. `S_P` is never replaced by `C0`; instead the compulsory outside-pair score is subtracted first, and the exact local radius/capacity function determines `sigma_P`.

---

## 9. Unit VII — intersecting pair feasibility with the rooted residual ledger

For the rooted residual, the previous minimal-reservoir theorem gives

`q+E_U >= E_*+M+ceil([R_0-(k+1)M]_+/2)`,                `(QE-MR)`

where

`R_0=Z_+ + kN-u(p-lambda)-E_*`

and `Z_+=ka+y(g+2)+g`.

The crucial point is that the pair/Hall gate restricts which values of M are actually available.

For fixed M, put

`D_M^X:=Q-kM`, `c_A=2k-1`, and define

> `h_A(D)=0`, if `D<=0`;
>
> `h_A(D)=ceil(D/c_A)`, if `0<D<=c_A g`;
>
> `h_A(D)=g+D-c_A g`, if `D>c_A g`.                      `(HA)`

This is exactly

`min_{0<=A<=g}{A+[D-c_A A]_+}`.

Hence define the admissible M-set

> `M_adm={0<=M<=N : M+h_A(Q-kM)<=B_P}`.                  `(MADM)`

Then the correctly intersected rooted bound is

> **`q+E_U >= min_{M in M_adm}`**
> ` {E_*+M+ceil([R_0-(k+1)M]_+/2)}`.                    `(QE-PAIR)`

If `M_adm` is empty, the minimal-reservoir branch is closed immediately.

This exposes the structural tension cleanly:

- Hall/score wants to spend the more efficient A-defects first;
- the rooted residual does not benefit from A and instead benefits from M, because each M reduces the residual gap by `k+1` while costing one unmatched-slack unit.

The next theorem should exploit this antagonism together with the rooted unused-slot/Hamming ledger, rather than return to a total-score scalarization.

---

## 10. Diagnostic audit

The companion checker independently verifies `(HMIN)` against brute-force integer minimization and repeats the same coarse parameter scan used by the preceding minimal-reservoir diagnostic.

Starting from the 123,585 abstract `m=g+1` states that survived the preceding score minimization:

- the additive X+Y Hall score rejects **13,198**;
- **110,387** remain;
- in the `t=1` slice, 116 of the preceding 5,520 are rejected, leaving **5,404**.

On this bounded box, every state surviving the sharpened additive score has `sigma_P=P_0`; consequently the exact pair-capacity gate adds no further rejection there. This is diagnostic information only. It does not prove `(PAIR)` redundant in general. It says that, in this tested range, the physical Y/core score already supplies enough pair budget for the exact crossing demand.

The bounded states are not graph counts and survival is not realizability evidence.

---

## 11. Negative control

`X_3` has canonical-root `u=0`. The present branch requires `k>0`, one unmatched buffer, `u>=x+2`, and `m=g+1` outside unmatched witnesses. Therefore `X_3` never enters the hypotheses. Nothing in this package promotes the false all-order conjecture.

---

## 12. Frontier

The useful change is conceptual as well as numerical. The minimal reservoir is now governed by two competing physical defect currencies rather than a loose scalar score:

1. A-defects are the efficient way to relieve the X-Hall bill;
2. M-defects are the efficient way to relieve the rooted residual bill;
3. the outside pair P has an exact local score interval and exact crossing-capacity threshold;
4. `(CROWD)` and `(ONE-P)` are provably subordinate in this equality geometry once the stronger physical bills are present.

The next move should remain inside `m=g+1`: classify the low-`H` / low-`QE` intersection defined by `(MADM)` and `(QE-PAIR)`, then feed its forced A/M allocation into the unused rooted-slot/Hamming ledger. Only after that intersection is exhausted should `m=g+2` be opened.