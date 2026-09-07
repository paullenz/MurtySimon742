#!/usr/bin/env python3
"""Replay stored certificates by default; --full also re-runs discovery/tests."""
import argparse,json,subprocess,sys,hashlib,platform
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--full',action='store_true');args=parser.parse_args()
    if args.full:
        subprocess.run([sys.executable,'run_experiments.py'],cwd=ROOT,check=True)
        subprocess.run([sys.executable,'family.py'],cwd=ROOT,check=True)
        from family import degree_family
        from pair_engine import prepare,legacy_tests,support_certificate,degree_budget_closure,check_degree_closure,degree_budget_certificate,find_weighted_certificate
        rows=[]
        for s in [1,2,3,4]:
            p=degree_family(s);data=prepare(p);old=legacy_tests(data)
            assert all(old.values()) and support_certificate(data) is None
            cert=degree_budget_closure(data);assert cert and check_degree_closure(p,cert)
            rows.append(dict(s=s,n=40*s+4,delta=20*s+3,edges=(40*s+4)**2//4+1,
                       legacy_tests=old,supplement_support_pass=True,closure=cert))
        (ROOT/'DEGREE_FAMILY_TESTS.json').write_text(json.dumps(dict(status='PASS',scope='Four explicit representatives; general proof in PROOF.md',rows=rows),indent=2)+'\n')
        p=dict(name='n64_retained_pattern_not_a_graph',a=30,b=33,t=2,d=[15]*4+[16]*26,R=[7]*4+[8]*26,rho=[1]*4+[8]*29)
        v=prepare(p)
        row=dict(profile=p,legacy_tests=legacy_tests(v),support_certificate=support_certificate(v),degree_closure_certificate=degree_budget_closure(v),degree_budget_certificate=degree_budget_certificate(v),weighted_certificate=find_weighted_certificate(v),status='RETAINED BY THESE TESTS ONLY; not a graph, counterexample, or infeasibility claim')
        (ROOT/'FRONTIER.json').write_text(json.dumps(row,indent=2)+'\n')
        subprocess.run([sys.executable,'validate_graphs.py'],cwd=ROOT,check=True)
    subprocess.run([sys.executable,'check_pack.py'],cwd=ROOT,check=True)
if __name__=='__main__':main()
