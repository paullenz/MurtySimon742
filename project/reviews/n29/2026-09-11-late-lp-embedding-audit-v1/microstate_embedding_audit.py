#!/usr/bin/env python3
"""Exact microstate -> grouped late-LP normalization regression for n=29.

Constructs explicit selected/residual microstates, averages them independently into
Y/T/W/P/Z, and evaluates every production LP row with Fraction arithmetic.  The
same assignments MUST fail against the quarantined v1 model, providing a sensitivity
control for the historical label-multiplicity bug.

The fixtures test the averaging/normalisation layer; they are not claimed to be
actual diameter-two-critical graphs.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import json, sys

HERE = Path(__file__).resolve().parent
PROD = HERE.parent / "2026-09-08-redteam-restart-v1"
sys.path.insert(0, str(PROD))
import independent_threshold_model_v2 as v2  # noqa: E402
import independent_threshold_model as v1      # noqa: E402

A, B = 12, 16


def balanced_edges(rowdeg, avoid=frozenset(), offset=0):
    col = [0] * A; edges = []
    for u, deg in enumerate(rowdeg):
        cand = [i for i in range(A) if (u, i) not in avoid]
        cand.sort(key=lambda i: (col[i], (i-u-offset) % A))
        assert len(cand) >= deg
        for i in cand[:deg]:
            col[i] += 1; edges.append((u, i))
    assert len(edges) == len(set(edges))
    return edges


def make_fixture(kind):
    if kind == "uniform":
        rho, q_target, s = [4]*B, [4]*B, [1]*A
    elif kind == "mixed":
        rho, q_target, s = [3]*8+[4]*8, [4]*8+[3]*8, [1]*6+[0]*6
    else:
        raise ValueError(kind)

    pair_arcs=[]; seen=set()
    for u, qq in enumerate(q_target):
        for step in range(1, qq+1):
            w=(u+step) % B
            assert u != w and (w,u) not in seen and (u,w) not in seen
            seen.add((u,w)); pair_arcs.append((u,w))

    q=[0]*B; p=[0]*B
    for u,w in pair_arcs: q[u]+=1; p[w]+=1
    assert q == q_target

    selected=balanced_edges(q, offset=0)
    residual=balanced_edges(rho, avoid=frozenset(selected), offset=5)
    assert not (set(selected) & set(residual))
    assert [sum(u0==u for u0,_ in selected) for u in range(B)] == q
    assert [sum(u0==u for u0,_ in residual) for u in range(B)] == rho

    x=[0]*A; R=[0]*A
    for _,i in selected: x[i]+=1
    for _,i in residual: R[i]+=1
    d=[R[i]+s[i] for i in range(A)]
    assert all(0 <= d[i] <= 10 and x[i] <= B-R[i] for i in range(A))

    assert sum(d) % 2 == 0
    r=sum(rho); t=sum(d)//2-r
    assert sum(R)==r and sum(d)==2*(r+t)

    for u,w in pair_arcs: assert rho[w]+q[w] >= q[u]-1
    for u in range(B):
        assert q[u]+rho[u] <= A
        assert p[u] <= rho[u]+3
        assert q[u]+p[u] <= B-1
    for u,i in selected:
        assert s[i] <= rho[u]
        assert d[i] <= rho[u]+R[i]
        assert d[i] <= rho[u]+q[u]-1
        assert R[i]+x[i] >= q[u]+p[u]

    return dict(kind=kind,rho=rho,q=q,p=p,s=s,R=R,x=x,d=d,
                selected=selected,residual=residual,pair_arcs=pair_arcs,t=t)


def group_data(vals):
    c=Counter(vals); ordered=sorted(c)
    idx={v:j for j,v in enumerate(ordered)}
    mult={idx[v]:c[v] for v in ordered}
    return idx,mult


def aggregate(f):
    g_of,ng=group_data(f['s']); k_of,nk=group_data(f['rho'])
    val=defaultdict(Fraction)
    for i in range(A):
        g=g_of[f['s'][i]]; d,R,x=f['d'][i],f['R'][i],f['x'][i]
        val[('Y',g,d,R)] += Fraction(1,ng[g])
        for h in range(1,B-R+1):
            if x>=h: val[('T',g,d,R,h)] += Fraction(1,ng[g])
    for u in range(B):
        k=k_of[f['rho'][u]]
        val[('W',k,f['q'][u],f['p'][u])] += Fraction(1,nk[k])
    for u,w in f['pair_arcs']:
        k,l=k_of[f['rho'][u]],k_of[f['rho'][w]]
        den=nk[k]*(nk[l]-(k==l)); assert den>0
        val[('P',k,l,f['q'][u],f['q'][w])] += Fraction(1,den)
    for u,i in f['selected']:
        k,g=k_of[f['rho'][u]],g_of[f['s'][i]]
        val[('Z',k,g,f['q'][u],f['p'][u],f['d'][i],f['R'][i])] += Fraction(1,nk[k]*ng[g])
    return dict(val)


def evaluate(model, assignment):
    names=set(model.names)
    missing=[(n,str(v)) for n,v in assignment.items() if v and n not in names]
    if missing: return dict(missing=missing,eq_bad=[],ub_bad=[])
    x=[]
    for n in model.names:
        v=assignment.get(n,Fraction(0)); assert 0<=v<=1,(n,v); x.append(v)
    eq_bad=[]
    for j,(row,rhs) in enumerate(model.eq):
        lhs=sum(Fraction(c)*x[i] for i,c in row.items())
        if lhs != rhs: eq_bad.append((j,str(lhs),str(rhs)))
    ub_bad=[]
    for j,(row,rhs) in enumerate(model.ub):
        lhs=sum(Fraction(c)*x[i] for i,c in row.items())
        if lhs > rhs: ub_bad.append((j,str(lhs),str(rhs)))
    return dict(missing=[],eq_bad=eq_bad,ub_bad=ub_bad,
                variables=len(model.names),equalities=len(model.eq),inequalities=len(model.ub))


def run_fixture(kind):
    f=make_fixture(kind); a=aggregate(f)
    c=evaluate(v2.build(f['s'],f['rho'],f['t']),a)
    o=evaluate(v1.build(f['s'],f['rho'],f['t']),a)
    assert not c['missing'] and not c['eq_bad'] and not c['ub_bad'],c
    old_fail=len(o['missing'])+len(o['eq_bad'])+len(o['ub_bad'])
    assert old_fail>0,"fixture did not detect historical v1 normalization bug"
    return {
      'fixture':kind,'t':f['t'],
      'demand_groups':sorted(Counter(f['s']).items()),
      'residual_groups':sorted(Counter(f['rho']).items()),
      'selected_pair_arcs':len(f['pair_arcs']),
      'selected_cross_edges':len(f['selected']),
      'residual_cross_edges':len(f['residual']),
      'corrected_v2':{'variables':c['variables'],'equalities':c['equalities'],
                      'inequalities':c['inequalities'],'violations':0},
      'quarantined_v1_failures':{'equalities':len(o['eq_bad']),
          'inequalities':len(o['ub_bad']),'missing_nonzero_variables':len(o['missing']),
          'total':old_fail}
    }


def main():
    results=[run_fixture('uniform'),run_fixture('mixed')]
    report={'schema':'n29-late-lp-microstate-embedding-audit-v1','status':'PASS',
      'purpose':'exact rational regression of graph-level averaging into corrected production late LP',
      'fixtures':results,'corrected_v2_all_rows_satisfied':True,
      'historical_v1_detectably_fails':True,'external_independence':False,
      'note':'Fixtures test averaging/normalisation algebra, not existence of diameter-two-critical graphs.'}
    (HERE/'MICROSTATE_AUDIT_REPORT.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__': main()
