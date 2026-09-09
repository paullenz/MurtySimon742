#!/usr/bin/env python3
"""Test one shared staircase potential using the FULL generated correction cut pool.

Unlike n29_shared_correction_scan, this does not restrict to shapes that were
proof-active in individually chosen Farkas certificates. It pools every BC/SH
shape generated during separation on the 38 profiles, plus the specialised n30
base support, then asks whether one common coefficient vector separates all 38.
If feasible, greedily prune the L1-active support. Floating reconnaissance only.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('gp',HERE/'shared_greedy_prune.py');gp=module_from_spec(sp);sp.loader.exec_module(gp)

def leq(a,b):return all(x<=y for x,y in zip(a,b))
def min_gens(g):
    pts=sorted(set(tuple(p) for p in g));return tuple(p for p in pts if not any(q!=p and leq(q,p) for q in pts))
def trim(g,dmax):return min_gens(p for p in g if p[0]<=dmax)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--correction-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    B=json.loads(z.boundary_json.read_text());S=json.loads(z.support_json.read_text());C=json.loads(z.correction_json.read_text());P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['trimmed_survivor_records']]
    bcpool={trim(tuple(tuple(p) for p in x['generators']),z.dmax) for x in S['active_BC']};shpool={tuple(tuple(p) for p in x['generators']) for x in S['active_SH']}
    total_generated=0
    for r in C['records']:
        for x in r['cuts']:
            total_generated+=1;g=tuple(tuple(p) for p in x['generators']);(bcpool if x['family']=='BC' else shpool).add(g)
    bc=sorted(bcpool);sh=sorted(shpool);M,res=gp.solve(P,bc,sh,z.a,z.b,z.dmax)
    out={'schema':'n29-shared-fullcut-scan-v1','profiles':len(P),'raw_generated_cuts':total_generated,'candidate_BC':len(bc),'candidate_SH':len(sh),'success':bool(res.success),'floating_point_reconnaissance_only':True}
    if res.success:
        active_bc=[bc[i] for i in range(len(bc)) if res.x[M.idx[('BC',i)]]>1e-8];active_sh=[sh[i] for i in range(len(sh)) if res.x[M.idx[('SH',i)]]>1e-8]
        bc2=list(active_bc);sh2=list(active_sh);history=[];changed=True
        while changed:
            changed=False
            for fam,i in [('BC',i) for i in range(len(bc2))]+[('SH',i) for i in range(len(sh2))]:
                xb=bc2[:i]+bc2[i+1:] if fam=='BC' else list(bc2);xs=sh2[:i]+sh2[i+1:] if fam=='SH' else list(sh2)
                _,q=gp.solve(P,xb,xs,z.a,z.b,z.dmax)
                if q.success:
                    history.append({'family':fam,'index':i,'remaining_BC':len(xb),'remaining_SH':len(xs)});bc2,sh2=xb,xs;changed=True;break
        MF,rf=gp.solve(P,bc2,sh2,z.a,z.b,z.dmax)
        out.update({'initial_active_BC':len(active_bc),'initial_active_SH':len(active_sh),'greedy_BC':len(bc2),'greedy_SH':len(sh2),'greedy_support':len(bc2)+len(sh2),'greedy_BC_shapes':[[list(p) for p in g] for g in bc2],'greedy_SH_shapes':[[list(p) for p in g] for g in sh2],'greedy_objective':float(rf.fun) if rf.success else None,'greedy_variables':{str(name):float(rf.x[i]) for i,name in enumerate(MF.names)} if rf.success else {},'history':history})
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('greedy_BC_shapes','greedy_SH_shapes','greedy_variables','history')},indent=2,sort_keys=True))
if __name__=='__main__':main()
