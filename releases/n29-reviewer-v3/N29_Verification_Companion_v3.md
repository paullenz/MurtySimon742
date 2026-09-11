---
title: "N=29 Murty-Simon candidate: verification companion"
subtitle: "Reviewer-v3 evidence, replay map, and audit boundaries"
author: "Paul Lenz"
date: "11 September 2026"
geometry: margin=27mm
fontsize: 11pt
header-includes:
  - \usepackage{amsmath,amssymb,booktabs,microtype}
  - \setlength{\emergencystretch}{2em}
---

11 September 2026. Research directed by Paul Lenz; mathematical development, implementation and internal checking by ChatGPT/Geeps.

**Status: candidate mathematics. Independent mathematical review, independent computational reproduction and novelty assessment remain OPEN.**

## 1. Purpose

This companion maps the evidence layer for the current reviewer-v3 candidate proof that every simple diameter-two edge-critical graph on 29 vertices satisfies

```text
e(G) <= 210,
with equality exactly K(14,15).
```

The current proof is deliberately narrower than the historical route. Reviewers do not need to validate every exploratory program preserved in the repository.

## 2. Current proof architecture

| Scope | Current method | Proof-critical computation? |
|---|---|---|
| Delta <= 14 | degree sum | no |
| Delta = 15 | witness-deficit hand proof and equality | no |
| Delta = 16, m = 210,211 | minimal trusted kernel + exact Farkas | yes |
| Delta = 16, m = 212 | trusted-kernel extension + exact Farkas | yes |
| Delta = 16, m = 213,214 | exact threshold/source-count/Hall arithmetic | small finite check |
| Delta = 16, m = 215 | hand threshold-capacity contradiction | no |
| Delta = 16, m >= 216 | pointwise 5/2 charging cap | no |
| Delta = 17 | pointwise charging hand bound | no |
| Delta = 18,...,27 | residual h-index hand bound | no |
| Delta = 28 | universal-vertex/star observation | no |

The old generic scan over `m=216..232` is now corroborative evidence only, not a logical dependency.

## 3. Main graph-to-model trust boundary

The self-contained bridge is

`project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md`.

Its proof-critical universal statements are:

1. exactly one selected cross quasi-edge is designated for each missing **unordered** B-pair;
2. the forced cross-edges used by the injections cannot secretly be selected when their endpoints jointly miss an A-vertex;
3. residual activity `rho_u >= 1` holds for every B-source when `t>0`;
4. selected-source demand satisfies `s_i <= rho_u`;
5. the charging inequality is necessary;
6. the threshold-capacity inequality is necessary;
7. the isolated-C exclusion is valid;
8. every actual graph satisfying the bridge maps into the corrected late linear relaxation.

A counterexample to any universal bridge lemma overrides all downstream computations that depend on it.

## 4. Minimal trusted kernel at 210 and 211

The preferred dense computation is recorded in

`project/reviews/n29/2026-09-08-redteam-restart-v1/MINIMAL_KERNEL_REPORT.json`.

| Edge count | t | Retained demands | Residual rows | Exact late rejections | Final survivors |
|---:|---:|---:|---:|---:|---:|
| 211 | 3 | 72 | 126 | 126 | 0 |
| 210 | 2 | 367 | 1,467 | 1,467 | 0 |

The proof-critical implementation is intentionally small:

- `minimal_prepare.py` - exact demand preparation and early exact cuts;
- `minimal_rows.cpp` - complete sorted residual-row enumeration with necessary Hall/refinement cuts;
- `run_minimal_kernel.py` - terminal certificate runner;
- `independent_threshold_model_v2.py` - corrected cumulative-threshold/source-q-flow model;
- the exact certificate machinery in `independent_threshold_model.py`.

The route does **not** depend on the old projected screen, joint propagator, shared LP, typed LP, endpoint LP, or older pair-capacity support formula.

## 5. Historical normalization bug

The first additional cumulative-threshold builder contained a real normalization error: label-group multiplicity was counted twice on the label side of the selected-incidence equations.

Accordingly:

- v1 cumulative-threshold certificates are invalid as proof evidence;
- the flawed v1 source remains preserved for audit history;
- `independent_threshold_model_v2.py` reconstructs the graph-derived builder with the corrected per-label normalization;
- the minimal trusted kernel uses v2;
- every terminal exclusion is rechecked by exact integer arithmetic.

The corrected selected-incidence normalization is schematically

```text
sum_k n_k Z = E[x] = sum_h T_h,
```

with no extra multiplication by the label-group size.

## 6. Exact Farkas semantics

Floating-point LP output is used only to **propose** a ray. Solver status alone is never an exclusion.

For nonnegative variables, the checker accepts only an exact integer combination in which:

- multipliers on `<=` inequalities are nonnegative;
- equality multipliers may be signed;
- the combined coefficient of every variable is nonnegative;
- the combined right-hand side is strictly negative.

This produces an inequality with nonnegative left side and negative right side, an exact contradiction. The final check uses integer arithmetic.

