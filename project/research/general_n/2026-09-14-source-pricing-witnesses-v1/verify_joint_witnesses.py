"""Integer-only verification of explicit relaxation witnesses, not graphs."""
from __future__ import annotations
from collections import Counter
from copy import deepcopy
import json
import hashlib
from pathlib import Path

HERE=Path(__file__).resolve().parent


def check(p: dict, witness: dict) -> dict:
    a,b=p['a'],p['b']
    s,q,rho,P=(p[k] for k in ('s','q','rho','P'))
    assert len(s)==a and all(len(v)==b for v in (q,rho,P))
    assert all(isinstance(v,int) and v>=0 for vec in (s,q,P) for v in vec)
    assert all(isinstance(v,int) and v>=1 for v in rho)
    assert all(q[u]+rho[u]<=a for u in range(b))
    Q=sum(q); r=sum(rho)
    assert sum(s)==r+2*p['t']+p['D0']
    assert Q==r+2*p['t']+p['D0']+p['Esel']
    chosen=witness['selected_labels']
    assert len(chosen)==b
    x=[0]*a
    for u,labels in enumerate(chosen):
        assert len(labels)==q[u] and len(set(labels))==len(labels)
        for i in labels:
            assert isinstance(i,int) and 0<=i<a and s[i]<=rho[u]
            x[i]+=1
    e=[x[i]-s[i] for i in range(a)]
    assert all(v>=0 for v in e) and sum(e)==p['Esel']
    assert e==witness['excess']
    seen=set(); incoming=[0]*b; outgoing=[0]*b
    for arc in witness['arcs']:
        assert len(arc)==2
        u,v=arc
        assert isinstance(u,int) and isinstance(v,int) and 0<=u<b and 0<=v<b and u!=v
        pair=tuple(sorted((u,v)))
        assert pair not in seen
        seen.add(pair)
        assert q[u]<=q[v]+rho[v]+1 and q[v]<=q[u]+rho[u]
        outgoing[u]+=1; incoming[v]+=1
    assert outgoing==q and incoming==witness['incoming'] and sum(incoming)==Q
    assert all(0<=incoming[u]<=P[u] for u in range(b))
    pressure=[max(0,incoming[u]-rho[u]+1) for u in range(b)]
    assert pressure==witness['pressure']
    endpoint_checks=0
    for u,labels in enumerate(chosen):
        for i in labels:
            if s[i]>0:
                assert pressure[u]<=e[i]
                endpoint_checks+=1
    return {'row':p['row'],'selected_incidences':Q,'directed_arcs':len(seen),
            'positive_endpoint_checks':endpoint_checks,'Esel':sum(e),'status':'PASS'}


def coupling_diagnostics(p, w):
    S=list(map(set,w['selected_labels'])); rho=p['rho']; pairs=[]; unions=[]
    for u,v in w['arcs']:
        uv=len(S[u]-S[v]); vu=len(S[v]-S[u])
        if not (1<=uv<=rho[v]+1 and vu<=rho[u]):
            pairs.append({'u':u,'v':v,'Su_minus_Sv':uv,'Sv_minus_Su':vu,
                          'rho_u':rho[u],'rho_v':rho[v]})
    for u in range(p['b']):
        forced=set().union(*(S[v] for a,v in w['arcs'] if a==u))-S[u]
        if len(forced)>rho[u]:
            unions.append({'u':u,'forced_labels':sorted(forced),
                           'required_residual':len(forced),'rho_u':rho[u]})
    full={'row':p['row'],'pair_violations':pairs,'residual_union_violations':unions}
    digest=hashlib.sha256(json.dumps(full,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return {'row':p['row'],'pair_violations':len(pairs),'residual_union_violations':len(unions),
            'first_union_violation':unions[0] if unions else None,'full_canonical_sha256':digest}


def main():
    inp=json.loads((HERE/'inputs.json').read_text())
    rows={p['row']:p for p in inp['rows']}
    witnesses=json.loads((HERE/'JOINT_WITNESSES.json').read_text())['witnesses']
    results=[];mutations=0;diagnostics=[]
    for w in witnesses:
        p=rows[w['row']]
        results.append(check(p,w))
        diagnostics.append(coupling_diagnostics(p,w))
        variants=[]
        bad=deepcopy(w); bad['excess'][0]+=1;variants.append(bad)
        bad=deepcopy(w); bad['incoming'][0]+=1;variants.append(bad)
        bad=deepcopy(w); bad['pressure'][0]+=1;variants.append(bad)
        bad=deepcopy(w); bad['arcs'].pop();variants.append(bad)
        bad=deepcopy(w); bad['arcs'].append(bad['arcs'][0]);variants.append(bad)
        bad=deepcopy(w)
        u=next(u for u,labels in enumerate(bad['selected_labels']) if labels)
        bad['selected_labels'][u].pop();variants.append(bad)
        for bad in variants:
            try:
                check(p,bad)
            except (AssertionError,ValueError,IndexError,KeyError,TypeError):
                mutations+=1
            else:
                raise AssertionError('corrupt witness accepted')
    return {'schema':'joint-relaxation-integer-witness-check-v1','results':results,
            'corruption_tests_rejected':mutations,'coupling_diagnostics':diagnostics,
            'scope':'Existence in precisely the documented necessary relaxation, NOT graph realization or unrestricted proof.'}

if __name__=='__main__':
    print(json.dumps(main(),sort_keys=True,indent=2))
