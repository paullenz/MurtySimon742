#!/usr/bin/env python3
"""Exact rational checker for the 889-profile common scalar template.

This script contains no LP solver.  It fixes the already exact primitive
16-term BC/slack potential and a small rational scalar vector, evaluates the
label/source envelopes by exhaustive finite minimisation with Fraction, and
reports exactly which regenerated n=29,t=2 frontier profiles have strict gap.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import argparse,json

W={(2,11):11,(2,12):12,(2,13):28,(2,14):8,
   (3,0):41,(3,4):8,(3,7):8,(3,8):8,(3,10):11,(3,12):5,
   (4,2):5,(4,3):5,(4,6):6,(4,9):8}
TH={'lambda':Q(277,9),'c':Q(176,5),'tau2':Q(17,2),'tau3':Q(253,10),
    'tau4':Q(151,10),'tau5':Q(15,2),'tau7':Q(11,7)}

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

def rat(x): return [x.numerator,x.denominator]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    P=load(z.demands_json,z.rows)
    if len(P)!=902:raise SystemExit(f'expected 902 profiles, got {len(P)}')
    lam=TH['lambda'];c=TH['c'];taus={j:TH.get(f'tau{j}',Q(0)) for j in range(1,13)}
    ell={s:min(lam*R+c*x+x*F(R+s,16-R-x) for R in range(10-s+1) for x in range(s,16-R+1)) for s in range(1,11)}
    sig={}
    for pf in P:
        for r in set(pf['rho']):
            qm=min(12-r,sum(si<=r for si in pf['s']));key=(r,qm)
            if key not in sig:
                sig[key]=min(-c*q+sum(taus[j]*tterm(r,q,p,j) for j in range(1,13))-q*F(r+q-1,16-q-p)
                             for q in range(qm+1) for p in range(min(r+3,15-q)+1))
    gaps=[]
    for pf in P:
        g=sum(n*ell[s] for s,n in Counter(pf['s']).items())
        for r,n in Counter(pf['rho']).items():
            qm=min(12-r,sum(si<=r for si in pf['s']));g+=n*sig[(r,qm)]
        g-=lam*sum(pf['rho']);gaps.append(g)
    covered=[i for i,g in enumerate(gaps) if g>0];outside=[i for i,g in enumerate(gaps) if g<=0]
    mingap=min(gaps[i] for i in covered)
    out={'schema':'n29-t2-common-scalar-889-exact-v1','status':'PASS' if len(covered)==889 else 'FAIL','profiles':len(P),'covered':len(covered),'outside_count':len(outside),'outside_indices':outside,
         'minimum_positive_gap':rat(mingap),'theta':{k:rat(v) for k,v in TH.items()},'primitive_potential_weights':{str(k):v for k,v in W.items()},
         'diagonal_weights':{'J2':15,'J0':14},'exact_fraction_arithmetic':True,'uses_lp_solver':False,
         'interpretation':'Exact finite statement: this one common scalar template plus the primitive integer potential proves the potential-certificate strict gap for 889 of the 902 regenerated n29,t2 profiles.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
    if out['status']!='PASS':raise SystemExit(1)
if __name__=='__main__':main()
