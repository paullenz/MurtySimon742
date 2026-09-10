#!/usr/bin/env python3
"""Probe rounded small-integer global potentials for n29,t2 all902.

The template is obtained by normalizing the exact 16-generator certificate by
its repeated unit 1,588,056 and rounding at a small multiplier. This is
reconnaissance only: success identifies a simpler exactification target.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time,math
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('base',HERE/'n29_t2_layer23_diag012_scan.py');base=module_from_spec(sp);sp.loader.exec_module(base)
BASE=1588056
RAW={
 ('r',2,11):2117408,('r',2,12):2288470,('r',2,13):5594580,('r',2,14):1525289,
 ('r',3,0):8060082,('r',3,4):1505280,('r',3,7):1588056,('r',3,8):1588056,('r',3,10):2117408,('r',3,12):1028710,
 ('r',4,2):938923,('r',4,3):1003596,('r',4,6):1146369,('r',4,9):1588056,
 ('j',14):2952282,('j',16):2792291}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--multiplier',type=int,required=True);ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    if z.multiplier<1:raise SystemExit('multiplier must be positive')
    W={k:max(1,round(v*z.multiplier/BASE)) for k,v in RAW.items()}
    raw=base.allx.load29(z.demands_json,z.rows,2);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
    M,rect,diag=base.build(P,layers=(2,3,4),steps=(14,16))
    for D,V,w in rect:
        val=W.get(('r',D,V),0);M.bounds[w]=(val,val)
    for K,w in diag:
        val=W[('j',K)];M.bounds[w]=(val,val)
    st=time.time();res=M.solve();sec=time.time()-st
    out={'schema':'n29-t2-c02-support16-small-integer-probe-v1','profiles':len(P),'multiplier':z.multiplier,'normalized_base':BASE,'fixed_integer_weights':{str(k):v for k,v in W.items()},'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.success else None,'rows':len(M.rows),'variables':len(M.names),'seconds':sec,'floating_feasibility_reconnaissance_only':True}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
