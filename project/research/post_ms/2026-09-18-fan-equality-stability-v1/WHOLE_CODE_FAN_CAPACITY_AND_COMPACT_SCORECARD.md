# Whole-code fan capacity and compact scorecard

Date: 2026-09-18

Status: internal structural theorem package for the eventual / sufficiently-large diameter-2-critical second-extremal programme around

`M(n)=floor((n-1)^2/4)+1`.

No global eventual theorem is claimed.

## 1. Why this note

The preceding bounded-hole analysis split an A/U fan into A-witnesses and U-witnesses and paid those two pieces from different reservoirs. That split is valid but loses a stronger fact already present in the preserved code machinery:

> **every witness in one A/U fan has the same Boolean code.**

Therefore the preserved same-code weighted edge capacity applies to the *entire* witness graph, including A-A, A-U and U-U witness edges simultaneously. This gives a substantially cleaner whole-code fan theorem and a sharper hole profile.

The new argument does not replace the beta-sensitive `q` information; it combines with it.

## 2. Setup and the exact code-pair edge budget

Fix one A/U unique-common-neighbour fan with A-source `x`, distinct A-heads `h_i`, distinct witnesses `w_i in A union U`, and order

`d=|H_x|=|W_x|`.

Write

`c=c(x)`.

Every witness has code `bar(c)`. Put

`V_gamma={z in A union U:c(z)=gamma}`,

`N_gamma=|V_gamma|`,

`S_gamma=sum_{z in V_gamma} epsilon_z`,

and `S=E_U+L_A=sum_gamma S_gamma`.

The preserved same-code weighted edge capacity is

`(lambda+1)e(G[V_gamma])`
` <= N_bar(gamma) S_gamma + N_gamma S_bar(gamma)`.       `(SCE)`

Assume `lambda+1>0`, as in the live branch.

For the complementary pair containing `c`, define the integer edge budget

> `E_x = floor((N_c S_bar(c)+N_bar(c) S_c)/(lambda+1))`. `(EX)`

Since `W_x subseteq V_bar(c)`, `(SCE)` gives

> `e(G[W_x]) <= E_x`.                                     `(EW)`

With `V_0=a+u`, the distribution-free bound is

> `E_x <= E_0 := floor(V_0 S/(lambda+1))`.                `(E0)`

The exact fan-hole notation remains

`Z_i=V(G)\({x,w_i} union N(x) union N(w_i))`,

`g_i=|Z_i|=epsilon_x+epsilon_{w_i}-(lambda+1)`,

`G_x=sum_i g_i`.

The preserved witness normal form gives

> `2e(overline{G[W_x]}) <= G_x`.                          `(EWM)`

## 3. Aggregate whole-code hole floor

Because

`e(overline{G[W_x]})=binom(d,2)-e(G[W_x])`,

`(EW)/(EWM)` immediately give:

### Theorem 3.1 — whole-code aggregate hole floor

> `G_x >= [d(d-1)-2E_x]_+`.                              `(WCHF)`

Coarsely,

> `G_x >= [d(d-1)-2E_0]_+`.                              `(WCHF0)`

This is the first point at which the A/U witness-type split disappears completely. If a same-code witness set is too large for its complementary-pair slack budget, the deficit is paid directly as fan-hole mass.

## 4. Low-hole witnesses see the entire fan

For integer `K>=0`, put

`I_K={i:g_i<=K}`,

`N_K=|I_K|`,

and let `A_K` be the number of witnesses in `I_K` that lie in `A`.

Every `w_i` with `i in I_K` has at most `K` non-neighbours inside the *whole* witness set `W_x`. If `w_i in A`, the root `v` is one of its holes and does not lie in `W_x`, so it has at most `K-1` witness non-neighbours.

Therefore

`sum_{i in I_K} d_{G[W_x]}(w_i)`
` >= N_K(d-1-K)+A_K`.

The left side is at most `2e(G[W_x])<=2E_x`. Hence:

### Theorem 4.1 — whole-fan low-hole incidence bound

> `N_K(d-1-K)+A_K <= 2E_x`.                              `(WFHI)`

This is stronger than applying a bounded-hole theorem only to the induced low-hole subfan: every low-hole witness must be adjacent to almost all `d` witnesses, including the high-hole ones.

