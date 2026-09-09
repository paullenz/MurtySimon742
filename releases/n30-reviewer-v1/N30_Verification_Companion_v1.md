---
title: "A candidate proof of the Murty-Simon conjecture at order 30 - verification companion"
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

**Claim under review.** `e(G) <= 225, with equality exactly K(15,15)`.

**Status.** complete candidate; independent mathematical review OPEN.

**Sources assembled verbatim below:**

- `project/reviews/n30/2026-09-09-candidate-v1/README.md`
- `project/reviews/n30/2026-09-09-candidate-v1/ASSEMBLY_AUDIT.md`

A failed or superseded route remains part of the repository history and is not silently promoted by inclusion in this companion. Reviewers should report suspected flaws through the repository's public review process.

---



\newpage

# Included source: `project/reviews/n30/2026-09-09-candidate-v1/README.md`

# n=30 Murty–Simon candidate package

9 September 2026.

**Status: COMPLETE CANDIDATE. Independent mathematical review, independent computational reproduction and novelty assessment remain OPEN.**

Candidate statement:

```text
Every 30-vertex simple diameter-two edge-critical graph G satisfies
  e(G) <= 225,
with equality exactly K(15,15).
```

## Start here

- [`PROOF.md`](PROOF.md) — assembled candidate proof.
- [`ASSEMBLY_AUDIT.md`](ASSEMBLY_AUDIT.md) — fresh hostile end-to-end audit.
- [`check_outer.py`](check_outer.py) — standard-library exact checker for Fan arithmetic, degree-sum entry points, and the empty charging domains for `Delta=18,...,28`.

## Proof structure

Fan's strict bound leaves only 226 edges as an upper-bound counterexample.

At 225 edges:

- `Delta=15` is a hand equality case and forces `K(15,15)`;
- `Delta=16` is excluded by the parameterized trusted kernel;
- `Delta=17` is excluded by the early charging/threshold/Hall kernel;
- `Delta=18,...,28` have empty exact charging domains;
- `Delta=29` forces a star.

At 226 edges the same exclusions apply beginning at `Delta=16`.

## Delta=16 evidence

Parameterization / source:

- [`project/research/n30/2026-09-08-minimal-kernel-recon-v1/N30_PARAMETERIZATION_AUDIT.md`](../../../research/n30/2026-09-08-minimal-kernel-recon-v1/N30_PARAMETERIZATION_AUDIT.md)
- [`project/research/n30/2026-09-08-minimal-kernel-recon-v1/ISOLATED_C_PARAMETERIC_LEMMA.md`](../../../research/n30/2026-09-08-minimal-kernel-recon-v1/ISOLATED_C_PARAMETERIC_LEMMA.md)
- [`project/research/n30/2026-09-08-minimal-kernel-recon-v1/n30_prepare.py`](../../../research/n30/2026-09-08-minimal-kernel-recon-v1/n30_prepare.py)
- [`project/research/n30/2026-09-08-minimal-kernel-recon-v1/n30_rows.cpp`](../../../research/n30/2026-09-08-minimal-kernel-recon-v1/n30_rows.cpp)
- [`project/research/n30/2026-09-08-minimal-kernel-recon-v1/n30_row_threshold.py`](../../../research/n30/2026-09-08-minimal-kernel-recon-v1/n30_row_threshold.py)
- [`project/research/n30/2026-09-08-minimal-kernel-recon-v1/n30_threshold_model.py`](../../../research/n30/2026-09-08-minimal-kernel-recon-v1/n30_threshold_model.py)

Clean GitHub Actions:

```text
34286806474  strengthened prepare + complete residual-row scan
34287440190  exact row-level threshold-capacity screen
34287739057  final exact Farkas replay
```

Final exact frontier:

```text
m=226: 9 rows -> 9 exact contradictions -> 0 survivors
m=225: 272 rows -> 272 exact contradictions -> 0 survivors
```

## Delta=17 evidence

- [`project/research/n30/2026-09-09-delta17-v1/README.md`](../../../research/n30/2026-09-09-delta17-v1/README.md)
- [`project/research/n30/2026-09-09-delta17-v1/D17_EXACT_DUAL_CERTIFICATES.json`](../../../research/n30/2026-09-09-delta17-v1/D17_EXACT_DUAL_CERTIFICATES.json)
- [`project/research/n30/2026-09-09-delta17-v1/verify_committed.py`](../../../research/n30/2026-09-09-delta17-v1/verify_committed.py)
- [`project/research/n30/2026-09-09-delta17-v1/CI_PROVENANCE_NOTE.md`](../../../research/n30/2026-09-09-delta17-v1/CI_PROVENANCE_NOTE.md)

Clean replay:

```text
34292054922
```

Exact result:

```text
m=226: 250 charging-feasible profiles, all 250 threshold-rejected.
m=225: 1,155 profiles; 1,137 early rejects + 18 exact Hall-dual rejects.
final survivors: 0.
```

