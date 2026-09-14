# Audit record — type-compressed orientation Hall

14 September 2026. **Internal exact audit green through the sharp-dominance and canonical-antichain layers. External mathematical review, novelty assessment and genuinely independent reproduction remain OPEN.**

## Whole-type Hall theorem

[`TYPE_COMPRESSED_ORIENTATION_HALL.md`](TYPE_COMPRESSED_ORIENTATION_HALL.md) proves two reductions for the directed target-capacity Hall relaxation associated with a fixed `(q,c,P)` profile.

1. Every labelled source subset is represented exactly by its counts `x_tau` in identical `(q,c,P)` type classes.
2. The Hall margin `F(x)=R(x)-L(x)` is discretely concave in each coordinate separately, so a global minimum over `0<=x_tau<=n_tau` occurs at a box vertex `x_tau in {0,n_tau}`.

Thus any failing target-Hall cut has a witness that is a union of complete `(q,c,P)` type classes.

The independent finite verifier [`verify_type_compressed_orientation_hall.py`](verify_type_compressed_orientation_hall.py) does not call the C++ relational scanners or a max-flow library. GitHub Actions run `34820069162` completed green:

```text
head:      d7cd31c89df42e8f9d069a579dc5bec7f27205cf
artifact:  10337932232
sha256:5c0c6dec9db66306d501e8f28d9ee3fc604d4d04363067b90e59f80c2ed4e55b
```

Frozen record: [`TYPE_COMPRESSED_ORIENTATION_HALL_VERIFICATION.json`](TYPE_COMPRESSED_ORIENTATION_HALL_VERIFICATION.json).

Across the exhaustive and deterministic random suites:

```text
profiles:                         14,330
labelled/compressed cut checks:  593,984
coordinate-concavity lines:      391,896
zero discrepancies.
```

## Exact type-level max-flow and submodularity

[`TYPE_LEVEL_MAXFLOW_COROLLARY.md`](TYPE_LEVEL_MAXFLOW_COROLLARY.md) replaces the labelled target network by an exact quotient network on `(q,c,P)` types and identifies the complete-type Hall margin as a submodular set function.

The separate verifier [`verify_type_level_maxflow.py`](verify_type_level_maxflow.py) constructs both networks independently, checks labelled/quotient maximum-flow equality, direct/closed-form cut equality and submodularity. GitHub Actions run `34821405958` completed green:

```text
head:      da1a964811a2b694c566da34a53af9431ce402ff
artifact:  10338800732
sha256:24c07f68d579c43cff168a2d4aab71c6e24be70f51629831555e4b5d625dab77
```

This is exact for the target-flow relaxation; it is not a third-party review of the graph-to-constraint bridge.

## Initial dominance-upset theorem

[`DOMINANCE_UPSET_HALL.md`](DOMINANCE_UPSET_HALL.md) adds the sufficient hardness order

```text
x >=_H y
iff q_x>=q_y,
    c_x<=c_y,
    P_x>=P_y.
```

The hand proof establishes a marginal exchange inequality; submodularity then makes every maximum-cardinality global minimum Hall witness an up-set under `>=_H`.

[`verify_dominance_upset_hall.py`](verify_dominance_upset_hall.py) independently checks interval compatibility, submodularity, every dominance exchange in its test universes, and equality between the unrestricted minimum and the minimum over hardness up-sets. GitHub Actions run `34827519117` completed green:

```text
head:      f9f317caa970677b3ef3bc6d09baa0db8cb9296a
artifact:  10339799796
sha256:5e0977bedbd2615df54f4f31f95ec4847635355f10fad835257d92a65697bd21
```

Frozen record: [`DOMINANCE_UPSET_HALL_VERIFICATION.json`](DOMINANCE_UPSET_HALL_VERIFICATION.json).

Audit totals:

```text
profiles:                         4,286
exhaustive profiles:              1,286
random profiles:                  3,000
interval checks:                101,928
Hall-margin evaluations:        221,532
submodularity checks:         1,123,108
dominance exchange checks:      263,285
hardness up-sets checked:         92,069
profiles with negative margin:     3,556
```

There were zero discrepancies.

## Sharpened dominance theorem

[`SHARP_DOMINANCE_UPSET_HALL.md`](SHARP_DOMINANCE_UPSET_HALL.md) proves that the `P` comparison is unnecessary when source demand strictly increases. The sharper relation is

```text
x >=_* y
iff c_x<=c_y
    and [q_x>q_y or (q_x=q_y and P_x>=P_y)].
```

The key bound is

```text
Delta_x(T)-Delta_y(T) <= 1-(q_x-q_y).
```

Thus a strict demand increase absorbs the at-most-one-unit diagonal swap; a demand gap of at least two gives a strict exchange. Every minimum Hall witness therefore obeys the corresponding closure whenever `q_x>=q_y+2` and `c_x<=c_y`.

The same-assistant local record [`SHARP_DOMINANCE_UPSET_HALL_LOCAL_AUDIT.json`](SHARP_DOMINANCE_UPSET_HALL_LOCAL_AUDIT.json) was preserved before CI. The dedicated independently launched repository replay is now also green: GitHub Actions run `34830228571`.

```text
head:      c57c7bf6a29a4c14104408c1b6e2db8e343cc62e
artifact:  10341459641
sha256:b686e3f9663a082aa9b0ff9fa89d1c0a29904ca3622f205421a895e3babbf37c
```

