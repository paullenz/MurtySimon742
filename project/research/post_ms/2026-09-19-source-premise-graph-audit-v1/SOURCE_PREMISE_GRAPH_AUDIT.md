# Source-premise graph audit

## Purpose

This checkpoint answers the highest-priority obligation in the 2026-09-19 daily red-team audit before any further downstream use of the finite source-tuple capacity theorem.  The audit distinguished two upstream premises:

1. **P1 (distinct physical sources):** for a fixed A-witness `x`, beta obligations on different target fibres use distinct physical sources `y in U`.
2. **P2 (global source-coordinate uniqueness):** a physical `(source y, target coordinate i)` is not reused across A-witnesses.

The finite source-tuple/FDPr/layer-cake theorem remains conditional on the exact semantics under which these premises are true.

## Independent graph-level reconstruction

A fresh checker was written from graph primitives rather than the abstract source-tuple formulas.  For every candidate graph it:

- verifies connectedness, diameter two, and edge-criticality under deletion;
- chooses a root `v`, sets `B=N(v)` and `A=V\({v} union B)`;
- identifies tight antipode pairs `q_i q_i'` in `B` by the raw condition
  `q_i q_i' notin E`, `N(q_i) cap N(q_i')={v}`, and every other vertex sees exactly one endpoint;
- verifies the tight pairs form a matching;
- puts unmatched root neighbours in `U`;
- records raw beta certificates `(x,i,y)` whenever `x in A`, `y in U`, `x-y` and `y-q_i` are edges, `x-q_i` is absent, and `N(x) cap N(q_i)={y}` (with the orientation in which `x` sees the mate of `q_i`).

This is deliberately below the later Hall/source-tuple abstraction.

## Actual-graph regression

All 21 unlabeled D2C graph-atlas classes through order seven were replayed, at every root.  In addition, hundreds of independently generated D2C graphs of orders 8--12 were obtained by starting from diameter-two graphs and greedily deleting edges while preserving diameter two, followed by an exact D2C recheck.  At the max-degree roots of the latter sample, 2,435 rooted instances were checked, 932 had at least one tight fibre, 2,353 had nonempty `U`, and 36 raw beta certificates occurred.

No P1 violation was found in this regression.  That is evidence only, not a proof.

## P2 is false as a raw graph-theoretic statement

The checker found seven realizable D2C roots in which the same physical `(y,i)` supports raw beta certificates for two different A-witnesses.  The smallest explicit example has order 9 and size 9:

```
E = {(0,1),(0,2),(1,3),(2,8),(3,8),(4,6),(4,7),(5,6),(5,7)}.
```

Take root `v=4`.  The tight fibre is `(6,8)`, `U={7}`, and

```
A={0,1,2,3,5}.
```

With coordinate `i=0`, endpoint `q_i=6` and mate `8`, the same source `y=7` gives both raw certificates

```
(x=2, i=0, y=7),
(x=3, i=0, y=7).
```

Indeed each of `x=2,3` is adjacent to `7`, each misses `6`, each sees mate `8`, and

```
N(2) cap N(6) = {7} = N(3) cap N(6).
```

Thus **raw P2 is not a consequence of diameter-two criticality**.

A second example, useful against accidental dependence on the first graph, has order 10 with

```
E = {(0,6),(0,8),(1,3),(1,8),(2,4),(2,8),(3,9),(4,5),(5,7),(6,7)}.
```

At root `1`, tight fibre `(3,5)` and `U={8}`, the same physical pair `(8,0)` has raw witnesses `x=0` and `x=2`.

## Selected P2 is a convention, not the falsified raw claim

The historical beta-source theorem in commit `cee68f4684f5e2ed348804fc931043a0f44f0d5d` states explicitly:

> The selected beta witness attached to a source y and target fibre i is a chosen representative of that single physical P--U obligation. Therefore, for fixed y, there is at most one selected beta witness per target fibre.

Consequently the project's **selected** `(source,coordinate)` uniqueness is best understood as a deduplication convention on physical obligations, not as uniqueness of all raw A-witness realizations.  The raw counterexample therefore does not by itself refute the abstract selected-system source-tuple theorem.

It does, however, create a mandatory interface obligation: every lower bound denoted `B_beta` that is fed into source-tuple capacity must be a lower bound on the number of **distinct physical source-coordinate obligations**, not merely on the number of A-witness/coordinate realizations before deduplication.  A lower bound of the latter kind cannot be transferred through selected P2 without a collision argument.

## P1 status

P1 survived the present graph-level regression but has not been proved from raw rooted criticality.  If one physical `y` were to serve two target fibres `i != j` for the same `x`, then `x~y`, `y~q_i,q_j`, `x` misses both `q_i,q_j`, and

```
N(x) cap N(q_i) = N(x) cap N(q_j) = {y},
```

while `x` sees both corresponding mates by tight-fibre transversality.  No contradiction from these facts alone has yet been established.  Hence the all-k beta-reuse/source-tuple applications remain conditional on P1.

## Audit consequence

The daily red-team concern was substantive and correctly prioritized.  The status should now be separated into three levels:

1. raw graph-level P2: **false**;
2. selected P2 after deduplicating physical `(y,i)` obligations: **valid by the documented selection convention**;
3. transfer of graph-level beta lower bounds into selected `B_beta`: **must be audited theorem by theorem**;
4. P1: **empirically supported but unresolved**.

No source-tuple consequence should be promoted as an unconditional graph theorem until (3) and P1 are closed.

## Next work forced by this audit

1. Inspect the root-imbalance and switching lower bounds on `B_beta` and determine whether their counting unit is already a distinct physical `(y,i)` obligation.  If not, introduce an explicit collision correction.
2. Continue a targeted P1 search on beta-rich realizable D2C roots and seek a direct proof from tight-fibre transversality/criticality.
3. Keep the actual-graph regression as a permanent hostile interface test, with the published order-12 graph `X_3` included explicitly.
4. Only after those interface checks are safe, resume the audit-prescribed one-code branch using exact pair-local `Ccap_P`, `(ONE)`, and `(CROWD)`.
