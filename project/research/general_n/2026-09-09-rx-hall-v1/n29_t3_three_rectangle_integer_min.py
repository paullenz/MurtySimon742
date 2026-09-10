#!/usr/bin/env python3
"""MILP reconnaissance: smallest nonnegative integer weights on the exact
n=29,t=3 three-rectangle support B(3,0), B(3,5), B(3,9).

All profile-specific scalar/envelope variables remain continuous.  This is a
coefficient-discovery step only; any resulting integer potential must still be
fed through an exact arithmetic checker before proof use.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix

HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('rd',HERE/'n29_t2_layer23_diag012_scan.py');rd=module_from_spec(sp);sp.loader.exec_module(rd)
RECT={(3,0),(3,5),(3,9)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    raw=rd.allx.load29(z.demands_json,z.rows,3)
    P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
    if len(P)!=94: raise SystemExit(f'expected 94 profiles, got {len(P)}')
    M,rect,diag=rd.build(P,12,16,10,(3,),())
    active=[]
    for D,V,w in rect:
        if (D,V) in RECT: active.append((D,V,w))
        else: M.bounds[w]=(0,0)
    n=len(M.names); A=lil_matrix((len(M.rows),n),dtype=float)
    for i,row in enumerate(M.rows):
        for j,v in row.items(): A[i,j]=v
    lb=np.full(n,-np.inf);ub=np.full(n,np.inf)
    for j,(lo,hi) in enumerate(M.bounds):
        if lo is not None: lb[j]=lo
        if hi is not None: ub[j]=hi
    c=np.zeros(n); integrality=np.zeros(n,dtype=np.uint8)
    for D,V,w in active: c[w]=1.0;integrality[w]=1
    st=time.time();res=milp(c,integrality=integrality,bounds=Bounds(lb,ub),constraints=LinearConstraint(A.tocsr(),-np.inf,np.asarray(M.rhs,dtype=float)),options={'time_limit':600,'mip_rel_gap':0.0})
    out={'schema':'n29-t3-three-rectangle-integer-min-v1','profiles':len(P),'rows':len(M.rows),'variables':n,'support':[list(x) for x in sorted(RECT)],'success':bool(res.success),'status':int(res.status),'message':res.message,'seconds':time.time()-st,'floating_milp_reconnaissance_only':True,'objective':float(res.fun) if res.fun is not None else None,'mip_gap':float(getattr(res,'mip_gap',float('nan'))) if getattr(res,'mip_gap',None) is not None else None,'mip_node_count':int(getattr(res,'mip_node_count',-1)) if getattr(res,'mip_node_count',None) is not None else None}
    if res.x is not None:
        out['integer_weights']={f'B({D},{V})':int(round(res.x[w])) for D,V,w in active}
        out['integer_weight_sum']=sum(out['integer_weights'].values())
        out['raw_weight_values']={f'B({D},{V})':float(res.x[w]) for D,V,w in active}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
    if not res.success: raise SystemExit(1)
if __name__=='__main__':main()
