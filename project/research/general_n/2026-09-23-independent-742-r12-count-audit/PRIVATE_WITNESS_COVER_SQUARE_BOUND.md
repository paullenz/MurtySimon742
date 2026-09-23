# Private-witness cover square bound

23 September 2026. Status: **proved internal structural lemma**, conditional only on the exact-H private-witness setup already preserved in `MINIMAL_HALL_MAXIMIZER_GEOMETRY.md` and `DEFICIT_MATCHING_REDUCTION.md`. This does not by itself exclude `H>=15`.

Let `L` be an inclusion-minimal exact-H maximizer. For each `i in L`, let `P_i` be its private certificate-edge set and write `p_i=|P_i|`. Let `W` be the bipartite private-witness graph between `L` and `B`: `i--t` means that a private physical edge `u_i t in P_i` certifies `N(i) intersect N(t)={u_i}`. Thus `deg_W(i)=p_i`. For `t in B`, write `r_t=deg_W(t)`.

## Lemma 1: collision degree forces label misses

For every edge `i--t` of `W`,

`h_i >= r_t`.

Proof. Fix `t` and list its `r_t` incident labels `i_1,...,i_r`, with private physical certificate edges `u_1 t,...,u_r t`. The private sets `P_i` are pairwise disjoint, so these physical edges are distinct and hence the `u_j` are distinct. For the pair `(i_j,t)`, `u_j` is the unique common neighbour. Therefore `i_j` is not adjacent to `u_k` for any `k != j`, because each `u_k` is adjacent to `t` and would otherwise be a second common neighbour of `i_j,t`. Also `i_j` is not adjacent to `t` itself. All `t,u_k (k!=j)` lie in `B`, giving `r_t` distinct B-vertices missed by `i_j`. Hence `h_{i_j}>=r_t`. QED.

This is a genuine multiplicity charge: reuse of one missed endpoint by many private witnesses automatically raises the missed-B load of every participating label. It does not assert injectivity and is compatible with the preserved collision negative controls.

## Lemma 2: square bound outside any private-witness vertex cover

Let `X union Y` be any vertex cover of `W`, with `X subset L`, `Y subset B`, and put `U=L minus X`, `y=|Y|`. Then all private-witness neighbours of every `i in U` lie in `Y`. The total private surplus of the uncovered labels obeys

`sum_{i in U} (2p_i-h_i) <= y^2`.

Proof. For `i in U`, all `p_i` distinct missed endpoints lie in `Y`, so `p_i<=y`; also `p_i<=h_i`. By Lemma 1, for every `t in N_W(i)`, `h_i>=r_t`. Since `h_i>0`,

`2p_i-h_i <= p_i^2/h_i`,

because the difference between the right side and the left side is `(h_i-p_i)^2/h_i`. Therefore

`2p_i-h_i <= sum_{t in N_W(i)} p_i/h_i <= sum_{t in N_W(i)} p_i/r_t`.

Summing over `i in U` and reversing the order,

`sum_{i in U}(2p_i-h_i) <= sum_{t in Y} (1/r_t) sum_{i in U intersect N_W(t)} p_i`.

For each fixed `t`, every such `p_i<=y`, while `|U intersect N_W(t)|<=r_t`; hence the inner contribution is at most `y`. There are at most `y` vertices of `Y`, proving the `y^2` bound. QED.

The argument remains valid if some `t in Y` has no neighbour in `U`; it then contributes zero.

## Consequence for the concentrated-cover branch

The exact minimal-maximizer decomposition is

`H = sum_{i in L}(2p_i-h_i) + 2|Q|`,

where `Q` is the set of physical B-edges lying in at least two `C_i`. Thus every vertex cover `X union Y` of the private-witness graph gives

`H <= |Y|^2 + sum_{i in X}(2p_i-h_i) + 2|Q|`.

Combined with the strict-counterexample deficit reduction, one may take a cover with

`|X|+|Y| <= floor(D/(rho+1))`,

where `rho=2Delta-n` and `D=sum_x(Delta-d(x)) < n rho/2`.

This is a real strengthening of the previous pointwise statement `h_i<=2|Y|-1` outside `X`: the entire uncovered private surplus is quadratically controlled by the B-side cover size. It does **not** yet control the private surplus on `X` or the shared-edge term `2|Q|`, so no `H<15` theorem is claimed.

Useful small-cover corollaries are immediate: if `|Y|<=3`, uncovered private surplus is at most 9; if `|Y|<=2`, at most 4; if `Y` is empty, all private surplus lies on `X`.

## Next exact target

Derive a deficit/collision charge for the remaining concentrated part

`sum_{i in X}(2p_i-h_i) + 2|Q|`,

or show that an `H>=15` minimal maximizer can always be covered with a split for which the square term plus that concentrated part is below 15. Any such step must retain the actual-graph realizability boundary and the balanced complete-bipartite equality controls.
