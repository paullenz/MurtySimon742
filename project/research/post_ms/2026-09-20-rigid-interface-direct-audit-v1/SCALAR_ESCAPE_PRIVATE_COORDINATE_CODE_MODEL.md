# Abstract private-coordinate code model for the scalar escape ray

Date: 2026-09-20

Status: same-session hostile diagnostic. This is **not** a D2C graph construction; it only tests whether the explicit large-gap ray is already impossible at the Boolean/private-coordinate level.

For the ray

`p=3t, y=t, x=5t, g_P=2t, k_P=3t, rho=2t`, `t>=2`,

choose the outside source code

`d=0^{3t}`.

Use `2t` distinct tight coordinates `1,...,2t` as the singleton matched-head support counted by `rho`. Abstractly assign the `d`-gamma matched endpoint in coordinate i to head `h_i`, and give that head the Boolean code

> `c(h_i)=e_i`,

where `e_i` is the unit vector with its unique 1 in coordinate i.

Then:

1. every `h_i` differs from `d` in its assigned private coordinate, as required for a matched endpoint nonadjacent to the d-source to be adjacent to that head;
2. the private coordinates are distinct, so one tight fibre contributes only one distinct singleton head;
3. `d_H(c(h_i),c(h_j))=2` for `i!=j`, matching the near-rigid conclusion that selected matched-covered heads are pairwise non-complementary and separated by at least two coordinates;
4. no `c(h_i)` is `d` or `bar d`, so these heads lie outside the outside pair P={d,bar d};
5. no two `c(h_i)` are complementary for `p=3t>=6`.

The remaining `x-rho=3t` crossing heads are precisely the number that the one-code theorem forces into the complementary U-witness channel.

Therefore:

> **the ray is not killed by private-coordinate/Hamming combinatorics alone.**

Any contradiction must use additional graph structure: actual matched-row/gamma realizability beyond this local incidence model, per-vertex U-witness reuse and its located nonedges/slack, the rooted residual identity, or the possibility that the rigid complete-cut event is unrealizable in an actual D2C graph.

This diagnostic also explains why the scalar Hamming floor is asymptotically attainable in order: the selected 2t heads can be separated using exactly 2t private coordinates while p=3t leaves a further t coordinates unused by this support model.
