# Strong repeated-code boundary wedge from singleton-coordinate repair pressure

Date: 2026-09-21

Status: exact/asymptotic necessary conditions inside the repeated rigid one-code `y>=2,m>=2` interface. This strengthens the earlier `(sqrt(71)-8)/7` wedge by inserting the raw singleton-coordinate extra-U bill proved in `ONE_CODE_BOUNDARY_EXTRA_U_TRADEOFF.md`. It remains conditional on reaching the rigid complete one-code interface.

## 1. Coordinates

Let `ell=|L|<=2`, `q=p-ell`, `d=e-q>=0`, and write the used boundary-witness population as

`|W|=q+a`, `0<=a<=d`.

The one-code identities are

`e=q+d`, `u=e+k=q+d+k`, `r=p-m`, `c=p+r-ell+d`,

and the standard exact relation `x=p+u-c`. Therefore

> **`x=p+k-r`.** `(1.1)`

Set `rho=r/p`, `beta=g0/p`, `delta=d/p`, `alpha=a/p`, `kappa=k/p`, and

> **`sigma=rho+beta+delta`.** `(1.2)`

Then `0<=alpha<=delta<=sigma`.

## 2. New asymptotic U-slack floor

The finite theorem in `ONE_CODE_BOUNDARY_EXTRA_U_TRADEOFF.md` is

`E_U >= (q+a)(g0+q+a-1)+yq`

`       + max{0,(q-a)(d+k-a)-x}+k(p-1)`.

Since `y=p-g0`, division by `p^2` gives, whenever `sigma<1`,

> **`E_U/p^2 >= F+o(1)`,** `(2.1)`

where

> **`F=2+delta+2kappa+alpha(1+beta-delta-kappa)+2alpha^2`.** `(2.2)`

## 3. Score ceiling

The preserved above-threshold score ceiling has normalized form

> **`S/p^2 <= U+o(1)`,** `(3.1)`

with

> **`U=(1+sigma)(2+delta+kappa)-(1+sigma)^2/2`.** `(3.2)`

Since `S>=E_U`, every unbounded survivor must satisfy `F<=U` asymptotically. Subtracting gives

> **`F-U = 1/2-sigma+sigma^2/2-delta sigma`**
>
> **`       +kappa(1-sigma-alpha)`**
>
> **`       +alpha(1+beta-delta)+2alpha^2`.** `(3.3)`

## 4. Universal forbidden neighborhood

Suppose `sigma<sqrt(2)-1`. Then `sigma<1/2`; because `0<=alpha<=delta<=sigma`, both `1-sigma-alpha` and `1+beta-delta` are positive. Thus alpha and kappa only worsen `(3.3)`. The most permissive choice is `alpha=kappa=0`; for fixed sigma the remaining expression is minimized by `delta=sigma`. Hence

> `F-U >= 1/2-sigma-sigma^2/2+o(1)`. `(4.1)`

This is positive exactly for `sigma<sqrt(2)-1`. Therefore every unbounded repeated one-code rigid survivor with `y>=2,m>=2` satisfies

> **`(r+g0+d)/p >= sqrt(2)-1-o(1)`**
>
> **`=0.4142135623...-o(1)`.** `(4.2)`

## 5. Exact finite inequality on the minimal-W face

When `a=0`, the full finite bill is

`E_U >= q(2p-ell-1)+q(d+k)-x+k(p-1)`.

Substitute `q=p-ell`, `x=p+k-r`, `u=p-ell+d+k`, `lambda=p+r+g0+d-ell-1` into the exact score ceiling

`E_U<=S<=C0=(lambda+2)(p+u)+p-A_lambda`

and use the preserved lower bound

`2A_lambda >= lambda^2+2lambda+8`.

A necessary condition for any finite minimal-W survivor is then

> **`0 >= N_min`,** `(5.1)`

where, writing `h=r+g0`,

> **`N_min = p^2-2p(d+h)-d^2+h^2`**
>
> **`       +2k(p-d-h-3)`**
>
> **`       +ell^2-2ell p+4ell`**
>
> **`       -2d+2r-10p+7`.** `(5.2)`

This is the finite antecedent of the asymptotic square-root threshold; no numerical scan is needed. In particular, when `k=0`, `ell=0` and `h=0`, it reduces to

> **`p^2-2pd-d^2-2d-10p+7<=0`,** `(5.3)`

whose leading root is exactly `d/p=sqrt(2)-1`. Thus the endpoint identified asymptotically is already visible in the exact integer score inequality, with only linear finite-size corrections.

## 6. Endpoint stability profile

Let a survivor sequence satisfy `sigma -> s0:=sqrt(2)-1`. Because the base lower bound tends to zero at `s0`, every nonnegative correction in `(3.3)` must also tend to zero. At `s0<1/2`, the coefficients of both kappa and alpha stay bounded away from zero. Hence

> **`alpha ->0`, `kappa->0`.** `(6.1)`

Moreover the base expression is minimized only when `delta=sigma`; therefore `delta-sigma->0`. Since `sigma=rho+beta+delta`,

> **`rho+beta ->0`.** `(6.2)`

Thus every asymptotically cheapest survivor is forced into the unique macroscopic profile

> **`d/p -> sqrt(2)-1`,**
>
> **`r/p ->0`, `g0/p ->0`, `k/p ->0`, `a/p ->0`.** `(6.3)`

The standard identities give

> **`u/p -> sqrt(2)`, `c/p -> sqrt(2)`, `lambda/p -> sqrt(2)`, `x/p ->1`, `y/p ->1`.** `(6.4)`

Using `n=4p+2u-lambda`,

> **`n/p ->4+sqrt(2)`.** `(6.5)`

Consequently

> **`c/n -> sqrt(2)/(4+sqrt(2))=(2sqrt(2)-1)/7 =0.261203874...`.** `(6.6)`

This is an equality-profile density, not a global c/n lower bound for every survivor.

## 7. Structural interpretation and trust boundary

Near equality, neither complementary selected witnesses nor boundary-service splitting can carry macroscopic mass. Almost all the necessary 41.42% escape is forced into extra forward-population d, while the used boundary witness set remains asymptotically minimal. The singleton-coordinate theorem then exposes a rectangular W-versus-extra-U hole block of asymptotic size `(sqrt(2)-1)p^2`, up to only linear X-certified repairs.

This remains a theorem inside the rigid one-code interface; it does not solve the zero-positive-fixture graph-level gap. The next high-value task is to feed the finite inequality and endpoint profile into the exact residual defect `delta=b(n-b)-m=r-e(F)` and rooted triangle count Q while maintaining X_3 and actual-graph regression. The old half-ray remains dead.
