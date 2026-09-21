# Corrected residual-one half-ray: raw boundary-certificate realizability closure

Date: 2026-09-21

Status: **closed at the raw boundary level** within the corrected rigid one-code interface. The key contradiction is a physical U-code-class population count and does not require the score ceiling, rooted-Q feedback, pair-local scalar gates, residual-slot equality faces, or the candidate superconstant H--U deficit theorem. The score calculations below are retained as an independent backup/audit trail.

This note is deliberately upstream of the superseded H--U private-foot route.

## 1. Corrected half-ray

Work with

`p=2t, c=y=t, lambda=2t-1, u=t+1, x=2t+1, k=2, m=p-1=2t-1`,

for integer `t>=4`, with residual coordinate j.

The one-code outside block is

`Y=A_d`, `|Y|=t`.

The X-side consists of

- `H={h_i : i!=j}`, with one vertex of code `d xor e_i` for each private coordinate i;
- two K-heads of the common residual code `d xor e_j`.

Hence every occupied X-code class has size at most two, and the unique size-two class is the K-code `d xor e_j`.

The exact score ceiling, used only in the backup calculation, is

> `E_U+L_A <= C0=4t^2+7t-3`.                             `(1.1)`

## 2. Every tight coordinate is boundary-exposed and none is universal

For every tight coordinate i,

> `i in I(d,X)`.

At the residual coordinate j every H-code agrees with d. At a private coordinate i choose any distinct private head `h_l`; its code agrees with d at i.

On the other hand

> **`C(d,X)=empty`.**                                     `(2.1)`

At a private coordinate i, the head h_i disagrees with d. At the residual coordinate j, both K-heads disagree with d.

Therefore the matched-forward arm of the raw boundary trichotomy is unavailable on **every** coordinate.

## 3. Reverse capacity per coordinate is at most two

For coordinate i, a reverse boundary certificate must use an X-witness of the forced code

`gamma_i=gamma(q_i^{d_i})`.

Let

`r_i=|X_{gamma_i}|`.

Since every X-code class has size at most two,

> `r_i<=2`.                                               `(3.1)`

For fixed source `q_i^{d_i}`, one physical witness cannot certify two distinct Y-heads, because its common-neighbour set with the source is fixed. Hence at most r_i of the y=t boundary edges at coordinate i can use the reverse arm.

Thus at least

> `f_i>=t-r_i>=t-2>0`                                    `(3.2)`

outside sources use U-forward certificates at **every** coordinate.

## 4. Pure population contradiction

A U-forward witness at coordinate i has the forced one-match code

> `bar d xor e_i`.

Therefore `(3.2)` implies that, for every one of the p=2t coordinates, the corresponding U-code class

`U_{bar d xor e_i}`

is nonempty.

These p code classes are pairwise disjoint because their codes are distinct. Consequently any literal realization would require

> `u>=p=2t`.                                              `(4.1)`

But the corrected half-ray has

> `u=t+1`.                                                `(4.2)`

For every `t>=2`, `t+1<2t`, contradicting `(4.1)`.

### Raw boundary closure theorem

> **There is no actual D2C realization of the corrected residual-one k=2 intermediate half-ray for any `t>=4`.**

The contradiction uses only:

1. the literal half-ray X-code multiplicities;
2. boundary exposure `I=[p]`;
3. `C=empty`, hence no matched-forward arm;
4. the raw reverse-code rule and fixed-source injectivity;
5. the forced U-forward code `bar d xor e_i`.

It does **not** use the global source-tuple capacity theorem or either of its two audit-sensitive upstream premises.

This is stronger and cleaner than the score closure first derived in this session.

## 5. Independent backup: exact U-slack bill

The population contradiction already finishes the ray. Retaining the same geometry gives an independent quantitative check.

If one U-forward witness w at coordinate i serves `t_w` outside sources, the exact U-degree identity gives

`epsilon_w >= p-y+t_w = t+t_w`.

Let W_i be the actual witness set at coordinate i. Then

`sum_{w in W_i} epsilon_w`
` >= t|W_i|+f_i`
` >= 2t-r_i`.                                             `(5.1)`

The W_i are pairwise disjoint, so

> `E_U >= 4t^2-sum_i r_i >=4t^2-4t`.                    `(5.2)`

Together with the corrected H/Y floor `L_A>=t^2`, this already contradicts `(1.1)` for `t>=11`.

## 6. Independent backup: gamma refinement

Let

`g=|{i: gamma_i=d xor e_j}|`,

the number of coordinates whose forced reverse code is the unique size-two K-code. Every other occupied forced gamma class has size at most one, so

`sum_i r_i<=p+g=2t+g`,

and hence

`E_U>=4t^2-2t-g`.                                        `(6.1)`

The preserved gamma-collision theorem gives

`L_A>=max{t^2,g(g-1)}`.                                  `(6.2)`

The exact minimum of `(6.1)+(6.2)` over `0<=g<=2t` is

> `E_U+L_A>=5t^2-3t`.                                    `(6.3)`

This contradicts `(1.1)` for every `t>=10`.

If one additionally uses the midnight-audited predecessor residual-slot floor `Delta>=h=2t-1`, then `L_A>=t^2+2t-1` and the score contradiction sharpens to every `t>=8`. These finite-threshold refinements are now strategically unnecessary because Section 4 rules out the entire ray.

## 7. Strategic consequence

The intermediate half-ray was previously treated as an unbounded method escape because aggregate pair-local and rooted-Q gates had quadratic margin. It is not a realizability escape. Raw B--A boundary criticality forces a nonempty, coordinate-distinct one-match U-code class for every tight coordinate, but the ray has fewer unmatched vertices than tight coordinates.

Therefore no further asymptotic H--U carrier optimization should be spent on this ray. The live frontier moves back upstream to general rigid-cut realizability: determine how broadly the same exposed-coordinate versus available-U-class obstruction applies before specializing to residual-one survivor algebra.

## 8. Scope and caveat

This theorem remains conditional on reaching the rigid complete-Hall-cut / one-code interface. Bounded actual-D2C regression contains zero positive rigid complete pair-family cuts with `x>=3`; X_3 remains the mandatory negative control. The result closes this diagnostic branch; it is not an unconditional eventual second-extremal theorem.
