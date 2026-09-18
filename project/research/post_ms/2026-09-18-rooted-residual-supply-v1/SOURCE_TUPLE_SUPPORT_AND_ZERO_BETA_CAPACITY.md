# Source-tuple support and zero-beta cross-edge capacity

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal structural theorem package. This note strengthens `ROOTED_TRIANGLE_RESIDUAL_AND_BETA_DEGREE_SUPPLY.md`. No global eventual theorem is claimed.

## 1. Why the zero-beta support is now the right object

The beta-sensitive degree-supply theorem gives

> `E_U>=u(p+u-1)-2au+B_beta-s_0-2N_1`,                  `(ELOW)`

where

- `A_0={x in A:ell_x=0}`;
- `N_0=|A_0|`;
- `s_0=sum_{x in A_0}d_U(x)`;
- `N_1=|{x:ell_x=1}|`.

The previous coarse elimination used only `ell_x<=min(p,u)`, giving a crude upper bound on `N_0`. The full source-tuple deficit profile gives a strictly more informative support theorem.

Recall the exact integrated source-tuple theorem: for every fixed `r>=3`, every subset `L subseteq A` of size `N` satisfies

> `sum_{x in L}(p-ell_x)>=Phi_r(N)`,                     `(IST)`

where

> `Phi_r(N)=sum_{K=0}^{p-r}(N-C_hat_r(K))_+`,
>
> `C_hat_r(K)=floor(((K+r)/r) binom(u,r)/binom(p-K,r))`.

## 2. Exact beta-support theorem

Let

> `A_+={x in A:ell_x>0}`,
>
> `N_+=|A_+|`.

Since the zero-load vertices contribute nothing to `B_beta`,

`B_beta=sum_{x in A_+}ell_x`.

Apply `(IST)` to `A_+`:

`N_+p-B_beta=sum_{x in A_+}(p-ell_x)>=Phi_r(N_+)`.

Thus:

### Theorem 2.1 (source-tuple beta-support capacity)

For every `r>=3`,

> `B_beta<=N_+ p-Phi_r(N_+)`.                            `(BSP)`

Equivalently, define

> `N_r(B)=min{N>=0:Np-Phi_r(N)>=B}`.                     `(NSr)`

Then every configuration with beta load `B_beta=B` satisfies

> `N_+>=N_r(B)`.                                          `(NS)`

This is exact and finite.

The elementary distinct-source support bound remains available as well. Put

> `L=min(p,u)`.

Since every positive beta-loaded vertex has `ell_x<=L`,

> `N_+>=ceil(B_beta/L)`.                                  `(DSLsup)`

Hence a convenient combined support floor is

> `N_sup(B)=max(ceil(B/L), max_{r>=3}N_r(B))`.             `(NSUP)`

Every actual configuration satisfies `N_+>=N_sup(B_beta)`.

## 3. Zero-beta cross-edge capacity

Since `N_0=a-N_+`, Theorem 2.1 gives

> `N_0<=a-N_sup(B_beta)`.                                 `(N0ST)`

Therefore

> `s_0<=u[a-N_sup(B_beta)]`.                              `(S0ST)`

This is exactly the missing bridge identified at the previous checkpoint: source-tuple scarcity does not merely bound the total beta traffic; it bounds how much of the A-layer can remain completely beta-free, and therefore how much cross-edge degree can hide in `s_0`.

## 4. Strengthened unmatched-slack and residual floors

Insert `(S0ST)` into `(ELOW)`. Since `N_1<=a`,

### Corollary 4.1

> `E_U`
> `>=u(p+u-1)-3au+B_beta`
> `  +u N_sup(B_beta)-2a`.                                `(ST-E)`

Likewise the residual lower bound

`r>=p(p-lambda)-s_0-N_1`

gives

### Corollary 4.2

> `r`
> `>=p(p-lambda)-u[a-N_sup(B_beta)]-a`.                   `(ST-R)`

Both statements are exact finite inequalities.

For an above-threshold candidate one may replace `B_beta` by any valid lower bound, in particular

> `B_*=max(0,p(lambda+1-2p),pu-R_hat a)`,

because `N_sup(B)` is nondecreasing in `B` and the right side of `(ST-E)` is nondecreasing in `B`.

Thus `(ST-E)` yields a stronger parameter-only pruning condition than the earlier ceiling-only `(PEF*)` whenever the source-tuple support floor exceeds `ceil(B_*/min(p,u))`.

