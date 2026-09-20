# Residual-one k=2 half-ray: first H--U orientation filter

Date: 2026-09-20

Status: **same-session conditional structural lemma**, downstream of the corrected minimal-B0 intermediate half-ray, the H--U triangle-scope lemma, and the standard rooted triangle-edge two-orientation theorem. No graph-level realizability claim is made.

## 1. Setup

Fix a triangular H--U edge

`h_i t`,

with `h_i in H` and `t in U`. Recall:

- every Y vertex is adjacent to every H vertex;
- every U vertex is adjacent to the root;
- for `h_i`, `c(h_i)=d xor e_i`;
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

This is a genuine location theorem, not a count.

On the corrected intermediate half-ray, global H/Y polarization already forces `d_Y(t)<=1` whenever `d_H(t)>0`. Hence `(HU-MATCHED-ONLY)` applies exactly to the H-multi-neighbour vertices carrying their unique possible Y-edge.

## 5. Reverse U-witnesses are endpoint-indexed

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

## 6. Combined H-side exceptional reservoir

Three phenomena are now charged to the same endpoint-indexed populations r_i:

1. U-certified H--H edges sourced at h_i;
2. possible triangle-free H--U edges incident with h_i;
3. reverse-U-certified triangular H--U edges sourced at h_i.

Each of the three totals is O(u), and all use the same disjoint code reservoir across i. This does not yet justify adding their counts, because one physical U vertex may participate in more than one role. But it does show that no quadratic H-side family can be explained by endpoint-indexed U witnesses alone.

Consequently any quadratic H--U incidence on the corrected half-ray must be carried mainly by

- matched-layer t-sourced certificates,
- non-U reverse certificates,
- or U vertices with very low H-degree.

The next attack should retain matched-coordinate identity in the first arm rather than replacing it by a scalar witness count.

Upstream caveat unchanged: bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`; `X_3` remains mandatory.