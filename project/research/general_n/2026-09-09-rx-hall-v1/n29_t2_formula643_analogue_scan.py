#!/usr/bin/env python3
"""Falsification test of the simple t=3 potential formula at n=29,t=2.

The t=3 exact potential is
    2t B(t,0) + (t+1) B(t,2t-1) + t B(t,3t).
At t=2 this predicts
    F = 4 B(2,0) + 3 B(2,3) + 2 B(2,6).

This script fixes those three global weights and gives every one of the 902 t=2
frontier profiles its own scalar/envelope variables.  A feasible result means
the simple potential survives this necessary test; infeasibility falsifies this
particular extrapolation.  Floating reconnaissance only.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('rd',HERE/'n29_t2_layer23_diag012_scan.py');rd=module_from_spec(sp);sp.loader.exec_module(rd)
WEIGHTS={(2,0):4,(2,3):3,(2,6):2}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    P0=rd.allx.load29(z.demands_json,z.rows,2);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in P0]
    if len(P)!=902: raise SystemExit(f'expected 902 profiles, got {len(P)}')
    M,rect,diag=rd.build(P,12,16,10,(2,),())
    for D,V,w in rect:
        val=WEIGHTS.get((D,V),0); M.bounds[w]=(val,val)
    st=time.time();res=M.solve()
    out={'schema':'n29-t2-t3formula-analogue-scan-v1','profiles':len(P),'global_potential':'4 B(2,0) + 3 B(2,3) + 2 B(2,6)',
         'formula':'2t B(t,0)+(t+1)B(t,2t-1)+tB(t,3t) at t=2','success':bool(res.success),'status':int(res.status),'message':res.message,
         'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st,'floating_point_reconnaissance_only':True,
         'interpretation':'Feasible means all 902 profiles admit profile-specific scalar certificates with this fixed three-rectangle potential. Infeasible falsifies this exact extrapolated potential.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
