#!/usr/bin/env python3
"""Cross-order transfer scan of the globally minimal n30 nine-shape support to n29.

For each positive zero-slack n29 RX-Hall hard profile, keep exactly the six BC
and three SH staircase generator shapes from the n30 global minimum-support
checkpoint, rebuild the envelope LP at (a,b,dmax)=(12,16,10), and allow only
the continuous coefficients/envelopes to refit. Numerical feasibility is
reconnaissance only. The question is whether the same finite staircase dictionary
has reach across orders, not whether n29 needs this route for its proof.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('gp',HERE/'shared_greedy_prune.py');gp=module_from_spec(sp);sp.loader.exec_module(gp)

def load(dp,rp,t):
    D=json.loads(Path(dp).read_text());out=[]
    for pos,line in enumerate(Path(rp).read_text().splitlines()):
        if not line.strip():continue
        z=list(map(int,line.split()));did,total,rho=z[0],z[1],z[2:];s=D[did]['s']
        if min(s)>0 and sum(s)==sum(rho)+2*t:out.append((pos,did,total,s,rho))
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--t',type=int,required=True);ap.add_argument('--shard',type=int,default=0);ap.add_argument('--shards',type=int,default=1);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    J=json.loads(z.support_json.read_text());bc=[tuple(tuple(p) for p in x['generators']) for x in J['active_BC']];sh=[tuple(tuple(p) for p in x['generators']) for x in J['active_SH']]
    hard=load(z.demands_json,z.rows,z.t);sel=[x for i,x in enumerate(hard) if i%z.shards==z.shard];rec=[];start=time.time()
    for local,(pos,did,total,s,rho) in enumerate(sel):
        P=[{'s':s,'rho':rho,'demand_id':did}];M,res=gp.solve(P,bc,sh,z.a,z.b,z.dmax)
        rec.append({'hard_position':next(i for i,x in enumerate(hard) if x[0]==pos and x[1]==did and x[4]==rho),'row_position':pos,'demand_id':did,'total':total,'feasible_shared_shape_envelope':bool(res.success),'objective':float(res.fun) if res.success else None})
    out={'schema':'n29-nine-shape-cross-order-transfer-v1','scope':{'a':z.a,'b':z.b,'dmax':z.dmax,'t':z.t},'support_source':str(z.support_json),'BC_shapes':len(bc),'SH_shapes':len(sh),'hard_rows_total':len(hard),'shard':z.shard,'shards':z.shards,'rows_in_shard':len(sel),'numerically_separated':sum(r['feasible_shared_shape_envelope'] for r in rec),'not_separated':sum(not r['feasible_shared_shape_envelope'] for r in rec),'records':rec,'seconds':time.time()-start,'floating_point_reconnaissance_only':True,'interpretation':'Feasible means the fixed nine-shape dictionary admits some profile-specific continuous envelope coefficients with margin >=1. This tests cross-order shape transfer only; it is not proof evidence and coefficients are not shared across profiles.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('records',)},indent=2,sort_keys=True))
if __name__=='__main__':main()
