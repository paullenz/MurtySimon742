#!/usr/bin/env python3
"""Floating template-cover reconnaissance for the fixed n=29,t=3 potential.

Fix
    F = 6 B(3,0) + 4 B(3,5) + 3 B(3,9).

The 94 profile-specific scalar solutions from one decoupled LP are treated as
candidate scalar templates.  Each candidate is cross-tested against every
profile by direct finite envelope minimisation, then a binary set-cover MILP
finds a smallest cover among these inherited rays.  This is DISCOVERY ONLY;
selected templates must be rationalised and checked exactly before proof use.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
from collections import Counter
import argparse,json,time
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix

HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('rd',HERE/'n29_t2_layer23_diag012_scan.py');rd=module_from_spec(sp);sp.loader.exec_module(rd)
WEIGHTS={(3,0):6,(3,5):4,(3,9):3}

def F(d,v):
    return sum(w for (D,V),w in WEIGHTS.items() if d>=D and v>=V)
def tterm(r,q,p,j):
    return (q if q>=j+1 else 0)-(p if r+q>=j else 0)
def theta_from(res,M,pi):
    th={
      'lambda':float(res.x[M.idx[('lambda',pi)]]),
      'c':float(res.x[M.idx[('c',pi)]]),
      'mu+':float(res.x[M.idx[('mu+',pi)]]),
      'mu-':float(res.x[M.idx[('mu-',pi)]])}
    for j in range(1,13): th[f'tau{j}']=float(res.x[M.idx[('tau',pi,j)]])
    return th
def gap(pf,th):
    lam=th['lambda'];c=th['c'];mp=th['mu+'];mm=th['mu-'];taus={j:th[f'tau{j}'] for j in range(1,13)}
    ell={s:min(lam*R+c*x+x*F(R+s,16-R-x) for R in range(10-s+1) for x in range(s,16-R+1)) for s in set(pf['s'])}
    sig={}
    for r in set(pf['rho']):
        qm=min(12-r,sum(si<=r for si in pf['s']))
        sig[r]=min(mp*(q-p)-mm*(q-p)-c*q+sum(taus[j]*tterm(r,q,p,j) for j in range(1,13))-q*F(r+q-1,16-q-p)
                   for q in range(qm+1) for p in range(min(r+3,15-q)+1))
    return sum(n*ell[s] for s,n in Counter(pf['s']).items())+sum(n*sig[r] for r,n in Counter(pf['rho']).items())-lam*sum(pf['rho'])

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    raw=rd.allx.load29(z.demands_json,z.rows,3);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
    if len(P)!=94: raise SystemExit(f'expected 94 profiles, got {len(P)}')
    M,rect,diag=rd.build(P,12,16,10,(3,),())
    for D,V,w in rect: M.bounds[w]=(WEIGHTS.get((D,V),0),WEIGHTS.get((D,V),0))
    st=time.time();res=M.solve()
    if not res.success: raise SystemExit('fixed 643 decoupled LP unexpectedly infeasible')
    candidates=[theta_from(res,M,i) for i in range(94)]
    gaps=np.zeros((94,94),dtype=float); cover=np.zeros((94,94),dtype=np.int8)
    for k,th in enumerate(candidates):
        for i,pf in enumerate(P):
            g=gap(pf,th);gaps[k,i]=g
            if g>1e-7: cover[k,i]=1
    own=[float(gaps[i,i]) for i in range(94)]
    uncovered=[i for i in range(94) if not cover[:,i].any()]
    selected=[];setcover_status=None;setcover_gap=None
    if not uncovered:
        A=lil_matrix((94,94),dtype=float)
        for i in range(94):
            for k in np.nonzero(cover[:,i])[0]: A[i,k]=-1.0
        rr=milp(np.ones(94),integrality=np.ones(94,dtype=np.uint8),bounds=Bounds(np.zeros(94),np.ones(94)),constraints=LinearConstraint(A.tocsr(),-np.inf,-np.ones(94)),options={'mip_rel_gap':0.0,'time_limit':300})
        setcover_status=int(rr.status);setcover_gap=float(getattr(rr,'mip_gap',float('nan'))) if getattr(rr,'mip_gap',None) is not None else None
        if rr.x is not None: selected=[i for i,x in enumerate(rr.x) if x>0.5]
    selcov={str(k):[i for i in range(94) if cover[k,i]] for k in selected}
    out={'schema':'n29-t3-fixed643-template-cover-scan-v1','status':'PASS_SCAN','profiles':94,'global_potential':'6 B(3,0)+4 B(3,5)+3 B(3,9)','floating_point_reconnaissance_only':True,
         'candidate_count':94,'uncovered_by_inherited_rays':uncovered,'own_gap_min':min(own),'own_gap_max':max(own),
         'coverage_counts':[int(cover[k].sum()) for k in range(94)],'selected_candidate_indices':selected,'selected_count':len(selected),
         'selected_coverage':selcov,'selected_theta':{str(k):candidates[k] for k in selected},'setcover_status':setcover_status,'setcover_mip_gap':setcover_gap,
         'seconds':time.time()-st,'interpretation':'Inherited floating scalar rays only. Any selected small cover must be rationalised and exact-Fraction checked before proof use.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
