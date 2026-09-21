#!/usr/bin/env python3
from itertools import product
from pathlib import Path
import json
from check_star_support import graph,d2c

def build(r,q):
    codes=['C00','C01','C10','C11','C20','S0','S3','S5','S6']+['P0']*r+['P1']*q
    ae=[(5,6),(7,8)]+[(i,9) for i in range(4)]+[(9+i,9+r+j) for i in range(r) for j in range(q)]
    return graph(codes,ae),codes,ae

def witnesses(adj):
    result=[]
    n=len(adj)
    # Record and independently validate an explicit newly-long pair after
    # every deletion, instead of relying only on the d2c boolean checker.
    for u in range(n):
        for v in sorted(adj[u]):
            if u>=v:continue
            adj[u].remove(v);adj[v].remove(u)
            bad=None
            for x in range(n):
                reached={x}|adj[x]
                for z in adj[x]:reached|=adj[z]
                for y in range(x+1,n):
                    if y not in reached:bad=[x,y];break
                if bad:break
            adj[u].add(v);adj[v].add(u)
            assert bad is not None,(u,v)
            result.append({'deleted_edge':[u,v],'newly_long_pair':bad})
    return result

def main():
    checks=[]
    for r,q in product(range(1,6),range(6)):
        adj,codes,ae=build(r,q);n=len(adj);m=sum(map(len,adj))//2;a=n-9
        assert d2c(adj),(r,q)
        assert m==26+4*a+r*q
        gap=((n-1)**2//4+1)-m
        assert gap==(9*n-139)//2+((r+q)**2//4-r*q)
        checks.append({'r':r,'q':q,'n':n,'m':m,'gap':gap,'d2c':True})
    adj,codes,ae=build(1,0)
    cert=witnesses(adj)
    assert len(cert)==66
    # An extra edge joining the two matched star pairs creates a competing
    # bridge and must not be silently accepted.
    bad=graph(codes,ae+[(5,7)])
    assert not d2c(bad)
    result={'checks':checks,'minimum_fixture':{'n':19,'m':66,'codes':codes,'A_edges':ae,'adjacency':[sorted(x) for x in adj], 'edge_deletion_witnesses':cert},'extra_star_edge_negative_control_rejected':True}
    Path(__file__).with_name('FIVE_COORDINATE_FAMILY_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: 30 actual D2C controls, exact floor identity, all 66 deletion certificates at n=19, extra-star-edge negative control')

if __name__=='__main__':main()
