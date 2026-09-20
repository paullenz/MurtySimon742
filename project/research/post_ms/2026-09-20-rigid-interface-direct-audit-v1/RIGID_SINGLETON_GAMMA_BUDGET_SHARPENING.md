# Rigid Hall cuts — singleton-gamma budget sharpening

Date: 2026-09-20

Status: **same-session structural strengthening / hostile follow-on** conditional on the exact rigid Hall event `M_X=E_X=0`, `x=|A_X|>=3`. This sharpens `RIGID_GAMMA_BUDGET.md` by budgeting the matched resources that can actually be singleton-head witnesses, rather than all fibres whose gamma pair is compatible with a source code. It does not resolve reachability of the rigid event; the zero-positive-fixture caveat remains binding.

## 1. Singleton resources are globally scarce

Let `D` be the set of distinct source codes represented in `Y`, `h=|D|`, and `y_d=|Y_d|` for `d in D`.

For a represented source code `d`, define

`mu_d := |{w : w is a tight matched endpoint, gamma(w)=d, |N(w) cap A_X|=1}|`.

The key point is that these are the matched endpoints that are physically capable of serving as rigid singleton-head witnesses for a `d`-coded source.

Fix one tight fibre `{q_i,r_i}`. Its two endpoints partition `A_X`, so

`d_{A_X}(q_i)+d_{A_X}(r_i)=x`.

Since `x>=3`, both degrees cannot equal one. Therefore **at most one endpoint of a tight fibre is a singleton on `A_X`**, irrespective of its gamma code. Summing over the `p` tight fibres gives the global budget

> **`sum_{d in D} mu_d <= p`.**                            `(SGB-1)`

This is strictly sharper for the present purpose than the earlier bound `sum_d g_{P(d)}<=2p`, because a gamma-compatible endpoint that is not singleton on `A_X` cannot certify a rigid crossing edge.

## 2. Exact code-specific U demand

Fix a source `s in Y_d`. The direct rigid-interface audit proves that its `x` crossing edges require `x` distinct physical singleton-head witnesses, all in tight matched endpoints or `U`.

At most `mu_d` of those witnesses can be matched endpoints. Hence every `d`-coded source needs at least

> `k_d := [x-mu_d]_+`                                     `(SGB-2)`

physical `U` witnesses.

Every such `U` witness has tight code `bar d`. Distinct source codes have distinct complementary `U`-code classes. Thus, writing

`K:=sum_{d in D} k_d`,

we have

> **`u>=K`.**                                              `(SGB-3)`

Using `[x-mu_d]_+ >= x-mu_d` and `(SGB-1)`,

`K >= h x-sum_d mu_d >= h x-p`.

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

A multiplicity-sensitive companion bound follows from `k_d >= x-mu_d`:

`sum_d y_d k_d >= x y-sum_d y_d mu_d`.

Because `max_d y_d <= y-h+1` and `sum_d mu_d<=p`,

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

When `g0<=1`, the predecessor convex-truncation argument remains valid with the sharper singleton demand `k_d`:

> **`E_U >= [sum_d y_d k_d-(1-g0)u]_+`.**                 `(SGB-EU-)`

## 5. Audit of possible double counting

The sharpening uses three physically different statements and does not identify incidences that are only witness selections:

1. `(SGB-1)` counts **physical tight matched endpoints** with singleton `A_X` neighbourhoods. One fibre contributes at most one.
2. `(SGB-3)` counts **physical U vertices** in disjoint tight-code classes. Reuse across sources of the same code is allowed; only the population required by one source is retained.
3. `(SGB-ZY)` counts **physical source--U nonedges**. If one U witness is reused by several sources, those are still different graph edges/nonedges, so the multiplicity is legitimate.

No selected `(source,coordinate)` injectivity theorem is needed beyond the direct rigid singleton-head fact that one fixed source requires distinct witnesses for its distinct crossing heads.

## 6. Strategic consequence

The empirical zero-fixture problem is now more constrained. Any exact rigid Hall cut with `x>=3` and `h` represented outside source codes must pay, before pair-local one-code purification,

- `u>= [h x-p]_+` physical complementary-code U vertices;
- `Z>=x[h x-p]_+` located A--U holes;
- and, for `g0>=1`, `E_U>=g0[h x-p]_+` U-slack.

The correct next step is to feed these sharpened singleton-resource bills into the exact rooted identity and the Hall near-equality provenance, while keeping pair-local quantities separate. In the one-code case `h=1`, the sharper object is still the exact `mu_d` / actual `k_*` tradeoff and the private-coordinate theorem; in the multi-code case `(SGB-4)` is a new global obstruction that should replace the older `u+2p` relaxation.