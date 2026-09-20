# Maximal m=2, p>=3, x=3: two-component reservoir and bounded-tail theorem

Date: 2026-09-20

Status: **internal candidate structural theorem**, conditional on the audited first-strict unique-hole setup, maximal raw eligibility matching number `m=2`, and the independently repaired same-code/selected-witness interface. This note follows `M2_FR_EXACT_HALL_CLOSURE.md`, which closes `x>=4` for `p>=3`.

## 1. Setup after the large-X closure

Assume maximal `m=2`, `p>=3`, `x=3`. Then `X'=X\{a_0}` has exactly two heads. The preserved `(NO-ONECODE)` theorem rules out a single X'-code class for `p>=3`, so the two heads have two distinct tight codes, say `C_1,C_2`, with disjoint nonempty agreement blocks.

The raw eligibility graph is the disjoint union of two code components. Since each component contains exactly one head and has matching number one, the physical outside reservoir splits as

`U_o=U_1 dotcup U_2`, `|U_i|=s_i>=1`, `s_1+s_2=omega`.

Every vertex of `U_i` has code `bar C_i`, is an eligible outside witness for the unique head of code `C_i`, is anticomplete to Y, and misses that head.

Write `k=3-g`, so `g in {0,1,2}`, and put

`tau=p-y>=1`.

## 2. Each physical code component is independent

### Lemma 2.1

> `G[U_i]` is edgeless for `i=1,2`.                     `(COMP-INDEP)`

### Proof

Suppose `zz'` is an edge inside one component. Its endpoints have the same U-code `bar C_i`. By the independently audited same-code raw-criticality theorem, a U-source on this edge requires an A-witness of complementary code `C_i`.

The only X'-vertex of code `C_i` is the component head `x_i`, and every physical witness in `U_i` is eligible for `bx_i`, hence is nonadjacent to `x_i`. If `a_0` also has code `C_i` (the Type-R possibility), every Type-R witness is adjacent to `a_0`, so `a_0` cannot be the required nonadjacent witness for the source orientation. No Y-vertex has code `C_i` because X'-codes are neither `d` nor `bar d`.

Thus neither orientation has the required singleton witness. `square`

Consequently the number of physically missing U--U pairs within the two components is at least

> `binom(s_1,2)+binom(s_2,2)`
> ` >= floor((omega-1)^2/4)`.                           `(COMP-QLOSS)`

## 3. Type-independent outside-reservoir score

A vertex `z in U_i` is anticomplete to all `y` vertices of Y, misses its certified head, and misses the other `s_i-1` vertices of its own component. Thus it has at least

`y+1+(s_i-1)=y+s_i`

located nonneighbours in `A union U`.

For a U-vertex, `epsilon_z=H_z+p-(x+y)` and here `x=3`. Therefore

> `epsilon_z >= p+s_i-3`.

Summing over the two components gives

> `E_{U_o} >= omega(p-3)+s_1^2+s_2^2`
> `          >= omega(p-3)+ceil(omega^2/2)`.            `(X3-UO-SCORE)`

The minimum occurs at the most balanced split.

## 4. Safe X-side Hall bill

The buffer contributes exactly one X--U nonedge, namely `ba_0`. Each common-core vertex has exactly one X-neighbour, hence contributes two X--U nonedges because `x=3`. Every physical outside witness misses at least its certified head. These located holes are disjoint, so

> `Z_X >= 1+2k+omega`.                                  `(X3-ZX)`

Since `e(X)<=binom(3,2)=3`, the exact Hall identity

`2e(X)=3(p-y)-L_X+Z_X`

gives

> `L_X >= 3tau+2k+omega-5`.                             `(X3-LX)`

The reverse-fan theorem still gives the exact Y bill

> `L_Y=y(p-g+1+omega)`.                                 `(X3-LY)`

For the rooted-slot side we retain only the universally safe local bound

> `r>=3+y`.                                             `(X3-RLOW)`

## 5. Relaxed analytic score and residual polynomials

Let

`u=k+1+omega`, `lambda=2p+omega-g-y`.

Use the disjoint physical lower bounds

- `(X3-LX)`;
- `(X3-LY)`;
- `E_core>=k(p+k)-1`;
- buffer slack `p-g+1`;
- `(X3-UO-SCORE)` weakened only by `ceil(omega^2/2)>=omega^2/2`.

