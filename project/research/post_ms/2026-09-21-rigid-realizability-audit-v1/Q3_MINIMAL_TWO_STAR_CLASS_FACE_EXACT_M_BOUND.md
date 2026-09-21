# Exact M(n) bound for the minimal two-opposite-star-class Q3 face

Date: 2026-09-21

## The face

Let `G` be diameter-2-critical with a root `v` whose neighbourhood `B=N(v)` induces `Q3`, and let `A=V(G)\(B∪{v})`. Assume every A-to-B neighbourhood is an antipodal transversal of Q3.

Assume further that the A-code population consists exactly of:

1. `p>=1` star vertices of code `S_c=N_Q[c]`;
2. `q>=1` star vertices of the opposite code `S_{bar c}`;
3. exactly one vertex in each of the six coordinate-halfcube codes `C_i^0,C_i^1`, `i=1,2,3`;
4. no parity-halfcube vertices and no other star or coordinate-code multiplicities.

Write `S` for the star population, `s=p+q`, and `W` for the six coordinate vertices. Then `|A|=a=s+6` and `n=a+9=s+15`.

The six coordinate codes are not an arbitrary assumption: they are the minimum leaf-certificate population forced by the two opposite star classes. This note proves that this **minimal** star-supported face already satisfies the target edge bound exactly.

## 1. Star-core bound

By `Q3_TWO_OPPOSITE_STAR_CLASSES_MANTEL_BOUND.md`,

`e(S) <= pq <= floor(s^2/4)`.

This bound allows non-bipartite one-for-one substitutions but no gain above the ordinary bipartite quadratic density.

## 2. Exact mixed star-coordinate ceiling

For every `x` of star type `S_c` and every leaf `s_i=c⊕e_i`, the star-fan alternatives for the physical edge `x s_i` are:

- a halfcube certificate of code `C_i^{1-c_i}`; or
- an adjacent star of code `S_{bar(c⊕e_i)}`.

The latter star centre is neither c nor `bar c`, hence is absent on the present face. Since there is exactly one physical vertex `h_i` of code `C_i^{1-c_i}`, that vertex must certify the leaf edge for **every** x of type `S_c`. In particular

`h_i x` is a nonedge for every `x∈X`.

Thus the three `h_i` are anticomplete to X.

Symmetrically, the three opposite-orientation coordinate witnesses `k_i` are anticomplete to the q vertices of `S_{bar c}`.

Therefore at least

`3p+3q=3s`

of the `6s` possible W-S pairs are missing, and hence

`e(W,S) <= 3s`.

No no-common-neighbour strengthening is needed for this ceiling.

## 3. Internal six-witness ceiling

Consider an A-edge incident to a coordinate-halfcube vertex h of code `C_i^epsilon`.

From h's side:

- a direct endpoint certificate is possible only when the other endpoint has the disjoint code `C_i^{1-epsilon}`;
- there is no B-target certificate, because a coordinate halfcube dominates every B-vertex outside the halfcube through its unique crossing cube neighbour, while vertices inside the halfcube are already adjacent to h;
- any third-A target must have B-code disjoint from `C_i^epsilon`, and among the 16 antipodal transversals the unique disjoint code is again `C_i^{1-epsilon}`.

Hence every W-edge not joining a complementary coordinate pair must be certified through a **missing complementary pair** whose two endpoints have the other edge endpoint as their unique common A-neighbour.

There are exactly three complementary physical pairs in W. Let `E_comp` of them be present. The remaining `3-E_comp` missing complementary pairs can each support at most two W-edges, namely the two sides of their one unique induced P3. Therefore

`e(W) <= E_comp + 2(3-E_comp) = 6-E_comp <= 6`.

## 4. Total A-edge bound

Combining the three independent edge classes,

`e(A) = e(S)+e(W,S)+e(W)`

`<= floor(s^2/4) + 3s + 6`.

Since `a=s+6`,

`floor(a^2/4)-3`

`= floor((s+6)^2/4)-3`

`= floor(s^2/4)+3s+6`.

Therefore

`e(A) <= floor(a^2/4)-3`.

For a Q3 root with every A-code of size four,

`e(G)=8+12+4a+e(A)=20+4a+e(A)`.

Also

`M(n)=floor((n-1)^2/4)+1`

with `n=a+9`, so

`M(n)=floor(a^2/4)+4a+17`.

Thus

`e(G) <= 20+4a+[floor(a^2/4)-3]`

`= floor(a^2/4)+4a+17`

`= M(n)`.

Hence the entire minimal two-opposite-star-class face satisfies

`boxed: e(G) <= M(n)`.

## 5. Equality requirements

Equality can occur only if all three bounds are tight simultaneously:

1. `pq=floor(s^2/4)`, so the two star multiplicities are balanced;
2. the star core attains the exact two-class Mantel bound, allowing only one-for-one cross-nonedge/same-centre substitutions;
3. exactly half of the W-S pairs are present, saturating `e(W,S)=3s`;
4. `e(W)=6`, forcing all three complementary coordinate pairs to be absent and each to support a full induced-P3 substitution, or another certificate pattern attaining the same six-edge ceiling.

These equality conditions are highly rigid and remain to be checked against the full D2C constraints. The present theorem does not claim equality is realizable; it proves the required upper bound throughout this face.

## Significance

This is a genuine graph-level closure inside the Q3 antipodal-transversal programme, not a conditional rigid-cut/Hall inequality. It shows that the most economical way to add a large opposite-star bipartite core to the six mandatory coordinate witnesses cannot exceed `M(n)`. Any star-supported counterexample above M must therefore escape the minimal face by adding at least one of:

- a third star-centre class;
- extra multiplicity in one of the coordinate-halfcube codes;
- a parity-halfcube vertex;
- or a non-antipodal-transversal A-to-B neighbourhood.

Those are now the precise next branches rather than an undifferentiated star search.
