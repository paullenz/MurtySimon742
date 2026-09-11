---
title: "The Murty-Simon bound at order 29"
subtitle: "Reviewer-v4 hand-reduced candidate proof"
author: "Paul Lenz"
date: "11 September 2026"
geometry: margin=27mm
fontsize: 11pt
header-includes:
  - \usepackage{amsmath,amssymb,mathtools,booktabs,microtype}
  - \setlength{\emergencystretch}{2em}
---
# Murty-Simon at n=29: reviewer-v4 candidate proof

11 September 2026. Research directed by Paul Lenz; mathematical development, implementation and internal checking by ChatGPT/Geeps.

**Status: serious candidate proof. Independent mathematical review, novelty assessment and independent computational reproduction remain OPEN.** Reviewer-v4 replaces the proof-critical Delta=16 computation of reviewer-v3 by a hand threshold-tail argument. Historical editions, computations, bugs and audits remain preserved unchanged.

## 1. Candidate statement

Let G be a simple diameter-two edge-critical graph on 29 vertices. The candidate statement is

$$
e(G)\le 210=\left\lfloor\frac{29^2}{4}\right\rfloor,
$$

with equality if and only if

$$
G\cong K_{14,15}.
$$

A bipartite graph of diameter two is complete bipartite, so the bipartite case is immediate. For the non-bipartite dense case, the published Dailly-Foucaud-Hansberg dominating-edge theorem gives at most 208 edges when a dominating edge exists (apart from its order-six exception). Hence any counterexample at 210 or more edges has no dominating edge. A universal vertex gives a star and is sparse.

## 2. Delta=15 and the equality graph

A direct witness is an edge uv whose endpoints have no common neighbour. A two-step witness is a nonedge uv whose endpoints have exactly one common neighbour. Every critical edge is covered by one such witness. A direct witness covers one edge; a two-step witness covers at most the two edges of its unique length-two path.

Because there is no dominating edge, every witness pair uv satisfies

$$
d(u)+d(v)\le 28. \tag{2.1}
$$

Assume Delta=15. Put

$$
\varepsilon_x=15-d(x),\qquad
L=\{x:\varepsilon_x\ge2\},\qquad
O=\{x:\varepsilon_x=1\}.
$$

Let h=|L|, o=|O|, and

$$
T=29\cdot15-2e(G).
$$

Every witness has deficit sum at least two, so

$$
2h+o\le T. \tag{2.2}
$$

Count all edges incident with L directly. An edge entirely outside L is witnessed either by an O-O witness, of capacity at most two, or by a missing L-X pair, of capacity at most one. Hence

$$
e(G)\le \binom h2+h(29-h)+o(o-1). \tag{2.3}
$$

At e(G)=211, T=13. The maximum right sides of (2.3) for h=0,...,6 are

```text
156, 138, 127, 123, 126, 136, 153,
```

all below 211. Thus Delta=15 is impossible at 211 and therefore at every larger edge count.

At e(G)=210, T=15. The corresponding maxima are

```text
210, 184, 165, 153, 148, 150, 159, 175.
```

Equality forces h=0 and o=15. All witnesses then lie inside O. Separating direct O-edges from two-step O-nonedges,

$$
210\le e(G[O])+2\left(\binom{15}{2}-e(G[O])\right)=210-e(G[O]),
$$

so O is independent. Its 15 vertices each have degree 14 and therefore meet all 14 vertices outside O. These 210 cross edges exhaust the graph. Hence

$$
G=K_{15,14}. \tag{2.4}
$$

## 3. The Delta=16 bridge

Put $H=\overline G$, choose a minimum-degree vertex $v$ of $H$, and set

```text
A=N_H(v),          |A|=a=12,
B=V(H)\N_H[v],     |B|=b=16.
```

Let $C=H[A]$, and let $F$ be the complement of $C$ on $A$; write $d_i=d_F(i)$. For every missing unordered $B$-pair choose exactly one cross quasi-edge representative `ui->w`, with exception $w$ in $B$. Call these cross-edges selected and all other existing $A$-$B$ edges residual. For $i\in A$, let $R_i$ be its residual degree into $B$ and set

$$
s_i=\max(0,d_i-R_i),\qquad S=\sum_i s_i.
$$

For $u\in B$ let $\rho_u$ be its residual $A$-degree and put $r=\sum_u\rho_u$. Finally set

$$
t=e(G)-208.
$$

The self-contained graph-to-model bridge is preserved at

`project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md`.

Reviewer-v4 uses only the following consequences of that bridge:

1. **Exact ledger and demand:**
   $$
   S\ge r+2t. \tag{3.1}
   $$
2. **Residual activity:** if t>0, then
   $$
   \rho_u\ge1\qquad(u\in B). \tag{3.2}
   $$
3. **Selected-incidence forcing:** at every selected incidence carrying label i,
   $$
   s_i\le \rho_u. \tag{3.3}
   $$
4. **Selected-source capacity:** a selected source has at least one selected edge, so
   $$
   \rho_u\le a-1=11. \tag{3.4}
   $$
   Consequently every positive demand satisfies 1<=s_i<=11.
