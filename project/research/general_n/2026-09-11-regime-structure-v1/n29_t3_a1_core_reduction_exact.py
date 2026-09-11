#!/usr/bin/env python3
"""Transparent exact reduction to the 11-profile n=29,t=3 A1 cell.

Starting assumptions only:
  * 12 positive integer demand degrees 1..11;
  * the exact charging inequality in the n=29, Delta=16, t=3 setup;
  * 16 positive residual degrees 1..12;
  * zero slack: sum(s)=sum(rho)+6;
  * h_res(rho)=4;
  * J=2#{rho>=2}-#{s=1}=14;
  * the scalar supplement-cutoff lemma q*_u=min(C_u,L);
  * total selected-incidence capacity and largest-demand-prefix Hall bounds.

No demand dual, threshold certificate, C++ scanner, LP/MIP solver, floating point,
or pre-saved frontier list is used to produce the 11 survivors. The final list
is only compared with the independently regenerated audited frontier.
"""
from __future__ import annotations
from argparse import ArgumentParser
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations_with_replacement
from pathlib import Path
import importlib.util,json

A=12;B=16;T=3

def load_module(path:Path):
 spec=importlib.util.spec_from_file_location('cover',path)
 m=importlib.util.module_from_spec(spec);assert spec.loader is not None
 spec.loader.exec_module(m);return m

def h_res(rho):
 h=0
 for k,x in enumerate(sorted(rho,reverse=True),1):
  if x>=k:h=k
  else:break
 return h

def charging_score(s):
 # Equivalent to r>=b+sum s(s-1)/(a-s) after substituting r=sum(s)-2t.
 return sum((Q(x*(A+1-2*x),A-x) for x in s),Q())

def demand_profiles():
 for s in combinations_with_replacement(range(1,A),A):
  if charging_score(s)>=B+2*T:
   yield s

@lru_cache(None)
def residual_options(z2:int,total_nonunit:int):
 out=[]
 for vals in combinations_with_replacement(range(2,A+1),z2):
  if sum(vals)!=total_nonunit:continue
  rho=(1,)*(B-z2)+vals
  if h_res(rho)==4:out.append(rho)
 return tuple(out)

def scalar_cutoff(s,rho):
 C=[min(A-r,sum(x<=r for x in s)) for r in rho]
 K=max(C,default=0);scores=[r+c for r,c in zip(rho,C)]
 good=[k for k in range(1,K+1) if sum(z>=k-1 for z in scores)>=k+1]
 L=max(good) if good else 0
 return L,[min(c,L) for c in C]

def first_hall_failure(s,rho,cap):
 if sum(cap)<sum(s):return ('total',0,sum(s),sum(cap))
 ss=sorted(s)
 for k in range(1,A+1):
  P=ss[A-k:];need=sum(P)
  supply=sum(min(cap[u],sum(x<=rho[u] for x in P)) for u in range(B))
  if supply<need:return ('prefix',k,need,supply)
 return None

def histkey(s,rho):
 sc=Counter(s);rc=Counter(rho)
 return (tuple(sc.get(i,0) for i in range(1,A)),tuple(rc.get(i,0) for i in range(1,A+1)))

