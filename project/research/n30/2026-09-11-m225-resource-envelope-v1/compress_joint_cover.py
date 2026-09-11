#!/usr/bin/env python3
"""Exact cross-evaluation of discovered potentials, then deterministic greedy cover."""
from collections import Counter
from fractions import Fraction
from math import gcd,lcm
from functools import lru_cache,reduce
from pathlib import Path
import argparse,json
from mine_joint_potential import label_states,source_states,lcoeff,scoeff

HERE=Path(__file__).resolve().parent

def primitive(raw):
    w=list(map(Fraction,raw));D=lcm(*(x.denominator for x in w))
    a=[int(x*D) for x in w];g=reduce(gcd,map(abs,a))
    return tuple(x//g for x in a)

@lru_cache(None)
def label_min(s,H,shapes,w):
    return min(sum(a*b for a,b in zip(w,lcoeff(s,R,x,shapes))) for R in range(13-s) for x in range(s,min(16-R,H)+1))

@lru_cache(None)
def source_min(r,Q,shapes,w):
    return min(sum(a*b for a,b in zip(w,scoeff(r,q,p,shapes))) for q in range(Q+1) for p in range(r+3))

def gap(row,shapes,w):
    s=row['s'];rhos=row['rho']
    ell={si:label_min(si,sum(r>=si for r in rhos),shapes,w) for si in set(s)}
    sig={r:source_min(r,min(13-r,sum(si<=r for si in s)),shapes,w) for r in set(rhos)}
    return sum(n*ell[si] for si,n in Counter(s).items())+sum(n*sig[r] for r,n in Counter(rhos).items())-w[0]*sum(rhos)

def cover(data):
    rows=data['rows'];shapes=tuple(data['shapes'])
    ws=list(dict.fromkeys(primitive(r['weights']) for r in rows if r.get('exact_positive')))
    covers=[{i for i,r in enumerate(rows) if gap(r,shapes,w)>0} for w in ws]
    rem=set().union(*covers);ans=[]
    while rem:
        j=max(range(len(ws)),key=lambda j:(len(covers[j]&rem),-sum(abs(x) for x in ws[j])))
        ids=sorted(covers[j]&rem);rem-=set(ids)
        ans.append({'weights':ws[j],'assigned':[{'s':rows[i]['s'],'rho':rows[i]['rho']} for i in ids],
                    'minimum_integer_gap':min(gap(rows[i],shapes,ws[j]) for i in ids)})
        print('template',len(ans),'new',len(ids),'full coverage',len(covers[j]),'weight sum',sum(abs(x) for x in ws[j]),flush=True)
    return {'schema':'n30-joint-greedy-integer-cover-v1','shapes':shapes,'coverage':sum(len(x['assigned']) for x in ans),'templates':ans}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,default=HERE/'JOINT_SMALL_DMAX12_DISCOVERY.json');ap.add_argument('--output',type=Path,default=HERE/'JOINT_SMALL_INTEGER_COVER.json');args=ap.parse_args()
    args.output.write_text(json.dumps(cover(json.loads(args.input.read_text())),indent=2)+'\n')
