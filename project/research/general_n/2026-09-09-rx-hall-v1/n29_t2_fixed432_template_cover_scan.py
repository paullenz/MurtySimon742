#!/usr/bin/env python3
"""Floating scalar-template cover scan for the simple n=29,t=2 potential.

Fix
    F = 4 B(2,0) + 3 B(2,3) + 2 B(2,6).

A decoupled LP gives one scalar ray per one of the 902 frontier profiles.  We
cross-test those rays on all profiles by direct finite envelope minimisation,
then solve a binary set-cover problem over the 902 inherited rays.

This is discovery/reconnaissance only.  A selected cover must be rationalised
and checked with exact Fraction arithmetic before proof use.
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
W={(2,0):4,(2,3):3,(2,6):2}

def F(d,v): return sum(w for (D,V),w in W.items() if d>=D and v>=V)
def tterm(r,q,p,j): return (q if q>=j+1 else 0)-(p if r+q>=j else 0)
def theta_from(res,M,pi):
    th={'lambda':float(res.x[M.idx[('lambda',pi)]]),'c':float(res.x[M.idx[('c',pi)]]),'mu+':float(res.x[M.idx[('mu+',pi)]]),'mu-':float(res.x[M.idx[('mu-',pi)]])}
    for j in range(1,13): th[f'tau{j}']=float(res.x[M.idx[('tau',pi,j)]])
    return th

def profile_keys(P):
    keys=set()
    for pf in P:
        for r in set(pf['rho']): keys.add((r,min(12-r,sum(si<=r for si in pf['s']))))
    return sorted(keys)

def all_gaps(P,keys,th):
    lam=th['lambda'];c=th['c'];mp=th['mu+'];mm=th['mu-'];taus={j:th[f'tau{j}'] for j in range(1,13)}
    ell={s:min(lam*R+c*x+x*F(R+s,16-R-x) for R in range(10-s+1) for x in range(s,16-R+1)) for s in range(1,11)}
    sig={}
    for r,qm in keys:
        sig[(r,qm)]=min(mp*(q-p)-mm*(q-p)-c*q+sum(taus[j]*tterm(r,q,p,j) for j in range(1,13))-q*F(r+q-1,16-q-p)
                           for q in range(qm+1) for p in range(min(r+3,15-q)+1))
    out=[]
    for pf in P:
        g=sum(n*ell[s] for s,n in Counter(pf['s']).items())
        for r,n in Counter(pf['rho']).items():
            qm=min(12-r,sum(si<=r for si in pf['s']));g+=n*sig[(r,qm)]
        g-=lam*sum(pf['rho']);out.append(g)
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    raw=rd.allx.load29(z.demands_json,z.rows,2);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
    if len(P)!=902: raise SystemExit(f'expected 902 profiles, got {len(P)}')
    M,rect,diag=rd.build(P,12,16,10,(2,),())
    for D,V,w in rect:
        val=W.get((D,V),0);M.bounds[w]=(val,val)
    st=time.time();res=M.solve()
    if not res.success: raise SystemExit('fixed 432 decoupled LP unexpectedly infeasible')
    candidates=[theta_from(res,M,i) for i in range(902)];keys=profile_keys(P)
    cover=np.zeros((902,902),dtype=np.int8);own=[];counts=[]
    for k,th in enumerate(candidates):
        gs=all_gaps(P,keys,th);own.append(gs[k]);mask=np.array([g>1e-7 for g in gs],dtype=np.int8);cover[k,:]=mask;counts.append(int(mask.sum()))
    uncovered=[i for i in range(902) if not cover[:,i].any()]
    selected=[];sc_status=None;sc_gap=None;sc_fun=None
    if not uncovered:
        A=lil_matrix((902,902),dtype=float)
        for i in range(902):
            for k in np.nonzero(cover[:,i])[0]: A[i,k]=-1.0
        rr=milp(np.ones(902),integrality=np.ones(902,dtype=np.uint8),bounds=Bounds(np.zeros(902),np.ones(902)),constraints=LinearConstraint(A.tocsr(),-np.inf,-np.ones(902)),options={'mip_rel_gap':0.0,'time_limit':300})
        sc_status=int(rr.status);sc_gap=float(getattr(rr,'mip_gap',float('nan'))) if getattr(rr,'mip_gap',None) is not None else None;sc_fun=float(rr.fun) if rr.fun is not None else None
        if rr.x is not None:selected=[i for i,x in enumerate(rr.x) if x>0.5]
    out={'schema':'n29-t2-fixed432-template-cover-scan-v1','status':'PASS_SCAN','profiles':902,'global_potential':'4 B(2,0)+3 B(2,3)+2 B(2,6)','floating_point_reconnaissance_only':True,
         'candidate_count':902,'source_key_count':len(keys),'uncovered_by_inherited_rays':uncovered,'own_gap_min':min(own),'own_gap_max':max(own),'coverage_count_min':min(counts),'coverage_count_max':max(counts),
         'selected_candidate_indices':selected,'selected_count':len(selected),'selected_coverage_counts':{str(k):counts[k] for k in selected},'selected_theta':{str(k):candidates[k] for k in selected},
         'setcover_status':sc_status,'setcover_mip_gap':sc_gap,'setcover_objective':sc_fun,'seconds':time.time()-st,
         'interpretation':'Inherited floating scalar rays only. A zero-gap set-cover optimum is minimal only within this candidate-ray dictionary. Selected rays require rationalisation and exact checking.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
