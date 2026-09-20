# Residual-one k=2: Y-independence and H--H certificate split

Date: 2026-09-20

Status: **same-session conditional structural strengthening**, under the rigid one-code residual-one branch, `k=2`, `J2=empty`, `p>=3`. No finite scan is used. This note corrects the live interpretation in `ONE_CODE_R1_K2_A_SIDE_COMPENSATOR_IDENTITY.md`: the class `B_+=U_bar(d)\B0` is a *location candidate* for a Y--Y complementary witness, but in fact no such witness can satisfy the singleton equation. Thus the Y-compensated arm disappears.

The upstream trust boundary is unchanged: the rigid complete Hall cut has no positive bounded actual-D2C fixture with `x>=3`, and `X_3` remains mandatory.

## 1. Setup

On the exact low-k ray,

- `u=x=p+1`, `y=|Y|=p-1`, `|H|=p-1`;
- `Y=A_d`;
- `K=A_C`, `C=d xor e_j`, `|K|=2`;
- for each private coordinate `i in I=[p]\{j}`, the matched head `h_i in H` has code `d xor e_i` because `J2=empty`;
- `q_i` denotes the tight matched endpoint selected by `bar d`; it has unique `A_X`-neighbour `h_i`;
- `B0={w in U_bar(d):d_H(w)=0}`.

The preceding hostile-replayed chain gives:

1. every `B0` vertex is Y-anticomplete;
2. every `bar d` vertex outside B0 has an H-neighbour;
3. the global polarization `d_H(t)>0 => d_Y(t)<=1` for every outside escape `t`.

## 2. Y is independent

> **THEOREM (Y-IND).** `G[Y]` is edgeless.

Suppose `y0 y1 in E(Y)`. Both endpoints have code d. By the repaired raw same-code criticality theorem, either orientation of this same-code A-edge requires a physical complementary witness of code `bar d`. Since `A_bar(d)=empty` in the present residual-one code repertoire, the witness lies in `U_bar(d)`.

Take one valid orientation, with source `y0`, singleton head `y1`, and witness `w in U_bar(d)`, so

`N(y0) cap N(w)={y1}`.

There are two possibilities.

### w in B0

Every B0 vertex is Y-anticomplete. Hence `w y1` is absent, contradicting the requirement that the witness be adjacent to the singleton head.

### w notin B0

Then w has an H-neighbour h. But every Y-vertex is adjacent to every H-vertex. Thus h is adjacent to both source y0 and witness w, producing a common neighbour distinct from the prescribed head y1. This contradicts the singleton equation.

Both possibilities fail. Reversing the orientation is identical. Hence no Y--Y edge exists.

> **`e(Y)=0`.**                                              `(YI-1)`

This supersedes the predecessor sentence that dense Y compensation could be supplied by a linear `B_+` witness class. `B_+` vertices cannot witness a Y--Y edge precisely because their H-neighbour becomes an illicit second common neighbour.

## 3. Consequence for A-side slack

The exact Y identity from the compensator note becomes

> **`L_Y=Z_{Y,U}-|Y|`.**                                  `(YI-2)`

Thus every quadratic Y--U hole block feeds directly into A-side slack. There is no internal Y-edge compensation term left.

The H-side identity remains

`L_H=Z_{H,U}+|H|-2e(H)`.

Hence low `L_A` can now be achieved only through the H layer; there is no Y-dense arm.

## 4. Exact H--H certificate dichotomy

Fix a distinct pair `i,l in I` with `h_i h_l in E(H)`. Consider an orientation sourced at `h_l`, with singleton head `h_i` and witness r:

`N(h_l) cap N(r)={h_i}`.                                  `(HH-0)`

The witness has only two possible physical forms.

### 4.1 Matched witness

The codes of h_l and h_i agree with d outside coordinates l and i. A matched endpoint outside fibre i cannot distinguish the required head from the source without creating an already-shared fibre endpoint; the residual fibre j cannot distinguish them because `J2=empty`; the endpoint q_l is adjacent to the source h_l rather than serving as its non-neighbour witness.

The unique private matched endpoint which can realize `(HH-0)` is

> **`r=q_i`.**                                             `(HH-M)`

