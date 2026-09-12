#!/usr/bin/env python3
"""Challenge sparse row encoding against direct combinatorial conditions."""
from itertools import product
from pathlib import Path
import json
from model import build
from check_witness import verify_objects,verify_vector
HERE=Path(__file__).resolve().parent

def vector_for(model,selected,residual,arcs):
    rec=model['record'];s=rec['s'];values=[]
    for n in model['variables']:
        kind=n[0]
        if kind in ('x','r','z'):value=int(tuple(n[1:]) in {'x':selected,'r':residual,'z':set(arcs)}[kind])
        elif kind=='y':value=sum(u==n[1] and v==n[2] for u,i,v in arcs)
        elif kind=='q':value=sum(u==n[1] for u,i in selected)
        elif kind=='p':value=sum(v==n[1] for u,i,v in arcs)
        else:value=int(sum(s[i]>=n[2] for u,i in selected if u==n[1])>n[2])
        values.append(value)
    return values

def rows_accept(model,vector):
    if not all(lo<=v<=hi for v,lo,hi in zip(vector,model['lower_bounds'],model['upper_bounds'])):return False
    for row in model['rows']:
        value=sum(vector[j]*c for j,c in row['terms'])
        if row['lower'] is not None and value<row['lower']:return False
        if row['upper'] is not None and value>row['upper']:return False
    return True

def main():
    checks=0;accepted={mode:0 for mode in ['degree_routing','label_compatible']};cache={}
    positions=list(product(range(3),range(2)))
    for pattern in product(range(3),repeat=6):
        selected={p for p,k in zip(positions,pattern) if k==1};residual={p for p,k in zip(positions,pattern) if k==2}
        rho=tuple(sum(u==v for u,i in residual) for v in range(3));rec=dict(a=2,b=3,t=0,s=[0,0],rho=list(rho))
        for mode in accepted:
            if (rho,mode) not in cache:cache[rho,mode]=build(rec,mode)
            model=cache[rho,mode]
            for targets in product(*[[v for v in range(3) if v!=u] for u,i in sorted(selected)]):
                arcs=[(u,i,v) for (u,i),v in zip(sorted(selected),targets)]
                try:verify_objects(rec,mode,selected,residual,arcs);expected=True
                except AssertionError:expected=False
                actual=rows_accept(model,vector_for(model,selected,residual,arcs));assert actual==expected,(pattern,mode,arcs)
                checks+=1;accepted[mode]+=actual
    # Nonvacuous heavy threshold and positive demands, with valid B-side domination.
    rec=dict(a=5,b=7,t=0,s=[2,2,2,0,0],rho=[2]*7)
    selected={(u,i) for u in [0,4] for i in range(3)}
    residual={(u,i) for u in [0,4,5,6] for i in [3,4]}|{(1,1),(1,2),(2,0),(2,2),(3,0),(3,1)}
    arcs={(u,i,i+1) for u in [0,4] for i in range(3)}
    control={}
    for mode in accepted:
        model=build(rec,mode);v=vector_for(model,selected,residual,arcs)
        control[mode]=verify_vector(model,v)
    bad_residual=(residual-{(1,1)})|{(1,0)}
    weak=build(rec,'degree_routing');strong=build(rec,'label_compatible')
    verify_vector(weak,vector_for(weak,selected,bad_residual,arcs))
    assert not rows_accept(strong,vector_for(strong,selected,bad_residual,arcs))
    example=dict(record=rec,selected=sorted(selected),residual=sorted(bad_residual),arcs=sorted(arcs),
        degree_routing='PASS',label_compatible='FAIL: incoming label 0 is present at destination 1',
        scope='One assignment; a different routing/cross pattern is not excluded.')
    (HERE/'shortcut_counterexample.json').write_text(json.dumps(example,indent=2)+'\n')
    report=dict(status='PASS',tiny_linear_vs_combinatorial_checks=checks,tiny_accepted_assignments=accepted,
        positive_demand_heavy_controls=control,invalid_coarse_sufficiency_example='shortcut_counterexample.json',
        no_positive_surplus_graph_claim=True)
    (HERE/'model_verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
