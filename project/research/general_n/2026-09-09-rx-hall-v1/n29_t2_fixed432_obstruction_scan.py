#!/usr/bin/env python3
"""Locate the n=29,t=2 profiles obstructing F=4B(2,0)+3B(2,3)+2B(2,6).

With the global potential fixed, all scalar/envelope variables are profile-local.
Hence a subset LP is feasible iff every profile in the subset is feasible.  We
use recursive binary splitting: test a block; if infeasible, split it until the
infeasible singleton profiles are isolated.  Floating reconnaissance only.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('rd',HERE/'n29_t2_layer23_diag012_scan.py');rd=module_from_spec(sp);sp.loader.exec_module(rd)
W={(2,0):4,(2,3):3,(2,6):2}

def build_solve(P):
    M,rect,diag=rd.build(P,12,16,10,(2,),())
    for D,V,w in rect:
        val=W.get((D,V),0);M.bounds[w]=(val,val)
    res=M.solve()
    return bool(res.success),int(res.status),res.message,len(M.rows),len(M.names)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    raw=rd.allx.load29(z.demands_json,z.rows,2);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
    if len(P)!=902:raise SystemExit(f'expected 902 profiles, got {len(P)}')
    cache={};tests=[]
    def test(indices):
        key=(indices[0],indices[-1],len(indices)) if indices else None
        if key in cache:return cache[key]
        st=time.time();ans=build_solve([P[i] for i in indices]);tests.append({'first':indices[0],'last':indices[-1],'count':len(indices),'success':ans[0],'status':ans[1],'seconds':time.time()-st});cache[key]=ans[0];return ans[0]
    bad=[]
    def split(indices):
        if test(indices):return
        if len(indices)==1:bad.append(indices[0]);return
        m=len(indices)//2;split(indices[:m]);split(indices[m:])
    st=time.time();split(list(range(len(P))))
    bad=sorted(bad)
    records=[]
    for i in bad:
        pf=P[i];records.append({'index':i,'demand_id':pf['demand_id'],'s':pf['s'],'rho':pf['rho'],'sum_s':sum(pf['s']),'sum_rho':sum(pf['rho'])})
    out={'schema':'n29-t2-fixed432-obstruction-scan-v1','status':'PASS_SCAN','profiles':len(P),'global_potential':'4 B(2,0)+3 B(2,3)+2 B(2,6)','floating_point_reconnaissance_only':True,'bad_profile_count':len(bad),'bad_indices':bad,'bad_profiles':records,'subset_lp_tests':len(tests),'tests':tests,'seconds':time.time()-st,'interpretation':'Each reported singleton is floating-infeasible with the fixed three-rectangle potential. Because scalar variables are profile-local once F is fixed, recursive block splitting is logically equivalent to individual feasibility testing, modulo solver correctness.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='tests'},indent=2,sort_keys=True))
if __name__=='__main__':main()
