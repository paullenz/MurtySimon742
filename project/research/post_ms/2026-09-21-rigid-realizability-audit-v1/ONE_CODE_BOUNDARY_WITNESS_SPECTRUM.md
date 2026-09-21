# Repeated one-code boundary witness spectrum

Date: 2026-09-21

Status: raw structural consequence of the corrected full-boundary theorem. Conditional on the rigid complete one-code interface; no graph-level reachability claim is made.

## 1. Setup

Let `Y=A_d` be a repeated outside block (`y>=2`) with selected matched-head count `m>=2`. Keep the notation of `ONE_CODE_FULL_BOUNDARY_EXPOSURE_THEOREM.md`:

- `u=|U|`;
- `k` selected complementary U-witnesses of code `bar d` for a minimum outside source;
- `e=u-k`;
- `L=L(d,X)` matched-forward head set;
- every boundary U-forward witness at coordinate `i` has code `bar d xor e_i`.

The full-boundary theorem gives

`p <= e+|L| = u-k+|L|`.                              `(1.1)`

## 2. Immediate U-size lower bounds

Since `k>=0`,

> **`u >= p-|L|`.**                                    `(2.1)`

Therefore the universal-coordinate split yields:

- `|C|=0` or `|C|>=3`: `L=empty`, so **`u>=p`**;
- `|C|=1`: **`u>=p-1`**;
- `|C|=2`: **`u>=p-2`**.

This is a physical population requirement, not just a scalar gap inequality.

## 3. Equality spectrum

Suppose equality holds in `(2.1)`, i.e.

`u=p-|L|`.

Then `(1.1)` forces equality throughout:

`p=u-k+|L|=p-k`,

so

> **`k=0`.**                                            `(3.1)`

Moreover exactly `p-|L|=u` coordinates must be U-forward. Distinct U-forward coordinates require distinct one-match code classes

`bar d xor e_i`.

Hence every vertex of U is consumed by one of those classes and each used class contains exactly one vertex.

In particular, in the generic faces `|C|=0` or `|C|>=3`, where `L=empty`, equality `u=p` implies

> **`U={w_1,...,w_p}` with `c(w_i)=bar d xor e_i` for every i.** `(3.2)`

There are no complementary `bar d` vertices and no other U-code classes.

## 4. Located X--U hole block

The raw boundary trichotomy gives more: a U-forward witness for the boundary edge at coordinate i is X-anticomplete. Thus every `w_i` in `(3.2)` satisfies

`N(w_i) cap X = empty`.

Consequently the entire cut between X and U is empty:

> **`e(X,U)=0`.**                                       `(4.1)`

Equivalently there are exactly

> **`x u = xp` located X--U holes.**                    `(4.2)`

This is a genuine physical block of missing edges and must be fed into any rooted defect/score ledger; it is invisible in a scalar parameter tuple that records only `(p,u,c,g0,k,m)`.

## 5. Consequence for the rooted-Q hostile scalar family

The hostile scalar ray

`g0=1, y=p-1, c=u=p, lambda=p, x=p, k=0, m=p, r=0`

lies in the generic `C=empty` face. If it were physically realizable inside the rigid interface, Sections 3--4 force

- exactly one U vertex of each code `bar d xor e_i`;
- no other U vertices;
- `e(X,U)=0`;
- hence exactly `p^2` located X--U holes.

Also `m=x=p`, and the selected matched heads themselves have the distinct codes `d xor e_i`; therefore X is exhausted by one selected head of each such code.

Thus the scalar ray has a completely rigid Hamming-layer spectrum:

> **X is the radius-one layer about d, U is the radius-one layer about bar d, and X--U is anticomplete.** `(5.1)`

This is a far stronger physical normal form than the scalar rooted-Q inequalities reveal.

## 6. Audit significance

The argument uses only:

1. corrected full boundary exposure for repeated codes;
2. the raw code of a U-forward witness;
3. the raw fact that a U-forward witness is X-anticomplete;
4. cardinality equality.

It does not invoke the audit-sensitive global source-tuple uniqueness premise. Distinctness within one source follows from distinct required code classes. Any attempt to extend `(3.2)` across multiple outside sources must therefore be audited separately rather than smuggling in global selected `(source,coordinate)` uniqueness.

The next useful step is to feed the forced `xp` X--U hole block into the independently verified rooted residual/score accounting, or—if that ledger is not presently independently established—to derive the cheapest possible defect contribution directly from the raw rooted partition.
