---
title: "Murty-Simon at n=28 - verification companion"
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

**Claim under review.** `e(G) <= 196, equality exactly K(14,14)`.

**Fan-free reduction.** `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md`.

**Hostile assembly audit.** `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_AUDIT.md`.

---


\newpage

# Included source: `project/reviews/n28/2026-09-09-fan-free-v2/HISTORY.md`

# n=28 proof history - Fan-free edition 2

Frozen reviewer-v1 source: `releases/n28-reviewer-v1/N28_Reviewer_Manuscript_v1.tex`

SHA-256 at build time: `d222f2c23c0be12c33b7ab100558427b02640ed518d4a799186e342b6fbc9e9b`

Edition 2 retains the direct 197-edge/equality mathematics, removes Fan's bound as the logical global cap, cites Fan historically, and points to `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md` for the direct exclusion of all larger edge counts. Reviewer v1 and all original archives remain unchanged.


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

# Included source: `project/reviews/n28/2026-09-07-redteam-v1/REPORT.md`

# Red-team audit of the direct order-28 candidate

**7 September 2026 — internal adversarial review, not independent expert certification.**  
Research directed by Paul Lenz. Audit, new tests and additional checker written by ChatGPT/Geeps.

## Executive conclusion

**No blocking mathematical, domain-coverage or certificate-arithmetic defect was found in the direct order-28 route examined in this audit.** The original v3–v8 numerical checking sequence was replayed, the equality-stage handoffs were compared byte-for-byte, and a new integer-accumulation kernel verified all 8,983 final certificate leaves across v6, LocalIncidence-v7 and direct197-v8. The order-28 statement remains a **complete candidate argument awaiting independent mathematical review**, not an externally certified theorem.

One reproducible **non-blocking input-validation defect** was found in v8's standalone C++ residual enumerator. An unsupported residual interval can be accepted with a successful empty report. The complete proof driver validates the exact permitted domain and input file before invoking that helper, so this does not affect any admitted proof input or recorded exclusion. An additive guard patch was tested on the entire valid 197-edge residual domain: all counts, survivor bytes and per-demand band bytes remain identical. Four malformed-input controls are rejected by the hardened copy. The frozen original source and archives were not edited.

The previously missing v6, LocalIncidence-v7 and v8 archives were located, matched to the original hashes and relocated unchanged in GitHub. The root README now begins with n=25, followed by n=27 and n=28, then general research, evidence and governance. Preservation is no longer the missing step for these three checkpoints.

## 1. Scope and immutable inputs

The principal target is the **direct** chain proposing that every simple diameter-two edge-critical graph on 28 vertices has at most 196 edges, with equality exactly for K(14,14). Its two numerical density scopes are treated separately:

* Equality: (n,a,b,m,t)=(28,12,15,196,1), using label-tail-v4, column-propagation-v5, shared-adjacency-v6 and **LocalIncidence-v7**.
* Upper-bound counterexample: (28,12,15,197,2), using the freshly generated **direct197-v8** domain.

The v3 n=28/Delta=16 scope is a separate degree-case dependency. The simple low-degree, high-degree and star reductions and Fan's cited upper bound complete the assembly. There is no assumption that deleting an edge preserves criticality, no reuse of the t=1 final survivors as the t=2 domain, and no weak-core reduction in this direct route.

Six original archives were checked: v3, v4, v5, v6, LocalIncidence-v7 and v8. They contain **400 manifested payloads plus six original manifests**. Every payload length and SHA-256 matches; ZIP CRCs, safe paths, duplicate membership and manifest coverage pass. `evidence/ARCHIVE_INTAKE.json` pins each complete ZIP hash and Git blob. `evidence/HANDOFF_AND_SCOPE_REPORT.json` confirms that the original payloads remain unchanged after the replays.

The separate repository **degree-load-v7** route uses a 173/215 final partition and a weak-core density reduction. It is not LocalIncidence-v7's 22/19/347 route. Its readable core-scope audit was inspected for dependency separation; its different complete binary bundle was not available among these six inputs and was **not computationally audited here**. This report neither rejects nor certifies that alternative. Unrelated infinite-profile-family claims, the general coefficient's novelty, and the complete frozen n=25/n=27 proofs are outside this order-28 audit's certification scope.

## 2. Mathematical attack surface

### 2.1 Complement correspondence and exceptional graphs

