# N30: assembled candidate proof by hand lemmas and explicit integer tables

11 September 2026. Research direction: Paul Lenz. Mathematical development, assembly and internal audit: ChatGPT/Geeps.

**Complete supplementary candidate argument. Internal arithmetic REPRODUCED; independent specialist review OPEN. The current frozen reviewer package remains N30 reviewer-v2. No governed theorem-ledger promotion or new PDF edition is made here.**

This assembly proves the candidate statement

$$
e(G)\le225,\qquad e(G)=225\Longleftrightarrow G\cong K_{15,15}
$$

for finite simple diameter-two edge-critical graphs G on thirty vertices. It uses the parameterized graph bridge, hand tail lemmas and explicit bounded integer tables. Large profile/residual searches, grouped LPs and Farkas rays are not premises of this supplementary route. The printed finite classification and envelope arithmetic **are** part of its proof obligations; this is not a table-free proof or a claim of external acceptance.

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

The [canonical parameterized bridge](../../general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md) supplies one selected cross-edge per missing unordered B-pair, with every other cross-edge residual. For labels use F-degree d_i, residual degree R_i, selected degree x_i and demand `s_i=max(0,d_i-R_i)`. For sources use residual degree rho_u, selected outdegree q_u and supplement indegree p_u. With `t=m-b(a+1)`, its needed conclusions are:

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

The [bridge audit](BRIDGE_AUDIT.md) checks the selected-edge injection, forced residual edges, residual activity, threshold pair counting, and the precise source domain. Charging and the isolated-C improvement are **not** needed in this assembly. The corrected canonical bridge already avoids two wording/display errors in older copies.

## 3. Delta>=17 has a hand exclusion

For `Delta=17,...,28`, `1<=a<=12`, `b>=17`, and at every `m>=225` the surplus `t=m-b(30-b)` is positive.

The [source-independent twelve-label lemma](TWELVE_LABEL_TRANSFER.md), applied after padding the demand vector with zeros, gives `Q<=18`. The bridge gives `Q>=b+2t>=19`, a contradiction. More sharply, at Delta=17 it gives `m<=221`.

If `Delta=29`, a universal vertex exists. Any edge between two other vertices could be deleted while the universal vertex still kept all pairs within distance two. Criticality therefore makes G a star, with only twenty-nine edges.

Thus every degree at least seventeen is excluded at the dense scopes. No historical Delta=17 profile checks, final Hall duals, or higher-degree charging scans remain necessary here.

## 4. Delta=16: the complete profile input is hand classified

Here `(a,b)=(13,16)` and `t=m-224`. In the dense scopes t is positive. The [hand classification](../2026-09-11-m225-hand-classification-v1/HAND_CLASSIFICATION.md) proves:

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

All summands are nonnegative integers, and `16>=z_2>=...>=z_13>=0`. Such tails determine rho uniquely. This is the [written threshold-slack reconstruction](../2026-09-11-threshold-tail-v1/N30_M225_THRESHOLD_SLACK_REDUCTION.md), with the new hand classification supplying completeness.

At t=2, the seven profiles with Q>=20 give nine rows. Six Q=20 profiles have no slack. For `(3^13)`, g2=g3=9 and all higher g are zero; its one unit of slack can be assigned to lambda, to z2, or to a new z4=1. There are no other monotone possibilities.

At t=1, at most three units are distributed, giving 272 rows. The independent audit reconstructs both sets by adding boxes to monotone tail diagrams, using no historical residual-row generator. It agrees exactly with the printed prior frontier.

Whenever every demand is positive, `s_i=d_i-R_i` pointwise, and the ledger gives `S=r+2t`. Hence lambda=0. This immediately excludes the one positive-slack t=2 row and all 61 positive-slack t=1 rows. It leaves eight rows at m226 and 211 at m225. This implication uses positivity, not an assumed demand equality; it resolves an imprecise sentence in the earlier m226 exposition.

## 6. The eight m226 rows

The [hand endpoint note](../2026-09-11-threshold-tail-v1/N30_M226_HAND_ENDPOINT_REDUCTION.md) states all eight rows and their small source certificates. Here is its algebraic mechanism.

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

The [four-envelope argument](../2026-09-11-m225-resource-envelope-v1/FOUR_ENVELOPE_REDUCTION.md) uses the exact local domains

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

Here lambda denotes the certificate's residual-budget coefficient, distinct from the already-zero ledger slack in Section 5. The [complete 211-row arithmetic appendix](../2026-09-11-m225-resource-envelope-v1/EXACT_APPENDIX.md) displays a strictly positive left side for every row. Certificates B1, B2, B3, C1 cover `195+13+2+1=211` rows; the minimum assigned integer gap is one.

The new independent audit recomputes all 12,772 local states with a separately written potential evaluator and reconstruction. It matches all 844 original per-template row gaps exactly. Every minimum can also be checked from the printed endpoint formulas in the four-envelope note. This is explicit finite integer arithmetic, not a numerical infeasibility conclusion.

Thus no Delta=16 graph has m225 or m226; Section 4 excluded all larger edge counts.

## 8. Complete assembly and remaining review boundary

At m>=226, Delta<=15 is excluded by degree sum; Delta=16 by Sections 4–7; Delta=17,...,28 by Section 3; and Delta=29 by the star argument. Hence m<=225.

At m225, Delta<=14 is excluded by degree sum, Delta=15 forces `K(15,15)` by Section 1, and all larger degrees are excluded above. The converse was verified in Section 1. This completes the supplementary candidate statement.

The logical route now uses neither Fan's density theorem nor the published dominating-edge reduction, and it retains no Delta=17 or higher-degree computational branch. The remaining substantial finite audit surface is the explicit Delta=16 classification, tail reconstruction and endpoint arithmetic.

The universal graph bridge and all printed proof-critical arithmetic still require independent specialist scrutiny. Internal checking does not create external acceptance. The frozen reviewer-v2 package, historical certificates and governed ledger remain unchanged; a new reviewer PDF edition has not been issued by this checkpoint.
