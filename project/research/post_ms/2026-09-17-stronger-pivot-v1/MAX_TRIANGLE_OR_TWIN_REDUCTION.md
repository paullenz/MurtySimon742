# Maximum-triangle-or-twin reduction at the second-extremal threshold

17 September 2026. Research directed by Paul Lenz; derivation and finite regression by ChatGPT/Geeps.

**Status: internal candidate structural reduction; external mathematical and novelty review open.** This does not prove the eventual second-extremal theorem. It replaces the previous maximum-triangle-root scope question by a sharper dichotomy: above the comparison threshold, either a maximum-degree triangle vertex exists, or the graph contains a large peelable false-twin class.

The false all-order 2019 second-extremal conjecture is not assumed. The published order-12, size-32 D2C exception remains a mandatory negative control throughout.

## 1. Why the previous scope question was too rigid

Let

\[
M(n)=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1.
\]

The predecessor `ALL_PRIVATE_EDGE_WITNESS_PRICING.md` shows that if a **maximum-degree** root lies in a triangle and

\[
n\ge 14,\qquad m\ge M(n)+1,
\]

then its all-private root-edge branch is impossible, so a disjoint-support antipode is forced.

The remaining scope question was whether every sufficiently dense triangle-bearing D2C graph must possess such a maximum-degree triangle root.

A direct degree-comparison proof has not been found. More importantly, it is unnecessarily strong. If a maximum-degree root lies outside every triangle, its neighbourhood is independent. That `Q=0` branch has enough structure to make a different reduction.

## 2. Independent maximum neighbourhood and exact defect coordinates

Let `G` be D2C of order `n`, let `v` have maximum degree

\[
b=\Delta(G),
\]

and put

\[
B=N_G(v),\qquad A=V(G)\setminus N_G[v],\qquad a=|A|=n-1-b.
\]

Assume

\[
Q=e(G[B])=0.
\]

Thus `B` is independent. Put

\[
F=G[A],\qquad f=e(F).
\]

For `x in A`, define

\[
R_x=b-|N_G(x)\cap B|,
\qquad
d_x=d_F(x),
\qquad
e_x=R_x-d_x.
\]

Since

\[
d_G(x)=b-R_x+d_x=b-e_x\le b,
\]

we have the exact pointwise identity

\[
\boxed{e_x=b-d_G(x)\ge0.} \tag{2.1}
\]

In the `Q=0` branch every missing `A-B` incidence is residual, so

\[
r=\sum_{x\in A}R_x.
\]

Because `sum d_x=2f`,

\[
r=2f+\sum_{x\in A}e_x.
\]

Writing

\[
E:=\sum_{x\in A}e_x,
\qquad
\delta:=b(n-b)-m=r-f,
\]

gives the particularly simple defect identity

\[
\boxed{\delta=f+E.} \tag{2.2}
\]

This is the key normalization for the independent-neighbourhood branch.

## 3. One triangle-free `F`-edge already pays the full second-extremal defect

> **Lemma 3.1 (triangle-free edge payment).**  
> If `xy in E(F)` lies in no triangle of `G`, then
>
> \[
> \boxed{\delta\ge b-1.} \tag{3.1}
> \]

### Proof

Since `xy` lies in no triangle, `x` and `y` have no common neighbour in `B`. Hence their `B`-neighbourhoods are disjoint:

\[
(b-R_x)+(b-R_y)\le b,
\]

so

\[
R_x+R_y\ge b. \tag{3.2}
\]

They also have no common neighbour in `A`. Therefore the `F`-edges incident with `x` and the `F`-edges incident with `y` overlap only in `xy`, giving

\[
f\ge d_x+d_y-1. \tag{3.3}
\]

From (2.2),

\[
\delta=f+E
       \ge d_x+d_y-1+e_x+e_y
       =R_x+R_y-1
       \ge b-1.
\]

This proves the lemma.

Hence:

> **Corollary 3.2.** If `delta<=b-2`, then **every edge of `F` lies in a triangle of `G`**.

