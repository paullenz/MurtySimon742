# Maximal m=2 small-fibre remainder: p=2 reduction

Date: 2026-09-20

Status: **internal candidate reduction** following the `p>=3` finite-order theorem. This note does not claim closure of the final one-code all-F `p=2` geometry.

## 1. p=1 is impossible before any m=2 analysis

Every X-code in the first-strict branch is neither `d` nor `bar d`. For `p=1` those are the only two binary tight codes. Hence the first-strict branch has no `p=1` realization.

Thus the only small-fibre remainder is

> `p=2`.

Since `p-y>=1` and `y>0`, necessarily

> `y=1`.

Also `g<p`, so `g in {0,1}` and `k=x-g`.

## 2. The only two nontrivial codes are the F/R pair

Write `S_0={s}`; it must be a singleton because the code of `a_0` is neither `d` nor `bar d`. Then `I_0` is the other singleton.

There are exactly two binary codes distinct from `d,bar d`:

- the R-code `C_R=c(a_0)`, with agreement block `I_0`;
- the F-code `C_F=bar C_R`, with agreement block `S_0`.

Every X'-head is therefore either F or R. A single R-code component has matching number one by the graph-fixed Type-R foot. Consequently a maximal-m2 one-code geometry, if it exists, must be **all-F**.

Thus the p=2 problem splits into:

1. both F and R represented (two code components, each of matching number one);
2. one all-F code component of matching number two.

## 3. Two-code p=2 branch inherits the physical F/R collapse

Assume both F and R are represented.

For `omega>2`, the R component has its unique witness `z_R`; the F component then has multiple physical witnesses and hence one F-head. For `omega=2`, each code component has one physical witness but may have several heads.

The raw witness-location arguments in `M2_FR_RAW_EDGE_COLLAPSE.md` do not require a third coordinate once the F/R normal form itself is already known. Replaying them head-by-head gives for every `omega>=2`:

- F-witnesses miss all R-heads;
- `z_R` misses all F-witnesses and all F-heads;
- every F-witness is A-anticomplete;
- every F--R edge is impossible;
- both same-code head classes are internally independent;
- `a_0` misses every F-head.

Therefore

> `G[X]` is edgeless, `G[U_o]` is edgeless,
>
> and the only X--U_o edge is `a_0z_R`.                 `(P2-FR-EMPTY)`

Exactly as in the p>=3 note,

> `L_X=x(p+k+omega-y)-k=x(k+omega+1)-k`,
>
> `L_Y=omega+3-g`,
>
> `E_core>=k(k+2)-1`,
>
> `epsilon_b=3-g`,
>
> `E_Uo>=omega^2+omega-1`.

Use the same upper relaxation for the score cap,

`2 floor((lambda+1)^2/4)>=lambda(lambda+2)/2`,

with `lambda=omega+3-g`. Twice the resulting score margin is

> `S=-g^2-4gk-2gomega+4g-4k^2+6k-omega^2+4omega+3`. `(P2-FR-S)`

For `g=0`, `k=x>=3`, so

`S<=-(omega-2)^2-11<0`.

For `g=1`, `k=x-1>=2`, so

`S<=-(omega-1)^2-5<0`.

Hence:

> **the maximal-m2 two-code p=2 branch is empty.**       `(P2-FR-CLOSED)`

This is a score contradiction after graph-level raw collapse, not a finite scan.

## 4. The only small-fibre branch left

The sole maximal-m2 first-strict branch not covered by the present chain is therefore:

> `p=2`, `y=1`, all of `X'=X\{a_0}` has the single F-code `C_F`, all of `U_o` has the complementary R-code `C_R=c(a_0)`, and the raw eligibility graph `H[X',U_o]` has matching number exactly two. `(P2-ALLF-M2)`

Every physical outside vertex certifies at least one F-head, so every `z in U_o` satisfies

- `z` is nonadjacent to `a_0`;
- `z` is nonadjacent to Y;
- `z` misses at least one F-head;
- the Type-F matched-foot funnel fixes the same-code pair `(z,a_0)` at the unique coordinate in `S_0`.

By Konig, the eligibility graph has a vertex cover of size two. Thus its physical incidence falls into exactly three forms:

1. a two-witness cover, forcing `omega=2`;
2. a two-head cover, forcing `x=3`;
3. a mixed cover with one distinguished head and one distinguished witness, all remaining heads eligible only to that witness and all remaining outside vertices eligible only to that head.

This is now the only possible unbounded maximal-m2 small-fibre geometry. It should be attacked by raw criticality of the unique differing matched fibre and by the physical two-centre eligibility cover, not by weakening it into another total-score scan.

## 5. Eventual significance

Combining this note with `M2_FR_EXACT_HALL_CLOSURE.md` and `M2_X3_BOUNDED_TAIL.md` gives the current maximal-m2 picture:

- `p>=3`: every survivor is finite-order, in fact `n<=39`;
- `p=1`: impossible;
- `p=2`: the two-code F/R branch is impossible;
- only the one-code all-F matching-two geometry `(P2-ALLF-M2)` remains potentially unbounded.

That isolates a single sharply specified interface for the next session.