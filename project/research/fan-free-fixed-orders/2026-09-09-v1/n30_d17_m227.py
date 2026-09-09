#!/usr/bin/env python3
"""Fan-free closure of n=30, Delta=17, m=227 using the established early kernel."""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
ROOT=Path(__file__).resolve().parents[4]
p=ROOT/'project/research/n30/2026-09-09-delta17-v1/delta17_kernel.py'
sp=spec_from_file_location('d17',p); d17=module_from_spec(sp); sp.loader.exec_module(d17)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,required=True); z=ap.parse_args()
    rec=d17.run_scope(6) # m=227 gives t=227-17*13=6
    out={
      'schema':'fan-free-n30-d17-m227-v1','n':30,'Delta':17,'m':227,'a':12,'b':17,'t':6,
      'charging_feasible_profiles':rec['charging_feasible_profiles'],
      'counts':rec['counts'],'final_survivors':rec['final_survivors'],
      'minimum_threshold_margin':rec['minimum_threshold_margin'],
      'minimum_dual_margin':rec['minimum_dual_margin'],
      'duals':rec['duals'],'opens':rec['opens'],
      'uses_established_n30_d17_kernel':True,
      'all_duals_exact_integer_verified_during_generation':True,
      'status':'candidate fixed-order proof component; independent review open'
    }
    assert out['final_survivors']==0, out
    z.output.parent.mkdir(parents=True,exist_ok=True); z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('duals','opens')},sort_keys=True))
if __name__=='__main__':main()
