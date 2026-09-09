#!/usr/bin/env python3
"""Resolve support complexity inside the n29 H0=4 layer by demand signature.

The Hmax scan shows all 16-shape complexity is concentrated at max(s)=4.
This script groups those profiles by exact demand vector s (equivalently the
retained demand_id here) and solves a minimum-support MILP for each group using
the 25-shape active common library. Floating reconnaissance only.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
from collections import Counter
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('hs',HERE/'n29_hmax_support_scan.py');hs=module_from_spec(sp);sp.loader.exec_module(hs)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--common-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--big-m',type=float,default=200);ap.add_argument('--time-limit',type=float,default=90);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();B=json.loads(z.boundary_json.read_text());J=json.loads(z.common_json.read_text());q=J['modes']['full'];bc=[tuple(tuple(p) for p in g) for g in q['active_BC_shapes']];sh=[tuple(tuple(p) for p in g) for g in q['active_SH_shapes']]
    raw=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['trimmed_survivor_records'] if max(r['s'])==4]
    groups={}
    for p in raw: groups.setdefault(tuple(p['s']),[]).append(p)
    results=[]
    for sig,P in sorted(groups.items(),key=lambda kv:(sum(kv[0]),kv[0])):
        m=hs.solve(P,bc,sh,z.a,z.b,z.dmax,z.big_m,z.time_limit)
        results.append({'s':list(sig),'S':sum(sig),'demand_id':P[0]['demand_id'],'profiles':len(P),'minimum':m})
    out={'schema':'n29-h4-demand-signature-support-v1','H0':4,'profiles':len(raw),'signatures':len(results),'candidate_BC':len(bc),'candidate_SH':len(sh),'floating_point_reconnaissance_only':True,'results':results,'interpretation':'Minimum support separately for each exact H0=4 demand signature. Distinguishes a single hard signature from complexity caused by common coverage across signatures.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps([{'demand_id':r['demand_id'],'profiles':r['profiles'],'S':r['S'],'support':r['minimum'].get('support_count'),'BC':r['minimum'].get('BC_count'),'SH':r['minimum'].get('SH_count'),'gap':r['minimum'].get('mip_gap')} for r in results],indent=2))
if __name__=='__main__':main()
