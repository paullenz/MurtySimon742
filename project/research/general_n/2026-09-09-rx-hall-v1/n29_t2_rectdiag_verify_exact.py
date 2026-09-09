#!/usr/bin/env python3
"""Independent arithmetic replay for n29_t2_rectdiag_exactify output.

Rebuilds the fixed-support LP, reads the committed integer numerators, and checks
all row inequalities, nonnegativity/fixed-zero bounds and 38 scaled margins using
Python integer arithmetic. Does not call the exactifier's repair/check routines.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('rd',HERE/'n29_t2_rectdiag_sparse_scan.py');rd=module_from_spec(sp);sp.loader.exec_module(rd)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--exact-json',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    E=json.loads(z.exact_json.read_text());B=json.loads(z.boundary_json.read_text())
    if E.get('status')!='PASS':raise SystemExit('exact source is not PASS')
    support={(int(q['D']),int(q['V'])) for q in E['rectangles']};scale=int(E['denominator_scale']);nums=E['integer_numerators']
    P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['trimmed_survivor_records']]
    M,rect,diag=rd.build(P,12,16,10,True)
    for D,V,w in rect:
        if (D,V) not in support:M.bounds[w]=(0,0)
    X=[];missing=[]
    for name in M.names:
        k=str(name)
        if k not in nums:missing.append(k);X.append(0)
        else:X.append(int(nums[k]))
    violations=[];margin_values=[];zero_max=None
    for i,(row,rhs) in enumerate(zip(M.rows,M.rhs)):
        lhs=sum(int(c)*X[j] for j,c in row.items());target=0 if rhs==0 else -scale
        if lhs>target:violations.append({'row':i,'lhs':lhs,'target':target})
        if rhs==0:zero_max=lhs if zero_max is None else max(zero_max,lhs)
        else:margin_values.append(lhs)
    boundviol=[]
    for j,(lo,hi) in enumerate(M.bounds):
        if lo is not None and X[j] < int(round(lo*scale)):boundviol.append({'var':str(M.names[j]),'side':'lo','value':X[j],'target':int(round(lo*scale))})
        if hi is not None and X[j] > int(round(hi*scale)):boundviol.append({'var':str(M.names[j]),'side':'hi','value':X[j],'target':int(round(hi*scale))})
    passflag=(not missing and not violations and not boundviol and len(margin_values)==38 and max(margin_values)<=-scale)
    out={'schema':'n29-t2-rectdiag-independent-replay-v1','status':'PASS' if passflag else 'FAIL','profiles':len(P),'rows':len(M.rows),'variables':len(M.names),'rectangle_count':len(support),'generator_count':len(support)+1,'scale':scale,'missing_variables':missing[:20],'row_violation_count':len(violations),'row_violations':violations[:20],'bound_violation_count':len(boundviol),'bound_violations':boundviol[:20],'zero_rhs_max_lhs':zero_max,'margin_count':len(margin_values),'worst_margin_numerator':max(margin_values) if margin_values else None,'required_margin_numerator':-scale,'integer_arithmetic_only':True,'interpretation':'Independent arithmetic replay of the fixed finite rectdiag certificate. Same state-model constructor is reused, but certificate checking code is separate from the exactifier.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
    if not passflag:raise SystemExit(1)
if __name__=='__main__':main()
