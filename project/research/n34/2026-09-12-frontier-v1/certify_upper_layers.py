#!/usr/bin/env python3
"""Discover exact scalar envelopes for the unchanged nine-rectangle potential.

Only t=3,4 are attempted. SciPy proposes coefficients; integer checks decide.
Full repaired coefficients are preserved for the solver-free verifier.
"""
import importlib.util
import json
from pathlib import Path
from check_frontier import expand

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
SOURCE=ROOT/'project/research/n33/2026-09-12-candidate-v1/n33_t2_shifted_potential_exact.py'
spec=importlib.util.spec_from_file_location('n33_envelope',SOURCE)
e=importlib.util.module_from_spec(spec)
spec.loader.exec_module(e)
e.A,e.B,e.DMAX=15,18,13


def integer_certificate(model):
    names,bounds,rows,rhs,kinds,res=model
    if not res.success:
        return None
    for den in (10000,100000,1000000,10000000):
        X=[round(float(v)*den) for v in res.x]
        for j,(lo,hi) in enumerate(bounds):
            if lo==0:
                X[j]=max(0,X[j])
        repair={}
        for co,b,kind in zip(rows,rhs,kinds):
            if kind[0]=='gap':
                continue
            violation=sum(int(a)*X[j] for j,a in co.items())-int(b)*den
            if violation>0:
                repair[kind[1]]=max(repair.get(kind[1],0),violation)
        for j,delta in repair.items():
            X[j]-=delta
        if any((lo is not None and X[j]<lo*den) or (hi is not None and X[j]>hi*den)
               for j,(lo,hi) in enumerate(bounds)):
            continue
        ok=True
        gap=None
        for co,b,kind in zip(rows,rhs,kinds):
            value=sum(int(a)*X[j] for j,a in co.items())
            if kind[0]=='gap':
                gap=value
            elif value>int(b)*den:
                ok=False
        if ok and gap is not None and gap<0:
            return dict(denominator=den,names=names,numerators=X,gap=gap)
    return None


def main():
    result=dict(schema='n34-upper-layers-integer-envelopes-v1',a=15,b=18,dmax=13,
                potential=[[D,V,w] for (D,V),w in e.PAT.items()],layers={})
    for t in (4,3):
        states,stats=expand(t)
        accepted=[];unresolved=[]
        for idx,(s,rho) in enumerate(states):
            assert min(s)>0
            model=e.build_envelope(s,rho)
            cert=integer_certificate(model)
            if cert is None:
                unresolved.append(dict(s=s,rho=rho,solver_status=int(model[-1].status)))
            else:
                accepted.append(dict(s=s,rho=rho,**cert))
            if idx%20==0:
                print('t',t,'processed',idx+1,'accepted',len(accepted),'unresolved',len(unresolved),flush=True)
        result['layers'][str(t)]=dict(frontier=stats,certificates=accepted,unresolved=unresolved)
        (HERE/'upper_layer_certificates.json').write_text(json.dumps(result,indent=2)+'\n')
        print('DONE',t,'accepted',len(accepted),'unresolved',len(unresolved),flush=True)


if __name__=='__main__':
    main()
