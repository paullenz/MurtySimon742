# Integrated fan-hole profile and scorecard

Date: 2026-09-18

Status: internal structural theorem package for the eventual / sufficiently-large diameter-2-critical second-extremal programme around

`M(n)=floor((n-1)^2/4)+1`.

The purpose of this note is to integrate the bounded-hole fan capacities over *all* hole thresholds. The result is a fan analogue of the preserved integrated source-tuple deficit profile: global A-slack and beta-sensitive U-edge capacity impose a complete lower staircase on the local fan-hole mass.

No global eventual theorem is claimed.

## 1. Setup

Fix an A/U unique-common-neighbour fan with A-source `x`, distinct A-heads `h_i`, distinct witnesses `w_i in A union U`, and order

`d=|H_x|=|W_x|`.

As before,

`N(x) intersect N(w_i)={h_i}`,

all witnesses have Boolean code `bar(c(x))`, and the head-witness cross graph is exactly the matching `h_iw_i`.

Put

`Z_i=V(G)\({x,w_i} union N(x) union N(w_i))`,

`g_i=|Z_i|=epsilon_x+epsilon_{w_i}-(lambda+1)`,

and

`G_x=sum_i g_i`.

Globally write

`S=E_U+L_A`,

`V_0=a+u`,

`Q_beta=au-B_beta+N_1`,

where the preserved beta-sensitive theorem gives

`q<=Q_beta`.

Assume `lambda+1>0`, as in the live near-full branch in which the same-code weighted edge capacity is used.

## 2. Low-hole counting function

For every integer `K>=0`, define

`N_K=|{i:g_i<=K}|`.

The preceding bounded-hole theorem applies to the subfan formed by any chosen subset of witnesses and their matched heads.

For `K=0`, A-witnesses are impossible because the root `v` is always an external hole of an A-witness pair. The zero-hole witnesses therefore lie in `U` and form a clique. Since `q<=Q_beta`, put

> `C_0=floor((1+sqrt(1+8Q_beta))/2)`.                    `(C0)`

Then

> `N_0<=C_0`.                                             `(LH0)`

For every integer `K>=1`, put

> `R_A(K)=`
> ` floor((K+sqrt(K^2+8V_0S/(lambda+1)))/2)`,             `(RAK)`
>
> `R_U(K)=`
> ` floor(((K+1)+sqrt((K+1)^2+8Q_beta))/2)`,              `(RUK)`
>
> `C_K=R_A(K)+R_U(K)`.                                    `(CK)`

The bounded-hole A/U capacity theorem gives

> `N_K<=C_K`                                              `(LHK)`

for every `K>=1`.

Thus the entire empirical distribution of fan-hole sizes is constrained by the global scorecard and beta-sensitive U-edge budget.

## 3. Integrated fan-hole profile

Define the finite staircase functional

> `Psi_hole(d;S,Q_beta)`
> ` := sum_{K>=0} (d-C_K)_+`,                             `(PSI)`

where `C_0` is given by `(C0)` and `C_K` for `K>=1` by `(CK)`.

The sum is finite because `C_K>=d` for all sufficiently large `K`.

### Theorem 3.1 — integrated fan-hole profile

Every A/U fan satisfies

> `G_x >= Psi_hole(d;S,Q_beta)`.                          `(IFHP)`

Proof. Since every `g_i` is a nonnegative integer,

`G_x=sum_i g_i`

`   =sum_{K>=0}|{i:g_i>=K+1}|`

`   =sum_{K>=0}(d-N_K)`.

For every `K`, `(LH0)/(LHK)` give

`d-N_K >= (d-C_K)_+`.

Summing proves `(IFHP)`. square

This is the exact layer-cake analogue of the integrated source-tuple deficit profile. It is stronger than choosing one bounded-hole threshold in isolation.

## 4. Quantile form

Order the hole sizes

`g_(1)<=g_(2)<=...<=g_(d)`.

The low-hole capacities give the equivalent quantile statement:

> if `j>C_K`, then `g_(j)>=K+1`.                          `(QNT)`

Hence a fan larger than the combined A-clique/U-near-clique capacity cannot merely contain one exceptional large-hole witness; an entire upper tail of witnesses is forced to have progressively larger hole surplus.

This is the correct stability interpretation of `(IFHP)`.

## 5. From hole mass to witness slack

The exact hole identity gives

`G_x=d epsilon_x+sum_i epsilon_{w_i}-d(lambda+1)`.

The source `x` is adjacent to all `d` distinct A-heads. Since an A-vertex has exactly

`d_{A union U}(x)=p+u-epsilon_x`

