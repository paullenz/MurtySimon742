# Rigid Hall cuts — singleton-gamma budget sharpening

Date: 2026-09-20

Status: **same-session structural strengthening / hostile follow-on** conditional on the exact rigid Hall event `M_X=E_X=0`, `x=|A_X|>=3`. This sharpens `RIGID_GAMMA_BUDGET.md` by budgeting the matched resources that can actually be singleton-head witnesses, rather than all fibres whose gamma pair is compatible with a source code. It does not resolve reachability of the rigid event; the zero-positive-fixture caveat remains binding.

## 1. Singleton resources are globally scarce

Let `D` be the set of distinct source codes represented in `Y`, `h=|D|`, and `y_d=|Y_d|` for `d in D`.

For a represented source code `d`, define

`M_d := {w : w is a tight matched endpoint, gamma(w)=d, |N(w) cap A_X|=1}`,

`mu_d:=|M_d|`,

and let

`rho_d:=|{h(w):w in M_d}|`

be the number of **distinct A_X heads** that occur among those singleton endpoints. Then `rho_d<=mu_d`.

Fix one tight fibre `{q_i,r_i}`. Its two endpoints partition `A_X`, so

`d_{A_X}(q_i)+d_{A_X}(r_i)=x`.

Since `x>=3`, both degrees cannot equal one. Therefore **at most one endpoint of a tight fibre is a singleton on `A_X`**, irrespective of its gamma code. Summing over the `p` tight fibres gives

> `sum_{d in D} mu_d <= p`, and hence **`sum_{d in D} rho_d<=p`.** `(SGB-1)`

The head-support form is the sharper one for witness capacity: several singleton endpoints of the same gamma code may have the same head, but a fixed source can use matched singleton witnesses on at most `rho_d` distinct crossing heads.

## 2. Exact code-specific U demand

Fix a source `s in Y_d`. The direct rigid-interface audit proves that its `x` crossing edges require `x` distinct physical singleton-head witnesses, all in tight matched endpoints or `U`.

Its selected matched witnesses have distinct heads. Every such head belongs to the physical head-support set counted by `rho_d`. Therefore at most `rho_d` crossing heads can be matched-certified, and every `d`-coded source needs at least

> `k_d := [x-rho_d]_+`                                    `(SGB-2)`

physical `U` witnesses.

This is at least as strong as the endpoint-count version `[x-mu_d]_+` and can be strictly stronger when one head has several private coordinates.

Every such `U` witness has tight code `bar d`. Distinct source codes have distinct complementary `U`-code classes. Thus, writing

`K:=sum_{d in D} k_d`,

we have

> **`u>=K`.**                                              `(SGB-3)`

Using `[x-rho_d]_+ >= x-rho_d` and `(SGB-1)`,

`K >= h x-sum_d rho_d >= h x-p`.

Since `K>=0`,

> **`K >= [h x-p]_+`, and therefore `h x <= u+p`.**       `(SGB-4)`

This improves the previous universal diversity obstruction `h x<=u+2p` to `h x<=u+p` **without** assuming that `Y` contains at most one code from each complementary pair.

## 3. Located A--U deficit forced by the same population

For each represented code `d`, let `W_d subseteq U_bar d` be the union of physical U-witnesses used by the `d`-coded sources. Then `|W_d|>=k_d`, and the sets `W_d` are disjoint across distinct `d`.

Every `w in W_d` is a singleton on `A_X`, so it misses `x-1` vertices of `A_X`. Therefore

> `Z_X >= (x-1)K`.                                        `(SGB-ZX)`

Each of the `y_d` sources of code `d` uses at least `k_d` distinct U-witnesses and is nonadjacent to each selected witness. Reuse by another source does not merge these source--witness nonedge pairs. Hence

> `Z_Y >= sum_d y_d k_d`.                                 `(SGB-ZY)`

Since every `y_d>=1`, `(SGB-ZX)` and `(SGB-ZY)` give the compact global consequence

> **`Z >= xK >= x[h x-p]_+`.**                            `(SGB-Z)`

A multiplicity-sensitive companion bound follows from `k_d >= x-rho_d`:

`sum_d y_d k_d >= x y-sum_d y_d rho_d`.

Because `max_d y_d <= y-h+1` and `sum_d rho_d<=p`,

> **`Z_Y >= [x y-p(y-h+1)]_+`.**                          `(SGB-ZY2)`

This bound is sometimes stronger than merely replacing `sum_d y_d k_d` by `K`.

## 4. U-slack price

Retain the rooted parameter

`g0=p-y`.

For `w in W_d`, let `t_w` be the number of `d`-coded sources using `w`. The raw singleton-head degree count gives

`epsilon_w >= [g0+t_w-1]_+`,

and

`sum_{w in W_d} t_w >= y_d k_d`.

When `g0>=1`, truncation disappears and

`sum_{w in W_d} epsilon_w`
` >= (g0-1)|W_d|+sum_w t_w`
` >= k_d(g0-1+y_d)`.

Thus

> **`E_U >= sum_d k_d(g0-1+y_d) >= g0 K >= g0[h x-p]_+`.** `(SGB-EU+)`

When `g0<=1`, the predecessor convex-truncation argument remains valid with the sharper distinct-head demand `k_d`:

> **`E_U >= [sum_d y_d k_d-(1-g0)u]_+`.**                 `(SGB-EU-)`

## 5. Audit of possible double counting

The sharpening uses three physically different statements and does not identify incidences that are only witness selections:

1. `(SGB-1)` counts physical tight matched singleton endpoints and then their distinct head support. One fibre contributes at most one endpoint, and `rho_d<=mu_d` prevents repeated private coordinates of one head from being treated as extra crossing heads.
2. `(SGB-3)` counts physical U vertices in disjoint tight-code classes. Reuse across sources of the same code is allowed; only the population required by one source is retained.
3. `(SGB-ZY)` counts physical source--U nonedges. If one U witness is reused by several sources, those are still different graph nonedges, so the multiplicity is legitimate.

No selected `(source,coordinate)` injectivity theorem is needed beyond the direct rigid singleton-head fact that one fixed source requires distinct witnesses for its distinct crossing heads.

## 6. Strategic consequence

Any exact rigid Hall cut with `x>=3` and `h` represented outside source codes must pay, before pair-local one-code purification,

- `u>= [h x-p]_+` physical complementary-code U vertices;
- `Z>=x[h x-p]_+` located A--U holes;
- and, for `g0>=1`, `E_U>=g0[h x-p]_+` U-slack.

The correct next step is to feed these sharpened singleton-resource bills into the exact rooted identity and the Hall near-equality provenance, while keeping pair-local quantities separate. In the one-code case `h=1`, the sharper objects are the exact distinct-head support `rho_d`, the actual per-source U count, and the private-coordinate theorem; in the multi-code case `(SGB-4)` should replace the older universal `u+2p` relaxation.