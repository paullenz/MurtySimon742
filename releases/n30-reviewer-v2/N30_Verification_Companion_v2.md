---
title: "Murty-Simon at n=30 - verification companion"
subtitle: "Fan-free reviewer edition 2; historical v1 preserved"
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
This companion records the direct Fan-free upper-range replacement, the hostile assembly audit prompted by external critique, exact computational provenance, and preserved proof history. Fan's 1987 result remains cited as historical context but is not a logical dependency of the current project proof. Same-assistant checking is not external verification.
\end{abstract}

**Claim under review.** `e(G) <= 225, equality exactly K(15,15)`.

**Fan-free reduction.** `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md`.

**Hostile assembly audit.** `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_AUDIT.md`.

---


\newpage

# Included source: `project/reviews/n30/2026-09-09-fan-free-v2/HISTORY.md`

# n=30 proof history - Fan-free edition 2

Frozen edition-1 source: `project/reviews/n30/2026-09-09-candidate-v1/PROOF.md`

SHA-256 at build time: `6a03ea7ce46d8f7e26921fcb03e2bcf58005d628b9763e481b647d10768be7da`

Edition 2 removes Fan's theorem as a logical upper-bound dependency, cites Fan historically, makes the unordered-pair selection convention explicit, and incorporates the complete Fan-free upper-range evidence in `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md`. The frozen edition-1 proof and all old evidence remain unchanged.


\newpage

# Included source: `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md`

# Fan-free upper-range reduction for the current fixed-order candidate frontier

9 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: candidate fixed-order proof component with exact finite arithmetic. Independent mathematical and computational review remains OPEN.**

## 1. Purpose and historical relation to Fan

The original fixed-order candidate manuscripts at `n=25,27,28,29,30` used G. Fan's 1987 theorem

> G. Fan, *On diameter 2-critical graphs*, Discrete Mathematics 67 (1987), 235-240, DOI 10.1016/0012-365X(87)90174-9,

as a convenient published upper reduction. Fan's result is historically important and stronger than the order-specific calculations below, so it remains cited.

This note removes **Fan's theorem as a logical dependency** of every current project fixed-order candidate proof at `n=25,27,28,29,30`. It does **not** claim to reproduce or supersede Fan's all-order theorem. Instead, each order is closed directly above the conjectured extremal value using the project's already stated witness/quasi-edge/residual lemmas together with exact finite arithmetic.

The old Fan-based manuscripts, reviewer packages, workflows, certificates and hashes remain frozen and preserved as historical versions. Reviewer-facing v2 editions cite Fan for history/attribution while using this note as the logical upper-range reduction.

## 2. Common ingredients

No new graph-theoretic hypothesis is introduced merely to remove Fan. The replacement uses consequences already stated and audited within the project:

1. degree-sum bounds;
2. direct/two-step witness deficit bounds where available;
3. the complement/quasi-edge construction;
4. the convention choosing **exactly one selected cross-edge for each missing unordered pair in B**;
5. the residual ledger

   ```text
   e(C)+r=L,
   e(F)=r+t,
   sum d_i = 2(r+t),
   sum rho_b = r;
   ```

6. residual activity `rho_b >= 1` when `t>0`;
7. selected-pair/source/supplement capacity inequalities;
8. charging and threshold-capacity inequalities;
9. the residual h-index bound;
10. exact Hall/source-capacity duals and, only where required, exact integer Farkas certificates for the stated relaxations.

The finite enumerations deliberately retain nongraphical numerical states. Therefore eliminating the relaxation is safe: every actual graph satisfying the written bridge is represented, while many impossible numerical states are intentionally retained.

### 2.1 Selection semantics made explicit

Selection is indexed by missing **unordered** B-pairs: one representative quasi-edge is designated for each such pair. Opposite orientations of the same B-pair can never both be selected. Hence the map from selected edges to unordered source/supplement pairs is injective by construction.

Likewise, whenever a residual-injection argument forces an A-B edge whose two endpoints both miss an A-vertex, that edge cannot be selected for a B-B missing pair: the unique exception of a selected edge belongs to B, so a selected edge must dominate every A-vertex. These are consequences of the construction, not additional assumptions.

