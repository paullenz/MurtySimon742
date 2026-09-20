# One-code rigid cut — rooted Q feedback from independent used witnesses

Date: 2026-09-20

Status: **same-session structural consequence**, conditional on the rigid one-code near-equality interface. It uses the independently replayed fact that the selected complementary-U witness union is independent. No finite scan is used.

The purpose is to feed the new physical witness theorem back into the exact rooted triangle channel `q=e(G[U])`, rather than using it only as a total-score price.

## 1. Minimum-source split

Fix a source in `Y=A_d` with minimum selected U-witness count k. Put

`d_U:=u-k`.

Then

`k=u-d_U`,

`m=x-k=p-c+d_U`,

where `c=lambda+1-g0` and `x=p+u-c`.

Let `W_s` be the k selected U-witnesses of this source. Since `W_s` is contained in the global used-witness union W, the hostile replay of the used-witness theorem gives

> `G[W_s]` independent.                                  `(QF-1)`

## 2. Exact U-edge ceiling

Every U-edge must therefore either join `W_s` to the `d_U` escaping vertices or lie completely among those escaping vertices. Hence

> **`q <= k d_U+binom(d_U,2)`**                           `(QF-2)`
>
> `   =d_U u-d_U(d_U+1)/2`.

Equivalently the independent selected witness set removes at least

> `binom(k,2)`

potential U-edges from the rooted triangle reservoir.

Since the predecessor occupancy theorem gives `d_U<=c`, `(QF-2)` already couples the rooted triangle count to the rooted gap. After private-coordinate exhaustion, whenever `k>0` one has the sharper `d_U<=c-1`.

In particular, for `k>0` and `c>=1`,

> `q <= (c-1)u-c(c-1)/2`                                 `(QF-3)`

whenever the right side is evaluated at the largest allowed escape `d_U=c-1` and `c-1<=u-1`; smaller actual `d_U` only strengthens the exact formula `(QF-2)`.

## 3. Located A--U deficit supplied by the same witnesses

Across all sources, every source uses at least k U-witnesses. Ordered selected `(source,witness)` pairs are distinct physical Y--U nonedges, so

> `Z_Y>=yk`.                                              `(QF-4)`

Every used U-witness has exactly one X-neighbour, so the global used-witness union has size at least k and gives

> `Z_X>=k(x-1)`.                                         `(QF-5)`

Therefore

> **`Z>=k(x+y-1)`.**                                      `(QF-6)`

For the same minimum source, the m selected matched singleton heads force `g_P>=m`, so the preserved gamma-collision price gives

> `L_A>=phi(m)`,                                          `(QF-7)`

where `phi(m)=m(m-1)` for `m>=3` and zero for `m<=2`.

## 4. Eliminate E_U from the rooted identity

Use the exact rooted identity

> `Z=u(p-lambda)+2q+E_U`                                  `(QF-8)`

and the above-M score ceiling

> `E_U+L_A<=C0`.                                          `(QF-9)`

Adding `L_A` to `(QF-8)` and applying `(QF-9)` gives

`Z+L_A <= u(p-lambda)+2q+C0`.

Now substitute `(QF-2)`, `(QF-6)`, and `(QF-7)`. Every survivor must satisfy the exact minimum-source necessary inequality

> **`(u-d_U)(x+y-1)+phi(p-c+d_U)`**
> **` <= u(p-lambda)+2d_Uu-d_U(d_U+1)+C0`.**              `(QF-10)`

This is a rooted-Q feedback inequality: the same selected witnesses that create located A--U holes also delete U--U triangle capacity.

It keeps the physical escape count `d_U` explicit. It is therefore strictly more informative than replacing `q` by `binom(u,2)` before the minimum-source geometry is used.

## 5. The residual-dimension form

Put

`r:=c-d_U=p-m`.

Then private-coordinate exhaustion says `r>=1` whenever `k>0`, and

`k=u-c+r`,

`m=p-r`,

`d_U=c-r`.

Thus `(QF-10)` can be written entirely in the residual Boolean dimension r:

> `(u-c+r)(x+y-1)+phi(p-r)`
>
> `<=u(p-lambda)+2(c-r)u-(c-r)(c-r+1)+C0`.               `(QF-R)`

This is the form to use when the post-exhaustion frontier is split into `r=1`, bounded r, and large-r regimes.

## 6. Strategic consequence

The one-code large-gap problem now has two independent physical effects tied to the same `r`:

1. the U-certified heads occupy at most `2^r-1` nonempty residual Boolean supports;
2. the used U-witness set has size at least `u-c+r` and removes `binom(u-c+r,2)` potential rooted U-edges.

The next structural attack should keep both facts simultaneously. If a new scaling family survives `(QF-R)`, it should be characterized in r-normal form rather than hidden inside another total-score minimization.