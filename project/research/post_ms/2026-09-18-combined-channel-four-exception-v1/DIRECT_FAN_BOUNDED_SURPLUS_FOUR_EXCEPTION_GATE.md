# Bounded-surplus direct fans: the four-exception gate

Date: 2026-09-18

Status: internal structural theorem package for the eventual / sufficiently-large diameter-2-critical second-extremal programme around

`M(n)=floor((n-1)^2/4)+1`.

This strengthens the previous three-exception theorem. The published order-12, size-32 graph `X_3` remains a mandatory negative control and is untouched: at its canonical root `f=0`, so there is no positive direct fan.

No all-order or eventual theorem is claimed.

## 1. Preserved direct-fan setup

Fix an A-source `x` with direct fan

`D={y in A:xy is direct}`, `d=|D|>=2`.

Put

`W=(V(G)\{v})\N(x)`,

`H_y=W\N(y)`,

`h_y=|H_y|=epsilon_x+epsilon_y-(lambda+1)`,

and

> `eta=sum_{y in D}h_y`.                                  `(FH0)`

Let

`w=|W|=a+epsilon_x`,

`Z=V(G)\(D union W)`,

`z=|Z|=b+1-d-epsilon_x`.

The preserved direct-fan geometry gives

- `D` is independent;
- no vertex of `D` is adjacent to `Z`;
- `e(D,W)=dw-eta`;
- `w>=d+1`.

If

> `eta<=d-2`,                                              `(FH1)`

there are at least two zero-hole leaves, hence a universal leaf `y_0` with `N(y_0)=W`. The preserved private-support theorem gives an injection from the internally active vertices

`W^+={t in W:d_{G[W]}(t)>0}`

into `Z`, with each support vertex seeing exactly its assigned vertex of `W`.

Writing `t=|W^+|`, one has

> `t<=z`,                                                  `(FH2)`
>
> `e(W,Z)<=zw-t(w-1)`,                                   `(FH3)`
>
> `e(G[W])<=binom(t,2)`,                                 `(FH4)`

and therefore

> `m<=w(n-w)+binom(z,2)-t(w-1)+binom(t,2)-eta`.          `(FH5)`

The previous note used this to close `z<=3`. We now treat `z=4`.

## 2. Four exceptions with an internally active W-layer

Assume `z=4` and `G[W]` is nonempty. Then `2<=t<=4`. In `(FH5)` the weakest internally active case is `t=2`, so it suffices to check

> `B_w+eta+2(w-1)-1-6 >= floor(n/2)-1`,                  `(FH6)`

where

`B_w=floor(n^2/4)-w(n-w)`.

Dropping the favourable `eta`, this is

> `B_w+2w-9 >= floor(n/2)-1`.                             `(FH7)`

Using `n=d+w+4` and `w>=d+1`, the parity calculations are elementary.

If `n=2h` and `w=h+r`, the difference between the two sides of `(FH7)` is

> `(r+1)^2+h-9`.                                         `(FH8)`

Here `w>=d+1` implies `r>=-1`, so `(FH8)` is nonnegative for `n>=18`.

If `n=2h+1`, the difference is

> `r^2+r+h-8`,                                            `(FH9)`

again with `r>=-1`; this is nonnegative for `n>=17`.

Hence

> `z=4`, `G[W]` nonempty, `n>=17` ==> `m<=M(n)`.          `(FH10)`

Thus only `W` independent remains.

## 3. The four-vertex kernel when W is independent

Assume from now on

`z=4`, `G[W]` independent,

and write

`J=G[Z]`.

Two elementary facts hold.

1. For every `w in W`, its Z-neighbourhood `S=N_Z(w)` dominates `J`. Indeed, if `wz` is a nonedge, a common neighbour of `w,z` cannot lie in `D` (D has no Z-neighbours) or in `W` (W is independent), so it must lie in `Z`.
2. Every `z in Z` has a W-neighbour, because `dist(y_0,z)<=2` and `N(y_0)=W`.

Also

> `m=dw-eta+e(W,Z)+e(J)`.                                `(FH11)`

