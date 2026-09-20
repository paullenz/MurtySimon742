# First-strict buffer criticality: the whole outside-U layer misses Y

Date: 2026-09-20

Status: **internal conditional structural theorem** inside the already audited first-strict unloaded unique-X-hole branch. It uses raw D2C triangle-edge criticality and the repaired first-strict geometry; it does not assert that the rigid complete-cut hypotheses are realizable.

## Audit reconciliation

The binding 20 September red-team audit remains in force. In particular `X_3` remains the mandatory hostile control, the rigid complete-cut interface still has no positive actual-D2C fixture with `x>=3`, exact pair-local `Ccap_P/(ONE-P)/(CROWD)` remains local, and finite scans remain diagnostics only. The raw same-code audit at `2026-09-20-same-code-raw-criticality-audit-v1/` has passed independently.

Use the verified first-strict unloaded geometry from `BUFFER_FIRST_STRICT_LAYER.md`:

- `A=X dotcup Y`, `X--Y` complete, `x>=3`, `y>0`;
- every Y-code is `d`, every X-code is neither `d` nor `bar d`;
- `U_-=W_0 dotcup {b}`, every vertex of `U_-` has code `bar d`;
- `d_Y(b)=0`;
- `a_0` is the unique X non-neighbour of b;
- b is complete to `X\{a_0}` and to `U_o=U\U_-`.

Write `S_0={i:c(a_0)_i != d_i}`. Since `c(a_0)!=d`, `S_0` is nonempty. At every `i in S_0`, `a_0` and b choose the same `bar d` matched endpoint.

## Theorem 1 — outside-U / Y anticompleteness

> `E(U_o,Y)=emptyset`.

### Proof

Suppose `w in U_o` and `y in Y` satisfy `wy in E`. Since b is complete to `U_o`, `bw in E`. Both b and w lie in the root neighbourhood, so the edge `bw` lies in a triangle through the root and raw triangle-edge criticality applies.

For either orientation of `bw`, a witness cannot lie at the root, at a tight matched endpoint, or in U: the source is a U-vertex and any B/U witness would give the root as an extra common neighbour distinct from the U-head. Thus any witness must lie in A.

**Orientation `b -> w`.** A witness q must be nonadjacent to b and adjacent to w. Since `N_A(b)=X\{a_0}`, necessarily `q in Y union {a_0}`.

- If `q in Y`, then q and b share every vertex of `X\{a_0}` as a common neighbour. There are `x-1>=2` such vertices, so the common neighbourhood cannot be the singleton `{w}`.
- If `q=a_0`, then b and `a_0` share a tight matched endpoint in every coordinate of the nonempty set `S_0`. Such a matched vertex is distinct from the U-head w, again contradicting singleton common neighbourhood.

So this orientation is impossible.

**Orientation `w -> b`.** An A-witness q must be adjacent to b, hence `q in X\{a_0}`. But w is adjacent to y by assumption and every such q is adjacent to y because `X--Y` is complete. Thus y is a common neighbour of w and q distinct from the head b. This orientation is impossible too.

The triangle edge `bw` therefore has no raw D2C certificate, contradiction. `square`

This theorem is upstream of all later all-R grid/resource calculations and uses no source-tuple capacity theorem.

## Theorem 2 — no outside `bar d` code

> `U_o cap V_{bar d}=emptyset`.

### Proof

Suppose `w in U_o` has code `bar d`. Then b and w are adjacent (b is complete to `U_o`) and have the same tight code. The independently re-derived same-code theorem says that either U-source orientation requires an A-witness of complementary code d, hence a witness in Y.

If the source is b, every Y-witness shares all `x-1>=2` vertices of `X\{a_0}` with b, so it cannot have singleton common neighbourhood `{w}`.

If the source is w, a Y-witness would have to be adjacent to the head b, but `d_Y(b)=0`.

Both orientations fail. `square`

## Consequences

1. No outside-U witness can certify an A-edge by being adjacent to a Y-head.
2. No outside-U witness can serve as a `bar d` complementary witness for a Y-source.
3. Any later complete-cut certificate argument in the first-strict branch must therefore use core/matched/A mechanisms, not an unpriced outside-U reservoir touching Y.

This is stronger than the earlier all-R fact that selected outside witnesses were Y-anticomplete: **every** vertex of `U_o` misses Y.