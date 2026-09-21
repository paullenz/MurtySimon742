# Rooted-Q feedback from the singleton boundary rectangle

Date: 2026-09-21

Status: same-session theorem inside the repeated rigid complete one-code interface `y>=2,m>=2`. It strengthens `ONE_CODE_GLOBAL_BOUNDARY_STRONG_WEDGE.md`. It remains conditional on reaching that interface; bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`.

## 1. Variables and inherited raw facts

Use the corrected boundary notation

- `ell=|L|<=2`, `q=p-ell`;
- `d=e-q>=0`, `|W|=q+a`, `0<=a<=d`;
- `W0` = singleton-coordinate used U-forward witnesses, so `|W0|>=q-a`;
- `R=U\W`, `h=|R|=d+k-a`;
- `r=p-m`, `x=p+k-r`, `y=p-g0`;
- `sigma=(r+g0+d)/p`, `rho=r/p`, `beta=g0/p`, `delta=d/p`, `alpha=a/p`, `kappa=k/p`.

The raw boundary theorem gives:

1. `G[W]` is independent;
2. every `w in W0` is X-anticomplete and Y-anticomplete;
3. every edge from `W0` to `R` must use a coordinate-specific X witness, hence

   `e(W0,R)<=x`.

These facts do not use the finite source-tuple capacity theorem, the independent global-U bound, or the superseded H-U private-foot chain.

## 2. Located rectangle and U-triangle ceiling

Because `|W\W0|<=2a`,

`e(G[U]) <= e(W0,R)+e(W\W0,R)+binom(h,2)`

and therefore

> **`q_U:=e(G[U]) <= x+2ah+binom(h,2)`.**        `(RQ-1)`

Moreover each vertex of `W0` is nonadjacent to every X- and Y-vertex, so for the rooted A-U nonedge count Z,

> **`Z >= |W0|(x+y) >= (p-ell-a)(x+y)`.**        `(RQ-2)`

The matched-head collision floor remains

> `L_A >= phi(p-r)`, with `phi(t)=t(t-1)` for `t>=3`.

Using the exact rooted identity

`Z=u(p-lambda)+2q_U+E_U`

and the score ceiling

`E_U+L_A<=C0`,

every finite survivor satisfies

> **`(p-ell-a)(x+y)+phi(p-r)`**
>
> **` <= u(p-lambda)+2x+4a(d+k-a)+(d+k-a)(d+k-a-1)+C0`.**   `(RQ-3)`

This is the key new physical feedback inequality.

## 3. Normalized gap

Ignoring only `O(1/p)` terms and writing `delta=sigma-rho-beta`, the old score gap is

`D = B(sigma)+sigma(rho+beta)+kappa(1-sigma-alpha)`

`    +alpha(1+beta-delta)+2alpha^2`,

where

`B(sigma)=1/2-sigma-sigma^2/2`.

The normalized left-minus-right gap of `(RQ-3)` is

`G=(1-alpha)(2+kappa-rho-beta)+(1-rho)^2`

`  +(1+delta+kappa)sigma-4alpha(delta+kappa-alpha)`

`  -(delta+kappa-alpha)^2-U`,

with

`U=(1+sigma)(2+delta+kappa)-(1+sigma)^2/2`.

Every asymptotic survivor needs simultaneously

> `D<=0` and `G<=0`.                                      `(RQ-4)`

At the former strong-wedge endpoint `sigma=delta=sqrt(2)-1`, `rho=beta=alpha=kappa=0`, one has exactly

> **`G=1`.**

Thus the old `sqrt(2)-1` endpoint is excluded with constant margin once the located rectangle is fed into rooted Q.

## 4. Exact endpoint reduction

For `sigma<1`, fix `t=rho+beta`. Replacing beta by rho while keeping t fixed decreases D (by alpha per unit transferred) and decreases G because

`partial G / partial rho |_(t fixed) = 2rho-2 <0`.

Hence a minimizing survivor may be taken with

> **`beta=0`.**                                           `(RQ-5)`

With beta zero and `alpha<=delta=sigma-rho`,

`partial G/partial kappa = -3alpha-2kappa+2rho-2sigma <= -5alpha-2kappa <=0`.

Whenever `1-sigma-alpha>0`, a minimizer therefore exhausts the score budget `D=0`. On that affine line, kappa is affine in rho and direct differentiation gives

> **`d^2G/drho^2 = 2(alpha+sigma)(alpha+sigma-2)/(1-alpha-sigma)^2 <0`.** `(RQ-6)`

So the minimum lies at an endpoint: `rho=0`, `kappa=0`, or the physical truncation `rho=sigma-alpha`. The latter is impossible, because already at `kappa=0`

> `D=(1-sigma)^2/2+alpha(1-sigma)+alpha^2>0`.              `(RQ-7)`

Thus only two one-variable endpoint families remain.

## 5. Clean 0.53 barrier

Assume `sqrt(2)-1 <= sigma <= 0.53`. Score feasibility implies

`alpha<0.198`, hence `1-sigma-alpha>0.272`, so the reduction above is valid.

### 5.1 rho=0 endpoint

Eliminate kappa with `D=0`. Apart from a positive denominator, G has numerator

`N_A=-28a^4+(4s-36)a^3+(8s^2-8s+28)a^2`

`    +(2s^3-2s^2+26s-18)a+s^4-2s^2-8s+5`,

where `s=sigma` and `a=alpha`.

Its s-derivative is

`4a^3+(16s-8)a^2+(6s^2-4s+26)a+4s^3-4s-8`.

On `s in [sqrt(2)-1,0.53]`, `a in [0,0.198]`, this is bounded above by

`-9.3725+5.0620+0.0189+0.0311 < -4.26`.

Hence the worst s is `0.53`. There

`N_A=0.27710481-4.484046a+26.0072a^2-33.88a^3-28a^4`.

For `0<=a<=0.12`, the last two terms are at least `-4.4688a^2`, leaving a quadratic whose minimum is greater than `0.0437`.

For `0.12<=a<=0.198`, `N_A'` is concave and is positive at both endpoints (`>0.1005` and `>0.9607`), so `N_A` is increasing there and remains `>0.0491`.

