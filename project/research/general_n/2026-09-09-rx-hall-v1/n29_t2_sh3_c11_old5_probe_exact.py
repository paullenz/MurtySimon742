#!/usr/bin/env python3
"""Exact probe: reuse the five rational scalar templates from the earlier
16-generator n=29,t=2 certificate against the new exact 11-term 3-D potential.

No LP/MIP solver participates in this checker.  It evaluates exact Fraction
envelopes for all 902 regenerated profiles.  This is a compression probe: PASS
only means the union of these fixed templates covers all profiles under the new
potential; partial coverage is still useful reconnaissance but not a complete
certificate by itself.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import argparse,json

BC={(3,6):3,(3,7):3,(3,8):3,(3,9):3,(3,10):4,(3,11):4,(3,12):4,(3,13):4}
J={14:8,16:7};SH3=29
TEMPLATES={
 'A0':{'lambda':Q(32),'c':Q(9),'mu+':Q(97,3),'tau2':Q(23,4),'tau3':Q(17,3),'tau4':Q(25,2)},
 'A1':{'lambda':Q(32),'c':Q(71,4),'mu+':Q(15,2),'tau3':Q(232,7),'tau5':Q(17,2),'tau6':Q(3)},
 'A79':{'lambda':Q(394,13),'c':Q(44),'tau2':Q(532,13),'tau3':Q(13),'tau4':Q(99,7)},
 'A82':{'c':Q(209,3),'tau2':Q(424,9),'tau3':Q(115,4)},
 'A94':{'lambda':Q(32),'c':Q(263,6),'tau2':Q(335,6),'tau3':Q(37,4),'tau5':Q(13,6),'tau7':Q(14,5)},
}

def phi(d,h,scoord):
 v=16-h;ans=0
 for (D,V),w in BC.items():
  if d>=D and v>=V:ans+=w
 for K,w in J.items():
  if d+v>=K:ans+=w
 if scoord>=3:ans+=SH3
 return Q(ans)
def tterm(r,q,p,j):return (q if q>=j+1 else 0)-(p if r+q>=j else 0)
def load(dp,rp):
 D=json.loads(Path(dp).read_text());out=[]
 for line in Path(rp).read_text().splitlines():
  if not line.strip():continue
  z=list(map(int,line.split()));did=z[0];rho=z[2:];s=D[did]['s']
  if min(s)>0 and sum(s)==sum(rho)+4:out.append({'s':s,'rho':rho,'demand_id':did})
 return out
def rat(x):return [x.numerator,x.denominator]

def cover(P,th):
 lam=th.get('lambda',Q(0));c=th.get('c',Q(0));mp=th.get('mu+',Q(0));mm=th.get('mu-',Q(0));taus={j:th.get(f'tau{j}',Q(0)) for j in range(1,13)}
 gaps=[]
 for pf in P:
  ell={s:min(lam*R+c*x+x*phi(R+s,R+x,s) for R in range(10-s+1) for x in range(s,16-R+1)) for s in set(pf['s'])}
  sig={}
  for r in set(pf['rho']):
   qm=min(12-r,sum(si<=r for si in pf['s']))
   sig[r]=min(mp*(q-p)-mm*(q-p)-c*q+sum(taus[j]*tterm(r,q,p,j) for j in range(1,13))-q*phi(r+q-1,q+p,r)
              for q in range(qm+1) for p in range(min(r+3,15-q)+1))
  g=sum(n*ell[s] for s,n in Counter(pf['s']).items())+sum(n*sig[r] for r,n in Counter(pf['rho']).items())-lam*sum(pf['rho']);gaps.append(g)
 return gaps

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();P=load(z.demands_json,z.rows)
 if len(P)!=902:raise SystemExit(f'expected 902, got {len(P)}')
 masks={};summary={}
 for name,th in TEMPLATES.items():
  gaps=cover(P,th);mask=[g>0 for g in gaps];masks[name]=mask;pos=[g for g in gaps if g>0]
  summary[name]={'coverage':sum(mask),'minimum_positive_gap':rat(min(pos)) if pos else None,'covered_indices':[i for i,x in enumerate(mask) if x]}
 union=[any(masks[k][i] for k in masks) for i in range(902)];missing=[i for i,x in enumerate(union) if not x]
 out={'schema':'n29-t2-sh3-c11-old5-exact-probe-v1','status':'PASS_COVER' if not missing else 'PARTIAL','profiles':902,'covered':sum(union),'missing_count':len(missing),'missing_indices':missing,'templates':summary,'potential':'3B(3,6..9)+4B(3,10..13)+8J2+7J0+29SH3','exact_fraction_arithmetic':True,'uses_lp_solver':False,'interpretation':'Exact cross-test of the five old rational scalar templates under the new exact 11-term 3-D potential.'}
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='templates'},indent=2,sort_keys=True));print(json.dumps({k:{'coverage':v['coverage'],'minimum_positive_gap':v['minimum_positive_gap']} for k,v in summary.items()},indent=2,sort_keys=True))
if __name__=='__main__':main()
