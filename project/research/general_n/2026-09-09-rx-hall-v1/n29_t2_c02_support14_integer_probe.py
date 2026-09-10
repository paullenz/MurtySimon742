#!/usr/bin/env python3
"""Probe small fixed-integer versions of the exact 14-generator n29,t2 potential.

Global weights are normalized by the repeated exact unit B(3,7)=B(3,8)=B(4,9)
and rounded at the requested multiplier. Profile-specific envelope variables
remain free. Floating reconnaissance only; any positive result requires an
exact replay with the global weights frozen.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('base',HERE/'n29_t2_layer23_diag012_scan.py');base=module_from_spec(sp);sp.loader.exec_module(base)
BASE=4927298
RAW={
 ('r',2,11):6569730,('r',2,12):7443376,('r',2,13):17353143,('r',2,14):4858018,
 ('r',3,0):27264267,('r',3,4):4985326,('r',3,7):4927298,('r',3,8):4927298,('r',3,10):6569730,
 ('r',4,3):3172445,('r',4,6):3557316,('r',4,9):4927298,
 ('j',14):9135500,('j',16):8642565}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--multiplier',type=int,required=True);ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
 if z.multiplier<1:raise SystemExit('multiplier must be positive')
 W={k:max(1,round(v*z.multiplier/BASE)) for k,v in RAW.items()}
 raw=base.allx.load29(z.demands_json,z.rows,2);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw];M,rect,diag=base.build(P,layers=(2,3,4),steps=(14,16))
 for D,V,w in rect:
  val=W.get(('r',D,V),0);M.bounds[w]=(val,val)
 for K,w in diag:
  val=W[('j',K)];M.bounds[w]=(val,val)
 st=time.time();res=M.solve();out={'schema':'n29-t2-c02-support14-small-integer-probe-v1','profiles':len(P),'multiplier':z.multiplier,'normalized_base':BASE,'fixed_integer_weights':{str(k):v for k,v in W.items()},'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.success else None,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st,'floating_feasibility_reconnaissance_only':True}
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
