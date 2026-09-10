#!/usr/bin/env python3
"""Ablate subsets of the c={0,1,2} diagonal slack thresholds on all n29,t=2.

Every test retains the full BC rectangle cone (all D=0..11,V=0..16) and no SH.
The selected c values correspond to K=b-c with b=16.

Floating reconnaissance only.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('base',HERE/'n29_t2_layer23_diag012_scan.py');base=module_from_spec(sp);sp.loader.exec_module(base)
sp2=spec_from_file_location('allx',HERE/'cross_order_all1003_fixed16.py');allx=module_from_spec(sp2);sp2.loader.exec_module(allx)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--c-values',required=True,help='comma-separated subset of 0,1,2');ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    cs=tuple(sorted({int(x) for x in z.c_values.split(',') if x!=''}))
    if not cs or any(c not in (0,1,2) for c in cs):raise SystemExit('c-values must be nonempty subset of 0,1,2')
    Ks=tuple(sorted(16-c for c in cs));raw=allx.load29(z.demands_json,z.rows,2);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
    st=time.time();M,rect,diag=base.build(P,layers=tuple(range(12)),steps=Ks);res=M.solve()
    out={'schema':'n29-t2-diagonal-subset-ablation-v1','profiles':len(P),'c_values':list(cs),'K_values':list(Ks),'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.success else None,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st,'full_rectangle_cone':True,'SH':False,'floating_point_reconnaissance_only':True}
    if res.success:
        ar,ad=base.extract(res,rect,diag);out['active_rectangle_count']=len(ar);out['active_D_layers']=sorted({q['D'] for q in ar});out['active_diagonals']=[{k:v for k,v in q.items() if k!='var'} for q in ad]
    out['interpretation']='Tests necessity/sufficiency of selected cumulative slack thresholds c among {0,1,2} when every BC rectangle is available. A failed subset is evidence that this restricted generator family cannot give one common finite potential.'
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
