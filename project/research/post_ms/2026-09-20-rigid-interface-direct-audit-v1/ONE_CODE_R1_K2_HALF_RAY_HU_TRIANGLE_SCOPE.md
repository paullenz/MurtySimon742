# Residual-one k=2 half-ray: H--U triangle scope

Date: 2026-09-20

Status: **same-session conditional structural lemma**, under residual dimension one, `k=2`, `J2=empty`. It is written for the new intermediate half-ray but the code-localization statement itself does not use its precise ratios. No graph-level realizability claim is made.

## 1. Setup

For each private coordinate `i in I=[p]\{j}`, the matched head

`h_i in H`

has code

`c(h_i)=d xor e_i`.

Hence its bitwise complementary U-code is

> `bar(c(h_i))=bar(d) xor e_i`.                           `(HU-COMP)`

The tight matching has one chosen endpoint in each coordinate for every code.

## 2. Exact triangle classification

Fix an H--U edge `h_i t`.

If

`c(t) != bar(d) xor e_i`,

then `c(t)` is not the bitwise complement of `c(h_i)`. Therefore the two codes agree in at least one tight coordinate. The vertices `h_i` and t are both adjacent to the same matched endpoint in that coordinate, so the edge `h_i t` lies in a triangle.

If instead

`c(t)=bar(d) xor e_i`,

then the tight matched-coordinate route supplies no common matched endpoint. But if `d_Y(t)>0`, choose `y in N_Y(t)`. Every Y vertex is adjacent to every H vertex, so

`t-y-h_i-t`

is a triangle.

Consequently:

> **the edge `h_i t` can be triangle-free only if**
>
> **`c(t)=bar(d) xor e_i` and `d_Y(t)=0`.**               `(HU-TF)`

This is exactly the endpoint-indexed U-code class already appearing in the H--H U-certificate dichotomy.

## 3. At most one possible triangle-free H-edge per U vertex

For distinct private coordinates `i!=l`, the codes

`bar(d) xor e_i`

and

`bar(d) xor e_l`

are distinct. Therefore a fixed U vertex t can satisfy `(HU-TF)` for **at most one** H-index i.

Hence:

> **the total number of triangle-free H--U edges is at most u.** `(HU-CAP)`

On the exact intermediate half-ray

`u=t+1`, `|H|=2t-1`,

so only `O(p)` H--U edges can escape triangle-edge criticality. Any quadratic H--U incidence is therefore overwhelmingly inside the valid two-orientation triangle regime.

## 4. Interaction with the H--H certificate split

The exceptional code class for `h_i t` is precisely

`U_{bar(d) xor e_i}`,

the same class from which a U-witness can certify an H--H edge sourced at `h_i`. Thus the two remaining H-side difficulties are not independent:

- using a large endpoint-indexed class to support H--H certificates also creates the only possible reservoir of triangle-free H--U edges for that index;
- but the endpoint-indexed classes are disjoint over i, and their total population is at most u.

This suggests retaining the per-index populations

`r_i=|U_{bar(d) xor e_i}|`

rather than aggregating them immediately. One has

`sum_i r_i <= u`,

and both H--H U-certificate capacity and H--U triangle exceptions are charged to the same `r_i` reservoir.

## 5. Next attack

On the b=0 intermediate half-ray, every U vertex has `d_Y<=1`, `e(Y)=0`, and `e(U)<=2u`. The present lemma adds:

> **all but at most u H--U edges are triangular.**

The next raw-criticality step should therefore orient the triangular H--U edges while keeping the exceptional endpoint-indexed classes `r_i` explicit. In particular, a U vertex with at least two H-neighbours cannot use a Y witness in a U-sourced singleton certificate for one H-edge, because every Y witness sees the other H-neighbour as an extra common neighbour. That observation should be combined with the private-foot alternatives before any scalar summation.

Upstream caveat unchanged: zero positive actual-D2C rigid complete Hall-cut fixtures with `x>=3` in bounded regression, with `X_3` mandatory.