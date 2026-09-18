# Distinct-source beta ceiling and beta-sensitive U-edge capacity

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal structural theorem package for the eventual / sufficiently-large second-extremal D2C project. The finite statements below are hand consequences of the preserved selected near-full system. The asymptotic statements are necessary conditions only. No all-order or eventual theorem is claimed.

The published 2024 order-12, size-32 graph `X_3` is untouched throughout: it has `u=0`, whereas every new statement below concerns the unmatched layer.

---

## 1. Setup and strategic reassessment

Retain the notation of `CURRENT_STATE.md`.

There are `p` tight matched fibres in `B=N(v)`, an unmatched set `U` of size `u`, and

`a=|A|=2p+u-lambda-1`.

For `x in A`, let

- `I_x` be the set of beta target fibres,
- `ell_x=|I_x|` be the beta load,
- `k_x=p-ell_x` be the beta deficit,
- `Y_x={y_i:i in I_x}` be the designated unmatched beta sources.

The preserved beta-reuse geometry gives two facts that are crucial here:

1. the vertices in `Y_x` are pairwise distinct;
2. on the targeted coordinates,

   `c(y_i)|_{I_x}=c(x)|_{I_x} Delta {i}`.              `(1.1)`

Put

`B_beta=sum_{x in A} ell_x=pu-h_alpha`.

The previous live priority was to obtain a beta/source-tuple-sensitive upper bound on `q=e(G[U])`, because the distribution-free sparse-U cap was the main obstruction in the high-root-imbalance branch. The first observation below is even simpler than expected: pairwise distinctness of the designated sources already yields a missing global beta-load ceiling. Feeding that ceiling into the switching lower bound gives a substantially stronger small-`rho` exclusion. The same local geometry then gives the desired beta-sensitive bound on `q` itself.

---

## 2. Exact distinct-source beta ceiling

Because `Y_x subseteq U` and its members are pairwise distinct,

> `ell_x<=min(p,u)`                                       `(DS1)`

for every `x in A`.

Summing gives the exact finite theorem:

### Theorem 2.1 (distinct-source beta ceiling)

> `B_beta<=a min(p,u)`.                                   `(DSB)`

In particular, whenever `u<=p`,

> `B_beta<=a u`.                                          `(DSB-u)`

This is independent of the scorecard and of the second-extremal threshold. It is a structural consequence of the selected beta-source system itself.

Although elementary, `(DSB-u)` is much stronger than the trivial `B_beta<=ap` precisely in the small-unmatched high-root-imbalance regime which remained difficult after the source-root switching run.

---

## 3. Finite root-imbalance consequence

The preserved root-imbalance beta floor is

> `B_beta>=p(lambda+1-2p)_+`.                             `(RBF-f)`

Assume `u<=p` and put

`L=lambda+1-2p`.

If `L<=0` there is nothing to prove. If `L>0`, then

`a=2p+u-lambda-1=u-L`.

Combining `(RBF-f)` with `(DSB-u)` gives

`pL<=u(u-L)`,

hence

> `L(p+u)<=u^2`.                                          `(3.1)`

Therefore:

### Theorem 3.1 (finite distinct-source root wedge)

Every selected partial-Boolean configuration with `u<=p` satisfies

> `lambda`
> `<=2p-1+floor(u^2/(p+u))`.                              `(FDRW)`

No above-`M(n)` assumption is needed.

### Continuum form

Suppose

`u/p->rho in (0,1)`,

`lambda/p->theta`,

`a/p->A=2+rho-theta>0`.

Then `(FDRW)` gives

> `theta<=2+rho^2/(1+rho)`.                               `(DRW)`

For `rho<=1/2`, this immediately implies the cleaner linear cap

> `theta<=2+rho/3`.                                       `(1/3W-weak)`

Already this improves the previous two-fifths wedge throughout `rho<=1/2`.

---

## 4. Source-tuple non-saturation makes the root wedge strict

The ceiling `(DSB-u)` cannot be asymptotically saturated by a linear population of A-vertices when `0<rho<1`.

### Theorem 4.1 (strict distinct-source ceiling)

Assume

`u/p->rho in (0,1)`,

`a/p->A>0`.

Then

> `limsup B_beta/p^2 < A rho`.                            `(SDSB)`

#### Proof

Suppose instead, along a subsequence,

`B_beta/p^2 -> A rho`.

Since every `ell_x<=u`,

`D:=sum_x (u-ell_x)=au-B_beta=o(p^2)`.                   `(4.1)`

Choose a fixed integer `r>=3` so large that

`(1-rho)/r < A/4`.

Then choose a fixed `eta in (0,rho)` sufficiently small that

> `[(1-rho+eta)/r] [rho/(rho-eta)]^r < A/2`.             `(4.2)`

Let

`X_eta={x:ell_x>=(rho-eta)p}`.

By `(4.1)`,

`|A\X_eta| eta p <=D`,

so