We classify the four-vertex graph `J` by edge count and isomorphism type.

## 4. Sparse kernels

### 4.1 No Z-edge

If `e(J)=0`, there is no triangle: `D` and `W` are independent, and no triangle can use a D-Z edge because none exists.

### 4.2 One Z-edge

Let the unique edge be `ab`, with `c,d` isolated in `J`. Every W-vertex must see both `c,d`.

If the graph is triangle-containing, some `x in W` sees both `a,b`. Applying triangle-edge criticality to `xa` shows

> `d_W(a)<=eta+1`,                                        `(FH12)`

and similarly

> `d_W(b)<=eta+1`.                                        `(FH13)`

The reason is the same as in the old three-exception one-edge kernel: a reverse W-witness is blocked by the universal leaf `y_0`; a reverse D-witness cannot see `a`; and a forward Z-witness can work only when `x` is already the unique W-neighbour of `a`. Otherwise a D-leaf must certify the edge, and every competing W-neighbour of `a` is a hole of that leaf.

Thus

`e(W,Z)<=2w+2eta+2`

and

> `m<=dw+2w+eta+3<=dw+2w+d+1<=M(n)`.                    `(FH14)`

### 4.3 Two Z-edges: P3 plus an isolated vertex

Let the path be `1-0-2` and let `3` be isolated. Every W-vertex sees `3`; on the path its neighbourhood is one of

`{0}`, `{1,2}`, `{0,1}`, `{0,2}`, `{0,1,2}`.

Let `E` be the number of path incidences beyond one per W-vertex. The three-exception path argument survives unchanged. If the graph contains a triangle, then

> `E<=eta+2`.                                              `(FH15)`

The isolated Z-vertex can replace a D-witness only in the degenerate case in which the relevant path leaf has a unique W-neighbour, which is already covered by the zero right-hand contribution in the quadratic hole estimate.

Therefore

> `e(W,Z)<=2w+eta+2`,                                     `(FH16)`

and, as `e(J)=2`,

> `m<=dw+2w+4<=M(n)`.                                    `(FH17)`

### 4.4 Two disjoint Z-edges

Let

`J=ab union cd`.

Every W-vertex sees at least one endpoint of each edge. Let

- `A` be the number of W-vertices seeing both `a,b`;
- `B` be the number seeing both `c,d`.

Then

> `e(W,Z)=2w+A+B`.                                        `(FH18)`

For a W-vertex counted by `A`, an edge such as `wa` lies in the triangle `w-a-b`. A Z-witness for the forward orientation can only be `c` or `d`, and a fixed such Z-vertex can certify at most one W-vertex. Hence all but at most two members of the A-family require distinct D-witnesses. Each such witness has at least `A-1` holes, because every other A-member is another W-neighbour of `a`. Thus

> `eta >= (A-2)_+(A-1)`.                                 `(FH19)`

Similarly

> `eta >= (B-2)_+(B-1)`.                                 `(FH20)`

Assume `A>=B`. If `A<=2`, then `A+B<=4`. If `A>=3`, `(FH19)` gives

`2A<=eta+4`.

Therefore in all cases

> `A+B<=eta+4`.                                           `(FH21)`

Using `(FH11)`,

> `m<=dw+2w+6<=M(n)`                                     `(FH22)`

throughout the range needed below.

## 5. A safe-incidence lemma

The remaining path `P4` and every four-vertex kernel with at least four edges admit a compact common treatment.

Let `S=N_Z(w)` for a W-vertex. For `z in S`, call the incidence `(w,z)` **safe** if

1. `wz` lies in a triangle inside `{w} union Z`;
2. no Z-vertex can certify the forward orientation of the triangle edge `wz`;
3. no Z-vertex can certify the reverse orientation.

Concretely, condition 2 means that every `q in S` nonadjacent to `z` has a common J-neighbour with `z`; condition 3 means that every `q notin S` adjacent to `z` has another neighbour in `S\{z}`.

### Lemma 5.1 — four-vertex safe-incidence table

If either

- `J=P4`, or
- `e(J)>=4`,

then every dominating `S subseteq Z` of order `r>=3` contains at least