The earlier failed Delta=17 CI runs are intentionally retained in Actions history. They exposed replay-provenance and stale-metadata problems; the final committed certificates were regenerated and then passed the exact standard-library verifier.

## Universal bridge

The graph-to-demand lemmas used here were isolated and hostile-audited in the n=29 standalone package:

- [`project/reviews/n29/2026-09-09-bridge-standalone-v1/GRAPH_TO_MODEL_BRIDGE.md`](../../n29/2026-09-09-bridge-standalone-v1/GRAPH_TO_MODEL_BRIDGE.md)
- [`project/reviews/n29/2026-09-09-bridge-standalone-v1/THRESHOLD_CAPACITY_LEMMA.md`](../../n29/2026-09-09-bridge-standalone-v1/THRESHOLD_CAPACITY_LEMMA.md)
- [`project/reviews/n29/2026-09-09-bridge-standalone-v1/BRIDGE_REDTEAM.md`](../../n29/2026-09-09-bridge-standalone-v1/BRIDGE_REDTEAM.md)

An external reviewer should attack these hand lemmas before spending time rerunning arithmetic.

## Review priorities

1. quasi-edge construction and injection;
2. residual activity;
3. source-demand and charging;
4. threshold-capacity lemma;
5. parameteric isolated-C lemma;
6. n=30 Delta=16 grouped-model normalization;
7. exact certificate semantics;
8. exact hypotheses of the cited published reductions.

Please report any suspected flaw through a GitHub Issue. A smallest counterexample or the first invalid implication is especially useful.

\newpage

# Included source: `project/reviews/n30/2026-09-09-candidate-v1/ASSEMBLY_AUDIT.md`

# n=30 complete-candidate assembly audit

9 September 2026. Hostile same-assistant audit by ChatGPT/Geeps at Paul Lenz's direction.

**Verdict:** no blocking defect found in the assembled n=30 candidate. Independent expert review remains OPEN. This audit is not external validation.

## 1. Object audited

Candidate statement:

```text
Every 30-vertex simple diameter-two edge-critical graph G satisfies
  e(G) <= 225,
with equality exactly K(15,15).
```

The assembly proof is `PROOF.md` in this directory.

The audit was performed against the current parameterized graph-to-demand bridge, the n=30 Delta=16 parameterization audit and clean exact workflows, the n=30 Delta=17 early-kernel package and clean replay, and a fresh standard-library outer arithmetic checker.

## 2. Outer edge-count reduction

The Fan expression used by the project evaluates exactly to

```text
7247/32 = 226.46875
```

at n=30. Because edge count is integral and the bound is strict, an upper-bound counterexample to 225 edges can only have 226 edges.

No assumption is made that deleting an edge from a 226-edge graph leaves an edge-critical 225-edge graph. Equality at 225 is treated independently.

**Verdict:** no defect found.

## 3. Bipartite branch

A bipartite graph of diameter at most two must be complete bipartite: any missing cross-part pair has odd distance at least three. Therefore a bipartite 30-vertex graph in the class has at most 15*15=225 edges, with equality only K(15,15).

K(15,15) is diameter-two edge-critical: deleting a cross edge makes its endpoints distance three.

**Verdict:** no defect found.

## 4. Degree coverage

At m=226:

```text
2m=452 > 30*15,
```

so Delta>=16.

At m=225:

```text
2m=450 = 30*15,
```

so Delta>=15, and Delta=15 forces 15-regularity.

The assembly covers every integer Delta from the entry point through 29:

```text
m=226: 16,17,18..28,29;
m=225: 15,16,17,18..28,29.
```

**Verdict:** no missing degree sector.

## 5. Delta=15 equality branch

This branch exists only at m=225 and is 15-regular.

For the non-bipartite branch, the cited dominating-edge theorem excludes a dominating edge at this density. Every critical edge supplies a direct or two-step witness. In either witness type, absence of a dominating edge gives degree sum at most n-1=29. A 15-regular graph gives degree sum 30 for every pair, contradiction.

The argument does not apply the dominating-edge theorem to the bipartite equality graph; the bipartite branch is handled separately.

**Verdict:** no defect found. External reviewers should still check the precise hypotheses of the cited dominating-edge theorem.

## 6. Universal graph-to-demand bridge

For Delta=16 and 17 the assembled proof uses the same symbolic bridge:

- complement/quasi-edge construction;
- selected-edge injection;
- exact ledger `e(F)=r+t`;
- demand `S>=r+2t`;
- residual activity for `t>0`;
- selected-source implication `s_i<=rho_u`;
- charging;
- threshold capacity.

All four n=30 dense Delta=16/17 scopes have positive t:

```text
Delta=16: t=2,1;
Delta=17: t=5,4.
```

Thus residual activity is used only inside its stated `t>0` range.

**Verdict:** no new n=30 bridge assumption found. The universal bridge remains the principal mathematical trust boundary.

## 7. Delta=17 audit

The Delta=17 route uses only the early kernel; it does not use residual-row enumeration or the cumulative-threshold endpoint LP.

