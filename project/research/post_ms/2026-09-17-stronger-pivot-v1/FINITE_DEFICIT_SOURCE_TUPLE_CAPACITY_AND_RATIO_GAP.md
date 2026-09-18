# Finite-deficit beta-source tuple capacity and a strict ratio gap below two

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal candidate structural theorem. The source-tuple inequalities below are exact hand combinatorics in the selected near-full system. The final ratio bound is an asymptotic internal candidate for fixed `lambda`, conditional only on the already-preserved near-full framework. External review open.

This note continues the directional ratio-two attack rather than returning to row classifications. The key observation is that a beta-heavy witness with only `k=p-ell_x` untargeted fibres forces every pair, and more generally every fixed tuple, of its designated unmatched sources into a very small Hamming pattern. Source-coordinate selected-witness uniqueness then gives a weighted capacity inequality which becomes singular as `k` tends to zero.

The first consequence is that the ratio-two polarization described in `RATIO_TWO_POLARIZATION_AND_SOURCE_PAIR_STABILITY.md` cannot actually occur. A quantitative triple-source specialization then pushes the fixed-`lambda` asymptotic frontier strictly below `27/14`.

---

## 1. Setup

Retain the partial-Boolean notation. For `x in A`, let

- `I_x subseteq [p]` be its beta target fibres;
- `ell_x=|I_x|`;
- `k_x=p-ell_x` be its **beta deficit**;
- `Y_x={y_i:i in I_x}` be its pairwise-distinct designated unmatched beta sources.

For every `i in I_x`, beta-reuse geometry says

`c(y_i)|_{I_x}=c(x)|_{I_x} Delta {i}`.                 (1.1)

Therefore for distinct `i,j in I_x`,

`dist_H(c(y_i),c(y_j)) <= k_x+2`.                       (1.2)

The preserved beta-source-pair theorem also gives, for distinct `y,z in U`,

`M(y,z):=|{x:{y,z} subseteq Y_x}| <= dist_H(c(y),c(z))`. (1.3)

---

## 2. Exact weighted pair-capacity theorem

Fix an unordered source pair `{y,z}` with Hamming distance `d>0`. For every common witness `x` containing the pair, (1.2) gives

`d <= k_x+2`,

so

`1/(k_x+2) <= 1/d`.

Summing over the common witnesses and using (1.3),

`sum_{x:{y,z} subseteq Y_x} 1/(k_x+2)`

`<= M(y,z)/d <=1`.                                      (2.1)

Pairs with `d=0` occur in no `Y_x`, because two distinct designated sources differ on their two assigned target coordinates.

Now sum (2.1) over all unordered pairs of `U`:

> **FINITE-DEFICIT PAIR CAPACITY**
>
> `sum_{x in A} binom(ell_x,2)/(p-ell_x+2) <= binom(u,2)`.   `(FDP2)`

This is exact and finite.

### Heavy-witness scarcity

For an integer `K` with `0<=K<=p-2`, let

`N_K=|{x in A:k_x<=K}|`.

Every such witness has `ell_x>=p-K`, so `(FDP2)` gives

> `N_K <= binom(u,2)(K+2)/binom(p-K,2)`.                 `(2.2)`

If `u=rho p+o(p)` and `K=o(p)`, then

`N_K <= (rho^2+o(1))K`.                                  (2.3)

Thus only `O(K)` A-vertices can have beta deficit at most `K` when `u=O(p)`. The full-load scarcity theorem is the endpoint `K=0`; (2.2) extends it to every finite or sublinear deficit.

---

## 3. Higher-order designated-source capacity

The pair inequality is only the first member of a hierarchy.

Fix an integer `r>=3` and an unordered `r`-set `R subseteq U`. For each `y in R`, let `a_y(R)` be the number of coordinates at which `y` is the unique member of `R` whose bit differs from the other `r-1` members. Put

`T(R)=|{i: the r code bits in coordinate i are not all equal}|`.

Suppose `R subseteq Y_x`. Each `y in R` is assigned by `x` to one target coordinate `i_x(y)`. At that coordinate `y` differs from `c(x)` and every other member of `R` agrees with `c(x)`, so `i_x(y)` is counted by `a_y(R)`.