## 3. n=25 without Fan

Let `m=e(G)`.

If `Delta<=12`, degree sum gives `m<=150`. If `Delta>=17`, the independent complement maximum-degree theorem already used in the frozen manuscript gives `m<=155`.

For `Delta=13`, the witness-deficit inequality

```text
m <= C(h,2) + h(25-h) + o(o-1),
2h+o <= 325-2m
```

is monotone stronger as `m` increases. The complete table at `m=157` is already strictly below 157, hence excludes every `m>=157` at `Delta=13`.

The frozen n=25 residual proof excludes `m=157` for `Delta=14,15,16`. For every larger degree-sum-possible count, the exact Fan-free outer verifier gives:

| Delta | edge counts scanned | outer states | survivors |
|---:|---:|---:|---:|
| 14 | 158..175 | 128,666 | 0 |
| 15 | 158..187 | 88 | 0 |
| 16 | 158..200 | 0 | 0 |

Therefore, without Fan,

```text
e(G) <= 156,
```

and the frozen equality chain forces `K(12,13)`.

## 4. n=27 without Fan

If `Delta<=13`, degree sum gives `m<=175`. If `Delta>=18`, the independent complement maximum-degree theorem gives `m<=181`.

For `Delta=14`, the witness bound

```text
m <= C(h,2) + h(27-h) + o(o-1),
2h+o <= 378-2m
```

is again monotone stronger with increasing `m`; the complete `m=183` table therefore excludes every `m>=183`.

The frozen n=27 proof excludes `m=183` at `Delta=15,16,17`. Above 183:

- `Delta=16`, all `m=184..216`: 8,880 outer states, zero survivors;
- `Delta=17`, all `m=184..229`: empty numerical domain;
- `Delta=15`, all `m>=186`: zero outer survivors.

Only `Delta=15,m=184,185` require the inherited residual-column stage:

```text
m=184: 651 outer survivors -> 49,073 canonical columns
       -> 1,175,094 labelled orbit mass -> 0 final survivors;
m=185: 10 outer survivors -> 388 canonical columns
       -> 10,036 labelled orbit mass -> 0 final survivors.
```

Scan and check modes agree on all counts and ordered-column digests; the replay directly verifies the recorded strict subset inequalities without invoking max flow.

Hence, without Fan,

```text
e(G) <= 182,
```

and equality remains exactly `K(13,14)`.

## 5. n=28 without Fan

The conjectured maximum is 196. The frozen direct-197 proof already excludes `m=197` at every maximum degree.

For every `m>=198`:

- `Delta<=14` is impossible by degree sum;
- `Delta=16` is excluded by the same pointwise charging bound used at 197: the right side depends only on the degree band while the required left side `b+2t` increases with `m`;
- `Delta=17,...,26` are excluded by the same residual h-index inequalities used at 197, again with a fixed right side and increasing left side;
- `Delta=27` is the universal-vertex/star case.

Thus only `Delta=15` needed fresh arithmetic.

### 5.1 Delta=15, m=198 and 199

The strengthened preparation uses charging, residual activity, `delta(C)>=1`, threshold capacity and exact source-capacity Hall dual lower bounds. It then exhaustively scans residual rows and applies exact row-level threshold capacity plus the corrected threshold/source-flow relaxation. Floating infeasibility alone is never accepted.

At `m=198` (`t=3`):

```text
charging-domain profiles: 6,859
retained demand profiles:    186
residual states:          649,380
row survivors:                418
row-threshold rejects:         418
final survivors:                0
```

At `m=199` (`t=4`):

```text
charging-domain profiles: 3,263
retained demand profiles:     22
residual states:           61,363
row survivors:                21
row-threshold rejects:         21
final survivors:                0
```

No final LP/Farkas call was needed in either scope because exact row-threshold capacity already closed every retained row.

### 5.2 Delta=15, m=200 through 210

The exact early kernel closes the entire demand domain:

```text
m=200 (t=5): 1,155 profiles = 1,070 threshold + 67 source-count + 18 exact Hall-dual rejects;
m=201 (t=6):   250 profiles, all threshold-rejected;
m=202 (t=7):    15 profiles, all threshold-rejected;
m=203..210:       0 charging-feasible profiles.
```

