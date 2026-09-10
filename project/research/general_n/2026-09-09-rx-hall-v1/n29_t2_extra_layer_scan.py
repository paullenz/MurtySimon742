#!/usr/bin/env python3
"""Test {D=2,3} plus one extra rectangle d-layer on all n29,t=2 profiles.

The diagonal family is fixed to K=14,15,16 (slack c=2,1,0); SH is absent.
This isolates which additional d-threshold layer, if any, is sufficient to repair
the failed two-layer order-wide transfer.

Floating reconnaissance only.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('base',HERE/'n29_t2_layer23_diag012_scan.py');base=module_from_spec(sp);sp.loader.exec_module(base)
sp2=spec_from_file_location('allx',HERE/'cross_order_all1003_fixed16.py');allx=module_from_spec(sp2);sp2.loader.exec_module(allx)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--extra-D',type=int,required=True);ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    if z.extra_D in (2,3) or not (0<=z.extra_D<=11):raise SystemExit('extra-D must be in 0..11 except 2,3')
    raw=allx.load29(z.demands_json,z.rows,2);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
    layers=tuple(sorted((2,3,z.extra_D)));st=time.time();M,rect,diag=base.build(P,layers=layers,steps=(14,15,16));res=M.solve()
    out={'schema':'n29-t2-one-extra-layer-v1','profiles':len(P),'layers':list(layers),'extra_D':z.extra_D,'diagonal_K':[14,15,16],'diagonal_c':[2,1,0],'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.success else None,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st,'floating_point_reconnaissance_only':True}
    if res.success:
        ar,ad=base.extract(res,rect,diag);out['active_rectangles']=[{k:v for k,v in q.items() if k!='var'} for q in ar];out['active_diagonals']=[{k:v for k,v in q.items() if k!='var'} for q in ad];out['active_generator_count']=len(ar)+len(ad);out['active_by_D']={str(D):sum(1 for q in ar if q['D']==D) for D in layers}
    out['interpretation']='Tests whether one additional d-threshold layer repairs the failed D={2,3} plus c={0,1,2} order-wide potential. No SH. Positive results are floating until exactified.'
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('active_rectangles','active_diagonals')},indent=2,sort_keys=True))
if __name__=='__main__':main()