5. **Threshold capacity:** for h>=2, with
   $$
   W_h=\sum_{i:s_i\ge h}s_i,
   \qquad z_h=|\{u\in B:\rho_u\ge h\}|,
   $$
   one has, whenever W_h>0,
   $$
   z_h\ge h,
   \qquad
   2W_h\le z_h^2-z_h+h(h+1). \tag{3.5}
   $$

The threshold-capacity proof had a non-blocking sign/order typo in an earlier explanatory sentence; the corrected identity is recorded in the historical lemma and is the direction used in (3.5). No numerical result changed.

Crucially, reviewer-v4 does **not** use the charging inequality, isolated-C lemma, residual-row enumeration, grouped LP or Farkas certificates in the Delta=16 branch.

## 4. Convert threshold capacity to a demand-only inequality

For h>=2 define

$$
g_h(W)=
\begin{cases}
0,&W=0,\\
\min\{z\in\{h,\ldots,16\}:2W\le z^2-z+h(h+1)\},&W>0.
\end{cases}
\tag{4.1}
$$

If the set in (4.1) is empty, the demand vector is already impossible. Otherwise (3.5) gives z_h>=g_h(W_h).

Because every rho_u>=1 when t>0 and rho_u<=12,

$$
r=16+\sum_{h=2}^{12}z_h
 \ge16+\sum_{h=2}^{11}g_h(W_h). \tag{4.2}
$$

Combining (3.1) and (4.2), every positive-surplus Delta=16 graph satisfies

$$
Q(s):=S-\sum_{h=2}^{11}g_h(W_h)\ge16+2t. \tag{4.3}
$$

The residual degree sequence has disappeared.

## 5. Hand threshold-tail lemma: Q(s)<=18

Let

$$
N_h=|\{i:s_i\ge h\}|,
\qquad p=N_1,
\qquad d_h=N_h-g_h(W_h),
$$

and

$$
D(s)=\sum_{h=2}^{11}d_h.
$$

The Ferrers-tail identity gives

$$
S=p+\sum_{h=2}^{11}N_h,
$$

and hence

$$
Q(s)=p+D(s). \tag{5.1}
$$

Since p<=12, it suffices to prove D(s)<=6. Write

$$
C_h(z)=\frac{z(z-1)+h(h+1)}2.
$$

### 5.1 Levels h>=7 are nonpositive

Fix h>=7 and N=N_h. If N=0 then d_h=0; if 0<N<h then g_h>=h>N and d_h<0. If N>=h, W_h>=hN. Were g_h<=N-1, then hN<=C_h(N-1). Write N=h+e. Since N<=12,

$$
0\le e\le12-h\le5.
$$

Twice the difference is

$$
2hN-[(N-1)(N-2)+h(h+1)]
=-e^2+3e+2h-2. \tag{5.2}
$$

This concave quadratic is positive at both endpoints e=0 and e=5 (the latter gives at least 2), contradiction. Thus g_h>=N_h and

$$
d_h\le0\qquad(h\ge7). \tag{5.3}
$$

Therefore clipping every demand above 6 down to 6 cannot decrease D: for h<=6, N_h is unchanged and W_h decreases; for h>=7, the new deficit is zero while the old one was nonpositive.

### 5.2 Clip 6 to 5

Assume max s_i<=6 and let k=N_6. For k<=10, g_6(6k)>=k, hence d_6<=0. For k<6 this is immediate from g_6>=6; for 6<=k<=10, testing z=k-1 gives

$$
12k-[(k-1)(k-2)+42]=-e^2+3e+10>0,
$$

where e=k-6 in {0,1,2,3,4}.

Only k=11,12 can have positive d_6, and in both cases d_6=1. If k=11, let l be 1 when the remaining demand is five and 0 otherwise. At h=5,

```text
before: W_5=66+5l,
after:  W'_5=55+5l.
```

Using C_5(10)=60, C_5(11)=70, C_5(12)=81, g_5 drops by at least one. If k=12, W_5 drops from 72 to 60 and g_5 drops from 12 to 10. Thus clipping 6->5 cannot decrease D.

### 5.3 Clip 5 to 4

Assume max s_i<=5 and let k=N_5. For k<=9, d_5<=0; for 5<=k<=9 this follows from

$$
10k-[(k-1)(k-2)+30]=-e^2+3e+8>0,
$$

with e=k-5 in {0,1,2,3,4}.

For k=10,11, d_5=1. Let l be the number of fours among the remaining entries. At h=4 the complete possibilities are

```text
(k,l)   W_4 -> W'_4     g_4 -> g'_4
(10,0)   50 -> 40        10 -> 9
(10,1)   54 -> 44        10 -> 9
(10,2)   58 -> 48        11 ->10
(11,0)   55 -> 44        10 -> 9
(11,1)   59 -> 48        11 ->10
```

so the lower-level gain pays for d_5. If k=12, the vector is (5^12), for which directly

