# One-code rigid cut — residual-one physical repricing and private-coordinate orientation

Date: 2026-09-20

Status: **same-session candidate theorem package after hostile replay**, conditional on the rigid one-code near-equality interface and the predecessor residual-one hub theorem. No finite scan is used as proof. The 20 September daily red-team gate remains binding: `X_3` is the mandatory negative control and bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`.

This note does two things. First, it hostile-replays the load-bearing residual-one hub/multiplicity package and sharpens its physical accounting. Second, it applies raw criticality to every private-coordinate spoke `z_h q_i`, producing an orientation matrix and a new code-concentration/slack dichotomy for radius-two matched heads.

## 1. Residual-one setup

Fix a minimum-U source `s in Y=A_d`. As in the predecessor notes:

- `K` is the set of `k` U-certified heads;
- `H={h_i:i in I}` is the set of `m=p-1` matched-covered heads;
- `R={j}` is the unique residual coordinate;
- `d_U=u-k=c-1`, hence `u=k+c-1`;
- `C=d xor e_j` and every vertex of K has code C;
- each matched head `h_i` has support `{i}` or `{i,j}` relative to d;
- `W_s={z_h:h in K}` is the selected witness set, with every `z_h` of code `bar d`.

The hostile-replayed hub package gives

`N_A(z_h)={h}`, `N_Y(z_h)=empty`, `E(W_s,U_bar(d))=empty`, and `E(K,H)=empty`.

For every h choose one hub beta witness

`f(h)=a_h in K\{h}`

with

`N(z_h) cap N(a_h)={q_j}` and `h a_h notin E`.

Put `r_a=|f^{-1}(a)|`, `s_f=|im f|`, and let

`E=U\W_s`, so `|E|=c-1`.

To avoid collision with the outside source s, this note writes the image size as `s_f`.

## 2. Hostile replay of the predecessor hub theorem

The critical orientation and location checks were repeated directly.

For the rooted B-edge `z_h q_j`, reverse orientation would require an A-witness adjacent to `z_h`. If that witness lies in X it is forced to be h, but `h q_j` is an edge. If it lies in Y then h is an illicit second common neighbour because the X--Y cut is complete. Thus reverse orientation is impossible.

In forward orientation the A-witness cannot lie in Y because Y has code d and does not contain `q_j`. It lies in X. Since `z_h` contains every `q_i`, `i in I`, singleton common-neighbourhood forces the witness to avoid all those `q_i`; at j it must contain `q_j`. Its code is therefore exactly `C=d xor e_j`, so it lies in K. This re-establishes

`f(h)=a_h in K\{h}` and `h a_h notin E`.

Every Y-vertex is adjacent to `a_h`; hence any Y-neighbour of `z_h` would be an extra common neighbour. Therefore `N_Y(z_h)=empty`. Together with the already audited unique-X-head property this gives `N_A(z_h)={h}`.

The same-code U--U orientation check then gives `E(W_s,U_bar(d))=empty`: if a same-code edge is oriented from a used witness `z_h`, its unique X-head h is an extra common neighbour with every complementary d-witness in Y; if it is oriented toward `z_h`, the complementary Y-witness would have to be adjacent to `z_h`, contradicting `N_Y(z_h)=empty`.

Finally, applying rooted criticality to `z_h q_i`, `i in I`, under the temporary assumption `h h_i in E`, kills both orientations exactly as in the predecessor note, giving `E(K,H)=empty`.

**Audit conclusion.** No missing witness location, orientation, or reuse pattern was found in these load-bearing steps. Their status remains conditional on reaching the rigid interface, not publication-grade graph-level closure.

## 3. The forced W--escape holes pay U-slack one-for-one

For each h, let `P_h` be the number of vertices of E that are forced nonadjacent to `z_h` by the beta singleton equation with `a_h`. Let

`P=sum_h P_h`.

The predecessor multiplicity theorem proved

`P >= sum_a r_a(t_a-1)`

and hence

`P >= sum_a r_a[lambda+r_a-epsilon_a]_+`,

where `t_a=d_U(a)` and `epsilon_a` is the maximum-degree slack of a.

The residual-one hub geometry lets us price these same physical holes directly on the U side. The preserved U degree identity is

`d_{A union U}(z)=p+u-1-epsilon_z`.

For `z_h` there is exactly one X-neighbour, no Y-neighbour, no neighbour in `W_s`, and at most `(c-1)-P_h` neighbours in E. Therefore

`p+u-1-epsilon_{z_h} <= c-P_h`.

Using `k=u-c+1` gives

> **`epsilon_{z_h} >= p+k-2+P_h`.**                       `(PR-1)`

Summing over the fixed-source witnesses:

> **`E_{W_s} >= k(p+k-2)+P`.**                            `(PR-2)`

This strictly refines the hostile-replayed quadratic witness bill `k(p+k-2)` whenever the beta map forces any additional W--escape hole.

## 4. The beta conservation law strengthens from coefficient two to coefficient one

All beta witnesses `a in im f` lie in K, so their slacks are contained in `L_X`.

For fixed `r>=1`, put `L=lambda+r`. For every nonnegative epsilon,

`epsilon + r[L-epsilon]_+ >= L`.

Indeed, below L this is `rL-(r-1)epsilon`, minimized at epsilon=L for `r>1` and constant for `r=1`; above L it is epsilon.

Using `(BM-P2)` and summing over the `s_f` image vertices yields

> **`L_X+P >= lambda s_f+k`.**                            `(PR-3)`

The predecessor note used the weaker displayed consequence `L_A+2P>=lambda s_f+k` because P was entering through rooted-Q. `(PR-3)` is a separate physical score statement: the same missing W--escape pairs also cost U-degree slack by `(PR-2)`.

Consequently

> **`E_U+L_A >= k(p+k-2)+lambda s_f+k`.**                 `(PR-4)`

This is safe because `E_U>=E_{W_s}` and `L_A>=L_X`.

## 5. Inactive K vertices add a second image-size price

If `b in K\im f`, the outgoing beta obligation `b f(b)` is a missing K-edge, so

`e_K(b)<=k-2`.

Also b is adjacent to exactly one vertex of `W_s`, namely `z_b`, and to at most all `c-1` vertices of E. Thus `t_b<=c`.

The exact K degree formula from the predecessor note is

`epsilon_b=g0+u-e_K(b)-t_b`.

With `u=k+c-1`,

> **`epsilon_b>=g0+1` for every `b in K\im f`.**           `(PR-5)`

Adding these inactive slacks to the active conservation `(PR-3)` gives

> **`L_X+P >= T(s_f):=`**
> **`lambda s_f+k+(k-s_f)(g0+1)`**
> **`=k(g0+2)+s_f(c-2)`.**                               `(PR-6)`

This is useful because it keeps the physical meaning of the beta-map image. For `c>2`, a large image is intrinsically expensive even before the missing-K-edge Hamming floor is invoked; for `c=2` this contribution is image-independent; for `c=1` the large-image endpoint is favoured.

A related pointwise bound is

`epsilon_a>=g0+r_a`

for every active image vertex a: it has at least `r_a` distinct K-nonneighbours and at most c U-neighbours.

## 6. Exact one-dimensional joint score/rooted gates

For `p>=4`, define the exact integral predecessor X-slack floor

`L0(s_f)=floor(x g0-p/2 + max{`
`  k(p+1)-2 floor(s_f/2),`
`  k(p+k-2c)`
`})+1`.

Every actual residual-one beta map has `2<=s_f<=k` and satisfies both

`L_X>=L0(s_f)`

and `(PR-6)`.

Since `(PR-2)` gives `E_{W_s}>=k(p+k-2)+P`, the standard above-M score ceiling implies the sharpened necessary condition

> **`C0 >= k(p+k-2)+max{L0(s_f),T(s_f)}`**                `(PR-SCORE)`

for the actual image size `s_f`.

The rooted-Q inequality is also sharpened by the inactive K slacks. The predecessor bound is

`q <= (c-1)u-c(c-1)/2-P`.

Combining it with the exact rooted identity gives

`Z+L_A+2P <= u(p-lambda)+2(c-1)u-c(c-1)+C0`.

For the active image vertices, `sum epsilon_a+2P>=lambda s_f+k`; adding `(PR-5)` on the inactive vertices yields again the lower bound `T(s_f)` on `L_A+2P`. Since `Z>=k(x+y-1)`, every survivor must also satisfy

> **`k(x+y-1)+T(s_f)`**
> **`<=u(p-lambda)+2(c-1)u-c(c-1)+C0`.**                 `(PR-ROOT)`

Thus the residual-one scalar optimization has genuinely become one-dimensional: an actual survivor must admit an integer `s_f in [2,k]` satisfying `(PR-SCORE)` and `(PR-ROOT)` simultaneously. Finite scans may diagnose this interval but are not proof.

## 7. The known stress family still survives: a genuine method boundary

For the exact preserved family

`c=p=2t`, `y=1`, `g0=2t-1`, `lambda=4t-2`, `u=x=3t`, `k=t+1`,

one has

`k(p+k-2)=3t^2+2t-1`,

`T(s_f)=2t^2+3t+1+(2t-2)s_f`,

and

`L0(s_f)=8t^2-t+2-2 floor(s_f/2)`.

For every `2<=s_f<=t+1` and `t>=2`, `L0(s_f)>T(s_f)`. Hence the new score gate reduces to the already-live X-slack obstruction and still has positive margin. The rooted margin after `(PR-ROOT)` is exactly

`9t^2+2t-5-2s_f(t-1)`,

which remains positive even at `s_f=t+1`.

Therefore the new physical repricing is a real strengthening but **does not close the exact unbounded residual-one stress ray**. This is a stop/pivot result: the next step must use additional physical orientation/code geometry, not another collapse of the same score and rooted-Q terms.

## 8. Private-coordinate orientation matrix

The edge `z_h q_i` exists for every `h in K` and every private coordinate `i in I`. Rooted B-edge criticality gives exactly two possible orientations.

### Forward orientation F(h,i)

The A-witness must contain `q_i`. By private-coordinate uniqueness, the only X-vertex containing `q_i` is `h_i`; no Y-vertex contains `q_i`. Thus the witness is `h_i` and

`N(z_h) cap N(h_i)={q_i}`.                                `(OM-F)`

### Reverse orientation R(h,i)

The A-witness must be adjacent to `z_h`. Since `N_A(z_h)={h}`, the witness is h and

`N(q_i) cap N(h)={z_h}`.                                  `(OM-R)`

These are exhaustive.

Now split the matched heads into

`J1={i: c(h_i)=d xor e_i}`

and

`J2={i: c(h_i)=d xor e_i xor e_j}`.

If `i in J2`, then both `z_h` and `h_i` are adjacent to the common residual hub `q_j`. Therefore `(OM-F)` would already have two common matched neighbours, `q_i` and `q_j`, and is impossible. Hence:

> **For every `i in J2` and every `h in K`, orientation is forced reverse:**
> **`N(q_i) cap N(h)={z_h}`.**                            `(OM-R2)`

This is a graph-level physical consequence of the radius-two choice at one matched head, not a scalar Hamming bill.

## 9. Radius-two heads force escape-code concentration or k-fold X-slack

Let

`E_bad={w in E : w q_i in E(G) for some i in J2}`

and put `b=|E_bad|`.

By `(OM-R2)`, if `w in E_bad` and `h in K`, then `wh` cannot be an edge: for a coordinate i witnessing membership in `E_bad`, w would otherwise be a second common neighbour of `q_i` and h besides `z_h`. Thus

> **`E(K,E_bad)=empty`.**                                 `(OM-BAD0)`

Equivalently, every escape U-neighbour of every K-head agrees with d on every radius-two private coordinate.

Each bad escape vertex therefore removes one possible U-neighbour from every K vertex. Repeating the degree count behind `(PR-5)` gives

> `epsilon_h>=g0+1+b` for every inactive h,

and, for an active image vertex a,

> `epsilon_a>=g0+r_a+b`.

In particular the aggregate K-slack gains at least `k b` over the corresponding `b=0` degree floor.

So the radius-two part of the matched layer creates a sharp dichotomy:

> **either `b=0`, in which case every escape U-vertex that touches K has code agreeing with d on all coordinates of J2; or each bad escape costs one missing K--U edge for every head in K, hence k units of X-slack.** `(OM-DICH)`

At the extreme `J2=I`, all K-neighbouring escape codes are fixed on all `p-1` private coordinates and have only the residual bit j free. Thus only the two code patterns d and C can occur among escape vertices adjacent to K. This is the next useful structural endpoint for the radius-two side.

## 10. Evidence status and next move

The advances in this note are structural and conditional:

1. hostile replay found no flaw in the residual hub/beta orientation package;
2. forced W--escape holes pay U-slack one-for-one, `(PR-1)--(PR-2)`;
3. the beta conservation law strengthens to `L_X+P>=lambda s_f+k` and, after inactive K vertices, to `(PR-6)`;
4. exact score/rooted feedback reduces to one image-size variable, `(PR-SCORE)--(PR-ROOT)`;
5. the known t-ray still survives those scalar gates, so no false closure is claimed;
6. every private spoke has an F/R orientation, and radius-two matched heads force R globally across K;
7. radius-two coordinates force the escape-code/slack dichotomy `(OM-DICH)`.

The highest-value next attack is the orientation matrix when the radius-one set J1 dominates. Forward entries force `N(z_h) cap N(h_i)={q_i}` and reverse entries force `N(q_i) cap N(h)={z_h}`. The aim should be a physical covering theorem showing that a large K x J1 matrix necessarily creates many distinct W--E or K--E holes, or else collapses escape U-codes to a tiny family. That would directly attack the exact unbounded residual-one ray, whose abstract code model may take all matched heads radius one.

The global caveat remains unchanged: bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`, so the entire package remains conditional on reachability of that interface.