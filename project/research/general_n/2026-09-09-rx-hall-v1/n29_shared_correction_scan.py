#!/usr/bin/env python3
"""Find and greedily compress one common staircase potential for all 38 n29 survivors.

Candidate dictionary = boundary-specialised n30 6+3 support union every distinct
proof-active BC/SH shape mined by the exact 38-profile correction run. The LP
uses one shared set of global/staircase coefficients across all 38 profiles and
profile-specific envelope variables. Floating reconnaissance only; any compact
support must be exactified separately.
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
    for x in C['pooled_proof_active_new_shapes']:
        g=tuple(tuple(p) for p in x['generators']);(bcpool if x['family']=='BC' else shpool).add(g)
    bc=sorted(bcpool);sh=sorted(shpool);M,res=gp.solve(P,bc,sh,z.a,z.b,z.dmax)
    out={'schema':'n29-shared-correction-scan-v1','profiles':len(P),'candidate_BC':len(bc),'candidate_SH':len(sh),'success':bool(res.success),'floating_point_reconnaissance_only':True}
    if res.success:
        active_bc=[bc[i] for i in range(len(bc)) if res.x[M.idx[('BC',i)]]>1e-8];active_sh=[sh[i] for i in range(len(sh)) if res.x[M.idx[('SH',i)]]>1e-8]
        initial={'BC':len(active_bc),'SH':len(active_sh),'total':len(active_bc)+len(active_sh),'objective':float(res.fun)}
        # deterministic greedy deletion from the L1-active support
        bc2=list(active_bc);sh2=list(active_sh);history=[];changed=True
        while changed:
            changed=False
            for fam,i in [('BC',i) for i in range(len(bc2))]+[('SH',i) for i in range(len(sh2))]:
                xb=bc2[:i]+bc2[i+1:] if fam=='BC' else list(bc2);xs=sh2[:i]+sh2[i+1:] if fam=='SH' else list(sh2)
                _,q=gp.solve(P,xb,xs,z.a,z.b,z.dmax)
                if q.success:
                    history.append({'family':fam,'index':i,'remaining_BC':len(xb),'remaining_SH':len(xs)});bc2,sh2=xb,xs;changed=True;break
        MF,rf=gp.solve(P,bc2,sh2,z.a,z.b,z.dmax)
        out.update({'initial_active':initial,'greedy_BC':len(bc2),'greedy_SH':len(sh2),'greedy_support':len(bc2)+len(sh2),'greedy_BC_shapes':[[list(p) for p in g] for g in bc2],'greedy_SH_shapes':[[list(p) for p in g] for g in sh2],'greedy_objective':float(rf.fun) if rf.success else None,'greedy_variables':{str(name):float(rf.x[i]) for i,name in enumerate(MF.names)} if rf.success else {},'history':history})
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('greedy_BC_shapes','greedy_SH_shapes','greedy_variables','history')},indent=2,sort_keys=True))
if __name__=='__main__':main()
