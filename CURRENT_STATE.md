# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-19  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is **not** the target. The published 2024 D2C graph `X_3` on 12 vertices and 32 edges has `M(12)=31` and remains a mandatory negative control. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not an optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_BUFFER_ROOTED_EDGE_STRICT_LAYER_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `7b5dc8c2d0d511d87981080ae5c2cceb953807b0`

LAST VERIFIED RESULT: `The former first positive-buffer equality layer is closed by an upstream raw-criticality obstruction. In the rigid one-code common-buffer setup with d_Y(b)=0 and epsilon_b=p-g, prior work forces every buffer--X edge bx to have an outside witness z in U_o with bz in E, xz notin E, N(x)∩N(z)={b}, c(z)=bar c(x), and z anticomplete to Y. Since c(x) != bar d, choose a tight coordinate i with c(x)_i=d_i. Then z and b share the matched endpoint q_i selected by bar d. The rooted B-edge zq_i must have a singleton A-witness orientation. Forward orientation cannot use Y because Y misses q_i, and cannot use X because b is an extra common neighbour under b--X completeness. Reverse orientation cannot use Y because z is anticomplete to Y, and cannot use X because b is again an extra common neighbour. Contradiction. More generally, any outside-U buffer certificate forces a physical buffer--X nonedge. Hence d_Y(b)=0 implies epsilon_b>=p-g+1. The first strict layer epsilon_b=p-g+1 has exact defect identity epsilon_b=(p-g)+h_X+h_o and splits into one X-hole or one U_o-hole. The U_o-hole subtype is impossible. Therefore the only live first-strict unloaded geometry has one unique X-hole ba_0 and b complete to U_o. Every remaining buffer--X edge is outside-U certified; rooted matched-edge certificates funnel through a_0. Writing S_0={i:c(a_0)_i!=d_i}, every buffer-neighbour x with outside witness z_x satisfies either Type F: |{i:c(x)_i=d_i}|=1 and that unique coordinate lies in S_0, or Type R: S_0 subseteq S_x and xa_0 is a nonedge. Consequently every X-neighbour of a_0 must have code at Hamming radius p-1 from d. This is now the live structural frontier.`

UNPRESERVED WORK: `None. The equality-layer closure is preserved under project/research/post_ms/2026-09-19-buffer-rooted-matched-edge-collapse-v1/ and the first-strict unique-hole classification is preserved under project/research/post_ms/2026-09-19-buffer-first-strict-layer-v1/. The predecessor shared-core resource cone remains preserved as correct conditional algebra but is no longer a live graph tail because its parent equality geometry is now proved empty.`

DEFERRED ADMIN: `README remains synchronized to the 19 September daily audit trust boundary. Do not erase the predecessor shared-core work; reclassify it as conditional downstream mathematics on a now-closed parent layer. Refresh reviewer-facing status at the next daily adversarial checkpoint unless repository integrity requires earlier repair.`

NEXT ACTION: `Stay in the first strict unloaded common-buffer layer before opening the loaded buffer. Intersect the unique-hole funnel with the exact Hall X-density identity and pair-local Ccap_P. Let a_0 be the unique X non-neighbour of b. Every b-neighbour x is outside-U certified and is either Type F (its code differs from d in p-1 coordinates) or Type R (S_0 subseteq S_x and xa_0 is a nonedge). Prove a density/support dichotomy: many Type F heads should incur extreme-radius / pair-capacity cost; Type R dominance makes a_0 nearly isolated in G[X] and should force Hall slack. Preserve pair-local S_P rather than total-score substitution. If this first-strict layer survives, feed its single physical buffer hole into the rooted slot/residual ledger delta=r-e(F); only then open the loaded-buffer alternative d_Y(b)>0. Keep m=g+2,z=2,k-small side branches and the four-exception gate subordinate unless they become load-bearing. Keep X_3 and the graph-level audit boundary explicit.`
<!-- CURRENT-STATUS:END -->

---

## 1. Mandatory audit gate

This run began by rereading `CURRENT_STATE.md`, root `README.md`, the latest commit chain, the 19 September daily adversarial audit, `INDEPENDENT_SOURCE_TUPLE_REPROOF.md`, the repaired source-premise / actual-D2C graph-level regression status, and the current shared-core handoff before forward mathematics.

Binding trust boundary:

- distinct physical beta-source identity: raw singleton-criticality proved;
- `(source,coordinate)` uniqueness: selected-representative uniqueness only, not raw-witness uniqueness;
- finite source-tuple capacity theorem: independently re-derived only conditional on those two named premises, not unconditional graph-level closure;
- actual-D2C regression: `X_3` retained, zero recorded graph/formula mismatches, but no bounded fixture realizes the full rigid complete-cut hypotheses;
- exact pair-local `S_P/Ccap_P` remains mandatory downstream;
- four-exception gate remains subordinate.

The predecessor proposed continuing inside the unmatched-heavy shared-core resource cone. This run departed from that downstream priority for a precise mathematical reason: a raw rooted B-edge criticality check closes the cone's parent buffer-equality hypothesis before source capacity or pair optimization is needed. The closure is therefore upstream of, and consistent with, the audit's preference for testing dominant premises before building further downstream theory.

---

## 2. Rooted matched-edge self-pricing

In the positive-buffer common-buffer branch, an outside Orientation-A certificate for `bx` has

`bz in E`, `xz notin E`, `N(x) cap N(z)={b}`,

`c(z)=bar c(x)`, and z anticomplete to Y.

Since `c(x) != bar d`, choose a tight coordinate i with `c(x)_i=d_i`. Then b and z both select the `bar d` matched endpoint `q_i`, so

`bq_i,zq_i in E`.

