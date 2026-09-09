# Profile-integral strengthening to 7/12

**Status: complete candidate hand argument; internal exact audits green and reviewer package published. Independent mathematical review, novelty assessment and external computational reproduction remain OPEN.**

This directory documents the current strongest reviewer-packaged profile-integral maximum-degree candidate.

Candidate statements:

```text
t < 5 a^2 / 128 + a / 8,
```

and, for a diameter-two edge-critical graph on `n>=6` vertices,

```text
Delta(G) >= (7/12)n  ==>  e(G) < floor(n^2/4).
```

The graph-to-demand construction and threshold-capacity lemma are unchanged from `../2026-09-08-profile-integral-v1/`. The improvement comes from observing that the integral substitution only requires a square-root minorant on `0<=u<=1/2`, allowing the sharper exact polynomial

```text
1 - u/2 - u^2/8 - 3u^3/32.
```

The resulting scalar certificate is

```text
x - Phi(x) < 5/64,
```

which yields the improved surplus coefficient `5/128`.

Reviewer entry point: [`../../../../releases/general-7-12-reviewer-v1/README.md`](../../../../releases/general-7-12-reviewer-v1/README.md).

Files and evidence:

- [`PROOF.md`](PROOF.md): standalone candidate hand proof;
- [`AUDIT.md`](AUDIT.md): completed internal hostile audit record;
- [`src/check_7_12.py`](src/check_7_12.py): primary exact standard-library algebra and degree-assembly checker;
- [`src/audit_7_12_independent.py`](src/audit_7_12_independent.py): separately structured exact audit with no imports from the primary checker;
- [`evidence/run-34355073705/`](evidence/run-34355073705/): durable exact reports and SHA-256 receipt;
- [`PROFILE_INTEGRAL_CEILING.md`](PROFILE_INTEGRAL_CEILING.md): strategic note on the intrinsic asymptotic ceiling of the scalar-uniform profile-integral architecture.

Audit summary:

- primary exact checker: green;
- separately structured exact audit: green;
- both reconstruct the same eleven finite assembly exceptions and the same exact threshold caps;
- primary degree-pair regression through `n=5000`: 5,207,079 eligible pairs;
- separate regression through `n=3000`: 1,874,246 eligible pairs;
- reviewer manuscript and verification companion: built, PDF/text/render preflight green, published to `main`;
- top-level README and review-paper index: synchronized.

The degree-pair regressions are consistency checks rather than proof by exhaustion. The principal trust boundary remains the shared graph-to-demand/profile-integral argument inherited from the 293/500 candidate. Same-assistant implementations are not external independent review.
