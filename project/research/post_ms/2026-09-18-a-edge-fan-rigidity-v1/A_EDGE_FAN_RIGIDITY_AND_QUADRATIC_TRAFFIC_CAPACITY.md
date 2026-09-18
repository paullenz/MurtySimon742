# A-edge fan rigidity and quadratic traffic capacity

Date: 2026-09-18

Status: internal structural theorem package for the eventual / sufficiently-large second-extremal diameter-2-critical programme. The target remains the eventual problem around

`M(n)=floor((n-1)^2/4)+1`.

The published 2024 order-12, size-32 D2C graph `X_3` remains a mandatory negative control. Nothing below suppresses it. No all-order or eventual second-extremal theorem is claimed.

## 1. Setup and reason for the move

Work in the live near-full partial-Boolean branch around a maximum-degree root `v`:

- `B=N(v)`, `A=V\N[v]`;
- `p` tight antipode pairs in `B`, unmatched set `U`, `u=|U|`;
- `a=|A|=2p+u-lambda-1`;
- `V_0=|A union U|=a+u=2p+2u-lambda-1`;
- `T=a-p=p+u-lambda-1`;
- `epsilon_z=b-d(z)`;
- `L_A=sum_{x in A} epsilon_x`;
- `E_U=sum_{y in U} epsilon_y`;
- `S=E_U+L_A`.

For a Boolean code `c`, write

- `A_c={x in A:c(x)=c}`, `n_c=|A_c|`;
- `V_c=(A union U)_c`, `N_c=|V_c|`;
- `L_c=sum_{x in A_c}epsilon_x`;
- `S_c=sum_{z in V_c}epsilon_z`.

The preceding checkpoint established the exact rooted-transfer lower bound

`f=e(G[A]) >= F_min`

for every above-`M(n)` candidate, together with a complete three-channel upper accounting of A-edges: direct edges, matched-B certificates, and A/U unique-common-neighbour certificates.

The coarse consequence was a macroscopic Boolean code class. The present note goes one level deeper: instead of only counting source/witness pairs, it uses the geometry of all certificates sharing one A-source. Two different fan types appear, and both are rigid.

## 2. Direct A-edge fans are near false-twin stars

Call `xy in E(G[A])` **direct** when

`N(x) intersect N(y)=empty`.

The preserved direct-edge theorem says `c(y)=bar(c(x))` and, for `lambda>=0`,

`epsilon_x+epsilon_y>=lambda+1`.

Fix `x in A` and let

`D_x={y in A: xy is direct}`,

`d_x=|D_x|`.

### Lemma 2.1 — direct-fan independence

`D_x` is an independent set.

Proof. If `y,y' in D_x` are distinct, then `y' in N(x)`. Directness of `xy` says `N(x) intersect N(y)=empty`, so `y' notin N(y)`. Hence `yy'` is not an edge. square

Thus every direct fan is a star whose leaves all have the same complementary Boolean code and are pairwise nonadjacent.

### Lemma 2.2 — exact direct-fan hole representation

Put

`W_x=(V(G)\{v})\N(x)`.

For each `y in D_x`, define

`H_x(y)=W_x\N(y)`.

Then

`N(y)=W_x\H_x(y)`

and

`|H_x(y)|=epsilon_x+epsilon_y-(lambda+1)`.               `(DFH)`

Consequently, for `y,y' in D_x`,

`|N(y) triangle N(y')| <= |H_x(y)|+|H_x(y')|`.           `(DFT)`

Proof. Since `xy` is direct, `N(y)` is disjoint from `N(x)`; since `y in A`, it is also disjoint from `{v}`. Hence `N(y) subseteq W_x`. Also

`|W_x|=n-1-d(x)`.

Using `n=2b-lambda`, `d(x)=b-epsilon_x`, and `d(y)=b-epsilon_y`,

`|W_x|-|N(y)|=epsilon_x+epsilon_y-(lambda+1)`.

The symmetric-difference bound follows because both neighbourhoods are complements of their hole sets inside the same `W_x`. square

### Corollary 2.3 — exact equality model

If every `y in D_x` satisfies

`epsilon_x+epsilon_y=lambda+1`,

then all vertices of `D_x` are false twins:

`N(y)=W_x` for every `y in D_x`.

Thus the zero-surplus direct fan is not merely sparse; it is an exact complete-bipartite-type false-twin block. This is the direct-edge analogue of the projective equality structures encountered elsewhere in the programme.

