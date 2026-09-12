#!/usr/bin/env python3
"""Exhaustive small partial orientations, independently checking routing caps."""
from itertools import combinations,product
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent

def main():
    counts=[]
    for z in range(6):
        pairs=list(combinations(range(z),2));checks=0
        for choices in product(range(3),repeat=len(pairs)):
            arcs=[(u,v) if choice==1 else (v,u) for (u,v),choice in zip(pairs,choices) if choice]
            p=[sum(v==w for u,v in arcs) for w in range(z)]
            for mask in range(1<<z):
                J={u for u in range(z) if mask>>u&1};j=len(J)
                incoming=[sum(u in J and v==w for u,v in arcs) for w in range(z)]
                D=sum(incoming)
                assert all(y<=min(p[w],j-int(w in J)) for w,y in enumerate(incoming))
                assert D<=j*(z-j)+j*(j-1)//2
                checks+=1
        counts.append(dict(z=z,partial_orientations=3**len(pairs),orientation_subset_checks=checks))
    failures=[
        dict(invalid_claim='Every destination has y<=j-1',Z=[0,1,2],J=[0,1],arcs=[[0,2],[1,2]],destination=2,y=2,claimed_bound=1,
             explanation='Only destinations inside J lose their own source; outside J can receive j arcs.'),
        dict(invalid_claim='Count both orientations of an internal pair independently',Z=[0,1],J=[0,1],arcs=[[0,1],[1,0]],D=2,pair_capacity=1,
             explanation='This input violates the single-orientation hypothesis and cannot represent canonical selected pairs.')]
    report=dict(status='PASS',scope='All partial orientations on labelled Z with 0<=z<=5, and every subset J. These are combinatorial models, not D2C graph realizations.',counts=counts,
                total_orientation_subset_checks=sum(x['orientation_subset_checks'] for x in counts),invalid_extensions=failures)
    (HERE/'routing_verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
