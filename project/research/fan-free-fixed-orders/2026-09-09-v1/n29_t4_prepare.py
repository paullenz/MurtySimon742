#!/usr/bin/env python3
"""Fan-free n29 Delta16 t=4 preparation using frozen minimal_prepare mathematics.

This wrapper imports the frozen functions but removes only the historical CLI
restriction choices=[2,3]. No formula is changed.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
ROOT=Path(__file__).resolve().parents[4]
p=ROOT/'project/reviews/n29/2026-09-08-redteam-restart-v1/minimal_prepare.py'
sp=spec_from_file_location('base',p);base=module_from_spec(sp);sp.loader.exec_module(base)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    a,b,t=12,16,4;z.output.mkdir(parents=True,exist_ok=True)
    counts={};kept=[];domain=0
    for s in base.demands(a,b,t):
        domain+=1;lo,hi=base.bounds(s,b,t);rec={'s':s,'rmin':lo,'rmax':hi}
        if lo>hi: cert={'kind':'bounds'}
        else: cert=base.threshold_certificate(s,b,hi) or base.dual_certificate(s,b,hi) or {'kind':'OPEN'}
        counts[cert['kind']]=counts.get(cert['kind'],0)+1
        if cert['kind']=='OPEN':kept.append(rec)
    (z.output/'demands.json').write_text(json.dumps(kept,separators=(',',':'))+'\n')
    (z.output/'demands.txt').write_text(str(len(kept))+'\n'+''.join(' '.join(map(str,r['s']+[r['rmin'],r['rmax']]))+'\n' for r in kept))
    rep={'schema':'fan-free-n29-t4-minimal-demand-v1','scope':{'n':29,'Delta':16,'m':212,'a':a,'b':b,'t':t},'demand_domain':domain,'counts':counts,'retained_demands':len(kept),'frozen_function_source':str(p.relative_to(ROOT)),'formula_changes':False,'cli_restriction_removed':True,'all_nontrivial_saved_cuts_exactly_checked':True}
    (z.output/'MINIMAL_PREPARE_REPORT.json').write_text(json.dumps(rep,indent=2)+'\n');print(json.dumps(rep))
if __name__=='__main__':main()
