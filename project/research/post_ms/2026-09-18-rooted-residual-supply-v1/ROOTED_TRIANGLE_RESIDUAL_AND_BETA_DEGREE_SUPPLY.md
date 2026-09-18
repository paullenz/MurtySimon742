# Rooted-triangle residual bridge and beta-sensitive degree supply

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal structural theorem package for the eventual / sufficiently-large second-extremal D2C programme. No all-order or eventual theorem is claimed. The published 2024 order-12, size-32 D2C graph `X_3` is retained as a mandatory hostile control and is analysed explicitly below.

## 1. Strategic reassessment

The live notes had begun to treat the scorecard `E_U+L_A` and the rooted triangle count `Q=e(G[N(v)])` as largely separate objects. In fact the near-full normal form contains a much tighter exact bridge. Making that bridge explicit is preferable to another blind optimization of `(CEIPM)`: it identifies exactly how rooted triangles transfer residual defect between the A-side and U-side slack accounts.

Retain the live notation

- `B=N(v)`, `A=V\N[v]`;
- `p` tight antipode pairs, unmatched set `U`, `u=|U|`;
- `a=2p+u-lambda-1`;
- `q=e(G[U])`, `s=e_G(A,U)`, `f=e(G[A])`;
- `Q=e(G[B])=p(p+u-1)+q`;
- `r=(p+u)(a-p)+p-s-q`;
- `delta=r-f=b(n-b)-m`;
- `E_U=u(p+u-1)-2q-s`;
- `L_A=a(p+u)-s-2f`.

Put

`c_lambda=ceil(lambda(lambda+2)/2)`.

## 2. Exact residual/slack identity

### Theorem 2.1 (residual-scorecard identity)

> `E_U+L_A = 2 delta + lambda(p+u)-p`.                    `(RS)`

### Proof

Substitute the definitions of `E_U,L_A,delta` and `a=2p+u-lambda-1`; all `q,s,f` terms cancel. The remaining difference is exactly `lambda(p+u)-p`.

Thus the global scorecard is not merely analogous to residual defect: it is an affine reparametrization of it.

## 3. Exact second-extremal residual threshold

Define

> `D_M := ceil((4p+2u-c_lambda-2)/2)`.                   `(DM)`

### Theorem 3.1

`D_M=b(n-b)-M(n)`, where `M(n)=floor((n-1)^2/4)+1`. Hence

> `m<=M(n)  iff  delta>=D_M`,
>
> `m>M(n)   iff  delta<=D_M-1`.                          `(RT)`

### Proof

The preserved scorecard equivalence is

`m<=M(n) iff E_U+L_A>=S_req`,

where

`S_req=p lambda+3p+u lambda+2u-c_lambda-2`.

Insert `(RS)`:

`2 delta >= S_req-lambda(p+u)+p`

`             =4p+2u-c_lambda-2`.

Since `delta` is integral, this is precisely `delta>=D_M`. The identity with `b(n-b)-M(n)` follows directly from `m=b(n-b)-delta`.

This is the clean residual-defect form of the second-extremal problem.

## 4. Rooted triangles are an exact transfer variable

### Theorem 4.1 (rooted-triangle transfer identities)

> `r+Q = L_A+2f`,                                         `(RQ1)`
>
> `delta+Q = L_A+f`,                                      `(RQ2)`
>
> `delta = E_U+Q-f-lambda(p+u)+p`.                        `(RQ3)`

Equivalently, with

> `T:=Q-f`,

one has

> `L_A=delta+T`,
>
> `E_U=delta+lambda(p+u)-p-T`.                            `(TR)`

### Proof

Using the displayed formulas,

`r+Q`

`=(p+u)(a-p)+p-s-q+p(p+u-1)+q`

`=a(p+u)-s=L_A+2f`,

which proves `(RQ1)` and then `(RQ2)` because `delta=r-f`. Combining `(RQ2)` with `(RS)` gives `(RQ3)`.

The quantity `T=Q-f` is therefore the exact amount of slack transferred from the U-side account into the A-side account.

### Corollary 4.2 (counterexample transfer window)