def main():
 ap=ArgumentParser();ap.add_argument('--cover-script',type=Path,required=True);ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
 broad=0;d1_broad=Counter();total_rej=Counter();prefix_rej=Counter();survivors=[];prefix_k=Counter()
 for s in demand_profiles():
  d1=s.count(1)
  if (14+d1)%2:continue
  z2=(14+d1)//2
  if not 0<=z2<=B:continue
  rho1=B-z2;R=sum(s)-2*T
  if R<rho1+2*z2:continue
  for rho in residual_options(z2,R-rho1):
   # J is automatic from z2 choice; zero slack and h=4 are automatic here.
   broad+=1;d1_broad[d1]+=1
   L,cap=scalar_cutoff(s,rho);fail=first_hall_failure(s,rho,cap)
   if fail is None:
    survivors.append({'s':list(s),'rho':list(rho),'L':L,'key':histkey(s,rho)})
   elif fail[0]=='total':total_rej[d1]+=1
   else:
    prefix_rej[d1]+=1;prefix_k[(d1,fail[1])]+=1
 if broad!=236885:raise AssertionError(('broad',broad))
 if dict(d1_broad)!={0:220966,2:15907,4:12}:raise AssertionError(('d1_broad',d1_broad))
 if sum(total_rej.values())!=226990 or sum(prefix_rej.values())!=9884:raise AssertionError((total_rej,prefix_rej))
 if len(survivors)!=11:raise AssertionError(('survivors',len(survivors)))
 if any(Counter(p['s']).keys()-{2,3,4} for p in survivors):raise AssertionError('demand support')
 if any(Counter(p['rho']).keys()-{1,3,4,5,6} for p in survivors):raise AssertionError('rho support')
 if any(p['s'].count(1)!=0 or p['rho'].count(1)!=9 or p['L']!=6 for p in survivors):raise AssertionError('survivor invariants')
 # Compare only after deriving the survivor set independently.
 mod=load_module(z.cover_script);P=mod.load(z.demands_json,z.rows);actual=[]
 for p in P:
  J=2*sum(r>=2 for r in p['rho'])-p['s'].count(1)
  if h_res(p['rho'])==4 and J==14:actual.append(histkey(p['s'],p['rho']))
 derived={p['key'] for p in survivors}
 if len(actual)!=11 or derived!=set(actual):raise AssertionError(('frontier_compare',len(actual),derived-set(actual),set(actual)-derived))
 hist=[]
 for p in survivors:
  sc=Counter(p['s']);rc=Counter(p['rho'])
  hist.append({'s_hist':[[k,sc[k]] for k in sorted(sc)],'rho_hist':[[k,rc[k]] for k in sorted(rc)],'L':p['L']})
 out={'schema':'n29-t3-a1-core-reduction-exact-v1','status':'PASS','starting_conditions':['positive demand degrees','charging inequality','positive residual degrees','zero slack','h_res=4','J=14','scalar supplement cutoff','total-incidence capacity','largest-demand-prefix Hall'],'broad_histogram_pairs':broad,'broad_D1_census':{str(k):v for k,v in sorted(d1_broad.items())},'total_capacity_rejections':sum(total_rej.values()),'total_capacity_rejections_by_D1':{str(k):v for k,v in sorted(total_rej.items())},'prefix_hall_rejections':sum(prefix_rej.values()),'prefix_hall_rejections_by_D1':{str(k):v for k,v in sorted(prefix_rej.items())},'prefix_failure_census':{f'D1={d1},k={k}':v for (d1,k),v in sorted(prefix_k.items())},'survivors':len(survivors),'survivor_support_s':[2,3,4],'survivor_support_rho':[1,3,4,5,6],'survivor_rho1':9,'survivor_scalar_cutoff_L':6,'derived_survivors_equal_regenerated_A1_cell':True,'survivor_histograms':hist,'uses_demand_dual':False,'uses_threshold_certificate':False,'uses_cpp_scanner':False,'solver_used':False,'floating_point_used':False,'arithmetic':'fractions.Fraction exact rational','interpretation':'The 11-profile A1 support class is recovered from a small transparent necessary-condition package, independently of the older demand dual and residual-row scanner. Combined with n29_t3_a1_slack_identity_exact.py, this gives a short finite lemma chain for the entire (h,J)=(4,14) regime. The remaining general-N issue is parameterising these inequalities rather than enumerating order 29.'}
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':'PASS','broad':broad,'total_rej':sum(total_rej.values()),'prefix_rej':sum(prefix_rej.values()),'survivors':len(survivors),'D1':dict(d1_broad),'prefix_k':{str(k):v for k,v in sorted(prefix_k.items())}},indent=2,sort_keys=True))
if __name__=='__main__':main()
