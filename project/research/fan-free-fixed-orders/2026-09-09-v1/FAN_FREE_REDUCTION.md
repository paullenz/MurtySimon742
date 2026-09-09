# Fan-free upper-range reduction for the n=25 and n=27 candidate proofs

9 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: candidate fixed-order proof component with exact finite arithmetic. Independent mathematical and computational review remains OPEN.**

## 1. Purpose and historical relation to Fan

The original n=25 and n=27 candidate manuscripts use G. Fan's 1987 theorem

> G. Fan, *On diameter 2-critical graphs*, Discrete Mathematics 67 (1987), 235-240, DOI 10.1016/0012-365X(87)90174-9,

as a convenient published reduction showing that only 157 edges at n=25 and 183 edges at n=27 need be examined above the conjectured extremal values.

This note removes **Fan's theorem as a logical dependency** of those two fixed-order candidate proofs. It does **not** claim to reproduce Fan's stronger all-order theorem. Instead it proves directly, using the project's already stated witness/quasi-edge/residual lemmas, that every edge count *above* the old Fan caps is impossible at these two orders.

The original Fan-based manuscripts remain frozen and preserved as historical versions. The reviewer-facing v2 assembly should cite Fan for attribution/history, but should use the argument below as the logical upper-range reduction.

## 2. Common ingredients

No new graph-theoretic hypothesis is introduced here. The finite verifier uses only necessary conditions already proved in the fixed-order manuscripts:

1. the complement/quasi-edge setup and the convention choosing **exactly one selected cross-edge for each missing unordered pair in B**;
2. the residual ledger

   ```text
   e(C)+r=L,
   e(F)=r+t,
   sum d_i = 2(r+t),
   sum rho_b = r;
   ```

3. residual activity `rho_b >= 1`, hence `r >= b`, whenever `t>0`;
4. the small-k necessary inequalities;
5. the selected-pair threshold inequality

   ```text
   ell_j <= #{ unordered {b,w} : rho_b+rho_w >= j };
   ```

6. source-cap and source-threshold upper bounds;
7. the residual-column h-index lower bound;
8. where necessary, the fixed residual-column source-cap refinement and strict subset-capacity inequality.

The enumeration deliberately retains nongraphical degree multisets. Therefore eliminating the enumerated relaxation is safe: every actual graph satisfying the bridge would appear in it, while many impossible numerical states are intentionally retained.

The selected-pair convention is important. Selection is indexed by the missing **unordered** B-pairs: one representative quasi-edge is chosen for each such pair. Opposite orientations of the same B-pair can never both be selected. Likewise, whenever the residual-injection proof forces an A-B edge whose two endpoints both miss an A-vertex, that edge cannot be selected for a B-B missing pair, because the unique exception of a selected edge belongs to B. These points are semantic consequences of the construction, not extra assumptions.

## 3. n=25 without Fan

Let `m=e(G)`.

### 3.1 Degree ranges outside Delta=14,15,16

If `Delta <= 12`, then the degree sum gives

```text
2m <= 25*12 = 300,
```

so `m <= 150`.

If `Delta >= 17`, the independent complement maximum-degree theorem already used in the frozen manuscript gives `m <= 155`; this step never depended on Fan.

For `Delta=13`, the witness-deficit inequality from Section 3 of the frozen n=25 proof is

```text
m <= C(h,2) + h(25-h) + o(o-1),
2h+o <= T := 325-2m.
```

For fixed `h`, the right-hand side is nondecreasing in the allowed integer `o>=0`. Hence, as `m` increases, `T` decreases and the witness upper bound cannot increase. The complete table at `m=157` already lies strictly below 157. Therefore the same argument excludes every `m>=157` at `Delta=13`.

Thus any graph with `m>=157` has `Delta in {14,15,16}`.

### 3.2 The edge count 157

The frozen n=25 candidate proof already excludes `m=157` in each of `Delta=14,15,16` by the residual finite argument. That part of the proof is retained unchanged.

### 3.3 Every larger edge count

For `m>=158`, the degree sum leaves only the finite ranges

```text
Delta=14: 158 <= m <= floor(25*14/2) = 175,
Delta=15: 158 <= m <= floor(25*15/2) = 187,
Delta=16: 158 <= m <= floor(25*16/2) = 200.
```

The exact Fan-free outer verifier scans **every integer edge count in all three ranges**. Its aggregate results are

| Delta | edge counts scanned | outer states | states surviving all outer necessary conditions |
|---:|---:|---:|---:|
| 14 | 158..175 | 128,666 | 0 |
| 15 | 158..187 | 88 | 0 |
| 16 | 158..200 | 0 | 0 |

Thus no graph with `m>=158` survives the necessary-condition relaxation.

Combining Sections 3.1-3.3 with the frozen exclusion of 157 gives, without Fan,

```text
e(G) <= 156.
```

The frozen equality argument at 156 is unchanged and forces `K(12,13)`.

## 4. n=27 without Fan

Again write `m=e(G)`.

### 4.1 Degree ranges outside Delta=15,16,17

If `Delta <= 13`, the degree sum gives

```text
2m <= 27*13 = 351,
```

hence `m <= 175`.

If `Delta >= 18`, the independent complement maximum-degree theorem already used in the frozen n=27 manuscript gives `m <= 181`; this step is independent of Fan.