For the triangle ceiling use

`q<=binom(u,2)-binom(k+1,2)-(k-1)-floor((omega-1)^2/4)`

and weaken

`floor((omega-1)^2/4)>=(omega-2)^2/4`.

Finally use `2 floor((lambda+1)^2/4)>=lambda(lambda+2)/2` in the weakening direction.

After multiplying by two, score feasibility implies

> `F>=0`, where
>
> `F=-g^2+2gp-2g tau-2g omega+8g`
> `  -p^2+2p tau-2p omega+2p`
> `  -tau^2+2tau omega+2tau+14omega-12`.                `(X3-F)`

After multiplying the residual inequality by four, feasibility implies

> `R>=0`, where
>
> `R=-2g^2+4gp+8g-2p^2-4pomega+16p`
> `  -2tau^2-8tau-omega^2+18omega-12`.                  `(X3-R)`

These are weakened necessary conditions: contradiction here is therefore sufficient.

## 6. p is absolutely bounded

Assume `p>=9`.

For fixed `p,omega`, `(X3-R)` is strictly decreasing in `tau>=1`. It is increasing on the allowed discrete range `g in {0,1,2}`, so its maximum occurs at `tau=1,g=2`.

For `p>=9`, its derivative in `omega>=2` is

`-4p-2omega+18<0`,

so the maximum also occurs at `omega=2`. Hence

> `R<=-2(p-9)(p+1)`.                                    `(P-CAP-R)`

Thus `p>9` is impossible. At `p=9`, equality in the relaxed residual bound forces the unique extremal choice

`tau=1`, `g=2`, `omega=2`.

Substitution into `(X3-F)` gives

`F=-24<0`.

Therefore

> **every maximal-m2, p>=3, x=3 survivor satisfies `p<=8`.** `(X3-P8)`

## 7. omega is absolutely bounded

Now assume `omega>=9`.

Again `(X3-R)` is strictly decreasing in `tau`, so maximize at `tau=1`; it is increasing in `g`, so maximize at `g=2`. For `omega>=9`, the resulting quadratic in `p>=3` has vertex `p=6-omega<3`, hence is decreasing throughout the allowed range. Therefore its maximum occurs at `p=3` and equals

> `R<=-(omega-10)(omega+4)`.                             `(OMEGA-R)`

Hence `omega>=11` is impossible. For `omega=9,10`, the only parameter choice with the relaxed residual condition `R>=0` is respectively

`(p,tau,g)=(3,1,2)`.

At these two points restore the **exact** balanced component costs rather than the relaxed quadratic floors:

- for `omega=9`, the exact rooted residual margin is `-1`;
- for `omega=10`, it is `-4`.

Thus both are impossible. Consequently

> **every maximal-m2, p>=3, x=3 survivor satisfies `omega<=8`.** `(X3-OMEGA8)`

The two exceptional calculations are literal substitutions in the exact inequalities of Sections 2--4; no bounded search is used in the proof.

## 8. Finite-order consequence

Since `y<=p-1`, `(X3-P8)` gives `y<=7`. Also

`u=k+1+omega<=3+1+8=12`.

The rooted partition has

`n=1+|A|+|B|=1+(3+y)+(2p+u)`.

Therefore

> `n<=1+10+28=39`.                                      `(X3-N39)`

Combining with `M2_FR_EXACT_HALL_CLOSURE.md` yields:

> **Conditional on the audited first-strict/maximal-selection setup, the entire maximal `m=2`, `p>=3` branch is finite-order: every survivor has `x=3` and `n<=39`.** `(M2-PGE3-FINITE)`

In particular this branch cannot support an unbounded sufficiently-large counterexample family.

## 9. Trust boundary and next move

This is an eventual-programme result, not an all-order closure: the remaining finite `n<=39` rows have not been classified as graphs, and the rigid complete-cut interface still lacks a positive actual-D2C fixture.

The next live branch is the small-fibre remainder `p<=2` under maximal `m=2`. It should be attacked structurally rather than by extending the finite scan. If that remainder is also absolutely bounded, maximal `m=2` is eliminated from the eventual problem even before the finite tail is reconstructed.
