#!/usr/bin/env python3
"""Reproduce structural gain, failure and unsafe-relaxation counterexamples."""
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
from copy import deepcopy
import sys
import verify_residual as v
from test_residual import instance,run_case,record,write


def main(out):
    counts=Counter(); records={}
    cases=[
      ('scc_gain',3,[[0,1,2]],[Q(1,2),0,1],[Q(1,2),Q(1,2),0],[(0,1),(0,2),(1,2)]),
      ('block_incomplete',3,[[0,1,2]],[1,0,1],[1,0,0],[(0,1),(0,2),(1,2)]),
      ('dropping_low_guard_is_unsound',3,[[0,1],[2]],[1,2,1],[0,2,0],[(0,2),(1,0),(1,2),(2,0)]),
      ('neutrality_alone_is_unsound',1,[[0]],[0],[0],[]),
      ('two_scc_choices',6,[[0,1,2],[3,4,5]],[Q(1,2),0,1]*2,[Q(1,2),Q(1,2),0]*2,
       [(3*i+a,3*i+b) for i in range(2) for a,b in [(0,1),(0,2),(1,2)]])]
    for name,n,bs,p,d,arcs in cases:
        c=instance(n,bs,p,d,arcs);o,r=run_case(c,counts,n<=3)
        records[name]=record(c,o,r)
        if name=='scc_gain':
            assert o['components']=={3,4} and o['minima']=={0,3,4,7}
            assert r['block']['accepted'] and not r['path']['accepted']
        if name=='block_incomplete':
            assert o['greatest']==4 and all(z['terminal']==7 for z in r.values())
            # A proposed forced-count guard gives two hand-oracle steps; this
            # is NOT acceptance by the current P/B verifier.
            trace=[];m=7
            for a,b,x,y in [(1,0,1,0),(0,0,1,0)]:
                forced=[i for i in range(n) if i in o['paths'][a]]
                lower=sum((i,x) in o['arcs'] for i in forced)
                assert lower*o['scale']>o['p'][x]
                assert (m^(1<<a)) in o['minima']
                assert all(t not in o['tight'] for t in o['minima'] if t&~m==0 and t>>a&1)
                trace.append(dict(before=m,remove=a,forced=forced,low_lower_bound=lower,
                                  x=x,y=y,path=o['paths'][a][b]))
                m^=1<<a
            assert m==o['greatest']
            records[name]['proposed_guard_hand_oracle_trace']=trace
        if name=='dropping_low_guard_is_unsound':
            assert c['flow']==[[1,0,1],[1,2,1]] and o['greatest']==3
            # All other P conditions hold at S=V for delete a=0, b=1,x=0,y=1.
            assert (0,0) not in o['arcs'] and 1 in o['paths'][0]
            assert 6 in o['minima'] and 3 in o['tight'] and 3&1
            yy=o['rows'][7]['counts'];sc=o['scale']
            assert max(o['p'][0],yy[1]*sc)<min(o['p'][1],yy[0]*sc)
            assert (1,0) in o['arcs'] and (1,1) not in o['arcs']
            assert all((z,1) not in o['arcs'] or (z,0) in o['arcs'] for z in range(n))
            step=dict(remove=[0],anchor=0,strict=1,x=0,y=1,path=o['paths'][0][1])
            inst=v.parse_instance(c);s,g,val,adj=v.flow_start(c,inst)
            try:v.deletion_step(inst,s,g,adj,v.source_components(adj,n),step,'path')
            except v.Invalid as e:
                assert str(e)=='removed block misses low receiver'
                records[name]['rejected_unsafe_step']={'step':step,'reason':str(e)}
            else:raise AssertionError('low-guard corruption accepted')
    corrupt=[]
    cert=records['scc_gain']['results']['block']['certificate']
    for remove in ([0],[1],[0,1,2]):
        c=deepcopy(cert);c['deletions'][0]['remove']=remove;c['deletions'][0]['anchor']=remove[0]
        c['deletions'][0]['path']=[remove[0]];c['deletions'][0]['strict']=remove[0]
        try:v.verify(c)
        except v.Invalid as e:corrupt.append(dict(remove=remove,rejected=True,reason=str(e),certificate=c))
        else:raise AssertionError('partial/invented SCC accepted')
    # Two independent two-source blocks have four states and four block moves.
    c=records['two_scc_choices']['instance'];local=Counter();o,r=run_case(c,local)
    assert local['block_states']==4 and local['block_witness_transitions']==4
    write(out/'DIAGNOSIS_RESULTS.json',dict(counts=dict(counts),cases=records,
                                          component_corruptions=corrupt,
                                          two_scc_choice_counts=dict(local)))
    print('diagnosed 5 examples; rejected 3 component corruptions and 1 unsafe low-guard deletion')


if __name__=='__main__':
    out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True);main(out)
