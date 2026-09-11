# Start here for reviewers

**Updated 11 September 2026.**

## What this repository is

This repository contains **AI-assisted candidate mathematics** concerning the Murty–Simon conjecture / Erdős Problem #742, together with code, exact certificates, replay workflows, red-team reports and failed intermediate approaches.

Nothing here should be treated as externally accepted mathematics merely because a workflow is green. The fixed-order results and general structural results are explicitly labelled **candidate** until they receive genuinely independent mathematical review. Same-assistant reimplementations reduce implementation risk but are not external independence.

Paul Lenz directed the project and chose the research priorities. ChatGPT/Geeps supplied the mathematical development, implementations, manuscripts and internal audits.

If you find an error, please open a GitHub Issue. A short counterexample or a precise identification of the first invalid implication is more valuable than a general assessment.

## Headline candidate results

The repository currently contains complete candidate fixed-order Murty–Simon results for:

- `n=25`: `e(G) <= 156`, equality only `K(12,13)`;
- `n=27`: `e(G) <= 182`, equality only `K(13,14)`;
- `n=28`: `e(G) <= 196`, equality only `K(14,14)`;
- `n=29`: `e(G) <= 210`, equality only `K(14,15)`;
- `n=30`: `e(G) <= 225`, equality only `K(15,15)`.

The PDF reviewer packages in [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md) are the **Fan-free v2 editions**. For `n=29`, the current text proof has since been hardened further as **reviewer-v3** after a blind external-assistant red-team; the v2 PDF remains preserved until a new reviewer PDF is built.

The strongest current reviewer-packaged general candidate is

```text
n >= 6 and Delta(G) >= (7/12)n  ==>  e(G) < floor(n^2/4).
```

Start with [`releases/general-7-12-reviewer-v1/README.md`](releases/general-7-12-reviewer-v1/README.md). This is a complete candidate hand argument with internal exact audits green; independent mathematical review, novelty assessment and external reproduction remain open.

The active RX-Hall / 3-D potential programme is attempting to go below the `7/12` frontier by retaining more joint profile information. It has exact finite compression results, but **no unrestricted theorem is claimed from that programme yet**.

No unrestricted all-order proof is claimed anywhere in the repository.

## n=25: the natural fixed-order paper to inspect

The project treats `n=25` as a candidate resolution of the conspicuous order-25 gap between Fan's published `n<=24` and `n=26` results.

Current package:

- [`releases/n25-reviewer-v2/README.md`](releases/n25-reviewer-v2/README.md)
- [`project/reviews/n25/2026-09-09-fan-free-v2/PROOF.md`](project/reviews/n25/2026-09-09-fan-free-v2/PROOF.md)
- [`project/reviews/n25/2026-09-08-reaudit-v1/README.md`](project/reviews/n25/2026-09-08-reaudit-v1/README.md)

The complete finite domain was replayed in sixteen disjoint clean-runner shards covering 543,578 outer states and 3,442,212 labelled columns. A separately written terminal re-audit imported no frozen verifier and independently reconstructed all 1,959 final equality certificates. No blocking mathematical defect was found in that internal re-audit.

The principal remaining question is therefore not whether the arithmetic replay terminates, but whether the graph-to-model reductions and their hypotheses are universally sound.

## Robustness milestone: Fan-free fixed-order proofs and analytic hardening

A hostile external-AI critique questioned both selected/residual semantics and the use of G. Fan's 1987 density theorem as an edge-count cap. The semantic objections were re-audited and resolved explicitly in the current proof text. The project then removed Fan as a **logical dependency** from its current fixed-order candidate proofs at `n=25,27,28,29,30`, while retaining Fan's theorem as historical attribution and preserving every reviewer-v1/proof source unchanged.

The direct replacement is [`FAN_FREE_REDUCTION.md`](project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md), and its assembled edge-range/source-integrity checks are recorded in [`FAN_FREE_AUDIT.md`](project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_AUDIT.md). The audit is internal; independent review of the graph-theoretic bridge remains open.