neighbours in the coded layer,

> `epsilon_x<=p+u-d`.                                     `(SRC)`

Recall

`T=p+u-lambda-1=a-p`.

Therefore

`lambda+1-epsilon_x >= d-T`,

and `(IFHP)` yields:

### Theorem 5.1 — integrated witness-slack floor

> `sum_i epsilon_{w_i}`
> ` >= Psi_hole(d;S,Q_beta)+d(d-T)`.                      `(IWS)`

The right side may be negative when `d<T`; of course the actual witness-slack sum is nonnegative, so the useful form is

> `sum_i epsilon_{w_i}`
> ` >= [Psi_hole(d;S,Q_beta)+d(d-T)]_+`.                  `(IWS+)`

This theorem says that once the low-hole witness reservoirs are exhausted, the fan must pay directly in witness degree deficit.

## 6. Strengthened fan scorecard

The preserved induced-matching fan theorem gives, for every head,

`epsilon_{h_i}>=(d-T)_+`.

The head and witness sets are disjoint. Hence their slack contributions can be added inside the global scorecard `S=E_U+L_A`.

### Theorem 6.1 — integrated fan-scorecard inequality

Every A/U fan satisfies

> `S`
> ` >= d(d-T)_+`
> `    +[Psi_hole(d;S,Q_beta)+d(d-T)]_+`.                 `(IFSC)`

In particular, if `d>T`, then

> `S >= Psi_hole(d;S,Q_beta)+2d(d-T)`.                   `(IFSC+)`

The old local fan inequality was only

`S>=2d(d-T)_+`.

Thus the integrated hole staircase contributes the additional positive term `Psi_hole` whenever the fan is above the outside-capacity threshold.

When `d<=T`, `(IFSC)` still gives the nontrivial condition

> `S >= [Psi_hole(d;S,Q_beta)-d(T-d)]_+`.                 `(IFSC-)`

A sufficiently large integrated hole deficit can therefore price a fan even below the old quadratic threshold.

## 7. A parameter-only fan admissibility test

All quantities on the right of `(IFSC)` are determined by

`d,p,u,lambda,S,B_beta,N_1`.

Consequently, for fixed global parameters, define

`R_int`

as the largest integer `d` satisfying `(IFSC)`.

Then every A/U certificate fan has

> `d<=R_int`.                                             `(RIC)`

This may be inserted directly into the rooted-transfer fan dichotomy in place of the older maximum-fan bound `R_C(T,S)`.

If

`H=(F_min-sigma_0a)_+`,

then the A/U branch requires

> `R_int>=ceil(H/(2a))`.                                  `(IRTF)`

Failure of `(IRTF)` forces the rooted-transfer mass into the direct-fan branch; if the direct fan is separately excluded by the false-twin quotient theorem, the candidate itself is excluded.

## 8. Asymptotic interpretation

The new profile clarifies what a hypothetical linear fan must do in a low-budget slice.

If for every fixed `K`

`R_A(K)+R_U(K)=o(p)`

while `d=alpha p+o(p)`, then for each fixed `K`

`N_K=o(p)`.

Thus almost every witness has `g_i>K`. Since `K` is arbitrary fixed,

> the typical fan-hole surplus tends to infinity.        `(DIV)`

This is stronger than the earlier statement that a fixed-`K` fan is impossible: the fan's hole distribution must itself escape to infinity.

If the profile remains low for many growing thresholds, `(IFHP)` converts that escape directly into a superlinear lower bound for `G_x`, and `(IWS)/(IFSC)` then convert it into scorecard consumption.

This is the natural bridge from local equality stability to residual-defect closure.

## 9. Scope and negative control

The published order-12, size-32 graph `X_3` remains untouched. At its canonical root `u=0` and the rooted-transfer floor is `F_min=0`, so no positive A/U fan is forced.

The theorem is conditional on the live partial-Boolean near-full setup and on one chosen A/U fan. It does not assert the false all-order 2019 conjecture or a complete eventual theorem.

## 10. Next move

The highest-value next calculation is to evaluate `(IFSC)/(IRTF)` against the exact above-threshold scorecard for the surviving parameter regimes, using the *forced* beta lower bounds rather than treating `B_beta` as free.

If that still leaves a branch, the quantile form `(QNT)` identifies its geometry: a linear fan must carry a growing tail of high-hole witnesses. The exact identity

`g_i=epsilon_x+epsilon_{w_i}-(lambda+1)`

then says that the tail must be paid by witness slack unless the single source `x` itself has very large slack; the source degree bound `(SRC)` limits that escape.