Therefore no graph has `m>=198`. Together with the frozen direct exclusion of 197,

```text
e(G) <= 196,
```

with the existing equality chain giving exactly `K(14,14)`.

## 6. n=29 without Fan

The target is 210 and the frozen proof excludes `m=211`.

For `m>=212`:

- `Delta<=14` is impossible by degree sum;
- the Section 3 witness argument at `Delta=15` is monotone stronger as `m` increases and therefore excludes every `m>=211`;
- the pointwise charging argument at `Delta=17` only strengthens with increasing `t`;
- the residual h-index argument excludes `Delta=18,...,27` more strongly as `m` rises;
- `Delta=28` is the star case.

Only `Delta=16` required fresh arithmetic.

### 6.1 Delta=16, m=212

Here `a=12,b=16,t=4`. An audited wrapper removes only the frozen preparation/row scripts' historical CLI restriction to `t in {2,3}`; no mathematical formula is changed.

The complete result is:

```text
charging-feasible demand profiles: 2,032
threshold rejects:                 1,706
source-count rejects:                258
exact early Hall-dual rejects:         65
open demand profiles:                   3
residual numerical states:          19,630
row survivors:                           2
exact late Farkas rejections:             2
final survivors:                          0
exact certificate RHS values:          -499, -434
```

Every late certificate is rebuilt in the independently reconstructed corrected threshold model and verified by exact integer arithmetic.

### 6.2 Delta=16, m=213 and above

The early exact-acceptance kernel gives:

```text
m=213 (t=5): 586 profiles = 576 threshold + 7 source-count + 3 exact Hall-dual rejects;
m=214 (t=6):  79 profiles, all threshold-rejected;
m=215 (t=7):   1 profile, threshold-rejected.
```

The generic outer scan has zero survivors at every `m=216..232`, the degree-sum ceiling for `Delta=16`.

Thus no `m>=212` graph exists, and with the frozen exclusion of 211:

```text
e(G) <= 210,
```

with equality exactly `K(14,15)`.

## 7. n=30 without Fan

The target is 225 and the frozen proof excludes `m=226` while characterizing equality at 225.

For `m>=227`, degree sum gives `Delta>=16`; `Delta=29` is the star case. For `Delta=18,...,28`, the frozen charging domain is already empty at `m=225,226`; for fixed degree band, increasing `m` increases `t` and hence the required left side `b+2t`, so those empty domains remain empty for every larger `m`.

It remains only to cover `Delta=16,17` through their degree-sum ceilings.

### 7.1 Delta=16, m=227 through 240

For the near boundary, the strengthened trusted kernel gives:

```text
m=227 (t=3): 32,031 demand profiles -> 977 retained;
              11,903,678 residual states -> 6,245 row survivors;
              all 6,245 exact row-threshold rejected; zero survivors.

m=228 (t=4): 19,260 demand profiles -> 285 retained;
               2,034,522 residual states -> 683 row survivors;
               all 683 exact row-threshold rejected; zero survivors.

m=229 (t=5): 10,037 demand profiles -> 59 retained;
                 245,666 residual states -> 29 row survivors;
                 all 29 exact row-threshold rejected; zero survivors.

m=230 (t=6): 4,299 demand profiles -> 3 retained;
               7,730 residual states -> 0 row survivors.
```

For `m=231..240`, the early exact-acceptance kernel closes the full demand domain:

```text
m=231 (t=7): 1,360 profiles = 1,346 threshold + 12 source-count + 2 exact Hall-dual rejects;
m=232 (t=8):   238 profiles, all threshold-rejected;
m=233 (t=9):     9 profiles, all threshold-rejected;
m=234..240:       0 charging-feasible profiles.
```

Thus the complete degree-sum range `m=227..240` at `Delta=16` is excluded.

### 7.2 Delta=17, m=227 through 255

The complete explicit upper-range scan was run rather than relying only on monotonicity:

```text
m=227 (t=6): 15 charging-feasible profiles, all threshold-rejected;
m=228..255:   0 charging-feasible profiles at every edge count.
```

