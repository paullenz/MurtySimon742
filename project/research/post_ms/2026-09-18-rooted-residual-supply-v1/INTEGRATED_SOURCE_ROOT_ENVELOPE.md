# Integrated source-root beta envelope

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal structural theorem / parameter envelope. No global eventual second-extremal theorem is claimed.

## 1. Reassessment

The existing source-root envelope `(SRE)` uses one source-deficit cutoff at a time. The preserved integrated source-tuple theorem is stronger than that use suggests: applying it to the **entire A-layer** gives a direct total beta-load envelope with no threshold parameter at all.

Recall that for every fixed `r>=3` and every subset `L subseteq A` of size `N`,

> `sum_{x in L}(p-ell_x)>=Phi_r(N)`,                     `(IST)`

where

> `Phi_r(N)=sum_{K=0}^{p-r}(N-C_hat_r(K))_+`.

## 2. Exact finite integrated beta envelope

Take `L=A`, so `N=a`. Since

`sum_{x in A}(p-ell_x)=ap-B_beta`,

we immediately obtain:

### Theorem 2.1 (integrated total beta envelope)

> `B_beta<=ap-Phi_r(a)`                                   `(ITB)`

for every `r>=3`.

This is exact and finite. It has no Hamming variable, alpha variable, code multiplicity or cutoff `K`.

It can be combined with every preserved beta lower bound. In particular, for an above-threshold candidate,

> `max(0,p(lambda+1-2p),pu-R_hat a)`
> `<= ap-Phi_r(a)`.                                      `(ITB*)`

This is a new parameter-only finite necessary condition.

## 3. Continuum integrated envelope

Assume

`u/p->rho>0`,

`a/p->A=2+rho-theta>0`,

`B_beta/p^2->beta`.

The continuum source profile gives

> `Phi_r(a)/p^2 -> phi_r(A;rho)`,

where

> `phi_r(A;rho)=int_0^1 [A-c_{r,rho}(kappa)]_+ d kappa`,
>
> `c_{r,rho}(kappa)=(kappa/r)(rho/(1-kappa))^r`.

Therefore `(ITB)` becomes

> `beta<=A-phi_r(A;rho)`.                                 `(CITB)`

Above threshold put

> `c=theta(1+rho)-theta^2/2`,
>
> `R=min(1,sqrt(c))`,
>
> `beta_*=max(0,theta-2,rho-A R)`.

Then every limiting candidate satisfies the compact integrated source-root condition

> `beta_*+phi_r(A;rho)<=A`.                               `(ISRE)`

This is the preferred parameter-only beta envelope at the present checkpoint. It uses the full source-deficit staircase rather than one cutoff.

## 4. Explicit triple-source form

For `r=3`, let `kappa_A in (0,1)` be the unique solution of

> `A = rho^3 kappa_A/[3(1-kappa_A)^3]`.                  `(KA)`

The explicit profile gives

`phi_3(A;rho)`

`=A kappa_A-(rho^3/3) kappa_A^2/[2(1-kappa_A)^2]`.

Hence

> `A-phi_3(A;rho)`
> `=rho^3 kappa_A(2+kappa_A)/[6(1-kappa_A)^2]`.           `(CAP3)`

Thus the triple-source integrated source-root envelope is simply

> `beta_*`
> `<=rho^3 kappa_A(2+kappa_A)/[6(1-kappa_A)^2]`,          `(ISRE3)`

with `kappa_A` determined by `(KA)`.

No numerical optimization is involved.

## 5. Relation to beta-support capacity

The source-support theorem defines `nu_3(beta;rho)` by

`nu_3-phi_3(nu_3;rho)=beta`.

Since `F_3(nu)=nu-phi_3(nu;rho)` is strictly increasing, `(ISRE3)` is equivalent to

> `nu_3(beta_*;rho)<=A`.                                  `(SUP-EQ)`

So the integrated source-root envelope and the A-support capacity theorem are two forms of the same structural obstruction:

- `(ISRE3)` says the required beta traffic exceeds the whole A-layer's integrated source-tuple capacity;
- `(SUP-EQ)` says carrying that beta traffic would require more positive beta witnesses than the A-layer contains.

The support formulation is the one needed for the new `s_0` / degree-supply bounds; the integrated formulation is the cleaner parameter-only filter.

## 6. Strategic consequence

The old high-`rho` source-root envelope `(SRE)` should no longer be treated as the terminal beta filter. Before invoking `(CEIPM)`, every parameter pair `(rho,theta)` should first be tested against `(ISRE3)` (and, where useful, higher `r`).

The live structural chain is now:

> beta lower bound
> `->` integrated source-root capacity `(ISRE)`
> `->` positive beta-support floor `(CSfloor)`
> `->` zero-beta cross-edge cap `(S0ST)`
> `->` joint degree-supply / residual floors `(ST-E)/(ST-R)`
> `->` rooted-triangle transfer window `(TW)`.

This chain is closer to a compact sufficiently-large structural theorem than optimizing the enhanced IPM in isolation.
