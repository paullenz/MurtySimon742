# Residual-one k=2 half-ray: reverse-certificate capacity and private-foot overlap

Date: 2026-09-20

Status: **same-session conditional structural theorem package**, downstream of the corrected intermediate half-ray, `J2=empty`, the residual-hub theorem, the H--U triangle-scope lemma, and the repaired raw singleton-certificate machinery. This note does **not** assert graph-level reachability of the rigid interface. `X_3` remains the mandatory negative control and bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`.

## 1. Exact half-ray setup

Use the corrected intermediate family

- `p=2t`, `c=y=t`,
- `lambda=2t-1`, `u=t+1`, `x=2t+1`,
- `k=2`, `m=p-1=2t-1`, residual dimension one,
- `H={h_i:i in I}`, `|H|=h=p-1`, with `c(h_i)=d xor e_i`,
- `K` the two residual heads of code `d xor e_j`,
- `E(K,H)=empty`,
- `q_i` the `bar d` endpoint of private coordinate i and `q_j` the `bar d` residual endpoint.

The root has degree `b=2p+u`; its neighbourhood contains every matched endpoint and every U-vertex.

Write

`M_H = binom(h,2)-e(H)`

for the number of missing H--H pairs, and `L_H=sum_{h_i in H} epsilon_i`.

## 2. Hostile replay of private-foot forcing: the source bit is fixed

Suppose a triangular H--U edge `t h_i` is t-sourced through the private foot `q_i`, so

`N(t) cap N(q_i)={h_i}`.                                      `(PF-1)`

The critical source and witness must be nonadjacent. Since a U-vertex is adjacent to `q_i` exactly when its code selects the `bar d` endpoint in coordinate i, `(PF-1)` implies

> **`c(t)_i=d_i`.**                                           `(PF-BIT)`

The predecessor slice exclusion is therefore exact:

> **`N_U(t) cap U_i^-=empty`, where `U_i^-={w in U:c(w)_i=bar d_i}`.** `(PF-SLICE)`

For a set `S(t)` of private-foot-certified H-indices, every U-neighbour w of t satisfies

> **`c(w)_i=d_i` for every `i in S(t)`.**                     `(PF-MULTI)`

In particular, if `|S(t)|>=2`, t is anticomplete to `U_bar(d)` and to every endpoint-indexed class `U_{bar(d) xor e_l}`: a code `bar d xor e_l` agrees with d on at most the single private coordinate l and therefore still selects a forbidden `q_i` for some `i in S(t)`.

This is a direct code-incidence consequence; no P1/P2 reuse claim is needed.

## 3. Reverse A_X witnesses are impossible

Consider a triangular H--U edge `h_i t` oriented from source `h_i`, with witness a and singleton head t:

`N(h_i) cap N(a)={t}`.                                      `(REV-0)`

The source and witness are nonadjacent.

No `a in Y` is possible because H--Y is complete. Now suppose `a in A_X`.

Every A_X code on the `J2=empty` half-ray is either

- `d xor e_l` for a matched head `h_l`, or
- `d xor e_j` for a residual K-head.

Relative to `c(h_i)=d xor e_i`, either code agrees with h_i in at least `p-2` matched coordinates. Hence `h_i` and a share at least `p-2` matched endpoints. For the present ray `p>=8`, so `(REV-0)` cannot be a singleton.

Therefore

> **no reverse H--U certificate can use an A_X witness.**    `(REV-X0)`

This removes an entire previously unpriced reverse arm.

## 4. Reverse matched witnesses are either a directed H-hole or the residual hub

A matched witness must be the endpoint opposite the one selected by `h_i` in some coordinate.

### Coordinate i

The opposite endpoint is the d-endpoint. Both it and `h_i` are adjacent to every Y-vertex, and `y=t>0`. Hence this endpoint cannot satisfy `(REV-0)`.

### A different private coordinate l

The opposite endpoint is `q_l`. Its unique A_X-neighbour is `h_l`. Thus if `h_i h_l` were an edge, `h_l` would be an extra common neighbour in `(REV-0)`. Consequently

> **a reverse witness `q_l`, `l!=i`, forces `h_i h_l` to be a missing H-edge.** `(REV-HOLE)`

For fixed ordered pair `(h_i,q_l)`, singleton uniqueness permits at most one U-head t. Hence all such private-coordinate reverse certificates number at most

> **`2 M_H`.**                                               `(REV-QCAP)`

### Residual coordinate j

The only remaining opposite matched endpoint is `q_j`. For each fixed source `h_i`, the pair `(h_i,q_j)` supports at most one singleton U-head. Therefore this arm has total capacity at most

> **`h`.**                                                   `(REV-JCAP)`

## 5. The root reverse arm is impossible

It is tempting to count the root as one further reverse witness per H-source. That is invalid.

The root is adjacent to all `2p` matched endpoints, while `h_i` is adjacent to exactly p of them. Hence `N(h_i) cap N(root)` already contains p matched vertices before any U-head is considered. It cannot equal the singleton `{t}`.

Thus

> **the root never reverse-certifies an H--U edge in this interface.** `(REV-ROOT0)`

This removes another linear exceptional arm.

## 6. Endpoint-indexed U exceptions form one shared reservoir

The predecessor H--U orientation theorem gives: a reverse U-witness for source `h_i` must lie in

`U_{bar(d) xor e_i}`

and have Y-degree zero. The triangle-scope theorem gives: a triangle-free edge `h_i w` can occur only when the endpoint w lies in the same class and has Y-degree zero.

These two uses are mutually exclusive for a fixed physical w:

- as a reverse witness, w must be nonadjacent to its indexed source `h_i`;
- as a triangle-free endpoint, w must be adjacent to `h_i`.

Moreover the code determines i uniquely. Hence, writing `r_i=|U_{bar(d) xor e_i}|`,

> **`#(reverse-U-certified triangular H--U edges) + #(triangle-free H--U edges) <= sum_i r_i <= u`.** `(REV-U-TF)`