The edge `zq_i` lies in the rooted B-layer. Raw rooted triangle-edge criticality therefore requires an A-witness in one of two singleton orientations.

Without assuming buffer equality, either orientation forces the A-witness to lie in X and to be nonadjacent to b:

- forward `z -> q_i`: Y misses q_i; any X-witness adjacent to b has b as a second common neighbour;
- reverse `q_i -> z`: Y cannot witness because z is anticomplete to Y; any X-witness adjacent to b again has b as a second common neighbour.

Thus every outside-U buffer certificate forces at least one physical buffer--X hole.

This lemma uses no source-tuple theorem, no selected representative uniqueness and no finite scan.

---

## 3. Former equality layer is empty

In the first positive-buffer equality layer

`d_Y(b)=0`, `epsilon_b=p-g`,

the exact buffer degree floor forces b complete to X and U_o. Previous repaired criticality already proves that reverse buffer certificates and matched Orientation-A certificates are impossible, so every `bx` must use an outside-U certificate.

But the self-pricing lemma says any such certificate forces a buffer--X nonedge. Contradiction.

Therefore

> `d_Y(b)=0  =>  epsilon_b>=p-g+1`.

This closes the entire parent layer for every `t=p-g>=1`. All `m=g+1`, E=1, shared-core E=2, one-core R2+R2 and R3 descendants inside the old equality layer cease to be live realizability branches. Their proved conditional implications remain archived.

`X_3` is untouched because it has `u=0` and never enters this branch.

---

## 4. Exact first-strict buffer split

For an unloaded buffer put

`h_X=e_bar({b},X)`, `h_o=e_bar({b},U_o)`.

Direct degree counting gives the exact identity

> `epsilon_b=(p-g)+h_X+h_o`.

Hence the first strict layer `epsilon_b=p-g+1` has only two possibilities:

1. `h_X=1,h_o=0`;
2. `h_X=0,h_o=1`.

The second is impossible. If b is complete to X and has one U_o non-neighbour z_0, matched Orientation A is unavailable and outside Orientation A is forbidden by self-pricing. Any reverse certificate must then use the same z_0, but the fixed pair `(b,z_0)` can have at most one singleton X-head while b has x>=3 X-edges.

Thus the only first-strict unloaded subtype is

> `h_X=1`, `h_o=0`.

Let `a_0` be the unique X-hole. Then b is complete to U_o and to `X\{a_0}`.

---

## 5. Every surviving buffer edge is outside-U certified

For an edge `bx`, `x!=a_0`, reverse orientation is impossible:

- root and matched witnesses fail by rooted common neighbours;
- U_o is complete to b;
- U_- shares tight matched neighbours with b;
- Y shares at least the x-1>=2 buffer-neighbour X-vertices with b;
- an X reverse witness has code neither d nor bar d, hence shares a tight matched neighbour with b.

Matched Orientation A is already excluded by the preserved matched-channel collapse. Therefore every edge from b to `X\{a_0}` uses an outside witness `z_x in U_o` with the standard complementary-code and Y-anticompleteness properties.

---

## 6. Unique-hole funnel and Boolean support dichotomy

For each such outside witness and every coordinate `i` with `c(x)_i=d_i`, the shared matched edge `z_x q_i` must use the unique buffer hole `a_0` as its rooted A-witness.

Set

`S_0={i:c(a_0)_i!=d_i}`,

`S_x={i:c(x)_i!=d_i}`,

`I_x=[p]\S_x`.

The adjacency `z_x a_0` fixes all rooted orientations generated by this witness.

- If `z_x a_0` is a nonedge, only the forward orientation is available. The fixed pair `(z_x,a_0)` can have only one singleton matched head, so `|I_x|=1`; that coordinate lies in `S_0`. This is **Type F** and `|S_x|=p-1`.
- If `z_x a_0` is an edge, only reverse orientations are available. Then every i in `I_x` has `c(a_0)_i=d_i`, so `I_x cap S_0=emptyset`, equivalently `S_0 subseteq S_x`. The original buffer certificate then forces `xa_0` to be a nonedge. This is **Type R**.

Consequently

> every X-neighbour of `a_0` has Hamming radius exactly `p-1` from d.

All non-extreme buffer neighbours are physically separated from `a_0` and their code supports contain `S_0`.

This is the live bridge into Hall density and pair capacity.

---

## 7. Preserved artifacts

New theorem packages:

- `project/research/post_ms/2026-09-19-buffer-rooted-matched-edge-collapse-v1/BUFFER_ROOTED_MATCHED_EDGE_COLLAPSE.md`
- `project/research/post_ms/2026-09-19-buffer-first-strict-layer-v1/BUFFER_FIRST_STRICT_LAYER.md`

Predecessor resource-cone package remains preserved at

- `project/research/post_ms/2026-09-19-shared-core-resource-cone-v1/`

with its original trust boundary. It is now historical conditional downstream mathematics, not the live branch.

---

## 8. Next handoff

Do **not** return to the old shared-core tail. Its parent equality layer is closed.

Stay in the first strict unloaded layer and use the unique-hole support dichotomy against the exact Hall identity. The desired compact theorem is a two-arm obstruction:

- many Type-F heads imply many radius-`p-1` codes and should be expensive under exact pair-local capacity / crowding;
- few Type-F heads imply `a_0` has small X-degree because all Type-R heads miss it, which should force Hall slack / rooted unused-slot cost.

Keep the exact pair variable `S_P`; do not replace it by total `C0`. If the unique-hole layer survives, feed the single located X-hole and its nested support geometry into `delta=r-e(F)` and Q before opening the loaded-buffer branch. The loaded branch, `z=2`, `m=g+2`, and the four-exception gate remain deferred until then.
