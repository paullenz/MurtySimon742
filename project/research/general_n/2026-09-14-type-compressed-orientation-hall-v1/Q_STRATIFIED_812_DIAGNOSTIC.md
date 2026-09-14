# q-stratified diagnosis of the 812 global-layer false negatives

14 September 2026. **Frozen reconnaissance result; no whole-state promotion.**

## Provenance

The source is the complete detailed exception table produced by GitHub Actions run

```text
run id:      34850187436
artifact id: 10351372086
artifact:    layered-receiver-exception-diagnostic
```

The extracted 812-row TSV hashes to

```text
sha256:c4f859f97bed726f6e4799473906bd1673520aa2501d755fc5136a1c3cb46885
```

Machine-readable frozen summary: [`Q_STRATIFIED_812_DIAGNOSTIC.json`](Q_STRATIFIED_812_DIAGNOSTIC.json).

## 1. Main result

The global receiver-layer rearrangement had 812 false negatives among 205,919 exact target-Hall failures.

Rearranging **separately inside each q-stratum** eliminates the entire residue:

```text
812 global-layer false negatives examined
812 q-stratified detections
812 q-stratified upper bounds equal exact receiver capacity
0   positive q-stratified gaps
```

Thus every one of the 812 failures is lost solely by allowing receiver capacity to be rearranged **across different q levels**.

No target-by-target information beyond `q` is needed on this frozen residue.

## 2. Selected status is q-homogeneous on the residue

For every one of the 812 canonical maximal witnesses, every fixed-q stratum has constant selected status:

```text
profiles with a q-level containing both selected and unselected target types: 0
```

Moreover the selected q-levels form a threshold among the q values present in the profile. The first selected q value is distributed as

```text
q*=3 : 349
q*=4 : 242
q*=5 : 173
q*=6 :  48
```

The gap from the largest unselected q to the smallest selected q is

```text
1 : 340
2 : 415
3 :  56
4 :   1
```

This is striking frozen-pilot evidence, **not yet a universal theorem**.

## 3. The exact crossing statistic vanishes

[`Q_STRATIFIED_CROSSING_GAP.md`](Q_STRATIFIED_CROSSING_GAP.md) identifies the exact q-only rearrangement loss as

```text
C_q = sum_{q,m} min(H^S_{q,m},L^O_{q,m}).
```

On the 812 residue,

```text
C_q=0
```

for every profile. This is equivalent to the observed 812/812 q-stratified exact-capacity matches.

The preserved counterexample in [`Q_STRATIFIED_EXACTNESS_COUNTEREXAMPLE.md`](Q_STRATIFIED_EXACTNESS_COUNTEREXAMPLE.md) shows that `C_q=0` is not an abstract Hall theorem and therefore requires a Murty-specific explanation if it is to be used universally.

## 4. Comparison with simpler scalar consequences

The newer residual/slack inequalities were also evaluated exactly on all 812 profiles.

### Coupled residual-slack budget

For every residual slack layer `j`,

```text
sum_{w:s_w>=j} max(0,y_w+a-b+j) <= r-b.
```

Across the 812 profiles the **smallest remaining slack is 17**.

So this inequality is valid and useful structurally, but by itself it does not come close to eliminating this residue.

### Positive-slack incidence pressure

The inequality

```text
D(O)+|O|+Y_1 <= sum_{w in Z} d_D^-(w)
```

has minimum slack **1** on the 812 set. It is much sharper, but still does not exclude any of the 812 profiles by itself.

The unique minimum-slack profile occurs in state 2984.

### Whole-exterior residual expansion

The exact residual capacity of the whole exterior exceeds exterior demand by at least **2** throughout the 812 set.

Thus the decisive refinement is not a hidden violation of the existing scalar slack budgets. It is the restoration of q-level correlation.

## 5. Research consequence

The target-correlation problem has narrowed to

```text
global receiver layers
 -> split by q
 -> exact capacity on all 812 difficult profiles
 -> only possible residual error is the explicit crossing statistic C_q.
```

The next all-order analytic target is therefore to control `C_q`, not an arbitrary target matching.

For the canonical maximal witness, [`CANONICAL_EQUAL_Q_SWAP_RIGIDITY.md`](CANONICAL_EQUAL_Q_SWAP_RIGIDITY.md) shows that every positive crossing forces a saturation wall: the selected higher-c endpoint is under-saturated, while every receiver gained by that higher-c source over the lower-c unselected endpoint is strictly over-saturated.

That rigid configuration is the natural point at which to apply the Murty residual/excess/source-cap budgets.

## 6. Trust boundary

This note is a deterministic analysis of a frozen GitHub Actions artifact. It promotes no scalar state and proves no all-order q-homogeneity theorem.

The full frozen-pilot q-crossing replay and independent finite verification of the crossing identity are separate audit gates. External mathematical review remains open.
