---
title: "A strengthened profile-integral maximum-degree bound for diameter-2 edge-critical graphs - verification companion"
subtitle: "Reviewer edition 1 - replay, audit and provenance"
author: "Paul Lenz research project; mathematical development and drafting with ChatGPT/Geeps"
date: "9 September 2026"
documentclass: article
fontsize: 11pt
geometry: [a4paper, margin=25mm]
colorlinks: true
linkcolor: "black"
urlcolor: "blue"
---

\begin{abstract}
This companion collects the principal replay instructions, audits, graph-to-model bridges and provenance documents supporting the reviewer manuscript. It is not a substitute for reading the mathematical proof. Exact arithmetic or certificate verification is identified as such in the underlying sources; same-assistant reconstructions are not represented as external independent review.
\end{abstract}

## Reviewer orientation

**Claim under review.** `n >= 6 and Delta(G) >= (7/12)n imply e(G) < floor(n^2/4)`.

**Status.** complete candidate hand argument; internal exact audits green; independent review and novelty assessment OPEN.

**Sources assembled verbatim below:**

- `project/research/general_n/2026-09-09-profile-integral-7-12-v1/README.md`
- `project/research/general_n/2026-09-09-profile-integral-7-12-v1/AUDIT.md`
- `project/research/general_n/2026-09-09-profile-integral-7-12-v1/evidence/run-34355073705/EXACT_CHECK.json`
- `project/research/general_n/2026-09-09-profile-integral-7-12-v1/evidence/run-34355073705/INDEPENDENT_AUDIT.json`
- `project/research/general_n/2026-09-09-profile-integral-7-12-v1/evidence/run-34355073705/RECEIPT.json`

A failed or superseded route remains part of the repository history and is not silently promoted by inclusion in this companion. Reviewers should report suspected flaws through the repository's public review process.

---



\newpage

# Included source: `project/research/general_n/2026-09-09-profile-integral-7-12-v1/README.md`

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


\newpage

# Included source: `project/research/general_n/2026-09-09-profile-integral-7-12-v1/AUDIT.md`

# Hostile audit — profile-integral 7/12 strengthening

9 September 2026.

**Current status: internal hostile audit PASS for the new scalar and degree-assembly layers. Candidate theorem promoted for reviewer packaging; independent mathematical review, novelty assessment and external computational reproduction remain OPEN.**

## Claim under audit

The strengthening is

```text
t < 5a^2/128 + a/8,
```

and consequently

```text
n>=6 and Delta(G)>=(7/12)n  ==>  e(G)<floor(n^2/4).
```

The graph-to-demand, threshold-capacity and shifted-midpoint ingredients are inherited unchanged from the earlier 293/500 candidate. The new attack surface is therefore concentrated in the scalar `5/64` estimate and the new degree assembly.

## Audit outcome

Workflow `General profile-integral 7/12 candidate audit`, run `34355073705`, completed green.

Two separately written standard-library implementations agree exactly:

- `src/check_7_12.py`;
- `src/audit_7_12_independent.py`.

Durable evidence is preserved in `evidence/run-34355073705/` with SHA-256 receipt. The primary checker regressed 5,207,079 eligible `(n,b)` pairs through `n=5000`; the independently structured audit regressed 1,874,246 eligible pairs through `n=3000`. These regressions are consistency checks, not proof by extrapolation.

Both implementations reconstruct the same eleven direct-assembly exceptions and the same threshold caps:

| a | least b | required t | exact upper bound on S-r |
|---:|---:|---:|---:|
| 4 | 7 | 1 | 1 |
| 6 | 10 | 2 | 2 |
| 9 | 14 | 4 | 5 |
| 11 | 17 | 6 | 8 |
| 14 | 21 | 9 | 13 |
| 19 | 28 | 16 | 26 |
| 24 | 35 | 25 | 43 |
| 29 | 42 | 36 | 64 |
| 34 | 49 | 49 | 90 |
| 39 | 56 | 64 | 121 |
| 44 | 63 | 81 | 155 |

