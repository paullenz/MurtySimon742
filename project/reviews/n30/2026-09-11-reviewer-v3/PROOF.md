# The Murty-Simon bound at order thirty

**Reviewer edition 3 - complete candidate argument, 11 September 2026.**

Research direction: Paul Lenz. Mathematical development, internal auditing and drafting: ChatGPT/Geeps.

## Abstract

We present a candidate proof that every finite simple diameter-two edge-critical graph on thirty vertices has at most 225 edges, with equality exactly for the complete bipartite graph $K_{15,15}$. The proof uses a complement construction with selected and residual cross-edges, a threshold-capacity inequality, hand clipping lemmas, and explicit finite integer tables. A source-independent twelve-label bound closes every dense case of maximum degree at least seventeen. The degree-fifteen equality case has an elementary proof. At maximum degree sixteen, a hand classification of 100 demand profiles leaves eight source inequalities at 226 edges and 211 envelope evaluations at 225 edges. Every required mathematical argument and finite table is included in this manuscript. The verification companion records reproducibility, provenance and the boundary of internal checking.

**Status.** Complete candidate mathematics; exact internal arithmetic REPRODUCED; independent specialist mathematical review OPEN. Separately written checks by the same assistant are internal corroboration, not external validation. This edition does not change the governed theorem ledger, assert novelty, or claim the unrestricted conjecture.

**Theorem 1 (candidate).** Let $G$ be a finite simple graph on thirty vertices with diameter two such that deleting any edge increases its diameter. Then

$$e(G)\le225,\qquad e(G)=225\Longleftrightarrow G\cong K_{15,15}.$$

Distances between disconnected vertices are infinite. Write $m=e(G)$ and $\Delta=\Delta(G)$. A histogram such as $(1^7,2,3^8)$ means seven entries equal to one, one equal to two, and eight equal to three. Empty multiplicities are omitted. Indicator functions have values zero or one.

## How to read the proof

Sections 1-8 give the complete assembly. Appendices A-H supply its arguments and finite arithmetic without requiring another paper or a computational acceptance result. The appendix order follows the dependencies:

| Appendix | Material | Role in the proof |
|---|---|---|
| A | Selected/residual bridge | Universal graph-theoretic implications |
| B | Twelve-label bound | Hand closure of all dense degrees at least 17 |
| C | Thirteen-label classification | Hand reduction to exactly 100 profiles |
| D | All five- and six-lift intervals | Proof-critical finite classification arithmetic |
| E | Residual-tail reconstruction | Completeness of the endpoint row lists |
| F | Eight source inequalities | Proof-critical arithmetic at 226 edges |
| G | Four monotone envelopes | Formulas and local domains at 225 edges |
| H | All 211 positive-gap rows | Proof-critical endpoint arithmetic |

The larger profile sweeps and earlier LP/Farkas systems are not premises. **The printed finite tables are premises to be checked.** All such tables occur here, including rejected preimage intervals and every endpoint gap. A successful checker run cannot replace review of the universal bridge.

Notation is scoped locally. In the tail lemmas $p=N_1$ counts positive demands; in graph formulas $p_u$ is supplement indegree. Section 5 and Appendix E use $\lambda$ for ledger slack. Appendix G and its envelope evaluations use $\lambda$ for a certificate coefficient after ledger slack has been set to zero. Bridge equation numbers and section references are local to Appendix A; analogous conventions apply to the other appendices.

\clearpage

## 1. Degree entry and the equality case Delta=15

If `m>=226`, degree sum gives `Delta>=16`. If `m=225`, it gives `Delta>=15`.

Suppose `m=225` and `Delta=15`. Every vertex then has degree fifteen. For any nonadjacent pair x,y, their two neighborhoods lie among the other twenty-eight vertices and have total size thirty, so they have at least two common neighbors.

Deleting a single edge can destroy at most one common neighbor of a fixed nonadjacent pair. Thus every originally nonadjacent pair remains at distance at most two after any one edge deletion. Every originally adjacent pair except the deleted edge's endpoints remains adjacent. Consequently, for an edge uv to be critical, its endpoints must have no common neighbor. Otherwise even that pair remains at distance two after deletion, contradicting criticality.

Every edge therefore lies in no triangle, so G is triangle-free. Choose an edge uv. The sets `N(u)` and `N(v)` are disjoint independent sets, each of size fifteen, and together contain every vertex. Every vertex has degree fifteen and can have neighbors only in the opposite set of size fifteen. All cross edges are therefore present, giving `G=K(15,15)`.

Conversely, `K(15,15)` has diameter two, and deleting a cross edge makes its endpoints distance three. This proves the entire Delta=15 equality branch directly. **No published dominating-edge theorem is a dependency of this assembly.** The same elementary argument applies to a d-regular diameter-two edge-critical graph on 2d vertices for d>=2.

## 2. The universal bridge used here

Choose a minimum-degree vertex v in the complement H and put

$$
A=N_H(v),\quad a=29-\Delta,\quad B=V(H)\setminus N_H[v],\quad b=\Delta.
$$

The canonical parameterized bridge (Appendix A) supplies one selected cross-edge per missing unordered B-pair, with every other cross-edge residual. For labels use F-degree d_i, residual degree R_i, selected degree x_i and demand `s_i=max(0,d_i-R_i)`. For sources use residual degree rho_u, selected outdegree q_u and supplement indegree p_u. With `t=m-b(a+1)`, its needed conclusions are:

$$
e(F)=r+t,\quad r=\sum R_i=\sum\rho_u,\quad S=\sum s_i\ge r+2t,
\quad x_i\ge s_i.
$$

For t>0, every source has rho_u>=1. Every selected incidence ui has

$$
s_i\le\rho_u,\quad d_i\le\rho_u+q_u-1,\quad R_i+x_i\ge q_u+p_u.
$$

Every selected source-to-supplement arc u->w has `rho_w+q_w>=q_u-1`. Source degree and simple-graph capacity give

$$
q_u\le a-\rho_u,\quad p_u\le\rho_u+b-a-1,\quad q_u+p_u\le b-1.
$$

Threshold capacity gives `W_h<=C_h(z_h)`, where `z_h=#{rho>=h}`, `W_h=sum_{s_i>=h}s_i`, and `C_h(z)=[z(z-1)+h(h+1)]/2`.

The internal bridge audit, reproduced in the verification companion, checks the selected-edge injection, forced residual edges, residual activity, threshold pair counting, and the precise source domain. Charging and the isolated-C improvement are **not** needed in this assembly. Appendix A includes the corrected source-degree identity and the precise unique-exception argument.

## 3. Delta>=17 has a hand exclusion

For `Delta=17,...,28`, `1<=a<=12`, `b>=17`, and at every `m>=225` the surplus `t=m-b(30-b)` is positive.

The source-independent twelve-label lemma (Appendix B), applied after padding the demand vector with zeros, gives `Q<=18`. The bridge gives `Q>=b+2t>=19`, a contradiction. More sharply, at Delta=17 it gives `m<=221`.

If `Delta=29`, a universal vertex exists. Any edge between two other vertices could be deleted while the universal vertex still kept all pairs within distance two. Criticality therefore makes G a star, with only twenty-nine edges.

Thus every degree at least seventeen is excluded at the dense scopes. No historical Delta=17 profile checks, final Hall duals, or higher-degree charging scans remain necessary here.

## 4. Delta=16: the complete profile input is hand classified

Here `(a,b)=(13,16)` and `t=m-224`. In the dense scopes t is positive. The hand classification (Appendix C) proves:

- `Q<=21` for every threshold-admissible demand vector;
- exactly 100 profiles have Q>=18;
- the score distribution is `64 at 18`, `29 at 19`, `6 at 20`, `1 at 21`;
- the unique Q=21 vector is `(3^13)`.

Its proof clips demands to four, classifies seventy profiles, recovers thirty five-containing lifts, and rules out all higher preimages. Every accepted and rejected preimage interval is printed. The historical exhaustive list is only corroboration.

Since the bridge requires `Q>=16+2t`, every `t>=3`, equivalently `m>=227`, is impossible. Only t=2 and t=1 remain.

## 5. Residual rows from at most three slack units

For h=2,...,13, let z_h be the residual-degree tails and put g_h equal to the minimum threshold for the demand tail; g_13=0. Residual activity gives `r=16+sum z_h`. The exact slack identity is

$$
Q-(16+2t)=\lambda+\sum_{h=2}^{13}(z_h-g_h),\qquad
\lambda=S-r-2t\ge0.
$$

All summands are nonnegative integers, and `16>=z_2>=...>=z_13>=0`. Such tails determine rho uniquely. This is the written threshold-slack reconstruction (Appendix E), with the new hand classification supplying completeness.

At t=2, the seven profiles with Q>=20 give nine rows. Six Q=20 profiles have no slack. For `(3^13)`, g2=g3=9 and all higher g are zero; its one unit of slack can be assigned to lambda, to z2, or to a new z4=1. There are no other monotone possibilities.

At t=1, at most three units are distributed, giving 272 rows. The independent audit reconstructs both sets by adding boxes to monotone tail diagrams, using no historical residual-row generator. It agrees exactly with the printed prior frontier.

Whenever every demand is positive, `s_i=d_i-R_i` pointwise, and the ledger gives `S=r+2t`. Hence lambda=0. This immediately excludes the one positive-slack t=2 row and all 61 positive-slack t=1 rows. It leaves eight rows at m226 and 211 at m225. This implication uses positivity, not an assumed demand equality; it resolves an imprecise sentence in the earlier m226 exposition.

## 6. The eight m226 rows

The hand endpoint note (Appendix F) states all eight rows and their small source certificates. Here is its algebraic mechanism.

For a tight row, put `e_i=x_i-s_i>=0`, `E=sum e_i`, `M=sum x_i=sum q_u`, and `alpha_u=max(0,p_u-rho_u+1)`. The selected incidence inequalities imply `e_i>=alpha_u`; the valid source bound `p_u<=rho_u+2` implies alpha_u<=3. Thus, with `c=max s_i+3`,

$$
B_0:=\sum q_u\alpha_u
\le\sum_i(s_i+e_i)\min(e_i,3)\le cE.
$$

For each k, supplement forcing gives

$$
H_k=\sum_{q_u\ge k+1}q_u-\sum_{\rho_w+q_w\ge k}p_w\le0.
$$

The eight explicit source inequalities in the cited table give `B_0-cE>=delta`, with respective positive deltas

$$
1,\ 3,\ 12,\ 3,\ 4,\ 6,\ 1,\ 3/2.
$$

Their direct integer minima use `0<=q<=13-rho`, `0<=p<=rho+2`, and q=0 when rho is below every demand. The independent implementation verifies all 859 source states in that table. Each row contradicts B0<=cE, completing m226.

## 7. The 211 m225 rows

For every tight row, including the four with a zero demand, equality in `sum max(0,d_i-R_i)>=sum(d_i-R_i)` forces `d_i=R_i+s_i` at every label.

The four-envelope argument (Appendix G) uses the exact local domains

