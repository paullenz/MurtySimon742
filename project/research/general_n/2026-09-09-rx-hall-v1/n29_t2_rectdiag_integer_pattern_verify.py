#!/usr/bin/env python3
"""Independent integer replay of the hand-integer rectdiag ray certificate.

Reconstructs the hard38 model and global pins from the published normalized
pattern and accepted ray scale.  It does not reuse the exactifier's repair or
acceptance functions.  Logical acceptance is:
  * every homogeneous coefficient row has integer lhs <= 0;
  * every profile contradiction row has integer lhs < 0;
  * every nonnegative/fixed global bound is respected exactly.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('rd',HERE/'n29_t2_rectdiag_sparse_scan.py');rd=module_from_spec(sp);sp.loader.exec_module(rd)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--certificate-json',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    E=json.loads(z.certificate_json.read_text());B=json.loads(z.boundary_json.read_text())
    if E.get('status')!='PASS':raise SystemExit('certificate source is not PASS')
    C=int(E['accepted_ray_scale']);denom=int(E['accepted_denominator_scale']);nums=E['scaled_integer_numerators']
    pat={(int(q['D']),int(q['V'])):int(q['weight']) for q in E['normalized_rectangles']};jw=int(E['normalized_diagonal']['weight'])
    P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['trimmed_survivor_records']]
    M,rect,diag=rd.build(P,12,16,10,True)
    pin={}
    for D,V,w in rect:
        val=C*pat.get((D,V),0);M.bounds[w]=(val,val);pin[w]=val
    val=C*jw;M.bounds[diag]=(val,val);pin[diag]=val
    X=[];missing=[]
    for name in M.names:
        k=str(name)
        if k not in nums:missing.append(k);X.append(0)
        else:X.append(int(nums[k]))
    zviol=[];margins=[]
    for i,(row,rhs) in enumerate(zip(M.rows,M.rhs)):
        lhs=sum(int(c)*X[j] for j,c in row.items())
        if rhs==0:
            if lhs>0:zviol.append({'row':i,'lhs':lhs})
        else:margins.append({'row':i,'lhs_numerator':lhs})
    bviol=[]
    for j,(lo,hi) in enumerate(M.bounds):
        if j in pin:
            target=int(pin[j]*denom)
            if X[j]!=target:bviol.append({'var':str(M.names[j]),'side':'pin','value':X[j],'target':target})
        else:
            if lo is not None and X[j]<int(round(lo*denom)):bviol.append({'var':str(M.names[j]),'side':'lo','value':X[j],'target':int(round(lo*denom))})
            if hi is not None and X[j]>int(round(hi*denom)):bviol.append({'var':str(M.names[j]),'side':'hi','value':X[j],'target':int(round(hi*denom))})
    nonneg=[m for m in margins if m['lhs_numerator']>=0]
    passed=(not missing and not zviol and not bviol and len(margins)==38 and not nonneg)
    out={'schema':'n29-t2-rectdiag-integer-pattern-independent-replay-v1','status':'PASS' if passed else 'FAIL','profiles':len(P),'rows':len(M.rows),'variables':len(M.names),'generator_count':11,'accepted_ray_scale':C,'denominator_scale':denom,'missing_variable_count':len(missing),'missing_variables':missing[:20],'zero_row_violation_count':len(zviol),'zero_row_violations':zviol[:20],'bound_violation_count':len(bviol),'bound_violations':bviol[:20],'margin_count':len(margins),'nonnegative_margin_count':len(nonneg),'nonnegative_margins':nonneg[:20],'worst_margin_numerator':max((m['lhs_numerator'] for m in margins),default=None),'worst_normalized_margin':max((m['lhs_numerator'] for m in margins),default=0)/denom/C if margins else None,'integer_arithmetic_only':True,'same_state_model_constructor_reused':True,'exactifier_acceptance_code_reused':False,'interpretation':'PASS independently rechecks the published integer numerators against the reconstructed finite hard38 state model. It is not external review and does not establish support minimality.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
    if not passed:raise SystemExit(1)
if __name__=='__main__':main()
