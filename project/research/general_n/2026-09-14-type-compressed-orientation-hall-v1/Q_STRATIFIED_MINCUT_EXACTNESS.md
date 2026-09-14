# q-stratified minimum-cut exactness

14 September 2026. **Candidate exact structural theorem for the current directed target-Hall model. External mathematical review and novelty assessment remain OPEN.**

This theorem resolves an important distinction exposed by the preserved q-stratified counterexample.

The q-only receiver rearrangement is **not pointwise exact**: for a fixed source set `S`, its upper bound `U_q(S)` can strictly exceed the exact receiver capacity `H(S)`. In particular the canonical maximal minimizer `M+` can have positive crossing statistic `C_q(M+)`.

Nevertheless, under the fixed-q target-cap monotonicity of the current post-pair model, the q-only rearrangement is exact **at the minimum Hall margin**:

```text
min_S [ H(S)-D(S) ]
=
min_S [ U_q(S)-D(S) ].                                (1)
```

Equivalently, an exact target-Hall failure exists if and only if a q-stratified receiver-layer failure exists for some source set.

This is stronger for minimum-cut purposes than proving `C_q(M+)=0`, and it does not contradict the preserved positive-`C_q` example.

## 1. Setup

For each labelled copy `w` write

```text
q_w,
c_w=q_w+rho_w,
P_w.
```

Assume

```text
c_w>=q_w,                                              (2)
```

and fixed-q target-cap monotonicity

```text
q_x=q_y,
c_x<=c_y
 => P_x<=P_y.                                         (3)
```

The directed compatibility relation is

```text
D(u,w)
 iff u!=w,
     q_u<=c_w+1,
     q_w<=c_u.                                        (4)
```

For a labelled source set `S`, define

```text
y_w(S)=#{u in S:D(u,w)},                              (5)

H(S)=sum_w min(P_w,y_w(S)),                           (6)

D(S)=sum_{u in S} q_u,                                (7)

F(S)=H(S)-D(S).                                       (8)
```

The q-only comonotone receiver upper bound is

```text
U_q(S)
 =sum_q sum_{k>=1} min(alpha_{q,k},beta_{q,k}),        (9)
```

where

```text
alpha_{q,k}=#{w:q_w=q, P_w>=k},
beta_{q,k}=#{w:q_w=q, y_w(S)>=k}.                     (10)
```

By rearrangement,

```text
U_q(S)>=H(S).                                         (11)
```

The audited crossing-gap identity gives

```text
U_q(S)-H(S)=C_q(S),                                   (12)
```

with

```text
C_q(S)=sum_{q,m} min(H^S_{q,m},L^O_{q,m}).            (13)
```

Thus `C_q(S)=0` if and only if the q-only receiver bound is exact at `S`.

## 2. Minimum-witness lattice

The Hall margin `F` is submodular, so its minimizers form a lattice under union and intersection. Let

```text
delta=min_S F(S),                                     (14)
```

and let

```text
M+=union of all minimizers.                           (15)
```

Then `M+` is the unique maximal minimizer. In particular,

```text
x notin M+
```

means that `x` belongs to **no** minimum Hall witness.

Because all quantities are integral, for any minimizer `S` and any `x notin M+`,

```text
F(S union {x})>=delta+1.                              (16)
```

## 3. Neutral deletion lemma

Let `S` be any minimum Hall witness contained in `M+`. Suppose there are distinct copies `x,y` such that

```text
x notin M+,
y in S,
q_x=q_y=q,
c_x<c_y,                                              (17)
```

and the selected target `y` has positive receiver slack:

```text
y_y(S)<P_y.                                           (18)
```

Then:

> **Neutral deletion lemma.**
>
> ```text
> F(S\{y})=F(S)=delta.                                (19)
> ```

### Proof

Put

```text
Z(S)={w:y_w(S)<P_w}.                                  (20)
```

Adding the exterior source `x` increases capped receiver capacity by exactly one on every target in

```text
N^+(x) cap Z(S),                                      (21)
```

and increases source demand by `q`. Since `x` lies in no minimizer, (16) gives

```text
|N^+(x) cap Z(S)|>=q+1.                               (22)
```

For deletion of `y`, put

```text
T(S)={w:y_w(S)<=P_w}.                                 (23)
```

Removing `y` decreases capped receiver capacity by exactly one on each target in

