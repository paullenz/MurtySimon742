#!/usr/bin/env python3
"""Exact five-template cover for all 902 n=29,t=2 RX-Hall frontier profiles.

No LP solver is used.  The script fixes the primitive 16-term integer potential
and five small rational scalar templates.  For each template it evaluates every
label/source envelope by exhaustive finite minimisation with Fraction arithmetic,
then checks which profiles have strict positive potential-certificate gap.  PASS
requires the union of the five exact covers to be all 902 profiles.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import argparse,json

W={(2,11):11,(2,12):12,(2,13):28,(2,14):8,
   (3,0):41,(3,4):8,(3,7):8,(3,8):8,(3,10):11,(3,12):5,
   (4,2):5,(4,3):5,(4,6):6,(4,9):8}
TEMPLATES={
 'A0':{'lambda':Q(32),'c':Q(9),'mu+':Q(97,3),'tau2':Q(23,4),'tau3':Q(17,3),'tau4':Q(25,2)},
 'A1':{'lambda':Q(32),'c':Q(71,4),'mu+':Q(15,2),'tau3':Q(232,7),'tau5':Q(17,2),'tau6':Q(3)},
 'A79':{'lambda':Q(394,13),'c':Q(44),'tau2':Q(532,13),'tau3':Q(13),'tau4':Q(99,7)},
 'A82':{'c':Q(209,3),'tau2':Q(424,9),'tau3':Q(115,4)},
 'A94':{'lambda':Q(32),'c':Q(263,6),'tau2':Q(335,6),'tau3':Q(37,4),'tau5':Q(13,6),'tau7':Q(14,5)},
}
ANCHORS={'A0':[0],'A1':[1,8,39],'A79':[79,145],'A82':[82],'A94':[94]}

def F(d,v):
 return sum(w for (D,V),w in W.items() if d>=D and v>=V)+15*(d+v>=14)+14*(d+v>=16)
def tterm(r,q,p,j): return (q if q>=j+1 else 0)-(p if r+q>=j else 0)
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
 ell={s:min(lam*R+c*x+x*F(R+s,16-R-x) for R in range(10-s+1) for x in range(s,16-R+1)) for s in range(1,11)}
 sig={}
 for pf in P:
  for r in set(pf['rho']):
   qm=min(12-r,sum(si<=r for si in pf['s']));key=(r,qm)
   if key not in sig:
    sig[key]=min(mp*(q-p)-mm*(q-p)-c*q+sum(taus[j]*tterm(r,q,p,j) for j in range(1,13))-q*F(r+q-1,16-q-p)
                 for q in range(qm+1) for p in range(min(r+3,15-q)+1))
 gaps=[]
 for pf in P:
  g=sum(n*ell[s] for s,n in Counter(pf['s']).items())
  for r,n in Counter(pf['rho']).items():
   qm=min(12-r,sum(si<=r for si in pf['s']));g+=n*sig[(r,qm)]
  g-=lam*sum(pf['rho']);gaps.append(g)
 return gaps

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
 P=load(z.demands_json,z.rows)
 if len(P)!=902:raise SystemExit(f'expected 902 profiles, got {len(P)}')
 masks={};summary={}
 for name,th in TEMPLATES.items():
  gaps=cover(P,th);mask=[g>0 for g in gaps];masks[name]=mask;pos=[g for g in gaps if g>0]
  assert all(mask[i] for i in ANCHORS[name])
  summary[name]={'anchors':ANCHORS[name],'coverage':sum(mask),'minimum_positive_gap':rat(min(pos)),'anchor_gaps':{str(i):rat(gaps[i]) for i in ANCHORS[name]},'theta':{k:rat(v) for k,v in th.items()}}
 union=[any(masks[k][i] for k in masks) for i in range(902)];missing=[i for i,x in enumerate(union) if not x]
 mult=Counter(sum(masks[k][i] for k in masks) for i in range(902))
 out={'schema':'n29-t2-five-scalar-templates-exact-v1','status':'PASS' if not missing else 'FAIL','profiles':902,'template_count':5,'covered':sum(union),'missing_indices':missing,'coverage_multiplicity':{str(k):v for k,v in sorted(mult.items())},'templates':summary,
      'primitive_potential':{'rectangles':{str(k):v for k,v in W.items()},'J2':15,'J0':14},'exact_fraction_arithmetic':True,'uses_lp_solver':False,
      'interpretation':'Five fixed rational scalar templates, together with one fixed exact primitive integer Hall/slack potential, give strict potential-certificate gap for every one of the 902 regenerated n29,t2 frontier profiles.'}
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
 if missing:raise SystemExit(1)
if __name__=='__main__':main()
