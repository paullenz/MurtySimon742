# Type-compressed orientation Hall v1

14 September 2026. **Candidate general structural package. Internal exact audits are green through the sharp-dominance and canonical-antichain layers; external mathematical review, novelty assessment and genuinely independent reproduction remain OPEN.**

## Headline progression

For the directed target-capacity Hall relaxation, group vertices by their identical triple

```text
(q,c,P),
```

where `q` is selected outdegree, `c=q+rho` is cross degree and `P` is the valid incoming target cap used by the relaxation.

The package now gives the following exact progression inside this relaxation.

1. **Whole-type compression.** The Hall deficit is separately discretely concave in every type-count coordinate. If any labelled source subset violates target Hall, then a union of complete `(q,c,P)` type classes also violates it with at least as large a deficiency. See [`TYPE_COMPRESSED_ORIENTATION_HALL.md`](TYPE_COMPRESSED_ORIENTATION_HALL.md).
2. **Exact quotient max-flow.** The labelled target network is min-cut equivalent to a network on the distinct types, and the complete-type Hall margin is submodular. See [`TYPE_LEVEL_MAXFLOW_COROLLARY.md`](TYPE_LEVEL_MAXFLOW_COROLLARY.md).
3. **Interval structure.** Numerical compatibility is exactly intersection of source interval `[q,c]` with target interval `[q,c+1]`, before deletion of the diagonal self-arc.
4. **Sharp dominance.** A maximum-cardinality minimum Hall cut can be chosen as an up-set under

   ```text
   x >=_* y iff c_x<=c_y
                  and [q_x>q_y or (q_x=q_y and P_x>=P_y)].
   ```

   If `q_x>=q_y+2` and `c_x<=c_y`, every minimum Hall witness containing `y` must contain `x`, irrespective of `P`. See [`SHARP_DOMINANCE_UPSET_HALL.md`](SHARP_DOMINANCE_UPSET_HALL.md).
5. **Canonical antichain certificate.** Submodularity makes the minimum-margin type sets a lattice. Their union is the unique maximal minimizer `M+`; it is a sharp-hardness up-set and has a unique minimal antichain boundary. A closure-augmented quotient max-flow recovers the same `M+` from one exact residual min-cut. See [`CANONICAL_ANTICHAIN_CERTIFICATE.md`](CANONICAL_ANTICHAIN_CERTIFICATE.md).

Thus the dominant target-Hall obstruction is no longer an arbitrary labelled max-flow failure: it has an exact type-level, submodular, dominance-closed staircase certificate.

## Verification

### Whole-type theorem

GitHub Actions run `34820069162` completed green. The frozen record [`TYPE_COMPRESSED_ORIENTATION_HALL_VERIFICATION.json`](TYPE_COMPRESSED_ORIENTATION_HALL_VERIFICATION.json) reports

```text
14,330 profiles,
593,984 labelled/compressed cut equalities,
391,896 coordinate-concavity lines,
zero discrepancies.
```

### Exact type-level max-flow

GitHub Actions run `34821405958` completed green. [`verify_type_level_maxflow.py`](verify_type_level_maxflow.py) independently compares labelled and quotient networks, direct and closed-form type cuts, and the submodular margin.

### Initial dominance theorem

GitHub Actions run `34827519117` completed green. The artifact digest is

```text
sha256:5e0977bedbd2615df54f4f31f95ec4847635355f10fad835257d92a65697bd21
```

### Sharp dominance theorem

GitHub Actions run `34830228571` completed green. The artifact digest is

```text
sha256:b686e3f9663a082aa9b0ff9fa89d1c0a29904ca3622f205421a895e3babbf37c
```

The frozen record [`SHARP_DOMINANCE_UPSET_HALL_VERIFICATION.json`](SHARP_DOMINANCE_UPSET_HALL_VERIFICATION.json) reports

```text
4,286 profiles,
1,123,108 submodularity checks,
372,455 sharp exchange checks,
126,654 strict demand-gap checks,
zero discrepancies.
```

### Canonical antichain certificate

GitHub Actions run `34830787798` completed green. The artifact digest is

```text
sha256:2ed919e019c7f65a21fbbe92d81e5db84db14e39889bd259d559e2feded08433
```

The frozen record [`CANONICAL_ANTICHAIN_CERTIFICATE_VERIFICATION.json`](CANONICAL_ANTICHAIN_CERTIFICATE_VERIFICATION.json) reports

```text
4,286 profiles,
198,140 type-set margins,
28,460 minimizer-lattice pair checks,
4,286 closure-flow value checks,
4,286 residual maximal-cut checks,
zero discrepancies.
```

Among the `3,556` negative-margin test profiles, the canonical antichain-generator distribution was

```text
1 generator:   869
2 generators: 1,303
3 generators: 1,005
4 generators:   324
5 generators:    49
6 generators:     6
```

This is audit evidence, not a theorem about generator-number distribution; it strongly cautions against trying to force a universal small-generator bound.

## Preserved failed simplifications

[`PRINCIPAL_UPSET_COUNTEREXAMPLE.md`](PRINCIPAL_UPSET_COUNTEREXAMPLE.md) gives a three-type `V` for which every principal hardness up-set is nondeficient but a two-generator up-set has margin `-1`. A four-type example needs three incomparable generators. Hence neither “one type” nor “one principal up-set” is an exact replacement for the antichain boundary.

The 15-state principal-upset reach pilot agrees with that diagnosis. The full relational stack excludes `13/15` pilot states, but principal up-sets completely explain only `2/13`; they kill more individual profiles than single-type cuts (`17,284` versus `14,768`) without eliminating the genuinely multi-generator obstruction.

## Current research use

The current all-order target is the **canonical antichain staircase**, not further arbitrary labelled Hall enumeration. The generator boundary has strictly increasing `c`; its `q` values are nondecreasing, and within an equal-`q` plateau the generator `P` values are strictly increasing. The next question is whether the Murty-Simon-specific relations among `q`, `rho`, `c=q+rho`, `P`, demand and excess impose stronger bounds on this staircase than are true for arbitrary target-Hall profiles.

In parallel, the checkpointed layer/state-safe relational scan of the canonical `3,607` survivor frontier is discovery only until its recovery and two-implementation audit chain completes. No scan-only candidate changes the canonical frontier.

## Trust boundary

Every theorem in this package is exact for the directed target-flow relaxation under its stated `(q,c,P)` data. Its Murty-Simon application inherits the canonical graph-to-constraint bridge and the validity of the target-capacity bounds. Target-flow feasibility is not graph feasibility.

Repository CI and separately written internal verifiers are not third-party mathematical review. External review and novelty assessment remain open, and the unrestricted Murty-Simon conjecture remains unproved by this project.
