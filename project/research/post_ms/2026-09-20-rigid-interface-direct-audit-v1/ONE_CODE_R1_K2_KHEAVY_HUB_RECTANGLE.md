# Residual-one k=2 K-heavy residual-hub rectangle

Date: 2026-09-20

Status: **same-session strengthening** of the predecessor K-heavy `q_j` spoke lemma, conditional on `J2=empty`. No finite scan is used.

## 1. Predecessor spoke lemma

Let R be the K-heavy escape set. At `J2=empty`, if `w in R` is adjacent to the residual hub q_j, the predecessor heavy-reservoir theorem proves that raw criticality forces a matched head h(w) with

> `N(q_j) cap N(h(w))={w}`.                              `(KH-HUB)`

Different w require different h(w).

## 2. The injective spokes create an H--R hole rectangle

Let

`R_j={w in R : w q_j in E}`, `rho=|R_j|`.

For each w in R_j choose its injective witness h(w). Every other `w' in R_j\{w}` is also adjacent to q_j. Therefore `(KH-HUB)` forces

`h(w)w' notin E`.

The rho distinct heads `H_j={h(w):w in R_j}` consequently miss all off-diagonal pairs to R_j:

> **`Z_{H_j,R_j} >= rho(rho-1)`.**                       `(KH-RECT)`

This is a located H--U block inside the X-side rooted deficit. It was implicit in the singleton equations but not retained in the predecessor statement.

## 3. Cheap K-heavy mass must be residual-hub sparse

Normalize `rho/p -> varrho`. Then `(KH-RECT)` alone contributes asymptotic coefficient at least

`varrho^2`

to Z_X/p^2. Hence any sequence attempting to approach a lower envelope that leaves no positive extra X-hole coefficient must satisfy

> **`rho=o(p)`.**                                         `(KH-NONHUB)`

So the same qualitative compression found for D1 applies to K-heavy vertices as well: a genuinely cheap linear K-heavy reservoir is forced toward q_j-nonneighbours.

## 4. Combined sparse-hub endpoint

At the current R+D1 coarse optimizer, both linear populations are now pushed toward missing the residual hub:

- D1 q_j-neighbours pay the weighted split penalty from `ONE_CODE_R1_K2_D1_QJ_SPLIT_WEIGHTED_AUDIT.md`;
- K-heavy q_j-neighbours pay `(KH-RECT)`.

Thus, up to lower-order exceptional mass, the entire escape reservoir E is driven toward U-codes that agree with d at the residual coordinate j.

The W_s-free private-spoke theorem then says that any remaining private support is either Y-killing forward or H-consuming reverse. Positive-density private support overlap between D1 and K-heavy vertices is also physically expensive.

## 5. Strategic consequence

The next hostile normal form to test is therefore:

- almost every escape misses q_j;
- almost every cheap D1 vertex has sparse private support;
- cheap K-heavy private support must either be sparse/separated or pay reverse-spoke H-holes;
- proper-support same-code classes are independent.

A plausible surviving abstract model may spread the p-1 escape vertices over p-1 private coordinates with nearly disjoint small supports. That possibility should be constructed explicitly as a method stress test before claiming that the present local theorems imply code concentration.

Global caveat unchanged: zero positive actual-D2C rigid complete Hall-cut fixtures with `x>=3` remain in bounded regression.