#!/usr/bin/env python3
"""Zero-gap big-M minimum-support MILP for all BC rectangles + J_b on n29 t2 hard38.

This is computational support evidence only. Positive support existence must be
exactified independently; matching optima at multiple M values strengthen but do
not convert the lower-bound side into an exact mathematical certificate.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix,vstack,csr_matrix
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('rd',HERE/'n29_t2_rectdiag_sparse_scan.py');rd=module_from_spec(sp);sp.loader.exec_module(rd)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--M',type=float,required=True);ap.add_argument('--time-limit',type=float,default=1200);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    B=json.loads(z.boundary_json.read_text());P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['trimmed_survivor_records']]
    M,rect,diag=rd.build(P,12,16,10,True);ngen=len(rect)+1;gen=[w for D,V,w in rect]+[diag]
    n0=len(M.names);n=n0+ngen
    A=lil_matrix((len(M.rows)+ngen,n));ub=np.empty(len(M.rows)+ngen)
    for i,(row,rhs) in enumerate(zip(M.rows,M.rhs)):
        for j,v in row.items():A[i,j]=v
        ub[i]=rhs
    for k,w in enumerate(gen):
        i=len(M.rows)+k;A[i,w]=1;A[i,n0+k]=-z.M;ub[i]=0
    lb=np.full(n,-np.inf);hi=np.full(n,np.inf)
    for j,(lo,up) in enumerate(M.bounds):
        if lo is not None:lb[j]=lo
        if up is not None:hi[j]=up
    for w in gen:lb[w]=0;hi[w]=z.M
    lb[n0:]=0;hi[n0:]=1
    c=np.zeros(n);c[n0:]=1
    integ=np.zeros(n,dtype=int);integ[n0:]=1
    st=time.time();res=milp(c,integrality=integ,bounds=Bounds(lb,hi),constraints=LinearConstraint(A.tocsr(),np.full(len(ub),-np.inf),ub),options={'time_limit':z.time_limit,'mip_rel_gap':0.0,'presolve':True});sec=time.time()-st
    out={'schema':'n29-t2-rectdiag-min-support-v1','profiles':len(P),'M':z.M,'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.fun is not None else None,'mip_gap':float(getattr(res,'mip_gap',np.nan)) if getattr(res,'mip_gap',None) is not None else None,'mip_node_count':int(getattr(res,'mip_node_count',-1)) if getattr(res,'mip_node_count',None) is not None else None,'seconds':sec,'generator_count':ngen,'rectangle_count':len(rect),'floating_point_MILP_support_evidence_only':True}
    if res.x is not None:
        selected=[]
        for k,(D,V,w) in enumerate(rect):
            if res.x[n0+k]>0.5:selected.append({'type':'BCrect','D':D,'V':V,'weight':float(res.x[w]),'z':float(res.x[n0+k])})
        k=len(rect)
        if res.x[n0+k]>0.5:selected.append({'type':'Jb','K':16,'weight':float(res.x[diag]),'z':float(res.x[n0+k])})
        out['selected']=selected;out['selected_count']=len(selected);out['positive_weight_count']=sum(1 for q in selected if q['weight']>1e-9)
    out['interpretation']='Zero-gap big-M MILP over every finite BC rectangle plus the single diagonal J_b. Matching optima across M values are computational support-minimality evidence only; exact positive existence requires integer/rational verification.'
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
    if res.status not in (0,1):raise SystemExit(1)
if __name__=='__main__':main()
