#!/usr/bin/env python3
"""Direct graph-level verification, independent of the code-relation pruning."""
from itertools import product
from pathlib import Path
import json
from check_star_support import graph,d2c

def build(r,q,coordinate_counts=(1,1,1,1,1,1),star_codes=('S0','S3','S5','S6'),forest=((0,1),(0,2),(0,3))):
    coords=[k for k,t in zip(('C00','C01','C10','C11','C20','C21'),coordinate_counts) for _ in range(t)]
    t=len(coords);s=len(star_codes);h=t+s
    codes=coords+list(star_codes)+['P0']*r+['P1']*q
    ae=[(t+x,t+y) for x,y in forest]+[(i,h) for i in range(t)]+[(h+i,h+r+j) for i in range(r) for j in range(q)]
    return graph(codes,ae),codes,ae

def main():
    checks=[]
    for r,q in product(range(1,5),range(5)):
        adj,codes,ae=build(r,q)
        assert d2c(adj),(r,q)
        n=len(adj);m=sum(map(len,adj))//2;a=n-9
        assert m==29+4*a+r*q
        gap=((n-1)**2//4+1)-m
        assert gap==5*n-82+((r+q)**2//4-r*q)
        checks.append({'r':r,'q':q,'n':n,'m':m,'gap_from_M':gap,'all_edges_critical':True})
    extras=[((2,1,3,1,2,1),('S0','S3','S5','S6'),((0,1),(2,3))),
            ((1,2,1,2,1,2),('S0','S3','S5','S6','S3','S0'),((0,1),(0,2),(0,3),(4,5)))]
    for counts,stars,forest in extras:
        adj,codes,ae=build(2,2,counts,stars,forest)
        assert d2c(adj)
        t=sum(counts);s=len(stars);a=len(codes)
        assert sum(map(len,adj))//2==20+4*a+t+len(forest)+4
        checks.append({'variant':'arbitrary multiplicity / multiple star components','n':len(adj),'m':sum(map(len,adj))//2,'all_edges_critical':True})
    # Deliberately violate a hypothesis: a triangle has no leaf edge and its
    # three star edges have competing antipode bridges.
    bad,_,_=build(1,1,star_codes=('S0','S3','S5','S6'),forest=((0,1),(1,2),(2,0),(2,3)))
    assert not d2c(bad)
    smallest,codes,ae=build(1,0)
    data={'scope':'22 exact finite controls of an independently hand-proved unbounded family','checks':checks,
          'invalid_non_star_forest_rejected':True,'smallest_fixture':{'codes':codes,'A_edges':ae,'adjacency':[sorted(v) for v in smallest]}}
    Path(__file__).with_name('STAR_FOREST_FAMILY_RESULTS.json').write_text(json.dumps(data,indent=2)+'\n')
    print('PASS: 22 direct D2C checks, exact density/gap formulas, one invalid-forest negative control; smallest fixture n=20,m=73')

if __name__=='__main__':main()