The published complement correspondence was checked against Haynes–Henning–van der Merwe–Yeo, Theorems 3.1–3.2, including their treatment of stars. Their definition excludes disconnected edge-deletions; allowing infinite diameter adds stars, which our assembly handles explicitly. A bipartite diameter-two graph must be complete bipartite. Its 196-edge extremal case has two parts of size 14. No complement theorem is applied to a graph with an isolated complementary vertex without first removing this exceptional case.

For a missing B-pair, its endpoints miss the chosen root v. Consequently the new edge itself cannot be the total dominating pair, and an existing cross quasi-edge with a unique B-exception exists. Its B-endpoint and exception identify the original missing pair. This justifies selecting one distinct cross edge for each missing unordered B-pair, with distinct labels and supplements at a fixed source. The proof does not assume an arbitrary injection where a quasi-edge could count two different missing B-pairs.

### 2.2 Residual bookkeeping and signs

Selected cross edges and existing H[B]-edges account for exactly choose(b,2) B-pairs. The ledger therefore gives e(F)=r+t and sum d_i=2(r+t), with t=m-b(n-b). Minimum H-degree yields R_i+x_i>=d_i and p_u<=rho_u+b-a-1. These signs and the one-vertex offsets were independently recomputed.

The demand s_i=max(0,d_i-R_i) is a **lower bound** on actual selected degree x_i, not an equality. Zero-demand labels may still carry selected edges. That distinction survives the preliminary caps, v5 matching/network tests and the later actual-x endpoint types; no dense graph is rejected by silently setting x=s.

### 2.3 Residual activity and the degree cap d_i<=10

Positive surplus is necessary for the inherited all-active argument. If a B-vertex has rho=0, all its A-neighbours are selected. No F-edge crosses from that selected set to its complement. Internal selected F-edges yield two distinct residual edges each, while internal missing-set F-edges yield one each through a different A-endpoint class. Their disjointness gives r>=e(F)=r+t, contradicting t>0. Empty selected or missing sets are covered.

A separate low-k injection excludes an isolated C=H[A] vertex. For k=0, the missing pairs in A minus that vertex yield a residual family P. For each B-endpoint used by P an additional residual edge to the isolated C-vertex is forced; each unused B-vertex supplies a residual edge by activity. These b edges lie outside P and are distinguished by B-endpoints. Thus b<=L-choose(a-1,2), where L=choose(a,2)-t. At a=12,b=15 the right side is 10 at t=1 and 9 at t=2: both impossible.

Therefore delta(C)>=1, d_i<=10 and r<=59 or 58 respectively. These numerical bounds are derived necessities, not unexplained solver pruning. The low-degree regular equality case is handled separately and is not forced through a positive-surplus argument.

### 2.4 Demand domains, symmetry and safe relaxations

From the selected-edge charges, rho_u>=s_i at every selected incidence. A demand at least a would require a positive selected degree at a source with rho>=a, which is impossible. Summing the source charge gives

    r-b >= sum_i s_i(s_i-1)/(a-s_i),  S=sum_i s_i >= r+2t.

Combining them yields the exact initial score domain. The independent checks establish tuple membership, uniqueness and equality with an independently computed domain cardinality. That is full domain coverage, not simply agreement of a few aggregate survivor counts.

Sorting demands and residual row degrees is relabelling. Individual (d_i,R_i,z_i) column options remain paired with their demand labels; R-columns are not independently sorted in a way that would lose assignments. Forced labels arise only when a proved superset of eligible sources has exactly the required cardinality. Repeated pruning is justified by the preservation of every actual graph witness at each step.

V5's one-source tests do not require all sources to share a single witnessing assignment. This is a relaxation and can leave spurious survivors, not a reason for a false rejection. Later models strengthen those consistency requirements explicitly. They are not asserted to construct graphs.

### 2.5 Activation costs and shared pair resources

For a selected arc u->w, q_w-l_w >= (l_u-1-rho_w-l_w)_+. Dividing the cost of each incoming arc by a proved incoming cap P_w ensures the sum charged at w is at most q_w-l_w; it does not charge the same necessary outgoing increase separately for every incoming arc. The required-incidence subset has exactly s_i selected edges at each label, while the upper bound on total Q includes all actual selections.

