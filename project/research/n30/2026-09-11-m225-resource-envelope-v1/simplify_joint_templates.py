#!/usr/bin/env python3
"""Find small integer shared templates; exact minima accept any proposed incumbent."""
from pathlib import Path
from collections import Counter
import argparse,json
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix
from mine_joint_potential import lcoeff,scoeff,label_states,source_states
from compress_joint_cover import gap

HERE=Path(__file__).resolve().parent

def simplify(shapes,rec):
    old=rec['weights'];active=[i for i,w in enumerate(old) if w]
    assert all(old[i]>0 for i in active)
    NW=len(active);pairs=[];ix={}
    for k,row in enumerate(rec['assigned']):
        for s in sorted(set(row['s'])):ix[k,'L',s]=NW+len(pairs);pairs.append((k,'L',s))
        for r in sorted(set(row['rho'])):ix[k,'S',r]=NW+len(pairs);pairs.append((k,'S',r))
    N=NW+len(pairs);rr=[];cc=[];vv=[];lower=[];upper=[]
    def add(d,lo,hi):
        i=len(lower);lower.append(lo);upper.append(hi)
        for j,v in d.items():
            if v:rr.append(i);cc.append(j);vv.append(v)
    for k,kind,v in pairs:
        row=rec['assigned'][k]
        coeffs=([lcoeff(v,R,x,shapes) for R,x in label_states(v,row['rho'])] if kind=='L'
                else [scoeff(v,q,p,shapes) for q,p in source_states(v,row['s'])])
        for coef in coeffs:
            d={j:-coef[i] for j,i in enumerate(active)};d[ix[k,kind,v]]=1
            add(d,-np.inf,0)
    for k,row in enumerate(rec['assigned']):
        d={ix[k,'L',s]:n for s,n in Counter(row['s']).items()}
        d.update({ix[k,'S',r]:n for r,n in Counter(row['rho']).items()})
        if 0 in active:d[active.index(0)]=-sum(row['rho'])
        add(d,1,np.inf)
    A=coo_matrix((vv,(rr,cc)),shape=(len(lower),N)).tocsc()
    sol=milp(np.r_[np.ones(NW),np.zeros(len(pairs))],integrality=np.r_[np.ones(NW),np.zeros(len(pairs))],bounds=Bounds([0]*NW+[-np.inf]*len(pairs),[10000]*NW+[np.inf]*len(pairs)),constraints=LinearConstraint(A,lower,upper),options={'time_limit':15,'mip_rel_gap':0.1})
    result={'status':int(sol.status),'constraint_count':len(lower),'integer_weight_variables':NW}
    if sol.x is not None:
        w=[0]*len(old)
        for j,i in enumerate(active):w[i]=int(round(sol.x[j]))
        g=[gap(row,tuple(shapes),tuple(w)) for row in rec['assigned']]
        if min(g)>0:
            result.update(weights=w,minimum_integer_gap=min(g),assigned=rec['assigned'],accepted=True)
    if not result.get('accepted'):
        result.update(weights=old,minimum_integer_gap=rec['minimum_integer_gap'],assigned=rec['assigned'],accepted=False)
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--kind',choices=['SMALL','RECTANGLES'],default='SMALL');args=ap.parse_args()
    data=json.loads((HERE/f'JOINT_{args.kind}_INTEGER_COVER.json').read_text());out=[]
    for i,rec in enumerate(data['templates']):
        ans=simplify(data['shapes'],rec);out.append(ans)
        print(args.kind,i+1,'rows',len(ans['assigned']),'sum weights',sum(ans['weights']),'accepted',ans['accepted'],'status',ans['status'],flush=True)
    (HERE/f'JOINT_{args.kind}_SIMPLIFIED.json').write_text(json.dumps({'schema':'n30-joint-shared-integer-templates-v1','shapes':data['shapes'],'templates':out},indent=2)+'\n')
