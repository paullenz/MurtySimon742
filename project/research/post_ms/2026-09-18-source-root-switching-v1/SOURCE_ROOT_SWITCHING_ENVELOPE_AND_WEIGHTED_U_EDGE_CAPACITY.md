# Source-root switching envelope and weighted U-edge capacity

**Status:** internal structural theorem package, 18 September 2026.

This note continues the eventual / sufficiently-large second-extremal D2C attack.  It is confined to the live near-full partial-Boolean branch and does **not** assert an all-order theorem.  The published 2024 order-12, size-32 graph `X_3` has `u=0` and is untouched throughout.

The immediate purpose was to carry out the advertised coupling of the new total beta-load envelope `(CBE)/(CBL)` with the global linear-scale analysis.  The main outcome is that the source-tuple envelope and switching lower bound already give a useful compact two-parameter exclusion before `(CEIPM)` is invoked.  A second outcome is a new scorecard-weighted theorem for all `U--U` edges, which clarifies exactly where the current `q` term can and cannot be improved.

---

## 1. Setup

Use the live notation from `CURRENT_STATE.md`.

There are `p` tight fibres, unmatched set `U` of size `u`, and

`a=2p+u-lambda-1`.

For a linear-scale sequence write

`u/p -> rho>0`,

`lambda/p -> theta`,

`a/p -> A=2+rho-theta>0`.

Put

`beta=limsup B_beta/p^2`,

and, for an above-`M(n)` sequence,

`c=c(rho,theta)=theta(1+rho)-theta^2/2`.

The exact source-tuple beta-load theorem gives, for every fixed `r>=3` and every fixed `0<kappa<1`,

> `beta <= A(1-kappa)`
> `        +(kappa^2/r)(rho/(1-kappa))^r`.               `(CBE)`

If `theta>2`, the exact root-imbalance beta floor gives

> `beta >= theta-2`.                                      `(RBF-c)`

Above threshold, switching gives

> `beta >= [rho-A R]_+`,                                  `(CBL-c)`

where

> `R=min(1,sqrt(c))`.

---

## 2. Continuum source-root envelope

Combining `(CBE)` with `(RBF-c)` eliminates beta load completely.

### Theorem 2.1 (source-root envelope)

Assume `rho>0`, `theta>2`, and `A>0`.  Then for every fixed `r>=3` and every `0<kappa<1`,

> `theta <= Theta_r(kappa;rho)`,                          `(SRE)`

where

> `Theta_r(kappa;rho)`
> `=[4+rho-(2+rho)kappa`
> `  +(kappa^2/r)(rho/(1-kappa))^r] /(2-kappa)`.

Hence

> `theta <= inf_{0<kappa<1} Theta_r(kappa;rho)`.

#### Proof

From `(RBF-c)` and `(CBE)`,

`theta-2`

`<= (2+rho-theta)(1-kappa)`

`   +(kappa^2/r)(rho/(1-kappa))^r`.

Move the `theta(1-kappa)` term to the left.  The coefficient of `theta` becomes `2-kappa`, giving `(SRE)`.

### Corollary 2.2 (quantitative strengthening of the strict beta wedge)

For `r=3`,

`Theta_3(0;rho)=2+rho/2`,

while

> `d/dkappa Theta_3(kappa;rho)|_{kappa=0}=-rho/4<0`.

Thus for every fixed `rho>0` the source-root envelope is **strictly** below the old line `2+rho/2` by a positive amount depending on `rho`.  This turns the former endpoint-only exclusion into a quantitative continuum gap.

For reference, at `rho=2` the minimizing `kappa` is the unique root in `(0,1)` of

> `3kappa^4-4kappa^3+14kappa^2-28kappa+3=0`,

namely `kappa=0.113377...`; the resulting cap is `theta<=2.965973...`.  This tiny decimal improvement is **not** the strategic point of the theorem and should not replace the cleaner rational bounds in expository work.

---

## 3. Switching-source sandwich when `c<1`

The stronger switching lower bound `(CBL-c)` becomes effective when the normalized scorecard `c` is below one.

### Theorem 3.1 (switching-source sandwich)

Assume an above-`M(n)` linear-scale sequence and `c<1`.  Then for every fixed `r>=3` and `0<kappa<1`,

