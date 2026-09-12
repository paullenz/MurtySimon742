#!/usr/bin/env python3
"""Solver-free integer verification and complete, disjoint m290 coverage.

Imports only the previously separate frontier checker, never discovery code.
"""
from collections import Counter
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'2026-09-12-frontier-v1'))
from check_frontier import expand

A, B, DMAX, T = 15, 18, 13, 2
FIXED = [('BC',1,9,7),('BC',1,6,11),('BC',1,4,5),
         ('BC',1,3,21),('BC',1,2,29),('BC',1,1,39),
         ('BC',2,4,6),('BC',3,8,5),('BC',3,7,8),('BC',3,5,11),
         ('DIAG',-1,0,17),('DIAG',0,0,8),('SH',2,17,39)]


def feature(term,s,d,h):
    kind,k,cutoff = term
    if kind == 'BC':
        assert 1 <= k <= DMAX and 0 <= cutoff <= B
        return d >= k and h <= cutoff
    if kind == 'SH':
        assert 1 <= k < A and 0 <= cutoff <= B
        return s >= k and h <= cutoff
    assert kind == 'DIAG' and -B <= k < A and cutoff == 0
    return d-h >= k


def check_certificate(cert,mode):
    s,rho = cert['s'],cert['rho']
    assert len(s)==A and len(rho)==B
    den = cert['denominator']
    assert type(den) is int and den > 0
    assert all(type(x) is int for x in cert['numerators'])
    names = [tuple(n) if isinstance(n,list) else n for n in cert['names']]
    assert len(names)==len(set(names))==len(cert['numerators'])
    X = dict(zip(names,cert['numerators']))
    common = {'lambda','c'} | {('tau',j) for j in range(1,A+1)}
    common |= {('ell',v) for v in s} | {('sig',v) for v in rho}
    weights = []
    if mode == 'baseline':
        assert set(X)==common|{'mu+','mu-'} and min(s)>0
        assert min(X['lambda'],X['c'],X['mu+'],X['mu-']) >= 0
        mu = X['mu+']-X['mu-']
    else:
        mu = X['mu']
        if mode == 'adaptive':
            for name,value in X.items():
                if isinstance(name,tuple) and name[0]=='weight':
                    assert len(name)==4 and value >= 0
                    feature(name[1:],0,0,0)  # Validate the allowed monotone basis.
                    weights.append((name[1:],value))
        else:
            assert mode == 'fixed'
        assert set(X)==common|{'mu'}|{('weight',)+term for term,value in weights}
    assert all(X['tau',j] >= 0 for j in range(1,A+1))

    def potential(demand,d,h):
        if mode == 'baseline':
            return den*(4*(d>=2)+2*(d>=2 and h<=11)+(d>=2 and h<=9)
                        +(d>=2 and h<=7)+(d>=2 and h<=4)+(d>=2 and h<=3)
                        +(d>=3 and h<=8)+(d>=3 and h<=6)+(d>=3 and h<=5))
        if mode == 'fixed':
            return den*sum(w*feature((kind,k,h0),demand,d,h) for kind,k,h0,w in FIXED)
        return sum(w*feature(term,demand,d,h) for term,w in weights)

    E = sum(s)-sum(rho)-2*T
    if mode != 'baseline':
        assert E >= 0 and s.count(0) <= 1
        assert min(s)==0 or E==0
    checks = 0
    for demand in set(s):
        options = 0
        for R in range(B+1):
            d = R+demand if demand else R-E
            if not 0 <= d <= DMAX:
                continue
            xmax = B-R
            if mode != 'baseline':
                xmax = min(xmax,sum(rv>=demand for rv in rho))
            for x in range(demand,xmax+1):
                assert X['ell',demand] <= X['lambda']*R+X['c']*x+x*potential(demand,d,R+x)
                checks += 1; options += 1
        assert options > 0
    for rv in set(rho):
        maxq = min(A-rv,sum(demand<=rv for demand in s))
        for q in range(maxq+1):
            for p in range(min(rv+B-A-1,B-1-q)+1):
                transport = sum(X['tau',j]*((q if q>=j+1 else 0)
                                -(p if rv+q>=j else 0)) for j in range(1,A+1))
                assert X['sig',rv] <= mu*(q-p)-X['c']*q+transport-q*potential(rv,rv+q-1,q+p)
                checks += 1
    gap = X['lambda']*sum(rho)
    gap -= sum(n*X['ell',v] for v,n in Counter(s).items())
    gap -= sum(n*X['sig',v] for v,n in Counter(rho).items())
    assert gap==cert['gap'] and gap < 0
    return checks,gap


def check_hand(rec):
    s,rho = rec['s'],rec['rho']
    method = rec['method']
    if method == 'positive_degree_mass':
        assert min(s)>0 and sum(s)!=sum(rho)+2*T
        assert rec['S']==sum(s) and rec['r']==sum(rho)
        return
    h = rec['h']; assert type(h) is int and h>=2
    z = sum(rv>=h for rv in rho)
    W = sum(sv for sv in s if sv>=h)
    assert z==rec['z'] and z>=h and 2*W==z*(z-1)+h*(h+1)
    if method == 'tight_total_threshold':
        assert min(s)>=h and B+2*T>h*(h+1)
        assert sum(s)>=sum(rho)+2*T
    else:
        assert method=='tight_subset_threshold'
        lo,hi = W-h*(h+1),sum(rv-1 for rv in rho if rv>=h)
        assert (rec['W'],rec['incoming_lower'],rec['incoming_upper'])==(W,lo,hi)
        assert lo>hi


def main():
    states,stats = expand(T)
    assert len(states)==1614 and len(set(states))==len(states)
    expected = set(range(len(states)))
    counts = Counter(); coverage = set(); checks = 0; gaps = {}
    for filename,mode in [('baseline.json','baseline'),('extended_fixed.json','fixed'),
                          ('extended_adaptive.json','adaptive')]:
        data = json.loads((HERE/filename).read_text())
        seen = set(); localgaps = []
        for key in ('hand','certificates','unresolved'):
            for rec in data[key]:
                idx = rec['state_id']
                assert type(idx) is int and idx in expected and idx not in seen
                assert (tuple(rec['s']),tuple(rec['rho']))==states[idx]
                seen.add(idx)
                if key=='unresolved':continue
                assert idx not in coverage
                coverage.add(idx)
                if key=='hand':
                    check_hand(rec);counts[rec['method']]+=1
                else:
                    n,gap = check_certificate(rec,mode)
                    checks+=n;localgaps.append(gap);counts[mode+'_certificates']+=1
        assert seen==expected, (filename,len(seen),len(expected))
        expected = {rec['state_id'] for rec in data['unresolved']}
        if localgaps:gaps[mode] = dict(count=len(localgaps),worst_integer_gap=max(localgaps))
    assert not expected and coverage==set(range(1614))
    report = dict(schema='n34-m290-solver-free-verification-v1',status='PASS',
                  frontier=stats,exclusions=dict(counts),local_integer_checks=checks,
                  certificate_gaps=gaps,covered_states=len(coverage),unresolved_states=0,
                  candidate_consequence='e(G)<=289 for n=34; equality classification OPEN',
                  external_review='OPEN')
    (HERE/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
