#!/usr/bin/env python3
"""Exact four-template compression for n=29,t=3 with F=6B(3,0)+4B(3,5)+3B(3,9).

Start from exact A0,A1,A38 and replace separate A5/A30 by one rational template
rationalised from the common-scalar LP on profiles {5,30}.  Acceptance uses only
Fraction arithmetic and exhaustive finite envelope minima; no solver.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import argparse,json
W={(3,0):6,(3,5):4,(3,9):3}
TEMPLATES={
 'A0': {'lambda':Q(140,81),'tau3':Q(29,12),'tau4':Q(23,12)},
 'A1': {'lambda':Q(9,5),'c':Q(16,3),'tau2':Q(23,3)},
 'A38':{'lambda':Q(9,5),'c':Q(141,70),'tau2':Q(841,210),'tau3':Q(1682,1155)},
 'A530':{'lambda':Q(9,5),'c':Q(103,144),'tau2':Q(1513,720),'tau3':Q(3101,1440),'tau4':Q(109,144)},
}
def F(d,v):return sum(w for (D,V),w in W.items() if d>=D and v>=V)
def tterm(r,q,p,j):return (q if q>=j+1 else 0)-(p if r+q>=j else 0)
def rat(x):return [x.numerator,x.denominator]
def load(dp,rp):
 D=json.loads(Path(dp).read_text());out=[]
 for line in Path(rp).read_text().splitlines():
  if not line.strip():continue
  z=list(map(int,line.split()));did=z[0];rho=z[2:];s=D[did]['s']
  if min(s)>0 and sum(s)==sum(rho)+6:out.append({'s':s,'rho':rho,'demand_id':did})
 return out
def gaps_for(P,th):
 lam=th.get('lambda',Q(0));c=th.get('c',Q(0));mp=th.get('mu+',Q(0));mm=th.get('mu-',Q(0));taus={j:th.get(f'tau{j}',Q(0)) for j in range(1,13)}
 ell={s:min(lam*R+c*x+x*F(R+s,16-R-x) for R in range(10-s+1) for x in range(s,16-R+1)) for s in range(1,11)}
 gaps=[]
 for pf in P:
  sig={}
  for r in set(pf['rho']):
   qm=min(12-r,sum(si<=r for si in pf['s']))
   sig[r]=min(mp*(q-p)-mm*(q-p)-c*q+sum(taus[j]*tterm(r,q,p,j) for j in range(1,13))-q*F(r+q-1,16-q-p)
              for q in range(qm+1) for p in range(min(r+3,15-q)+1))
  g=sum(n*ell[s] for s,n in Counter(pf['s']).items())+sum(n*sig[r] for r,n in Counter(pf['rho']).items())-lam*sum(pf['rho']);gaps.append(g)
 return gaps
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();P=load(z.demands_json,z.rows)
 if len(P)!=94:raise SystemExit(f'expected 94 profiles, got {len(P)}')
 masks={};summ={}
 for name,th in TEMPLATES.items():
  gs=gaps_for(P,th);m=[g>0 for g in gs];masks[name]=m;pos=[g for g in gs if g>0]
  summ[name]={'coverage':sum(m),'covered_indices':[i for i,x in enumerate(m) if x],'minimum_positive_gap':rat(min(pos)) if pos else None,'gap_at_0':rat(gs[0]),'gap_at_5':rat(gs[5]),'gap_at_30':rat(gs[30]),'theta':{k:rat(v) for k,v in th.items()}}
 union=[any(masks[k][i] for k in masks) for i in range(94)];missing=[i for i,x in enumerate(union) if not x]
 unique={k:sorted(set(i for i,x in enumerate(masks[k]) if x)-set().union(*(set(i for i,x in enumerate(masks[j]) if x) for j in masks if j!=k))) for k in masks}
 out={'schema':'n29-t3-four-scalar-templates-exact-v1','status':'PASS' if not missing else 'FAIL','profiles':94,'covered':sum(union),'missing_indices':missing,'template_count':4,'templates':summ,'unique_coverage':unique,'primitive_potential':{'B(3,0)':6,'B(3,5)':4,'B(3,9)':3},'exact_fraction_arithmetic':True,'uses_lp_solver':False,'pair_template_provenance':{'floating_run_id':34497333867,'profiles':[5,30]},'interpretation':'Exact four-template compression succeeds iff missing_indices is empty. A530 was only discovered numerically; all acceptance here is direct rational arithmetic.'}
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
 if missing:raise SystemExit(1)
if __name__=='__main__':main()
