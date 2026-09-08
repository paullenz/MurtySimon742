# Start here for reviewers

## What this repository is

This repository contains **AI-assisted candidate mathematics** concerning the Murty–Simon conjecture / Erdős Problem #742, together with code, exact certificates, replay workflows, red-team reports and failed intermediate approaches.

Nothing here should be treated as externally accepted mathematics merely because a workflow is green. The fixed-order results and general structural results are explicitly labelled **candidate** until they receive genuinely independent mathematical review. Same-assistant reimplementations reduce implementation risk but are not external independence.

Paul Lenz directed the project and chose the research priorities. ChatGPT/Geeps supplied the mathematical development, implementations, manuscripts and internal audits.

If you find an error, please open a GitHub Issue. A short counterexample or a precise identification of the first invalid implication is more valuable than a general assessment.

## Headline candidate results

The repository currently contains candidate fixed-order Murty–Simon results for:

- `n=25`: `e(G) <= 156`, equality only `K(12,13)`;
- `n=27`: `e(G) <= 182`, equality only `K(13,14)`;
- `n=28`: `e(G) <= 196`, equality only `K(14,14)`;
- `n=29`: `e(G) <= 210`, equality only `K(14,15)`.

It also contains a general structural programme, including the candidate implication

```text
n >= 6 and Delta(G) >= (293/500)n  ==>  e(G) < floor(n^2/4).
```

No unrestricted all-order proof is claimed.

## Recommended first review: n=29

The n=29 candidate is the cleanest current place to audit the programme because most degree ranges are eliminated by short hand arguments and the difficult `Delta=16` case now has a deliberately reduced trusted kernel.

Main proof:

- [`project/reviews/n29/2026-09-08-candidate-v1/PROOF.md`](project/reviews/n29/2026-09-08-candidate-v1/PROOF.md)

Restarted hostile audit:

- [`project/reviews/n29/2026-09-08-redteam-restart-v1/N29_RED_TEAM_RESTART.md`](project/reviews/n29/2026-09-08-redteam-restart-v1/N29_RED_TEAM_RESTART.md)
- [`project/reviews/n29/2026-09-08-redteam-restart-v1/SOURCE_AND_CERTIFICATE_AUDIT.md`](project/reviews/n29/2026-09-08-redteam-restart-v1/SOURCE_AND_CERTIFICATE_AUDIT.md)
- [`project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md`](project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md)

### n=29 proof structure

For a 29-vertex diameter-two edge-critical graph `G`:

1. Published reductions and degree sum leave a small number of dense degree cases.
2. `Delta=15` is handled by a witness/deficit hand count; at 210 edges equality forces `K(14,15)`.
3. `Delta=16` is excluded by the finite trusted kernel described below.
4. `Delta=17` is excluded by a short pointwise charging inequality.
5. `Delta=18,...,27` are excluded by the residual h-index inequality.
6. `Delta=28` gives a universal vertex and hence a star.

The highest-value mathematical review is therefore the **graph-to-demand bridge for `Delta=16`**, not another rerun of the arithmetic.

## Minimal trusted kernel for n=29, Delta=16

The preferred current route deliberately removes several older layers of computation. Its logical chain is:

```text
quasi-edge / selected-residual construction
        -> residual activity
        -> demand and charging inequalities
        -> exact threshold-capacity inequality
        -> exact source-capacity dual pruning
        -> simple residual-row Hall/refinement scan
        -> corrected cumulative-threshold/source-q-flow LP
        -> exact integer Farkas verification
```

The clean-runner result is recorded in:

- [`project/reviews/n29/2026-09-08-redteam-restart-v1/MINIMAL_KERNEL_REPORT.json`](project/reviews/n29/2026-09-08-redteam-restart-v1/MINIMAL_KERNEL_REPORT.json)

It reports:

| Edge count | `t` | Demand profiles retained | Residual rows | Exact late rejections | Final survivors |
|---:|---:|---:|---:|---:|---:|
| 211 | 3 | 72 | 126 | 126 | 0 |
| 210 | 2 | 367 | 1,467 | 1,467 | 0 |

Every late exclusion is rechecked by exact integer arithmetic. Floating-point LP output is used only to propose a Farkas ray; solver status by itself is never a proof event.

The minimal route does **not** use the old projected screen, joint propagator, shared LP, typed LP, old endpoint LP or the older pair-capacity support formula. Those remain in the repository as redundant evidence and research history.

Relevant source:

- [`minimal_prepare.py`](project/reviews/n29/2026-09-08-redteam-restart-v1/minimal_prepare.py)
- [`minimal_rows.cpp`](project/reviews/n29/2026-09-08-redteam-restart-v1/minimal_rows.cpp)
- [`independent_threshold_model_v2.py`](project/reviews/n29/2026-09-08-redteam-restart-v1/independent_threshold_model_v2.py)
- [`run_minimal_kernel.py`](project/reviews/n29/2026-09-08-redteam-restart-v1/run_minimal_kernel.py)
- [clean GitHub Actions workflow](.github/workflows/n29-minimal-kernel.yml)

## Important audit history: a real bug was found

During the hostile n=29 bridge audit, an error was found in the first version of the *additional* cumulative-threshold verifier, `independent_threshold_model.py`.

The grouped selected-incidence equation multiplied label-side capacity by the label-group multiplicity twice. In normalized form the correct identity is per label, schematically

```text
sum_k n_k Z_kg = sum_h T_h,
```

not

```text
sum_k n_k Z_kg = n_g * sum_h T_h.
```

Accordingly:

- the **v1 cumulative-threshold certificates are not valid proof evidence**;
- the flawed v1 source is retained for audit history and must not be cited as a verifier;
- the error did not affect the original n=29 direct route or the separate fully fresh implementation, which use different machinery;
- [`independent_threshold_model_v2.py`](project/reviews/n29/2026-09-08-redteam-restart-v1/independent_threshold_model_v2.py) fixes the normalization;
- corrected v2 was replayed cleanly and again produced zero survivors;
- the later minimal trusted-kernel replay also uses the corrected v2 model and produced zero survivors.

This history is intentionally public. Finding such an error is evidence that the red-team process is doing useful work; it is not being silently edited out of the record.

## What to attack first

A useful hostile review would try to break these points in roughly this order:

1. **Complement/quasi-edge construction.** Does every missing `B`-pair really force the selected cross-edge structure claimed?
2. **Injection and uniqueness.** Are selected edges, supplements and unordered `B`-pairs counted without collisions?
3. **Residual activity.** For `t>0`, is the proof that every `B` row has positive residual degree valid in all edge cases?
4. **Demand implication.** Does `s_i=max(0,d_i-R_i)` genuinely require `s_i` distinct selected sources with enough residual degree?
5. **Charging inequality.** Check the per-source charge budget and the passage to the summed demand inequality.
6. **Threshold-capacity lemma.** Check the high-demand/high-residual source counting and unordered-pair capacity.
7. **Exact source-capacity dual.** Verify that it is only a necessary Hall relaxation and that the saved integer dual inequality proves each rejection.
8. **Residual-row scanner.** Check that every pruning operation enlarges or preserves the graph-realizable set before rejection.
9. **Corrected v2 LP normalization.** Track every grouped variable dimensionally: per label, per source, or per possible pair.
10. **Exact Farkas checker.** Confirm multiplier signs, equality treatment, coefficientwise nonnegativity and strictly negative combined RHS.

A single valid counterexample to any universal lemma is enough to invalidate the dependent route and should be reported immediately.

## Other fixed-order packages

For the older fixed-order cases, start from the root [`README.md`](README.md) and then use the release/review directories it links. Each scope has its own proof, replay artefacts and audit status.

## General structural programme

The current general candidate route is:

- [`project/research/general_n/2026-09-08-profile-integral-v1/PROOF.md`](project/research/general_n/2026-09-08-profile-integral-v1/PROOF.md)
- [`project/research/general_n/2026-09-08-profile-integral-v1/AUDIT.md`](project/research/general_n/2026-09-08-profile-integral-v1/AUDIT.md)

Earlier structural checkpoints are preserved because failed or superseded approaches may still contain useful lemmas or ideas. Their presence should not be read as multiple independent proofs of the same statement.

## Reproduction philosophy

The repository attempts to distinguish:

- mathematical lemmas;
- finite necessary-condition systems;
- exploratory numerical solver output;
- exact machine-checkable certificates;
- same-assistant reimplementation;
- genuinely independent external review.

Only the first four can currently be supplied internally. External mathematical and computational review remains explicitly open.

## How to report a problem

Please open a GitHub Issue and include, where possible:

- the exact file and lemma/constraint;
- the smallest configuration or parameter values that expose the problem;
- whether the issue is mathematical, implementation, reproducibility, attribution/literature, or exposition;
- whether it changes a headline candidate result or only a redundant verification route.

Corrections should preserve the original evidence and failure history rather than overwrite it silently.

## Licence

The repository is released under the MIT licence in [`LICENSE`](LICENSE).