Every final column is strictly less than `2t_required`.

## Scalar red-team checklist

1. **Domain shrink — PASS.** `u=y^2/(2x)` satisfies `u<=1/2` because `0<=y<=x<=1`. The cubic minorant is used only on this restricted interval.
2. **Minorant sign — PASS.** `B(u)=1-u/2-u^2/8-3u^3/32` is decreasing and `B(1/2)=181/256>0`.
3. **Square gap — PASS.** Both checkers reconstruct

   ```text
   1-u-B(u)^2 = u^3(64-112u-24u^2-9u^3)/1024.
   ```

   The cubic factor is decreasing and equals `7/8` at `u=1/2`.
4. **Integrated coefficients — PASS.** Independent hand re-expansion gives `x^2/12`, `x^3/160`, `3x^4/1792`.
5. **q substitution — PASS.** Both derivations give

   ```text
   P(q)=2q^2-4q^3+(2/3)q^5+(1/10)q^7+(3/56)q^9.
   ```
6. **Three interval cover — PASS.** `[0,1/3]`, `[1/3,7/20]`, `[7/20,1/sqrt(2)]` cover the complete q-domain.
7. **Low interval — PASS.** `P'>=0` because `Q>=4-12q>=0`.
8. **Middle interval — PASS.** The cubic base decreases, the positive tail increases, and exact arithmetic gives the tail at `7/20` below `1/250`.
9. **High interval — PASS.** `Q'<=-365/64<0` and `Q(7/20)=-1631127391/30720000000<0`.
10. **Strictness — PASS.** The final scalar margin is exactly `11/216000>0`.

## Profile-integral inheritance checklist

1. Cauchy–Schwarz direction — rechecked; unchanged from the 293/500 proof.
2. Lower bound `z_h>=H0>=h` — rechecked and still explicitly required.
3. Nested budget `sum_h z_h<=r` — unchanged.
4. Shifted-midpoint argument and endpoint loss `<=a/4` — re-expanded; unchanged.
5. Domain `s_i/a in [0,1]` — valid, including `s_i=0` separately.

**Trust boundary:** these inherited points remain same-assistant candidate mathematics. A later flaw in the shared graph-to-demand or exact threshold-capacity lemma would affect both this 7/12 result and the earlier 293/500 result.

## Degree-assembly red-team checklist

1. From `b>=7n/12`, exact algebra gives `5b>=7(a+1)` and `(b-a-1)/2 >= (a+1)/5` — PASS.
2. Parity identity `floor(n^2/4)-b(n-b)=floor((b-a-1)^2/4)` — exact regression PASS.
3. Floor loss at most `1/4` — PASS.
4. Large-a difference

   ```text
   D(a)=(a+1)^2/25-1/4-5a^2/128-a/8
   ```

   has coefficient `3/3200`, `D(53)=123/3200`, and first forward difference `177/3200` — PASS in both implementations.
5. Least eligible degree `ceil(7(a+1)/5)` and monotone required surplus — PASS.
6. Direct-bound exception list reconstructed independently as

   ```text
   4,6,9,11,14,19,24,29,34,39,44.
   ```
7. Every exception is closed by the `K_h,w_h,L_h` threshold certificate — PASS, exact table above.
8. `a=0` star and `a=1` edgeless-F cases remain separate — PASS.

## Independence / evidence policy

The two checker implementations share no code, but both were produced within the same AI-assisted project. They are therefore **not external independent reproduction**. The green checks promote the result only to the repository's candidate-theorem status.

The next required steps are reviewer manuscript/verification companion generation, top-level README synchronization, and external specialist review.


\newpage

# Included source: `project/research/general_n/2026-09-09-profile-integral-7-12-v1/evidence/run-34355073705/EXACT_CHECK.json`