$$
D(5^{12})=(12-12)+(12-11)+(12-11)+(12-10)=4\le6.
$$

Thus every remaining vector either already satisfies the target or can be clipped 5->4 without decreasing D.

### 5.4 Clip 4 to 3

Assume max s_i<=4 and let k=N_4. For k<=8, d_4<=0; for 4<=k<=8 this follows from

$$
8k-[(k-1)(k-2)+20]=-e^2+3e+6>0,
$$

with e=k-4 in {0,1,2,3,4}.

For k=9,10, d_4=1; checking the at most four possible numbers l of remaining threes shows g_3 drops by at least one under 4->3. For k=11, d_4=2: if the remaining entry is at most two, g_3 drops by two; if it is three, the change (3,4^11)->(3^12) drops g_3 by one and g_2 by one. For k=12, (4^12)->(3^12) likewise drops g_3 and g_2 by one each, paying for d_4=2.

Hence it remains only to treat demands in {0,1,2,3}.

### 5.5 Final two-level inequality

Put

$$
x=N_2,\qquad y=N_3,\qquad 0\le y\le x\le12.
$$

Then

$$
W_2=2x+y,\qquad W_3=3y,
$$

and

$$
D=x+y-g_2(2x+y)-g_3(3y). \tag{5.4}
$$

If 0<=y<=6, then

$$
x-g_2(2x+y)\le5,
\qquad y-g_3(3y)\le0,
$$

so D<=5. For x>=8, the first inequality follows because capacity at z=x-6 is too small:

$$
2x-C_2(x-6)=\frac{-x^2+17x-48}{2}>0;
$$

the smaller x cases follow from g_2>=2. The y inequality is immediate for y<=3 and for 4<=y<=6 follows from

$$
3y-C_3(y-1)=\frac{-y^2+9y-14}{2}>0.
$$

If 7<=y<=10, then

$$
y-g_3(3y)\le2
$$

because

$$
3y-C_3(y-3)=\frac{-y^2+13y-24}{2}>0.
$$

Also

$$
x-g_2(2x+y)\le4,
$$

because capacity at z=x-5 is too small:

$$
(2x+y)-C_2(x-5)
=\frac{-x^2+15x+2y-36}{2}
\ge\frac{-x^2+15x-22}{2}>0
$$

for 7<=x<=12. Hence D<=6.

Finally, if 11<=y<=12, then

$$
y-g_3(3y)\le3
$$

because

$$
3y-C_3(y-4)=\frac{-y^2+15y-32}{2}>0.
$$

Since y<=x<=12, x is 11 or 12, and

$$
x-g_2(2x+y)\le3
$$

because

$$
(2x+y)-C_2(x-4)
=\frac{-x^2+13x+2y-26}{2}
\ge\frac{-x^2+13x-4}{2}>0.
$$

Thus D<=6 in all cases. From (5.1),

$$
\boxed{Q(s)\le18}. \tag{5.5}
$$

A small exact integer checker independently regression-tests the clipping endpoint tables and the final 91 (x,y) pairs, while a separate historical checker exhausts all 1,352,078 nondecreasing 12-demand multisets. Both agree with (5.5), but neither computation is a logical premise of reviewer-v4.

## 6. Consequence: all dense Delta=16 cases disappear

From (4.3) and (5.5),

$$
16+2t\le18,
$$

so

$$
t\le1. \tag{6.1}
$$

But e(G)>=210 means t=e(G)-208>=2. Therefore

$$
\boxed{\Delta=16\text{ is impossible for every }e(G)\ge210.} \tag{6.2}
$$

This single hand argument replaces the entire proof-critical Delta=16 finite stack in reviewer-v3: demand enumeration, residual-row enumeration, Hall pruning, supplement refinement, corrected grouped LP and exact Farkas certificates. Those artifacts remain preserved as independent computational corroboration and audit history.

## 7. Delta=17

For Delta=17, a=11. The bridge charging inequality requires

$$
17+2t\le\sum_{i=1}^{11}\frac{s_i(12-2s_i)}{11-s_i}.
$$

For every integer 0<=s<=10,

$$
\frac{s(12-2s)}{11-s}\le\frac{16}{7},
$$

since

$$
\frac{16}{7}-\frac{s(12-2s)}{11-s}
=\frac{2(s-4)(7s-22)}{7(11-s)}\ge0.
$$

Thus the right side is at most 176/7<29. At 210 edges the required left side is already 29 and increases with e(G). Hence Delta=17 is impossible throughout the relevant range.

## 8. Delta=18 through 27

Let h be the largest integer for which at least h residual rows have degree at least h. A label of demand s_i needs s_i distinct selected sources of residual degree at least s_i, so s_i<=h and S<=ah. Residual activity gives

$$
r\ge h^2+(b-h)=b+h(h-1).
$$

Combining with S>=r+2t,

$$
b+2t\le(a+1)h-h^2
\le\left\lfloor\frac{(a+1)^2}{4}\right\rfloor
=\left\lfloor\frac{(29-b)^2}{4}\right\rfloor. \tag{8.1}
$$

