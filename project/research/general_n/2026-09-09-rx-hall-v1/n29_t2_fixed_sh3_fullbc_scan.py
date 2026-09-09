#!/usr/bin/env python3
"""Test selected 3-SH supports across all 902 n29 t=2 profiles with full BC.

The canonical 75 BC shapes are all available. SH is fixed to one of the two
zero-gap 3-shape supports found by the hard38 minimum-SH scan (M200 or M1000).
One common BC/SH weight vector is required across all 902 t=2 profiles; scalar
dual bookkeeping remains profile-specific. Floating reconnaissance only.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('cp',HERE/'n29_common_potential_profile_scalars.py');cp=module_from_spec(sp);sp.loader.exec_module(cp)
sp2=spec_from_file_location('ex',HERE/'n29_all_t23_exactify.py');ex=module_from_spec(sp2);sp2.loader.exec_module(ex)

def tup(g):return tuple(tuple(p) for p in g)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--dictionary-json',type=Path,required=True);ap.add_argument('--min-sh-json',type=Path,required=True);ap.add_argument('--candidate',choices=['M200','M1000'],required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    P=ex.load(z.demands,z.rows,2);D=json.loads(z.dictionary_json.read_text());S=json.loads(z.min_sh_json.read_text());bc=[tup(x['generators']) for x in D['BC']];allsh=[tup(x['generators']) for x in D['SH']]
    key='M200' if z.candidate=='M200' else 'M1000_validation';idx=list(S[key]['active_SH_indices']);sh=[allsh[i] for i in idx]
    st=time.time();M=cp.build(P,bc,sh,12,16,10);res=M.solve()
    out={'schema':'n29-t2-fixed-sh3-fullbc-v1','candidate':z.candidate,'profiles':len(P),'BC_count':len(bc),'SH_indices':idx,'SH_count':len(sh),'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.success else None,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st,'floating_point_reconnaissance_only':True,'interpretation':'All 75 canonical BC shapes are available. SH is fixed to one hard38-minimal three-shape support. One common staircase-weight vector spans all 902 t=2 profiles if success=true.'}
    if res.success:
        ab=[i for i in range(len(bc)) if res.x[M.idx[('BC',i)]]>1e-8];out['active_BC_indices']=ab;out['active_BC_count']=len(ab);out['BC_weights']=[float(res.x[M.idx[('BC',i)]]) for i in ab];out['SH_weights']=[float(res.x[M.idx[('SH',i)]]) for i in range(len(sh))]
        out['SH_shapes']=[[list(p) for p in g] for g in sh]
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('BC_weights','SH_weights','SH_shapes')},indent=2,sort_keys=True))
if __name__=='__main__':main()