`|X_eta|=(A-o(1))p`.                                     `(4.3)`

But every `x in X_eta` has

`k_x<=K=(1-rho+eta)p+o(p)`.

The exact source-tuple threshold bound `(FDPr)` gives

`|X_eta|/p`

`<= [(1-rho+eta)/r] [rho/(rho-eta)]^r+o(1)`

`<A/2+o(1)`,                                             `(4.4)`

contradicting `(4.3)`.

Thus `(SDSB)` holds.

### Corollary 4.2 (strict root wedge)

For every linear-scale selected sequence with

`0<rho<1`, `theta>2`,

one has

> `theta < 2+rho^2/(1+rho)`.                              `(SDRW)`

Indeed, equality in `(DRW)` would give

`A=rho/(1+rho)`

and force the root beta lower bound to equal `A rho`, contradicting `(SDSB)`.

Hence on `rho<=1/2`,

> `theta<2+rho/3`.                                        `(1/3W)`

This strictly supersedes the previous `(2/5W)` result.

---

## 5. Above-threshold switching strengthens the ceiling again

Above `M(n)`, let

`R_hat=min(p,R_*)`,

where `R_*` is the preserved switching bound. Then

> `B_beta >= [pu-R_hat a]_+`.                             `(STL)`

Combine this with `(DSB-u)`.

If `pu<=R_hat a`, then trivially `pu<=a(u+R_hat)`.

If `pu>R_hat a`, then

`pu-R_hat a<=B_beta<=au`,

and the same conclusion follows.

Thus:

### Theorem 5.1 (finite distinct-source switching sandwich)

Every above-`M(n)` partial-Boolean candidate with `u<=p` satisfies

> `pu <= a(u+R_hat)`.                                     `(DSS-f)`

This is a parameter-only finite necessary condition.

### Continuum form

For a linear-scale above-threshold sequence, put

`c=theta(1+rho)-theta^2/2`,

`R=min(1,sqrt(c))`.

Then `(DSS-f)` gives

> `A(rho+R)>=rho`.                                        `(DSS)`

When `0<rho<1` and `theta>2`, the inequality is in fact strict:

> `A(rho+R)>rho`.                                         `(SDSS)`

To see this, note that `A<rho`, so `rho-AR>0`; equality in `(DSS)` would force the switching lower bound for beta traffic to saturate the ceiling `A rho`, contradicting `(SDSB)`.

The point is that `(SDSS)` contains no beta variable, Hamming energy, alpha distribution or variational parameter.

---

## 6. Exact improvement of the small-unmatched exclusion

The strict switching sandwich gives a clean radical endpoint.

### Theorem 6.1 (new small-unmatched high-imbalance exclusion)

Every above-`M(n)` linear-scale partial-Boolean survivor with

`theta>2`

satisfies

> `rho>2-sqrt(3)=0.2679491924...`.                         `(RHO27)`

#### Proof

Suppose `0<rho<1/2` and `theta>2`.

Then

`A=2+rho-theta<rho`.

Also

`c(theta)=theta(1+rho)-theta^2/2`

is strictly decreasing for `theta>2`, because

`c'(theta)=1+rho-theta<rho-1<0`.

At `theta=2`, `c=2rho<1`. Therefore throughout `theta>2`,

`R=sqrt(c)<sqrt(2rho)`.

Hence

`A(rho+R)`

`<rho[rho+sqrt(2rho)]`.                                  `(6.1)`

But `(SDSS)` requires the left side to exceed `rho`. Thus necessarily

`rho+sqrt(2rho)>1`.                                      `(6.2)`

Squaring the equivalent inequality `sqrt(2rho)>1-rho` gives

`rho^2-4rho+1<0`.

The smaller root is `2-sqrt(3)`, proving `(RHO27)`.

This replaces the previous `rho>4/25=0.16` exclusion by an exact structural threshold larger by about 67%.

Combining Theorem 6.1 with `(1/3W)` gives the clean surviving small-rho slice

> `2-sqrt(3)<rho<=1/2`,
>
> `2<theta<2+rho/3`,                                     `(SMALL-SLICE)`

with the stronger implicit constraint `(SDSS)` available when needed.

---

## 7. Beta-sensitive upper bound for `q=e(G[U])`

The same local geometry supplies the missing beta-sensitive `q` theorem.

Choose, for every edge of `G[U]`, one of the preserved triangle-edge criticality orientations and one A-side unique-common-neighbour witness. For `x in A`, let `w_x` be the number of chosen U-edge certificates using `x` as witness.

Every edge certified by `x` has a source `y` with

`c(y)=bar(c(x))`.

A fixed ordered pair `(y,x)` can certify at most one U-edge, because the singleton common neighbourhood `N(y) cap N(x)={z}` determines the head `z`. Therefore

> `w_x<=t_bar(c(x))`.                                     `(7.1)`

Now compare the complementary source class with the designated beta sources `Y_x`.