### Lemma 2.4 — direct-fan slack threshold

For every `y in D_x`,

`epsilon_y >= d_x-T`.

Therefore

`L_A >= d_x(d_x-T)_+`.                                   `(DFS)`

Proof. By Lemma 2.1, `y` has no neighbours in `D_x\{y}`. The coded layer `A union U` has size `V_0`, so `y` has at most `V_0-d_x` coded-layer neighbours. But an A-vertex has exactly

`d_{A union U}(y)=p+u-epsilon_y`.

Thus

`p+u-epsilon_y <= V_0-d_x`,

which is equivalent to `epsilon_y>=d_x-T`. Sum over the `d_x` leaves and take the positive part. square

Define

`R_D(T,L)=floor((T+sqrt(T^2+4L))/2)`.

Then every direct fan satisfies

`d_x<=R_D(T,L_A)`,

and if `D` is the total number of direct A-edges,

`D<=a R_D(T,L_A)/2`.                                    `(DFC)`

## 3. A/U certificate fans contain an induced matching cut

Now fix one A-source `x` and consider the chosen A/U unique-common-neighbour certificates attached to A-edges oriented out of `x`.

For each such edge `xh`, let `w` be its chosen A/U witness, so

`N(x) intersect N(w)={h}`.

Let

- `H_x` be the set of certified heads `h`;
- `W_x` be the set of chosen witnesses `w`;
- `d_x=|H_x|=|W_x|`.

The equality of the two cardinalities is exact: different certified edges have different heads, and a fixed source-witness pair can certify at most one head, so the chosen witnesses are distinct.

All witnesses in `W_x` have Boolean code `bar(c(x))`.

### Lemma 3.1 — induced matching cut

There is a canonical bijection `h_i <-> w_i` such that the only edges between `H_x` and `W_x` are the matched pairs

`h_i w_i`.

Equivalently,

`G[H_x,W_x]` is exactly a matching of size `d_x`.          `(IMC)`

Proof. By definition `w_i` is adjacent to its head `h_i`. If `j!=i`, then `h_j in N(x)`. Since

`N(x) intersect N(w_i)={h_i}`,

`w_i` cannot be adjacent to `h_j`. square

Thus one high-outdegree source creates a rigid two-layer object: `x` is adjacent to every head and to no witness, while the head-witness cross graph is an induced matching.

### Lemma 3.2 — witness-fan missing-edge payment

For `w in W_x`, let

`h(x,w)=epsilon_x+epsilon_w-(lambda+1)`.

Then

`d_{overline{G[W_x]}}(w) <= h(x,w)`.

Consequently

`2 e(overline{G[W_x]})`
` <= d_x epsilon_x + sum_{w in W_x}epsilon_w`
`    -d_x(lambda+1)`.                                    `(WFD)`

Proof. Every other witness `w' in W_x` is nonadjacent to `x`. If also `ww'` is a nonedge, then `w'` is adjacent to neither `x` nor `w`. It is therefore one of the external holes of the unique-common-neighbour pair `(x,w)`. The exact hole count is `epsilon_x+epsilon_w-(lambda+1)`. Sum over `w`. square

Hence low-slack A/U fans force their witnesses, all of one Boolean code, to form a near-clique.

### Lemma 3.3 — A/U fan slack threshold

Every head `h in H_x` satisfies

`epsilon_h>=d_x-T`.

Every witness `w in W_x` satisfies

`epsilon_w>=d_x-T`;

if `w in A`, the stronger `epsilon_w>=d_x-T+1` holds.

Since `H_x` and `W_x` are disjoint,

`S >= 2d_x(d_x-T)_+`.                                   `(AUFS)`

Proof. A head `h_i` is nonadjacent to the other `d_x-1` witnesses. Hence it has at most `V_0-d_x` coded-layer neighbours. Since `h_i in A`,

`p+u-epsilon_{h_i}<=V_0-d_x`,

which gives `epsilon_{h_i}>=d_x-T`.

A witness `w_i` is nonadjacent to `x` and to the other `d_x-1` heads, so it has at most `V_0-1-d_x` coded-layer neighbours. If `w_i in A`, use `d_{A union U}(w_i)=p+u-epsilon_{w_i}`; if `w_i in U`, use `d_{A union U}(w_i)=p+u-1-epsilon_{w_i}`. These give the stated bounds. Finally `H_x cap W_x=empty` because heads are adjacent to `x` and witnesses are not. square