Every b=18,...,27 violates (8.1) already at 210 edges, and increasing e(G) only strengthens the contradiction. Delta=28 is the universal-vertex/star case.

## 9. Assembly

At e(G)>=211:

- Delta<=14 is impossible by the degree sum;
- Delta=15 is impossible by Section 2;
- Delta=16 is impossible by Section 6;
- Delta=17 is impossible by Section 7;
- Delta=18,...,27 are impossible by Section 8;
- Delta=28 gives a star.

Hence e(G)<=210.

At e(G)=210, Delta<=14 is again impossible by degree sum. Sections 6-8 exclude every Delta>=16. Therefore Delta=15, and Section 2 forces

$$
G\cong K_{14,15}.
$$

This establishes the stated **candidate** order-29 result, subject to the independent-review boundary below.

## 10. What reviewer-v4 no longer depends on

For the theorem proof, reviewer-v4 does not require:

- Fan's 1987 density theorem;
- the N29 minimal trusted computational kernel;
- the corrected late cumulative-threshold LP;
- exact Farkas certificates;
- residual-row enumeration;
- source-capacity Hall pruning;
- the isolated-C lemma in the Delta=16 branch;
- the Delta=16 charging enumeration;
- the historical upper-range Delta=16 scans;
- the active RX-Hall / 3-D potential programme.

All remain preserved where historically relevant.

## 11. Current trust boundary

The highest-value independent mathematical targets are now substantially narrower:

1. the complement/quasi-edge selected/residual construction;
2. the exact ledger and demand implication S>=r+2t;
3. residual activity rho_u>=1 for t>0;
4. selected-incidence forcing s_i<=rho_u and selected-source capacity rho_u<=11;
5. the threshold-capacity lemma (3.5);
6. the hand threshold-tail clipping proof D<=6;
7. the Delta=15 witness-capacity/equality argument;
8. the Delta=17 pointwise charging bound and Delta>=18 residual h-index argument;
9. the cited Dailly-Foucaud-Hansberg dominating-edge theorem.

A counterexample to any universal bridge lemma overrides every downstream conclusion. No unrestricted Murty-Simon theorem, external endorsement or novelty determination is claimed.

## 12. Canonical supporting files

- Frozen self-contained bridge: `project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md`.
- Detailed threshold-tail hand proof: `project/research/general_n/2026-09-11-threshold-tail-collapse-v1/N29_DELTA16_THRESHOLD_TAIL_HAND_PROOF.md`.
- Threshold-tail audit README: `project/research/general_n/2026-09-11-threshold-tail-collapse-v1/README.md`.
- Historical minimal-kernel report: `project/reviews/n29/2026-09-08-redteam-restart-v1/MINIMAL_KERNEL_REPORT.json`.
- Blind hostile review follow-up: `project/reviews/n29/2026-09-11-blind-external-ai-redteam-v1/FOLLOWUP.md`.
- Cross-order bridge re-audit: `project/reviews/cross-cutting/2026-09-11-n29-cross-order-reaudit-v1/REPORT.md`.

Reviewer-v3 and all earlier packages remain frozen for provenance.

\newpage

# Appendix A. Frozen self-contained Delta=16 graph-to-model bridge


11 September 2026. Reviewer-v3 bridge. Research directed by Paul Lenz; mathematical development and checking by ChatGPT/Geeps. Hardened after a blind external-assistant red-team.

**Status: candidate mathematics; independent expert review remains open.** This version is deliberately self-contained at the main trust boundary. In particular, the threshold-capacity argument is proved here rather than merely cited from a companion note.

## 1. Setup

Let `G` be a simple diameter-two edge-critical graph on 29 vertices with `Delta(G)=16`. Put `H=complement(G)`. Choose a minimum-degree vertex `v` of `H`. Then

```text
d_H(v)=29-1-16=12.
```

Set

```text
A=N_H(v),             |A|=a=12,
B=V(H)\N_H[v],        |B|=b=16.
```

Let `C=H[A]`, and let `F` be the complement of `C` on A. Write `d_i=d_F(i)`.

For an edge count `m=e(G)`, define

```text
t=m-b(29-b)=m-208.
```

The proof-critical dense scopes are `t=2,3,4` for `m=210,211,212`; the upper-range hand arguments below also use larger t.

## 2. Quasi-edges and one representative per missing unordered B-pair

Take a missing pair `uw` of `H[B]`. Adding `uw` to H corresponds to deleting the critical edge `uw` from G. In `H+uw` a new adjacent total-dominating pair appears.

That pair must use u or w because no other adjacency changed. It cannot be `{u,w}` because both still miss v. Hence, after interchanging u,w if necessary, there is an existing edge `ui` of H such that

```text
N_H(u) union N_H(i) = V(H)\{w}.
```

The auxiliary i lies in A because the pair must dominate v. Write

```text
ui -> w.
```

For every missing **unordered** pair `{u,w}` in `H[B]`, choose exactly one such cross-edge, after orienting the pair if necessary. Call it **selected**. Every other existing A-B edge is **residual**.

