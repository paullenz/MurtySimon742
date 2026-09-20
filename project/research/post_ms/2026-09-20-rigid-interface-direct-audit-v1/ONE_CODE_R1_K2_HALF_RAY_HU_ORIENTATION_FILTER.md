# Residual-one k=2 half-ray: H--U orientation filter and private-foot forcing

Date: 2026-09-20

Status: **same-session conditional structural lemma**, downstream of the corrected minimal-B0 intermediate half-ray, the H--U triangle-scope lemma, and the standard rooted triangle-edge two-orientation theorem. No graph-level realizability claim is made.

## 1. Setup

Fix a triangular H--U edge

`h_i t`,

with `h_i in H` and `t in U`. Recall:

- every Y vertex is adjacent to every H vertex;
- every U vertex is adjacent to the root;
- for `h_i`, `c(h_i)=d xor e_i`;
- `q_i` is the private matched endpoint selected by `bar d` in coordinate i and is the unique A_X neighbour in that private fibre;
- only `O(p)` H--U edges can be triangle-free, so the present triangle-edge regime contains every quadratic H--U bulk.

Assume first that

`d_H(t)>=2`.

Choose another H-neighbour `h_l!=h_i` of t.

## 2. A t-sourced Y witness is impossible

Suppose the triangle-edge certificate is oriented from t toward singleton head h_i and uses a Y-witness y, so

`N(t) cap N(y)={h_i}`.

But y is adjacent to every H vertex. Since t is also adjacent to `h_l`, the vertex `h_l` is a second common neighbour of t and y, contradiction.

Therefore:

> **if `d_H(t)>=2`, no t-sourced certificate for `t h_i` can use a Y-witness.** `(HU-F1)`

## 3. A t-sourced U witness is always impossible

Any two U vertices share the root. Hence if a t-sourced certificate used a witness `w in U`, the root would be a common neighbour of t and w distinct from the prescribed singleton head h_i.

Thus:

> **no t-sourced H--U certificate can use a U-witness.**    `(HU-F2)`

This does not require `d_H(t)>=2`.

## 4. If t also touches Y, A_X witnesses disappear too

Now assume in addition

`d_Y(t)>0`,

and choose `y0 in N_Y(t)`.

Every vertex of A_X is adjacent to every Y vertex across the complete cut. Therefore if a t-sourced witness `a` lay in A_X, then y0 would be adjacent to both t and a, again producing an extra common neighbour.

Combining with `(HU-F1)` and `(HU-F2)` gives:

> **If `d_H(t)>=2` and `d_Y(t)>0`, then every t-sourced certificate for a triangular H--U edge `t h_i` must use the matched layer.** `(HU-MATCHED-ONLY)`

On the corrected intermediate half-ray, global H/Y polarization already forces `d_Y(t)<=1` whenever `d_H(t)>0`. Hence `(HU-MATCHED-ONLY)` applies exactly to the H-multi-neighbour vertices carrying their unique possible Y-edge.

## 5. The matched witness is forced to the private foot q_i

Continue under `d_H(t)>=2` and `d_Y(t)>0`, and suppose the edge `t h_i` is t-sourced. By `(HU-MATCHED-ONLY)` let r be its matched-layer witness:

`N(t) cap N(r)={h_i}`.                                   `(HU-M0)`

Because r must be adjacent to h_i, inspect the matched coordinates selected by `h_i=d xor e_i`.

- In coordinate i, h_i selects the `bar d` endpoint `q_i`.
- In every other private coordinate l, h_i agrees with d and selects the d-endpoint.
- At the residual coordinate j, `J2=empty` means h_i again agrees with d and selects the d-endpoint.

Every d-endpoint is adjacent to every Y vertex, while t has a Y-neighbour y0. Hence choosing any d-endpoint for r would make y0 a second common neighbour of t and r in `(HU-M0)`.

Therefore the only possible matched witness is

> **`r=q_i`.**                                            `(HU-PRIVATE)`

Thus the t-sourced certificate is forced into the exact singleton equation

> **`N(t) cap N(q_i)={h_i}`.**                            `(HU-QI)`

This is substantially sharper than mere matched-layer localization.

## 6. Coordinate hole consequence

Because q_i is the `bar d` endpoint in coordinate i, every U vertex w whose code selects q_i is adjacent to q_i. Equation `(HU-QI)` therefore forces t to be nonadjacent to every such w except the prescribed head h_i is in A_X, not U.

Equivalently, if

`U_i^-={w in U : c(w)_i=bar d_i}`,                       `(HU-UI)`

then every t-sourced H-edge of the present type forces

> **`N_U(t) cap U_i^-=empty`.**                           `(HU-IHOLE)`

So each private-foot orientation deletes a whole coordinate slice from the U-neighbourhood of t. Distinct H-head indices correspond to distinct private coordinates.

This is the first non-scalar mechanism on the intermediate half-ray: a U vertex using several t-sourced H certificates accumulates several coordinate restrictions on its possible U-neighbours.

## 7. Reverse U-witnesses are endpoint-indexed

Consider instead an orientation sourced at h_i with singleton head t, using a U-witness w:

`N(h_i) cap N(w)={t}`.

Any tight matched coordinate on which w agrees with `c(h_i)` would supply an extra matched common neighbour. Hence w must have the bitwise complementary code

> **`c(w)=bar(d) xor e_i`.**                               `(HU-RCODE)`

Moreover h_i is adjacent to every Y vertex, so any Y-neighbour of w would be an extra common neighbour. Therefore

> **`d_Y(w)=0`.**                                         `(HU-RY0)`

Thus reverse U-witnesses for H--U edges lie in the same endpoint-indexed class

`U_{bar(d) xor e_i}`

already controlling U-certified H--H edges and the only possible triangle-free H--U edge for index i.

For fixed ordered pair `(h_i,w)`, singleton common-neighbour uniqueness allows at most one head t. Therefore if

`r_i=|U_{bar(d) xor e_i}|`,

the number of H--U edges sourced at h_i and reverse-certified by U is at most r_i.

Summing over i,

> **the total number of reverse-U-certified H--U edges is at most `sum_i r_i <= u`.** `(HU-RCAP)`

## 8. Combined H-side exceptional reservoir

Three phenomena are charged to the same endpoint-indexed populations r_i:

1. U-certified H--H edges sourced at h_i;
2. possible triangle-free H--U edges incident with h_i;
3. reverse-U-certified triangular H--U edges sourced at h_i.

Each total is O(u), and all use the same disjoint code reservoir across i. They cannot simply be added because one physical U vertex may play several roles, but no quadratic H-side family can be explained by endpoint-indexed U witnesses alone.

The new private-foot forcing adds a different alternative: any H-multi/Y-active U vertex whose incident H-edge is t-sourced must pay a coordinate-slice exclusion `(HU-IHOLE)` in its U-neighbourhood.

The next attack should aggregate these exclusions only after controlling overlaps between the coordinate slices `U_i^-`; source-coordinate uniqueness or a direct code-incidence argument is the natural tool.

Upstream caveat unchanged: bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`; `X_3` remains mandatory.