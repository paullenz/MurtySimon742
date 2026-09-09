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
