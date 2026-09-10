#!/usr/bin/env python3
"""Single-generator ablation inside the exact c02 D={2,3,4} n29,t2 support.

Floating falsification/pruning scan only. A successful deletion must be
re-exactified before promotion.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('base',HERE/'n29_t2_layer23_diag012_scan.py');base=module_from_spec(sp);sp.loader.exec_module(base)
RECT={(2,11),(2,12),(2,13),(2,14),(3,0),(3,2),(3,4),(3,5),(3,7),(3,8),(3,10),(3,12),(4,2),(4,3),(4,6),(4,9)}
DIAG={14,16}

def parse_drop(s):
    z=s.split(':')
    if z[0]=='r' and len(z)==3:return ('r',int(z[1]),int(z[2]))
    if z[0]=='j' and len(z)==2:return ('j',int(z[1]))
    raise SystemExit('drop must be r:D:V or j:K')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--drop',required=True);ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();drop=parse_drop(z.drop)
    raw=base.allx.load29(z.demands_json,z.rows,2);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
    M,rect,diag=base.build(P,layers=(2,3,4),steps=(14,16))
    for D,V,w in rect:
        if (D,V) not in RECT or drop==('r',D,V):M.bounds[w]=(0,0)
    for K,w in diag:
        if K not in DIAG or drop==('j',K):M.bounds[w]=(0,0)
    st=time.time();res=M.solve();sec=time.time()-st
    out={'schema':'n29-t2-c02-234-single-drop-v1','profiles':len(P),'base_nonzero_generator_count':18,'drop':z.drop,'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.success else None,'rows':len(M.rows),'variables':len(M.names),'solve_seconds':sec,'floating_point_reconnaissance_only':True}
    if res.success:
        ar,ad=base.extract(res,rect,diag);out['active_rectangles']=[{k:v for k,v in q.items() if k!='var'} for q in ar];out['active_diagonals']=[{k:v for k,v in q.items() if k!='var'} for q in ad];out['active_generator_count']=len(ar)+len(ad)
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('active_rectangles','active_diagonals')},indent=2,sort_keys=True))
if __name__=='__main__':main()
