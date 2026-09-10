#!/usr/bin/env python3
"""L1 generator-coordinate decomposition for all 902 n29,t=2 profiles.

Generators:
  * every BC rectangle B_{D,V}, D=0..11, V=0..16;
  * exactly the three diagonal slack thresholds K=14,15,16 (c=2,1,0);
  * no SH.

This is equivalent in expressive type to the successful 'near' diagonal-step
supermodular scan, but it exposes the supermodular part in its exact rectangle
Möbius coordinates.  Floating reconnaissance only.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('base',HERE/'n29_t2_layer23_diag012_scan.py');base=module_from_spec(sp);sp.loader.exec_module(base)
sp2=spec_from_file_location('allx',HERE/'cross_order_all1003_fixed16.py');allx=module_from_spec(sp2);sp2.loader.exec_module(allx)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    raw=allx.load29(z.demands_json,z.rows,2);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
    layers=tuple(range(12));st=time.time();M,rect,diag=base.build(P,layers=layers,steps=(14,15,16));res=M.solve()
    out={'schema':'n29-t2-all902-rectdiag-l1-v1','profiles':len(P),'layers':list(layers),'diagonal_K':[14,15,16],'diagonal_c':[2,1,0],'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.success else None,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st,'floating_point_reconnaissance_only':True}
    if res.success:
        ar,ad=base.extract(res,rect,diag);ar=[{k:v for k,v in q.items() if k!='var'} for q in ar];ad=[{k:v for k,v in q.items() if k!='var'} for q in ad]
        out['active_rectangles']=ar;out['active_diagonals']=ad;out['active_rectangle_count']=len(ar);out['active_diagonal_count']=len(ad);out['active_generator_count']=len(ar)+len(ad)
        by={}
        for q in ar:by.setdefault(str(q['D']),[]).append({'V':q['V'],'weight':q['weight']})
        out['active_by_D']=by;out['active_D_layers']=sorted(int(k) for k in by)
    out['interpretation']='L1 decomposition of the successful all-902 rectangle+{c=0,1,2} family. It exposes which d-layers carry positive rectangle Möbius mass; no sparsity minimality or exactness is claimed.'
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
