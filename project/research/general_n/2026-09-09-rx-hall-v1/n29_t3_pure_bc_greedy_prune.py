#!/usr/bin/env python3
"""Greedily prune the exact 16-active-BC n29 t=3 common potential.

Start from the 16 canonical BC indices with nonzero exact rational coefficient in
N29_T3_PURE_BC_EXACT_M200_RUN_34383214636. Attempt to delete one shape at a time,
re-solving the continuous common-potential LP across all 94 regenerated t=3 hard
profiles. Repeat passes until no deletion succeeds. `normal` and `reverse` orders
probe simple path dependence. Floating pruning only; any survivor must be
exactified again before use.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('cp',HERE/'n29_common_potential_profile_scalars.py');cp=module_from_spec(sp);sp.loader.exec_module(cp)
sp2=spec_from_file_location('ex',HERE/'n29_all_t23_exactify.py');ex=module_from_spec(sp2);sp2.loader.exec_module(ex)
START=[2,3,4,5,6,13,14,15,17,31,45,47,48,50,56,70]
def tup(g):return tuple(tuple(p) for p in g)
def feasible(P,allbc,idx):
    M=cp.build(P,[allbc[i] for i in idx],[],12,16,10);r=M.solve();return bool(r.success),float(r.fun) if r.success else None,len(M.rows),len(M.names)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--dictionary-json',type=Path,required=True);ap.add_argument('--order',choices=['normal','reverse'],required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    P=ex.load(z.demands,z.rows,3);D=json.loads(z.dictionary_json.read_text());allbc=[tup(x['generators']) for x in D['BC']];cur=list(START);history=[];changed=True;passes=0;st=time.time()
    ok,_,rows,vars=feasible(P,allbc,cur)
    if not ok:raise SystemExit('starting exact-active 16 support unexpectedly infeasible')
    while changed:
        changed=False;passes+=1;seq=list(cur) if z.order=='normal' else list(reversed(cur))
        for i in seq:
            if i not in cur:continue
            trial=[j for j in cur if j!=i];ok,obj,_,_=feasible(P,allbc,trial);history.append({'pass':passes,'removed_candidate':i,'trial_count':len(trial),'feasible':ok,'objective':obj})
            print(json.dumps(history[-1],sort_keys=True),flush=True)
            if ok:cur=trial;changed=True
    out={'schema':'n29-t3-pure-bc-greedy-prune-v1','order':z.order,'profiles':len(P),'start_indices':START,'start_count':len(START),'final_indices':cur,'final_count':len(cur),'passes':passes,'tests':len(history),'rows_at_start':rows,'variables_at_start':vars,'seconds':time.time()-st,'floating_point_reconnaissance_only':True,'history':history,'interpretation':'Greedy continuous-LP pruning from the exact 16-active-BC support. A smaller final support is only a numerical candidate until separately exactified.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='history'},indent=2,sort_keys=True))
if __name__=='__main__':main()