A selected edge determines its B-source u and its unique exception w. Therefore it recovers its indexing missing unordered B-pair. Consequently:

1. two different missing unordered B-pairs cannot choose the same selected cross-edge;
2. opposite orientations of one unordered pair cannot both be designated selected;
3. at a fixed source, selected labels and supplements are distinct.

For `u in B`, define

```text
rho_u = residual degree into A,
q_u   = selected outdegree,
p_u   = selected indegree as supplement/exception.
```

For `i in A`, define

```text
R_i = residual degree into B,
x_i = selected degree into B.
```

Let

```text
r=sum_u rho_u=sum_i R_i.
```

## 3. Exact ledger and label demand

Selected cross-edges and existing edges of `H[B]` partition the unordered pairs of B, so

```text
#selected + e(H[B]) = C(b,2).
```

Direct edge counting gives

```text
e(F)=r+t,                                  (3.1)
sum_i d_i=2(r+t).                          (3.2)
```

Minimum degree in H gives `d_H(i)>=a` for every `i in A`. Since

```text
d_H(i)=1+(a-1-d_i)+R_i+x_i,
```

we have

```text
x_i>=d_i-R_i.
```

Define

```text
s_i=max(0,d_i-R_i),
S=sum_i s_i.
```

Then

```text
x_i>=s_i.                                  (3.3)
```

Also

```text
S >= sum_i(d_i-R_i)
  = 2(r+t)-r
  = r+2t.                                  (3.4)
```

Thus a label of demand `s_i` genuinely requires at least `s_i` distinct selected source incidences.

## 4. Pointwise forcing from a selected edge

Fix a selected edge `ui->w`.

### 4.1 `d_i<=rho_u+R_i`

Let j be an F-neighbour of i, so `ij` is absent from `H[A]`. Since `{u,i}` must dominate j, `uj` is an H-edge.

If `uj` is residual, charge j to a residual source slot at u. Otherwise `uj` is selected, say `uj->z`. Distinct selected labels at u have distinct supplements, so `z!=w`. Since `ui->w` must dominate z and `uz` is missing in `H[B]`, `iz` is an H-edge.

Moreover `iz` cannot be selected: i and z both miss the A-vertex j (`ij` is an F-edge and j is the unique exception of `uj->z`). A selected A-B edge has its unique exception in B and therefore must dominate every A-vertex. Hence `iz` is residual.

Distinct selected j give distinct supplements z, so the non-residual `uj` cases inject into distinct residual edges at label i. Therefore

```text
d_i<=rho_u+R_i.                            (4.1)
```

In particular, at every selected incidence,

```text
s_i<=rho_u.                                (4.2)
```

### 4.2 `d_i<=rho_u+rho_w`

For the same F-neighbour j, if `uj` is residual charge it to rho_u. Otherwise write `uj->z`. Since `{u,j}` must dominate w and `uw` is missing, `jw` is an H-edge.

The edge `jw` cannot be selected from source w: j and w both miss the A-vertex i (`ij` is an F-edge and `iw` is missing because w is the exception of `ui->w`). Hence `jw` is residual. Distinct j give distinct residual edges at w. Therefore

```text
d_i<=rho_u+rho_w.                          (4.3)
```

### 4.3 Source degree and supplement forcing

Every F-neighbour j of i is a cross-neighbour of u. Source u has exactly `rho_u+q_u` cross-neighbours, one of which is i, so

```text
d_i<=rho_u+q_u-1.                         (4.4)
```

For every other selected `uj->z` at u, the pair `{u,j}` must dominate w. Since `uw` is missing, `jw` is an H-edge. The `q_u-1` other selected labels are distinct, so w has at least `q_u-1` cross-neighbours among them. These are partitioned into residual and selected edges from w, hence

```text
rho_w+q_w>=q_u-1.                         (4.5)
```

## 5. Missing degree in B and endpoint load

Every missing unordered B-pair incident with u is oriented exactly once, either outward from u or inward to u. Hence

```text
q_u+p_u = missing degree of u in H[B].    (5.1)
```

Since

```text
d_H(u)=rho_u+(b-1)-(q_u+p_u)>=a,
```

we obtain

```text
p_u<=rho_u+(b-a-1)=rho_u+3.               (5.2)
```

Also

```text
q_u+p_u<=15,
q_u+rho_u<=12.                            (5.3)
```

For selected `ui->w`, label i is adjacent in B to:

- u itself;
- the `q_u-1` supplements of the other outward selected pairs at u;
- the `p_u` sources of selected pairs oriented into u.

These vertices are distinct. An incoming source cannot equal an outgoing supplement because that would orient the same missing unordered B-pair both ways. Therefore

```text
R_i+x_i>=q_u+p_u.                         (5.4)
```

## 6. Residual activity for positive surplus

Assume `t>0`. We prove

```text
rho_u>=1 for every u in B.                (6.1)
```

Suppose instead `rho_u=0`. Put

