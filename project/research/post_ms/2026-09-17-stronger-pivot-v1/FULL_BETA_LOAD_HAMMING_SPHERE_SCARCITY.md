# Full beta-load witnesses are Hamming-sphere scarce

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal candidate exact combinatorial lemma in the selected near-full system; external review open.

The ratio-two polarization theorem suggests beta-heavy A-vertices with load close to `p`. This note isolates the exact endpoint `ell_x=p` and shows that genuinely full-load witnesses are extremely scarce when `u=O(p)`. The argument uses only the one-coordinate-deviation geometry and a hypercube incidence count.

---

## 1. A full-load witness forces a complete Hamming sphere in U-support

Let `x in A` satisfy

`ell_x=p`.

Then `I_x=[p]`. Put `c=c(x)`.

For every coordinate `i`, the designated beta source `y_i` differs from `x` at `i` and agrees with `x` at every other target coordinate. Since every coordinate is targeted,

> `c(y_i)=c Delta {i}`.                                  (1.1)

The `p` sources are distinct. Therefore every Hamming neighbour of `c` occurs as a U-code:

> `N_H(c)={c Delta {i}:1<=i<=p} subseteq supp(U)`.       (1.2)

So every distinct full-load centre consumes an entire radius-one sphere in the U-code support.

---

## 2. Only constantly many distinct full-load centres when u=O(p)

Let

`C={c(x):x in A, ell_x=p}`

be the set of distinct full-load centre codes, and put `m=|C|`. Let

`S=supp(U)`

be the set of distinct U-codes. Then `|S|<=u` and, by (1.2), every `c in C` has all `p` Hamming neighbours in `S`.

Consider the bipartite incidence graph between `C` and `S`, joining codes at Hamming distance one. Every centre has degree `p`, so

`sum_{z in S} d_C(z)=mp`.                                (2.1)

Two distinct hypercube vertices have at most two common Hamming neighbours: exactly two when their mutual Hamming distance is two, and none otherwise. Hence

`sum_{z in S} binom(d_C(z),2)<=2 binom(m,2)=m(m-1)`.     (2.2)

Therefore

`sum_{z in S} d_C(z)^2<=mp+2m(m-1)`.                    (2.3)

Cauchy--Schwarz now gives

`m^2 p^2`

`<=|S| [mp+2m(m-1)]`

`<=u m[p+2m-2]`.                                         (2.4)

If `m>0` and `p^2>2u`, rearrangement yields

> **FULL-LOAD CENTRE BOUND**
>
> `m <= u(p-2)/(p^2-2u)`.                                (2.5)

In particular, for every fixed `rho` with `u<=rho p+o(p)`, the number of distinct full-load centre codes is `O_rho(1)`.

At the ratio-two frontier `u/p -> 2`, (2.5) gives

> `m<=2`                                                 (2.6)

for all sufficiently large `p`.

---

## 3. Multiplicity at one centre is also constant

Fix a full-load centre code `c`, and let

`N_c=|{x in A:c(x)=c, ell_x=p}|`.

For any coordinate `i`, all these A-vertices beta-certify obligations with the same matched target, namely the endpoint opposite `c_i`. Their designated sources must be distinct, because one physical source--fibre obligation has only one selected witness.

By (1.1), every such source has exact U-code `c Delta {i}`. Hence

`N_c<=t_{c Delta {i}}`                                   (3.1)

for every `i`.

The `p` neighbour codes `c Delta {i}` are distinct, so summing (3.1) over coordinates gives

`pN_c<=sum_i t_{c Delta {i}}<=u`.                        (3.2)

Therefore

> `N_c<=floor(u/p)`.                                     (3.3)

Combining (2.5) and (3.3):

> **FULL-LOAD WITNESS SCARCITY**
>
> `|{x in A:ell_x=p}|`
>
> `<= floor(u/p) * floor(u(p-2)/(p^2-2u))`              (3.4)
>
> whenever `p^2>2u`.

At `u/p -> 2`, the right side is eventually at most

> `4`.                                                    (3.5)

Thus the ratio-two polarization cannot be realised by a linear population of exactly full-load witnesses. The beta-heavy population must remain slightly below full load, even though its average deficit is `o(p)`.

---

## 4. Strategic consequence

This does not by itself improve the asymptotic ratio below two: a load `p-o(p)` can evade the exact radius-one sphere count by leaving `o(p)` coordinates untargeted. But it removes the simplest equality model and identifies the next finite-width object:

> quantify how many A-vertices can have beta deficit `k=p-ell_x` when `k=o(p)`.

Any strengthening of (3.4) from `k=0` to `k=O(sqrt(p))` would feed directly into the product defect

`J=sum_x(p-ell_x)(u-d_U(x))`

and may improve the additive `O(sqrt(p))` error in the directional ratio-two theorem.

The order-12/32 `X_3` graph has `u=0` and is untouched.

---

## 5. Trust boundary

- The Hamming-sphere inclusion (1.2) is the exact full-load case of the preserved beta-reuse exclusion theorem.
- The incidence bound (2.5) is elementary hypercube counting.
- The multiplicity bound (3.3) uses only source-coordinate selected-witness uniqueness.
- No asymptotic finite-deficit extension is claimed here.
