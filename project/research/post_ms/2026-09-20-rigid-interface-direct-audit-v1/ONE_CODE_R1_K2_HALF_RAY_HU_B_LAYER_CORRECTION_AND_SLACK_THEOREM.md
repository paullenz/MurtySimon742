# Residual-one k=2 half-ray: B-layer correction and H-slack theorem

Date: 2026-09-20

Status: **same-session hostile correction plus replacement theorem**, conditional on the corrected intermediate half-ray, `J2=empty`, residual-hub geometry, the repaired singleton-certificate machinery, and the H--U triangle-scope theorem. This note **supersedes the H--U private-foot claims** in `ONE_CODE_R1_K2_HALF_RAY_HU_ORIENTATION_FILTER.md` and in the same-session file `ONE_CODE_R1_K2_HALF_RAY_HU_REVERSE_CAPACITY_AND_PRIVATE_FOOT_OVERLAP.md`.

The correction is load-bearing: every matched endpoint lies in the rooted B-layer `B=N(v)`, just as every U-vertex does. Therefore a U-source and a matched witness share the root and can never form a singleton common-neighbour pair with an A-head. The previous `HU-PRIVATE/HU-QI/HU-IHOLE` claims are invalid and must not be used downstream.

The repair is stronger in a different direction: once B-layer witnesses are removed from the U-sourced arm, all H--U edges admit a tight orientation-capacity classification, yielding an exact linear lower bound on H-slack on the corrected half-ray.

## 1. Setup

Use

- `p=2t`, `c=y=t`,
- `lambda=2t-1`, `u=t+1`, `x=2t+1`,
- `k=2`, `m=p-1=2t-1`, `J2=empty`,
- `H={h_i:i in I}`, `h=|H|=p-1`, `c(h_i)=d xor e_i`,
- `K` the two heads of code `d xor e_j`, with `E(K,H)=empty`,
- `q_i` the `bar d` matched endpoint in private coordinate i and `q_j` the residual `bar d` endpoint.

The rooted B-layer contains all `2p` matched endpoints and all U-vertices, and the root v is adjacent to every vertex of that layer. In particular

> `U union {all matched endpoints} subseteq N(v)`.          `(BL-0)`

The selected witnesses `W_s` are two distinct vertices of `U_bar(d)` with H-degree zero.

Write

`M_H=binom(h,2)-e(H)` and `L_H=sum_{h_i in H} epsilon_i`.

## 2. Correction: a U-sourced H--U certificate cannot use any B-layer witness

Take a triangular H--U edge `t h_i` with `t in U` and suppose the valid orientation is sourced at t:

`N(t) cap N(r)={h_i}`.                                      `(FWD-0)`

The source and witness are nonadjacent. If `r in B=N(v)`, then both t and r are adjacent to the root v, so v is an additional common neighbour. Hence

> **every t-sourced witness r lies in A, not in B.**        `(FWD-A)`

In particular, neither a U-vertex nor any matched endpoint `q_i` can be the witness.

This directly invalidates the predecessor claim

`N(t) cap N(q_i)={h_i}`

and every coordinate-slice consequence derived from it. Those statements are superseded by this note.

## 3. Classification of the t-sourced arm

Because `r in A`, there are only Y and `A_X` possibilities.

The singleton head `h_i` lies in A, not in a matched fibre. Therefore t and r may share no matched endpoint. Their p-bit fibre codes must be coordinatewise complementary:

> **`c(r)=bar(c(t))`.**                                   `(FWD-COMP)`

### 3.1 Y witness

If `r in Y`, then `c(r)=d`, so

`c(t)=bar d`.

Every Y-vertex is adjacent to every H-vertex. Thus if t has two H-neighbours, a second H-neighbour is an illicit common neighbour of t and r. Therefore a Y-witness can occur only when

> `c(t)=bar d` and `d_H(t)=1`.                            `(FWD-Y)`

Such vertices lie in the H-positive `bar d` class, disjoint from `B0` and in particular disjoint from the two selected witnesses `W_s`.

### 3.2 A_X witness

A K-vertex cannot witness because `E(K,H)=empty`, so it is not adjacent to the singleton head `h_i`.