```text
U=N_A(u),
T=A\U.
```

Every cross-edge from u is then selected. There is no F-edge between U and T: if `i in U`, `j in T` and `ij in F`, the selected edge at `ui` would have to dominate j, forcing `uj in H`, contradiction.

Now count forced residual edges.

For every F-edge `ij` inside U, the selected edges from u to i and j have distinct supplements. Cross-domination forces two residual edges, one at each A-endpoint. They are residual because each forced edge has endpoints that jointly miss an A-vertex. The ordered F-edge endpoints inject into these residual cross-edges, giving `2e(F[U])` distinct residual edges with A-endpoint in U.

Now take an F-edge `ij` inside T. Adding ij to H creates a quasi-edge with exception i or j. Its auxiliary cannot be v, because the pair with v already dominates the opposite A-endpoint; it cannot be u because u is adjacent to neither endpoint. If its auxiliary z lay in A, domination of u would force `z in U`. But a quasi-edge with exception in T would then require an absent U-T pair, contradicting `F(U,T)=empty`. Hence the auxiliary lies in B.

That cross quasi-edge has its unique exception in A, so it cannot be one of the selected representatives whose exception lies in B; it is residual. Its A-endpoint together with the unique exception recovers the original F-edge, so distinct F[T]-edges give distinct residual cross-edges. Their A-endpoints lie in T and are therefore disjoint from the U-family.

Thus

```text
r>=2e(F[U])+e(F[T])
 >=e(F[U])+e(F[T])
 =e(F)
 =r+t,
```

contradicting `t>0`. Therefore (6.1) holds, and in particular

```text
r>=b=16.                                  (6.2)
```

## 7. Charging inequality

For each label i choose exactly `s_i` of its actual selected incidences, possible by (3.3). By (4.2), a chosen source u for label i satisfies

```text
rho_u>=s_i.
```

Also `q_u<=a-rho_u`. Charge each chosen incidence from source u by

```text
(rho_u-1)/(a-rho_u).
```

A chosen source has `q_u>=1`, so `rho_u<=a-1` and the denominator is positive. Source u participates in at most `q_u<=a-rho_u` chosen incidences, so its total charge is at most `rho_u-1`. Summing over all B-sources gives total charge at most

```text
r-b.
```

The charge function is increasing in integer rho on `1<=rho<a`. A label with demand `s_i` therefore receives at least

```text
s_i(s_i-1)/(a-s_i).
```

Hence

```text
r-b >= sum_i s_i(s_i-1)/(a-s_i).         (7.1)
```

Combining (7.1) with `S>=r+2t` gives

```text
sum_i s_i(a+1-2s_i)/(a-s_i) >= b+2t.     (7.2)
```

At `a=12,b=16`,

```text
sum_i s_i(13-2s_i)/(12-s_i) >= 16+2t.    (7.3)
```

## 8. Threshold-capacity lemma — complete proof

Fix an integer `h>=1` and define

```text
I_h={i:s_i>=h},
W_h=sum_{i in I_h}s_i,
Z_h={u:rho_u>=h},
z_h=|Z_h|.
```

Choose `s_i` actual selected incidences for each `i in I_h`. By (4.2), every chosen source belongs to `Z_h`.

Call a selected incidence **heavy** if its label lies in `I_h`. Let `ell_u` be the number of actual heavy selected incidences from source u. Then

```text
W_h<=sum_{u in Z_h} ell_u.                (8.1)
```

Let

```text
J={u in Z_h:ell_u>h},
j=|J|.
```

Fix `u in J` and a heavy selected edge `ui->w`. For each other heavy selected label k at u, `{u,k}` must dominate w; because `uw` is missing, `kw` is an H-edge. There are `ell_u-1>=h` such distinct heavy labels k.

We claim `w in Z_h`. If none of those forced edges `kw` is selected from source w, then all are residual and `rho_w>=ell_u-1>=h`. If at least one forced edge `kw` is selected from w, then its label k is heavy, so `s_k>=h`; applying (4.2) to that selected incidence gives `rho_w>=s_k>=h`. Thus every supplement of a heavy arc from J lies in `Z_h`.

Therefore every heavy selected arc contributed by a source in J uses an unordered B-pair entirely inside `Z_h` and incident with J. Because selection is injective on unordered B-pairs, the number of such arcs is at most

```text
j(z_h-j)+C(j,2)=j*z_h-j(j+1)/2.          (8.2)
```

Every source in `Z_h\J` contributes at most h heavy arcs by definition of J. Combining with (8.1),

```text
W_h <= (z_h-j)h + j*z_h - j(j+1)/2.      (8.3)
```

If `W_h>0`, some label has demand at least h and therefore needs at least h distinct sources in `Z_h`; so `z_h>=h`. Put

```text
q=z_h-h.
```

Now

```text
[h*z_h+C(q,2)] - RHS(8.3)
  = (q-j)(q-j-1)/2
  >=0,                                    (8.4)
```

because `q-j` is an integer and the product of two consecutive integers is nonnegative. Thus

