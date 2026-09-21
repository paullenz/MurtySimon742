# Strong repeated-code boundary wedge from singleton-coordinate repair pressure

Date: 2026-09-21

Status: asymptotic necessary condition inside the repeated rigid one-code `y>=2,m>=2` interface. This strengthens the earlier `(sqrt(71)-8)/7` wedge by inserting the raw singleton-coordinate extra-U bill proved in `ONE_CODE_BOUNDARY_EXTRA_U_TRADEOFF.md`. It remains conditional on reaching the rigid complete one-code interface.

## 1. Coordinates

Let `ell=|L|<=2`, `q=p-ell`, `d=e-q>=0`, and write the used boundary-witness population as

`|W|=q+a`, `0<=a<=d`.

The one-code identities are

`e=q+d`, `u=e+k=q+d+k`, `r=p-m`, `c=p+r-ell+d`,

and the standard exact relation `x=p+u-c`. Therefore

> **`x=p+k-r`.** `(1.1)`

Set

`rho=r/p`, `beta=g0/p`, `delta=d/p`, `alpha=a/p`, `kappa=k/p`,

and

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

## 5. Endpoint stability profile

The proof gives more than the numerical threshold. Let a survivor sequence satisfy

> `sigma -> s0:=sqrt(2)-1`.

Because the base lower bound in `(4.1)` tends to zero at `s0`, every nonnegative correction in `(3.3)` must also tend to zero. At `s0<1/2`, the coefficients of both kappa and alpha stay bounded away from zero. Hence

> **`alpha ->0`, `kappa->0`.** `(5.1)`

Moreover the base expression is minimized only when `delta=sigma`; therefore

> **`delta-sigma ->0`.** `(5.2)`

Since `sigma=rho+beta+delta` with all three terms nonnegative,

> **`rho+beta ->0`.** `(5.3)`

Thus every asymptotically cheapest survivor is forced into the unique macroscopic profile

> **`d/p -> sqrt(2)-1`,**
>
> **`r/p ->0`, `g0/p ->0`, `k/p ->0`, `a/p ->0`.** `(5.4)`

The standard identities then give

> **`u/p -> sqrt(2)`, `c/p -> sqrt(2)`, `lambda/p -> sqrt(2)`, `x/p ->1`, `y/p ->1`.** `(5.5)`

Using `n=4p+2u-lambda`,

> **`n/p ->4+sqrt(2)`.** `(5.6)`

Consequently the rooted-gap parameter has the endpoint density

> **`c/n -> sqrt(2)/(4+sqrt(2))=(2sqrt(2)-1)/7 =0.261203874...`.** `(5.7)`

This is not a global lower bound on `c/n` for every survivor: it describes the only asymptotic geometry that can approach equality in the new boundary wedge. It is nevertheless a sharp stability target for the next rooted-defect/Q replay.

## 6. Structural interpretation

The strong wedge does not use the independent global U-bound. Near equality, neither complementary selected witnesses nor boundary-service splitting can carry macroscopic mass. Almost all the necessary 41.42% escape is forced into **extra forward-population** `d`, while the used boundary witness set remains asymptotically minimal. In that geometry the singleton-coordinate theorem exposes a rectangular W-versus-extra-U hole block of asymptotic size `(sqrt(2)-1)p^2`, up to only linear X-certified repairs.

This is substantially narrower than the three-arm escape permitted by the earlier 6.09% wedge and supplies a concrete normal form for the rooted residual-defect attack.

## 7. Trust boundary and next test

This remains a theorem inside the rigid one-code interface; it does not solve the zero-positive-fixture graph-level gap. The next high-value tasks are: retain the linear `x=p+k-r` correction to derive a finite version of the wedge; then feed the endpoint profile and rectangular hole block into the exact residual defect `delta=b(n-b)-m=r-e(F)` and rooted triangle count Q. The old half-ray remains dead and should not be revisited.
