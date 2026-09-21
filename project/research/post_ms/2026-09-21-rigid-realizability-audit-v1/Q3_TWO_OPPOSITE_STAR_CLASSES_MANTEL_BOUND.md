# Exact Mantel bound for the two-opposite-star-class face

Date: 2026-09-21

## Setup

Work in the Q3-root antipodal-transversal branch and suppose the physical star-code population uses only one antipodal pair of centres:

- `X`: vertices with code `S_c`, `|X|=p`;
- `Z`: vertices with code `S_{bar c}`, `|Z|=q`.

Other A-vertices, if present, may be halfcube-coded; the theorem concerns the induced star subgraph `G[X∪Z]` and its criticality certificates. Let

- `E_cross=e(X,Z)`;
- `M_cross=pq-E_cross`;
- `E_same=e(X)+e(Z)`.

## Key observation: same-centre edges have only the third-star mechanism

Take a same-centre edge `xy` with `x,y∈X`. From the exact star-side incident-edge classification:

- direct endpoint certification is impossible because `H_x=H_y=S_c` is not disjoint;
- antipode-B certification from x is impossible because y's code `S_c` does not contain the undominated antipode `bar c`;
- therefore any certificate from the x side must be a third-A certificate through some `z∈Z` with

  `xz` a nonedge, `yz` an edge,

  and y the unique common A-neighbour of x and z.

The symmetric statement holds if the edge is certified from y instead. Thus every same-centre X-edge determines a missing cross pair `(x,z)` or `(y,z)` for which the opposite endpoint of the X-edge is the unique common A-neighbour.

Exactly the same argument applies to a same-centre edge inside Z, with a missing cross pair to X.

## Physical injection

Choose one valid endpoint certificate for every same-centre star edge and map the edge to its missing cross pair.

This map is injective across **all** same-centre edges.

Indeed, fix one missing cross pair `x∈X`, `z∈Z`. Any third-star certificate using this pair requires a unique common A-neighbour y of x and z. If such y exists, it belongs either to X or to Z.

- If `y∈X`, the pair can certify the one same-centre edge `xy` and no Z-Z edge.
- If `y∈Z`, it can certify the one same-centre edge `zy` and no X-X edge.

A second same-centre edge using the same missing pair would require a second common A-neighbour, contradicting the certificate uniqueness condition.

Therefore

`E_same <= M_cross`.

## Exact edge bound

Consequently

`e(G[X∪Z]) = E_cross + E_same`

`<= E_cross + (pq-E_cross)`

`= pq`.

Hence

`e(G[X∪Z]) <= pq <= floor((p+q)^2/4)`.

This is an exact Mantel-strength bound obtained from D2C certificate geometry, even though `G[X∪Z]` need not itself be triangle-free.

## Equality interpretation

If `e(G[X∪Z])=pq`, then every missing cross edge is used exactly once as the endpoint pair of a unique induced P3 that replaces it by one same-centre edge. Thus equality is a literal edge-substitution system:

`missing opposite-centre edge  <->  one same-centre edge`.

The complete bipartite graph `K_{p,q}` is the zero-substitution equality face. Any non-bipartite equality graph must consist entirely of one-for-one substitutions satisfying the unique-common-neighbour condition.

## Consequence for the full Q3 programme

A dense star population concentrated in a single antipodal centre pair cannot beat the ordinary bipartite quadratic density. Therefore a star-supported construction capable of erasing the known linear gap of the odd-halfcube/parity-bridge family cannot obtain its gain merely by making one opposite star pair internally dense. Any genuine improvement must use either:

1. several star-centre antipodal pairs interacting at once;
2. halfcube-star edges in a way that changes the global A-edge accounting; or
3. an equality substitution system whose interaction with the mandatory three coordinate-halfcube directions reduces the surrounding linear tax.

This narrows the asymptotic star escape to a genuinely multi-centre or mixed-code phenomenon.