{
  "degree_assembly": {
    "D53": "123/3200",
    "exception_count": 11,
    "exceptions": [
      {
        "HS_cases": 21,
        "a": 4,
        "first_maximising_HS": [
          1,
          4
        ],
        "least_b": 7,
        "required_t": 1,
        "threshold_cases": 48,
        "upper_S_minus_r": 1
      },
      {
        "HS_cases": 80,
        "a": 6,
        "first_maximising_HS": [
          1,
          6
        ],
        "least_b": 10,
        "required_t": 2,
        "threshold_cases": 290,
        "upper_S_minus_r": 2
      },
      {
        "HS_cases": 296,
        "a": 9,
        "first_maximising_HS": [
          2,
          18
        ],
        "least_b": 14,
        "required_t": 4,
        "threshold_cases": 1668,
        "upper_S_minus_r": 5
      },
      {
        "HS_cases": 560,
        "a": 11,
        "first_maximising_HS": [
          2,
          22
        ],
        "least_b": 17,
        "required_t": 6,
        "threshold_cases": 3905,
        "upper_S_minus_r": 8
      },
      {
        "HS_cases": 1196,
        "a": 14,
        "first_maximising_HS": [
          3,
          42
        ],
        "least_b": 21,
        "required_t": 9,
        "threshold_cases": 10738,
        "upper_S_minus_r": 13
      },
      {
        "HS_cases": 3096,
        "a": 19,
        "first_maximising_HS": [
          5,
          79
        ],
        "least_b": 28,
        "required_t": 16,
        "threshold_cases": 38133,
        "upper_S_minus_r": 26
      },
      {
        "HS_cases": 6371,
        "a": 24,
        "first_maximising_HS": [
          6,
          126
        ],
        "least_b": 35,
        "required_t": 25,
        "threshold_cases": 99728,
        "upper_S_minus_r": 43
      },
      {
        "HS_cases": 11396,
        "a": 29,
        "first_maximising_HS": [
          8,
          208
        ],
        "least_b": 42,
        "required_t": 36,
        "threshold_cases": 216398,
        "upper_S_minus_r": 64
      },
      {
        "HS_cases": 18546,
        "a": 34,
        "first_maximising_HS": [
          9,
          276
        ],
        "least_b": 49,
        "required_t": 49,
        "threshold_cases": 414018,
        "upper_S_minus_r": 90
      },
      {
        "HS_cases": 28196,
        "a": 39,
        "first_maximising_HS": [
          11,
          369
        ],
        "least_b": 56,
        "required_t": 64,
        "threshold_cases": 723463,
        "upper_S_minus_r": 121
      },
      {
        "HS_cases": 40721,
        "a": 44,
        "first_maximising_HS": [
          12,
          462
        ],
        "least_b": 63,
        "required_t": 81,
        "threshold_cases": 1180608,
        "upper_S_minus_r": 155
      }
    ],
    "first_forward_difference": "177/3200",
    "large_a_start": 53,
    "ordinary_small_a_count": 40
  },
  "regression": {
    "eligible_degree_pairs_checked": 5207079,
    "max_n": 5000
  },
  "scalar": {
    "Q_at_7_over_20": "-1631127391/30720000000",
    "Qprime_uniform_upper": "-365/64",
    "consequence": "t < 5*a^2/128 + a/8",
    "middle_margin": "11/216000",
    "scalar_upper": "5/64",
    "sqrt_minorant_B_at_half": "181/256",
    "sqrt_minorant_core_at_half": "7/8",
    "tail_at_7_over_20": "43868404489/12288000000000"
  },
  "schema": "profile-integral-7-12-exact-check-v1"
}


\newpage

# Included source: `project/research/general_n/2026-09-09-profile-integral-7-12-v1/evidence/run-34355073705/INDEPENDENT_AUDIT.json`