### Uniform bounded-hole corollary

If every witness satisfies `g_i<=K`, and `d_A=|W_x intersect A|`, then

> `d(d-1-K)+d_A <= 2E_x`.                                `(UBH)`

In particular,

> `d(d-1-K) <= 2E_x <= 2E_0`.                            `(UBH0)`

Thus the previous split cap `d<=R_A(K)+R_U(K)` is supplemented by a single whole-code quadratic constraint on the total fan.

## 5. Reinsert the beta-sensitive U-edge budget

Let

`Q_beta=au-B_beta+N_1`,

so the preserved beta-sensitive theorem gives `q<=Q_beta`.

Among the low-hole witnesses, put

`U_K=|I_K intersect U|`.

Inside `I_K intersect U`, every vertex has at most `K` missing U-witness edges. Therefore

`U_K(U_K-K-1) <= 2q <= 2Q_beta`.

Define

> `R_U(K)=max{r>=0:r(r-K-1)<=2Q_beta}`.                   `(RUK)`

Equivalently,

`R_U(K)=floor(((K+1)+sqrt((K+1)^2+8Q_beta))/2)`.

For `K>=1`,

`A_K=N_K-U_K >= (N_K-R_U(K))_+`.

Combining with `(WFHI)` gives:

### Theorem 5.1 — whole-code / beta hybrid low-hole cap

For `K>=1`,

> `N_K(d-1-K)+(N_K-R_U(K))_+ <= 2E_x`.                  `(HBH)`

When `0<=K<=d-2`, put `t=d-1-K>0`. Then `(HBH)` is equivalent to the two linear inequalities

`N_K t <= 2E_x`,

`N_K(t+1) <= 2E_x+R_U(K)`.

Hence

> `N_K <= C_x(K;d)`,                                      `(CX)`

where

> `C_x(K;d)=min{`
> ` d,`
> ` floor(2E_x/(d-1-K)),`
> ` floor((2E_x+R_U(K))/(d-K))`
> `}`.                                                     `(CXF)`

For `K=0`, A-witnesses are impossible because the root is always an external hole. Thus

> `N_0 <= min{d,R_U(0),floor(2E_x/(d-1))}`               `(CX0)`

when `d>=2`.

This is the sharper replacement for the recent independent-reservoir picture. Low-hole A and U witnesses do not merely consume separate budgets: together they must fit inside one same-code witness graph.

## 6. Strengthened integrated fan-hole profile

Let `C_K^old` denote the preserved capacities from `INTEGRATED_FAN_HOLE_PROFILE_AND_SCORECARD.md`.

For `0<=K<=d-2`, define

> `C_K^sharp(d)=min(C_K^old,C_x(K;d))`,                   `(CSH)`

with `(CX0)` at `K=0`. For `K>=d-1`, retain `C_K^old`.

Define

> `Psi_sharp(d)=sum_{K>=0}(d-C_K^sharp(d))_+`.            `(PSH)`

The sum is finite. Layer cake gives

> `G_x >= Psi_sharp(d)`.                                  `(IFHP+)`

Since `C_K^sharp<=C_K^old`, this dominates the preceding integrated profile. The aggregate whole-code floor is independent information, so put

> `Gamma_x(d)=max{`
> ` 0,`
> ` d(d-1)-2E_x,`
> ` Psi_sharp(d)`
> `}`.                                                     `(GAM)`

Then

> `G_x >= Gamma_x(d)`.                                    `(GF)`

The value of retaining both terms is structural: `d(d-1)-2E_x` is the strongest cheap aggregate consequence, while `Psi_sharp` records how the hole mass must be distributed among witnesses.

## 7. Strengthened fan scorecard

Put

`P=p+u`,

`T=P-lambda-1=a-p`.

The source-degree bound is

> `epsilon_x<=P-d`.                                       `(SRC)`

The exact hole identity gives

`sum_i epsilon_{w_i}`
` =G_x+d(lambda+1-epsilon_x)`
` >=G_x+d(d-T)`.

The heads satisfy the preserved bound

`sum_i epsilon_{h_i}>=d(d-T)_+`.

The head and witness sets are disjoint. Therefore:

### Theorem 7.1 — whole-code strengthened fan scorecard

