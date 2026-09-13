#!/usr/bin/env python3
"""Separate weighted pair-only obstructions from joint endpoint/pair obstructions."""
from pathlib import Path
from fractions import Fraction as F
import json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
from endpoint_control import frozen_patterns
from shared_pair_cover import options,exact_check,solve_integer_system
HERE=Path(__file__).resolve().parent

def run(rec,S):
    D,edges,opts=options(rec,S);b=rec['b'];n=len(opts)
    rows=[];cols=[];vals=[]
    for k,(u,R,covered) in enumerate(opts):
        for e in covered:rows.append(e);cols.append(k);vals.append(-1)
    for e in range(len(edges)):rows.append(e);cols.append(n);vals.append(-1)
    ub=coo_matrix((vals,(rows,cols)),shape=(len(edges),n+1)).tocsr();rhs=[-D[e] for e in edges]
    eq=coo_matrix(([1]*n,([u for u,R,c in opts],list(range(n)))),shape=(b,n+1)).tocsr()
    res=linprog([0]*n+[1],A_ub=ub,b_ub=rhs,A_eq=eq,b_eq=[1]*b,bounds=(0,None),method='highs',options={'time_limit':20})
    out={'layer':rec['layer'],'state_id':rec['state_id'],'solver_status':int(res.status),'message':res.message}
    assert res.success
    out['minimum_relaxation']=float(res.fun)
    if res.fun>1e-7:
        for scale in (100,1000,10000,1000000):
            w=[max(0,round(-v*scale)) for v in res.ineqlin.marginals]
            gap,lhs,rhs0,local=exact_check(rec,S,D,edges,opts,w,{},[0]*rec['a'],0)
            if gap>0:break
        assert gap>0
        out.update(exact_pattern_exclusion=True,exact_gap=str(gap),exact_lhs=str(lhs),exact_rhs=str(rhs0),certificate={'pair_weights':[[*e,str(w[k])] for k,e in enumerate(edges) if w[k]],'endpoint_weights':[],'residual_prices':['0']*rec['a'],'incoming_multiplier':'0','local_maxima':list(map(str,local))})
    else:
        support=[k for k,v in enumerate(res.x[:-1]) if v>1e-9]
        active=np.flatnonzero(np.abs(ub@res.x-np.array(rhs))<1e-7)
        matrix=eq[:,support].toarray().astype(int).tolist()+ub[active,:][:,support].toarray().astype(int).tolist()
        target=[1]*b+[rhs[k] for k in active]
        sol=solve_integer_system(matrix,target)
        z=[(opts[k][0],opts[k][1],v) for k,v in zip(support,sol) if v]
        assert all(v>=0 for u,R,v in z)
        assert all(sum((v for u0,R,v in z if u0==u),F(0))==1 for u in range(b))
        for (i,j),need in D.items():
            assert sum((v for u,R,v in z if i in S[u]|set(R) and j in S[u]|set(R) and not(i in S[u] and j in S[u])),F(0))>=need
        out['exact_pair_only_fractional_witness']=[[u,list(R),str(v)] for u,R,v in z]
    return out

def main():
    pair=json.loads((HERE/'SHARED_PAIR.json').read_text());ids={(x['layer'],x['state_id']) for x in pair['records'] if x.get('shared_pair',{}).get('exact_pattern_exclusion')}
    records=[run(rec,S) for rec,S,_ in frozen_patterns() if (rec['layer'],rec['state_id']) in ids]
    summary={'tested':len(records),'weighted_pair_only_exclusions':sum(x.get('exact_pattern_exclusion',False) for x in records),'require_joint_constraints_vs_separately_feasible_controls':sum('exact_pair_only_fractional_witness' in x for x in records),'whole_state_exclusions':0}
    (HERE/'PAIR_ONLY_CONTROL.json').write_text(json.dumps({'schema':'pair-only-attribution-control-v1','scope':'All 25 joint pair-stage rejections, on fixed selected patterns. Exact positive pair-only and endpoint-control mixtures establish separate relaxation feasibility only.','summary':summary,'records':records},separators=(',',':'))+'\n');print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
