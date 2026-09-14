# Audit record — type-compressed orientation Hall

14 September 2026. **Internal exact audit green. External mathematical review, novelty assessment and genuinely independent reproduction remain OPEN.**

## Hand result under audit

[`TYPE_COMPRESSED_ORIENTATION_HALL.md`](TYPE_COMPRESSED_ORIENTATION_HALL.md) proves two reductions for the directed target-capacity Hall relaxation associated with a fixed `(q,c,P)` profile.

1. Every labelled source subset is represented exactly by its counts `x_tau` in identical `(q,c,P)` type classes.
2. The Hall margin `F(x)=R(x)-L(x)` is discretely concave in each coordinate separately. Therefore a global minimum over the integer box `0<=x_tau<=n_tau` occurs at a box vertex, so it is enough to test

```text
x_tau in {0,n_tau}.
```

Thus any failing target-Hall cut has a witness that is a union of complete `(q,c,P)` type classes.

## Independent finite verifier

[`verify_type_compressed_orientation_hall.py`](verify_type_compressed_orientation_hall.py) does not call the C++ relational scanners or a max-flow library. It directly enumerates labelled source subsets and independently evaluates the compressed formulas.

GitHub Actions run:

```text
run id:    34820069162
head:      d7cd31c89df42e8f9d069a579dc5bec7f27205cf
conclusion: success
artifact:  10337932232
artifact digest:
sha256:5c0c6dec9db66306d501e8f28d9ee3fc604d4d04363067b90e59f80c2ed4e55b
```

The frozen verification record is [`TYPE_COMPRESSED_ORIENTATION_HALL_VERIFICATION.json`](TYPE_COMPRESSED_ORIENTATION_HALL_VERIFICATION.json).

### Exhaustive small universe

The verifier exhaustively checked every labelled profile of orders `1,...,5` over the six-type universe

```text
(0,0,0), (0,1,1),
(1,1,0), (1,2,1),
(2,2,1), (2,3,2).
```

Totals:

```text
profiles:                    9,330
labelled/formula cut checks: 271,452
coordinate concavity lines:  307,290
profiles containing a Hall violation: 6,430
```

There were zero discrepancies.

### Deterministic broad random challenge

With seed `7420914`, the verifier generated 5,000 additional canonical-shaped profiles of orders up to eight, with repeated random `(q,c,P)` types satisfying `c=q+rho>=q`.

Totals:

```text
profiles:                    5,000
labelled/formula cut checks: 322,532
coordinate concavity lines:   84,606
profiles containing a Hall violation: 2,418
```

Again there were zero discrepancies.

Across the two suites this gives

```text
14,330 profiles,
593,984 labelled/compressed cut equalities,
391,896 coordinate-concavity lines,
```

with no counterexample to the hand theorem.

## Exact type-level max-flow corollary

[`TYPE_LEVEL_MAXFLOW_COROLLARY.md`](TYPE_LEVEL_MAXFLOW_COROLLARY.md) replaces the labelled target network by an exact quotient network on `(q,c,P)` types and identifies the complete-type Hall margin as a submodular set function.

The separate independent verifier and CI replay are green:

```text
run id:    34821405958
head:      da1a964811a2b694c566da34a53af9431ce402ff
conclusion: success
artifact:  10338800732
artifact digest:
sha256:24c07f68d579c43cff168a2d4aab71c6e24be70f51629831555e4b5d625dab77
```

This audit is exact for the target-flow relaxation; it is not a third-party review of the graph-to-constraint bridge.

## Dominance-upset theorem

[`DOMINANCE_UPSET_HALL.md`](DOMINANCE_UPSET_HALL.md) adds an order-theoretic reduction. For labelled vertices define the sufficient hardness order

```text
x >=_H y
iff q_x>=q_y,
    c_x<=c_y,
    P_x>=P_y.
```

The hand proof establishes a marginal exchange inequality. Combining that exchange with submodularity shows that a maximum-cardinality global minimum Hall witness is an up-set under `>=_H`; identical `(q,c,P)` vertices therefore enter as complete type classes.

[`verify_dominance_upset_hall.py`](verify_dominance_upset_hall.py) independently checks the labelled formula, submodularity, every dominance exchange in its test universes, and equality between the unrestricted minimum and the minimum over hardness up-sets.

