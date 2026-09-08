# N=29 public-release audit and corrected trusted-kernel status

8 September 2026.

**Status:** public-release preparation note. The n=29 result remains a **candidate theorem**, not an externally reviewed theorem. This file records the late hostile audit, the defect found in an auxiliary verifier, the correction, and the reduced proof-critical computational path.

## 1. Purpose

Before public release, the n=29 argument was attacked from the graph-to-model bridge rather than by merely rerunning the original computation. The goal was to identify the smallest set of mathematical lemmas and exact computational steps that an external reviewer must trust.

The audit deliberately treated implementation agreement as secondary evidence. A repeated calculation is not useful if two programs encode the same invalid mathematical implication.

## 2. Graph-to-model bridge: current audit outcome

No blocking defect was found in the following proof-critical graph implications after fresh hostile rederivation:

- complement/quasi-edge construction from a missing pair in `H[B]`;
- uniqueness of the exception and injection from missing unordered `B`-pairs to selected cross-edges;
- distinction between selected and residual cross-edges;
- exact edge ledger `e(F)=r+t`, `sum d_i=2(r+t)`, `sum R_i=r`;
- minimum-degree implication `x_i >= s_i`, where `s_i=max(0,d_i-R_i)`;
- source/supplement forcing inequalities, including `s_i <= rho_u` for a selected source;
- residual activity for `t>0`: every `B`-source has `rho_u>=1`;
- source and supplement capacity bounds;
- charging inequality and its summed demand consequence;
- threshold-capacity inequality for high-demand labels and high-residual sources;
- source-local degree-load inequality used by the stronger endpoint formulations.

This is still same-assistant mathematical review. It materially increases confidence but does not replace an independent mathematician.

## 3. A real defect was found in the additional threshold verifier

The hostile dimensional audit found a genuine normalization error in the first cumulative-threshold verifier:

- historical source: `independent_threshold_model.py`;
- affected evidence: the first cumulative-threshold v1 certificates;
- nature of error: a grouped label multiplicity was applied twice in the label-side selected-incidence/tail equation.

The grouped selected-incidence variable is normalized per source-label pair. Therefore the correct per-label identity is schematically

```text
sum_k n_k Z_kg = sum_h T_h,
```

whereas v1 encoded

```text
sum_k n_k Z_kg = n_g * sum_h T_h.
```

For any label group of multiplicity `n_g>1`, this can overconstrain the relaxation.

### Consequence

The v1 cumulative-threshold certificates are **invalid as proof evidence** and should not be cited.

The defect is confined to that additional verifier. It does not occur in:

1. the original n=29 direct197-derived route;
2. the separate fully fresh n=29 Delta=16 implementation; or
3. the corrected cumulative-threshold v2 model.

The flawed v1 file is intentionally retained so the failure history remains auditable.

## 4. Corrected v2 threshold verifier

The corrected implementation is:

- `independent_threshold_model_v2.py`.

The replay workflow was changed to use v2 and completed successfully.

Corrected v2 results:

| Edge count | Projected rows | Exact rejections | Final survivors | Exact certificate RHS range |
|---:|---:|---:|---:|---:|
| 211 | 118 | 118 | 0 | -795 to -40 |
| 210 | 1,225 | 1,225 | 0 | -999801 to -1 |

Every exclusion was re-verified after aggregation using exact integer arithmetic. The report is `INDEPENDENT_THRESHOLD_REPORT.json` with schema `n29-independent-threshold-flow-complete-v2`.

Evidence commit:

```text
18937b3ef39b1f73bac1af718c3064b257b6e53d
Preserve corrected v2 n29 threshold-flow certificates
```

## 5. Minimal trusted kernel

After the graph-to-model audit, several older finite stages were found to be unnecessary for a proof-critical n=29 Delta=16 route.

The preferred reduced chain is now:

```text
quasi-edge / selected-residual construction
        -> residual activity
        -> charging inequality
        -> exact threshold-capacity inequality
        -> exact source-capacity dual pruning
        -> simple residual-row Hall/refinement scanner
        -> corrected v2 cumulative-threshold/source-q-flow LP
        -> exact integer Farkas checker
```

The following older machinery is no longer required by this reduced route:

- old pair-capacity support formula;
- projected pair screen;
- joint propagator;
- shared-adjacency LP;
- degree-typed LP;
- old endpoint LP.

Those stages remain preserved as independent/redundant assurance and as research history.

## 6. Minimal-kernel clean replay

The clean GitHub Actions workflow `n29-minimal-kernel.yml` completed successfully.

Its exact result is recorded in `MINIMAL_KERNEL_REPORT.json`:

| Edge count | `t` | Retained demands | Residual rows | Exact Farkas rejections | Final survivors |
|---:|---:|---:|---:|---:|---:|
| 211 | 3 | 72 | 126 | 126 | 0 |
| 210 | 2 | 367 | 1,467 | 1,467 | 0 |

The aggregate checker rebuilt the corrected v2 model for every residual row and re-verified every saved integer certificate.

The report explicitly records:

```text
uses_projected_screen = false
uses_joint_propagator = false
uses_old_shared_typed_endpoint_models = false
uses_old_pair_capacity_support_formula = false
all_late_exclusions_exact_integer_farkas_reverified = true
final_survivors = 0
```

Clean workflow run:

```text
34274211354
```

## 7. Interpretation

The late audit changed the evidence hierarchy in a useful way:

- one auxiliary verification route was shown to contain a genuine bug;
- that route was corrected and still closes the full frontier;
- the proof-critical finite chain was then simplified substantially;
- the simplified chain also closes cleanly with exact certificates.

This does **not** upgrade n=29 from candidate to theorem. The principal remaining risk is the correctness and novelty of the hand graph-theoretic bridge, not whether the existing finite arithmetic can be rerun.

## 8. What an external reviewer should check first

Highest priority:

1. quasi-edge construction and injection;
2. residual-activity lemma;
3. `s_i<=rho_u` source-demand implication;
4. charging inequality;
5. threshold-capacity lemma;
6. exact source-capacity Hall relaxation;
7. dimensional normalization and necessity of every corrected-v2 LP constraint;
8. exact Farkas verification logic.

A counterexample to any one of the universal graph lemmas should be treated as a blocking result even if all workflows remain green.

## 9. Public-review status

Independent mathematical review: **OPEN**.

Independent external computational reproduction: **OPEN**.

Novelty assessment: **OPEN**.

Unrestricted Murty–Simon conjecture: **NOT CLAIMED SOLVED**.
