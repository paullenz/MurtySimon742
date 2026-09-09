#!/usr/bin/env python3
"""Fan-free demand preparation for n=28, Delta=15, m=198 or 199.

Uses the established strengthened preparation formulas parameterized to A=12,
B=15.  The imported functions read A/B dynamically; no frozen source is edited.
All nontrivial dual lower bounds are accepted only after Fraction checks in the
imported implementation.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
ROOT=Path(__file__).resolve().parents[4]
p=ROOT/'project/research/n30/2026-09-08-minimal-kernel-recon-v1/n30_prepare.py'
sp=spec_from_file_location('base',p);base=module_from_spec(sp);sp.loader.exec_module(base)
base.N=28;base.A=12;base.B=15

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--m',type=int,choices=[198,199],required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    t=z.m-15*(28-15);z.output.mkdir(parents=True,exist_ok=True)
    counts={'domain':0,'basic_empty':0,'threshold_empty':0,'dual_empty':0,'retained':0};kept=[]
    for s in base.demands(t):
        counts['domain']+=1;lo,hi=base.basic_bounds(s,t)
        if lo>hi:counts['basic_empty']+=1;continue
        tl=base.threshold_min_r(s)
        if tl is None or tl>hi:counts['threshold_empty']+=1;continue
        score=base.dual_bound(s);dlo=base.B+(score.numerator+score.denominator-1)//score.denominator
        lo=max(lo,tl,dlo)
        if lo>hi:counts['dual_empty']+=1;continue
        kept.append((s,lo,hi));counts['retained']+=1
    with open(z.output/'demands.txt','w') as f:
        f.write(str(len(kept))+'\n')
        for s,lo,hi in kept:f.write(' '.join(map(str,(*s,lo,hi)))+'\n')
    rep={'schema':'fan-free-n28-d15-prepare-v1','scope':{'n':28,'Delta':15,'m':z.m,'a':12,'b':15,'t':t},'counts':counts,'retained':len(kept),'uses_deltaC_positive':True,'dual_lower_bounds_exactly_checked':True,'frozen_source_modified':False,'parameterized_source':str(p.relative_to(ROOT))}
    (z.output/'PREPARE_REPORT.json').write_text(json.dumps(rep,indent=2,sort_keys=True)+'\n');print(json.dumps(rep,sort_keys=True))
if __name__=='__main__':main()
