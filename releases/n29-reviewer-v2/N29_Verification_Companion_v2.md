---
title: "Murty-Simon at n=29 - verification companion"
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

**Claim under review.** `e(G) <= 210, equality exactly K(14,15)`.

**Fan-free reduction.** `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md`.

**Hostile assembly audit.** `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_AUDIT.md`.

---


\newpage

# Included source: `project/reviews/n29/2026-09-09-fan-free-v2/HISTORY.md`

# n=29 proof history - Fan-free edition 2

Frozen edition-1 source: `project/reviews/n29/2026-09-08-candidate-v1/PROOF.md`

SHA-256 at build time: `b5e8f78a9175d3a00f3911e17a24f388d735555975eca30690b9cacfda494b27`

Edition 2 removes Fan's theorem as a logical upper-bound dependency, cites Fan historically, makes the unordered-pair selection convention explicit, and points the assembly to `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md`. The frozen edition-1 proof and all old evidence remain unchanged.


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

# Included source: `project/reviews/n29/2026-09-09-bridge-standalone-v1/BRIDGE_REDTEAM.md`

# Hostile audit of the standalone n=29 Delta=16 graph-to-model bridge

9 September 2026. Audit performed by ChatGPT/Geeps. Same-assistant red-team only; independent expert review remains open.

## Verdict

No blocking counterexample has been found in the bridge after rederiving the implications from the graph definitions.

One real exposition defect was found immediately in the first standalone draft: the threshold-capacity lemma was stated with an over-compressed justification. It is now expanded separately in `THRESHOLD_CAPACITY_LEMMA.md`. The defect was in exposition/traceability, not a discovered reversal of the inequality.

The current highest-risk hand obligations remain the quasi-edge injection, residual-activity lemma, and the `delta(C)=0` exclusion. These should receive external review before any theorem promotion.

## Audit method

For every displayed implication in `GRAPH_TO_MODEL_BRIDGE.md`, the audit asked:

1. Is the conclusion necessary for every actual graph, or only typical?
2. Is an injection being assumed where only a many-to-one map is known?
3. Can two forced residual edges collide?
4. Can a cross-edge counted as residual actually be selected in the opposite orientation?
5. Does a selected-edge claim rely on the exception being in `B`?
6. Is an upper bound substituted where a lower bound is required, or vice versa?
7. Does grouping or sorting silently assume graph symmetry?

## RT-BRIDGE-001 — complement/quasi-edge construction

**Attack.** After adding a missing `B`-edge `uw` to `H`, could the new adjacent total-dominating pair avoid both `u,w`, or equal `{u,w}`, or use an auxiliary outside `A`?

**Resolution.** No other adjacency changes, so a genuinely new adjacent pair must use `u` or `w`. The pair `{u,w}` still misses `v`. If the pair is `{u,i}`, then `u` misses `v`, so domination of `v` forces `iv in H`, hence `i in A`. Before insertion `{u,i}` covered every vertex except `w`, otherwise it would already have been total-dominating in `H`.

**Verdict:** survives.

## RT-BRIDGE-002 — selected-edge injection

**Attack.** Could two missing unordered `B`-pairs select the same cross-edge `ui`?

**Resolution.** The cross-edge determines its `B` source `u`; the unique vertex omitted by `N_H(u) union N_H(i)` determines the supplement `w`. Thus the missing pair `{u,w}` is recovered from the selected edge.

At a fixed source, selected labels are distinct because the selected objects are edges. Supplements are distinct because the same source-supplement pair is one missing unordered `B`-pair, for which only one selected orientation is chosen.

**Verdict:** survives.

## RT-BRIDGE-003 — exact ledger

Starting from

```text
q_total + e(H[B]) = C(b,2),
```

and

```text
e(H)=a+e(C)+r+q_total+e(H[B]),
```

with `e(C)=C(a,2)-e(F)` and `n=a+b+1`, direct simplification gives

```text
m=e(G)=b(n-b)+e(F)-r.
```

Therefore

```text
t=m-b(n-b)=e(F)-r,
e(F)=r+t.
```

No approximate or asymptotic identity is used.

**Verdict:** survives.

## RT-BRIDGE-004 — demand implication

Minimum `H`-degree gives

```text
x_i >= d_i-R_i,
```

hence `x_i>=s_i=max(0,d_i-R_i)`.

Also

```text
S=sum s_i >= sum(d_i-R_i)
             =2(r+t)-r
             =r+2t.
```

The inequality is in the safe direction: replacing `max(0,d_i-R_i)` by `d_i-R_i` only lowers the sum.

**Verdict:** survives.

## RT-BRIDGE-005 — source-demand injection `s_i<=rho_u`

Fix selected `ui->w` and an `F`-neighbour `j` of `i`. Then `uj in H` because `{u,i}` must dominate `j`.

If `uj` is residual, charge `j` to one of the `rho_u` residual source slots.

If `uj` is selected, write `uj->z`. Distinct selected labels at source `u` have distinct supplements. Since `ui->w` must dominate `z != w` and `uz` is missing in `H[B]`, `iz in H`. Moreover `iz` cannot itself be selected: both `i` and `z` miss `j` (`ij` is an `F`-edge and `z` is the exception of `uj->z`), whereas a selected cross-edge has its unique exception in `B`, not in `A`. Thus `iz` is residual.

This injects every `F`-neighbour not charged to a residual source edge into a distinct residual edge at label `i`, yielding

```text
d_i<=rho_u+R_i,
s_i<=rho_u.
```

**Verdict:** survives; this is one of the most important bridge steps.

## RT-BRIDGE-006 — pair residual inequality `d_i<=rho_u+rho_w`