> `rho-A sqrt(c)`
> `<= A(1-kappa)`
> `   +(kappa^2/r)(rho/(1-kappa))^r`.                    `(SSS)`

This is a parameter-only necessary condition.  It contains neither beta load, Hamming energy, alpha diversion, nor a code-distribution variable.

#### Proof

When `c<1`, `(CBL-c)` gives `beta>=rho-A sqrt(c)`.  Compare directly with `(CBE)`.

---

## 4. A clean lower bound on the unmatched ratio in the high-imbalance branch

The switching-source sandwich excludes a genuine open neighbourhood of `rho=0`.

### Theorem 4.1 (small-unmatched high-imbalance exclusion)

There is no above-`M(n)` partial-Boolean sequence with

> `theta>2` and `0<rho<=4/25`.

Equivalently, every above-threshold linear-scale survivor with `theta>2` satisfies

> `rho>4/25`.                                             `(RHO16)`

#### Proof

Fix `rho<=4/25` and suppose `theta>2`.

Because `rho<1`, both

`A=2+rho-theta`

and

`c=theta(1+rho)-theta^2/2`

strictly decrease as `theta` increases above `2`.  At `theta=2`,

`A=rho`, `c=2rho<=8/25<1`.

Hence throughout `theta>2` the lower side `rho-A sqrt(c)` of `(SSS)` increases, while the upper side decreases.  It therefore suffices to test the limiting value `theta=2`.

Take `r=3` and `kappa=13/20`.  Dividing the resulting strict comparison by `rho>0`, a contradiction follows whenever

> `13/20 - [(13/20)^2 rho^2]/[3(7/20)^3]`
> `> sqrt(2rho)`.                                         `(R16-1)`

The left-minus-right side is strictly decreasing in `rho`, so it suffices to check `rho=4/25`.  There

> `13/20 - [(13/20)^2(4/25)^2]/[3(7/20)^3]`
> `=291161/514500`,

and

> `(291161/514500)^2-8/25`
> `=67447921/264710250000>0`.

Thus `(R16-1)` holds at `4/25`, hence on the whole interval `(0,4/25]`, contradicting `(SSS)`.

---

## 5. A sharper high-imbalance wedge for `rho<=1/2`

The same argument yields a useful linear wedge that is substantially stronger than `theta<2+rho/2` in the small-to-moderate unmatched range.

### Theorem 5.1 (two-fifths wedge)

For every above-`M(n)` linear-scale partial-Boolean sequence with

> `0<rho<=1/2` and `theta>2`,

one has

> `theta < 2+(2/5)rho`.                                   `(2/5W)`

Together with Theorem 4.1, the surviving part of this slice satisfies

> `4/25<rho<=1/2`,
> `2<theta<2+(2/5)rho`.

#### Proof

Suppose instead that `theta>=theta_0:=2+(2/5)rho`.

At `theta_0`,

> `A_0=3rho/5`,
>
> `c_0=8rho(rho+5)/25`.

For `rho<=1/2`, `c_0<=22/25<1`.  Also `A` and `c` both decrease as `theta` increases on this range.  Thus it again suffices to test `(SSS)` at `theta_0`.

Take `r=3` and `kappa=2/5`.  At `theta_0`, the beta upper bound is

> `rho(500rho^2+729)/2025`,

whereas the switching lower bound is

> `rho[1-(6/25)sqrt(2rho^2+10rho)]`.

After division by `rho`, define their lower-minus-upper difference by `m(rho)`.  Direct differentiation gives

> `m'(rho)`
> `=-(1000 rho^(3/2)sqrt(rho+5)`
> `    +486 sqrt(2)rho+1215 sqrt(2))`
> `  /(2025 sqrt(rho)sqrt(rho+5)) <0`.

Therefore the smallest margin on `(0,1/2]` occurs at `rho=1/2`.  There

> `m(1/2)=1171/2025-3sqrt(22)/25>0`,

because

> `(1171/2025)^2-198/625=72163/4100625>0`.

So `(SSS)` fails at `theta_0`, and a fortiori at every larger `theta`.

---

## 6. Weighted criticality for all `U--U` edges