Frozen CI record: [`SHARP_DOMINANCE_UPSET_HALL_VERIFICATION.json`](SHARP_DOMINANCE_UPSET_HALL_VERIFICATION.json).

```text
profiles:                       4,286
interval checks:              101,928
margin evaluations:           221,532
submodularity checks:       1,123,108
sharp exchange checks:        372,455
strict-gap checks:            126,654
zero discrepancies.
```

This remains internal exact audit evidence, not third-party mathematical review.

## Dominance-closed quotient network

[`DOMINANCE_CLOSED_MAXFLOW.md`](DOMINANCE_CLOSED_MAXFLOW.md) records the exact network consequence: adding capacity-`Q+1` closure arcs from an easier source type to each harder dominating type does not change the quotient min-cut value, because an optimal sharp-hardness up-set already exists. The selected source side of such a minimum cut is therefore dominance closed.

## Canonical antichain certificate

[`CANONICAL_ANTICHAIN_CERTIFICATE.md`](CANONICAL_ANTICHAIN_CERTIFICATE.md) combines submodularity and sharp dominance into a canonical failure certificate.

- Minimum-margin type sets are closed under union and intersection.
- Their intersection `M-` and union `M+` are the unique inclusion-minimal and inclusion-maximal minimizers.
- `M+` is the unique maximum-cardinality minimizer and therefore a sharp-hardness up-set.
- The minimal elements of `M+` form a unique antichain and reconstruct `M+` by sharp up-closure.
- Sorted by increasing cross degree `c`, those generators have nondecreasing demand `q`; on an equal-`q` plateau their target caps `P` strictly increase.
- In the closure-augmented quotient network, the residual vertices unable to reach the sink give the unique maximal source-side minimum cut, whose source-type projection is exactly `M+`.

The self-contained verifier [`verify_canonical_antichain_certificate.py`](verify_canonical_antichain_certificate.py) independently enumerates type-set margins and separately builds the closure-augmented quotient max-flow. GitHub Actions run `34830787798` completed green:

```text
head:      b81fb8ee5e7e9a4ab51153081b5154921ceff0a4
artifact:  10342426285
sha256:2ed919e019c7f65a21fbbe92d81e5db84db14e39889bd259d559e2feded08433
```

Frozen record: [`CANONICAL_ANTICHAIN_CERTIFICATE_VERIFICATION.json`](CANONICAL_ANTICHAIN_CERTIFICATE_VERIFICATION.json).

Audit totals:

```text
profiles:                            4,286
negative-margin profiles:            3,556
type-set margins:                  198,140
minimizer-lattice pair checks:      28,460
generator antichain pair checks:     7,361
different-q staircase checks:        6,374
equal-q staircase checks:              987
closure-flow value checks:           4,286
residual maximal-cut checks:         4,286
zero discrepancies.
```

The canonical generator counts among the `3,556` negative test profiles were:

```text
1:   869
2: 1,303
3: 1,005
4:   324
5:    49
6:     6
```

The maximum observed generator count was six. This distribution is audit evidence only, not an all-order generator bound.

## Red-team history

The first draft deliberately treated “whole type classes only” as an unproved possible shortcut and proposed searching for a counterexample. Search instead suggested the stronger statement; coordinatewise concavity supplied the proof.

The earlier one-dimensional Ferrers/prefix simplification remains false, with its explicit counterexample preserved in `ORIENTATION_FLOW_HALL.md`.

The next attempted simplification asked whether one principal hardness up-set generated by a single type always suffices. It does not. [`PRINCIPAL_UPSET_COUNTEREXAMPLE.md`](PRINCIPAL_UPSET_COUNTEREXAMPLE.md) preserves a three-type `V` example in which every principal up-set has margin `>=0` but the two-generator up-set has margin `-1`. A separate four-type example needs three incomparable generators.

The 15-state principal-upset pilot reinforces that negative result: principal cuts remove more individual profiles than single-type cuts (`17,284` versus `14,768`) but completely explain only `2` of the `13` relationally excluded pilot states.

Thus the current safe hierarchy is

```text
arbitrary labelled subsets
 -> complete (q,c,P) types
 -> exact type-level max-flow
 -> submodular minimum cuts
 -> sharp hardness up-sets
 -> canonical antichain staircase,
```

but **not**

```text
one-dimensional prefix,
one generator / one principal up-set,
or a universal two-generator bound.
```

Failed shortcuts and weaker precursor statements remain preserved in Git history rather than silently erased.

## What this does not establish

This audit does not prove that:

- the target-flow relaxation is sufficient for a diameter-two edge-critical graph;
- the canonical Murty-Simon bridge is externally verified;
- any of these reductions is novel in the literature;
- the canonical antichain has a universal constant-size generator set;
- the unrestricted Murty-Simon conjecture is proved.

The interval representation identifies a useful incidence structure, but no literature novelty claim is made for that observation without a separate literature review.

## Current research use

The full relational frontier reconnaissance indicates that directed target-Hall is the dominant new exclusion layer. The exact obstruction is now represented by a unique preferred object: the maximal minimum-cut sharp up-set and its antichain staircase boundary.

The next structural question is Murty-Simon-specific: use `c=q+rho`, the canonical caps on `q`, the target-capacity formula `P`, demand forcing and excess constraints to control this staircase more strongly than is possible for arbitrary Hall profiles. In parallel, the layer/state-safe 3,607-state relational scan continues as discovery; no scan-only candidate becomes canonical without recovery, fresh two-implementation audit and separate gated promotion.