The v5 flow relaxation intentionally omits some opposite-orientation pair and outgoing-total constraints. Since every actual required subset still gives a permitted flow, those omissions only weaken the test. Exact cut and potential certificates remain valid lower bounds for the relaxed problem. The audit found no double-counted resource in this step.

### 2.6 Source-local residual injection

For a source u partition A into selected neighbours S, residual neighbours T and missing neighbours M. Selected-edge domination rules out F(S,M). The new inequality is

    rho_u + 2e_F(S) + e_F(M) - e_C(T,M) <= r.

The proof supplies three disjoint residual-edge families by their A-endpoints in S, M and T. Missing M-pairs may use an auxiliary in T; allowing up to e_C(T,M) such pairs is necessary and is subtracted. The remaining auxiliary is in B and gives a residual cross edge with an A-exception. Unique exceptions and fixed endpoint classes establish the injection.

The degree-only consequences were rederived algebraically:

    sum_{i in S} d_i <= rho_u(2a-rho_u-3+q_u)-2t,
    sum_{i in S} R_i <= r-rho_u.

**Scope boundary:** the derivation for M-pairs uses full criticality, not merely the chosen B-quasi-edges. In the audited direct route it is applied to the original critical graph. This report does not silently import it into the alternative weak-core route.

### 2.7 Event normalisations and branch integrality

Label classes agree in demands, whole column domains and forced-source masks; source classes agree in residual degree, cap and forced-label pattern. Averaging relabelled copies within these classes does not assert that the graph has those automorphisms. Variables are probabilities of events and may be fractional even for an integral graph.

The audit checked the distinct-endpoint corrections, including N_g-1 and M_k-1 within a class, choose(N_g,2) for unordered same-class F-pairs, and both orientations of cross-status events. Source-conditioned ledger totals remain fixed after multiplying by the indicator q_u=q; no unjustified independence of column and source types is introduced.

V6 branches only on genuine integral counts of vertices, F-edges or selected/residual incidences, with their class-size multipliers. Its two branches are <=k and >=k+1. The additional kernel independently reconstructs those count multipliers and checks both children of every closed tree. It does not treat an unscaled averaged coordinate as Boolean. All 91 roots and 572 leaf certificates pass.

### 2.8 Actual endpoint degree types

For selected ui->w, label i neighbours u and every missing-B-pair neighbour of u except w. These are q_u+p_u distinct vertices. Hence

    R_i+x_i >= q_u+p_u.

The endpoint model attaches actual q,p and x types to the same selected incidence. Marginal totals at both ends count the same edges; their class-size factors are not inferred regularity. The allowed x range includes zero-demand extras, and the p range uses both minimum H-degree and the b-1 pair bound.

The final model omits the larger local J-variable extension but retains separately justified degree-only inequalities. The model stages need not be nested: each rejection has its own valid necessary-system certificate and the final disposition partition is complete. No graph-realisation search or unclosed branch is counted as a proof.

## 3. Complete fresh arithmetic replays

All six original checking jobs finished successfully. V4 was run in full `--replay` mode; v5/v6/v7/v8 used their complete `--check` routes, not smoke tests. The v3 checker includes the required order-28/Delta=16 scope. Per-job commands, exit codes, logs and fresh reports are preserved. These are reruns of the original separately written implementations, not additional independent researchers.

### Equality scope: 196 edges

| Stage | Exact recorded outcome |
|---|---|
| Initial score domain | 18,645 demand tuples; 1,976 retained intervals |
| Residual expansion | 17,669,896 rows; 24,411 survivors |
| Projected tests | 13,196 survivors |
| V5 joint and activation tests | 7,725 then 6,918 survivors |
| V6 shared and source-type tests | 4,617 then 479 survivors |
| V6 exact branch trees | 91 rows excluded by 572 leaves; 388 survivors |
| LocalIncidence-v7 | 22+19+347 exclusions; zero survivors |
| Separate Delta=16 scope | All 39 demand profiles and 604 residual profiles excluded |

Five inter-package handoffs, including decompression where appropriate, match byte-for-byte. Their source bytes and hashes are recorded in `HANDOFF_AND_SCOPE_REPORT.json`; they connect the full replayed equality domain to the exact final exclusions.

### Upper-bound scope: 197 edges

