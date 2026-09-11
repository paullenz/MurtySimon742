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