Again fix `ui->w` and `F`-neighbour `j`.

If `uj` is residual, charge to `rho_u`. Otherwise `uj->z` with `z!=w`. Since that quasi-edge must dominate `w` and `uw` is missing, `jw in H`.

The edge `jw` cannot be selected from source `w`: both `w` and `j` miss `i` (`wi` is missing because `w` is the exception of `ui->w`, and `ji` is an `F`-edge), which would leave an `A`-vertex undominated. Therefore `jw` is residual.

Distinct `j` give distinct residual `w-j` edges, proving

```text
d_i<=rho_u+rho_w.
```

**Verdict:** survives.

## RT-BRIDGE-007 — supplement forcing

For every other selected `uj->z` at source `u`, `z!=w`. The pair `{u,j}` must dominate `w`; since `uw` is missing, `jw in H`. The `q_u-1` other selected labels are distinct, so `w` has at least `q_u-1` cross-neighbours among those labels. They are partitioned into residual and selected edges at source `w`, hence

```text
rho_w+q_w>=q_u-1.
```

**Verdict:** survives.

## RT-BRIDGE-008 — exact `q+p` missing degree and endpoint load

Every missing unordered `B`-pair incident with `u` is oriented either outward from `u` or inward to `u`, exactly once. Thus `q_u+p_u` is exactly the missing degree of `u` in `H[B]`.

For selected `ui->w`, the following `B`-vertices are distinct neighbours of `i`:

- `u`;
- supplements of the other `q_u-1` outward arcs at `u`;
- sources of the `p_u` incoming arcs into `u`.

An incoming source cannot equal an outgoing supplement, because that would assign both orientations to the same missing unordered pair. For an incoming source `z`, the pair `uz` is missing and `z!=w`; since `ui->w` must dominate `z`, `iz in H`. The same covering argument handles outgoing supplements.

Therefore

```text
R_i+x_i>=q_u+p_u.
```

**Verdict:** survives.

## RT-BRIDGE-009 — residual activity

Assume `rho_u=0`, put `U=N_A(u)`, `T=A\U`.

Because every `u-i` with `i in U` is selected, an `F`-edge from `U` to `T` would contradict the selected quasi-edge's need to dominate its `T` endpoint. Hence `F(U,T)` is empty.

For each `F`-edge `ij` in `U`, the two selected edges from `u` to `i,j` have distinct supplements. Cross-domination forces two residual edges `i-w_j` and `j-w_i`. They are residual because each would otherwise fail to dominate the opposite `A` endpoint. The mapping from the ordered endpoints of `F[U]` to these residual edges is injective.

For an `F`-edge `ij` in `T`, adding `ij` to `H` creates a quasi-edge. Its auxiliary cannot be `v` (the pair would miss `u`), cannot be `u` (no adjacency), and cannot lie in `A`: to dominate `u`, an `A` auxiliary would have to lie in `U`, but being the auxiliary for exception in `T` would require an `F(U,T)` edge. Therefore an auxiliary lies in `B`, producing a residual cross-edge with `A` endpoint in `T`. Different `F[T]` pairs give different cross-edges because the edge plus its unique `A` exception recover the pair.

The `F[U]` and `F[T]` residual families are disjoint by their `A` endpoints. Hence

```text
r>=2e(F[U])+e(F[T])>=e(F)=r+t,
```

contradicting `t>0`.

**Verdict:** survives after explicit collision audit.

## RT-BRIDGE-010 — charging inequality

For each label choose `s_i` actual selected incidences. Each chosen source satisfies `rho_u>=s_i`. A chosen source also has `q_u>=1`, so `rho_u<=a-1`; the denominator `a-rho_u` is never zero.

Source `u` has at most `a-rho_u` selected incidences in total. Charging each chosen incidence by

```text
(rho_u-1)/(a-rho_u)
```

therefore charges source `u` by at most `rho_u-1`. The charge function is increasing in integer `rho` on `[1,a-1]`, so a demand-`s_i` label receives at least

```text
s_i(s_i-1)/(a-s_i).
```

Summation gives the claimed inequality.

**Verdict:** survives.

## RT-BRIDGE-011 — threshold-capacity proof compression

**Finding:** the first standalone draft did not contain enough detail to justify

```text
2W_h<=z_h^2-z_h+h(h+1).
```

This was an exposition/traceability failure and was not accepted silently.

**Repair:** `THRESHOLD_CAPACITY_LEMMA.md` now gives the complete high-load-source/unordered-pair proof. It uses only:

- `s_i<=rho_u`;
- distinct selected labels and supplements;
- one selected orientation per missing unordered `B`-pair.

No old `pair_capacity()` implementation is a dependency.

**Verdict after repair:** no mathematical defect found.

## RT-BRIDGE-012 — `delta(C)=0` exclusion

This remains the least compact bridge step. The hostile audit rechecked the counting logic used to obtain

```text
b<=[C(a,2)-t]-C(a-1,2).
```

For `a=12,b=16,t in {2,3}` the right side is only `9` or `8`, respectively, so any valid version of the injection has large slack.

The proof depends on separating a family of residual cross-edges forced by missing pairs inside `A\{x}` from an additional family covering all `B` endpoints, using residual activity. No collision was found in the rederivation, but this is specifically marked for external review because it compresses several quasi-edge uniqueness arguments.

**Verdict:** no defect found; elevated review priority.

## Overall conclusion

The bridge has now been reduced to a small set of hand obligations with explicit injection/collision arguments. The finite trusted kernel begins only after these obligations.

No theorem status is promoted. A single counterexample to any universal bridge lemma overrides every green workflow downstream.


\newpage

# Included source: `project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md`

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
