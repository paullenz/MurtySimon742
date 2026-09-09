#!/usr/bin/env python3
"""Fan-free early-kernel closure for n=30, Delta=16, m=231..240."""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
ROOT=Path(__file__).resolve().parents[4]
p=ROOT/'project/research/n30/2026-09-09-delta17-v1/delta17_kernel.py'
sp=spec_from_file_location('base',p); base=module_from_spec(sp); sp.loader.exec_module(base)
base.A=13;base.B=16

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    results={}
    for m in range(231,241):
        t=m-16*(30-16)
        rec=base.run_scope(t)
        assert rec['final_survivors']==0,(m,rec['opens'])
        results[str(m)]={k:v for k,v in rec.items() if k not in ('duals','opens')}
        results[str(m)]['exact_dual_count']=len(rec['duals'])
    out={'schema':'fan-free-n30-d16-upper-early-v1','n':30,'Delta':16,'a':13,'b':16,
         'results':results,'all_final_survivors_zero':True,
         'dual_acceptance':'exact integer/rational checks inside established source-capacity implementation',
         'status':'candidate fixed-order proof component; independent review open'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,sort_keys=True))
if __name__=='__main__':main()
