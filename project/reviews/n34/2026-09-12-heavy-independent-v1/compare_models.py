#!/usr/bin/env python3
"""Audit every original row against the separate whole-count formulation.

Translate the preserved certificate to the new model; comparison uses exact
rational arithmetic, canonical row forms, and duplicate-row multiplicities.
"""
from collections import Counter,defaultdict,deque
from fractions import Fraction
from functools import reduce
from importlib.util import module_from_spec,spec_from_file_location
from math import gcd,lcm
from pathlib import Path
import json
from count_model import build,verify

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
OLD=ROOT/'project/research/n34/2026-09-12-equality-v1'
spec=spec_from_file_location('historical_heavy',OLD/'heavy_model.py')
old=module_from_spec(spec);spec.loader.exec_module(old)


def canonical(co,rhs,kind):
    co={n:Fraction(v) for n,v in co.items() if v}
    den=lcm(*(v.denominator for v in [*co.values(),Fraction(rhs)]))
    ints={n:int(v*den) for n,v in co.items()};b=int(Fraction(rhs)*den)
    divisor=reduce(gcd,[abs(v) for v in ints.values()]+[abs(b)]) or 1
    ordered=sorted(ints)
    sign=1
    if kind=='eq' and ((ints[ordered[0]] if ordered else b)<0):sign=-1
    key=(tuple((n,sign*ints[n]//divisor) for n in ordered),sign*b//divisor)
    return key,Fraction(sign*divisor,den)


def translated_name(n):
    tag,*v=n
    if tag=='W':k,q,p,H=v;return ('source',[1,2][k],q,p,H)
    if tag=='L':g,R,x=v;return ('label',[1,2][g],R,x)
    if tag=='P':k,l,q,q2=v;return ('arc',[1,2][k],[1,2][l],q,q2)
    assert tag=='Z'
    k,g,q,p,H,R,x=v;return ('incidence',[1,2][k],[1,2][g],q,p,H,R,x)


def main():
    source=json.loads((OLD/'heavy_certificate.json').read_text())
    legacy=old.build(source['s'],source['rho'],source['h'])
    fresh=build();names=[translated_name(n) for n in legacy.names]
    assert len(names)==len(set(names)) and set(names)==set(fresh['scales'])
    converted={'eq':[],'ub':[]};counts={}
    for kind,rows,rhs in [('eq',legacy.eq,legacy.be),('ub',legacy.ub,legacy.bu)]:
        buckets=defaultdict(deque)
        for i,row in enumerate(fresh['rows'][kind]):
            key,factor=canonical(row['coefficients'],row['rhs'],kind)
            buckets[key].append((i,factor))
        assignment={}
        for i,(row,b) in enumerate(zip(rows,rhs)):
            co={names[j]:Fraction(c,fresh['scales'][names[j]]) for j,c in row.items() if c}
            key,factor=canonical(co,b,kind)
            assert buckets[key],(kind,i,'unmatched original row')
            target,newfactor=buckets[key].popleft()
            assignment[i]=(target,factor/newfactor)
        assert not any(buckets.values()),'unmatched count row'
        counts[kind]=len(rows)
        for i,w in source['certificate'][kind]:
            target,factor=assignment[i]
            converted[kind].append((target,w*factor))
    scale=lcm(*(w.denominator for kind in converted for i,w in converted[kind]))
    cert={kind:[[i,int(w*scale)] for i,w in converted[kind]] for kind in converted}
    cert['rhs']=source['certificate']['rhs']*scale
    factor=reduce(gcd,[abs(w) for kind in ['eq','ub'] for i,w in cert[kind]]+[abs(cert['rhs'])]) or 1
    for kind in ['eq','ub']:cert[kind]=[[i,w//factor] for i,w in cert[kind]]
    cert['rhs']//=factor
    checked=verify(fresh,cert)
    (HERE/'count_certificate.json').write_text(json.dumps(cert,separators=(',',':'))+'\n')
    report=dict(schema='n34-heavy-independent-count-audit-v1',status='PASS',
                variables=len(names),matched_equalities=counts['eq'],matched_inequalities=counts['ub'],
                exact_row_multiset_equality=True,translated_certificate=checked,
                external_independence=False,external_review='OPEN')
    (HERE/'comparison.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
