#!/usr/bin/env python3
"""Test dmax-specialisation of the n30 nine-shape BC dictionary on n29.

Any BC minimal generator (D,-H) with D>dmax has no label-side support at the
new order. Removing it produces another valid BC upper set and can only reduce
the source-side indicator while leaving the realised label-side set unchanged.
This is therefore a natural order-specialisation, not a new staircase family.

Floating feasibility is reconnaissance only. Reports both baseline and trimmed
coverage, with full survivor identifiers for follow-up.
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

def trim_shape(g,dmax):
    return tuple(p for p in g if p[0]<=dmax)

def scan_profile(s,rho,did,bc,sh,a,b,dmax):
    P=[{'s':s,'rho':rho,'demand_id':did}]
    M,res=gp.solve(P,bc,sh,a,b,dmax)
    return bool(res.success), (float(res.fun) if res.success else None)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--t',type=int,required=True);ap.add_argument('--shard',type=int,default=0);ap.add_argument('--shards',type=int,default=1);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    J=json.loads(z.support_json.read_text());base_bc=[tuple(tuple(p) for p in x['generators']) for x in J['active_BC']];sh=[tuple(tuple(p) for p in x['generators']) for x in J['active_SH']]
    trim_bc=[trim_shape(g,z.dmax) for g in base_bc]
    if any(not g for g in trim_bc):raise SystemExit('trim produced empty BC shape')
    changed=[i for i,(x,y) in enumerate(zip(base_bc,trim_bc)) if x!=y]
    hard=load(z.demands_json,z.rows,z.t);sel=[(i,x) for i,x in enumerate(hard) if i%z.shards==z.shard];rec=[];start=time.time()
    for hp,(pos,did,total,s,rho) in sel:
        b_ok,b_obj=scan_profile(s,rho,did,base_bc,sh,z.a,z.b,z.dmax)
        t_ok,t_obj=scan_profile(s,rho,did,trim_bc,sh,z.a,z.b,z.dmax)
        rec.append({'hard_position':hp,'row_position':pos,'demand_id':did,'total':total,'s':s,'rho':rho,'baseline_separated':b_ok,'trimmed_separated':t_ok,'baseline_objective':b_obj,'trimmed_objective':t_obj})
    out={'schema':'n29-nine-shape-boundary-specialisation-v1','scope':{'a':z.a,'b':z.b,'dmax':z.dmax,'t':z.t},'changed_BC_indices':changed,'baseline_BC_shapes':[[list(p) for p in g] for g in base_bc],'trimmed_BC_shapes':[[list(p) for p in g] for g in trim_bc],'SH_shapes':[[list(p) for p in g] for g in sh],'hard_rows_total':len(hard),'shard':z.shard,'shards':z.shards,'rows_in_shard':len(sel),'baseline_separated':sum(r['baseline_separated'] for r in rec),'trimmed_separated':sum(r['trimmed_separated'] for r in rec),'baseline_survivors':sum(not r['baseline_separated'] for r in rec),'trimmed_survivors':sum(not r['trimmed_separated'] for r in rec),'records':rec,'seconds':time.time()-start,'floating_point_reconnaissance_only':True,'interpretation':'Trim deletes BC generators with D>dmax. This is an order-specific valid upper-set specialisation, not a new shape family. Feasibility is numerical reconnaissance only.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('records','baseline_BC_shapes','trimmed_BC_shapes','SH_shapes')},indent=2,sort_keys=True))
if __name__=='__main__':main()