No diameter-criticality beyond the setup is needed for this local payment; maximum degree supplies (2.1).

## 4. The threshold itself forces `delta<=b-2`

For every integer `b`,

\[
b(n-b)-(b-1)
  =b((n-1)-b)+1
  \le \left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1
  =M(n). \tag{4.1}
\]

Therefore

\[
m\ge M(n)+1
\]

implies

\[
\boxed{\delta=b(n-b)-m\le b-2.} \tag{4.2}
\]

Thus in any graph above the comparison threshold whose maximum root has `Q=0`, every `F`-edge is triangular by Corollary 3.2.

This observation is stronger strategically than trying to prove immediately that `Q` must be positive.

## 5. Tight `A`-vertices either produce the desired root or become twins

Call `x in A` **tight** when

\[
e_x=0.
\]

By (2.1), a tight vertex has

\[
d_G(x)=b=\Delta(G).
\]

Suppose `m>=M(n)+1` and `Q=0`.

If a tight vertex `x` is incident with an `F`-edge `xy`, then Corollary 3.2 says that `xy` lies in a triangle. Thus `x` is itself a maximum-degree vertex lying in a triangle. This is exactly the root needed by the dense-root antipode theorem.

The only way to avoid a maximum-degree triangle vertex is therefore:

> every tight `A`-vertex is isolated in `F`.

For such a tight isolated vertex,

\[
d_x=0,\qquad e_x=0,
\]

so `R_x=0`. Hence it is adjacent to every vertex of `B` and to no vertex of `A` or to `v`. Thus

\[
N_G(x)=B=N_G(v). \tag{5.1}
\]

So every tight isolated `A`-vertex is a false twin of the maximum root `v`.

Put

\[
D=\{x\in A:e_x>0\}.
\]

If no maximum-degree triangle vertex exists, then

\[
F=F[D], \tag{5.2}
\]

and

\[
W:=\{v\}\cup(A\setminus D)
\]

is a false-twin class with common neighbourhood `B`. Since `B` is independent, every member of `W` is triangle-free.

Moreover, each vertex of `D` contributes at least one unit to `E`, so

\[
|D|\le E=\delta-f. \tag{5.3}
\]

## 6. Above the threshold the false-twin class has size at least three

In the triangle-bearing branch, `Q=0` implies `f>=1`: if `F` were empty, the bipartition

\[
B\quad\text{and}\quad \{v\}\cup A
\]

would make `G` bipartite and hence triangle-free.

Using (5.3),

\[
|W|
 =1+a-|D|
 \ge 1+a-(\delta-f)
 =n-b-\delta+f. \tag{6.1}
\]

Since `f>=1` and

\[
\delta\le b(n-b)-M(n)-1,
\]

we get

\[
|W|
 \ge n-b-\bigl(b(n-b)-M(n)-1\bigr)+1
 =M(n)+2-(b-1)(n-b). \tag{6.2}
\]

But `(b-1)+(n-b)=n-1`, so

\[
(b-1)(n-b)\le
\left\lfloor\frac{(n-1)^2}{4}\right\rfloor
=M(n)-1.
\]

Consequently

\[
\boxed{|W|\ge3.} \tag{6.3}
\]

Thus the obstruction to a maximum-degree triangle root is not diffuse: it contains at least three maximum-degree false twins with a common independent neighbourhood.

## 7. Triangle-free false twins can be peeled while preserving D2C

> **Lemma 7.1 (false-twin peeling).**  
> Let `G` be D2C and let `x,y` be nonadjacent twins with
>
> \[
> N_G(x)=N_G(y)=B,
> \]
>
> where `B` is independent. Suppose deleting `y` leaves at least one other vertex of the twin class, so the resulting graph is noncomplete. Then
>
> \[
> G-y
> \]
>
> is again D2C.

### Diameter

Any length-at-most-two path between surviving vertices that used `y` internally has the form

\[
p-y-q
\]

with `p,q in B`. Replacing `y` by its twin `x` gives

\[
p-x-q.
\]

Thus every surviving pair remains at distance at most two. Since another twin remains, the graph is noncomplete, so its diameter is two.

