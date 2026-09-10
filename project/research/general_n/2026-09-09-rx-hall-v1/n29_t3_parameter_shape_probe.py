#!/usr/bin/env python3
"""Falsification probe for the t-parametric BC shape on n29,t=3.

Tests all V rectangle thresholds on D={t,t+1,t+2}={3,4,5} together with the
exact diagonal slack thresholds c={0,t}={0,3}, i.e. K={16,13}. If feasible,
optionally greedy-prunes global generators. Floating reconnaissance only.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('base',HERE/'n29_t2_layer23_diag012_scan.py');base=module_from_spec(sp);sp.loader.exec_module(base)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--greedy',action='store_true');z=ap.parse_args()
 raw=base.allx.load29(z.demands_json,z.rows,3);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw];st=time.time();M,rect,diag=base.build(P,a=12,b=16,dmax=10,layers=(3,4,5),steps=(13,16));res=M.solve()
 out={'schema':'n29-t3-parametric-three-layer-shape-probe-v1','t':3,'profiles':len(P),'layers':[3,4,5],'diagonal_K':[13,16],'diagonal_c':[3,0],'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.success else None,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st,'floating_point_reconnaissance_only':True}
 if res.success:
  ar,ad=base.extract(res,rect,diag);out['active_rectangles_initial']=[{k:v for k,v in q.items() if k!='var'} for q in ar];out['active_diagonals_initial']=[{k:v for k,v in q.items() if k!='var'} for q in ad];out['active_generator_count_initial']=len(ar)+len(ad)
  if z.greedy:
   rr,ar2,ad2,att=base.greedy_prune(M,res,rect,diag);out['active_rectangles_greedy']=[{k:v for k,v in q.items() if k!='var'} for q in ar2];out['active_diagonals_greedy']=[{k:v for k,v in q.items() if k!='var'} for q in ad2];out['active_generator_count_greedy']=len(ar2)+len(ad2);out['greedy_attempts']=att;out['objective_greedy']=float(rr.fun)
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if not k.startswith('active_') and k!='greedy_attempts'},indent=2,sort_keys=True))
if __name__=='__main__':main()