A second blind external-assistant red-team of `n=29`, supplied on 11 September without project background, attacked the bridge, residual activity, threshold capacity, isolated-C, corrected late-LP normalization, exact Farkas semantics and the hand assembly and reported no fatal defect. Its follow-up and our independent reproduction are preserved in [`FOLLOWUP.md`](project/reviews/n29/2026-09-11-blind-external-ai-redteam-v1/FOLLOWUP.md).

That review also found a useful pointwise charging bound which removes several historical computations from the **logical** dependency chain. The exact cross-order derivation is [`POINTWISE_CAPS.md`](project/research/fan-free-fixed-orders/2026-09-11-pointwise-analytic-caps-v1/POINTWISE_CAPS.md). In particular:

- `n=28, Delta=15`: every `m>=203` is now a hand exclusion;
- `n=29, Delta=16`: `m=215` is a hand threshold contradiction and every `m>=216` is a one-line hand exclusion;
- `n=30, Delta=17`: every `m>=228` is now a hand exclusion;
- `n=30, Delta=16`: every `m>=234` is now a hand exclusion.

Historical workflows for those ranges remain preserved as corroborating evidence only.

## Recommended bridge audit: n=29

The n=29 candidate remains a clean place to audit the universal graph-to-demand machinery because most degree ranges are eliminated by short hand arguments and the difficult `Delta=16` case has a deliberately reduced trusted kernel. The same bridge is then parameterised at n=30.

**Current reviewer-v3 text proof:**

- [`project/reviews/n29/2026-09-11-reviewer-v3/README.md`](project/reviews/n29/2026-09-11-reviewer-v3/README.md)
- [`project/reviews/n29/2026-09-11-reviewer-v3/PROOF.md`](project/reviews/n29/2026-09-11-reviewer-v3/PROOF.md)

**Current self-contained graph-to-model bridge:**

- [`project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md`](project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md)

**Blind external red-team follow-up:**

- [`project/reviews/n29/2026-09-11-blind-external-ai-redteam-v1/FOLLOWUP.md`](project/reviews/n29/2026-09-11-blind-external-ai-redteam-v1/FOLLOWUP.md)

Historical bridge/audit surfaces remain preserved:

- [`project/reviews/n29/2026-09-09-bridge-standalone-v1/GRAPH_TO_MODEL_BRIDGE.md`](project/reviews/n29/2026-09-09-bridge-standalone-v1/GRAPH_TO_MODEL_BRIDGE.md)
- [`project/reviews/n29/2026-09-09-bridge-standalone-v1/THRESHOLD_CAPACITY_LEMMA.md`](project/reviews/n29/2026-09-09-bridge-standalone-v1/THRESHOLD_CAPACITY_LEMMA.md)
- [`project/reviews/n29/2026-09-09-bridge-standalone-v1/BRIDGE_REDTEAM.md`](project/reviews/n29/2026-09-09-bridge-standalone-v1/BRIDGE_REDTEAM.md)
- [`project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md`](project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md)

The highest-value mathematical review is the **graph-to-demand bridge**, not another rerun of the arithmetic.

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

The clean-runner result is recorded in [`MINIMAL_KERNEL_REPORT.json`](project/reviews/n29/2026-09-08-redteam-restart-v1/MINIMAL_KERNEL_REPORT.json):

| Edge count | `t` | Demand profiles retained | Residual rows | Exact late rejections | Final survivors |
|---:|---:|---:|---:|---:|---:|
| 211 | 3 | 72 | 126 | 126 | 0 |
| 210 | 2 | 367 | 1,467 | 1,467 | 0 |

Every late exclusion is rechecked by exact integer arithmetic. Floating-point LP output is used only to propose a Farkas ray; solver status by itself is never a proof event.

The minimal route does **not** use the old projected screen, joint propagator, shared LP, typed LP, old endpoint LP or the older pair-capacity support formula. Those remain in the repository as redundant evidence and research history.

For the Fan-free `Delta=16` upper range, reviewer-v3 further reduces the necessary computation:

```text
m=212: exact trusted-kernel extension;
m=213,214: exact threshold/source-count/Hall arithmetic;
m=215: hand threshold-capacity contradiction;
m>=216: hand pointwise charging cap.
```

Thus the old generic `m=216..232` scan is no longer logically required.

