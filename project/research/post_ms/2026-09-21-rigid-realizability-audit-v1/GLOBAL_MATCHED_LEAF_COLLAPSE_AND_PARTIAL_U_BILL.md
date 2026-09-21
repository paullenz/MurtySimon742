# Rigid complete one-code cut: global matched-leaf collapse and partial U-forward slack

Date: 2026-09-21

Status: raw graph-theoretic consequence of the post-audit boundary-code-edge trichotomy and universal opposite-endpoint independence. It is upstream of the residual-one half-ray H--U machinery and is a necessary condition for an actual D2C graph to realize the rigid complete cut.

## 1. Setup

Use the notation of `RIGID_CUT_BOUNDARY_CODE_EDGE_TRICHOTOMY.md`. Thus `Y=A_d`, the cut `X--Y` is complete, and

- `I=I(d,X)` is the set of boundary coordinates exposed by X;
- `C=C(d,X)` is the set of coordinates on which every X-code agrees with d;
- `R_d` is the relative matched-row graph;
- a matched-forward boundary witness must be an opposite endpoint indexed by some `j in C` satisfying `N_{R_d}(j)={i}`.

Let `L(d,X)` be the set of heads i having such matched-forward support.

The companion theorem `UNIVERSAL_OPPOSITE_ENDPOINT_INDEPENDENCE.md` proves that the selected endpoints indexed by C form a clique in `R_d` whenever `|C|>=2`.

## 2. Global matched-forward support is at most two

### Theorem 2.1

For every rigid complete one-code cut,

> **`|L(d,X)| <= 2`.**

More precisely:

1. if `C=empty`, then `L=empty`;
2. if `|C|=1`, then `|L|<=1`;
3. if `|C|=2`, then `|L|<=2`, with two supported heads possible only when the two universal coordinates form an isolated `K_2` in `R_d`;
4. if `|C|>=3`, then `L=empty`.

### Proof

A matched-forward witness must be indexed by `j in C` and must be a global leaf of `R_d`, with its unique neighbour equal to the supported head i.

If C is empty there is no candidate j. If `|C|=1`, the sole candidate can be a global leaf and therefore supplies at most one head.

If `|C|>=2`, universal opposite-endpoint independence implies that `R_d[C]` is complete. For `|C|>=3`, every `j in C` already has at least two neighbours inside C, so no j can be a global leaf; hence no matched-forward support exists anywhere, not merely on universal heads.

For `|C|=2`, each universal coordinate already sees the other. A coordinate can be a global leaf only if that edge is its sole R_d edge. Hence at most the two universal coordinates can serve, and simultaneous support occurs exactly when their induced K2 is isolated from the rest of R_d. `square`

This strengthens the earlier universal-coordinate statement by controlling matched-forward witnesses globally.

## 3. Partial U-forward slack interpolation

Fix an exposed coordinate `i in I`. Let

- `r_i=|X_{gamma_i}|`, where `gamma_i=gamma(q_i^{d_i})` is the forced reverse X-code;
- `f_i` be the number of outside sources `y0 in Y` whose edge `y0 q_i^{d_i}` uses the U-forward mechanism;
- `W_i` be the set of actual unmatched witnesses used by those f_i edges;
- `t_w` the number of those sources served by `w in W_i`.

If coordinate i has no matched-forward support, fixed-source injectivity on the reverse arm gives

> `f_i >= (y-r_i)_+`.                                    `(3.1)`

For every `w in W_i`, the boundary trichotomy gives `c(w)=bar d xor e_i` and `N_X(w)=empty`. Since w is nonadjacent to each of its `t_w` source vertices in Y, the exact U-degree identity gives

> `epsilon_w >= p-y+t_w`.                                `(3.2)`

Therefore, whenever `f_i>0`,

> `sum_{w in W_i} epsilon_w`
> ` >= (p-y)|W_i|+f_i`.                                  `(3.3)`

If `p>=y`, this is minimized at one witness and, using `(3.1)`, yields

> **`sum_{w in W_i} epsilon_w >= p-r_i`**                `(3.4)`

whenever `r_i<y` and i has no matched-forward support.

Distinct coordinates use distinct one-match U-code classes `bar d xor e_i`, so these slack bills are physically disjoint and add in `E_U`.

## 4. Master boundary count

Let `J=I\L` be the exposed coordinates without matched-forward support. For each `i in J`, either `r_i>=y`, or the coordinate pays at least `p-r_i` U-slack when `p>=y`.

Independently, the reverse-gamma multiplicity theorem bounds the number of coordinates that can be carried by repeated large reverse classes under the A-slack ceiling. Together with `|L|<=2`, this gives the clean qualitative dichotomy:

> almost all exposed coordinates must either consume a distinct one-match U-forward class with located U-slack, or force large repeated gamma classes in X and hence gamma-collision A-slack.

This is the correct raw-realizability interface to feed into one-code survivor geometry; matched-forward support is only an O(1) exceptional channel.

## 5. Audit boundary

No graph-level reachability claim is made. The bounded actual-D2C regression still contains zero positive rigid complete pair-family cuts with `x>=3`; X_3 remains the mandatory negative control. The theorem above is a necessary condition *if* such a cut is realized.
