# Above-threshold slack stability forces large row cover and caps alpha twin classes

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: internal candidate structural theorem; not externally reviewed.** This note combines three already-preserved ingredients:

1. the row-kernel theorem;
2. the projective-twin interpretation of alpha-code multiplicity;
3. the zero-signing-subcore/slack stability theorem.

The outcome is the first general quantitative lower bound on **every** unmatched row-cover number in a hypothetical graph above `M(n)`.

---

## 1. The permitted zero-subcore radius

Retain

`S_req=p lambda+3p+u lambda+2u-c_lambda-2`,

`c_lambda=ceil(lambda(lambda+2)/2)`.

If `m>M(n)`, then

`E_U+L_A<=S_req-2`.

Put

`C=S_req-2`.                                                     `(RC1)`

When `C>=0`, define

`R=floor((1+sqrt(1+4C))/2)`,                                    `(RC2)`

and

`R_*=max(2,R)`.                                                  `(RC3)`

The zero-signing-subcore theorem says that every zero-signed induced matched subcore of order at least three has size at most `R`. Therefore every zero-signed subcore, with the harmless size-one/two cases included, has size at most `R_*`.

If `C<0`, there is no above-threshold candidate at all.

---

## 2. Row-kernel classes are zero-signed subcores

Fix `y in U` and let

`t=tau(Psi(K_y))`.

Apply the row-kernel theorem with a minimum cover. There is an exceptional coordinate set `X` with

`|X|<=t`

such that `[p]\X` is partitioned into at most `t` equal-open-neighbourhood classes in the row sign graph `L_y=bar K_y`.

Each such class is independent in `L_y`. Therefore each class, by itself, is a zero-signing subcore of the matched 2-lift in the coordinate system centred at `y`.

The largest class has size at least

`D>=ceil((p-|X|)/t)>=ceil((p-t)/t)`.                             `(RC4)`

An above-threshold candidate must have

`D<=R_*`.                                                        `(RC5)`

Combining `(RC4)`--`(RC5)` gives

`(p-t)/t<=R_*`,

hence:

> **UNMATCHED ROW-COVER LOWER BOUND.** In every near-full above-`M(n)` candidate,
>
> `tau(Psi(K_y)) >= ceil(p/(R_*+1))`                             `(RC6)`
>
> for every unmatched vertex `y`.

This is a global theorem, not a cheap-row case classification.

---

## 3. Hardest lambda=-1 layer

At `lambda=-1`,

`C=2p+u-4`,

so

`R=floor((1+sqrt(8p+4u-15))/2)`.                                `(RC7)`

Thus every unmatched row of an above-threshold candidate satisfies

> `tau(Psi(K_y)) >= ceil(p/(R_*+1))`.                            `(RC8)`

If `u=O(p)`, then `R=O(sqrt(p))` and therefore

> `tau(Psi(K_y))=Omega(sqrt(p))`                                `(RC9)`

**for every unmatched row**.

This is qualitatively stronger than excluding the exact `tau<=1` and `tau<=2` normal forms: all bounded row-cover kernels disappear simultaneously in the linear-unmatched regime.

---

## 4. Projective alpha classes are also zero-signed subcores

The preserved projective-twin theorem identifies

`mu_alpha=max_c |alpha^{-1}(c)|`

with the largest true-twin clique obtainable in any switching state of the matched 2-lift.

A true-twin clique on a coordinate set `I` means that, in that switching state, the corresponding selected endpoints form a clique; equivalently the sign graph has no edges inside `I`. Hence `I` is a zero-signing subcore.

Therefore an above-threshold candidate also satisfies

> **ALPHA TWIN CAP.**
>
> `mu_alpha<=R_*`.                                               `(AC1)`

This feeds directly into the preserved Hall estimate

`s=e(A,U)>=pu-mu_alpha a`,

so

> `s>=pu-R_* a`.                                                 `(AC2)`

Equivalently, using `E_U<=2 bar q+mu_alpha a`,

> `E_U<=2 bar q+R_* a`.                                         `(AC3)`

The main value of `(AC1)` is not the coarse scalar inequality by itself. It says that an above-threshold configuration cannot hide many alpha obligations in a large repeated switching true-twin class: every such capacity class is at most `O(sqrt(p+u))` in the near-full regime.

---

## 5. Combined structural picture

For `u=O(p)` and fixed `lambda`, a hypothetical above-`M(n)` graph now has to satisfy simultaneously:

1. switching-deletion number
   `kappa_sw=p-O(sqrt(p))`;
2. every unmatched row has
   `tau(Psi(K_y))=Omega(sqrt(p))`;
3. every projective alpha / switchable true-twin class has
   `mu_alpha=O(sqrt(p))`.

So the surviving matched core is forced into a genuinely high-complexity regime from three different viewpoints:

- far from a cut even after vertex deletion;
- no cheap row-cover kernels;
- no large alpha-capacity/twin class.

This is a much tighter frontier than the earlier catalogue of one-code and two-code rows.

---

## 6. Next move

The natural next theorem is an **aggregate Hall-capacity lower bound** in this high-complexity regime. Since each of the `u` rows needs at least `Omega(sqrt(p))` code vertices, while every repeated alpha class has capacity at most `R_*`, one should try to prove that either

- beta obligations occupy enough distinct A-code / A--U incidence capacity to force A-side slack, or
- the required overlap creates complementary fan structure, which is already priced by the Boolean antipode theorem.

The exact row-cover bound `(RC6)` and alpha cap `(AC1)` provide explicit numerical parameters for that argument.

The published order-12/size-32 hostile control remains in the separate full-tight `u=0` branch and is unaffected.

No all-order second-extremal theorem is claimed.