| Stage | Exact recorded outcome |
|---|---|
| Fresh t=2 score domain | 12,012 tuples; 1,229 retained intervals |
| Residual expansion | 8,216,928 rows; 5,154 survivors |
| Projected tests | 2,959 survivors |
| Joint column tests | 1,584 survivors |
| Final shared/source-type/endpoint tests | 787+790+7 exclusions; zero survivors |

This route generates and checks its own t=2 domains and every handoff. No equality-only survivor list is used as the new search universe.

## 4. Additional red-team checks

### Third arithmetic kernel

`scripts/third_certificate_kernel.py` uses a fresh dense integer accumulator, rather than the original sparse certificate-verification routine. It recomputes row signatures, multiplier types and signs, all aggregate coefficients and the strictly negative final right side. It also independently rebuilds branch count expressions and branch-path inequalities.

It checked **7,011 v6 leaves, 388 v7 leaves and 1,584 v8 certificates: 8,983 leaf systems and 833,923 cited constraint terms**. These support 6,530, 388 and 1,584 row exclusions in their respective input scopes. No floating-point solver is used. Six deliberate malformed-certificate controls per scope are rejected. Six additional damaged-tree controls reject missing children, invalid or fractional splits, an unscaled probability, a copied wrong child and a forged leaf.

**Independence limit:** this additional kernel imports the preserved checker model constructors. It is independent arithmetic and branch checking, **not a third independent graph-to-model derivation**. The original discovery/checker implementations and mathematical source review remain relevant to that separate obligation.

### Fresh graph regressions

`scripts/graph_stress.py` imports no project graph generator, quasi-edge unpacker or lemma checker. It constructs greedy edge-minimal diameter-two samples, C5 blowups, a Petersen graph and K(14,14), then directly verifies edge-criticality by every edge deletion. A fixed seed and complete encoded input record make the sample replayable.

The sample contains **107 labelled graphs at orders 5–28**, including 102 non-bipartite graphs. It checks **462 selected-system occurrences**, 1,659 selected incidences and 3,147 source-local instances. Nontrivial local terms occur: 145 instances have selected-internal F-edges and 861 have missing-internal F-edges. The shared-neighbourhood union is strictly stronger than a one-source maximum in 463 instances. Sixty-two one-spare-source premises are exercised. All checks pass.

The system occurrences need not all be distinct. The sample is not exhaustive. **None has positive surplus**, so these tests do not empirically validate the hypothetical dense-case exclusion. Universal correctness must rest on the proof. The older saved graph-lift and abstract-system tests were also rerun by their original wrappers; their limitations are unchanged.

## 5. Findings and severity

### RT-01 — non-blocking standalone helper input validation

The frozen v8 `src/check_rows.cpp` reads residual intervals and indexes a fixed bucket array without checking the interval range. A direct invocation with an unsupported 64..64 interval returned success and a report with zero states and zero survivors. A sanitizer run did not issue a diagnostic; absence of that warning does not validate the out-of-range input.

This is **not a failure of the n=28 proof driver**. `check197.py` independently establishes every OPEN interval, explicitly enforces 15<=lo<=hi<=63, verifies the complete retained demand list and checks the exact text file before calling the C++ program. Every actual proof input passes those gates. A zero-row malformed standalone run is not admitted as an exclusion certificate.

`patches/check_rows_input_guard.patch`, generated and tested by `scripts/harden_helper.py`, adds range, ordering, record-count and trailing-input checks to a separate copy. It rejects four malformed cases and processes the full valid 8,216,928-row scope with exactly the original report, survivor bytes and band bytes. The original archived source is retained unchanged. Use the full driver, not a bare helper's exit code, as the proof entry point.

### RT-02 — resolved evidence-publication discrepancy

The three original ZIPs are now present in their dated repository directories with the same Git objects, sizes and payload checksums. The earlier missing-archive statements remain in historical receipts but are explicitly superseded. The separate degree-load-v7 bundle is a different artifact and remains separately tracked; it is not required by the direct route audited here.

### RT-03 — remaining trust boundaries, not failed calculations

The strongest remaining obligations are independent review of the structural injections and graph-to-model lift, independent reproduction by another researcher, and a presentation that keeps the two v7 routes and the two edge densities distinct. Formal-kernel verification has not been performed. Both original implementations and this audit were produced by the same assistant under the same project direction. Repeated agreement is not independence of authorship.

