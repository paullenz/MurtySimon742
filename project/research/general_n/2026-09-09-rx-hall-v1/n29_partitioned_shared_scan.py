#!/usr/bin/env python3
"""Test whether shared staircase coefficients need only low-dimensional profile parameters.

Uses the same pooled candidate dictionary as n29_shared_correction_scan. Tests
shared-envelope feasibility after partitioning the 38 profiles by natural scalar
invariants, especially r=sum(rho)=S-4. Floating reconnaissance only.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
from collections import defaultdict,Counter
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('gp',HERE/'shared_greedy_prune.py');gp=module_from_spec(sp);sp.loader.exec_module(gp)

def leq(a,b):return all(x<=y for x,y in zip(a,b))
def min_gens(g):
    pts=sorted(set(tuple(p) for p in g));return tuple(p for p in pts if not any(q!=p and leq(q,p) for q in pts))
def trim(g,dmax):return min_gens(p for p in g if p[0]<=dmax)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--correction-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    B=json.loads(z.boundary_json.read_text());S=json.loads(z.support_json.read_text());C=json.loads(z.correction_json.read_text());raw=B['trimmed_survivor_records'];P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id'],'hard_position':r['hard_position']} for r in raw]
    bcpool={trim(tuple(tuple(p) for p in x['generators']),z.dmax) for x in S['active_BC']};shpool={tuple(tuple(p) for p in x['generators']) for x in S['active_SH']}
    for x in C['pooled_proof_active_new_shapes']:
        g=tuple(tuple(p) for p in x['generators']);(bcpool if x['family']=='BC' else shpool).add(g)
    bc=sorted(bcpool);sh=sorted(shpool)
    funcs={
      'r':lambda p:sum(p['rho']),
      'H':lambda p:max(p['s']),
      'rho_max':lambda p:max(p['rho']),
      'r_H':lambda p:(sum(p['rho']),max(p['s'])),
      'r_rhomax':lambda p:(sum(p['rho']),max(p['rho'])),
      'H_rhomax':lambda p:(max(p['s']),max(p['rho'])),
    }
    results={}
    for name,f in funcs.items():
        groups=defaultdict(list)
        for p in P:groups[str(f(p))].append(p)
        grecs=[]
        for key,G in sorted(groups.items()):
            M,res=gp.solve(G,bc,sh,z.a,z.b,z.dmax)
            active_bc=sum(res.success and res.x[M.idx[('BC',i)]]>1e-8 for i in range(len(bc))) if res.x is not None else None
            active_sh=sum(res.success and res.x[M.idx[('SH',i)]]>1e-8 for i in range(len(sh))) if res.x is not None else None
            grecs.append({'key':key,'profiles':len(G),'positions':[p['hard_position'] for p in G],'success':bool(res.success),'active_BC':active_bc,'active_SH':active_sh,'objective':float(res.fun) if res.success else None})
        results[name]={'groups':len(grecs),'all_groups_feasible':all(g['success'] for g in grecs),'failed_groups':sum(not g['success'] for g in grecs),'records':grecs}
    out={'schema':'n29-partitioned-shared-correction-scan-v1','profiles':len(P),'candidate_BC':len(bc),'candidate_SH':len(sh),'floating_point_reconnaissance_only':True,'results':results,'interpretation':'Tests whether the pooled pairwise staircase dictionary admits shared coefficients within natural scalar parameter layers. Feasible is numerical reconnaissance only.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:{'groups':v['groups'],'all_groups_feasible':v['all_groups_feasible'],'failed_groups':v['failed_groups']} for k,v in results.items()},indent=2,sort_keys=True))
if __name__=='__main__':main()
