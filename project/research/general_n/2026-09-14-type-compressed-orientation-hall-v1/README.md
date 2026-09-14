# Type-compressed orientation Hall v1

14 September 2026. **Candidate general structural result. Internal exact audit green; external mathematical review, novelty assessment and independent reproduction remain OPEN.**

## Headline result

For the directed target-capacity Hall relaxation, group vertices by their identical triple

```text
(q,c,P),
```

where `q` is selected outdegree, `c=q+rho` is cross degree and `P` is the valid incoming target cap used by the relaxation.

The exact Hall deficit is separately discretely concave in every type-count coordinate. Consequently:

> If any source subset violates target Hall, then a union of complete `(q,c,P)` type classes also violates it with at least as large a deficiency.

Thus a profile with `k` distinct types needs at most `2^k` complete-type cuts rather than arbitrary labelled subsets. See [`TYPE_COMPRESSED_ORIENTATION_HALL.md`](TYPE_COMPRESSED_ORIENTATION_HALL.md) for the proof.

## Verification

[`AUDIT.md`](AUDIT.md) records the internal audit. GitHub Actions run `34820069162` completed green.

The frozen verifier record reports:

```text
14,330 profiles,
593,984 labelled/compressed cut equalities,
391,896 coordinate-concavity lines,
zero discrepancies.
```

The verifier is [`verify_type_compressed_orientation_hall.py`](verify_type_compressed_orientation_hall.py); its frozen output is [`TYPE_COMPRESSED_ORIENTATION_HALL_VERIFICATION.json`](TYPE_COMPRESSED_ORIENTATION_HALL_VERIFICATION.json).

## Why it matters

The current full post-pair frontier reconnaissance indicates that directed target-Hall is the dominant new exclusion layer. This theorem converts those max-flow failures into compact exact type-set certificates and narrows the next all-order question to a two-dimensional dominance problem on types.

It does **not** restore the disproved one-dimensional Ferrers-prefix shortcut. A minimum deficient type set can still have genuinely two-dimensional structure.

## Trust boundary

The theorem is exact for the target-flow network. Its Murty-Simon application inherits the canonical bridge and target-cap hypotheses. Target-flow feasibility is not graph feasibility, and the unrestricted Murty-Simon conjecture remains unproved by this project.