$$
0\le R\le12-s,\quad s\le x\le\min(16-R,\#\{u:\rho_u\ge s\}),
$$

$$
0\le q\le\min(13-\rho,\#\{i:s_i\le\rho\}),\quad 0\le p\le\rho+2.
$$

These are necessary simple-graph capacities. The stronger historical isolated-C degree bound is not used.

On a selected incidence the label coordinates `(s,R+s,16-R-x)` are componentwise at most the source coordinates `(rho,rho+q-1,16-q-p)`. A nondecreasing potential therefore gives

$$
\sum_i x_i\Phi(s_i,R_i+s_i,16-R_i-x_i)
\le\sum_u q_u\Phi(\rho_u,\rho_u+q_u-1,16-q_u-p_u).
$$

Combine this with `sum R=r`, `sum x=sum q=sum p` and the supplement tails H_k<=0. For the four printed nonnegative integer coefficient sets, take local minima ell_s and sigma_rho of the resulting label and source expressions. Any actual graph must satisfy

$$
\sum_s n_s\ell_s+\sum_\rho n_\rho\sigma_\rho-\lambda r\le0.
$$

Here lambda denotes the certificate's residual-budget coefficient, distinct from the already-zero ledger slack in Section 5. The complete 211-row arithmetic appendix (Appendix H) displays a strictly positive left side for every row. Certificates B1, B2, B3, C1 cover `195+13+2+1=211` rows; the minimum assigned integer gap is one.

The new independent audit recomputes all 12,772 local states with a separately written potential evaluator and reconstruction. It matches all 844 original per-template row gaps exactly. Every minimum can also be checked from the printed endpoint formulas in the four-envelope note. This is explicit finite integer arithmetic, not a numerical infeasibility conclusion.

Thus no Delta=16 graph has m225 or m226; Section 4 excluded all larger edge counts.

## 8. Complete assembly and remaining review boundary

At m>=226, Delta<=15 is excluded by degree sum; Delta=16 by Sections 4-7; Delta=17,...,28 by Section 3; and Delta=29 by the star argument. Hence m<=225.

At m225, Delta<=14 is excluded by degree sum, Delta=15 forces `K(15,15)` by Section 1, and all larger degrees are excluded above. The converse was verified in Section 1. This completes the candidate proof of Theorem 1.

The logical route now uses neither Fan's density theorem nor the published dominating-edge reduction, and it retains no Delta=17 or higher-degree computational branch. The remaining substantial finite audit surface is the explicit Delta=16 classification, tail reconstruction and endpoint arithmetic.


\clearpage

# Appendix A. Universal selected/residual bridge

## A.1. Setup

Let `G` be a finite simple diameter-two edge-critical graph on `n` vertices. Put

```text
H = complement(G).
```

Choose a minimum-degree vertex `v` of H and write

```text
A = N_H(v),
a = |A| = delta(H) = n-1-Delta(G),
B = V(H) \ N_H[v],
b = |B| = Delta(G).
```

Thus

```text
n=a+b+1.
```

Let

```text
C=H[A],
F=complement(C) on A.
```

For `i in A`, let `d_i=d_F(i)`.

Write `m=e(G)` and define the surplus over the complete bipartite benchmark determined by B as

```text
t = m-b(n-b) = m-b(a+1).
```

The strongest conclusions below assume `t>0`. The quasi-edge construction and exact ledger do not.

## A.2. Complement form of diameter-two edge-criticality

Take an edge `uw` of G, equivalently a missing pair `uw` of H. Deleting `uw` from G is the same as adding `uw` to H.

Because G is diameter-two edge-critical, in `G-uw` some pair `x,y` has distance greater than two. Equivalently, in `H+uw`, the pair `x,y` is adjacent and its open neighbourhoods together contain every vertex: it is an adjacent total-dominating pair.

No adjacent total-dominating pair existed already in H, because that would correspond to a pair at distance greater than two in G. Hence the newly total-dominating pair must use `u` or `w`, the only vertices whose H-neighbourhoods changed.

Now suppose `u,w in B`. The new total-dominating pair cannot be `{u,w}`, because both miss `v`. Hence, after interchanging u and w if necessary, there is an existing cross-edge `ui` with `i in A` such that

```text
N_H(u) union N_H(i) = V(H) \ {w}.        (2.1)
```

Write

```text
ui -> w.
```

The vertex w is the unique exception of the adjacent pair `{u,i}` in H.

## A.3. One selected representative per missing unordered B-pair

For every missing **unordered** pair `{u,w}` of `H[B]`, choose exactly one cross-edge supplied by Section A.2, after orienting the pair if necessary.

Call these chosen A-B edges **selected**. Call every other existing A-B edge **residual**.

A selected edge `ui->w` determines:

- its B-source u;
- its A-label i;
- its unique B-exception w.

Therefore the selected cross-edge recovers the missing unordered B-pair `{u,w}`. Consequently:

1. distinct missing unordered B-pairs cannot choose the same selected cross-edge;
2. the two orientations of one missing B-pair cannot both be selected;
3. at a fixed source u, selected labels are distinct and their supplements/exceptions are distinct.

For `u in B` define

```text
rho_u = residual degree of u into A,
q_u   = number of selected edges with source u,
p_u   = number of selected missing B-pairs whose exception is u.
```

For `i in A` define

```text
R_i = residual degree of i into B,
x_i = selected degree of i into B.
```

Let

```text
r = sum_{u in B} rho_u = sum_{i in A} R_i.
```

## A.4. Exact ledger

Every unordered pair of B is exactly one of:

- an edge of `H[B]`; or
- a missing pair of `H[B]`, carrying exactly one selected representative.

Hence

```text
#selected cross-edges + e(H[B]) = C(b,2).  (4.1)
```

Also

```text
e(H)=C(n,2)-m
    = a + e(C) + r + #selected + e(H[B]).
```

Using (4.1), `n=a+b+1`, and `t=m-b(a+1)`, this rearranges exactly to

```text
e(C)+r = C(a,2)-t.                         (4.2)
```

Since F is the complement of C on A,

```text
e(F)=r+t,                                  (4.3)
sum_i d_i = 2(r+t).                        (4.4)
```

No inequality has been used here.

## A.5. Label demand

Because v has minimum H-degree a, every `i in A` satisfies `d_H(i)>=a`. Its H-neighbours consist of:

- v;
- `a-1-d_i` neighbours inside A;
- `R_i+x_i` neighbours in B.

Thus

```text
1+(a-1-d_i)+R_i+x_i >= a,
```

so

```text
x_i >= d_i-R_i.
```

Define

```text
s_i=max(0,d_i-R_i),
S=sum_i s_i.
```

Then

```text
x_i>=s_i.                                  (5.1)
```

Summing the weaker inequalities `s_i>=d_i-R_i` and using (4.4) gives

```text
S >= 2(r+t)-r = r+2t.                      (5.2)
```

A positive demand `s_i` therefore corresponds to at least `s_i` distinct selected A-B incidences, hence `s_i` distinct B-sources.

## A.6. Pointwise forcing from a selected edge

Fix a selected edge

```text
ui -> w.
```

### A.6.1. Label residual forcing

Let j be an F-neighbour of i, so `ij` is absent from H[A]. Since j is an A-vertex and w is the unique exception in (2.1), `uj` must be an H-edge.

If `uj` is residual, charge j to a residual source incidence at u.

Otherwise `uj` is selected, say `uj->z`. The supplement z differs from w because the missing unordered pair `{u,w}` already has its unique selected orientation. Since `ui->w` must dominate z and `uz` is missing in H[B], `iz` is an H-edge.

Moreover `iz` is residual. Indeed, `ij` is absent, and because z is the exception of `uj->z`, `jz` is absent. Thus both endpoints of `iz` miss the A-vertex j. A selected A-B edge has its unique exception in B and must dominate every A-vertex, so `iz` cannot be selected.

Distinct selected j at u have distinct supplements z. Therefore the F-neighbours of i inject into at most `rho_u` residual source incidences and `R_i` residual label incidences:

```text
d_i <= rho_u+R_i.                          (6.1)
```

In particular, at every selected incidence of label i,

```text
s_i <= rho_u.                              (6.2)
```

### A.6.2. Supplement residual forcing

For the same F-neighbour j, again `uj` is an H-edge. If it is residual, charge it at u. Otherwise write `uj->z`.

The supplements z and w are distinct. The selected pair `{u,j}` must therefore dominate w. Since `uw` is missing, `jw` is an H-edge.

This edge is residual: `ij` is absent and `iw` is absent because w is the exception of `ui->w`, so both endpoints j and w miss the A-vertex i. Distinct j give distinct residual edges at w. Hence

```text
d_i <= rho_u+rho_w.                        (6.3)
```

### A.6.3. Source selected-degree forcing

Every F-neighbour j of i is a cross-neighbour of u. Source u has exactly `rho_u+q_u` A-neighbours, one of which is i. Therefore

```text
d_i <= rho_u+q_u-1.                       (6.4)
```

### A.6.4. Supplement forcing

For every other selected edge `uj->z` at u, its exception z differs from w. Thus `{u,j}` must dominate w. Since `uw` is missing, `jw` is an H-edge.

The `q_u-1` other selected labels j are distinct. They therefore give `q_u-1` distinct A-neighbours of w, each either residual or selected from source w. Hence

```text
rho_w+q_w >= q_u-1.                       (6.5)
```

## A.7. Exact missing degree in B and source capacities

Every missing unordered B-pair incident with u is selected in exactly one orientation: outward from u or inward to u. Therefore

```text
q_u+p_u = missing degree of u in H[B].    (7.1)
```

The H-degree of u is

```text
d_H(u)
 = (rho_u+q_u) + [(b-1)-(q_u+p_u)]
 = rho_u+b-1-p_u.
```

Minimum H-degree gives

```text
p_u <= rho_u+b-a-1.                       (7.2)
```

Also

```text
q_u+p_u <= b-1,                           (7.3)
q_u+rho_u <= a.                           (7.4)
```

Equation (7.4) is simply the A-side capacity at source u.

## A.8. Endpoint load

Again fix `ui->w`.

The following are distinct B-neighbours of label i:

1. u itself;
2. the `q_u-1` supplements of the other selected edges from source u;
3. the `p_u` sources of selected missing B-pairs oriented into u.

For family 2, if `uj->z` is another selected edge at u, then z differs from w and `ui->w` must dominate z; because `uz` is missing, `iz` is an H-edge.

For family 3, let a missing pair be oriented `y->u`. The source y cannot equal w, because `ui->w` already orients the missing pair `{u,w}` as `u->w`. Since `uy` is missing and `ui->w` dominates y, `iy` is an H-edge.

Families 2 and 3 cannot collide: a collision would orient the same missing unordered pair `{u,z}` both as `u->z` and `z->u`.

Therefore label i has at least

```text
1+(q_u-1)+p_u=q_u+p_u
```

B-neighbours, giving

```text
R_i+x_i >= q_u+p_u.                       (8.1)
```

## A.9. Residual activity for positive surplus

Assume from now on

```text
t>0.
```

We prove

```text
rho_u>=1 for every u in B.                (9.1)
```

Suppose instead `rho_u=0`. Put

```text
U=N_A(u),
T=A\U.
```

Every A-B edge incident with u is selected.

There is no F-edge between U and T. Indeed, if `i in U`, `j in T`, and `ij in F`, then the selected edge at `ui` has its unique exception in B and must dominate j. Since `ij` is absent, this forces `uj` in H, contradicting `j in T`.

Now count residual cross-edges forced by F.

Take an F-edge `ij` inside U. The selected edges from u to i and j have distinct supplements, say `ui->w_i` and `uj->w_j`. Because `w_i!=w_j`, the selected pair `{u,j}` must dominate `w_i`; since `uw_i` is missing, `jw_i` is an H-edge. Similarly `iw_j` is an H-edge. Both are residual: `jw_i` has endpoints that jointly miss the A-vertex i, and `iw_j` has endpoints that jointly miss j. Distinct ordered F-edge endpoints give distinct residual cross-edges. Thus F[U] forces `2e(F[U])` residual edges with A-endpoint in U.

Now take an F-edge `ij` inside T. Adding ij to H creates a new adjacent total-dominating pair using i or j. It cannot be `{i,j}` because both miss u. Its auxiliary cannot be v: v already neighbours both i and j, so adding ij cannot repair a failure at the opposite endpoint. It cannot be u because u is adjacent to neither endpoint.

If the auxiliary z lay in A, domination of u would force `z in U`. But the unique exception before adding ij is the other endpoint in T, so z would miss that T-vertex, creating an F-edge between U and T, impossible. Hence the auxiliary lies in B.

The resulting cross quasi-edge has its unique exception in A. Selected representatives have their unique exception in B, so this cross-edge is residual. The cross-edge together with its unique A-exception recovers the original F[T]-edge, giving an injection from F[T] to residual edges with A-endpoint in T.

The U- and T-families are disjoint. Therefore

```text
r >= 2e(F[U])+e(F[T])
  >= e(F[U])+e(F[T])
  = e(F)
  = r+t,
```

contradicting `t>0`.

Thus (9.1) holds, and

```text
r>=b.                                      (9.2)
```

## A.11. Threshold-capacity inequality

Fix an integer `h>=1` and define

```text
I_h={i:s_i>=h},
W_h=sum_{i in I_h}s_i,
Z_h={u:rho_u>=h},
z_h=|Z_h|.
```

Choose `s_i` actual selected incidences for every `i in I_h`. By (6.2), every chosen source lies in Z_h.

Call an actual selected incidence **heavy** if its label lies in I_h. Let `ell_u` be the number of heavy selected incidences from source u. Then

```text
W_h <= sum_{u in Z_h} ell_u.              (11.1)
```

Let

```text
J={u in Z_h:ell_u>h},
j=|J|.
```

Fix `u in J` and a heavy selected edge `ui->w`. For each other heavy selected label k at u, `{u,k}` must dominate w; since `uw` is missing, `kw` is an H-edge. There are `ell_u-1>=h` such distinct heavy labels.

We claim `w in Z_h`. If none of those forced edges `kw` is selected from source w, all are residual and `rho_w>=h`. If at least one is selected from w, its heavy label k has `s_k>=h`, and (6.2) applied to that selected incidence gives `rho_w>=s_k>=h`.

Thus every supplement of a heavy selected edge from J lies in Z_h. By injectivity on missing unordered B-pairs, the number of heavy selected arcs from J is at most the number of unordered pairs inside Z_h incident with J:

```text
j(z_h-j)+C(j,2)=j z_h-j(j+1)/2.           (11.2)
```

Every source in `Z_h\J` contributes at most h heavy incidences. Therefore

```text
W_h <= (z_h-j)h + j z_h-j(j+1)/2.         (11.3)
```

If `W_h>0`, some label needs at least h distinct selected sources in Z_h, so `z_h>=h`. Put

```text
q=z_h-h.
```

Then

```text
[h z_h+C(q,2)] - RHS(11.3)
 = (q-j)(q-j-1)/2
 >=0,                                     (11.4)
```

because `q-j` is an integer and the product of consecutive integers is nonnegative. Hence

```text
W_h <= h z_h+C(z_h-h,2),
```

or equivalently

```text
2W_h <= z_h^2-z_h+h(h+1).                 (11.5)
```

This is a necessary capacity bound; sufficiency is not claimed.

Residual activity also gives, for `h>=2`,

```text
r >= b+z_h(h-1).                           (11.6)
```

Thus any valid upper bound `r<=r_max` implies

```text
z_h <= floor((r_max-b)/(h-1)).             (11.7)
```


\clearpage

# Appendix B. A source-independent twelve-label tail bound

## B.1. Remove the source cutoff from the definition

For each integer `h>=2`, set

$$
C_h(z)=\frac{z(z-1)+h(h+1)}2,\qquad
\gamma_h(0)=0,
$$

and, for `W>0`, define `gamma_h(W)` as the least **integer z>=h**, with no upper cutoff, for which `W<=C_h(z)`. This minimum always exists.

For twelve demands `0<=s_i<=11`, put

$$
N_h=\#\{i:s_i\ge h\},\quad W_h=\sum_{s_i\ge h}s_i,
\quad p=N_1,
$$

$$
D=\sum_{h=2}^{11}(N_h-\gamma_h(W_h)),\qquad
Q=\sum_i s_i-\sum_{h=2}^{11}\gamma_h(W_h)=p+D.
$$

We prove `D<=6`, hence **Q<=18**. The source-count cutoff is absent from this definition. The proof below uses only lower bounds on gamma and small capacity values; no step needs `z<=16`.

## B.2. Clip high demands to six

For `h>=7`, let `N=N_h`. If `0<N<h`, then `gamma_h>=h>N`. Otherwise write `N=h+e`, with `0<=e<=12-h<=5`. Since `W_h>=hN`, a positive deficit would imply `hN<=C_h(N-1)`. But

$$
2hN-2C_h(N-1)=-e^2+3e+2h-2>0.
$$

The concave quadratic is positive at both endpoints of `[0,5]`, where it has values `2h-2` and `2h-12`. Thus every deficit at level at least seven is nonpositive.

Clipping all demands above six to six removes these nonpositive deficits. At lower levels it keeps `N_h` fixed and decreases `W_h`, so it cannot decrease `D`.

## B.3. Clip six, five and four

When the maximum is six, let `k` count the sixes. Their level-six deficit is nonpositive for `k<=10`. For `k=11,12` it equals one. If `l` counts existing fives, the required payments are:

| k,l | W5 before | W5 after | gamma5 drop |
|---|---:|---:|---:|
| 11,0 | 66 | 55 | 1 |
| 11,1 | 71 | 60 | 2 |
| 12,0 | 72 | 60 | 2 |

Each drop pays the lost positive level-six deficit. Thus six-to-five clipping never decreases `D`.

At maximum five, the level-five deficit is nonpositive for `k<=9`, and equals one for `k=10,11`. If `l` counts fours, the five possibilities `(k,l)=(10,0),(10,1),(10,2),(11,0),(11,1)` all have

$$
\gamma_4(5k+4l)-\gamma_4(4(k+l))=1.
$$

This pays the lost deficit. The exceptional vector `(5^12)` is discharged directly: its thresholds `(gamma2,gamma3,gamma4,gamma5)=(12,11,11,10)` give `D=4`. Thus every vector is either already bounded or clips to maximum four without decreasing `D`.

At maximum four, the level-four deficit is nonpositive for `k<=8`, one for `k=9,10`, and two for `k=11,12`. Let `l` count threes. For `k=9`, the gamma3 drops at `l=0,1,2,3` are `2,1,1,1`; for `k=10`, the drops at `l=0,1,2` are `1,2,1`. These pay the deficit one.

For `k=11` with the last entry at most two, gamma3 drops by two. If the last entry is three, both gamma3 and gamma2 drop from ten to nine. For `(4^12)`, both again drop from ten to nine. These pay the deficit two. Clipping to maximum three therefore cannot decrease `D`.

All these statements are direct substitutions in `C_h(z)`. Nonpositive-deficit cutoffs can also be checked by testing `z=k-1`, exactly as in Section B.2. Lower levels not used for payment only improve.

## B.4. Two tail counts finish the bound

At maximum three, set `x=N_2`, `y=N_3`, so `0<=y<=x<=12`. Then

$$
D=x+y-\gamma_2(2x+y)-\gamma_3(3y).
$$

The following three ranges suffice.

| Range | x-gamma2(2x+y) at most | y-gamma3(3y) at most | D at most |
|---|---:|---:|---:|
| 0<=y<=6 | 5 | 0 | 5 |
| 7<=y<=10 | 4 | 2 | 6 |
| 11<=y<=12 | 3 | 3 | 6 |

For completeness, the strict capacity defects proving the entries are:

- For the first range, `x<=7` is immediate from `gamma2>=2` when `x>0`; for `8<=x<=12`, testing `z=x-6` gives `2x-C_2(x-6)=(-x^2+17x-48)/2>0`. The y-bound is immediate for `y<=3`; for `4<=y<=6`, test `z=y-1` to get `3y-C_3(y-1)=(-y^2+9y-14)/2>0`.
- For `7<=y<=10`, test `z=y-3` in gamma3: the defect is `(-y^2+13y-24)/2>0`. Test `z=x-5` in gamma2: the defect is `(-x^2+15x+2y-36)/2>=(-x^2+15x-22)/2>0` for `7<=x<=12`.
- For `11<=y<=12`, test `z=y-4` in gamma3, obtaining `(-y^2+15y-32)/2>0`. Only `x=11,12` are possible; testing `z=x-4` in gamma2 gives `(-x^2+13x+2y-26)/2>=(-x^2+13x-4)/2>0`.

The empty tails have gamma equal to zero and are handled separately in the first range. Positivity over each listed interval follows by checking the endpoints of the concave quadratics. Therefore `D<=6` and `Q<=p+6<=18`. QED.

## B.5. Transfer to actual graphs with any source count

Use the canonical parameterized bridge (Appendix A). Let

$$
a=n-1-\Delta,\quad b=\Delta,\quad
t=m-b(a+1)>0.
$$

An actual graph gives positive residual degrees on all b sources and demands `0<=s_i<=a-1`. Its residual tails `z_h` satisfy `z_h>=gamma_h(W_h)` whenever the demand tail is nonempty. For empty demand tails, the right side is zero. Extend these zeros to all residual levels. The tail-sum identity and demand ledger give

$$
S\ge r+2t=b+2t+\sum_{h=2}^{a}z_h
\ge b+2t+\sum_{h=2}^{a-1}\gamma_h(W_h),
$$

so

$$
Q\ge b+2t. \tag{B.1}
$$

There is no issue when gamma would exceed b: then no actual residual tail could satisfy the necessary capacity inequality in the first place.

If `1<=a<=12`, pad the demand vector with zeros to length twelve. The score is unchanged because all added higher tails have zero demand. Section B.4 therefore gives `Q<=18`, regardless of b.

Consequently, if `1<=a<=12` and `b>=17`, positive integer surplus would give

$$
19\le b+2t\le Q\le18,
$$

a contradiction. We obtain the candidate general corollary

$$
1\le n-1-\Delta\le12,\quad \Delta\ge17
\quad\Longrightarrow\quad
e(G)\le\Delta(n-\Delta).
$$

This bound is attained by the corresponding complete bipartite graph; no uniqueness assertion at this bound is made. It is a consequence of the project's candidate universal bridge and this hand lemma, not a claim of independent novelty or an unrestricted solution.


\clearpage

# Appendix C. The complete thirteen-label classification

## C.1. Statement and threshold notation

Let thirteen integers satisfy `0<=s_i<=12`. For `h>=1` put

$$
N_h=\#\{i:s_i\ge h\},\qquad W_h=\sum_{s_i\ge h}s_i.
$$

For `h>=2`, define

$$
C_h(z)=\frac{z(z-1)+h(h+1)}2,
\qquad g_h(0)=0,
$$

and, when `W>0`, let `g_h(W)` be the least `z` in `{h,...,16}` with `W<=C_h(z)`. If no such `z` exists, the profile is threshold-inadmissible and is excluded immediately; equivalently assign it score minus infinity. All subsequent finite calculations have defined thresholds.

Write

$$
p=N_1,\quad D=\sum_{h=2}^{12}(N_h-g_h(W_h)),\quad
Q=\sum_i s_i-\sum_{h=2}^{12}g_h(W_h)=p+D. \tag{C.1}
$$

The last identity is the Ferrers-tail sum. The established graph bridge at `t=m-224=1` requires `Q>=16+2t=18`.

**Classification.** Exactly 100 demand multisets have `Q>=18`. Seventy have maximum demand at most four and appear in Table 1. The other thirty contain fives and appear in Table 2. None contains a demand at least six. Their scores are distributed as follows.

| Q | Number of profiles |
|---|---:|
| 18 | 64 |
| 19 | 29 |
| 20 | 6 |
| 21 | 1 |

In particular `Q<=21`, and equality holds only for `(3^13)`.

## C.2. Monotone clipping, including zeros and ones

The following clipping arguments apply to arbitrary demands, including zeros and ones.

For `h>=8`, let `N=N_h`. If `0<N<h`, then `g_h>=h>N`. Otherwise write `N=h+e`, where `0<=e<=13-h<=5`. Because `W_h>=hN`, a positive deficit would require `hN<=C_h(N-1)`. But

$$
2hN-2C_h(N-1)=-e^2+3e+2h-2>0. \tag{C.2}
$$

This concave quadratic is positive at both endpoints of `[0,5]`: the endpoint values are `2h-2` and `2h-12`. Thus every deficit at level at least eight is nonpositive. Clipping demands above seven to seven removes only nonpositive deficits; at lower levels it leaves `N_h` fixed and decreases `W_h`. It cannot decrease `D` or `Q`, and preserves `p`.

Now clip seven to six. If the number `k` of sevens is at most twelve, its level-seven deficit is nonpositive: for `k>=7`, the same capacity defect is `12+3e-e^2>0` with `e=k-7<=5`. The only positive case is `(7^13)`, whose level-seven deficit is one. The level-six threshold drops from `g_6(91)=13` to `g_6(78)=12`, paying that unit. All lower deficits improve or stay fixed.

For clipping six to five, the level-six deficit is nonpositive unless `k=11,12,13`; in those three cases it is one. Let `l` count the fives already present. The complete positive-deficit payment table is:

| k | l | Drop in g5 |
|---:|---:|---:|
| 11 | 0 | 1 |
| 11 | 1 | 2 |
| 11 | 2 | 1 |
| 12 | 0 | 2 |
| 12 | 1 | 1 |
| 13 | 0 | 1 |

Each drop is `g_5(6k+5l)-g_5(5(k+l))`, so it pays the lost level-six deficit.

Finally clip five to four. The level-five deficit is nonpositive for `k<=9`, one for `k=10,11`, and two for `k=12,13`. If `l` counts the existing fours, then `g_4(5k+4l)-g_4(4(k+l))=1` in every positive-deficit case: `l=0,...,3` for `k=10`, `l=0,...,2` for `k=11`, `l=0,1` for `k=12`, and `l=0` for `k=13`.

When another unit is needed, it comes from level three:

| k,l | W3 before | W3 after | Guaranteed drop in g3 |
|---|---|---|---:|
| 12,0 | 60 or 63 | 48 or 51 | 1 |
| 12,1 | 64 | 52 | 1 |
| 13,0 | 65 | 52 | 1 |

In the first row the remaining entry is any of `0,1,2,3`; it contributes three precisely when it is three. This explicitly covers the low-demand cases absent from the earlier endpoint assumptions.

Consequently, clipping an arbitrary demand vector to four by this sequence preserves `p` and never decreases `Q`. It also preserves `N_2` and `N_3`. Completeness requires examining the reverse lifts; Sections C.5-C.6 do so.

## C.3. Only four low-dimensional cases remain at cap four

At cap four put `x=N_2`, `y=N_3`, `z=N_4`. Then

$$
0\le z\le y\le x\le p\le13,
\quad D_4(x,y,z)=x+y+z-g_2(2x+y+z)-g_3(3y+z)-g_4(4z). \tag{C.3}
$$

The multiset is `(0^(13-p),1^(p-x),2^(x-y),3^(y-z),4^z)`.

For `x>=1`, adjoining a demand two to the part counted by `x` cannot decrease `D_4`: it increases `x` by one and `W_2` by two, and increases `g_2` by at most one. Indeed `C_2(z+1)-C_2(z)=z>=2` once `g_2>=2`. Thus when `1<=x<=10` it suffices to bound `D_4(10,y,z)`; `x=0` has deficit zero.

At `z=0`, the deficits for `y=0,...,10` are

$$
(3,1,2,3,3,2,2,3,3,4,4).
$$

For `0<=z<=8`, `z-g_4(4z)<=0`, while increasing `z` cannot improve either of the first two terms in (3). Hence `D_4<=4`. For `z=9,10`, the only pairs `(y,z)` are `(9,9),(10,9),(10,10)`, with deficits `2,3,2`. We have proved `x<=10 => D_4<=4`.

If `x=11` and `y<=10`, comparison with `x=10` gives `D_4<=5`. At `x=y=11`, the values for `z=0,...,11` are

$$
(5,2,2,3,4,4,4,3,3,4,3,4).
$$

Thus `x<=11 => D_4<=5`. The requirement `p+D_4>=18` now forces exactly one of

$$
(p,x)=(12,12),(13,11),(13,12),(13,13). \tag{C.4}
$$

Indeed `p<=11` gives `Q<=16`; `p=12,x<=11` gives `Q<=17`; and `p=13,x<=10` gives `Q<=17`.

## C.4. The seventy cap-four profiles

Table 1 lists every permitted value of `y` for each `z` and each pair in (4). A dash means the set is empty. The inequalities `z<=y<=x` are always imposed.

| z | p=12,x=12 | p=13,x=11 | p=13,x=12 | p=13,x=13 |
|---:|---|---|---|---|
| 0 | 11,12 | 9,11 | 0,7,9,10,11,12 | 0,3,4,5,7,8,9,10,11,12,13 |
| 1 | - | - | - | - |
| 2 | - | - | - | 13 |
| 3 | - | - | 12 | 10,12,13 |
| 4 | - | - | 10,11,12 | 9,10,11,12,13 |
| 5 | - | - | 12 | 11,12,13 |
| 6 | - | - | 12 | 11,12,13 |
| 7 | - | - | - | 11,12,13 |
| 8 | - | - | - | 11,12,13 |
| 9 | - | - | 11,12 | 10,11,12,13 |
| 10 | - | - | 12 | 10,11,12,13 |
| 11 | 12 | - | 11,12 | 11,12,13 |
| 12 | 12 | - | 12 | 12,13 |
| 13 | - | - | - | 13 |
| **Count** | **4** | **2** | **18** | **46** |

Here is a direct method to verify both inclusion and omission in this table, without a demand search. Fix `p,x,z`; substitute (3) into `p+D_4>=18`. The only changing thresholds are `g_2(2x+y+z)` and `g_3(3y+z)`. Their changes occur just after

$$
y=C_2(a)-2x-z,\qquad
y=\left\lfloor\frac{C_3(b)-z}{3}\right\rfloor. \tag{C.5}
$$

Within each resulting integer interval both thresholds are constant, so `Q` is `y` plus a fixed integer. Intersect that interval with the resulting lower bound on `y`. Check `y=z=0` separately, since `g_3(0)=0`. This produces exactly Table 1.

For example, at `p=13,x=12,z=0`, (3) gives

$$
Q=25+y-g_2(24+y)-g_3(3y).
$$

For `y=0,...,12`, its values are

$$
(18,15,16,17,17,17,17,18,17,18,18,19,19),
$$

yielding the indicated six values of `y`. Each other row uses precisely the same two threshold boundaries. The capacity values needed for this table and the lifts below are:

| z | C2(z) | C3(z) | C4(z) | C5(z) | C6(z) |
|---:|---:|---:|---:|---:|---:|
| 2 | 4 | - | - | - | - |
| 3 | 6 | 9 | - | - | - |
| 4 | 9 | 12 | 16 | - | - |
| 5 | 13 | 16 | 20 | 25 | - |
| 6 | 18 | 21 | 25 | 30 | 36 |
| 7 | 24 | 27 | 31 | 36 | 42 |
| 8 | 31 | 34 | 38 | 43 | 49 |
| 9 | 39 | 42 | 46 | 51 | 57 |
| 10 | 48 | 51 | 55 | 60 | 66 |
| 11 | 58 | 61 | 65 | 70 | 76 |
| 12 | 69 | 72 | 76 | 81 | 87 |
| 13 | 81 | 84 | 88 | 93 | 99 |

All threshold arguments in Sections C.3-C.6 are at most 78, so these capacities suffice; no threshold above thirteen is needed there.

## C.5. All cap-five preimages: thirty more profiles

Any cap-five profile with `Q>=18` clips to Table 1. To recover it, replace `k` of the `z` fours by fives, where `1<=k<=z`. Its exact score is

$$
\begin{aligned}
Q_5(p,x,y,z,k)={}&p+x+y+z+k\\
&-g_2(2x+y+z+k)-g_3(3y+z+k)\\
&-g_4(4z+k)-g_5(5k). \tag{C.6}
\end{aligned}
$$

The complete solutions are Table 2. All have `p=x=13`.

| y | z | Permitted k | Number |
|---:|---:|---|---:|
| 12 | 10 | 5 | 1 |
| 12 | 12 | 5,6,7,12 | 4 |
| 13 | 10 | 5,6 | 2 |
| 13 | 11 | 5,6,7,8,10,11 | 6 |
| 13 | 12 | 4,5,6,7,10,12 | 6 |
| 13 | 13 | 3,4,5,6,7,8,9,10,11,12,13 | 11 |
| **Total** | | | **30** |

The corresponding multiset is `(2^(13-y),3^(y-z),4^(z-k),5^k)`.

To check completeness, apply the same interval argument to (6). Its threshold changes occur just after

$$
\begin{split}
k={}&C_2(a)-(2x+y+z),\\
k={}&C_3(b)-(3y+z),\\
k={}&C_4(c)-4z,\\
k={}&\lfloor C_5(d)/5\rfloor. \tag{C.7}
\end{split}
$$

Between changes, `Q_5=k+constant`; intersect with `Q_5>=18`. Table 1 has altogether 366 possible positive lifts, split by (7) into 230 affine intervals. The complete preimage appendix (Appendix D) prints every interval, its constant threshold vector, the formula for `Q_5`, and its accepted integers. It includes rejected lifts from **every** Table 1 row with `z>0`, including those with a zero or a one. Thus Table 2 is not an inference from the historical survivor list.

## C.6. No original profile containing six or more is hidden by clipping

Suppose an original profile with `Q>=18` contains a value at least six. After clipping to six it still has `Q>=18` and contains a six. After the next clipping, it is a Table 2 profile containing fives. Therefore it suffices to lift one of the thirty profiles in Table 2: raise `j` of its `k` fives to six, where `1<=j<=k`.

The exact score of that lift is

$$
\begin{aligned}
Q_6(y,z,k,j)={}&26+y+z+k+j\\
&-g_2(26+y+z+k+j)-g_3(3y+z+k+j)\\
&-g_4(4z+k+j)-g_5(5k+j)-g_6(6j). \tag{C.8}
\end{aligned}
$$

Again, the score is `j+constant` between threshold changes. The changes occur just after the four capacities minus their displayed bases, and after `floor(C_6(d)/6)`. The maximum on each interval is its value at the right endpoint. This gives:

| y | z | k ranges from Table 2 | Maximum Q6 over all permitted k and 1<=j<=k |
|---:|---:|---|---:|
| 12 | 10 | 5 | 14 |
| 12 | 12 | 5,6,7,12 | 15 |
| 13 | 10 | 5,6 | 15 |
| 13 | 11 | 5,6,7,8,10,11 | 15 |
| 13 | 12 | 4,5,6,7,10,12 | 16 |
| 13 | 13 | 3,4,5,6,7,8,9,10,11,12,13 | 16 |

For example, lifting `(5^13)` gives

$$
Q_6=65+j-g_2(65+j)-g_3(65+j)-g_4(65+j)-g_5(65+j)-g_6(6j).
$$

At `j=1,...,13`, these scores are

$$
(13,14,15,16,16,16,16,15,15,15,16,15,15).
$$

There are only 225 positive six-lifts in total, divided into 131 affine intervals. Every interval and its maximum is printed in the second half of the appendix. All have score at most sixteen, contradicting `Q>=18`.

This rules out all original demands at least six, including seven through twelve: the forward clipping already proved that none could disappear without leaving a six-lift with a score at least as large. Together with Sections C.4-C.5, this proves the classification. QED.


\clearpage

# Appendix D. Complete preimage arithmetic

Companion to the written hand classification. Each interval records the affine formula `Q(v)=offset+v`; threshold vectors are constant throughout it. The final point therefore attains the interval maximum. All omitted accepted-value sets below are empty.

## Cap-five lifts of every cap-four profile containing a four

| p,x,y,z | k interval | (g2,g3,g4,g5) | Q(k) | accepted k |
|---|---|---|---|---|
| 12,12,12,11 | 1-1 | 10,10,9,5 | 13+k | none |
| 12,12,12,11 | 2-2 | 11,10,9,5 | 12+k | none |
| 12,12,12,11 | 3-4 | 11,10,10,5 | 11+k | none |
| 12,12,12,11 | 5-5 | 11,11,10,5 | 10+k | none |
| 12,12,12,11 | 6-6 | 11,11,10,6 | 9+k | none |
| 12,12,12,11 | 7-7 | 11,11,10,7 | 8+k | none |
| 12,12,12,11 | 8-8 | 11,11,10,8 | 7+k | none |
| 12,12,12,11 | 9-10 | 11,11,10,9 | 6+k | none |
| 12,12,12,11 | 11-11 | 11,11,10,10 | 5+k | none |
| 12,12,12,12 | 1-3 | 11,10,10,5 | 12+k | none |
| 12,12,12,12 | 4-5 | 11,11,10,5 | 11+k | none |
| 12,12,12,12 | 6-6 | 11,11,10,6 | 10+k | none |
| 12,12,12,12 | 7-7 | 11,11,10,7 | 9+k | none |
| 12,12,12,12 | 8-8 | 11,11,11,8 | 7+k | none |
| 12,12,12,12 | 9-10 | 11,11,11,9 | 6+k | none |
| 12,12,12,12 | 11-12 | 12,11,11,10 | 4+k | none |
| 13,12,12,3 | 1-3 | 10,9,4,5 | 12+k | none |
| 13,12,10,4 | 1-1 | 9,9,5,5 | 11+k | none |
| 13,12,10,4 | 2-4 | 10,9,5,5 | 10+k | none |
| 13,12,11,4 | 1-4 | 10,9,5,5 | 11+k | none |
| 13,12,12,4 | 1-2 | 10,9,5,5 | 12+k | none |
| 13,12,12,4 | 3-4 | 10,10,5,5 | 11+k | none |
| 13,12,12,5 | 1-1 | 10,9,6,5 | 12+k | none |
| 13,12,12,5 | 2-5 | 10,10,6,5 | 11+k | none |
| 13,12,12,6 | 1-1 | 10,10,6,5 | 12+k | none |
| 13,12,12,6 | 2-5 | 10,10,7,5 | 11+k | none |
| 13,12,12,6 | 6-6 | 10,10,7,6 | 10+k | none |
| 13,12,11,9 | 1-2 | 10,10,8,5 | 12+k | none |
| 13,12,11,9 | 3-4 | 10,10,9,5 | 11+k | none |
| 13,12,11,9 | 5-5 | 11,10,9,5 | 10+k | none |
| 13,12,11,9 | 6-6 | 11,10,9,6 | 9+k | none |
| 13,12,11,9 | 7-7 | 11,10,9,7 | 8+k | none |
| 13,12,11,9 | 8-8 | 11,10,9,8 | 7+k | none |
| 13,12,11,9 | 9-9 | 11,10,9,9 | 6+k | none |
| 13,12,12,9 | 1-2 | 10,10,8,5 | 13+k | none |
| 13,12,12,9 | 3-3 | 10,10,9,5 | 12+k | none |
| 13,12,12,9 | 4-5 | 11,10,9,5 | 11+k | none |
| 13,12,12,9 | 6-6 | 11,10,9,6 | 10+k | none |
| 13,12,12,9 | 7-7 | 11,11,9,7 | 8+k | none |
| 13,12,12,9 | 8-8 | 11,11,9,8 | 7+k | none |
| 13,12,12,9 | 9-9 | 11,11,9,9 | 6+k | none |
| 13,12,12,10 | 1-2 | 10,10,9,5 | 13+k | none |
| 13,12,12,10 | 3-5 | 11,10,9,5 | 12+k | none |
| 13,12,12,10 | 6-6 | 11,11,9,6 | 10+k | none |
| 13,12,12,10 | 7-7 | 11,11,10,7 | 8+k | none |
| 13,12,12,10 | 8-8 | 11,11,10,8 | 7+k | none |
| 13,12,12,10 | 9-10 | 11,11,10,9 | 6+k | none |
| 13,12,11,11 | 1-2 | 10,10,9,5 | 13+k | none |
| 13,12,11,11 | 3-5 | 11,10,10,5 | 11+k | none |
| 13,12,11,11 | 6-6 | 11,10,10,6 | 10+k | none |
| 13,12,11,11 | 7-7 | 11,10,10,7 | 9+k | none |
| 13,12,11,11 | 8-8 | 11,11,10,8 | 7+k | none |
| 13,12,11,11 | 9-10 | 11,11,10,9 | 6+k | none |
| 13,12,11,11 | 11-11 | 11,11,10,10 | 5+k | none |
| 13,12,12,11 | 1-1 | 10,10,9,5 | 14+k | none |
| 13,12,12,11 | 2-2 | 11,10,9,5 | 13+k | none |
| 13,12,12,11 | 3-4 | 11,10,10,5 | 12+k | none |
| 13,12,12,11 | 5-5 | 11,11,10,5 | 11+k | none |
| 13,12,12,11 | 6-6 | 11,11,10,6 | 10+k | none |
| 13,12,12,11 | 7-7 | 11,11,10,7 | 9+k | none |
| 13,12,12,11 | 8-8 | 11,11,10,8 | 8+k | none |
| 13,12,12,11 | 9-10 | 11,11,10,9 | 7+k | none |
| 13,12,12,11 | 11-11 | 11,11,10,10 | 6+k | none |
| 13,12,12,12 | 1-3 | 11,10,10,5 | 13+k | none |
| 13,12,12,12 | 4-5 | 11,11,10,5 | 12+k | none |
| 13,12,12,12 | 6-6 | 11,11,10,6 | 11+k | none |
| 13,12,12,12 | 7-7 | 11,11,10,7 | 10+k | none |
| 13,12,12,12 | 8-8 | 11,11,11,8 | 8+k | none |
| 13,12,12,12 | 9-10 | 11,11,11,9 | 7+k | none |
| 13,12,12,12 | 11-12 | 12,11,11,10 | 5+k | none |
| 13,13,13,2 | 1-1 | 10,9,4,5 | 13+k | none |
| 13,13,13,2 | 2-2 | 10,10,4,5 | 12+k | none |
| 13,13,10,3 | 1-1 | 10,8,4,5 | 12+k | none |
| 13,13,10,3 | 2-3 | 10,9,4,5 | 11+k | none |
| 13,13,12,3 | 1-3 | 10,9,4,5 | 13+k | none |
| 13,13,13,3 | 1-3 | 10,10,4,5 | 13+k | none |
| 13,13,9,4 | 1-3 | 10,8,5,5 | 11+k | none |
| 13,13,9,4 | 4-4 | 10,9,5,5 | 10+k | none |
| 13,13,10,4 | 1-4 | 10,9,5,5 | 11+k | none |
| 13,13,11,4 | 1-4 | 10,9,5,5 | 12+k | none |
| 13,13,12,4 | 1-2 | 10,9,5,5 | 13+k | none |
| 13,13,12,4 | 3-4 | 10,10,5,5 | 12+k | none |
| 13,13,13,4 | 1-4 | 10,10,5,5 | 13+k | none |
| 13,13,11,5 | 1-4 | 10,9,6,5 | 12+k | none |
| 13,13,11,5 | 5-5 | 10,10,6,5 | 11+k | none |
| 13,13,12,5 | 1-1 | 10,9,6,5 | 13+k | none |
| 13,13,12,5 | 2-5 | 10,10,6,5 | 12+k | none |
| 13,13,13,5 | 1-4 | 10,10,6,5 | 13+k | none |
| 13,13,13,5 | 5-5 | 11,10,6,5 | 12+k | none |
| 13,13,11,6 | 1-1 | 10,9,6,5 | 13+k | none |
| 13,13,11,6 | 2-3 | 10,9,7,5 | 12+k | none |
| 13,13,11,6 | 4-5 | 10,10,7,5 | 11+k | none |
| 13,13,11,6 | 6-6 | 11,10,7,6 | 9+k | none |
| 13,13,12,6 | 1-1 | 10,10,6,5 | 13+k | none |
| 13,13,12,6 | 2-4 | 10,10,7,5 | 12+k | none |
| 13,13,12,6 | 5-5 | 11,10,7,5 | 11+k | none |
| 13,13,12,6 | 6-6 | 11,10,7,6 | 10+k | none |
| 13,13,13,6 | 1-1 | 10,10,6,5 | 14+k | none |
| 13,13,13,6 | 2-3 | 10,10,7,5 | 13+k | none |
| 13,13,13,6 | 4-5 | 11,10,7,5 | 12+k | none |
| 13,13,13,6 | 6-6 | 11,10,7,6 | 11+k | none |
| 13,13,11,7 | 1-2 | 10,9,7,5 | 13+k | none |
| 13,13,11,7 | 3-3 | 10,10,7,5 | 12+k | none |
| 13,13,11,7 | 4-4 | 10,10,8,5 | 11+k | none |
| 13,13,11,7 | 5-5 | 11,10,8,5 | 10+k | none |
| 13,13,11,7 | 6-6 | 11,10,8,6 | 9+k | none |
| 13,13,11,7 | 7-7 | 11,10,8,7 | 8+k | none |
| 13,13,12,7 | 1-3 | 10,10,7,5 | 13+k | none |
| 13,13,12,7 | 4-5 | 11,10,8,5 | 11+k | none |
| 13,13,12,7 | 6-6 | 11,10,8,6 | 10+k | none |
| 13,13,12,7 | 7-7 | 11,10,8,7 | 9+k | none |
| 13,13,13,7 | 1-2 | 10,10,7,5 | 14+k | none |
| 13,13,13,7 | 3-3 | 11,10,7,5 | 13+k | none |
| 13,13,13,7 | 4-5 | 11,10,8,5 | 12+k | none |
| 13,13,13,7 | 6-6 | 11,11,8,6 | 10+k | none |
| 13,13,13,7 | 7-7 | 11,11,8,7 | 9+k | none |
| 13,13,11,8 | 1-1 | 10,9,8,5 | 13+k | none |
| 13,13,11,8 | 2-3 | 10,10,8,5 | 12+k | none |
| 13,13,11,8 | 4-5 | 11,10,8,5 | 11+k | none |
| 13,13,11,8 | 6-6 | 11,10,8,6 | 10+k | none |
| 13,13,11,8 | 7-7 | 11,10,9,7 | 8+k | none |
| 13,13,11,8 | 8-8 | 11,10,9,8 | 7+k | none |
| 13,13,12,8 | 1-2 | 10,10,8,5 | 13+k | none |
| 13,13,12,8 | 3-5 | 11,10,8,5 | 12+k | none |
| 13,13,12,8 | 6-6 | 11,10,8,6 | 11+k | none |
| 13,13,12,8 | 7-7 | 11,10,9,7 | 9+k | none |
| 13,13,12,8 | 8-8 | 11,11,9,8 | 7+k | none |
| 13,13,13,8 | 1-1 | 10,10,8,5 | 14+k | none |
| 13,13,13,8 | 2-4 | 11,10,8,5 | 13+k | none |
| 13,13,13,8 | 5-5 | 11,11,8,5 | 12+k | none |
| 13,13,13,8 | 6-6 | 11,11,8,6 | 11+k | none |
| 13,13,13,8 | 7-7 | 11,11,9,7 | 9+k | none |
| 13,13,13,8 | 8-8 | 11,11,9,8 | 8+k | none |
| 13,13,10,9 | 1-2 | 10,9,8,5 | 13+k | none |
| 13,13,10,9 | 3-3 | 10,9,9,5 | 12+k | none |
| 13,13,10,9 | 4-5 | 11,10,9,5 | 10+k | none |
| 13,13,10,9 | 6-6 | 11,10,9,6 | 9+k | none |
| 13,13,10,9 | 7-7 | 11,10,9,7 | 8+k | none |
| 13,13,10,9 | 8-8 | 11,10,9,8 | 7+k | none |
| 13,13,10,9 | 9-9 | 11,10,9,9 | 6+k | none |
| 13,13,11,9 | 1-2 | 10,10,8,5 | 13+k | none |
| 13,13,11,9 | 3-5 | 11,10,9,5 | 11+k | none |
| 13,13,11,9 | 6-6 | 11,10,9,6 | 10+k | none |
| 13,13,11,9 | 7-7 | 11,10,9,7 | 9+k | none |
| 13,13,11,9 | 8-8 | 11,10,9,8 | 8+k | none |
| 13,13,11,9 | 9-9 | 11,10,9,9 | 7+k | none |
| 13,13,12,9 | 1-1 | 10,10,8,5 | 14+k | none |
| 13,13,12,9 | 2-2 | 11,10,8,5 | 13+k | none |
| 13,13,12,9 | 3-5 | 11,10,9,5 | 12+k | none |
| 13,13,12,9 | 6-6 | 11,10,9,6 | 11+k | none |
| 13,13,12,9 | 7-7 | 11,11,9,7 | 9+k | none |
| 13,13,12,9 | 8-8 | 11,11,9,8 | 8+k | none |
| 13,13,12,9 | 9-9 | 11,11,9,9 | 7+k | none |
| 13,13,13,9 | 1-2 | 11,10,8,5 | 14+k | none |
| 13,13,13,9 | 3-3 | 11,10,9,5 | 13+k | none |
| 13,13,13,9 | 4-5 | 11,11,9,5 | 12+k | none |
| 13,13,13,9 | 6-6 | 11,11,9,6 | 11+k | none |
| 13,13,13,9 | 7-7 | 11,11,9,7 | 10+k | none |
| 13,13,13,9 | 8-8 | 11,11,9,8 | 9+k | none |
| 13,13,13,9 | 9-9 | 11,11,9,9 | 8+k | none |
| 13,13,10,10 | 1-2 | 10,9,9,5 | 13+k | none |
| 13,13,10,10 | 3-5 | 11,10,9,5 | 11+k | none |
| 13,13,10,10 | 6-6 | 11,10,9,6 | 10+k | none |
| 13,13,10,10 | 7-7 | 11,10,10,7 | 8+k | none |
| 13,13,10,10 | 8-8 | 11,10,10,8 | 7+k | none |
| 13,13,10,10 | 9-10 | 11,10,10,9 | 6+k | none |
| 13,13,11,10 | 1-1 | 10,10,9,5 | 13+k | none |
| 13,13,11,10 | 2-5 | 11,10,9,5 | 12+k | none |
| 13,13,11,10 | 6-6 | 11,10,9,6 | 11+k | none |
| 13,13,11,10 | 7-7 | 11,10,10,7 | 9+k | none |
| 13,13,11,10 | 8-8 | 11,10,10,8 | 8+k | none |
| 13,13,11,10 | 9-10 | 11,11,10,9 | 6+k | none |
| 13,13,12,10 | 1-5 | 11,10,9,5 | 13+k | 5 |
| 13,13,12,10 | 6-6 | 11,11,9,6 | 11+k | none |
| 13,13,12,10 | 7-7 | 11,11,10,7 | 9+k | none |
| 13,13,12,10 | 8-8 | 11,11,10,8 | 8+k | none |
| 13,13,12,10 | 9-10 | 11,11,10,9 | 7+k | none |
| 13,13,13,10 | 1-2 | 11,10,9,5 | 14+k | none |
| 13,13,13,10 | 3-5 | 11,11,9,5 | 13+k | 5 |
| 13,13,13,10 | 6-6 | 11,11,9,6 | 12+k | 6 |
| 13,13,13,10 | 7-7 | 11,11,10,7 | 10+k | none |
| 13,13,13,10 | 8-8 | 11,11,10,8 | 9+k | none |
| 13,13,13,10 | 9-9 | 11,11,10,9 | 8+k | none |
| 13,13,13,10 | 10-10 | 12,11,10,9 | 7+k | none |
| 13,13,11,11 | 1-2 | 11,10,9,5 | 13+k | none |
| 13,13,11,11 | 3-5 | 11,10,10,5 | 12+k | none |
| 13,13,11,11 | 6-6 | 11,10,10,6 | 11+k | none |
| 13,13,11,11 | 7-7 | 11,10,10,7 | 10+k | none |
| 13,13,11,11 | 8-8 | 11,11,10,8 | 8+k | none |
| 13,13,11,11 | 9-10 | 11,11,10,9 | 7+k | none |
| 13,13,11,11 | 11-11 | 12,11,10,10 | 5+k | none |
| 13,13,12,11 | 1-2 | 11,10,9,5 | 14+k | none |
| 13,13,12,11 | 3-4 | 11,10,10,5 | 13+k | none |
| 13,13,12,11 | 5-5 | 11,11,10,5 | 12+k | none |
| 13,13,12,11 | 6-6 | 11,11,10,6 | 11+k | none |
| 13,13,12,11 | 7-7 | 11,11,10,7 | 10+k | none |
| 13,13,12,11 | 8-8 | 11,11,10,8 | 9+k | none |
| 13,13,12,11 | 9-9 | 11,11,10,9 | 8+k | none |
| 13,13,12,11 | 10-10 | 12,11,10,9 | 7+k | none |
| 13,13,12,11 | 11-11 | 12,11,10,10 | 6+k | none |
| 13,13,13,11 | 1-1 | 11,10,9,5 | 15+k | none |
| 13,13,13,11 | 2-2 | 11,11,9,5 | 14+k | none |
| 13,13,13,11 | 3-5 | 11,11,10,5 | 13+k | 5 |
| 13,13,13,11 | 6-6 | 11,11,10,6 | 12+k | 6 |
| 13,13,13,11 | 7-7 | 11,11,10,7 | 11+k | 7 |
| 13,13,13,11 | 8-8 | 11,11,10,8 | 10+k | 8 |
| 13,13,13,11 | 9-10 | 12,11,10,9 | 8+k | 10 |
| 13,13,13,11 | 11-11 | 12,11,10,10 | 7+k | 11 |
| 13,13,12,12 | 1-3 | 11,10,10,5 | 14+k | none |
| 13,13,12,12 | 4-5 | 11,11,10,5 | 13+k | 5 |
| 13,13,12,12 | 6-6 | 11,11,10,6 | 12+k | 6 |
| 13,13,12,12 | 7-7 | 11,11,10,7 | 11+k | 7 |
| 13,13,12,12 | 8-8 | 11,11,11,8 | 9+k | none |
| 13,13,12,12 | 9-10 | 12,11,11,9 | 7+k | none |
| 13,13,12,12 | 11-12 | 12,11,11,10 | 6+k | 12 |
| 13,13,13,12 | 1-5 | 11,11,10,5 | 14+k | 4,5 |
| 13,13,13,12 | 6-6 | 11,11,10,6 | 13+k | 6 |
| 13,13,13,12 | 7-7 | 11,11,10,7 | 12+k | 7 |
| 13,13,13,12 | 8-8 | 12,11,11,8 | 9+k | none |
| 13,13,13,12 | 9-10 | 12,11,11,9 | 8+k | 10 |
| 13,13,13,12 | 11-12 | 12,12,11,10 | 6+k | 12 |
| 13,13,13,13 | 1-3 | 11,11,10,5 | 15+k | 3 |
| 13,13,13,13 | 4-5 | 11,11,11,5 | 14+k | 4,5 |
| 13,13,13,13 | 6-6 | 11,11,11,6 | 13+k | 6 |
| 13,13,13,13 | 7-7 | 12,11,11,7 | 11+k | 7 |
| 13,13,13,13 | 8-8 | 12,11,11,8 | 10+k | 8 |
| 13,13,13,13 | 9-9 | 12,11,11,9 | 9+k | 9 |
| 13,13,13,13 | 10-10 | 12,12,11,9 | 8+k | 10 |
| 13,13,13,13 | 11-12 | 12,12,11,10 | 7+k | 11,12 |
| 13,13,13,13 | 13-13 | 12,12,11,11 | 6+k | 13 |

## Cap-six lifts of all thirty cap-five survivors

| y,z,k | j interval | (g2,g3,g4,g5,g6) | Q(j) | interval maximum |
|---|---|---|---|---|
| 12,10,5 | 1-1 | 11,11,9,6,6 | 10+j | 11 |
| 12,10,5 | 2-5 | 11,11,10,6,6 | 9+j | 14 |
| 12,12,5 | 1-2 | 11,11,10,6,6 | 11+j | 13 |
| 12,12,5 | 3-3 | 11,11,11,6,6 | 10+j | 13 |
| 12,12,5 | 4-5 | 12,11,11,6,6 | 9+j | 14 |
| 12,12,6 | 1-1 | 11,11,10,7,6 | 11+j | 12 |
| 12,12,6 | 2-2 | 11,11,11,7,6 | 10+j | 12 |
| 12,12,6 | 3-6 | 12,11,11,7,6 | 9+j | 15 |
| 12,12,7 | 1-1 | 11,11,11,7,6 | 11+j | 12 |
| 12,12,7 | 2-6 | 12,11,11,8,6 | 9+j | 15 |
| 12,12,7 | 7-7 | 12,12,11,8,7 | 7+j | 14 |
| 12,12,12 | 1-1 | 12,11,11,11,6 | 11+j | 12 |
| 12,12,12 | 2-5 | 12,12,11,11,6 | 10+j | 15 |
| 12,12,12 | 6-6 | 12,12,12,11,6 | 9+j | 15 |
| 12,12,12 | 7-7 | 12,12,12,11,7 | 8+j | 15 |
| 12,12,12 | 8-8 | 13,12,12,11,8 | 6+j | 14 |
| 12,12,12 | 9-9 | 13,12,12,11,9 | 5+j | 14 |
| 12,12,12 | 10-10 | 13,12,12,11,10 | 4+j | 14 |
| 12,12,12 | 11-11 | 13,12,12,12,10 | 3+j | 14 |
| 12,12,12 | 12-12 | 13,12,12,12,11 | 2+j | 14 |
| 13,10,5 | 1-1 | 11,11,9,6,6 | 11+j | 12 |
| 13,10,5 | 2-4 | 11,11,10,6,6 | 10+j | 14 |
| 13,10,5 | 5-5 | 12,11,10,6,6 | 9+j | 14 |
| 13,10,6 | 1-3 | 11,11,10,7,6 | 10+j | 13 |
| 13,10,6 | 4-6 | 12,11,10,7,6 | 9+j | 15 |
| 13,11,5 | 1-3 | 11,11,10,6,6 | 11+j | 14 |
| 13,11,5 | 4-5 | 12,11,10,6,6 | 10+j | 15 |
| 13,11,6 | 1-2 | 11,11,10,7,6 | 11+j | 13 |
| 13,11,6 | 3-5 | 12,11,10,7,6 | 10+j | 15 |
| 13,11,6 | 6-6 | 12,12,11,7,6 | 8+j | 14 |
| 13,11,7 | 1-1 | 11,11,10,7,6 | 12+j | 13 |
| 13,11,7 | 2-4 | 12,11,10,8,6 | 10+j | 14 |
| 13,11,7 | 5-6 | 12,12,11,8,6 | 8+j | 14 |
| 13,11,7 | 7-7 | 12,12,11,8,7 | 7+j | 14 |
| 13,11,8 | 1-3 | 12,11,10,8,6 | 11+j | 14 |
| 13,11,8 | 4-6 | 12,12,11,9,6 | 8+j | 14 |
| 13,11,8 | 7-7 | 12,12,11,9,7 | 7+j | 14 |
| 13,11,8 | 8-8 | 12,12,11,9,8 | 6+j | 14 |
| 13,11,10 | 1-1 | 12,11,10,9,6 | 12+j | 13 |
| 13,11,10 | 2-6 | 12,12,11,10,6 | 9+j | 15 |
| 13,11,10 | 7-7 | 12,12,11,10,7 | 8+j | 15 |
| 13,11,10 | 8-8 | 12,12,11,10,8 | 7+j | 15 |
| 13,11,10 | 9-9 | 12,12,11,10,9 | 6+j | 15 |
| 13,11,10 | 10-10 | 13,12,11,10,10 | 4+j | 14 |
| 13,11,11 | 1-5 | 12,12,11,10,6 | 10+j | 15 |
| 13,11,11 | 6-6 | 12,12,11,11,6 | 9+j | 15 |
| 13,11,11 | 7-7 | 12,12,11,11,7 | 8+j | 15 |
| 13,11,11 | 8-8 | 12,12,11,11,8 | 7+j | 15 |
| 13,11,11 | 9-9 | 13,12,11,11,9 | 5+j | 14 |
| 13,11,11 | 10-10 | 13,12,11,11,10 | 4+j | 14 |
| 13,11,11 | 11-11 | 13,12,12,11,10 | 3+j | 14 |
| 13,12,4 | 1-3 | 11,11,10,5,6 | 12+j | 15 |
| 13,12,4 | 4-4 | 12,11,11,5,6 | 10+j | 14 |
| 13,12,5 | 1-2 | 11,11,10,6,6 | 12+j | 14 |
| 13,12,5 | 3-5 | 12,11,11,6,6 | 10+j | 15 |
| 13,12,6 | 1-1 | 11,11,10,7,6 | 12+j | 13 |
| 13,12,6 | 2-4 | 12,11,11,7,6 | 10+j | 14 |
| 13,12,6 | 5-6 | 12,12,11,7,6 | 9+j | 15 |
| 13,12,7 | 1-1 | 12,11,11,7,6 | 11+j | 12 |
| 13,12,7 | 2-3 | 12,11,11,8,6 | 10+j | 13 |
| 13,12,7 | 4-6 | 12,12,11,8,6 | 9+j | 15 |
| 13,12,7 | 7-7 | 12,12,11,8,7 | 8+j | 15 |
| 13,12,10 | 1-1 | 12,12,11,9,6 | 11+j | 12 |
| 13,12,10 | 2-6 | 12,12,11,10,6 | 10+j | 16 |
| 13,12,10 | 7-7 | 12,12,11,10,7 | 9+j | 16 |
| 13,12,10 | 8-8 | 12,12,12,10,8 | 7+j | 15 |
| 13,12,10 | 9-9 | 13,12,12,10,9 | 5+j | 14 |
| 13,12,10 | 10-10 | 13,12,12,10,10 | 4+j | 14 |
| 13,12,12 | 1-5 | 12,12,11,11,6 | 11+j | 16 |
| 13,12,12 | 6-6 | 12,12,12,11,6 | 10+j | 16 |
| 13,12,12 | 7-7 | 13,12,12,11,7 | 8+j | 15 |
| 13,12,12 | 8-8 | 13,12,12,11,8 | 7+j | 15 |
| 13,12,12 | 9-9 | 13,12,12,11,9 | 6+j | 15 |
| 13,12,12 | 10-10 | 13,13,12,11,10 | 4+j | 14 |
| 13,12,12 | 11-11 | 13,13,12,12,10 | 3+j | 14 |
| 13,12,12 | 12-12 | 13,13,12,12,11 | 2+j | 14 |
| 13,13,3 | 1-3 | 11,11,11,5,6 | 11+j | 14 |
| 13,13,4 | 1-2 | 11,11,11,5,6 | 12+j | 14 |
| 13,13,4 | 3-4 | 12,11,11,5,6 | 11+j | 15 |
| 13,13,5 | 1-1 | 11,11,11,6,6 | 12+j | 13 |
| 13,13,5 | 2-4 | 12,11,11,6,6 | 11+j | 15 |
| 13,13,5 | 5-5 | 12,12,11,6,6 | 10+j | 15 |
| 13,13,6 | 1-3 | 12,11,11,7,6 | 11+j | 14 |
| 13,13,6 | 4-6 | 12,12,11,7,6 | 10+j | 16 |
| 13,13,7 | 1-1 | 12,11,11,7,6 | 12+j | 13 |
| 13,13,7 | 2-2 | 12,11,11,8,6 | 11+j | 13 |
| 13,13,7 | 3-6 | 12,12,11,8,6 | 10+j | 16 |
| 13,13,7 | 7-7 | 12,12,12,8,7 | 8+j | 15 |
| 13,13,8 | 1-1 | 12,11,11,8,6 | 12+j | 13 |
| 13,13,8 | 2-3 | 12,12,11,8,6 | 11+j | 14 |
| 13,13,8 | 4-5 | 12,12,11,9,6 | 10+j | 15 |
| 13,13,8 | 6-6 | 12,12,12,9,6 | 9+j | 15 |
| 13,13,8 | 7-7 | 12,12,12,9,7 | 8+j | 15 |
| 13,13,8 | 8-8 | 12,12,12,9,8 | 7+j | 15 |
| 13,13,9 | 1-4 | 12,12,11,9,6 | 11+j | 15 |
| 13,13,9 | 5-6 | 12,12,12,9,6 | 10+j | 16 |
| 13,13,9 | 7-7 | 12,12,12,10,7 | 8+j | 15 |
| 13,13,9 | 8-8 | 12,12,12,10,8 | 7+j | 15 |
| 13,13,9 | 9-9 | 13,12,12,10,9 | 5+j | 14 |
| 13,13,10 | 1-1 | 12,12,11,9,6 | 12+j | 13 |
| 13,13,10 | 2-3 | 12,12,11,10,6 | 11+j | 14 |
| 13,13,10 | 4-6 | 12,12,12,10,6 | 10+j | 16 |
| 13,13,10 | 7-7 | 12,12,12,10,7 | 9+j | 16 |
| 13,13,10 | 8-8 | 13,12,12,10,8 | 7+j | 15 |
| 13,13,10 | 9-9 | 13,12,12,10,9 | 6+j | 15 |
| 13,13,10 | 10-10 | 13,12,12,10,10 | 5+j | 15 |
| 13,13,11 | 1-2 | 12,12,11,10,6 | 12+j | 14 |
| 13,13,11 | 3-5 | 12,12,12,10,6 | 11+j | 16 |
| 13,13,11 | 6-6 | 12,12,12,11,6 | 10+j | 16 |
| 13,13,11 | 7-7 | 13,12,12,11,7 | 8+j | 15 |
| 13,13,11 | 8-8 | 13,12,12,11,8 | 7+j | 15 |
| 13,13,11 | 9-9 | 13,12,12,11,9 | 6+j | 15 |
| 13,13,11 | 10-11 | 13,13,12,11,10 | 4+j | 15 |
| 13,13,12 | 1-1 | 12,12,11,11,6 | 12+j | 13 |
| 13,13,12 | 2-5 | 12,12,12,11,6 | 11+j | 16 |
| 13,13,12 | 6-6 | 13,12,12,11,6 | 10+j | 16 |
| 13,13,12 | 7-7 | 13,12,12,11,7 | 9+j | 16 |
| 13,13,12 | 8-8 | 13,12,12,11,8 | 8+j | 16 |
| 13,13,12 | 9-9 | 13,13,12,11,9 | 6+j | 15 |
| 13,13,12 | 10-10 | 13,13,12,11,10 | 5+j | 15 |
| 13,13,12 | 11-11 | 13,13,12,12,10 | 4+j | 15 |
| 13,13,12 | 12-12 | 13,13,12,12,11 | 3+j | 15 |
| 13,13,13 | 1-4 | 12,12,12,11,6 | 12+j | 16 |
| 13,13,13 | 5-5 | 13,12,12,11,6 | 11+j | 16 |
| 13,13,13 | 6-6 | 13,12,12,12,6 | 10+j | 16 |
| 13,13,13 | 7-7 | 13,12,12,12,7 | 9+j | 16 |
| 13,13,13 | 8-8 | 13,13,12,12,8 | 7+j | 15 |
| 13,13,13 | 9-9 | 13,13,12,12,9 | 6+j | 15 |
| 13,13,13 | 10-11 | 13,13,12,12,10 | 5+j | 16 |
| 13,13,13 | 12-12 | 13,13,13,12,11 | 3+j | 15 |
| 13,13,13 | 13-13 | 13,13,13,12,12 | 2+j | 15 |

No interval in the second table reaches 18.


\clearpage

# Appendix E. Complete residual-tail reconstruction

For $(a,b)=(13,16)$ and $t=m-224>0$, put $g_{13}=0$ and use the thresholds $g_2,\ldots,g_{12}$ from Appendix C. Every actual residual degree is in $\{1,\ldots,13\}$. Let

$$z_h=\#\{u:\rho_u\ge h\},\qquad r=16+\sum_{h=2}^{13}z_h.$$

The thresholds and the demand ledger give $z_h\ge g_h$ and $\lambda=S-r-2t\ge0$. Substitution yields

$$Q-(16+2t)=\lambda+\sum_{h=2}^{13}(z_h-g_h).$$

Thus the residual rows are exactly those reconstructed by assigning this many nonnegative integer units to $\lambda,z_2-g_2,\ldots,z_{13}-g_{13}$, imposing $16\ge z_2\ge\cdots\ge z_{13}\ge0$. This means completeness of the integer relaxation; no sufficiency for an actual graph is asserted. A monotone tail determines a unique histogram, with multiplicities $16-z_2$ at one, $z_h-z_{h+1}$ at $h=2,\ldots,12$, and $z_{13}$ at thirteen. The thresholds $g_h$ need not themselves be monotone, so monotonicity must be imposed after the slack is assigned.

At $t=1$, at most three units are available. Applying this rule to the 100 profiles in Appendix C gives the following complete distribution.

| $Q$ | $\lambda$ | Rows |
|---:|---:|---:|
| 18 | 0 | 64 |
| 19 | 0 | 96 |
| 19 | 1 | 29 |
| 20 | 0 | 42 |
| 20 | 1 | 18 |
| 20 | 2 | 6 |
| 21 | 0 | 9 |
| 21 | 1 | 5 |
| 21 | 2 | 2 |
| 21 | 3 | 1 |

The total is 272. Appendix C shows that every high-score profile containing a zero has $p=12,x=12$ and $Q=18$. Such a profile has no available slack at $t=1$. Consequently every row with positive ledger slack has every demand positive. Its definition then gives $s_i=d_i-R_i$ at each label, so

$$S=\sum_i d_i-\sum_i R_i=2(r+t)-r=r+2t,$$

contradicting $\lambda>0$. This excludes exactly 61 rows. The remaining 211 rows are all printed in Appendix H. Checking that list against the reconstruction rule is a finite proof obligation; the count alone is not a completeness certificate.

At $t=2$, only the six $Q=20$ profiles and the unique $Q=21$ profile remain. The former have no available slack. For $s=(3^{13})$, $g_2=g_3=9$ and all higher thresholds vanish. Its one unit may be placed only in $\lambda$, in $z_2$, or in $z_4$; adding it at $z_3$ or any higher position violates monotonicity. This gives nine rows in total. The positive-ledger-slack row is $(s,\rho)=((3^{13}),(1^7,3^9))$ and is impossible by the same positive-demand argument. The other eight rows are all printed in Appendix F.

For the ledger-tight rows, equality in $\sum_i\max(0,d_i-R_i)\ge\sum_i(d_i-R_i)$ implies $d_i-R_i\ge0$ at every label. Hence $d_i=R_i+s_i$ also at zero-demand labels. This is the precise tightness fact used in the envelope argument.


\clearpage

# Appendix F. Eight explicit inequalities at 226 edges

The reconstruction in Appendix E leaves the following eight tight rows.

## F.2. Tight demand and selected excess

Every one of the remaining eight rows has

```text
S=r+4.
```

Since always

```text
S=sum_i max(0,d_i-R_i) >= sum_i(d_i-R_i)=r+4,
```

and every displayed demand is positive, equality forces

```text
s_i=d_i-R_i                              (2.1)
```

for every label.

Let

```text
x_i = selected degree of label i,
e_i = x_i-s_i >=0,
M   = sum_i x_i = sum_u q_u,
E   = sum_i e_i = M-S.
```

Fix a selected incidence `ui->w`. The universal bridge gives

```text
d_i <= rho_u+q_u-1                       (2.2)
q_u+p_u <= R_i+x_i.                       (2.3)
```

Substitute `d_i=R_i+s_i` and `x_i=s_i+e_i`. Eliminating `R_i,q_u` gives

```text
e_i >= p_u-rho_u+1.                       (2.4)
```

Also

```text
p_u <= rho_u+2,
```

so with

```text
alpha_u=max(0,p_u-rho_u+1),
```

we have

```text
0<=alpha_u<=3.                             (2.5)
```

The selected-incidence forcing lemma also gives

```text
s_i<=rho_u                                 (2.6)
```

on every selected incidence. In particular, if `rho_u<min_i s_i`, then `q_u=0`.

## F.3. Label-side upper bound

Define

```text
B0=sum_u q_u alpha_u.
```

Each of the `q_u` selected incidences from source `u` lands at a label with `e_i>=alpha_u`. Since `alpha_u<=3`, summing incidence by incidence gives

```text
B0 <= sum_i x_i min(e_i,3).                (3.1)
```

For every `s>=0,e>=0`,

```text
(s+e) min(e,3) <= (s+3)e.                 (3.2)
```

Indeed this is immediate for `e<=3`, while for `e>=3` it is equivalent to `3s+3e <= se+3e`, i.e. `s(e-3)>=0`.

Let

```text
c=max_i s_i + 3.
```

Then (3.1)--(3.2) give

```text
B0 <= c sum_i e_i = cE.                   (3.3)
```

Thus any actual graph must satisfy `B0<=cE`.

## F.4. Supplement Hall tails

For `k>=1`, define

```text
H_k = sum_{u:q_u>=k+1} q_u
      - sum_{w:rho_w+q_w>=k} p_w.
```

The supplement-forcing lemma says that every selected arc from source `u` to supplement `w` satisfies

```text
rho_w+q_w >= q_u-1.
```

Hence every outgoing selected arc from a source with `q_u>=k+1` must land at a vertex counted in the second term. The selected orientations form genuine source-to-supplement arcs, so

```text
H_k<=0                                    (4.1)
```

for every `k`.

No pair-capacity inequality, cumulative-threshold LP, Farkas certificate, or selected-label-group source cap is used below.

## F.5. Tiny source certificates

For a source of residual degree `rho`, define

```text
h_k(rho,q,p)=q*1[q>=k+1]-p*1[rho+q>=k].
```

For each residual row in the table below, choose denominator `D`, put `c=max s+3`, and use the listed nonzero integer weights `z_k`.

For every allowed source type

```text
0<=q<=13-rho,
0<=p<=rho+2,
q+p<=15,
```

with the additional necessary condition `q=0` whenever `rho<min s`, direct integer minimisation of the displayed piecewise-linear expression gives

```text
D*q*(alpha-c) + sum_k z_k h_k(rho,q,p) >= L_rho.   (5.1)
```

The table records the exact minima `L_rho`. Each is checked over the displayed finite integer source domain; the verification companion gives corroborating replay instructions.

| demand `s` | residual histogram `rho` | `D` | `c` | nonzero `z_k` | exact `L_rho` by residual degree | `delta` |
|---|---|---:|---:|---|---|---:|
| `(2^2,3^11)` | `(1^7,2,3^8)` | 2 | 6 | `z2=6,z5=z6=z8=1` | `L1=0,L2=-42,L3=-50` | 1 |
| `(2,3^12)` | `(1^7,3^9)` | 2 | 6 | `z2=3,z3=4,z6=z8=1` | `L1=0,L3=-50` | 3 |
| `(3^13)` | `(1^7,3^8,4)` | 2 | 6 | `z2=7,z6=z7=1` | `L1=0,L3=-48,L4=-60` | 12 |
| `(3^13)` | `(1^6,2,3^9)` | 2 | 6 | `z2=3,z3=4,z6=z8=1` | `L1=0,L2=-12,L3=-50` | 3 |
| `(3^4,4^9)` | `(1^6,3^2,4^8)` | 3 | 7 | `z2=11,z5=z6=1,z7=2` | `L1=0,L3=-90,L4=-102` | 4 |
| `(3^2,4^11)` | `(1^5,2,3,4^9)` | 3 | 7 | `z2=6,z3=z4=3,z6=z7=z8=1` | `L1=0,L2=-24,L3=-90,L4=-102` | 6 |
| `(3,4^12)` | `(1^5,2,4^10)` | 2 | 7 | `z2=z3=z5=3,z8=1` | `L1=0,L2=-12,L4=-70` | 1 |
| `(4^13)` | `(1^5,3,4^10)` | 2 | 7 | `z1=1,z2=5,z4=z5=z6=z7=1` | `L1=-3,L3=-30,L4=-68` | `3/2` |

Here

```text
delta = cS + (1/D) sum_rho n_rho L_rho,
```

where `n_rho` is the multiplicity of residual degree `rho` in the row. All eight values are strictly positive.

Now sum (5.1) over all sixteen sources. The `h_k` terms sum to `H_k`, so

```text
D(B0-cM) + sum_k z_k H_k >= sum_rho n_rho L_rho.
```

By (4.1), every `H_k<=0` and every `z_k>=0`. Therefore

```text
D(B0-cM) >= sum_rho n_rho L_rho.
```

Adding `DcS` and using `E=M-S` gives

```text
B0-cE >= delta >0.                        (5.2)
```

Thus

```text
B0 > cE,                                  (5.3)
```

contradicting the necessary label-side inequality (3.3).

All eight nontrivial rows are impossible.


\clearpage

# Appendix G. Four exact monotone-envelope certificates

## G.1. Exact setup and the additional individual label cap

Use the selected/residual construction with

```text
a=13, b=16, t=m-224=1.
```

For labels, use demand `s_i`, F-degree `d_i`, residual degree `R_i` and selected degree `x_i`. At a source use residual degree `rho_u`, selected outdegree `q_u` and supplement indegree `p_u`. Write

```text
S=sum_i s_i, r=sum_u rho_u=sum_i R_i.
```

The threshold-slack reduction (Appendix E) leaves 211 rows with

```text
S=r+2.
```

Since `s_i=max(0,d_i-R_i)` and `sum_i(d_i-R_i)=r+2`, this equality forces

```text
d_i=R_i+s_i
```

at **every** label, including labels with zero demand. Also `x_i>=s_i`.

The bridge gives `s_i<=rho_u` on every selected incidence at `i`. Each source can be selected at a fixed label at most once because the selected cross-edges form a subset of the edges of a simple graph. Therefore define

```text
H_s = #{u:rho_u>=s},
Q_rho = min(13-rho, #{i:s_i<=rho}).
```

Every individual label of demand `s` and source of residual degree `rho` obeys

```text
Label domain:
  0<=R<=12-s,
  s<=x<=min(16-R,H_s).

Source domain:
  0<=q<=Q_rho,
  0<=p<=rho+2.                                    (1)
```

The label bound `R<=12-s` uses only `d_F<=12`, since F has thirteen vertices. The stronger isolated-C bound `d_F<=11` used in older models is **not** a premise here.

The supplement bound in (1) follows from the corrected degree identity

```text
deg_H(u)=(rho_u+q_u)+(15-q_u-p_u)=rho_u+15-p_u>=13.
```

It is `p<=rho+2`, not the previously rejected `rho+1` tightening. Since `q<=13-rho`, the rectangular source domain already ensures `q+p<=15`.

## G.2. The monotone-incidence inequality

For a label state define

```text
d=R+s, v=16-R-x.
```

For a source state define

```text
alpha=rho+q-1, w=16-q-p.
```

On every selected source-label incidence the bridge gives

```text
s<=rho,
d<=alpha,
v<=w.                                             (2)
```

Consequently any coordinatewise nondecreasing function `Phi(s,d,v)` obeys

```text
sum_i x_i Phi(s_i,R_i+s_i,16-R_i-x_i)
  <= sum_u q_u Phi(rho_u,rho_u+q_u-1,16-q_u-p_u).  (3)
```

Apply monotonicity separately to each selected edge and then sum. Every label occurs exactly `x_i` times and every source exactly `q_u` times. This is a direct count on the actual selected incidences; no converse construction from an integer relaxation is assumed.

The useful new simple term is `s*v`. Both factors in (2) are nonnegative, so

```text
s*v <= rho*w
```

on each selected incidence. It retains how demand interacts with the remaining cross-capacity, which the previous aggregate excess estimate discarded.

## G.3. Resource identities and supplement tails

The exact identities are

```text
sum_i R_i=r,
sum_i x_i=sum_u q_u,
sum_u q_u=sum_u p_u.                               (4)
```

For each `j>=1`, let

```text
T_j = sum_{u:q_u>=j+1} q_u
      - sum_{w:rho_w+q_w>=j} p_w.
```

Every selected arc from a source with `q_u>=j+1` has a supplement satisfying `rho_w+q_w>=q_u-1>=j`. Therefore

```text
T_j<=0.                                            (5)
```

The selected orientations count each arc once; the supplement's total incoming degree is `p_w`.

## G.4. Exact scalar envelopes

Choose nonnegative integer coefficients `lambda,c,mu,tau_j`, and a nondecreasing potential `Phi`. Define the two finite envelopes over the entire domains in (1):

```text
ell_s = min [lambda*R + c*x
             + x*Phi(s,R+s,16-R-x)],

sigma_rho = min [mu*(q-p)-c*q
                  + sum_j tau_j*(q*1[q>=j+1]-p*1[rho+q>=j])
                  - q*Phi(rho,rho+q-1,16-q-p)].      (6)
```

Let `n_s` be the demand multiplicities and `n_rho` the residual-degree multiplicities. A necessary condition for an actual graph is

```text
gap := sum_s n_s*ell_s + sum_rho n_rho*sigma_rho
       - lambda*r <= 0.                            (7)
```

**Proof.** The minima in (6) are lower bounds for the values at the actual vertex states. Sum those bounds over all labels and sources. The `c` and `mu` terms cancel by (4). The `tau` terms are nonpositive by (5); the potential difference is nonpositive by (3). The only remaining contribution is `lambda*sum_i R_i=lambda*r`. This proves (7). Thus any strictly positive value is an exact contradiction. No optimizer, transport matrix or numerical infeasibility decision is a premise. QED.

## G.5. Four explicit potentials

Use the monotone generators

```text
V(s,d,v)=s*v,
E_k(s,d,v)=1[d+v>=16-k],
J(s,d,v)=1[s>=2],
R_{D,V0}(s,d,v)=1[d>=D and v>=V0].
```

All variables lie in a nonnegative domain. Each generator is coordinatewise nondecreasing, and each coefficient below is nonnegative. At a label, `E_k=1[x-s<=k]`; at a source, `E_k=1[p<=rho+k-1]`.

### Certificate B1

```text
lambda=150, c=88, mu=150,
tau_2=11, tau_3=107, tau_5=5,

Phi = 4V + 51E_0 + 40E_1 + 40E_2 + 150J
      + 91R_{1,13} + 142R_{1,14}
      + 36R_{2,10} + 37R_{2,11} + 61R_{2,12}
      + 21R_{4,7} + 21R_{4,8} + 32R_{4,9} + R_{4,10}.
```

This single certificate excludes 195 of the 211 tight rows.

### Certificate B2

```text
lambda=15, c=8, mu=17,
tau_2=3, tau_3=4,

Phi = 3E_0 + 6E_1 + 3E_2 + 14J + 11R_{1,14}
      + 3R_{2,7} + 2R_{2,8} + 5R_{2,9}
      + 5R_{2,10} + 5R_{2,11} + 7R_{2,12} + 8R_{2,13}.
```

It excludes 79 rows in total, including 13 not excluded by B1.

### Certificate B3

```text
lambda=18, c=4, mu=24,
tau_2=2, tau_3=4,

Phi = V + 4E_0 + 8E_1 + 3E_2 + 7J
      + 2R_{1,12} + 11R_{1,13} + 14R_{1,14}
      + 3R_{3,11} + R_{3,12} + R_{4,9} + 3R_{4,10}.
```

It excludes 24 rows in total, including the next two rows missed by B1 and B2.

### Certificate C1

```text
lambda=25, c=28, mu=0,
tau_2=22, tau_4=6,
Phi=V=s*v.
```

It excludes ten rows in total, including the sole row missed by B1, B2 and B3. All unlisted `tau_j` are zero.

Together the four certificates cover

```text
195 + 13 + 2 + 1 = 211
```

distinct rows. This includes the four zero-demand rows and all 207 positive-demand rows. Four is a convenient explicit cover; **minimality is not claimed**. This count concerns a different profile domain and different potentials from the earlier fixed-potential two-template result on seven hard N30 rows.

## G.6. The final exceptional row, written out

The row missed by the first three certificates is

```text
s=(2,5^12),
rho=(1^4,2,4,5^10),
S=62, r=60.
```

For C1, the exact minima in (6) are

```text
ell_2=112, ell_5=415,
sigma_1=0, sigma_2=-138, sigma_4=-232, sigma_5=-322.
```

Consequently

```text
gap = 112 + 12*415 -138 -232 -10*322 -25*60
    = 2 > 0.
```

This contradicts (7). The complete appendix (Appendix H) gives the same type of explicit arithmetic for every one of the 211 rows; the minimum assigned gap is one.

## G.7. Why the envelope tables can be checked without optimization

For each fixed label value `x`, the expression in (6) is linear in `R` between the rectangle breakpoints. It therefore suffices to check the endpoints

```text
R=0, R=min(12-s,16-x),
R=D-s-1, D-s,
R=16-V0-x, 17-V0-x
```

for the active rectangles, retaining only values inside the allowed interval. These include the integer states immediately before and after each rectangle indicator changes. The diagonal indicators depend only on `x-s`; the `s*v` term is linear in R for fixed x.

For each fixed source value `q`, the source expression is linear in `p` between indicator changes. It suffices to check

```text
p=0, rho+2;
p=rho+k-1, rho+k for each active E_k;
p=16-q-V0, 17-q-V0 for each active rectangle whose
  source degree rho+q-1 is at least D.
```

Again retain only admissible p values. These formulas account for both sides of every discrete jump, including the endpoints `p=rho+2` and `R=12-s`. There is no hidden minimization over fractional vertex states.


\clearpage

```{=latex}
\begin{landscape}
```

# Appendix H. All 211 tight endpoint rows

Each positive gap is sum(n_s * ell_s) + sum(n_rho * sigma_rho) - lambda*r. Every template is evaluated on every tight row before the first successful one is assigned.

| Template | Demand s | Residual rho | Label minima ell_s | Source minima sigma_rho | Positive gap |
|---|---|---|---|---|---:|
| B1 | (0,2,3^11) | (1^7,2,3^8) | {0: 0, 2: 1546, 3: 2247} | {1: -469, 2: -1480, 3: -2010} | 470 |
| B1 | (0,3^12) | (1^7,3^9) | {0: 0, 3: 2247} | {1: -469, 3: -2010} | 491 |
| B1 | (0,3,4^11) | (1^6,3,4^9) | {0: 0, 3: 2247, 4: 2756} | {1: -469, 3: -1905, 4: -2268} | 682 |
| B1 | (0,4^12) | (1^6,4^10) | {0: 0, 4: 2756} | {1: -469, 4: -2268} | 678 |
| B3 | (1^2,2^2,3^9) | (1^8,2,3^7) | {1: 61, 2: 156, 3: 234} | {1: -72, 2: -141, 3: -180} | 5 |
| B3 | (1^2,3^11) | (1^7,2,3^8) | {1: 61, 3: 232} | {1: -72, 2: -134, 3: -180} | 2 |
| B2 | (1,2^12) | (1^9,2^7) | {1: 31, 2: 152} | {1: -51, 2: -150} | 1 |
| B2 | (1,2^5,3^7) | (1^8,2^2,3^6) | {1: 31, 2: 152, 3: 192} | {1: -51, 2: -150, 3: -150} | 77 |
| B2 | (1,2^3,3^9) | (1^7,2^2,3^7) | {1: 31, 2: 152, 3: 192} | {1: -51, 2: -148, 3: -150} | 32 |
| B2 | (1,2^2,3^10) | (1^7,2,3^8) | {1: 31, 2: 152, 3: 192} | {1: -51, 2: -147, 3: -150} | 56 |
| B1 | (1,2^2,3^6,4^4) | (1^7,2,3^4,4^4) | {1: 512, 2: 1546, 3: 2247, 4: 2756} | {1: -469, 2: -1836, 3: -2010, 4: -2268} | 329 |
| B1 | (1,2,3^11) | (1^7,2,3^7,4) | {1: 512, 2: 1546, 3: 2247} | {1: -469, 2: -1480, 3: -2010, 4: -2268} | 574 |
| B1 | (1,2,3^11) | (1^7,3^9) | {1: 512, 2: 1546, 3: 2247} | {1: -469, 3: -2010} | 302 |
| B2 | (1,2,3^11) | (1^6,2^2,3^8) | {1: 31, 2: 152, 3: 192} | {1: -51, 2: -136, 3: -150} | 7 |
| B1 | (1,2,3^7,4^4) | (1^7,3^5,4^4) | {1: 512, 2: 1546, 3: 2247, 4: 2756} | {1: -469, 3: -2010, 4: -2268} | 706 |
| B1 | (1,2,3^2,4^9) | (1^6,2,3,4^8) | {1: 512, 2: 1546, 3: 2247, 4: 2756} | {1: -469, 2: -1480, 3: -2010, 4: -2268} | 458 |
| B1 | (1,2,4^11) | (1^6,3,4^9) | {1: 512, 2: 1546, 4: 2756} | {1: -469, 3: -1905, 4: -2268} | 493 |
| B1 | (1,3^12) | (1^7,3^8,4) | {1: 512, 3: 2247} | {1: -469, 3: -2010, 4: -2268} | 595 |
| B1 | (1,3^12) | (1^6,2,3^9) | {1: 512, 3: 2247} | {1: -469, 2: -1321, 3: -2010} | 1 |
| B1 | (1,3^9,4^3) | (1^7,3^5,4^4) | {1: 512, 3: 2247, 4: 2756} | {1: -469, 3: -2010, 4: -2268} | 898 |
| B1 | (1,3^8,4^4) | (1^6,2,3^5,4^4) | {1: 512, 3: 2247, 4: 2756} | {1: -469, 2: -1321, 3: -2010, 4: -2268} | 405 |
| B1 | (1,3^7,4^5) | (1^6,2,3^4,4^5) | {1: 512, 3: 2247, 4: 2756} | {1: -469, 2: -1321, 3: -2010, 4: -2268} | 506 |
| B1 | (1,3^6,4^6) | (1^6,2,3^3,4^6) | {1: 512, 3: 2247, 4: 2756} | {1: -469, 2: -1321, 3: -2010, 4: -2268} | 607 |
| B1 | (1,3^3,4^9) | (1^6,3^2,4^8) | {1: 512, 3: 2247, 4: 2756} | {1: -469, 3: -2010, 4: -2268} | 479 |
| B1 | (1,3^2,4^10) | (1^6,3,4^9) | {1: 512, 3: 2247, 4: 2756} | {1: -469, 3: -2010, 4: -2268} | 580 |
| B1 | (1,3,4^11) | (1^6,3,4^8,5) | {1: 512, 3: 2247, 4: 2756} | {1: -469, 3: -1905, 4: -2268, 5: -2502} | 810 |
| B1 | (1,3,4^11) | (1^6,4^10) | {1: 512, 3: 2247, 4: 2756} | {1: -469, 4: -2268} | 681 |
| B1 | (1,3,4^11) | (1^5,2,3,4^9) | {1: 512, 3: 2247, 4: 2756} | {1: -469, 2: -1321, 3: -1905, 4: -2268} | 192 |
| B1 | (1,4^12) | (1^6,4^9,5) | {1: 512, 4: 2756} | {1: -469, 4: -2268, 5: -2502} | 806 |
| B1 | (1,4^12) | (1^5,2,4^10) | {1: 512, 4: 2756} | {1: -469, 2: -1321, 4: -2268} | 188 |
| B2 | (2^13) | (1^8,2^8) | {2: 152} | {1: -51, 2: -150} | 8 |
| B2 | (2^10,3^3) | (1^8,2^5,3^3) | {2: 152, 3: 192} | {1: -51, 2: -150, 3: -150} | 83 |
| B2 | (2^9,3^4) | (1^8,2^4,3^4) | {2: 152, 3: 192} | {1: -51, 2: -150, 3: -150} | 108 |
| B1 | (2^8,3^5) | (1^8,2^3,3^5) | {2: 1546, 3: 2247} | {1: -450, 2: -1836, 3: -2010} | 95 |
| B2 | (2^6,3^7) | (1^7,2^3,3^6) | {2: 152, 3: 192} | {1: -51, 2: -150, 3: -150} | 84 |
| B1 | (2^5,3^8) | (1^7,2^2,3^7) | {2: 1546, 3: 2247} | {1: -450, 2: -1836, 3: -2010} | 14 |
| B1 | (2^4,3^9) | (1^7,2^2,3^6,4) | {2: 1546, 3: 2247} | {1: -450, 2: -1836, 3: -2010, 4: -2268} | 307 |
| B1 | (2^4,3^9) | (1^7,2,3^8) | {2: 1546, 3: 2247} | {1: -450, 2: -1836, 3: -2010} | 391 |
| B2 | (2^4,3^9) | (1^6,2^3,3^7) | {2: 152, 3: 192} | {1: -51, 2: -148, 3: -150} | 41 |
| B1 | (2^4,3^5,4^4) | (1^7,2,3^4,4^4) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1836, 3: -2010, 4: -2268} | 795 |
| B1 | (2^3,3^10) | (1^7,2,3^7,4) | {2: 1546, 3: 2247} | {1: -450, 2: -1836, 3: -2010, 4: -2268} | 684 |
| B1 | (2^3,3^10) | (1^7,3^9) | {2: 1546, 3: 2247} | {1: -450, 3: -2010} | 768 |
| B2 | (2^3,3^10) | (1^6,2^2,3^8) | {2: 152, 3: 192} | {1: -51, 2: -147, 3: -150} | 66 |
| B1 | (2^3,3^7,4^3) | (1^7,2,3^4,4^4) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1836, 3: -2010, 4: -2268} | 987 |
| B2 | (2^3,3^6,4^4) | (1^6,2^2,3^4,4^4) | {2: 152, 3: 192, 4: 216} | {1: -51, 2: -147, 3: -150, 4: -164} | 46 |
| B1 | (2^3,3,4^9) | (1^6,2,3,4^8) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1836, 3: -2010, 4: -2268} | 549 |
| B1 | (2^3,4^10) | (1^6,2,4^9) | {2: 1546, 4: 2756} | {1: -450, 2: -1836, 4: -2268} | 650 |
| B1 | (2^2,3^11) | (1^7,2,3^7,5) | {2: 1546, 3: 2247} | {1: -450, 2: -1480, 3: -2010, 5: -2502} | 1357 |
| B1 | (2^2,3^11) | (1^7,2,3^6,4^2) | {2: 1546, 3: 2247} | {1: -450, 2: -1480, 3: -2010, 4: -2268} | 1333 |
| B1 | (2^2,3^11) | (1^7,3^8,4) | {2: 1546, 3: 2247} | {1: -450, 3: -2010, 4: -2268} | 1061 |
| B1 | (2^2,3^11) | (1^6,2^2,3^7,4) | {2: 1546, 3: 2247} | {1: -450, 2: -1480, 3: -2010, 4: -2268} | 561 |
| B1 | (2^2,3^11) | (1^6,2,3^9) | {2: 1546, 3: 2247} | {1: -450, 2: -1480, 3: -2010} | 289 |
| B2 | (2^2,3^11) | (1^5,2^3,3^8) | {2: 152, 3: 192} | {1: -51, 2: -136, 3: -150} | 28 |
| B1 | (2^2,3^7,4^4) | (1^6,2,3^5,4^4) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1480, 3: -2010, 4: -2268} | 693 |
| B1 | (2^2,3^6,4^5) | (1^6,2,3^4,4^5) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1480, 3: -2010, 4: -2268} | 794 |
| B1 | (2^2,3^5,4^6) | (1^6,2,3^3,4^6) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1480, 3: -2010, 4: -2268} | 895 |
| B1 | (2^2,3^4,4^7) | (1^6,2,3^2,4^7) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1480, 3: -2010, 4: -2268} | 996 |
| B1 | (2^2,3^3,4^8) | (1^6,2,3,4^8) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1480, 3: -2010, 4: -2268} | 1097 |
| B1 | (2^2,3^2,4^9) | (1^6,2,3,4^7,5) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1480, 3: -2010, 4: -2268, 5: -2502} | 1222 |
| B1 | (2^2,3^2,4^9) | (1^6,2,4^9) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1480, 4: -2268} | 1198 |
| B1 | (2^2,3^2,4^9) | (1^6,3^2,4^8) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268} | 926 |
| B1 | (2^2,3^2,4^9) | (1^5,2^2,3,4^8) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1480, 3: -2010, 4: -2268} | 426 |
| B1 | (2^2,3,4^10) | (1^6,3,4^9) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268} | 1027 |
| B1 | (2^2,4^11) | (1^6,3,4^8,5) | {2: 1546, 4: 2756} | {1: -450, 3: -1905, 4: -2268, 5: -2502} | 1257 |
| B1 | (2^2,4^11) | (1^6,4^10) | {2: 1546, 4: 2756} | {1: -450, 4: -2268} | 1128 |
| B1 | (2^2,4^11) | (1^5,2,3,4^9) | {2: 1546, 4: 2756} | {1: -450, 2: -1480, 3: -1905, 4: -2268} | 461 |
| B1 | (2,3^12) | (1^7,3^8,5) | {2: 1546, 3: 2247} | {1: -450, 3: -2010, 5: -2502} | 1378 |
| B1 | (2,3^12) | (1^7,3^7,4^2) | {2: 1546, 3: 2247} | {1: -450, 3: -2010, 4: -2268} | 1354 |
| B1 | (2,3^12) | (1^6,2,3^8,4) | {2: 1546, 3: 2247} | {1: -450, 2: -1321, 3: -2010, 4: -2268} | 741 |
| B1 | (2,3^12) | (1^6,3^10) | {2: 1546, 3: 2247} | {1: -450, 3: -2010} | 310 |
| B1 | (2,3^12) | (1^5,2^2,3^9) | {2: 1546, 3: 2247} | {1: -450, 2: -1321, 3: -2010} | 128 |
| B1 | (2,3^9,4^3) | (1^6,2,3^5,4^4) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1321, 3: -2010, 4: -2268} | 1044 |
| B1 | (2,3^8,4^4) | (1^6,2,3^5,4^3,5) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1321, 3: -2010, 4: -2268, 5: -2502} | 1169 |
| B1 | (2,3^8,4^4) | (1^6,2,3^4,4^5) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1321, 3: -2010, 4: -2268} | 1145 |
| B1 | (2,3^8,4^4) | (1^6,3^6,4^4) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268} | 714 |
| B1 | (2,3^8,4^4) | (1^5,2^2,3^5,4^4) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1321, 3: -2010, 4: -2268} | 532 |
| B1 | (2,3^7,4^5) | (1^6,2,3^4,4^4,5) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1321, 3: -2010, 4: -2268, 5: -2502} | 1270 |
| B1 | (2,3^7,4^5) | (1^6,2,3^3,4^6) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1321, 3: -2010, 4: -2268} | 1246 |
| B1 | (2,3^7,4^5) | (1^6,3^5,4^5) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268} | 815 |
| B1 | (2,3^7,4^5) | (1^5,2^2,3^4,4^5) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1321, 3: -2010, 4: -2268} | 633 |
| B1 | (2,3^6,4^6) | (1^6,2,3^3,4^5,5) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1321, 3: -2010, 4: -2268, 5: -2502} | 1371 |
| B1 | (2,3^6,4^6) | (1^6,2,3^2,4^7) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1321, 3: -2010, 4: -2268} | 1347 |
| B1 | (2,3^6,4^6) | (1^6,3^4,4^6) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268} | 916 |
| B1 | (2,3^6,4^6) | (1^5,2^2,3^3,4^6) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1321, 3: -2010, 4: -2268} | 734 |
| B1 | (2,3^5,4^7) | (1^6,3^3,4^7) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268} | 1017 |
| B1 | (2,3^4,4^8) | (1^6,3^2,4^8) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268} | 1118 |
| B1 | (2,3^3,4^9) | (1^6,3^2,4^7,5) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268, 5: -2502} | 1243 |
| B1 | (2,3^3,4^9) | (1^6,3,4^9) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268} | 1219 |
| B1 | (2,3^3,4^9) | (1^5,2,3^2,4^8) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1321, 3: -2010, 4: -2268} | 606 |
| B1 | (2,3^2,4^10) | (1^6,3,4^8,5) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268, 5: -2502} | 1344 |
| B1 | (2,3^2,4^10) | (1^6,4^10) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 4: -2268} | 1320 |
| B1 | (2,3^2,4^10) | (1^5,2,3,4^9) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1321, 3: -2010, 4: -2268} | 707 |
| B1 | (2,3^2,4^5,5^5) | (1^5,2,3,4^4,5^5) | {2: 1546, 3: 2247, 4: 2756, 5: 3195} | {1: -450, 2: -1321, 3: -2010, 4: -2268, 5: -2502} | 982 |
| B1 | (2,3,4^11) | (1^5,2,3,4^8,5) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1321, 3: -1905, 4: -2268, 5: -2502} | 937 |
| B1 | (2,3,4^11) | (1^5,2,4^10) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1321, 4: -2268} | 808 |
| B1 | (2,3,4^11) | (1^5,3^2,4^9) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 3: -1905, 4: -2268} | 587 |
| B1 | (2,3,4^11) | (1^4,2^2,3,4^9) | {2: 1546, 3: 2247, 4: 2756} | {1: -450, 2: -1321, 3: -1905, 4: -2268} | 300 |
| B1 | (2,4^12) | (1^5,2,4^9,5) | {2: 1546, 4: 2756} | {1: -450, 2: -1321, 4: -2268, 5: -2502} | 933 |
| B1 | (2,4^12) | (1^5,3,4^10) | {2: 1546, 4: 2756} | {1: -450, 3: -1584, 4: -2268} | 904 |
| B1 | (2,4^12) | (1^4,2^2,4^10) | {2: 1546, 4: 2756} | {1: -450, 2: -1321, 4: -2268} | 296 |
| B1 | (2,4^7,5^5) | (1^5,3,4^5,5^5) | {2: 1546, 4: 2756, 5: 3195} | {1: -450, 3: -1584, 4: -2268, 5: -2502} | 1179 |
| B1 | (2,4^6,5^6) | (1^5,3,4^4,5^6) | {2: 1546, 4: 2756, 5: 3195} | {1: -450, 3: -1584, 4: -2268, 5: -2502} | 1234 |
| B1 | (2,4^5,5^7) | (1^5,3,4^3,5^7) | {2: 1546, 4: 2756, 5: 3195} | {1: -450, 3: -1584, 4: -2268, 5: -2502} | 1289 |
| C1 | (2,5^12) | (1^4,2,4,5^10) | {2: 112, 5: 415} | {1: 0, 2: -138, 4: -232, 5: -322} | 2 |
| B1 | (3^13) | (1^7,3^8,6) | {3: 2247} | {1: -450, 3: -2010, 6: -2775} | 1656 |
| B1 | (3^13) | (1^7,3^7,4,5) | {3: 2247} | {1: -450, 3: -2010, 4: -2268, 5: -2502} | 1671 |
| B1 | (3^13) | (1^7,3^6,4^3) | {3: 2247} | {1: -450, 3: -2010, 4: -2268} | 1647 |
| B1 | (3^13) | (1^6,2,3^8,5) | {3: 2247} | {1: -450, 2: -644, 3: -2010, 5: -2502} | 1735 |
| B1 | (3^13) | (1^6,2,3^7,4^2) | {3: 2247} | {1: -450, 2: -644, 3: -2010, 4: -2268} | 1711 |
| B1 | (3^13) | (1^6,3^9,4) | {3: 2247} | {1: -450, 3: -2010, 4: -2268} | 603 |
| B1 | (3^13) | (1^5,2^2,3^8,4) | {3: 2247} | {1: -450, 2: -644, 3: -2010, 4: -2268} | 1775 |
| B1 | (3^13) | (1^5,2,3^10) | {3: 2247} | {1: -450, 2: -644, 3: -2010} | 667 |
| B1 | (3^13) | (1^4,2^3,3^9) | {3: 2247} | {1: -450, 2: -644, 3: -2010} | 1839 |
| B1 | (3^11,4^2) | (1^6,2,3^5,4^4) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 3: -2010, 4: -2268} | 1913 |
| B1 | (3^10,4^3) | (1^6,2,3^5,4^3,5) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 3: -2010, 4: -2268, 5: -2502} | 2038 |
| B1 | (3^10,4^3) | (1^6,2,3^4,4^5) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 3: -2010, 4: -2268} | 2014 |
| B1 | (3^10,4^3) | (1^6,3^6,4^4) | {3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268} | 906 |
| B1 | (3^10,4^3) | (1^5,2^2,3^5,4^4) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 3: -2010, 4: -2268} | 2078 |
| B1 | (3^9,4^4) | (1^6,3^6,4^3,5) | {3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268, 5: -2502} | 1031 |
| B1 | (3^9,4^4) | (1^6,3^5,4^5) | {3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268} | 1007 |
| B1 | (3^9,4^4) | (1^5,2,3^6,4^4) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 3: -2010, 4: -2268} | 1071 |
| B1 | (3^8,4^5) | (1^6,3^5,4^4,5) | {3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268, 5: -2502} | 1132 |
| B1 | (3^8,4^5) | (1^6,3^4,4^6) | {3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268} | 1108 |
| B1 | (3^8,4^5) | (1^5,2,3^5,4^5) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 3: -2010, 4: -2268} | 1172 |
| B1 | (3^7,4^6) | (1^6,3^4,4^5,5) | {3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268, 5: -2502} | 1233 |
| B1 | (3^7,4^6) | (1^6,3^3,4^7) | {3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268} | 1209 |
| B1 | (3^7,4^6) | (1^5,2,3^4,4^6) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 3: -2010, 4: -2268} | 1273 |
| B1 | (3^6,4^7) | (1^6,3^3,4^6,5) | {3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268, 5: -2502} | 1334 |
| B1 | (3^6,4^7) | (1^6,3^2,4^8) | {3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268} | 1310 |
| B1 | (3^6,4^7) | (1^5,2,3^3,4^7) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 3: -2010, 4: -2268} | 1374 |
| B1 | (3^5,4^8) | (1^6,3^2,4^7,5) | {3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268, 5: -2502} | 1435 |
| B1 | (3^5,4^8) | (1^6,3,4^9) | {3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268} | 1411 |
| B1 | (3^5,4^8) | (1^5,2,3^2,4^8) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 3: -2010, 4: -2268} | 1475 |
| B1 | (3^4,4^9) | (1^6,3^2,4^7,6) | {3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268, 6: -2775} | 1521 |
| B1 | (3^4,4^9) | (1^6,3^2,4^6,5^2) | {3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268, 5: -2502} | 1560 |
| B1 | (3^4,4^9) | (1^6,3,4^8,5) | {3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268, 5: -2502} | 1536 |
| B1 | (3^4,4^9) | (1^6,4^10) | {3: 2247, 4: 2756} | {1: -450, 4: -2268} | 1512 |
| B1 | (3^4,4^9) | (1^5,2,3^2,4^7,5) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 3: -2010, 4: -2268, 5: -2502} | 1600 |
| B1 | (3^4,4^9) | (1^5,2,3,4^9) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 3: -2010, 4: -2268} | 1576 |
| B1 | (3^4,4^9) | (1^5,3^3,4^8) | {3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268} | 468 |
| B1 | (3^4,4^9) | (1^4,2^2,3^2,4^8) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 3: -2010, 4: -2268} | 1640 |
| B1 | (3^3,4^10) | (1^5,2,3,4^8,5) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 3: -2010, 4: -2268, 5: -2502} | 1701 |
| B1 | (3^3,4^10) | (1^5,2,4^10) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 4: -2268} | 1677 |
| B1 | (3^3,4^10) | (1^5,3^2,4^9) | {3: 2247, 4: 2756} | {1: -450, 3: -2010, 4: -2268} | 569 |
| B1 | (3^3,4^10) | (1^4,2^2,3,4^9) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 3: -2010, 4: -2268} | 1741 |
| B1 | (3^3,4^5,5^5) | (1^5,3^2,4^4,5^5) | {3: 2247, 4: 2756, 5: 3195} | {1: -450, 3: -2010, 4: -2268, 5: -2502} | 844 |
| B1 | (3^3,4^4,5^6) | (1^5,3^2,4^3,5^6) | {3: 2247, 4: 2756, 5: 3195} | {1: -450, 3: -2010, 4: -2268, 5: -2502} | 899 |
| B1 | (3^2,4^11) | (1^5,2,3,4^8,6) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 3: -1905, 4: -2268, 6: -2775} | 1892 |
| B1 | (3^2,4^11) | (1^5,2,3,4^7,5^2) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 3: -1905, 4: -2268, 5: -2502} | 1931 |
| B1 | (3^2,4^11) | (1^5,2,4^9,5) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 4: -2268, 5: -2502} | 1802 |
| B1 | (3^2,4^11) | (1^5,3^2,4^8,5) | {3: 2247, 4: 2756} | {1: -450, 3: -1905, 4: -2268, 5: -2502} | 904 |
| B1 | (3^2,4^11) | (1^5,3,4^10) | {3: 2247, 4: 2756} | {1: -450, 3: -1905, 4: -2268} | 775 |
| B1 | (3^2,4^11) | (1^4,2^2,3,4^8,5) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 3: -1905, 4: -2268, 5: -2502} | 1971 |
| B1 | (3^2,4^11) | (1^4,2^2,4^10) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 4: -2268} | 1842 |
| B1 | (3^2,4^11) | (1^4,2,3^2,4^9) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 3: -1905, 4: -2268} | 944 |
| B1 | (3^2,4^11) | (1^3,2^3,3,4^9) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 3: -1905, 4: -2268} | 2011 |
| B1 | (3^2,4^6,5^5) | (1^5,3,4^5,5^5) | {3: 2247, 4: 2756, 5: 3195} | {1: -450, 3: -1905, 4: -2268, 5: -2502} | 1050 |
| B1 | (3^2,4^5,5^6) | (1^5,3,4^4,5^6) | {3: 2247, 4: 2756, 5: 3195} | {1: -450, 3: -1905, 4: -2268, 5: -2502} | 1105 |
| B1 | (3^2,4^4,5^7) | (1^5,3,4^3,5^7) | {3: 2247, 4: 2756, 5: 3195} | {1: -450, 3: -1905, 4: -2268, 5: -2502} | 1160 |
| B1 | (3^2,4^3,5^8) | (1^5,3,4^2,5^8) | {3: 2247, 4: 2756, 5: 3114} | {1: -450, 3: -1905, 4: -2268, 5: -2502} | 567 |
| B1 | (3^2,4,5^10) | (1^4,2,3,4,5^9) | {3: 2247, 4: 2756, 5: 3114} | {1: -450, 2: -644, 3: -1905, 4: -2268, 5: -2502} | 555 |
| B1 | (3^2,5^11) | (1^4,2,3,5^10) | {3: 2247, 5: 3114} | {1: -450, 2: -644, 3: -1905, 5: -2502} | 529 |
| B1 | (3,4^12) | (1^5,2,4^9,6) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 4: -2268, 6: -2775} | 1888 |
| B1 | (3,4^12) | (1^5,2,4^8,5^2) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 4: -2268, 5: -2502} | 1927 |
| B1 | (3,4^12) | (1^5,3,4^9,5) | {3: 2247, 4: 2756} | {1: -450, 3: -1584, 4: -2268, 5: -2502} | 1221 |
| B1 | (3,4^12) | (1^5,4^11) | {3: 2247, 4: 2756} | {1: -450, 4: -2268} | 771 |
| B1 | (3,4^12) | (1^4,2^2,4^9,5) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 4: -2268, 5: -2502} | 1967 |
| B1 | (3,4^12) | (1^4,2,3,4^10) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 3: -1584, 4: -2268} | 1261 |
| B1 | (3,4^12) | (1^3,2^3,4^10) | {3: 2247, 4: 2756} | {1: -450, 2: -644, 4: -2268} | 2007 |
| B1 | (3,4^8,5^4) | (1^5,3,4^5,5^5) | {3: 2247, 4: 2756, 5: 3195} | {1: -450, 3: -1584, 4: -2268, 5: -2502} | 1441 |
| B1 | (3,4^7,5^5) | (1^5,3,4^5,5^4,6) | {3: 2247, 4: 2756, 5: 3195} | {1: -450, 3: -1584, 4: -2268, 5: -2502, 6: -2775} | 1457 |
| B1 | (3,4^7,5^5) | (1^5,3,4^4,5^6) | {3: 2247, 4: 2756, 5: 3195} | {1: -450, 3: -1584, 4: -2268, 5: -2502} | 1496 |
| B1 | (3,4^7,5^5) | (1^5,4^6,5^5) | {3: 2247, 4: 2756, 5: 3195} | {1: -450, 4: -2268, 5: -2502} | 1046 |
| B1 | (3,4^7,5^5) | (1^4,2,3,4^5,5^5) | {3: 2247, 4: 2756, 5: 3195} | {1: -450, 2: -644, 3: -1584, 4: -2268, 5: -2502} | 1536 |
| B1 | (3,4^6,5^6) | (1^5,3,4^4,5^5,6) | {3: 2247, 4: 2756, 5: 3195} | {1: -450, 3: -1584, 4: -2268, 5: -2502, 6: -2775} | 1512 |
| B1 | (3,4^6,5^6) | (1^5,3,4^3,5^7) | {3: 2247, 4: 2756, 5: 3195} | {1: -450, 3: -1584, 4: -2268, 5: -2502} | 1551 |
| B1 | (3,4^6,5^6) | (1^5,4^5,5^6) | {3: 2247, 4: 2756, 5: 3195} | {1: -450, 4: -2268, 5: -2502} | 1101 |
| B1 | (3,4^6,5^6) | (1^4,2,3,4^4,5^6) | {3: 2247, 4: 2756, 5: 3195} | {1: -450, 2: -644, 3: -1584, 4: -2268, 5: -2502} | 1591 |
| B1 | (3,4^5,5^7) | (1^5,3,4^3,5^6,6) | {3: 2247, 4: 2756, 5: 3195} | {1: -450, 3: -1584, 4: -2268, 5: -2502, 6: -2775} | 1567 |
| B1 | (3,4^5,5^7) | (1^5,3,4^2,5^8) | {3: 2247, 4: 2756, 5: 3114} | {1: -450, 3: -1584, 4: -2268, 5: -2502} | 1039 |
| B1 | (3,4^5,5^7) | (1^5,4^4,5^7) | {3: 2247, 4: 2756, 5: 3195} | {1: -450, 4: -2268, 5: -2502} | 1156 |
| B1 | (3,4^5,5^7) | (1^4,2,3,4^3,5^7) | {3: 2247, 4: 2756, 5: 3195} | {1: -450, 2: -644, 3: -1584, 4: -2268, 5: -2502} | 1646 |
| B1 | (3,4^2,5^10) | (1^4,2,4^2,5^9) | {3: 2247, 4: 2756, 5: 3114} | {1: -450, 2: -644, 4: -2268, 5: -2502} | 551 |
| B1 | (3,5^12) | (1^4,3,4,5^10) | {3: 2247, 5: 3114} | {1: -450, 3: -1584, 4: -1944, 5: -2502} | 117 |
| B1 | (4^13) | (1^5,3,4^9,6) | {4: 2756} | {1: -450, 3: -1340, 4: -2268, 6: -2775} | 1551 |
| B1 | (4^13) | (1^5,3,4^8,5^2) | {4: 2756} | {1: -450, 3: -1340, 4: -2268, 5: -2502} | 1590 |
| B1 | (4^13) | (1^5,4^10,5) | {4: 2756} | {1: -450, 4: -2268, 5: -2502} | 896 |
| B1 | (4^13) | (1^4,2,3,4^9,5) | {4: 2756} | {1: -450, 2: -644, 3: -1340, 4: -2268, 5: -2502} | 1630 |
| B1 | (4^13) | (1^4,2,4^11) | {4: 2756} | {1: -450, 2: -644, 4: -2268} | 936 |
| B1 | (4^13) | (1^4,3^2,4^10) | {4: 2756} | {1: -450, 3: -1340, 4: -2268} | 1168 |
| B1 | (4^13) | (1^3,2^2,3,4^10) | {4: 2756} | {1: -450, 2: -644, 3: -1340, 4: -2268} | 1670 |
| B1 | (4^10,5^3) | (1^5,3,4^5,5^5) | {4: 2756, 5: 3195} | {1: -450, 3: -1340, 4: -2268, 5: -2502} | 1755 |
| B1 | (4^9,5^4) | (1^5,4^6,5^5) | {4: 2756, 5: 3195} | {1: -450, 4: -2268, 5: -2502} | 1116 |
| B1 | (4^8,5^5) | (1^5,4^6,5^4,6) | {4: 2756, 5: 3195} | {1: -450, 4: -2268, 5: -2502, 6: -2775} | 1132 |
| B1 | (4^8,5^5) | (1^5,4^5,5^6) | {4: 2756, 5: 3195} | {1: -450, 4: -2268, 5: -2502} | 1171 |
| B1 | (4^8,5^5) | (1^4,2,4^6,5^5) | {4: 2756, 5: 3195} | {1: -450, 2: -644, 4: -2268, 5: -2502} | 1211 |
| B1 | (4^7,5^6) | (1^5,4^5,5^5,6) | {4: 2756, 5: 3195} | {1: -450, 4: -2268, 5: -2502, 6: -2775} | 1187 |
| B1 | (4^7,5^6) | (1^5,4^4,5^7) | {4: 2756, 5: 3195} | {1: -450, 4: -2268, 5: -2502} | 1226 |
| B1 | (4^7,5^6) | (1^4,2,4^5,5^6) | {4: 2756, 5: 3195} | {1: -450, 2: -644, 4: -2268, 5: -2502} | 1266 |
| B1 | (4^6,5^7) | (1^4,2,4^4,5^7) | {4: 2756, 5: 3195} | {1: -450, 2: -644, 4: -2268, 5: -2502} | 1321 |
| B1 | (4^5,5^8) | (1^4,2,4^3,5^8) | {4: 2756, 5: 3114} | {1: -450, 2: -644, 4: -2268, 5: -2502} | 728 |
| B1 | (4^4,5^9) | (1^4,2,4^2,5^9) | {4: 2756, 5: 3114} | {1: -450, 2: -644, 4: -2268, 5: -2502} | 702 |
| B1 | (4^3,5^10) | (1^4,3,4^2,5^9) | {4: 2756, 5: 3114} | {1: -450, 3: -1340, 4: -2268, 5: -2502} | 214 |
| B1 | (4^2,5^11) | (1^4,3,4,5^10) | {4: 2756, 5: 3114} | {1: -450, 3: -1340, 4: -2154, 5: -2502} | 302 |
| B1 | (4,5^12) | (1^4,3,4,5^9,6) | {4: 2756, 5: 3114} | {1: -450, 3: -1340, 4: -1944, 5: -2502, 6: -2775} | 447 |
| B1 | (4,5^12) | (1^4,3,5^11) | {4: 2756, 5: 3114} | {1: -450, 3: -1340, 5: -2502} | 162 |
| B1 | (4,5^12) | (1^4,4^2,5^10) | {4: 2756, 5: 3114} | {1: -450, 4: -1944, 5: -2502} | 116 |
| B1 | (4,5^12) | (1^3,2,3,4,5^10) | {4: 2756, 5: 3114} | {1: -450, 2: -644, 3: -1340, 4: -1944, 5: -2502} | 526 |
| B1 | (5^13) | (1^4,3,5^10,6) | {5: 3114} | {1: -450, 3: -1340, 5: -2502, 6: -2775} | 97 |
| B1 | (5^13) | (1^4,4,5^11) | {5: 3114} | {1: -450, 4: -1608, 5: -2502} | 102 |
| B1 | (5^13) | (1^3,2,3,5^11) | {5: 3114} | {1: -450, 2: -644, 3: -1340, 5: -2502} | 176 |

```{=latex}
\end{landscape}
```

\clearpage

# Review boundary

The candidate theorem follows from the implications and finite arithmetic printed above. The companion records where these texts originated, which historical dependencies were removed, and what the internal checks established. Independent specialist review of the bridge, both clipping arguments, completeness of the tables and every endpoint inequality remains OPEN.