> `r-2` safe coordinates.                                `(SAFE)`

### Hand verification

There are only five relevant isomorphism types:

- `P4`;
- `C4`;
- the paw (triangle with one pendant edge);
- `K4-e`;
- `K4`.

For `C4`, `K4-e` and `K4`, every coordinate in every dominating 3- or 4-set is safe. For the paw, every dominating 3-set has at least two safe coordinates and the 4-set has four. For `P4`, the four dominating 3-sets

`012`, `013`, `023`, `123`

have safe coordinates respectively

`{0,1}`, `{1}`, `{2}`, `{2,3}`,

while the 4-set has safe coordinates `{1,2}`.

Thus `(SAFE)` follows by a finite hand table; no graph enumeration is required for the proof.

### Why safe incidences force D-witnesses

Consider a safe triangle edge `wz`. A W-witness is impossible: in the reverse orientation the universal leaf `y_0` is an additional common neighbour, while W is independent for the forward orientation. A reverse D-witness is impossible because D has no Z-neighbours. The safe definition excludes all Z-witnesses. Therefore the certificate must be a **forward D-witness** `y` with

> `N(z) intersect N(y)={w}`.                              `(FH23)`

For fixed `z`, different assigned W-vertices need different D-witnesses. If `A_z` safe incidences are assigned to coordinate `z`, every such witness has at least `A_z-1` holes. Hence

> `eta>=A_z(A_z-1)`.                                      `(FH24)`

Put

> `R_eta=floor((1+sqrt(1+4eta))/2)`.                      `(FH25)`

Then `A_z<=R_eta` for each of the four Z-coordinates.

For every W-vertex assign `(|N_Z(w)|-2)_+` distinct safe incidences. This is possible by Lemma 5.1 in the relevant kernels. Thus, with

> `E_+=sum_{w in W}(|N_Z(w)|-2)_+`,                      `(FH26)`

we have

> `E_+=sum_z A_z<=4R_eta`.                                `(FH27)`

The elementary integer inequality

> `4R_eta-eta<=6`                                         `(FH28)`

holds for every `eta>=0`: if `R_eta=k`, then `eta>=k(k-1)`, so

`4R_eta-eta<=5k-k^2<=6`.

Finally

> `e(W,Z)<=2w+E_+`.                                       `(FH29)`

## 6. The remaining three-edge kernels

### 6.1 P4

Apply the safe-incidence lemma. Since `e(J)=3`, `(FH11)`, `(FH28)` and `(FH29)` give

> `m<=dw+2w+9`.                                           `(FH30)`

This is below `M(n)` in the global `n>=23` range of the theorem.

### 6.2 K3 plus an isolated vertex

Every W-vertex sees the isolated Z-vertex and at least one triangle coordinate. Criticality of the three triangle edges forces singleton triangle-neighbourhood W-types on a vertex cover of the K3, hence on at least two coordinates, say `1,2`.

Let `X_i` be the number of W-vertices adjacent to `i` and to at least one further triangle coordinate. For `i=1,2`, every such triangular incidence needs a distinct D-witness; the isolated Z-vertex cannot certify it because the singleton W-type gives another common neighbour. Therefore

> `eta>=X_i^2`.                                           `(FH31)`

If

`E=e(W,Z)-2w`

is the number of triangle incidences beyond one per W-vertex, then

> `E<=X_1+X_2<=eta+1`.                                    `(FH32)`

Consequently

> `m<=dw+2w+4<=M(n)`.                                    `(FH33)`

### 6.3 K1,3

Let `0` be the centre and `1,2,3` the leaves. A dominating Z-neighbourhood either contains the centre or is exactly `{1,2,3}`.

Let

- `R` be the number of W-vertices of type `{1,2,3}` without the centre;
- `A_i` be the number of W-vertices adjacent to both `0` and leaf `i`.

Then

> `e(W,Z)=w+A_1+A_2+A_3+2R`.                             `(FH34)`

For every `i`, each of the `A_i` triangle incidences requires a distinct D-witness, and each such witness has at least `A_i+R-1` holes. Hence

