# A sharp-support dense family lies outside the matched-pair interface

21 September 2026. Internally proved; external review open.

Use the five-coordinate parity-plane family from `PARITY_PLANE_MINIMUM_ORDER_AND_IMPROVED_FAMILY.md`, with r=q or r=q+1, r>=1. The construction has n=18+r+q vertices and m=62+4r+4q+rq edges. Its only maximum-degree roots are cube vertices 1 and 2, both of degree b=10+q.

At either maximum-degree root the exact rooted quantities are

    a=7+r, b=u=10+q, p=0, lambda=2+q-r,
    Q=13, f=e(G[A])=15+r,
    delta=b(n-b)-m=18+6r+4q,
    rho=33+7r+4q, delta=rho-f.

Here rho is the unused selected B-slot count (renamed from the project's usual r to avoid collision with the construction multiplicity). Thus the family has positive linear residual defect and no tight-pair interface. Its existence does not validate the conditional rigid-Hall capacity theorem.

## Maximum degree and the tight-pair obstruction

The degrees in the construction are:

- odd cube vertices with bit 2 zero (1,2): 10+q;
- odd cube vertices with bit 2 one (4,7): 9+q;
- even cube vertices with bit 2 zero (0,3): 8+r;
- even cube vertices with bit 2 one (5,6): 7+r;
- original root: 8;
- designated P0 hub: 8+q; other P0 vertices: 4+q;
- P1 vertices: 4+r;
- four connected coordinate vertices and all star vertices: 5;
- the isolated C20 coordinate vertex: 4.

For r-q in {0,1}, vertices 1 and 2 are therefore exactly the maximum-degree roots. It suffices to work at w=1; translation by cube vector 3 swaps roots 1,2 and preserves the construction up to code relabelling.

Every tight pair x,y at root w must satisfy

    d(x)+d(y)=n-1,

because N(x) intersect N(y)={w} and each other vertex outside x,y,w is adjacent to exactly one endpoint.

If r=q=k, every vertex in N(w) has degree at most k+8, so any pair has degree sum at most 2k+16<n-1=2k+17. No tight pair exists.

If r=k+1,q=k, the only neighbours of w of degree k+9 are cube vertices 0,3. Every other neighbour has degree at most k+8. Hence the only possible degree-sum candidate is {0,3}. These two cube vertices have both 1 and 2 as common neighbours (and also the original root), so they are not a tight pair at w. This includes k=0. Thus p=0 throughout both balanced subfamilies.

## Exact triangle and outside-edge counts

For w=1 its neighbours, besides the q P1 vertices, are

    original root; cube vertices 0,3,5;
    C01,C10,C20; S0,S3,S5.

The induced neighbourhood has three original-root/cube edges, six coordinate/cube edges, three star/cube edges and the single star edge S0--S3. No other edge occurs. Hence Q=13, independently of r,q.

The outside set A consists of cube vertices 2,4,6,7; coordinates C00,C11; star S6; and the r P0 vertices. It has three cube edges, six coordinate/cube edges, four S6/cube edges, r parity/cube edges and two coordinate/hub edges. Therefore f=15+r.

The expressions for a,b,lambda and delta follow by counting and expansion. Finally the exact rooted residual identity gives rho=delta+f=33+7r+4q. Independent replay of the original selected-slot extraction verifies this value for six balanced parameter pairs at both maximum roots.

## Consequence for the research plan

The original construction root sees Q3 and four antipodal pairs, but it is not maximum-degree and has negative lambda. Maximum-degree rooting instead produces p=0 and Q=13. This provides an explicit infinite example of why successful Q3 star geometry cannot automatically be fed into the nonnegative-lambda matched-pair branch. The residual ledger remains meaningful; the rigid-pair theorem does not apply.
