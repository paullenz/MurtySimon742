#!/usr/bin/env python3
"""Hierarchy test for compact n=29,t=2 RX-Hall potential geometry.

The fixed coefficient triple 4,3,2 on B(2,0),B(2,3),B(2,6) is infeasible for
107/902 profiles.  That does NOT imply the three-rectangle support is itself
insufficient.  This script tests, in increasing geometric richness:

  1. same three rectangles with FREE nonnegative common weights;
  2. the complete D=2 rectangle layer B(2,V), V=0..16;
  3. complete D=2 layer plus exact diagonal-slack cuts c=0,2 (K=16,14);
  4. complete D=2 and D=3 rectangle layers, no diagonals.

Every profile retains its own scalar/envelope variables.  Floating LP results
are reconnaissance only; any positive result must be exactified separately.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time

HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('rd',HERE/'n29_t2_layer23_diag012_scan.py');rd=module_from_spec(sp);sp.loader.exec_module(rd)

CASES=[
 ('three_free',(2,),(),{(2,0),(2,3),(2,6)}),
 ('D2_all',(2,),(),None),
 ('D2_all_J02',(2,),(14,16),None),
 ('D2_D3_all',(2,3),(),None),
]

def solve_case(P,name,layers,steps,allowed):
    st=time.time();M,rect,diag=rd.build(P,12,16,10,layers,steps)
    if allowed is not None:
        for D,V,w in rect:
            if (D,V) not in allowed:M.bounds[w]=(0,0)
    res=M.solve();rec={'case':name,'layers':list(layers),'diagonal_K':list(steps),'success':bool(res.success),'status':int(res.status),'message':res.message,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st}
    if res.success:
        rec['objective']=float(res.fun)
        rec['active_rectangles']=[{'D':D,'V':V,'weight':float(res.x[w])} for D,V,w in rect if res.x[w]>1e-8]
        rec['active_diagonals']=[{'K':K,'c':16-K,'weight':float(res.x[w])} for K,w in diag if res.x[w]>1e-8]
        rec['active_generator_count']=len(rec['active_rectangles'])+len(rec['active_diagonals'])
    return rec

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    raw=rd.allx.load29(z.demands_json,z.rows,2);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
    if len(P)!=902:raise SystemExit(f'expected 902 profiles, got {len(P)}')
    out={'schema':'n29-t2-geometry-hierarchy-scan-v1','profiles':902,'floating_point_reconnaissance_only':True,'fixed_432_obstruction_count':107,'cases':[]}
    for cfg in CASES:
        rec=solve_case(P,*cfg);out['cases'].append(rec);print(json.dumps(rec,indent=2,sort_keys=True),flush=True)
    out['interpretation']='The fixed 4,3,2 weights were already falsified. This scan distinguishes coefficient failure from support/geometry failure. Any feasible case is only a candidate architecture until exactified.'
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if __name__=='__main__':main()