## 5. Continuum support function

Assume

`u/p->rho>0`,

`B_beta/p^2->beta>0`,

`N_+/p->nu`.

For fixed `r>=3`, the continuum source profile is

> `phi_r(nu;rho)=int_0^1 [nu-c_{r,rho}(kappa)]_+ d kappa`,

where

> `c_{r,rho}(kappa)=(kappa/r)(rho/(1-kappa))^r`.

Dividing `(BSP)` by `p^2` gives

> `nu-beta>=phi_r(nu;rho)`.                               `(CSPsup)`

Put

> `F_r(nu;rho)=nu-phi_r(nu;rho)`.

For `nu>0`, the derivative of `phi_r` with respect to `nu` is the measure of the set on which `c_{r,rho}(kappa)<nu`, and is strictly between zero and one. Therefore `F_r` is strictly increasing from zero.

Hence for every `beta>0` there is a unique support threshold `nu_r(beta;rho)>beta` satisfying

> `F_r(nu_r;rho)=beta`.                                   `(CSroot)`

Every limiting configuration obeys

> `nu>=nu_r(beta;rho)`.                                   `(CSfloor)`

Together with the distinct-source ceiling,

> `nu>=beta/min(1,rho)`,

so one may take the maximum of the two lower bounds.

The strict inequality `nu_r(beta;rho)>beta` is important when `rho>=1`: a positive quadratic beta load cannot be carried by merely `beta p+o(p)` A-vertices. Source-tuple scarcity forces a positive additional support population, shrinking the zero-beta escape.

## 6. Explicit triple-source support function

For `r=3`, let `kappa in (0,1)` be determined by

> `nu=kappa rho^3/[3(1-kappa)^3]`.                        `(Tnu)`

The preserved explicit profile gives

`phi_3(nu;rho)`

`=nu kappa-(rho^3/3) kappa^2/[2(1-kappa)^2]`.

Therefore

> `nu-phi_3(nu;rho)`
> `=rho^3 kappa(2+kappa)/[6(1-kappa)^2]`.                 `(TF)`

For prescribed `beta>0`, put

> `t=6beta/rho^3`.

The unique solution is

> `kappa=t/(t+1+sqrt(3t+1))`,                             `(Tk)`

and hence

> `nu_3(beta;rho)=rho^3 kappa/[3(1-kappa)^3]`.            `(Tsup)`

This gives an explicit radical support floor with no numerical optimization.

## 7. Strengthened continuum degree-supply envelope

Let

`A=2+rho-theta`,

and write `e_U=liminf E_U/p^2`.

From `(ST-E)`, the negligible `2a/p^2` term disappears, giving

> `e_U`
> `>=rho(1+rho-3A)+beta+rho nu`.                          `(CST-E)`

Using the triple-source support floor,

> `e_U`
> `>=rho(1+rho-3A)+beta+rho nu_3(beta;rho)`.              `(CST3)`

Above threshold,

`e_U<=c=theta(1+rho)-theta^2/2`,

while

> `beta>=beta_*:=max(0,theta-2,rho-A R)`,
>
> `R=min(1,sqrt(c))`.

Since `nu_3(beta;rho)` is increasing in `beta`, every limiting above-threshold candidate must satisfy

> `rho(1+rho-3A)`
> ` +beta_*+rho nu_3(beta_*;rho)`
> ` <=c`.                                                 `(STDS)`

This is a parameter-only necessary condition. It strengthens the previous coarse degree-supply envelope `(CDS)` by replacing the crude support term with the exact triple-source support floor.

A second necessary condition is simply

> `nu_3(beta_*;rho)<=A`,                                  `(STSUP)`

because the positive beta support lies inside the A-layer.

## 8. Strategic consequence

The zero-beta obstruction is no longer distribution-free. The source-tuple hierarchy forces a minimum **number of positive beta witnesses**, not merely a minimum total beta load. Thus large beta traffic simultaneously:

1. consumes A-layer support through `(BSP)/(STSUP)`;
2. reduces the zero-beta cross-edge reservoir `s_0` through `(S0ST)`;
3. increases `E_U` through `(ST-E)/(STDS)`;
4. increases the residual floor through `(ST-R)`.

This is exactly the coupling needed after the rooted-triangle transfer pivot. The next high-value step is to combine `(ST-R)` with the transfer window `(TW)` and the actual rooted triangle quantity `Q=p(p+u-1)+q`, rather than returning to q-only optimization.