Fan's original 1987 proof was not re-audited: its publisher endpoint returned HTTP 403. The bound was checked in Wang's primary manuscript and recomputed with exact rational arithmetic. The complement correspondence and star convention were checked in the published Haynes et al. paper, including a rendered page. The Wang PDF screenshot endpoint failed; its formula was read from the parsed text. Neither source-access limit is concealed as a completed original-proof audit.

## 6. Assembly and disposition

For m=197, Delta<=14 is excluded by the degree sum; Delta=15 by the fresh complete computation. At Delta=16 the required charging sum is 26, while eleven integer-demand terms supply at most 176/7. The pointwise factorisation proving the maximum 16/7 was checked for every permitted integer. Delta=17 through 26 violate the inherited h-index bound, and Delta=27 forces a star. Fan's strict bound is exactly 78883/400, so integer m<=197 and the candidate upper bound becomes 196.

For m=196, Delta<=14 forces a 14-regular graph. Two nonadjacent vertices have at least two common neighbours, so no edge can rely on a unique two-step witness. Critical edges therefore lie in no triangle. The regular triangle-free graph is K(14,14). The other degrees are excluded by the replayed Delta=15 and Delta=16 scopes and the high-degree/star reductions. K(14,14) is directly verified as diameter-two edge-critical in the fresh graph tests.

**Audit disposition: no blocking defect found in this internal pass; direct order-28 candidate remains supported.** This is not a guarantee that an external reviewer will find no gap. No frozen theorem ledger is promoted, no order above 28 is claimed complete, and no priority, novelty or all-order claim follows.

## Sources and reproducibility

Mathematical sources are the original PROOF.md files and associated checker source in the six hash-pinned archives; the n27 Section 5–7 residual/activity/low-k arguments at repository commit `bdf22db366c66516c2ce21e26fedaa5408c7ce08`; and the following published inputs:

1. Tao Wang, *On Murty-Simon Conjecture*, arXiv:1205.4397, pp. 2–3: https://arxiv.org/pdf/1205.4397 . Used for the reported Fan bound and corroborating complement correspondence; Fan's original proof remains an external input.
2. T. W. Haynes, M. A. Henning, L. C. van der Merwe and A. Yeo, *A maximum degree theorem for diameter-2-critical graphs*, Central European Journal of Mathematics 12(12) (2014), 1882–1889, Theorems 3.1–3.2 and Observation 3.4: https://d-nb.info/1372516379/34 . Used with the explicit star convention, not a blanket unqualified complement assumption.

The audit package contains scripts, complete fresh reports, command logs, the guard patch, encoded fresh graph inputs, source archive hashes and a replay driver. Original proof archives are required separately and are never recompressed or replaced. See README.md for exact commands. A proof about all relevant graphs and a test run on finitely many examples remain different things.


\newpage

# Included source: `project/research/general_n/2026-09-07-direct-197-v8/README.md`

# Direct 197-edge exclusion at order 28 — v8

7 September 2026. **Candidate mathematics; creation-session complete direct arithmetic REPRODUCED; independent mathematical review OPEN.**

Read [DIRECT_197_SUMMARY.md](DIRECT_197_SUMMARY.md), [RESULTS.json](RESULTS.json) and [EXACT_CHECK_REPORT.json](EXACT_CHECK_REPORT.json). Full proof, code and exact certificates are in the [complete original ZIP](MurtySimon_N28_197_Direct_v8.zip), now attached to this directory.

The fresh (n,Delta,m)=(28,15,197), t=2 calculation excludes every final row: 787 shared, 790 source-degree-type and seven endpoint-type certificates, with zero survivors. No integer branching, t=1 survivor-list transfer or weak-core density reduction is used. Other maximum degrees at 197 are covered explicitly; Fan's strict 197.2075 bound supplies the candidate upper bound 196. The separately preserved equality chain supplies the equality characterization K(14,14).

## Archive and replay

The unchanged archive uploaded by Paul in commit `9698513eb20817ebfa9556e79b11d5f538280065` contains 90 payload files plus MANIFEST.json. It is 5,677,524 bytes; SHA-256 `b753076ffc755066a0c57756be91cc5b265c163d869244d3aa65e3943799347b`; Git blob `45889e1b36f0bc395f9f39b9c18035b52ce74dbb`.