Define

`R_C(T,S)=floor((T+sqrt(T^2+2S))/2)`.

Then every A/U certificate fan satisfies

`d_x<=R_C(T,S)`.                                         `(AUFC)`

If `C` is the total number of chosen A/U certificates over all A-sources,

`C<=a R_C(T,S)`.                                         `(AUFC2)`

## 4. Fan-square capacity for the A/U channel

The preceding maximum-fan bound is useful when one source is very heavily loaded. A second theorem prices diffuse quadratic traffic.

Fix a code `c`. For `z in A_c`, let `W_z` be its chosen A/U witness fan and put `d_z=|W_z|`. Let

`C_c=sum_{z in A_c}d_z`.

The preserved weighted A/U capacity is

`(lambda+1)C_c <= N_bar(c)L_c+n_c S_bar(c)`.             `(AUC)`

Define its nonnegative surplus

`M_c:=N_bar(c)L_c+n_cS_bar(c)-(lambda+1)C_c`.

Summing `(WFD)` over all sources of code `c` gives

`2 sum_{z in A_c} e(overline{G[W_z]}) <= M_c`.           `(FMS)`

Indeed, each source occurs with at most `N_bar(c)` distinct witnesses and each witness with at most `n_c` sources.

On the other hand

`sum_z e(G[W_z]) <= n_c e(G[V_bar(c)])`,

because a fixed same-code witness edge can occur in at most all `n_c` source fans. The preserved same-code weighted edge capacity gives

`(lambda+1)e(G[V_bar(c)])`
` <= N_c S_bar(c)+N_bar(c)S_c`.                          `(SCE)`

Since

`sum_z binom(d_z,2)`
` =sum_z e(G[W_z])+sum_z e(overline{G[W_z]})`

and

`sum_z d_z^2 >= C_c^2/n_c`,

we obtain the following new traffic inequality.

### Theorem 4.1 — directed fan-square inequality

For `n_c>0`,

`C_c^2/n_c + lambda C_c`
` <= [2n_c/(lambda+1)]`
`      [N_c S_bar(c)+N_bar(c)S_c]`
`    +N_bar(c)L_c+n_cS_bar(c)`.                          `(FS-c)`

If `n_c=0`, then `C_c=0` and the statement is void.

This adds a genuine quadratic penalty in directed A/U traffic; it is not present in the older linear source-witness capacity.

### Corollary 4.2 — complementary-pair fan-square inequality

For an unordered complementary pair `P={c,bar c}`, put

- `C_P=C_c+C_bar(c)`;
- `A_P=n_c+n_bar(c)`;
- `L_P=max(N_c,N_bar(c))`;
- `W_P=max(N_c+n_c,N_bar(c)+n_bar(c))`;
- `S_P=S_c+S_bar(c)`.

Then

`C_P^2/A_P + lambda C_P`
` <= [2A_P L_P/(lambda+1)+W_P] S_P`.                    `(FS-P)`

The zero-denominator convention is harmless: if `A_P=0`, then `C_P=0`.

Proof. Add `(FS-c)` in the two directions. The fractional terms combine as

`[2A_P/(lambda+1)]`
` [N_bar(c)S_c+N_cS_bar(c)]`
` <= [2A_P L_P/(lambda+1)]S_P`.

The remaining terms are at most

`W_P S_P`.

Finally use

`C_c^2/n_c+C_bar(c)^2/n_bar(c)>=C_P^2/A_P`.

### Corollary 4.3 — distribution-free global quadratic A/U cap

Let

`C=sum_P C_P`

be the total chosen A/U certificate traffic. Since the complementary pairs partition `A` and `A union U`,

`sum_P A_P=a`.

Define

`K_0=2aV_0/(lambda+1)+a+V_0`.

Then

`C^2/a + lambda C <= K_0 S`.                             `(GFS)`

Hence

`C <= C_fan:=`
` (-a lambda+sqrt(a^2 lambda^2+4aK_0S))/2`.             `(GFC)`

This is a parameter-only quadratic cap for the A/U criticality channel. It is independent of `mu_A`, `mu_V`, or a chosen cylinder class.

## 5. Global A-edge fan-feasibility theorem

Let

- `D` be the number of direct A-edges;
- `P` the number of chosen matched-B certificates;
- `C` the number of chosen A/U certificates.

The channel decomposition is exact:

`f=D+P+C`.

The preserved matched-B theorem gives

`P<=sigma_0 a`.