### Edge criticality

Take an edge `e` surviving in `G-y`. Since `G` is D2C, `G-e` has a pair at distance greater than two.

If one such witness pair avoids `y`, the same pair survives in `(G-y)-e`.

Otherwise take a witness pair `(y,z)`.

If `e` is not incident with `x`, swapping the twins `x,y` is an automorphism of `G-e`, so `(x,z)` is also at distance greater than two and survives the deletion of `y`.

The only remaining case is

\[
e=xu,\qquad u\in B.
\]

After deleting `xu`, the vertices `x,u` have no common neighbour: every neighbour of `x` lies in the independent set `B`, and no vertex of `B` is adjacent to `u`. Hence `d(x,u)>2`.

Therefore every surviving edge remains critical.

The proof is direct. It is consistent with the MacDougall--Eggleton twin-extension criterion quoted as Theorem 22 by Dailly--Foucaud--Hansberg (2019): for a vertex lying in no triangle, the condition for adding a twin is vacuous.

## 8. Core reduction and defect invariance

Starting from the class `W` in Section 6, repeatedly apply Lemma 7.1 until one member `w` remains.

The resulting graph `G_0` is D2C. No triangle is lost because all removed twins are triangle-free. The maximum degree remains `b`:

- `w` still has degree `b`;
- vertices of `D` are unaffected and have degree `b-e_x<=b-1`;
- vertices of `B` only lose neighbours as twins are deleted.

The property “no maximum-degree vertex lies in a triangle” is therefore preserved if it held before peeling.

For the final root `w`,

\[
N_{G_0}(w)=B,\qquad
A_0=D.
\]

Hence

\[
n_0=b+|D|+1. \tag{8.1}
\]

The internal graph `F[D]`, the values `e_x`, `f`, and `E` are unchanged. Each removed twin deletes exactly `b` edges while decreasing the order by one, so

\[
\delta_0
 =b(n_0-b)-m_0
 =\delta. \tag{8.2}
\]

Equivalently,

\[
m_0=b(|D|+1)-\delta. \tag{8.3}
\]

Every nonroot vertex of `A_0=D` has positive degree slack:

\[
e_x=b-d_{G_0}(x)\ge1. \tag{8.4}
\]

Thus the unresolved branch has been compressed to a smaller D2C core with the **same residual defect**, an independent maximum neighbourhood, and no tight vertices outside the root.

## 9. Main reduction theorem

Combining the preceding sections gives the useful scope replacement.

> **MAXIMUM-TRIANGLE-OR-TWIN REDUCTION (internal candidate).**  
> Let `G` be a triangle-containing D2C graph of order `n` and size
>
> \[
> m\ge M(n)+1.
> \]
>
> Choose any maximum-degree vertex `v`, of degree `b`.
>
> Then at least one of the following holds.
>
> **(T) Maximum-triangle branch.**  
> Some vertex of degree `b` lies in a triangle.
>
> **(W) Twin-core branch.**  
> `G` contains a false-twin class `W` of at least three maximum-degree, triangle-free vertices with a common independent neighbourhood `B`. Peeling all but one member of `W` preserves D2C, all triangles, maximum degree `b`, and the residual defect `delta`, and produces a core `G_0` satisfying (8.1)--(8.4).

If the chosen maximum root already has `Q>0`, branch (T) is immediate. If `Q=0`, Sections 3--6 prove that failure of (T) forces (W).

So the previous “maximum-triangle-root question” no longer needs to be solved as an all-or-nothing lemma. **The only dense obstruction to it is a very explicit twin expansion.**

## 10. The stronger independent-neighbourhood target

The natural next theorem is now sharply visible:

> **Independent-neighbourhood defect target.**  
> If `G` is non-bipartite D2C, `v` is a maximum-degree vertex, and `N(v)` is independent, prove
>
> \[
> \boxed{\delta\ge b-1.} \tag{IN}
> \]

This would immediately give

\[
m=b(n-b)-\delta
 \le b(n-b)-(b-1)
 \le M(n),
\]