Publication intake checked CRCs, safe paths, exact manifest coverage and every payload length and SHA-256. Extract into a fresh directory and, inside `MurtySimon_N28_197_Direct_v8`, run:

```sh
python3 -I -B replay.py --verify-only
python3 -I -B replay.py --check --output /absolute/path/to/new-v8-replay
```

Integrity checking uses Python's standard library. Complete arithmetic checking also requires g++ with C++17 and Boost headers, no optimisation solver or network. Keep assertions enabled; do not use `-O`. No prior ZIP is needed for the new direct197 replay; the equality chain is a separate dependency.

## Provenance and review boundaries

The [previous directory guide](README_before_archive_publication.md), earlier PUBLICATION_RECEIPT.json and the original files inside the ZIP preserve the historical documentation-only state. Their statements that the binary archive was pending are superseded by this publication, not silently rewritten as historical successes.

The [v6 archive](../2026-09-07-shared-adjacency-v6/README.md) and [LocalIncidence-v7 archive](../2026-09-07-local-incidence-v7/README.md) are now attached too. They are distinct from the separate degree-load-v7 audit bundle, whose availability remains separately recorded.

A full direct197 check was recorded in the creation session, with fresh v6/v7 and Delta16 checks. A fresh full-chain red-team audit is being conducted separately; this publication does not pre-announce its outcome. Universal lemmas, graph-to-model lifting and upstream coverage remain mathematical review obligations. Both original implementations are by the same assistant, not independent researchers. Frozen n25/n27 proofs and the governed ledger are unchanged.


\newpage

# Included source: `project/research/general_n/2026-09-07-direct-197-v8/EXACT_CHECK_REPORT.json`

{
  "LP_exact_rejections": {
    "endpoint": 7,
    "shared": 787,
    "typed": 790
  },
  "LP_inputs": 1584,
  "all_joint_survivor_columns_caps_forced_labels_reconstructed": true,
  "charging_domain": 12012,
  "complete_fresh_domain_and_disjoint_handoffs": true,
  "discovery_or_optimisation_imported": false,
  "every_LP_constraint_rebuilt_by_separate_checker": true,
  "final_survivors": 0,
  "full_upstream_equality_chain_replayed_here": false,
  "initial_counts": {
    "OPEN": 1229,
    "dual": 1570,
    "source_count": 9146,
    "support": 67
  },
  "joint": {
    "exact_rejections": 1375,
    "inputs": 2959,
    "surviving_demand_patterns": 359,
    "survivors": 1584
  },
  "mathematical_status": "candidate; independent mathematical review OPEN",
  "negative_controls": {
    "duplicate_LP_disposition": "REJECTED",
    "duplicate_LP_multiplier": "REJECTED",
    "duplicate_demand": "REJECTED",
    "empty_LP_contradiction": "REJECTED",
    "forged_LP_rhs": "REJECTED",
    "negative_inequality_multiplier": "REJECTED",
    "omitted_LP_disposition": "REJECTED",
    "omitted_demand": "REJECTED",
    "unknown_LP_constraint": "REJECTED",
    "wrong_LP_input_row": "REJECTED",
    "wrong_edge_scope": "REJECTED",
    "wrong_t_scope": "REJECTED",
    "zero_initial_dual": "REJECTED"
  },
  "old_t1_survivors_used_as_t2_domain": false,
  "projected": {
    "complete_partition": true,
    "negative_controls": {
      "forged_pair_count_rejected": true,
      "omitted_survivor_detected": true
    },
    "projected_pair_certificates": 162,
    "rows_checked": 5154,
    "surviving_demands": 497,
    "surviving_rows": 2959,
    "zero_slack_certificates": 2033
  },
  "residual_domain": {
    "fnv64": "16479821321584091042",
    "initial_source_rejections": 8194665,
    "low_k_rejections": 0,
    "refined_source_rejections": 17109,
    "states": 8216928,
    "survivors": 5154
  },
  "retained_demands": 1229,
  "scope": {
    "a": 12,
    "b": 15,
    "m": 197,
    "n": 28,
    "t": 2
  },
  "seconds": 118.0112499559998,
  "stage_seconds": {
    "LP": 21.353939716000014,
    "initial": 1.2517029109999385,
    "joint": 92.313489936,
    "projected": 0.6093683980000151,
    "residual_enumeration": 1.2512035390000165
  },
  "weak_core_reduction_used": false
}