## n=30 complete candidate

Current proof and audit:

- [`project/reviews/n30/2026-09-09-fan-free-v2/PROOF.md`](project/reviews/n30/2026-09-09-fan-free-v2/PROOF.md)
- [`project/reviews/n30/2026-09-09-candidate-v1/ASSEMBLY_AUDIT.md`](project/reviews/n30/2026-09-09-candidate-v1/ASSEMBLY_AUDIT.md)
- [`project/reviews/n30/2026-09-09-fan-free-v2/ANALYTIC_HARDENING_2026-09-11.md`](project/reviews/n30/2026-09-09-fan-free-v2/ANALYTIC_HARDENING_2026-09-11.md)

Its candidate statement is

```text
e(G) <= 225,
with equality exactly K(15,15).
```

The current edition does not use Fan's density theorem logically. For `Delta=17`, the difficult scopes close by threshold/source-count inequalities and exact Hall duals; the new analytic hardening removes every upper-range `Delta=17` scope with `m>=228` from the computational chain. For `Delta=16`, the bridge is genuinely parameterised to `(a,b)=(13,16)` and the remaining final rows are rejected by exact integer Farkas certificates; `m>=234` is now excluded analytically. The final assembly replay is green. This is still same-assistant evidence, not external validation.

## General 7/12 candidate

The current strongest reviewer-packaged maximum-degree candidate is

```text
n >= 6 and Delta(G) >= (7/12)n  ==>  e(G) < floor(n^2/4).
```

Reviewer material:

- [`releases/general-7-12-reviewer-v1/README.md`](releases/general-7-12-reviewer-v1/README.md)
- [`project/research/general_n/2026-09-09-profile-integral-7-12-v1/PROOF.md`](project/research/general_n/2026-09-09-profile-integral-7-12-v1/PROOF.md)
- [`project/research/general_n/2026-09-09-profile-integral-7-12-v1/AUDIT.md`](project/research/general_n/2026-09-09-profile-integral-7-12-v1/AUDIT.md)

The scalar estimate gives

```text
t < 5a^2/128 + a/8.
```

Two separately written standard-library checkers agree on the exact scalar arithmetic and the finite assembly exceptions. The large `n` regressions are consistency checks, not proof by extrapolation. The main mathematical trust boundary is the shared graph-to-demand/profile-integral bridge.

The associated ceiling analysis places the asymptotic limit of the current scalar-uniform profile-integral architecture near `0.582066`, close to `7/12 = 0.583333...`; further progress is therefore expected to require additional joint profile information.

## 10 September RX-Hall / 3-D potential frontier

The active continuation is documented under [`project/research/general_n/2026-09-09-rx-hall-v1/`](project/research/general_n/2026-09-09-rx-hall-v1/README.md).

Three current finite compression milestones are particularly relevant:

1. **n=29, t=3.** All 94 regenerated hard profiles admit one exact rational analytic min-hinge potential with nine breakpoints. See [`MIN_HINGE_ANALYTIC_REDUCTION.md`](project/research/general_n/2026-09-09-rx-hall-v1/MIN_HINGE_ANALYTIC_REDUCTION.md).
2. **n=30, t=1.** A naive BC/diagonal parameter rule failed one of seven hard profiles. Restoring the first Hall coordinate with the single threshold `1[s>=2]` yields an exact 13-generator 3-D potential with two rational scalar templates covering all seven profiles and minimum exact strict gap `1/2`. See [`N30_T1_TWO_TEMPLATE_POTENTIAL.md`](project/research/general_n/2026-09-09-rx-hall-v1/N30_T1_TWO_TEMPLATE_POTENTIAL.md).
3. **n=29, t=2.** A fixed 11-term primitive 3-D potential plus exactly three rational scalar templates covers all 902 regenerated profiles. An exact rational Farkas incompatibility triangle proves that, for this fixed potential, two templates cannot suffice. See [`N29_T2_3D_THREE_TEMPLATE_EXACT.md`](project/research/general_n/2026-09-09-rx-hall-v1/N29_T2_3D_THREE_TEMPLATE_EXACT.md).

