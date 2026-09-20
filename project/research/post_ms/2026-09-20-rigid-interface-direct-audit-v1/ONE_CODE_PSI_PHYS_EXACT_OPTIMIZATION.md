# One-code rigid cut — exact optimization of the physical gamma/U obstruction

Date: 2026-09-20

Status: **same-session analytic theorem**, conditional on the rigid one-code interface and the hostile-replayed used-witness independence theorem. It optimizes the already-proved physical score floor; it does not assert graph-level reachability.

## 1. Physical score function

For `g0=p-y>=1`, the used-witness theorem gives

`E_W>=k_P(p+k_P-2)`,

where

`k_P=(x-g_P)_+`.

The gamma collision price is

`phi(g)=0` for `g<=2`,

`phi(g)=g(g-1)` for `g>=3`.

Therefore every one-code rigid candidate satisfies

> `Psi_phys(p,x)<=C0`,                                    `(PO-0)`

where

> `Psi_phys(p,x)=min_{0<=g<=p}`
> ` {phi(g)+(x-g)_+(p+(x-g)_+-2)}`.                      `(PO-1)`

The predecessor note introduced `(PO-1)` but did not optimize it.

## 2. Exact minimizer when x>=p

Assume `p>=3` and `x>=p`. Then `(x-g)_+=x-g` throughout `0<=g<=p`.

For `g=0,1,2`, the witness term strictly decreases with g, so g=2 is the best point in that range.

For `g>=3`, put

> `Q(g)=g(g-1)+(x-g)(p+x-g-2)`
>
> `    =2g^2-(p+2x-1)g+x(p+x-2)`.                       `(PO-2)`

This is a convex quadratic with real vertex

> `v=(p+2x-1)/4`.                                        `(PO-3)`

Hence the exact integer minimum is obtained by comparing only

- `g=2`, and
- the floor/ceiling of v after clipping to `[3,p]`.

Thus `Psi_phys` is a constant-time exact expression; no scan over g is mathematically necessary.

## 3. A parity-free lower envelope

The real minimum of Q is

`x(p+x-2)-(p+2x-1)^2/8`.

The only exceptional point is g=2, where `phi(2)=0` is two units below the quadratic continuation `g(g-1)=2`. Therefore, for every `p>=2`, `x>=p`,

> **`Psi_phys(p,x)`**
> **`>=x(p+x-2)-(p+2x-1)^2/8-2`.**                       `(PO-LB)`

This two-unit relaxation is convenient because it can be compared analytically with the exact above-M ceiling.

## 4. Substitute the rooted size identity

In the one-code large-gap parameterization,

`x=p+u-c`.

The present section treats

> `u>=c`,                                                 `(PO-U)`

so that `x>=p` and `(PO-LB)` applies.

Substitution gives

`8 Psi_phys >=`

> `4c^2-12cp-8cu+12c+7p^2+12pu-10p+4u^2-12u-17`.       `(PO-4)`

## 5. Uniform upper bound for C0

Recall

`lambda=p-y+c-1`,

`1<=y<=p-1`, and

`C0=(lambda+2)(p+u)+p-A_lambda`,

where

`A_lambda=floor(lambda^2/2)+lambda+4+(lambda mod 2)`.

Under `u>=c`, C0 is nondecreasing in lambda throughout the allowed range. Indeed

`A_{lambda+1}-A_lambda` is either `lambda+1` or `lambda+2`, while

`p+u>=p+c>=lambda+2`.

Therefore C0 is maximized at `y=1`, i.e.

`lambda_0=p+c-2`.

Using

`A_lambda>=lambda^2/2+lambda+4`

gives the safe uniform ceiling

> `C0 <=[-c^2+2cu+2c+p^2+2pu+4p-8]/2`.                  `(PO-CUP)`

## 6. Elliptic large-gap constraint

A survivor has `Psi_phys<=C0`. Combining `(PO-4)` and `(PO-CUP)` yields the necessary inequality

> **`3p^2+4pu+4u^2-12cp-16cu+8c^2`**
> **` -26p-12u+4c+15 <=0`.**                             `(PO-E)`

This has an exact completed-square form. Put

`R=p-c-5`,

`S=u-3c/2+1`.

Then `(PO-E)` is equivalent to

> **`3R^2+4RS+4S^2 <= 10c^2+40c+44`.**                   `(PO-ELL)`

Thus the physical witness-independence theorem compresses the entire `u>=c` large-gap region into an explicit ellipse around

`p approximately c+5`, `u approximately 3c/2-1`.

This is much sharper than the predecessor conservative bounds `p<=6c+4`, `u<4p+3c`.

## 7. Explicit coordinate and order bounds

The quadratic form in `(PO-ELL)` has matrix

`[[3,2],[2,4]]`

with inverse

`(1/8)[[4,-2],[-2,3]]`.

Writing

`K=10c^2+40c+44`,

Cauchy in this quadratic norm gives

> **`p <= c+5+sqrt(5c^2+20c+22)`,**                      `(PO-P)`
>
> **`u <= 3c/2-1+(1/2)sqrt(15c^2+60c+66)`.**             `(PO-U2)`

Since `lambda>=c`,

`n=4p+2u-lambda<=4p+2u-c`.

The linear functional `(4,2)` has dual quadratic norm squared `11/2`, so `(PO-ELL)` gives

> **`n <= 6c+18+sqrt(55c^2+220c+242)`**                  `(PO-N)`

throughout the `u>=c` branch.

Asymptotically this is

`n <= (6+sqrt(55))c+O(1)`,

with leading constant about 13.416 rather than the predecessor 77.

The theorem does **not** make c bounded; it proves that any surviving large-order family must keep c itself linear in n and confines the possible `(p/c,u/c)` ratios to a fixed ellipse.

## 8. Why the optimization does not yet close the branch

The ellipse has nonempty interior, so `(PO-N)` is still a gap-versus-order theorem, not a finite-order closure. In particular there are exact integer rays inside it. Private-coordinate exhaustion eliminates the naive boundary `d_U=c,m=p,k>0`, but the adjacent residual-dimension-one boundary survives the present scalar score package and must be attacked structurally.

That family is recorded in `ONE_CODE_POST_EXHAUSTION_ESCAPE_FAMILY.md`.

## 9. Evidence status

All displayed bounds are analytic. A companion diagnostic may replay them over finite boxes, but no finite box is used as proof. `X_3` remains the mandatory negative control and is not claimed to enter this rigid one-code interface.