Therefore

> **`G>0` throughout the rho=0 endpoint family.**          `(RQ-8)`

### 5.2 kappa=0 endpoint

Eliminating rho with `D=0` gives, apart from the positive denominator `2(alpha+sigma)`, numerator

`N_B=-6a^3-2a^2+(2s^2-8s+4)a+s^3-3s+2`.

On the same rectangle, the coefficient `2s^2-8s+4` is positive. Also

`s^3-3s+2 >= 0.5588`,

while

`2a^2+6a^3 <0.125`.

Hence

> **`N_B>0.433`, so `G>0`.**                               `(RQ-9)`

Both endpoint families contradict the necessary condition `G<=0`.

## 6. Theorem

Therefore every unbounded repeated rigid one-code survivor with `y>=2,m>=2` satisfies

> **`(r+g0+d)/p >= 0.53-o(1)`.**                          `(RQ-10)`

The intermediate `0.47` and `1/2` barriers are superseded by `(RQ-10)` but remain useful audit checkpoints.

## 7. Row concentration

The same raw rectangle gives a useful structural normal form. If `r_i=d_R(w_i)` for `w_i in W0`, then

`sum r_i=e(W0,R)<=x`.

Thus for every threshold `T>=1`, at most `floor(x/T)` singleton rows have `r_i>=T`. In particular, whenever `|W0|=p-o(p)` and `x=O(p)`, choosing `T=sqrt(p)` leaves `p-o(p)` coordinate-indexed witnesses with only `o(p)` neighbours in the extra-U population. They are simultaneously X-anticomplete, Y-anticomplete and mutually independent.

## 8. Trust boundary and next move

The theorem is conditional on the repeated rigid complete one-code interface and does not close the zero-positive-fixture graph-level gap. The next mathematical target is the exact rho=0 endpoint polynomial beyond `sigma=0.53`: analytic optimization indicates that this family is the first place where the current combined score/rooted-Q package can eventually lose positivity. That line should be sharpened structurally, not by replacing proof with a finite scan. In parallel the actual-D2C/X3 regression remains mandatory.
