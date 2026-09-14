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

## Red-team history

The first draft deliberately treated “whole type classes only” as an unproved possible shortcut and proposed searching for a counterexample. Direct search instead suggested the stronger statement. The reason was then identified analytically: every target-type contribution to the Hall margin is concave in one source-type count, including the diagonal-deletion term. This yielded the coordinatewise concavity proof now in the theorem note.

The initial weaker wording is preserved in Git history rather than silently erased.

## What this does not establish

This audit does not prove that:

- the target-flow relaxation is sufficient for a diameter-two edge-critical graph;
- the canonical Murty-Simon bridge is externally verified;
- the theorem is novel in the literature;
- a still smaller family such as one-dimensional prefixes, ideals, antichains or single-type cuts is sufficient;
- the unrestricted Murty-Simon conjecture is proved.

The earlier explicit counterexample to one-dimensional prefix sufficiency in `ORIENTATION_FLOW_HALL.md` remains valid. The new theorem reduces arbitrary source subsets to unions of full **two-dimensional types**, not to a single linear order.

## Current research use

The full relational frontier reconnaissance is showing that directed target-Hall is the dominant new exclusion layer. The whole-type theorem therefore supplies a compact, exact certificate format for that dominant obstruction and a natural starting point for further symbolic compression of the two-dimensional dominance system.