Together with `(DFC)` and `(AUFC2)` this gives:

### Theorem 5.1 — finite fan-feasibility cap

`f <= a[ sigma_0 + R_D(T,L_A)/2 + R_C(T,S) ]`.          `(FFC)`

A stronger hybrid replaces the last term by the smaller of the maximum-fan and fan-square caps:

`f <= sigma_0 a`
`   + a R_D(T,L_A)/2`
`   + min{aR_C(T,S), C_fan}`.                            `(HFFC)`

For an above-`M(n)` candidate, the rooted-transfer theorem therefore imposes

`F_min <= sigma_0 a`
`       + a R_D(T,L_A)/2`
`       + min{aR_C(T,S), C_fan}`.                        `(RTF)`

Using `L_A<=S<=C_0` and `sigma_0<=R_A(C_0)` produces a fully parameter-only necessary condition if desired. The code-resolved and actual-slack versions are preferable when available.

## 6. Structural dichotomy forced by rooted transfer

The real value of `(RTF)` is structural rather than numerical.

Put

`H=(F_min-sigma_0a)_+`.

Then `D+C>=H`. Consequently at least one of the following holds:

1. **direct-fan branch:** `D>=H/2`, hence some `x in A` has

   `d_D(x)>=H/a`;

   its direct neighbours form an independent complementary-code class whose neighbourhoods differ only through the exact hole sets `(DFH)`;

2. **A/U-fan branch:** `C>=H/2`, hence some A-source has at least `H/(2a)` distinct complementary-code witnesses and distinct A-heads; the head-witness cross graph is an induced matching, while low hole surplus forces the witness side towards a same-code clique by `(WFD)`.

Thus the previous coarse “macroscopic code class” frontier can be sharpened to a **macroscopic fan geometry**: large rooted-triangle transfer cannot be absorbed by anonymous code multiplicity. It must produce either a near-false-twin direct star or an induced-matching A/U fan, unless the matched-B channel already pays through `sigma_0`.

This is a more concrete target for stability/classification than the bare size of a Boolean code class.

## 7. Mandatory negative control

For the published `X_3` graph,

`p=4`, `u=0`, `lambda=4`, `a=3`, `f=0`, `F_min=0`.

Thus `(FTR)` places no positive A-edge demand on `X_3`, and every fan theorem above is vacuous. The order-12, size-32 exception remains explicitly allowed.

## 8. Independent audit and trust boundary

The generic D2C fan geometry was independently replayed on all 21 graph-atlas D2C isomorphism classes through order seven, over every maximum-degree root:

- 43 nonempty direct fans;
- 48 direct fan incidences;
- 5 pairs of leaves inside direct fans;
- 48 exact direct-hole identities;
- 101 external unique-common-neighbour source/witness pairs;
- 36 two-certificate fan-pair tests with distinct heads;
- 19 nonadjacent witness-pair hole tests;
- failures: 0.

The audit checks the graph-theoretic kernels: direct-fan independence and hole representation, unique-common-neighbour hole counts, and the off-diagonal induced-matching rule. It does not replace the hand proofs and does not by itself certify the partial-Boolean degree formulas.

Promoted internally:

- `(DFH)/(DFT)/(DFS)` direct-fan near-false-twin and slack theorems;
- `(IMC)/(WFD)/(AUFS)` A/U induced-matching fan geometry;
- `(FS-c)/(FS-P)/(GFS)` quadratic A/U traffic capacity;
- `(FFC)/(HFFC)/(RTF)` global A-edge fan-feasibility consequences.

Not claimed:

- an eventual second-extremal theorem;
- an exclusion of the published `X_3` graph;
- a proof that either fan equality model is globally realizable;
- a closure of the separate `Q=0` / false-twin-core branch.

## 9. Next move

The highest-value next theorem is a stability/classification result for the two fan equality models.

- In the direct branch, many low-hole leaves of one centre are near false twins. The exact zero-hole case is a complete-bipartite-type block. The target is to show that a triangle-containing near-full graph cannot sustain a linear direct fan with sublinear total hole mass unless the graph collapses into the already-separated false-twin/bipartite regime.
- In the A/U branch, a linear fan gives an induced matching `H_x--W_x`, with `W_x` same-code and near-clique when the hole surplus is small. The target is to combine this matching cut with the same-code edge payment and rooted triangle count `Q`.

This keeps the attack on one coherent structural object rather than returning to numerical constant optimization.