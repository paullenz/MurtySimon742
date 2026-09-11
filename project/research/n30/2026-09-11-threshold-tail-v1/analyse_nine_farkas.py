#!/usr/bin/env python3
"""Rebuild and structurally classify the nine historical N30 m=226 Farkas rays.

This is theorem-discovery tooling, not a new proof.  It imports the fresh
(a,b)=(13,16) grouped model that already underlies the preserved exact replay,
regenerates an exact ray for each of the nine threshold-tail-forced rows, and
reports which *kinds* of constraints carry the ray.  Variable-bound repair
rows are reported separately so they cannot masquerade as structural insight.
"""
from __future__ import annotations
import json, sys
from collections import Counter, defaultdict
from pathlib import Path

HERE=Path(__file__).resolve().parent
MODEL_DIR=HERE.parent/'2026-09-08-minimal-kernel-recon-v1'
sys.path.insert(0,str(MODEL_DIR))
from n30_threshold_model import build, exact_certificate, verify_certificate

ROWS=[
    ('2233', [2,2]+[3]*11, [1]*7+[2]+[3]*8),
    ('2331', [2]+[3]*12,   [1]*7+[3]*9),
    ('3^13-r34', [3]*13,   [1]*7+[3]*9),
    ('3^13-r35a',[3]*13,   [1]*7+[3]*8+[4]),
    ('3^13-r35b',[3]*13,   [1]*6+[2]+[3]*9),
    ('3344', [3]*4+[4]*9,  [1]*6+[3]*2+[4]*8),
    ('3344b',[3]*2+[4]*11, [1]*5+[2]+[3]+[4]*9),
    ('3444',[3]+[4]*12,    [1]*5+[2]+[4]*10),
    ('4^13',[4]*13,        [1]*5+[3]+[4]*10),
]


def vtypes(m,row):
    return {m.names[j][0] if isinstance(m.names[j],tuple) else str(m.names[j]) for j in row}


def ub_kind(m,i):
    if i>=m.bound_start:return 'variable_bound'
    row,rhs=m.ub[i]; ts=vtypes(m,row)
    if ts<= {'T','Y'} and rhs==0:return 'T_monotonic_or_forced_cap'
    if ts=={'P'} and rhs==1:return 'source_pair_capacity'
    if ts<= {'W','Z'} and 'W' in ts:return 'source_label_capacity'
    if ts<= {'T','Z'} and 'T' in ts:return 'nested_endpoint_load'
    return 'ub_other_'+','.join(sorted(ts))


def eq_kind(m,i):
    row,rhs=m.eq[i]; ts=vtypes(m,row)
    if ts=={'Y'}:
        return 'label_normalization' if rhs==1 else 'label_degree_or_residual_total'
    if ts<= {'T','Y'}:return 'forced_demand_tail'
    if ts=={'W'}:return 'source_normalization'
    if ts<= {'W','P'} and 'P' in ts:return 'source_supplement_flow'
    if ts<= {'W','Z'} and 'Z' in ts:return 'source_selected_degree'
    if ts<= {'T','Z'} and 'Z' in ts:return 'label_selected_degree_tail_identity'
    return 'eq_other_'+','.join(sorted(ts))


def expression(m, kind, i, iseq=False, maxterms=8):
    row,rhs=(m.eq if iseq else m.ub)[i]
    parts=[]
    for j,c in sorted(row.items(),key=lambda z:(str(m.names[z[0]]),z[1]))[:maxterms]:
        parts.append(f'{c:+g}*{m.names[j]}')
    if len(row)>maxterms:parts.append(f'...({len(row)-maxterms} more)')
    op='=' if iseq else '<='
    return f"{' '.join(parts)} {op} {rhs}"


def main():
    out={'schema':'n30-m226-nine-farkas-structure-v1','rows':[]}
    all_ub=Counter(); all_eq=Counter()
    structural_sets=[]
    for tag,s,rho in ROWS:
        m=build(s,rho,2)
        sol=m.solve()
        assert sol.status==2,(tag,sol.status)
        c=exact_certificate(m); assert c is not None,tag
        verify_certificate(m,c)
        u=Counter();e=Counter();struct=[]
        uw=defaultdict(int);ew=defaultdict(int)
        for i,w in c['ub']:
            k=ub_kind(m,i);u[k]+=1;uw[k]+=w
            if k!='variable_bound':struct.append(('ub',k,i,w))
        for i,w in c['eq']:
            k=eq_kind(m,i);e[k]+=1;ew[k]+=abs(w)
            struct.append(('eq',k,i,w))
        all_ub.update(u);all_eq.update(e)
        structural_sets.append({(x[0],x[1]) for x in struct})
        # Highest-weight non-bound structural rows, useful for reverse-engineering.
        top=[]
        for typ,k,i,w in sorted(struct,key=lambda x:-abs(x[3]))[:30]:
            top.append({'type':typ,'kind':k,'index':i,'weight':w,
                        'expr':expression(m,k,i,typ=='eq')})
        out['rows'].append({
            'tag':tag,'s':s,'rho':rho,'r':sum(rho),'rhs':c['rhs'],
            'variables':len(m.names),'ub_rows':len(m.ub),'eq_rows':len(m.eq),
            'ub_support_counts':dict(u),'ub_weight_sums':dict(uw),
            'eq_support_counts':dict(e),'eq_abs_weight_sums':dict(ew),
            'nonbound_top':top,
        })
    out['aggregate_support_occurrences']={'ub':dict(all_ub),'eq':dict(all_eq)}
    common=set.intersection(*structural_sets)
    out['structural_categories_present_in_every_certificate']=[list(x) for x in sorted(common)]
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':main()