> `S`
> ` >= d(d-T)_+`
> `   +[Gamma_x(d)+d(d-T)]_+`.                            `(WCSC)`

This strictly contains the information in the old local inequality `S>=2d(d-T)_+` and strengthens the preceding integrated fan scorecard whenever the whole-code term or the hybrid low-hole term is active.

A distribution-free version follows by replacing `E_x` with `E_0` and retaining the old/beta caps in `Psi_sharp`.

## 8. Compact finite fan inequalities

There is also a useful closed form that avoids the staircase.

Because the source `x` and all witnesses are distinct vertices of `A union U`,

`epsilon_x+sum_i epsilon_{w_i}<=S`.

Hence

`G_x`
` =d epsilon_x+sum_i epsilon_{w_i}-d(lambda+1)`
` <=S+(d-1)epsilon_x-d(lambda+1)`
` <=S+(d-1)(P-d)-d(lambda+1)`.

Combine this with `(WCHF)`.

### Theorem 8.1 — compact whole-code fan capacity

Every A/U fan satisfies

> `2d^2-(T+2)d+P <= S+2E_x`.                              `(CFC)`

Coarsely,

> `2d^2-(T+2)d+P <= S+2E_0`.                             `(CFC0)`

Thus, if

`Delta_f=(T+2)^2-8P+8S+16E_x`,

then any feasible fan must have `Delta_f>=0` and

> `d <= floor((T+2+sqrt(Delta_f))/4)`.                    `(CFCR)`

This is useful precisely below the old threshold `d>T`, where `2d(d-T)_+` is silent.

### Complement-pair local form

Since all witnesses lie in `V_bar(c)`,

`sum_i epsilon_{w_i}<=S_bar(c)`.

Without replacing `epsilon_x`, `(WCHF)` therefore gives the stronger source-local statement

> `d(d+lambda-epsilon_x) <= S_bar(c)+2E_x`.              `(PFC)`

Using `epsilon_x<=P-d`,

> `2d^2-(T+1)d <= S_bar(c)+2E_x`.                        `(PFC2)`

This identifies the next bottleneck cleanly: a large low-hole A/U fan must concentrate substantial slack in the *same complementary code pair* that contains its source and witnesses.

## 9. Rooted-transfer consequence

Above `M(n)`, rooted triangles force

`f>=F_min=(p-lambda)(p+u)+q-D_M+1`.

After the matched-B allowance, put

`H=(F_min-sigma_0a)_+`.

The preserved fan gate says that either a direct fan has order at least `H/a`, or an A/U fan has order at least `ceil(H/(2a))`.

Define `R_whole` as the largest integer `d` satisfying `(WCSC)` (or, more cheaply, `(CFC0)`) with the candidate's global parameters. Then the A/U branch requires

> `R_whole >= ceil(H/(2a))`.                              `(WRTF)`

Failure forces the rooted-triangle transfer mass into the direct-fan / false-twin branch.

This is a direct bridge from the residual target `delta>=D_M` to one compact whole-code fan obstruction.

## 10. Critical reassessment

The recent A/U split was useful for discovering the one-hole and bounded-hole geometry, but it should no longer be the primary capacity model. Once all witnesses are recognized as one Boolean code class, the correct hierarchy is:

1. exact complementary-pair same-code edge budget `E_x`;
2. whole-code aggregate hole floor `(WCHF)`;
3. beta-sensitive low-hole refinement `(HBH)/(CX)`;
4. strengthened scorecard `(WCSC)`;
5. rooted fan gate `(WRTF)`.

A deliberately conservative parameter scan using only the *global maximum* above-threshold scorecard does not by itself close the remaining branch; the global allowance can make `E_0` too large. That is a useful obstruction: the next gain should come from `(PFC)`, i.e. proving that the forced fan cannot place enough of the global slack into its one complementary code pair, rather than from another distribution-free optimization of `E_0`.

The direct fan branch remains separate and should be attacked through its false-twin/common-side sparsity theorem and the rooted count `Q=e(G[B])`.

## 11. Scope and negative control

The published order-12, size-32 graph `X_3` remains untouched. At its canonical root `u=0`, `F_min=0`, so no positive rooted A/U fan is forced.

Nothing here asserts the false all-order 2019 conjecture. The statements are internal structural theorems inside the live near-full partial-Boolean setup.
