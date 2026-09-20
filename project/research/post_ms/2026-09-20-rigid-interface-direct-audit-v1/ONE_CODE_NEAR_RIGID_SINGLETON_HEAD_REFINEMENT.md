# One-code near-rigid cut — distinct singleton-head refinement

Date: 2026-09-20

Status: **same-session strengthening / hostile replay** of `ONE_CODE_NEAR_RIGID_SLOT_PRICE.md`. Conditional on the same exact near-rigid Hall event and `x>=3`. The purpose is to replace the gamma-compatible matched-fibre count by the smaller physical set of heads that can actually be singleton-certified.

## 1. Physical matched-head capacity

Assume `Y` has one tight code `d`. Let

`M_d={w : w is a tight matched endpoint, gamma(w)=d, |N(w) cap A_X|=1}`

and let

`rho:=|{h(w):w in M_d}|`

be the number of distinct `A_X` heads represented by those singleton endpoints.

The same-session correction to `RIGID_PRIVATE_COORDINATE_NORMAL_FORM.md` is important here: several physical singleton endpoints may have the same head. They are several private coordinates, but they do **not** allow one source to matched-certify several crossing heads. Thus `rho`, not `|M_d|`, is the exact physical upper bound on the number of distinct heads that can be matched-certified for one `d`-coded source.

For every source `s in Y`, if `k_s` is its selected U-witness count, then

> **`k_s >= k_rho:=[x-rho]_+`.**                           `(NRH-1)`

Hence

> **`k_*:=min_s k_s >= k_rho`.**                           `(NRH-2)`

Because every singleton endpoint counted by `rho` has gamma `d`, `rho<=g_P`; therefore `k_rho>=k_P=[x-g_P]_+`. This strictly strengthens the lower endpoint used in the original near-rigid `Theta` optimization whenever gamma-compatible fibres repeat heads or fail the singleton condition.

## 2. Hostile replay of the near-rigid slot derivation

The rest of the original theorem survives with the actual `k_*` unchanged:

1. one minimum-U source has `m=x-k_*` simultaneously matched-covered heads;
2. if `m>=3`, private coordinates imply no two of those heads are complementary and every internal edge of the covered set has Hamming distance at least two;
3. the exact near-equality provenance `J_X+kappa_X<1` gives `J_X<1`;
4. summing the local rooted Hamming inequality gives `J_X>=4e(H)/p`, hence `e(H)<p/4`;
5. deleting the `k_*` U-certified heads removes at most `k_*x-k_*(k_*+1)/2` internal X-edges;
6. with `2e_X=xg0-L_X+Z_X` and the physical floor `Z_X>=k_*(x-1)`, one obtains

   `2e(H)>=xg0-L_X-k_*(x-k_*)`;

7. therefore, when `k_*<=x-3`,

   > **`L_X > xg0-k_*(x-k_*)-p/2`.**                     `(NRH-LX)`

No step in this chain requires the full physical head map on all singleton matched endpoints to be injective; only the selected matched witnesses for one fixed source need distinct heads, which follows from their graph-fixed singleton sets.

## 3. Sharpened one-dimensional floor

Define, as before,

`ell(k):=max(0,floor(xg0-k(x-k)-p/2)+1)`.

Let

`F(k)=k(p-1)+ell(k)` for `k<=x-3`,

and

`F(k)=k(p-1)` for `k>=x-2`.

Then the physical distinct-head support permits the stronger floor

> **`Theta_rho(p,x,g0,rho):=min_{k_rho<=k<=x} F(k)`,**    `(NRH-THETA)`

and every near-rigid one-code cut satisfies

> **`L_A+E_U >= Theta_rho`.**                              `(NRH-SCORE)`

The pair-local gamma collision price remains logically separate. For actual `k_*<=x-3`, a safe combined form is

> `L_A+E_U >= k_*(p-1)+max{ell(k_*),phi(g_P)}`,

but the optimization domain now starts at `k_rho`, not merely `k_P`.

## 4. Rooted coupling

From `RIGID_SINGLETON_BUDGET_ROOTED_COLLAPSE.md`, any exact rigid cut satisfies

`g0<=lambda+1`.

In the one-code case, if `c:=lambda+1-g0`, then the physical U population already forces

`k_* >= [x-rho]_+`

and, whenever `x>p`, at least `u-c` physical U vertices lie in the mandatory complementary witness population. Thus the near-rigid optimization should retain the tuple

`(c,rho,k_*,g_P,L_X,E_U)`

rather than treating `g_P` alone as matched relief.

## 5. Audit conclusion

The near-rigid Hamming-slot theorem survives hostile replay at its stated scope, but its natural physical parameter is the **distinct singleton-head support `rho`**. Future diagnostics and exact pair-local optimization should use `k_*>=x-rho`, with `rho<=|M_d|<=g_P`, and should not count repeated private coordinates of one head as separate matched-certified crossing heads.