# Mixed star-coordinate deficit with arbitrary coordinate multiplicity

Date: 2026-09-21

## Scope

In the Q3-root antipodal-transversal branch, suppose the only star centres present are one antipodal pair `c,bar c`, with physical star classes X,Z of sizes p,q. Allow arbitrary multiplicity in the six coordinate-halfcube codes, and allow parity-halfcube vertices as well.

Let T be the full physical coordinate-halfcube population, `t=|T|`, and `s=p+q`.

## Mandatory certifying nonedges

For every `x∈X` and each leaf `c⊕e_i` of `S_c`, the star-fan certificate alternatives are:

- a coordinate-halfcube vertex of code `C_i^{1-c_i}` nonadjacent to x; or
- an adjacent star of centre `bar c⊕e_i`.

The second centre is absent by hypothesis. Hence for every pair `(x,i)` there exists at least one physical vertex `h∈C_i^{1-c_i}` with `xh` a nonedge (indeed with x,h having no common A-neighbour).

These three missing pairs are distinct for each x because the three coordinate code classes are distinct. Summing over X gives at least `3p` missing X-T pairs.

Symmetrically, every `z∈Z` has at least one certifying nonneighbour in each opposite coordinate class `C_i^{c_i}`, giving at least `3q` further missing Z-T pairs. The X-side and Z-side pair sets are disjoint as physical pairs.

Therefore

`missing(S,T) >= 3(p+q)=3s`.

Equivalently,

`e(S,T) <= s t - 3s = s(t-3)`.

This holds for arbitrary coordinate multiplicities; it does not require sharing one witness across a star class. The minimal-face bound `e(S,T)<=3s` is the special case `t=6`.

## Additional consequence

All six coordinate code classes are necessarily nonempty whenever both opposite star classes occur: three orientations are forced by X leaf spokes and the complementary three by Z leaf spokes. Hence `t>=6`.

The remaining extra-multiplicity problem is now separated cleanly into three terms:

1. `e(S)<=pq` for the two-centre star core;
2. `e(S,T)<=s(t-3)` from the mandatory leaf-certificate nonedges;
3. coordinate-internal noncomplementary edges are charged to missing complementary coordinate pairs by `Q3_COORDINATE_CODE_GLOBAL_SUBSTITUTION_CHARGE.md`.

What is still uncontrolled is enough cross-direction coordinate density, parity interaction and star-parity density to determine whether these three exact bills already imply a global linear gap from M for the full two-star-centre branch.
