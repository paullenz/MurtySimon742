# Residual-one k=2 global coefficient with K-heavy Y-capacity

Date: 2026-09-20

Status: **same-session analytic synthesis**, conditional on the preserved k=2 class partition, F0 exception conservation, and K-heavy Y-edge witness-capacity theorem. No finite scan is used.

The predecessor additive partition bound `(7-sqrt(33))/8≈0.15693` did not retain the fact that only fully free F0 vertices can support many K-heavy--Y certificates. Keeping that physical capacity raises the global low-ray quadratic-defect coefficient substantially.

## 1. Partition

On the exact low-k ray partition the `p-1` escape vertices as

- R: K-heavy, size r;
- D: W_s-free but non-K-heavy, size d;
- T: F1 plus W-heavy, size theta;
- M: mixed, size m.

Inside D let F0 be the fully K/W_s-free class, size f. Thus `f<=d`.

Normalize

`r/p->alpha`, `d/p->delta`, `theta/p->vartheta`, `m/p->mu`, `f/p->phi`,

so asymptotically

`alpha+delta+vartheta+mu=1`, `0<=phi<=delta`.

Use the common physical functional

`D_phys=E_U+Z_X+Z_Y+M_U`.

## 2. First simultaneous lower bound: additive non-R sectors

The predecessor additive theorem gives

`D_phys >= d(p-2)/2 + theta(p-1+r)+m(p+1)`.

Hence

> **`liminf D_phys/p^2 >=`**
> **`L1:=delta/2+vartheta(1+alpha)+mu`.**                 `(GC-L1)`

For fixed alpha and phi, the cheapest destination for all remaining mass is D rather than T or M, because the D coefficient 1/2 is smaller than 1 and 1+alpha. Therefore any minimizer of the eventual max-bound may be taken with

`vartheta=mu=0`, `delta=1-alpha`,

which reduces `(GC-L1)` to

> `L1=(1-alpha)/2`.                                      `(GC-L1R)`

## 3. Second lower bound: R/F0 conservation plus located Y--R holes

The R/F0 coupled theorem remains valid in the presence of the other classes because none of them can repair K-heavy internal/Y edges:

- D1 and mixed vertices have a K-neighbour and fail the K-free witness requirement;
- F1 and W-heavy vertices touch W_s and are inert by the preserved orientation theorem.

Thus only F0 supplies exceptional K-heavy repair.

The R/F0 physical functional obeys asymptotically

> `D_RF/p^2 >= max{(alpha^2+phi)/3, phi/2}`.              `(GC-RF)`

Independently, the K-heavy Y-capacity theorem gives

`d_Y(w)<=max{1,f}`

for every K-heavy w. Since `|Y|=p-1`, this forces the located block

> **`Z_Y(R)/p^2 >= alpha(1-phi)-o(1)`.**                 `(GC-ZY)`

This block is disjoint from every currency in D_RF: D_RF uses R/F0 slack, H--R holes, F0 H/Y holes and F0-incident U holes, whereas `(GC-ZY)` consists only of Y--R pairs.

Therefore

> **`liminf D_phys/p^2 >=`**
> **`L2:=alpha(1-phi)+max{(alpha^2+phi)/3,phi/2}`.**      `(GC-L2)`

The two global bounds `(GC-L1)` and `(GC-L2)` are simultaneous, so

`liminf D_phys/p^2 >= max{L1,L2}`.

## 4. Exact minimization over the F0 density

For fixed alpha, compare

`A=(alpha^2+phi)/3`, `B=phi/2`.

One has `A>=B` exactly when `phi<=2alpha^2`.

### `0<=alpha<=1/3`

On the A-branch,

`L2=alpha+alpha^2/3+phi(1/3-alpha)`,

which is nondecreasing in phi. The B-branch cannot lower it. Hence the minimum is at

> `phi=0`, `L2=alpha+alpha^2/3`.                          `(GC-SMALL)`

### `1/3<alpha<1/2`

The A-branch decreases up to `phi=2alpha^2`, while the B-branch increases thereafter. Hence

`min_phi L2=alpha+alpha^2-2alpha^3`.

This is increasing on `[1/3,1/2]` and at alpha=1/3 equals `10/27≈0.37037`.

### `alpha>=1/2`

Here `1-alpha<=2alpha^2`, so the permitted interval remains on the A-branch and its coefficient of phi is negative. The minimum is at `phi=1-alpha`, giving

`min_phi L2=(4alpha^2-alpha+1)/3>=1/2`.

Therefore the global minimum below 10/27 must occur in the first regime with phi=0.

## 5. New global coefficient

For `0<=alpha<=1/3`, minimize

`max{(1-alpha)/2, alpha+alpha^2/3}`.

The two terms balance when

`2alpha^2+9alpha-3=0`,

so

> **`alpha_*=(sqrt(105)-9)/4≈0.3117377`.**               `(GC-ALPHA)`

The common value is

> **`tau_Y=(13-sqrt(105))/8≈0.3441312`.**                `(GC-TAU)`

Hence every asymptotic low-k configuration in the present class package satisfies

> **`liminf D_phys/p^2 >= (13-sqrt(105))/8`.**           `(GC-MAIN)`

This more than doubles the predecessor additive coefficient `0.15693`.

The relaxed minimizer has

- K-heavy density `alpha_*≈0.31174`;
- F0 density `phi=0`;
- all remaining mass placed in the cheap D class, density `≈0.68826`;
- no linear T or mixed population.

Since F0 vanishes at the new optimizer, the D mass must asymptotically be D1 rather than fully free. This is exactly the class attacked by the new hub/private-support/cross-code theorems.

## 6. Consequence and method boundary

The new coefficient still does not by itself contradict the existing coarse score/rooted ceilings; its value is a structural compression, not a final closure. But it changes the asymptotic target sharply:

> the only way to approach the new global envelope is a roughly 31:69 K-heavy/D1 reservoir with no linear F0 repair class.

That geometry activates additional theorems unavailable to the old relaxation:

- with no F0, K-heavy vertices have `d_Y<=1` literally;
- cheap D1 mass is pushed off q_j and toward sparse proper support;
- proper-support q_j-nonneighbours are globally independent in U;
- nonhub K-heavy vertices have at most two neighbours in that proper-support D1 set.

The next weighted optimization should therefore start from `(GC-ALPHA)` and retain the **location** of the D1 defect, especially its quadratic missing-U-edge block, rather than optimizing another unweighted total.

Global caveat unchanged: bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`; this remains conditional downstream mathematics.