#!/usr/bin/env python3
"""Floating common-scalar tests for the n29,t=3 fixed-643 exceptional profiles.

The exact broad templates A1 and A38 cover 91/94 profiles; their joint missing
set is {0,5,30}.  Test whether these three profiles can share one scalar template
under F=6B(3,0)+4B(3,5)+3B(3,9).  Pairwise tests are included to diagnose any
triple failure. Discovery only; any successful theta must be rationalised and
checked exactly before proof use.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('rd',HERE/'n29_t2_layer23_diag012_scan.py');rd=module_from_spec(sp);sp.loader.exec_module(rd)
WEIGHTS={(3,0):6,(3,5):4,(3,9):3}
GROUPS=[(0,5,30),(0,5),(0,30),(5,30)]

def solve_group(P,indices):
    Q=[P[i] for i in indices]
    M,rect,diag=rd.build(Q,12,16,10,(3,),())
    for D,V,w in rect:
        val=WEIGHTS.get((D,V),0);M.bounds[w]=(val,val)
    keys=[('lambda',),('c',),('mu+',),('mu-',)]+[('tau',j) for j in range(1,13)]
    for pi in range(1,len(Q)):
        for key in keys:
            if key[0]=='tau': n0=('tau',0,key[1]);ni=('tau',pi,key[1])
            else:n0=(key[0],0);ni=(key[0],pi)
            a=M.idx[n0];b=M.idx[ni];M.le({b:1,a:-1},0);M.le({a:1,b:-1},0)
    st=time.time();res=M.solve();out={'indices':list(indices),'success':bool(res.success),'status':int(res.status),'message':res.message,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st}
    if res.success:
        vals={}
        for key in keys:
            name=('tau',0,key[1]) if key[0]=='tau' else (key[0],0)
            v=float(res.x[M.idx[name]])
            if abs(v)>1e-9:vals['tau'+str(key[1]) if key[0]=='tau' else key[0]]=v
        out['theta_nonzero']=vals
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    raw=rd.allx.load29(z.demands_json,z.rows,3);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
    if len(P)!=94:raise SystemExit(f'expected 94 profiles, got {len(P)}')
    tests=[solve_group(P,g) for g in GROUPS]
    out={'schema':'n29-t3-fixed643-exception-group-scan-v1','profiles':94,'global_potential':'6 B(3,0)+4 B(3,5)+3 B(3,9)','groups':tests,'floating_point_reconnaissance_only':True,'interpretation':'The exact A1+A38 union misses exactly profiles 0,5,30. A feasible triple would reduce the current exact five-template architecture to a candidate three-template architecture after exactification.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
