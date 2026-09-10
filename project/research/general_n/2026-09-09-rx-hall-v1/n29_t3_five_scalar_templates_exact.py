#!/usr/bin/env python3
"""Exact five-template cover for the 94 n=29,t=3 RX-Hall frontier profiles.

No LP/MIP solver is used for acceptance.  The global Hall potential is fixed to

    F(d,v) = 6 B(3,0) + 4 B(3,5) + 3 B(3,9),

where B(D,V)=1[d>=D and v>=V].  Five small rational scalar templates were
rationalised from floating inherited rays discovered in run 34496380911.
For each template this script evaluates every label/source envelope by exhaustive
finite minimisation with Fraction arithmetic and checks its strict gap profile by
profile. PASS requires the exact union to cover all 94 regenerated t=3 profiles.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import argparse,json

W={(3,0):6,(3,5):4,(3,9):3}
TEMPLATES={
 'A0': {'lambda':Q(140,81),'tau3':Q(29,12),'tau4':Q(23,12)},
 'A1': {'lambda':Q(9,5),'c':Q(16,3),'tau2':Q(23,3)},
 'A5': {'lambda':Q(9,5),'c':Q(19,330),'tau2':Q(3173,660),'tau4':Q(73,330)},
 'A30':{'lambda':Q(9,5),'c':Q(202,245),'tau2':Q(167,245),'tau3':Q(71,28),'tau4':Q(213,140)},
 'A38':{'lambda':Q(9,5),'c':Q(141,70),'tau2':Q(841,210),'tau3':Q(1682,1155)},
}
DISCOVERY_INDICES={'A0':0,'A1':1,'A5':5,'A30':30,'A38':38}

def F(d,v):
    return sum(w for (D,V),w in W.items() if d>=D and v>=V)
def tterm(r,q,p,j):
    return (q if q>=j+1 else 0)-(p if r+q>=j else 0)
def rat(x): return [x.numerator,x.denominator]

def load(dp,rp):
    D=json.loads(Path(dp).read_text()); out=[]
    for line in Path(rp).read_text().splitlines():
        if not line.strip(): continue
        z=list(map(int,line.split())); did=z[0]; rho=z[2:]; s=D[did]['s']
        # For t=3, sum(s)=sum(rho)+2t=sum(rho)+6 on this frontier.
        if min(s)>0 and sum(s)==sum(rho)+6:
            out.append({'s':s,'rho':rho,'demand_id':did})
    return out

def gaps_for(P,th):
    lam=th.get('lambda',Q(0));c=th.get('c',Q(0));mp=th.get('mu+',Q(0));mm=th.get('mu-',Q(0))
    taus={j:th.get(f'tau{j}',Q(0)) for j in range(1,13)}
    ell={s:min(lam*R+c*x+x*F(R+s,16-R-x)
               for R in range(10-s+1) for x in range(s,16-R+1))
         for s in range(1,11)}
    sig={}
    for pf in P:
        for r in set(pf['rho']):
            qm=min(12-r,sum(si<=r for si in pf['s'])); key=(r,qm)
            if key not in sig:
                sig[key]=min(mp*(q-p)-mm*(q-p)-c*q
                    +sum(taus[j]*tterm(r,q,p,j) for j in range(1,13))
                    -q*F(r+q-1,16-q-p)
                    for q in range(qm+1)
                    for p in range(min(r+3,15-q)+1))
    gaps=[]
    for pf in P:
        g=sum(n*ell[s] for s,n in Counter(pf['s']).items())
        for r,n in Counter(pf['rho']).items():
            qm=min(12-r,sum(si<=r for si in pf['s']))
            g+=n*sig[(r,qm)]
        g-=lam*sum(pf['rho']); gaps.append(g)
    return gaps

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    P=load(z.demands_json,z.rows)
    if len(P)!=94: raise SystemExit(f'expected 94 profiles, got {len(P)}')
    masks={}; summary={}
    for name,th in TEMPLATES.items():
        gaps=gaps_for(P,th); mask=[g>0 for g in gaps]; masks[name]=mask; pos=[g for g in gaps if g>0]
        summary[name]={
          'discovery_index':DISCOVERY_INDICES[name],
          'coverage':sum(mask),
          'covered_indices':[i for i,x in enumerate(mask) if x],
          'minimum_positive_gap':rat(min(pos)) if pos else None,
          'maximum_gap':rat(max(gaps)),
          'minimum_gap':rat(min(gaps)),
          'theta':{k:rat(v) for k,v in th.items()}}
    union=[any(masks[k][i] for k in masks) for i in range(94)]
    missing=[i for i,x in enumerate(union) if not x]
    mult=Counter(sum(masks[k][i] for k in masks) for i in range(94))
    # Exact redundancy check: which individual templates can be deleted from THIS rational family?
    deletable=[]
    for omit in TEMPLATES:
        if all(any(masks[k][i] for k in TEMPLATES if k!=omit) for i in range(94)): deletable.append(omit)
    out={'schema':'n29-t3-five-scalar-templates-exact-v1','status':'PASS' if not missing else 'FAIL',
         'profiles':94,'template_count':len(TEMPLATES),'covered':sum(union),'missing_indices':missing,
         'coverage_multiplicity':{str(k):v for k,v in sorted(mult.items())},'templates':summary,
         'primitive_potential':{'rectangles':{str(k):v for k,v in W.items()},'weight_sum':sum(W.values())},
         'exact_fraction_arithmetic':True,'uses_lp_solver':False,'deletable_templates_within_this_family':deletable,
         'discovery_provenance':{'run_id':34496380911,'floating_selected_indices':[0,1,5,30,38]},
         'interpretation':'Five fixed rational scalar templates together with F=6B(3,0)+4B(3,5)+3B(3,9) give exact strict potential-certificate gaps for the regenerated n29,t3 frontier iff missing_indices is empty. No LP/MIP participates in acceptance.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
    if missing: raise SystemExit(1)
if __name__=='__main__': main()
