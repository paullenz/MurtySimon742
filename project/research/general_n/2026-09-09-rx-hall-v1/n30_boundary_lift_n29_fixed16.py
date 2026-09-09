#!/usr/bin/env python3
"""Test the dmax=10 -> 11 boundary lift of the exact n29 16-shape family on n30.

The two n29 BC staircases obtained earlier by specialising the n30 base family
lost the endpoint (11,-11) when dmax dropped from 11 to 10.  Restore that endpoint
in exactly those two shapes, keep the other 14 shapes unchanged, and solve for a
fresh common n30 staircase-weight vector across all seven n30 t=1 hard profiles.

Success would support a parameterized boundary-extension rule for the BC family.
Floating reconnaissance only; a positive result needs exactification.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('co',HERE/'cross_order_common_potential.py');co=module_from_spec(sp);sp.loader.exec_module(co)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--n30-json',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    N=json.loads(z.n30_json.read_text());J=json.loads(z.support_json.read_text())
    bc=[tuple(tuple(p) for p in g) for g in J['BC_shapes']];sh=[tuple(tuple(p) for p in g) for g in J['SH_shapes']]
    target1=((1,-2),(2,-4),(3,-6),(7,-8),(8,-9))
    target2=((1,-2),(3,-5))
    changed=[];lifted=[]
    for i,g in enumerate(bc):
        if g in (target1,target2):
            ng=tuple(sorted(set(g)|{(11,-11)}));lifted.append(ng);changed.append(i)
        else:lifted.append(g)
    if len(changed)!=2:raise SystemExit(f'expected exactly two boundary-sensitive BC shapes, found {changed}')
    P=[{'order':'n30t1','id':i,'s':r['s'],'rho':r['rho'],'a':13,'b':16,'dmax':11} for i,r in enumerate(N['records'])]
    st=time.time();M=co.build(P,lifted,sh);res=M.solve()
    out={'schema':'n30-boundary-lift-n29-fixed16-v1','profiles':len(P),'BC_count':len(lifted),'SH_count':len(sh),'support_count':len(lifted)+len(sh),'changed_BC_positions':changed,'added_endpoint':[11,-11],'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.success else None,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st,'floating_point_reconnaissance_only':True,'interpretation':'Only the two dmax-sensitive BC shapes are lifted by adding (11,-11); all other n29 exact16 shapes are unchanged, with fresh common n30 weights.'}
    out['BC_shapes']=[[list(p) for p in g] for g in lifted];out['SH_shapes']=[[list(p) for p in g] for g in sh]
    if res.success:
        out['BC_weights']=[float(res.x[M.idx[('BC',i)]]) for i in range(len(lifted))];out['SH_weights']=[float(res.x[M.idx[('SH',i)]]) for i in range(len(sh))]
        out['active_BC']=[i for i in range(len(lifted)) if res.x[M.idx[('BC',i)]]>1e-8];out['active_SH']=[i for i in range(len(sh)) if res.x[M.idx[('SH',i)]]>1e-8]
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('BC_shapes','SH_shapes','BC_weights','SH_weights')},indent=2,sort_keys=True))
if __name__=='__main__':main()
