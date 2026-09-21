#!/usr/bin/env python3
"""Bounded seeded diagnostic; absence of a fixture is never nonexistence."""
from pathlib import Path
from itertools import combinations
import json,random,time
from check_star_support import relation,graph,d2c

def bits(adj):return [sum(1<<j for j in ns) for ns in adj]
def diameter(a):
    mask=(1<<len(a))-1
    for x,ns in enumerate(a):
        reach=ns|(1<<x);left=ns
        while left:
            bit=left&-left;left-=bit;reach|=a[bit.bit_length()-1]
        if reach!=mask:return False
    return True
def critical(a,x,y):
    a[x]^=1<<y;a[y]^=1<<x
    out=not diameter(a)
    a[x]^=1<<y;a[y]^=1<<x
    return out

def main():
    rng=random.Random(2026092147);d=relation((0,1,2,3));R=set(d['allowed_pairs']);R|={(b,a) for a,b in R}
    rows=[];best=None;found=[];start=time.monotonic()
    for copies in (1,2,3,4):
        codes=['C00','C01','C10','C11','P0','P1']+['C21']*copies+['S0','S1','S2','S3']
        potential=[(i,j) for i,j in combinations(range(len(codes)),2) if (codes[i],codes[j]) in R]
        base=bits(graph(codes,potential));assert diameter(base)
        record={'outward_copies':copies,'trials':0,'best_noncritical_fixed_edges':9999}
        for trial in range(300):
            a=base.copy();edges=potential.copy();rng.shuffle(edges)
            for i,j in edges:
                x,y=i+9,j+9
                if not critical(a,x,y):a[x]^=1<<y;a[y]^=1<<x
            fixed=[(x,y) for x in range(len(a)) for y in range(x+1,len(a)) if x<9 and a[x]>>y&1]
            bad=[(x,y) for x,y in fixed if not critical(a,x,y)]
            record['trials']+=1
            if len(bad)<record['best_noncritical_fixed_edges']:
                record['best_noncritical_fixed_edges']=len(bad);record['best_bad_edges']=bad
                record['best_A_edges']=[(i,j) for i,j in potential if a[i+9]>>(j+9)&1]
            if not bad:
                ae=record['best_A_edges'];assert d2c(graph(codes,ae));found.append({'codes':codes,'A_edges':ae});break
        rows.append(record);print(record['outward_copies'],record['trials'],record['best_noncritical_fixed_edges'],flush=True)
    result={'seed':2026092147,'method':'random greedy A-edge deletion from all necessary-type-permitted edges, preserving diameter two','trials':rows,'actual_D2C_fixtures':found,'elapsed_seconds':time.monotonic()-start,'scope':'bounded diagnostic on fixed multiplicities; no nonexistence conclusion from search failure'}
    Path(__file__).with_name('COORDINATE_FACE_SEARCH_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()
