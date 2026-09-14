# Type-compressed orientation Hall v1

14 September 2026. **Candidate general structural package. Internal exact audits are green through the exact staircase-threshold theorem and the staircase-band necessary relaxation; external mathematical review, novelty assessment and genuinely independent third-party reproduction remain OPEN.**

## Headline progression

For the directed target-capacity Hall relaxation, group vertices by their identical triple

```text
(q,c,P),
```

where `q` is selected outdegree, `c=q+rho` is cross degree and `P` is the valid incoming target cap used by the relaxation.

The package now gives the following chain.

1. **Whole-type compression — exact.** The Hall deficit is separately discretely concave in every type-count coordinate. If any labelled source subset violates target Hall, then a union of complete `(q,c,P)` type classes also violates it with at least as large a deficiency. See [`TYPE_COMPRESSED_ORIENTATION_HALL.md`](TYPE_COMPRESSED_ORIENTATION_HALL.md).
2. **Exact quotient max-flow — exact.** The labelled target network is min-cut equivalent to a network on the distinct types, and the complete-type Hall margin is submodular. See [`TYPE_LEVEL_MAXFLOW_COROLLARY.md`](TYPE_LEVEL_MAXFLOW_COROLLARY.md).
3. **Interval structure — exact.** Numerical compatibility is exactly intersection of source interval `[q,c]` with target interval `[q,c+1]`, before deletion of the diagonal self-arc.
4. **Sharp dominance — exact.** A maximum-cardinality minimum Hall cut can be chosen as an up-set under

   ```text
   x >=_* y iff c_x<=c_y
                  and [q_x>q_y or (q_x=q_y and P_x>=P_y)].
   ```

   If `q_x>=q_y+2` and `c_x<=c_y`, every minimum Hall witness containing `y` must contain `x`, irrespective of `P`. See [`SHARP_DOMINANCE_UPSET_HALL.md`](SHARP_DOMINANCE_UPSET_HALL.md).
5. **Canonical antichain certificate — exact.** Submodularity makes the minimum-margin type sets a lattice. Their union is the unique maximal minimizer `M+`; it is a sharp-hardness up-set and has a unique minimal antichain boundary. A closure-augmented quotient max-flow recovers the same `M+` from one exact residual min-cut. See [`CANONICAL_ANTICHAIN_CERTIFICATE.md`](CANONICAL_ANTICHAIN_CERTIFICATE.md).
6. **Moving staircase threshold — exact.** If the minimal generators are ordered by increasing cross degree `c`, their demand `q` is nondecreasing and `P` strictly increases on equal-`q` plateaus. Every type's membership is determined exactly by the first generator cross-degree above it and one moving `(q,P)` threshold. See [`STAIRCASE_THRESHOLD_HALL.md`](STAIRCASE_THRESHOLD_HALL.md).
7. **Staircase-band flow — necessary relaxation.** Group selected sources by staircase band. Every target type sees a contiguous interval of generator-compatible bands, giving a smaller capacitated interval-neighborhood flow. Exact target-flow feasibility implies band-flow feasibility, but not conversely. See [`STAIRCASE_BAND_HALL.md`](STAIRCASE_BAND_HALL.md).

Thus the dominant target-Hall obstruction is no longer an arbitrary labelled max-flow failure: its exact certificate is a canonical type-level staircase, and it admits a further consecutive-band relaxation suitable for aggregate all-order arguments.

## Verification

### Whole-type theorem

GitHub Actions run `34820069162` completed green. [`TYPE_COMPRESSED_ORIENTATION_HALL_VERIFICATION.json`](TYPE_COMPRESSED_ORIENTATION_HALL_VERIFICATION.json) reports

```text
14,330 profiles,
593,984 labelled/compressed cut equalities,
391,896 coordinate-concavity lines,
zero discrepancies.
```

### Exact type-level max-flow

GitHub Actions run `34821405958` completed green. [`verify_type_level_maxflow.py`](verify_type_level_maxflow.py) independently compares labelled and quotient networks, direct and closed-form type cuts, and the submodular margin.

### Initial dominance theorem

GitHub Actions run `34827519117` completed green.

```text
sha256:5e0977bedbd2615df54f4f31f95ec4847635355f10fad835257d92a65697bd21
```

### Sharp dominance theorem

GitHub Actions run `34830228571` completed green.

```text
sha256:b686e3f9663a082aa9b0ff9fa89d1c0a29904ca3622f205421a895e3babbf37c
```

[`SHARP_DOMINANCE_UPSET_HALL_VERIFICATION.json`](SHARP_DOMINANCE_UPSET_HALL_VERIFICATION.json):

```text
4,286 profiles,
1,123,108 submodularity checks,
372,455 sharp exchange checks,
126,654 strict demand-gap checks,
zero discrepancies.
```

### Canonical antichain certificate

GitHub Actions run `34830787798` completed green.