These are exact finite RX-Hall results conditional on the graph-to-profile bridge and the 3-D monotone transport/potential lemma. They are **not** unrestricted Murty–Simon theorems and are not dependencies of the current fixed-order proofs.

The current high-value research target is to explain the three `t=2` scalar regimes by simple profile statistics and determine whether the resulting inequalities extend symbolically in `(n,t)`. That is the path being tested toward a genuinely reusable infinite-family theorem below the `7/12` frontier.

## Important audit history: a real n=29 bug was found

During the hostile n=29 bridge audit, an error was found in the first version of the *additional* cumulative-threshold verifier, `independent_threshold_model.py`.

The grouped selected-incidence equation multiplied label-side capacity by the label-group multiplicity twice. Accordingly:

- the **v1 cumulative-threshold certificates are not valid proof evidence**;
- the flawed v1 source is retained for audit history and must not be cited as a verifier;
- the error did not affect the original n=29 direct route or the separate fully fresh implementation;
- [`independent_threshold_model_v2.py`](project/reviews/n29/2026-09-08-redteam-restart-v1/independent_threshold_model_v2.py) fixes the normalization;
- corrected v2 was replayed cleanly and again produced zero survivors;
- the later minimal trusted-kernel replay uses the corrected v2 model and produced zero survivors;
- the n=30 `Delta=16` grouped model was written fresh with the corrected normalization.

This history is intentionally public. It should not be silently edited out of the record.

A separate 11 September proof-text audit found an intermediate sign/order typo in the expanded threshold-capacity lemma's explanatory algebra. The corrected sign is exactly the direction required to prove the same final threshold inequality, so no computation or candidate status changed. The correction is recorded in the historical lemma itself and the reviewer-v3 bridge writes the proof self-contained from scratch.

## What to attack first

A useful hostile review would try to break these points in roughly this order:

1. **Complement/quasi-edge construction.** Does every missing `B`-pair really force the selected cross-edge structure claimed?
2. **Injection and uniqueness.** Are selected edges, supplements and unordered `B`-pairs counted without collisions?
3. **Residual activity.** For `t>0`, is the proof that every `B` row has positive residual degree valid in all edge cases?
4. **Demand implication.** Does `s_i=max(0,d_i-R_i)` genuinely require `s_i` distinct selected sources with enough residual degree?
5. **Charging inequality.** Check the per-source charge budget and the passage to the summed demand inequality.
6. **Threshold-capacity lemma.** Check the high-demand/high-residual source counting and unordered-pair capacity.
7. **Parameterized isolated-C lemma.** Check the auxiliary-location argument and disjoint residual-edge families.
8. **Exact source-capacity dual.** Verify that it is only a necessary Hall relaxation and that the saved integer dual inequality proves each rejection.
9. **Residual-row scanner.** Check that every pruning operation enlarges or preserves the graph-realizable set before rejection.
10. **Corrected grouped LP normalization.** Track every grouped variable dimensionally: per label, per source, or per possible pair.
11. **3-D transport/potential lemma.** Check that every asserted coordinatewise incidence inequality is justified and that every used potential is coordinatewise nondecreasing on the required domain.
12. **Exact Farkas checkers.** Confirm multiplier signs, equality treatment, coefficientwise conditions and strictly negative combined RHS where required.

A single valid counterexample to any universal lemma is enough to invalidate the dependent route and should be reported immediately.

## Reproduction philosophy

The repository attempts to distinguish clearly between:

- mathematical lemmas;
- finite necessary-condition systems;
- exploratory numerical solver output;
- exact machine-checkable certificates;
- same-assistant reimplementation;
- genuinely independent external review.

Only the first five can currently be supplied internally. External mathematical and computational review remains explicitly open.

## How to report a problem

Please open a GitHub Issue and include, where possible:

- the exact file and lemma/constraint;
- the smallest configuration or parameter values that expose the problem;
- whether the issue is mathematical, implementation, reproducibility, attribution/literature, or exposition;
- whether it changes a headline candidate result or only a redundant verification route.

Corrections should preserve the original evidence and failure history rather than overwrite it silently.

## Licence

The repository is released under the MIT licence in [`LICENSE`](LICENSE).
