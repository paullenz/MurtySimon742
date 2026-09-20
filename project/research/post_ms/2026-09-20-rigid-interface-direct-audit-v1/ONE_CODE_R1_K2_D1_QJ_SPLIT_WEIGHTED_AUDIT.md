# Residual-one k=2 D1 hub-split weighted audit

Date: 2026-09-20

Status: **same-session hostile replay and weighted refinement**, conditional on the residual-one k=2 low-ray package and `J2=empty`. No finite scan is used. This note corrects one accounting point in the predecessor reverse-spoke note and then optimizes the D1 hub split without promoting the conditional rigid interface.

## 1. Accounting correction: the `2v` H--W_s block is real but not new

The predecessor reverse-spoke theorem gives, for `T` the D1 vertices adjacent to `q_j`, reverse subset `T_R` of size `v`, and injective reverse heads `H_R`,

`Z_{H_R,T} >= v(|T|-1)`

and

`Z_{H_R,W_s} >= 2v`.

Both statements are correct. However the second block is **not incremental** in the global residual-one ledger. The already-preserved hub theorem gives

`N_A(z_h)={h}`

for every selected witness `z_h`. Since `H subset A_X\K`, every selected witness is already anticomplete to all of H. Therefore every pair in `H_R x W_s` already belongs to the baseline selected-witness X-hole bill.

> **Audit rule.** The genuinely new reverse D1 contribution is `v(|T|-1)` on `H_R--T`; do not add `2v` again on top of the residual-one selected-witness baseline.

This is a bookkeeping correction, not an invalidation of the predecessor structural theorem.

## 2. Forward D1 vertices have amplified U-slack

Let `R` be the K-heavy reservoir, `|R|=r`. A D1 vertex t is `W_s`-free and has exactly one K-neighbour. Write

- `alpha_t=|H\N(t)|`,
- `beta_t=|Y\N(t)|`,
- `gamma_t=|(E\{t})\N(t)|`.

The exact D1 sector identity is

`alpha_t+beta_t+gamma_t=p-3+epsilon_t`.                 `(DS-DEF)`

If t is a **forward** `q_j`-neighbour, the raw spoke theorem gives

`N_Y(t)=empty`, `E(t,R)=empty`.

Hence

`beta_t>=p-1`, `gamma_t>=r`.

Substituting into `(DS-DEF)` gives

> **`epsilon_t >= r+2`.**                                `(DS-FSLACK)`

Thus a forward D1 population `F` of size f simultaneously pays

`E_U(F)>=f(r+2)`,

`Z_Y(F)>=f(p-1)`,

`M_U(R,F)>=fr`.                                          `(DS-FBILL)`

These lie in three different physical currencies.

## 3. Exact D1 physical conversion

Let D be any D1 set of size d. Put

`A=Z_{H,D}`, `B=Z_{Y,D}`,

and let `Gamma=sum_{t in D} gamma_t`.

Summing `(DS-DEF)` gives

`A+B+Gamma=d(p-3)+E_D`.                                 `(DS-SUM)`

Every missing U--U pair represented in Gamma is counted at most twice, so the number `M_D` of distinct missing U--U pairs with at least one endpoint in D satisfies

`M_D>=Gamma/2`.

Consequently

`E_D+A+B+M_D`
` >= d(p-3)/2 + 3E_D/2 + (A+B)/2`.                     `(DS-PHYS)`

Since every escape has `epsilon>=2`,

> **`E_D+A+B+M_D >= d(p+3)/2+(A+B)/2`.**                `(DS-BASE)`

This is sharper than the predecessor coarse D-sector bill `d(p-2)/2` because it retains U-slack instead of discarding it.

## 4. Insert the forward/reverse q_j split

Write the D1 q_j-neighbour set as

`T=T_F disjoint_union T_R`,

with sizes f and v, and `tau=f+v`.

The forward theorem gives `B>=f(p-1)`. The reverse theorem gives the genuinely incremental block

`A>=v(tau-1)`.

Moreover `(DS-FSLACK)` raises the baseline D1 slack by at least `fr` over the universal `2d` floor. The forward R--D1 nonedges are also a literal U--U block `fr`. In the conversion `(DS-PHYS)`, those `fr` pairs would otherwise receive only the half-weight coming through `Gamma/2`; retaining them explicitly adds another `fr/2`. Altogether the forward amplification over `(DS-BASE)` is `2fr`.

Therefore

> **`D_phys(D;R) >= d(p+3)/2 + 2fr`**
> **`                 + f(p-1)/2 + v(tau-1)/2`,**       `(DS-MAIN)`

where the left side denotes the D1 U-slack plus its H/Y holes and its distinct U--U holes, including the R--F cross block.

No `2v` H--W_s term is included, by Section 1.

## 5. Asymptotic optimization forces the cheap D1 mass away from q_j

Normalize along an unbounded low-ray sequence:

`r/p -> alpha`, `d/p -> beta`, `f/p -> phi`, `v/p -> psi`,

and put `delta=phi+psi` for the q_j-neighbour D1 density.

Dividing `(DS-MAIN)` by `p^2`, the D1 contribution has lower envelope

`beta/2 + 2 alpha phi + phi/2 + psi delta/2`.

Equivalently, the extra price above the generic `beta/2` D1 sector floor is

> **`delta^2/2 + phi(2alpha+1/2-delta/2)`.**             `(DS-EXTRA)`

At the R+D1 endpoint, `delta<=beta<=1-alpha`. Hence

`2alpha+1/2-delta/2 >= (5/2)alpha >=0`.

For fixed alpha and delta the cheapest orientation is therefore `phi=0`: all q_j-neighbours reverse. Even then they pay

> **extra coefficient at least `delta^2/2`.**            `(DS-DELTA)`

Thus any sequence that approaches the predecessor additive lower envelope

`max{alpha^2/3,(1-alpha)/2}`

with no positive coefficient loss must satisfy

> **`delta=o(1)` in normalized terms:**
> **all but o(p) of the cheap D1 population are q_j-nonneighbours.** `(DS-NONHUB)`

This is the desired structural compression. The q_j-neighbour branch cannot realize the coarse additive optimizer at positive density.

## 6. Strategic consequence

The live cheap endpoint is now literal: a linear D1 population, almost all of whose vertices

- miss both selected witnesses,
- have exactly one K-neighbour,
- and miss the residual hub `q_j`.

The next attack should use their private-coordinate support in the matched layer, not another global partition scalar. The natural object is the set of private endpoints `q_i` seen by each such D1 vertex and the F/R orientation matrix for the corresponding `t q_i` spokes.

Global caveat unchanged: bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`; all statements here are conditional downstream mathematics pending independent hostile replay.