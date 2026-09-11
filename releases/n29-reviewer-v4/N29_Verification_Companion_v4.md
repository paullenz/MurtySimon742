---
title: "N=29 Murty-Simon candidate: verification companion"
subtitle: "Reviewer-v4 dependency map, regressions, and audit boundaries"
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

## 1. What changed in v4

Reviewer-v3 made the corrected minimal trusted kernel proof-critical for `Delta=16` at 210 and 211 edges and used progressively smaller finite checks higher in the same degree branch.

Reviewer-v4 replaces **all** proof-critical `Delta=16` computation at every `m>=210` by the hand threshold-tail inequality

```text
Q(s) <= 18,
```

which combines with the bridge lower bound

```text
Q(s) >= 16 + 2t,     t=m-208,
```

to force `t<=1`. Therefore `Delta=16` is impossible whenever `m>=210`.

The theorem-level candidate statement is unchanged:

```text
e(G) <= 210,
with equality exactly K(14,15).
```

## 2. Current proof architecture

| Scope | reviewer-v4 method | Proof-critical computation? |
|---|---|---|
| Delta <= 14 | degree sum | no |
| Delta = 15 | witness-deficit hand proof; equality forces K(14,15) | no |
| Delta = 16, every m >= 210 | bridge + threshold capacity + hand tail-deficit bound | **no** |
| Delta = 17 | pointwise charging hand bound | no |
| Delta = 18,...,27 | residual h-index hand bound | no |
| Delta = 28 | universal-vertex/star observation | no |

Thus the current N29 candidate proof is logically computation-free. Exact programs remain independent regression evidence.

## 3. Delta=16 trust boundary

The frozen self-contained bridge is

`project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md`.

Reviewer-v4 uses only these Delta=16 consequences:

1. `S>=r+2t`;
2. residual activity `rho_u>=1` for `t>0`;
3. selected-incidence forcing `s_i<=rho_u`;
4. a selected source has `rho_u<=11`, so positive `s_i<=11`;
5. threshold capacity

   ```text
   2W_h <= z_h^2-z_h+h(h+1).
   ```

It does not use the isolated-C lemma, grouped LP embedding or Farkas checker semantics.

## 4. Threshold-tail reduction

For `h>=2`, define

```text
W_h = sum_{i:s_i>=h} s_i,
g_h(W) = least threshold-compatible z_h,
Q(s) = S - sum_{h=2}^{11} g_h(W_h).
```

Residual activity turns `r=sum rho_u` into a tail sum and yields

```text
Q(s) >= 16+2t.
```

The hand proof then writes

```text
N_h = #{i:s_i>=h},
p=N_1,
D=sum_{h=2}^{11}(N_h-g_h(W_h)),
Q=p+D.
```

It proves `D<=6` by monotone clipping:

```text
all demands >6 -> 6 -> 5 -> 4 -> 3,
```

with explicit endpoint cases, then reduces to

```text
x=N_2,
y=N_3,
D=x+y-g_2(2x+y)-g_3(3y),
0<=y<=x<=12,
```

and proves `D<=6` in three elementary ranges of y. Since `p<=12`, `Q<=18`.

Detailed proof:

`project/research/general_n/2026-09-11-threshold-tail-collapse-v1/N29_DELTA16_THRESHOLD_TAIL_HAND_PROOF.md`.

## 5. Independent exact regressions

The hand argument is not dependent on these computations, but two exact checks independently support it.

### Local hand-obligation checker

`n29_delta16_threshold_tail_hand_check.py` checks only the finite endpoint tables used by the clipping proof and the final 91 pairs `0<=y<=x<=12`. It uses integer arithmetic only, no solver and no floating point.

### Full demand-domain checker

`n29_delta16_threshold_tail_collapse_exact.py` exhausts all

```text
C(23,12)=1,352,078
```

nondecreasing demand multisets `0<=s_i<=11` and independently finds

```text
max Q(s)=18.
```

The four maximisers are

```text
(2,3^11), (3^12), (3,4^11), (4^12).
```

Both checks passed together in GitHub Actions run `34617844004`.

A separate rowwise audit regenerated the historical `t=3` minimal kernel and found that all 126 residual rows fail the written threshold family, including all 94 positive zero-slack RX-Hall profiles. Run `34616219528` passed. This is corroboration only.

## 6. Historical minimal kernel: retained, not proof-critical

The corrected reviewer-v3 route remains valuable independent evidence:

| Edge count | t | Retained demands | Residual rows | Exact Farkas rejections | Final survivors |
|---:|---:|---:|---:|---:|---:|
| 211 | 3 | 72 | 126 | 126 | 0 |
| 210 | 2 | 367 | 1,467 | 1,467 | 0 |

The v1 grouped cumulative-threshold builder had a real label-group multiplicity bug and its certificates remain quarantined. Corrected v2 and exact integer Farkas verification remain preserved. Reviewer-v4 simply no longer needs that stack logically.

## 7. Why this reduces correlated-error risk

Reviewer-v3's largest correlated risk was the actual-graph-to-averaged-variable embedding of the corrected late LP. Reviewer-v4 removes that model from the theorem proof completely.

The highest-value independent targets are now:

1. complement/quasi-edge and selected/residual semantics;
2. residual activity;
3. selected-incidence demand forcing;
4. threshold capacity;
5. the hand tail-deficit clipping proof;
6. Delta=15 witness/equality counting;
7. Delta=17 pointwise charging and Delta>=18 residual h-index;
8. the dominating-edge citation.

## 8. Recommended review order

A hostile reviewer should:

1. reconstruct the selected/residual bridge from the graph;
2. verify the exact ledger `S>=r+2t`;
3. attack residual activity for collisions or hidden selected edges;
4. verify `s_i<=rho_u` and `rho_u<=11` at selected sources;
5. independently prove threshold capacity;
6. independently check each clipping step in `D<=6`;
7. verify the final two-level inequalities;
8. audit the short Delta=15,17 and h-index branches;
9. only then use the exact regressions as corroboration.

No rerun of the LP/Farkas stack is required to assess reviewer-v4.

## 9. Provenance rule

Reviewer-v3 and all earlier packages remain frozen. The old computational route, the normalization bug, its correction and every audit report stay public. Reviewer-v4 is a successor, not a rewrite of history.
