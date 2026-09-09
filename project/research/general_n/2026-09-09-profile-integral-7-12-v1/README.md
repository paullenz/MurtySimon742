# Profile-integral strengthening to 7/12

**Status: candidate theorem under internal hostile audit; not yet promoted to the repository review-paper index. Independent mathematical review and novelty assessment OPEN.**

This directory tests and documents a strengthening of the existing profile-integral maximum-degree result.

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

Files:

- [`PROOF.md`](PROOF.md): standalone candidate hand proof;
- [`src/check_7_12.py`](src/check_7_12.py): exact standard-library algebra and degree-assembly checker;
- `AUDIT.md`: hostile audit record, to be completed before promotion;
- `evidence/`: durable exact run reports.

Promotion gate:

1. exact checker green;
2. independently structured assembly/scalar audit green;
3. hostile proof audit records no unresolved logical defect;
4. reviewer manuscript and verification companion built;
5. top-level README and reviewer index synchronized.
