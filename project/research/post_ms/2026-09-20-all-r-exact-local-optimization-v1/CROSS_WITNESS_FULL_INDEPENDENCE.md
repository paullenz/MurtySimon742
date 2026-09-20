# Full independence of the outside cross-witness population

Date: 2026-09-20

Status: internal conditional strengthening of `CROSS_WITNESS_INDEPENDENCE.md`.

The earlier note proves independence separately inside the C-type and D-type outside cross-witness families. In fact cross-type edges are impossible as well.

Let `w_C` be a C-type witness with code `bar C` and fixed Y-head `N_Y(w_C)={y_C}`. Let `w_D` be a D-type witness with code `bar d` and fixed X-head `N_X(w_D)={x_D}`. Suppose `w_Cw_D` were an edge.

Because both endpoints lie in U, a raw triangle-edge certificate cannot use a U-witness or matched-B witness: the root is then an extra common neighbour. Consider the two source orientations.

### Source `w_C`, head `w_D`

An X-witness must be the unique X-neighbour `x_D` of the head. But every X-vertex is adjacent to `y_C`, and `w_Cy_C` is an edge, so `y_C` is an extra common neighbour of source and witness.

A Y-witness cannot be `y_C` because it is adjacent to the source. Any other Y-witness has code d, while `w_C` has code `bar C`; these two codes agree in the single coordinate where C differs from d, so source and witness share a tight matched neighbour, again contradicting singleton common neighbourhood.

### Source `w_D`, head `w_C`

An X-witness has code C while `w_D` has code `bar d`; those codes agree in the special coordinate, so they share a tight matched neighbour unless the witness is the source-adjacent head `x_D`, which is invalid as a nonadjacent witness anyway.

The only Y-vertex adjacent to the head `w_C` is `y_C`. If `y_C` is nonadjacent to the source, it still shares the X-neighbour `x_D` with `w_D` because X--Y is complete. Thus it cannot give a singleton common neighbourhood.

Both orientations fail. Hence

> the entire outside cross-witness set `C_cross union D_cross` is independent. `(CROSS-INDEP)`

If `s=s_C+s_D`, the physical triangle ceiling therefore sharpens from separate same-type charges to

> `q <= binom(u,2)-binom(k+1,2)-k-d-binom(J,2)-binom(s,2)`. `(Q-CROSS-ALL)`

The parameter-only corollary remains `-binom(min{g,y},2)` because the residual-grid cover already forces `s>=min{g,y}`. The focused e(X)=0 diagnostic count does not change from the separate-independence checkpoint because its cheapest feasible covers already concentrate in one witness type; nevertheless `(CROSS-INDEP)` is structurally stronger and should replace the split independence statement downstream.
