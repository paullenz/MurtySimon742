# Six-coordinate-witness tax for the two-opposite-star-class face

Date: 2026-09-21

## Setup

Continue in the Q3-root antipodal-transversal branch. Suppose the star-code population uses only one antipodal pair of centres:

- `X`: code `S_c`, `|X|=p>=1`;
- `Z`: code `S_{bar c}`, `|Z|=q>=1`.

Let `S=X∪Z`, `s=|S|`, and let `d_S(u)` denote degree inside the physical star subgraph.

The preceding exact Mantel theorem gives `e(S)<=pq`; this note extracts the additional **linear mixed-code tax** forced by criticality of star-to-B leaf edges.

## Each side forces three coordinate witness types

Fix `x∈X`. For each leaf

`s_i=c⊕e_i`  (`i=1,2,3`)

of the star code `S_c`, criticality of the physical A-B edge `x s_i` has only the two star-fan mechanisms:

1. a nonadjacent halfcube certificate `D_{s_i}`;
2. an adjacent star of code `S_{bar s_i}`.

But

`bar s_i = bar c ⊕ e_i`

has Hamming distance two from c and one from `bar c`, so this star code is neither `S_c` nor `S_{bar c}`. By the two-centre hypothesis it is absent. Therefore mechanism 2 is unavailable.

Hence every x and every coordinate i has a physical halfcube certificate of code

`D_{s_i}=C_i^{1-c_i}`.

For the critical pair `(x,h_i)` to work, `xh_i` is a nonedge and x,h_i have no common A-neighbour. Thus

`N_A(h_i) ∩ N_A(x) = ∅`.

Applying the same argument to `z∈Z` forces three halfcube certificates of the opposite coordinate orientations

`C_i^{c_i}`.

The six code types

`C_i^{1-c_i}, C_i^{c_i}` for `i=1,2,3`

are pairwise distinct, so choosing one certificate in each type produces six distinct physical halfcube vertices.

## Degree-to-missing-edge conversion

Choose `x∈X` of maximum star degree within X and `z∈Z` of maximum star degree within Z. Let

`h_1,h_2,h_3`

be leaf certificates for x and

`k_1,k_2,k_3`

leaf certificates for z.

Because x and `h_i` have no common A-neighbour, each `h_i` is nonadjacent not only to x but to every star neighbour of x. Therefore `h_i` misses at least

`d_S(x)+1`

physical pairs into S. Similarly each `k_i` misses at least `d_S(z)+1` pairs into S.

Since the six witnesses are distinct, these missing witness-star pairs are disjoint as edge variables. Hence the six mandatory coordinate witnesses create at least

`3(d_S(x)+1)+3(d_S(z)+1)`

missing A-pairs between those witnesses and the star population.

Equivalently,

`missing(W,S) >= 3(d_S(x)+d_S(z)+2)`.

## Density form

The class-average star degrees satisfy

`d_S(x) >= (2e(X)+e(X,Z))/p`,

`d_S(z) >= (2e(Z)+e(X,Z))/q`.

In particular their sum is at least the overall average star degree:

`d_S(x)+d_S(z) >= 2e(S)/s`.

Therefore the six-coordinate-witness tax has the clean global form

`missing(W,S) >= 6 e(S)/s + 6`.

Thus whenever the star core has quadratic density, the mandatory coordinate witnesses force a **linear number of absent mixed A-edges**. If `e(S)=(1/4-o(1))s^2`, then

`missing(W,S) >= (3/2-o(1))s`.

For the literal complete bipartite core `K_{p,q}`, the sharper class-max form gives exactly the lower bill

`3(p+q+2)=3s+6`.

## Significance

The two-opposite-star-class escape is therefore constrained at both scales:

1. its internal star density cannot exceed Mantel: `e(S)<=pq<=s^2/4`;
2. approaching that quadratic density necessarily makes the six coordinate certificate vertices sparse toward the star core, producing a linear mixed-edge deficit.

This is the first direct graph-level mechanism in the star branch that recovers a linear tax from raw criticality rather than from the conditional rigid-cut/Hall machinery. To turn it into a full gap from `M(n)`, the remaining task is to account for edges among the six coordinate witnesses and any additional halfcube population without double-counting the same missing pairs.
