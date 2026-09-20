# Residual-one k=2 half-ray: H--U triangle scope

Date: 2026-09-20

Status: **same-session conditional structural lemma**, under residual dimension one, `k=2`, `J2=empty`. It is written for the corrected intermediate half-ray with the mandatory two selected B0 witnesses, but the code-localization statement itself does not use its precise ratios. No graph-level realizability claim is made.

## 1. Setup

For each private coordinate `i in I=[p]\{j}`, the matched head `h_i in H` has code

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

then the tight matched-coordinate route supplies no common matched endpoint. But if `d_Y(t)>0`, choose `y in N_Y(t)`. Every Y vertex is adjacent to every H vertex, so `t-y-h_i-t` is a triangle.

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

are distinct. Therefore a fixed U vertex t can satisfy `(HU-TF)` for at most one H-index i.

Hence:

> **the total number of triangle-free H--U edges is at most u.** `(HU-CAP)`

On the corrected exact intermediate half-ray

`u=t+1`, `|H|=2t-1`,

so only `O(p)` H--U edges can escape triangle-edge criticality. Any quadratic H--U incidence is therefore overwhelmingly inside the valid two-orientation triangle regime.

## 4. Interaction with the H--H certificate split

The exceptional code class for `h_i t` is precisely

`U_{bar(d) xor e_i}`,

the same class from which a U-witness can certify an H--H edge sourced at `h_i`. Thus the two remaining H-side difficulties are not independent:

- using a large endpoint-indexed class to support H--H certificates also creates the only possible reservoir of triangle-free H--U edges for that index;
- the endpoint-indexed classes are disjoint over i, and their total population is at most u.

Retain the per-index populations

`r_i=|U_{bar(d) xor e_i}|`.

Then

`sum_i r_i<=u`,

and both H--H U-certificate capacity and H--U triangle exceptions are charged to the same `r_i` reservoir.

## 5. Corrected half-ray context

The companion half-ray note now uses the mandatory floor

`B0 superseteq W_s`, `|W_s|=2`.

In the minimal assignment `B0=W_s`, not `B0=empty`. Consequently it is **not** valid to claim every U vertex has Y-degree at most one. What survives exactly is:

- `e(Y)=0`;
- `e(Y,U)=O(p)` from the two-witness reverse-certificate capacity;
- `e(U)=O(p)` from B0 independence and D-source capacity;
- all but at most u H--U edges are triangular by `(HU-CAP)`.

Thus the H-side target is still a sparse Y/U system, but with two concentrated B0 witnesses rather than an empty B0 class.

## 6. Next attack

Orient the triangular H--U bulk while keeping `r_i` and the two selected B0 witnesses explicit. A U vertex with at least two H-neighbours cannot use a Y witness in a U-sourced singleton certificate for one H-edge, because every Y witness sees the other H-neighbour as an extra common neighbour. Combine that observation with the private-foot alternatives and source-coordinate uniqueness before any scalar summation.

Upstream caveat unchanged: zero positive actual-D2C rigid complete Hall-cut fixtures with `x>=3` in bounded regression, with `X_3` mandatory.