## 7. Upper-range finite checks still used by reviewer-v3

For `Delta=16`, `t=m-208`.

At `m=212` (`t=4`):

```text
2032 charging-feasible profiles
1706 threshold rejects
 258 source-count rejects
  65 exact early Hall-dual rejects
   3 open demand profiles
19630 residual numerical states
   2 residual-row survivors
   2 exact late Farkas rejections
   0 final survivors
```

At `m=213` (`t=5`), all 586 profiles are excluded by 576 threshold cuts, 7 source-count cuts and 3 exact Hall duals.

At `m=214` (`t=6`), all 79 charging-feasible profiles are threshold-rejected.

No finite verifier is logically required at `m=215` or above.

## 8. Blind hostile review and independent reruns

A separate ChatGPT instance without the project background performed a hostile review supplied by the user. It reported no fatal flaw after independently attacking the graph-to-model bridge, residual activity, threshold capacity, isolated-C, corrected LP normalization, exact Farkas semantics, the witness equality argument, the Delta=17 bound, the residual h-index calculation and the cited dominating-edge theorem.

The preserved follow-up is

`project/reviews/n29/2026-09-11-blind-external-ai-redteam-v1/FOLLOWUP.md`.

### Charging-domain census

The blind reviewer independently obtained the complete nondecreasing demand counts

```text
t=2: 9251
t=3: 4867
t=4: 2032
t=5:  586
t=6:   79
t=7:    1
t=8:    0
```

and the project regenerated exactly the same sequence again. The rerunnable check is

`project/reviews/n29/2026-09-11-blind-external-ai-redteam-v1/independent_charging_census.py`.

### Graph-atlas bridge regression

The blind reviewer reported an exhaustive NetworkX graph-atlas check through order 7. The project independently reproduced:

```text
21 unlabeled diameter-two-edge-critical isomorphism types
50 maximum-degree rooted cases
58 admissible selection configurations
0 bridge failures
```

The regression checks the exact ledger, demand implication, selected-edge injections, supplement forcing, source capacities, endpoint load and selected-source demand. All small examples have `t in {-3,-2,-1,0}`, so this does **not** test positive-surplus residual activity, charging or threshold capacity.

The rerunnable script is

`project/reviews/n29/2026-09-11-blind-external-ai-redteam-v1/graph_atlas_bridge_regression.py`.

## 9. Analytic upper-range hardening

For integer `0 <= s <= 11`, reviewer-v3 uses

```text
s(13-2s)/(12-s) <= 5/2,
```

with equality only at `s=4`. Therefore the twelve-label charging sum is at most 30, while the bridge requires at least `16+2t`. Hence `t<=7`, or `m<=215`.

At `m=215`, equality forces all twelve demands to equal four. The charging lower bound and `S>=r+2t` force `r=34`; residual activity gives `z_4<=6`; threshold capacity would require

```text
96 <= z_4^2-z_4+20 <= 50,
```

a contradiction.

Thus the historical `m=216..232` scan and the former `m=215` finite check are no longer proof-critical.

The cross-order propagation is preserved in

`project/research/fan-free-fixed-orders/2026-09-11-pointwise-analytic-caps-v1/POINTWISE_CAPS.md`.

## 10. Remaining correlated-error risk

The largest remaining correlated-error risk is the **actual-graph-to-averaged-variable embedding of the corrected late LP**. The current model has survived hostile dimensional and normalization review, but an independent mathematician/programmer should reconstruct this mapping from scratch.

The next most valuable independent checks are residual activity, threshold capacity, isolated-C, and an independently authored exact verifier.

## 11. Recommended reviewer order

A hostile independent audit should proceed in this order:

1. reconstruct the complement/quasi-edge construction;
2. attack selected-edge and forced-residual injections for collisions;
3. reconstruct residual activity;
4. reconstruct `s_i<=rho_u` and charging;
5. reconstruct threshold capacity;
6. reconstruct isolated-C;
7. map an actual graph into every grouped variable of the corrected late model;
8. independently implement the late linear relaxation;
9. verify a sample and then all exact Farkas certificates;
10. regenerate the finite frontiers from independently written code.

## 12. Canonical files

Current proof sources:

- `project/reviews/n29/2026-09-11-reviewer-v3/PROOF.md`
- `project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md`

Evidence and audits:

- `project/reviews/n29/2026-09-08-redteam-restart-v1/MINIMAL_KERNEL_REPORT.json`
- `project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md`
- `project/reviews/n29/2026-09-11-blind-external-ai-redteam-v1/FOLLOWUP.md`
- `project/reviews/cross-cutting/2026-09-11-n29-cross-order-reaudit-v1/REPORT.md`
- `project/research/fan-free-fixed-orders/2026-09-11-pointwise-analytic-caps-v1/POINTWISE_CAPS.md`

Historical reviewer-v2 PDFs remain preserved for provenance but are superseded by reviewer-v3.