Hence an A_X witness is some matched head `h_l`. By `(FWD-COMP)`,

> `c(t)=bar d xor e_l`.                                   `(FWD-XCODE)`

The code determines l uniquely. The fixed physical pair `(t,h_l)` has one common-neighbour set and therefore can support at most one singleton head. Thus

> **each U-vertex can source at most one triangular H--U edge.** `(FWD-CAP1)`

More precisely, the t-sourced edges split between the H-positive `bar d` class in `(FWD-Y)` and the disjoint endpoint-indexed classes `U_{bar d xor e_l}` in `(FWD-XCODE)`.

## 4. Reverse A- and root-witness arms are impossible

Now orient a triangular H--U edge from source `h_i`:

`N(h_i) cap N(r)={t}`.                                    `(REV-0)`

### Y witness

Impossible because H--Y is complete, so source and witness would be adjacent.

### A_X witness

Every A_X code is either `d xor e_l` or `d xor e_j`. Relative to `c(h_i)=d xor e_i`, it agrees in at least `p-2` matched coordinates. Thus h_i and r share at least `p-2` matched endpoints, contradicting singleton `(REV-0)`.

### Root witness

The root is adjacent to all matched endpoints. The source h_i has p matched neighbours, so `N(h_i) cap N(v)` already contains p matched vertices. The root cannot be a singleton witness.

Therefore reverse witnesses lie only in the matched layer or U.

## 5. Reverse matched witnesses

A matched witness must be the endpoint opposite the one selected by h_i.

### Private coordinate i

The opposite endpoint is the d-endpoint. It and h_i are both adjacent to all y>0 vertices of Y, so it cannot satisfy `(REV-0)`.

### Private coordinate l != i

The opposite endpoint is `q_l`, whose unique A_X-neighbour is `h_l`. If `h_i h_l` were present, h_l would be an extra common neighbour. Hence a reverse q_l certificate forces the H-hole `h_i h_l notin E`.

A fixed ordered pair `(h_i,q_l)` supports at most one U-head. Summing directed missing H-pairs gives

> **`R_q <= 2 M_H`.**                                    `(REV-Q)`

### Residual coordinate j

The only remaining matched witness is q_j. For each h_i the fixed pair `(h_i,q_j)` supports at most one singleton U-head, so

> **`R_j <= h`.**                                        `(REV-J)`

## 6. Reverse-U and triangle-free edges share one endpoint-indexed reservoir

The predecessor reverse-U calculation remains valid: a reverse U-witness for source h_i must lie in

`U_{bar d xor e_i}`

and have Y-degree zero.

Independently, the triangle-scope theorem gives that a triangle-free edge `h_i w` can occur only for a Y-anticomplete endpoint

`w in U_{bar d xor e_i}`.

For a fixed physical `w in U_{bar d xor e_i}` these two roles are mutually exclusive:

- reverse witness requires `w h_i` to be absent;
- triangle-free endpoint requires `w h_i` to be present.

The code fixes i. Therefore, if `r_i=|U_{bar d xor e_i}|`,

> **`R_U + T_F <= sum_i r_i`.**                           `(REV-U-TF)`

## 7. The forward endpoint-indexed arm uses the same reservoir too

A t-sourced A_X-witness certificate from section 3 has

`t in U_{bar d xor e_l}`

and witness `h_l`, with `t h_l` absent.

For the same physical pair `(t,h_l)`, the common-neighbour set is fixed. It cannot simultaneously be a reverse-U H--U certificate, whose singleton head is a U-vertex, and a forward A_X-witness certificate, whose singleton head is an H-vertex. It is also incompatible with the triangle-free endpoint role, which requires `t h_l` present.

Thus

> **`F_X + R_U + T_F <= sum_i r_i`.**                     `(SHARED-R)`

The remaining t-sourced Y-witness edges use H-positive `bar d` vertices. Let `B_1` be the subset of `U_bar(d)` with H-degree exactly one. Then

> **`F_Y <= |B_1|`.**                                    `(SHARED-B)`

The code classes `B_1` and all `U_{bar d xor e_i}` are disjoint. Moreover the two selected witnesses `W_s subseteq U_bar(d)` have H-degree zero and lie in neither family. Hence

