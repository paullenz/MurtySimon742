#!/usr/bin/env python3
"""Test c={0,1} and c={0,2} on each compact three-layer n29,t2 family.

All rectangle thresholds V=0..16 are allowed on the chosen three D layers.
Floating reconnaissance only; positive results require exactification.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('base',HERE/'n29_t2_layer23_diag012_scan.py');base=module_from_spec(sp);sp.loader.exec_module(base)
LAYERS={'123':(1,2,3),'234':(2,3,4)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--family',choices=sorted(LAYERS),required=True);ap.add_argument('--c-values',choices=['0,1','0,2'],required=True)
    ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    cs=tuple(map(int,z.c_values.split(',')));Ks=tuple(sorted(16-c for c in cs));raw=base.allx.load29(z.demands_json,z.rows,2);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
    st=time.time();M,rect,diag=base.build(P,layers=LAYERS[z.family],steps=Ks);res=M.solve()
    out={'schema':'n29-t2-three-layer-diagonal-pair-ablation-v1','family':z.family,'layers':list(LAYERS[z.family]),'profiles':len(P),'c_values':list(cs),'K_values':list(Ks),'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.success else None,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st,'all_rectangles_on_selected_layers':True,'SH':False,'floating_point_reconnaissance_only':True}
    if res.success:
        ar,ad=base.extract(res,rect,diag);out['active_rectangles']=[{k:v for k,v in q.items() if k!='var'} for q in ar];out['active_diagonals']=[{k:v for k,v in q.items() if k!='var'} for q in ad];out['active_generator_count']=len(ar)+len(ad)
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('active_rectangles','active_diagonals')},indent=2,sort_keys=True))
if __name__=='__main__':main()
