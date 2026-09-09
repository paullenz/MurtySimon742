#!/usr/bin/env python3
"""Decode threshold/equality families in exact n29 pairwise correction certificates.

Rebuilds each of the 38 saved correction models from committed s/rho, the saved
specialised base support, and the recorded generated cuts. Recomputes an exact
integer Farkas certificate, then reports which original source threshold rows
h=1..a and which structural equalities carry nonzero multipliers.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
from collections import Counter
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('cm',HERE/'n29_pairwise_correction_miner.py');cm=module_from_spec(sp);sp.loader.exec_module(cm);cg=cm.cg;ex=cm.ex

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--correction-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();C=json.loads(z.correction_json.read_text())
    basebc=[tuple(tuple(p) for p in g) for g in C['base_support']['BC']];basesh=[tuple(tuple(p) for p in g) for g in C['base_support']['SH']];outrec=[];threshold_profile_counts=Counter();threshold_total_weight=Counter()
    for old in C['records']:
        m,sources,labels=cg.build_master(z.a,z.b,z.dmax,old['s'],old['rho'])
        for g in basebc:m.le(cm.shape_row(sources,labels,g,'BC'),0)
        for g in basesh:m.le(cm.shape_row(sources,labels,g,'SH'),0)
        for c in old['cuts']:
            g=tuple(tuple(p) for p in c['generators']);m.le(cm.shape_row(sources,labels,g,c['family']),0)
        before_bounds=len(m.ub);ex.add_unit_density_bounds(m);cert=ex.exact_certificate(m)
        if cert is None:raise RuntimeError(('lost exact certificate',old['hard_position']))
        ubw=dict(cert['ub']);eqw=dict(cert['eq']);th=[]
        for i in range(z.a):
            w=ubw.get(i,0)
            if w:th.append({'h':i+1,'weight':w});threshold_profile_counts[i+1]+=1;threshold_total_weight[i+1]+=w
        sg=len(sorted(Counter(old['rho']).items()));lg=len(sorted(Counter(old['s']).items()));qbal=sg;lnorm_start=sg+1;Ridx=lnorm_start+lg;H0idx=Ridx+1
        eqsem={'q_minus_p':eqw.get(qbal,0),'R_total':eqw.get(Ridx,0),'H0_incidence':eqw.get(H0idx,0)}
        outrec.append({'hard_position':old['hard_position'],'demand_id':old['demand_id'],'thresholds':th,'threshold_count':len(th),'structural_equalities':eqsem,'unit_bound_rows_active':sum(i>=before_bounds for i,w in cert['ub'] if w),'certificate_rhs':cert['rhs']})
    out={'schema':'n29-pairwise-semantic-threshold-decode-v1','profiles':len(outrec),'threshold_profile_counts':{str(h):threshold_profile_counts[h] for h in sorted(threshold_profile_counts)},'threshold_total_weights':{str(h):threshold_total_weight[h] for h in sorted(threshold_total_weight)},'records':outrec,'integer_farkas_acceptance':True,'interpretation':'Threshold rows are the original source threshold-transport inequalities in build_master, before any Hall/base rows. Certificates are recomputed and verified exactly.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2,sort_keys=True));print('position0',json.dumps(outrec[0],indent=2,sort_keys=True))
if __name__=='__main__':main()