```text
W_h<=h*z_h+C(z_h-h,2),
```

or equivalently

```text
2W_h<=z_h^2-z_h+h(h+1).                  (8.5)
```

This is a necessary capacity bound only; no sufficiency is claimed.

Two useful consequences are immediate. If `H0=max_i s_i>0`, then

```text
z_H0>=H0.                                 (8.6)
```

Also, residual activity gives every B-source baseline degree at least one, so for `h>=2`,

```text
r>=b+z_h(h-1).                            (8.7)
```

Hence any upper bound `r<=rmax` implies

```text
z_h<=floor((rmax-b)/(h-1)).               (8.8)
```

## 9. Excluding an isolated vertex of C

Suppose x is isolated in `C=H[A]`. Put `X=A\{x}`.

Because x is C-isolated,

```text
e(C)=e(C[X]).
```

From the exact ledger `e(C)+r=C(a,2)-t`, the number `P0` of missing H-edges inside X is

```text
P0=C(a-1,2)-e(C[X])
   =r-(a-1-t).                             (9.1)
```

Take a missing pair ij inside X. Adding ij to H creates a new adjacent total-dominating pair using i or j. It cannot be `{i,j}` because both miss x. Suppose it is `iz->j`. The auxiliary z cannot be v: v already neighbours j, so adding ij does not newly make `{i,v}` total dominating. It cannot lie in A: every A-vertex other than x misses x or, if z=x, `ix` is not an edge. Hence `z in B`.

Thus every missing X-pair gives a cross quasi-edge with auxiliary in B and exception in A. Such an edge cannot be selected, because selected representatives have their unique exception in B. Hence it is residual. Distinct missing X-pairs give distinct residual cross-edges because a cross quasi-edge has a unique exception. Let P be this family. Then

```text
|P|=P0=r-(a-1-t).                         (9.2)
```

Let Z be the set of B-endpoints used by P. For `z in Z`, choose `iz->j` from P. The pair `{i,z}` must dominate x, and i misses x, so `xz` is an H-edge. This edge is residual: if xz were selected for a missing B-pair, its selected pair would have to dominate every A-vertex, but `iz->j` implies z misses j while x is isolated in C and also misses j. Thus xz is residual. It lies outside P because its A-endpoint is x.

For each `z in B\Z`, residual activity supplies a residual edge incident with z; it is outside P because no edge of P has B-endpoint z. Therefore every one of the b vertices of B supplies a distinct residual edge outside P. Hence

```text
r>=|P|+b.
```

Using (9.2),

```text
b<=a-1-t.                                 (9.3)
```

At `a=12,b=16`, (9.3) is impossible for every positive t of interest. Therefore

```text
delta(C)>=1.                              (9.4)
```

Consequently

```text
d_i<=10,
e(C)>=6,
r<=C(12,2)-t-6=60-t.                    (9.5)
```

## 10. The exact bridge passed to the finite kernel

Every actual n=29, Delta=16 graph in a positive-surplus scope induces data satisfying:

```text
a=12, b=16;
1<=rho_u<=12;
0<=d_i<=10;
r=sum rho=sum R;
e(F)=r+t;
s_i=max(0,d_i-R_i);
S>=r+2t;
q_u+rho_u<=12;
p_u<=rho_u+3;
q_u+p_u<=15;
for selected ui->w:
  d_i<=rho_u+R_i,
  d_i<=rho_u+rho_w,
  d_i<=rho_u+q_u-1,
  rho_w+q_w>=q_u-1,
  R_i+x_i>=q_u+p_u;
charging inequality (7.3);
threshold-capacity inequalities (8.5)-(8.8);
r<=60-t.
```

The finite kernel deliberately enumerates a **superset** of graph-realizable arithmetic states satisfying necessary consequences of this bridge. Eliminating the relaxation is therefore safe provided every pruning rule is necessary and every terminal contradiction is checked exactly.

## 11. Hand cap for the upper range

For every integer `0<=s<=11`,

```text
s(13-2s)/(12-s)<=5/2,                    (11.1)
```

because

```text
5/2-s(13-2s)/(12-s)
 =(s-4)(4s-15)/(2(12-s))>=0.             (11.2)
```

Equality occurs only at `s=4`. With twelve labels, (7.3) gives

```text
16+2t<=30,
```

so

```text
t<=7,
m<=215.                                  (11.3)
```

Thus no Delta=16 graph exists at `m>=216`.

At `m=215`, `t=7`, equality in (11.3) forces every demand to equal four. Hence `S=48`. Equation (7.1) gives

```text
r>=16+12*(4*3/8)=34,
```

while `S>=r+14` gives `r<=34`, so `r=34`. From residual activity,

```text
34>=16+3z_4,
```

hence `z_4<=6`. But threshold capacity gives

```text
96=2W_4<=z_4^2-z_4+20<=50,
```

contradiction. Therefore `m=215` is also excluded by hand.

The only upper-range Delta=16 scopes above 211 that still require finite arithmetic are consequently

```text
m=212,213,214.
```

## 12. Review priorities