Exact complete domains:

```text
m=226: 250 charging-feasible profiles; all 250 threshold-rejected.
m=225: 1,155 charging-feasible profiles;
       1,070 threshold-rejected;
          67 source-count rejected;
          18 exact Hall-dual rejected.
```

The clean workflow run `34292054922` is green. It regenerated the complete domain, recovered exactly the 18 post-threshold profiles, verified freshly generated exact duals, and independently verified the committed 18 exact integer duals using a standard-library checker.

Earlier failed CI attempts are preserved in `CI_PROVENANCE_NOTE.md`. They exposed replay-contract and stale-certificate-metadata defects; they did not produce a mathematical survivor. The committed certificate file was regenerated from the exact kernel and the subsequent run passed.

**Verdict:** no blocking Delta=17 defect found.

## 8. Parameteric isolated-C lemma

The Delta=16 row bounds require `delta(C)>=1`. The expanded parameteric proof is preserved at

`project/research/n30/2026-09-08-minimal-kernel-recon-v1/ISOLATED_C_PARAMETERIC_LEMMA.md`.

The key necessary consequence is

```text
if C has an isolated vertex, then b <= a-1-t.
```

At `(a,b)=(13,16)` this becomes 16<=10 at t=2 or 16<=11 at t=1, impossible. Hence `delta(C)>=1`, so `d_i<=11`, `e(C)>=7`, and `r<=69/70` in the two scopes.

The expanded proof explicitly checks why a quasi-edge for a missing pair inside `A\{x}` cannot use `v` or an auxiliary in A, and why the resulting residual families are disjoint.

**Verdict:** no defect found after hostile rederivation. This remains a high-priority external-review lemma.

## 9. Delta=16 finite chain

The parameterization audit records every changed constant from n=29 to n=30 and finds no hidden n=29 dimension assumption.

### Preparation / residual rows

Clean run `34286806474`:

```text
m=226: 48,046 charging profiles -> 2,590 demands;
       50,690,620 raw residual states -> 35,530 row survivors.

m=225: 67,050 charging profiles -> 5,379 demands;
       158,314,695 raw residual states -> 150,896 row survivors.
```

The row scanner uses only necessary prefix Hall bounds and monotone supplement-cap refinement.

### Exact row threshold

Clean run `34287440190` applies the exact threshold theorem using each concrete residual row and leaves

```text
m=226: 9 rows;
m=225: 272 rows.
```

### Final exact model

The n=30 cumulative-threshold/source-flow model is a fresh file specialized to `(a,b)=(13,16)` and uses the corrected per-label normalization

```text
sum_k n_k Z = sum_h T_h.
```

Its same-group pair capacity is weakened rather than strengthened, so the relaxation may admit false survivors but cannot exclude a graph on that basis.

Clean final run `34287739057` gives

```text
m=226: 9/9 exact Farkas rejections;
m=225: 272/272 exact Farkas rejections;
final survivors: 0 in both scopes.
```

Floating-point infeasibility is not accepted as proof; every counted exclusion has an integer Farkas certificate directly verified against the reconstructed model.

**Verdict:** no blocking Delta=16 defect found.

## 10. Delta=18 through 28

The standard-library `check_outer.py` completely enumerates sorted integer demand profiles satisfying the charging inequality for each degree and both dense edge counts.

For every Delta=18,...,28 at m=225 and m=226, the charging-feasible domain is empty.

This is stronger than the earlier scalar h-index reconnaissance and removes any need to inspect these degree values separately.

**Verdict:** no survivor and no missing case found.

## 11. Delta=29

A universal vertex forces a star in a diameter-two edge-critical graph: any edge among the other vertices could otherwise be deleted without increasing diameter beyond two. The star has 29 edges.

**Verdict:** excluded.

## 12. Equality assembly

At 225 edges:

- bipartite equality gives K(15,15);
- non-bipartite Delta=15 is impossible;
- Delta=16 and 17 are computationally/exactly excluded;
- Delta>=18 is charging-excluded or star.

No other equality branch remains.

**Verdict:** equality uniqueness assembled correctly.

## 13. Findings from the hostile process

No blocking mathematical defect was found, but the process did find and preserve several nontrivial audit issues:

1. the isolated-C proof needed a more explicit parameteric derivation;
2. requiring freshly proposed LP dual rays to reproduce the same certificate bytes/vectors was an invalid replay invariant;
3. one committed Delta=17 dual record had stale derived `lhs/rhs` metadata despite valid weights; the exact checker caught it and the file was regenerated before the clean successful replay.

These findings increase confidence in the audit process but do not constitute external independence.

## 14. Final audit verdict

Within the current audited bridge framework, all n=30 dense sectors close and equality is uniquely K(15,15).

**Project status recommended:** `COMPLETE CANDIDATE`, not theorem.

Promotion beyond candidate requires at minimum independent expert review of the universal graph lemmas and independent scrutiny/reproduction of the computational relaxations.