> **`|B_1| + sum_i r_i <= u-2`.**                         `(SHARED-TOTAL)`

Combining `(SHARED-R)` and `(SHARED-B)`, the total capacity of

- all triangle-free H--U edges,
- all reverse-U-certified triangular H--U edges,
- all t-sourced triangular H--U edges

is at most `u-2` after the reverse matched arms are separated.

## 8. Exact H-degree conservation

For `h_i in H`, let `m_i` be its missing H-degree. Since `|H|=p-1`,

`d_H(h_i)=p-2-m_i`.

The root degree is `b=2p+u`, while h_i has p matched neighbours, all y Y-neighbours, no K-neighbours, its H-neighbours and its U-neighbours. Hence

`epsilon_i=p+u-y-d_H(h_i)-d_U(h_i)`.

On the half-ray `p+u-y=p+1`, so

> **`d_U(h_i)=m_i+3-epsilon_i`.**                         `(H-LOCAL)`

Summing over H yields

> **`e(H,U)=2M_H+3h-L_H`.**                               `(H-GLOBAL)`

This identity is exact and independent of any certificate orientation choice.

## 9. Replacement H-slack theorem

Every H--U edge is either

1. triangle-free, counted in the shared endpoint-indexed reservoir;
2. triangular and reverse-certified by a private q_l, capacity at most `2M_H`;
3. triangular and reverse-certified by q_j, capacity at most h;
4. triangular and reverse-U-certified, counted in the shared endpoint-indexed reservoir;
5. triangular and t-sourced, counted either in the endpoint-indexed reservoir or in `B_1`.

Sections 3--7 prove the exhaustive capacity bound

> **`e(H,U) <= 2M_H + h + (u-2)`.**                      `(HU-CAP)`

Insert `(H-GLOBAL)` and cancel the same `2M_H` term:

`2M_H+3h-L_H <= 2M_H+h+u-2`.

Therefore

> **`L_H >= 2h-u+2`.**                                   `(HU-SLACK)`

On the corrected half-ray `h=2t-1`, `u=t+1`, this becomes

> **`L_H >= 3t-1 = 3p/2-1`.**                            `(HU-SLACK-RAY)`

This is the correct replacement for the invalid private-foot coordinate-slice theorem.

The result is only linear in p and therefore does not by itself close the half-ray against the quadratic score ceiling. It is nevertheless a genuine structural theorem: the exact H-degree identity and certificate capacities cancel all dependence on the unknown H-density, forcing linear H-slack in every realization of the corrected half-ray.

## 10. Immediate score improvement

The corrected half-ray already has

`e(Y)=0`,

`L_Y >= t^2-3t+1`.

Since H- and Y-slack are disjoint parts of `L_A`, `(HU-SLACK-RAY)` gives

> **`L_A >= t^2`.**                                      `(HU-LA)`

The preserved rooted identity also gave

`E_U >= t^2-5t+8`.

Hence the safely combined score floor improves to

> **`E_U+L_A >= 2t^2-5t+8`.**                            `(HU-SCORE)`

The exact score ceiling remains `C0=4t^2+7t-3`, so a large quadratic margin survives. No closure is claimed.

## 11. Strategic consequence

The previous plan to aggregate `HU-IHOLE` coordinate-slice exclusions must be abandoned because those exclusions came from an impossible B--B singleton pair.

The live H--U theorem is now the orientation-capacity/slack statement `(HU-SLACK)`. The next high-value attack is to study the equality geometry of `(HU-CAP)`:

- almost every directed missing H-pair must be used by a q_l reverse certificate;
- almost every H source must use its q_j reverse slot;
- the remaining H--U edges must saturate the disjoint endpoint-indexed / `B_1` reservoir.

That simultaneous saturation is far more rigid than the aggregate inequality records. In particular, the same endpoint-indexed code classes are already load-bearing for triangle-free H--U edges and U-certified H--H edges. Any incompatibility among those roles can improve `(HU-SLACK)` beyond linear or force a new located quadratic defect.

Upstream caveat unchanged: bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`, so this remains conditional downstream mathematics.