> `eta>=A_i(A_i+R-1)`.                                    `(FH35)`

If all `A_i=0`, the graph is triangle-free. Otherwise put `A=max A_i>=1`.

- If `A=1`, then `sum A_i<=3` and `(FH35)` gives `eta>=R`, so

  `A_1+A_2+A_3+2R-eta<=3+R<=d+1`,

  using `R<=eta<=d-2`.

- If `A>=2`, then

  `A_1+A_2+A_3+2R-eta`

  `<=3A+2R-A(A+R-1)`

  `<=4`,

  and `(FH35)` together with `eta<=d-2` forces `d>=4`, so again the expression is at most `d+1`.

Thus

> `m<=dw+w+d+4<=M(n)`.                                   `(FH36)`

## 7. Four or more Z-edges

If `e(J)>=4`, Lemma 5.1 applies. Using `(FH11)`, `(FH28)`, `(FH29)` and `e(J)<=6`,

> `m<=dw+2w+12`.                                          `(FH37)`

With `n=d+w+4`, `w>=d+1`, this lies below `M(n)` for every `n>=23`.

A convenient square check is

`(d+w+3)^2-4(dw+2w+11)`

`=(w-d-1)^2+4d-36`.

Under `n=d+w+4>=23` and `w-d>=1`, the right-hand side is nonnegative (the minimum is attained at the boundary `d=8,w-d=3`). Hence the floor in `M(n)` causes no problem.

## 8. Four-exception closure theorem

Combining the preserved `z<=3` theorem with Sections 2--7 gives the main result.

### Theorem 8.1 — bounded-surplus four-exception gate

Let `x in A` support a direct fan of order `d>=2` in a D2C graph. If

> `eta<=d-2`                                               `(FH38)`

and

> `z=b+1-d-epsilon_x<=4`,                                 `(FH39)`

then for `n>=23` at least one of the following holds:

1. `G` is triangle-free;
2. `m<=M(n)`.

Therefore every live triangle-containing above-`M(n)` candidate with `n>=23` satisfies, for every direct fan,

> `eta>=d-1`,
>
> **or**
>
> `z>=5`.                                                  `(FH40)`

Equivalently,

> `eta>=d-1`,
>
> **or**
>
> `d+epsilon_x<=b-4`.                                     `(FH41)`

This improves the previous three-exception alternative `d+epsilon_x<=b-3`.

### Corollary 8.2 — exact zero-surplus branch

If `eta=0`, then every live triangle-containing above-threshold candidate of order at least 23 satisfies

> `d+epsilon_x<=b-4`.                                     `(FH42)`

### Corollary 8.3 — earlier triggering of the local slack bill

If instead

> `d+epsilon_x>=b-3`,                                     `(FH43)`

then `(FH41)` forces `eta>=d-1`. Expanding `eta` gives

> `sum_{y in D}epsilon_y`
> ` >=d(lambda+2-epsilon_x)-1`.                           `(FH44)`

Thus the preserved direct-fan self-pricing bill now activates one external exception earlier than at the preceding checkpoint.

## 9. Scope and trust boundary

- The proof uses the preserved bounded-surplus private-support theorem, triangle-edge criticality, diameter two and a finite hand classification of graphs on the four external vertices.
- The finite four-vertex table is independently exhaustively checked in the companion verifier, but the proof above does not depend on computation.
- The threshold `n>=23` is driven only by the deliberately uniform bound for the dense four-vertex kernels; several sparse kernels close much earlier.
- No claim is made that 23 is optimal.
- The theorem does not touch `X_3`: at the canonical root there is no positive direct fan.
- No global eventual second-extremal theorem is asserted.

## 10. Research consequence

The live direct branch has moved from

`low hole surplus -> at least four external exceptions`

to

> `low hole surplus -> at least five external exceptions`.

Together with the new combined complementary-pair channel capacity, both non-matched-B A-edge mechanisms are now constrained by compact slack-priced statements. The next synthesis should retain the actual split `S=E_U+L_A` and intersect the complete A-edge capacity with the independent beta-sensitive `q` ceiling and the exact rooted residual target `delta>=D_M`.
