# Hostile review checklist — Erdős 742 bounded submission v1

The purpose of this checklist is to make the submission easy to falsify. A single valid failure of a universal lemma or a missed graph-realizable case invalidates any dependent fixed-order claim.

## A. Scope and statement

- [ ] Confirm the submission claims only `n in {25,27,28,29,30}`.
- [ ] Confirm it does not silently assert every `n<=30`.
- [ ] Confirm the equality statement is `K(floor(n/2),ceil(n/2))` at each submitted order.
- [ ] Confirm the definition of diameter-2-critical matches the source problem / formalization used by the reviewer.

## B. Universal graph-theoretic bridge

Audit these before spending substantial time rerunning arithmetic:

- [ ] Complement/quasi-edge construction: every required missing pair produces the claimed selected cross-edge structure.
- [ ] Selection uniqueness: selection is per missing **unordered** pair and no multiplicity is silently introduced.
- [ ] Injection: forced cross-edges and selected edges cannot collide in the way excluded by the proof.
- [ ] Residual activity: the claimed positive residual degree statements hold in every boundary case.
- [ ] Demand implication: `s_i=max(0,d_i-R_i)` really forces the stated number of distinct selected sources with the required residual properties.
- [ ] Charging inequality: each source's charge budget is valid and the summation does not double count.
- [ ] Threshold-capacity inequality: high-demand / high-residual source counts respect unordered-pair capacity.
- [ ] Any isolated-C / auxiliary-location lemma used at n=30 is valid with the stated parameter range and disjointness assumptions.

## C. Fan-free upper-range reduction

Use the current v2 proof surfaces, not the historical reviewer-v1 editions.

- [ ] Verify the direct upper-range reduction covers every edge count above the lower proof frontier for each submitted order.
- [ ] Verify every case split in the Fan-free reduction is exhaustive.
- [ ] Verify no current v2 proof step still logically invokes Fan's 1987 density theorem.
- [ ] Treat Fan citations in historical material as provenance only.

Primary files:

```text
project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md
project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_AUDIT.md
```

## D. Finite-model soundness

For every computational rejection used in a proof:

- [ ] Check that the finite model is a **necessary-condition relaxation** of graph realizability, never an accidental strengthening.
- [ ] Check every pruning step preserves or enlarges the graph-realizable set before rejection.
- [ ] Track dimensions carefully: per label, per source, per unordered pair, or per group.
- [ ] Check grouped multiplicities are applied exactly once.
- [ ] Check boundary values (`0`, maximum degrees, equality cases) are included rather than lost to strict/weak inequality conversion.

## E. Known n=29 normalization failure

A real bug was found in the historical additional verifier `independent_threshold_model.py`.

- [ ] Do **not** accept its v1 cumulative-threshold certificates as evidence.
- [ ] Verify the corrected grouped identity in `independent_threshold_model_v2.py`.
- [ ] Prefer the later minimal trusted kernel as the proof-critical n=29 route.
- [ ] Confirm no current proof surface imports a result only available from the flawed v1 route.

## F. Exact certificate checking

- [ ] Floating-point solver status is never accepted as a proof event.
- [ ] Farkas multipliers have the required signs.
- [ ] Equality constraints are treated correctly when combined.
- [ ] The combined coefficient of every primal variable has the required sign / vanishes as intended.
- [ ] The combined right-hand side is strictly contradictory.
- [ ] Scaling is checked correctly: if a rational contradiction margin is `-1`, a common-denominator integer check requires `<= -scale`, not merely `<= -1`.
- [ ] Independent replay reconstructs the finite rows from source data rather than trusting serialized solver matrices where claimed.

## G. Order-specific reproduction

### n=25

- [ ] Replay all 16 disjoint clean-runner shards.
- [ ] Reconcile 543,578 outer states and 3,442,212 labelled columns.
- [ ] Independently reconstruct the 1,959 final equality certificates.

### n=27

- [ ] Run hardened replay.
- [ ] Reconcile 80,978,546 canonical columns.
- [ ] Reconstruct all 35,435 terminal source-cap vectors.

### n=28

- [ ] Replay the current Fan-free reviewer-v2 dependency chain.
- [ ] For the direct 197-edge component, reproduce the 787 shared + 790 source-degree-type + 7 endpoint-type certificate exclusions and zero survivors.
- [ ] Check the separate equality chain forcing `K(14,14)`.

### n=29

- [ ] Reproduce the minimal trusted kernel.
- [ ] At 211 edges: 72 demand profiles, 126 residual rows, 126 exact late rejections, zero survivors.
- [ ] At 210 edges: 367 demand profiles, 1,467 residual rows, 1,467 exact late rejections, zero survivors.
- [ ] Audit the standalone graph-to-model bridge before treating exact arithmetic as decisive.

### n=30

- [ ] Reproduce Delta=17 clean replay `34292054922`.
- [ ] Reproduce Delta=16 clean runs `34286806474`, `34287440190`, `34287739057`.
- [ ] Confirm 9 final rows at 226 edges and 272 at 225 edges are all exactly rejected.
- [ ] Reproduce final assembly replay `34292557008`.

## H. Equality characterization

For every submitted order:

- [ ] Check the upper-bound argument and equality argument are logically connected rather than merely adjacent computations.
- [ ] Verify the surviving equality conditions force the stated complete bipartite graph.
- [ ] Check no non-isomorphic equality graph is omitted by canonicalization or symmetry reduction.

## I. External-independence standard

A rerun by the same codebase or another program written by the same assistant is useful robustness evidence but is **not independent external verification**.

A strong external reproduction would ideally include at least one of:

- a fresh implementation from the mathematical specification;
- a hand audit of the universal bridge plus an independent exact certificate checker;
- formalization of the bridge / fixed-order theorem in Lean or another proof assistant;
- a specialist graph theorist's line-by-line review.

## Reporting failures

Please report the smallest reproducible failure possible, including:

```text
order / parameter scope
file + lemma or constraint
smallest counterexample or inconsistent row
whether the defect is mathematical, computational, coverage, provenance, or exposition
whether it affects the headline claim or only a redundant route
```

GitHub Issues in `paullenz/MurtySimon742` are the preferred public reporting route.