Every above-`M(n)` candidate satisfies

> `L_A-D_M+1 <= T`
>
> `              <= D_M-1+lambda(p+u)-p-E_U`.            `(TW)`

This is simply `(TR)` together with `delta<=D_M-1`.

The triangle-containing branch can therefore be attacked by proving that the structural `T=Q-f` forced by criticality cannot lie in `(TW)` once the matched core is sufficiently large.

## 5. The order-12 negative control is an endpoint-saturated transfer example

For the published `X_3` graph the certified data are

`p=4, u=0, lambda=4, a=3, q=s=f=r=0`.

Hence

`Q=12`, `delta=0`, `E_U=0`, `L_A=12`, and `D_M=1`.

Therefore `(TW)` collapses to

> `12 <= T <= 12`.

So the finite exception is not merely compatible with the transfer picture: it saturates it exactly, with

> `T=Q-f=12`.

This gives a useful hostile-control interpretation. Any eventual proof based on rooted triangles must allow this exact small-core endpoint mechanism while ruling out its persistence for large cores.

## 6. Beta-loaded witnesses also control total U degree supply

For each `x in A`, let

- `ell_x` be its beta load;
- `Y_x` its `ell_x` pairwise-distinct designated beta sources;
- `d_x=d_U(x)`;
- `w_x` the number of chosen oriented `U--U` criticality certificates using `x` as A-side witness.

As in the preserved beta-sensitive `q` theorem, every source of a `U--U` certificate using `x` has code `bar(c(x))`, and a fixed source-witness pair certifies at most one U-edge.

The beta-cylinder geometry yields a stronger observation than was used in `(BQ)`.

### Lemma 6.1 (complementary-code non-neighbourhood)

If `ell_x>=2`, then **no U-neighbour of `x` has code `bar(c(x))`**. Hence

> `w_x<=u-d_x`.                                           `(CN2)`

If `ell_x=1`, at most the unique designated beta source can have complementary code, so

> `w_x<=u-d_x+1`.                                         `(CN1)`

If `ell_x=0`, trivially `w_x<=u`.

### Proof

Every central U-neighbour of `x` agrees with `c(x)` on every targeted coordinate, so it cannot be complementary once `ell_x>0`. A designated source `y_i` differs from `c(x)` at its own target coordinate `i`, but when `ell_x>=2` it agrees with `c(x)` at every other target coordinate `j in I_x\{i}`. Thus it too cannot be complementary. For `ell_x=1`, only that sole designated source remains as a possible complementary neighbour.

## 7. Exact joint `q+s` and `2q+s` bounds

Put

- `N_1=|{x:ell_x=1}|`;
- `A_0={x:ell_x=0}`;
- `N_0=|A_0|`;
- `s_0=sum_{x in A_0} d_x`;
- `B_beta=sum_x ell_x`.

Since `q=sum_x w_x` and `s=sum_x d_x`, Lemma 6.1 gives:

### Theorem 7.1 (beta-sensitive degree-supply theorem)

> `q+s <= a u+s_0+N_1`,                                  `(QS)`
>
> `2q+s <= 2a u-B_beta+s_0+2N_1`.                        `(2QS)`

### Proof

For `ell_x>=2`, `(CN2)` gives `w_x+d_x<=u` and, because `d_x>=ell_x`,

`2w_x+d_x<=2u-d_x<=2u-ell_x`.

For `ell_x=1`, `(CN1)` gives

`w_x+d_x<=u+1`,

`2w_x+d_x<=2u-d_x+2<=2u+1=(2u-ell_x)+2`.

For `ell_x=0`, use

`w_x+d_x<=u+d_x`,

`2w_x+d_x<=2u+d_x`.

Summing the three classes proves `(QS)` and `(2QS)`.

This is the desired direct control of the combined degree supply `2q+s`; it remains nontrivial when `u>=p`, unlike the special distinct-source ceiling `ell_x<=u` used in the small-unmatched branch.

## 8. Direct residual and unmatched-slack consequences

The exact normal-form identities immediately give:

### Corollary 8.1

> `r >= p(p-lambda)-s_0-N_1`.                             `(RLOW)`