All target coordinates of `x` other than these `r` assigned coordinates are constant on `R`: every member of `R` is then an "other designated source" and agrees with `x` there. Therefore every additional nonconstant coordinate of `R` must lie outside `I_x`, whence

`T(R) <= k_x+r`.                                         (3.1)

Across two distinct common witnesses containing `R`, the assignment coordinate of a fixed physical source `y` cannot repeat, because the selected witness for the source-coordinate obligation `(y,i)` is unique. Hence if

`M_R=|{x:R subseteq Y_x}|`,

then

`M_R <= min_{y in R} a_y(R)
     <= (sum_{y in R}a_y(R))/r
     <= T(R)/r`.                                         (3.2)

If `T(R)=0`, then `M_R=0`. Otherwise, from (3.1),

`sum_{x:R subseteq Y_x} 1/(k_x+r)
 <= M_R/T(R)
 <=1/r`.                                                  (3.3)

Summing over all `r`-sets gives:

> **SOURCE-TUPLE CAPACITY HIERARCHY.** For every integer `r>=3`,
>
> `sum_{x in A} binom(ell_x,r)/(p-ell_x+r)
>  <= (1/r) binom(u,r)`.                                  `(FDPr)`

Consequently, if

`N_K^{(r)}=|{x:k_x<=K}|`

and `p-K>=r`, then

> `N_K^{(r)} <= ((K+r)/r) * binom(u,r)/binom(p-K,r)`.     `(3.4)`

For fixed `r`, `u=rho p+o(p)` and `K=o(p)`,

`N_K^{(r)} <= ((rho^r/r)+o(1))K`.                        (3.5)

At the ratio-two endpoint, `r=3` improves the pair coefficient from `4K` to `(8/3)K`.

---

## 4. Ratio two is impossible

Assume, for contradiction, a fixed-`lambda` above-`M(n)` sequence with

`p -> infinity`, `u/p ->2`.

The preserved ratio-two polarization theorem supplies a set `X subseteq A` with

`|X|=(2+o(1))p`,

`D_X:=sum_{x in X} k_x=o(p^2)`.                          (4.1)

Choose any integer sequence `K_p` such that

`K_p=o(p)` and `D_X/K_p=o(p)`;

for example, if `D_X>0`, one may take `K_p=ceil(sqrt(D_X))`, with the trivial bounded adjustment when `D_X=0`.

By Markov,

`|{x in X:k_x>K_p}| <= D_X/K_p=o(p)`,

so

`N_{K_p} >= (2-o(1))p`.                                  (4.2)

But `(2.2)` gives

`N_{K_p} <= (4+o(1))K_p=o(p)`,                           (4.3)

a contradiction.

Therefore:

> **ENDPOINT EXCLUSION.** No fixed-`lambda` above-threshold near-full sequence can satisfy `u/p ->2`.

Combined with the directional theorem `limsup u/p<=2`, this already implies a nonquantitative strict gap below two for every fixed `lambda`.

---

## 5. A quantitative triple-source gap

The same mechanism yields an explicit gap without invoking the endpoint polarization theorem.

Suppose a fixed-`lambda` above-threshold sequence has

`u/p -> rho`,

where initially `rho<=2` by the directional ratio theorem. The preserved directional deficiency--Hamming budget gives

`J <= [rho(2-rho)/2+o(1)]p^3`,                           (5.1)

`H <= [rho(2-rho)+o(1)]p^3`,                             (5.2)

where

`J=sum_x (p-ell_x)(u-d_U(x))`.

### 5.1 Bad fibres at threshold `p`

Let

`K_0={i:|d_i|>=p}`, `j=|K_0|`.

From (5.2),

`j/p <= gamma+o(1)`,

where

`gamma=rho(2-rho)`.                                      (5.3)

Let

`L={x:ell_x>j}`, `l=|L|`.

Since

`B=sum_x ell_x=pu-h_alpha=rho p^2+o(p^2)`,

while a vertex outside `L` contributes at most `j` and one inside contributes at most `p`,

`B <= lp+(a-l)j`.

Using `a=(rho+2)p+o(p)` and (5.3),

