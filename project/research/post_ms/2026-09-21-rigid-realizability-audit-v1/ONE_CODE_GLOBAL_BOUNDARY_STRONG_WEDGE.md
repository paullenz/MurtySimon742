# Strong repeated-code boundary wedge from singleton-coordinate repair pressure

Date: 2026-09-21

Status: asymptotic necessary condition inside the repeated rigid one-code `y>=2,m>=2` interface. This strengthens the earlier `(sqrt(71)-8)/7` wedge by inserting the raw singleton-coordinate extra-U bill proved in `ONE_CODE_BOUNDARY_EXTRA_U_TRADEOFF.md`. It remains conditional on reaching the rigid complete one-code interface.

## 1. Coordinates

Let `ell=|L|<=2`,

`q=p-ell`,

`d=e-q>=0`,

and write the used boundary-witness population as

`|W|=q+a`, `0<=a<=d`.

The one-code identities are

`e=q+d`,

`u=e+k=q+d+k`,

`r=p-m`,

`c=p+r-ell+d`,

and the standard exact relation

`x=p+u-c`.

Therefore, importantly,

> **`x=p+k-r`.** `(1.1)`

So x is only linear in p throughout an asymptotic normalization and the `-x` correction in the singleton rectangular bill is lower order compared with a genuinely quadratic rectangle.

Set

`rho=r/p`, `beta=g0/p`, `delta=d/p`, `alpha=a/p`, `kappa=k/p`,

and

> **`sigma=rho+beta+delta`.** `(1.2)`

Then `0<=alpha<=delta<=sigma`.

## 2. New asymptotic U-slack floor

The finite theorem in `ONE_CODE_BOUNDARY_EXTRA_U_TRADEOFF.md` is

`E_U >= (q+a)(g0+q+a-1)+yq`

`       + max{0,(q-a)(d+k-a)-x}+k(p-1)`.

Since `y=p-g0`, dividing by `p^2` and letting p tend to infinity gives, whenever `sigma<1` (hence `alpha<1`),

> **`E_U/p^2 >= F+o(1)`,** `(2.1)`

where

`F=(1+alpha)(1+beta+alpha)+(1-beta)+kappa`

`  +(1-alpha)(delta+kappa-alpha)`

and therefore

> **`F=2+delta+2kappa+alpha(1+beta-delta-kappa)+2alpha^2`.** `(2.2)`

The rectangular term is valid even when the extra U-population is complementary-code: singleton coordinate witnesses are Y-anticomplete, so every physical edge from such a witness to any extra U-vertex must use the fixed X-forward class.

## 3. Score ceiling

The preserved above-threshold score ceiling, in the same normalization used in the earlier global wedge, is

> **`S/p^2 <= U+o(1)`,** `(3.1)`

with

> **`U=(1+sigma)(2+delta+kappa)-(1+sigma)^2/2`.** `(3.2)`

Since `S>=E_U`, every unbounded survivor must satisfy

`F<=U` asymptotically.

Subtracting gives

> **`F-U = 1/2-sigma+sigma^2/2-delta sigma`**
>
> **`       +kappa(1-sigma-alpha)`**
>
> **`       +alpha(1+beta-delta)+2alpha^2`.** `(3.3)`

## 4. Universal forbidden neighborhood

Suppose

> **`sigma<sqrt(2)-1`.**

Then in particular `sigma<1/2`. Because `0<=alpha<=delta<=sigma`,

`1-sigma-alpha >= 1-2sigma >0`,

and

`1+beta-delta > 1-sigma >0`.

Thus every term in the second and third lines of `(3.3)` is nonnegative. The most permissive choice is therefore

`kappa=0`, `alpha=0`.

For fixed sigma, the remaining expression

`1/2-sigma+sigma^2/2-delta sigma`

is minimized by the largest allowed `delta`, namely `delta=sigma`. Hence

> `F-U >= 1/2-sigma-sigma^2/2+o(1)`. `(4.1)`

The right side is positive exactly when

`sigma^2+2sigma-1<0`,

that is when

`sigma<sqrt(2)-1`.

Therefore:

> **Strong repeated-code boundary wedge.** Every unbounded repeated one-code rigid survivor with `y>=2,m>=2` satisfies
>
> **`(r+g0+d)/p >= sqrt(2)-1-o(1)`**
>
> **`=0.4142135623...-o(1)`.** `(4.2)`

This replaces the earlier 6.09% necessary wedge by a 41.42% wedge.

## 5. Why the optimum is structurally meaningful

The proof does not invoke the independent global U-bound at all. In the entire forbidden range `sigma<sqrt(2)-1`, adding complementary selected witnesses (`kappa>0`) only worsens the score because their gain in the score ceiling is outweighed by the selected-witness bill and the singleton repair rectangle. Likewise splitting boundary service among extra physical W-witnesses (`alpha>0`) only worsens the score in this range.

The cheapest hypothetical escape is therefore forced toward

`alpha=0`, `kappa=0`, `delta=sigma`, `rho=beta=0`,

at the endpoint `sigma=sqrt(2)-1`.

In words: the extremal pressure now pushes the survivor toward a pure forward-population-excess direction, with minimal boundary-witness multiplicity and no complementary selected U-witness density. That is a much narrower geometry than the three-arm escape permitted by the previous global wedge.

## 6. Trust boundary and next test

This remains a theorem **inside** the rigid one-code interface; it does not solve the zero-positive-fixture graph-level gap. The next high-value task is hostile replay of the singleton-coordinate rectangle and then a finite/exact version of `(4.2)` with the linear `x=p+k-r` correction retained. After that, feed the 41.4% gap into the exact residual-defect and rooted-Q ledger rather than returning to the dead half-ray.