```text
sha256:2ed919e019c7f65a21fbbe92d81e5db84db14e39889bd259d559e2feded08433
```

[`CANONICAL_ANTICHAIN_CERTIFICATE_VERIFICATION.json`](CANONICAL_ANTICHAIN_CERTIFICATE_VERIFICATION.json):

```text
4,286 profiles,
198,140 type-set margins,
28,460 minimizer-lattice pair checks,
4,286 closure-flow value checks,
4,286 residual maximal-cut checks,
zero discrepancies.
```

### Exact staircase threshold

GitHub Actions run `34831605792` completed green.

```text
sha256:96ca7d14e9b823ae428f677f21cf60cfa519e7f6326799fcf9b331e433d38ace
```

[`STAIRCASE_THRESHOLD_HALL_VERIFICATION.json`](STAIRCASE_THRESHOLD_HALL_VERIFICATION.json):

```text
4,286 profiles,
69,136 sharp up-sets,
77,285 generator-step checks,
411,436 membership checks,
69,136 exact staircase reconstructions,
69,136 rectangle-margin checks,
zero discrepancies.
```

### Staircase-band relaxation

GitHub Actions run `34832155910` completed green.

```text
sha256:ced7c25892c42a0a13a61c404642da6f27af21607655be255b20efd498a03a24
```

[`STAIRCASE_BAND_HALL_VERIFICATION.json`](STAIRCASE_BAND_HALL_VERIFICATION.json):

```text
2,786 profiles,
39,991 sharp up-sets,
112,807 source-interval containment checks,
214,908 consecutive target-band checks,
1,334,288 incoming upper-bound checks,
210,356 band-set capacity checks,
zero discrepancies.
```

For detailed provenance and trust boundaries see [`AUDIT.md`](AUDIT.md) and the continuation [`STAIRCASE_AUDIT.md`](STAIRCASE_AUDIT.md).

## Preserved failed simplifications

[`PRINCIPAL_UPSET_COUNTEREXAMPLE.md`](PRINCIPAL_UPSET_COUNTEREXAMPLE.md) gives a three-type `V` for which every principal hardness up-set is nondeficient but a two-generator up-set has margin `-1`. A four-type example needs three incomparable generators. Hence neither “one type” nor “one principal up-set” is an exact replacement for the antichain boundary.

The 15-state principal-upset reach pilot agrees with that diagnosis. The full relational stack excludes `13/15` pilot states, but principal up-sets completely explain only `2/13`; they kill more individual profiles than single-type cuts (`17,284` versus `14,768`) without eliminating the genuinely multi-generator obstruction.

## Murty-specific generator complexity

[`MURTY_ANTICHAIN_PROFILE_STATS_PILOT.md`](MURTY_ANTICHAIN_PROFILE_STATS_PILOT.md) instruments the same deterministic 15-state Murty-Simon pilot. Every labelled target-Hall failure is cross-checked against the independently built sharp-dominance-closed quotient max-flow before its canonical generator count is recorded.

GitHub Actions run `34831697002` completed green; artifact digest:

```text
sha256:b0f5596399faf3e273a981a0e8c2929b3c1c2c34bf50047e2be085bf4bb65222
```

Across `201,493,148` tested profiles there were `205,919` target-Hall failures, with canonical generator counts:

```text
1:      214
2:    6,722
3:   41,452
4:   80,972
5:   58,775
6:   16,349
7:    1,426
8:        9
9+:       0
```

The modal obstruction has **four** generators and actual Murty-Simon profiles reach eight. This is reconnaissance, not a theorem or promotion, but it decisively lowers the priority of any universal small-generator approach.

## Current research use

The current all-order target is the **aggregate staircase-band flow**. The exact canonical boundary has strictly increasing `c`, nondecreasing `q`, and strictly increasing `P` along equal-`q` plateaus. In the current Murty-Simon source universe `q<=a-rho` and `c=q+rho`, hence `c<=a` and there is at most one generator breakpoint per integer cross-degree level.

The next question is whether the Murty-Simon-specific relations among `q`, `rho`, target cap `P`, demand, selected incidence, pair capacity and excess force the consecutive-band Hall inequalities automatically, or reduce a violating band interval to a small parametric family. That route can remain compact even though the raw number of generators is not small.

In parallel, the checkpointed layer/state-safe relational scan of the canonical `3,607` survivor frontier is discovery only until its recovery and two-implementation audit chain completes. No scan-only candidate changes the canonical frontier.

## Trust boundary

Theorems through the staircase threshold are exact for the directed target-flow relaxation under their stated `(q,c,P)` data. The staircase-band result is explicitly a necessary relaxation. Their Murty-Simon application inherits the canonical graph-to-constraint bridge and the validity of the target-capacity bounds. Target-flow feasibility is not graph feasibility.

Repository CI and separately written internal verifiers are not third-party mathematical review. External review and novelty assessment remain open, and the unrestricted Murty-Simon conjecture remains unproved by this project.