```text
N^+(y) cap T(S).                                      (24)
```

Since `S` is minimum,

```text
F(S\{y})-F(S)
 =q-|N^+(y) cap T(S)|
 >=0,                                                 (25)
```

so

```text
|N^+(y) cap T(S)|<=q.                                 (26)
```

Because `q_x=q_y=q` and `c_x<c_y`, numerical compatibility gives

```text
D(x,y)=1.                                             (27)
```

By (18), `y in Z(S)`, so

```text
y in N^+(x) cap Z(S).                                 (28)
```

For every third target `w`, source-neighborhood containment gives

```text
D(x,w)=>D(y,w).                                       (29)
```

Hence

```text
(N^+(x) cap Z(S))\{y}
 subseteq N^+(y) cap T(S).                            (30)
```

Combining (22), (26), and (30),

```text
q
 >= |N^+(y) cap T(S)|
 >= |N^+(x) cap Z(S)|-1
 >= q.                                                (31)
```

Equality holds throughout. Therefore

```text
|N^+(y) cap T(S)|=q,                                  (32)
```

and (25) is zero. This proves (19). QED.

The same argument also gives the double-tightness identities recorded in [`CROSSING_WALL_CHARGE_AND_TIGHTNESS.md`](CROSSING_WALL_CHARGE_AND_TIGHTNESS.md).

## 4. Every positive crossing supplies a deletable endpoint

Suppose `C_q(S)>0`. Then some equal-`(q,m)` crossing block contains

```text
x notin S with P_x<m,
y in S     with P_y>=m.                                (33)
```

For the selected endpoint,

```text
y_y(S)=m-1<P_y,                                      (34)
```

so `y` has the positive slack required by the neutral deletion lemma.

Also

```text
P_x<P_y.                                              (35)
```

By fixed-q monotonicity (3), (35) forces

```text
c_x<c_y.                                              (36)
```

Thus every positive crossing contains a pair with exactly the geometric ordering required by Section 3.

The only remaining issue is to know that the low endpoint `x` lies outside the original maximal minimizer `M+`, not merely outside the current reduced minimizer. The iterative construction below maintains precisely that invariant.

## 5. Crossing-removal algorithm

Start with

```text
S_0=M+.                                                (37)
```

If `C_q(S_t)=0`, stop. Otherwise choose any crossing block and one pair `(x,y)` as in (33), and set

```text
S_{t+1}=S_t\{y}.                                      (38)
```

We prove inductively that:

1. every `S_t` is a minimum Hall witness;
2. every removed vertex can never become a low crossing endpoint later;
3. therefore every low crossing endpoint encountered by the algorithm lies outside `M+`.

The first deletion has `x notin M+` automatically because `S_0=M+`, so Section 3 shows that `S_1` is minimum.

When `y` is removed from a crossing block, it satisfies

```text
P_y>=m_y(S_t).                                        (39)
```

Subsequent steps only delete sources. Therefore for every later set `S_j subseteq S_t`,

```text
m_y(S_j)<=m_y(S_t).                                   (40)
```

Combining (39)-(40),

```text
P_y>=m_y(S_j).                                        (41)
```

But a low unselected crossing endpoint must satisfy

```text
P_y<m_y(S_j).                                         (42)
```

So a previously removed vertex can never become a low endpoint.

Hence, at every later positive crossing, its low endpoint `x` was never removed. Since `x notin S_t subseteq M+`, this implies

```text
x notin M+.                                           (43)
```

The neutral deletion lemma therefore applies again, so `S_{t+1}` is minimum.

Each step deletes one source, so the process terminates after finitely many steps at a minimum witness `S*` with

```text
C_q(S*)=0.                                            (44)
```

This proves:

> **Crossing-free minimum-witness theorem.** Every instance satisfying (2)-(4) has at least one minimum Hall witness `S*` for which the q-only rearrangement is exact:
>
> ```text
> U_q(S*)=H(S*).                                      (45)
> ```

## 6. q-stratified minimum-cut exactness

Let

```text
G_q(S)=U_q(S)-D(S).                                   (46)
```

Since `U_q(S)>=H(S)` pointwise,

```text
G_q(S)>=F(S)                                          (47)
```

for every source set. Therefore

```text
min_S G_q(S)>=min_S F(S)=delta.                       (48)
```

But Section 5 supplies a minimum Hall witness `S*` with `U_q(S*)=H(S*)`. Hence