The highest-value independent attacks remain:

1. the quasi-edge construction and one-representative-per-unordered-pair convention;
2. the residual/non-selected status of the forced cross-edges in Section 4;
3. residual activity in Section 6;
4. the charging budget in Section 7;
5. threshold capacity in Section 8;
6. the isolated-C injection in Section 9;
7. the graph-to-averaged-LP embedding used after this bridge;
8. exact certificate semantics.

A single counterexample to a universal bridge lemma overrides every green computation downstream. This remains candidate mathematics until independent expert review is completed.

\newpage

# Appendix B. Reviewer-v4 hostile-audit hardening


11 September 2026.

This supplement records **non-blocking self-containedness and presentation hardening** identified in the hostile reviewer-v4 audit. It changes no mathematical conclusion.

## 1. Complement / total-domination correspondence

Let `H=complement(G)`. A pair `{x,y}` is a two-vertex total dominating set of `H` exactly when:

1. `xy` is an H-edge, hence a G-nonedge; and
2. every vertex is adjacent in H to at least one of x,y, equivalently x and y have no common neighbour in G.

Thus a two-vertex total dominating set in H is the complement-language form of a G-pair at distance greater than two.

If `xy` is an edge of the D2C graph G, deleting it makes some pair have distance greater than two. Equivalently, after adding `xy` to H, a two-vertex total dominating set appears. Because the only changed adjacency is `xy`, every newly appearing pair must use x or y. This is the quasi-edge premise used in the selected/residual bridge.

## 2. Delta=15 witness-capacity count made explicit

Let L be the vertices of deficit at least two, O the vertices of deficit one. Write

```text
P_L = C(h,2)+h(29-h)
```

for the total number of unordered vertex pairs incident with L.

Partition these pairs into actual G-edges `E_L` and missing pairs `M_L`. Every graph edge outside L is covered either by:

- an O-O witness, with capacity at most two; or
- a missing L-X two-step witness, with capacity at most one on edges outside L.

Therefore

```text
e(G)
 = |E_L| + e_G(V\L)
 <= |E_L| + |M_L| + 2 C(o,2)
 = P_L + o(o-1),
```

which is the manuscript inequality (2.3).

## 3. Full 4->3 clipping endpoint table

In the hand threshold-tail proof, after `max s_i<=4`, let `k=N_4` and let `l` be the number of threes among the remaining entries.

For `k=9`, `d_4=1` and the level-three changes are:

```text
l      W_3 -> W'_3      g_3 -> g'_3      drop
0       36 -> 27          9 -> 7           2
1       39 -> 30          9 -> 8           1
2       42 -> 33          9 -> 8           1
3       45 -> 36         10 -> 9           1
```

For `k=10`, again `d_4=1`:

```text
l      W_3 -> W'_3      g_3 -> g'_3      drop
0       40 -> 30          9 -> 8           1
1       43 -> 33         10 -> 8           2
2       46 -> 36         10 -> 9           1
```

So the loss of `d_4=1` is always paid for.

For `k=11`, `d_4=2`. If the remaining entry is at most two,

```text
W_3: 44 -> 33,
g_3: 10 -> 8,
```

so the level-three gain is two. If the remaining entry is three, `(3,4^11)->(3^12)` gives one unit of gain at each of levels two and three.

For `k=12`, `(4^12)->(3^12)` likewise decreases each of `g_2,g_3` from 10 to 9, paying the two-unit loss of `d_4`.

## 4. Explicit parameterisation for Delta>=17

For the N29 degree split, set

```text
b = Delta(G),
a = 28-b,
t = m - b(29-b).
```

The selected/residual bridge is parameterised in `(a,b)`; its proofs of the exact ledger, residual activity, selected-incidence forcing, charging and residual h-index use no special numerical property of `(a,b)=(12,16)` until the final substitutions.

Thus:

- `Delta=17`: `a=11,b=17,t=m-204`;
- `Delta=18,...,27`: `a=28-b` and the same `t=m-b(29-b)`.

At `m=210`, `Delta=17` gives `t=6` and hence the charging lower bound `b+2t=29` used in reviewer-v4.

## 5. Dominating-edge citation

The cited result is:

Antoine Dailly, Florent Foucaud, Adriana Hansberg, **Strengthening the Murty-Simon conjecture on diameter 2 critical graphs**, *Discrete Mathematics* 342 (2019), 3142-3159. DOI: `10.1016/j.disc.2019.06.023`.

Their Theorem 4 states that a non-bipartite D2C graph with a dominating edge, other than the six-vertex graph H5, has at most

```text
floor(n^2/4)-2
```

edges. At n=29 this gives 208.

## 6. Independence wording

The exact programs in this project are **separately implemented internal regressions**, not independent external validation. Independent mathematical review and independent computational reproduction remain open.

## 7. Disposition

No mathematical correction to reviewer-v4 is made by this supplement. The hostile audit found no blocking flaw; these additions make the review surface easier to reconstruct without relying on implicit parameterisation or omitted tiny case tables.
