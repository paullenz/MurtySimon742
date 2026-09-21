# Reverse-gamma multiplicity obstruction for rigid-cut realizability

Date: 2026-09-21

Status: synthesis of the raw boundary-code-edge trichotomy with the already preserved gamma-collision theorem. This is a necessary condition for a rigid complete Hall cut to be realizable in an actual D2C graph; it does not assume the later half-ray geometry.

## 1. General reverse-only coordinate compression

Keep the notation of `RIGID_CUT_BOUNDARY_CODE_EDGE_TRICHOTOMY.md`. Fix one outside code `d` and let

`Y_d={y in Y:c(y)=d}`, `y_d=|Y_d|`.

Let

`R_d^rev = I(d,X) \ (U_0(d,X) union L(d,X))`

be the coordinates having neither even coarse U-forward support nor matched-leaf forward support. Put

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

Hence:

### Theorem 1.1 — reverse-gamma multiplicity bill

If `r>0`, then either

`y_d>x`,

which is impossible, or `s>=1` and, with

`g=ceil(r/s)`,

one has

`g<=2`

or

`L_A>=g(g-1)`.

For an above-`M(n)` candidate with the preserved score ceiling `L_A<=C0`, this gives the finite necessary bound

`r <= s G(C0)`,

where

`G(C0)=max(2, floor((1+sqrt(1+4C0))/2))`.

The use of `max(2,...)` is deliberate: the safe gamma-collision floor is zero for multiplicity one or two.

## 2. Two-sided occupied X-pairs force full boundary exposure

Now specialize to the one-code outside branch

`Y=A_d`.

Suppose `X` contains a complementary pair class in which **both orientations are occupied**: there are vertices of codes `c` and `bar c` in X.

Then at every tight coordinate `i`, exactly one of `c_i,bar c_i` equals `d_i`. Therefore

`I(d,X)=[p]`.

Moreover no coordinate is universal across X, because `c` and `bar c` disagree at every coordinate. Hence

`C(d,X)=empty`,

so the matched-forward mechanism of the boundary trichotomy is unavailable on **every** coordinate.

The coarse U-forward support uses distinct one-match codes `bar d xor e_i`; consequently at most `u` coordinates can even have possible U-forward support. Thus at least

`r >= (p-u)_+`

coordinates are reverse-only.

Combining with Theorem 1.1 gives:

### Theorem 2.1 — two-sided-pair realizability obstruction

In a rigid complete one-code cut with a two-sided occupied complementary pair inside X, put

`s=floor(x/y)`.

If `p>u`, then necessarily `s>=1`, so in particular

`y<=x`.

Furthermore, with

`g=ceil((p-u)/s)`,

either `g<=2` or

`L_A>=g(g-1)`.

For an above-`M(n)` candidate,

`p-u <= floor(x/y) G(C0)`

is therefore necessary.

Equivalently, whenever

`p-u > floor(x/y) G(C0)`,

every complementary pair class represented inside X must be **one-sided occupied**.

This is a new route toward code collapse which is upstream of `(ONE-P)`: it comes from trying to realize the boundary B--A edges of the rigid cut at all, not from paying for the complete A-cut after the fact.

## 3. Structural interpretation

The obstruction is strongest when

- the tight-fibre count exceeds the unmatched rooted reservoir (`p-u` large);
- the outside one-code block is not tiny compared with X (`x/y` bounded);
- and the A-slack ceiling is small.

In that regime a two-sided X-pair exposes every tight coordinate. Too few coordinates can be handled by unmatched forward witnesses, matched-forward witnesses are forbidden because there are no universal coordinates, and the remaining coordinates all demand large reverse X-code classes. Either those gamma classes are too numerous to fit in X or many coordinates share one gamma class, which is exactly the configuration charged by the gamma-collision theorem.

This does not yet prove nonrealizability of all rigid cuts. It does, however, turn the empirical “zero positive fixture” gap into a concrete structural dichotomy that can be tested directly on the one-code survivors and on future actual-graph regression fixtures.
