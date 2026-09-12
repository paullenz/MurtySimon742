#!/usr/bin/env python3
"""Exact-budget envelopes, including the uniquely zero-demand label."""
from collections import Counter
import json
import sys
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix
from discover import HERE, integer_certificate

A, B, DMAX, T = 15, 18, 13, 2


def subset_reason(s, rho):
    for h in range(2, max(s)+1):
        W = sum(x for x in s if x >= h)
        z = sum(x >= h for x in rho)
        lower = W-h*(h+1)
        upper = sum(x-1 for x in rho if x >= h)
        if z >= h and 2*W == z*(z-1)+h*(h+1) and lower > upper:
            return dict(method='tight_subset_threshold', h=h, z=z, W=W,
                        incoming_lower=lower, incoming_upper=upper)
    return None


def basis(kind, k, h, s, d, load):
    if kind == 'BC':
        return int(d >= k and load <= h)
    if kind == 'SH':
        return int(s >= k and load <= h)
    assert kind == 'DIAG'
    return int(d-load >= k)


FIXED = [('BC',1,9,7),('BC',1,6,11),('BC',1,4,5),
         ('BC',1,3,21),('BC',1,2,29),('BC',1,1,39),
         ('BC',2,4,6),('BC',3,8,5),('BC',3,7,8),('BC',3,5,11),
         ('DIAG',-1,0,17),('DIAG',0,0,8),('SH',2,17,39)]


def build(s, rho, adaptive=False):
    r = sum(rho)
    deficit = sum(s)-r-2*T
    assert deficit >= 0 and s.count(0) <= 1
    assert min(s) == 0 or deficit == 0
    names, bounds, rows, rhs, kinds = [], [], [], [], []

    def var(name, bound=(None,None)):
        names.append(name); bounds.append(bound)
        return len(names)-1

    lam, c, mu = var('lambda'), var('c'), var('mu')
    tau = {j:var(('tau',j),(0,None)) for j in range(1,A+1)}
    ell = {v:var(('ell',v)) for v in sorted(set(s))}
    sig = {v:var(('sig',v)) for v in sorted(set(rho))}
    terms = ([('BC',d,h) for d in range(1,DMAX+1) for h in range(B+1)]
             + [('SH',d,h) for d in range(1,A) for h in range(B+1)]
             + [('DIAG',k,0) for k in range(-B,A)]) if adaptive else []
    weights = {term:var(('weight',)+term,(0,None)) for term in terms}

    def row(co, sign, s0, d, load, repair):
        # sign=+x for label lower-envelope cost, -q for source cost.
        if adaptive:
            for term,j in weights.items():
                v = basis(*term,s0,d,load)
                if v and sign:
                    co[j] = -sign*v
            value = 0
        else:
            value = sign*sum(w*basis(k,a,h,s0,d,load) for k,a,h,w in FIXED)
        rows.append(co);rhs.append(value);kinds.append(('local',repair))

    for sv in ell:
        for R in range(B+1):
            d = R+sv if sv else R-deficit
            if not 0 <= d <= DMAX:
                continue
            xmax = min(B-R, sum(rv >= sv for rv in rho))
            for x in range(sv,xmax+1):
                row({ell[sv]:1,lam:-R,c:-x},x,sv,d,R+x,ell[sv])
    for rv in sig:
        qmax = min(A-rv,sum(sv <= rv for sv in s))
        for q in range(qmax+1):
            for p in range(min(rv+B-A-1,B-1-q)+1):
                co = {sig[rv]:1,mu:-(q-p),c:q}
                for j,idx in tau.items():
                    v = (q if q >= j+1 else 0)-(p if rv+q >= j else 0)
                    if v:co[idx] = -v
                row(co,-q,rv,rv+q-1,q+p,sig[rv])
    gap = {lam:r}
    for sv,n in Counter(s).items():gap[ell[sv]] = -n
    for rv,n in Counter(rho).items():gap[sig[rv]] = -n
    rows.append(gap);rhs.append(-1);kinds.append(('gap',None))
    mat = lil_matrix((len(rows),len(names)))
    for i,co in enumerate(rows):
        for j,v in co.items():mat[i,j] = v
    res = linprog(np.zeros(len(names)),A_ub=mat.tocsr(),b_ub=rhs,bounds=bounds,method='highs')
    if res.status == 4:
        res = linprog(np.zeros(len(names)),A_ub=mat.tocsr(),b_ub=rhs,bounds=bounds,method='highs-ipm')
    return names,bounds,rows,rhs,kinds,res


def main():
    adaptive = '--adaptive' in sys.argv
    source = 'extended_fixed.json' if adaptive else 'baseline.json'
    outname = 'extended_adaptive.json' if adaptive else 'extended_fixed.json'
    records = json.loads((HERE/source).read_text())['unresolved']
    out = dict(schema='n34-exact-budget-envelope-v1', adaptive=adaptive,
               fixed_potential=FIXED, hand=[], certificates=[], unresolved=[])
    if '--resume' in sys.argv:
        out = json.loads((HERE/outname).read_text())
    covered = {rec['state_id'] for key in ('hand','certificates','unresolved') for rec in out[key]}
    for i,rec in enumerate(records):
        if rec['state_id'] in covered:
            continue
        state = {k:rec[k] for k in ('state_id','s','rho')}
        reason = subset_reason(rec['s'],rec['rho'])
        if reason:
            out['hand'].append(dict(**state,**reason))
        else:
            model = build(rec['s'],rec['rho'],adaptive)
            cert = integer_certificate(model)
            if cert:
                # Omitted adaptive weights are exactly zero, not rounded away.
                keep = [j for j,n in enumerate(cert['names'])
                        if not (isinstance(n,tuple) and n[0]=='weight' and cert['numerators'][j]==0)]
                cert['names'] = [cert['names'][j] for j in keep]
                cert['numerators'] = [cert['numerators'][j] for j in keep]
                out['certificates'].append(dict(**state,**cert))
            else:
                out['unresolved'].append(dict(**state,solver_status=int(model[-1].status)))
        (HERE/outname).write_text(json.dumps(out,separators=(',',':'))+'\n')
        if (i+1)%10 == 0 or i+1 == len(records):
            print(i+1,{k:len(out[k]) for k in ('hand','certificates','unresolved')},flush=True)
    print('COMPLETE',len(records),flush=True)


if __name__ == '__main__':
    main()
