# Rigid complete cut: raw witness-channel collapse and the exact reuse obstruction

Date: 2026-09-21

## Scope

This note works directly from the graph-level criticality certificate used by `check_rigid_graph_level.py`.  It does **not** assume the conditional source-tuple capacity theorem, distinct physical-source identity, or global selected `(source,coordinate)` uniqueness.

Let `v` be the root, `B=N(v)`, `A=V(G)\(B∪{v})`, and let `A=X⊔Y`, with `|X|>=2`, such that every X-Y pair is an edge.  Suppose a crossing edge `yx` is certified in the orientation `source=y∈Y`, `head=x∈X` by a vertex `w`, meaning

- `yw` is a nonedge;
- `xw` is an edge; and
- `N(y)∩N(w)={x}`.

This is exactly the raw certificate predicate reconstructed in the graph-level checker.

## Lemma 1 — complete-cut witness-channel collapse

Every such witness `w` lies in `B`.

### Proof

`w≠v`, because `x∈A` is not adjacent to the root.  Also `w∉X`, because cross completeness gives `yw∈E(G)` for every `w∈X`, contrary to the witness nonedge `yw∉E(G)`.

If `w∈Y`, then `w` is adjacent to every vertex of `X`.  Since `|X|>=2`, choose `x'∈X\{x}`.  Cross completeness also gives `yx'∈E(G)`, so both `x` and `x'` are common neighbours of `y,w`, contradicting `N(y)∩N(w)={x}`.  Therefore `w∉A∪{v}`, hence `w∈B`. ∎

This explains, directly at graph level, why the rigid singleton-head regression has only the matched-B and U channels once the Hall cut is complete.

## Lemma 2 — per-source physical witness injection

Fix `y∈Y`.  Criticality witnesses for the crossing edges `yx`, `x∈X`, are necessarily pairwise distinct physical vertices.

### Proof

If one physical `w` certified both `yx` and `yx'` with `x≠x'`, then `w` is adjacent to both `x,x'`, while cross completeness makes `y` adjacent to both.  Thus `x,x'∈N(y)∩N(w)`, contradicting the singleton-common-neighbour condition for either certificate. ∎

Hence raw graph criticality already gives an injection

`X -> B\N(y)`

for each fixed source `y`.

## What raw criticality does *not* give

The argument above does **not** prohibit the same physical witness from serving the same head/coordinate for two different sources.  At the level of the certificate predicate alone, the local pattern

- distinct sources `y1,y2`;
- one head `x`;
- one witness `w`;
- `y1x,y2x,wx` edges;
- `y1w,y2w` nonedges;
- no other common neighbour of either `(yi,w)`;

simultaneously certifies both `y1x` and `y2x`.

This is not asserted to extend to a D2C graph; it is a hostile local model showing that **cross-source physical-witness uniqueness is not a consequence of the singleton criticality predicate by itself**.  Any proof of the audit-sensitive global selected `(source,coordinate)` uniqueness premise therefore needs an additional global ingredient (for example rooted-slot injection, Hall-selection structure, or a D2C-wide obstruction), not merely the local certificate axiom.

## Consequence for the current programme

The raw graph-level realizability gap is now more sharply localized:

1. complete Hall-cut geometry itself forces every Y→X certificate into `B`;
2. raw criticality gives exact per-source witness injection across X;
3. the unresolved step is **cross-source reuse** of the same B witness at the same coordinate/head.

The next useful test is therefore not another scalar rigid-capacity inequality.  It is to examine, on actual D2C roots and on the X3 negative control, whether global D2C criticality/rooted-slot structure forbids or limits this cross-source reuse, and if so to isolate the smallest exact graph-level statement.
