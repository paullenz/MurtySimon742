#!/usr/bin/env python3
"""Apply the exact 14-shape common F+G weights to the full n29 hard frontier.

The BC/SH shapes and common weights are frozen from an exact integer checkpoint.
For each regenerated n29 (s,rho) hard profile, only its scalar lambda,c,mu,tau_h
and envelope variables may vary. This tests reach of one fixed combinatorial
potential across t=2 and t=3 frontiers.

Numerical feasibility is reconnaissance here; the frozen weights themselves come
from an exact checkpoint, but per-profile scalar solutions are not exactified by
this scan.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('cp',HERE/'n29_common_potential_profile_scalars.py');cp=module_from_spec(sp);sp.loader.exec_module(cp)

def load(dp,rp,t):
    D=json.loads(Path(dp).read_text());out=[]
    for pos,line in enumerate(Path(rp).read_text().splitlines()):
        if not line.strip():continue
        z=list(map(int,line.split()));did,total,rho=z[0],z[1],z[2:];s=D[did]['s']
        if min(s)>0 and sum(s)==sum(rho)+2*t:out.append((pos,did,total,s,rho))
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--exact-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--t',type=int,required=True);ap.add_argument('--shard',type=int,default=0);ap.add_argument('--shards',type=int,default=1);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();J=json.loads(z.exact_json.read_text());assert J['status']=='PASS';scale=J['scale'];bc=[tuple(tuple(p) for p in g) for g in J['BC_shapes']];sh=[tuple(tuple(p) for p in g) for g in J['SH_shapes']];weights_bc=[J['integer_variables'][str(('BC',i))]/scale for i in range(len(bc))];weights_sh=[J['integer_variables'][str(('SH',i))]/scale for i in range(len(sh))]
    hard=load(z.demands_json,z.rows,z.t);sel=[(i,x) for i,x in enumerate(hard) if i%z.shards==z.shard];rec=[];start=time.time()
    for hp,(pos,did,total,s,rho) in sel:
        P=[{'s':s,'rho':rho,'demand_id':did}];M=cp.build(P,bc,sh,z.a,z.b,z.dmax)
        for i,w in enumerate(weights_bc):M.bounds[M.idx[('BC',i)]]=(w,w)
        for i,w in enumerate(weights_sh):M.bounds[M.idx[('SH',i)]]=(w,w)
        res=M.solve();rec.append({'hard_position':hp,'row_position':pos,'demand_id':did,'total':total,'separated':bool(res.success),'objective':float(res.fun) if res.success else None})
    out={'schema':'n29-fixed-exact-potential-full-frontier-v1','scope':{'a':z.a,'b':z.b,'dmax':z.dmax,'t':z.t},'source_exact_checkpoint':str(z.exact_json),'support_count':len(bc)+len(sh),'hard_rows_total':len(hard),'shard':z.shard,'shards':z.shards,'rows_in_shard':len(sel),'separated':sum(r['separated'] for r in rec),'survivors':sum(not r['separated'] for r in rec),'records':rec,'seconds':time.time()-start,'floating_scalar_reconnaissance_only':True,'frozen_FG_weights_from_exact_checkpoint':True,'interpretation':'One exact-checkpoint F+G is held fixed. Only profile scalar/envelope variables refit numerically. Survivors are envelope-model states, not graphs.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2,sort_keys=True))
if __name__=='__main__':main()
