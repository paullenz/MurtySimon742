#!/usr/bin/env python3
"""Independent integer replay for n29 t2 compact-potential certificates.

This script does not call the floating solver or the exactifier. It rebuilds the
finite model from the pinned profile inputs, reads the stored integer vector, and
checks every row, profile margin, and bound directly with Python integers.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,gzip,hashlib,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('base',HERE/'n29_t2_layer23_diag012_scan.py');base=module_from_spec(sp);sp.loader.exec_module(base)
sp2=spec_from_file_location('allx',HERE/'cross_order_all1003_fixed16.py');allx=module_from_spec(sp2);sp2.loader.exec_module(allx)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--certificate',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    raw=allx.load29(z.demands_json,z.rows,2);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
    with gzip.open(z.certificate,'rb') as f:C=json.loads(f.read())
    layers=tuple(C['layers']);scale=int(C['scale']);X=[int(v) for v in C['X']]
    M,rect,diag=base.build(P,layers=layers,steps=(14,15,16))
    errors=[];zero_max=None;margins=[]
    if len(X)!=len(M.names):errors.append(['vector_length',len(X),len(M.names)])
    else:
        for i,(row,rhs) in enumerate(zip(M.rows,M.rhs)):
            lhs=sum(int(c)*X[j] for j,c in row.items());target=0 if rhs==0 else int(rhs)*scale
            if lhs>target and len(errors)<20:errors.append(['row',i,lhs,target])
            if rhs==0:zero_max=lhs if zero_max is None else max(zero_max,lhs)
            else:margins.append(lhs)
        for j,(lo,hi) in enumerate(M.bounds):
            if lo is not None and X[j] < int(round(lo*scale)) and len(errors)<20:errors.append(['bound_lo',j,X[j],lo])
            if hi is not None and X[j] > int(round(hi*scale)) and len(errors)<20:errors.append(['bound_hi',j,X[j],hi])
    ok=(not errors and len(margins)==len(P) and max(margins)<=-scale)
    out={'schema':'n29-t2-compact-independent-replay-v1','status':'PASS' if ok else 'FAIL','profiles':len(P),'layers':list(layers),'scale':scale,'rows':len(M.rows),'variables':len(M.names),'certificate_sha256':hashlib.sha256(z.certificate.read_bytes()).hexdigest(),'integer_only':True,'floating_solver_used':False,'zero_rhs_max_lhs':zero_max,'worst_margin_numerator':max(margins) if margins else None,'required_margin_numerator':-scale,'errors':errors}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
    if not ok:raise SystemExit(1)
if __name__=='__main__':main()
