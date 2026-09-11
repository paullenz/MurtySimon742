#!/usr/bin/env python3
"""Exact verifier for the n=29,t=2 unit-demand regime partition.

For the fixed three exact rational scalar templates T0,T1,T2 already preserved
in n29_t2_sh3_c11_three_scalar_exact.py, assign by

  nu1 = #{i : s_i = 1}
  nu1=2 -> T0, nu1=1 -> T1, nu1=0 -> T2.

The script regenerates no certificates itself: it imports the exact Fraction
potential/template evaluator, recomputes every template gap, and requires the
assigned template to have strictly positive gap for every one of the 902
frontier profiles.  It also records exact minima and their witness profiles.
"""
from pathlib import Path
import argparse, importlib.util, json


def loadmod(path: Path):
    spec=importlib.util.spec_from_file_location('t2exact',path)
    mod=importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def rat(x): return [x.numerator,x.denominator]


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--demands-json',type=Path,required=True)
    ap.add_argument('--rows',type=Path,required=True)
    ap.add_argument('--exact-script',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    z=ap.parse_args()
    ex=loadmod(z.exact_script)
    P=ex.load(z.demands_json,z.rows)
    if len(P)!=902: raise SystemExit(f'expected 902 profiles, got {len(P)}')
    gaps={name:ex.gaps(P,th) for name,th in ex.TEMPLATES.items()}
    assign={0:'T2',1:'T1',2:'T0'}
    groups={0:[],1:[],2:[]}; bad=[]
    for i,pf in enumerate(P):
        nu1=pf['s'].count(1)
        if nu1 not in assign:
            bad.append({'index':i,'kind':'unexpected_nu1','nu1':nu1})
            continue
        name=assign[nu1];g=gaps[name][i];groups[nu1].append((i,g))
        if g<=0:bad.append({'index':i,'kind':'nonpositive_assigned_gap','nu1':nu1,'template':name,'gap':rat(g)})
    expected={0:825,1:76,2:1}
    outgroups={}
    for nu1,rows in groups.items():
        if len(rows)!=expected[nu1]:bad.append({'kind':'group_count','nu1':nu1,'got':len(rows),'expected':expected[nu1]})
        m=min(g for _,g in rows);ids=[i for i,g in rows if g==m]
        outgroups[str(nu1)]={
          'template':assign[nu1],
          'profiles':len(rows),
          'minimum_assigned_gap':rat(m),
          'minimum_gap_profile_indices':ids,
          'minimum_gap_profiles':[{'index':i,'demand_id':P[i]['demand_id'],'s':P[i]['s'],'rho':P[i]['rho']} for i in ids],
        }
    out={
      'schema':'n29-t2-unit-demand-regime-exact-v1',
      'status':'PASS' if not bad else 'FAIL',
      'profiles':len(P),
      'regime_statistic':'nu1 = count(s_i == 1)',
      'assignment':{'0':'T2','1':'T1','2':'T0'},
      'groups':outgroups,
      'bad':bad,
      'exact_fraction_arithmetic':True,
      'uses_lp_solver':False,
      'floating_point_used':False,
      'interpretation':'All 902 regenerated n29,t2 frontier profiles are exactly assigned to one of the three already-exact rational templates using only nu1=count(s_i=1).',
    }
    z.output.parent.mkdir(parents=True,exist_ok=True)
    z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
    if bad:raise SystemExit(1)

if __name__=='__main__':main()