There is a third use of the same reservoir. If a t-sourced H--U certificate uses an A_X witness, then t and that witness can share no matched endpoint, so their codes must be complementary. K cannot witness an H-head because `E(K,H)=empty`; therefore the witness is the unique `h_l` with

`c(t)=bar(d) xor e_l`.

The pair `(t,h_l)` is nonadjacent. The same physical pair cannot simultaneously supply a reverse-U H--U certificate, whose singleton head would be a U-vertex, and a forward A_X-witness certificate, whose singleton head is an H-vertex. It is also incompatible with the triangle-free endpoint role, which requires `t h_l` to be an edge.

Therefore the stronger shared-reservoir bound is

> **`TF + R_U + F_X <= sum_i r_i <= u`,**                   `(REV-SHARED)`

where `F_X` counts t-sourced triangular H--U edges whose witness lies in A_X.

## 7. Exact local H conservation law

For `h_i in H`, let `m_i` be its number of missing neighbours inside H. Since `|H|=p-1`,

`d_H(h_i)=p-2-m_i`.

Its degree is

`d(h_i)=p+y+d_H(h_i)+d_U(h_i)`,

because it has p matched neighbours, all y Y-neighbours, no K-neighbours, its H-neighbours and its U-neighbours. With root degree `b=2p+u`, on the half-ray `p+u-y=p+1`, so

`epsilon_i=p+1-d_H(h_i)-d_U(h_i)`.

Substituting `d_H=p-2-m_i` gives the exact pointwise identity

> **`d_U(h_i)=m_i+3-epsilon_i`.**                          `(H-LOCAL)`

Summing over H,

> **`e(H,U)=2M_H+3h-L_H`.**                               `(H-GLOBAL)`

Thus the H--U load is not independent of H-density: each missing H-edge creates two units of potential H--U degree, plus a fixed three-per-H surplus reduced exactly by H-slack.

## 8. High-H-degree forward certificates are almost all private-foot

Let t be a U-vertex with `d_H(t)>=3`, and consider a t-sourced triangular edge `t h_i`.

- a U-witness is impossible because any two U-vertices share the root;
- a Y-witness is impossible because it sees every H-neighbour of t, including an H-neighbour other than `h_i`;
- the root is adjacent to t and so cannot be the nonadjacent witness.