This is exactly the private foot of the singleton head h_i.

### 4.2 U witness

If r lies in U, then source h_l and witness r must share no matched endpoint outside the prescribed A-head. Therefore their p-bit matched-fibre selections are complementary. Since

`c(h_l)=d xor e_l`,

we obtain

> **`c(r)=bar(d) xor e_l`.**                               `(HH-U-CODE)`

Moreover h_l is complete to Y. Any Y-neighbour of r would therefore be a second common neighbour in `(HH-0)`. Thus

> **`N_Y(r)=empty`.**                                     `(HH-U-Y0)`

The reverse orientation has the symmetric alternatives `q_l` or a Y-anticomplete witness in `U_{bar(d) xor e_i}`.

Consequently every H--H edge is certified either by one of its two private feet or by an endpoint-indexed U-code class.

## 5. Global capacity of U-certified H--H edges

Orient every H--H edge by one valid certificate. If an edge is U-certified and its source is h_l, its witness lies in the class

`U_{bar(d) xor e_l}`.

For one fixed source h_l, one physical witness cannot certify two different singleton heads. Therefore the number of U-certified outgoing edges from h_l is at most

`|U_{bar(d) xor e_l}|`.

The code classes for distinct l are disjoint. Summing over all l gives

> **the total number of U-certified H--H edges is at most u=p+1.** `(HH-UCAP)`

Thus all but O(p) edges of a dense H graph must be certified by private feet.

## 6. B+ touched set is internally sparse

Let

`B_+=U_bar(d)\B0`

and let

`S={h_i in H : N_{B_+}(h_i) != empty}`,

with `s=|S|`.

Take an edge `h_i h_l` with both endpoints in S.

- The private-foot orientation sourced at h_l through q_i is impossible: choose `w in B_+ cap N(h_l)`. Because `c(w)=bar d`, w is adjacent to q_i. Then w is a second common neighbour of h_l and q_i, distinct from h_i.
- Symmetrically, the orientation sourced at h_i through q_l is impossible.

Therefore every edge of `G[H[S]]` must be U-certified. Applying `(HH-UCAP)` gives

> **`e(H[S]) <= p+1`.**                                   `(HH-S-SPARSE)`

Hence

> **`e(H) <= binom(p-1,2)-binom(s,2)+(p+1)`.**            `(HH-HMAX)`

Combining this with the exact global escape hole block and `(YI-1)` yields the safe exact A-slack consequence

> **`L_A >= [s(s-1)-2(p+1)]_+`.**                        `(HH-LA)`

The important point is structural: a linear B+ population can reduce its own U-slack only by touching many H vertices, but a large touched set destroys the only remaining internal A-side compensator.

## 7. B+ slack versus touched-set size

Write `b_+=|B_+|` and `T=e(B_+,H)`. For `w in B_+`, global polarization gives `d_Y(w)<=1`, while `d_K(w)<=2`. Hence

`z_A(w)>=2p-3-d_H(w)`.

Using the exact U identity

`z_A(w)+m_U(w)=p+epsilon_w`,

we obtain

`epsilon_w>=p-3-d_H(w)+m_U(w)`.

Summing over B+ and dropping the nonnegative missing-U incidence term,

> **`E_U(B_+) >= b_+(p-3)-T`.**                           `(HH-BSLACK)`

Since `T<=b_+ s`,

> **`E_U(B_+) >= b_+[p-3-s]_+`.**                        `(HH-BSLACK2)`

Thus B+ cannot simultaneously be linear, low-slack, and supported on a small H-set.

## 8. Strategic consequence

The predecessor H-dense / Y-dense split is now replaced by a single live arm:

> **all low-A-slack compensation must occur in H, and all but O(p) dense-H edges must be private-foot certified.**

The next attack should therefore combine:

1. `e(Y)=0`;
2. the H--H private-foot/U dichotomy;
3. the global H/Y escape polarization;
4. B0 independence and U-source collapse;
5. the exact score inequality `E_U+L_A<=C0`.

In particular, dense H forces most H--H edges onto private feet, while any attempt to use H-positive `bar d` vertices to alter the U geometry creates an internally sparse touched set and a direct B+ slack bill.

No claim about graph-level realizability of the rigid interface is made.