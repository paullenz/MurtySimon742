#!/usr/bin/env python3
"""Reproduce the obstruction to a single uniform crossing pair."""
from collections import Counter
from pathlib import Path
import sys
import test_closure as t


def main(out):
    c=t.make(3,[[0,1,2]],[2,1,0],[1,0,1],[(0,1),(0,2),(1,2),(2,0)])
    counts=Counter();o,r=t.run_case(c,counts,True)
    assert o['minima']==set(range(8)) and o['tight']=={0,4,5} and o['greatest']==5
    assert r['closure']['terminal']==7 and not r['closure']['accepted']
    pairs=[(x,y) for x in range(3) for y in range(3) if o['p'][x]<o['p'][y]]
    def crossing(m,x,y):
        yy=o['rows'][m]['counts'];sc=o['scale']
        return max(o['p'][x],yy[y]*sc)<min(o['p'][y],yy[x]*sc)
    rows=[]
    for m in range(8):
        rows.append(dict(mask=m,crossings=[list(pair) for pair in pairs if crossing(m,*pair)],**{k:z for k,z in o['rows'][m].items() if k!='mask'}))
    domains={False:[2,6],True:[3,7]};branch=[]
    for present,ms in domains.items():
        pair=(2,0) if present else (2,1)
        assert all(crossing(m,*pair) for m in ms)
        branch.append(dict(source0_present=present,exact_minima=ms,uniform_pair=list(pair)))
    fixed=[]
    for pair in pairs:
        witnesses=[m for m in [2,3,6,7] if not crossing(m,*pair)]
        assert witnesses
        fixed.append(dict(pair=list(pair),counterexamples=witnesses))
    # Deleting the bad source 1 yields greatest tight {0,2}, but neither branch
    # is permission to delete the branching source 0 from the actual state.
    assert 7&~(1<<1)==5 and 5 in o['tight']
    data=dict(instance=c,all_subsets=rows,minimum_cuts=o['cuts'],counts=dict(counts),
              exact_minima=sorted(o['minima']),tight_minima=sorted(o['tight']),greatest_tight=5,
              old_and_new_results=r,bad_anchor=1,branch_on=0,branches=branch,
              every_fixed_pair_fails=fixed,
              status='two-case hand/oracle exclusion proof; branching verifier NOT implemented')
    t.old.write(out/'BRANCHING_OBSTRUCTION.json',data)
    print('all 8 subsets and 64 cuts checked; both branches exclude source 1; every fixed pair fails')


if __name__=='__main__':
    out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True);main(out)
