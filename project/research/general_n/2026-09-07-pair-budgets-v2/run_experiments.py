#!/usr/bin/env python3
import json,sys,platform
from pathlib import Path
from pair_engine import *
BASE=Path(__file__).resolve().parent
p64=dict(name='n64_counterexample_level_relaxation',a=30,b=33,t=8,
 d=[10]*22+[11]*8,R=[4]*4+[5]*26,rho=[2]*13+[6]*20)
p44=dict(name='n44_counterexample_level_relaxation',a=20,b=23,t=2,
 d=[6]*6+[7]*14,R=[3]*15+[4]*5,rho=[1]*9+[4]*14)
results=[]
for p in [p64,p44]:
 data=prepare(p)
 print(p['name'], 'r',data['r'],'demand',sum(data['demand']),'triples',len(data['triples']),'pairs',len(data['pairs']),flush=True)
 old=legacy_tests(data)
 print('legacy',old,flush=True)
 cert=support_certificate(data)
 if cert: assert check_support(p,cert)
 weighted=find_weighted_certificate(data)
 if weighted: assert check_weighted(p,weighted)
 rec=dict(profile=p,legacy_tests=old,support_certificate=cert,weighted_certificate=weighted,
          caps=data['caps'],incoming_caps=data['incoming_caps'],permitted_pairs=len(data['pairs']),
          degree_budget_certificate=degree_budget_certificate(data),
          degree_closure_certificate=degree_budget_closure(data))
 if not cert and not weighted:
  rec['integer_witness']=find_integer_witness(data,15)
  print('witness',rec['integer_witness']['status'],flush=True)
 results.append(rec)
 print('support',cert,'weighted?',bool(weighted),flush=True)
report=dict(date='2026-09-07',environment=dict(python=platform.python_version()),
 status='candidate graph lemmas; exact profile certificate checks; external review OPEN',
 scope='Two deliberately constructed test profiles. NOT an exhaustive order scan.',results=results)
(BASE/'EXPERIMENTS.json').write_text(json.dumps(report,indent=2)+'\n')