GitHub Actions replay:

```text
run id:    34827519117
head:      f9f317caa970677b3ef3bc6d09baa0db8cb9296a
conclusion: success
artifact:  10339799796
artifact digest:
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

[`SHARP_DOMINANCE_UPSET_HALL.md`](SHARP_DOMINANCE_UPSET_HALL.md) observes that the `P` comparison is unnecessary when source demand strictly increases. The sharper relation is

```text
x >=_* y
iff c_x<=c_y
    and [q_x>q_y or (q_x=q_y and P_x>=P_y)].
```

The key bound is

```text
Delta_x(T)-Delta_y(T) <= 1-(q_x-q_y).
```

Thus any strict demand increase absorbs the at-most-one-unit diagonal swap, and a demand gap of at least two gives a strict exchange. Consequently, every minimum Hall witness obeys the corresponding closure whenever `q_x>=q_y+2` and `c_x<=c_y`.

The preserved same-assistant local audit record is [`SHARP_DOMINANCE_UPSET_HALL_LOCAL_AUDIT.json`](SHARP_DOMINANCE_UPSET_HALL_LOCAL_AUDIT.json), with verifier source in [`verify_sharp_dominance_upset_hall.py`](verify_sharp_dominance_upset_hall.py). It records

```text
profiles:                       4,286
interval checks:              101,928
margin evaluations:           221,532
submodularity checks:       1,123,108
sharp exchange checks:        372,455
strict-gap checks:            126,654
```

with zero discrepancies. This is **not yet an independent GitHub CI or third-party reproduction** and is labelled accordingly.

## Red-team history

The first draft deliberately treated “whole type classes only” as an unproved possible shortcut and proposed searching for a counterexample. Direct search instead suggested the stronger statement. The reason was then identified analytically: every target-type contribution to the Hall margin is concave in one source-type count, including the diagonal-deletion term. This yielded the coordinatewise concavity proof now in the theorem note.

The next attempted simplification asked whether one principal hardness up-set generated by a single type always suffices. It does not. [`PRINCIPAL_UPSET_COUNTEREXAMPLE.md`](PRINCIPAL_UPSET_COUNTEREXAMPLE.md) preserves a three-type `V` example in which every principal up-set has margin `>=0` but the two-generator up-set has margin `-1`. A separate four-type example needs three incomparable generators.

Thus the current safe hierarchy is

```text
arbitrary labelled subsets
 -> complete (q,c,P) types
 -> hardness up-sets
 -> antichain boundary,
```

but **not**

```text
one generator / one principal up-set.
```

The initial weaker wording and failed shortcuts are preserved in Git history rather than silently erased.

## Dominance-closed quotient network

[`DOMINANCE_CLOSED_MAXFLOW.md`](DOMINANCE_CLOSED_MAXFLOW.md) records the exact network consequence: adding capacity-`Q+1` closure arcs from an easier source type to each harder dominating type does not change the quotient min-cut value, because an optimal hardness up-set already exists. The boundary of the selected source set can therefore be represented by an antichain.

## What this does not establish

This audit does not prove that:

- the target-flow relaxation is sufficient for a diameter-two edge-critical graph;
- the canonical Murty-Simon bridge is externally verified;
- any of these reductions is novel in the literature;
- one-dimensional prefixes, one principal up-set, or a bounded number of antichain generators are sufficient;
- the unrestricted Murty-Simon conjecture is proved.

The earlier explicit counterexample to one-dimensional prefix sufficiency in `ORIENTATION_FLOW_HALL.md` remains valid. The new interval representation identifies the compatibility relation as an interval-digraph / interval-bigraph incidence structure, but no literature novelty claim is made for that observation.

## Current research use

The full relational frontier reconnaissance is showing that directed target-Hall is the dominant new exclusion layer. The current theorem chain supplies progressively smaller exact descriptions of that obstruction:

```text
labelled target flow
 -> complete-type Hall cuts
 -> exact type-level max-flow
 -> submodular Hall margin
 -> dominance-upset minimum cut
 -> antichain boundary.
```

The active empirical question is how complicated that antichain boundary actually is on the surviving Murty-Simon profiles. Principal-upset reach is being measured separately as reconnaissance; any new whole-state closures remain unpromoted until the full cross-implementation audit chain is complete.