The attempt to feed the new beta constraints into `(CEIPM)` exposes the `+2xi` term, where `xi=q/p^2`, as the principal remaining distribution-free slack.  There is an exact scorecard-weighted strengthening of the old selected orientation bound for `q`.

For a Boolean code `c`, put

`n_c=|A_c|`, `t_c=|U_c|`,

`L_c=sum_{x in A_c}epsilon_x`,

`E_c=sum_{y in U_c}epsilon_y`.

### Theorem 6.1 (weighted U-edge orientation)

Assume `lambda>=0`.  Then

> `(lambda+1) q`
> `<= sum_c [n_bar(c) E_c + t_c L_bar(c)]`.              `(WU)`

#### Proof

Every edge `yz` of `G[U]` lies in the root triangle `yvz`.  Since the graph is diameter-2-critical, triangle-edge criticality lets us orient the edge, say `y -> z`, and choose a witness `x` with

> `N(y) cap N(x)={z}`.

Because `y in B=N(v)`, the witness cannot lie in `B` (otherwise `v` is a second common neighbour), and it cannot be `v`; hence `x in A`.  If `x` agreed with `y` in any tight coordinate, their selected matched endpoint in that fibre would be a second common neighbour.  Thus

> `c(x)=bar(c(y))`.

The unique-common-neighbour slack identity gives

> `epsilon_y+epsilon_x>=lambda+1`.

Choose one such certificate for every `U--U` edge.  A fixed ordered pair `(y,x)` can certify at most one edge because its singleton common neighbourhood determines the head `z`.  Therefore a source `y in U_c` occurs at most `n_bar(c)` times, while a witness `x in A_bar(c)` occurs at most `t_c` times.  Sum the slack inequality over all `q` oriented edges to obtain `(WU)`.

### Corollary 6.2 (coarse weighted q cap)

With

`mu_UA=max_c max(n_c,t_c)`,

> `(lambda+1)q <= mu_UA(E_U+L_A)`.                       `(WU2)`

Hence above threshold

> `q <= mu_UA C_0/(lambda+1)`.                            `(WU3)`

The theorem is structurally independent of the old unweighted bound `(SU)`.

### Corollary 6.3 (continuum q cap)

For a linear-scale above-threshold sequence with `theta>0`, the complementary-pair mass bound gives asymptotically

`mu_UA/p<=A`.

Consequently

> `xi <= A c/theta = A(rho+A)/2`.                        `(WU4)`

Together with `(SU)`,

> `xi <= A min(RA,(rho+A)/2)`,                           `(QMIN)`

where `R=min(1,sqrt(c))`.

This comparison is informative about strategy:

- if `theta<2`, then `A>rho`, and `(WU4)` can improve the old `A^2` sparse-U cap when `R=1`;
- if `theta>2`, then `A<rho`, so `(WU4)` is weaker than `A^2`, and `(SU)` remains the better distribution-free q bound (even more so when `R<1`).

Thus the new weighted theorem helps the moderate linear-imbalance branch, but it does **not** by itself solve the high-`theta` `CEIPM` bottleneck.

---

## 7. Strategic reassessment

The advertised `CBE/CBL -> CEIPM` coupling was carried out far enough to identify the correct division of labour.

1. In the high-root-imbalance branch `theta>2`, the compact source/switching sandwich is already stronger than the current distribution-free use of `(CEIPM)` near small `rho`.  It gives the explicit exclusions `(RHO16)` and `(2/5W)` without introducing Hamming or alpha variables.
2. The new weighted `q` theorem is exact and useful, but comparison with `(SU)` shows that it improves the `q` term primarily when `theta<2`, not in the high-`theta` branch where `A<rho`.
3. Therefore the next high-value high-`theta` step is **not** another blind optimization of `(CEIPM)`.  It is to obtain a genuinely beta-sensitive or source-tuple-sensitive upper bound on `q` (or on the combined `2q+s` degree supply), because the present distribution-free `q` allowance is what prevents the enhanced IPM from exploiting the new beta envelope sharply.
4. In parallel, `(WU)/(QMIN)` should be fed into `(CEIPM)` for `0<theta<2`, where it is a genuine improvement and attacks a different unresolved linear-imbalance slice.

The order-12 `X_3` negative control remains full-tight with `u=0` and is unaffected by every statement in this note.
