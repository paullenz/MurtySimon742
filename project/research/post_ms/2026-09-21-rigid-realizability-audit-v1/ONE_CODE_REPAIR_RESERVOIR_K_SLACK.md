# Complementary repair vertices add their own U-slack bill

Date: 2026-09-21

Status: structural/score lemma inside the repeated rigid one-code near-equality face `e=u-k=p`. Conditional on reaching the rigid interface; no graph-level reachability claim.

## 1. Setup

Use the exact spectrum from `ONE_CODE_BOUNDARY_REPAIR_RESERVOIR.md`:

`U = K disjoint_union W`,

where `|K|=k`, every vertex of K has code `bar d`, and `W={w_1,...,w_p}` consists of the one-match boundary vertices. The set K is the selected complementary-U witness population of a minimum outside source.

Let `t_z` be the number of outside sources `y in Y=A_d` for which a fixed `z in K` is used as a selected complementary U-witness.

## 2. Direct rooted deficit identity

For any unmatched rooted neighbour `z in U`, let

- `z_A` be the number of missing A-neighbours of z;
- `m_U(z)` be the number of missing U-neighbours of z.

Because z sees the root and exactly one endpoint of every tight pair,

`deg(z)=1+p+(u-1-m_U(z))+(a-z_A)`.

Since the root degree is `b=2p+u`, the standard rooted deficit is

> **`epsilon_z = z_A + m_U(z) - (a-p)`.**                `(2.1)`

## 3. A selected complementary witness costs A-holes

If z is used as the U-witness for a crossing edge sourced at `y in Y`, then the singleton-head property gives exactly one neighbour of z in X. Hence z misses at least `x-1` vertices of X. It also misses the source y itself. If z is used for `t_z` distinct outside sources, then

`z_A >= (x-1)+t_z`.

Dropping the nonnegative U-missing term from `(2.1)` yields

`epsilon_z >= x-1+t_z-(a-p)`.

Using `a=x+y` and `g0=p-y`,

> **`epsilon_z >= g0+t_z-1`.**                           `(3.1)`

This is the local singleton-head slack inequality rederived directly from the rooted partition.

## 4. Sum over K

Every outside source has at least k selected complementary U-witnesses. On the exact `e=p` spectrum the only U-vertices of complementary code are the k vertices of K, so the total selected source-witness incidence satisfies

`sum_{z in K} t_z >= yk`.

Because the repeated large-gap branch has `g0>=1`, summing `(3.1)` gives

`E_K >= yk+k(g0-1)`

and therefore

> **`E_K >= k(p-1)`.**                                  `(4.1)`

The sets K and W are disjoint. Combining `(4.1)` with the independently proved boundary-layer bill

`E_W >= p(2p-1)`

gives the stronger total floor

> **`E_U >= p(2p-1)+k(p-1)`.**                          `(4.2)`

## 5. Significance

The complementary vertices that repair the diameter-two failures are not free. Enlarging K increases the score bill linearly by at least `p-1` per repair vertex in addition to the quadratic cost already forced by W.

This sharply changes the repair-budget arithmetic: on the old `lambda=p` hostile spine, the denominator in the score comparison collapses from order p to the constant 3 after cancellation, forcing `k=Omega(p^2)` rather than merely `Omega(p)`.

## 6. Scope

No global selected `(source,coordinate)` uniqueness, source-tuple capacity theorem, rooted-Q inequality, or H--U private-foot argument is used. The only selected-system input is that each outside source has at least k complementary U-witnesses and those witnesses are physical vertices in K; the slack inequality is rederived from raw rooted degrees.