closing the entire `Q=0` branch.

Lemma 3.1 already proves `(IN)` whenever `F` contains even one edge lying in no triangle. Therefore any counterexample to `(IN)` must satisfy the much narrower conditions:

1. every edge of `F` lies in a triangle;
2. after peeling tight twins, every remaining `A`-vertex has positive degree slack;
3. the same `delta` survives the peeling.

This is the next structural target. It is substantially narrower than the original maximum-triangle-root problem.

The expanded-`C5` equality family is consistent with `(IN)` at equality: for its maximum roots one has

\[
\delta=b-1,
\]

and the graphs have exactly `M(n)` edges.

## 11. Near-maximum triangle-root fallback

A separate fallback remains available if the twin-core route stalls.

Let `v` be a triangle root of degree `b` and put

\[
\varepsilon=\Delta(G)-b.
\]

Repeating the all-private edge-witness argument with maximum-degree slack `epsilon` gives

\[
\boxed{
3\delta_v+\varepsilon(2a-t)
\ge
\binom t2+2s+2t(b-t),
} \tag{11.1}
\]

where `delta_v=b(n-b)-m`, `t` is the number of triangle-active vertices in `N(v)`, and `s=binom(t,2)-Q`.

The derivation differs from `ALL_PRIVATE_EDGE_WITNESS_PRICING.md` only in two places:

- for `y in Y`, maximum degree gives `d_F(y)<=h_y+epsilon`, adding `epsilon(a-t)` to the private-foot estimate;
- total degree slack on `A` gains `a epsilon`.

The critical-edge injection is unchanged.

This does **not** by itself close the `epsilon=1` case, so it is retained as a fallback rather than the primary route.

## 12. Mandatory negative and equality controls

### 12-vertex / 32-edge hostile control

The reconstructed `X_3` graph has

\[
n=12,\quad m=32,\quad M(12)=31.
\]

Its unique maximum-degree root has

\[
b=8,\quad Q=12,\quad \delta=0.
\]

Thus it enters branch (T) immediately. The reduction does not exclude or misclassify the published small-order obstruction.

### Expanded `C5`

The known expanded-`C5` second-extremal family has exactly `M(n)` edges and satisfies `delta=b-1` at maximum roots. It is therefore a boundary control for the proposed `(IN)` theorem rather than a contradiction to it.

## 13. Regression and trust boundary

The companion `check_max_triangle_or_twin_reduction.py` performs:

- direct D2C checks on all 21 graph-atlas D2C isomorphism classes through order 7;
- 41 maximum-root `Q=0` instances;
- 18 triangle-free `F`-edge payment records;
- 82 direct false-twin peel operations;
- 12,497,497 integer threshold/twin-class arithmetic records through `n=5000`;
- 285 expanded-`C5` equality controls through order 30;
- the explicit `X_3` order-12 / size-32 negative control.

Recorded result:

`PASS_MAX_TRIANGLE_OR_TWIN_REDUCTION`.

These finite checks are regression evidence only. The hand arguments above are the mathematical basis. No eventual second-extremal theorem, novelty claim, or classification is promoted.

## 14. Next mathematical obligation

Do **not** return to the old mixed `{4,5}` selected-excess ladder, and do not spend the next unit trying to prove the obsolete blanket maximum-triangle-root statement.

The highest-value target is now the peeled `Q=0` core:

\[
N(v)=B\text{ independent},\qquad
A=D,\qquad
e_x\ge1\ \forall x\in A,\qquad
\delta=f+\sum e_x.
\]

Try to prove `(IN)`, namely `delta>=b-1`, by pricing the fact that **every edge of `F` is triangular and critical**. In particular, distinguish whether a critical arm for an `F`-edge lies in `A` or `B`; an `A`-arm already gives a full `b`-sized endpoint payment, while the unresolved case is when the required arms can all be routed through `B`.

If `(IN)` fails, preserve an explicit incidence-level obstruction. The twin reduction ensures that such an obstruction is the genuine remaining scope issue rather than an artefact of root choice.