{
  "assembly": {
    "D53": "123/3200",
    "exceptions": [
      {
        "HS_cases": 21,
        "a": 4,
        "cap_S_minus_r": 1,
        "least_b": 7,
        "required_t": 1,
        "threshold_cases": 48,
        "witness_HS": [
          1,
          4
        ]
      },
      {
        "HS_cases": 80,
        "a": 6,
        "cap_S_minus_r": 2,
        "least_b": 10,
        "required_t": 2,
        "threshold_cases": 290,
        "witness_HS": [
          1,
          6
        ]
      },
      {
        "HS_cases": 296,
        "a": 9,
        "cap_S_minus_r": 5,
        "least_b": 14,
        "required_t": 4,
        "threshold_cases": 1668,
        "witness_HS": [
          2,
          18
        ]
      },
      {
        "HS_cases": 560,
        "a": 11,
        "cap_S_minus_r": 8,
        "least_b": 17,
        "required_t": 6,
        "threshold_cases": 3905,
        "witness_HS": [
          2,
          22
        ]
      },
      {
        "HS_cases": 1196,
        "a": 14,
        "cap_S_minus_r": 13,
        "least_b": 21,
        "required_t": 9,
        "threshold_cases": 10738,
        "witness_HS": [
          3,
          42
        ]
      },
      {
        "HS_cases": 3096,
        "a": 19,
        "cap_S_minus_r": 26,
        "least_b": 28,
        "required_t": 16,
        "threshold_cases": 38133,
        "witness_HS": [
          5,
          79
        ]
      },
      {
        "HS_cases": 6371,
        "a": 24,
        "cap_S_minus_r": 43,
        "least_b": 35,
        "required_t": 25,
        "threshold_cases": 99728,
        "witness_HS": [
          6,
          126
        ]
      },
      {
        "HS_cases": 11396,
        "a": 29,
        "cap_S_minus_r": 64,
        "least_b": 42,
        "required_t": 36,
        "threshold_cases": 216398,
        "witness_HS": [
          8,
          208
        ]
      },
      {
        "HS_cases": 18546,
        "a": 34,
        "cap_S_minus_r": 90,
        "least_b": 49,
        "required_t": 49,
        "threshold_cases": 414018,
        "witness_HS": [
          9,
          276
        ]
      },
      {
        "HS_cases": 28196,
        "a": 39,
        "cap_S_minus_r": 121,
        "least_b": 56,
        "required_t": 64,
        "threshold_cases": 723463,
        "witness_HS": [
          11,
          369
        ]
      },
      {
        "HS_cases": 40721,
        "a": 44,
        "cap_S_minus_r": 155,
        "least_b": 63,
        "required_t": 81,
        "threshold_cases": 1180608,
        "witness_HS": [
          12,
          462
        ]
      }
    ],
    "forward_53": "177/3200"
  },
  "degree_pairs_regressed": 1874246,
  "scalar": {
    "B_half": "181/256",
    "Q_7_20": "-1631127391/30720000000",
    "Qprime_cap": "-365/64",
    "core_half": "7/8",
    "gap_coefficients": [
      "0",
      "0",
      "0",
      "1/16",
      "-7/64",
      "-3/128",
      "-9/1024"
    ],
    "margin": "11/216000",
    "tail_7_20": "43868404489/12288000000000"
  },
  "schema": "profile-integral-7-12-independent-audit-v1"
}


\newpage

# Included source: `project/research/general_n/2026-09-09-profile-integral-7-12-v1/evidence/run-34355073705/RECEIPT.json`

{
  "files": {
    "EXACT_CHECK.json": {
      "bytes": 3359,
      "sha256": "aa8f445276d6c0f2f39ae3ac02c3d39c00a5ea6434405c1bba924462a38f32e7"
    },
    "INDEPENDENT_AUDIT.json": {
      "bytes": 3077,
      "sha256": "19200edb90c10765dba2bddafebb00e5aa5700a897ab0f42d945a93518036377"
    }
  },
  "run_id": "34355073705",
  "schema": "profile-integral-7-12-audit-receipt-v1"
}