### Corollary 8.2

> `E_U`
> `>=u(p+u-1)-2a u+B_beta-s_0-2N_1`.                     `(ELOW)`

These are hand structural bounds, not scan-derived inequalities.

The residual statement `(RLOW)` is especially useful because it isolates the only escape from a large positive residual: A-vertices carrying **zero beta load**. Thus the remaining obstruction to turning beta traffic directly into residual defect is sharply localized in the zero-load cross-edge supply `s_0`.

## 9. Eliminating the zero-load population coarsely

Let

> `L=min(p,u)`

and assume `u>0`. Since every nonzero beta-loaded A-vertex has `ell_x<=L`,

> `B_beta<=L(a-N_0)`.

Therefore

> `N_0<=a-ceil(B_beta/L)`,                                `(N0)`

and so

> `s_0<=u[a-ceil(B_beta/L)]`.                             `(S0)`

Also `N_1<=a`. Substituting in `(ELOW)` yields the parameter-level floor

> `E_U`
> `>=u(p+u-1)-3a u+B_beta`
> `  +u ceil(B_beta/L)-2a`.                               `(PEF)`

The right side is monotone nondecreasing in `B_beta`.

For an above-threshold candidate put

> `B_* = max(0, p(lambda+1-2p), pu-R_hat a)`,             `(B*)`

where `R_hat=min(p,R_*)` is the preserved switching bound. Since `B_beta>=B_*`, every above-threshold candidate with `u>0` satisfies

> `E_U >= F_E(p,u,lambda):=`
> `u(p+u-1)-3a u+B_*+u ceil(B_*/L)-2a`.                  `(PEF*)`

In particular, because `E_U<=C_0`,

> `F_E(p,u,lambda)<=C_0`                                  `(DSF)`

is a new finite parameter-only necessary condition.

## 10. Continuum degree-supply envelope

For a linear-scale sequence write

`u/p->rho>0`, `lambda/p->theta`, `a/p->A=2+rho-theta`,

`B_beta/p^2->beta`, and

`c=theta(1+rho)-theta^2/2`, `R=min(1,sqrt(c))`.

From `(PEF)`,

> `liminf E_U/p^2`
> `>=rho(1+rho-3A)`
> ` +(1+max(1,rho)) beta`.                                `(CDE)`

Above threshold one has `E_U/p^2<=c+o(1)` and

> `beta>=beta_*:=max(0,(theta-2),rho-A R)`.               `(CB*)`

Therefore every limiting above-threshold candidate satisfies

> `rho(1+rho-3A)`
> ` +(1+max(1,rho)) beta_* <= c`.                         `(CDS)`

This is independent of Hamming energy, alpha overflow and the variational threshold in `(CEIPM)`.

For example, on `rho>=1`, `theta>2`, using only `beta>=theta-2` gives the explicit necessary cap

> `theta <= -3rho+sqrt(13rho^2+14rho+4)`.                 `(CDS+)`

This is not claimed to supersede the source-root envelope `(SRE)` numerically; its value is different. It converts beta traffic directly into **unmatched slack / residual degree supply**, and identifies the zero-beta A-layer as the unique coarse escape.

## 11. Strategic consequence

The best next compact structural target is now clearer.

1. The residual threshold itself is exact: prove `delta>=D_M`.
2. Rooted triangles enter only through the transfer variable `T=Q-f`; a counterexample must place `T` inside the narrow exact window `(TW)`.
3. Beta traffic directly caps `q+s` and `2q+s`; the only uncontrolled contribution is `s_0`, the A--U degree carried by zero-beta witnesses.
4. Therefore a high-value next theorem is a **zero-beta cross-edge capacity theorem**: show that large `s_0` forces alpha congestion, A-side slack, or a large switching/true-twin class. Such a theorem would feed simultaneously into `(RLOW)`, `(ELOW)`, `(TW)`, and the residual target `delta>=D_M`.

This route is structurally closer to the stated second-extremal problem than further decimal optimization of `(CEIPM)`. The enhanced IPM remains preserved as a supporting global constraint.