```text
G_q(S*)=F(S*)=delta,                                  (49)
```

so

> **q-stratified minimum-cut exactness.**
>
> ```text
> min_S [U_q(S)-D(S)]
> =min_S [H(S)-D(S)].                                 (50)
> ```

In particular,

```text
exists S: H(S)<D(S)
iff
exists S: U_q(S)<D(S).                                (51)
```

Thus q-only receiver stratification is an exact detector of target-Hall failure **after minimization**, despite not being pointwise exact.

## 7. Why the preserved counterexample is not a contradiction

The five-copy counterexample has canonical maximal minimizer

```text
M+={A,B1,B2,B3}
```

with

```text
F(M+)=-1,
C_q(M+)=1,
G_q(M+)=0.                                            (52)
```

So q-only rearrangement genuinely misses the failure at `M+`.

The crossing endpoint `A` is neutral-deletable. Removing it gives

```text
S*={B1,B2,B3},                                        (53)
```

which is the other minimum witness. There

```text
F(S*)=-1,
C_q(S*)=0,
G_q(S*)=-1.                                           (54)
```

The counterexample therefore demonstrates exactly the distinction proved here:

```text
pointwise q-exactness: false,
minimum-cut q-exactness: true.                        (55)
```

## 8. Finite verification

[`verify_q_stratified_mincut_exactness.py`](verify_q_stratified_mincut_exactness.py) independently enumerates every labelled source subset, compares the exact and q-stratified minimum margins, and replays the crossing-removal algorithm.

The frozen local verification record [`Q_STRATIFIED_MINCUT_EXACTNESS_VERIFICATION.json`](Q_STRATIFIED_MINCUT_EXACTNESS_VERIFICATION.json) reports:

```text
exhaustive labelled profiles:              4,992
exhaustive n:                              1..4
exhaustive q values:                       0,1
exhaustive rho values:                     0,1
exhaustive P values:                       0,1,2
exhaustive profiles with C_q(M+)>0:          177
exhaustive neutral deletions:                204

random trials:                           30,000
random maximum n:                            8
random profiles with C_q(M+)>0:              145
random neutral deletions:                    147

preserved hostile counterexample:           PASS
result:                                      PASS
```

The exhaustive phase filters to exactly the fixed-q monotone cap assignments required by (3). The random phase uses a deterministic seed and larger monotone-cap profiles.

This finite testing is deliberately rich in positive-crossing maximal minimizers; it is not merely replaying the zero-crossing Murty pilot.

## 9. Relation to the frozen Murty pilot

GitHub Actions run `34859094097` found the stronger empirical property

```text
C_q(M+)=0
```

for all `205,919` target-Hall failures in the frozen 15-state pilot. That remains useful reconnaissance, but theorem (50) shows that proving this stronger **maximal-witness** property is unnecessary for exact q-stratified detection.

Even if future Murty profiles have `C_q(M+)>0`, the crossing-removal theorem supplies another minimum witness at which the q-only capacity is exact.

## 10. Research consequence

The all-order target can now skip the attempted Murty-specific proof

```text
C_q(M+)=0.                                            (56)
```

The exact target-Hall obstruction may instead be studied as

```text
min_S [U_q(S)-D(S)]<0,                                (57)
```

where receiver capacity is represented only by q-stratified one-dimensional layer counts.

The next hand-proof problem is therefore to control the q-stratified layer quantities

```text
alpha_{q,k}, beta_{q,k}                               (58)
```

at a crossing-free minimum witness, using the canonical Murty constraints (`q+rho<=a`, residual budget, selected-excess budget, potential-pair capacity and source-demand forcing).

This is a materially simpler target than controlling arbitrary target correlation or proving pointwise q-only exactness.

## 11. Trust boundary

The proof uses:

- the exact crossing-gap identity;
- fixed-q target-cap monotonicity in the current post-pair model;
- the directed compatibility relation and equal-q source-neighborhood containment;
- submodularity/lattice closure of Hall minimizers;
- integrality of the Hall margin.

Its Murty-Simon application inherits the canonical graph-to-constraint bridge and the validity of the current target caps. It is an exact theorem about the target-Hall relaxation, not a proof of graph realizability and not a proof of the unrestricted Murty-Simon conjecture.

External mathematical review and genuinely independent reproduction remain open.
