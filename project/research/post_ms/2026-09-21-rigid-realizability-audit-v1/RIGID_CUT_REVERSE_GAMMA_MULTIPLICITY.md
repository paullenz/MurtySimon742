# Reverse-gamma multiplicity obstruction for rigid-cut realizability

Date: 2026-09-21

Status: synthesis of the raw boundary-code-edge trichotomy with the preserved gamma-collision theorem and the post-audit global matched-leaf collapse. This is a necessary condition for a rigid complete Hall cut to be realizable in an actual D2C graph; it does not assume the later half-ray geometry.

## 1. General reverse-only coordinate compression

Keep the notation of `RIGID_CUT_BOUNDARY_CODE_EDGE_TRICHOTOMY.md`. Fix one outside code d and let

`Y_d={y in Y:c(y)=d}`, `y_d=|Y_d|`.

Let

`R_d^rev = I(d,X) \ (U_0(d,X) union L(d,X))`

be the coordinates having neither coarse U-forward support nor matched-leaf forward support. Put

`r=|R_d^rev|`.

For every `i in R_d^rev`, Corollary 3.1 of the trichotomy gives

`|X_{gamma_i}| >= y_d`,

where `gamma_i=gamma(q_i^{d_i})`.

Distinct gamma codes correspond to disjoint X-code classes. Therefore, if `r>0`,

`#{ gamma_i : i in R_d^rev } <= floor(x/y_d)`.

In particular `y_d<=x` is necessary whenever a reverse-only coordinate exists.

Put

`s=floor(x/y_d)`.

If `s>=1`, pigeonhole gives a gamma code repeated on at least

`g >= ceil(r/s)`

of the reverse-only coordinates.

The preserved gamma-collision theorem says that a common gamma class on `g>=3` tight fibres forces

`L_A >= g(g-1)`.

### Theorem 1.1 — reverse-gamma multiplicity bill

If `r>0`, then either `y_d>x`, which is impossible, or `s>=1` and, with

`g=ceil(r/s)`,

one has `g<=2` or `L_A>=g(g-1)`.

For an above-M candidate with the preserved score ceiling `L_A<=C0`, this gives

> **`r <= s G(C0)`**,                                     `(1.1)`

where

`G(C0)=max(2, floor((1+sqrt(1+4C0))/2))`.

The `max(2,...)` is deliberate: the safe gamma-collision floor is zero for multiplicity one or two.

## 2. Global exposed-coordinate master inequality

The raw trichotomy partitions every exposed coordinate into three support channels:

1. a coordinate with at least one U-forward witness;
2. a coordinate with matched-leaf forward support;
3. a reverse-only coordinate.

Different U-forward coordinates require different one-match U-code classes, so the first set has size at most u. The global matched-leaf collapse theorem proves that the second set has size at most two. Therefore

> `r >= |I(d,X)|-u-2`.                                   `(2.1)`

Combining `(2.1)` with `(1.1)` yields:

### Theorem 2.1 — boundary exposure master bound

For an above-M rigid complete cut and one outside code d with `y_d>=1`, if reverse-only coordinates exist then necessarily `y_d<=x` and

> **`|I(d,X)| <= u+2+floor(x/y_d) G(C0)`.**              `(2.2)`

If `y_d>x`, reverse-only support is impossible and the sharper bound is

> **`|I(d,X)|<=u+2`.**                                   `(2.3)`

The theorem requires no two-sided complementary pair inside X. It is a general raw-realizability constraint for every represented outside code.

This is particularly useful when boundary exposure is itself forced by the X-code geometry: then a large I cannot be hidden in aggregate Hall capacity; it must be physically routed through at most u one-match U-code classes, at most two matched leaves, and a gamma-collision-limited reverse reservoir.

## 3. Two-sided occupied X-pairs force full boundary exposure

Now specialize to the one-code outside branch `Y=A_d`.

Suppose X contains a complementary pair class in which **both orientations are occupied**: there are vertices of codes c and `bar c` in X.

Then at every tight coordinate i, exactly one of `c_i,bar c_i` equals `d_i`. Therefore

`I(d,X)=[p]`.

Moreover no coordinate is universal across X, because c and `bar c` disagree at every coordinate. Hence

`C(d,X)=empty`,

so the matched-forward mechanism is unavailable on **every** coordinate.

The coarse U-forward support uses distinct one-match codes `bar d xor e_i`; consequently at most u coordinates can have U-forward support. Thus at least

`r >= (p-u)_+`

coordinates are reverse-only.

### Theorem 3.1 — two-sided-pair realizability obstruction

In a rigid complete one-code cut with a two-sided occupied complementary pair inside X, put `s=floor(x/y)`.

If `p>u`, then necessarily `s>=1`, so `y<=x`. Furthermore, with

`g=ceil((p-u)/s)`,

either `g<=2` or

`L_A>=g(g-1)`.

For an above-M candidate,

> **`p-u <= floor(x/y) G(C0)`**                          `(3.1)`

is necessary.

Equivalently, whenever

`p-u > floor(x/y) G(C0)`,

every complementary pair class represented inside X must be one-sided occupied.

## 4. Structural interpretation

The general obstruction is strongest when

- the exposed-coordinate count exceeds the unmatched rooted reservoir;
- the outside code class is not tiny compared with X;
- and the A-slack ceiling is small.

Too few coordinates can be handled by unmatched forward witnesses, matched-forward support is globally O(1), and the remaining coordinates demand large reverse X-code classes. Either those gamma classes are too numerous to fit in X or many coordinates share one gamma class, triggering the gamma-collision theorem.

This does not yet prove nonrealizability of all rigid cuts. It does, however, turn the empirical zero-positive-fixture gap into a compact structural inequality that can be tested directly against all one-code survivor parameter ranges and against future actual-graph regression fixtures.
