# Beta-sensitive fan-hole and rooted-feedback theorem

Date: 2026-09-18

Status: follow-on finite theorem package for the live eventual / sufficiently-large D2C second-extremal programme. No global eventual theorem is claimed.

## 1. Inputs

For one A/U certificate fan with A-source `x`, order `d`, and external-hole masses

`g_i=epsilon_x+epsilon_{w_i}-(lambda+1)`,

put

`G_x=sum_i g_i`.

The fan equality/stability package proved

> `q >= max{0, binom((d-G_x)_+,2)-floor(G_x/2)}`.         `(FQLB)`

The preserved beta-sensitive U-edge theorem gives

> `q<=Q_beta:=au-B_beta+N_1`,                              `(BQ)`

where

`B_beta=sum_{z in A} ell_z`

and

`N_1=|{z in A:ell_z=1}|`.

The coarser bound `N_1<=a` gives

`Q_beta<=au-B_beta+a`.

These two inequalities can be combined without any asymptotic optimization.

## 2. Exact fan-hole floor from beta-sensitive q capacity

### Theorem 2.1 — beta-sensitive fan-hole floor

Every A/U certificate fan satisfies

> `G_x >= [d-floor(sqrt(2Q_beta+d))]_+`.                  `(BFH)`

Consequently also

> `G_x >= [d-floor(sqrt(2(au-B_beta+a)+d))]_+`.           `(BFH-c)`

Proof. If `G_x>=d`, the claim is immediate. Assume `G_x<d` and put

`r=d-G_x>0`.

From `(FQLB)` and `(BQ)`,

`binom(r,2)-floor(G_x/2) <= Q_beta`.

Since `G_x=d-r`,

`r(r-1) <= 2Q_beta + 2floor((d-r)/2)`

`          <= 2Q_beta+d-r`.

Therefore

`r^2<=2Q_beta+d`.

Thus

`r<=floor(sqrt(2Q_beta+d))`,

and `G_x=d-r` gives `(BFH)`. square

This theorem prices the equality model in exactly the regime in which the global beta machinery makes `q` scarce: a source cannot carry a large A/U fan with many zero-hole witnesses unless the global beta-sensitive U-edge budget is large enough to hold the resulting witness clique.

## 3. Exact cap on the zero-hole population

Let

`z_0=|{i:g_i=0}|`.

Every zero-hole witness lies in `U`, and any two zero-hole witnesses in the same fan are adjacent by the exact witness-neighbourhood normal form. Hence they form a clique in `U`.

### Theorem 3.1 — zero-hole population cap

> `binom(z_0,2)<=q<=Q_beta`,                               `(ZHC1)`

so

> `z_0 <= floor((1+sqrt(1+8Q_beta))/2)`.                  `(ZHC2)`

In particular, whenever `Q_beta=o(p^2)`, a linear A/U fan has only `o(p)` zero-hole witnesses.

If `Q_beta=O(p)`, then only `O(sqrt(p))` witnesses can be zero-hole.

This makes precise the sense in which the exact zero-hole U-clique equality model cannot dominate in a beta-saturated / sparse-U slice.

## 4. Rooted-triangle feedback

Write

`F_0=(p-lambda)(p+u)-D_M+1`.

The rooted-transfer floor is

`F_min=F_0+q`.

Therefore every A/U fan gives the direct lower bound

> `F_min >= F_0`
> ` + max{0,binom((d-G_x)_+,2)-floor(G_x/2)}`.            `(RFF)`

Thus the geometry used to certify the forced A-edge mass can itself increase the rooted-triangle count and hence increase the A-edge mass that must be certified.

This is a genuine feedback term, not present in the previous parameter-only fan cap.

## 5. Conditional fixed-point gate for the A/U branch

The preserved rooted-transfer fan dichotomy says that, with

`H=(F_min-sigma_0a)_+`,

one of the following occurs:

- a direct fan has order at least `H/a`; or
- an A/U fan has order at least `H/(2a)`.

On the A/U branch, choose such a fan. Then `(RFF)` yields the finite self-consistency condition

> `d >= (1/(2a))`
> ` [F_0`
> `  +max{0,binom((d-G_x)_+,2)-floor(G_x/2)}`
> `  -sigma_0a]_+`.                                       `(AFG)`

Together with `(BFH)`, this is an explicit two-variable gate in `(d,G_x)` whose coefficients are determined by the global near-full parameters and beta traffic.

The important strategic point is that `q` is no longer a free nuisance parameter in the A/U fan equality analysis: it is squeezed from below by the fan and from above by beta-source geometry.

## 6. Asymptotic reading

Suppose `d/p->alpha>0` and `Q_beta=o(p^2)`. Then `(BFH)` gives

> `G_x >= alpha p-o(p)`.                                  `(ABFH)`

So a linear fan in a sparse-U beta-saturated slice must carry asymptotically at least one unit of total hole mass per witness on average. At the same time `(ZHC2)` shows that only `o(p)` witnesses can be genuinely zero-hole.

This does not by itself close the branch: the cheapest surviving possibility is a near-one-hole fan rather than the exact zero-hole U-clique model. That is a useful narrowing of the equality frontier, not a global theorem.

The next local classification target should therefore be the **one-hole / bounded-hole fan**. The root `v` supplies a canonical single hole for A-witnesses, while U-witnesses require a different hole. Distinguishing those two mechanisms should interact with the Hamming localization theorem and the same-code witness-edge payment.

## 7. Scope

The mandatory 12-vertex, 32-edge `X_3` graph remains untouched: at its canonical root `u=0` and the rooted-transfer floor does not force the A/U fan branch.

The inequalities above are finite consequences of previously proved hand statements `(FQLB)` and `(BQ)`. They do not promote the false all-order 2019 conjecture or any eventual theorem.
