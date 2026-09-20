# Two-X-hole branch — explicit finite-order tail after the x>=16 closure

Date: 2026-09-20

Status: **same-session internal analytic bound** inside the core-saturated exact second-strict two-X-hole branch (`y>=2`, `x>=4`). Combined with `TWO_X_HOLE_EVENTUAL_X16_CLOSURE.md`, this shows that the whole branch has bounded order; no finite parameter scan is used as proof.

## 1. Starting necessary inequality

Let

`M=M_H=m_{H_0}+m_{H_1}`

be the distinguished physical hole-code witness resource.

The exact positive-combination argument in `TWO_X_HOLE_BOUNDED_HOLE_RESOURCE_CLOSURE.md` did not require `M<=8` until its final specialization. Its general necessary condition is

> **`Phi<=11M`,**                                         `(T-PHI-M)`

where

`Phi=8L+P-2eps`
`    +3p^2+2p omega-3py-8p`
`    +omega^2-4omega x+omega y-8omega`
`    +5x^2-3xy-10x+2y^2+4y+20`,                         `(T-PHI)`

with

`P=[omega(p-x)+2L]_+>=0`, `eps in {0,1}`.

For distinct hole codes, the two complementary witness classes are disjoint, so `M<=omega`. If the holes have the same code, the definition counts that physical class twice, so always

> **`M<=2omega`.**                                        `(T-M)`

Consequently every survivor satisfies the very coarse but universal bound

> **`Phi<=22omega`.**                                     `(T-PHI-OMEGA)`

The forward-routing surcharge can only improve this inequality, so it is not needed below.

## 2. A coercive lower bound for Phi

Put

> `S=p+omega`.

Separate the quadratic part in `(p,omega,y)`:

`Q=3p^2+2p omega-3py+omega^2+omega y+2y^2`.

### Lemma 2.1 — positive-orthant quadratic floor

For all `p,omega,y>=0`,

> **`Q>=7S^2/8`.**                                        `(T-Q)`

Proof. For fixed p and omega, Q is convex in y.

If `omega<=3p`, its unconstrained nonnegative minimizer is

`y_*=(3p-omega)/4`,

and direct substitution gives

`Q_min=(p+omega)(15p+7omega)/8 >=7(p+omega)^2/8`.

If `omega>=3p`, the minimum over `y>=0` occurs at `y=0`, where

`Q=3p^2+2p omega+omega^2 >=(p+omega)^2>=7S^2/8`.

This proves `(T-Q)`. `square`

### Lemma 2.2 — full Phi floor

The branch has

`lambda=2p+omega-y>=0`,

so

`y<=2p+omega<=2S`.

Discard the nonnegative terms `8L` and P and use `-2eps>=-2`. The remaining x-dependent linear terms satisfy

`-8p-(4x+8)omega-(3x-4)y`
` >=-(4x+8)S-2(3x-4)S`
` =-10xS`.

The constant

`5x^2-10x+20-2`

is positive for every `x>=4`. Therefore

> **`Phi>=7S^2/8-10xS`.**                                `(T-COERCIVE)`

## 3. Universal parameter bound in the finite-head tail

Combine `(T-PHI-OMEGA)` and `(T-COERCIVE)`. Since `omega<=S` and `S>0`,

`7S^2/8-10xS <=22omega<=22S`.

Divide by S:

> `7S/8<=10x+22`,

hence

> **`p+omega=S <= (8/7)(10x+22)`.**                      `(T-SBOUND)`

`TWO_X_HOLE_EVENTUAL_X16_CLOSURE.md` already proves that every survivor has

`4<=x<=15`.

Therefore

`S <= (8/7)(10*15+22)=1376/7<197`.

Since S is integral,

> **`p+omega<=196`.**                                     `(T-S196)`

Also

`y<=2p+omega<=2S<=392`.                                  `(T-Y392)`

Thus the allegedly unbounded `x<=15` tail is in fact globally bounded in every remaining size parameter.

## 4. Explicit order bound

The rooted partition has

- one root vertex;
- `|A|=x+y`;
- `2p` tight matched vertices;
- `u=x+1+omega` unmatched root-neighbours.

Hence

> `n=1+(x+y)+2p+(x+1+omega)`
> ` =2x+y+2p+omega+2`.                                   `(T-N)`

Using

- `x<=15`;
- `y<=2p+omega`;
- `p+omega<=196`;

we get

`n<=2x+(2p+omega)+(2p+omega)+2`
` <=32+4(p+omega)`
` <=32+784`
` =816`.

Therefore:

> **TWO-X-HOLE FINITE-ORDER CLOSURE.** Every graph in the core-saturated exact second-strict two-X-hole branch satisfies
>
> **`n<=816`.**                                           `(2X-N816)`

Equivalently, conditional on the audited rigid one-code interface,

> **the exact second-strict two-X-hole branch is impossible for every `n>=817`.** `(2X-N817-CLOSED)`

This is an explicit analytic finite-order reduction, not a conclusion inferred from a bounded scan.

## 5. Interpretation

The two-X-hole arm no longer contributes an asymptotic family to the eventual-D2C programme. Its remaining configurations form a genuinely bounded parameter set.

The numerical threshold 816 is intentionally coarse. It uses only

- the general `Phi<=11M` density-rebate budget;
- the trivial `M<=2omega` multiplicity bound;
- positivity of the quadratic form on the positive orthant;
- `lambda>=0`.

The stronger forward-routing surcharge, exact pair-local `Ccap_P/(ONE-P)/(CROWD)`, class self-pricing and Hamming-slot bills can only lower the bound. They should be used later if a small-tail classification is desired, but they are unnecessary for the eventual conclusion of this branch.

## 6. Audit boundary

Hostile replay should check:

1. that `Phi<=11M` is indeed a general necessary condition before the bounded-resource specialization;
2. the repeated-hole-code convention in `M<=2omega`;
3. the positive-orthant quadratic minimization `(T-Q)`;
4. the rooted partition identity `(T-N)`.

No claim is made here about branches outside the exact second-strict two-X-hole geometry, and the zero-positive-rigid-cut regression gap remains fully binding.