Workflow run `34398181000` completed successfully and committed the durable checkpoint `checkpoints_N30_D17_UPPER.json`.

Hence every `m>=227` is impossible. Combining this with the frozen exclusion of 226 and equality analysis at 225 gives, without Fan,

```text
e(G) <= 225,
with equality exactly K(15,15).
```

## 8. Computational provenance

### n=25 and n=27

Primary upper-range scan:

```text
run 34393554788
head commit efe189ad911a3968e5b7d63a3de43a05c664bfb2
```

n=27 Delta15 residual-column closure:

```text
run 34393710385
head commit 7cc1971604efdf8fea5ec11bbc3b8826868c55ff
```

### n=28

Generic discovery scan:

```text
run 34394955761
```

Trusted near-boundary closure:

```text
run 34396969425
m=198 artifact SHA256 cf71339f83d49fc1a53bfaee66e73061bebbc8e9cbb7488c0655da7a76c1b4bd
m=199 artifact SHA256 820703855b824b638ea0e36dc8b83d61da05df9515d7b7536b38a5c8f645e057
```

High-surplus early kernel:

```text
run 34397027512
artifact SHA256 aef829a157de26e2c92ca3ea131778e290026988c079142d37c00023e0d17108
```

### n=29

Generic upper discovery scan:

```text
run 34394955761
```

Exact `m=212` trusted-kernel closure:

```text
run 34396452149 — SUCCESS
checkpoint checkpoints_N29_D16_M212.json
```

`m=213..215` early closure:

```text
run 34396555260
artifact SHA256 a2f94dd6a81941ba767c68a2d5dc89a14cda8dab01b4b96c5391e0369a473827
```

### n=30

Delta16 `m=227..230` trusted closure:

```text
run 34397132809
all four mathematical jobs completed; three final Git writes raced and their receipts were recovered from the uploaded artifacts
```

Delta16 `m=231..240` early closure:

```text
run 34396592020
artifact SHA256 b92efe1f4afe87ec1e3fa7d912713b9e84d98a07f4a953fba5efcd9df2020157
```

Delta17 complete upper range:

```text
run 34398181000 — SUCCESS
checkpoint checkpoints_N30_D17_UPPER.json
```

All arithmetic exclusions accepted as proof events are exact integer/rational checks. Floating-point LP is used only to propose dual/Farkas multipliers where applicable.

## 9. Trust boundary and status

Fan's 1987 theorem is now **historical attribution only** for the current fixed-order candidate frontier `n=25,27,28,29,30`; none of those candidate proofs requires Fan's bound logically.

This does not remove other published dependencies explicitly retained by the manuscripts, such as complement/total-domination or dominating-edge results where used. It also does not convert same-assistant computation into external review. The graph-to-residual/quasi-edge lemmas remain the principal mathematical trust boundary.

The old Fan-based manuscripts, reviewer packages, evidence, failed exploratory routes, workflows and hashes remain preserved. New reviewer-facing v2 editions must point back to those versions rather than overwrite them.


\newpage

# Included source: `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_AUDIT.md`

# Hostile assembly audit — Fan-free fixed-order frontier

9 September 2026. **PASS internally; independent external review remains OPEN.**

This audit was written after an external-AI critique challenged two selection/residual semantics and the reliance on Fan's 1987 upper bound. The two semantic objections were resolved by explicit definitions; the project then went further and removed Fan as a logical dependency from its current fixed-order candidate proofs at n=25,27,28,29,30.

The audit checks the replacement as an assembled dependency chain rather than merely trusting green workflows. It verifies complete edge-range coverage of the new upper-band computations, zero final survivors in every required exact checkpoint, exact-certificate acceptance flags, the absence of the old logical Fan phrases from v2 proof surfaces, and SHA-256 integrity of every frozen historical source named by the v2 history files.

Result: **PASS** on all machine-checkable assembly checks. See `FAN_FREE_AUDIT_REPORT.json`.

The result is deliberately not described as external verification. The universal graph-to-residual lemmas and the short hand monotonicity arguments remain the main mathematical trust boundary. Historical v1 proof surfaces and Fan citations are retained rather than overwritten.


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