For `Delta=14`, the witness-deficit inequality from Section 3 of the frozen n=27 proof is

```text
m <= C(h,2) + h(27-h) + o(o-1),
2h+o <= T := 378-2m.
```

As above, for fixed `h` the right-hand side is nondecreasing in `o`, while `T` decreases as `m` increases. The complete table at `m=183` lies strictly below 183, so the same witness argument excludes every `m>=183` at `Delta=14`.

Thus an above-target graph can only have `Delta in {15,16,17}`.

### 4.2 The edge count 183

The frozen n=27 candidate proof already excludes `m=183` for `Delta=15,16,17`. That proof component is retained unchanged.

### 4.3 Delta=16 and Delta=17 above 183

The Fan-free outer verifier scans every larger degree-sum-possible edge count:

| Delta | edge counts scanned | outer states | outer survivors |
|---:|---:|---:|---:|
| 16 | 184..216 | 8,880 | 0 |
| 17 | 184..229 | 0 | 0 |

Hence no larger graph occurs in these two degree bands.

### 4.4 Delta=15 above 183

For `Delta=15`, every integer `m=184,...,202` was scanned. The complete outer scan contains 2,858,079 states. Only 661 survive the outer necessary conditions:

```text
m=184: 772,670 outer states, 651 survivors;
m=185: 579,204 outer states, 10 survivors;
m>=186: zero outer survivors at every edge count through 202.
```

The 661 retained states were then passed through the same canonical residual-column and subset-capacity machinery used in the frozen n=27 proof.

At `m=184`:

```text
outer survivors:             651
canonical residual columns:  49,073
labelled orbit mass:          1,175,094
columns reaching subset flow:1
final column survivors:       0
```

At `m=185`:

```text
outer survivors:             10
canonical residual columns:  388
labelled orbit mass:          10,036
columns reaching subset flow:0
final column survivors:       0
```

The scan and replay modes agree exactly on the state count, canonical-column count, labelled orbit mass, survivor count and ordered per-column SHA-256 digest:

```text
m=184: 89e4e1d033ef0edd98aa557cb6df8d5fd2eea145b036c8604d0ac66c44f364be
m=185: 162403cef4b12375be6c442c91471fdd63aea9a2d3d04412ecc99f6ee723391f
```

The replay mode does not invoke max flow: it rederives the source caps and directly checks each recorded strict subset inequality.

Therefore every `m>=184` is impossible at `Delta=15`.

Combining Sections 4.1-4.4 with the frozen exclusion of 183 yields, without Fan,

```text
e(G) <= 182.
```

The frozen equality argument at 182 remains unchanged and forces `K(13,14)`.

## 5. Computational provenance

Primary Fan-free upper-range workflow:

```text
Fan-free n25/n27 upper-range scan
run 34393554788
head commit efe189ad911a3968e5b7d63a3de43a05c664bfb2
```

The six artifacts and their workflow-recorded SHA-256 digests are:

```text
fan-free-25-14  3f2e38c5d6cdf4895a77e3c9aaf2980ff2899a8565019af265264a7c18d9deb9
fan-free-25-15  17087194b6cb13720051e335847eb0c4819bdb171d4ece4f234ba3c776f32fba
fan-free-25-16  4e3c28d2a93798e8e307cffad14a0c02ab41b78f25e263481d8b9d20576e7c62
fan-free-27-15  03fbb10af9505fc4115a874cdba975e74eb8a8a5dbc5348c63919cf845aadf21
fan-free-27-16  96544a8f570cb54780e6496fac0411a035efc94e894e7abc4533d054f6d43178
fan-free-27-17  2130aca03ca9738531800698b6b5dfe34e30ff7e46c7a0f66d9b5dbc69b8f179
```

The only nonzero outer frontier, `n=27, Delta=15, m=184,185`, was closed by:

```text
Fan-free n27 delta15 column closure
run 34393710385
head commit 7cc1971604efdf8fea5ec11bbc3b8826868c55ff
```

Artifacts:

```text
fan-free-n27-d15-184  3cb20da5f70ece0990f665e4f6a35e13b5baaabdeb9b61cf37009af534ec63ac
fan-free-n27-d15-185  b9c2086cbc15f97ef61b494df340aaf9d04e543a123dfdd716d0c23ec76dbaa2
```

The source `fan_free_outer.cpp` is a count-only extraction of the already published fixed-order outer necessary conditions. The `m=184,185` closure deliberately reuses the frozen `survey.cpp` and `columns.cpp`, with `columns check` providing a second algorithmic route for the strict subset acceptance layer. All arithmetic is integer arithmetic.

## 6. Trust boundary and status

This removes Fan's 1987 theorem as a logical dependency of the **n=25 and n=27 fixed-order candidate proofs**. Fan remains cited because his theorem historically supplied the original reduction and is stronger than the order-specific replacement proved here.

This change does not remove the other published dependencies already disclosed in the fixed-order manuscripts, in particular the complement/total-domination reductions. Nor does it convert same-assistant computation into external review. The graph-to-residual lemmas remain hand mathematics and are still the main trust boundary.

The old Fan-based manuscripts, evidence packages and hashes remain preserved. Reviewer-facing v2 materials should identify this document as the replacement for the original Fan reduction and link the old versions as historical provenance.