If the witness lies in A_X, the no-shared-matched-endpoint argument in section 6 forces the unique endpoint-indexed witness `h_l`; for a fixed t the code fixes l, and the fixed pair `(t,h_l)` has at most one singleton head. Therefore **at most one** t-sourced H-edge at t can use an A_X witness.

If the witness lies in the matched layer, inspect an endpoint selected by `h_i`.

- The residual d-endpoint is adjacent to every H-vertex, so another H-neighbour of t is an extra common neighbour.
- A d-endpoint in a private coordinate `l!=i` is adjacent to every H-head except `h_l`. Since t has at least two H-neighbours besides `h_i`, at least one of them is different from `h_l`, again producing an extra common neighbour.

The only remaining matched witness is `q_i` itself.

Hence

> **for `d_H(t)>=3`, all but at most one t-sourced triangular H--U edge at t are private-foot certified through their own `q_i`.** `(PF-HIGH)`

This removes the former `d_Y(t)>0` hypothesis for all but one forward edge per high-H-degree U-vertex.

## 9. Global private-foot lower bound on the half-ray

Partition H--U edges into:

1. private-coordinate reverse matched certificates `q_l`, total at most `2M_H`;
2. residual-hub reverse matched certificates `q_j`, total at most h;
3. the shared endpoint-indexed exceptional reservoir `TF + R_U + F_X`, total at most u;
4. edges incident with U-vertices of H-degree at most two, total at most `2u`;
5. the remaining t-sourced high-H-degree edges, which are private-foot certified by `(PF-HIGH)`.

Using `(H-GLOBAL)`, the number `P_F` of forced private-foot H--U certificates therefore satisfies

`P_F >= e(H,U)-2M_H-h-u-2u`

and hence

> **`P_F >= 2h-3u-L_H`.**                                `(PF-GLOBAL)`

On the corrected half-ray `h=2t-1`, `u=t+1`, so

> **`P_F >= t-5-L_H = p/2-5-L_H`.**                      `(PF-RAY)`

Thus either H-slack is already linear, or the half-ray contains a linear family of exact private-foot singleton equations and coordinate-slice U-exclusions.

The bound is only linear and therefore does **not** close the half-ray against the present quadratic score margin. Its value is structural: it proves that the private-foot phenomenon cannot be isolated to a few Y-active vertices; after all reverse and triangle-free exception arms are priced correctly, it survives globally unless H itself spends linear slack.

## 10. A coordinate-column consequence of reverse q_l certificates

A reverse private-coordinate equation

`N(h_i) cap N(q_l)={t}`, `l!=i`,                         `(COL-0)`

also has a useful dual interpretation. Every U-vertex w with `c(w)_l=bar d_l` is adjacent to `q_l`. Therefore `(COL-0)` implies

> **among the U-neighbours of h_i, at most the singleton head t can lie in `U_l^-`.** `(COL-1)`

If `R_i` is a set of distinct private coordinates used by reverse q_l certificates from source `h_i`, then

> **`sum_{w in N_U(h_i)} |{l in R_i:c(w)_l=bar d_l}| <= |R_i|`.** `(COL-2)`

So both major orientations now create code-incidence restrictions:

- forward/private-foot edges delete an entire coordinate slice from `N_U(t)`;
- reverse/q_l edges allow at most one bar-bit U-neighbour in the corresponding column of `N_U(h_i)`.

This is the natural incidence matrix for the next attack.

## 11. Strategic consequence

The scalar `Ccap_P/(ONE-P)/(CROWD)` gates have large quadratic margin on this ray and should not be re-optimized. The live object is now the H-by-U orientation/code matrix.

A promising next theorem would show that the simultaneous row restrictions `(PF-MULTI)` and column restrictions `(COL-2)` cannot coexist with `(H-LOCAL)` on a linear set of H and U vertices without producing an additional quadratic block in `M_U`, `Z_{H,U}`, or `L_H`.

Any such aggregation must avoid double-counting the already-large missing-U currency: the corrected ray already has `e(U)=O(p)`. The useful target is therefore a new *located* H--U/A--U/slack obstruction, or a classification of the equality geometry, not another bare lower bound on `M_U`.

Upstream caveat unchanged: all claims remain conditional downstream of the unresolved rigid complete Hall-cut reachability interface.