> `l/p >= L_0(rho)+o(1)`,                                (5.4)
>
> `L_0(rho)=[rho-(rho+2)gamma]/(1-gamma)`.

Every `x in L` targets at least one coordinate outside `K_0`; the side-occupancy lemma therefore gives

`d_U(x) <= (u+p)/2+o(p)`,

so

`u-d_U(x) >= [(rho-1)/2+o(1)]p`.                         (5.5)

Combining (5.1) and (5.5),

> `sum_{x in L} k_x <= [D_0(rho)+o(1)]p^2`,              (5.6)
>
> `D_0(rho)=rho(2-rho)/(rho-1)`.

### 5.2 Deficit threshold `p/6`

Let

`L'= {x in L:k_x<=p/6}`.

By (5.6),

`|L'|/p >= L_0(rho)-6D_0(rho)+o(1)`.                    (5.7)

Apply the exact triple-source inequality `(FDP3)` with `K=floor(p/6)`. It gives asymptotically

`|L'|/p <= 12rho^3/125+o(1)`.                            (5.8)

Hence every possible limit ratio `rho in (1,2]` must satisfy

> `F(rho):=L_0(rho)-6D_0(rho)-12rho^3/125 <=0`.          `(5.9)`

Direct simplification gives

`F(rho)`

`= -rho(12rho^4-24rho^3-863rho^2+2250rho-1125)`

`  /[125(rho-1)^2]`.                                     (5.10)

At

`rho_0=27/14`,

`F(rho_0)=219672/7245875>0`.                             (5.11)

Let

`P(rho)=12rho^4-24rho^3-863rho^2+2250rho-1125`.

On `[27/14,2]`,

`P''(rho)=2(72rho^2-72rho-863)<0`,

so `P'` is decreasing. Also `P'(27/14)<0`, hence `P` is decreasing there; finally

`P(27/14)=-4068/2401<0`.

Therefore `P(rho)<0` and hence `F(rho)>0` throughout `[27/14,2]`, contradicting the necessary inequality (5.9).

We obtain:

> **TRIPLE-SOURCE RATIO GAP — internal candidate.**
>
> For every fixed `lambda`, any above-`M(n)` near-full sequence with `p->infinity` satisfies
>
> `limsup u/p < 27/14 = 1.928571428...`.                  `(RG3)`

This strictly supersedes the directional endpoint `limsup u/p<=2`. The constant `27/14` is deliberately chosen for a short exact proof; no claim of optimization is made.

---

## 6. Strategic consequence

The ratio-two bipolar model is not merely unstable; it is impossible because a linear population of beta-heavy witnesses would require too many finite-deficit designated-source spheres inside only `O(p)` unmatched vertices.

The surviving fixed-`lambda` near-full branch is now quantitatively separated from ratio two. The next useful target is not decimal optimization of `(RG3)`. The more structural question is whether the tuple-capacity hierarchy can be combined directly with the exact beta-side hole identity and A-side slack to force a payment in `E_U+L_A` throughout the remaining `u/p<27/14` regime.

A promising finite object is the joint distribution of

`(k_x, epsilon_x, d_U(x))`:

- `(FDPr)` penalizes small `k_x`;
- `(BH)` turns small `epsilon_x` into near-exhaustion of every targeted fibre side;
- `(DHB)` penalizes simultaneous beta deficit and U-degree deficit.

A convex or dyadic decomposition using all three quantities may attack `(GS-A)` directly, rather than through another asymptotic ratio constant.

---

## 7. Trust boundary

- `(FDP2)` and `(FDPr)` are exact hand double counts using only the already-preserved designated-source geometry and source-coordinate selected-witness uniqueness.
- `(RG3)` uses the preserved fixed-`lambda` estimates `h_alpha,q=O(p^(3/2))`, `E_U=O(p)`, the directional deficiency--Hamming budget, and side occupancy. It is asymptotic, not a finite threshold theorem.
- No statement is made for arbitrary growing `lambda`.
- The separate `Q=0` / false-twin-core branch remains open.
- The published 12-vertex/32-edge `X_3` graph has `u=0` and is untouched.
- No all-order second-extremal claim is made.