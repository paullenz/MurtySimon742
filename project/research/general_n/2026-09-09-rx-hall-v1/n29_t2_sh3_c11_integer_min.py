#!/usr/bin/env python3
"""MILP discovery: minimize integer global weights on the clean full-902 t=2
3-D support C = D3 + J0 + J2 + SH3.

Support fixed from workflow 34501809375:
  D3 rectangles V=6,...,13; diagonals K=14,16; SH threshold S=3.
All profile-local scalar/envelope variables remain continuous.  This is
coefficient discovery only; any returned weights require exact arithmetic
acceptance and an independent replay before proof use.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix

HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('lat',HERE/'n29_t2_bad107_sh3_subset_lattice.py')
lat=module_from_spec(sp);sp.loader.exec_module(lat)
rd=lat.rd
RECT_SUPPORT={(3,V) for V in range(6,14)}
DIAG_SUPPORT={14,16}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
 raw=rd.allx.load29(z.demands_json,z.rows,2);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
 if len(P)!=902:raise SystemExit(f'expected 902 profiles, got {len(P)}')
 M,rect,diag,sh,layers,steps=lat.build(P,{'J0','J2'})
 active=[]
 for D,V,w in rect:
  if (D,V) in RECT_SUPPORT:active.append((f'B({D},{V})',w))
  else:M.bounds[w]=(0,0)
 for K,w in diag:
  if K in DIAG_SUPPORT:active.append((f'J({16-K})',w))
  else:M.bounds[w]=(0,0)
 active.append(('SH3',sh))
 n=len(M.names);A=lil_matrix((len(M.rows),n),dtype=float)
 for i,row in enumerate(M.rows):
  for j,v in row.items():A[i,j]=v
 lb=np.full(n,-np.inf);ub=np.full(n,np.inf)
 for j,(lo,hi) in enumerate(M.bounds):
  if lo is not None:lb[j]=lo
  if hi is not None:ub[j]=hi
 c=np.zeros(n);integrality=np.zeros(n,dtype=np.uint8)
 for _,w in active:c[w]=1.0;integrality[w]=1
 st=time.time();res=milp(c,integrality=integrality,bounds=Bounds(lb,ub),constraints=LinearConstraint(A.tocsr(),-np.inf,np.asarray(M.rhs,dtype=float)),options={'time_limit':900,'mip_rel_gap':0.0})
 out={'schema':'n29-t2-sh3-c11-integer-min-v1','profiles':len(P),'rows':len(M.rows),'variables':n,'support_rectangles':[list(x) for x in sorted(RECT_SUPPORT)],'diagonal_K':sorted(DIAG_SUPPORT),'SH_threshold':3,'floating_milp_reconnaissance_only':True,'success':bool(res.success),'status':int(res.status),'message':res.message,'seconds':time.time()-st,'objective':float(res.fun) if res.fun is not None else None,'mip_gap':float(getattr(res,'mip_gap',float('nan'))) if getattr(res,'mip_gap',None) is not None else None,'mip_node_count':int(getattr(res,'mip_node_count',-1)) if getattr(res,'mip_node_count',None) is not None else None}
 if res.x is not None:
  out['integer_weights']={name:int(round(res.x[w])) for name,w in active};out['integer_weight_sum']=sum(out['integer_weights'].values());out['raw_weight_values']={name:float(res.x[w]) for name,w in active}
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
 if not res.success:raise SystemExit(1)
if __name__=='__main__':main()