If `ell_x>=2`, then no vertex of `Y_x` has code `bar(c(x))`: by `(1.1)` a designated source differs from `x` in exactly one targeted coordinate, while `bar(c(x))` differs from `x` in every targeted coordinate. Thus

`t_bar(c(x))<=u-ell_x`.                                  `(7.2)`

If `ell_x=1`, at most one designated source may have complementary code, so

`t_bar(c(x))<=u=u-ell_x+1`.                              `(7.3)`

If `ell_x=0`, trivially `t_bar(c(x))<=u`.

Let

`N_1=|{x in A:ell_x=1}|`.

From `(7.1)--(7.3)`,

> `w_x<=u-ell_x+1_{ell_x=1}`.

Summing over `A` and using `q=sum_x w_x` gives:

### Theorem 7.1 (beta-sensitive U-edge capacity)

> `q<=a u-B_beta+N_1`
> ` <=a u-B_beta+a`.                                     `(BQ)`

This is exact and finite.

Unlike `(SU)` and `(WU)`, the new theorem becomes stronger as beta traffic increases. It therefore couples the source-root/switching beta lower bounds directly to the internal U-edge supply.

### Continuum form

If

`q/p^2->xi`, `B_beta/p^2->beta`,

then

> `xi<=A rho-beta`.                                       `(CBQ)`

Combining with the switching beta lower bound gives, whenever that lower bound is positive,

> `xi<=A(rho+R)-rho`.                                     `(SQ)`

For the high-root-imbalance branch `theta>2`, `0<rho<1`, positivity is automatic because `A<rho` and `R<=1`.

Thus, near the new switching boundary `(SDSS)`, the allowed internal-U density is forced to zero. This is exactly the coupling missing from the previous distribution-free `q` estimates.

---

## 8. Comparison with the old sparse-U cap

The old switching/Hall sparse-U bound has continuum form

> `xi<=R A^2`.                                            `(SU-c)`

Compare it with `(SQ)`:

`[A(rho+R)-rho]-R A^2`

`=(1-A)(AR-rho)`.                                        `(8.1)`

In the high-root-imbalance branch, `AR-rho<0`. Therefore whenever

> `A<1`,

one has

> `A(rho+R)-rho < R A^2`.                                `(8.2)`

So `(SQ)` is **strictly stronger** than the old distribution-free sparse-U cap throughout every high-imbalance region with `A<1`.

In particular, if `0<rho<1` and `theta>2`, then `A<rho<1`, and the new beta-sensitive `q` theorem always improves `(SU-c)`.

This directly resolves the strategic obstruction recorded in the previous checkpoint for the entire small-unmatched high-imbalance branch. It does not by itself settle the larger-`rho` branch where `A` can exceed one.

---

## 9. Consequences for the live research programme

The present run changes the priority order.

1. **Small unmatched, high root imbalance (`theta>2`, `rho<1`) is now much narrower.** The old `rho>4/25` and two-fifths wedge are superseded by

   `rho>2-sqrt(3)` and `theta<2+rho^2/(1+rho)`,

   with the stronger implicit switching curve `(SDSS)`.

2. **The requested beta-sensitive `q` cap now exists.** In continuum form it is `(CBQ)/(SQ)`, and for `A<1` it strictly dominates the old sparse-U bound.

3. The next high-value step should therefore be to insert

   `xi<=A(rho+R)-rho`

   into the preserved enhanced IPM on the slice `theta>2`, `rho<1`, rather than continuing to use `xi<=RA^2` there.

4. For `rho>=1`, the distinct-source ceiling becomes `B_beta<=ap` and loses its special strength. The source-root envelope `(SRE)` and source-tuple beta-load envelope remain the main compact tools there.

5. The finite theorem `(DSS-f)` is worth using before any continuum optimization: it can prune candidate parameter triples using only `(p,u,lambda,C_0)`.

The separate `Q=0` / false-twin-core branch remains open.

---

## 10. Trust boundary

- `(DSB)` uses only pairwise distinctness of the designated beta sources, already part of the preserved beta-reuse geometry.
- `(FDRW)` additionally uses the preserved exact root-imbalance beta floor.
- `(SDSB)` is a hand consequence of the exact source-tuple threshold hierarchy `(FDPr)`; it is not a numerical claim.
- `(DSS-f)` additionally uses the preserved above-threshold switching/Hall beta lower bound.
- `(RHO27)` is an exact analytic consequence of `(SDSS)` and the monotonicity of `A` and `c` for `rho<1`, `theta>2`.
- `(BQ)` uses the preserved A-side critical witness for every U--U edge, uniqueness of a source-witness pair, and the beta-target code rule `(1.1)`.
- The audit accompanying this note checks the local complement-avoidance kernel and finite/continuum arithmetic only; it does not replace these hand proofs.
- The published 12/32 `X_3` graph has `u=0` and is untouched.
- No all-order or eventual second-extremal theorem is claimed.
